# Event 006 visual asset wiring repair

Date: 2026-09-03. This narrow parent-owned repair follows the complete icon and runtime consumer audit and changes only references that pointed to absent Event 006 sprites.

## Repairs

`common/ideas/006_independence_wave_ideas_registry.txt` contained six `picture = independence_wave_recognition_diplomacy` references and five `picture = independence_wave_recognition_campaign` references. Neither token had an Event 006 GFX definition or accepted matrix row. The six patron-compact consumers now use `picture = independence_wave_patron_pressure`, and the five autonomous-league consumers now use `picture = independence_wave_league_membership`.

`common/decisions/006_independence_wave_siberian_decisions.txt` contained two `icon = GFX_decision_independence_wave_network_actions` references without a definition or runtime DDS. Both now use the registered accepted `GFX_decision_independence_wave_network_aid` decision family.

These are same-family semantic repairs. No artwork was generated, copied across asset families, resized, relabelled, or substituted from another event. The accepted 64x64 idea and 32x32 decision DDS files remain the runtime sources.

## Consumer and definition checks

After the repair, all 31 Event 006 idea picture tokens resolve to local GFX definitions, all 67 Event 006 decision icon references resolve to local or intentional vanilla definitions, all 46 Event 006 character portrait references resolve, and all 121 focus icon references resolve with paired shine sprites. The four Event 006 GFX files contain 450 unique sprite names and texture paths with zero missing paths. The two intentional vanilla restore keys, `GFX_portrait_RHI_josef_matthes` and `GFX_portrait_BAY_rupprecht_of_bavaria`, were retained because they are the installed vanilla character portraits used by cleanup paths.

The five shared Event 006 compact category icons and four category pictures remain registered through `interface/visual_consistency_repair.gfx`; moving them would break their current consumers and would not correct a defect. The unregistered portrait candidates remain documented `unused_orphan` evidence and were not deleted or wired speculatively.

## Validation and boundary

The strict Event 006 allocator and scenario matrix validators pass after the reference changes. The repaired IW-098 focus and FORM-05 decision DDS files were decoded and visually inspected at native size after conversion. No live Hearts of Iron IV launch, save/load, or MCP event-runtime claim was made. The parent visual audit remains `HOLD/PARTIAL` because portrait source and rights gates, ASSET-046 identity coverage, GUI dynamic visibility, and super-event/audio reachability are still unresolved.
