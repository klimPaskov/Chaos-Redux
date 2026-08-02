# Fallout Ration Thief Election chain proof

## Scope

Candidate `394` is implemented as a dormant country-level chain in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. It uses event blocks `394` through `400`, transaction key `710030`, route `7130`, and Event Log history `9135`.

## Authored mechanics

- The opening selects the lowest qualifying native state id through `fallout_event_394_ration_state_is_current`.
- The country gate requires current Fallout registry and resource rows, surviving population, accepted state grades, Air Winter exposure bounds, and food, medicine, recognition, and cohesion reserves.
- Public election, tribunal, purge, and private settlement are distinct government-aware policies with different costs and consequences.
- Frozen food, medicine, recognition, cohesion, ration trust, government legitimacy, and faction pressure ledgers grade success, partial success, or failure after 28 days.
- Results alter survival resources, cohesion, stability, war support, reclamation, supply access, exposure, government ledgers, dynamic state modifiers, branch memories, building integrity, and population through `apply_exact_state_civilian_population_loss` on failure.
- A 240-day second-count callback applies a second authored outcome, records a second Event Log payload, and schedules scheduler-owned cleanup.
- Human and hidden AI paths use separate event tokens and visible-budget modes. Cleanup clears frozen inputs, registry pointers, tickets, and temporary flags while retaining durable state memories and history.

## Cross-file wiring

- Constants: `common/script_constants/fallout_consolidated_constants.txt`.
- Triggers: `common/scripted_triggers/fallout_consolidated_triggers.txt`.
- Effects: `common/scripted_effects/fallout_consolidated_effects.txt`.
- Candidate row: `common/scripted_effects/fallout_consolidated_effects.txt`.
- Dynamic modifiers: `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`.
- Events: `events/fallout_world_end_events.txt`.
- Event Log mappings: `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and the dedicated scripted localisation file.
- Localisation: `localisation/english/fallout_consolidated_l_english.yml`.
- Asset package: `docs/assets/air_cleanliness_fallout/fallout_ration_thief_election/` with dedicated runtime DDS and GFX registration.
- Catalog row: `FALLOUT-394` in the workbook and exported Events CSV.

## Static review evidence

The new script files have balanced braces and no unsupported comparison operators. Event ids `394` through `400` occur exactly once. All event title, description, option, tooltip, and Event Log localisation references resolve within the dedicated BOM-prefixed file. The runtime DDS is 210 by 176 with one mip level, uncompressed 32 bit BGRA payload, and 147968 bytes. No zombie asset, zombie id, zombie audio, zombie sprite, or zombie path is referenced.

## Dormant boundary and engine status

The candidate row does not set scheduler activation flags and no event is fired by the producer. No HOI4 runtime was launched for this tranche. The chain proves source structure, deterministic selection, receipt ownership, delayed result data, and cleanup design only. Live scheduler delivery, host authority, multiplayer save recovery, and countable release-floor credit remain unproven.
