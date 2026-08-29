# Core Reconciliation Owner Patch Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and status

This handoff records the bounded core implementation for the famine and migration system and is intended for `/root` to reconcile with the other owners.

The implementation covers sparse lifecycle retirement, exact aligned-cohort selection and physical-host proof, paired flight/trapped settlement, survivor-flight production, reception-capacity services, native safety callbacks, and exact transfer projections.

No event ID, event-pool row, pacing pulse, third mapmode, shared full scripted GUI, decision file, localisation file, mapmode file, achievement file, workbook, event file, or permanent architecture document was added by this patch.

The worktree contains unrelated concurrent edits from other owners; they were preserved and no reset or commit was performed.

## Files changed

- `common/script_constants/famine_migration_constants.txt` adds the `famine_migration_core_reconciliation` enum/tuning category and the `famine_migration_capacity` six-input service category.
- `common/scripted_triggers/chaosx_famine_migration_triggers.txt` updates state/country obligation predicates, exact host proof, role validation, candidate validity, and current-capacity validity.
- `common/scripted_triggers/famine_migration_destination_selection_triggers.txt` adds the chain-local candidate and route-safety proof without consuming the unavailable `famine_migration_route_unsafe` token.
- `common/scripted_effects/chaosx_famine_migration_effects.txt` updates runtime initialization, registry retirement, exact cohort lifecycle, selectors, transfer settlement, transfer projections, reception delta, survivor-flight production, sparse callbacks, native projections, and lifecycle wrappers.
- `common/scripted_effects/famine_migration_destination_selection_effects.txt` updates weighted destination preflight and stale normal-destination proof cleanup.
- `common/scripted_effects/famine_migration_spontaneous_movement_effects.txt` supplies the spontaneous role and uses the exact transfer contract.
- `common/scripted_effects/famine_migration_forced_movement_effects.txt` supplies the deportation role and uses the exact transfer contract.
- `common/scripted_effects/famine_migration_corridor_effects.txt` supplies the organized-evacuation role immediately before exact transfer and preserves the canonical corridor receipt path.
- `common/scripted_effects/famine_migration_capacity_effects.txt` adds the sparse candidate registry, people-unit shelter and medical adapters, dirty callbacks, and bounded country recomputation.
- `common/scripted_effects/famine_migration_capacity_effects.md` documents the public capacity adapters, formula, sparse scheduling, invalidation, and fail-closed behavior.
- `common/on_actions/chaosx_famine_migration_on_actions.txt` keeps reassessment callbacks bounded and normalizes its explicit `check_variable` form.
- `common/scripted_effects/chaosx_dynamic_effects.md` documents the exact transfer, paired settlement, projection, stable refresh wrapper, food-only clear, and capacity compatibility contracts.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/core_reconciliation_owner_patch.md` is this implementation handoff.

## Changed identifiers

The principal constants are `famine_migration_core_reconciliation.schema_version`, selector values, `cohort_live_minimum`, protected-floor and stage-flight shares, `transfer_projection_invalid`, `transfer_projection_valid`, the nine transfer-role enum values, and `route_damage_threshold`.

The capacity constants are schema/version values, normalized component floors, six equal quality weights, safe-state/population factors, service/population ratios, bounded civilian-factory administration throughput, food-quality bands, war/outbreak/contamination/load penalties, and `revision_increment`.

The core trigger identifiers updated are `famine_migration_state_can_retire`, `famine_migration_state_has_migration_obligations`, `famine_migration_terminal_state_references_clear`, `famine_migration_terminal_country_references_clear`, `famine_migration_country_has_migration_obligations`, `famine_migration_cohort_current_host_proof_is_valid`, `famine_migration_transfer_role_request_is_valid`, `famine_migration_reception_candidate_is_valid`, and `famine_migration_reception_capacity_is_valid`.

The destination trigger identifiers are `famine_migration_destination_selection_reception_available`, `famine_migration_destination_selection_border_admissible`, `famine_migration_destination_selection_reception_policy_blocks_admission`, `famine_migration_destination_selection_foreign_policy_rejection_candidate_is_valid`, and `famine_migration_destination_selection_candidate_is_valid`.

The exact-transfer identifiers are `famine_migration_initialize_runtime`, `famine_migration_record_displaced_cohort`, `famine_migration_bind_cohort_destination`, `famine_migration_bind_cohort_destination_forced`, `famine_migration_rebind_cohort_destination_safe`, `famine_migration_cleanup_cohort_record`, `famine_migration_cleanup_cohort_records_for_state`, `famine_migration_full_invalidate_state_registration`, `famine_migration_reconcile_state_cohort_selection`, `famine_migration_reconcile_country_cohort_selection`, `famine_migration_prove_transfer_current_host`, `famine_migration_transfer_civilians_exact`, `famine_migration_reconcile_successful_transfer_obligations`, `famine_migration_record_transfer_projection`, `famine_migration_apply_destination_credit`, `famine_migration_restore_origin_population_residual`, and `famine_migration_update_cohort_host_after_transfer`.

The reception and pressure identifiers are `famine_migration_apply_reception_delta`, `famine_migration_refresh_reception_capacity`, `famine_migration_submit_survivor_flight_request`, `famine_migration_transition_food_stage`, `famine_migration_retire_recovered_state`, `famine_migration_clear_dynamic_modifiers`, `famine_migration_clear_food_dynamic_modifiers`, `famine_migration_refresh_dynamic_modifiers`, `famine_migration_refresh_state_modifiers`, `famine_migration_cleanup_state_registration`, `famine_migration_cleanup_country_registration`, and `famine_migration_clear_stale_normal_destination_proofs`.

The native/callback identifiers are `famine_migration_refresh_native_state_safety_projections`, `famine_migration_consume_registered_state_reassessment`, `famine_migration_process_registered_food_state`, `famine_migration_process_registered_displacement_state`, `famine_migration_process_registered_displacement_country`, `famine_migration_handle_state_control_change`, `famine_migration_mark_country_war_reassessment`, `famine_migration_mark_country_peace_reassessment`, and `famine_migration_handle_nuclear_state_change`.

The destination effect identifiers are `famine_migration_destination_selection_bind_actor`, `famine_migration_destination_selection_calculate_candidate_weight`, `famine_migration_destination_selection_preflight_closed_border_rejection`, `famine_migration_destination_selection_run_weighted_pool`, `famine_migration_select_general_safe_evacuation_destination`, `famine_migration_select_internal_safe_route_destination`, `famine_migration_select_foreign_transit_destination`, `famine_migration_select_third_country_resettlement_destination`, and `famine_migration_select_safe_food_reserve_donor`.

The movement identifiers are `famine_migration_spontaneous_movement_cleanup_destination_proofs`, `famine_migration_spontaneous_movement_submit_request`, `famine_migration_process_spontaneous_movement_owner`, and `famine_migration_execute_forced_transfer_exact`.

The corridor identifiers changed for this contract are `famine_migration_prepare_corridor_contract`, `famine_migration_corridor_record_evacuation`, `famine_migration_execute_corridor_evacuation`, and the narrow role/reconciliation call site in `famine_migration_corridor_effects.txt`.

The capacity identifiers are `famine_migration_register_reception_candidate_state`, `famine_migration_unregister_reception_candidate_state`, `famine_migration_mark_reception_capacity_dirty`, `famine_migration_set_reception_shelter_service`, `famine_migration_set_reception_medical_service`, `famine_migration_clear_reception_shelter_service`, `famine_migration_clear_reception_medical_service`, and `famine_migration_recalculate_reception_capacity`.

## Core contracts

### Sparse lifecycle and old-save safety

Runtime initialization creates only missing counters, schema markers, and repair markers and never clears or truncates an existing aligned array.

Missing next-ID state with live rows marks the runtime for repair and fails closed instead of inventing IDs.

Food retirement is separate from displacement-scheduler retirement and full invalidation.

A food-stable state retains positive paired flight ledgers, paired trapped ledgers, reception load, live cohorts, selectors, mission/corridor obligations, projections, and durable totals.

Country and state retirement predicates include only bounded real obligation variables and aligned live-row references; durable totals never block scheduler retirement and are never cleared.

Failed or zero transactions do not clean ledgers.

Registered state processing calls `famine_migration_clear_stale_normal_destination_proofs` when no chain-local normal destination target exists.

State cleanup clears food-only modifiers first and unregisters the displacement scheduler only inside the no-obligation branch; active migration obligations re-register the state for sparse processing.

### Exact aligned cohorts and physical-host proof

The aligned global row is authoritative and state/country selector values are derived caches.

The exact resolver accepts an explicit `famine_migration_cohort_id_request`; a positive invalid ID never falls back to a selector.

Zero valid rows clear the state cache, one valid row stores its exact ID, and more than one stores the ambiguity marker.

Country caches count valid live rows where the country is either persisted owner or authoritative current host, allowing recovery from a stale ambiguity marker.

`famine_migration_prove_transfer_current_host` resolves the exact aligned row, checks active/destination-bound status and positive amount, compares the persisted host state to the saved physical origin scope, and requires exactly one match.

Cleanup resolves and validates exact origin, host, destination, persisted-owner, and current-host scopes before removing one exact terminal zero row; unresolved scope references fail closed.

No row-wide cleanup is performed for a recovered or changed state.

### Paired settlement and conservation

`famine_migration_reconcile_successful_transfer_obligations` computes one flight settlement as `min(actual_origin_debit, famine_migration_flight_pressure, famine_migration_state_flight_population)` and subtracts that exact value from both ledgers once.

The trapped pair follows the same minimum rule with `famine_migration_trapped_population` and `famine_migration_state_trapped_population`.

If one paired ledger is missing, settlement is zero and the obligation remains visible for repair.

Mismatched larger residuals remain visible rather than being silently erased, and route deaths are never touched by ledger settlement.

The exact transfer conserves `actual_origin_debit = route_deaths + survivor_credit`, restores only a measured residual, and never writes a duplicate population or death debit.

Reception load is mutated only by `famine_migration_apply_reception_delta`, which requires positive measured deltas, valid state/country scope, and sufficient funds before applying one paired state/country load change.

### Survivor flight producer

`famine_migration_submit_survivor_flight_request` runs only for a positive food-stage upgrade and one crisis-plus-stage-generation request.

Desired flight is the live-population clamp multiplied by the stage share, reduced by accepted flight/trapped/live-cohort obligations, and bounded by the protected population floor.

Stage upgrades submit only the positive incremental share and never mutate population, deaths, or cohort rows at pressure creation.

The pressure source remains `famine_migration_pressure_source.resource_shortage` until an exact movement owner supplies the destination lane classification.

Direct hazard wrappers remain food-only unless their owner supplies a separate explicit survivor request.

### Reception capacity

The migration-owned service contract uses a sparse registered candidate-state array and the existing registered-country host pulse.

Each valid candidate contributes six normalized inputs: current food quality, shelter service per candidate population, infrastructure quality, transport availability, medical service per candidate population, and administration quality from governance plus bounded civilian-factory throughput.

`famine_migration_reception_transport_availability` is the normalized transport component `(max_component - component_transport) / max_component`; it is availability evidence and not route proof.

Safe-state and safe-population fractions bound the aggregate quality factor.

War is applied once after the candidate loop, while outbreak and contamination are population-weighted across safe candidates and each penalty is applied once.

Published capacity is the effective threshold `round(gross * safe_factor * war_factor * outbreak_factor * contamination_factor * load_factor)` and does not subtract reception load a second time.

Invalid or unsafe candidates contribute zero; registry-length/schema corruption is the only candidate-count poison.

No safe candidate or missing shelter/medical adapter fails closed.

Every completed recomputation increments `famine_migration_reception_capacity_revision` and clears dirty; `famine_migration_reception_capacity_is_valid` requires current schema, positive revision, valid result, positive capacity, positive safe candidates, and dirty equal to zero.

### Native tokens and callbacks

Rail safety uses `damaged_building_level@rail_way` and the configured damage threshold.

Strategic-bombing safety uses `days_since_last_strategic_bombing` and never fabricates attacker attribution.

Control, war, peace, and nuclear reassessment markers are consumed through exact registered callbacks and cleared only after bounded reconciliation.

The unavailable `famine_migration_route_unsafe` and unavailable persecution/ordinary-bombing actor facts are not treated as safety evidence.

## Exact transfer projection receipt

On every successful positive debit, the origin scope receives `famine_migration_projection_last_origin_population_before`, `famine_migration_projection_last_origin_debit`, `famine_migration_projection_last_survivor_credit`, `famine_migration_projection_last_route_deaths`, `famine_migration_projection_last_origin_departure_share`, `famine_migration_projection_last_cohort_id`, `famine_migration_projection_last_generation`, and `famine_migration_projection_last_role`.

For positive survivor credit only, the destination receives `famine_migration_projection_last_survivor_credit`, `famine_migration_projection_last_reception_share`, `famine_migration_projection_last_population_after_credit`, `famine_migration_projection_last_cohort_id`, `famine_migration_projection_last_generation`, and `famine_migration_projection_last_role`.

The origin share is `actual_origin_debit / origin_population_before`.

The destination share is `survivor_credit / destination_population_after_credit` and is not written for an all-death result.

The role enum is caller-supplied and supports spontaneous exodus, organized evacuation, forced movement, deportation, transit, resettlement, voluntary return, forced return, local integration, and unspecified.

Receipt generation is incremented only by successful positive exact debit and receipts remain until guarded no-obligation cleanup; failed and zero transactions are inert.

The current aligned cohort schema has no separate per-row generation array, so cleanup is exact-ID/status/zero/reference-bound and does not invent or truncate a generation array.

## Marker producer/consumer census

`famine_migration_control_reassessment_pending` is produced by `famine_migration_handle_state_control_change` and consumed by `famine_migration_consume_registered_state_reassessment` and guarded state cleanup.

`famine_migration_nuclear_reassessment_pending` is produced by `famine_migration_handle_nuclear_state_change` and consumed by the same bounded registered-state callback and guarded cleanup.

`famine_migration_country_war_reassessment_pending` and `famine_migration_country_peace_reassessment_pending` are produced by their mark effects and consumed by `famine_migration_process_registered_displacement_country` and guarded country cleanup.

The canonical capacity-exhausted fact is the decision-facing exact comparison against live reception load and published effective capacity; no orphan `famine_migration_reception_capacity_exhausted` producer was added.

## Validation performed

A brace-stack parser over all owned Clausewitz files reported balanced blocks after the survivor-flight helper closure correction.

An explicit-form census reported no malformed `check_variable` hybrids, no direct unsupported `<=` or `>=`, and no temporary proof cleanup through `clear_variable`.

A code census reported no active `famine_migration_route_unsafe` consumer under `common`.

A capacity census confirmed the central penalty constant, one aggregate war/outbreak/contamination application, six quality accumulators, normalized transport output, revision increment, dirty-zero validity, and no second load subtraction from published capacity.

The requested source-level scenarios are represented by guarded contracts: A-to-B followed by stale-A debit fails the physical-host proof, two live rows produce ambiguity and then recover after one terminal row is removed, food recovery preserves active migration obligations, exact-zero and partial transfer paths preserve conservation, aligned arrays are never cleared by initialization, and dirty capacity recomputation increments revision before consumers can authorize.

Live game execution was not performed because it belongs to the user runtime.

## MCP evidence and blockers

No event, map, GUI, or focus surface was touched, so no event/map/GUI MCP route was applicable.

The weighted destination selector remains the existing bounded adjacent-state weighted pool with chain-local safety proofs, but the enabled runtime did not expose a callable `hoi4.probability_inspect` route or `chaosx_ai_probability_auditor` route for this subagent, and the parent instructed that further MCP retries stop; source evidence is therefore recorded as a blocker rather than represented as engine evidence.

Vanilla offline references used for the native facts were `dynamic_variables_documentation.md` for `damaged_building_level@rail_way` and `triggers_documentation.md` for `days_since_last_strategic_bombing`; neither supports attacker attribution.

## Parent-required follow-up

The decision/mission owner must supply an exact `famine_migration_cohort_id_request`, explicit physical-origin scope, and caller role immediately before every exact transfer, plus exact role values for transit, resettlement, returns, and local integration.

The decision/mission owner must wire history no-repeat, return/resettlement exceptions, closure receipts, exact mission subjects, and guarded rewards through the public narrow core adapters without editing the core receipt names.

The presentation owner must consume `famine_migration_refresh_state_modifiers` and the projection receipt fields, retain ownership of the ten exact phase modifiers and the two frozen mapmodes, and avoid restoring the legacy generic displacement modifier path.

The corridor owner must resolve the remaining external route-geometry and actor-attribution facts through supported producers; core does not fabricate `route_unsafe` or distant geometry.

The parent should decide whether a future schema revision can add a per-row generation array; this patch intentionally fails closed on such an absent or misaligned array.

No simplification was silently substituted for the missing engine facts; unavailable facts and the probability MCP route are explicitly listed above.
