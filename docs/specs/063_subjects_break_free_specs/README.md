# Event 063: Subjects Break Free

This folder is the source specification package for Chaos Redux Event 063.

## Catalog identity

- Event ID: `63`
- Event name: Subjects Break Free
- Event slug: `subjects_break_free`
- Type: Minor Repeatable
- Status during planning: To Be Reworked
- Chaos level: 1
- Primary cluster: Liberations
- Primary cluster role: Medium member
- Secondary cluster classification: Domestic Unrest
- Secondary cluster role: Medium member

## Design summary

Several existing subject countries become independent during one firing. The event changes their diplomatic status in place, preserving the countries that already exist in the campaign. The size of the release batch scales with the current valid subject pool. Separations can be negotiated, recognized after a unilateral declaration, contested without immediate war, or resisted through an independence war.

Countries freed through this event can cooperate with countries created through Independence Wave and compatible successors from Soviet Collapse. The shared connection records liberation origin without moving release ownership into a common system. At high Chaos, the network can hold a congress and form a Liberation Pact with collective defense, support for later breakaways, and one visible public value called Liberation Cohesion.

## Package map

### Specifications

1. `specs/063_subjects_break_free_spec_part_1_core.md`
2. `specs/063_subjects_break_free_spec_part_2_settlements.md`
3. `specs/063_subjects_break_free_spec_part_3_network_and_pact.md`
4. `specs/063_subjects_break_free_spec_part_4_evolutions_clusters_and_connections.md`
5. `specs/063_subjects_break_free_spec_part_5_decisions_missions_and_ai.md`
6. `specs/063_subjects_break_free_spec_part_6_presentation_assets_achievements_and_acceptance.md`

### Handoff prompts

- `prompts/063_subjects_break_free_asset_prompt.md`
- `prompts/063_subjects_break_free_achievement_prompt.md`
- `prompts/063_subjects_break_free_decision_mission_prompt.md`
- `prompts/063_subjects_break_free_shared_system_prompt.md`
- `prompts/063_subjects_break_free_coding_prompt.md`
- `prompts/063_subjects_break_free_goal_prompt.md`

### Research and quality material

- `research/063_subjects_break_free_research_notes.md`
- `research/063_subjects_break_free_source_inventory.md`
- `diagrams/063_subjects_break_free_flow.md`
- `quality/063_subjects_break_free_probability_scenarios.md`
- `quality/063_subjects_break_free_role_reviews.md`
- `quality/063_subjects_break_free_acceptance_matrix.md`
- `handoffs/063_subjects_break_free_catalog_handoff.md`

## Reading order

Read the six numbered specification files first. The diagrams and quality files explain the transaction flow and the expected probability ordering. Use the specialized prompt files only after the design files have been read.

## Source boundary

Event 063 releases countries that already exist as subjects. It does not create replacement tags, redraw their territory, replace their governments, or assume ownership of Independence Wave country packages. Event 144, Freedom or Death, remains a separate future concept for a mass declaration and National Liberation Front crisis.

## Planning status

The package contains the complete accepted design handoff. Final player-facing localisation remains an implementation task guided by the tone and information rules in the specification. Working labels in this package identify systems and assets. They are not final in-game text.
