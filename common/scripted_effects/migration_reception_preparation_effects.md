# Paid reception preparation

`migration_prepare_reception_services` runs in COUNTRY scope on the receiver.
The caller must save the exact selected STATE as regular `migration_reception_preparation_state` and predeclare temporary `migration_reception_preparation_result = 0` before calling it.
The result is reset to zero on entry and becomes one only after a meaningful successful service or reception-policy change; it remains available to the caller.

The helper reobserves current famine-owned food facts, checks current actor/control/hazards and exact pending-front identity, then spends exactly the three central `migration_reception_preparation_cost` amounts once.
It submits population-scaled shelter and medical services through the existing capacity-owner setters using `migration_reception_bootstrap.shelter_population_share` and `.medical_population_share`.
It never supplies food reserves, native housing, free medical service, population, route authorization, or reception load.
Policy-only success is allowed only for an actual transition to `humanitarian_open` with valid current service/capacity receipts.
The departure-policy request is explicitly zeroed before a reception-only policy call.
Every attempted service/policy setter must report valid; another state's valid capacity cannot mask a rejected selected-state setup.

For a pending evacuation, success additionally requires the same generation, exact whole live origin row, and current receiver load plus the full offered amount no greater than capacity.
An already-installed identical open-policy/service configuration cannot be charged again.
A prepared but insufficient receiver fails and refunds all three resources rather than shrinking or splitting the offer.

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

Costs live only in `common/script_constants/migration_reception_preparation_constants.txt`: political power 20, support equipment 100, fuel 500.
Parent-owned display quotes are projections of those same constants, never payment authority.
No icon, GUI, mapmode, event, or new public value is introduced.
The current implementation evidence and source-case limits are in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/prospective_reception_implementation_20261003.md`.
