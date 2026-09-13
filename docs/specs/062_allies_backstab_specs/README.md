# Event 062: Allies Backstab

This folder is the source specification pack for Event 62, Allies Backstab.

## Catalog identity

- Event ID: `62`
- Event name: Allies Backstab
- Type: Minor Repeatable
- Chaos level: `1`
- Cluster: Wars
- Cluster role: High member
- Entry event: `chaosx.nr62.1`

## Design promise

Several alliances identify vulnerable members, remove them, and turn their military power against them. The event selects multiple valid factions in one global firing. Each faction resolves through its own safe transaction so membership changes, subject relationships, existing wars, military access, and delayed declarations cannot produce contradictory war sides.

Weakness drives victim selection, but raw division count is not enough. The selection model also reads manpower, equipment readiness, industry, controlled territory, supply position, military losses, war contribution, political isolation, and current front pressure. Faction leaders are protected during the baseline purge. Strong core members receive major protection without becoming absolutely immune.

The player-facing system stays compact. Participants receive role-specific events and a temporary crisis decision category. One public value, working label `Crisis Cohesion`, summarizes whether their side is disintegrating, shaken, coordinated, or unified. Hidden scoring handles target choice, defection interest, war viability, settlement willingness, and outside support.

## Pack contents

### Source specifications

- `specs/062_allies_backstab_spec_part_1_core.md`
- `specs/062_allies_backstab_spec_part_2_selection.md`
- `specs/062_allies_backstab_spec_part_3_transaction_and_war.md`
- `specs/062_allies_backstab_spec_part_4_decisions_and_missions.md`
- `specs/062_allies_backstab_spec_part_5_evolutions.md`
- `specs/062_allies_backstab_spec_part_6_outcomes_connections.md`
- `specs/062_allies_backstab_spec_part_7_ai_achievements_presentation.md`

### Research and source review

- `research/062_allies_backstab_research_notes.md`
- `research/062_allies_backstab_source_review.md`

### Quality and implementation handoffs

- `quality/062_allies_backstab_chaos_impact_map.md`
- `quality/062_allies_backstab_probability_scenarios.md`
- `quality/062_allies_backstab_acceptance_scenarios.md`
- `quality/062_allies_backstab_implementation_surface_map.md`
- `quality/062_allies_backstab_subagent_handoff_matrix.md`
- `quality/062_allies_backstab_improvement_loop_review.md`

### Separate prompts

- `prompts/062_allies_backstab_asset_prompt.md`
- `prompts/062_allies_backstab_super_event_prompt.md`
- `prompts/062_allies_backstab_achievement_prompt.md`
- `prompts/062_allies_backstab_decision_mission_prompt.md`
- `prompts/062_allies_backstab_coding_prompt.md`
- `prompts/062_allies_backstab_goal_prompt.md`

## Specification authority

The files under `specs/` define the accepted event design. The files under `quality/` define proof requirements, audit scenarios, and implementation boundaries. The files under `prompts/` are context-complete handoffs for implementation and specialist work.

Final localisation must be written during implementation. Working labels in this pack describe functions and should not be copied into player-facing text without a localisation pass.

## Source limitations

Every file supplied with the planning request was read in full, including all records in the three CSV catalogs and all twenty subagent TOML files in the supplied archive. The mounted environment did not contain the Chaos Redux repository, the offline Paradox wiki snapshot, or the installed Hearts of Iron IV vanilla files and documentation. Repository paths, engine precedents, and exact Clausewitz effect availability therefore remain implementation verification gates.

The project subagent definitions were available and fully read. An actual subagent invocation route was not available in the current tool set. A tool registry probe also failed with an HTTP 429 response. The pack includes context-complete handoffs for the required future subagent passes and does not present any section as a subagent-produced result.

No design branch was shortened for speed. The missing repository, wiki, vanilla, MCP, and live subagent checks are recorded as verification blockers, not silently replaced by assumptions.
