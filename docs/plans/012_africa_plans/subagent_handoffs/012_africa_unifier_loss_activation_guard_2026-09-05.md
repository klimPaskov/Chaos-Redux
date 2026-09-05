# Event 012 unifier-loss activation guard — 2026-09-05

Disposition: implemented.

The Event 012 Gods initializer now rejects `gods_of_africa_cancelled_on_unifier_loss` in addition to its existing host, generation, capitulation, active-state, and final-settlement gates. This closes the delayed-event edge case where `chaosx.nr12.600` could arrive after a unifier-loss callback, find the consolidation clock no longer valid, and restart the subsystem through the initializer's fallback path.

Evidence:

- `common/scripted_effects/012_africa_gods_effects.txt` adds the loss-receipt guard to `gods_of_africa_initialize_system`.
- `common/scripted_triggers/012_africa_gods_triggers.txt` already rejects the same loss receipt in `gods_of_africa_system_can_activate`.
- `common/on_actions/012_africa_gods_on_actions.txt` calls `gods_of_africa_cancel_on_unifier_loss` for active, pending, or scheduled host state.
- A successor host generation clears the loss receipt during initialization before starting a fresh lifecycle.

Validation boundary: source-level and targeted Event 012 MCP lint remain the applicable evidence. Live save/playback validation is user-owned and was not performed.
