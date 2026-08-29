# Famine and migration separation architecture handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: read-only architecture audit, 25 August 2026.

Scope: separate the famine and migration mechanics while preserving their explicit causal seams, exactly two mapmodes, sparse scheduling, exact civilian accounting, and existing player-facing intent.

This handoff is the implementation plan for the owner and final auditor. No gameplay, localisation, asset, workbook, specification, or existing handoff file was edited by this audit, and no commit was created.

## Binding verdict

Famine and migration are two mechanics, not two views of one mechanic.

The final implementation must contain zero `famine_migration_*` identifiers in gameplay, UI, localisation, sprites, variables, flags, effects, triggers, or mapmode definitions.

Famine-owned identifiers must use `famine_*`, migration-owned identifiers must use `migration_*`, and genuinely low-level shared primitives must use neutral names such as `civilian_transfer_*`, `state_population_*`, `humanitarian_*`, or `sparse_scheduler_*`.

The final implementation has exactly two dedicated mapmodes, `famine_state_map_mode` and `migration_state_map_mode`.

Both mapmode buttons remain visible from campaign start because they are static map UI consumers; each mapmode renders a neutral or untracked result until its own mechanic has an exact state fact.

There must be two separate decision categories, two separate reveal/retire lifecycles, two separate registries, two separate job families, two separate cleanup owners, two separate player metric sets, and two separate causal fact namespaces.

There must be no united decision category, combined report header, third mapmode, full replacement GUI, or recurring world scan.

The present source is not in that state. The owner must treat this handoff as a broad namespace and ownership split, not as a cosmetic rename.

## Evidence and required references

Before source inspection I read `AGENTS.md`, the complete `chaos-redux-state-ledgers`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` skills.

I read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, map modding, interface modding, and scripted GUI modding.

I read the applicable vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, and `script_math_functions.md`.

The read-only MCP evidence is as follows.

| Surface | Evidence | Limit |
| --- | --- | --- |
| Weighted mission surface | `hoi4.probability_inspect` source artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3556a0b0fd901bbe286798c325a259de78d653764644b5135021ca20cc3ec773/eaa82fd52c0c55243217f1bfc234979ded320d20c7b3b65eff0c1cc5e40af402/probability-inspect-2e2d4e39c5ac.json` and mission inspection artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0da670cee3e121cacb804b7168819e636547456231d93d68951e342c8cb5f3a7/5f798721a06340cbd8de8a43660feb87fc34928401af5c8ec5fbfd10308c3602/probability-inspect-2e2d4e39c5ac.json` | The candidate pool was incomplete (`poolComplete=false`, 17 unresolved inputs), and the required `chaosx_ai_probability_auditor` route is not callable in the current tool set, so no probability evidence pass or compare is claimed. |
| Map substrate | `hoi4.map_inspect` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd9a242ab535978d44c70e64bc11e861bf698615740fa828c85846b93ea9b6a1/d278dbbc5cfbc04627f82f30352a779d7f6afd4523b10b397355ac604ae7439c/map-inspect.3d4633a269b9efa3.json` | The map substrate was inspected, but diagnostics were truncated after 2,654 unrelated building/port position errors. This does not prove mapmode colour or tooltip execution. |
| Decision GUI surface | `hoi4.gui_inspect` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8976479bf5d13ab64d0d39987a38128d8a9eff2cb6bf7ed3e18c52abe54a6501/5d5df9e2065d8ac2052ccfd371d1cc44f1ab36fd4c2ed012f07ea3cc46bdfc6d/gui-inspect.17b1271f552d4366.json` | The decision window returned zero modelled elements, 2,000 graph diagnostics, and no proof of category header runtime. A full GUI rewrite is out of scope. |
| Event surfaces | Prior event-inspect and lint evidence is recorded in `event_boundary_adapter_final_audit.md` and `scripted_system_architect.md` | Several narrow event routes were partial, while broad decision/event inspection timed out. The owner must retain these blockers rather than treating source-only inspection as engine evidence. |

The current source facts below are based on direct inspection and the preceding handoffs in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/`, especially `completion_final_audit.md`, `decision_mission_final_audit.md`, `two_mapmode_owner_patch.md`, `presentation_integration_architecture.md`, `final_cohort_selection_architecture.md`, and `adapter_wiring_closure.md`.

## Current ownership audit

### Famine-owned surfaces

Famine owns all state food inputs and outputs, including the food-security formula, component contributions, pressure accumulation and decay, food stage transitions, exposure, reserve capacity and reserve transactions, blockade proof and blockade components, relief access and food relief, famine-specific incidents and reports, famine mortality, and the `Deaths` reason for famine.

The famine state machine is the only writer of food stage, food pressure, food reserves, food exposure, blockade proof, famine recovery proof, famine relief donor state, and famine mortality totals.

Famine mortality must remain an exact physical civilian-population loss owned by famine. The shared population primitive may apply the loss and the shared `Deaths` API may record it, but migration must not re-apply the same loss or reinterpret famine mortality as route death.

The current source evidence is in `common/scripted_effects/chaosx_famine_migration_effects.txt` around `famine_migration_initialize_food_state` (the food initializer begins near line 3507), `famine_migration_evaluate_food_security` (near line 4566), the food-reserve effects (near lines 4762–5150), and `famine_migration_apply_famine_mortality` (near line 5152).

Famine owns its own sparse state registry and jobs: active food-state registration, food reassessment, food evaluation, stage transition, reserves, blockade proof refresh, relief-donor processing, famine modifier refresh, famine report selection, famine category reveal, and famine retirement.

Famine decisions are the food and relief actions: release or import reserves, repair or escort relief, emergency airlift, invite relief, conceal the crisis, maintain extraction, and requisition a safer state.

Famine missions are `deliver relief before reserves fail` and `secure relief route`.

The evacuation decision is not famine-owned merely because famine can cause it. The movement transaction, cohort ledger, route deaths, reception, and return remain migration-owned.

### Migration-owned surfaces

Migration owns displaced cohorts, cohort identity, current host, origin and host history, transfer transactions, route deaths, displacement and flight obligations, trapped state, departure and reception border policies, corridors, reception load and capacity, shelter and medical services, integration, resettlement, transit, return, destination selection, migration relief, migration category reports, migration achievements, and migration-specific decisions and missions.

The migration state machine is the only writer of cohort ledger rows, current host, history rows, route/departure result, route deaths, flight population, trapped population, reception load, capacity, border posture, corridor status, integration, resettlement, and return projections.

The current source evidence is in `common/scripted_effects/chaosx_famine_migration_effects.txt` around the cohort and transfer effects (near lines 82–2865), the border/reception/return effects (near lines 2365–2908), migration selection and load effects (near lines 3163–3469), and migration request effects (near lines 5629–5778).

Migration owns its own sparse state and country registries and jobs: active displacement states, active migration countries, reception candidate states, cohort selection and transfer processing, reception/capacity processing, route cleanup, migration country retirement, migration category reveal, migration reports, and migration achievements.

Migration decisions are preparation and movement actions: prepare evacuation, famine evacuation, evacuate vulnerable people, evacuate workers, negotiate or accept or reject a corridor, close or restrict or open departure routes, enforce closure, open or control reception, transit-only reception, distribute arrivals, local integration, third-country resettlement, voluntary return, and forced repatriation.

Migration missions are `hold humanitarian corridor`, `prepare safe return route`, `prevent reception collapse`, and `protect evacuation transport`.

`fm_famine_evacuation` is migration-owned despite its famine trigger because its effect is a civilian movement request. The famine category may expose a link or a causal explanation, but it must not own the movement transaction.

### Shared infrastructure that may remain shared

Only the following may remain shared, and each must have a neutral namespace and no mechanic-specific state hidden inside it.

| Shared primitive | Allowed contract | Forbidden use |
| --- | --- | --- |
| State population | Read the exact state population primitive and invoke one exact civilian transfer/loss primitive with explicit owner, source, amount, and result. | A shared helper may not decide whether a population change is famine or migration, and it may not write either mechanic's ledger. |
| `Deaths` API | Record famine mortality under a famine reason and route or coercive movement deaths under separate migration reasons. | One generic death counter or one shared cause flag that makes famine deaths appear as migration route deaths. |
| Sparse scheduler shell | A host-owned shell may iterate registered arrays and dispatch independent famine and migration jobs. | A food job may not reconcile or clean cohorts, and a migration job may not initialize or retire food state. |
| Script constants | Neutral population units, result codes, schema revisions, scheduler cadence, and shared lower-level bounds may be global constants. | Food-stage thresholds, reserve bands, border policy, reception capacity, and movement tuning may not share a combined table. |
| Mapmode engine and static buttons | The engine can expose two static buttons and invoke two independent mapmode definitions. | A combined mapmode, dynamic button hiding, a shared color resolver, or a third mapmode is not allowed. |
| Compatibility result envelopes | A neutral result can carry success, failure, amount, generation, and revision. | The result may not carry both food and flight mutations through one generic pressure request. |
| Coordination wrapper | An optional neutral coordinator can dispatch owner-local refreshes in a fixed order. | It may not broad-clear both owners, own flags, or infer one mechanic's state from the other. |

## Concrete coupling defects in the current source

The following are confirmed source defects, not hypothetical risks.

| Defect | Evidence | Required ownership correction |
| --- | --- | --- |
| Migration-only organized evacuation sets food pressure | `famine_migration_request_organized_evacuation` in `chaosx_famine_migration_effects.txt` sets both `famine_migration_pressure_request_apply_food = 1` and `famine_migration_pressure_request_apply_flight = 1` around lines 5696–5758. | The migration evacuation must submit only a migration flight request. If an evacuation causes food pressure, it must call a separately proven migration-to-famine adapter with its own amount, cause, generation, and receipt. |
| Food initializer creates migration ledgers | `famine_migration_initialize_food_state` writes `famine_migration_state_reception_load`, `state_resettled_population`, `state_returned_population`, `state_flight_population`, and `state_trapped_population` around lines 3491–3556. | Split `famine_initialize_food_state` from `migration_initialize_state`. A famine initializer may only initialize famine variables and shared population identity; a migration initializer owns migration ledgers. |
| Famine exposure reveals migration category | `famine_migration_refresh_decision_phase_from_state` near lines 1136–1160 registers a migration country when food exposure or famine incidents pass thresholds. | Famine reveal writes only famine category state. Migration reveal requires a positive cohort, flight, trapped, corridor, reception, or other migration obligation. |
| Generic pressure API has cross-owner defaults | `famine_migration_apply_pressure_request` near lines 1165–1213 defaults `apply_food = 1`, optionally applies flight, and initializes food before processing a request. | Delete the merged request API. Create separate famine pressure effects and migration movement/demand effects; external callers select one or two explicit owner adapters. |
| Food job calls migration selection and cleanup | `famine_migration_process_registered_food_state` near lines 5332–5361 calls `famine_migration_reconcile_state_cohort_selection`, and its inactive branch calls `famine_migration_cleanup_cohort_records_for_state`. | Food processing may call famine cleanup only. Migration obligations are never reconciled or deleted by famine retirement. |
| Migration job calls a combined state reconciliation and broad cleanup | `famine_migration_process_registered_displacement_state` near lines 5363–5385 calls the same combined selection and cohort cleanup path and then broad state cleanup. | Migration processing uses migration selection, transfer, reception, and migration cleanup only. A named adapter may publish a famine demand, but the migration job does not mutate famine state. |
| Migration country retirement depends on famine state | `famine_migration_process_registered_displacement_country` near lines 5387–5436 uses `any_owned_state` OR food-active OR displacement-active conditions before retiring a migration country. | Migration retirement is based only on migration obligations and migration durable memory. Famine retirement is a separate country/state lifecycle. |
| One cleanup clears both mechanics | `famine_migration_cleanup_state_registration` near lines 3026–3103 clears famine state, migration obligations, migration contexts, flight/trapped variables, and food components. | Replace with `famine_cleanup_state_registration` and `migration_cleanup_state_registration`, each proving its own retirement conditions and clearing only its own facts. |
| One dynamic modifier clear removes both owner sets | `famine_migration_clear_dynamic_modifiers` and `famine_migration_refresh_dynamic_modifiers` near lines 2939–3021 clear famine stage modifiers and migration flow modifiers in one helper. | Split modifier files and owner-local clear/refresh effects. A neutral coordinator may invoke both narrow clears but may not own either modifier set. |
| One report scene clear crosses ownership | `famine_migration_clear_report_scene` in `famine_migration_report_effects.txt` clears famine, blockade, wartime evacuation, border, relief arrival, nuclear evacuation, and return flags around lines 10–18. | Famine report selection clears only famine/blockade/food-relief scene flags. Migration report selection clears only evacuation/border/reception/return scene flags. Nuclear or relief events emit two independent reports only when both contracts are proven. |
| Migration selection reads raw famine state | `famine_migration_spontaneous_movement_effects.txt` and destination selection in the main effect file read `famine_migration_food_pressure` or initialize food state while scoring destinations. | Famine publishes a destination food-safety adapter. Migration consumes the proven adapter and never initializes or reads raw famine pressure in a migration decision. |
| Capacity reads raw famine stage | `famine_migration_capacity_effects.txt` derives reception food quality from food-stage fields. | Famine publishes a versioned food-safety quality fact; migration reception capacity consumes that fact as an optional input with fail-closed defaults. |
| Famine evaluator reads raw migration trapped population | `famine_migration_evaluate_food_security` around lines 4578–4596 reads `famine_migration_trapped_population` directly into famine need pressure. | Migration publishes `migration_to_famine_reception_demand` with proof and generation. Famine consumes only that adapter output. |
| Border policy is one mixed metric | `famine_migration_border_policy` and its flags are used by departure, reception, and mapmode logic. | Split `migration_departure_policy` and `migration_reception_policy`, with independent validation and player-facing localisation. |
| Registries and counters have a combined namespace | `famine_migration_active_food_states`, `active_displacement_states`, `active_displacement_countries`, and one combined mission count are initialized together near lines 11–64 and processed from one runtime. | Keep separate famine and migration arrays, counts, mission slots, and registration effects. The scheduler shell may dispatch them independently. |
| Cohort cleanup is callable from famine paths | `famine_migration_cleanup_cohort_records_for_state` near lines 547–554 is reachable from the food processor and broad state cleanup. | Cohort cleanup is migration-only and must only run after migration owner checks current host, generation, identity, and durable outcome. |
| Achievements are reconciled through combined lifecycle | Migration cohort achievement reconciliation and famine/blockade achievement recording are reached from shared processors and cleanup. | Famine achievements (stage, blockade, reserves, famine recovery, famine mortality) and migration achievements (cohort, corridor, reception, return, transfer) have independent initialization, progression, retirement, and durable history. |
| Category, phase, and reports use one fallback chain | `famine_migration_categories.txt` and `famine_migration_scripted_localisation.txt` combine food exposure with flight, trapped, reception, and border phases. | Split category IDs, phase selectors, response metrics, report headers, and localisation selectors. No cross-owner fallback is permitted. |
| Combined scripted GUI header is presented as one mechanic | The shared category references `famine_migration_report_header_scripted_gui`. | Remove the united header. Ordinary category dynamic localisation is sufficient; any future narrow owner GUI requires a separate approved scope and MCP inspection. |
| `fm_` decisions and missions have no owner namespace | All current decisions and missions live under one category and use the ambiguous `fm_` prefix. | Rename each decision and mission to `famine_*` or `migration_*` according to the ownership census below. |
| Current files and identifiers describe one system | `chaosx_famine_migration_effects.txt`, `famine_migration_*` variables, flags, effects, modifiers, reports, and localisation are shared by naming even where behavior is partly separate. | Split files and perform a token-level owner rename. A shared file may not preserve the old prefix merely for convenience. |

## Causal seams and API contracts

The two mechanics may connect only through explicit, versioned, one-way adapter facts. An adapter is not permission for one mechanic to write the other's ledger.

### Famine to migration survivor displacement

When famine stage transition or famine mortality proves that survivors must leave, famine computes the positive survivor displacement request from the famine-owned population and protected floor.

Famine then calls a migration-owned request with `source_state`, `owner_country`, `amount_people`, `cause = famine_survivor_displacement`, `famine_stage`, `famine_generation`, `protected_floor`, `request_id`, and `proof = famine_survivor_displacement_proven`.

The migration owner validates state ownership, amount, generation, current population, and idempotence, then creates or updates the migration flight/cohort obligation. Only migration writes flight population, cohort rows, current host, route state, and later transfer outcomes.

The adapter must not write a migration ledger from a famine initializer, and it must not apply a second civilian population loss. Famine mortality and survivor displacement are separate facts with separate amounts and causes.

The existing `famine_migration_submit_survivor_flight_request` near lines 4368–4432 is the correct conceptual seam but is currently an owner-mixed implementation. It must become a famine publisher plus migration request consumer.

### Migration to famine reception and demand

Migration owns reception load, trapped population, capacity, shelter, medical service, and arrival demand.

After a migration owner update, it may publish `migration_to_famine_reception_demand` with `destination_state`, `owner_country`, `amount_people`, `demand_kind`, `migration_generation`, `migration_revision`, `proof = migration_reception_demand_proven`, and an expiry or consumed revision.

Famine may consume the demand as one named need component. Famine must not read `migration_trapped_population`, `migration_reception_load`, or any cohort row directly.

No demand is published when migration has no positive obligation, the state identity is stale, or capacity/reception proof is absent.

### Migration route disruption to famine

Migration owns corridor, route, departure, transfer, and reception disruption.

Migration may publish `migration_to_famine_route_disruption` with `source_state`, `destination_state` where applicable, `owner_country`, `amount_or_pressure`, `cause`, `migration_generation`, `route_revision`, and `proof = migration_route_disruption_proven`.

Famine consumes the adapter only as an external transport or relief-access component. It does not infer route disruption from a generic `route_unsafe` or `route_damaged` token, because those tokens are currently dead or ambiguous in the source.

### Famine to migration destination safety and reception quality

Famine owns food safety and relief access.

Famine may publish `famine_to_migration_destination_food_safety` with `state`, `food_stage`, `quality_value`, `food_generation`, `food_revision`, and `proof = famine_destination_food_safety_proven`.

Migration destination selection and reception capacity may consume this fact as one input. They must not initialize famine state or read raw food pressure, food stage, or food reserve variables.

### External adapters

Air cleanliness, condemnation, camps, genocide, occupation, chemical, biological, nuclear, bombing, natural disasters, war/peace, and event-specific callers must call either a famine owner API, a migration owner API, or two independent APIs.

When two mechanics are affected, each call carries its own `state`, `owner`, `amount`, `cause`, `generation`, `revision`, and proof receipt. One generic pressure request is forbidden.

Event 149 `Immigrations` remains retired or disabled; it must not be revived as a flat global drain. Event adapters must remain bounded to the event scope and registered state/country, not a world scan.

## Decision categories, player metrics, and lifecycle

### Famine category

The implementation target is `famine_category` in a dedicated category file.

The category is hidden when the country has no famine-owned active state, famine pressure, reserve failure, blockade proof, exposure, or durable famine response memory.

The category reveals only when famine registration or an explicit famine action creates a positive famine fact. It must not inspect migration flags, cohorts, flight, trapped population, reception load, or border policy.

The primary player metric is Food Security with stage and score. Supporting metrics are Reserves, Exposure, Blockade/Relief Access, and Famine Mortality where a report needs it.

The category owns the famine decisions and missions listed in the famine audit above.

Famine retirement clears only famine decision phase, famine category-active state, famine modifiers, famine reports, and famine registry entries after food recovery and relief obligations are proven complete. It preserves famine history, achievements, and any migration obligation created by a survivor adapter.

### Migration category

The implementation target is `migration_category` in a dedicated category file.

The category is hidden when the country has no migration-owned cohort, flight, trapped, reception, corridor, departure, return, or resettlement obligation or durable migration response memory.

The category reveals only when migration registration or a migration-owned action creates a positive migration fact. Famine exposure alone does not reveal it.

The primary player metric is Displacement Load. Supporting metrics are Reception Capacity/Load, Border Departure Policy, Border Reception Policy, Corridor State, and Return/Integration status.

The category owns the migration decisions and missions listed in the migration audit above.

Migration retirement clears only migration category-active state, migration decisions/missions, migration modifiers, migration reports, migration registry entries, and completed cohort working rows after current-host and durable-outcome proofs succeed. It preserves migration history and achievements and does not clear famine facts.

### Reveal and retire state contract

Use separate country flags and sparse arrays such as `famine_category_revealed`, `famine_category_active`, `migration_category_revealed`, and `migration_category_active`.

Use owner-local dormant or durable-memory flags if the player must retain a history/report action after the active problem resolves, but never make a dormant migration flag satisfy a famine reveal trigger or vice versa.

The existing shared category's `visible_when_empty = no` behavior can be retained independently in both categories, but each category's `visible` trigger must be owner-local.

Mapmode buttons are an explicit exception to category visibility: both mapmode buttons stay visible from campaign start and display neutral/untracked output until their own producer facts exist.

## Exact two mapmodes

Keep exactly `famine_state_map_mode` and `migration_state_map_mode` in the mapmode registry.

`famine_state_map_mode` consumes only famine stage, food score/pressure, reserve state, exposure, blockade proof, famine relief access, and famine-owned safety facts.

`migration_state_map_mode` consumes only migration cohorts, current-host projections, displacement status, flight, trapped, reception load/capacity, departure/reception policy, corridors, transit, return, integration, resettlement, and migration relief.

If migration needs food quality for reception or route choice, it consumes the versioned famine-to-migration adapter and renders a migration-owned result. It must not read raw food stage or food pressure.

If famine needs migration demand for its food formula, it consumes the versioned migration-to-famine adapter and renders a famine-owned result. It must not read raw trapped or reception ledgers.

The existing mapmode definitions in `common/map_modes/chaosx_state_map_modes.txt` are conceptually two modes, but the file and shared presentation identifiers still use the old namespace and must be split or renamed.

Keep the four existing static mapmode button consumers and their approved assets. Rename sprite and localisation identifiers to owner-neutral or owner-specific names as part of the namespace pass; do not add a third button or full GUI.

The dynamic mapmode colour/tooltips/click paths were not fully executable in the available MCP run, so the owner must perform the final source and engine audit after renaming.

## Exhaustive namespace and ownership routing matrix

The old prefix is evidence of the current source only. It must not survive the final implementation. The rule for any token not covered below is to stop the rename and assign an owner before editing it.

| Current family or file | Final owner | Final namespace/file route | Notes |
| --- | --- | --- | --- |
| `famine_migration_initialize_runtime`, active food arrays, food counts, food registration, food reassessment, food processors | Famine plus neutral shell | `famine_initialize_runtime`, `famine_active_food_states`, `famine_process_registered_state` in famine effect files; neutral scheduler dispatch in `sparse_scheduler_*` | The runtime shell may initialize both independent registries, but it must not own their data. |
| `famine_migration_initialize_migration_state`, active displacement arrays/counts/country registration, displacement processors | Migration | `migration_initialize_state`, `migration_active_displacement_states`, `migration_active_countries`, `migration_process_registered_state/country` | No food initialization from this path. |
| `famine_migration_record_displaced_cohort`, save/rebind/resolve/cleanup cohort effects | Migration | `migration_record_cohort`, `migration_save_previous_host`, `migration_bind_destination`, `migration_resolve_origin`, `migration_cleanup_cohort` | Cohort identity, current host, history, and cleanup are migration-only. |
| `famine_migration_cleanup_cohort_records_for_state`, `famine_migration_abort_staged_cohort_record`, full cohort invalidation | Migration | `migration_cleanup_cohort_records_for_state`, `migration_abort_staged_cohort`, `migration_invalidate_state` | Call sites must be migration owner checks only. |
| Historical profile candidates, anchors, memory, profile selection, and context | Famine | `famine_historical_*` in famine effect files | Historical famine context must not open migration category or write migration ledgers. |
| `famine_migration_apply_pressure_request` and `pressure_request_apply_food/apply_flight` | No final shared owner | Delete merged API; route to `famine_request_*` or `migration_request_*` | The two booleans are a direct merged-mechanics defect. |
| `famine_migration_request_famine_pressure`, food security, occupation, camp, gulag, forced labor, bombing, nuclear, fallout, outbreak, disaster, war, peace, event, air cleanliness, chemical aftermath, biological warfare, cluster, scenario, blockade pressure | Famine for food contribution, or explicit external adapter | `famine_request_*_pressure` for food inputs; `famine_to_*` or `*_to_famine` adapters for external causes | A source that also creates movement must make a second migration call with a separate proof. |
| `famine_migration_request_flight_pressure`, displacement pressure, cross-border flight, organised evacuation, deportation flow, internal displacement | Migration | `migration_request_flight`, `migration_request_displacement`, `migration_request_cross_border_flight`, `migration_request_organized_evacuation`, `migration_request_deportation`, `migration_request_internal_displacement` | These write migration requests only. |
| Blockade candidates, proof, components, duration, exposure, reserve and route proof | Famine | `famine_blockade_*` | Route disruption consumed from migration must be an adapter, not a shared blockade flag. |
| Relief access components and donor registration | Famine for food relief; migration for reception relief | `famine_relief_*` and `migration_relief_*` | Split relief proof and scene flags even when one event supplies both. |
| Exact transfer preflight, host proof, civilian transfer, destination credit, residual restoration, finalization, transaction | Neutral primitive with migration caller | `civilian_transfer_*` for physical primitive; `migration_*` wrappers for cohort/route semantics | The primitive accepts explicit source/destination/amount/result and does not own cohorts or food. |
| Border policy and border request/result/flags | Migration | `migration_departure_policy_*` and `migration_reception_policy_*` | One legacy `border_policy` variable cannot remain. |
| Trapped, reception, capacity, shelter, medical, overcrowded, transit, integration, resettlement, return | Migration | `migration_trapped_*`, `migration_reception_*`, `migration_capacity_*`, `migration_integration_*`, `migration_resettlement_*`, `migration_return_*` | These are migration player metrics and ledgers. |
| `famine_migration_clear_dynamic_modifiers`, state modifier refresh, route cleanup | Owner-local | `famine_clear_dynamic_modifiers`, `migration_clear_dynamic_modifiers`, and owner-local refresh files | A coordinator may call both narrow effects in a documented order. |
| `famine_migration_clear_food_dynamic_modifiers` | Famine | `famine_clear_food_dynamic_modifiers` | Keep only famine stage modifiers. |
| `famine_migration_cleanup_state_registration` | Split | `famine_cleanup_state_registration` and `migration_cleanup_state_registration` | Each proves its own state retirement and clears only its own variables/flags. |
| `famine_migration_cleanup_country_registration` | Migration plus separate famine country cleanup | `migration_cleanup_country_registration` and `famine_cleanup_country_registration` | Corridor/cohort/mission cleanup remains migration; famine donor/history cleanup remains famine. |
| `famine_migration_reconcile_state_cohort_selection`, country selection, displacement load, cohort achievement | Migration | `migration_reconcile_state_cohort_selection`, `migration_reconcile_country_cohort_selection`, `migration_refresh_displacement_load`, `migration_reconcile_cohort_achievement` | Remove every call from famine jobs. |
| `famine_migration_initialize_food_state`, surface context, food evaluation, stage transition, reserve effects, famine mortality | Famine | `famine_initialize_food_state`, `famine_submit_surface_context`, `famine_evaluate_food_security`, `famine_transition_food_stage`, `famine_*_reserve`, `famine_apply_mortality` | The initializer must not set migration ledgers. |
| `state_reception_load`, `state_resettled_population`, `state_returned_population`, `state_flight_population`, `state_trapped_population` currently set by the food initializer | Migration | `migration_state_reception_load`, `migration_state_resettled_population`, `migration_state_returned_population`, `migration_state_flight_population`, `migration_state_trapped_population` initialized only by migration | The rename alone is insufficient; the writer must move. |
| Survivor flight request | Famine publisher plus migration consumer | `famine_publish_survivor_displacement` and `migration_accept_famine_survivor_request` | The seam is explicit and one-way. |
| Raw trapped/reception demand consumed by famine | Migration publisher plus famine consumer | `migration_publish_reception_demand` and `famine_consume_migration_reception_demand` | Include generation, revision, amount, cause, and proof. |
| Raw route disruption consumed by famine | Migration publisher plus famine consumer | `migration_publish_route_disruption` and `famine_consume_migration_route_disruption` | Fail closed if proof is stale. |
| Raw food safety consumed by migration | Famine publisher plus migration consumer | `famine_publish_destination_food_safety` and `migration_consume_famine_food_safety` | Never initialize food from migration selection. |
| `famine_migration_process_registered_runtime` | Neutral scheduler shell | `sparse_scheduler_process_registered_runtime` | It may dispatch two loops, but it must not perform owner logic or broad cleanup. |
| State control, annex, war, peace, invasion, paradrop, nuclear, and wartime candidate callbacks | Each owner plus neutral callback envelope | `famine_handle_*`, `migration_handle_*`, or `humanitarian_*` callback with explicit owner calls | Existing bounded callback scopes may remain; do not add recurring every-world iteration. |
| `famine_migration_report_*` effects and scene flags | Split | `famine_report_*` and `migration_report_*` files and flags | Famine report clearing must not clear evacuation, border, or return reports. |
| `famine_migration_state_*` dynamic modifiers | Split | `famine_state_supply_strain`, `famine_state_acute_shortage`, `famine_state_famine`, `famine_state_catastrophic`; `migration_state_preparing_to_leave`, `migration_state_exodus`, `migration_state_reception`, etc. | Preserve the two existing modifier families, but remove the old prefix and broad clear. |
| `famine_migration_categories.txt` and `chaosx_famine_migration_category` | Split | `famine_category` and `migration_category` in separate category files | No compatibility category with the old united title. |
| `fm_*` famine decisions | Famine | Rename to `famine_*`: `famine_release_reserves`, `famine_emergency_imports`, `famine_repair_relief_route`, `famine_escorted_relief_convoy`, `famine_emergency_airlift`, `famine_invite_relief`, `famine_conceal_crisis`, `famine_maintain_extraction`, `famine_requisition_safer_state` | Keep triggers/effects owner-local. |
| `fm_*` famine missions | Famine | `famine_mission_deliver_relief_before_reserves_fail`, `famine_mission_secure_relief_route` | Separate mission slot flags and retirement. |
| `fm_*` movement and border decisions | Migration | Rename to `migration_prepare_evacuation`, `migration_famine_evacuation`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, `migration_negotiate_corridor`, `migration_accept_corridor_offer`, `migration_reject_corridor_offer`, `migration_close_border`, `migration_restrict_departure`, `migration_open_departure_routes`, `migration_enforce_closure`, `migration_controlled_medical_reception`, `migration_open_reception`, `migration_transit_only`, `migration_distribute_arrivals`, `migration_local_integration`, `migration_third_country_resettlement`, `migration_voluntary_return`, and `migration_forced_repatriation` | `migration_famine_evacuation` retains famine as cause in localisation, not ownership. |
| `fm_*` migration missions | Migration | `migration_mission_hold_humanitarian_corridor`, `migration_mission_prepare_safe_return_route`, `migration_mission_prevent_reception_collapse`, `migration_mission_protect_evacuation_transport` | No mission completion/retirement flag may clear a famine mission. |
| Combined scripted localisation and category phase selectors | Split | `famine_scripted_localisation.txt` and `migration_scripted_localisation.txt` | No food-to-displacement fallback chain or mixed primary metric. |
| `famine_migration_report_header_scripted_gui` | None in this scope | Remove the united header; use category localisation. | A future narrow GUI would need a separately named owner and a fresh MCP inspect/render/review. |
| `famine_state_map_mode` and `migration_state_map_mode` | Famine and migration respectively | Keep exactly these two identifiers in owner-specific mapmode files | Mapmode engine registration is shared infrastructure; color/tooltip consumers are not. |
| `GFX_fm_*`, `fm_*` mapmode localisation, and shared mapmode report tokens | Owner-specific UI | Rename to `GFX_famine_*` or `GFX_migration_*` and `famine_map_*`/`migration_map_*` | Existing static button assets may be reused, but identifier ownership must be explicit. |
| `famine_migration_achievement_*` | Famine or migration by evidence | Famine: blockade, extraction, reserves, famine recovery, famine mortality, famine relief; migration: cohort, arrival, corridor, reception, integration, return, transfer, displacement, forced/voluntary movement | No combined achievement initializer, counter, or retirement hook. Neutral campaign metadata may use `achievement_*` only if it is not mechanic state. |
| `famine_migration_*` adapter names in external event files | Explicit owner adapter | `famine_to_migration_*`, `migration_to_famine_*`, or `humanitarian_*` with explicit owner payload | The old prefix cannot be kept as a generic facade. |
| Any remaining `famine_migration_*` token discovered by final scan | Unassigned blocker | Stop and route manually before merge | The final scan must return zero in runtime source, UI, localisation, sprites, variables, flags, effects, triggers, mapmodes, decisions, and missions. |

The final namespace scan must cover `common/`, `events/`, `decisions/`, `interface/`, `localisation/`, `gfx/`, and any script-enumeration or achievement files that consume these identifiers.

## File and patch order

The owner should apply the split in this dependency order.

1. Resolve the design-source conflict first: older source specifications describe one shared humanitarian category, while the binding clarification requires two categories and zero old identifiers. Update the authoritative spec outside this handoff before implementation; this audit intentionally did not edit specs.

2. Freeze an ownership manifest containing every old identifier, its new owner, the target file, the call sites, and its retirement rule. A token without an owner is a blocker.

3. Extract neutral primitives first: `state_population_*`, `civilian_transfer_*`, separate Deaths reason constants, result envelopes, schema revisions, and the sparse scheduler shell. These primitives must have no famine or migration state writes.

4. Split and rename famine core files and calls: food initializer, food registry, formula, stage, reserves, blockade, famine relief, mortality, famine modifiers, famine reports, famine achievements, famine category, and famine mapmode. Remove all migration writes from the food initializer and food jobs.

5. Split and rename migration core files and calls: state initializer, cohort identity/history, current-host proof, exact transfer wrappers, route deaths, flight/trapped, reception/capacity, border policies, corridors, integration, resettlement, return, migration relief, migration modifiers, migration reports, migration achievements, migration category, and migration mapmode. Remove all food writes from migration jobs.

6. Replace the combined pressure request with owner-local request APIs. Migrate famine callers to `famine_request_*` and movement callers to `migration_request_*`. Delete the two `apply_food`/`apply_flight` fields rather than preserving them under a new file.

7. Install the four explicit causal seams with request/reply receipts and generation checks. Wire famine survivor displacement first, then migration reception demand and route disruption into famine, then famine food safety into migration selection/capacity.

8. Split decisions and missions into two categories and rename every `fm_*` identifier to its owner prefix. Separate mission counters, active slots, decision phase variables, category visibility, localisation, and retirement. Do not leave a hidden united category as a compatibility alias.

9. Split reports, scripted localisation, dynamic modifiers, mapmode localisation, static button names, sprite identifiers, and scripted GUI references. Remove the combined report header rather than creating a replacement full GUI.

10. Rewire external adapters and event callbacks one source at a time. Each callback must show which owner API it invokes and must not use a generic pressure facade.

11. Perform a literal old-token purge and source census. Run an exact search for `famine_migration_` and the ambiguous `fm_` ownership prefix across runtime files; review every match rather than assuming generated or documentation references are harmless. The implementation gate is zero old runtime tokens and zero unowned `fm_` decisions/missions.

12. Run owner-local syntax/static checks, exact transfer conservation checks, stale-host and generation checks, category visibility scenarios, mapmode neutral-state scenarios, and the required MCP re-inspections. The owner must not launch HOI4 or claim live validation from these checks.

## Compatibility and migration risks

The rename is not save-compatible by default. HOI4 does not provide a general variable-key enumeration and rename primitive, so a final source with zero `famine_migration_*` identifiers cannot itself retain a permanent alias for every old variable, flag, array, event target, decision ID, or modifier ID.

The owner must make an explicit release decision between a fresh-save requirement and a one-release external migration bridge. If an old-save bridge is approved, it must be a bounded, explicit inventory of known old tokens, copy only into new owner variables, verify generation and ownership, then clear the old token; it must be removed before the final zero-token gate. Do not leave a compatibility alias in the final implementation.

Old cohort rows are especially risky because current-host identity and generation may be stale. A migration bridge must reject a row that cannot prove origin, current host, owner, generation, status, and durable outcome, and must never let famine cleanup delete a migration row.

The current transfer architecture still carries prior P0 risks from `final_cohort_selection_architecture.md` and `completion_final_audit.md`: current-host assertions, state retirement proofs, paired flight ledgers, reception scope, capacity fallback, and route-death accounting require final owner validation. This separation plan does not declare those risks fixed.

The source specification conflict is a blocker until the specification owner records that two categories supersede the older shared-category wording. This handoff does not silently reconcile the specs.

The probability evidence pass is blocked because the required `chaosx_ai_probability_auditor` route is unavailable and the current mission candidate pool has unresolved inputs. No AI weight or mission score change should be accepted on this audit alone.

The GUI inspection returned no modelled decision elements and the map inspection proves substrate only. The owner must not claim a dynamic category header, clickable report view, or mapmode tooltip rewrite from those artifacts.

The map substrate includes unrelated diagnostics in `mod:map/buildings.txt`; those are recorded as an environment blocker and are not silently attributed to the separation patch.

## No-world-scan proof

The implementation must preserve the existing sparse model.

Registration happens at the producer's exact state or country scope, and registration is idempotent.

The host scheduler uses `is_global_host` and loops the separate famine and migration arrays. It must not introduce an `on_daily` or `on_weekly` action that iterates every country or every state.

State control, annexation, war, peace, invasion, paradrop, nuclear, and wartime candidate hooks may process the bounded states in the callback scope and update sparse registration. They must not perform a new whole-world census.

Category visibility checks country-local flags and `any_owned_state` for that country only. A mapmode's engine-side map iteration is presentation infrastructure, not a gameplay world scan, and it must not write state.

The final audit must show that every owner job has an array or exact callback input, every cleanup call has an owner-local retirement proof, and no new unbounded iterator was added.

## Completion checklist

The owner and final auditor should mark this architecture complete only when every item below has evidence.

- [ ] The authoritative specification records two connected mechanics, two independent decision categories, and zero final `famine_migration_*` identifiers.
- [ ] Every old identifier has an ownership manifest entry and a final `famine_*`, `migration_*`, or neutral shared replacement.
- [ ] No `famine_migration_*` token remains in runtime gameplay, UI, localisation, sprite, mapmode, decision, mission, trigger, effect, modifier, achievement, or variable/flag source.
- [ ] No unowned `fm_*` decision or mission remains.
- [ ] Famine formula, stages, reserves, exposure, blockade proof, relief, mortality, Deaths reason, famine registry, famine jobs, famine category, famine reports, famine decisions, famine missions, and famine mapmode are owner-local.
- [ ] Migration cohorts/current host/history, transfer transaction, route deaths, displacement, trapped, reception/capacity, departure/reception policy, integration, resettlement, return, migration registry, migration jobs, migration category, migration reports, migration decisions, migration missions, and migration mapmode are owner-local.
- [ ] The food initializer writes no migration ledger, and the migration initializer writes no famine ledger.
- [ ] Famine jobs never reconcile, select, invalidate, or clean migration cohorts.
- [ ] Migration jobs never initialize, evaluate, retire, or broad-clear famine state.
- [ ] Famine and migration registries, counts, active mission slots, category flags, phase variables, cleanup, retirement, and achievement hooks are independent.
- [ ] The combined `apply_food`/`apply_flight` pressure request and all generic merged pressure callers are removed.
- [ ] Famine survivor displacement is a one-way, generation-checked adapter into migration; famine does not write migration cohort or flight ledgers.
- [ ] Migration reception demand and route disruption reach famine only through proven, versioned adapter facts.
- [ ] Famine food safety reaches migration selection/capacity only through a proven, versioned adapter fact.
- [ ] Departure policy and reception policy are separate state facts and player metrics.
- [ ] Famine and migration report scene clearing, scripted localisation, dynamic modifiers, and sprite/localisation identifiers are separate.
- [ ] Famine and migration achievements cannot initialize, advance, retire, or disqualify each other.
- [ ] Exactly two mapmodes exist, both buttons remain visible from campaign start, both render neutral output without own facts, and no third mapmode or full GUI was added.
- [ ] Static mapmode button assets are reused or owner-renamed without adding a dynamic button-visibility dependency.
- [ ] Exact civilian transfer conservation, current-host proof, route-death accounting, protected floors, idempotence, and stale generation rejection are demonstrated for migration transactions.
- [ ] Famine mortality is applied once through the shared physical-population primitive and recorded under a famine Deaths reason; route deaths use separate migration reasons.
- [ ] Sparse registries and host scheduler loops are the only recurring processing mechanism; no recurring world scan was added.
- [ ] All external events and adapters have an owner matrix and independent proof payloads.
- [ ] Required source lint and focused MCP re-inspections are rerun after the rename; unavailable routes and truncated diagnostics are carried into the final report.
- [ ] Probability scenarios receive the required baseline and compare through `chaosx_ai_probability_auditor` once that route is available; until then, no weighted-surface completion claim is made.
- [ ] Old-save compatibility is explicitly decided, and any temporary bridge is removed before the final zero-token scan.

## Concise handoff verdict

The current package is a partially split implementation wrapped in a merged namespace and merged lifecycle, with three confirmed high-severity couplings: migration-only evacuation mutates food pressure, food initialization creates migration ledgers, and famine exposure reveals migration category.

The owner must split the package into famine and migration cores, route only the four explicit causal seams, rename every runtime token out of `famine_migration_*`, preserve exactly two always-visible mapmode buttons, and expose two independently hidden/revealed/retired decision categories.

Until the namespace purge, owner-local cleanup/jobs/registries, spec conflict resolution, old-save decision, and blocked MCP evidence are addressed, the separation is incomplete.
