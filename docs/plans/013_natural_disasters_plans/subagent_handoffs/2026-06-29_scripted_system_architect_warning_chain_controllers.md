# Event 13 scripted warning and chain controller handoff

## Scope

Implemented the focused scripted-system blockers from `2026-06-29_event013_focused_improvement_addendum.md` for Event 13 Natural Disasters.

This handoff covers only warning capacity logic, Evolution II and III chain controllers, constants, flags, variables, and cleanup in the allowed scripted files.

## Files changed by this pass

- `events/013_natural_disasters.txt`
- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-06-29_scripted_system_architect_warning_chain_controllers.md`

`common/scripted_triggers/013_natural_disasters_triggers.txt` was inspected because it is used by target selection. No new trigger identifier was required for the chain-controller work in this pass.

## Warning helper map

| Helper | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `natural_disasters_prepare_warning_score_for_current_target` | State | Current family, current evolution, owner state, control, infrastructure, radar or anti-air, airbase, coastal or port access, active aftermath, owner war state, stability, preparedness actions, radio tech, maximum barrage flag | Writes and clamps `natural_disaster_warning_score`. |
| `natural_disasters_roll_warning_for_current_target` | State | `natural_disaster_warning_score`, random roll constants | Sets `natural_disaster_warning_available` on success, or applies missed-warning penalty on failure. Writes owner `natural_disasters_current_incident_has_warning`. |
| `natural_disasters_apply_missed_warning_penalty` | State | Failed warning roll | Sets `natural_disaster_warning_missed`, clears warning availability, and raises impact aftermath multiplier through the existing Event 13 impact path. |
| `natural_disasters_prepare_warning_outcome` | Country | Current target state mark | Runs the target-state warning roll instead of fixed family and evolution odds. |

## Chain helper map

| Helper | Scope | Purpose |
| --- | --- | --- |
| `natural_disasters_start_delayed_tsunami_chain_from_state` | State | Saves the anchor state and schedules the delayed tsunami warning controller. |
| `natural_disasters_start_storm_corridor_chain_from_state` | State | Starts a moving storm corridor chain from the abnormal corridor anchor. |
| `natural_disasters_start_meteor_cluster_chain_from_state` | State | Starts a meteor cluster, records planned and actual impact counts, and enables meteor command support. |
| `natural_disasters_start_rupture_wave_chain_from_state` | State | Starts a massive rupture wave with neighbor-state follow-up impacts and optional tsunami continuation. |
| `natural_disasters_start_massive_eruption_chain_from_state` | State | Starts a massive eruption chain with ashfall and lahar follow-up behavior and optional tsunami continuation. |
| `natural_disasters_maybe_start_chain_from_state` | State | Selects the proper chain after a current impact is dispatched. |
| `natural_disasters_prepare_neighbor_chain_target` | Country | Scores neighbor states around the anchor, then falls back to owned matching states if needed. |
| `natural_disasters_prepare_scored_chain_target` | Country | Uses normal Event 13 target scoring for same-country chain targets. |
| `natural_disasters_apply_chain_current_target_impact` | Country | Applies the existing family impact dispatch to the current chain target and keeps deaths on the Event 13 dynamic path. |
| `natural_disasters_tick_active_chain_counter` | Country | Advances stage and decrements remaining chain impacts through constants. |
| `natural_disasters_complete_active_chain` | Country | Clears chain context, or pivots rupture and eruption chains into delayed tsunami when the pending flag is set. |
| `natural_disasters_continue_rupture_wave_chain` | Country | Applies the massive rupture wave follow-up controller. |
| `natural_disasters_continue_storm_corridor_chain` | Country | Moves corridor storms across scored neighbor targets. |
| `natural_disasters_continue_meteor_cluster_chain` | Country | Applies additional meteor impacts and command flag escalation. |
| `natural_disasters_continue_eruption_ashfall_chain` | Country | Applies massive eruption follow-up, then switches later ticks to landslide and lahar behavior. |
| `natural_disasters_prepare_delayed_tsunami_warning` | Country | Selects a tsunami target, marks a forecast state, opens the warning window, and schedules impact. |
| `natural_disasters_apply_delayed_tsunami_impact` | Country | Applies delayed tsunami impact through existing dispatch and cleanup. |
| `natural_disasters_continue_active_chain_controller` | Country | Dispatches the hidden rupture wave controller. |
| `natural_disasters_clear_chain_state_marks` | Country | Clears anchor, forecast, impacted, and secondary chain state flags. |
| `natural_disasters_clear_active_chain_context` | Country | Clears active chain flags, variables, meteor counters, and chain state marks. |

## Event controllers added

- `chaosx.nr13.40`: hidden country event for the massive rupture wave controller.
- `chaosx.nr13.41`: hidden country event for delayed tsunami warning preparation.
- `chaosx.nr13.42`: hidden state event for delayed tsunami impact.
- `chaosx.nr13.43`: hidden country event for moving storm corridor ticks.
- `chaosx.nr13.44`: hidden country event for meteor cluster ticks.
- `chaosx.nr13.45`: hidden country event for massive eruption, ashfall, and lahar ticks.

The normal hidden scheduler `chaosx.nr13.10` now waits while `natural_disasters_chain_active` is set, so chain controllers do not race a new normal incident.

## Constants added

- `natural_disasters_warning_score`
- `natural_disasters_warning_threshold`
- `natural_disasters_chain_type`
- `natural_disasters_chain`
- `natural_disasters_preparedness_multiplier.missed_warning`

## Flags, variables, and event targets

Country flags:

- `natural_disasters_chain_active`
- `natural_disasters_pending_tsunami_chain`

State flags:

- `natural_disaster_warning_missed`
- `natural_disaster_chain_anchor`
- `natural_disaster_chain_forecast_state`
- `natural_disaster_chain_impacted_state`
- `natural_disaster_chain_secondary_state`

Country variables:

- `natural_disasters_active_chain_family`
- `natural_disasters_active_chain_type`
- `natural_disasters_chain_stage`
- `natural_disasters_chain_remaining`
- `natural_disasters_chain_warning_quality`
- `natural_disasters_chain_anchor_state_score`
- `natural_disasters_meteor_cluster_impacts`
- `natural_disasters_meteor_cluster_planned_impacts`

State variables:

- `natural_disaster_warning_score`
- `natural_disaster_warning_roll`

Event target:

- `natural_disaster_chain_anchor` is a regular event target created with `save_event_target_as`. No global event target was added.

## Cleanup

State aftermath cleanup now clears warning availability, missed-warning state, chain state flags, and warning score or roll variables.

Sequence cleanup now clears active chain country flags, chain variables, meteor counters, and chain state marks through `natural_disasters_clear_active_chain_context`.

## Validation

- Checked the allowed Event 13 scripted files for unsupported `<=` or `>=`.
- Checked the allowed Event 13 scripted files for added `on_daily`, `on_weekly`, or `on_monthly` iteration.
- Checked `events/` for duplicate `chaosx.nr13.40` through `chaosx.nr13.45` event ids.
- Ran `git diff --check` on the touched scripted files and this handoff.
- Ran brace-balance checks on the touched Event 13 script files.

## Remaining risks

- The controllers are script-wired but still need live-session verification for pacing, warning display timing, and edge cases where no valid neighbor target exists.
- The warning score uses existing HOI4 state building checks and existing Event 13 preparedness variables. It does not add a new observatory building or decision surface because those were outside scope.
- The moving storm, rupture, meteor, eruption, and tsunami chains continue to use the existing Event 13 dynamic impact and death path. No new casualty route was added.
- No decisions, achievements, news, spreadsheet, assets, or system docs were touched.
