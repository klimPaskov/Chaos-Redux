# Famine and Migration Event-Boundary and Adapter Final Audit

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-25

Auditor mode: read-only event completion audit

Repository revision observed at final source pass: `ba119e7591d6e43ac65eb4277181c2e67aa595ab`

HOI4 MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`

HOI4 MCP event-graph revision observed by successful requests: `59143acd4a234aef98ca0b6cfbb7b07211d4aa80f99536718b30e126b1deb6f9`

The worktree contained concurrent famine-system edits during this audit, including changes to `common/on_actions/chaosx_famine_migration_on_actions.txt`, `common/scripted_effects/020_black_plague_effects.txt`, `common/scripted_effects/chaosx_famine_migration_effects.txt`, and `common/scripted_effects/famine_migration_adapter_effects.txt`. This report is revision-sensitive and does not claim that later edits have been audited.

## Final status

| Surface | Status | Finding |
| --- | --- | --- |
| Shared-system event boundary | Finished | The famine and migration system has no assigned Chaos Redux event ID, no event root, no event-pool registration, no event pacing update, and no event-log evolution count. |
| State pulse boundary | Finished | The daily sparse-state processor evaluates registered famine and displacement state, but it does not call an event, event-log registration, event pacing, event timers, or event-weight updates. The pulse is not event pacing. |
| Event 149 retirement | Finished | Event 149 `Immigrations` has no source event or pool entry and no remaining flat population drain. The workbook and exported catalog explicitly mark it retired, absorbed, unavailable, and non-random. |
| Direct exact adapters | Partial | Exact owner receipts exist for Event 13 natural-disaster mortality, Event 20 Black Plague mortality, Event 12 consequences that resolve through Event 13, native nuclear strikes including Event 28, Air/Fallout mortality, and some exact corridor attacks. Several accepted deep-event rows still expose only an API or generic reassessment. |
| Unavailable legacy events | Blocked by missing source | Events 118, 120, 131, 141, and 149 have no live event roots to inspect or wire. No proxy event IDs or invented callbacks were accepted. |
| Cluster adapters | Partial | Disease and Natural Disasters reach exact member-owner adapters. Liberations, Wars, and Peace do not supply exact state, actor, cohort, and amount receipts at cluster dispatch. Cluster selection itself does not count as an additional famine event. |
| Scenario adapters | Partial | Disaster Barrage, Black Plague Unbound, and Fallout reach exact owner systems downstream. Soviet Collapse and Hunger Lines lack exact famine receipts. No separate famine event or scenario-history entry is created. |
| MCP event evidence | Partial with exact blockers | Narrow `event_inspect` succeeded for 19 named live event roots and `event_render` succeeded for Event 13. Other mandatory requests timed out. The only available historical compare target lacked an artifact provenance manifest, so comparison was blocked. Source review is not presented as a substitute for those failed MCP routes. |
| Owner patch required | Yes, for accepted incomplete adapters | Event owners must supply exact receipts for the implementable rows identified below. No owner patch is required to create a famine event ID, revive Event 149, or duplicate generic nuclear handling. |

Overall verdict: the shared-system event boundary and Event 149 retirement pass, but adapter closure remains partial and cannot support a system-complete claim.

## Authority and material inspected

Required instructions and references inspected:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- `.agents/skills/xlsx/SKILL.md`, used only to guide read-only workbook inspection
- All eight `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_*.md` files
- Every matrix, prompt, routing note, bibliography, closure review, and subagent prompt under `docs/specs/famine_and_migration_system_specs/`
- Offline wiki pages `Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`
- Vanilla `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and available on-action documentation and event precedents under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`

Primary current implementation and registry files inspected:

- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_effects/chaosx_famine_migration_effects.txt`
- `common/scripted_effects/famine_migration_adapter_effects.txt`
- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `common/on_actions/chaosx_famine_migration_on_actions.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_effects/020_black_plague_effects.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_effects/camp_repression_rework_effects.txt`
- `common/scripted_effects/cbrn_occupation_effects.txt`
- `common/scripted_effects/009_white_peace_effects.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/scripted_effects/019_infantry_spawn_achievement_effects.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `events/005_soviet_collapse.txt`, `events/006_independence_wave.txt`, `events/009_white_peace.txt`, `events/010_death.txt`, `events/011_secret_alliance.txt`, `events/012_african_union.txt`, `events/013_natural_disasters.txt`, `events/014_cannibalism.txt`, `events/015_utopia_manifesto.txt`, `events/016_brilliant_scientist.txt`, `events/018_random_resource.txt`, `events/019_infantry_spawn.txt`, `events/020_black_death.txt`, `events/021_random_civil_war.txt`, `events/023_soviet_nukes.txt`, `events/025_antarctic_ufo_race.txt`, `events/028_asteroid_impact.txt`, `events/032_missile_crisis.txt`, `events/033_acid_rain.txt`, `events/043_massive_flood.txt`, `events/050_the_great_embargo.txt`, `events/051_heat_wave.txt`, and `events/095_occupation_revolt.txt`
- `events/000_chaosx_events.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, read-only with `openpyxl`
- `docs/spreadsheets/chaos_redux_events_catalog.csv`, `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`, read-only corroboration only
- `docs/systems/famine_and_migration_system.md`
- `docs/plans/famine_and_migration_system_plans/adapter_wiring_closure.md`
- `docs/plans/famine_and_migration_system_plans/event_adapter_owner_map.md`
- Existing completion and closure reviews under `docs/plans/famine_and_migration_system_plans/`

Exact event IDs taken from the specifications and matrices and audited here are 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25, 28, 32, 33, 43, 50, 51, 95, 118, 120, 131, 141, and 149.

## Proof of the event boundary

The source specification states the boundary directly. `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_1_core.md:7` defines the feature as a shared system with no event ID and no random-event-pool entry. `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_goal_prompt.md:3` and `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_coding_prompt.md:5` repeat that the system is not a random event and that its state pulses must not count as event pacing. Part 7 repeats the no-extra-pacing rule at lines 220, 411, 470, 499, and 502.

Current source matches that contract:

- `common/scripted_effects/chaosx_logic_effects.txt:223-327` initializes `global.major_events`, `global.fire_once_events`, and `global.repeatable_events`. It contains ordinary event IDs named by the integration matrix, but contains no famine-system identifier and no Event 149 entry.
- `events/000_chaosx_events.txt` is a header-only file and does not define a famine-system root.
- Repository searches found no `chaosx.nr149` definition or invocation in `events/` or `common/`.
- `common/scripted_effects/chaosx_logic_effects.txt:850-865` owns actual event pacing through `on_minor_event_global_pacing_update` and `on_major_event_global_pacing_update`, including `global.total_events_fired`, `global.minor_events_since_major`, repeatable/major weight updates, and event-timer updates.
- No famine-system effect or on-action calls either pacing handler or directly changes `global.total_events_fired`, `global.minor_events_since_major`, event timers, or event weights.
- `common/on_actions/chaosx_on_actions_chaos_meter.txt:26` calls `famine_migration_process_registered_runtime` once through the existing host coordinator.
- `common/scripted_effects/chaosx_famine_migration_effects.txt:5449-5485` iterates only sparse registered arrays for historical anchors and candidates, active food states, active displacement states and countries, reception candidates, and relief donor states.
- `common/scripted_effects/chaosx_famine_migration_effects.txt:5320-5345` processes a registered food state by refreshing safety, consuming reassessment, reconciling cohorts, and evaluating food security. Searches across the famine-system files found no `country_event`, `news_event`, `state_event`, `record_events_log`, event evolution recorder, event pacing handler, or event-weight update in this pulse path.
- `common/scripted_effects/chaosx_event_cluster_effects.txt`, `common/scripted_effects/chaosx_events_log_effects.txt`, and shared event-log scripted localisation contain no famine-system event registration or evolution registration.

Conclusion: the daily state pulse is system maintenance and simulation, not a random-event firing, event history entry, or evolution. It must not be added to any event-count or pacing surface.

## Event 149 disposition

Event 149 is retired and absorbed, not merely hidden:

- No `chaosx.nr149` root, call, namespace member, or event file exists in live gameplay source.
- No pool array in `common/scripted_effects/chaosx_logic_effects.txt:223-327` contains 149.
- No current source associated with Event 149 applies a population change, flat population drain, famine request, displacement request, or migration request.
- The `Events` sheet in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, workbook row 150, records ID 149 as `Immigrations`, description `Retired and absorbed into the shared dynamic famine and migration system. Unavailable as a random event.`, status `Unavailable`.
- `docs/spreadsheets/chaos_redux_events_catalog.csv:227` exports the same disposition.
- `docs/systems/famine_and_migration_system.md:220` documents the retirement.

Two dormant generic numeric-name selectors remain at `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:2210-2211` and `:6215-6216`, with another at `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:645-646`. They translate numeric value 149 to `chaosx.event_name.149` inside generic display lookup tables. They do not define, register, fire, pace, evolve, or apply Event 149. Their presence is stale compatibility/display metadata, not evidence of a competing event or drain. A localisation curator may remove or explicitly retire them if the lookup table no longer needs historic IDs, but no gameplay owner patch is required for the Event 149 retirement boundary.

## Per-event adapter matrix

Verdicts distinguish a real owner call from a wrapper definition. `common/scripted_effects/chaosx_famine_migration_effects.txt:1267-1357` defines generic pressure APIs for occupation, camps, gulags, forced labour, deportation, bombing, nuclear, fallout, outbreaks, disasters, war, peace, events, air, chemical, biological warfare, clusters, scenarios, and blockades. A definition is not counted as integration unless a producer passes the exact supported context.

| Event | Catalog/source state | Adapter verdict | Evidence and remaining boundary |
| --- | --- | --- | --- |
| 5 Soviet Union Collapse | Live root, Needs Testing | API-only | The release owner has no exact state/cohort/actor/amount return or displacement receipt. The Soviet Collapse scenario dispatcher is not a substitute. Owner patch required if the accepted collapse-return design remains in scope. |
| 6 Independence Wave | Live root, Needs Testing | API-only | No exact release-state or return-cohort receipt was found. Owner patch required for accepted liberation return logic. |
| 9 White Peace | Live root, Needs Testing | Partial lifecycle only | `common/scripted_effects/009_white_peace_effects.txt:888-890` performs exact peace, while `common/on_actions/chaosx_famine_migration_on_actions.txt:81-99` marks country-level peace reassessment. No exact cohort/route/return receipt is supplied by Event 9. Explicit famine return decisions remain the exact transfer owner. |
| 10 Death | Live root, Needs Testing | Contextual design gap | No direct famine adapter call exists. A blockade or island-starvation adapter is justified only when the owner proves living civilians, exact affected states, an actor, and an amount. No speculative call should be added. |
| 11 Secret Alliance | Live root, Needs Testing | Partial, exact corridor attack only | `common/scripted_effects/011_secret_alliance_effects.txt:4479-4499` calls `famine_migration_corridor_handle_exact_state_attack` with an exact attacker and state. Broader speculative alliance migration consequences are not implemented. |
| 12 Africa Is One | Live root, Needs Testing | Implemented indirectly for destructive disaster consequences | Event 12 preserves caller proof into Event 13. `common/scripted_effects/013_natural_disasters_effects.txt:5347-5362` recognizes Event 12 hostile-natural-disaster context, while the exact state loss reaches the Event 13 famine adapter. No separate Event 12 pacing or proxy event is needed. |
| 13 Natural Disasters | Live root, Needs Testing | Implemented for exact positive civilian mortality | `common/scripted_effects/013_natural_disasters_effects.txt:5334-5344` calculates and registers exact state deaths, then calls `famine_migration_adapt_natural_disaster_state`. Nonlethal or severity-only aftermath still has only the generic API unless its owner supplies exact pressure. |
| 14 Cannibalism | Live root, Needs Testing | API-only | No exact ordinary-hunger, persecution, or flight receipt was found. Owner patch required for accepted Hunger Lines or cannibalism integration once exact state, actor, and amount are available. |
| 15 Utopia Manifesto | Live root, Needs Testing | API-only | No exact return, expulsion, reception, or food-security receipt was found. Owner patch required only for the accepted, context-proven consequences. |
| 16 Brilliant Scientist | Live root, Needs Testing | No applicable accepted receipt yet | The specs forbid inventing technology consequences. No proven current scientist outcome requires a famine adapter. Reassess only when an owner implements a concrete relevant technology or disaster outcome. |
| 18 Resources Found | Live root, Needs Testing | Partial, exact corridor attack only | `common/scripted_effects/018_resources_found_decision_effects.txt:2569` and `:2592` call the exact corridor attack handler. No additional generic migration call is justified without a concrete owner consequence. |
| 19 Soldiers from Nowhere | Live root, Needs Testing | Partial, exact corridor attack only | `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1631-1656` supplies exact attacker and defender-state context to the corridor attack handler. Broader speculative population consequences are absent. |
| 20 The Black Plague | Live root, Needs Testing | Implemented for exact positive mortality | `common/scripted_effects/020_black_plague_effects.txt:1427-1434` invokes `famine_migration_adapt_black_plague_state` only after exact population loss reports a positive applied amount. |
| 21 Random Civil War | Live root, To Be Reworked | API-only | Generic war reassessment exists, but no exact front state, actor, cohort, or amount receipt is supplied by the event owner. Owner patch required when the rework establishes those facts. |
| 23 SOV Nuclear Bombs | Live root, To Be Reworked | Downstream native coverage, no direct population effect | `events/023_soviet_nukes.txt:52-66` grants reactors and bombs but does not itself strike a populated state. Later native launches are covered by `on_nuke_drop`; an event-specific famine call at grant time would be false duplication. |
| 25 Alien technology in Antarctica | Live root, To Be Reworked | Not currently applicable | The specs require no civilian adapter unless a populated Antarctic settlement exists. No such exact civilian state consequence was found. |
| 28 Asteroid incoming | Live root, To Be Reworked | Implemented through the native nuclear owner | `events/028_asteroid_impact.txt:131-186` uses `launch_nuke`. `common/on_actions/chaosx_famine_migration_on_actions.txt:121-140` captures the launcher and nuked state, invokes the corridor nuclear receipt, reports evacuation, calculates pressure, and calls `famine_migration_handle_nuclear_state_change`. A duplicate Event 28 call is not required. |
| 32 Missiles | Live root, To Be Reworked | Partial/design-gated | No Event 32-specific famine call exists. Native nuclear, chemical, or biological owner hooks may cover actual warhead outcomes, but the current event is marked for rework and the broader matrix contract is not proven. Owner patch is required only at the exact destructive effect site. |
| 33 Acid rain | Live root, To Be Reworked | API-only | No current exact state loss or food-security adapter call was found. The accepted event-owner row remains implementable once state, actor, and amount are proven. |
| 43 Massive flood | Live root, To Be Reworked | API-only and MCP-blocked | No direct adapter call was found. If this event remains live, its exact destructive state result should route through the disaster adapter. Current MCP inspect and render both timed out. |
| 50 Great Embargo | Live root, To Be Reworked | API-only | No exact blockade state, actor, duration, or pressure amount reaches the famine system. Owner patch required when the embargo owner exposes those facts. |
| 51 Heat Wave | Live root, To Be Reworked | API-only and MCP-blocked | No direct adapter call was found. Route only an exact state food-security or mortality result, not the firing itself. Current MCP inspect and render both timed out. |
| 95 Occupation revolt | Live root, To Be Reworked | API-only | Occupation APIs exist, but Event 95 supplies no exact state, occupier, affected cohort, or amount receipt. Owner patch required when the rework owns those facts. |
| 118 Locust | Source unavailable, Unavailable | Blocked | No event root exists. The workbook and export mark the event unavailable. Do not invent a callback or reuse Event 13 as a proxy ID. |
| 120 Volcano | Source unavailable, Unavailable | Blocked | No event root exists. The workbook and export mark the event unavailable. Do not invent a callback or proxy ID. |
| 131 Mutiny | Source unavailable, Unavailable | Blocked | No event root exists. The workbook and export mark the event unavailable. No exact mutiny source exists to own a famine consequence. |
| 141 Suicide Wave | Source unavailable, Unavailable | Blocked and semantically constrained | No event root exists. The specs forbid relabelling suicide deaths as famine. A future owner may request flight only when it can prove the correct state and population movement. |
| 149 Immigrations | Retired and absorbed, Unavailable | Finished retirement, no adapter | No source, pool entry, pacing, flat drain, or adapter remains. Do not restore the event or create a proxy firing. |

## Cluster adapter matrix

The cluster dispatcher remains event selection and pacing infrastructure. A cluster must not add a second famine event, history entry, evolution, or population effect merely because a member event fired.

| Cluster | Catalog members | Verdict | Evidence and boundary |
| --- | --- | --- | --- |
| Disease | Event 20 | Implemented at member owner, cluster API-only | Event 20 sends exact positive mortality through `famine_migration_adapt_black_plague_state`. No extra cluster-level call is required. |
| Natural Disasters | Event 13 repeated family | Implemented at member owner for mortality, cluster API-only for other aftermath | Event 13 sends exact positive state mortality. Generic cluster severity without exact state and amount must not generate a second pressure pulse. |
| Liberations | Events 5 and 6 | API-only | Neither release owner supplies an exact safe-return/cohort/amount receipt. The cluster membership itself is insufficient context. |
| Wars | Events 4 and 7 in the catalog; famine specs discuss war/front consequences | Partial lifecycle only | War on-actions mark country reassessment and revalidate corridors. They do not supply exact front state, actor, cohort, or amount. No cluster-level proxy was found. |
| Peace | Event 9 | Partial lifecycle only | Peace on-actions mark reassessment. Exact voluntary or forced return remains owned by famine decisions. Cluster dispatch cannot infer a transferable cohort. |

## Scenario adapter matrix

| Scenario | Workbook status | Verdict | Evidence and boundary |
| --- | --- | --- | --- |
| SCN-003 Soviet Collapse | Needs Testing | API-only | `trigger_selected_chaosx_scenario` routes to `trigger_soviet_collapse_scenario`, but Event 5 still lacks exact famine receipt data. Scenario country and intensity are not substitutes for an affected state, actor, cohort, and amount. |
| SCN-007 Disaster Barrage | Needs Testing | Implemented downstream at Event 13 owner | `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1045-1126` passes scenario context into `call_natural_disaster`; exact state mortality later reaches `famine_migration_adapt_natural_disaster_state`. No scenario-level duplicate call is required. |
| SCN-010 The Hunger Lines | Needs Testing | API-only | The owner path is Event 14, which has no exact ordinary-hunger or displacement receipt. Owner patch required when exact state, actor, and amount are known. |
| SCN-012 Black Plague Unbound | Needs Testing | Implemented downstream at Event 20 owner | Exact positive Black Plague mortality reaches the famine adapter at the Event 20 population-loss site. No scenario-level duplicate is required. |
| Fallout and legacy Final Silence route | Not an ordinary catalog scenario row | Implemented at the Fallout and native-nuclear owners | `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:924-945` routes both current Fallout and legacy Final Silence IDs to `trigger_fallout_scenario`. Lines 2418-2424 explicitly keep it out of normal event/evolution registration and invoke the Fallout manual owner. `common/scripted_effects/fallout_consolidated_effects.txt:4022-4035` adapts exact positive Air/Fallout mortality, while `on_nuke_drop` handles native nuclear strikes. |

## Other real owner integration found

These are real source calls relevant to the shared adapter boundary, although they are not separate random-event IDs:

- `common/scripted_effects/famine_migration_adapter_effects.txt:220-325` contains active bridges for Air/Fallout, camp system, chemical aftermath, Black Plague, and natural disasters.
- `common/scripted_effects/camp_repression_rework_effects.txt:1962` and `:5104` call the camp-related adapter path from real owner effects.
- `common/scripted_effects/cbrn_occupation_effects.txt:516` calls the accepted CBRN occupation adapter path.
- `common/scripted_effects/fallout_consolidated_effects.txt:4034` calls the Air/Fallout adapter only after a positive exact population loss.
- `common/on_actions/chaosx_famine_migration_on_actions.txt:103-140` captures exact naval invasion, paradrop, and nuclear state receipts. War and peace callbacks at lines 68-99 remain reassessment-only.

No external owner call was found for the generic `famine_migration_request_event_pressure`, `famine_migration_request_cluster_pressure`, or `famine_migration_request_scenario_pressure` wrappers. No external exact producer was found for the generic occupation, bombing, war, peace, deportation, or biological-warfare wrapper solely by its public request name. Those APIs are not counted as completed adapter wiring merely because they exist.

## Accepted-plan disposition

| Accepted requirement or plan row | Disposition |
| --- | --- |
| Shared system must have no event ID, pool registration, pacing count, or evolution count | Implemented and evidenced in current source. |
| State pulses must not count as event pacing | Implemented and evidenced in the sparse host processor. |
| Event 149 must be disabled, converted, retired, or absorbed with no competing flat drain | Implemented as retirement and absorption. |
| Exact adapter after Event 13 natural-disaster population loss | Implemented. |
| Exact adapter after Event 20 Black Plague population loss | Implemented. |
| Exact native nuclear receipt, including Event 28 launches | Implemented through `on_nuke_drop`; no duplicate event-local call required. |
| Disaster Barrage, Black Plague Unbound, and Fallout scenario integration | Implemented at downstream owners, not at generic scenario dispatch. |
| Exact corridor attack ownership in Events 11, 18, and 19 | Implemented for the bounded attack surfaces found. |
| Release/return integration for Events 5 and 6 | Accepted but incomplete/API-only. |
| Hunger, displacement, expulsion, blockade, occupation, civil-war, acid-rain, flood, heat-wave, and embargo rows | Accepted or conditionally accepted but incomplete. They require exact owner context before a safe patch. |
| Cluster-level generic pressure calls | Correctly not promoted as proxy integration. Member-owner exact receipts are required. |
| Events 118, 120, 131, and 141 | Blocked by unavailable source. Their rows remain unavailable rather than being silently mapped to another event. |
| Event 149 as a live adapter producer | Rejected by retirement contract. It must not be revived. |

The existing closure and owner-map documents correctly separate wired owner calls from API-only rows. They do not support a claim that every integration-matrix row is implemented.

## MCP event evidence

Mandatory event routes were attempted with narrow selectors of the form `{ "kind": "event", "eventId": "chaosx.nr<ID>.1" }`. All successful inspect requests used the `state_flow` view. All render requests used the `overview` view. A first Event 118 inspect accidentally supplied a string selector and was rejected with MCP `-32602`, `expected object, received string`; it was immediately retried with the valid object selector and that valid request timed out.

Every successful inspect returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and informational `MCP_INLINE_FILES_TRUNCATED` because the workspace had 355 event-related files and only 64 were inline. Workspace-wide helper and lifecycle projections were deferred, so successful narrow inspection is not evidence of complete workspace validation. The graph summary at this revision was 9,513 events, 14,705 options, 1,073 entries, 8,301 unresolved nodes, 7,652 terminals, 37,134 edges, 28,241 state accesses, 2,130 diagnostics, and zero blocking diagnostics.

### Inspect results

| Event roots | Result |
| --- | --- |
| 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25, 28, 32, 33 | `EVENT_INSPECTED_PARTIAL`; individual state-flow artifacts listed below. |
| 43, 50, 51, 95 | Valid narrow inspect requests each timed out after 180 seconds; no artifact was returned. |
| 118, 120, 131, 141, 149 | Valid narrow inspect requests each timed out after 180 seconds; no artifact was returned. Source independently shows no live roots, but that source fact is not treated as successful MCP evidence. |

Successful inspect artifact URIs:

- Event 5: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66b280f255c6c5bfaee8fd2fe4662b9e5ff6fe4af337c1301ce5699d87fb57f8/5046c6857415a3144092bb727341159d843e9f03f290593ffb2d5371ab1a17cf/event-state_flow-59143acd4a23.json`
- Event 6: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49218ba976d48bdf6e36de343a6f3187bae50d69edbdfa4246f41b4cf6a82169/eba5301adc523dc34b840e0393a614019acf9e87d9065407e452d7b64c4fd828/event-state_flow-59143acd4a23.json`
- Event 9: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c713e94491eded5505b3ada4ec59852e5e37f9eafbf6ae673ea5c72dde883fd2/8f5b1c01efd60d1375d1f3e194ced15d648052ab8df9d0fcb66b395de568f99d/event-state_flow-59143acd4a23.json`
- Event 10: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d44df91451cbe853ca4603fa6154bc117bb1698051a6722aa205eb0ca758cf9/c738df68b2316db750ff98bdb98ac8b64b63d7112034caa3b92b4389bff1507d/event-state_flow-59143acd4a23.json`
- Event 11: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d34cdcdcbf2c365be5621554b272d4e17b8da8788e2ea0e0cc8e4db6fba50960/7ad638bd443731620c8ef0933913c3db715c71a783961b94391e628ba12bd6d7/event-state_flow-59143acd4a23.json`
- Event 12: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a6cfd02180a0cb63e1757d37ffba293f534f995923a05538d5e74b9f1f76f5b/c17c412c14092fb601e52fa0d5e30cb0c01cced653f04561ebcf7ebbdc6b7aeb/event-state_flow-59143acd4a23.json`
- Event 13: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0b143e33000febafd62d326478d901ab4eb57600e12c47b1bae63638c84b5dd/c2b221e4e476a1cfe399131888e4dd0c8fed89251514915df4d42029713a216b/event-state_flow-59143acd4a23.json`
- Event 14: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/976ebbcc2bf8ba6ad0cdbaa1818ece5c7016be9eabfc6def86240dec356e0f09/57657dcb5876fc56d21d386bfd99f1d4e5f2b175dcd4d240096ef9278119613a/event-state_flow-59143acd4a23.json`
- Event 15: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a21be1e76ef65dfd61077a7044e04522a96641f3de3a90dde5dce2b16cc5db0f/40c79ed2d74b80d11e29373e334077079fee9bfdfc46872adb9e8dfbf9aaffd8/event-state_flow-59143acd4a23.json`
- Event 16: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b94972d17fdb7b21fd0abc1ae4cde132b8cc3b479fdbb76afd18f1fc99b61b3/5cf885c7f2e3d559a8deda8274a644d28a5e2a4e3981167038ebb62289c7dc9f/event-state_flow-59143acd4a23.json`
- Event 18: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48240f4a754cd0415b7b6b20f4ba0d69fa894405e9206711a3472abcf51e3f40/840fac92d2609386b1d451fb4fc01fd68fe4069264516801eaaeadb97ded290f/event-state_flow-59143acd4a23.json`
- Event 19: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b7db0a85b656e0547d7f03293fd17f8dd695ef8630874dc11c3f274162479b4/7a38b1a9afa0a95b6c7eecdaa66cdaed6815466a940546b439e8a79b6bdd0d53/event-state_flow-59143acd4a23.json`
- Event 20: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a60d798c750d4caba7303b23dbef31426bb23fb28b5f098c5567a281c1e99ae/9e7a6faab2db545448c81aa6f80700164e93416d2421ffd540566661c3840383/event-state_flow-59143acd4a23.json`
- Event 21: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/481a5ffb53648ab87345531a5c22c9db1f8a47eeb7b8b1d452a19b533972ac8b/e03bf6766a24ab4a7eb0c5e5d63666b9239b079047a38921ce21094d13673d79/event-state_flow-59143acd4a23.json`
- Event 23: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/934a12c0ec40d5ade6ed0b6fbaf87bed45bb44af7f4ef28c97b8084a7bd103eb/8b4ae7283e4c36ae6a29cb3fb925f9e89c4f54c6e22aac8b7298afae8373bacd/event-state_flow-59143acd4a23.json`
- Event 25: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/896e886b7b63e667328139f9ddc1353f4f051a9869802e70d1cfcf52da13e8db/a0b0fc4836e249a4efa5f49d555e9f433a83df30103b0a1c353d613a5a0f7684/event-state_flow-59143acd4a23.json`
- Event 28: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe51fe10b9062cb350db66dd74cd50ea7174d54b79792443e6fadb925de23ced/f20e07e008fbbeb2525e191cdbe5240a546cc7621f24b67c32721d2afb4622a1/event-state_flow-59143acd4a23.json`
- Event 32: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a1adf25454127001054a6c351b3ed51ed19df829ab51bea6bbc10703ac1ebdb/12b709b81f5c99d0b034120077a398dad7870e6c2dab49dc8a8f08b16fd70f16/event-state_flow-59143acd4a23.json`
- Event 33: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b7469adbd341081acd55c4d6ecf5e98262cd00b23444e4c5a2677b96eec867/4cc73f0818dcd398499734d1c5495bf6ec8752900234be0104856727032253fb/event-state_flow-59143acd4a23.json`

### Render results

Event 13 rendered successfully with `EVENT_RENDERED_PARTIAL`, four selected nodes, and zero blocking diagnostics. Its artifacts are:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5e0a29ee91c16eeccb41f5c200dca84543e9b31170e7b9e9fec8de4ad22038b/7f7fcf0c75728c3a03d9e3163a8b6db34129d83b38c790e1f72b79e406e93fd3/event-overview-59143acd4a23-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1bad937ccea9f95f3402db1a7883e74302661f454a6cbdcb3ad06c33e6a6f019/e9e872b77f44e16e19af6dde3a3523a721aca801dcdeb274c38d28c93ba4836f/event-overview-59143acd4a23.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d47f6ae9591ad2533ee8485885119ef97c3d84226c1c52c8523eba20406c5992/ba978ff225ca97f9433f150782140360d27662d96c97f492be9ef8268963bb4e/event-overview-59143acd4a23.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d950a9480aa61cbf3e2f97723c93006f89502f758b1c496ce76598669f6ce27b/33d4848d41a1bd66ecf361a8b77e9bf4dd30c5d013ae6829b9f9cbdf4c44e16c/event-overview-59143acd4a23.png`

Valid overview render requests for Events 5, 6, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, 25, 28, 32, 33, 43, 50, 51, 95, 118, 120, 131, 141, and 149 each timed out after 180 seconds and returned no artifact. Event 5 was also retried alone and timed out, so the blocker was not limited to the large batch. These routes remain missing MCP render evidence.

### Compare result

The only available pre-existing candidate baseline was an older Event 33 state-flow artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13dd5082ed9c7d2fefae142e4bc569bf9516be61d0653c7cc4e9ef35c5b0434d/d4b831fd715ab0363e4ff49f298510e915dae579b26de4833fff795991d1080f/event-state_flow-b98e7381a4c7.json`

Reading that artifact returned `Artifact provenance manifest is unavailable`. A compare request using the complete current revision and the old artifact URI returned `ARTIFACT_NOT_FOUND` with the same missing-provenance blocker and created no comparison artifact. An earlier attempt using the short revision `b98e7381a4c7` was rejected because the route requires a full 64-character revision. No other valid baseline or changed revision was available to this read-only auditor, so no successful `event_compare` evidence exists.

## Weighted logic disposition

No famine adapter callsite, event-boundary registration, or state pulse inspected here adds or changes `ai_chance`, MTTH, a `random_list` weight, event selection weight, decision score, strategy factor, or another weighted surface. The live random-event pool has weights, but this audit did not change or balance that separate system. Therefore no probability balance pass was triggered by this read-only boundary audit. This does not validate the independent event-pool weighting system.

## Meaningful validation and limits

Validation performed:

- Cross-checked every exact event ID named by the specs and matrices against `events/`, the event-pool arrays, scripted owner effects, adapter definitions, on-actions, the workbook, and the exported catalogs.
- Distinguished wrapper definitions from real producer calls by searching the repository for external callsites.
- Traced the daily host coordinator into each sparse runtime array and checked that it does not invoke event pacing or event-log evolution.
- Traced Event 13 and Event 20 adapters from exact positive population-loss sites.
- Traced Event 28 from `launch_nuke` to the native `on_nuke_drop` famine receipt.
- Read the workbook directly and used CSV exports only as corroboration, without changing either source or exports.
- Attempted mandatory narrow MCP inspect and overview render routes for every exact named event ID, and attempted compare where a historical artifact appeared to exist.

Validation missing or blocked:

- MCP inspect evidence is absent for Events 43, 50, 51, 95, 118, 120, 131, 141, and 149 because every valid request timed out after 180 seconds.
- MCP render evidence is absent for every audited event except Event 13 because valid requests timed out after 180 seconds.
- MCP compare evidence is absent because the only historical Event 33 artifact had no provenance manifest and no other baseline or changed revision existed.
- Successful event inspections were partial and explicitly deferred workspace-wide helper and lifecycle validation due inline-file truncation.
- Events 118, 120, 131, 141, and 149 have no source event root. Their intended runtime behavior cannot be inspected or adapted until a real owner exists, except Event 149 whose accepted disposition is retirement.
- Exact adapter completion is blocked wherever the owner does not expose affected state, actor, cohort or population basis, amount, and deduplication receipt. Generic event, cluster, and scenario IDs are insufficient evidence.
- Concurrent edits mean any post-audit change to the files listed at the top requires a fresh narrow source and MCP pass before relying on this report for final completion.

## Implementable defects and recommended owner actions

1. Add exact owner-side adapter receipts for Events 5 and 6 if their accepted release/return integration remains in scope. The event or release owner must provide exact origin/destination state, actor, cohort, amount, and deduplication proof.
2. Add exact owner-side receipts for Event 14 and the Hunger Lines scenario when the hunger state, actor, and applied amount are known. Do not call a generic adapter at scenario dispatch.
3. Add exact owner-side receipts for Event 15 only for concrete expulsion, reception, return, or food-security consequences.
4. Complete Event 21 war/front integration when its rework establishes an exact state, attacker or controller, population basis, and one-shot receipt. Do not treat country-level war reassessment as a population transfer.
5. Add exact owner-side adapters for Events 33, 43, 50, 51, and 95 when their reworks apply a real state consequence. Event 43 and 51 also need fresh MCP inspect and render evidence because the present routes timed out.
6. Keep generic cluster and scenario adapters dormant until a member owner supplies exact context. Do not create extra event pacing, log entries, evolutions, or duplicate pressure solely from the cluster/scenario selection.
7. Do not add duplicate Event 28 or Event 23 famine calls. Native nuclear consequences already belong to `on_nuke_drop`; Event 23's grant of bombs is not itself a population loss.
8. Keep Events 118, 120, 131, and 141 blocked until actual source owners exist. Do not invent callbacks or substitute Event 13 or another live ID.
9. Keep Event 149 retired and absorbed. Do not restore its flat population drain or add it to a random-event array.
10. Optionally route the dormant Event 149 numeric-name selectors to documentation/localisation cleanup, but do not interpret that optional cleanup as a gameplay boundary failure.

Owner patch required: yes for accepted implementable rows with real live owners and missing exact receipts, principally Events 5, 6, 14, 15, 21, 33, 43, 50, 51, and 95, plus any future exact war, peace, occupation, bombing, liberation, or blockade producer. No patch is authorized or required to create a shared-system event, revive Event 149, add proxy IDs, or duplicate exact downstream Event 13, Event 20, Fallout, or nuclear handling.

## Simplifications, omissions, and blockers

No fallback event ID, proxy callback, fabricated source, or source-only substitute for failed MCP evidence was used in this audit.

The adapter system is simplified relative to the full specification matrices because several live event owners expose only generic country reassessment or a public adapter API rather than exact state/cohort/amount receipts. That is incomplete work, not a completed integration.

The missing MCP routes and missing legacy event sources are explicit blockers. They prevent a final all-events adapter completion claim even though the no-event boundary and Event 149 retirement are proven from current source and catalog evidence.
