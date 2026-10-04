#!/usr/bin/env bash
# USG-3P offline installation, pinned OpenWrt 25.12.5 archive.
# Overwrites stock USB boot files and partition 2; requires the verified backup.
# Device names are specific to the supplied Kali screenshot. Guards recheck them.
set -euo pipefail
cd "$HOME/USG-Revival/OpenWrt-25.12.5"
printf '%s  %s\n' '22a7fe40330126ce772de8c89062844197681276fc0ba452bc3ba3e6f607c7df' 'usg-openwrt.tar' | sha256sum --check -
if [[ "$(lsblk -dn -o TRAN /dev/sdb | xargs)" != usb || "$(lsblk -dn -o MODEL /dev/sdb | xargs)" != 'UDinfo UF2 4GB' ]]; then
    echo 'STOP: /dev/sdb is not the expected UDinfo USB.' >&2
    exit 1
fi
sudo -v
[[ "$(sudo blockdev --getsize64 /dev/sdb)" == 4009754624 ]] || { echo 'STOP: USB size differs from preserved original.' >&2; exit 1; }
[[ "$(sudo blkid -s TYPE -o value /dev/sdb1)" == vfat ]] || { echo 'STOP: partition 1 is not FAT32.' >&2; exit 1; }
[[ "$(sudo blkid -s TYPE -o value /dev/sdb2)" == ext3 ]] || { echo 'STOP: partition 2 differs from original; send output.' >&2; exit 1; }
tar -xf usg-openwrt.tar
usg_kernel='sysupgrade-ubnt,usg/kernel'
usg_root='sysupgrade-ubnt,usg/root'
[[ -s "$usg_kernel" && -s "$usg_root" ]]
[[ "$(od -An -tx1 -N4 "$usg_kernel" | tr -d ' \n')" == 7f454c46 ]] || { echo 'STOP: kernel is not ELF.' >&2; exit 1; }
[[ "$(od -An -tx1 -N4 "$usg_root" | tr -d ' \n')" == 68737173 ]] || { echo 'STOP: root is not SquashFS.' >&2; exit 1; }
usg_root_bytes=$(stat -c %s "$usg_root")
(( usg_root_bytes < $(sudo blockdev --getsize64 /dev/sdb2) ))
for usg_partition in /dev/sdb1 /dev/sdb2 /dev/sdb3; do
    if findmnt -rn -S "$usg_partition" >/dev/null; then sudo umount "$usg_partition"; fi
done
if lsblk -nr -o MOUNTPOINTS /dev/sdb | grep -q '[^[:space:]]'; then
    echo 'STOP: a USB partition is still mounted.' >&2
    exit 1
fi
usg_boot=$(mktemp -d "$PWD/usg-boot.XXXXXX")
trap 'if mountpoint -q "$usg_boot"; then sudo umount "$usg_boot"; fi; rmdir "$usg_boot"' EXIT
sudo mount -t vfat /dev/sdb1 "$usg_boot"
sudo cp "$usg_kernel" "$usg_boot/vmlinux.64"
md5sum "$usg_kernel" | cut -d ' ' -f 1 | sudo tee "$usg_boot/vmlinux.64.md5" >/dev/null
sudo cmp "$usg_kernel" "$usg_boot/vmlinux.64"
echo 'KERNEL COPY: OK'
sync
sudo umount "$usg_boot"
sudo dd if="$usg_root" of=/dev/sdb2 bs=4M conv=fsync status=progress
sudo cmp -n "$usg_root_bytes" "$usg_root" /dev/sdb2
echo 'ROOTFS READ-BACK: OK'
sync
echo 'INSTALL COMPLETE - all USB partitions unmounted. Capture this output before removing the USB.'
