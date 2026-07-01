# Event 013 Natural Disasters Planning Package

This package is a source-spec handoff for the full rework of Event 013, Natural Disasters.
It expands the user brief into a reusable disaster season system, detailed disaster-family mechanics, recovery decisions, cluster behavior, manual scenario behavior, evolution behavior, scripted GUI needs, super-event directions, achievement directions, and coding prompts.

The package uses working labels for routes, systems, files, disaster families, and prompt routing. It does not provide final player-facing localisation. Final event text, decision text, focus text, achievement text, GUI labels, super-event titles, super-event quotes, cultural remarks, and audio choices must be written or researched during implementation.

## Internal structure

- `specs/013_natural_disasters_spec_part_1_core.md`
- `specs/013_natural_disasters_spec_part_2_disaster_families.md`
- `specs/013_natural_disasters_spec_part_3_evolutions_cluster_scenario.md`
- `specs/013_natural_disasters_spec_part_4_api_acceptance.md`
- `specs/013_natural_disasters_spec_part_5_text_gui_documentation.md`
- `matrices/013_natural_disasters_hazard_region_matrix.md`
- `matrices/013_natural_disasters_sequence_api_examples.md`
- `prompts/013_natural_disasters_localisation_prompt.md`
- `prompts/013_natural_disasters_spreadsheet_prompt.md`
- `matrices/013_natural_disasters_disaster_family_matrix.md`
- `matrices/013_natural_disasters_recovery_decision_matrix.md`
- `matrices/013_natural_disasters_ai_tuning_matrix.md`
- `prompts/013_natural_disasters_asset_prompt.md`
- `prompts/013_natural_disasters_super_event_prompt.md`
- `prompts/013_natural_disasters_achievement_prompt.md`
- `prompts/013_natural_disasters_decision_mission_prompt.md`
- `prompts/013_natural_disasters_coding_prompt.md`
- `prompts/013_natural_disasters_goal_prompt.md`
- `research/013_natural_disasters_research_notes.md`
- `research/013_natural_disasters_catalog_alignment.md`
- `subagent_handoffs/013_natural_disasters_subagent_routing_plan.md`
- `source_reading_manifest.md`

## Design boundary

Event 013 remains a minor repeatable event, but one fired event represents a whole disaster season. The individual earthquakes, floods, storms, fires, and abnormal disasters inside that season are not separate Event Log entries. The deaths system, disaster reports, recovery decisions, super-event moments, and the manual Disaster Barrage scenario can still record their own appropriate surface data.

The rework integrates the old Earth Earthquake concept from Event 046 into Evolution III as the global rupture family. It also turns the old Sandstorm Event 099 into a placeholder once Event 013 owns reusable sand and dust storm behavior. Event 051 Heat Wave remains separate, while Event 013 heat-wave disasters must avoid stacking with it.
