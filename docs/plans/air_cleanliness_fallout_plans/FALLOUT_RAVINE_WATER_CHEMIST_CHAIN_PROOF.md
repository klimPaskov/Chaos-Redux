# Fallout Ravine Water Chemist chain proof

## Reviewed identity

The reviewed row is candidate `499`, transaction `710045`, route `7145`, event ids `499` through `505`, and Event Log history `9150`. It is a follow-up to Ice Melt Rations and remains dormant, so it contributes zero countable blocks to the `0 of 660` release-floor total.

## Entry and determinism

`common/scripted_triggers/fallout_world_end_ravine_water_chemist_event_triggers.txt` requires a current produced Air Winter state, Ice Melt success or partial memory, adaptation, exposure, reclamation, water security, disease pressure, refugee pressure, surviving state population, and a supported urban category. The producer selects the lowest valid target state and a separate lowest-id origin state with surviving population. The origin id is retained until cleanup.

`common/scripted_effects/fallout_world_end_event_candidate_effects.txt` writes one candidate row through the existing Fallout candidate append helper. It does not set an activation flag or fire an event. Human and AI event tokens are separate and use the same target and transaction schemas.

## Four choices and delayed phases

The opening in `events/fallout_world_end_events.txt` exposes a clinic service, a clean-ice family escort, a ravine quarantine, and a shared district method. Each choice has its own Food, Water, Medicine, Filters, Recognition, and Cohesion costs. The result is delayed `49` days and the callback is delayed `210` days. Both phases have visible human and hidden-AI events. Cleanup uses event token `505` and the standard delayed-cleanup receipt.

## Effects and Deaths integration

`common/scripted_effects/fallout_world_end_ravine_water_chemist_event_effects.txt` freezes the numerical contract, calculates deterministic success, partial, or failure outcomes, updates Air Winter disease, refugee, exposure, adaptation, reclamation, and supply values, and applies branch-specific state modifiers. Result failure requests `1.2%` state population loss through `apply_exact_state_civilian_population_loss`. Callback failure requests `0.8%` through the same effect. An escort requests origin-state population loss with `log_deaths = 0`, then moves the applied amount into target-state manpower and refugee-arrival memory. The migration route is recorded on both native states and on the country ledger.

The cleanup effect releases result and callback tickets idempotently, clears frozen values and transient registry state, closes the chain, and preserves durable chemist, disease, method, and migration memories.

## Assets and Event Log

The dedicated asset package is under `docs/assets/air_cleanliness_fallout/fallout_ravine_water_chemist/`. The runtime DDS is wired by `interface/fallout_world_end.gfx` and the event picture uses the same dedicated sprite. The Event Log maps history `9150` in `common/scripted_effects/chaosx_events_log_effects.txt` and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. Fifteen payload selectors live in `common/scripted_localisation/fallout_world_end_ravine_water_chemist_event_log_scripted_localisation.txt`.

## Remaining proof boundary

No HOI4 run was requested or performed. Engine-native scheduler activation, multiplayer host authority, save recovery, blackout input blocking, and all-province thermonuclear sweep remain unproven. This tranche does not claim those surfaces or overall Fallout completion.
