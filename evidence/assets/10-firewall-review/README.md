# Firewall Review

[Full evidence index](../../README.md)

- **E047** — [47-openwrt-firewall-zone-settings.png](47-openwrt-firewall-zone-settings.png): LuCI Firewall > General Settings shows global input/forward reject and output accept; SYN-flood protection enabled; drop-invalid unchecked; flow offloading None. LAN input/output/intra-zone forwarding are accept and LAN forwards to WAN. WAN input is reject, output accept, intra-zone forwarding drop, with IPv4 masquerading enabled. No sensitive details were identified. This is a zone-configuration review, not a traffic-rule/port-forward audit or an inbound enforcement test.
