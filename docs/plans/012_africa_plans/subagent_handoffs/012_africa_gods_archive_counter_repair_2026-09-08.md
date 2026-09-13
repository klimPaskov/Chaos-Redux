# Event 012 Gods of Africa archive counter repair

## Disposition

Implemented. This repair keeps the owner demand budget correct when a maintained participant is archived for capitulation, deletion, special-country conversion, or host replacement.

## Changed surfaces

- `common/scripted_effects/012_africa_gods_effects.txt`
  - `gods_of_africa_archive_invalid_participant` now decrements `gods_of_africa_active_demand_count` once when the archived participant still carries `gods_of_africa_demand_active`, before removing the participant from the registry.
- `docs/events/012_africa/gods_of_africa.md`
  - Records the counter-release behavior in the bounded registry description.

## Behavior

The archive path remains idempotent and host-local. It only decrements the counter when the host value is present, above zero, and the participant still has an active demand flag, so stale records cannot consume dispatch budget after their demand state is cleared. Normal cleanup and final settlement paths retain their existing accounting.

## Validation

- The edited scripted-effect block remains brace-balanced and uses the existing owner event target and fixed-point counter constant.
- No decision category, non-Africa subsystem, or generic recurring on-action was changed.
- MCP event evidence remains the existing partial aggregate inspection for this large workspace; live save playback remains user-owned.

## Remaining limits

This is a source-level lifecycle repair. The installed MCP adapter does not execute a full annexation/capitulation save scenario, so the exact `REG-08` counter transition remains pending live validation.
