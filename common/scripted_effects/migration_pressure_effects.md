# Migration pressure adapters

`migration_pressure_effects.txt` contains event-driven state-local flight-pressure adapters. It never applies physical population loss or credit, records route deaths, creates a cohort, or scans the world.

`migration_pressure_apply_outbreak_neighbor_flight` runs after the famine adapter accepts its owner-proven Black Plague receipt or when the existing state-control callback gives a state to a live standard or weaponized zombie country. It checks only immediate neighbor states, requires a valid normal-civilian owner/controller state and an active adjacent outbreak, computes 2% of live population above the 15% protected origin floor, and requests flight through `migration_request_outbreak_pressure`. After an accepted migration request it stores `migration_pressure_outbreak_cooldown_until_date` for 14 days. It also honors the existing hostile-capture cooldown so a zombie front capture cannot submit both special-front and outbreak requests for the same neighboring state.

`migration_pressure_apply_war_front_flight` runs in one owned state during war relation or state-control callbacks. An adjacent state's actual controller must be at war with the current state's owner. It requests 2% of live population above the same protected floor through `migration_request_war_pressure` and shares the existing `humanitarian_capture_cooldown_until_date` receipt to prevent stacking with hostile-capture and special-front adapters.

`migration_pressure_build_local_flight_request` converts `state_population_k` to people, calculates the movable amount above the protected floor, multiplies by the caller's fixed-point share, and rounds the final request. The builder resets `migration_pressure_adapter_share` to the existing zero constant after calculating its output because HOI4 exposes no `clear_temp_variable` effect.
The caller owns the `migration_pressure_request_amount` output storage before the call.
The existing migration flight validator and `migration_apply_flight_request` remain authoritative for accepted requests and state registration.

The shared tuning block is `migration_pressure_runtime` in `common/script_constants/migration_pressure_constants.txt`. The outbreak cooldown is state-local and does not use a global scheduler. War and front work is bounded to the two countries in `on_war_relation_added`, the changed state's immediate neighbors, or the outbreak state's immediate neighbors.

## API contracts

| Helper | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `migration_pressure_apply_outbreak_neighbor_flight` | State: established outbreak origin | Established Black Plague state or a live standard/weaponized zombie-controlled state | Adds flight pressure only in eligible adjacent states; stores `migration_pressure_outbreak_cooldown_until_date` only after an accepted request. |
| `migration_pressure_apply_war_front_flight` | State: an owned state considered by a war/control callback | Valid civilian owner, live war, and actual hostile adjacent controller | Adds flight pressure through the migration request contract; shares the existing humanitarian capture cooldown variable. |
| `migration_pressure_build_local_flight_request` | State: eligible receiving pressure | Temporary `migration_pressure_adapter_share` fixed-point fraction | Produces temporary `migration_pressure_request_amount`; does not mutate people. |

No cohort arrays are added or changed by these adapters. The only new persistent state field is `migration_pressure_outbreak_cooldown_until_date`; front pressure uses the existing capture cooldown field.
