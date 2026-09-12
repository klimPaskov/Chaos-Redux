# Event 006 IW-006 AFX bounded country-package audit

Date: 2026-09-12

Scope: current-worktree audit of the admitted Event 006 IW-006 Wallonia package (`AFX`) against the accepted Level 2 contract, the 2026-07-16 admission handoff, current source-of-truth routing, and the current package dispatch, attestation, Join, and cleanup surfaces.

Disposition: **NO GAMEPLAY CHANGE / SOURCE PASS WITH EVIDENCE LIMITATIONS**.

No current AFX source defect was proven strongly enough to justify a gameplay edit inside this bounded task. IW-006 is already present in the central content-attestation and scenario-preflight predicates, so the historical 2026-07-16 admission edit was not reapplied.

## Authority and comparison basis

- Accepted design: `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:7`.
- Accepted binding row: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:7` (`IW-006`, `AFX`, anchor state `34`, `RG-34`, Level 2, Northern and Western Europe, industrial-security force).
- Historical admission baseline: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_afx_final_admission_audit_2026-07-16.md`.
- Current path authority: `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:1` and its current Event 006 HOLD / PARTIAL boundary.
- Current source is consolidated in the paths named below; removed pre-merge parser paths in the 2026-07-16 handoff are historical provenance only.

## Central attestation, preflight, Join, and cleanup

The central compile-time registration is present and exact.

- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-62` includes `IW-006` in `has_independence_wave_runtime_package_adapter_for_execution_id`.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-201` includes `IW-006` in `has_independence_wave_runtime_package_content_attestation_for_execution_id`.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-230` keeps the AFX absent-or-dormant tag proof (`original_tag = AFX` or `exists = no`) behind the shared preflight and content-attestation gate.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:411-429` includes the exact `IW-006` / `is_independence_wave_exact_package_iw_006_tag_available` branch for scenario preflight.
- `common/scripted_effects/006_independence_wave_effects.txt:3690-3717` dispatches AFX package setup, `:3722-3749` dispatches package final validation, and `:3753-3780` dispatches package cleanup through the shared one-result contract.
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:294-304` requires `has_complete_independence_wave_iw_006_package_setup`, aligned active/network arrays, AFX membership in both arrays, and the network-member flag before final completion.
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:913-972` removes the AFX mission, all nine AFX decisions, AFX ideas, continuity, FORM-03 runtime, AFX flags, lifecycle/setup receipts, and the selected formable-family flags.
- `common/scripted_effects/006_independence_wave_join_effects.txt` and the consolidated Join triggers in `common/scripted_triggers/006_independence_wave_triggers.txt:1024-1145` remain shared transaction logic; no AFX-specific Join bypass or duplicate registration was found.

The Formable-03 dependency is also linked rather than bypassed.

- `common/scripted_triggers/006_independence_wave_form03_triggers.txt:202-220` defines the exact readiness attestation used by AFX and requires carrier, progression, low-countries family, territory, flag, identity, integration, and member-policy receipts.
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:208-230` requires the low-countries family, `independence_wave_form03_readiness_attestation`, the Meuse ambition, p6 force mapping, lifecycle, founding incident, and state-34 capital for the prepared proof.
- `common/decisions/006_independence_wave_form03_decisions.txt:178-195` keeps autonomous-member Join behind the active LCX connection and consent path; AFX does not self-form LCX or bypass the independent FORM-03 mutation.

## Country package coverage checklist

| Surface | Current result | Evidence |
|---|---|---|
| Identity and registration | PASS | `common/country_tags/006_independence_wave_countries.txt:17`; country file `common/countries/006_independence_wave_shared_western_european.txt`; exact `IW-006`/`AFX` predicates above. |
| Dormant setup and history | PASS | `history/countries/AFX - Wallonia.txt:1-18` supplies baseline laws and both male characters without static ownership or OOB. |
| State 34 and map binding | SOURCE PASS; MCP PARTIAL | Vanilla `history/states/34-Wallonie.txt` is the state-34 anchor with BEL owner/core, 3,043,170 manpower, steel 22, coal 5, Namur/Liege/Charleroi VPs, infrastructure 3, one arms factory, four civilian factories, and four provinces. `hoi4.map_inspect` inspected state 34 with valid state/network/adjacency/supply/rail data, but workspace-wide position validation retained 2,654 unrelated errors (1,323 building-position and 1,331 port-adjacency diagnostics). |
| Former-host survival | SOURCE PASS; runtime proof open | Setup requires a live former-host target not equal to AFX and state 34 owned/controlled by the executing country in `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:20-41`; frozen execution validates host ownership before transfer in `common/scripted_effects/006_independence_wave_execution_effects.txt`. The static allocator witness retains BEL state 6. No live transaction, save/load, or long-form host-survival receipt is claimed. |
| Politics, parties, and routes | PASS | `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:763-839` initializes AFX politics, baseline laws, four government routes, four host routes, the civilian-versus-army struggle, ambition, league, low-countries family, and FORM-03 readiness. |
| Leaders and gender metadata | PASS | `common/characters/006_independence_wave_characters_registry.txt:1324-1380` defines male `AFX_walloon_provisional_assembly` and male `AFX_walloon_reserve_commander`; the latter is a corps commander. `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:6-7` uses Jules Destrée and Louis Hubert baron Ruquoy. No female metadata or opposite-gender pool was found. |
| Ideas and lifecycle | PASS | AFX ideas in `common/ideas/006_independence_wave_ideas_registry.txt` are AFX-allowed; setup refreshes the disrupted industrial belt or Sambre-Meuse covenant and route ideas, while cleanup removes them. |
| Forces and reinforcement | SOURCE PASS; runtime materialization open | `common/script_constants/006_independence_wave_constants_registry.txt:2033,2247,2461,2675` maps p6 to profile `2` (`industrial_security`), military tradition `61`, reinforcement mask `589`, and no inheritance mask. The mask exposes five pathways (integrate militias, secure depots, convert defectors, factory/rail guards, professional officers); shared force effects create bounded divisions, stockpiles, technology/slot inheritance, and production. No live force-materialization claim is made. |
| Focus overlay | MCP PASS for structure | Eight AFX focus IDs occupy `common/national_focus/006_independence_wave_focus.txt:2493-2674`; package gates, route/host/continuity prerequisites, effects, localisation, icons, and AI weights are present. `hoi4.focus_inspect` returned 184 focuses and 196 connectors with no crossings, node intersections, or too-close pairs; only an unrelated vanilla localisation warning and one long generic connector were reported. Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/febdb7cdc0279bc4bd153479733d6eb67210692dd0b3fda9a3e7c38faf0ada4d/independence_wave_focus_tree.focus.svg`. |
| Decisions and mission | SOURCE PASS; dedicated decision viewer unavailable | `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:13-294` contains the AFX founding mission, four industrial recovery projects, four mutually exclusive route decisions, and the Meuse conference project. Visibility, cost, active-project serialization, capital/control cancellation, war cancellation, and cleanup are package-gated. No dedicated `hoi4.decision_inspect` or `hoi4.mission_inspect` route is exposed. |
| Incidents and event support | MCP PARTIAL | `events/006_independence_wave_support_events.txt` owns `chaosx.nr6.18`, `.19`, and `.20` for founding, route, and ambition incidents. Narrow `hoi4.event_inspect` and `hoi4.event_render` calls returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` with the same workspace aggregate (9,741 events, 15,167 options, 38,369 edges, 8,737 unresolved entries, one aggregate blocking diagnostic) and deferred helper/lifecycle projections. Useful event artifacts are the `.18` lint `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ad32643c6d040b3e342a05323519b8d2bdd8fb96313549fefc0b167e90c2011/1af1bd42ed3ca5857cb9f5679fca8a87e0431b8414e2dcc62ac1d370e18b7c21/event-lint-4bccb6ec7fe1.json` and `.18` overview `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68d532ba3907cea4356c539f71c92264264efe928f5ed38565cca1b926cfa45d/81ed5f90317c2cbdf326d6bb8161d56773463a0221553ea693eaecb3d3dc5b71/event-overview-4bccb6ec7fe1.svg`. |
| Visible ledgers and focus overlay GUI | Shared surface pass with warnings | Current `hoi4.gui_inspect` for `independence_wave_status_window` reports 48 inspected elements, zero missing and zero unresolved resources. Current normal-state `hoi4.gui_render` at 1920x1080 reports `GUI_RENDERED`, no blockers, and zero comparison pixels; inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/391983e6312918537a361f2d2267f311e37078642d9c1ce11e76f0137cb5443f/22d00d3b84b3a397029bd208da71c27cf99dc1042fec3127e85d79b1e4fd154e/gui-inspect.002afb7d0452a975.json`, render full SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc69780fac3983cbe079ad279a24b3314e1233d7df969141e47d8a4fb1596eff/567c217e62d42e2346d0941ca75404d8f9f5759458782e2bf822c77aef61459b/independence_wave_status_window-full.svg`. The window is shared and parent-owned; its current inspect/render retain 64 non-blocking overlaps, four missing static animation fallbacks, and incomplete synthetic state coverage in the bounded normal render, so no AFX-specific UI edit or dynamic tab/playback claim follows. |
| AI and weighted surfaces | SOURCE PASS; quantitative claim blocked | AFX strategy definitions at `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3460-3550` cover industrial survival, founding restraint, host threat, emergency command, and civic industrial policy with route/threat gates and values 60/45/35/20/30/75/100/-140/-45. Mandatory `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces` for `ai_strategy_factor` (artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21227fdeebc145b9b78c80422abc82a2acc161571a002da3db3024fdeed057f3/213f9daa9f188da1a4840b62e8c400349175888388515ef51b37c656a6eedc4f/probability-inspect-b84ee2ca17f4.json`). Decision inspection found zero decision candidates and suggested mission inspection; mission inspection found ten AFX candidates but zero available weighted candidates (artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b4c2f393bc4a05953318319067eaed315362ba840a21ad1134600489ac02661/73b2d636b6a15981c11a7070e3c5ced1e9652c11c302069cdfab34cddba30612/probability-inspect-e218a903de85.json`). Focus inspection found eight candidates and zero available weighted candidates (artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c695d74bb11ad1498bb54cd9ad6887ef0ac25493529f2c538c3a0eeeb905b62/801a31ff2740332420e860c7de773b6e61a16d36121c667b9824d282d7c23306/probability-inspect-d4970a31fc37.json`). No balance patch or probability-comparison claim is made. |
| Technology and research | Inherited; viewer gap | AFX defines no package-specific technology tree and shared force effects inherit former-host technology and research slots. Read-only tech inspect/render completed a broad scan/summary, but validation was false with 1,337 blocking workspace diagnostics; scan artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5bf0e5cac5006844e2955ca7ddc5f7b034a3596fceaba5abee092710f48f4f8/412de5ce6d92481a89ea376b09a3d7d312d7a83a9eda8717d193b50dfc0a2de0/technology-scan-c15bde174d27.json`. Package inspection of `C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.9\node_modules\hoi4-agent-tools\package.json` found only stdio/http/setup binaries and no standalone Technology Tree Viewer entry point. This is a tooling gap, not a package-specific technology defect. |
| Flags and GFX | PASS for runtime coverage | Normal, medium, and small AFX flag families each contain `AFX.tga` plus communism, democratic, fascism, and neutrality variants. `interface/006_independence_wave_small_assets.gfx:261-280` wires eight focus sprites and three event/report sprites. Portrait consumers are wired in `interface/006_independence_wave_portraits_registry.gfx:243-248` to the two existing runtime DDS paths. |
| Localisation | SOURCE PASS | Country/character/party, focus, decision, mission, idea, and incident keys are present in `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`; the current character names match the live character tokens. |
| Formable, league, host links | SOURCE PASS; runtime proof open | AFX setup registers the low-countries family, candidate flag, FORM-03 readiness, Meuse ambition, league route, and network member. The package-specific focus/decision gates preserve the separate LCX contract and host-settlement ledger. No live league/formable execution or save/load proof is claimed. |

## Map and setup details

The accepted compact anchor remains state 34, with extended Low Countries territory represented by claims, diplomacy, plebiscite, integration, and FORM-03 routes rather than automatic release ownership. The current setup predicate requires the AFX package ID, Northern and Western Europe region, regional depth, industrial-breakaway archetype, event-targeted state 34, a distinct former host, baseline civilian/export/volunteer laws, and both AFX characters. The current prepared proof adds route availability, host routes, power struggle, ambition, league, low-countries family, FORM-03 readiness, p6 force mapping, applied current-generation forces, AI profile, lifecycle, founding incident, and state-34 capital.

The map inspection is useful for state-34 connectivity and network presence, but its workspace-wide position/port diagnostics prevent a global clean-map claim. No map write was attempted.

## Stale or contradictory documentation

- `docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:13` still lists IW-006 among 39 blocked generated-flag packages even though the current AFX flag triplets exist and the package is centrally attested. This is a documentation reconciliation item, not a reason to alter assets in this bounded audit.
- Older handoffs retain pre-consolidation paths such as `interface/006_independence_wave_wallonia_frisia_assets.gfx`, while the current authority is `interface/006_independence_wave_small_assets.gfx` as stated by `006_source_of_truth_map.md:1` and confirmed by current GFX wiring.
- The 2026-07-25 postwire handoff records a historical portrait-token typo claim, but the current `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wallonia_ruquoy_trial_01/manifest.md:1-24` and live character/GFX/runtime paths use `AFX_walloon_reserve_commander`; no runtime token defect is present.
- Current runtime portrait provenance is documented by `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/manifest.md:18,33` as `approved_for_runtime`; no archive path is used by runtime GFX.

## Focused validators and MCP evidence

The following read-only checks were run against the current worktree.

- `python .tools/audit_event6_country_api.py` passed: 242 broad unique tags, 191 resolved carriers, zero missing/duplicate tags, and the IW-031 crosswalk passed.
- `python .tools/audit_event6_flags.py --strict` passed: 102 registered Event 006 tags and 102 complete flag families.
- `python .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 40 runtime adapters, 32 attested packages, 29 compatible groups, and a 20-package static witness with BEL=6 host retention.
- `python .tools/audit_event6_form16.py` passed; no AFX-specific FORM-16 mutation was introduced.
- `python .tools/audit_event6_scenario_matrix.py` passed for all 32 SCN-008 cells and eight edge cases.
- `python .tools/audit_event6_gui_matrix.py` passed its shared five-tab semantic source matrix, with live rendering/save-load still explicitly unclaimed.
- `hoi4.focus_inspect` and `hoi4.focus_render` completed read-only with no Event 006 geometry blockers.
- `hoi4.map_inspect` completed read-only for state 34 but retained the unrelated workspace-wide position/port diagnostic set described above.
- `hoi4.gui_inspect` and bounded normal-state `hoi4.gui_render` completed read-only with no hard blockers; shared-surface warnings remain.
- `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr6.18`, `.19`, and `.20` completed only as partial workspace projections with helper/lifecycle deferral.
- `hoi4.probability_inspect` was run first for AFX AI, mission, decision, and focus weighted surfaces; required typed candidates were unavailable, so no quantitative AI claim or compare was attempted.
- `hoi4.tech_inspect` and `hoi4.tech_render` completed as aggregate source-linked evidence, but validation was false and no standalone Technology Tree Viewer entry point is installed.

## Changed files, commits, and blockers

Changed files: only this dated handoff was added.

No gameplay, country, focus, decision, event, AI, map, UI, asset, localisation, catalog, attestation, or admission source was changed.

No commit was created because the parent explicitly requested no staging/commit while concurrent work was in progress and the repository had an index-lock/concurrent-edit risk. No unrelated worktree changes were staged or reverted.

Remaining blockers are evidence and documentation boundaries: shared Event 006 remains HOLD / PARTIAL; event helper/lifecycle projections remain deferred; no live allocation, release/materialization, state-transfer, former-host survival, force materialization, league/formable execution, or save/load proof exists; shared status-window state/playback coverage is incomplete; package-specific weighted AI fixtures are unavailable; the standalone Technology Tree Viewer is absent; and the generated-flag blocker document is stale for AFX. None of these blockers proves a narrow AFX gameplay defect, so no source patch is recommended from this audit.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-events`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-comfyui`
- `chaos-redux-scripted-gui`

No skill was created or updated during this audit.
