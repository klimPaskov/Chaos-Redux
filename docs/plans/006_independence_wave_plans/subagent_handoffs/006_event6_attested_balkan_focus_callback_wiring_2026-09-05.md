# Event 006 attested Balkan focus callback wiring handoff (2026-09-05)

## Scope and disposition

This bounded tranche repairs missing shared-tree call sites for the already-attested IW-024 Banat carrier `AXX` and IW-026 Macedonia carrier `MAC`.

Disposition: **implemented** for focus callback reachability. Central admission, package identity, assets, probability, and live runtime evidence are unchanged.

## Change

`common/national_focus/006_independence_wave_focus.txt` now calls the existing package effects at the matching shared nodes.

- `independence_wave_prepare_capital_administration` calls `independence_wave_axx_focus_publish_banat_charter` and `independence_wave_mac_focus_publish_vardar_charter`.
- `independence_wave_inventory_the_state` calls `independence_wave_axx_focus_settle_community_rights` and `independence_wave_mac_focus_settle_community_rights`.
- `independence_wave_bind_the_first_oath` calls `independence_wave_axx_focus_integrate_mountain_networks` and `independence_wave_mac_focus_integrate_mountain_networks`.
- `independence_wave_define_former_host_policy` calls `independence_wave_axx_focus_settle_romanian_ledgers` and `independence_wave_mac_focus_settle_yugoslav_ledgers`.
- `independence_wave_recognize_fellow_new_states` calls `independence_wave_axx_focus_open_danube_network` and `independence_wave_mac_focus_open_danube_network`.

The callbacks already existed in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt`, retain their package-specific ledger, host, and network effects, and are guarded by the existing `is_independence_wave_axx_package` or `is_independence_wave_mac_package` predicates. No new effect, flag, route, decision, asset, or admission entry was created.

## Validation

- A source crosswalk now finds zero unreferenced `independence_wave_*_focus_*` definitions in `006_independence_wave_balkan_package_effects.txt`; the ten AXX/MAC callbacks are all reachable from the shared tree.
- `hoi4_focus_inspect` returned `FOCUS_INSPECTED` with 184 focuses, 195 connectors, zero crossings, zero node intersections, zero long connectors, and layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07508cbdcbf8e6f8949d6f91855b543a2cc7a4a768457515b4150f75be16d82b/ce1fa7aa65897113b5682260233e175f10bef3b87669882340766f3fddae33f0/focus-inspect.eff12e5cf8c19c9b.json`.
- `hoi4_focus_render` returned `FOCUS_RENDERED` with HTML, SVG, JSON, source-map, and plan artifacts. HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc05e3f89c2b7a36e9e3d3e19ef1002a270328beb49079506a9070d3fbca9bc0/1c04b5b39a028f071f49461662e9d5046c6ccb0b37d4f2505904dbe57c857cf7/independence_wave_focus_tree.focus.html`.
- Strict allocator, flag, country API, scenario matrix, FORM-16, and Statehood Ledger semantic audits passed. The allocator remains at 32 attested packages, 29 compatible reservation groups, 40 adapters, and 161 unattested selectable rows with the exact 3/4/5/7/10 ladder.
- The only focus diagnostic remains the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning, and focus validation reports no blocking diagnostics.

## Boundary and follow-up

This patch does not promote any package or claim live release, state transfer, host survival, save/load, AI balance, or final Event 006 completion. The broader event remains **HOLD / PARTIAL** until the remaining package, asset-rights, probability, audio, GUI reachability, and engine evidence gates are resolved.

No fallback or simplification was introduced.
