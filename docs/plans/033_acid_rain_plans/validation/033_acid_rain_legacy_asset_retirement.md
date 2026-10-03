# Event 033 prototype presentation retirement

## Disposition and authority

Disposition: implemented, with final MCP evidence still unresolved.
The user requested implementation of the Event 033 package and repair of every Event 033 visual consumer, including stale registrations and orphaned files.
The parent accepted retirement of the prototype definitions after exact consumer searches showed that the current event, decisions, modifiers, achievements, and dedicated GUI use the Event 033 package registrations instead.
This acceptance covers removal of unused definitions only.

## Current implementation

The retirement removes twelve unused sprite registrations and the unbound `acid_rain_decisions_container` prototype window.
The window's only element was `placeholder_acid_rain_map`, which displayed `GFX_acid_rain_1` without a scripted GUI attachment.
The 35 unused DDS files were moved out of `gfx/` into `docs/assets/033_acid_rain/retired_runtime/`, preserving each original `gfx/...` relative path beneath that recovery folder.
Every source file's SHA-256 matched the individually decoded inventory before the move and matched its recovery copy afterward.
The table records each former runtime path, and every listed file is classified as `unused_orphan` with no final runtime consumer.
They are not accepted final artwork, and their unknown source rights do not establish permission to use them in a live consumer.

| Asset | Asset family | Gameplay consumer | Sprite | Source or master | Final runtime path | Expected size | Actual size | Alpha or frame treatment | Visual defects | Wiring defects | Repair performed | Final status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prototype category icon | Decision category icon | None | `GFX_decision_category_acid` | Unavailable | `gfx/interface/decisions/033_acid_rain/decision_category_acid.dds` | Retired consumer | 52x40 | Legacy alpha | No final-family acceptance | Unused registration | Removed registration | `unused_orphan` |
| Prototype response icon | Decision icon | None | `GFX_decision_acid` | Unavailable | `gfx/interface/decisions/033_acid_rain/decision_acid.dds` | Retired consumer | 40x27 | Legacy alpha | No final-family acceptance | Unused registration | Removed registration | `unused_orphan` |
| Prototype Europe map | GUI image | Unbound prototype window | `GFX_acid_rain_1` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_europe.dds` | Retired 256x98 window | 256x98 | Single frame | Static prototype presentation | Window had no attachment | Removed window and registration | `unused_orphan` |
| Prototype Middle East map | GUI image | None | `GFX_acid_rain_2` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_middle_east.dds` | Retired consumer | 256x98 | Single frame | Static prototype presentation | Unused registration | Removed registration | `unused_orphan` |
| Prototype Asia map | GUI image | None | `GFX_acid_rain_3` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_asia.dds` | Retired consumer | 256x98 | Single frame | Static prototype presentation | Unused registration | Removed registration | `unused_orphan` |
| Prototype Africa map | GUI image | None | `GFX_acid_rain_4` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_africa.dds` | Retired consumer | 256x98 | Single frame | Static prototype presentation | Unused registration | Removed registration | `unused_orphan` |
| Prototype Australia map | GUI image | None | `GFX_acid_rain_5` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_australia.dds` | Retired consumer | 256x98 | Single frame | Static prototype presentation | Unused registration | Removed registration | `unused_orphan` |
| Prototype North America map | GUI image | None | `GFX_acid_rain_6` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_north_america.dds` | Retired consumer | 256x98 | Single frame | Static prototype presentation | Unused registration | Removed registration | `unused_orphan` |
| Prototype South America map | GUI image | None | `GFX_acid_rain_7` | Unavailable | `gfx/interface/decisions/033_acid_rain/acid_rain_south_america.dds` | Retired consumer | 256x98 | Single frame | Static prototype presentation | Unused registration | Removed registration | `unused_orphan` |
| Prototype arrival news | News picture | None | `GFX_news_acid_rain` | Unavailable | `gfx/event_pictures/033_acid_rain/news_acid_rain.dds` | News canvas | 397x153 | Opaque grayscale | Source rights unverified | Unused registration | Removed registration | `unused_orphan` |
| Prototype departure news | News picture | None | `GFX_news_acid_rain_end` | Unavailable | `gfx/event_pictures/033_acid_rain/news_acid_rain_end.dds` | News canvas | 397x153 | Opaque grayscale | Source rights unverified | Unused registration | Removed registration | `unused_orphan` |
| Prototype report | Report picture | None | `GFX_report_event_acid_rain` | Unavailable | `gfx/event_pictures/033_acid_rain/report_event_acid_rain.dds` | Report canvas | 210x176 | Tilted card alpha | Source rights unverified | Unused registration | Removed registration | `unused_orphan` |

## Consumer and visual evidence

Exact identifier searches covered `common/`, `events/`, `interface/`, and `localisation/`, including literal references and the Event 033 dynamic constructors.
The old news event IDs `chaosx.news.37` and `chaosx.news.38` are absent from the current engine source.
The only prototype map sprite consumer was the unbound window removed in this change.
No current gameplay consumer was redirected or given replacement art.
Each of the twelve DDS files was decoded and opened individually during the parent visual pass.
The retained review paths and dimensions are recorded in `docs/assets/033_acid_rain/final_inventory_review/runtime_inventory.json` and its `dds_roundtrip/` directory.
Those working paths are evidence only and are not referenced by engine source.
The immutable pre-retirement inventory is `runtime_inventory_before_retirement.json` in the same evidence folder.
The post-retirement decoder found 80 current Event 033 DDS files, with zero legacy registrations and zero unused runtime files in its exact inventory scope.
Missing required animation files are absent from that count and remain blockers.

The reverse inventory found 115 Event 033 DDS files before retirement, comprising 80 accepted-package files, 12 legacy registrations, and 23 other unused files.
These are file counts, not final requirement coverage or a visual completion claim.
The 23 other unused files comprise ten superseded achievement icons and thirteen superseded decision icons.
All ten superseded achievement masters, processed previews, and decoded DDS files were opened individually.
All thirteen superseded decision masters, processed previews, and decoded DDS files were opened individually.
Several decision source masters contain colored transparent-edge contamination, most visibly the soil-reclamation source.
Those candidates are rejected for final use, and their recoverable retirement resolves their shipping disposition without repairing art for decisions that do not exist.

| Asset | Asset family | Gameplay consumer | Sprite | Source or master | Final runtime path | Expected size | Actual size | Alpha or frame treatment | Visual defects | Wiring defects | Repair performed | Final status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `achievement_acid_rain_01_first_rain` | Superseded achievement | None | None | `source_png/achievement_acid_rain_01_first_rain_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_02_shelter_network` | Superseded achievement | None | None | `source_png/achievement_acid_rain_02_shelter_network_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_03_water_guardian` | Superseded achievement | None | None | `source_png/achievement_acid_rain_03_water_guardian_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_04_rail_survivor` | Superseded achievement | None | None | `source_png/achievement_acid_rain_04_rail_survivor_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_05_three_fronts` | Superseded achievement | None | None | `source_png/achievement_acid_rain_05_three_fronts_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_06_dead_forest` | Superseded achievement | None | None | `source_png/achievement_acid_rain_06_dead_forest_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_07_wardens_watch` | Superseded achievement | None | None | `source_png/achievement_acid_rain_07_wardens_watch_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_08_global_storm` | Superseded achievement | None | None | `source_png/achievement_acid_rain_08_global_storm_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_09_clean_return` | Superseded achievement | None | None | `source_png/achievement_acid_rain_09_clean_return_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `achievement_acid_rain_10_coverage_complete` | Superseded achievement | None | None | `source_png/achievement_acid_rain_10_coverage_complete_source.png` | None | Retired family | 64x64 | Single opaque source | Wrong accepted achievement family | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_corrosion_control` | Superseded decision icon | None | None | `source_png/decision_acid_rain_corrosion_control_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_deploy_wardens` | Superseded decision icon | None | None | `source_png/decision_acid_rain_deploy_wardens_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_emergency_decon` | Superseded decision icon | None | None | `source_png/decision_acid_rain_emergency_decon_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_evacuate_state` | Superseded decision icon | None | None | `source_png/decision_acid_rain_evacuate_state_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_protect_food` | Superseded decision icon | None | None | `source_png/decision_acid_rain_protect_food_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_protect_water` | Superseded decision icon | None | None | `source_png/decision_acid_rain_protect_water_source.png` | None | Retired family | 32x32 | Source alpha | Superseded composition | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_reclaim_soil` | Superseded decision icon | None | None | `source_png/decision_acid_rain_reclaim_soil_source.png` | None | Retired family | 32x32 | Source alpha | Damaged colored edges and transparent holes | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_reopen_services` | Superseded decision icon | None | None | `source_png/decision_acid_rain_reopen_services_source.png` | None | Retired family | 32x32 | Source alpha | Superseded composition | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_repair_transport` | Superseded decision icon | None | None | `source_png/decision_acid_rain_repair_transport_source.png` | None | Retired family | 32x32 | Source alpha | Superseded composition | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_restore_water` | Superseded decision icon | None | None | `source_png/decision_acid_rain_restore_water_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_seal_reservoirs` | Superseded decision icon | None | None | `source_png/decision_acid_rain_seal_reservoirs_source.png` | None | Retired family | 32x32 | Source alpha | Superseded composition | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_shelter_network` | Superseded decision icon | None | None | `source_png/decision_acid_rain_shelter_network_source.png` | None | Retired family | 32x32 | Source alpha | Colored edge contamination | Unused file | Moved to recovery | `unused_orphan` |
| `decision_acid_rain_suspend_rail` | Superseded decision icon | None | None | `source_png/decision_acid_rain_suspend_rail_source.png` | None | Retired family | 32x32 | Source alpha | Superseded composition | Unused file | Moved to recovery | `unused_orphan` |

Source paths in this second table are relative to `docs/assets/033_acid_rain/`.
The exact former runtime paths, dimensions, checksums, and decoded review paths remain in the pre-retirement inventory.

## Accepted report path repair

Five accepted report files were moved concurrently from the loose `gfx/event_pictures/` root into `gfx/event_pictures/033_acid_rain/`.
The parent verified that each moved file matched its previously decoded SHA-256 exactly.
Twelve report and event sprite aliases in `interface/033_acid_rain.gfx` now point to those existing event-scoped files.
The five corresponding report records in the working asset manifest use the same paths.
This repair preserves the art and sprite identifiers and restores consumers that otherwise referenced absent files.

## Files changed

- `interface/chaosx_decisions.gfx`: removed the two prototype decision/category sprites and seven prototype map sprites.
- `interface/chaosx_decisions.gui`: removed the unbound prototype map window.
- `interface/chaosx_pictures.gfx`: removed the unused prototype news and report sprites.
- `interface/chaosx_gfx_cleanup.gfx`: removed the unused prototype departure-news sprite.
- `docs/events/033_acid_rain/overview.md`: records retirement and distinguishes implemented source from outstanding integration and validation.
- Thirty-five unused DDS files: moved to `docs/assets/033_acid_rain/retired_runtime/` after path, consumer, and checksum verification.

Unrelated changes in shared files remain owned by their existing authors.

## Reference sections

- Offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, lines 178-194: `iconType` sprite linkage and click-through properties. SHA-256 `B74AFC86BE4E5DBB3B0FC600820D73A8340F7DC1821FC5EF02C9EE1F028C0B1C`.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/decisions.gfx`, lines 1-43: exact category sprite definitions and engine texture paths. SHA-256 `2B643E92154AF5C0F4A33DA4E19E3209815A9FCD670D3959F7D8B799B4BFE673`.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 1213-1257: scope-array iteration and the separate numeric-loop limits. SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
- Installed `documentation/effects_documentation.md`, lines 4296-4331: `for_each_scope_loop` and `for_loop_effect`. SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.

The connected tool list exposed reference context, search, read, and source lookup routes.
The reference-context request lost its execution handle without a final result, so no MCP reference citation is claimed from it.
The local sections above supplied the pertinent rule evidence.
The exact source lookup request was `hoi4.source_lookup({symbol: "acid_rain_decisions_container", maxLines: 30, maxReferences: 15, includeReferences: true})`.
It returned `timed out awaiting tools/call after 600s`.
That route gap leaves MCP source inspection unresolved.
Six specialist tasks returned `workspace routing discovery timed out`, so their requested audits and production handoffs are not acceptance evidence.
The affected roles were the probability auditor, scripted-system architect, event UI worker, icon artist, generated-art worker, and decision auditor.
No current-source GUI rendering or engine execution is claimed by this retirement note.

## Remaining work

The accepted animation runtime package, GUI repair and matched renders, achievement integration, probability scenarios, remaining individual asset review, final catalog alignment, improvement-loop disposition, and completion audit are still required.
The goal remains incomplete.
