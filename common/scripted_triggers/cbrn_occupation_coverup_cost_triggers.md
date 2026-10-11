# CBRN occupation coverup recovery preflight

`cbrn_occupation_coverup_can_retry_refund` is a COUNTRY-scoped scripted trigger with FROM as the selected STATE.
Its purpose is to expose the same valid recovery-only action to native availability and parent-owned scripted localisation.
It does not refund, debit, settle, change flags, or mutate normal payer fields.
It does not test or widen the existing decision's route, target-control, visibility or record requirements.

It requires a positive exact-state open receipt ID, existing saved target, paid amount and phase, saved target equal to FROM, positive paid amount, and either `unrecorded_refund` or `recorded_refund` phase.
An applied settlement is not a refund click.
Zero, unknown, wrong-target, missing-paid and wrong-phase pointers cannot authorize recovery through this trigger.
A valid private preflight does not prove that the shared core receipt is valid.
The real recovery API still validates the shared row, retaining rejected proof rather than inferring a refund.

There are no input temporaries.
The two temporary outputs are `cbrn_occupation_coverup_target` and `cbrn_occupation_coverup_receipt_id`.
Any caller consuming those fields after return initializes both to zero before the call.
The trigger sets target to FROM and initializes receipt ID to zero before testing the pointer.
Partial output values after a false result are diagnostic only.
Only a true result permits reading the retained paid amount as refund display data.

```txt
set_temp_variable = { cbrn_occupation_coverup_target = constant:universal_cost_framework.zero }
set_temp_variable = { cbrn_occupation_coverup_receipt_id = constant:universal_cost_framework.zero }
cbrn_occupation_coverup_can_retry_refund = yes
# After success, read cbrn_occupation_coverup_receipt_paid_@var:cbrn_occupation_coverup_receipt_id.
```

Direct consumers are the two `cbrn_occupation_can_pay_*_pp` bodies and the parent's four quote/detail getters in `common/scripted_localisation/cbrn_occupation_value_localisation.txt`.
Fresh availability also rejects the presence of any open pointer before invoking the normal price producer.
The parent getters use the same exclusion for their fresh-price branches and show price unavailable for malformed pointers.
The original four public quote outputs remain unchanged.

The [effect contract](../scripted_effects/cbrn_occupation_coverup_cost_effects.md) documents normal payer storage, actual-payment receipt roles, recovery phases and the owner integration boundary.
The [handoff](../../docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-07_cbrn_coverup_cost_adapter.md) records validation and native evidence limits.

`cbrn_occupation_coverup_has_pending_receipt` is a payer-scope trigger with no FROM requirement.
It is true while the payer's pending cover-up receipt queue is non-empty and drives the visibility of the `cbrn_recover_coverup_payment` decision, which calls `cbrn_occupation_recover_paid_coverups` so an outstanding refund stays reachable when no state can start another cover-up.
