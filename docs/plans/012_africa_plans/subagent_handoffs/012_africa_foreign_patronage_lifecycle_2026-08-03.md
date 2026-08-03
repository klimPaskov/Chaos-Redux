# Event 012 foreign-patronage lifecycle repair

## Finding

The `counter_foreign_patronage` action (62) required `africa_foreign_patronage_active`, but the Event 012 source had no writer for that flag. The player and AI validators therefore could never accept a documented foreign-sponsored African state.

## Implemented repair

- `common/scripted_effects/012_africa_effects.txt` now defines `africa_reconcile_foreign_patronage_state`.
- `common/on_actions/012_africa_world_order_on_actions.txt` calls the helper from `on_join_faction` and `on_leave_faction`.
- The relationship transition calls the same helper immediately after registration, so a member that was already factioned when it entered the Charter still receives the derived receipt.
- The helper sets the receipt only for a current-generation registered Event 012 member that joins a faction led by an external, non-member leader outside the host's faction. It clears the receipt on departure or when the callback does not prove that relationship.
- The callback is country-bounded and does not use a recurring action or world iteration. It preserves the existing Action 62 success cleanup and temporary patron-state update.

## Validation and remaining boundary

Static source review must confirm one helper definition, two lifecycle callsites, and the existing Action 62 read/clear paths. The Event 012 root/event lint remains the appropriate parser check. Faction-leader succession without a join/leave callback is not inferred; future work may add a bounded leadership transition owner if the accepted specification requires it.
