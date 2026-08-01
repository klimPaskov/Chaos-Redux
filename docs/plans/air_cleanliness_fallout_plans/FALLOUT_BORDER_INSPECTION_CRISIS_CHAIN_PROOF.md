# Border Inspection Crisis chain proof

## Ownership

The chain is Fallout-owned and dormant. Gameplay source lives in `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_world_end_border_inspection_crisis_event_triggers.txt`, `common/scripted_effects/fallout_world_end_border_inspection_crisis_event_effects.txt`, the Border Inspection Crisis constants, the dedicated dynamic modifiers, and the candidate producer block in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.

Candidate `726`, transaction `710075`, route `7182`, history `9181`, and event ids `726` through `732` are unique to this chain. The route upper bound is `7183`.

## Mechanics

The producer selects the lowest eligible native Quarantine Air Winter state after the Clean Certificate memory and requires a foreign neighboring state. The opening receipt freezes both state identities, both owners and controllers, generation, Air Winter values, Supply Access, health ledgers, border ledgers, trade dependency, crossing backlog, and cause memory. Delayed result, callback, and cleanup triggers revalidate the same receipts and reject stale ownership, control, generation, or neighbor relationships.

Four player branches have separate costs, AI priorities, thresholds, Air Winter deltas, resource deltas, social ledgers, bilateral opinion outcomes, and persistent memories. Hidden AI selects the highest affordable branch score and uses the same scheduling path as a human choice. A failed result and failed callback call `apply_exact_state_civilian_population_loss` with the Fallout aftermath Deaths reason and a minimum remaining population.

The result writes survivor-country Event Log history payloads through `events_log_system_event_id = 9181` and `fallout_event_726_log`. The main Event Log scripted localisation routes history `9181` to `fallout.event_log.border_inspection_crisis`, and the dedicated payload localizer covers all four choices, twelve branch outcomes, three callback outcomes, and cancellation. Cleanup releases the target and neighbor reservations and preserves the branch memories.

## Engine-sensitive surfaces recorded

The chain uses the existing state-scope `any_neighbor_state`, `every_neighbor_state`, `is_owned_by`, `owner`, `CONTROLLER`, `state = var:`, `var:` scope, `add_opinion_modifier`, `set_state_flag`, and `clear_state_flag` patterns already used by repository border and bilateral systems. It uses the existing Fallout delayed-result and authenticated cleanup helpers rather than a second scheduler or an ordinary super-event. The dedicated GFX sprite is registered in `interface/fallout_world_end.gfx` and points to the dedicated Fallout asset path.

This proof is source evidence only. Hearts of Iron IV was not launched, and no live dispatch, save recovery, multiplayer, or player-facing render claim is made here.
