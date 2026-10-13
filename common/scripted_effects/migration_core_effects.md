# Migration core caller output contracts

The complete mechanic is described in [migration_system.md](../../docs/systems/migration_system.md).
This note documents the temporary return storage used by the evacuation and deportation request owners in `migration_core_effects.txt`.

Both helpers run in the exact origin STATE and require the existing positive request, actor, owner, and action-specific transport or policy proofs.
Before calling `migration_record_displaced_cohort`, they declare `migration_cohort_record_result = constant:civilian_transfer_route_result.invalid` and `migration_cohort_id_result = constant:humanitarian_runtime.zero`.
The recorder returns a valid result and exact group identity only after recording succeeds.
Declarations made first inside the recorder cannot substitute for this caller storage.

`migration_request_organized_evacuation` consumes the result and identity for organized-evacuation presentation and the existing destination/transfer path.
`migration_request_deportation_flow` consumes the result before publishing deportation pressure and activating its state context.
Neither request invents a new movement outcome, repairs a rejected group, or changes the exact transfer owner's debit and survivor accounting.

The neutral `civilian_transfer_execute_transaction` and `civilian_transfer_rollback_transaction` callers also declare `migration_reception_delta_result` as invalid and `migration_reception_delta_applied` as zero before invoking the reception owner.
Forward source/departure, destination/arrival, and compensating reception updates therefore retain their exact applied amounts after the nested helper returns.
These declarations add no transfer, credit, refund, or repair by themselves.

Voluntary-return, resettlement, forced-return, custody, and forced-transfer callers declare the cohort-origin and destination resolution results, match count, resolved amount, source, and status before calling `migration_resolve_cohort_origin`.
The results default to invalid, zero, unknown source, and no status, so an unresolved or rejected group cannot reuse a preceding group's returned values.
The resolved origin and host event targets remain the resolver's existing scope pointers.

Example within an already proven request owner:

```text
set_temp_variable = { migration_cohort_record_result = constant:civilian_transfer_route_result.invalid }
set_temp_variable = { migration_cohort_id_result = constant:humanitarian_runtime.zero }
migration_record_displaced_cohort = yes
if = {
	limit = { check_variable = { migration_cohort_record_result = constant:civilian_transfer_route_result.valid } }
	set_temp_variable = { migration_cohort_id_request = migration_cohort_id_result }
}
```

## Industrial workforce registration

The `migration_priority_register_workforce_state` helper adds a valid nonzero-balance state to the existing `global.migration_active_states` array without publishing `migration_displacement_active`. `migration_state_has_obligations` includes the signed industrial balance, so integration does not retire a settled workforce projection. `migration_cleanup_state_registration` leaves an industrial-only state registered without changing its displacement presentation. The existing sparse `migration_process_registered_state` calls the state modifier refresh for nonzero balances; when the balance returns to zero, the ordinary obligation and unregister path retires the state. Invalid-state control changes remove the stored producer contribution and clear the balance.

