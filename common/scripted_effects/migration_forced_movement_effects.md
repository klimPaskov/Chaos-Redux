# Migration forced movement effects

This file documents the bounded owner contract implemented in `migration_forced_movement_effects.txt`.

## Purpose and ownership

`migration_execute_forced_transfer_exact` is the single forced-movement producer for the Germany camp-prison transfer currently owned by `camp_rework_germany_apply_prisoner_transfer`.

The caller is the successful owner transaction in `common/scripted_effects/camp_repression_major_country_effects.txt`.

The caller runs with `ROOT` as actor, `FROM` as the exact origin state, and state `88` as the explicit destination state.

The helper never scans states or countries, selects a neighbor, invents a destination, or calls the older genocide transfer effect.

After the shared exact transfer returns a valid positive survivor credit, the helper emits two post-success receipts: one canonical reception delta in the explicit destination state and one deportation condemnation in the saved ROOT actor country. These receipts do not alter population or the live cohort amount.

## Contract inputs

The source-state caller must provide positive `migration_forced_transfer_requested_people`, a positive `migration_forced_transfer_transaction_id`, and proof variables for request, origin, destination, actor, and transaction identity.

The caller must provide `migration_forced_transfer_cause = constant:migration_forced_movement_cause.deportation_camp_prison_transfer` and `migration_forced_transfer_custody_status = constant:migration_forced_movement_custody.forced`.

The caller must provide source pressure-owner proof and reception-owner proof, and must save explicit event targets for origin, destination, actor, source owner, pressure owner, and reception owner.

The destination owner must provide transient food-safe and reception proof for this owner-controlled camp intake; these proofs are not a humanitarian route claim and are not inferred by the helper.

The route-death request defaults to zero.

Any positive route-death request additionally requires an explicit route-death proof, the distinct `constant:chaos_meter_deaths_reason.forced_displacement` reason, and death logging proof.

The exact state-88 caller supplies no route-death proof and therefore records movement as movement rather than death.

## Helper map

`migration_forced_transfer_live_ledger_arrays_are_aligned` is a read-only global trigger that proves the seven live cohort arrays and live count have equal lengths.

`migration_forced_transfer_contract_is_valid` is evaluated in the origin state and verifies the explicit request, identity, cause, custody, ownership, targets, valid origin, distinct valid destination, and destination intake proofs.

`migration_forced_transfer_route_death_request_is_valid` is a read-only contract trigger that accepts zero deaths or the separately proven death slice described above.

`migration_forced_transfer_staged_cohort_proof_is_valid` is evaluated after provisional record and origin resolution and requires one positive live row with the exact requested amount, exact origin target, and active status.

`migration_forced_transfer_bound_cohort_proof_is_valid` is evaluated after entering the destination state and requires a valid forced bind and a route destination equal to the caller-supplied state 88 target.

`migration_forced_transfer_cleanup_staged_cohort` is an any-scope cleanup effect that removes a failed provisional row by explicit ID and clears matching source, destination, and owner selection pointers.

`migration_execute_forced_transfer_exact` is the state-scope owner effect that stages one bounded cohort, enters the explicit destination, binds the row as `destination_bound_unsafe`, delegates the sole population mutation to `civilian_transfer_execute_transaction`, applies the measured survivor reception delta, emits exact-actor deportation condemnation, and returns temporary result and amount outputs.

## Exact amount and conservation

The Germany caller computes the requested amount as `round(state_population_k * constant:chaos_meter_deaths.people_per_k * constant:migration_decision_threshold.transfer_share)` after the existing camp owner transaction.

The protected source floor is `round(state_population_k * constant:chaos_meter_deaths.people_per_k * constant:migration_decision_threshold.transfer_minimum_origin_share)`.

The shared exact helper clamps the request to the live source amount above that floor and debits the source once with `apply_state_population_loss_without_recruitable_manpower_gain`.

The actual debit is partitioned as `actual_origin_debit = route_deaths + survivor_credit`.

Only the survivor credit is added to state 88 through the shared destination-credit helper, including its existing manpower reconciliation.

Any positive conservation residual is restored to the origin before the transaction is considered valid.

The shared global conservation ledgers receive the actual debit, destination survivor credit, route-death slice, and residual separately.

The live cohort amount is overwritten by `migration_update_cohort_host_after_transfer` only after positive destination credit, so the durable row records the actually debited surviving cohort rather than the provisional request.

Only the measured `migration_forced_transfer_survivor_credit` is passed as `migration_reception_delta_amount` in the destination state with credit mode. `migration_apply_reception_delta` owns the paired state `migration_state_reception_load` and destination-owner `migration_reception_load` increments, sparse state/country registration, reception-context refresh, and overcrowding evaluation. The destination state initializes missing food/reception projection variables before this receipt so the canonical helper can register the exact state without inventing a second load owner.

The reception call retains the already-bound `destination_bound_unsafe` cohort, its deportation source, forced custody, and transaction metadata. It does not call a safe bind, integration, resettlement, or any population effect.

The same valid-positive branch enters `event_target:migration_forced_transfer_actor`, which is the saved ROOT responsible country, sets zero civilian-death and contamination inputs, and calls `migration_condemn_deportation` once. It persists the accepted transaction, cohort, survivor, origin, and destination evidence on that actor country after the adapter call. No Deaths entry is produced by this condemnation receipt.

Zero survivor credit removes the row and its visit history; a failed bind, invalid route, or failed conservation also removes the provisional row.

## Idempotency and lifecycle

The caller supplies `genocide_decisions_taken` after the existing successful owner transaction as the positive transaction identity for this actor-owned series.

The origin state persists the last transaction signature, destination state, actor, requested amount, actual debit, route deaths, survivor credit, destination credit, conservation residual, and result.

A lower transaction identity fails closed.

A matching transaction identity with the same destination, actor, and requested amount returns `already_applied` with the persisted outputs and performs no second debit, credit, reception delta, or condemnation call.

A matching transaction identity with a different signature fails closed.

On successful positive transfer, source and source-owner selection pointers are cleared while the destination state retains the live cohort pointer.

On cleanup, the explicit cohort row, history receipts, destination pointer, source pointer, and source-owner pointer are cleared only when they match the transaction's cohort ID.

The destination metadata records actor, source, destination, reception owner, pressure owner, cause, custody status, requested amount, actual debit, route deaths, survivor credit, destination credit, and conservation ledger after a valid positive transfer.

No achievement receipt, second history receipt, or separate camp population credit is emitted by this owner; the shared exact helper owns the one population destination credit and row amount update, while the canonical reception helper owns the one paired state/country load receipt.

## Files and call site

The constants are in `common/script_constants/migration_forced_movement_constants.txt`.

The fail-closed triggers are in `common/scripted_triggers/migration_forced_movement_triggers.txt`.

The effects are in `common/scripted_effects/migration_forced_movement_effects.txt`.

The authoritative caller is `camp_rework_germany_apply_prisoner_transfer` in `common/scripted_effects/camp_repression_major_country_effects.txt`.

There are no localisation keys, icons, map modes, GUI surfaces, decisions, events, or additional owner files for this bounded contract.

## Future work and known limits

Any additional forced-movement owner must submit a distinct transaction identity and explicit origin, destination, actor, ownership, cause, custody, amount, and live aligned-cohort proof through this contract.

No new owner should reuse state 88 or proxy another historical destination without an authoritative state-scoped proof and a separately reviewed caller.

The current camp caller has no dedicated intake-capacity API, so its state-88 food and reception proofs are explicit owner acknowledgements that are validated by the shared destination contract but do not synthesize a humanitarian capacity model.

The exact route is intentionally death-free until a future owner can prove route conditions and provide the separate death slice required by the trigger.

The current route has no additional caller-side reception or condemnation line; both post-success outputs remain inside the exact forced-movement owner so replay, failure, and zero-credit paths cannot reach them.
