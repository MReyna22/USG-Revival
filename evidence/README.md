# Evidence index

All 46 publication images have been reviewed and individually captioned. Black rectangles are permanent privacy redactions; context banners and amber outlines are documented additions. Private originals remain separate.

Evidence numbers preserve the source collection order. E007 was unavailable and is not represented as recovered.

[Image manifest](image-manifest.json) · [Local browser gallery](evidence-gallery.html) · [Final validation summary](results/validation-summary.json)

The gallery is a local HTML file: clone/download the repository and open it in a browser. GitHub displays HTML source instead of rendering this gallery. Earlier result snapshots reflect their capture point; use the final validation summary for the completed scope.

## Teardown and internal boot media

### [E001 — motherboard overview](assets/01-teardown/01-motherboard-overview.png)

The opened USG shows the motherboard, internal USB boot media, heatsink and surrounding components. Device labels are redacted.

### [E002 — internal usb closeup](assets/01-teardown/02-internal-usb-closeup.png)

A closer view shows the boot drive partly withdrawn from the internal USB-A port; board identifiers are redacted.

### [E003 — empty usb port](assets/01-teardown/03-empty-usb-port.png)

The internal USB-A port is empty after boot media removal; board identifiers are redacted.

### [E004 — removed usb seam](assets/01-teardown/04-removed-usb-seam.png)

The removed USB boot drive is shown from the metal casing seam side, with no external model label visible.

### [E005 — removed usb flat face](assets/01-teardown/05-removed-usb-flat-face.png)

The flat face of the removed USB boot drive shows its unmarked metal casing.

### [E006 — removed usb edge](assets/01-teardown/06-removed-usb-edge.png)

An edge view documents the compact physical profile of the removed USB boot drive.


## Windows storage inspection

### [E008 — 194950](assets/02-storage-inspection/08-194950.png)

Windows reports FAT32, volume capacity and space usage for the boot volume; this is not the capacity of the entire USB.

### [E009 — 195008](assets/02-storage-inspection/09-195008.png)

Windows File Explorer shows the paired vmlinux boot files and their MD5 files; the personal account label is redacted.

### [E010 — 195450](assets/02-storage-inspection/10-195450.png)

Windows identifies the attached boot media as a UDinfo UF2 4GB USB device.

### [E011 — 200053](assets/02-storage-inspection/11-200053.png)

A second Explorer view records boot filenames, sizes and modification dates; the unrelated sidebar is redacted.

### [E012 — 203556](assets/02-storage-inspection/12-203556.png)

Get-Disk reports the USB as healthy, online and MBR-partitioned; both drive serial numbers are redacted.

### [E013 — 203931](assets/02-storage-inspection/13-203931.png)

Get-Partition lists three USB partitions, including the FAT32 boot partition; the unique device path is redacted.

### [E014 — 204307](assets/02-storage-inspection/14-204307.png)

Detailed disk properties record capacity, sector size and partition count; unique identifiers and hostname are redacted.


## Original USB preservation

### [E015 — ftk preservation 1](assets/03-firmware-preservation/15-ftk-preservation-1.png)

PowerShell records the SHA-256 of the complete acquired USB image; personal filesystem paths are redacted.

### [E016 — ftk preservation 2](assets/03-firmware-preservation/16-ftk-preservation-2.png)

FTK reports matching MD5 and SHA-1 verification results and no bad blocks for the acquired image.

### [E017 — ftk preservation 3](assets/03-firmware-preservation/17-ftk-preservation-3.png)

The FTK acquisition summary records image size, timestamps and matching verification results; the personal path is redacted.

### [E018 — ftk preservation 4](assets/03-firmware-preservation/18-ftk-preservation-4.png)

The FTK source properties record USB geometry and capacity; the serial number and personal path are redacted.

### [E019 — ftk preservation 5](assets/03-firmware-preservation/19-ftk-preservation-5.png)

The acquisition report records FTK version and case identifiers; examiner name and computer hostname are redacted.

### [E020 — ftk preservation 6](assets/03-firmware-preservation/20-ftk-preservation-6.png)

The destination dialog records the image filename and acquisition options; the personal destination path is redacted.

### [E021 — ftk preservation 7](assets/03-firmware-preservation/21-ftk-preservation-7.png)

The source selection dialog shows the UDinfo USB selected as the physical drive to acquire.

### [E022 — ftk preservation 8](assets/03-firmware-preservation/22-ftk-preservation-8.png)

FTK is configured to acquire a physical drive rather than only the mounted FAT32 volume.

### [E023 — ftk preservation 9](assets/03-firmware-preservation/23-ftk-preservation-9.png)

The installer confirms FTK Imager installation completed; unrelated background terminal information is redacted.


## OEM filesystem analysis

### [E024 — ftk evidence tree](assets/04-filesystem-analysis/24-ftk-evidence-tree.png)

The evidence tree shows one FAT32 and two Ext3 partitions. The same image appears twice in the tree.

### [E025 — partition 2 root file list](assets/04-filesystem-analysis/25-partition-2-root-file-list.png)

Partition 2 root contains paired version and squashfs files, checksum files, and working directories.

### [E026 — partition 3 root file list](assets/04-filesystem-analysis/26-partition-3-root-file-list.png)

Partition 3 root lists only lost+found; this does not establish the absence of deleted or unallocated data.

### [E027 — version o preview](assets/04-filesystem-analysis/27-version-o-preview.png)

The version.o preview contains v4.4.56.5449062.211020.0831, identifying the older version label.

### [E028 — version preview](assets/04-filesystem-analysis/28-version-preview.png)

The version preview contains v4.4.57.5578372.230112.0823, identifying the newer version label.

### [E029 — squashfs img md5 preview](assets/04-filesystem-analysis/29-squashfs-img-md5-preview.png)

The squashfs.img.md5 preview supplies the declared checksum for squashfs.img; independent verification is recorded separately.

### [E030 — squashfs o md5 preview](assets/04-filesystem-analysis/30-squashfs-o-md5-preview.png)

The squashfs.o.md5 preview supplies the declared checksum for squashfs.o; independent verification is recorded separately.

### [E031 — exported firmware hash results](assets/04-filesystem-analysis/31-exported-firmware-hash-results.png)

Both exported firmware files match their declared MD5 values; independent SHA-256 hashes are recorded and personal prompts are redacted.

### [E032 — ugw blank file list](assets/04-filesystem-analysis/32-ugw-blank-file-list.png)

FTK lists zero entries in ugw with no visible error; the expanded w.o directory shows other subdirectories.

### [E033 — w config file list](assets/04-filesystem-analysis/33-w-config-file-list.png)

The w/config listing contains config.boot, DHCP lease files and UniFi-related files; their contents have not been published.

### [E034 — partition 1 root file list](assets/04-filesystem-analysis/34-partition-1-root-file-list.png)

Partition 1 root lists paired vmlinux files and MD5 files, plus vmlinux.tmp.m marked with a red X; its significance remains unverified.

### [E035 — vmlinux 64 md5 preview](assets/04-filesystem-analysis/35-vmlinux-64-md5-preview.png)

The vmlinux.64.md5 preview supplies the declared checksum for vmlinux.64; the exported file independently matches this value.

### [E036 — vmlinux 64o md5 preview](assets/04-filesystem-analysis/36-vmlinux-64o-md5-preview.png)

The vmlinux.64o.md5 preview supplies the declared checksum for vmlinux.64o; the exported file independently matches this value.


## Linux identification and firmware preparation

### [E037 — linux vm usb identification](assets/05-openwrt-preparation/37-linux-vm-usb-identification.png)

Kali 2026.3 in VMware identifies the 3.7 GiB UDinfo USB as /dev/sdb with three mounted partitions and the 70 GiB VM system disk as /dev/sda. Personal mount paths and prompt labels are redacted. Device names must be checked again after reconnecting.

### [E038 — openwrt download checksum and contents](assets/05-openwrt-preparation/38-openwrt-download-checksum-and-contents.png)

The USG-specific OpenWrt 25.12.5 download passes the pinned SHA-256 check. Its archive lists CONTROL, kernel and root under sysupgrade-ubnt,usg; installation and boot are not established by this screenshot.


## Stock-drive installation

### [E039 — openwrt installation complete](assets/06-openwrt-installation/39-openwrt-installation-complete.png)

The installation output reports archive verification, successful kernel comparison and root filesystem read-back comparison, 3,614,720 root bytes written, and unmounted USB partitions. USG boot success has not yet been tested.


## First boot and resource reporting

### [E040 — openwrt luci first boot login](assets/07-first-boot/40-openwrt-luci-first-boot-login.png)

The OpenWrt LuCI login page responds at 192.168.1.1 after the first USG boot. The user reports PC-001 connected directly to LAN1 with Cat 6 and Wi-Fi disabled after a five-minute wait. Running firmware version and authenticated access remain unverified at this stage.

### [E041 — openwrt status system overview](assets/07-first-boot/41-openwrt-status-system-overview.png)

Authenticated LuCI Status Overview identifies the Ubiquiti UniFi Security Gateway running OpenWrt 25.12.5 r33051-f5dae5ece4 on octeon/generic with kernel 6.12.94. Uptime is 1h 6m 4s and load averages are 0.01, 0.02, 0.00. The displayed June 29, 2026 UTC time is inconsistent with the October 4 capture date; clock synchronization is unverified. Password setup, writable storage and reboot persistence remain unverified.

### [E042 — openwrt memory storage and port status](assets/07-first-boot/42-openwrt-memory-storage-and-port-status.webp)

LuCI Status Overview reports 334.19 MiB available of 399.58 MiB memory (83%), disk usage of 87.76 MiB out of 1.62 GiB (5%), and eth1 linked at 1 GbE while eth0 and eth2 have no link. Uptime is 1h 22m 3s and local time now displays October 4, 2026, 3:13:14 AM CDT. The browser-tab email identifier is redacted. Storage capacity is visible; persistent configuration writes and reboot retention are not yet tested, and the time synchronization method is unknown.


## Configuration persistence

### [E043 — openwrt hostname after reboot](assets/08-reboot-validation/43-openwrt-hostname-after-reboot.webp)

Following the requested reboot test, authenticated LuCI Overview shows hostname USG-Revival with uptime 0h 1m 6s, compared with 1h 22m 3s in the prior resource photograph. The hostname is retained across the restart; OpenWrt 25.12.5 and kernel 6.12.94 remain running. Memory available is 337.59 MiB of 399.58 MiB and disk usage is 87.76 MiB of 1.62 GiB. The user reports changing the administrator password; explicit fresh login using that password is not separately documented. Personal browser-tab email details are redacted.


## WAN and client Internet validation

### [E044 — upstream wifi ipv4 subnet check](assets/09-wan-validation/44-upstream-wifi-ipv4-subnet-check.png)

The laptop Wi-Fi adapter lists an upstream private IPv4 address, a 255.255.255.0 subnet mask and a default gateway. The observed upstream /24 does not overlap with the USG default 192.168.1.0/24 LAN, so no USG LAN renumbering is required for the planned downstream router test. Home IPv4 and gateway values are redacted; WAN connectivity is not yet tested.

### [E045 — openwrt wan dhcp lease](assets/09-wan-validation/45-openwrt-wan-dhcp-lease.png)

LuCI Network > Interfaces shows LAN br-lan at the default 192.168.1.1/24 with carrier present and WAN eth0 as a DHCP client with carrier present and an upstream private IPv4 /24 lease. WAN uptime is 0h 2m 13s with receive and transmit traffic. WAN6 shows a DHCPv6 client and a ULA IPv6 address, which does not establish public IPv6 Internet connectivity. MAC addresses, unique IPv6 identifiers and the home WAN IPv4 value are redacted. Client Internet routing and DNS tests remain pending.

### [E046 — pc001 internet ping and dns](assets/09-wan-validation/46-pc001-internet-ping-and-dns.png)

PC-001 PowerShell shows ping -n 4 1.1.1.1 with four replies, zero lost packets and round-trip minimum/maximum/average of 13/22/15 ms. nslookup example.com identifies USG-Revival.lan as the responding DNS server and returns A and AAAA records. Account paths and the unique local IPv6 DNS-server address are redacted; public test targets and observed DNS answers are retained. This documents IPv4 reachability and DNS resolution in the reported Ethernet-only test topology; HTTPS browsing and public IPv6 reachability are not yet tested.


## Firewall-zone review

### [E047 — openwrt firewall zone settings](assets/10-firewall-review/47-openwrt-firewall-zone-settings.png)

LuCI Firewall > General Settings shows global input/forward reject and output accept; SYN-flood protection enabled; drop-invalid unchecked; flow offloading None. LAN input/output/intra-zone forwarding are accept and LAN forwards to WAN. WAN input is reject, output accept, intra-zone forwarding drop, with IPv4 masquerading enabled. No sensitive details were identified. This is a zone-configuration review, not a traffic-rule/port-forward audit or an inbound enforcement test.

