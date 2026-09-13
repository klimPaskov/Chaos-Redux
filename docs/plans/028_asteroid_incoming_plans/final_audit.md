# Event 028 final audit packet

Status: incomplete pending required engine-backed evidence and explicit asset-provenance limitations.

This packet is the current audit record for Event 028. Older exploratory handoffs in this directory are historical baselines only; current source files, the asset audit, and this packet take precedence where they differ.

## Implemented source surfaces

The global root is `chaosx.nr28.1` with `fire_only_once = yes`, and Event 028 is registered in `global.major_events` rather than the stale repeatable-event row. The opening chain, impact resolver, recovery, triggers, achievements, decisions, category, ideas, dynamic modifiers, CXT setup, on-actions, localisation, event history/details, super-event, audio registration, and workbook row are present in the Event 028 surfaces listed in `docs/events/028_asteroid_incoming/overview.md`.

The target board persists three distinct country/state pairs and a miss/N/A branch. Confirmation locks the selected pair for two days. The resolver plans strongest-profile footprints, records actual deaths, removes main-crater civilians/buildings, relocates a destroyed capital, aggregates reports, applies dust/fragments/minerals, refreshes current-control armour, and cleans the transaction. Fragment centers prefer valid land neighbors when the remaining global pool provides them and fall back only when no such candidate remains. The miss path clears preview/evolution and transaction state without impact, crater, fragment, dust, Deaths, nuclear, or hidden punishment records.

The recovery package contains the shared category, fourteen exact-target decisions, five missions, reserve-floor triggers, action-specific costs and blocked reasons, current-state checks, national closeout, cleanup, and AI weights. The package does not create a dedicated Event 028 window.

## Visual and audio evidence

The durable visual audit covers 52 unique mod-owned runtime DDS files plus the live vanilla category icon. The files were decoded and opened at native dimensions, and the final DDS round trips are retained under `docs/assets/028_asteroid_incoming/dds_roundtrip/final_runtime/`. The inventory is four 210x176 report cards, two 397x153 news files, one 114x101 category picture, seven 32x32 state icons, eight 64x64 idea icons, fourteen unique 32x32 decision icons, one 457x328 super-event image, and fifteen 64x64 achievement triplet layers.

The `asteroid_incoming_fragment_center_recovery` dynamic modifier is a documented second consumer of `fragment_crater.dds` through `GFX_idea_asteroid_incoming_fragment_center_recovery`. Part 9 requires seven distinct state-modifier assets and does not define a separate recovery icon, so this is an explicit same-site alias rather than a missing texture or an unrelated fallback.

The category picture was selected after inspecting the canonical category family and vanilla `countrydecisionview.gui`; it is paired with the installed vanilla generic-crisis category icon. The previous misplaced state and decision files were moved to their consumer families. The rejected sibling category candidate is archived and not wired. The inherited impact-news DDS is valid DXT1 at 397x153, but its original master was not available. Three rival actions intentionally share the accepted reconnaissance icon and are documented as an alias.

The super-event is registered as Event 116 in the shared image/title/quote/remark/description selectors and sprite registry. Its unique final WAV is `sound/028_asteroid_incoming/super_event_028_asteroid_impact.wav`, with source, license, duration, and SHA256 recorded in the super-event research and music catalog. Playback is dispatched only to human countries through the existing settings-aware `play_current_super_event_audio` pattern.

## Acceptance matrix

| Surface | Source evidence | Current result |
| --- | --- | --- |
| Major classification and fire-once behavior | `common/scripted_effects/chaosx_logic_effects.txt`; `events/028_asteroid_impact.txt`; late event inspect | Source and registry are correct; event inspect returned partial because the large-workspace lifecycle/helper pass was deferred, while the bounded options resource still reports three unresolved Event 028 helper catalog entries; default queue remains disabled pending open gates |
| Three pairs, miss, and N/A | Event 028 target triggers/runtime effects and `.1.na.tt`; late event inspect/render | Source wiring and the N/A trigger are present; the bounded render confirms the five opening options, but three helper calls remain unresolved in the active MCP catalog and exact runtime pair availability is not proven because target event targets are absent from the probability context |
| Two-day lock and state/tag persistence | `asteroid_incoming_accept_selected_target`; locked global event targets | Implemented in source; live save/reload and annex/control-change confirmation remains user-owned |
| Main crater and three adjacency rings | profile loader, receipt applicators, state flags, dynamic modifiers; late map inspect | Four representative states passed state-region, geometry, adjacency, railway, and supply checks; overall map validation remains false because unrelated shared locator errors were retained |
| Actual Deaths and one report per country | population receipts, country aggregation, `.5`/`.7` reports | Implemented in source; runtime Deaths totals and consolidated-report counts require live transaction evidence |
| Dust, Air Cleanliness, protection, mitigation, decay | Event 028 dust effects, shared source registry, monthly host hooks | Source and shared source-slot wiring are present; live decay, protection, Event 013 bounds, and cleanup confirmation remains pending |
| Fragmentation and conditional minerals | Event 028 evolution/fragment runtime effects; map inspect; event probability artifacts | Source is wired and representative map data is usable; probability evaluation is partial because the target pool and dynamic scenario inputs are unresolved |
| Recovery decisions, missions, AI reserve floors | `common/decisions/028_asteroid_incoming_decisions.txt` and recovery triggers; mission probability artifacts | Mission adapter inspection is complete as score-only; seven recovery scenarios ran with ten unresolved eligibility items; the requested decision adapter exposed no decision candidates |
| Five achievements and triplets | achievements, achievement triggers, localisation, `interface/chaosx_achievements.gfx`; monthly achievement hook | Definitions, setters, triplets, and monthly tracking are wired; persistent hold/reset behavior still requires live save/reload/control evidence |
| Event History, Details, reports, news, super-event | Event 028 event/localisation/shared registries; late event render | Render artifact was produced, but the bounded options resource still carries the three unresolved helper entries; large-workspace lifecycle validation was deferred and live presentation remains pending |
| Audio and settings-aware playback | asset, sound asset, music catalog, Event `.4` | Source registration and human-only settings-aware dispatch are present; live playback confirmation remains pending |
| Workbook and generated exports | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and generated CSV | Row 28 is reconciled; exports were regenerated on 2026-09-05 with recorded hashes |

## Captured MCP evidence and exact limitations

The late `hoi4_event_inspect` call for `chaosx.nr28.1` returned `EVENT_INSPECTED_PARTIAL` with source revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74a9c5d40dc10aa2978af866ac8ab679be71c557b92753bafdf54446e8ce45f3/cd7ae586d0b55d81d90be78e4ed172ac6e47cffb6ef92a7f4a4dfef5c5affa16/event-lint-1102e50fad94.json`. The wrapper report has `issueCount=0`, `diagnosticsCount=0`, and no blocking diagnostics, but its workspace-wide helper/lifecycle pass is deferred after `MCP_INLINE_FILES_TRUNCATED`. The bounded options resource for the same revision is not clean: it contains three Event 028 `missing_helper` entries for `asteroid_incoming_resolve_miss`, `asteroid_incoming_prepare_random_event_fire`, and `asteroid_incoming_stage_selected_target`, each blocked by `EVENT_HELPER_UNRESOLVED` because the active MCP catalog says the helper is absent. The corresponding source definitions are present under `common/scripted_effects/`, but the route does not provide engine-resolved evidence for them.

The matching late `hoi4_event_render` overview returned `EVENT_RENDERED_PARTIAL`. The manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51ba4df799bc517b22ed7b16d5f90fdbb9175afd252eb409f589543db4a36837/f72abd2eed660d817944a21d2502b92fe43ee6f3582367ca0d83084cad8b139a/event-overview-1102e50fad94-manifest.json`, and the PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4883ae1dfa2453e26c182cca89f5ca0d08c49d58b117e5ff00344fd2fed22cfe/49d4f93f207ee18f4d85967842d64006d9c4dc3a2dd5a3e8c1143390af4d809d/event-overview-1102e50fad94.png`. It has the same source/graph hash and the same explicit large-workspace validation limitation.

The late `hoi4_probability_inspect` route for the opening options completed static source discovery with `poolComplete=false`, four candidates, zero unresolved source nodes, and eleven required runtime inputs including the six target event targets and dynamic triggers. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a741c4925a54c7266465c50c7eca63c5e8c59a521bfa3ea356ea0525951eb76d/3c27f8ffd4a447e5b975f96acf1022db7e041b795a37687edc47100b69fe65e6/probability-inspect-267fa9c2bd4a.json`. The route therefore cannot produce normalized opening-option probabilities without a populated target-pool scenario.

The ten named opening AI situations were evaluated by `hoi4_probability_evaluate` under scenario set `AST_AI_FINAL_20260905`. The partial artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8840f0ffafcf04164fcf8363f91647210cd06cd9b567fedaaaed938d0845d7/efd508e1b6087925375b376fb2d74b7ee701b98940ac7bb00f2b03513ba25edc/probability-c47b6b6288b9ca5ad5fa7cd6.json` and records 10 scenarios, 40 candidate rows, 23 unresolved items, and 16 diagnostics. It explicitly withholds normalized probabilities because the candidate pool is incomplete, reports no unconditional AI fallback, and flags the miss-weight jump from 1 to 1000 as `PROBABILITY_EXTREME_MODIFIER_GROWTH`.

The explicit sensitivity sweep `AST_AI_SWEEP_20260905` completed as a one-point partial sweep because target-pool inputs remained unresolved. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15ff6d194b57ec7b8ea7baeb5074068ae625d70ad01a29141e386d66b8110ba9/dd21c95193b59b099e80c04be2718c35b78c67e7472a8767616ee3c8fcb67a93/probability-cbec23e40e30d173982098f9.json`. No ranking or threshold claim is made from this partial result.

The late `hoi4_map_inspect` route completed for state IDs 8, 28, 42, and 51. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6abecfdf4d96d77a032607a36a093e9dc02eded6fbb547a21189b3bb545a3070/2efbd137ede573d1b8a0cb3322ab4bf76efc2a693e6473a299ab22b1d1c602bf/map-inspect.f307a444eabf8bd0.json`. State-region membership, bitmap geometry, adjacency, railways, and supply validation passed for the requested map surfaces. The overall positions/locators validator is false because the shared existing `map/buildings.txt` contains 1323 `MAP_BUILDING_POSITION_INVALID` and 1331 `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics; the report is truncated at its 2000-diagnostic limit, with an example at `map/buildings.txt:26352` for state 12/province 1885.

The requested decision probability adapter was inspected against the exact sixteen decision IDs. The route returned `requested_adapter_empty` with zero decision candidates while exposing 21 entries under `mission_ai_will_do`; this is recorded as a route mismatch, not relabelled as decision evidence. The five actual Event 028 missions were inspected with `mission_ai_will_do` and `poolComplete=true`; the adapter is score-only rather than normalized probability. The seven recovery scenarios `AST_RECOVERY_01` through `AST_RECOVERY_07` evaluated partially with 10 unresolved eligibility items and five `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostics because the hidden target/country state was not represented in the supplied contexts.

The workbook export command was rerun after the current workbook state. The generated files contain 166 event rows, 20 cluster rows, and 16 scenario rows; the recorded SHA256 values are `1524940040a38b32176bebf797d2686c9e2ea6b49b7f2693ae7a3bbd177f3691`, `24a914fb257c99c8fc221c88828a229190de2555629dc751df05df1383be5e1e`, and `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7` respectively.

## Required evidence blockers

The event inspect/render routes are partial because the workspace-wide helper/lifecycle analysis is deferred after inline-source truncation, and the bounded Event 028 options resource still reports the three unresolved scripted helpers named above. The source definitions exist, but the MCP route did not resolve them in its active catalog. This is not treated as a full engine acceptance pass.

The opening probability source and ten-scenario evaluation are partial because the six locked target event targets and dynamic pool state cannot be supplied as a static probability scenario. The deliberate 1-to-1000 miss-weight growth remains an explicit probability diagnostic. The one-point sweep does not establish a complete sensitivity matrix, and no before/after `hoi4_probability_compare` evidence exists for the current AI patch.

The map route is available for four representative states, but overall map validation remains false due the unrelated shared `map/buildings.txt` locator diagnostics listed above. Event 028-specific map evidence does not override those existing blockers.

The requested decision adapter remains unavailable for this source: `decision_ai_will_do` returned zero candidates and suggested `mission_ai_will_do`. Mission score evidence exists, but it is not equivalent to the requested decision-AI evidence.

The fresh `chaosx_decision_mission_auditor` and `chaosx_ai_probability_auditor` subagent jobs terminated because the worker hit its usage limit before returning a handoff. No subagent patch or audit claim is being treated as evidence for those surfaces.

Four distinct rejected category evidence files were overwritten by a same-basename archive move before this final packet was written. The surviving rejected processed/round-trip PNG and DDS, the accepted candidate, and the limitation are recorded in the asset audit; the lost pre-overwrite evidence cannot be reconstructed from the current checkout without an external recovery source.

Event 028 is intentionally absent from the default-enabled rework allowlist while these implementation/audit gates remain open. It is registered as a Major event, but the current queue will not expose it automatically until the default-enable decision is made with current engine evidence.

No live HOI4 process was launched, in accordance with the repository instructions; user-owned live validation remains separate from this source and MCP audit.

## Disposition

The implementation is substantially wired but not complete for the requested goal. The exact blockers above must be resolved, the workbook export must be regenerated and verified after any workbook edit, and the final event, probability, map, decision/mission, localisation, asset, and completion audits must be attached before enabling Event 028 by default or claiming completion.
