# Event 012 result, world-order text, and capacity visibility tranche

## Scope

This bounded tranche closes three presentation-facing gaps without changing tags, models, action IDs, external package gates, or terminal readiness flags.

## Changes

- `africa_resolve_action` snapshots `africa_active_action_objective` before creating `chaosx.nr12.220`. Idempotent cleanup keeps the same snapshot for later history, so the result popup reads the row-specific objective rather than the neutral label.
- `africa_world_order.110.d` and `africa_world_order_terminal_presentation_not_ready_tt` now describe unresolved continental diplomacy and the closing ceremony in player-facing political language. They no longer expose package, asset, review, roster, or implementation terminology.
- `africa_charter_gui_project_summary` now shows active project/action caps plus administration and intelligence capacity lanes. These values are the existing host variables consumed by the shared action quote; no second capacity store was added.

## Files

- `common/scripted_effects/012_africa_action_effects.txt`
- `localisation/english/012_africa_world_order_l_english.yml`
- `localisation/english/012_africa_charter_gui_l_english.yml`
- `docs/events/012_africa/action_duration_objective_contract.md`
- `docs/events/012_africa/overview.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_action_objective_result_visibility_2026-08-02.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_charter_gui_handoff_2026_07_24.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-07-30_g1_diaspora_owner_protocol_handoff.md`

## Validation boundary

The patch preserves existing localisation keys, uses already-initialised host variables, and introduces no gameplay readiness setter. Static script/localisation checks and focused Event 012 inspection remain required; live popup ordering and GUI rendering remain user-owned.
