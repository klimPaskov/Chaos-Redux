# Event 012 Gods of Africa Evolution I consolidation clock

Disposition: **implemented** for the activation timing anchor; overall Gods of Africa completion remains partial.

## Acceptance basis

The active user objective requires Africa Is One, a valid unifier, Evolution I, and a passed consolidation delay before activation.

The current feature contract in `docs/events/012_africa/gods_of_africa.md` states that Evolution I starts the 180-day host-owned consolidation clock, and the Evolution I effect calls `africa_gods_of_africa_begin_consolidation`.

## Implementation

`gods_of_africa_start_consolidation` now sets `gods_of_africa_consolidation_start_day` to `global.num_days` when the Evolution I owner path initializes the subsystem.

The former anchor, `africa_host_established_day`, is written when a unifier is established or transferred and may be much older than Evolution I, allowing the former due date to expire before the subsystem's accepted delay began.

The helper adds `constant:gods_of_africa_timing.consolidation_days` (180 days), schedules `chaosx.nr12.600`, and `.600` rechecks the current host, Evolution I, Event 012 state, and generation before activation.

The SCN-011 Africa Is One path uses the same initializer, so its clock also starts when that scenario records Evolution I.

## Evidence and limits

The relevant source paths are `common/scripted_effects/012_africa_gods_effects.txt`, `common/scripted_effects/012_africa_evolution_effects.txt`, `common/scripted_effects/012_africa_triggerable_scenario_effects.txt`, `common/scripted_triggers/012_africa_gods_triggers.txt`, `common/script_constants/012_africa_gods_constants.txt`, and `events/012_africa_gods_of_africa.txt`.

The narrow HOI4 MCP event inspect and timing render returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics, but their focused boundary deferred helper projections and lifecycle passes; they do not establish runtime timing or activation.

No AI weights changed, so no probability comparison was required for this patch.
