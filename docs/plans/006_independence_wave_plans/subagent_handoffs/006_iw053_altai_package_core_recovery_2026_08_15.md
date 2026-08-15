# IW-053 Altai package-local core recovery handoff

Status: package-local source recovery complete for parent review, with admission intentionally fail-closed.

Date: 2026-08-15.

Owner: country-package subagent.

## Guidance and source review

AGENTS.md, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions` were read before editing.

The required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, and country creation were consulted.

Vanilla script documentation for effects, triggers, modifiers, script concepts, and script constants was consulted.

Vanilla ALT country, history, characters, and state references were inspected read-only.

## Scope and ownership boundary

This tranche covers only the ALT package-local constants already present in the worktree, scripted triggers, scripted effects, ideas, AI strategy, decisions, decision category, localisation, the five explicitly permitted shared-focus callbacks, the package mechanic documentation, and this handoff.

The central adapter, attestation, normal and scenario preflight, SCN-008, deterministic Join, central dispatcher, Event 005, workbook, map, vanilla ALT files, runtime flags, portraits, and flag assets were not changed.

Package-local setup/final-validation/cleanup aliases remain in the ALT effects file, but no central dispatcher registration was added.

## Country package coverage checklist

- Tag and identity: `ALT`, exact package `independence_wave_package_id.iw_053`, identity/rights gate `independence_wave_iw_053_identity_rights_cleared`, and Soviet Collapse rejection are present in `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt:9`.
- Binding: anchor state `654`, optional state `40`, capital state `654`, and reservation group `RG-654-40` are represented in the package gates and source-of-truth bindings.
- Host: former-host event target and protected-state ownership are required before initialization and final runtime readiness.
- Roster: `ALT_grigory_gurkin` and `ALT_samuil_yufit` are required only behind the identity/rights gate.
- Politics: setup initializes democratic 50, communist 30, neutrality 10, and fascist 10; cleanup restores vanilla ALT 50/30/10/10 and vanilla party keys.
- Focus: the full shared framework and four allowed route families are assigned by the package setup path.
- Ideas: the fragmented mandate, stable compact, Oyrot council, mountain council charter, land-rights compact, workers' council, and emergency command are defined and localised.
- Decisions: one timed founding mission and ten serialized decisions are defined under the Altai mountain compact category.
- AI: four ALT package strategies are gated by identity, package setup, and route state.
- Assets: existing shared decision/focus icon names are reused; no new icon registration or runtime visual asset is introduced.
- Force: the accepted `mounted_mobile` profile and five accepted pathways are checked; navy and air inheritance remain disabled.

## Changed or recovered source surfaces

- `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt` defines package admission, exact map/host/roster/setup gates, ledger gates, decision readiness, and the explicit force mapping contract.
- `common/scripted_effects/006_independence_wave_altai_package_effects.txt` defines lifecycle, ledgers, route installers, project progress/failure, focus callbacks, setup, package-local dispatch aliases, validation, and cleanup.
- `common/ideas/006_independence_wave_altai_ideas.txt` defines the seven package ideas.
- `common/ai_strategy/006_independence_wave_altai.txt` defines the mountain-survival, host-restraint, settled-frontier, and emergency-mountain-guard strategy blocks.
- `common/decisions/006_independence_wave_altai_decisions.txt` defines `independence_wave_altai_hold_mountain_council` plus `independence_wave_altai_secure_oyrot_depots`, `independence_wave_altai_integrate_mountain_guards`, `independence_wave_altai_register_communities`, `independence_wave_altai_settle_former_host_ledgers`, `independence_wave_altai_ratify_constitutional_autonomy`, `independence_wave_altai_adopt_traditional_compact`, `independence_wave_altai_convene_socialist_councils`, `independence_wave_altai_establish_emergency_command`, `independence_wave_altai_codify_durable_sovereignty`, and `independence_wave_altai_open_frontier_network`.
- `common/decisions/categories/006_independence_wave_altai_categories.txt` registers `independence_wave_altai_mountain_compact_category` behind the exact setup gate.
- `localisation/english/006_independence_wave_altai_l_english.yml` contains the ALT party, idea, category, mission, decision, tooltip, callback, and cost keys and is UTF-8 with BOM. This file is concurrently owned by `/root/iw053_altai_localisation`; no further edits were made after that ownership notice.
- `common/national_focus/006_independence_wave_focus.txt` adds only five guarded ALT callbacks at the capital-administration, state-inventory, first-oath, former-host-policy, and fellow-new-states rewards.
- `docs/events/006_independence_wave/altai_package.md` documents the mechanic and future admission work.

## Exact force mapping mismatch and fail-closed behavior

The accepted ALT force row is recorded package-locally as `p61` with military tradition `61` and the `mounted_mobile` profile.

The shared force table currently exposes `p61 = 57`.

The package does not tune the shared value and does not substitute a different row.

`has_independence_wave_altai_force_mapping_contract` at `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt:110` requires the materialized package ID, profile, tradition `61`, exactly the five accepted pathway flags, and no navy/air or unaccepted pathway flags.

`independence_wave_setup_iw_053_altai` at `common/scripted_effects/006_independence_wave_altai_package_effects.txt:325` applies dynamic starting force only when that contract passes; otherwise it sets `independence_wave_altai_force_mapping_blocked` and leaves package setup incomplete.

The prepared setup gate at `common/scripted_triggers/006_independence_wave_altai_package_triggers.txt:170` repeats the exact tradition, path, generation, and applied-force checks.

## Roster, politics, cleanup, and symmetry audit

`has_independence_wave_altai_command_roster` requires the identity/rights clearance plus both vanilla character IDs and creates no character or portrait.

Setup clears package flags and variables, initializes baseline laws, installs the package political baseline, starts both ledgers from package constants, assigns the shared focus framework, registers route and host paths, and records the package AI profile.

The four route installers set only package party names, route flags, route popularity, route ideas, and package ledger deltas.

Cleanup removes the mission, all ten decisions, package ideas, package variables, package flags, package AI profile, and force-block marker, then restores vanilla ALT political popularity and party keys.

No `set_cosmetic_tag`, `drop_cosmetic_tag`, portrait effect, flag effect, map effect, state ownership effect, or vanilla file write is present in the package source.

## Map and state setup findings

The binding source accepts state `654` as the owned and controlled anchor and state `40` only as an optional reserved extension.

The mandatory map inspection selected states `654` and `40` and returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/243f13531696b527e2d493ae2337a8f350ff1ad4ea8fde9d9c23c1d3ec62f83b/ab3265d122b6ec48f348ba2a1dd7f984ba48d5ce7e77b396eee88a6c2bf2b6c1/map-inspect.06d72f2473304651.json`.

The selected state and region/network checks passed, while aggregate validation remains false because unrelated `map/buildings.txt` diagnostics report 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` entries.

The owner-layer map render returned `MAP_RENDERED` with PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ad1da38e5d6e5aaf4fc6f4c86817a2e5e5a064029f78c1a5b993fe0f0fa60e1/e50b8fee57f8b6f4e5f6f0f65d41d964f0fe0ca2f716b2ce9ccf4d616711b069/map-owner.png` and linked JSON/HTML artifacts.

No map write or state mutation was attempted.

## Focus inspection findings

The five shared callbacks are guarded by `original_tag = ALT` and `is_independence_wave_altai_package = yes`, so an unset identity/rights gate prevents all package callbacks.

The mandatory focus inspection returned `FOCUS_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62088d7c70321674e14879124fa349cac094a29ffd72f38c012831ea23a295c2/3a803536e1569edfd147ffef0b5a4ef9b2947eb5f371bed3c9eab2f5b8816a3b/focus-inspect.2bb18e64d6d24d6a.json`.

Focus rendering returned `FOCUS_RENDERED` with HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fea223a189955642fb67f60f9037afe95abc93e814bb78043d0c425f9f394e7/99c2d1f9f4f4807a966746f145468fb9e6d287c4efa840151800860f58df6b42/independence_wave_focus_tree.focus.html` and linked SVG/JSON/source-map/plan artifacts.

The focus viewer still reports 14 unrelated missing continuous-focus icon diagnostics, so aggregate focus validation is false for workspace reasons unrelated to the five ALT callback lines.

## Event inspection findings

No Event 006 event source was edited by this tranche.

The mandatory event scan returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1cfa366af3517d2d93590f68ef27176a790b1e8b60d13848d761b030063129a/3a0535805bc7da2b5544c99b60a0e8d9b312bc63a0e1067b6f542ec391457266/event-scan-741883f50501.json`.

The event overview render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f87d16d1812c66aca0ccd623da9a866fa4f1ec0074ec618f8f04123c499d67e/86258778917fc50e5d06dd83633a75150f7ffd8265a57c1ee65b6b011b8b76f0/event-overview-741883f50501-manifest.json`.

The partial result is the installed large-workspace limitation and reports no event-specific blocker for this package-local tranche.

## AI and probability findings

The ALT AI source contains four strategy blocks with identity and setup gates and no route-specific central AI registration.

Direct `hoi4.probability_inspect` through the `ai_strategy_factor` adapter returned `PROBABILITY_SOURCE_DISCOVERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebc42736b605aac69ca8721e2253a433201a5f078ee955a632e8234d2a726e52/5582606c40e88f05fbf0a64fe1a0b50d2f63d287eab534af2bdb7e93e3877f6d/probability-inspect-866eded80f10.json` and `candidates = 0`, `discoveryReason = no_weighted_surfaces`.

Direct probability inspection of the ALT decision source returned `PROBABILITY_SOURCE_DISCOVERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d0bf584bc24b5f7b1333236de2220df61bae969f71dc70af21564e2ab7b8df1/2da01e8da92bbf07b0e3f8124340a128d3e613f9ecbd77491931d78a4220727d/probability-inspect-b67eeba93d8f.json`.

The decision inspection found 11 mission candidates, including `independence_wave_altai_hold_mountain_council`, under the suggested `mission_ai_will_do` adapter; no quantitative balance claim is made.

The required `chaosx_ai_probability_auditor` callable was not exposed by the installed tool inventory, so an auditor-mediated probability compare could not be run.

## Technology and asset limitations

The installed package exposes no Technology Tree Viewer, so technology-tree MCP evidence is unavailable and no technology source was changed.

The vanilla ALT characters and portrait tokens remain untouched, and the separate portrait source-research handoff remains the authority for any future identity/asset decision.

No flag runtime change or new visual asset was made.

## Static validation and remaining blockers

The touched Clausewitz source brace counts are balanced, the package-specific decision helper references resolve to source definitions, the five ALT focus callback references resolve to package effects, and the localisation file begins with UTF-8 BOM bytes `EF BB BF`.

Remaining blockers are the parent-owned identity/rights clearance, the accepted p61 tradition 61 versus shared p61 tradition 57 contract mismatch, aggregate unrelated map/focus diagnostics, unavailable auditor-mediated probability compare, unavailable Technology Tree Viewer, and lack of live HOI4 runtime validation.

No simplification was made beyond preserving these explicit fail-closed gates and the requested package-local ownership boundaries.

The package-local source tranche and this handoff were committed by the parent as `d1dad8eb6` after review. The separate decision/category tranche is committed as `9a4426865`; the shared-focus callback tranche is committed as `de917ef6f`. Central admission, attestation, preflight, dispatcher, SCN-008, and Join remain intentionally untouched.

## Parent current-turn evidence supersession

After the package-local source was stabilized, the parent reran the mandatory probability and Event MCP surfaces against workspace `mod_chaos_redux_ea3b2d67c2c0`.

The ALT mission inspection returned `PROBABILITY_SOURCE_INSPECTED`, source revision `2a004de66ea0bd47285b217f5dd5344a2654f08d3b923f84495ce1f704bdf3cc`, source hash `b67eeba93d8f5d9d52798291e90df35f9760eff4c8942be623f19ca66e1fa6fa`, 11 candidates, zero available candidates, `poolComplete = false`, and 16 required inputs. The current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6b12a4583406b98ca8c492e24b74df5ffa3e0a543d5d34a6a8f6fd7c8b1c2c4/35cc9ad57b7f0af7ce1745a075d56371d7e4d2435740ffadf67ee47ab18d4a31/probability-inspect-b67eeba93d8f.json`.

The ALT AI strategy inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebc42736b605aac69ca8721e2253a433201a5f078ee955a632e8234d2a726e52/5582606c40e88f05fbf0a64fe1a0b50d2f63d287eab534af2bdb7e93e3877f6d/probability-inspect-866eded80f10.json`.

The six-scenario ALT mission evaluation `IW053_ALT_TYPED_EMPTY_CURRENT_2026_08_15` was partial: 66 candidate/scenario rows, 146 unresolved inputs, and 11 never-eligible diagnostics across empty fixtures. It proves no numeric ranking, probability, timing, dominance, or balance claim. The primary JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64e13d3fd262440697e87064270b3dafec0576b795ac2db747863d3a43acfac8/e6d7d1e1d6f2d0c4d1623a46a88d653568e5d1d50d1dd76b53467fd4c6bb7ad6/probability-032b886968fb82bf811ecb0e.json`.

The focused Event MCP state-flow inspection for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with zero selected blocking diagnostics but deferred workspace-wide helper/lifecycle projection. The state-flow artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77fbefdffb3687d52d3392595ce0878bea1dbcc368d3560896f8044a5061b257/3c72f17222e5e4d3935ed125ad8cec16797583a927036ce79a59398a5f022b96/event-state_flow-741883f50501.json`. The corresponding state render returned `EVENT_RENDERED_PARTIAL`; its source-linked SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b221ba88360f39b5b3485aae88637d83299d88a520372905c772acdff23fe5d6/027d54e90fec0714b3727143566887e1707656b80858ccf560628534069be71d/event-state-741883f50501.svg`.

These parent receipts supersede older artifact examples above where they describe the same surface. ALT remains package-local and fail-closed because identity/rights, neutral flag provenance, and the p61 tradition mismatch are unresolved; no quantitative AI or full Event 006 completion claim is made.
