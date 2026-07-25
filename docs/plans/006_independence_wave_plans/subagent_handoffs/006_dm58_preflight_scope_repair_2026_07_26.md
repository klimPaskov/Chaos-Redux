# Event 006 DM-58 preflight scope repair

Date: 2026-07-26.

## Change

The DM-58 candidate trigger `is_independence_wave_reclamation_front_member_candidate` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` now evaluates candidate legality against the country selected by the enclosing `any_country` scope. In the nested `any_state -> owner` chain, `PREV` is the candidate state and `PREV.PREV` is the iterated candidate member. The helper no longer uses `ROOT` for candidate war legality or for the owner self-tag exclusion.

The paid resolver and rollback path remain authoritative. This repair only removes the initiator-versus-candidate scope ambiguity from the availability preflight; it does not claim that the trigger can express a complete injective member-to-owner matching proof.

## Validation

- Re-read the offline Scopes reference for chained `PREV.PREV` semantics and the owner/state scope tree.
- Confirmed the trigger keeps the candidate state claim, controller, state-array, target-array, and existing-wargoal guards intact.
- Confirmed no decision cost, effect, attestation, or runtime package gate changed.
- No Hearts of Iron IV process was launched and no live DM-58 scenario was run.

## Remaining boundary

The preflight can still admit members whose only legal objectives share an owner. Execution must continue to stage distinct state and owner pairs and roll back cleanly when the minimum cannot be assembled. A future injective feasibility check requires a separately validated design and is not inferred from this narrow scope repair.
