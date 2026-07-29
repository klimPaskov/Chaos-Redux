# Event 20 Part 9 Triggerable Scenario Completion Audit

## Outcome

**Status: blocked and not implemented.**

The accepted Part 9 triggerable scenario does not exist in the live Triggerable Scenarios window or in Event 20 gameplay.

The shared data-driven scenario GUI is ready to host Event 20, and the Event 20 core disease runtime, state registry, shared disease board, selected-state response decisions, weekly scheduler, mortality ledger, and black contamination-mapmode rendering provide reusable foundations.

The required scenario adapter cannot truthfully be completed yet because the live repository has no Event 20 Evolution I-IV recording providers, Rat Nation tag pool or country packages, separate Rat King package, Royal Basin transaction, rat armies, rat focus trees, rat AI, growth and dominance pulses, consolidation grace-period system, coronation super-event, Event 20 evolution log entries, or scenario achievement disqualifier.

This was a read-only completion audit.

No gameplay, GUI, localisation, spreadsheet, or asset file was edited.

The only added file is this audit handoff.

## Scope boundary

The assigned implementation request conflicts with the event-completion-auditor role, which forbids gameplay edits and fixes.

The audit therefore inspected the complete Part 9 contract and its dependent Part 4-Part 6 surfaces, mapped them against the live scenario and Event 20 systems, and recorded the blockers and required implementation order.

The shared Black Plague response tranche and Doctor Wu files were inspected only as downstream providers and were not modified.

## Accepted-plan disposition

| Accepted or rejected direction | Disposition in the live repository |
| --- | --- |
| Part 9 controls the triggerable scenario | Accepted in `review/source_of_truth_and_plan_disposition.md:18`, but unimplemented |
| Manual bootstrap forces Evolutions I-IV | Accepted at `review/source_of_truth_and_plan_disposition.md:38`, but no Event 20 evolution writers or recorders exist |
| Manual launch does not grant Evolution V or `world_end` | Accepted at `review/source_of_truth_and_plan_disposition.md:39`; no conflicting Event 20 scenario implementation exists |
| Existing disease category and mapmode are reused | Accepted and implemented as reusable providers |
| Rat Nations share one deep tree with origin modules | Accepted in the planning package, but the tree and country package do not exist |
| Independent Rat Nations coexist with a separate Rat King during a grace period | Accepted in Part 9, but none of the country, grace-period, allegiance, dominance, or royal-consolidation providers exist |
| Dedicated scenario window or scenario art is unnecessary | Accepted and supported by the existing generic scenario GUI |
| New broad design addendum is unnecessary until implementation exposes a real engine problem | Still valid; the current blockers are missing implementation, not missing design |

The planning candidate `SCN-008` is stale.

The live shared registry already assigns ID `8` to `independence_wave`, while `common/script_constants/020_black_plague_constants.txt:19` reserves raw ID `12` for Event 20.

The shared scenario ID table uses `1` through `11` and `13`, leaving `12` collision-free.

The implementation should promote Event 20 to `SCN-012`, not retain the planning candidate `SCN-008`.

## Completion status by surface

| Surface | Status | Evidence and consequence |
| --- | --- | --- |
| Shared scenario window, four intensity stops, dynamic list, and confirmation flow | Finished provider | `common/scripted_guis/chaosx_scripted_gui_settings.txt:2656-2859` already supplies the generic list, selected detail, four slider stops, trigger gate, confirmation, and final dispatch |
| Event 20 stable scenario identity | Partial | `common/script_constants/020_black_plague_constants.txt:19` reserves ID `12`, but `common/script_constants/chaosx_triggerable_scenarios_constants.txt:15-26` has no `black_plague = 12` entry or name sort value |
| Scenario registry and all sort views | Missing | `triggerable_scenarios_initialize_registry` at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:67-166` and the four rebuild branches at lines `168-577` contain no Event 20 row |
| Scenario selection and fixed type | Missing | The scenario has no selected-name, entry-name, entry-ID, description, fixed-type, intensity-impact, or warning branches in `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` |
| Player-facing scenario localisation | Missing | No Black Plague scenario keys exist in `localisation/english/chaosx_gui_l_english.yml` or another live localisation file |
| Launch eligibility | Missing | `triggerable_scenario_can_launch_selected` at `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt:156-248` has no Event 20 branch |
| Confirmation dispatch | Missing | `trigger_selected_chaosx_scenario` at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:900-1044` has no Event 20 branch |
| Preflight and all-or-nothing transaction | Missing | No Event 20 scenario trigger or effect validates the minimum continents, states, free Rat Nation slots, free Rat King slot, Royal Basin capital, or transfer safety before mutation |
| Permanent repeat-launch state | Missing | No Event 20 scenario-launched flag, setup serial, launch history, or repeat-launch status text exists |
| Scoped bootstrap and bypass cleanup | Missing | No Event 20 scenario bootstrap flag, pulse suppression transaction, temporary reservation ledger, rollback proof, or cleanup effect exists |
| Idempotent upgrade of an active outbreak | Missing | Core state registration is idempotent, but no scenario effect counts existing established states, existing Rat Nations, an existing Rat King, or existing evolution records toward an intensity target |
| Four intensity packages | Missing | No Event 20 scenario tuning table implements the accepted continent, established-state, brood, Royal Basin, army, or Chaos-floor bands |
| Multi-continent seed selection | Missing | The live natural helper selects one weighted mainland origin and adjacent threatened states; it does not build an eligible-continent manifest or the accepted global seed-ring transaction |
| Disease state initialization | Partial provider | `black_plague_initialize_runtime`, `black_plague_apply_exposure`, `black_plague_set_current_state_phase`, and `black_plague_register_current_state` provide reusable core writes, but no scenario composes the required Threatened, Incubating, Infected, Severe, Collapsed, and rat-basin mix |
| Opening deaths | Missing scenario layer | Exact Black Plague mortality records into the shared Deaths ledger, but no bounded scenario opening-loss package exists |
| Evolution I | Simplified consumer only | Mortality and spread read `black_plague_evolution_i_active`, but no live file writes the flag, records the evolution, or protects it against duplicate scenario history |
| Evolution II | Simplified consumer only | Overseas spread reads `black_plague_evolution_ii_active`, but no live file writes or records the evolution |
| Evolution III | Missing | The board can display an Evolution III label, but no Rat Nation emergence provider, actor record, event, log entry, or flag writer exists |
| Evolution IV | Missing | The board can display an Evolution IV label, but no Rat King creation provider, alternate scenario coronation, actor record, event, log entry, or flag writer exists |
| Evolution V and terminal victory exclusion | Design complete, runtime untestable | The scenario must not write them, but there is no scenario runtime to verify and the live earned Evolution V provider is also absent |
| Rat Nation tag pool and country packages | Missing blocker | No Event 20 rat country tags, histories, identities, leaders, flags, portraits, ideas, units, focus trees, decisions, AI, or reusable-slot transaction exist |
| Separate Rat King package and Royal Basin | Missing blocker | No separate tag, Royal Basin selection, country creation, capital proof, government route, royal army, royal pulse, focus tree, decision package, or preservation path exists |
| Rat Nation and Rat King coexistence grace period | Missing | No flag, timed state, dominance/absorption gate, AI behavior, or cleanup exists |
| Rat armies and reinforcement | Missing | No scenario or live rat unit templates, materialization effects, manpower-independent reinforcement economy, army scaling, or supply validation exists |
| Rat Nation and Rat King focus trees | Missing | No Event 20 national-focus file or tree provider exists |
| Rat Nation and Rat King AI | Missing | No rat production, diplomacy, war, route-choice, consolidation, or dominance AI package exists |
| Human response AI and decisions | Partial provider | The current shared category contains Black Plague response decisions and AI weights, but no scenario performs the accepted immediate post-seed country and board reconciliation |
| Chaos floor | Missing | No scenario constants or effect apply `400`, `600`, `800`, or `999` as a minimum without lowering a higher current value |
| Shared world-threat integration | Missing blocker | `refresh_world_threat_state` at `common/scripted_effects/chaosx_dynamic_effects.txt:462-505` has no Black Plague or rat source flag, and its documentation lists no such provider |
| Weekly disease pulse | Finished provider | `black_plague_run_weekly_pulse` and the guarded state scheduler exist and can continue after a correctly completed bootstrap |
| Brood, dominance, and royal pulses | Missing | No live rat runtime exists to schedule |
| Black Plague disease board | Finished provider | The shared disease board rebuilds Black Plague entries and selected-state response status from the live state registries |
| Black contamination-mapmode rendering | Finished provider | `common/map_modes/chaosx_state_map_modes.txt:110-269` renders visible established Black Plague states with the dedicated black base and phase or rat-control border |
| Batched mapmode refresh | Finished provider, scenario call missing | `black_plague_refresh_mapmode_once` at `common/scripted_effects/020_black_plague_effects.txt:1331-1337` performs the required explicit refresh |
| Global launch report | Missing | Event 20 has no scenario report event or dynamic launch summary |
| Rat King coronation super-event | Missing blocker | Event 20 reserves super-event ID `85`, but no super-event effect, scripted-localisation branch, GUI/GFX registration, event, art, audio, or launch call exists |
| Event history and event details | Partial and stale | Generic event-name selectors know Event ID `20`, but Event 20 has no event-details text, scenario history writer, actor mapping, or scenario launch row; the live name remains `Black Death` |
| Evolution log and evolution details | Missing blocker | No Event 20 evolution effects call `record_events_log_evolution_entry`, and no Event 20 evolution detail localisation exists |
| Achievements and scenario disqualification | Missing | No Event 20 achievement runtime exists and no permanent scenario disqualifier is consumed |
| Scenario assets | No dedicated row art required | Part 9 correctly reuses the generic window |
| Resulting Rat Nation and Rat King assets | Missing blocker | The repository has response-decision source art, but no Event 20 rat flags, portraits, focus icons, rat decision art, coronation report art, or final manifest |
| Event documentation | Stale | `docs/events/020_black_plague/overview.md:127-130` still lists the response board, decisions, Doctor Wu bridge, evolutions, rat packages, scenario, logs, catalog, and workbook together as remaining tranches even though some response surfaces now exist |
| Triggerable-scenario system documentation | Stale | `docs/systems/triggerable_scenarios.md` has no SCN-012 Event 20 row |
| Catalog workbook | Stale | The `Events` row remains `Black Plague` / `To Be Reworked`, the `Clusters` sheet has no matching Black Plague row, and the `Scenarios` sheet has no Event 20 or SCN-012 row |

## Concrete live-source findings

### Shared GUI extension points

The existing UI does not require a new window.

The generic scripted GUI reads `global.triggerable_scenario_view_ids`, writes the clicked row into `triggerable_scenarios_selected`, presents four intensity stops, calls one pure launch trigger, opens one confirmation window, and calls one shared dispatch effect after confirmation.

That architecture matches Part 9.

The missing integration is limited to the shared registry, selectors, eligibility, dispatch, and Event 20-owned runtime providers.

The scripted-localisation fallbacks make partial registration unsafe.

Without Event 20-specific selector branches, an ID that reaches the window falls through to Zombie Apocalypse names, descriptions, types, and intensity impacts at `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:63-65`, `130-132`, `842-904`, and `1163-1183`.

Event 20 must therefore not be registered until all scenario localisation branches are present.

### Event 20 runtime foundations

The live Event 20 entry file contains only:

- `chaosx.nr20.1`, the hidden natural outbreak entry;
- `chaosx.nr20.900`, the state scheduler callback;
- `chaosx.nr20.901`, the open-board refresh callback;
- `chaosx.nr20.902`, the country response pulse;
- `chaosx.nr20.903`, the state response callback.

No scenario report, evolution event, Rat Nation event, Rat King event, or coronation event exists.

`black_plague_initialize_runtime` is idempotent at the disease-runtime level and initializes the disease arrays only when `black_plague_system_started` is absent.

`black_plague_register_current_state` prevents duplicate state and country array entries and grants the crisis-board flag to owners and controllers.

These are useful providers but do not implement scenario-level idempotency.

`black_plague_start_natural_outbreak` is not an acceptable scenario substitute.

It checks ordinary automatic availability, chooses one natural origin, schedules from one anchor, and sets natural-outbreak history.

Part 9 explicitly requires a scoped bypass, a preflight manifest, several continents, missing-target top-up, Evolutions I-IV, Rat Nations, a Royal Basin, a separate Rat King, and one post-transaction refresh.

### Evolution and rat-provider absence

Across live gameplay, GUI, and localisation sources:

- `black_plague_evolution_i_active` is only read by mortality, spread, and status localisation;
- `black_plague_evolution_ii_active` is only read by overseas spread and status localisation;
- `black_plague_evolution_iii_active` and `black_plague_evolution_iv_active` are only read by status localisation;
- `black_plague_rat_country` and `black_plague_rat_king_country` only appear in core human-host and rat-controller guard triggers;
- no live writer sets any Event 20 evolution active flag;
- no live country package sets either rat-country flag;
- no Event 20 effect records an evolution entry.

The Part 9 adapter therefore has no canonical provider to call for required steps 9-15.

Writing those major systems inside the shared scenario dispatcher would violate the accepted ownership model and produce an undisclosed scenario-only substitute.

### Mapmode and disease-board readiness

The black mapmode base, visibility guards, detailed tooltips, and Rat-Controlled border are present.

The event-owned refresh helper performs one direct `force_update_map_mode` of `contaminated_states_map_mode`.

The disease board rebuild reads the Event 20 registries and exposes the selected-state response layer.

A future scenario transaction should defer ordinary refreshes during setup, register every committed state, rebuild Event 20 counts and response registries once, refresh open boards once, and call `black_plague_refresh_mapmode_once` once after commit.

No separate mapmode or disease category should be created.

### World-threat gap

The shared `refresh_world_threat_state` effect is the correct aggregator, but its current source list contains zombies, Holy Realm, Mengele, Fury, Death, Cannibalism, cave threats, and Brilliant Scientist only.

Event 20 needs a dedicated source flag whose activation and cleanup are owned by the live Rat Nation/Rat King system, followed by the shared refresh call.

Calling the current aggregator without first adding that provider would not make the scenario a registered world threat.

## Accepted intensity contract still awaiting implementation

| Intensity | Continents | Established states | Independent Rat Nations | Rat King states | Chaos floor |
| --- | ---: | ---: | ---: | ---: | ---: |
| Low | 3 | 12-18 | 2-3 | 1-2 | 400 |
| Medium | 4 | 24-36 | 4-6 | 2-4 | 600 |
| High | 5 or every eligible continent when fewer exist | 45-65 | 7-10 | 4-6 | 800 |
| Maximum | every eligible inhabited continent | 75-110 | 10-16, capped by the safe tag pool | 7-10 | 999 |

No live scenario constant implements these values.

The design allows optional targets to scale down after the minimum package is proved, but it does not permit the core identity to degrade.

At minimum, a successful launch must still prove multiple continents, at least two independent Rat Nations, a separate valid Rat King country and capital, and all Evolution I-IV providers.

## Validation performed

### Task-specific static validation

- Confirmed the live shared scenario IDs are `1-11` and `13`, while Event 20 reserves `12`; there is no live ID collision for SCN-012.
- Confirmed the shared registry and four sort-view branches do not contain Event 20.
- Confirmed the pure launch gate and confirmation dispatcher do not contain Event 20.
- Confirmed no Black Plague scenario name, description, fixed type, intensity impact, warning, blocked status, or ready status exists in the shared scenario selectors or English GUI localisation.
- Confirmed the Event 20 event file contains only the natural entry and four hidden runtime or response callbacks.
- Confirmed Event 20 evolution flags have consumers but no writers or event-log recorders.
- Confirmed the rat-country flags have guard consumers but no country-package writers.
- Confirmed no Event 20 rat tags, country histories, focus trees, AI strategies, rat decision package, Rat King package, grace-period provider, or coronation presentation exists.
- Confirmed the existing contamination mapmode implements the accepted black base and Rat-Controlled border.
- Confirmed the event-owned mapmode helper can perform the required one-shot explicit refresh.
- Confirmed the shared world-threat registry does not include a Black Plague or rat source.
- Read the workbook source of truth without editing it and confirmed its Event, Cluster, and Scenario surfaces are stale or absent for Part 9.

### Optional HOI4 event inspection

A refreshed narrow trace of `chaosx.nr20.1` was blocked by the event inspector's fixed global issue ceiling: `23,398` indexed issues exceeded the `20,000` maximum.

A cached file scan completed only as `EVENT_INSPECTED_PARTIAL` and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41b114408a7e3e37354393296a21e6526badad4cd47f3dc12649d633d9a26d83/38238153ee76465f494afe9856d6fe295aec57099d83e773c6314655ea8962d9/event-scan-aaffc8cf272a.json`.

That scan indexed the workspace and reported no skipped event-analysis sources, but it did not provide a bounded Event 20 trace and is not treated as a passing Event 20 validation.

All completion conclusions rely on direct source evidence.

### Validation that remains impossible or missing

- Low, Medium, High, and Maximum launch behavior;
- active-natural-outbreak upgrade behavior;
- existing Rat Nation and existing Rat King reuse;
- one-row-only event and evolution history;
- all-or-nothing preflight and rollback;
- tag-pool exhaustion handling;
- Royal Basin capital and connected-state proof;
- army strength, supply, and performance caps;
- grace-period expiry and post-grace dominance behavior;
- immediate mapmode and board rendering after a full scenario commit;
- absence of Evolution V and `world_end` writes after launch;
- save and reload persistence;
- repeat-launch disablement;
- Maximum performance with 75-110 states and 10-16 broods.

These are not deferred polish.

They are required completion evidence once the missing providers and adapter exist.

## Asset and documentation gaps

Part 9 requires no dedicated scenario-window art.

That does not remove the downstream asset blockers.

The resulting live state requires twelve Rat Nation identities, one Rat King identity, flags, portraits or army scenes, focus icons, rat decision icons, rat ideas, coronation presentation, final runtime files, manifests, and wiring handoffs.

The current Event 20 asset directory contains source art for response decisions only.

The coronation super-event research exists in the planning pack, but there is no final gameplay presentation package.

Documentation gaps are:

- no SCN-012 entry in `docs/systems/triggerable_scenarios.md`;
- stale `docs/events/020_black_plague/overview.md` implementation status;
- no Event 20 scenario implementation handoff;
- no Event 20 scenario row in the workbook;
- stale Event 20 workbook status and detail text;
- no Event 20 evolution-detail or scenario-detail localisation;
- no final rat or coronation asset manifest.

The workbook should be updated only after final in-game wording and implementation facts exist, then exported through `.tools/export_event_catalog_csv.py`.

## Remaining blockers

1. The read-only event-completion-auditor role prohibits the requested gameplay and GUI patch.
2. Evolution I-IV activation and event-log providers are absent.
3. The reusable Rat Nation tag pool and complete country package are absent.
4. The separate Rat King and Royal Basin package is absent.
5. Rat armies, focus trees, decisions, AI, reinforcement, growth, dominance, allegiance, and royal-consolidation providers are absent.
6. The scenario grace period cannot be implemented safely until the live dominance and absorption effects exist to consume it.
7. The Rat King coronation presentation is absent.
8. Event 20 world-threat registration and scenario achievement disqualification are absent.
9. The full launch transaction has no preflight, frozen manifest, commit, cleanup, or idempotent top-up architecture.
10. No task-specific runtime validation can be performed before those systems exist.

## Recommended implementation order

1. Implement and validate the canonical Evolution I and II activation plus one-row event-log providers.
2. Implement and validate the finite Rat Nation pool, country transaction, identity package, armies, reinforcement economy, shared deep focus tree, decisions, AI, growth pulse, dominance behavior, and Evolution III recorder.
3. Implement and validate the separate Rat King tag, Royal Basin transaction, capital proof, government routes, royal army, royal pulse, focus tree, decisions, AI, allegiance and absorption mechanics, coronation presentation, and Evolution IV recorder.
4. Add the grace-period gate to the canonical dominance and royal-absorption consumers so the scenario can reuse real live logic rather than a scenario-only substitute.
5. Add Event 20 world-threat source ownership and refresh integration.
6. Implement an Event 20-owned scenario constants, triggers, and effects tranche with a pure preflight, frozen manifest, all-or-nothing core commit, idempotent active-crisis top-up, permanent SCN-012 history, temporary bootstrap and pulse suppression, cleanup proof, four intensity packages, bounded opening deaths, Chaos floor, response reconciliation, one board rebuild, and one mapmode refresh.
7. Register SCN-012 in the shared ID table, name-sort table, aligned registry arrays, all four sort views, pure launch gate, fixed-type selectors, scenario text selectors, launch-status selector, and confirmation dispatch.
8. Add one global launch report, Event 20 event-details text, one base event history row, Evolutions I-IV details, actor mappings, and one coronation presentation call.
9. Add the permanent scenario achievement disqualifier to every Event 20 achievement evaluator.
10. Run the full four-intensity and cross-case matrix, including active outbreak, existing broods, existing King, duplicate-history, tag pressure, repeat launch, map refresh, save and reload, and Maximum performance.
11. Update `docs/events/020_black_plague/overview.md`, `docs/systems/triggerable_scenarios.md`, the final asset manifests, and the source workbook from verified implementation facts.

## Files changed

- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-07-24_part9_triggerable_scenario_completion_audit.md`

No subagent gameplay patch or commit was created.

Concurrent worktree changes were preserved.

## Skills and references applied

The audit applied:

- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- `chaos-redux-event-planning`
- `chaos-redux-event-assets`
- `hoi4-decisions-missions`
- `xlsx`

The audit also consulted the required offline Paradox wiki pages, official vanilla script documentation, the live generic scenario framework, the implemented SCN-013 integration handoff, the complete Event 20 planning inventory, all Part 9 and dependency-specific sections, and the current Event 20 source providers.
# Supersession note

The incomplete-scenario findings in this historical audit are superseded by `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`. The live `SCN-012` transaction now creates the required outbreak, Rat Nation, Rat King, evolution, logging, and mapmode state while preserving the Evolution V and world-end gates.
