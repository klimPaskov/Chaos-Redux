# Event 013 Natural Disasters planning package

This package contains the expanded Event 013 Natural Disasters source design. It combines the first full source-spec pass, the second continuation pass, and a closure-ready follow-up that does not add new disaster mechanics. The third pass adds implementation-readiness support so the next agent can start coding from the closure handoff instead of reopening broad planning.

## Source-spec parts

- `specs/013_natural_disasters_spec_part_1_core.md`
- `specs/013_natural_disasters_spec_part_2_reusable_system.md`
- `specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md`
- `specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md`
- `specs/013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md`
- `specs/013_natural_disasters_spec_part_6_presentation_assets_super_events.md`
- `specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md`
- `specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md`
- `specs/013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md`
- `specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md`

## Second-pass support files

- `matrices/013_super_event_research_handoff_matrix.md`
- `docs_alignment/013_catalog_and_docs_alignment.md`
- `diagrams/013_abnormal_gui_player_flow.mmd`
- `research/004_final_improvement_loop_anti_bloat_closure.md`
- `research/005_second_pass_public_research_notes.md`
- `research/006_second_pass_source_reading_log.md`
- `research/007_second_pass_validation_notes.md`

## Closure-ready third-pass additions

- `docs_alignment/013_source_of_truth_and_disposition_map.md` records accepted source files, support files, superseded prompts, and coding-pass read order.
- `matrices/013_implementation_readiness_ledger.md` turns the package into implementation gates and forbidden simplification checks.
- `prompts/natural_disasters_implementation_resume_prompt.md` is the practical next prompt for a coding pass.
- `research/008_closure_followup_final_readiness_pass.md` records that no broad new planning was added after the closure handoff.
- `research/009_third_pass_validation_notes.md` records package-level consistency checks.

## Prompt files

The prompt folder includes implementation, asset, super-event, decision and mission, achievement, goal, subagent routing, and implementation resume prompts. The old continuation prompt is superseded because the continuation work has been completed in this package.

## Reading and tooling honesty

The package was created from the uploaded project files and the existing expanded package in this environment. I did not inspect a live Chaos Redux repository checkout, offline `paradox_wiki/`, vanilla HOI4 files, or execute project subagents. The source reading logs state that limitation directly.
