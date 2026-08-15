# IW-013 NAV current-authority reconciliation

Date: `2026-08-13`.

This docs-only receipt records the installed-map authority used by the current NAV package. The compact release anchor is state `792` País Vasco; states `172` Navarra and `806` French Basque remain optional extension objectives. The reservation-group identifier remains `RG-172` because that identifier is part of the accepted registry and loader contract; it does not make state `172` the runtime compact anchor.

Current runtime sources are `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt`, `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt`, and the NAV package setup/final/cleanup adapters. Current player-facing package documentation is `docs/events/006_independence_wave/iberian_registered_packages.md`, `docs/events/006_independence_wave/country_api.md`, and the current package-admission sections of `docs/events/006_independence_wave/overview.md`, `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`.

Dated audits that call state `172` the compact anchor remain historical evidence and are not runtime authority. No runtime binding, reservation group, FORM-07 anchor, or country history was changed by this reconciliation. The NAV project-ready lifecycle fix is separately recorded in `006_iw013_nav_project_lifecycle_patch_2026_08_13.md`.

Validation: targeted `rg` review found current package docs consistently describe `792` as the compact anchor and `172/806` as optional extensions; remaining state-172 compact-anchor claims are inside explicitly dated historical handoffs. Static allocator, scenario, flag, GUI-matrix, and protected-tag audits remain the current shared receipts. No MCP runtime or live-game claim follows from this docs-only receipt.
