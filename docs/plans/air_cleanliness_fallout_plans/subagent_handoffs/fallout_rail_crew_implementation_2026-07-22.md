# Rail Crew Twenty-Seven implementation handoff

## Status

Implemented as a dormant, uncounted global-survival pilot. The chain is not activated and does not claim a release-floor block.

## Changed files

- `common/script_constants/fallout_consolidated_constants.txt`
- `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `events/fallout_world_end_events.txt`
- `localisation/english/fallout_consolidated_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `docs/assets/fallout_world_end/living_world_pilot/manifest.md`
- `docs/assets/fallout_world_end/living_world_pilot/gfx_handoff.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_RAIL_CREW_TUNING_AND_REGISTRY.md`

## Implemented identifiers

- Opening human event 114
- Opening hidden AI event 115
- Human delayed results 116, 117, 118, and 122
- Human callback 119
- Hidden cleanup 120
- Hidden AI delayed results 1014, 1015, 1016, and 1017
- Hidden AI callback 1018
- Event-log history 9107 with fifteen typed payloads

## Handoff notes

The event takes its state from the ordinary Fallout receipt rather than inventing a province or state in event text. It authenticates the state and country ownership again before every result and cleanup. Result and callback receipts are terminalized before their gameplay effects run. The result cleanup can release its row without clearing the registry, and final cleanup waits for both result and callback rows. Failure branches call the shared exact civilian population loss effect, which routes through the Deaths system. Native rail damage is branch-specific. Human and hidden AI resolution share the same scoring and effect path.

The four authored choices and their values are centralized in the event constants. The transport resource, fuel, scrap, power, recognition, stability, cohesion, war support, rail reclamation, equipment, and native rail effects are branch-specific. The callback creates protected crew, atrocity, or fragmented-route outcomes with durable state and country memories.

## Known simplifications and blockers

- The chain has no activation caller. It must stay dormant until the Fallout-owned scheduler is reviewed.
- The neighbor-access branch records a country and state access pilot. It is not a complete bilateral partner registry and does not write a diplomatic relation.
- The engine has not been launched. Numeric state target liveness, `rail_way` reads, native building damage, delayed receipts, save and multiplayer persistence, modifier placement, Deaths accounting, event-log rendering, and performance remain unproven.
- No transport decision surface was added in this tranche. Decisions, missions, focus links, military operation hooks, and diplomacy links remain future work.
- The rail chain is not included in the 660-event release-floor count.

## Static checks

Brace counts are balanced for every touched script and event file. The namespace has no duplicate event IDs. The localisation file retains UTF-8 with BOM. The new rail files contain no zombie references, no scheduler activation flags, no unsupported comparison operators, and no non-ASCII control characters.

## Next review gate

Before activation, prove the state target route with the Fallout scheduler, validate the native rail and building-damage surfaces, add a bilateral partner registry or narrow the neighbor branch, review dynamic modifier placement, and run a static event completion audit. Do not remove the dormant guard until those gates are recorded.
