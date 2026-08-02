# Event 012 weather-attempt cooldown closure

## Scope

This handoff closes the partial/failure retry path for the Rain and Drought action family without adding a second action ledger, target store, tag, model, or recurring world scan.

## Defect

`africa_call_hostile_natural_disaster_from_action` runs only for a full shared-action result, so its 180-day weapon cooldown was absent after partial and failed results even though the caller reserve had already been paid.

## Change

`africa_cleanup_action` now detects a consumed weather reserve before clearing it. It applies `constant:africa_natural_disaster.cooldown_days` to the current host and, when the action has a saved priority-member actor, to that actor as well. Existing cooldown flags are guarded so a full Event 013 bridge is not extended or duplicated.

## Validation

The source review confirms both weather action IDs still use the shared quote, mission, target, reservation, and cleanup kernels. Full results keep the existing Event 013 bridge cooldown; partial and failed results now receive the same actor cooldown during cleanup. The existing exact target and global-pointer cleanup remains unchanged.

No live HOI4 session was launched. Required live receipts remain: full accepted/rejected/backfire, partial, failed, host caller, member caller, and retry-blocked scenarios for both Rain and Drought.
