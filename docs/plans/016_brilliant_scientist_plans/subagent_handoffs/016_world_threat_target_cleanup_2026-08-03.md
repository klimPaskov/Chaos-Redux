# Event 016 world-threat target cleanup handoff

Date: 2026-08-03

## Scope

This narrow repair removes one dead global event target from the Event 016 world-threat activation path. It does not change threat scoring, activation thresholds, super-event IDs, world-end routes, or Fallout ownership.

## Change

`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` no longer calls `save_global_event_target_as = brilliant_scientist_world_threat_actor` when the shared Event 016 threat source activates.

Repository-wide search found no consumer, localisation reference, trigger, cleanup call, or event-log use for `brilliant_scientist_world_threat_actor`. The visible threat package already binds its actor through the queued `brilliant_scientist_super_event_actor` target, so retaining the unused global pointer only left stale state in saves.

## Validation

- The edited file has equal brace counts: 468 opening and 468 closing braces.
- Repository-wide search returns zero remaining references to `brilliant_scientist_world_threat_actor`.
- Focused Event Inspector lint for `chaosx.nr16.918` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. The workspace-wide helper projection remains deferred by the MCP analysis boundary.
- `git diff --check` is clean for the edited file.

## Remaining limits

No live game or save was launched. Native CBRN callback work, quantitative and transfer validation, Event 019 live isolation, GUI/audio presentation, external portrait rights, and the no-model boundary remain unchanged.
