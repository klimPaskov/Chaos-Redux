# Famine and Migration System

Status: This is the reconciled documentation ledger for the current source snapshot and is not a gameplay-completion claim.

## Scope and authority

The accepted design source is `docs/specs/famine_and_migration_system_specs/`, including its eight specification parts, matrices, routing notes, bibliography, closure, and documentation-curator prompt.

The reusable public-contract reference is `common/scripted_effects/chaosx_dynamic_effects.md`, while subsystem-private implementation is in `common/scripted_effects/chaosx_famine_migration_effects.txt` and `common/scripted_effects/famine_migration_adapter_effects.txt`.

The ordinary decision surface is in `common/decisions/famine_migration_decisions.txt` and `common/decisions/categories/famine_migration_categories.txt`.

The dedicated mapmode source is `common/map_modes/chaosx_state_map_modes.txt`, with presentation notes in `docs/systems/state_map_modes.md`.

The current implementation and handoff disposition ledger are recorded in `docs/plans/famine_and_migration_system_plans/handoff_dispositions.md` and `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md`.

Subagent handoffs remain evidence for parent review, not independent approval of gameplay behavior.

## Current-state ledger

| Surface | Current evidence | Documentation status | Remaining gate |
| --- | --- | --- | --- |
| Food-security evaluator | `famine_migration_evaluate_food_security` composes eight normalized inputs with centralized weights and hysteresis thresholds, and integrates the state-owned persistent food reserve ledger. | Source and public contract documented. | Parent gameplay and balance review remains required. |
| Famine mortality | `famine_migration_apply_famine_mortality` uses measured state population, a protected floor, dynamic exposure factors, and one `From famine` population-loss transaction. | Exact ownership and no-double-debit contract documented. | Runtime validation and balance evidence remain open. |
| Civilian transfer | `famine_migration_transfer_civilians_exact` validates one route, debits origin once, separates route deaths, credits survivors, restores any uncredited destination residual to origin, and records a conservation residual. | Accepted contract documented. | Parent review of all owner call sites remains required. |
| Sparse scheduler | The host-only coordinator processes historical anchors/candidates, active food states, active displacement states, and active displacement countries. | Registry and lifecycle documented. | Runtime save/load and long-run behavior remain unproven here. |
| Decision category | `chaosx_famine_migration_category` is ordinary, hidden at campaign start, and revealed only by active/resolution state or sustained/large exposure thresholds. | Lifecycle documented. | Final player-facing runtime gate remains parent-owned. |
| Decisions and missions | The source contains 26 supporting decisions and three non-selectable missions. | IDs and ownership documented below. | Weighted scenario compare and live outcome validation remain open. |
| Owner adapters | Direct famine, transfer, reception, return, integration, resettlement, projection, five condemnation paths, and exact owner callbacks for Air/Fallout, camps, CBRN chemical, Black Plague, Event 013, and nuclear drop have source call sites. | Active-vs-API-only boundary documented. | Cross-system owner wiring remains incomplete where noted below. |
| Historical profiles | Fifteen profile IDs and their bounded state mappings are present in the selector and constants. | All 15 mappings documented below. | Eligibility is source evidence; no claim is made that every profile has been observed in play. |
| Dedicated mapmodes | Exactly `famine_state_map_mode` and `migration_state_map_mode` are present for this package. | Source and presentation documented. | Dedicated visual runtime proof is limited by the available GUI route. |
| Achievements | Eight IDs, completion predicates, localisation, and 24 achievement DDS variants are present. | Asset and source wiring documented. | Several disqualifier producers and lifecycle proofs remain under achievement-audit review, so unlock behavior is not claimed complete. |
| Assets | The package manifest records 46 assigned category/state/decision/achievement/Deaths DDS rows plus separate report-image rows, with current GFX and Deaths-localisation registrations for the package surfaces. | Provenance and consumer wiring documented. | Report-event consumers remain unresolved. |
| Event 149 | No Event 149 gameplay source exists; the binding plan retires and absorbs the old flat-drain concept without a replacement event ID. | Retirement status and catalog alignment documented. | No replacement source or event-pacing weight is permitted. |
| CXT fixture | `famine_migration_register_cxt_test_content` and `chaosx_cxt_extension_famine_migration_apply` provide bounded test-country setup. | Fixture contract documented. | CXT live verification remains outside this documentation pass. |

## Food formula, exposure, and mortality

The normalized food score is `clamp(((1.15*production) + (1.10*transport) + (1.25*extraction) + (1.00*need) + (0.80*environment) + (0.90*vulnerability) + (0.95*governance) - (1.20*relief)) / 7.15, 0, 200)` after each component is clamped to 0-100.

Stable is below 25, supply strain begins at 25, acute shortage at 50, famine at 75, and catastrophic famine at 100.

Upward entry durations are 7, 7, 14, 21, and 30 days for stable, supply strain, acute shortage, famine, and catastrophic famine respectively.

Recovery hysteresis thresholds are 20, 40, 60, and 80 with durations of 14, 21, 30, and 45 days for the active stage.

The evaluator adds trapped-population pressure as `clamp((trapped_population / (state_population_k * constant:chaos_meter_deaths.people_per_k)) * 100, 0, 100)`.

That normalized trapped pressure contributes to both the need and vulnerability components, so the same trapped headcount has pressure proportional to the state's measured civilian population.

Famine mortality runs only after the relevant stage exposure minimum and due date, scales by stage rate, exposure, vulnerability, access, extraction, environment, governance, and relief, and calls `apply_exact_state_civilian_population_loss` once.

The famine mortality owner is the famine system and its exact Deaths reason is `constant:chaos_meter_deaths_reason.famine`, displayed as `From famine`.

The mortality helper records the applied amount and does not write a second population debit.

## Exact transfer and death-reason ownership

The exact transfer contract requires a valid origin, destination, amount, route, border, transport, safety, actor, destination-food, and destination-reception proof set.

The origin debit is measured from `state_population_k` multiplied by `constant:chaos_meter_deaths.people_per_k` and is applied once through `apply_state_population_loss_without_recruitable_manpower_gain`.

Route deaths are a slice of that debit, are logged with population application disabled, and default to the `From forced displacement` reason unless an explicit owner-provided route-death reason is valid.

Destination credit is survivors only and uses positive state population credit with the owner/controller manpower correction required by the shared contract.

If the destination API credits fewer survivors than requested, `famine_migration_restore_origin_population_residual` restores the uncredited residual to the origin and removes incidental owner/controller recruitable-manpower gains from that restoration.

The transfer then subtracts the actual restored amount from the measured origin debit and recomputes `actual_origin_debit = route_deaths + actual_survivor_credit`.

The conservation identity must have a zero residual and a positive actual origin debit before the transfer result is valid.

The movement contract never converts movement into a death and never credits route deaths at the destination.

| Physical cause | Exact reason owner | Current status |
| --- | --- | --- |
| Food-security mortality | `chaos_meter_deaths_reason.famine`, rendered as `From famine` | Active in the famine mortality helper. |
| Route loss during an exact transfer | `chaos_meter_deaths_reason.forced_displacement` or an explicit validated route-death reason | Active in the transfer contract without a second population debit. |
| Occupation repression | Existing occupation/Deaths owner through the famine pressure seam | API-only: the state-control callback proves a changed controller, not the occupation law, responsible actor, or repression amount. |
| Forced labor | Existing forced-labor/Deaths owner | Camp callback wired after the exact Deaths amount and responsible country are recorded; no second population debit. |
| Border closure or violent pushback | Condemnation owner and decision condemnation wrappers | Five decision condemnation paths have active source call sites. |
| Bombing, nuclear, fallout, outbreak, chemical, biological, camp, genocide, or natural disaster deaths | The existing owner system and its exact Deaths reason | Nuclear, fallout, outbreak, chemical, camp/genocide, and Event 013 callbacks register owner-applied amounts; strategic bombing and unresolved biological/nonhuman paths remain blocked by missing exact owner callbacks. |

One physical population loss has one Deaths owner, and a movement route does not duplicate a direct death source.

## Lifecycle, category reveal, and dormant retirement

The decision category is hidden at campaign start through `visible_when_empty = no` and the absence of emerging, active, or resolution markers.

`famine_migration_refresh_decision_phase_from_state` accepts only a registered valid state and reveals `emerging` when sustained food exposure, qualifying food incident count, flight pressure, trapped population, or state reception load reaches the centralized category threshold.

The reveal helper does not expose the category from a single unqualified registration or isolated pressure pulse.

If the owner country is not already active or in resolution, the helper registers the country in the sparse displacement registry, sets emerging, and clears dormant state.

Active and resolution phases remain visible while their selected cohort or reception load is being worked even if pressure temporarily falls below the reveal threshold.

`famine_migration_retire_inactive_displacement_country` removes a dormant scheduler entry only when the country is valid, has no current country cohort, has zero or absent reception load, and owns no active food or displacement state.

That retirement clears transient scheduler, phase, capacity, load, and transaction-proof variables and removes the country from `global.famine_migration_active_displacement_countries`.

It deliberately preserves integrated, resettled, and returned historical ledgers for achievements and historical consumers.

## Sparse registries and jobs

The runtime coordinator is entered through the existing host-only Chaos Meter hook and does not introduce a whole-world `every_state` or `every_country` scan.

The bounded arrays are `global.famine_migration_historical_profile_anchor_states`, `global.famine_migration_historical_profile_candidate_states`, `global.famine_migration_active_food_states`, `global.famine_migration_active_displacement_states`, and `global.famine_migration_active_displacement_countries`.

State control, annexation, war, peace, peace-conference, and nuclear callbacks register or invalidate only their actual affected scopes.

State and country cleanup removes stale registry rows and transient variables without deleting durable cohort identity or historical ledgers that remain valid.

## Decisions, missions, and category surface

The three missions are `fm_mission_secure_relief_route`, `fm_mission_hold_humanitarian_corridor`, and `fm_mission_prevent_reception_collapse`.

The 26 supporting decisions are `fm_release_reserves`, `fm_emergency_imports`, `fm_repair_relief_route`, `fm_escorted_relief_convoy`, `fm_emergency_airlift`, `fm_invite_relief`, `fm_famine_evacuation`, `fm_requisition_safer_state`, `fm_conceal_crisis`, `fm_maintain_extraction`, `fm_prepare_evacuation`, `fm_evacuate_vulnerable`, `fm_evacuate_workers`, `fm_open_departure_routes`, `fm_restrict_departure`, `fm_negotiate_corridor`, `fm_open_reception`, `fm_controlled_medical_reception`, `fm_distribute_arrivals`, `fm_transit_only`, `fm_close_border`, `fm_enforce_closure`, `fm_local_integration`, `fm_third_country_resettlement`, `fm_voluntary_return`, and `fm_forced_repatriation`.

The category exposes one primary `Displacement Load` modifier and up to two supporting `Reception Capacity` and `Border Policy` values through the ordinary decision panel.

No shared scripted GUI is part of this system contract.

## Ideology and gate precedence

Ideology appears only as a bounded AI modifier on an otherwise valid policy choice or destination candidate.

Destination validity, route safety, food safety, reception capacity, actor authority, and border-policy requirements are gate-level checks and cannot be bypassed by ideological affinity.

Persecution, famine, bombing, camps, occupation conduct, and contamination override any ideological preference when they make a route or destination unsafe.

A same-ideology relationship cannot authorize an unsafe route, and a different-ideology destination can outrank an unsafe ideological ally when the safety and capacity gates pass.

Forced return uses its explicit unsafe-host and policy proof contract and is not authorized by ideology alone.

## Active and API-only adapters

| Adapter family | Source status | Boundary |
| --- | --- | --- |
| Famine and food-security pressure | Active through the decision surface and evaluator | Owner proof and amount remain explicit. |
| Exact civilian transfer and destination credit | Active through evacuation, reception, return, and resettlement decision paths | One transaction owns debit, route deaths, survivors, and conservation. |
| Reception capacity and exact reception delta | Active through CXT and reception decisions | State and owner-country ledgers are updated together. |
| State resettlement and return projections | Active through validated decision transactions | Projections never create population and are visible to state mapmode consumers. |
| Cohort integration, safe resettlement rebind, voluntary return, and forced return | Active source contracts with decision call sites | Forced return retains separate unsafe-host and policy proof. |
| Condemnation for concealment, relief obstruction, deliberate starvation, violent pushback, and forced return | Active decision call sites | Condemnation remains the sanction owner and does not replace direct Deaths ownership. |
| Occupation, deportation, bombing, war, peace, event, cluster, scenario, and blockade pressure seams | API-only with exact source blockers recorded in the adapter handoff | No stable owner callback proves all required state, actor, and context fields; no scan or pacing fallback is added. |
| Air Cleanliness and Fallout | Wired from `air_winter_apply_state_population_loss` | Uses the exact owner-applied civilian loss; fallout is selected only when the state has `nuclear_fallout_state`. |
| Camps, gulags, forced labor, and genocide | Wired from `camp_rework_record_latest_state_deaths` | Uses the exact Deaths amount and `genocide_responsible_country`; site type selects camp/gulag/forced-labor source. |
| Outbreak and chemical aftermath | Wired from Black Plague mortality and accepted CBRN nerve-suppression operation callbacks | Uses exact owner-applied civilian loss; nonhuman/zombie sources remain excluded by the shared state classifier. |
| Nuclear strike and Event 013 disaster | Wired from `on_nuke_drop` and `natural_disaster_apply_population_loss` | Nuclear uses the centralized strike-population fraction because the callback exposes no applied loss; Event 013 passes its exact `natural_disaster_last_deaths`. |
| Internal displacement, cross-border flight, organized evacuation, and deportation request adapters | API-only skeletons for owner-local flows | They register pressure and proof but do not debit population or fabricate a destination. |
| Direct occupation, labor, camp, outbreak, bombing, nuclear, fallout, and disaster death wrappers | API-only in this package | Existing owner systems retain exact Deaths reason ownership. |

The accepted transfer and safe-resettlement contracts include `famine_migration_rebind_cohort_destination_safe`, which supersedes the earlier handoff concern about a regular destination bind for third-country resettlement.

## Historical profile matrix

All fifteen profiles are dynamic starting context and eligibility branches, not fixed historical death outcomes.

| ID | Profile ID | Mode | Audited mapping and proof |
| --- | --- | --- | --- |
| 1 | `hist_soviet_1932_memory` | memory | States 192, 193, 202, 218, 221, 227, 233, 239, 583, 589, and 590 with `SOV` owner/controller, explicit memory proof, and positive live food pressure. |
| 2 | `hist_china_henan_1942` | historical window | Henan state 607 with `CHI`/`MAN` owner/controller, 1942-01-01 through 1943-12-31, and live war or surface-context proof. |
| 3 | `hist_china_policy_famine` | policy analogue | Henan state 607 with `CHI` owner/controller, post-1936 policy-structure proof from the occupation resolver, and positive live food pressure. |
| 4 | `hist_bengal_1943` | historical window | East/West Bengal states 430/431 with `RAJ`/`ENG` owner/controller, 1943-01-01 through 1944-12-31, and live war or positive food pressure. |
| 5 | `hist_vietnam_1944` | historical window | Tonkin/Cochinchina states 671/1066 with `FRA`/`JAP` owner/controller, 1944-01-01 through 1945-12-31, and live war or positive food pressure. |
| 6 | `hist_java_1944` | historical window | West/East Java states 335/1051 with `HOL`/`JAP` owner/controller, 1944-01-01 through 1945-12-31, and live war or positive food pressure. |
| 7 | `hist_greece_1941` | historical window | Greece/Peloponnese/Aegean states 47/186/187 with `GRE`/`GER`/`ITA` owner/controller, 1941-01-01 through 1942-12-31, and live war or positive food pressure. |
| 8 | `hist_leningrad_siege` | historical window | Leningrad state 195 with `SOV`/`GER` owner/controller, 1941-01-01 through 1944-12-31, and live war or proven local blockade insufficiency. |
| 9 | `hist_dutch_hunger_winter` | historical window | Holland/Friesland states 7/36 with `HOL`/`GER` owner/controller, 1944-01-01 through 1945-12-31, and live war or positive food pressure. |
| 10 | `hist_spain_early_1940s` | historical window | Audited states 41, 165-178, and 788-794 with `SPR` owner/controller, 1939-01-01 through 1943-01-01, and live war or positive food pressure. |
| 11 | `hist_ireland_memory` | memory | Ireland state 113 with `IRE`/`ENG` owner/controller, explicit memory proof, and positive live food pressure. |
| 12 | `hist_brazil_ceara` | dynamic regional | Ceará state 935 with `BRA` owner/controller, occupation/policy proof, and positive live food pressure. |
| 13 | `hist_congo_interaction` | dynamic regional | Congo/Middle Congo states 295/772 with `BEL`/`FRA` owner/controller, occupation/policy proof, and positive live food pressure. |
| 14 | `hist_ethiopia_policy` | policy analogue | Ethiopia/Tigray states 271/842 with `ETH`/`ITA` owner/controller, 1936-01-01 through 1942-01-01, and live war or policy proof. |
| 15 | `hist_nuclear_winter_global` | dynamic regional | Any explicitly registered valid state with Air Cleanliness contamination or Air Winter evidence, local vulnerability proof, and positive live food pressure, with no whole-world activation. |

The selector, constants, and scripted localisation use the same fifteen IDs and a `none` value.

## Mapmodes

Exactly two dedicated mapmodes belong to this system: `famine_state_map_mode` and `migration_state_map_mode`.

The famine mapmode colors by food stage, with the score and normalized components available to authorized tooltip viewers.

The migration mapmode prioritizes trapped population, active exodus/flight, overcrowded reception, resettlement or return projections, and ordinary reception.

The migration mapmode does not draw route arrows, infer destinations, or scan global cohorts, and persistent cohort destination/status remains transaction-ledger data.

The other mapmodes in `docs/systems/state_map_modes.md` are contamination, civilian deaths, and Air Winter and are not additional famine or migration mapmodes.

## Achievements and assets

The eight achievement IDs are `famine_migration_break_the_blockade`, `famine_migration_no_one_left_at_the_gate`, `famine_migration_roads_home`, `famine_migration_bread_across_the_front`, `famine_migration_hungry_not_contagious`, `famine_migration_a_place_at_the_table`, `famine_migration_the_grain_stayed_home`, and `famine_migration_the_country_did_not_empty`.

The achievement source, localisation, and effect predicates are present, while unlock completion still depends on the runtime state and transaction ledgers.

The package asset manifest records one category icon, nine state/reception icons, ten decision icons, eight achievement triplets, and two Deaths-reason texticons, while the separate package asset records cover one category picture and seven report-image subjects.

The manifest records source, processed, and DDS rows for the assigned visual package, and current interface sources register the category, state, decision, report, dedicated mapmode, and Deaths-reason sprites.

`fm_deaths_famine` and `fm_deaths_displacement` are 18x18 native-alpha uncompressed BGRA8 one-mip texticons registered as `GFX_fm_deaths_famine` and `GFX_fm_deaths_displacement` in `interface/chaosx_texticons.gfx`.

The current Deaths cause localisation consumes `£fm_deaths_famine` for `From famine` and `£fm_deaths_displacement` for `From forced displacement`, so the texticon consumer is wired in the current source snapshot.

The report images and category picture have current sprite registrations but no confirmed compatible shared report/notification carrier in the current source, so asset delivery is documented separately from runtime report integration.

The report-picture carrier conflict is tracked as FM-R2 in `docs/plans/famine_and_migration_system_plans/improvement_review_addendum.md` because the accepted incident/report requirement must use an existing non-pool carrier or obtain a parent design decision without allocating a replacement Event 149 ID or random-event pool entry.

## Event 149 retirement

No `chaosx.nr149.1` Event 149 source or replacement event chain exists in the current implementation.

The accepted binding decision retires and absorbs the old `Immigrations` flat-drain concept into the shared famine and migration system, forbids a replacement event ID, and forbids an event-pacing weight.

The exported spreadsheet row at `docs/spreadsheets/chaos_redux_events_catalog.csv:311` now reads `Retired and absorbed into the shared dynamic famine and migration system. Unavailable as a random event.` and remains marked unavailable with no replacement event ID.

## CXT fixture

`common/scripted_effects/famine_migration_cxt_test_effects.txt` defines `famine_migration_register_cxt_test_content` and `chaosx_cxt_extension_famine_migration_apply` for the token `chaosx_cxt_extension_famine_migration`.

When initialized, the fixture gives CXT reception capacity from `constant:famine_migration_decision_threshold.category_reception_load`, sets capital-state input components to `constant:famine_migration_food_score.supply_strain_threshold` with relief at zero, and submits a proven context.

The fixture deliberately creates no route, transfer, severe famine, mortality transaction, or ordinary gameplay event.

Startup and `on_daily_CXT` registration are additive and idempotent, as documented in `docs/testing/chaosx_test_country.md`.

## Persistent food-reserve ledger

The food-security state owns a sparse reserve ledger in addition to the normalized pressure score. It is a bounded supporting input, not a second economic simulator: it stores one amount, one capacity, one target, one date guard, bounded daily replenishment/depletion, and cumulative transaction totals per already-registered state, with no goods types, market prices, national stockpile, world scan, or parallel population ledger.

Reserve units are thousand-person-days, so `state_population_k` is the population driver without a raw-person overflow. `daily_need = round(max(1, state_population_k * constant:famine_migration_food_reserve.daily_need_per_k))`; `logistics_factor` is the clamped base plus infrastructure contribution minus normalized production and transport penalties; `capacity = round(max(1, daily_need * capacity_days * logistics_factor))`; and `target = min(capacity, round(max(1, daily_need * target_days * logistics_factor)))`.

Initialized stable states replenish once per game date toward target using daily need, production and transport headroom, and logistics factor. An uninitialized zero ledger does not self-create stock. Active supply strain, acute shortage, famine, and catastrophic famine states deplete once per game date using centralized shares 0.05, 0.20, 0.50, and 1.00 multiplied by daily need and normalized component need. Both paths cap the actual mutation at the remaining target gap or current amount and record exact last-day and cumulative totals.

The first refresh does not assert an unowned stockpile. An owner must set a positive `famine_migration_food_reserve_initial_amount` together with `famine_migration_food_reserve_initialization_proven > 0`, or a positive amount must already exist in a save, before `famine_migration_food_reserve_initialized` is set. A zero amount therefore remains zero until an explicit proven import or initial allocation, which keeps initialization fail-closed when no vanilla state-level food-stock carrier is available.

`famine_migration_consume_food_reserve_for_relief` consumes only the actual amount available and returns `famine_migration_food_reserve_consume_result`, `..._consumed_output`, `..._relief_granted_output`, and `..._remaining_output`. Public aliases are `famine_migration_release_food_reserves` and `famine_migration_consume_food_reserves_as_relief`.

`famine_migration_add_food_reserves` accepts only proven positive import requests, credits free capacity, and returns `famine_migration_food_reserve_add_result`, `..._added_output`, `..._remaining_output`, and `..._capacity_output`. Its public alias is `famine_migration_import_food_reserves`.

`famine_migration_transfer_food_reserves` runs in a proven source state with a distinct regular event-target destination. It returns `famine_migration_food_reserve_transfer_result`, `..._transfer_source_debit_output`, `..._transfer_destination_credit_output`, and `..._transfer_remaining_output`. Accepted amount is `min(request, source amount, destination free capacity)`; the actual source debit and destination credit are measured after mutation, any non-zero residual is rolled back, and cumulative transfer totals advance only when `source_debit - destination_credit = 0`. Its public alias is `famine_migration_requisition_food_reserves`.

The evaluator adds `clamp((reserve_amount / daily_need) * constant:famine_migration_food_reserve.relief_per_day_covered + famine_migration_food_reserve_relief, 0, constant:famine_migration_food_reserve.relief_maximum)` to the existing normalized relief component. Reserve relief decays once per day, is separate from historical population ledgers, and never changes population.

State cleanup removes active registration and transient pressure components but preserves reserve amount, capacity, target, initialization proof, last-update date, cumulative reserve totals, and all historical/population ledgers. The bounded runtime coordinator reaches the update only through the existing active-food registry.

Decision owners set one documented request/proof bundle, call the matching public alias in the actual state scope, read the explicit result and accepted outputs in the same effect chain, and do not write reserve amount directly. This contract leaves decision costs, AI weights, localisation, and presentation ownership to the decision tranche.

## Audit evidence and limitations

The current bounded HOI4 map inspection returned `MAP_INSPECTED` for 32 requested historical-profile states and passed state definitions, bitmap, state-region membership, adjacency, supply, and railway checks.

The current map artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34498d56d4bf765796f793b12431c8e42bf07506d9484b1c7f3a961900f58b1d/66c0aca0d881147df54e388a8d987bf4f8422ed0c1b6fa779fc8ea008ddb3eb0/map-inspect.456c28c5a8e6bad1.json`.

The same inspection reported unrelated workspace-wide floating-harbor and building-position diagnostics from `map/buildings.txt`, with 2,654 omitted diagnostics after the retained-error ceiling.

The pre-change AI probability baseline proves that Event 149 and the shared weighted surfaces were absent before implementation, but it is not current balance evidence.

The post-change decision handoff records a full 20-scenario probability evaluation timeout and no completed before/after `hoi4.probability_compare` result, so weighted balance remains unresolved.

The required read-only `hoi4.event_inspect` lint request for `common/decisions/famine_migration_decisions.txt` with `expandHelpers = true`, `maxNodes = 800`, `maxEdges = 1600`, and workspace `chaos_redux` was accepted but timed out at 180 seconds without diagnostics; source checks are not treated as an equivalent engine result.

The available GUI route modeled zero elements for the hardcoded `mapmodes` window and timed out on the corresponding render attempt, so mapmode source evidence is not a complete visual runtime proof.

## Open blockers and parent decisions

1. Resolve the owner-source blockers listed in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/adapter_wiring_closure.md` for occupation-law changes, strategic bombing, deportation, war/peace state aftermath, event and cluster members, and unavailable Event 118/120/131/149 roots. The validated Air/Fallout, camps, CBRN, Black Plague, Event 013, and nuclear adapters are wired without duplicate deaths or new pacing scans.
2. Resolve the report-picture carrier conflict and provide report-event registry and consumer ownership for the delivered report assets and category picture without adding a replacement random-event ID or pool entry.
3. Rerun the named 20 weighted scenarios through the required probability inspection and compare workflow with stable scenario inputs.
4. Complete the achievement audit for disqualifier producers, cohort lifecycle evidence, and cleanup/identity transitions before any unlock-completion claim.
5. Obtain a supported mapmode GUI/render artifact or retain the current runtime visual gate as an explicit external validation requirement.
6. Review the unrelated `map/buildings.txt` locator diagnostics separately from this system.
7. Provide an owner-supplied, proven initial reserve amount or import source for states that should begin with non-zero stock; the scoped engine APIs expose no vanilla state-level food-stock carrier, so the ledger remains zero until that causality is supplied.

No gameplay completion claim is made until these gates and parent-owned runtime checks are resolved.
