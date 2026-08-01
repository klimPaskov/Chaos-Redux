# Children of the Cordon chain proof

## Ownership

The chain is Fallout-owned and dormant. Gameplay source lives in `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_world_end_children_of_cordon_event_triggers.txt`, `common/scripted_effects/fallout_world_end_children_of_cordon_event_effects.txt`, the Children of the Cordon constants, the dedicated dynamic modifiers, and the candidate producer block in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.

Candidate `733`, transaction `710076`, route `7184`, history `9182`, and event ids `733` through `739` are unique to this chain. The route upper bound is `7185`.

## Mechanics

The producer selects a country with a completed Border Inspection Crisis memory, a current durable survival row, a generation-change count, and one affordable branch. The opening freezes country-level Cohesion, Food, Shelter, Recognition, generation, youth trust, and movement-law values without manufacturing a state target. The result and callback authenticate country ownership and scheduler generation before applying effects.

Four branches have distinct costs, AI priorities, viability thresholds, dynamic modifiers, government-route values, and youth or movement-law consequences. The result and callback share the human and hidden AI lane effects. Result failure and callback failure call `apply_exact_state_civilian_population_loss` with the Fallout aftermath Deaths reason and a minimum remaining population across every owned state.

The result writes history payloads through `events_log_system_event_id = 9182` and `fallout_event_733_log`. The main Event Log scripted localisation routes history `9182` to `fallout.event_log.children_of_cordon.detail`, and the dedicated payload localizer covers all four choices, twelve result outcomes, three callback outcomes, and cleanup-safe fallback text.

## Engine-sensitive surfaces recorded

The chain uses the established country-scope candidate registry, ordinary receipt authentication, delayed-result scheduling, delayed cleanup release, `every_owned_state`, `apply_exact_state_civilian_population_loss`, dynamic modifiers, and Event Log history helpers already used by adjacent Fallout chains. It uses no invented state target and does not add an `on_daily` world iterator. The dedicated GFX sprite is registered in `interface/fallout_world_end.gfx` and points to the dedicated Fallout asset path.

This proof is source evidence only. Hearts of Iron IV was not launched, and no live dispatch, save recovery, multiplayer, or player-facing render claim is made here.
