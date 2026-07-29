# Event 269: Names for the Missing

## Player-facing purpose

After mass civilian loss, a country must decide who controls the names of the missing. The event turns incomplete shelter and Deaths records into a political memory choice with consequences for Recognition, Cohesion, resource ledgers, and the next season's public authority.

## Chain layout

| Stage | Human | AI | Delay | Contract |
| --- | --- | --- | --- | --- |
| Opening | 269 | 270 | Immediate receipt | Four country-level policies |
| Delayed result | 271 to 274 | 275 to 278 | 21 days | Branch grading with success, partial, or failure |
| Callback | 279 | 280 | 180 days | Durable memory and maintenance review |
| Cleanup | 281 | 281 | Queue-owned | Release both receipts and clear temporary fields |

The chain uses `chaosx.fallout` ids 269 through 281 and history id 9118. It is owned by the Fallout scheduler and does not reuse zombie ids, paths, art, audio, or sprites.

## Mechanics

Eligibility requires a current country registry, a durable survival resource row, at least 25,000 civilian deaths in the Deaths register, Recognition below 65, and one affordable branch. The country freezes deaths, Recognition, Cohesion, and the Fallout intelligence-exposure ledger before the delayed transaction is reserved. The deterministic score is weighted from Recognition, Cohesion, and a capped death-pressure term.

The four policies have separate costs and outcome effects. All resource changes are clamped through the survival ledger. Failure applies a 0.4 percent state population request through `apply_exact_state_civilian_population_loss`. Callback failure applies 0.2 percent through the same API. No direct population effect exists in this chain.

The result installs one branch-specific timed modifier or a register backlog modifier. The callback installs a maintenance or backlog modifier and closes the durable chain memory. Recognition and exposure remain visible country variables for later cause-memory and successor content.

## Wiring

- Script: `events/fallout_world_end_events.txt`
- Effects: `common/scripted_effects/fallout_world_end_names_missing_event_effects.txt`
- Triggers: `common/scripted_triggers/fallout_world_end_names_missing_event_triggers.txt`
- Constants: `common/script_constants/fallout_world_end_event_constants.txt`
- Modifiers: `common/dynamic_modifiers/fallout_world_end_names_missing_dynamic_modifiers.txt`
- Event Log scripted localisation: `common/scripted_localisation/fallout_world_end_names_missing_event_log_scripted_localisation.txt`
- Event Log central mappings: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and `common/scripted_effects/chaosx_events_log_effects.txt`
- Report art: `interface/fallout_world_end.gfx` and `gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds`
- Player text: `localisation/english/fallout_world_end_names_missing_l_english.yml`

## Runtime review boundary

The candidate is deliberately dormant. It is not counted toward the 660 reviewed event-block release floor until a live activation audit proves receipt production, human and AI dispatch, delayed result and callback delivery, idempotent cleanup, and save recovery. No HOI4 runtime was used for this tranche.
