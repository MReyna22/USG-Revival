# Openwrt Preparation

[Full evidence index](../../README.md)

- **E037** — [37-linux-vm-usb-identification.png](37-linux-vm-usb-identification.png): Kali 2026.3 in VMware identifies the 3.7 GiB UDinfo USB as /dev/sdb with three mounted partitions and the 70 GiB VM system disk as /dev/sda. Personal mount paths and prompt labels are redacted. Device names must be checked again after reconnecting.
- **E038** — [38-openwrt-download-checksum-and-contents.png](38-openwrt-download-checksum-and-contents.png): The USG-specific OpenWrt 25.12.5 download passes the pinned SHA-256 check. Its archive lists CONTROL, kernel and root under sysupgrade-ubnt,usg; installation and boot are not established by this screenshot.
