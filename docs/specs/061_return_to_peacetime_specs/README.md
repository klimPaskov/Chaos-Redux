# Event 061: Return to Peacetime

## Specification status

This directory is the source design package for Event 61, **Return to Peacetime**.

The event remains a **Minor Repeatable** event at **Chaos level 1** and a **High** member of the **Peace** cluster.

The package replaces the old catalog placeholder named `Half mils into civs` with a complete global demobilization and rearmament system.

## Design summary

Return to Peacetime forces ordinary countries to convert wartime institutions back toward civilian life.

Every firing applies the following baseline transaction to each valid country:

- one half of eligible military factories are converted into civilian factories
- one half of current War Support is removed and transferred into Stability
- the economy law moves one valid step toward Civilian Economy
- the conscription law moves one valid step toward Disarmed Nation
- mobilization released by the law change returns to civilian life through the ordinary manpower model
- a staged Industrial Reconversion Shock reduces military production during the transition

Each country receives a Return to Rearmament decision category.

The category uses one public value, **Rearmament Readiness**, and a physical state-level ledger for converted factories.

The ledger allows countries to reopen the same factories that were converted without creating free building levels. It remains attached to the state, follows ownership, supports repeat firings, and can be permanently abandoned by the current owner.

The three evolutions deepen the same transition:

1. **Swords into Ploughshares** dismantles a share of eligible surplus equipment for civilian reconstruction.
2. **The Great Demobilization** musters out a share of eligible standing divisions and returns their manpower and equipment.
3. **Permanent Peace** introduces Peacetime Economy and No Army, with forced adoption for countries that have not established a credible rearmament program.

The evolved effects are staggered through missions and scheduled reports. They do not all execute on the same game tick.

## Package map

### Package metadata

- `package_manifest.json`

### Source specifications

- `specs/061_return_to_peacetime_spec_part_1_core.md`
- `specs/061_return_to_peacetime_spec_part_2_rearmament.md`
- `specs/061_return_to_peacetime_spec_part_3_evolutions.md`
- `specs/061_return_to_peacetime_spec_part_4_ai_integration.md`
- `specs/061_return_to_peacetime_spec_part_5_balance_edge_cases.md`
- `specs/061_return_to_peacetime_spec_part_6_presentation_achievements.md`
- `specs/061_return_to_peacetime_spec_part_7_implementation_architecture.md`

### Research and probability plans

- `research/061_return_to_peacetime_historical_research.md`
- `research/061_return_to_peacetime_ai_probability_scenarios.md`

### Diagrams

- `diagrams/061_return_to_peacetime_lifecycle.md`
- `diagrams/061_return_to_peacetime_factory_ledger.md`

### Implementation prompts

- `prompts/061_return_to_peacetime_coding_prompt.md`
- `prompts/061_return_to_peacetime_decision_mission_prompt.md`
- `prompts/061_return_to_peacetime_asset_prompt.md`
- `prompts/061_return_to_peacetime_achievement_prompt.md`
- `prompts/061_return_to_peacetime_subagent_prompts.md`
- `prompts/061_return_to_peacetime_goal_prompt.md`

### Handoffs

- `handoffs/061_return_to_peacetime_catalog_alignment.md`
- `handoffs/061_return_to_peacetime_localisation_handoff.md`
- `handoffs/061_return_to_peacetime_asset_requirements.md`
- `handoffs/061_return_to_peacetime_engine_validation_gates.md`

### Quality and review

- `quality/061_return_to_peacetime_acceptance_matrix.md`
- `quality/061_return_to_peacetime_source_audit.md`
- `quality/061_return_to_peacetime_subagent_review_matrix.md`
- `quality/061_return_to_peacetime_source_of_truth_map.md`
- `quality/061_return_to_peacetime_risk_register.md`
- `quality/061_return_to_peacetime_source_read_inventory.csv`
- `quality/061_return_to_peacetime_package_validation.md`
- `quality/061_return_to_peacetime_package_file_manifest.csv`
- `../../plans/061_return_to_peacetime_plans/061_return_to_peacetime_manual_improvement_loop_closure.md`

## Source authority

The user brief is authoritative for the event name, ID, type, status, chaos level, cluster, baseline effects, decision-category premise, evolution names, and evolution thresholds.

The uploaded event and cluster CSV files are export snapshots. They contain stale Event 61 and Peace cluster rows. They are evidence of the records that must be replaced, not the design source for this rework.

The authoritative workbook must be edited during implementation. The CSV exports must then be regenerated through the repository exporter.

## Working labels

Names for internal decisions, missions, ideas, helper effects, variables, achievements, and asset files in this package are stable working labels unless the text explicitly states that a user-facing name is fixed.

The event name and evolution names supplied by the user are fixed.

The planning files provide writing direction and dynamic information requirements. They do not provide paste-ready final localisation.

## Completion boundary

This package is a design specification. It does not claim that gameplay script, final localisation, final art, probability evidence, workbook changes, or in-game validation already exist.

The implementation prompt requires all of those surfaces to be completed before the event can move from `To Be Reworked` to an implemented or testing status.
