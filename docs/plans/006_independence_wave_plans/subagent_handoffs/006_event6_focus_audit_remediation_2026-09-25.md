# Event 006 focus-audit remediation and integration — 2026-09-25

## Disposition

**Implemented for the accepted former-host focus icon tranche and the narrow DM-53 League-state reveal gate correction.** The user approved the full Event 006 work. This handoff records source changes and evidence for these two focus-audit findings; it does not close the whole Event 006 plan, package overlays, or live-runtime acceptance.

## Implemented changes

The twelve accepted former-host child focuses now each use distinct generated art. The shared root `independence_wave_define_former_host_policy` and package-overlay focus references remain unchanged, and focus rewards, prerequisites, positions, localisation, and AI scores were not changed by the art tranche.

The parent registered twelve base sprites and twelve `_shine` siblings in `interface/006_independence_wave.gfx` and changed only the twelve matching `icon =` fields in `common/national_focus/006_independence_wave_focus.txt`. Runtime DDS files are under `gfx/interface/goals/006_independence_wave/former_host_route/`. The per-focus mapping and asset evidence are recorded in `subagent_handoffs/006_event6_former_host_icon_art_handoff_2026-09-25.md`; the accepted production brief is `subagent_handoffs/006_event6_former_host_icon_diversification_brief_2026-09-25.md`.

Parent review of the final DDS contact sheet confirmed distinct central subjects and a consistent visual family. Independent Pillow inspection confirmed all twelve DDS files decode at 94×86 to the exact RGBA pixels in their matching processed PNGs, with twelve unique pixel payloads; source and processed images retain transparency. The artist verified DDS headers, pitch, alpha corners, source hashes, and file-level round trips. Two additional native candidates remain explicitly documented as unused alternates. No background-removal fallback was used.

The `revealed_by_league_state` branch of `has_independence_wave_formable_discovery_gate` no longer accepts `independence_wave_league_route_available` by itself. It now requires `independence_wave_regional_conferences_opened`, `independence_wave_charter_vote_open`, `independence_wave_league_member`, or `independence_wave_formable_league_reveal_ready`, matching Part 6's regional-caucus, charter, or member-vote reveal rule. The first two receipts are written by the corresponding League phase transitions in `common/scripted_effects/006_independence_wave_effects.txt`. Static search found no current literal setter for the optional explicit `independence_wave_formable_league_reveal_ready` receipt; the regional-conference, charter-vote, and membership receipt paths are present. The DM-53 `ai_will_do` formula and weights are unchanged. The player-facing system document now names the same four receipts in `docs/events/006_independence_wave/systems/formable_registry.md`.

## Post-integration focus MCP evidence

The parent ran `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` against `independence_wave_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0` after the runtime DDS files and sprite wiring were present. Inspect revision is `d946269a909bfe05580f6143828fa563cd1db31f29ce577162a12a3d36a429d2`; the layout hash remains `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.

Inspect reports 184 focuses and 196 connectors, zero crossings, zero node intersections, no blocking diagnostics, and minimum same-row spacing of two columns. Render and raster returned `FOCUS_RENDERED` and `FOCUS_RASTERIZED`; all twelve new runtime textures appear in the scanned source inventory. The raster review image is 8,570×976 at `reviewScale = 0.4` and was visually reviewed alongside the final DDS contact sheet. No new layout, clipping, missing-texture, or sprite-registration issue was observed.

The remaining focus diagnostics are the previously accepted connector from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine` (ten columns by one row) and an unrelated vanilla `continuous_restrict_freedom_desc` localisation warning. The initial 0.75-scale raster request timed out after 180 seconds; the 0.4-scale retry completed successfully.

- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fe3bbcc6059f36441e6791825da39354c7b6b995d4984e75366fd24ddb4c738/6e64ced02eaec6ba3fc7a3bdc8d16334f4bda7c2d1a58ec0ca937523288c7ca4/focus-inspect.d946269a909bfe05.json`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/352b090f1cd955f9cbb30a41e0ae581761c08f51f20d788d63598a7bd7d4c3e2/ebfb2438d49a6d882f95706395d4824399b883ccdacf7262f60240cf16087386/independence_wave_focus_tree.focus.svg`.
- Raster PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/433f0f762f6b5c90f68e2a7b5394b213f31edef40cb5a92666cd9850dd3e0338/cc93971b4e59f97b422d0bb734b98e99b1282e2d4a63645b0636a945fab8b02f/independence_wave_focus_tree.focus.png`.

The shared national tree render does not establish overlay geometry. Earlier per-overlay inspect calls returned `FOCUS_TREE_NOT_FOUND`; source reachability of imported roots is not overlay layout proof. No standalone focus lint route was exposed, and live-game inspection remains user-owned.

## Probability and lifecycle evidence

The baseline probability audit and same-scenario post-patch comparison are recorded in `subagent_handoffs/006_event6_focus_probability_audit_2026-09-25.md`. The exact nine-scenario hash was reused. `hoi4.probability_compare` returned `PROBABILITY_ANALYZED_PARTIAL` through the `mission_ai_will_do` fallback with four unresolved inputs and `comparisonChanges=0`; the decision adapter returned `candidate_pool_not_found` for DM-53. The follow-up render returned `PROBABILITY_ANALYSIS_NOT_CACHED`. The partial zero-change count does not establish AI candidate-availability or effective-score equality, and no quantitative AI claim is made.

The bounded 14-case League lifecycle audit is `subagent_handoffs/006_event6_league_lifecycle_audit_2026-09-25.md`. Its source crosswalk found no new transition, alignment, ownership, reachability, cost-count, cleanup, or exploit defect and confirms the DM-53 gate semantics above. It remains **HOLD / PARTIAL** because typed League probability evidence is incomplete, the Event MCP graph is partial, status-window visual findings remain unclassified, and runtime/save-load evidence remains user-owned. The auditor reports 63 unclassified status-window overlap findings and an unclear network-standing scale; neither was changed in this focus tranche.

## Simplifications, omissions, and remaining blockers

No fallback or substitute asset was used, and no gameplay reward, AI score, focus geometry, or localisation was simplified in this tranche. The two unused candidate images are documented and are not wired.

Package-overlay geometry remains unresolved because the MCP overlay route returned `FOCUS_TREE_NOT_FOUND`. DM-53 effective AI candidate availability and scenario scores remain unresolved because the decision adapter does not recognize DM-53 and the fallback compare has four unresolved inputs. League typed AI evidence and GUI visual review remain open. SCN-008 execution, rollback, and save/load evidence, package/identity and rights admission, broad map checks, and the other Event 006 completion gates remain open; overall Event 006 stays **HOLD / PARTIAL**. Live-game validation was not performed by the agent and remains user-owned.
