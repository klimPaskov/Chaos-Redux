/goal Implement Event 013 Natural Disasters to its fullest extent from the source pack at `docs/specs/013_natural_disasters_specs/`, especially:
- `specs/013_natural_disasters_spec_part_1.md`
- `specs/013_natural_disasters_evolutions_and_variants.md`
- `matrices/013_natural_disasters_decision_mission_map.md`
- `matrices/013_natural_disasters_ai_balance_and_validation.md`
- `matrices/013_natural_disasters_event_log_catalog_and_localisation_map.md`
- `prompts/013_natural_disasters_asset_prompt.md`
- `prompts/013_natural_disasters_super_event_prompt.md`
- `prompts/013_natural_disasters_achievement_prompt.md`
- `prompts/013_natural_disasters_decision_mission_prompt.md`
- `prompts/013_natural_disasters_coding_prompt.md`

Follow `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and use focus/country package skills as negative checks because this event should not create countries or focus trees.

Pass/fail requirements: keep Event 13 Minor Repeatable; baseline hits a clearly named area, damages industry and population, and is noticeable but not campaign-ending; add warning events; add recovery decisions/missions with concrete costs, not a PP store; implement disaster families and Evolutions I-IV as mutation tracks with active-event and pre-fire evolved openings; Evolution IV includes meteor showers, massive volcano/tsunami/storm variants, and absorbs Event 46 Earth Earthquake. Strip Event 46 to an unknown placeholder and remove duplicate active gameplay. No world-end scenario. Add the manual Disaster Barrage scenario with type and intensity controls. Keep the Natural Disasters cluster as only Event 13 with Low member severity. Wire event log, event details, evolution details, cluster details, docs, localisation, AI, helpers/constants/cleanup, assets, achievements, and spreadsheet handoff.

Use subagents for helpers, decisions, localisation, assets, super-event text/audio, spreadsheet, and completion audit. Treat unresearched super-event title/button/quote/audio as blocked, not as final localisation. Keep iterating until the implementation satisfies the spec; do not claim completion with missing AI, localisation, assets, docs, scenario, achievements, Event 46 cleanup, or unresolved simplifications. Provide a concrete completion report.
