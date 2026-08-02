# Fallout Thaw Water chain proof

## Implemented surfaces

- Constants: `common/script_constants/fallout_consolidated_constants.txt`
- Dynamic modifiers: `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`
- Triggers: `common/scripted_triggers/fallout_consolidated_triggers.txt`
- Effects: `common/scripted_effects/fallout_consolidated_effects.txt`
- Candidate producer: `common/scripted_effects/fallout_consolidated_effects.txt`
- Events: `events/fallout_world_end_events.txt`, ids `chaosx.fallout.457` through `.463`
- Event Log mappings: `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and the dedicated payload localisation file
- Localisation: `localisation/english/fallout_consolidated_l_english.yml`
- Asset wiring: `interface/fallout_consolidated.gfx`, `gfx/event_pictures/fallout/report_event_fallout_thaw_water.dds`, and the dedicated source and manifest package

## Deterministic state and scheduler proof

The candidate selects the lowest owned native state with current Fallout identity, durable resources, produced Air Winter provenance, a thaw-eligible visual state, surviving population, exposure in range, reclamation, low water security, and high disease pressure. The producer initializes five persistent Thaw Water ledgers and records candidate `457`, transaction `710039`, route `7139`, history `9144`, Air Winter phase six, and the target state.

The chain freezes all nine result inputs before scheduling a 60-day delayed result. The 480-day callback uses the same state, owner, generation, result ticket, and callback ticket. Cleanup releases delayed transactions through the shared coordinator, marks the memory closed before clearing the state registry, and clears all frozen ledgers so the candidate cannot reopen as an unbounded loop.

## Mechanical proof

The four branches have distinct costs and outcomes. Draining lowers flood pressure and can stabilize the settlement. Evacuating raises water safety at a supply and manpower cost. Rebuilding raises channel trust and infrastructure capacity. Using floodwater fields trades recognition and food for a monitored agricultural gamble. Result and callback failures use `apply_exact_state_civilian_population_loss`, state building damage, Air Winter water and disease changes, exposure, and supply loss.

## Air Winter proof

The opening trigger explicitly requires `air_winter_visual_thaw_is_eligible = yes`. Success and partial outcomes improve `air_winter_water_security` or limit its loss. Failure reduces water security and increases disease pressure. The chain therefore consumes and writes the same normal-map winter state used by the Air Winter visual system.

## AI and ownership boundary

Human and hidden-AI lanes share delayed tickets, owner and generation receipts, Event Log payloads, and cleanup. The chain does not use zombie ids, zombie files, zombie assets, native character creation, dynamic successor tags, native state-population relocation, native wildlife simulation, or mutant-country creation.

## Static review record

The tranche review records unique event ids and candidate keys, balanced new script blocks, absent unsupported comparison operators, absent em dashes and semicolons, no split `fallout` token, localisation BOM, resolved dedicated localisation keys, and the runtime DDS header. No HOI4 runtime was launched.

The chain remains dormant and earns zero release-floor credit until scheduler activation, host authority, save recovery, multiplayer behavior, full-screen Fallout blackout, and runtime Event Log delivery are observed.
