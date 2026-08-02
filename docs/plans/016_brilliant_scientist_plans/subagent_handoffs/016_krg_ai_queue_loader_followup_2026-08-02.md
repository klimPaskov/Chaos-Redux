# Event 016 Kruger State AI and super-event queue loader follow-up

Date: 2026-08-02

## Scope

This loader-safety follow-up tightens two existing Event 016 consumers without changing route selection, focus order, super-event IDs, rewards, or model contracts.

## Changes

- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` now uses the direct `original_tag = KRG` gate in each plan's `allowed` block and keeps the existing `brilliant_scientist_is_kruger_sovereign_country = yes` condition in `enable`. Formation, project, diplomacy, takeover, and terminal conditions remain unchanged; this avoids evaluating the broader scripted sovereign-country helper as a database-load eligibility gate.
- `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` resolves the first queued actor through `var:global.brilliant_scientist_super_event_queue_actor_entries^0`, matching the repository's persisted-array scope syntax before removing the queue row and dispatching the reserved visible ID.

## Validation and boundary

- Both touched files remain brace-balanced and contain no unsupported comparison operators.
- All 17 AI plan identifiers and their focus lists remain present; the patch changes only the allowed/enable gate placement.
- The super-event queue still removes the first ID and actor row, clears the cleanup flag, and preserves the existing dispatch guard.
- No Hearts of Iron IV session was launched. Formation, AI plan activation, and queued super-event playback remain user-owned live checks.
- No asset, model, event ID, focus, decision, country, or localisation contract was added.
