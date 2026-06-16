# Coding-Agent Prompt — Event 013 Natural Disasters

Implement Event 013 Natural Disasters according to this source spec pack:

- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_1.md`
- `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_evolutions_and_variants.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_natural_disasters_decision_mission_map.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_natural_disasters_ai_balance_and_validation.md`
- `docs/specs/013_natural_disasters_specs/matrices/013_natural_disasters_event_log_catalog_and_localisation_map.md`
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_asset_prompt.md`
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_super_event_prompt.md`
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_achievement_prompt.md`
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_decision_mission_prompt.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `hoi4-decisions-missions`, `hoi4-focus-trees` as a negative check for no focus tree need, and `chaos-redux-subagents`.

## Non-negotiables

- Keep Event 13 Minor Repeatable.
- Baseline disaster must clearly name affected area, damage industry and population, and stay noticeable but not campaign-ending.
- Add warning events and recovery decisions/missions.
- Implement disaster families: earthquake, flood, storm, drought, wildfire, landslide/avalanche, volcano, tsunami as chain, and Evolution IV meteor/abnormal variants.
- Implement Evolutions I–IV exactly as mutation tracks, including active-event and pre-fire evolved opening behavior.
- Evolution IV absorbs Event 46 Earth Earthquake. Event 46 must be stripped to placeholder/unknown and removed from active duplicate gameplay.
- No world-end scenario for Event 13.
- Add a manual triggerable scenario that fires disasters in a short period with intensity and type controls.
- Keep Natural Disasters cluster as only Event 13 with Low member severity; do not add other disaster-like catalog events to it.
- Use dynamic target scoring, reusable helpers, script constants, event targets, cleanup, and no scattered magic numbers.
- Use concrete costs in decisions: equipment, trucks, trains, convoys, fuel, manpower, factories, stability, war support, supply, unit presence, XP, or command power when appropriate. Do not make a PP store.
- Add event-log, event detail, evolution detail, cluster detail, scenario detail, docs, and spreadsheet-alignment handoff.
- Add/hand off required assets, including static and animated UI pieces with fallbacks where planned.
- Research final super-event title, quote, button remark, and audio through the super-event workflow if the Evolution IV super-event is implemented. Treat unresearched text/audio as blocked.
- Implement achievements or report them as blocked if achievement system access is unavailable.

## Subagents to use

Use `chaosx_scripted_system_architect` for helpers/constants, `chaosx_decision_mission_auditor` for the response category, `chaosx_localisation_auditor` for visible text, asset subagents for assets, super-event text/audio researchers for the Evolution IV super-event, `chaosx_spreadsheet_doc_worker` after final localisation exists, and `chaosx_event_completion_auditor` before claiming completion.

## Completion report

Report files changed, systems touched, evolutions implemented, disaster families implemented, decisions/missions implemented, scenario support, Event 46 placeholder disposition, cluster disposition, assets status, super-event status, achievements status, validation performed, and all blockers/simplifications. Do not claim complete with placeholders, missing AI, missing localisation, missing assets, stale docs/spreadsheet, or unresolved accepted plans.
