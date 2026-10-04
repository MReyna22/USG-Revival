# Filesystem Analysis

[Full evidence index](../../README.md)

- **E024** — [24-ftk-evidence-tree.png](24-ftk-evidence-tree.png): The evidence tree shows one FAT32 and two Ext3 partitions. The same image appears twice in the tree.
- **E025** — [25-partition-2-root-file-list.png](25-partition-2-root-file-list.png): Partition 2 root contains paired version and squashfs files, checksum files, and working directories.
- **E026** — [26-partition-3-root-file-list.png](26-partition-3-root-file-list.png): Partition 3 root lists only lost+found; this does not establish the absence of deleted or unallocated data.
- **E027** — [27-version-o-preview.png](27-version-o-preview.png): The version.o preview contains v4.4.56.5449062.211020.0831, identifying the older version label.
- **E028** — [28-version-preview.png](28-version-preview.png): The version preview contains v4.4.57.5578372.230112.0823, identifying the newer version label.
- **E029** — [29-squashfs-img-md5-preview.png](29-squashfs-img-md5-preview.png): The squashfs.img.md5 preview supplies the declared checksum for squashfs.img; independent verification is recorded separately.
- **E030** — [30-squashfs-o-md5-preview.png](30-squashfs-o-md5-preview.png): The squashfs.o.md5 preview supplies the declared checksum for squashfs.o; independent verification is recorded separately.
- **E031** — [31-exported-firmware-hash-results.png](31-exported-firmware-hash-results.png): Both exported firmware files match their declared MD5 values; independent SHA-256 hashes are recorded and personal prompts are redacted.
- **E032** — [32-ugw-blank-file-list.png](32-ugw-blank-file-list.png): FTK lists zero entries in ugw with no visible error; the expanded w.o directory shows other subdirectories.
- **E033** — [33-w-config-file-list.png](33-w-config-file-list.png): The w/config listing contains config.boot, DHCP lease files and UniFi-related files; their contents have not been published.
- **E034** — [34-partition-1-root-file-list.png](34-partition-1-root-file-list.png): Partition 1 root lists paired vmlinux files and MD5 files, plus vmlinux.tmp.m marked with a red X; its significance remains unverified.
- **E035** — [35-vmlinux-64-md5-preview.png](35-vmlinux-64-md5-preview.png): The vmlinux.64.md5 preview supplies the declared checksum for vmlinux.64; the exported file independently matches this value.
- **E036** — [36-vmlinux-64o-md5-preview.png](36-vmlinux-64o-md5-preview.png): The vmlinux.64o.md5 preview supplies the declared checksum for vmlinux.64o; the exported file independently matches this value.
