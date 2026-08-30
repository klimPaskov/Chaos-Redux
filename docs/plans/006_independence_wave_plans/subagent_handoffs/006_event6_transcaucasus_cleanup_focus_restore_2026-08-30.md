# Event 006 Transcaucasus Country Cleanup Focus Restore Handoff

Date: 2026-08-30

Owner: `/root/event6_country_package_repair`

Disposition: bounded patch ready for parent review and commit.

## Scope

This audit covers the five currently attested Event 006 packages in the current tranche, with the concrete patch limited to IW-070 Armenia (`ARM`, state `230`), IW-071 Georgia (`GEO`, state `231`), and IW-072 Azerbaijan (`AZR`, state `229`).

The accepted registry is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, rows 71-73 and 174 and 185. The latest tranche handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_country_tranche_global_2026_08_30.md`.

## Concrete source-backed gap

The Transcaucasus setup adapters call `independence_wave_assign_focus_framework` in `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:349-463`, which assigns the shared `independence_wave_focus_tree` through `common/scripted_effects/006_independence_wave_focus_effects.txt:33-83`.

The shared `independence_wave_clear_focus_runtime` helper in `common/scripted_effects/006_independence_wave_focus_effects.txt:90-110` clears Event 006 focus flags but does not restore a baseline tree.

Before this patch, `independence_wave_cleanup_iw070_iw071_iw072_transcaucasus` removed package state and ideas but did not call `load_focus_tree`, so a normally ended ARM, GEO, or AZR origin could retain the shared Event 006 tree after teardown.

`independence_wave_end_active_origin` dispatches package cleanup at `common/scripted_effects/006_independence_wave_effects.txt:2949-2982`, making this a reachable teardown path rather than a hypothetical state.

The installed vanilla focus directory contains no dedicated ARM, GEO, or AZR tree file, while vanilla focus behavior therefore falls back to `generic_focus`. The offline wiki documents focus tree IDs and `load_focus_tree`, and the installed vanilla `effects_documentation.md:4771-4787` documents the same effect shape.

The Pacific package cleanup already uses the identical guarded generic-tree restoration pattern at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:919-922`, `:965-968`, `:1006-1009`, and `:1052-1055`.

## Patch

Changed file: `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:578-583`.

Added an existing-tree guard followed by `load_focus_tree = { tree = generic_focus keep_completed = no }` after Transcaucasus package cleanup removes its package ideas.

The guard checks `has_focus_tree = independence_wave_focus_tree`, so unrelated vanilla or custom trees are not overwritten.

No new tag, state, leader, party, focus ID, localisation key, asset, formable, AI weight, admission predicate, force contract, or map mutation was introduced.

Before behavior was Event 006 cleanup followed by flag and idea removal while the shared Event 006 tree could remain loaded.

After behavior is Event 006 cleanup followed by restoration of `generic_focus` only when the shared Event 006 tree is still active.

## Country package coverage checklist

| Surface | ARM / GEO / AZR | HAW / HBX | Evidence or limitation |
|---|---|---|---|
| Registry, tag, definition, history, dispatch | Pass | Pass in current tranche handoff | Candidate registry, package triggers, package effects, and country/history registries were cross-checked. |
| State ownership, controller, capital, host, and anchor | Pass for states 230, 231, and 229 | Pass for states 629 and 378 in current tranche handoff | Package initializer and runtime-ready predicates require exact state and capital contracts. |
| Politics, leaders, parties, and portraits | Pass using existing package or vanilla carriers | Pass in current tranche handoff | No identity or portrait change was needed; portrait-specific work remains with the portrait worker boundary. |
| Focus tree assignment, route gates, decisions, missions, and ideas | Pass after cleanup patch | Pass in current tranche handoff | Shared Event 006 tree is assigned at setup and generic baseline is restored at teardown. |
| Starting military, technology, industry, supply, and production | Source contracts present | Source contracts present in current tranche handoff | No custom technology or production gap was proven; technology MCP route was blocked. |
| AI strategy and playability | Source strategy and lifecycle contracts present | Source strategy and lifecycle contracts present in current tranche handoff | Probability evidence is blocked, so no AI balance change is claimed. |
| Map, state geometry, ports, supply, and railways | Selected states pass membership and geometry checks | Selected states pass in the same map inspection | Global map diagnostics remain unrelated to these selected states. |
| Release, cleanup, Form-16, and evolution links | Form-16 audit pass; cleanup now restores baseline focus | Form-16 and Pacific cleanup patterns pass in current tranche handoff | No formable or admission gate was changed. |
| Localisation, flags, and runtime assets | Existing coverage retained | Existing coverage retained | No new player-facing identifiers or assets were added. |

## Required MCP evidence

The read-only focus inspection for `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` returned `FOCUS_INSPECTED` with 184 nodes, 195 connectors, zero geometry defects, and one non-blocking vanilla continuous-focus localisation warning.

The read-only focus render returned `FOCUS_RENDERED` with validation true and the same single warning.

Focus artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92db31057fd7b0211dae4dac48e5dba74c126e9543aca6591cea03b1937f7324/d777446920bbffe5298190906f5ea4bcc8606d3f34d1167fbbf6d8c5c9e7ff89/focus-inspect.b6f54d991563992a.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/950a6e4fa0bd853873cf59cf106a041824bfe4cbcf84b82c4bc6fbc39267c756/694bad6e8636dd6174648451728b082dbd2d81bfe249c208e62c5023870e87c9/independence_wave_focus_tree.focus.html`.

Event artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc0035fceb0dd7e1e8328c6c7c8f34037ce46dd8a0f3784b5f60680c9dc87ce4/5001a539b3564e8d55c6c39feee565809d0e514e16efd689ac18ae3ed2a9545c/event-scan-ac2516cf55a8.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90d383d86eb7109f2c1c19e39ddc9a5da818b5fae406a8a6e2655a9e010682fe/0ed76f2c5846e17b05de540babe8639b3d687d8cb348d278787386e379a34d26/event-overview-ac2516cf55a8-manifest.json`.

The read-only Event 006 inspect and render returned partial results because the workspace-wide helper and lifecycle projections exceeded the configured diagnostics boundary. The inspect reported four blocking global diagnostics and deferred large helper projections, so it is not package-local proof of a clean event graph.

The read-only map inspection for states 229, 230, 231, 378, and 629 passed selected membership, geometry, region, network, and adjacency checks. It reported 2,655 global errors from `mod:map/buildings.txt`, consisting of 1,332 `MAP_PORT_ADJACENT_SEA_INVALID` and 1,323 `MAP_BUILDING_POSITION_INVALID` diagnostics, with no selected-state package defect established.

Map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea2ae86f29afca1b5dddfe32fc7ebd5ae0b90b2ca1c787157f77251804ef7fec/9d1903e8079b3e8a17fceb09cfae4b799842a8d31591098b96d08160d675dd89/map-inspect.9c7ba486b7479c29.json`.

The map render completed as an offline representation with validation true. No map rewrite was needed or authorized for this bounded patch.

The technology inspection and render both stopped with the exact `SCAN_BYTE_LIMIT` blocker. The installed package exposes no Technology Tree Viewer, which remains an unresolved limitation.

The required `chaosx_ai_probability_auditor` route is not callable in this runtime. The exposed HOI4 probability inspector accepted the source path but returned `INTERNAL_ERROR` without evidence, so no weighted AI claim or AI patch is made.

## Targeted validation

`python -B .tools/audit_event6_country_api.py` passed with zero missing and zero duplicate carriers.

`python -B .tools/audit_event6_form16.py` passed and preserved the admitted ARM, GEO, and AZR member-state and fail-closed readiness contracts.

`python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and edge cases.

`python -B .tools/audit_event6_flags.py --strict` passed with 102 registered tags and zero incomplete flag families.

The changed file was clean before this patch, and the bounded change set contains only the one scripted-effects file plus this handoff.

## Remaining risks and next owner

The patch does not resolve the global map diagnostics, Event 006 partial graph projection, technology scan limit, unavailable Technology Tree Viewer, or unavailable probability-auditor route.

The patch does not assert new AI balance because the mandatory scenario probability pass could not produce evidence.

The parent agent should review the six added script lines, commit them with this handoff, and retain the existing fail-closed admission boundary.

No simplification, fallback, invented identity, gate relaxation, unrelated edit, or asset substitution was used.
