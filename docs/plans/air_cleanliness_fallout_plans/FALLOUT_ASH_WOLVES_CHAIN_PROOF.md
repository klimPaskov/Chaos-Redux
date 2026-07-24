# Fallout Ash Wolves chain proof

## Implemented surfaces

- Constants: `common/script_constants/fallout_world_end_ash_wolves_constants.txt`
- Dynamic modifiers: `common/dynamic_modifiers/fallout_world_end_ash_wolves_dynamic_modifiers.txt`
- Triggers: `common/scripted_triggers/fallout_world_end_ash_wolves_event_triggers.txt`
- Effects: `common/scripted_effects/fallout_world_end_ash_wolves_event_effects.txt`
- Candidate producer: `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
- Events: `events/fallout_world_end_events.txt`, ids `chaosx.fallout.450` through `.456`
- Event Log mappings: `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and the dedicated payload localisation file
- Asset wiring: `interface/fallout_world_end.gfx`, `gfx/event_pictures/fallout_world_end/report_event_fallout_ash_wolves.dds`, and the dedicated source and manifest package

## Deterministic state and scheduler proof

The candidate selects the lowest owned native state with the explicit altered-biosphere state receipt, current produced Air Winter provenance, surviving population, and usable reclamation. The country gate requires current Fallout ownership, cause-memory provenance, campaign-day eligibility, and survival resources. The chain freezes its ledgers before scheduling the 60-day delayed result. The 480-day callback and cleanup use the shared delayed-result coordinator and owner and generation receipts. Cleanup closes the cause-memory receipt after both delayed transactions are released, so the candidate cannot reopen as an unbounded loop.

## Mechanical proof

The four branches have distinct costs and outcomes. Hunting changes food, medicine, manpower, safety, pack pressure, military speed, and attrition. Fencing changes supply, infrastructure repair, local movement, and safety. Studying changes research, field safety, medicine, and altered-pressure memory. Leaving the corridor changes recognition, altered ecology, route safety, and state resources. Result and callback failures use `apply_exact_state_civilian_population_loss`, state building damage, exposure, and supply loss.

## Fiction and ownership boundary

The pack is fictional altered ecology. The chain does not use zombie ids, zombie files, zombie assets, native wildlife simulation, native character creation, dynamic successor tags, or mutant-country creation. The localisation explicitly avoids presenting ordinary radiation as a real source of new species.

## Static review record

The final review records brace balance, unique event ids, absent unsupported comparison operators, absent em dashes and semicolons, no split `fallout` token, localisation BOM, resolved dedicated localisation keys, and the runtime DDS header. No HOI4 runtime was launched.

The chain remains dormant and earns zero release-floor credit until scheduler activation, host authority, save recovery, multiplayer behavior, full-screen Fallout blackout, and runtime Event Log delivery are observed. Native wildlife simulation remains an engine-surface boundary.
