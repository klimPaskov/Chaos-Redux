# Migration priority effects

These state- and country-scoped helpers attach player-selected classes to exact migration cohorts and maintain their industrial workforce contribution. They run only on finalized transfer, registration, rollback, and existing state-control boundaries; there is no world scan or periodic scheduler.

## `migration_priority_reconcile_industrial_transfer`

Purpose: move the signed industrial-workforce contribution from the exact physical origin to the route destination after a finalized transfer.

Scope: the migration cohort host updater, after it resolves `migration_cohort_row_id` and before it changes host, destination, amount, or status arrays.

Inputs: exact `migration_cohort_row_id`, `civilian_transfer_finalize_result`, the current `civilian_transfer_generation`, measured `civilian_transfer_actual_origin_debit`, `civilian_transfer_survivor_credit`, `civilian_transfer_physical_origin`, and `civilian_transfer_route_destination`. An explicit `migration_cohort_priority_request` from an evacuation action replaces the cohort's stored class before the transfer is reconciled.

Output: the cohort class stored at `global.migration_cohort_priority_<cohort_id>`, a last-applied generation receipt, and paired state workforce deltas.

Defaults: older cohorts without a priority variable read as general priority. General, vulnerable, and administrative cohorts do not change industrial output. A repeated transfer generation is ignored. An industrial cohort's physical origin loses the measured debit; its destination receives only positive survivor credit.

Side effects: updates only the existing industrial cohort's origin and destination state contribution and their current owner-country output totals. Route deaths remain part of the origin debit and create no destination contribution.

## `migration_priority_register_workforce_state`

Purpose: retain a valid state with a nonzero industrial workforce balance in the existing sparse migration state registry without setting the displacement-active flag.

Scope: one state; caller invokes it only after the signed workforce balance is nonzero.

Inputs: valid human-system state and the existing `global.migration_active_states` array.

Output: unique state-array membership and an updated `global.migration_active_states_count`.

Defaults: an already registered state is unchanged; invalid states are not registered.

Side effects: registry membership only. No migration presentation, population, cohort, or displacement flag is set.

## `migration_priority_apply_workforce_delta`

Purpose: apply one signed, exact cohort delta to `migration_industrial_workforce_delta` in a state.

Scope: one physical origin or destination state.

Inputs: `migration_priority_workforce_delta`, negative at the source by the full measured debit and positive at the destination by survivor credit.

Output: refreshed local construction/repair modifier and state-weighted country factory and dockyard output contributions for the current controller.

Defaults: an absent state balance starts at zero; a zero delta is not submitted.

Side effects: changes only state and current producer-country variables, flags, and dynamic modifiers. It does not change population or country factory counts.

## `migration_priority_refresh_state_industrial_projection`

Purpose: calculate the local construction and repair effect and the state's signed contributions to the current controller's factory-output and dockyard-output modifiers.

Scope: state.

Inputs: the state's current `state_population_k`, `building_level@industrial_complex`, `building_level@arms_factory`, `building_level@dockyard`, the signed `migration_industrial_workforce_delta`, and the valid current controller's `num_of_factories`.

Output: `migration_industrial_output_factory_state_contribution` and `migration_industrial_output_dockyard_state_contribution`, stored with `migration_industrial_output_producer` for exact removal/replacement on capture, release, or the next refresh.

Formula: clamp the workforce delta divided by live state population to [-1, 1]. Factory output contribution is that signed share multiplied by this state's industrial-complex plus arms-factory levels divided by the current controller's `num_of_factories`; dockyard output uses the dockyard level over the same denominator. The state construction and industrial-complex repair modifier is the signed workforce share multiplied by `industrial_state_construction_per_share`, clamped to the shared state modifier bounds.

Defaults: a zero population or zero factory denominator produces no country output contribution. A state with no industrial cohort balance removes its local modifier and its prior country contribution.

Side effects: subtracts both previous state contributions from their stored controller, computes the contributions for the current controller, and refreshes that controller's country dynamic modifier. State-control changes call this helper through the existing registered-state modifier refresh.

## `migration_priority_refresh_country_industrial_output`

Purpose: apply the sums of weighted state contributions through `migration_country_industrial_workforce`, `industrial_capacity_factory`, and `industrial_capacity_dockyard`.

Scope: country.

Inputs: `migration_priority_country_industrial_output` and `migration_priority_country_industrial_dockyard_output`, adjusted by the state's contribution deltas.

Output: one country dynamic modifier while either signed total is nonzero.

Defaults: absent country totals start at zero. When both totals are zero the helper clears the flag and modifier; otherwise the two signed totals directly adjust factory and dockyard output.

Side effects: country flag and dynamic-modifier lifecycle only.

## `migration_priority_record_corridor_origin_loss`

Purpose: record the existing origin population-share construction penalty after an organized corridor transfer.

Scope: origin state.

Inputs: organized-evacuation route role, finalized transfer, positive measured origin debit and survivor credit, exact corridor cohort, and the transfer core's pre-debit population.

Output: the existing `migration_presentation_organized_evacuation_*` projection.

Defaults: invalid finalization, non-organized corridor role, zero debit/credit, or missing pre-debit population produces no projection.

Side effects: state presentation variables and migration presentation modifiers; no population, cohort, Deaths, or reception mutation.

## Cohort priority storage

`migration_evacuate_civilians`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`, and `migration_evacuate_administration` select `general`, `vulnerable`, `industrial`, or `administrative`; `migration_record_displaced_cohort` stores the class at `global.migration_cohort_priority_<cohort_id>`. Priority is selected by the player for the actual moved group; it does not claim that the remaining residents have a known age, occupation, or household composition. The priority target and last-transfer-generation target are cleared only when the exact staged row aborts or the terminal row is cleaned.

The exact movement balance is `actual origin debit = route deaths + survivor credit`. The state workforce ledger applies `-actual origin debit` at the source and `+survivor credit` at the destination, so the global signed workforce balance declines by route deaths only. Transit and return use the same cohort ID and generation owner; they move the contribution instead of granting it again. Integration leaves the cohort's contribution in its current host because the workers remain there.

Priority identifiers and tuning are in `common/script_constants/migration_cohort_priority_constants.txt`. Output follows the valid state controller, not the owner: capture subtracts the saved contribution from the former controller before adding it to the new controller, and release reverses that transaction. `migration_cohort_priority_is_valid` and the administrative decision contract are documented in `common/scripted_triggers/migration_priority_triggers.md`.
