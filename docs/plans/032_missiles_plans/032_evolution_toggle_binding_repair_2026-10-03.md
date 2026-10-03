# Event 032 evolution toggle binding repair

Disposition: accepted and queued.
Acceptance basis: the user's full Event 32 contract requires separate evolution enable gates and safe disabled behavior for all five tracks.
The implementation change waits for the required read-only probability baseline and same-scenario comparison.
The auditor was dispatched before any binding change, but its runtime returned `workspace routing discovery timed out` and has been asked to resume.

## Source finding

`events_log_toggle_current_evolution_disabled` in `common/scripted_effects/chaosx_events_log_effects.txt` writes `events_log_disabled_evolution_[EVOLUTION_EVENT_ID]_[EVOLUTION_TYPE]_[EVOLUTION_STAGE]`.
Event 32's `missiles_record_evolution_unlock` records event `32`, types `1` through `5`, and stage `1`.
The current Event 32 gates instead read `event_evolution_disabled_32_1` through `event_evolution_disabled_32_5`, which are not the flags written by the shared toggle.
This can leave disabled tracks eligible for adoption, incident and guidance branches, scenario setup, and achievement credit.

## Exact binding correction

| Track | Current read | Shared toggle read |
| --- | --- | --- |
| Saturation Arsenals | `event_evolution_disabled_32_1` | `events_log_disabled_evolution_32_1_1` |
| Unreliable Guidance | `event_evolution_disabled_32_2` | `events_log_disabled_evolution_32_2_1` |
| Special Warheads | `event_evolution_disabled_32_3` | `events_log_disabled_evolution_32_3_1` |
| Rogue Launch Commands | `event_evolution_disabled_32_4` | `events_log_disabled_evolution_32_4_1` |
| Automatic Retaliation | `event_evolution_disabled_32_5` | `events_log_disabled_evolution_32_5_1` |

Preserve all numeric weights, tuning constants, resource costs, site custody, existing unlock receipts, and Event Logs ownership.
Replace only the Event 32 disabled-gate bindings in its operation, scenario, achievement, and trigger surfaces.
Check that pending schedules clear when their track is disabled, the default blocked paths remain safe after adoption, and no disable or re-enable invents missiles or payload inventory.

## Evidence and validation gate

Immutable before sources are stored in `docs/plans/032_missiles_plans/baselines/2026-10-03_evolution_gates/`.
The exact source set is `032_missiles_operations_effects.txt`, `032_missiles_achievement_effects.txt`, `032_missiles_scenario_effects.txt`, `032_missiles_triggers.txt`, and `032_missiles_scenario_triggers.txt`.
Use `EVO-10`, `EVO-11`, and `EVO-12` from the accepted matrix, including the actual canonical shared flags, for the baseline and after comparison.
The read-only auditor must preserve the scenario fixture and compare each exact before source with its current owning path.
Any unresolved flag, scope, eligibility, or candidate-pool binding remains an evidence gap.
Source matching and unchanged weight tokens cannot substitute for that comparison.
