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
| `famine_register_state_in_runtime` | Exact valid state. | Idempotent membership/count in existing `global.famine_active_states`, temporary registry result. | Common insertion only. Sets no state/category/phase activation. Used by ordinary registration and pending observation enqueue. |
| `famine_register_active_state` | Exact valid state under an ordinary famine owner. | Existing simulation-active flag and registry result. | Retains ordinary registration and candidate-capacity dirty marking after common insertion. |
| `famine_enqueue_food_observation_assessment` | Exact valid state with a genuine material assessment. | Existing sparse registry membership and `famine_food_observation_pending_job` only when simulation is not already active. | No query-caused active/category flags. `famine_process_registered_state` consumes the pending job before ordinary activation/evaluation. Cleanup clears pending markers. |

Stored famine dates are copies of `global.date`, which counts one game hour as 0.00001.
Day counts therefore pass through the shared `chaosx_convert_days_to_date_offset` helper before they are added to a date, and date differences are compared with converted thresholds or turned back into days with `chaosx_convert_date_offset_to_days`.
`famine_schedule_next_mortality_date` (state scope, input temporary `famine_mortality_interval` in days) sets `famine_food_next_mortality_date`.
`famine_set_mission_relief_deadline` and `famine_set_mission_route_hold_deadline` (state scope, no inputs) set the relief and route-hold mission deadlines from `famine_mission_timing`.
Stage candidate and recovery timers compare the elapsed date difference with the converted day threshold, and `famine_food_exposure_days` stores whole elapsed days.

Temporary return fields must be declared in the caller before invoking the shared helper so their lifetime spans the parent effect chain.
The evaluator and observer declare `famine_food_reserve_score_relief_output`, `famine_food_score_raw` and `famine_requested_food_stage` before the relevant calls, and each helper that sums components declares `famine_food_pressure_sum` itself.

Reserve ledger rules used by the evaluator (`famine_refresh_reserve_capacity`, `famine_update_reserve`):

- The first refresh of a state with no initialized reserve seeds `initial_target_share` of its target, unless an owner supplied a proven initial amount or the save already holds positive stock.
- Each day the reserve is drawn by the stage share of the previous `famine_food_deficit_score` (25, 50, 75 or 100 percent of daily need from supply strain to catastrophic famine), and by at least `blockade_import_share` while `famine_blockade_isolation_proof` holds.
- Only a stable state with no shortage replenishes toward target.
- `famine_state_can_retire` keeps a state registered while its stored deficit is at supply strain or above.

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
