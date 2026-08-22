# Persistent food-reserve ledger handoff

## Scope and files

This tranche adds a sparse state-owned reserve ledger to the existing famine and migration food evaluator.

Changed gameplay files are `common/script_constants/famine_migration_constants.txt`, `common/scripted_effects/chaosx_famine_migration_effects.txt`, and `common/scripted_triggers/chaosx_famine_migration_triggers.txt`.

Changed public-contract documentation is `common/scripted_effects/chaosx_dynamic_effects.md` and `docs/systems/famine_and_migration_system.md`.

The CXT contract was reviewed against the current repository guidance; no duplicate carrier or setup effect was added because the existing bounded `famine_migration_register_cxt_test_content` fixture already owns this general-system test registration.

No decisions, localisation, mapmodes, achievements, adapters, on-actions, assets, spreadsheets, specs, population effects, cohort arrays, or civilian transfer/update helpers were edited.

## Supporting-input boundary and initial causality

The reserve is intentionally a bounded supporting input rather than a second detailed economic simulator or global stockpile.

Each active state stores one aggregate amount, capacity, target, daily need, logistics factor, date guard, bounded last-day deltas, and cumulative transaction totals; there are no goods types, prices, factories, national stockpiles, market flows, per-province rows, or world iteration.

The existing host-only runtime coordinator reaches the reserve only through the already-registered active food-state array, so work remains proportional to active entries.

Reserve units are thousand-person-days, which makes the state population and logistics relationship explicit without modifying the population ledger or using raw-person values that can overflow.

The ledger does not silently invent an opening stockpile.

The first refresh requires a positive `famine_migration_food_reserve_initial_amount` plus `famine_migration_food_reserve_initialization_proven > 0`, or a positive amount already present in a save, before setting `famine_migration_food_reserve_initialized`.

A zero amount remains zero until a proven initial allocation or an explicit import helper accepts stock.

This fail-closed initialization is deliberate because no vanilla state-level food-stock carrier was identified in the scoped effect/triggers documentation, and assigning a fixed percentage of target would assert an unowned economic fact.

## Central constants and formulas

All reserve tuning is centralized under `famine_migration_food_reserve` in `common/script_constants/famine_migration_constants.txt`.

The current constants are `daily_need_per_k = 1.00`, `capacity_days = 45.00`, `target_days = 30.00`, logistics base/per-infrastructure/minimum/maximum `0.50/0.10/0.25/1.25`, transport and production capacity penalties `0.003/0.002`, replenishment rate `0.15`, replenishment minimum factor `0.10`, depletion minimum factor `0.25`, stage depletion shares `0.05/0.20/0.50/1.00`, relief per covered day `1.50`, relief maximum `35.00`, and relief decay `0.50` per day.

For a valid state, `daily_need = round(max(1, state_population_k * daily_need_per_k))`.

`logistics_factor = clamp(logistics_factor_base + infrastructure_level * logistics_factor_per_infrastructure - component_transport * transport_capacity_penalty - component_production * production_capacity_penalty, logistics_factor_minimum, logistics_factor_maximum)`.

`capacity = round(max(1, daily_need * capacity_days * logistics_factor))`.

`target = min(capacity, round(max(1, daily_need * target_days * logistics_factor)))`.

Initialized stable replenishment is `min(target - amount, round(daily_need * replenishment_per_k_per_day * max(replenishment_factor_minimum, 1 - component_production / 100) * max(replenishment_factor_minimum, 1 - component_transport / 100) * logistics_factor))`; an uninitialized zero ledger does not self-create stock.

Active depletion is `min(amount, round(daily_need * stage_depletion_share * max(depletion_factor_minimum, component_need / 100)))`.

Evaluator relief is `clamp((amount / daily_need) * relief_per_day_covered + famine_migration_food_reserve_relief, 0, relief_maximum)` and is added to the existing normalized relief component before the existing weighted score composition.

## Persistent variables and lifecycle

`famine_migration_initialize_food_state` initializes the following state variables without touching population: `famine_migration_food_reserve_amount`, `famine_migration_food_reserve_initial_amount`, `famine_migration_food_reserve_initialization_proven`, `famine_migration_food_reserve_capacity`, `famine_migration_food_reserve_target`, `famine_migration_food_reserve_daily_need`, `famine_migration_food_reserve_logistics_factor`, `famine_migration_food_reserve_relief`, `famine_migration_food_reserve_last_update_date`, `famine_migration_food_reserve_last_replenished`, `famine_migration_food_reserve_last_depleted`, `famine_migration_food_reserve_last_imported`, `famine_migration_food_reserve_last_consumed`, `famine_migration_food_reserve_last_transfer_in`, `famine_migration_food_reserve_last_transfer_out`, `famine_migration_food_reserve_total_replenished`, `famine_migration_food_reserve_total_depleted`, `famine_migration_food_reserve_total_imported`, `famine_migration_food_reserve_total_consumed`, `famine_migration_food_reserve_total_transfer_in`, and `famine_migration_food_reserve_total_transfer_out`.

The `famine_migration_food_reserve_initialized` state flag is set only after proven initial amount or an existing positive amount is observed.

`famine_migration_update_food_reserve` records `famine_migration_food_reserve_last_update_date` and therefore runs replenishment, depletion, and relief decay at most once for a game date.

State registration cleanup intentionally leaves reserve amount, capacity, target, initialization flag, date guard, cumulative reserve totals, and historical/population ledgers intact.

## Helper contracts

### `famine_migration_refresh_food_reserve_capacity`

Scope: valid state.

Inputs: live `state_population_k`, `infrastructure_level`, and already-composed `famine_migration_component_production` and `famine_migration_component_transport` values.

Outputs: temporary `famine_migration_food_reserve_refresh_result`, `famine_migration_food_reserve_capacity_output`, `famine_migration_food_reserve_target_output`, `famine_migration_food_reserve_amount_output`, `famine_migration_food_reserve_daily_need_output`, and `famine_migration_food_reserve_logistics_factor_output`.

Side effects: writes capacity, target, need, and logistics fields; may set the initialization flag only under the proven conditions above; never changes population.

### `famine_migration_update_food_reserve`

Scope: valid state already reached through the active-food registry.

Inputs: refreshed reserve fields, current food stage, current normalized production/transport/need components, and `global.date`.

Outputs: temporary `famine_migration_food_reserve_update_result`, `famine_migration_food_reserve_replenished_output`, `famine_migration_food_reserve_depleted_output`, `famine_migration_food_reserve_amount_output`, `famine_migration_food_reserve_daily_need_output`, and `famine_migration_food_reserve_relief_output`.

Side effects: one date-guarded replenishment or depletion, relief decay, last-day deltas, and cumulative totals.

### `famine_migration_consume_food_reserve_for_relief`

Scope: state.

Inputs: positive `famine_migration_food_reserve_release_amount`, `famine_migration_food_reserve_release_request_proven > 0`, and `famine_migration_food_reserve_release_actor_proven > 0`.

Outputs: temporary `famine_migration_food_reserve_consume_result`, `famine_migration_food_reserve_consumed_output`, `famine_migration_food_reserve_relief_granted_output`, and `famine_migration_food_reserve_remaining_output`.

Side effects: debits only actual available amount, increments the consumed total, adds bounded transient relief, and clears one-shot request/proof variables.

Public aliases: `famine_migration_release_food_reserves` and `famine_migration_consume_food_reserves_as_relief`.

### `famine_migration_add_food_reserves`

Scope: state.

Inputs: positive `famine_migration_food_reserve_import_amount`, `famine_migration_food_reserve_import_request_proven > 0`, `famine_migration_food_reserve_import_source_proven > 0`, and `famine_migration_food_reserve_import_actor_proven > 0`.

Outputs: temporary `famine_migration_food_reserve_add_result`, `famine_migration_food_reserve_added_output`, `famine_migration_food_reserve_remaining_output`, and `famine_migration_food_reserve_capacity_output`.

Side effects: credits only free capacity, records the accepted amount in imported totals, and clears one-shot request/proof variables.

Public alias: `famine_migration_import_food_reserves`.

### `famine_migration_transfer_food_reserves`

Scope: source state.

Inputs: positive `famine_migration_food_reserve_transfer_amount`, `famine_migration_food_reserve_transfer_request_proven > 0`, `famine_migration_food_reserve_transfer_route_proven > 0`, `famine_migration_food_reserve_transfer_actor_proven > 0`, and a distinct valid regular event target `famine_migration_food_reserve_destination`.

Outputs: temporary `famine_migration_food_reserve_transfer_result`, `famine_migration_food_reserve_transfer_source_debit_output`, `famine_migration_food_reserve_transfer_destination_credit_output`, and `famine_migration_food_reserve_transfer_remaining_output`.

Side effects: debits source and credits destination exactly once, records matching transfer totals only after conservation succeeds, and clears one-shot request/proof variables.

Public alias: `famine_migration_requisition_food_reserves`.

## Conservation proof

The source effect refreshes both states, computes `accepted = min(request, source amount, destination free capacity)`, and performs one source subtraction and one destination addition using that same accepted amount.

The source debit is measured as `source_before - source_after` and the destination credit as `destination_after - destination_before`.

The residual `source_debit - destination_credit` is checked after mutation.

A positive residual restores source stock, while a negative residual removes only the excess destination credit through a negated temporary amount; cumulative transfer totals are not advanced until the residual equals zero.

The successful result therefore proves `source_debit = destination_credit`, `source_total_transfer_out` increases by that exact debit, and `destination_total_transfer_in` increases by that exact credit.

No population, manpower, food pressure, cohort row, or global array is touched by this reserve transfer.

## Decision integration contract

Owner decisions remain responsible for choosing costs, actor authority, route/source proof, and player-facing localisation.

Before calling a public alias, an owner decision must set the matching amount and proof bundle in the actual state scope and, for transfer, save the actual destination as the regular event target.

After the alias returns, the owner reads the temporary result and accepted amount outputs in the same effect chain and records any decision-specific cost or outcome exactly once.

The owner must not write `famine_migration_food_reserve_amount` or cumulative totals directly.

The current tranche does not edit decision files, AI weights, localisation, or GUI surfaces; those consumers remain parent-owned follow-up work.

## Validation and blockers

Static validation reviewed the touched effect and trigger blocks, confirmed balanced Clausewitz braces, checked that no unsupported `<=` or `>=` operators or unary variable negation were introduced, checked helper-name uniqueness, and reviewed the diff for scope ownership.

The required offline wiki and vanilla documentation review covered data structures, triggers, effects, modifiers, localisation, scopes, on-actions, event/decision/idea/AI modding, script constants, dynamic variables, event targets, `state_population_k`, infrastructure, variable arithmetic, and rounding/clamping precedents.

No weighted or probability-bearing helper was added, so the probability-inspection route was not applicable.

No focus, GUI, map, or event surface was changed, so no linked-surface MCP inspection was applicable.

Live game load/save and decision consumer validation remain parent-owned because this tranche does not launch Hearts of Iron IV and does not edit decisions.

The main semantic blocker is the absence of a vanilla state-level food-stock carrier in the scoped APIs; initialization therefore fails closed instead of asserting a 75 percent target fill. A decision or adapter owner must provide proven initial amount or import causality before reserve release can produce stock relief.

No population mutation, CXT carrier duplication, global scan, second economic simulator, or fallback stock assertion was added.
