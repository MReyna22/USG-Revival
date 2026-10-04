"""Check the public evidence set without executing device installation commands."""
import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT/'evidence'
manifest = json.loads((EVIDENCE/'image-manifest.json').read_text(encoding='utf-8'))
assert len(manifest) == 46, 'Expected 46 reviewed publication images'
assert len({e['source_order'] for e in manifest}) == len(manifest), 'Duplicate evidence IDs'
listed = set()
for entry in manifest:
    path = (EVIDENCE/entry['file']).resolve()
    assert path.is_relative_to(EVIDENCE.resolve()), 'Image path outside evidence folder'
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == entry['sha256'], f'Hash mismatch: {path.name}'
    if path.suffix == '.webp':
        assert data[:4] == b'RIFF' and data[8:12] == b'WEBP'
        assert struct.unpack('<I', data[4:8])[0] + 8 == len(data)
        offset, chunks = 12, []
        while offset < len(data):
            kind = data[offset:offset+4]
            length = struct.unpack('<I', data[offset+4:offset+8])[0]
            assert offset+8+length <= len(data)
            chunks.append(kind)
            if kind == b'VP8L':
                assert data[offset+8] == 0x2f
                bits = struct.unpack('<I', data[offset+9:offset+13])[0]
                assert ((bits & 0x3fff)+1, ((bits >> 14) & 0x3fff)+1) == (entry['width'],entry['height'])
            offset += 8+length+(length & 1)
        assert offset == len(data) and chunks == [b'VP8L'], 'Expected metadata-free lossless WebP'
        listed.add(path)
        continue
    assert data[:8] == b'\x89PNG\r\n\x1a\n', f'Not PNG: {path.name}'
    offset, chunks = 8, []
    while offset < len(data):
        length = struct.unpack('>I',data[offset:offset+4])[0]
        kind = data[offset+4:offset+8]
        assert offset+12+length <= len(data), f'Truncated PNG: {path.name}'
        chunks.append(kind)
        if kind == b'IHDR':
            assert struct.unpack('>II',data[offset+8:offset+16]) == (entry['width'],entry['height'])
        offset += length+12
        if kind == b'IEND': break
    assert offset == len(data), f'Extra bytes after PNG: {path.name}'
    assert chunks[0] == b'IHDR' and chunks[-1] == b'IEND'
    assert set(chunks) <= {b'IHDR',b'IDAT',b'IEND'}, f'Unexpected metadata chunks: {path.name}'
    listed.add(path)
assert listed == {p.resolve() for p in (EVIDENCE/'assets').rglob('*') if p.suffix in {'.png','.webp'}}, 'Unlisted/missing image'

excluded = {'.001','.dd','.raw','.img','.bin','.tar','.tgz','.zip','.pem','.key'}
for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.relative_to(ROOT).parts: continue
    assert path.suffix.lower() not in excluded, f'Excluded artifact: {path.relative_to(ROOT)}'
    assert not path.name.endswith('.tar.gz'), f'Configuration archive: {path.name}'
    assert not any(part in {'private','private-originals'} for part in path.relative_to(ROOT).parts)

references = 0
for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    targets = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text)
    targets += re.findall(r'<img[^>]+src="([^"]+)"',text)
    for target in targets:
        if target.startswith(('https://','http://','#','mailto:')): continue
        target = unquote(target.split('#',1)[0])
        resolved = (path.parent/target).resolve()
        assert resolved.is_relative_to(ROOT), f'Link outside repo: {path.name}'
        assert resolved.exists(), f'Broken local reference in {path.name}: {target}'
        references += 1
print(f'PASS: {len(manifest)} image hashes, metadata/dimensions, excluded artifacts and {references} local references.')
