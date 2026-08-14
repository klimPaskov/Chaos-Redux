# Source specification acceptance checklist

This checklist evaluates the planning package against the Event 6 request. `Complete in source design` means the requirement is fully specified but not implemented. `Implementation gate` means the final value depends on repository inspection, asset research, MCP inspection, or source audit.

The controlling 2026-07-29 acceptance decision makes source and static evidence the completion authority. MCP inspections, transaction/source audits, asset audits, documentation reconciliation, and catalog alignment remain required. Live or in-game execution, save/load behavior, runtime consumer observation, and player-owned evidence are optional future QA and are not completion blockers. Static package capacity, incomplete package or formable coverage, focus diagnostics, rights, route, AI, asset, and wiring blockers remain in force.

Current implementation authority after the IW-045 admission is 32 content-attested selectable packages across 29 compatible reservation groups, 161 unattested selectable rows out of 193 non-overlay rows, and 40 runtime adapters. Eight adapter-only rows remain fail-closed: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM. IW-040, IW-044, and IW-045 are inserted after IW-038 and before IW-033 in deterministic Join order; IW-045 passes the central content-attestation and normal/scenario preflight gates under its exact dormant BSK/state-651 contract. The parent-applied focus cleanup removed ten redundant visible edges while preserving all corresponding `available` gates; the current MCP receipt is 184 focuses, 196 connectors, zero crossings, zero node intersections, two long connectors, and 14 blocking diagnostics. This remains a current HOLD surface, not a completion receipt. Current IW-040, IW-044, and IW-045 mission probability evidence is partial with incomplete typed candidate pools and no quantitative balance claim. The whole Event 006 disposition remains HOLD / PARTIAL.

Current collision-gate continuation (2026-08-06): the cross-group Trabzon conflict is guarded by `is_independence_wave_region_06_state_354_mutex_open` and both IW-067/IW-068 planners. The Kashmir/Himalayan conflict is guarded by `is_independence_wave_region_12_state_441_mutex_open` and both IW-139/IW-149 planners. These source gates preserve the separate reservation groups and reject a state-441 reservation already held by the other package; they do not promote either package or formable.

## 2026-07-29 shared core and registry API milestone

The following bounded implementation milestone is closed under source and static evidence. It does not mark the full Event 006 specification complete and does not promote country-specific package content.

| Milestone surface | Status | Boundary that remains open |
| --- | --- | --- |
| Automatic loop, World Collapse allocation, and Event 005/Event 006 transaction boundary | Source-closed | The active automatic ladder is 3/4/5/7/10, with World Collapse also targeting 10. Scenario and static capacity counts remain separate evidence surfaces. |
| Shared dynamic systems | Source-closed | Package-specific route writers, package AI and balance, and package admission still require their own audits. |
| Country registration and reusable `chaosx_country_*` API | Source-closed | Registration does not promote country definitions, leaders, portraits, flags, focuses, decisions, forces, AI, formables, or assets. |

Evidence is recorded in `subagent_handoffs/006_core_loop_closure_v35_2026_07_29.md`, `subagent_handoffs/006_dynamic_systems_closure_v35_2026_07_29.md`, and `subagent_handoffs/006_registry_api_closure_v35_2026_07_29.md`. The whole-event disposition remains **HOLD / PARTIAL** for the unresolved package and static acceptance surfaces.

This checklist is frozen source-design evidence. Current implementation status,
including sixteen achievement definitions/localisation sets, final bounded
IW-043/IW-058 package assets, and the operational exact-carrier signature
transactions, is maintained in
`../../../plans/006_independence_wave_plans/006_source_of_truth_map.md`.

| Requirement | Evidence | Status | Remaining gate |
| --- | --- | --- | --- |
| Event identity is Event 6, Independence Wave, Minor Repeatable | `README.md`, Part 1 | Complete in source design | Register and validate in the event system |
| Event belongs to the Liberations cluster with Event 5 | Part 1, catalog handoff | Complete in source design | Keep cluster ID 2 and Low participation behavior |
| Countries release instantly in a synchronized wave | Part 1 synchronized planner, release planner diagram | Complete in source design | Implement atomic planning and execution helpers |
| Automatic wave sizes are exactly 3, 4, 5, 7, and 10 | Part 1 exact wave ladder, `006_wave_tuning_model.csv` | Complete in source design | Tune supporting package strength and World Collapse intensity without changing these counts; World Collapse also targets 10 |
| Host-facing Independence Wave crisis opens under severe occupation or low stability | Part 2 crisis surface, Part 3 crisis mission | Complete in source design | Expose the scoped costed mission, queue the ordinary synchronized planner on success, wait through the bounded retry window when the coordinator is busy, and fail closed without direct ownership changes when the plan remains invalid |
| Early waves favor existing and normal releasables | Part 1 candidate layers A and B | Complete in source design | Verify registered tags and release effects |
| Later waves add researched historical and local polities | Part 1 layers C and D, candidate registry, research rules | Complete in source design | Package-level historical research and asset review |
| High chaos can create stranger, stronger, unstable, and ambitious openings | Part 2 evolutions 3 to 5, Part 7 balance model | Complete in source design | Implement dynamic strength and route gates |
| Host countries always survive with at least one state | Part 1 host survival covenant | Complete in source design | Verify state reservations in every wave and scenario |
| Host capital is preferred as the retained remnant | Part 1 host survival covenant | Complete in source design | Current-state capital and map validity checks |
| Release origin stays separate from Soviet Collapse | Part 1 origin separation, origin diagram | Complete in source design | Implement and audit persistent origin state |
| A reused tag receives content from its actual origin | Part 1 tree and package rules, Part 4 assignment rule | Complete in source design | Load focus overlays and decisions only from matching origin |
| Concurrent Event 5 and Event 6 use reservation logic | Part 1 shared-tag collision rule | Complete in source design | Integrate with cluster runtime preparation |
| Every Event 6 country receives common survival content | Parts 3 and 4 | Complete in source design | Implement shared mechanics, decisions, ideas, and tree overlay |
| Countries can pursue recognition, government, army, host settlement, aid, and autonomy | Parts 3 and 4 | Complete in source design | Final costs, missions, AI, and localisation |
| Legitimacy, recognition, foreign support, patron influence, league cooperation, claims, instability, and formables are represented | Parts 3 and 6 | Complete in source design | Script constants, variables, UI, and cleanup |
| Shared content adapts across all candidates | Part 4 shared framework, Part 5 overlays, registries | Complete in source design | Prove country-specific play in audit |
| Strong packages receive signature ambitions | Part 5 signature modules and candidate registry | Complete in source design | Historical leaders, routes, symbols, and state mapping |
| IW-043 and IW-058 signature transactions preserve member sovereignty | Parts 3, 5, and 6 plus the dated transaction audits | Implemented for exact carriers | Whole-event completion audit and static transaction/source audit |
| New Event 6 tags end in X | Candidate registry, Part 1 tag rule, 2026-07-15 installed-registry scan | Complete in source design and current snapshot | Repeat the collision scan if either registry changes |
| Existing registered tags can be reused | Part 1 tag policy, 2026-07-15 installed-registry scan | Complete in source design and current snapshot | Implement and validate all thirteen package compatibility adapters |
| Vanilla route identities remain non-selectable overlays | Part 1 representation architecture, tag audit, candidate registry | Complete in source design and current snapshot | Implement and validate all thirteen exact additive overlay hooks |
| Regional formables use data-driven families | Part 6 and formable registry | Complete in source design | Final state groups and tag or cosmetic-tag choices |
| Formables require territory, politics, recognition, or league proof | Part 6 formation methods and discovery | Complete in source design | Implement readable requirements and staged integration |
| A league or coalition can form among released countries | Part 6 network and league | Complete in source design | Implement faction, charter, goals, AI, and cleanup |
| The league has goals, values, membership rules, and failure states | Part 6 | Complete in source design | Scripted GUI or decision presentation and AI equivalence |
| A super-event marks league formation | Part 6, approved text research, corrected audio-rights research | Complete in source design, text research complete | Clear the exact `23` recording rights before audio production or wiring, then produce the remaining package |
| A second super-event marks a dangerous global milestone | Part 6 dangerous milestone, super-event prompt | Complete in source design | Select the qualifying milestone during implementation |
| Ordinary waves do not receive super-events | Part 6 trigger thresholds | Complete in source design | Audit visibility flags and call sites |
| The event has five evolutions | Part 2 | Complete in source design | Implement enable gates, MTTH, logging, and active actor updates |
| Evolutions support active countries and evolved first openings | Part 2 | Complete in source design | Validate both entry paths separately |
| The triggerable scenario attempts every viable candidate at every intensity | Part 6 scenario preparation and intensity | Complete in source design | Build registry iteration, collision resolution, and summary |
| Scenario intensity changes territory and starting forces rather than candidate completeness | Part 6 scenario intensity | Complete in source design | Tune low through maximum packages |
| Scenario types cover faction and immediate-war variants | Part 6 scenario types | Complete in source design | Final scenario ID, UI registration, and AI setup |
| Released countries receive dynamic starting forces and reinforcement routes | Parts 2, 3, 5, and 7 | Complete in source design | Templates, stockpiles, commanders, and scaling implementation |
| Focus routes have route-specific AI and visible identity changes | Parts 4 and 7, AI matrix | Complete in source design | Focus audit and country package audit |
| Decisions use active objectives and concrete costs | Part 3 and decision map | Complete in source design | Cost tuning, tooltips, mission timing, and exploit audit |
| Sensitive identities are resolved through named, conditional, formable, or scenario dispositions rather than generalized | Resolution matrix and sensitive package ledger | Complete in source design and research | Enforce each recorded disposition and source rule |
| Historical flags, symbols, and real portraits are sourced | Part 7, asset prompt | Complete in source design | Source, license, processing, DDS, and manifest work |
| Fictional and alternate visual states can use generated art | Part 7 and asset prompt | Complete in source design | Use the correct art subagent and asset workflow |
| Animation uses real per-frame art and static fallbacks | Part 7 and asset prompt | Complete in source design | Produce frame plans, source frames, sheets, DDS, and handoff |
| Difficult achievements cover survival, league, formables, signature packages, and scenario play | Part 7 and achievement matrix | Implemented in bounded source and proof writers | Parent-wide completion audit and static proof/source matrix; live validation is optional future QA |
| Event log, docs, catalog, and workbook alignment are planned | Part 7, catalog handoff, and dated direct comparison | Shared Event 6 mirror fields aligned | Recheck when player-facing localisation changes and finish parent-wide documentation |
| Final player-facing text is direction-only in the source spec | All spec parts and prompts | Complete in source design | Implementation writes final localisation and runs text audit |
| Final super-event titles, descriptions, buttons, quotes, and musical selections are sourced | Approved text research and corrected audio-rights research | Text complete, `24` source verified, `23` blocked | Preserve approved wording and attribution, do not process `23` without clearance |
| Completion requires focused audits across all major surfaces | Part 7 acceptance and subagent briefs | Complete in source design | Run the named auditors after implementation |


## Research closure

- [x] All 206 candidate packages have a resolved representation and disposition.
- [x] The 102 custom Event 6 tags are unique and end in `X`.
- [x] The 91 registered reuses and 13 non-selectable route overlays are identified exactly.
- [x] State anchors and overlap reservation groups are recorded.
- [x] The ten signature packages have period institutions, leadership, territory, and symbol rules.
- [x] Broad and sensitive packages are converted into explicit automatic, conditional, formable, community-specific, or scenario outcomes.
- [x] Both super-event text packages are sourced and approved.
- [x] Both super-event musical selections and edit plans are recorded.
- [x] The `24` source and rights basis are verified.
- [ ] The exact `23` recording has United States redistribution clearance.
- [x] The source register records core, regional, signature, sensitive-identity, quote, and audio sources.

## Dated reconciliation gates

- [x] All 206 packages were evaluated against the installed 2026-07-14 map.
- [x] The superseded all-row map ledger contains 149 bound and 57 unbound rows across all 111 accepted reservation groups.
- [x] The current selectable country pool contains 138 bound and 55 unbound packages after all 13 overlay rows are excluded.
- [x] All 14 collision rows were independently recomputed.
- [ ] All thirteen registered-tag compatibility adapters are implemented and route-preservation audited, including the `IW-153 POK` preservation obligations.

Current source evidence for the thirteen package-local boundaries is consolidated in `../../../plans/006_independence_wave_plans/subagent_handoffs/006_registered_tag_compatibility_adapters_audit_2026_08_14.md`. The checkbox remains open because the adapter receipts are dormant and fail-closed until each package's identity, asset, host/collision, and complete admission evidence is independently accepted.
- [x] All thirteen additive vanilla route-overlay hooks are implemented and kept out of the release selector; the final IW-156/IW-196/IW-197/IW-204 adapters are source-validated but not package-admitted.

IW-022 has a bounded CRO-origin `dalmatia` source adapter, IW-025 has a bounded HUN-origin `vojvodina` source adapter, IW-035 has a bounded living-LIT `LIVONIA` adapter, IW-059 has a bounded formed `neo_mesopotamia` adapter, IW-085 has a bounded Italian-autonomy `LBA` adapter, IW-101/IW-102/IW-105 have bounded mutually exclusive COG cosmetic adapters, and IW-156/IW-196/IW-197/IW-204 have bounded TNE, Antilles, and Chilean vanilla overlays. Their meaningful-tree, network, league, formable, symbol, save/load, and live-runtime evidence are intentionally not counted toward either unchecked acceptance gate; no exact route-overlay hook remains absent.
- [x] An explicit state-level mutual exclusion guards the Trabzon cross-group automatic conflict.
- [x] The Himalayan confederation route consumes or excludes the Kashmir reservation through the shared state-441 mutex.
