# Original USB preservation

Before changing the boot media, I acquired the complete UDinfo UF2 4GB USB with FTK Imager 8.3.0.27. The original USB had no readable exterior model label; Windows supplied the device identification.

| Property | Recorded value |
|---|---|
| Capacity | 4,009,754,624 bytes |
| Partition scheme | MBR |
| Partitions | Three |
| Sector size | 512 bytes |
| Sector count | 7,831,552 |
| Image filename | `USG_OEM_USB_original_2026-10-03.001` |
| Acquisition type | Complete physical drive, raw image |

FTK reported matching MD5 and SHA-1 verification results with no bad blocks reported during imaging. Before the stock-drive installation, the preserved image was hashed again: MD5 and SHA-1 matched the original acquisition report, and SHA-256 was independently recomputed.

| Algorithm | Verified full-image digest |
|---|---|
| MD5 | `DD75A3D92282660F4108649A007AFD9B` |
| SHA-1 | `BBE6A03F8F7BA0FD8C369D88E6FA1C95531FF028` |
| SHA-256 | `E922CEAA5FD97AA5908C5E173B4F0884E9CFC649486167EF93006C0B5CAD7517` |

An earlier manual SHA-256 transcription contained one extra zero. Recomputing the digest from the preserved file corrected the record; the acquired image itself was unchanged.

Windows had mounted the USB before imaging, and no hardware write blocker was documented. This is a recovery and learning project; I do not claim a forensically pristine acquisition or a formal chain of custody. The backup preserves the acquired state, including whatever earlier mounting may have changed.

The raw image and acquisition report remain private. They may contain prior configuration, lease data, and device identifiers. The public repo contains reviewed screenshots and verification values, not the disk image.

## Evidence

- [E012–E014](../evidence/README.md): Windows physical-disk and partition inspection.
- [E015–E022](../evidence/README.md): Acquisition setup and verification records.
- [Preservation values](../evidence/results/original-usb-preservation.json): Sanitized structured record.

## Recovery limit

The image provides a way to restore USB contents if the drive remains writable. It does not repair a physically failed drive or unrelated bootloader/hardware damage. A full restoration was not tested in this project.
