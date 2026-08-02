# The Weapons in the Nursery chain proof

## Static implementation

The chain is defined in `events/fallout_world_end_events.txt` as `chaosx.fallout.513` through `chaosx.fallout.519`. Event `513` is the human opening, `514` is hidden AI choice, `515` and `516` are delayed result reports, `517` and `518` are the safety callback, and `519` releases cleanup. All requests use the shared Fallout scheduler and the existing ordinary receipt coordinator.

The country-owned candidate row is produced by `fallout_event_build_pilot_candidate_registries` in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`. It uses candidate `513`, transaction `710047`, route `7147`, the `war` cooldown family, Power as its required resource, Air Winter phase three, and the lowest valid owned urban state. The producer initializes durable arms-discipline, accident-risk, civic-trust, and nursery-memory ledgers. It never fires an event or sets scheduler activation flags.

The event triggers and effects are isolated in `common/scripted_triggers/fallout_world_end_weapons_in_nursery_event_triggers.txt` and `common/scripted_effects/fallout_world_end_weapons_in_nursery_event_effects.txt`. The result freezes all survival and state receipts, computes a deterministic branch outcome, applies state Supply Access and building consequences, routes failures through the Deaths system, schedules a 180-day callback, records branch and callback history, and clears the registry only after both cleanup receipts have released.

## Dedicated asset evidence

The fictional generated source, prompt, processed PNG, preview, runtime DDS, manifest, and handoff are under `docs/assets/air_cleanliness_fallout/fallout_weapons_in_nursery/`. The mod runtime copy is `gfx/event_pictures/fallout/report_event_fallout_weapons_in_nursery.dds` and the sprite is registered in `interface/fallout_world_end.gfx`.

The source is 1369 by 1149 RGB with SHA256 `96615FF6B3BD6857D309524096A8D3CAD3B3BE1702D90A7D94AA927C5C669ECF`. The processed report card is 210 by 176 RGBA with SHA256 `984134E65971D55BBBAC3802B8D4A21F2E5A00BA1B15A44FF942251988A92E68`. The runtime and mod DDS copies are 147968 bytes with SHA256 `2724BA3368A635A65F621728164372E6258E1A36BCCDE2247690366AE8F4C39B`.

## Dormant boundary and blockers

The candidate and event chain remain dormant. Activation flags have no setter in this tranche, so the chain contributes zero countable blocks toward the 660-block release floor. The exact engine-native all-province thermonuclear sweep, host-authoritative full-screen blackout delivery, save recovery, and multiplayer input blocking remain unproven elsewhere in the package. Those surfaces must be proven before any Fallout activation claim.

HOI4 was not launched, per the user's instruction. Static proof does not claim runtime scheduling, AI frequency, save recovery, or presentation success.
