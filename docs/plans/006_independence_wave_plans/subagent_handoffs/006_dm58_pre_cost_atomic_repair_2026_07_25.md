# Event 006 DM-58 pre-cost atomic repair

Date: 2026-07-25

Scope: parent implementation follow-up after the decision and completion audits identified that the reclamation-front mission could charge material costs before the complete member/target set was known.

## Source changes

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt` keeps the availability preflight as an on-demand, non-mutating member count and adds the war-legality check to the exact state resolver.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` clears stale event targets before every member resolution, records a member-specific staging receipt, and adds a rollback effect that removes staged claims, finite `take_state_focus` wargoals, state markers, generation variables, arrays, and staging receipts.
- `common/decisions/006_independence_wave_decisions.txt` resolves every member and freezes unique state/owner pairs before paying strategic or major security costs. A shortfall rolls the staged transaction back before payment and enters the crisis branch; only a complete minimum set pays and commits.
- `docs/events/006_independence_wave/reclamation_front_lifecycle.md` and the DM-58 localisation describe the pre-cost freeze and rollback.

## Evidence

The resolver's state limit rejects living league-member owners, current wars, duplicate state and owner arrays, stale generation markers, missing controllers, and non-claim/non-border objectives. Its nested owner scope checks `ROOT = { can_declare_war_on = PREV }` before any claim or wargoal is created. The same member loop increments the synchronized count, so the minimum set is an actual distinct reservation result rather than a separate eligibility count.

The paid branch is now after the count gate. A failed member loop invokes `independence_wave_rollback_reclamation_front_staging` and does not call either payment effect. A successful branch clears temporary staging receipts only after both costs are paid and the finite fronts are committed.

## Validation

- Python transient brace/quote scan passed for the three touched gameplay files.
- `git diff --check` is clean for the touched decision, trigger, effect, lifecycle, and localisation files.
- No Hearts of Iron IV process was launched; this is source-level evidence only.

## Remaining boundary

The exact ten-country automatic bands remain fail-closed because the ten attested packages provide only nine mutually compatible reservation groups: IW-008 RHI and IW-010 AJX share `RG-RHINE-SAAR`. This repair does not authorize a new package, map rebinding, or fallback.
