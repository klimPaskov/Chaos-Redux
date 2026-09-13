# Event 043: Monsters from the Deep

## Package status

This folder is the planning source package for Chaos Redux Event 043, **Monsters from the Deep**.

The package replaces the old Event 043 **Massive Flood** concept. It defines the intended event design, country packages, unit families, focus-tree architecture, decisions, evolutions, pacts, terminal route, manual scenario, presentation, asset work, acceptance evidence, and implementation prompts.

This package does not claim that the event is implemented. It does not contain gameplay script, final localisation, final art, final audio, or live-engine proof.

## Accepted catalog identity

| Field | Value |
| --- | --- |
| Event ID | `43` |
| Event name | Monsters from the Deep |
| Replaces | Massive Flood |
| Type | Major |
| Status during planning | To Be Reworked |
| Chaos level | 3 |
| Cluster | None |
| Member severity | Not applicable |
| Evolution I | The Rising Tide |
| Evolution II | Every Sea Opens |
| Public world-end scenario | Cthulhu's Dominion |
| Manual scenario proposal | `SCN-015` Monsters from the Deep |

The cluster field is intentionally empty. The original brief contains an early `Alien Invasions` cluster label and a later direct statement that the event belongs to no cluster. The later event-specific rule controls this package because no `Alien Invasions` cluster exists in the supplied cluster catalog.

## Design summary

Event 043 opens several geographically separated coastal invasions at once. Each invasion creates one nonhuman country ruled by a named mythic sea creature. That creature is also represented by one unique apex division. The country cannot train ordinary units, recruit normal manpower, or replace a dead apex. Supporting seamonster formations arrive through conquest, feeding, lair development, pacts, focuses, and event milestones.

The ordinary invasion remains tied to salt water. A physical inland-depth registry gives coastal states depth `0`, then counts connected inland layers. Monster countries can operate only within the range their focus route has unlocked. Combat penalties grow with depth. Cthulhu's terminal unification removes almost all of this restriction.

The monster player tracks two persistent values:

1. **Hunger**, from `0` to `100`. High Hunger weakens control, increases pressure for destructive feeding, and can block expensive brood actions.
2. **Sea Bond**, from `0` to `100`. Sea Bond reflects access to ports, coastal territory, connected lairs, and the named apex's physical link to salt water.

Inland depth, reinforcement receipts, pact readiness, target scoring, regional coverage, and terminal readiness remain hidden calculations or qualitative tooltips. The event does not expose a ledger of internal numbers.

## Roster

The accepted roster contains sixteen full monster countries:

- Titanus Kraken
- Titanus Scylla
- Titanus Leviathan
- Titanus Cetus
- Titanus Hafgufa
- Titanus Jormungandr
- Titanus Iku-Turso
- Titanus Umibozu
- Titanus Akkorokamui
- Titanus Jiaolong
- Titanus Bakunawa
- Titanus Timingila
- Titanus Te Wheke
- Titanus Lusca
- Titanus Cipactli
- Titanus Ipupiara

No extra Pacific Northwest creature is added solely to fill geography. The current roster already places a full monster country in continental North America through Yucatán. Cultural review also found that treating Sisiutl as a generic hostile invader would flatten a living Kwakwaka'wakw supernatural tradition.

## Package map

### Sequential specification

1. [`specs/043_monsters_from_the_deep_spec_part_1_core.md`](specs/043_monsters_from_the_deep_spec_part_1_core.md)
2. [`specs/043_monsters_from_the_deep_spec_part_2_opening_and_geography.md`](specs/043_monsters_from_the_deep_spec_part_2_opening_and_geography.md)
3. [`specs/043_monsters_from_the_deep_spec_part_3_shared_mechanics.md`](specs/043_monsters_from_the_deep_spec_part_3_shared_mechanics.md)
4. [`specs/043_monsters_from_the_deep_spec_part_4_country_and_unit_packages.md`](specs/043_monsters_from_the_deep_spec_part_4_country_and_unit_packages.md)
5. [`specs/043_monsters_from_the_deep_spec_part_5_focus_trees.md`](specs/043_monsters_from_the_deep_spec_part_5_focus_trees.md)
6. [`specs/043_monsters_from_the_deep_spec_part_6_decisions_and_counterplay.md`](specs/043_monsters_from_the_deep_spec_part_6_decisions_and_counterplay.md)
7. [`specs/043_monsters_from_the_deep_spec_part_7_evolutions_pacts_and_terminal.md`](specs/043_monsters_from_the_deep_spec_part_7_evolutions_pacts_and_terminal.md)
8. [`specs/043_monsters_from_the_deep_spec_part_8_ai_scenarios_chaos_aftermath.md`](specs/043_monsters_from_the_deep_spec_part_8_ai_scenarios_chaos_aftermath.md)
9. [`specs/043_monsters_from_the_deep_spec_part_9_presentation_achievements_and_acceptance.md`](specs/043_monsters_from_the_deep_spec_part_9_presentation_achievements_and_acceptance.md)

### Matrices

- [`matrices/043_monster_country_package_matrix.md`](matrices/043_monster_country_package_matrix.md)
- [`matrices/043_focus_route_matrix.md`](matrices/043_focus_route_matrix.md)
- [`matrices/043_support_unit_matrix.md`](matrices/043_support_unit_matrix.md)
- [`matrices/043_ai_strategy_matrix.md`](matrices/043_ai_strategy_matrix.md)
- [`matrices/043_decision_mission_map.md`](matrices/043_decision_mission_map.md)
- [`matrices/043_chaos_impact_map.md`](matrices/043_chaos_impact_map.md)
- [`matrices/043_probability_scenario_matrix.md`](matrices/043_probability_scenario_matrix.md)
- [`matrices/043_asset_requirement_crosswalk.md`](matrices/043_asset_requirement_crosswalk.md)
- [`matrices/043_3d_model_brief_matrix.md`](matrices/043_3d_model_brief_matrix.md)
- [`matrices/043_acceptance_scenarios.md`](matrices/043_acceptance_scenarios.md)
- [`matrices/043_catalog_replacement.md`](matrices/043_catalog_replacement.md)
- [`matrices/043_legacy_replacement_map.md`](matrices/043_legacy_replacement_map.md)

### Diagrams

- [`diagrams/043_event_state_machine.md`](diagrams/043_event_state_machine.md)
- [`diagrams/043_focus_tree_lane_diagram.md`](diagrams/043_focus_tree_lane_diagram.md)
- [`diagrams/043_terminal_route_diagram.md`](diagrams/043_terminal_route_diagram.md)

### Research and source control

- [`research/043_research_notes_and_bibliography.md`](research/043_research_notes_and_bibliography.md)
- [`research/043_cultural_handling_notes.md`](research/043_cultural_handling_notes.md)
- [`research/043_source_review_log.md`](research/043_source_review_log.md)

### Implementation prompts

- [`prompts/043_monsters_from_the_deep_goal_prompt.md`](prompts/043_monsters_from_the_deep_goal_prompt.md) is the bounded implementation goal prompt.
- The remaining files in `prompts/` are context-complete assignments for the parent implementation agent and every relevant project specialist. They do not assume access to this conversation.

### Quality controls

- [`quality/043_design_limits_and_non_goals.md`](quality/043_design_limits_and_non_goals.md)
- [`quality/043_subagent_execution_status.md`](quality/043_subagent_execution_status.md)
- [`quality/043_completion_definition.md`](quality/043_completion_definition.md)
- [`quality/043_implementation_sequence.md`](quality/043_implementation_sequence.md)
- [`quality/043_package_manifest.md`](quality/043_package_manifest.md)

## Source precedence

Use this order when implementation sources conflict:

1. Explicit user corrections and accepted decisions written into this package.
2. The sequential specification files in this package.
3. The package matrices and diagrams.
4. Current repository source and current system documentation.
5. Older plans, exports, and implementation handoffs.
6. The old Event 043 flood files, which are replacement targets only.

The authoritative event catalog workbook remains the only editable catalog source. The CSV files reviewed during planning are export snapshots. Implementation must update the workbook and regenerate the exports.

## Hard implementation gates

Implementation must stop and report a blocker when any of these gates cannot be proven:

- unique collision-free three-character tags for all sixteen monster countries and the terminal country
- valid landing-state and inland-depth registries against the installed map
- a safe way to prevent voluntary deletion, conversion, duplication, or replacement of each apex division
- proper transfer and survival tracking for apex divisions during Cthulhu unification
- custom nonhuman unit models, substantive skeletal actions, sourced sound packages, and bespoke counters
- exact population loss through the shared Deaths transaction
- public world-end row and toggle integration
- full manual scenario registration and cleanup
- route-specific AI probability evidence
- focus-tree and event-chain MCP evidence
- final super-event quote, music, image, and audio rights evidence

No static unit, renamed counter, generic focus tree, copied portrait loop, placeholder audio, or ordinary manpower division may be accepted as a silent substitute.

## Planning completeness statement

No supplied source file was skipped or read only through a truncated preview. The source review log records the complete supplied set.

The named project subagents did not execute in this chat because the outer Codex bridge returned gateway errors. The prompt package preserves the required specialist work as explicit, context-complete tasks. The separate Windows repository, offline Paradox wiki snapshot, installed vanilla files, HOI4 MCP runtime, Meshy, Blender, and live game were unavailable in this environment. Their required checks remain implementation gates.

No intentional design truncation was used. Exact state IDs, final tag tokens, raw unit values, final localisation, quotes, audio choices, and engine-specific lock mechanisms remain open because deciding them without the required local evidence would be guesswork.
