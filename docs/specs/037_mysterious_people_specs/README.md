# Event 037: Mysterious People specification pack

This folder is the accepted planning handoff for Chaos Redux Event 037, **Mysterious People**.

Place the folder at:

```text
docs/specs/037_mysterious_people_specs/
```

The ZIP is arranged for extraction into the repository root.

## Event identity

| Field | Value |
| --- | --- |
| Event ID | `37` |
| Event name | Mysterious People |
| Event type | Minor Repeatable |
| Status before implementation | To Be Reworked |
| Chaos level | `1` |
| Cluster | Various Anomalies |
| Member severity | Low |

## Source specification

1. [`specs/037_mysterious_people_spec_part_1_core.md`](specs/037_mysterious_people_spec_part_1_core.md)
2. [`specs/037_mysterious_people_spec_part_2_population_and_ledger.md`](specs/037_mysterious_people_spec_part_2_population_and_ledger.md)
3. [`specs/037_mysterious_people_spec_part_3_pressure_and_evolutions.md`](specs/037_mysterious_people_spec_part_3_pressure_and_evolutions.md)
4. [`specs/037_mysterious_people_spec_part_4_decisions_missions_and_ai.md`](specs/037_mysterious_people_spec_part_4_decisions_missions_and_ai.md)
5. [`specs/037_mysterious_people_spec_part_5_events_flavour_and_reactions.md`](specs/037_mysterious_people_spec_part_5_events_flavour_and_reactions.md)
6. [`specs/037_mysterious_people_spec_part_6_system_connections.md`](specs/037_mysterious_people_spec_part_6_system_connections.md)
7. [`specs/037_mysterious_people_spec_part_7_assets_achievements_and_catalog.md`](specs/037_mysterious_people_spec_part_7_assets_achievements_and_catalog.md)

## Supporting design files

- [`quality/037_mysterious_people_balance_matrix.md`](quality/037_mysterious_people_balance_matrix.md) defines grant examples, pressure expectations, exploit limits, and tuning review cases.
- [`quality/037_mysterious_people_probability_scenarios.md`](quality/037_mysterious_people_probability_scenarios.md) defines the named scenarios required for AI and weighted-logic inspection.
- [`quality/037_mysterious_people_acceptance_criteria.md`](quality/037_mysterious_people_acceptance_criteria.md) defines implementation and validation gates.
- [`quality/037_mysterious_people_parent_improvement_review.md`](quality/037_mysterious_people_parent_improvement_review.md) records the final parent-led depth and anti-bloat review.
- [`quality/037_mysterious_people_source_reading_manifest.md`](quality/037_mysterious_people_source_reading_manifest.md) records the complete uploaded-source review.
- [`quality/037_mysterious_people_package_manifest.md`](quality/037_mysterious_people_package_manifest.md) records the final file inventory and checksums.
- [`diagrams/037_mysterious_people_system_flow.md`](diagrams/037_mysterious_people_system_flow.md) maps ownership and runtime flow.
- [`research/037_mysterious_people_research_boundary.md`](research/037_mysterious_people_research_boundary.md) defines the research boundary and explanation firewall.
- [`handoffs/037_mysterious_people_catalog_and_cluster_alignment.md`](handoffs/037_mysterious_people_catalog_and_cluster_alignment.md) replaces the obsolete catalog premise and records cluster disposition.
- [`handoffs/037_mysterious_people_subagent_routing.md`](handoffs/037_mysterious_people_subagent_routing.md) defines the recommended implementation and audit sequence.

## Prompt files

- [`prompts/037_mysterious_people_asset_prompt.md`](prompts/037_mysterious_people_asset_prompt.md)
- [`prompts/037_mysterious_people_achievement_prompt.md`](prompts/037_mysterious_people_achievement_prompt.md)
- [`prompts/037_mysterious_people_decision_mission_prompt.md`](prompts/037_mysterious_people_decision_mission_prompt.md)
- [`prompts/037_mysterious_people_population_ledger_and_adapters_prompt.md`](prompts/037_mysterious_people_population_ledger_and_adapters_prompt.md)
- [`prompts/037_mysterious_people_coding_prompt.md`](prompts/037_mysterious_people_coding_prompt.md)
- [`prompts/037_mysterious_people_goal_prompt.md`](prompts/037_mysterious_people_goal_prompt.md)

## Design boundaries

Event 037 is a global civilian-population anomaly. It creates real population, records the created cohort by state, and later converts that demographic gift into support pressure. It uses the existing Famine, Migration, Deaths, Camp and Repression, and Condemnation systems for consequences that those systems already own.

The player manages one public event value, **Overpopulation Pressure**. Detailed state provenance, support calculations, integration facts, Famine inputs, Migration receipts, and population-composition accounting remain internal.

The event uses ordinary events, an ordinary decision category, selected-state actions, shared map modes, and static visual assets. The design remains focused on the demographic loop and does not add unrelated presentation or country systems.

## Evidence boundary

The planning pack was created from the complete uploaded project bundle and the complete extracted subagent definitions. It is a design handoff. It does not claim repository implementation, HOI4 MCP evidence, offline wiki inspection, vanilla-file inspection, workbook editing, custom subagent execution, desktop testing, or in-game validation.
