# Migration local integration settlement

Source: [migration_integration_effects.txt](migration_integration_effects.txt).
Caller: `migration_local_integration` in `common/decisions/migration_decisions.txt`, and the adapter name `migration_request_integration` in `migration_core_effects.txt`.

## `migration_settle_integrated_cohort`

Purpose: settle one whole hosted cohort into the country that shelters it.
Integration changes the cohort's status only; native state population is unchanged, `migration_record_transfer_projection` is never called and nobody moves.

Scope: the host STATE that currently shelters the cohort.

Inputs, consumed and reset on exit:

| Input | Meaning |
|---|---|
| temporary `migration_integration_settlement_proven` | Must be 1. |
| temporary `migration_integration_settlement_cohort_id` | Exact cohort ID, usually the state's `migration_current_cohort_id`. |
| event target `migration_integration_settlement_actor` | The integrating country. |

Outputs, declared by the caller before the call because temporary values set inside a scripted effect are not guaranteed to survive it:

| Output | Meaning |
|---|---|
| `migration_integration_settlement_result` | 1 when the cohort was settled, otherwise 0. |
| `migration_integration_settlement_amount` | People settled, 0 on rejection. |
| `migration_integration_result` | Result of the national credit, read by the cohort-resolution achievement gate. |

Steps:

1. Prove the actor is a valid country that owns and controls the host, the cohort ledger is aligned and not awaiting repair, and the cohort ID names exactly one row.
2. Prove the row is live (active or destination-bound), carries people, has this state as its current host, and that the state's reception load and the owner's national reception load each already cover the whole row.
3. Debit both reception ledgers once through `migration_apply_reception_delta`, with its context refresh deferred.
4. Only after a valid debit, write the row as `completed` with zero people (the same terminal representation the transfer finalizer uses for a zero-survivor row) and reconcile the state and country cohort selection.
5. Credit national integration in the actor through `migration_integrate_displaced_cohort`, then refresh the state's reception context and decision phase.

A rejected settlement leaves the row, both ledgers and the national integration total unchanged.
Because a settled row is completed with zero people, repeating the action cannot settle it again, consume another cohort's reception load, or credit integration twice.

The decision pays its fee before the settlement, as accepted for the paid-action tranche.
Its visibility, target filter, availability and start preflight all require `migration_local_integration_host_can_settle`, so the fee is only taken when the integrating country owns and controls the host and both reception ledgers already cover the hosted group, which are the settlement's own ledger conditions.
After a successful settlement it records the integrated receiving state and cohort-resolution achievements, asks `migration_cleanup_cohort_record` to remove the terminal row once nothing else references it, and updates the migration phase flags.

## `migration_integrate_displaced_cohort`

COUNTRY scope national credit helper in `migration_core_effects.txt`.
It adds `migration_integration_people` to `migration_integrated_population`, sets `migration_cohort_integrated` and `migration_cohort_resolution_transaction_proven`, and returns `migration_integration_result`.
It is called only by the settlement and is never an integration path on its own.

## Usage

```text
# COUNTRY scope of the integrating decision; FROM is the host state.
set_temp_variable = { migration_integration_settlement_result = constant:humanitarian_runtime.zero }
set_temp_variable = { migration_integration_settlement_amount = constant:humanitarian_population.zero }
set_temp_variable = { migration_integration_result = constant:humanitarian_runtime.zero }
save_event_target_as = migration_integration_settlement_actor
FROM = {
	set_temp_variable = { migration_integration_settlement_cohort_id = migration_current_cohort_id }
	set_temp_variable = { migration_integration_settlement_proven = constant:humanitarian_runtime.one }
	migration_settle_integrated_cohort = yes
}
```
