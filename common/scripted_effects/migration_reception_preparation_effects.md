# Paid reception preparation

`migration_prepare_reception_services` runs in COUNTRY scope on the receiver.
The caller must save the exact selected STATE as regular `migration_reception_preparation_state` and predeclare temporary `migration_reception_preparation_result = 0` before calling it.
The result is reset to zero on entry and becomes one only after a meaningful successful service or reception-policy change; it remains available to the caller.

The helper reobserves current famine-owned food facts, checks current actor/control/hazards and exact pending-front identity, then spends the standard selected-state transport quote once through `migration_transport_pay_state_cost`, plus support equipment from `migration_reception_preparation_cost`.
It submits population-scaled shelter and medical services through the existing capacity-owner setters using `migration_reception_bootstrap.shelter_population_share` and `.medical_population_share`.
It never supplies food reserves, native housing, free medical service, population, route authorization, or reception load.
Policy-only success is allowed only for an actual transition to `humanitarian_open` with valid current service/capacity receipts.
The departure-policy request is explicitly zeroed before a reception-only policy call.
Every attempted service/policy setter must report valid; another state's valid capacity cannot mask a rejected selected-state setup.

For a pending evacuation, success additionally requires the same generation, exact whole live origin row, and current receiver load plus the full offered amount no greater than capacity.
An already-installed identical open-policy/service configuration cannot be charged again.
A prepared but insufficient receiver fails and refunds the actual paid resources rather than shrinking or splitting the offer.

Rollback restores only this click's changed shelter/medical fields and attempted policy fields, preserving previous valid receipts.
Candidate flag, sparse array membership, and optional candidate revision are snapshotted and restored independently, and global candidate count is recomputed.
Capacity is then recalculated from the restored current owner inputs; previously dirty capacity is not restored as a stale cache.
Existing active-country registration belongs to the real origin/pending-request lifecycle and is not removed by a failed paid preparation.
Regular scope targets end with the effect chain, and all child temporary results consumed after return are declared before their calls.

After a genuine paid success for a still-valid pending evacuation request, the helper publishes the `prepared` reception intent on the request's front through `migration_publish_reception_front_intent_from_contract` (see [migration_reception_front_intent_effects.md](migration_reception_front_intent_effects.md)).
That publication is presentation only: it cannot charge, refund, reject the setup or change capacity, and a refunded or unchanged setup never advances the phase.

```text
# COUNTRY scope, FROM is the exact selected owned/controlled STATE
set_temp_variable = { migration_reception_preparation_result = constant:humanitarian_runtime.zero }
FROM = { save_event_target_as = migration_reception_preparation_state }
migration_prepare_reception_services = yes
```

The preparation cost retains support equipment 100 in `common/script_constants/migration_reception_preparation_constants.txt` and uses the standard physical quote from `migration_transport_cost_constants.txt`, fuel 10k for connected states or fuel 20k and 10 convoys for disconnected states.
The exact selected-state transport receipt is recorded on the receiving payer before debit and is refunded from its saved quantities on rollback or cleared after success.
No political power is charged or refunded.
See [the transport API](migration_transport_cost_effects.md) for affordability, payer/action/state receipt identity, geography and validation limits.
Country fuel display quotes project those same constants in k, while each cost selector uses the live selected FROM state for geography and fresh constants for affordability.
Displayed support equipment reads its own central constant directly.
The display cache never governs payment.
No icon, GUI, mapmode, event, or new public value is introduced.
The current implementation evidence and source-case limits are in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/prospective_reception_implementation_20261003.md`.
