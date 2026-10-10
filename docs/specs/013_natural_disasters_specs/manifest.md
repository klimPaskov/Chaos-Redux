# Event 013 Natural Disasters planning package manifest

Accepted source design and historical build material for the implemented Event 013 Natural Disasters engine.
The README is the entry point and records file roles, shared-system hooks, open questions and the changelog.

## Package contents

- `README.md`
- `diagrams/013_abnormal_gui_player_flow.mmd`
- `diagrams/013_abnormal_gui_state_flow.mmd`
- `diagrams/013_disaster_controller_flow.mmd`
- `docs_alignment/013_catalog_and_docs_alignment.md`
- `docs_alignment/013_source_of_truth_and_disposition_map.md`
- `implementation_readiness/013_acceptance_gate_matrix.md`
- `implementation_readiness/013_source_to_file_surface_map.md`
- `implementation_readiness/013_validation_scenario_matrix.md`
- `manifest.md`
- `matrices/013_aftershock_and_aftermath_matrix.md`
- `matrices/013_disaster_call_contract.md`
- `matrices/013_implementation_readiness_ledger.md`
- `matrices/013_news_report_direction_matrix.md`
- `matrices/013_super_event_research_handoff_matrix.md`
- `prompts/natural_disasters_achievement_prompt.md`
- `prompts/natural_disasters_asset_prompt.md`
- `prompts/natural_disasters_decision_mission_prompt.md`
- `prompts/natural_disasters_implementation_resume_prompt.md`
- `prompts/natural_disasters_super_event_prompt.md`
- `research/000_source_reading_log.md`
- `research/001_catalog_notes.md`
- `research/002_public_research_notes.md`
- `research/003_manual_improvement_loop_pass.md`
- `research/004_final_improvement_loop_anti_bloat_closure.md`
- `research/005_second_pass_public_research_notes.md`
- `research/006_second_pass_source_reading_log.md`
- `research/007_second_pass_validation_notes.md`
- `research/008_closure_followup_final_readiness_pass.md`
- `research/008_third_pass_closure_alignment_log.md`
- `research/009_third_pass_validation_notes.md`
- `specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md`
- `specs/013_natural_disasters_spec_part_1_core.md`
- `specs/013_natural_disasters_spec_part_2_reusable_system.md`
- `specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md`
- `specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md`
- `specs/013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md`
- `specs/013_natural_disasters_spec_part_6_presentation_assets_super_events.md`
- `specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md`
- `specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md`
- `specs/013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md`

## Removed files

- `prompts/natural_disasters_continuation_prompt.md`, superseded before the 2026-10-10 audit.
- On 2026-10-10: `implementation_readiness/013_closure_resume_packet.md`, `implementation_readiness/013_dependency_order_and_subagent_sequence.md`, `implementation_readiness/013_final_prompt_for_next_agent.md`, `implementation_readiness/013_simplification_blocklist.md`, `prompts/natural_disasters_coding_prompt.md`, `prompts/natural_disasters_goal_prompt.md` and `prompts/natural_disasters_subagent_routing_prompt.md`, merged into `prompts/natural_disasters_implementation_resume_prompt.md`.

## Historical planning-run limitations

- The original planning run produced documentation only and had no live checkout, offline wiki, vanilla files, game validation or executable subagents.
- Those limits apply to the `research/` logs, which remain unchanged provenance; implementation evidence lives in `docs/events/013_natural_disasters/overview.md` and `docs/plans/013_natural_disasters_plans/`.
