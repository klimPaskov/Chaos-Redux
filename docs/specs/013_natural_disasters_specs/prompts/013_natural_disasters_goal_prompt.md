/goal Implement the full Event 013 Natural Disasters rework from the source spec package.

Read and follow:
- `docs/specs/013_natural_disasters_specs/013_natural_disasters_spec_part_1_core.md`
- `docs/specs/013_natural_disasters_specs/013_natural_disasters_spec_part_2_disaster_families.md`
- `docs/specs/013_natural_disasters_specs/013_natural_disasters_spec_part_3_evolutions_cluster_scenario.md`
- `docs/specs/013_natural_disasters_specs/013_natural_disasters_spec_part_4_api_acceptance.md`
- `docs/specs/013_natural_disasters_specs/013_natural_disasters_spec_part_5_text_gui_documentation.md`
- the package prompts for assets, super-events, achievements, decisions, and coding.

Non-negotiables:
- Event 013 is Minor Repeatable and one firing is a delayed disaster season.
- Individual disasters inside a season must not create separate Event Log entries.
- Baseline disasters must damage buildings and reduce real state population through the Deaths system.
- Delays are required, with baseline roughly five to ten days and compressed delays for larger seasons.
- Every disaster family needs unique target logic, damage, aftermath, recovery hooks, AI priority, and news policy.
- Evolution I adds varied multi-region seasons.
- Evolution II creates global disaster seasons, throttled news, multi-state damage, and chained aftermath.
- Evolution III adds meteor showers, global rupture, massive eruptions, delayed tsunamis, and moving storm corridors with scripted GUI and animated assets.
- Disaster Response and Reconstruction decisions must use concrete costs and missions, not a political power store.
- Other events must be able to call individual disasters through reusable scripted effects or triggers.
- SCN-007 Disaster Barrage must use the same sequence controller.
- Natural Disasters clusters must support multiple delayed Event 013 members.
- Event 046 Earth Earthquake and Event 099 Sandstorm become placeholders after their logic is integrated. Event 051 Heat Wave remains separate and must not stack with Event 013 heat.
- Super-event titles, quotes, remarks, and audio require research and documentation before final wiring.

Keep iterating until the implementation satisfies the spec to its fullest extent. Do not use fallbacks or simplifications without explicit approval. Do not claim completion until gameplay, localisation, event log, deaths, decisions, GUI, assets, super-events, docs, catalog alignment, AI behavior, and validations are complete or honestly reported as blocked.
