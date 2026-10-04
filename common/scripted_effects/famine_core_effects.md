# Famine core calculation helpers

The state simulation and the famine-owned destination observer share these calculation helpers.
They retain the existing component weights, bounds, score formula and stage thresholds from `famine_core_constants.txt`.
Simulation clocks, stock mutation, stage commits, mortality, flight and presentation remain in their existing owners.

| Helper | Scope and inputs | Outputs/defaults | Side effects and call sites |
| --- | --- | --- | --- |
| `famine_rebuild_food_components` | State with initialized `famine_input_*`, `famine_profile_*`, food pressure, current `famine_external_*` collector outputs and optional proven reception-demand population. | Rebuilds the eight bounded normal `famine_component_*` fields. Reception demand defaults to zero when no positive demand is present. | Changes components only. Used by `famine_evaluate_food_security` and `famine_observe_migration_food_context`. |
| `famine_apply_existing_reserve_relief` | State with existing reserve amount, daily need and transient reserve-relief fields. | Adds bounded stock/transient relief to the current relief component and returns temporary `famine_food_reserve_score_relief_output`. Non-positive daily need contributes no stock-days relief. | Never creates or changes stock. The ordinary evaluator calls `famine_update_reserve` first. Observation reads the existing values. |
| `famine_calculate_food_score` | State with the eight current components. | Writes normal `famine_food_security_score`, temporary `famine_food_score_raw` and temporary `famine_requested_food_stage`. The requested stage begins at stable and follows existing thresholds. | Calculation only. It neither commits a stage nor changes candidate/recovery/exposure/mortality timers. Both evaluator and observer use it. |
| `famine_apply_current_blockade_components` | State after current blockade proof, with existing blockade exposure. | Adds existing constant-backed transport/need pressure and bounded duration pressure only when the full proof passes. | Does not advance or reset blockade exposure. Used by observation and the ordinary simulation wrapper. |
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
The evaluator and observer declare `famine_food_reserve_score_relief_output`, `famine_food_score_raw` and `famine_requested_food_stage` before the relevant calls.

Example, after initializing owner facts and collecting current context:

```text
famine_rebuild_food_components = yes
set_temp_variable = { famine_food_reserve_score_relief_output = constant:famine_food_reserve.zero }
famine_apply_existing_reserve_relief = yes
famine_refresh_blockade_proof = yes
famine_apply_relief_access_components = yes
famine_apply_current_blockade_components = yes
set_temp_variable = { famine_food_score_raw = constant:famine_food_score.zero }
set_temp_variable = { famine_requested_food_stage = constant:famine_food_stage.stable }
famine_calculate_food_score = yes
```

This example does not update reserves or advance a simulation stage.
Use the public observer contract documented in `famine_adapter_effects.md` for destination assessment, and retain the full evaluator for ordinary registered simulation.
