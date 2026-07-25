# Event 006 DM-58 preflight alignment handoff

Date: 2026-07-25

Scope: narrow decision-trigger repair for the DM-58 Coordinate Reclamation Fronts mission.

## Change

`common/scripted_triggers/006_independence_wave_decision_triggers.txt` now makes `is_independence_wave_reclamation_front_member_candidate` mirror the paid resolver's owner legality checks before the mission can be selected.

Each candidate state now rejects a self-owned state, a state whose owner is already in the Event 006 league, an existing war with the member, an unavailable war declaration, or an existing `take_state_focus` wargoal against that owner.

The resolver remains the authoritative synchronized lock: it still selects one state and one living external owner per member, prevents duplicate state and owner entries through the frozen global arrays, and rolls back all staged claims and finite wargoals before any strategic or security cost is paid when the required distinct-front count is not reached.

## Validation

- Read the offline trigger/effect documentation and the vanilla `can_declare_war_on` and `has_wargoal_against` precedents before editing.
- Re-read the resolver at `common/scripted_effects/006_independence_wave_decision_effects.txt:667` and its rollback at `:718` to keep the availability probe aligned with the cost-atomic path.
- No Hearts of Iron IV process was launched and no live scenario execution was claimed.

## Remaining boundary

The mission availability trigger is still a read-only candidate probe; the synchronized resolver remains the final injective state/owner lock because ordinary triggers cannot reserve several candidate members atomically during availability evaluation.
