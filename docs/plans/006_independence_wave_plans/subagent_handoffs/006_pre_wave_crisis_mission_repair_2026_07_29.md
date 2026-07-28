# Event 006 pre-wave crisis mission repair — 2026-07-29

## Scope

This narrow implementation repairs the host-facing Independence Wave crisis mission without changing the synchronized release planner, ownership rules, queue protocol, or crisis thresholds.

## Changes

- `common/decisions/categories/006_independence_wave_crisis_categories.txt` keeps the category visible while `independence_wave_open_host_crisis` is active by checking `has_active_mission` in addition to the durable runtime flag.
- `common/decisions/006_independence_wave_crisis_decisions.txt` removes the ineffective mission-local `visible` block, keeps activation in the documented `activation` trigger, and moves the two AI weights into the shared crisis constants.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt` adds the standard 20 command-power requirement to `can_pay_independence_wave_security_standard_cost`, matching the command power deducted by `independence_wave_pay_crisis_cost` and already shown in the cost localisation.
- `common/script_constants/006_independence_wave_crisis_constants.txt` adds `independence_wave_crisis_ai.base = 1` and `independence_wave_crisis_ai.pressure_factor = 2` as the central AI tuning surface.

## Validation

- Offline decision documentation confirms that mission availability controls selection and that mission `visible` is not the mission lifecycle trigger; `has_active_mission` is documented and used by vanilla decision categories.
- The four edited Clausewitz files have balanced braces and no whitespace errors in the edited hunks.
- Static checks confirm the category retains an active-mission visibility branch, the crisis payment trigger requires command power, and the decision reads the central AI constants.

## Remaining boundary

This patch does not claim live UI, AI selection, save/load, queue retry, or allocator execution evidence. Those remain runtime completion gates in the Event 006 source-of-truth map.
