# Subagent Prompts

These prompts are implementation handoffs. Spawn every project subagent with `fork_context=false`.

Replace `<MOD_ROOT>` only after resolving the real Chaos Redux repository root.

Required prompts:

- `01_repo_explorer.md`
- `02_scripted_system_architect.md`
- `03_ai_probability_auditor_baseline.md`
- `04_decision_mission_auditor.md`
- `05_localisation_auditor.md`
- `06_icon_artist.md`
- `07_generated_event_art.md`
- `09_documentation_curator.md`
- `10_improvement_loop_planner.md`
- `11_event_completion_auditor.md`
- `12_spreadsheet_doc_worker.md`

Conditional prompts:

- `08_asset_source_researcher.md`
- `13_skill_maintainer.md`
- `14_country_package_auditor.md`
- `15_focus_tree_auditor.md`

The AI probability auditor requires a second compare pass after weighted patches. Reuse prompt 03 with the final source and require `hoi4.probability_compare` against the same scenario IDs.
