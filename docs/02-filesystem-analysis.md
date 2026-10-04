# Filesystem and OEM firmware analysis

I inspected the preserved image in FTK Imager before installing OpenWrt. Windows initially showed only a small FAT32 volume, but the physical drive was about 4 GB and contained three partitions. FTK identified the two Windows-unknown partitions as Ext3.

| Partition | FTK size label | Filesystem | Observed contents |
|---|---|---|---|
| 1 | 142 MB | FAT32 | Paired `vmlinux` files and MD5 files; `System Volume Information`; `vmlinux.tmp.m` marked with a red X |
| 2 | 1669 MB | Ext3 | Version labels, paired SquashFS files, and working/configuration directories |
| 3 | 1812 MB | Ext3 | Root listing showed `lost+found` |

These are the tools' displayed size labels. The Windows volume capacity and partition-size displays used different values/units; they are retained as observations, not treated as the physical USB capacity.

## Paired version labels

| File | Text shown in FTK |
|---|---|
| `version.o` | `v4.4.56.5449062.211020.0831` |
| `version` | `v4.4.57.5578372.230112.0823` |

The `.o` names and older file dates suggest a retained previous firmware set. I did not establish which OEM set had been active at boot, or independently extract version metadata from inside the SquashFS files.

## Exported file verification

I exported four OEM boot/firmware files. Their MD5 values were recomputed and compared with the adjacent checksum files shown in FTK; all four matched. Independent SHA-256 values were also recorded.

| File | Bytes | MD5 match |
|---|---:|---|
| `vmlinux.64` | 5,755,016 | Yes |
| `vmlinux.64o` | 5,755,016 | Yes |
| `squashfs.img` | 103,428,096 | Yes |
| `squashfs.o` | 103,796,736 | Yes |

The complete values are in [kernel hashes](../evidence/results/kernel-file-hashes.json) and [firmware hashes](../evidence/results/firmware-file-hashes.json). Checksum agreement establishes consistency with the declared values; it does not establish publisher authenticity, active boot selection, or successful OEM operation. The exported binaries remain private.

## Directory observations and limits

- `ugw` showed a blank file list with zero entries. This records FTK's visible result; it does not prove the directory was historically empty or explain deleted content.
- `w.o` contained directories including `config`, `etc`, `home`, `opt`, `run`, and `var`.
- `w/config` listed `config.boot`, DHCP lease files, `mgmt`, `unifi`, and `wizard`. I did not publish their contents because they could expose prior configuration or identifiers.
- Partition 3 listed only `lost+found` at its root. Deleted and unallocated contents were not analyzed.
- The red X beside `vmlinux.tmp.m` was recorded without assigning an unverified meaning.

The [captioned evidence index](../evidence/README.md) covers E024–E036. Added banners identify the relevant partition/directory/file; amber outlines mark visible selections where the screenshot permits it. A cropped file list is labeled without inventing a tree selection.
