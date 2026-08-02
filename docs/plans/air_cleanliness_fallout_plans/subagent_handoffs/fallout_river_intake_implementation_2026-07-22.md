# River Intake at Dawn implementation handoff

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
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_RIVER_INTAKE_TUNING_AND_REGISTRY.md`

## Implemented identifiers

- Opening human event 107
- Opening hidden AI event 108
- Human delayed results 109, 110, 111, and 121
- Human callback 112
- Hidden cleanup 113
- Hidden AI delayed results 1009, 1010, 1011, and 1012
- Hidden AI callback 1013
- Event-log history 9106 with fifteen typed payloads

## Handoff notes

The event takes its state from the ordinary Fallout receipt rather than inventing a province or state in event text. It authenticates the state and country ownership again before every result and cleanup. Result and callback receipts are terminalized before their gameplay effects run. The result cleanup can release its row without clearing the registry, and final cleanup waits for both result and callback rows. Failure branches call the shared exact civilian population loss effect, which routes through the Deaths system. The result and callback paths share the same effects for human and hidden AI resolution.

The four authored choices and their values are centralized in the event constants. The water resource, filters, medicine, fuel, recognition, stability, war support, army experience, and state water changes are all branch-specific. The callback creates compact, unequal-access, or epidemic outcomes with durable state memories.

## Known simplifications and blockers

- The chain has no activation caller. It must stay dormant until the Fallout-owned scheduler is reviewed.
- The foreign testing branch is a country modifier and recognition result, not a complete bilateral partner registry. It is a pilot and is not a completed diplomacy chain.
- The event bible's separate river-raid continuation is not implemented in this tranche.
- The engine has not been launched. Numeric state target liveness, delayed receipts, save and multiplayer persistence, modifier placement, Deaths accounting, event-log rendering, and performance remain unproven.
- No water decision surface was added in this tranche. Decisions, missions, and focus links remain future work.
- The water chain is not included in the 660-event release-floor count.

## Static checks

Brace counts are balanced for every touched script and event file. The namespace has no duplicate event IDs. The localisation file retains UTF-8 with BOM. The new water files contain no zombie references and no scheduler activation flags.

## Next review gate

Before activation, prove the state target route with the Fallout scheduler, add a bilateral partner registry for foreign testing, review dynamic modifier placement, and run a static event completion audit. Do not remove the dormant guard until those gates are recorded.
