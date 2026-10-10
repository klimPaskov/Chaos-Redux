# Event 050: The Great Embargo specification pack

## Authority and current workflow

The [source conflict ledger](matrices/050_source_conflict_ledger.md) records user-design constraints and unresolved cluster data. Supplied-export observations are historical snapshots.
Use current [planning](../../../.claude/skills/chaos-redux-event-planning/SKILL.md), [events](../../../.claude/skills/chaos-redux-events/SKILL.md), [assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md) guidance.
Unattributed design remains `unresolved`; rediscover current tools and source state before a separately authorized implementation task.


This is the source design package for Chaos Redux Event 050, **The Great Embargo**.

The source pack lives at `docs/specs/050_the_great_embargo_specs/`.
The [source conflict ledger](matrices/050_source_conflict_ledger.md) records the originating user-design constraints and unresolved catalog fields.
Related working reviews belong under `docs/plans/050_the_great_embargo_plans/`.

## Accepted catalog identity

- Event ID: `50`
- Event name: The Great Embargo
- Event type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: 1
- Cluster: Negative Economy
- Member severity: Medium
- Public event value: Embargo Pressure

The workbook already places Event 50 in Negative Economy (cluster 10); its details row is still the one-line legacy text and is updated with the implementation wording.
The runtime slot `events/050_the_great_embargo.txt` holds the legacy stub, which registers native embargo claims from every country with no release (see Part 8).

## Source specifications

- `specs/050_the_great_embargo_spec_part_1_core.md`
- `specs/050_the_great_embargo_spec_part_2_pressure_and_economic_impact.md`
- `specs/050_the_great_embargo_spec_part_3_target_responses.md`
- `specs/050_the_great_embargo_spec_part_4_coalition_and_neutrals.md`
- `specs/050_the_great_embargo_spec_part_5_evolutions_and_fragmentation.md`
- `specs/050_the_great_embargo_spec_part_6_ai_balance_and_probability.md`
- `specs/050_the_great_embargo_spec_part_7_presentation_logs_and_assets.md`
- `specs/050_the_great_embargo_spec_part_8_achievements_interactions_and_acceptance.md`

## Matrices and design contracts

- `matrices/050_event_map.md`
- `matrices/050_pressure_state_matrix.md`
- `matrices/050_target_response_matrix.md`
- `matrices/050_coalition_role_matrix.md`
- `matrices/050_runtime_ledger_contract.md`
- `matrices/050_probability_scenario_matrix.md`
- `matrices/050_achievement_matrix.md`
- `matrices/050_asset_requirement_matrix.md`
- `matrices/050_acceptance_scenarios.md`
- `matrices/050_source_conflict_ledger.md`

## Research and diagrams

- `research/050_the_great_embargo_research_notes.md`
- `diagrams/050_the_great_embargo_lifecycle.md`

## Implementation prompts

- `prompts/050_the_great_embargo_goal_prompt.md`
- `prompts/050_the_great_embargo_coding_agent_prompt.md`
- `prompts/050_the_great_embargo_decision_mission_prompt.md`
- `prompts/050_the_great_embargo_script_architect_prompt.md`
- `prompts/050_the_great_embargo_ai_probability_audit_prompt.md`
- `prompts/050_the_great_embargo_asset_prompt.md`
- `prompts/050_the_great_embargo_achievement_prompt.md`
- `prompts/050_the_great_embargo_localisation_audit_prompt.md`
- `prompts/050_the_great_embargo_spreadsheet_prompt.md`
- `prompts/050_the_great_embargo_completion_audit_prompt.md`

## Quality material

- `quality/050_source_reading_ledger.md`
- `quality/050_manual_subagent_review_matrix.md`
- `quality/050_presentation_choice_and_scope_review.md`
- `quality/050_design_risk_register.md`
- `quality/050_spec_completion_checklist.md`
- `quality/050_external_evidence_limits.md`
- `quality/050_planning_completion_report.md`
- `quality/050_package_manifest.md`

## Main design decisions

Each ordinary firing creates one fresh embargo crisis around one eligible player country or major power. Evolution II may create up to three concurrent crises, each with its own target, coalition, Pressure, duration, decisions, and cleanup.

Embargo Pressure is the only persistent custom value shown to the player. Dependence on imported resources, fuel, shipping, and foreign support remains an internal calculation that changes the consequences of a given Pressure level.

The coalition is formed from meaningful economic actors. Resource suppliers, shipping powers, financial centers, neighbors, faction partners, rivals, and replacement-route countries matter more than a raw country count.

The target manages the crisis through a compact decision category. The visible action set changes by phase and never exceeds five primary actions plus one active mission. Stronger late responses replace weaker or irrelevant actions.

The event uses ordinary decision presentation with a static category picture. It has no dedicated mechanic window. Report events, dynamic tooltips, stage text, and map-aware decision targets carry the necessary information.

Evolution I adds secondary sanctions and direct pressure on countries that keep trading with the target. Evolution II permits several embargo systems to overlap and enables temporary cooperation between embargoed countries without creating a formal faction.

Broad expansion stops at the point where the event has a complete crisis loop, meaningful choices, AI behavior, replay value, presentation, achievements, cross-system integration, and clean termination.

## Open questions

- Shared-owner hook: the Famine owner must accept a donor exclusion in Import Food's donor search for coalition members of an active embargo at Pressure 40 or higher (Part 8).
  Until it exists, the embargo has no food consequence, which is safe but weaker.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Recorded that Negative Economy is cluster 10 with Event 50 already a member, replacing the "incomplete cluster export" instructions (README, Part 8).
- Tied the Condemnation section to the implemented native embargo ownership helper and recorded that the legacy stub's unreleased all-country claims must be replaced.
- Replaced `AGENTS.md` and `.agents` skill links with `CLAUDE.md` and `.claude`.

Pass 2, design improvement:
- Replaced the long food-exemption negotiation with one concrete link: coalition members stop being eligible donors for Famine's Import Food at Pressure 40, a food exemption is one concession term, and refusing it during famine counts as relief obstruction.
- Cut the target header from seven items to four (Pressure with stage and direction, the most urgent exposure, the coalition member that matters most, the active route or mission); response effects stay in their own tooltips.
