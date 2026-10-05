# Famine core calculation helpers

The state simulation and the famine-owned destination observer share these calculation helpers.
They read the component weights, bounds, score normalizer, reserve and stage thresholds from `famine_core_constants.txt`.
Simulation clocks, stock mutation, stage commits, mortality, flight and presentation remain in their existing owners.

| Helper | Scope and inputs | Outputs/defaults | Side effects and call sites |
| --- | --- | --- | --- |
| `famine_rebuild_food_components` | State with initialized `famine_input_*`, `famine_profile_*`, food pressure, current `famine_external_*` collector outputs and optional proven reception-demand population. | Rebuilds the eight bounded normal `famine_component_*` fields. Reception demand defaults to zero when no positive demand is present. | Changes components only. Used by `famine_evaluate_food_security` and `famine_observe_migration_food_context`. |
| `famine_apply_existing_reserve_relief` | State with existing reserve amount, daily need and transient reserve-relief fields. | Adds bounded stock/transient relief to the current relief component and returns temporary `famine_food_reserve_score_relief_output`. Non-positive daily need contributes no stock-days relief. | Never creates or changes stock. The ordinary evaluator calls `famine_update_reserve` first. Observation reads the existing values. |
| `famine_sum_food_pressure_components` | State with the seven pressure components. | Temporary `famine_food_pressure_sum`, the weighted sum before relief; the caller declares it first. | Calculation only. Shared by the exhaustion helper and the score. |
| `famine_apply_reserve_exhaustion` | State after components, blockade and relief access are applied. | Stores `famine_food_deficit_score` (weighted sum divided by `pressure_normalizer`, before relief and before exhaustion) and `famine_food_exhaustion_need`. When the reserve ledger is initialized, the deficit reaches supply strain or the island blockade is proven, and the reserve covers fewer than `exhaustion_reserve_days` days, it adds `exhaustion_need_maximum` times the missing share of those days to unmet need. Food already released for rationing (`famine_food_reserve_relief` divided by `relief_per_day_covered`) counts as covered days. | Changes the need component and the two stored values only. Both evaluator and observer call it before the score; an observed state without a reserve ledger only stores the deficit. |
| `famine_calculate_food_score` | State with the eight current components. | Writes normal `famine_food_security_score`, temporary `famine_food_score_raw` and temporary `famine_requested_food_stage`. The score is `clamp((weighted sum - 1.20 * relief) / pressure_normalizer, 0, 200)`, and the requested stage follows the 25, 50, 75 and 100 thresholds. | Calculation only. It neither commits a stage nor changes candidate/recovery/exposure/mortality timers. Both evaluator and observer use it; the evaluator then limits the request to one stage above or below the committed stage. |
| `famine_apply_current_blockade_components` | State after current blockade proof, with existing blockade exposure. | Adds constant-backed transport/need pressure and bounded duration pressure, and the duration pressure times `duration_vulnerability_share` to vulnerability, only when the full proof passes. | Does not advance or reset blockade exposure. Used by observation and the ordinary simulation wrapper. |
| `famine_apply_blockade_components` | Registered simulation state after blockade proof. | Advances one isolation day and calls `famine_apply_current_blockade_components`, or resets exposure when proof fails. | Retains the existing simulation clock and blockade source attribution. Observation never invokes this wrapper. |
| `famine_resolve_local_war_evidence` | State, after `famine_resolve_occupation_profile` (reads its temporary `famine_occupation_profile`). | Temporary `famine_local_war_evidence`, one when the state's controller is at war and the state is occupied, borders a state held by an enemy of its controller, is under a harsher-than-standard occupation rule, passes `famine_blockade_isolation_proof`, or has proven local supply failure. For the two Bengal anchors it also holds when a neighbouring Bengal anchor borders a state held by an enemy of the controller (Bengal is one food region fed through Burma). Zero otherwise. | Saves the regular event target `famine_local_war_controller` and changes nothing else. Called by the surface collector, historical selector, and selected profile mapper. The eight historical-window crisis profiles (Henan 1942, Bengal, Vietnam, Java, Greece, Leningrad, Dutch Hunger Winter, Spain) require this local cause instead of a war elsewhere. |
| `famine_register_state_in_runtime` | Exact valid state. | Idempotent membership/count in existing `global.famine_active_states`, temporary registry result. | Common insertion only. Sets no state/category/phase activation. Used by ordinary registration and pending observation enqueue. |
| `famine_register_active_state` | Exact valid state under an ordinary famine owner. | Existing simulation-active flag and registry result. | Retains ordinary registration and candidate-capacity dirty marking after common insertion. |
| `famine_enqueue_food_observation_assessment` | Exact valid state with a genuine material assessment. | Existing sparse registry membership and `famine_food_observation_pending_job` only when simulation is not already active. | No query-caused active/category flags. `famine_process_registered_state` consumes the pending job before ordinary activation/evaluation. Cleanup clears pending markers. |

Stored famine dates are copies of `global.date`, which counts one game hour as 0.00001.
Day counts therefore pass through the shared `chaosx_convert_days_to_date_offset` helper before they are added to a date, and date differences are compared with converted thresholds or turned back into days with `chaosx_convert_date_offset_to_days`.
`famine_schedule_next_mortality_date` (state scope, input temporary `famine_mortality_interval` in days) sets `famine_food_next_mortality_date`.
`famine_set_mission_relief_deadline` and `famine_set_mission_route_hold_deadline` (state scope, no inputs) set the relief and route-hold mission deadlines from `famine_mission_timing`.
Stage candidate and recovery timers compare the elapsed date difference with the converted day threshold, and `famine_food_exposure_days` stores whole elapsed days.

`famine_collect_surface_context` resolves occupation and local-war evidence for its exact STATE before collecting the current pressure components.
It adds war transport 8 and unmet need 4 only when local-war evidence holds and both owner and controller are at war.
The observer uses the same calculation without granting stock, advancing clocks, or committing a stage.
An accepted outbreak food request contributes production 20, transport 20, vulnerability 20, and environment 10 until `famine_outbreak_context_until_date`.
An accepted disaster or Acid Rain food request contributes production 30, transport 15, and need 20 until `famine_disaster_context_until_date`.
Those windows last 30 and 60 days respectively, using `famine_surface_context` constants and the shared date converter.
Repeated accepted requests extend the corresponding date without stacking a second contribution.
The collector ignores a context at or after its expiry, and `famine_cleanup_state_registration` clears both dates on retirement.
The standalone unrelieved outbreak and disaster component totals each score 28.4 before current stock relief, shock, exhaustion, or other causes.
Local-war components alone score 5.2, below the supply-strain threshold of 25.
These are source calculations, not observed campaign timing.

The China policy, Ceara, and Congo profile selector and mapper use the same cause gates documented in `famine_core_triggers.md`.
All three require positive current food pressure, their existing regional ownership/control, and a present cause.
Their anchor IDs, profile component tables, and stage thresholds stay in the existing tuning tables.
A peaceful zero-pressure anchor never activates one of these profiles by date alone.

Temporary return fields must be declared in the caller before invoking the shared helper so their lifetime spans the parent effect chain.
The evaluator and observer declare `famine_food_reserve_score_relief_output`, `famine_food_score_raw` and `famine_requested_food_stage` before the relevant calls, and each helper that sums components declares `famine_food_pressure_sum` itself.

`famine_select_historical_profile_id` and `famine_resolve_historical_profile_context` declare `famine_occupation_profile = constant:famine_occupation_profile.none` before resolving occupation conduct.
The selector declares `famine_local_war_evidence = constant:humanitarian_runtime.zero` before resolving local war.
Any surface collector that invokes the local-war resolver must do the same in its own call frame.
`famine_apply_historical_profile_context` declares both `famine_historical_profile_state_proven` and `famine_historical_profile_context_proven` as zero before calling the profile resolver.
These are temporary outputs, with no scope prefix, and cannot be replaced by declarations first made in the returning helper.

Stage escalation and recovery require uninterrupted qualifying conditions.
An upward candidate clears the recovery clock, and a downward candidate clears the escalation clock, so a change of direction cannot reuse elapsed time from an earlier attempt.
Each accepted step consumes its qualifying clock, and state retirement clears both clocks so dormant time cannot count toward a later crisis.

Reserve ledger rules used by the evaluator (`famine_refresh_reserve_capacity`, `famine_update_reserve`):

- The first refresh of a state with no initialized reserve seeds `initial_target_share` of its target, unless an owner supplied a proven initial amount or the save already holds positive stock.
- Each day the reserve is drawn by the stage share of the previous `famine_food_deficit_score` (25, 50, 75 or 100 percent of daily need from supply strain to catastrophic famine), and by at least `blockade_import_share` while `famine_blockade_isolation_proof` holds.
- Only a stable state with no shortage replenishes toward target.
- `famine_state_can_retire` keeps a state registered while its stored deficit is at supply strain or above.

`famine_consume_reserve_for_relief` converts the remaining rationing-relief capacity into a stock amount before debiting.
It floors the accepted amount to whole reserve units, preserves unused stores, and reports zero consumed stock when no rationing capacity remains.
The release decision declares its consumed/result/relief outputs before the wrapper call and returns its paid political power, support equipment, and fuel only when the measured stock debit is zero.
That refund sits inside the exact paid-work branch, after consuming its payment marker, so a repeated callback cannot refund again.

The relief delivery wrapper declares the reserve transfer's result, source debit, and destination credit before calling `famine_transfer_reserves`.
The corridor relief wrapper declares `famine_relief_delivery_result` before calling that delivery owner.
Measured food delivery therefore remains available through both nested return boundaries, with population and Deaths accounting untouched.
Delivery copies stay temporary throughout the donor-to-recipient scope change, and the recipient's durable last-delivery amounts read those unscoped returns rather than unrelated donor variables.

Example, after initializing owner facts and collecting current context:

```text
famine_rebuild_food_components = yes
set_temp_variable = { famine_food_reserve_score_relief_output = constant:famine_food_reserve.zero }
famine_apply_existing_reserve_relief = yes
famine_refresh_blockade_proof = yes
famine_apply_relief_access_components = yes
famine_apply_current_blockade_components = yes
famine_apply_reserve_exhaustion = yes
set_temp_variable = { famine_food_score_raw = constant:famine_food_score.zero }
set_temp_variable = { famine_requested_food_stage = constant:famine_food_stage.stable }
famine_calculate_food_score = yes
```

This example does not update reserves or advance a simulation stage.
Use the public observer contract documented in `famine_adapter_effects.md` for destination assessment, and retain the full evaluator for ordinary registered simulation.
