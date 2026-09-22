# Event 073 planning package

## Deliverable

This package expands the attached Mongols Rise brief into a substantial campaign design and an organized implementation handoff. It extracts directly into `docs/specs/073_mongols_rise_specs/` and `docs/plans/073_mongols_rise_plans/`. It contains no implemented game code, final media, or changes to the live repository.

Read [the specification index](../../specs/073_mongols_rise_specs/README.md), then [the implementation stages](execution/01_implementation_stages.md). The three political paths, all requested expansion directions, four regional country packages, tribute and succession systems, three Evolutions, sixteen achievements, twenty-two action families and thirteen mission families are designed in separate files.

## Status that matters

All 43 supplied textual sources were read, including all twenty subagent profiles. Linked local references and templates, the full repository, the installed game, and the complete mod inventory were not all available. No subagent was executed. The mandatory independent improvement-loop review is still open. Native rendering, media production, and live-game validation were not performed.

The files are a parent-authored planning baseline, not a claim of separate user approval or finished implementation. Exact map bindings, the Karakorum capital move, country and character identities, final media sources, and several engine capabilities require local verification. The source and conflict records state these gaps explicitly.

## Ready task prompts

- [Event 073 achievement implementation and asset prompt](prompts/073_mongols_rise_achievement_prompt.md)
- [Event 073 asset production prompt](prompts/073_mongols_rise_asset_prompt.md)
- [Event 073 implementation prompt](prompts/073_mongols_rise_coding_prompt.md)
- [Event 073 decisions, missions, and GUI prompt](prompts/073_mongols_rise_decision_mission_prompt.md)
- [/goal](prompts/073_mongols_rise_goal_prompt.md)
- [Event 073 super-event research and production prompt](prompts/073_mongols_rise_super_event_prompt.md)

## Handoffs and evidence

### Execution

- [Implementation stages](execution/01_implementation_stages.md)
- [MCP and tool contract](execution/02_mcp_and_tool_contract.md)
- [Durable resume packet](execution/03_resume_packet.md)

### Integration

- [Event engine and catalog handoff](integration/01_event_engine_and_catalog.md)
- [Lifecycle and transaction contracts](integration/02_state_lifecycle_and_transactions.md)
- [Chaos source map](integration/03_chaos_source_map.md)
- [Map bindings, country identities, and compatibility](integration/04_map_bindings_and_compatibility.md)

### Balance

- [Dynamic tuning anchors](balance/01_dynamic_tuning_anchors.md)

### Actions and missions

- [Action and mission matrix](interaction/01_action_and_mission_matrix.md)

### Assets

- [Asset manifest and production gates](assets/01_asset_manifest.md)
- [Mounted model and animation handoff](assets/02_mounted_model_and_animation_handoff.md)

### Research

- [Historical research and authored design](research/01_history_and_design_basis.md)
- [Repository evidence record](research/02_repository_evidence.md)

### Audits and traceability

- [Read status and limits](audits/01_read_status_and_limits.md)
- [Conflicts and dispositions](audits/02_conflicts_and_dispositions.md)
- [Parent design review](audits/03_parent_design_review.md)
- [Requirements traceability](audits/04_requirements_traceability.md)

### Validation

- [Game validation matrix](validation/01_game_test_matrix.md)
- [AI scenario matrix](validation/02_ai_scenario_matrix.md)
- [Actual package check report](validation/03_package_check_report.md)
- [validate_planning_package.py](validation/validate_planning_package.py)

### Source provenance

- [Mongols Rise](sources/073_mongols_rise_original_brief.md)
- [Supplied source records](sources/README.md)
- [source_archive_identity.json](sources/source_archive_identity.json)
- [source_read_ledger.csv](sources/source_read_ledger.csv)

[All twenty separate subagent handoffs](subagents/README.md) state their ownership, required reading, assigned work, expected evidence and NOT EXECUTED status.

## Package checks

The included validator checks manifest hashes and local document links. It does not run Hearts of Iron IV. After extraction, run `python docs/plans/073_mongols_rise_plans/validation/validate_planning_package.py` from the repository or open its report. The final manifest identifies every delivered file except itself.

The 88 game tests and twenty AI scenarios are all marked NOT RUN. They are acceptance work for a future implemented build. Do not change their status because a package hash check passes.

[Manifest of delivered files and SHA-256 hashes](package_manifest.json).
