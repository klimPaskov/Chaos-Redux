# Event 062: Allies Backstab

## Authority and disposition

The original source review records supplied planning inputs and limitations.
The seven numbered parts, quality matrices, and specialist prompts preserve the planner’s selection, war, crisis, evolution, super-event, and achievement proposals.
Acceptance remains `unresolved` where the original user brief or attributable parent decision cannot be recovered; preserve those claims for review under [AGENTS.md](../../../AGENTS.md#specs-and-plans).
The [design record](research/062_allies_backstab_source_review.md) and numbered specifications are the design map; [current event guidance](../../../.claude/skills/chaos-redux-events/SKILL.md) and [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md) own implementation workflow.
Original source-reading, repository-baseline, tooling-failure, and manual-review reports are historical planning evidence, not current source verification, service-health findings, or completed independent audits.


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

The files under `specs/` hold the event design for review. The files under `quality/` define proof requirements, audit scenarios, and implementation boundaries. The files under `prompts/` are context-complete handoffs for implementation and specialist work.

Final localisation must be written during implementation. Working labels in this pack describe functions and should not be copied into player-facing text without a localisation pass.

## Source limitations

The original planning environment had no repository, wiki, vanilla files, MCP, or subagent runtime; [the source review](research/062_allies_backstab_source_review.md) records those limits. Repository paths, engine precedents, and exact Clausewitz effect availability remain implementation verification gates.

## Changelog

### 2026-10-10 spec audit

- Pool the Emergency Reserves is removed. It rebuilt ordinary lend-lease as a separate decision with its own cooldown and floors; the Expelled Governments Liaison now grants mutual military access and co-victims share equipment through lend-lease.
- The category header shows four items (role, Crisis Cohesion stage, principal mission, linked opponent); the exact cohesion value, next threshold, and side leader move into the role line or tooltip.
- The README's planning-environment limitations are shortened to a pointer to the source review. Subagent instructions use the Claude-first wording.
