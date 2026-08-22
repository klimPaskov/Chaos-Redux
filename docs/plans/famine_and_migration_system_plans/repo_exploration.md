# Repo Explorer Handoff

## Scope read

- Parent task: bounded seam map for the shared famine and migration system.
- Explicit constraints: read-only exploration, no gameplay or asset edits, no broad repo scan, and write only this report.
- Files or ids requested: state population-loss/manpower reconciliation; Deaths reasons; Air Cleanliness; Condemnation; occupation/camps/gulag/genocide/forced labor; bombing/nuclear/fallout/outbreak/disaster hooks; event/cluster/scenario hooks; Event 149; achievements; active registries/on-actions; workbook and edit order.
- Skills or docs read: `AGENTS.md`; `chaos-redux-events`; `chaos-redux-subagents`; the supplied implementation surface map, integration matrix, death-reason ownership table, and explorer prompt; required offline wiki pages; installed vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and related documentation headers.

## Primary findings

- The shared population API already exists. `apply_exact_state_civilian_population_loss` is the high-confidence exact transaction used by Event 014, Event 015, Event 018, and Event 020. Do not duplicate state arithmetic in event files.
- The separate `apply_state_population_loss_without_recruitable_manpower_gain` helper is used by the Chaos Meter and Fallout paths and carries the explicit no-manpower semantic. Manpower reconciliation must remain coupled to the chosen helper, not added as a second event-side effect.
- Event and cluster integration belongs in the shared registries and log pipeline. The event skill identifies `chaosx_events_log_effects`, `chaosx_logic_effects`, `chaosx_event_cluster_effects`, `chaosx_settings_effects`, the shared event-log GUI/scripted GUI, event-name/debug selectors, and the catalog workbook as the synchronized seam.
- Event 149 has no `events/` source hit for `chaosx.nr149.*` in the bounded search. Treat it as a compatibility/retirement decision, not as an existing event to extend.
- The existing HOI4 MCP route is structurally useful but partial at this repository size. A fresh narrow Event 005 inspect and overview render returned no blocking diagnostics while still scanning 9,513 events, reporting 8,271 unresolved nodes, and deferring helper/lifecycle projection. This is not complete runtime proof.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | Shared state-population contracts, including `apply_exact_state_civilian_population_loss` and `apply_state_population_loss_without_recruitable_manpower_gain`. | Existing repo-cleanup baseline records 204 references to the exact helper and the no-manpower helper at line 719. |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Public helper contract documentation. | Paired documentation file is present and is required for any new reusable adapter. |
| `common/scripted_effects/chaos_meter_effects.txt` | Chaos Meter Deaths path and the no-recruitable-manpower population-loss caller. | Baseline records caller at `:2944`. |
| `common/scripted_effects/fallout_consolidated_effects.txt` | Fallout state-loss aftermath and the no-recruitable-manpower caller. | Baseline records caller at `:40919`; Fallout is the confirmed shared nuclear/contamination seam. |
| `common/scripted_effects/014_cannibalism_effects.txt` | Existing exact state population-loss caller and Event 014 death/effect ownership. | Baseline records `apply_exact_state_civilian_population_loss` at `:4102`. |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | Existing exact state population-loss caller for Event 015. | Baseline records caller at `:915`. |
| `common/scripted_effects/018_resources_found_incident_effects.txt` | Existing exact state population-loss caller for Event 018. | Baseline records caller at `:48`. |
| `common/scripted_effects/020_black_plague_effects.txt` | Outbreak death, spread, state-loss, and movement adapter seam. | Baseline records exact population-loss caller at `:1427`. |
| `common/scripted_effects/020_black_plague_evolution_effects.txt` | Outbreak evolution aftermath and exact state-loss caller. | Baseline records caller at `:850`. |
| `common/scripted_effects/020_black_plague_scenario_effects.txt` | Manual scenario aftermath and exact state-loss caller. | Baseline records caller at `:314`. |
| `common/scripted_effects/020_black_plague_shared_response_effects.txt` | Existing relief, reception, and response-cost adapter surface. | File and helper names are recorded in the existing Event 020 source-of-truth handoffs. |
| `common/scripted_effects/020_black_plague_weaponization_effects.txt` | Existing outbreak weaponization and direct-death ownership boundary. | File is referenced by the Event 020 source map and event package. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Event 005 grain extraction, gulag/deportation/collapse adapters, and existing dynamic helper use. | Baseline records active Event 005 helper calls at `:8861` and `:8924`, plus world-threat calls at `:2658`. |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Event 013 disaster dispatch and aftermath jobs. | Baseline records `call_natural_disaster` at `:8525`; the event itself calls it from `events/013_natural_disasters.txt:60`. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Cluster definitions, member rows, automatic cluster dispatch, history recording, and natural-disaster cluster call. | Baseline records `call_natural_disaster` at `:1225`; event skill defines `initialize_event_cluster_definitions`, `event_belongs_to_cluster`, `load_event_cluster_members`, and `record_events_log_cluster_entry`. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Death/event history, actor mapping, Event Details registries, and view rebuilds. | Event skill ownership contract. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Random selection, fired-event handlers, timers, event type accounting, and pacing boundary calls. | Event skill ownership contract; existing probability baseline inspected this source for custom weighted pools. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Settings controls and generic event/cluster firing helpers. | Event skill ownership contract. |
| `common/scripted_guis/chaosx_scripted_gui_events_log.txt` | Event log, Event Details, and cluster click routing. | Event skill ownership contract. |
| `interface/chaosx_events_log_popup.gui` | Shared event-log/Event Details/cluster layout. | Shared GUI MCP baseline inspected `events_log_popup_window`. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event name, detail, cluster, and evolution selectors. | Event skill ownership contract. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | Debug-name selectors for event ids. | Event skill ownership contract. |
| `localisation/english/chaosx_event_names_l_english.yml` | Visible event-name localisation. | Event skill ownership contract. |
| `localisation/english/chaosx_gui_l_english.yml` | Shared Event Details, cluster, scenario, and status text. | Event skill ownership contract. |
| `common/script_constants/event_cluster_constants.txt` | Cluster ids, unlock tiers, cooldowns, and related tuning. | Event skill identifies this as the cluster constants file. |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | Scenario registration/launch/intensity/type controls. | Event skill identifies this as the triggerable-scenario effect surface. |
| `common/on_actions/chaosx_on_actions_system.txt` | Shared scoped on-action adapters. | Event skill identifies this shared hook file. |
| `common/on_actions/chaosx_on_actions.txt` | Shared legacy/on-action hooks and special-country cleanup seam. | Baseline records a commented cleanup call at `:57`; do not add a whole-world hook without explicit approval. |
| `events/005_soviet_collapse.txt` | Event 005 root `chaosx.nr5.1`. | Direct search confirmed `:24`. |
| `events/006_independence_wave.txt` | Event 006 root `chaosx.nr6.1`. | Direct search confirmed `:12`. Companion Event 006 files are listed by the source tree and should be followed only where release/migration ownership is direct. |
| `events/013_natural_disasters.txt` | Event 013 root `chaosx.nr13.1`. | Direct search confirmed `:12`; volcano and disaster incidents are inside this family. |
| `events/014_cannibalism.txt` | Event 014 root `chaosx.nr14.1`. | Direct search confirmed `:19`. |
| `events/015_utopia_manifesto.txt` | Event 015 root `chaosx.nr15.1`. | Direct search confirmed `:17`. |
| `events/020_black_death.txt` | Event 020 root `chaosx.nr20.1`. | Direct search confirmed `:16`. |
| `events/020_black_plague_weaponization.txt` | Event 020 weaponization event family. | Direct file search confirmed the file exists. |
| `events/021_random_civil_war.txt` | Event 021 root `chaosx.nr21.1`. | Direct search confirmed `:23`. |
| `events/028_asteroid_impact.txt` | Event 028 root `chaosx.nr28.1`. | Direct search confirmed `:23`. |
| `events/033_acid_rain.txt` | Event 033 root `chaosx.nr33.1`. | Direct search confirmed `:23`. |
| `events/050_the_great_embargo.txt` | Event 050 root `chaosx.nr50.1`. | Direct search confirmed `:23`. |
| `events/095_occupation_revolt.txt` | Event 095 root `chaosx.nr95.1`. | Direct search confirmed `:23`. |
| `common/achievements/chaos_redux_achievements.txt` | Single root-only Chaos Redux achievement registry. | `chaos-redux-events` explicitly reserves this file for event achievements. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Authoritative event/cluster/scenario workbook. | `AGENTS.md` and `chaos-redux-events`; CSVs are export-only. |
| `.tools/export_event_catalog_csv.py` | Required workbook export command. | `AGENTS.md` and `chaos-redux-events`. |

## Existing patterns

### Population and manpower

Use `apply_exact_state_civilian_population_loss` for an exact state transaction and preserve its current manpower semantics. Use `apply_state_population_loss_without_recruitable_manpower_gain` only when the caller explicitly owns direct population loss without a recruitable-manpower gain. The current Chaos Meter and Fallout callers prove that this distinction is already deliberate.

The integration matrix requires public contracts for food-security pressure, flight pressure, exact state transfer, route resolution, reception, return, integration, resettlement, and invalid-cohort cleanup. No source evidence in this bounded pass proves that those migration contracts already exist. They should be added through the shared helper owner, not copied into Event 005, 006, 013, 014, 015, 020, or 095 files.

### Event and cluster registry

The event skill's shared pattern is: register the event in `initialize_event_categories`, keep `get_event_type` and debug-name selectors aligned, record history through `chaosx_events_log_effects`, map visible names/details in scripted localisation, then add cluster membership and ordered parallel arrays in `chaosx_event_cluster_effects`. Automatic cluster firing is downstream of selected-event handling. Manual settings firing intentionally bypasses tier/cooldown/disabled/member checks, so any migration adapter must not add a second pacing loop.

### Public event adapters

Event-owned files should resolve exact actor, state, cause, and severity, then call shared contracts. The death-reason table must be treated as the source boundary: famine remains the proximate reason for later hunger deaths after bombing, nuclear, disaster, or chemical damage, while nuclear, fallout, strategic bombing, forced displacement, forced labor, occupation repression, outbreak, chemical, natural disaster, military, and camp/genocide direct reasons remain owned by the originating system.

### Scoped hooks and classifiers

The only safe shared cadence patterns are existing bounded hooks such as `on_startup`, `on_daily_CXT`, `on_weekly_CXT`, or an event-specific/scoped action. Do not introduce a new unscoped `on_daily`, `on_weekly`, or `on_monthly` loop. Special Chaos and actual nonhuman eligibility must continue through the shared classifiers in `common/scripted_triggers/chaosx_dynamic_triggers.txt`, not event-local copies.

## Vanilla or reference precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` documents `add_manpower`, `country_event`, `state_event`, `random_list`, `save_event_target_as`, and `set_variable`, which are the relevant engine primitives for exact loss, event adapters, and persisted scope pointers.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` documents `state_population` and `state_population_k`, the direct engine checks for state population eligibility.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` documents global `script_constants` and the `constant:` access form. Use it for shared thresholds/cooldowns, while respecting field limitations.
- `game:common/on_actions/00_on_actions.txt` and `game:events/Generic.txt` were present in the installed vanilla files scanned by the read-only Event Chain Viewer. These are the appropriate vanilla structural precedents for on-action dispatch and generic event firing.
- Offline wiki pages consulted for the same surfaces: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, `Interface modding - Hearts of Iron 4 Wiki.md`, and `Scripted GUI modding - Hearts of Iron 4 Wiki.md`.

## Likely edit order for the parent

1. Confirm the missing public-contract and source-of-truth paths for Deaths, Air Cleanliness, Condemnation, camps/occupation, bombing/nuclear, achievements, and active on-action registry before editing. The bounded pass found the shared population, event-log, cluster, scenario, workbook, and named event files but did not prove every owner-local adapter path.
2. Lock the shared state transaction and migration API first. Reuse the two existing population-loss helpers and define exact inputs/outputs, scope, defaults, side effects, and death-reason handoff before adding callers.
3. Add Deaths reason constants, arrays, selectors, filters, and localisation as a single synchronized surface. Keep physical reason and responsible actor/evidence separate.
4. Add Air Cleanliness and Condemnation public adapters, then map occupation/camp/genocide/forced-labor/deportation callers to those adapters. Preserve direct camp/genocide deaths as camp/atrocity-owned.
5. Add bounded owner adapters for Fallout/nuclear, bombing, outbreaks, and Event 013 disaster aftermath. Resolve state and actor locally, call shared pressure/flight/reception/return helpers, and do not create extra pacing events.
6. Update scoped on-action adapters and special-country exclusions only after helper contracts exist. Keep every cadence bounded and idempotent.
7. Reconcile Event 005, 006, 013, 014, 015, 020, 021, 028, 033, 050, and 095 in that order. Treat Events 118, 120, and 131 as missing source inputs, and stop for a design decision on Event 149 retirement/disable/adapter conversion.
8. Update event/cluster/scenario registries, names/details/debug selectors, Event Details rows, achievements, and the authoritative workbook only after final localisation and runtime identifiers are known.
9. Run the workbook exporter, then task-specific duplicate/id/localisation/registry checks. Any weighted change requires a separate named scenario baseline and same-scenario compare through the probability auditor.

## Validation checks

- Confirm every public helper call site resolves the intended state scope and uses one exact population transaction per physical death/loss. Search for duplicate state-population arithmetic outside `chaosx_dynamic_effects.txt`.
- Confirm the manpower reconciliation branch matches the helper's documented semantic, especially the no-recruitable-manpower Chaos Meter/Fallout path.
- Confirm every death reason in `famine_and_migration_system_death_reason_ownership.csv` has one reason id, one selector/localisation path, and no duplicate reason count from a secondary pressure source.
- Confirm all new adapter calls are behind exact state/actor/contamination/outbreak/disaster proofs and that special Chaos/nonhuman classifiers fail closed.
- Confirm event ids `chaosx.nr5.1`, `.nr6.1`, `.nr13.1`, `.nr14.1`, `.nr15.1`, `.nr20.1`, `.nr21.1`, `.nr28.1`, `.nr33.1`, `.nr50.1`, and `.nr95.1` remain registered in the correct event category arrays and resolve through `get_event_type`.
- Confirm Event 149 has an explicit source-of-truth disposition. A missing `chaosx.nr149.*` source hit must not be silently replaced by a new event chain.
- Confirm cluster member arrays stay parallel across member id, role, chance, minimum tier, and danger fields.
- Confirm scoped on-action additions do not introduce unscoped world iteration and are idempotent across existing saves.
- Confirm achievement definitions, triplet GFX/localisation, tracking flags, and disqualifiers are all present before adding workbook rows.
- After workbook changes, run `python .tools/export_event_catalog_csv.py` from the mod root and inspect the three generated export snapshots without editing them directly.
- For any event-chain source change, use the narrow `hoi4.event_inspect` and `hoi4.event_render` routes again. For any weighted AI/MTTH/random/selection change, begin with `hoi4.probability_inspect`, route the detailed pass through `chaosx_ai_probability_auditor`, and use same-scenario `hoi4.probability_compare` after the owner patch.

## Risks and blockers

### Confirmed blockers

- The exact source files for Deaths reason constants/localisation/view arrays, Air Cleanliness public adapters, Condemnation source records, occupation-law/camp/gulag/genocide/forced-labor adapters, achievement GFX/localisation, and the active scoped on-action registry were not independently resolved before the parent requested report writing. Do not infer filenames. Parent should run narrow symbol searches for the named contracts and record the actual owners.
- `chaosx.nr149.*` is absent from the bounded event-source search. The parent needs an explicit retire, disable, or convert-to-adapter decision before implementation.
- Events 118, 120, and 131 have no `chaosx.nr118.1`, `chaosx.nr120.1`, or `chaosx.nr131.1` source hits in `events/`. Event 120's volcano content appears under Event 013 localisation (`localisation/english/013_natural_disasters_l_english.yml`, `chaosx.nr13.116.t`), so the matrix labels cannot be treated as source event ids without reconciliation.
- The installed `chaosx_ai_probability_auditor` route is not callable in this runtime. The existing direct `hoi4.probability_inspect` artifact is evidence only, not an auditor pass or balance conclusion.
- The installed Event Chain Viewer has a large-workspace projection limit. A bounded Event 005 request still scanned 9,513 events and returned `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL`; helper/lifecycle validation remains unresolved.

### Ordinary risks

- Death reasons can be double-counted when famine is recorded alongside nuclear, fallout, bombing, displacement, camp, outbreak, or disaster context. Keep physical reason and responsibility/evidence separate.
- Public adapters that accept a state without exact controller/owner/actor proof can leak pressure or responsibility to invalid targets.
- New whole-world on-actions would create a performance regression. Prefer existing CXT/scoped hooks and explicit state lists.
- Event 006, Event 020, Fallout, and cluster settings already have large helper graphs. Avoid adding a second queue, cooldown, or pacing source.
- Event Details and workbook wording must remain premise-focused and synchronized with localisation. The workbook is not a source for gameplay identifiers.

## MCP evidence and unresolved analysis

- Fresh read-only Event 005 inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdd639bcb5c06669a0b071538e94326fa080df638e2e79b0b046259981efecc0/d7d9356ab8e8c01ba022b26fa0f7885dad99b56e973206c16768873b024d25bf/event-lint-f571ec78c744.json`. Result: `EVENT_INSPECTED_PARTIAL`, workspace `mod_chaos_redux_ea3b2d67c2c0`, no blockers, zero blocking diagnostics, helper/lifecycle projection deferred.
- Fresh read-only Event 005 overview render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ce79eb38b5b93de5e5ab1390476c43cd26a0ebc8e9e10810e15f4a7cc83c793/f89d0c3028274da1a6e10f757ac2293a03231f47f05a66bebef2bdfa3f35e76c/event-overview-f571ec78c744-manifest.json`. Result: `EVENT_RENDERED_PARTIAL`; selected nodes 2, omitted nodes 41,202, validation false only because large-workspace analysis was deferred.
- Existing roots 1–20 structural artifact index: `docs/plans/repo_cleanup/subagent_handoffs/shared_helper_architecture_baseline_2026-08-22.md`. It records one `hoi4.event_inspect` artifact for each root, with the same `MCP_INLINE_FILES_TRUNCATED` and deferred-helper limitations. Reuse those artifacts instead of repeating workspace scans.
- Existing shared Event Log GUI inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/922e791efa3e7f79b89c8554be19b5da743f0abcb4dcbe4dcbf285f8a420b805/453308075164395336e7c4c3de561b72fba8007710d9826e1f0e617edc436376/gui-inspect.1391d8530b419297.json`. It inspected `events_log_popup_window`; layout diagnostics were truncated and no coordinate conclusion is claimed.
- Existing weighted-source inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3a7bed6e8e3d5e23416794b68e928d4a3c14aaecba41d8618761acbcdfc7e8e/d28276c76aee90b542dc05f97871aa4c06fc2f676a36f690d1d545757b012bf2/probability-inspect-6d5d6adb4e5b.json`. It inspected `common/scripted_effects/chaosx_logic_effects.txt`, found zero custom-pool candidates, and does not justify a balance claim. The required `chaosx_ai_probability_auditor` route is unavailable.

## Recommended next action

Before implementation, resolve the seven unconfirmed owner-local seams with narrow symbol searches and make a one-line source-of-truth decision for Event 149 and the absent 118/120/131 ids. Then implement the shared population/death-reason contract and its documentation first, using the existing exact-loss helpers and preserving the MCP limitations above.
