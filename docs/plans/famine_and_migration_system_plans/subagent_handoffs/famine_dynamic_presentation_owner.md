# Famine and migration dynamic presentation owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Ownership and completion boundary

This handoff covers the bounded presentation layer only.

Changed gameplay surfaces are `common/dynamic_modifiers/famine_migration_state_modifiers.txt`, `common/script_constants/famine_migration_presentation_constants.txt`, and `common/scripted_effects/famine_migration_presentation_effects.txt`.

The matching scripted-effect documentation is `common/scripted_effects/famine_migration_presentation_effects.md`.

The existing UTF-8 BOM localisation file `localisation/english/famine_migration_l_english.yml` received five new modifier title/description pairs.

No core transfer effect, decision, on-action, mapmode, achievement, workbook, or shared asset file was edited.

No Git commit was created.

## Helper map

| Identifier | Scope | Inputs | Outputs | Side effects | Parent-owned callsite |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_presentation_compute_share` | Current state or any scope with temporary values | Temporary proof, people, and denominator | Temporary clamped `famine_migration_presentation_share` | None | Internal call from each projection record and the state refresh. |
| `famine_migration_presentation_record_preparing_projection` | State | Preparing proof, people, denominator, positive generation and role; cohort id may be missing or zero because preparation is pre-cohort | Preparing projection receipt variables and `famine_migration_presentation_preparing_projection_active` | Overwrites only the preparing receipt and consumes its phase input; generic metadata remains action-local until refresh; never changes population | Call after an exact preparation/request proof and before the refresh. |
| `famine_migration_presentation_record_organized_evacuation_projection` | State | Organized proof, people, denominator, and generic exact cohort/generation/role metadata | Organized projection receipt variables and `famine_migration_presentation_organized_projection_active` | Overwrites only the organized receipt and consumes its phase input; generic metadata remains action-local until refresh; never changes population | Call after an exact prepared/mission/request proof and before the refresh. |
| `famine_migration_presentation_record_depopulated_projection` | State | One exact actual origin debit, its pre-debit denominator, positive cohort/generation/role, and the core transfer generation | Cumulative depopulated projection receipt variables, `..._projection_last_generation`, and `famine_migration_presentation_depopulated_projection_active` | Adds the debit exactly once when its generation is newer than the stored generation, preserves the first valid pre-debit denominator, consumes its phase input, and never changes population | Call after successful exact origin debit and after the core receipt is persisted, before the refresh. |
| `famine_migration_presentation_record_transit_projection` | State | Exact hosted transit amount, denominator, and generic exact cohort/generation/role metadata | Transit projection receipt variables and `famine_migration_presentation_transit_projection_active` | Overwrites only the transit receipt and consumes its phase input; generic metadata remains action-local until refresh; never changes population | Call when a hosted transit cohort is accepted or its exact load changes. |
| `famine_migration_presentation_record_return_readiness_projection` | State | Exact eligible return amount, denominator, and generic exact cohort/generation/role metadata | Return-readiness projection receipt variables and `famine_migration_presentation_return_readiness_projection_active` | Overwrites only the readiness receipt and consumes its phase input; generic metadata remains action-local until refresh; never changes population | Call when the eligible cohort or exact readiness denominator changes. |
| `famine_migration_presentation_record_resettlement_return_projection` | State | Exact survivor credit or durable outcome amount, denominator, and generic exact cohort/generation/role metadata | Resettlement/return projection receipt variables and `famine_migration_presentation_resettlement_projection_active` | Overwrites only the return receipt and consumes its phase input; generic metadata remains action-local until refresh; never changes population | Call after exact survivor credit or durable return/resettlement outcome is written. |
| `famine_migration_presentation_clear_preparing_projection` | State | None | Clears preparing receipt and active flag | Touches no other projection | Call when preparation is canceled or execution begins. |
| `famine_migration_presentation_clear_organized_evacuation_projection` | State | None | Clears organized receipt and active flag | Touches no other projection | Call after successful organized debit before recording depopulation. |
| `famine_migration_presentation_clear_depopulated_projection` | State | None | Clears cumulative depopulation receipt, last-generation idempotency key, and active flag | Touches no other projection | Call only on exact state retirement or history reset. |
| `famine_migration_presentation_clear_transit_projection` | State | None | Clears transit receipt and active flag | Touches no other projection | Call when the hosted transit cohort leaves, integrates, or reaches terminal failure. |
| `famine_migration_presentation_clear_return_readiness_projection` | State | None | Clears readiness receipt and active flag | Touches no other projection | Call when readiness expires, is canceled, or becomes a return transfer. |
| `famine_migration_presentation_clear_resettlement_return_projection` | State | None | Clears return receipt and active flag | Touches no other projection | Call only on exact state retirement or history reset. |
| `famine_migration_presentation_clear_all_projections` | State | None | Clears all six presentation projection receipts | Idempotently clears only this layer's projection data | Call during complete state retirement after core ledgers are no longer needed. |
| `famine_migration_presentation_clear_state` | Valid state | None | Zeroed derived shares and modifier values, cleared presentation flags | Removes ten flow modifiers and forces a dynamic update; preserves persistent projection receipts and core ledgers | Call with core cleanup for invalidated, removed, annexed, wasteland, or otherwise retired states. |
| `famine_migration_presentation_refresh_state` | Valid state | Exact core live ledgers, persistent presentation receipts, and one-shot `famine_migration_presentation_input_*` values | Ten phase shares, dynamic modifier values, presentation flags, temporary refresh result | Clears and re-adds only presentation flow modifiers, forces a dynamic update, and consumes direct one-shot inputs after a valid refresh | Call after each authoritative transfer/reception/trapped/flight/return lifecycle transition and after projection receipt updates. |

The presentation layer has no event-target API and does not persist a scope pointer.

Projection receipts are phase-owned and independent; a record or clear operation for one phase never clears another phase's stored amount, denominator, share, cohort, generation, role, or active flag. The generic metadata is one action-local staging bundle, so owners performing multiple role updates in one chain must set it immediately before each record call; the refresh clears it only after all phase reads complete. Preparing may explicitly stage cohort id zero or omit it, while every other persisted role requires a positive cohort id.

## Receipt sufficiency checkpoint

The current authoritative core variables are sufficient to rebuild five presentation roles without a presentation receipt: active exodus has the positive equal paired flight variables, reception and overcrowding have exact `famine_migration_state_reception_load` plus context flags, trapped population has exact `famine_migration_state_trapped_population`, and resettlement/return has exact durable counters plus context flags.

The current authoritative core census does not provide a bounded live amount and lifecycle receipt for the other five roles: preparing to leave, organized evacuation preparation, cumulative depopulated-district history, hosted transit load, and return-readiness eligibility.

The existing origin transfer receipt names are `famine_migration_projection_last_origin_population_before`, `famine_migration_projection_last_origin_debit`, `famine_migration_projection_last_survivor_credit`, `famine_migration_projection_last_route_deaths`, `famine_migration_projection_last_origin_departure_share`, `famine_migration_projection_last_cohort_id`, `famine_migration_projection_last_generation`, and `famine_migration_projection_last_role`. They are exact last-transaction facts, not a cumulative history ledger, and the presentation layer does not rewrite or reinterpret them as active flight.

The destination transfer receipt exposes exact survivor credit and destination metadata, while `famine_migration_state_reception_load` remains the live destination reception amount consumed by the presentation refresh.

The six record effects provide the missing presentation-only persistence, but the parent/core/decision owners must call them with exact source variables and exact generation/role metadata; a positive cohort id is required for every persisted role except preparing.

## Exact formulas and data sources

For every phase, the shared formula is `share = clamp(actual_people / exact_population_denominator, 0, 1)`.

The live state denominator is `state_population_k * constant:famine_migration_presentation.people_per_k`.

Active exodus requires `famine_migration_displacement_active`, positive `famine_migration_flight_pressure`, positive `famine_migration_state_flight_population`, equality between those two current ledgers, and a positive live denominator.

The active-exodus people amount is the equal current `famine_migration_flight_pressure`/`famine_migration_state_flight_population` pair divided by the live denominator.

The paired flight amount is a presentation-only current obligation and is not an origin debit, survivor credit, route-death amount, or destination population.

The completed `famine_migration_projection_last_origin_departure_share` is historical receipt data and is not used as an active-exodus amount or organized-evacuation amount.

Active exodus does not consult `famine_migration_projection_last_role` or require a prior live cohort; organized projection remains the explicit exclusion.

An active organized projection also suppresses the active-exodus presentation, preventing one lifecycle from rendering as two active movement phases.

Organized evacuation is read from an active persisted prepared/mission/request receipt tied to exact cohort and generation, or from a direct exact one-shot proof that includes the same lifecycle metadata.

After successful organized debit, the organized projection must be cleared and depopulation must be recorded from the exact actual origin debit and exact pre-debit denominator. The depopulation record adds that debit once per newer core transfer generation and preserves the first valid pre-debit denominator as its durable baseline.

Core increments `global.famine_migration_transfer_generation` once in `famine_migration_record_transfer_projection` after a successful exact debit and writes that value to `famine_migration_projection_last_generation`; the presentation accumulator stores the accepted generation per state as `famine_migration_presentation_depopulated_projection_last_generation`, so duplicate post-receipt calls are idempotent.

Reception uses exact `famine_migration_state_reception_load` and the live state denominator.

Overcrowded reception uses that same exact state load and requires the core `famine_migration_overcrowded_context_active` owner-capacity breach flag.

Trapped population uses exact `famine_migration_state_trapped_population` and the live state denominator.

Transit requires a persisted exact hosted-cohort amount and denominator; destination population and flight-pressure projections are not used.

Return readiness requires a persisted exact eligible-cohort amount and denominator.

Resettlement/return prefers a persisted exact survivor-credit or durable-outcome receipt and otherwise uses the larger exact durable `famine_migration_state_resettled_population` and `famine_migration_state_returned_population` counter while either exact core context flag remains active.

Origin debit includes route deaths for reconciliation, but route deaths remain a separate Deaths/condemnation channel and are never used as a presentation people amount.

Destination reception and transit people use survivor credit or exact hosted-cohort load, never route deaths and never duplicated origin debit.

## Modifier and tuning table

| Phase | Modifier identifier | Full-share consequence |
| --- | --- | --- |
| Preparing to leave | `famine_migration_state_preparing_to_leave` | `-0.03` state production and `-0.02` controller army speed. |
| Active exodus | `famine_migration_state_exodus` | Existing `famine_migration_modifier.exodus_production` and `.exodus_speed` scaled by share. |
| Organized evacuation | `famine_migration_state_organized_evacuation` | `-0.08` state production and `-0.05` controller army speed. |
| Depopulated districts | `famine_migration_state_depopulated_districts` | `-0.15` state production, `-0.20` local manpower ratio, and `-0.10` local building-slots factor. |
| Reception | `famine_migration_state_reception` | Existing reception supply/production values scaled by share and `-0.02` controller army speed. |
| Overcrowded reception | `famine_migration_state_overcrowded` | Existing overcrowded supplies/attrition values scaled by share and `-0.08` controller army speed. |
| Trapped population | `famine_migration_state_trapped_border` | Existing trapped supplies/speed values scaled by share. |
| Transit | `famine_migration_state_transit` | `-0.12` local supplies, `-0.05` state production, and `-0.08` controller army speed. |
| Return readiness | `famine_migration_state_return_readiness` | `-0.04` state production and `-0.02` controller army speed. |
| Resettlement/return | `famine_migration_state_return` | Existing return production value and `-0.02` controller army speed scaled by share. |

All new full-share values are centralized in `common/script_constants/famine_migration_presentation_constants.txt`.

All derived outputs are clamped between the centralized presentation modifier floor and ceiling.

The existing final icon families are reused without new assets: exodus for departure/depopulation/transit, reception for reception, overcrowded for overload, trapped-border for trapped, and return for return readiness/resettlement.

## Input and output variable contract

The generic metadata variables are `famine_migration_presentation_input_generation` and `famine_migration_presentation_input_role` for every persistent projection record, plus `famine_migration_presentation_input_cohort_id` for every role except preparing. Preparing may set the cohort input to zero or leave it absent in a clean action scope.

The organized record rejects any role other than organized evacuation, the transit record rejects any role other than transit, and the resettlement/return record accepts only resettlement, voluntary return, or forced return roles.

Preparing input names are `famine_migration_presentation_input_preparing_proven`, `..._people`, and `..._denominator`.

The old active-exodus input names are cleanup-only compatibility fields; no producer should stage them because refresh derives active exodus exclusively from the current equal flight pair.

Organized evacuation input names are `famine_migration_presentation_input_organized_evacuation_proven`, `..._people`, and `..._denominator`.

Depopulated-district input names are `famine_migration_presentation_input_depopulated_districts_proven`, `..._people`, and `..._denominator`.

Transit input names are `famine_migration_presentation_input_transit_proven`, `..._people`, and `..._denominator`.

Return-readiness input names are `famine_migration_presentation_input_return_readiness_proven`, `..._people`, and `..._denominator`.

Return/resettlement input names are `famine_migration_presentation_input_resettlement_return_proven`, `..._people`, and `..._denominator`.

`proven` must be positive, `people` must be positive, and `denominator` must be positive for a phase to display or be recorded. Generation and role must be positive for every persistent record; cohort id must additionally be positive for organized evacuation, depopulated districts, transit, return readiness, and resettlement/return.

Projection outputs store phase-specific people, denominator, share, cohort id, generation, role, and active flag values under the names documented in `common/scripted_effects/famine_migration_presentation_effects.md`; preparing may store cohort id zero because it is pre-cohort, and depopulation additionally stores its last accepted generation.

Invalid or incomplete inputs fail closed to a zero share and no new receipt.

## Required parent/core/decision integration callsites

After an exact preparation, organized request, exact cumulative debit, transit-host update, return-readiness eligibility update, or survivor-credit/durable-return outcome is proven, the owner must set that phase's input bundle and generic metadata, call the matching `famine_migration_presentation_record_*_projection` effect, and call `famine_migration_presentation_refresh_state` in the same state scope.

After `famine_migration_record_transfer_projection` succeeds, the origin owner must refresh after core receipt variables are persisted and must record depopulation from the exact actual origin debit when that departure is terminal.

The origin owner must not use `famine_migration_projection_last_origin_departure_share` as active exodus or organized people data.

The active-exodus owner must refresh after the current paired flight obligation is updated and both flight ledgers are equal.

The destination owner must refresh after exact survivor credit and reception delta accounting have completed.

After `famine_migration_apply_reception_delta` and `famine_migration_refresh_reception_context`, refresh the receiving state so its live load and overload flag are current.

After `famine_migration_register_trapped_population` or its equivalent trapped-ledger update, refresh the affected state.

After `famine_migration_record_state_resettlement_projection` or `famine_migration_record_state_return_projection`, refresh the state after the projection context flag and durable counter are written, or record the exact survivor-credit/durable-outcome receipt when the cohort-specific amount is available.

On an exact terminal transition, call only the matching projection clear effect and then refresh, so one role update cannot erase another role's receipt.

Before core clears or retires an invalid state, call `famine_migration_presentation_clear_state` while the state still resolves as valid, and call `famine_migration_presentation_clear_all_projections` when the state history itself is being retired.

The parent/core owner must extend the core `famine_migration_clear_dynamic_modifiers` lifecycle to remove `famine_migration_state_preparing_to_leave`, `famine_migration_state_organized_evacuation`, `famine_migration_state_depopulated_districts`, `famine_migration_state_transit`, and `famine_migration_state_return_readiness`, because this bounded task did not edit the shared core effect.

The presentation refresh must run after the core refresh when both are used, because the core refresh still adds the original flow identifiers from its lifecycle flags and this presentation refresh intentionally replaces those with receipt-scaled values.

No callsites were edited in this bounded ownership tranche.

## Exhaustive current producer and terminal-clear matrix

The following matrix is the current read-only census of every known producer seam and the exact presentation API call that remains parent-owned. The listed file and effect owners must stage inputs in the state scope after the authoritative ledger or receipt is written, because this bounded tranche does not edit those owner files.

The external-call census is zero for all presentation `record_*_projection` and role-specific `clear_*_projection` effects. The only existing consumer is the core `famine_migration_refresh_state_modifiers` wrapper, which calls `famine_migration_presentation_refresh_state`; the matrix below is therefore an explicit integration handoff, not a claim that the ten-role API is already wired.

| Phase | Current authoritative producer and transaction phase | Required parent/core/decision callsite and input contract | Terminal clear owner and API |
| --- | --- | --- | --- |
| Preparing to leave | `common/decisions/famine_migration_decisions.txt` `fm_prepare_evacuation` remove effect at `famine_migration_evacuation_prepared` (line 694) writes only a state flag. `common/scripted_effects/famine_migration_corridor_effects.txt` `famine_migration_prepare_corridor_contract` (lines 48-220) stores an exact corridor amount, cohort id, and route generation when the corridor request is proven. `fm_open_departure_routes` and `fm_restrict_departure` change policy only. | Decision owner must emit `famine_migration_presentation_input_preparing_proven`, exact `..._people`, exact `..._denominator`, positive `..._generation`, and positive `..._role`; cohort id may be absent or explicitly zero because this phase is pre-cohort. Then call `famine_migration_presentation_record_preparing_projection` and `famine_migration_presentation_refresh_state`. The generic preparation flag alone fails closed. | Decision owner clears on preparation cancellation or execution start; corridor owner clears on `famine_migration_corridor_cleanup` (lines 902-1015). Call `famine_migration_presentation_clear_preparing_projection` and then refresh. |
| Active exodus | Core `famine_migration_submit_survivor_flight_request` (lines 3842-3914) and `famine_migration_apply_pressure_request` (lines 1229-1425) maintain the current paired `famine_migration_flight_pressure` and `famine_migration_state_flight_population` obligation. Core `famine_migration_reconcile_successful_transfer_obligations` (lines 1879-1914) settles the pair after a successful exact debit. | Core owner must call `famine_migration_presentation_refresh_state` after both current flight ledgers are written or settled. Refresh requires displacement active, both values positive, and exact equality; it uses that pair as presentation people over the live denominator, excludes an active organized projection, and does not read `famine_migration_state_live_cohort_amount` or `famine_migration_projection_last_role`. | Core owner clears the live presentation by settling both ledgers and clearing the displacement lifecycle through `famine_migration_clear_dynamic_modifiers` or state cleanup. There is no active-exodus projection receipt to clear and no depopulation history may be cleared by this terminal. |
| Organized evacuation | The request seam is core `famine_migration_request_organized_evacuation` (lines 5150-5210), with corridor preparation in `famine_migration_prepare_corridor_contract` (lines 48-220). Decision exact-transfer producers are `fm_famine_evacuation` (line 1793), `fm_evacuate_vulnerable` (line 2002), and `fm_evacuate_workers` (line 2219); corridor execution is `famine_migration_execute_corridor_evacuation` (lines 522-553); arrival redistribution is `fm_distribute_arrivals` (line 2968). | Decision/corridor owners must record only a prepared, mission, or request receipt tied to exact cohort and generation: set generic metadata and `famine_migration_presentation_input_organized_evacuation_proven`, exact `..._people`, and exact `..._denominator`, then call `famine_migration_presentation_record_organized_evacuation_projection` and refresh. After a successful exact debit, use the actual debit and pre-debit denominator to record depopulation, clear organized, and refresh. | Decision owner clears failed or canceled evacuation branches (`fm_famine_evacuation`, `fm_evacuate_vulnerable`, and `fm_evacuate_workers` clear their prepared flag around lines 1954, 2010, 2167, 2227, and 2304). Corridor owner clears completed, rejected, unsafe, deadline, control-change, or route-closed contracts through `famine_migration_corridor_cleanup`. Verify the stored cohort and generation are terminal before calling the phase-wide `famine_migration_presentation_clear_organized_evacuation_projection`. |
| Depopulated districts | All exact transfer producers converge on core `famine_migration_record_transfer_projection` (lines 1918-1960) after `famine_migration_transfer_civilians_exact` proves a positive actual origin debit. Current exact transfer callsites are spontaneous owner `famine_migration_process_spontaneous_movement_owner` line 196, corridor owner `famine_migration_execute_corridor_evacuation` line 537, forced owner `famine_migration_execute_forced_transfer_exact` line 210, and decisions `fm_famine_evacuation` line 1793, `fm_evacuate_vulnerable` line 2002, `fm_evacuate_workers` line 2219, `fm_distribute_arrivals` line 2968, `fm_transit_only` line 3191, `fm_enforce_closure` line 3363, `fm_third_country_resettlement` line 3669, `fm_voluntary_return` line 3913, and `fm_forced_repatriation` line 4112. The camp producer `camp_rework_germany_apply_prisoner_transfer` calls the forced owner at line 928. | Parent/core should patch the centralized `famine_migration_record_transfer_projection` success seam once, rather than adding duplicate writers to every producer above. After the exact receipt is persisted, stage `..._people = famine_migration_transfer_actual_origin_debit`, `..._denominator = famine_migration_transfer_origin_population_before`, and the exact receipt cohort, generation, and role, then call `famine_migration_presentation_record_depopulated_projection` and refresh. If a producer-local patch is selected instead, exactly one local owner must call it after the same receipt and the centralized writer must not also call it. The core transfer generation is the idempotency key; a duplicate generation adds nothing, a newer generation adds exactly one debit, and the first valid pre-debit denominator remains the cumulative baseline. Route deaths stay in the separate Deaths channel and never enter this people input. | Core state-retirement owner clears only on exact history retirement or reset through `famine_migration_presentation_clear_depopulated_projection`; ordinary transfer completion must preserve the durable cumulative receipt. All state history retirement paths also use `famine_migration_presentation_clear_all_projections`. |
| Reception | Core `famine_migration_apply_reception_delta` (lines 2249-2272) is the authoritative state-load credit/debit seam and calls `famine_migration_refresh_reception_context` (lines 2191-2212). Current direct survivor-credit/debit callsites are decisions at lines 1855, 2061, 2278, 2980, 3005, 3203, 3226, 3374, 3514, 3680, 3707, 3724, 3736, 3924, and 4123; corridor line 551; forced owner line 234; spontaneous owner line 218. | Core owner must refresh the affected destination state after every exact reception delta and after `famine_migration_refresh_reception_capacity` (line 2322) changes capacity. Decision owner must preserve the existing state scope around `fm_open_reception` (line 2710), `fm_controlled_medical_reception` (line 2764), and `fm_distribute_arrivals` (line 2844), then let the core context refresh derive live reception share. No presentation receipt is needed. | Live reception clears when the exact state reception load reaches zero or state cleanup retires the state. `famine_migration_presentation_clear_state` is the presentation cleanup call; do not clear durable depopulation or return receipts merely because reception load is zero. |
| Overcrowded reception | Core `famine_migration_refresh_reception_context` (lines 2191-2212) sets `famine_migration_overcrowded_context_active` only when exact live reception load breaches the owner capacity. It is reached from `famine_migration_apply_reception_delta` line 2272 and capacity recalculation paths. | Core owner must refresh after each load delta and after capacity-only changes from `famine_migration_refresh_reception_capacity` line 2322 and the reception decisions named above. Refresh derives the overload share from exact live reception load and the live denominator, gated by the core capacity-breach flag; no flat threshold or projection receipt is accepted. | Core context owner clears `famine_migration_overcrowded_context_active` when load or capacity breach ends and state cleanup clears the presentation. Call `famine_migration_presentation_clear_state` after the context is invalidated; no role-specific projection clear is required. |
| Trapped population | Sole request producer is `famine_migration_spontaneous_movement_trap_request` (lines 94-108), which calls core `famine_migration_register_trapped_population` (lines 2166-2181). Corridor settlement `famine_migration_corridor_record_evacuation` (lines 453-479) and core `famine_migration_reconcile_successful_transfer_obligations` (lines 1879-1914) subtract the exact settled debit from the trapped ledger. | Core/spontaneous owner must call `famine_migration_presentation_refresh_state` immediately after `famine_migration_register_trapped_population` or any exact trapped-ledger settlement. Refresh uses only positive `famine_migration_state_trapped_population` over the live denominator and never route deaths. | Core owner clears the derived phase when `famine_migration_state_trapped_population` reaches zero or the trapped state is retired. Call `famine_migration_presentation_clear_state` after the ledger and context clear; no projection receipt is required. |
| Transit | The exact transit role producer is decision `fm_transit_only` (lines 3073-3247), which sets role transit and executes exact transfer at line 3191, then debits source reception at line 3203 and destination reception at line 3226. `fm_local_integration` (lines 3427-3547) resolves a hosted cohort and calls integration at line 3505, which is a terminal hosted-cohort path. | Decision owner must emit an exact hosted transit cohort after the destination rebind, with generic cohort/generation/role transit metadata, `famine_migration_presentation_input_transit_proven`, survivor-credit or live hosted amount, and the exact current denominator, then call `famine_migration_presentation_record_transit_projection` and refresh. The generic live cohort amount and destination population are not sufficient because they are not role-filtered hosted transit ledgers. | Decision owner must verify the stored transit cohort and generation are the terminal one before calling the phase-wide `famine_migration_presentation_clear_transit_projection` after onward transit debit, integration, resettlement, return, route failure, control change, or state cleanup, then refresh. |
| Return readiness | Core `famine_migration_evaluate_voluntary_return` (lines 2333-2350), called by decision `fm_voluntary_return` at line 3897, sets only the country eligibility flag and saved route endpoints. Forced-return decisions `fm_enforce_closure` and `fm_forced_repatriation` stage return obligations but do not currently expose a bounded eligible amount. | Core/decision owner must emit the exact eligible cohort amount, live denominator, cohort id, generation, and return role after eligibility proof, then call `famine_migration_presentation_record_return_readiness_projection` and refresh. The country flag alone fails closed. | Decision/core owner must verify the stored readiness cohort and generation are the terminal one before calling the phase-wide `famine_migration_presentation_clear_return_readiness_projection` on expiry, cancel, route transfer, or failed return through `fm_voluntary_return` cancellation at line 3992, forced-return cancellation at line 4175, and `famine_migration_cleanup_route_request` (line 2430), then refresh. |
| Resettlement/return | Exact durable producers are core `famine_migration_record_state_resettlement_projection` (lines 2284-2296) and `famine_migration_record_state_return_projection` (lines 2304-2316). Decision producers are `fm_third_country_resettlement` at line 3724, `fm_enforce_closure` at line 3410, `fm_voluntary_return` at line 3961, and `fm_forced_repatriation` at line 4160, each after exact survivor-credit accounting. | Core/decision owner must prefer a cohort-specific exact survivor-credit or durable-outcome receipt: set generic metadata and `famine_migration_presentation_input_resettlement_return_proven`, exact `..._people`, and exact `..._denominator`, then call `famine_migration_presentation_record_resettlement_return_projection` and refresh. Existing durable counters remain read-only fallback while their exact context flags are active. | Core state-history owner clears only on exact history retirement or reset with `famine_migration_presentation_clear_resettlement_return_projection`; ordinary cohort cleanup preserves durable history. State cleanup also calls `famine_migration_presentation_clear_all_projections`. |

The shared refresh wrapper is core `famine_migration_refresh_state_modifiers` (definition at current line 2546), which already calls the presentation refresh after the legacy refresh. Its current exact callsites are successful transfer destination/origin settlement at lines 1848 and 1851, reception-context update at line 2235, resettlement projection at line 2319, return projection at line 2339, recovered-state retirement at line 4038, food-security evaluation at line 4262, valid state-control change at line 5022, and valid nuclear-state change at line 5131. The parent/core owner must preserve this bounded state-scoped reachability and add the five new modifier removals to `famine_migration_clear_dynamic_modifiers` (definition at current line 2469).

The all-projection terminal clear belongs in `famine_migration_cleanup_state_registration` (definition at current line 2551) and must be reached by `common/on_actions/chaosx_famine_migration_on_actions.txt` `on_annex` line 62, invalid registered displacement/food state cleanup, `famine_migration_retire_recovered_state`, invalid state-control handling, and invalid nuclear-state handling. Routine refresh, a single role update, or a successful movement receipt must never clear another role's persisted projection. The exact cleanup effect names are the binding callsite contract because concurrent core edits can move line anchors.

## Migration from the prior static flow layer

The four food-stage modifiers remain unchanged.

The original five flow modifier identifiers remain stable for compatibility, but their enable/remove flags now use presentation-only flags and their fields read dynamic state variables.

Five narrow modifiers were added for preparing to leave, organized evacuation, depopulated districts, transit, and return readiness.

Six bounded projection record effects and six idempotent terminal clear effects were added for lifecycle persistence where no authoritative live ledger exists.

No population or route logic moved from core files.

## Risks, unsupported inputs, and blockers

The current core census does not expose an authoritative preparation amount, organized prepared/mission/request receipt, cumulative actual-origin-debit history, current hosted transit-load ledger, or exact return-readiness eligible-cohort amount, so those five phases remain absent until parent/core/decision owners provide exact record inputs. The presentation layer supplies the durable cumulative depopulation accumulator from exact transfer receipts but does not claim that the core ledger itself is cumulative.

The six presentation projection receipts solve lifecycle persistence but are not population authority and must never be used to debit, credit, kill, or reconcile population.

The active-exodus pair is presentation-only and must be equal and positive; any mismatch or missing side fails closed, even when one flight ledger is positive.

Some existing organized-evacuation requests do not set the core transfer role, so those callsites must provide the exact organized metadata bundle rather than relying on a completed transfer receipt.

The durable return/resettlement counters are exact projections but can be historical within an active context, so a parent should prefer the cohort-specific survivor-credit/durable-outcome receipt when overlapping cohort lifecycles make a cumulative fallback too broad.

The depopulated accumulator is safe only when the owner passes the core generation written after the successful exact debit. A caller must not synthesize a generation, reuse a stale generation for a new debit, or call the accumulator before `famine_migration_record_transfer_projection` has persisted the receipt.

The core `famine_migration_clear_dynamic_modifiers` effect does not yet remove the five new modifier identifiers; parent/core cleanup wiring remains required.

The installed HOI4 MCP inventory exposed no `hoi4.*modifier*`, `hoi4.*dynamic_modifier*`, or equivalent inspect/lint route for these definitions, so the handoff records source/documentation evidence rather than engine proof for this surface.

No GUI, map, event, focus, or probability MCP route applied to this ownership tranche, and no source-only inspection is claimed as engine proof for those unsupported surfaces.

No Hearts of Iron IV process was launched, and no live save validation was performed.

## Validation evidence

The scripted effect file has balanced braces after adding six projection record effects, six terminal clear effects, and the refresh integration branches.

The depopulated record was self-reviewed against the core receipt order: it accepts only a positive actual debit and positive generation, adds a generation once, preserves the first positive pre-debit denominator, stores the latest exact metadata, and clears its generation key only through the explicit history clear.

The preparing record and refresh path were self-reviewed to allow a missing or zero cohort id while retaining positive generation and role proof.

The dynamic modifier file has balanced braces and ten flow identifiers that match the refresh and clear callsites.

All new dynamic modifier fields were compared with vanilla dynamic-modifier precedents for `state_production_speed_buildings_factor`, `army_speed_factor_for_controller`, `local_supplies`, `attrition_for_controller`, `local_non_core_manpower`, and `local_building_slots_factor`.

Vanilla documentation gives `local_manpower` zero decimal places, so the presentation layer does not apply a 0..1 share to that flat field. It uses the two-decimal `local_non_core_manpower` ratio with the dynamic `local_building_slots_factor`; the flat `local_building_slots` field is also avoided.

All new constants are in `common/script_constants/` and all references resolve to either the new `famine_migration_presentation` category, the existing `famine_migration_modifier` category, or the existing `famine_migration_core_reconciliation` role category.

The localisation file retained its UTF-8 BOM after the five title/description additions.

The existing exodus, reception, overcrowded, trapped-border, and return icon definitions were inspected and reused; no asset request or asset edit was made.

The matching effect documentation records scope, inputs, outputs, defaults, side effects, persistent lifecycle, role separation, cleanup, and fail-closed behavior.
