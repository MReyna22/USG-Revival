# OpenWrt installation on the stock USB

## Hardware and release

The USG-3P boots its operating system from an internal USB drive. I removed that drive and passed it through to a Kali GNU/Linux Rolling 2026.3 virtual machine running in VMware. See the [OpenWrt USG device page](https://openwrt.org/toh/ubiquiti/unifi_security_gateway_3p) for device-specific boot and installation details.

In this session, `/dev/sda` was the 70 GB VM system disk and `/dev/sdb` was the 3.7 GiB UDinfo UF2 4GB USB. These names were verified for this machine and session; they are not portable identifiers.

| Release field | Value used |
|---|---|
| OpenWrt release | 25.12.5 |
| Target | `octeon/generic` |
| Device profile | `ubnt_unifi-usg` |
| Archive | `openwrt-25.12.5-octeon-generic-ubnt_unifi-usg-squashfs-sysupgrade.tar` |
| Archive SHA-256 | `22a7fe40330126ce772de8c89062844197681276fc0ba452bc3ba3e6f607c7df` |

The archive was downloaded from the [official release directory](https://downloads.openwrt.org/releases/25.12.5/targets/octeon/generic/) and checked against the pinned value from [official SHA-256 sums](https://downloads.openwrt.org/releases/25.12.5/targets/octeon/generic/sha256sums). E038 shows the successful check and the `CONTROL`, `kernel`, and `root` members under `sysupgrade-ubnt,usg/`.

## Why I reused the stock drive

I did not have a spare USB available. After preserving and re-verifying the full original image, I chose to overwrite the existing drive and accepted the possibility that the attempt could fail. This was a conscious project decision. It did not establish that the old drive was fault-free, and the backup could not recover from physical failure.

## Why the partitions were retained

The first installation kept the existing layout:

- **Partition 1:** retained FAT32; replaced `vmlinux.64` with the OpenWrt kernel and generated its matching MD5 file.
- **Partition 2:** wrote the archive's raw SquashFS root image at the beginning of the partition, replacing the original filesystem there.
- **Partition 3:** left untouched; not used by this tested installation.

The sysupgrade archive supplies components rather than a complete disk image. Consolidating the USB into one partition was not required. Keeping the layout limited the changes needed for the first boot. A later resize could use more capacity, but no consolidation or expansion was performed here. The running system reported 1.62 GiB of disk space, and the saved hostname survived a restart.

## Recorded procedure

The [installation script](../scripts/install-stock-usb.sh) is the exact guarded procedure prepared for this session. It is a historical record for the original USB state, not a general flashing tool. It contains destructive writes to the specifically checked USB.

Before any write, the script checked USB transport, model, exact capacity, original partition types, archive SHA-256, ELF kernel magic, SquashFS root magic, and available target size. It unmounted all USB partitions, copied the kernel and checksum to FAT32, compared the kernel bytes, then wrote the root image and compared its written bytes. The Ext3 precondition deliberately prevents rerunning the original-state procedure against the already-installed OpenWrt root partition.

The user executed the script in the VM. [E039](../evidence/assets/06-openwrt-installation/39-openwrt-installation-complete.png) records:

```text
usg-openwrt.tar: OK
KERNEL COPY: OK
3614720 bytes copied
ROOTFS READ-BACK: OK
INSTALL COMPLETE - USB partitions unmounted.
```

No installation script was executed by the repository validation tools.

## First boot

With power disconnected, I reinstalled the USB and closed the USG. LAN1 was connected to PC-001 using Cat 6; PC-001 Wi-Fi was disabled. After about five minutes, LuCI appeared at `192.168.1.1`. I set a new administrator password, changed the hostname, and used a normal reboot to test persistence.

The authenticated Status Overview confirmed OpenWrt 25.12.5 and kernel 6.12.94. The [validation record](04-validation.md) covers the subsequent LAN/WAN and client tests.
