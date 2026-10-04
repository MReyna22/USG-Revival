# Decisions and lessons

## Check the device-specific options

The early discussion was too quick to dismiss replacement firmware for the USG. Finding OpenWrt's device-specific installation page changed the direction of the project. I learned to check the exact device and boot method before treating a first assumption as the final answer.

OpenWrt became the selected path. The earlier pfSense/OPNsense idea was dropped, and the mini PCs stayed available for other lab roles. This repo records the OpenWrt implementation that was actually completed.

## Preserve the starting point

The full USB image gave me a record of the acquired state before installing a different OS. Checking the backup again before the write also caught a manually mistyped SHA-256. The useful lesson was to verify the file itself when a recorded value looks wrong, rather than silently carrying the typo into later documentation.

## Distinguish a volume from a physical drive

Windows showed a small FAT32 volume even though the USB was about 4 GB. Physical-disk and partition inspection explained where the rest of the capacity was. FTK then identified the Ext3 filesystems that Windows had labeled unknown.

## Make the stock-drive decision explicit

I did not have a spare USB. I chose to proceed with the stock drive after preserving the original contents and understanding the limits of that backup. The successful outcome does not erase the risk I accepted or prove the drive will remain reliable indefinitely.

## Change enough for the first boot

I asked why the drive was not consolidated and formatted as one larger boot disk. The installation used the separate FAT32 kernel partition and raw root image on partition 2. A successful first boot and saved-setting test were more useful milestones than adding a resize before knowing the installation worked.

## Verify one layer at a time

The installation's read-back checks did not prove the USG would boot. The login page did not prove the running release. A WAN lease did not prove PC-001 could reach the Internet. Each later test answered the next question: release, storage, persistence, WAN addressing, ping, DNS, browsing, and zone configuration.

## Keep claims tied to the evidence

Some results have screenshots; password login, backup generation, and the web page load have direct operator reports. I kept those evidence types distinct. I also left untested areas visible, including inbound enforcement, public IPv6, throughput, long-term reliability, and later home-network deployment.

## Keep the evidence usable

Technical screenshots need their context. Captions and added labels identify which partition, directory, or test the image belongs to. Permanent redaction removes account paths, email identifiers, MAC addresses, private network identifiers, and other sensitive details while preserving the technical observations.

This project gave me a concrete example of turning donated equipment into a working lab appliance and documenting the process well enough for someone else to follow the decisions.
