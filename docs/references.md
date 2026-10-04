# References

References explain the selected procedure and how checks were interpreted. The screenshots and operator reports establish what happened in this project.

| Source | Use in this project |
|---|---|
| [OpenWrt USG-3P device page](https://openwrt.org/toh/ubiquiti/unifi_security_gateway_3p) | Device support, internal USB boot design, port names, and installation guidance |
| [OpenWrt 25.12.5 octeon/generic release directory](https://downloads.openwrt.org/releases/25.12.5/targets/octeon/generic/) | Device-specific archive used in the installation |
| [Official release SHA-256 sums](https://downloads.openwrt.org/releases/25.12.5/targets/octeon/generic/sha256sums) | Pinned archive verification value |
| [OpenWrt initial login walkthrough](https://openwrt.org/docs/guide-quick-start/walkthrough_login) | Initial local LuCI access and setting an administrator password |
| [OpenWrt Internet checks](https://openwrt.org/docs/guide-quick-start/checks_and_troubleshooting) | Existing-router LAN to OpenWrt WAN test setup |
| [OpenWrt Internet troubleshooting](https://openwrt.org/docs/guide-quick-start/troubleshooting_internetconnectivity) | Check for overlapping LAN/WAN address ranges |
| [OpenWrt firewall4 default configuration](https://lxr.openwrt.org/source/firewall4/root/etc/config/firewall) | Comparison of visible LAN/WAN zone policies and masquerading |
| [LuCI backup interface source](https://github.com/openwrt/luci/blob/master/modules/luci-mod-system/htdocs/luci-static/resources/view/system/flash.js) | Generate a configuration archive |
| [Microsoft ping reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ping) | IPv4 ICMP connectivity test and statistics |
| [Microsoft nslookup reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup) | DNS test through the client's configured resolver |
| [Ubiquiti USG quick-start guide](https://dl.ui.com/qsg/USG/USG_EN.html) | Official 12 V DC / 1 A power adapter specification |

The recorded firmware release is the one actually downloaded and observed during this project. This document is not a recommendation to install that release indefinitely or a claim about the latest release at a later date.

## Equipment provenance

[SLB Corona Donated Gear](https://github.com/MReyna22/slb-corona-donated-gear) is the parent equipment inventory and acknowledgment of Antonio Corona's donation. The USG is GW-001 and the wired test client is PC-001.
