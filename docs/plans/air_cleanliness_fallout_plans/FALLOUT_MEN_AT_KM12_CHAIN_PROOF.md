# Fallout The Men at Kilometer Twelve chain proof

## Ownership

The chain is owned by `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. It uses event ids 506 through 512, candidate 506, transaction 710046, route 7146, and history 9151. It does not reuse zombie ids or assets.

## Static implementation evidence

- `common/script_constants/fallout_consolidated_constants.txt` contains branch, timing, resource cost, viability, Deaths, state, trust, raider, modifier, AI, and history values.
- `common/scripted_triggers/fallout_consolidated_triggers.txt` authenticates the current Air Winter state receipt, country row, target, generation, owner, result, and cleanup.
- `common/scripted_effects/fallout_consolidated_effects.txt` contains the Deaths requests, deterministic outcome, four costs, delayed result, branch-aware result effects, callback, Event Log record, and idempotent cleanup.
- `common/scripted_effects/fallout_consolidated_effects.txt` initializes durable trust and raider ledgers, selects the lowest eligible state, and appends one dormant typed candidate row.
- `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt` exposes route supply, army readiness, and failure attrition outcomes.
- `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt` route history 9151.
- `interface/fallout_consolidated.gfx` registers the dedicated report picture. The source, processed PNG, runtime DDS, hashes, prompt, and handoff are under the dedicated asset package.

## Review boundary

The source is static proof only. The scheduler activation flags remain unset by design. No HOI4 runtime was launched. A live session is still required to prove target retention across 120 and 210 day receipts, Deaths readback, state modifier expiry, save reconstruction, multiplayer host behavior, and hidden AI parity.
