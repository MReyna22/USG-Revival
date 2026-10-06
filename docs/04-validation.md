# Validation record

The goal was to demonstrate that the repurposed USG boots, retains a tested setting, provides local administration, and supports basic client Internet access. Physical work and device-side commands were performed by the project owner. Screenshots and direct operator reports are identified separately below.

## Functional checks

| Test | Method | Result | Basis |
|---|---|---|---|
| USB write verification | Compare copied kernel and written root bytes | Both comparisons passed; root write 3,614,720 bytes | E039 screenshot |
| First boot / local management | PC-001 → LAN1, Wi-Fi off; open `192.168.1.1` | LuCI login page appeared | E040 screenshot and operator connection report |
| Running release | Authenticated Status Overview | Ubiquiti USG; `octeon/generic`; OpenWrt 25.12.5; kernel 6.12.94 | E041 screenshot |
| Memory / storage | Status Overview | 334.19 MiB available of 399.58 MiB; disk usage 87.76 MiB of 1.62 GiB | E042 screenshot at that point in time |
| Ethernet | Port status | eth1 linked at 1 GbE | E042 screenshot |
| Saved hostname | Save `USG-Revival`, reboot, inspect Overview | Hostname retained; uptime reset to 0h 1m 6s | E043 screenshot and requested test sequence |
| Changed administrator password | Log out, log in using the updated password after reboot | Successful | Direct operator report; password never collected |
| Configuration backup | Generate archive in LuCI | Generated and kept private/outside the public repo | Direct operator report; file and restore not inspected/tested |
| Subnet separation | Compare laptop upstream IPv4/mask with USG LAN | Two non-overlapping private `/24` networks | E044 screenshot; home values redacted |
| WAN DHCP | Existing router LAN → USG WAN1; inspect Interfaces | DHCP client on eth0, carrier present, upstream private IPv4 lease | E045 screenshot |
| Client IPv4 Internet reachability | `ping -n 4 1.1.1.1` on PC-001 | Sent 4, received 4, lost 0; min/avg/max 13/15/22 ms | E046 screenshot |
| Client DNS | `nslookup example.com` | Response from `USG-Revival.lan`; A and AAAA records returned | E046 screenshot |
| Client web access | Open `example.com` in Edge on PC-001 | Page loaded without issues | Direct operator report; requested URL was HTTPS, actual scheme/TLS details not captured |

The client tests used the previously reported Ethernet-only topology with PC-001 Wi-Fi disabled. The terminal photograph itself does not independently display adapter state. Four pings are a small connectivity sample, not a benchmark or long-term stability test.

## Subsequent PC-001 client verification — October 5, 2026

The [PC-001 device record](https://github.com/MReyna22/slb-corona-donated-gear/blob/main/docs/devices/PC-001.md) contains a later Ethernet-only check with Wi-Fi shown disconnected, a 1 Gbps Ethernet link, four ping replies with no loss, and successful DNS resolution. The operator reported Ethernet connected through the USG for that check. This adds explicit client adapter-state evidence to the earlier routing tests; the original observations above remain unchanged.

A separate Wi-Fi-only check, with Ethernet shown disconnected, is documented in the same device record. It verifies PC-001's wireless connectivity and is not evidence of routing through the USG. Link rates are not throughput measurements, and these checks do not establish extended stability or inbound firewall enforcement.

## Firewall-zone configuration review

[E047](../evidence/assets/10-firewall-review/47-openwrt-firewall-zone-settings.png) shows the following policies. They agree with the [OpenWrt firewall4 default zone configuration](https://lxr.openwrt.org/source/firewall4/root/etc/config/firewall).

| Scope | Input | Output | Intra-zone forwarding | Other setting |
|---|---|---|---|---|
| Global defaults | reject | accept | Global forward: reject | SYN-flood protection checked |
| LAN | accept | accept | accept | Explicit LAN → WAN forwarding; masquerading unchecked |
| WAN | reject | accept | drop | IPv4 masquerading checked |

Flow offloading was `None`; drop-invalid was unchecked. I recorded the visible configuration without adding performance tuning or hardening changes to this revival phase.

The WAN input policy is a baseline policy, not a claim that every kind of inbound packet is rejected. Rules can make exceptions. Traffic-rule and port-forward tabs were not audited, and an external inbound enforcement test was not performed.

## Time display

E041 displayed June 29, 2026 in UTC. Later photos displayed October 4 in CDT, with a different time after reboot. The displayed time changed, but its synchronization method and absolute accuracy were not established. The project is dated by the operator's capture/session context rather than relying on the device clock for chronology.

## Scope completed and work left separate

**Completed:** basic appliance revival, local management, tested hostname/password persistence, private backup generation, WAN DHCP, client IPv4/DNS/web access, and visible firewall-zone review.

**Not performed:** public IPv6 reachability, inbound firewall enforcement, traffic-rule/port-forward audit, throughput measurements, extended soak testing, backup restoration, VLAN isolation, VPN, IDS/IPS, and deployment as the household's main gateway. These can be separate follow-up projects; this repo does not claim their results.

Machine-readable snapshots are under [evidence/results](../evidence/results). Earlier snapshots retain what was known at their capture point; [the final validation summary](../evidence/results/validation-summary.json) gives the completed scope.
