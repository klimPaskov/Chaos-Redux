# Independence Wave planning package

Event ID: `6`

Event name: Independence Wave

Event type: Minor Repeatable

Cluster: Liberations

This folder is the source specification package for the Event 6 rework. The package is design-first. It defines player experience, release logic, country coverage, regional overlays, mechanics, focus architecture, decisions, missions, formables, league behavior, AI, achievements, visual direction, approved super-event research packages, triggerable scenario behavior, and acceptance criteria.

All route, focus, event, decision, achievement, country, faction, and super-event names in this package are working labels unless a source note explicitly says otherwise. They are not final localisation.

## Research completion layer

The added research layer contains a 206-row resolution matrix, state reservation groups, tag collision audit, ten signature dossiers, a sensitive-identity disposition ledger, final super-event text research, final audio research, and a source register. `research/006_research_completion_report.md` is the entry point.

## Package map

### Specifications

- `specs/006_independence_wave_spec_part_1_core.md`
- `specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md`
- `specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`
- `specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`
- `specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`
- `specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`
- `specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`

### Matrices

- `matrices/006_candidate_country_registry.csv`
- `matrices/006_regional_overlay_matrix.csv`
- `matrices/006_formable_family_registry.csv`
- `matrices/006_decision_mission_map.csv`
- `matrices/006_ai_strategy_matrix.csv`
- `matrices/006_idea_lifecycle_matrix.csv`
- `matrices/006_achievement_matrix.csv`
- `matrices/006_asset_family_registry.csv`
- `matrices/006_wave_tuning_model.csv`

### Diagrams

- `diagrams/006_release_planner_flow.md`
- `diagrams/006_focus_tree_lane_map.md`
- `diagrams/006_league_state_machine.md`
- `diagrams/006_origin_separation_model.md`

### Research

- `research/006_research_completion_report.md`
- `research/006_package_research_resolution.csv`
- `research/006_state_anchor_and_reservation_groups.csv`
- `research/006_tag_collision_and_reuse_audit.md`
- `research/006_signature_country_research_dossiers.md`
- `research/006_sensitive_package_resolution.md`
- `research/006_super_event_text_research.md`
- `research/006_super_event_audio_research.md`
- `research/006_source_register.csv`
- `research/006_historical_and_institutional_research_notes.md`
- `research/006_research_bibliography.md`
- `research/006_sensitive_identity_research_rules.md`

### Prompts

- `prompts/independence_wave_asset_prompt.md`
- `prompts/independence_wave_super_event_prompt.md`
- `prompts/independence_wave_achievement_prompt.md`
- `prompts/independence_wave_decision_mission_prompt.md`
- `prompts/independence_wave_coding_prompt.md`
- `prompts/independence_wave_goal_prompt.md`
- `prompts/independence_wave_subagent_routing_and_briefs.md`

### Quality and handoff

- `quality/source_reading_manifest.md`
- `quality/manual_improvement_loop_review.md`
- `quality/spec_acceptance_checklist.md`
- `quality/simplifications_omissions_and_blockers.md`
- `quality/catalog_alignment_handoff.md`
- `quality/research_acceptance_checklist.md`
- `quality/research_validation_report.md`
- `quality/package_manifest.md`

## Source-of-truth rules

The seven files under `specs/` are the event design source. The CSV matrices are authoritative registries for broad coverage and should be read alongside the relevant spec part. The prompt files translate the source design into bounded implementation, asset, research, audit, and catalog tasks.

The research-complete package assigns a resolved registered or reserved tag to every candidate, provides a dated public state-ID anchor baseline and reservation group, closes every candidate research disposition, and approves both super-event text and audio source packages. Installed-game state rebinding, a final repository collision scan, final localisation outside the approved super-event text, asset production, audio conversion, focus coordinates, and gameplay validation remain implementation work. Every new Event 6 tag ends in `X`.
