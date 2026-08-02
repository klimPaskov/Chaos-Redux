# The Captain Refuses chain proof

## Static implementation

The chain is defined in `events/fallout_world_end_events.txt` as `chaosx.fallout.520` through `chaosx.fallout.526`. Event `520` is the human opening, `521` is hidden AI choice, `522` and `523` are delayed result reports, `524` and `525` are the command review callback, and `526` releases cleanup. All requests use the shared Fallout scheduler and the existing ordinary receipt coordinator.

The country-owned candidate row is produced by `fallout_event_build_pilot_candidate_registries` in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`. It uses candidate `520`, transaction `710048`, route `7148`, the `war` cooldown family, Equipment as its required resource, Air Winter phase three, and the lowest valid owned exposed state. The producer initializes durable captain-loyalty, mission-mandate, field-autonomy, and refusal-memory ledgers. It never fires an event or sets scheduler activation flags.

The event triggers and effects are isolated in `common/scripted_triggers/fallout_world_end_captain_refuses_event_triggers.txt` and `common/scripted_effects/fallout_world_end_captain_refuses_event_effects.txt`. The result freezes all survival, command, and state receipts, computes a deterministic branch outcome, applies state Supply Access and repairable building consequences, routes failures through the Deaths system, schedules a 240-day callback, records branch and callback history, and clears the registry only after both cleanup receipts have released.

## Dedicated asset evidence

The fictional generated source, prompt, processed PNG, preview, runtime DDS, manifest, and handoff are under `docs/assets/air_cleanliness_fallout/fallout_captain_refuses/`. The mod runtime copy is `gfx/event_pictures/fallout/report_event_fallout_captain_refuses.dds` and the sprite is registered in `interface/fallout_world_end.gfx`.

The source is 1672 by 941 RGB with SHA256 `662DC7B458D703C8B6E7FA836145636101EF5E916A949CAD2334CCEDB3EB5973`. The processed report card is 210 by 176 RGBA with SHA256 `0265124EF75E3DBB758C0C489E7453371291D54C6365BC40DB51AE7C3B36E3CE`. The runtime and mod DDS copies are 147968 bytes with SHA256 `AF44539F129DF9908E4B24A744B539FF98847DF18D595D2CC0F1CED2BBFE97E0`.

## Dormant boundary and blockers

The candidate and event chain remain dormant. Activation flags have no setter in this tranche, so the chain contributes zero countable blocks toward the 660-block release floor. The exact engine-native all-province thermonuclear sweep, host-authoritative full-screen blackout delivery, save recovery, and multiplayer input blocking remain unproven elsewhere in the package. Those surfaces must be proven before any Fallout activation claim.

HOI4 was not launched, per the user's instruction. Static proof does not claim runtime scheduling, AI frequency, save recovery, or presentation success.
