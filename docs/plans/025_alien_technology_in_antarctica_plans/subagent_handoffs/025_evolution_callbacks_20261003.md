# Event 025 delayed evolution callback guards, 2026-10-03

Disposition: implemented within the user-authorized rework.
Acceptance basis: all five evolutions must respect their own Event Details toggle and Chaos gate, including delayed delivery and replacement of an invalid scheduler.

The scheduling effect sets temporary evolution-log context before checking the shared settings trigger.
That context does not survive into a delayed country event or a later pulse.
Callbacks and scheduler-rehome checks now use exact stage-specific read-only guards.
Each guard reads its stable shared settings flag and the existing threshold from chaosx_nr25_evolution_gate.
The 200, 400, 600, 800 and 1000 thresholds and all MTTH parameters are unchanged.

Files:
- common/scripted_triggers/025_alien_technology_in_antarctica_evolution_gate_triggers.txt
- five rehome checks in common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt
- five event triggers in events/025_alien_technology_in_antarctica.txt
- .tools/test_event025_evolution_callbacks.py

Four source-execution tests pass.
They test all threshold boundaries, each toggle against the other four tracks, absent/foreign temporary context, and wiring of all five callbacks and rehome paths.
The existing nine recovery and ten lifecycle tests still pass.

The temporary-variable lifetime rule is documented in the offline Data structures wiki, Variables section, lines 440–442.
The reference states that temporary variables do not carry into events and remain unscoped during their originating effect.
The shared has_disabled_current_evolution trigger builds its settings address from that temporary context.
The new guards bypass only that lost-context dependency; shared UI, history, settings implementation, and owner technology logic are unchanged.

Independent probability and completion audits remain unresolved because the workers failed with workspace routing discovery timed out.
Narrow domain MCP retries and user-owned live-game evidence remain separate acceptance gates.
This patch does not claim that disabled tracks' already-active hazard cleanup, evolved first openings, or the whole Event 025 rework are complete.
No route or requested requirement was removed as a simplification.
