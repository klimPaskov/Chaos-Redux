# Event 40: Lawrence of Arabia Specification Pack

## Status

This directory is the source design for Event 40.

- Event ID: `40`
- Type: Minor Fire-Once
- Minimum Chaos level: `1`
- Cluster: none
- Planning status: complete
- Implementation status: not implemented by this package
- Catalog status: keep To Be Reworked until implementation and validation

## Source review

All 22 supplied top-level project files and all 20 subagent definitions inside `subagents(4).zip` were read in full before this specification was written. See:

`quality/040_lawrence_of_arabia_source_read_manifest.md`

The available tool registry did not expose project-subagent spawning or HOI4 MCP actions. No subagent or MCP audit was run. Context-complete future handoffs are included under:

`docs/plans/040_lawrence_of_arabia_plans/subagent_handoffs/`

## Design decisions

The specification preserves the user's core idea and makes these critical corrections:

- Lawrence publicly died in 1935, so the 1936 event begins from concealed survival and British recall.
- Lawrence is one actor inside a network of local rulers, officers, political groups, routes, and British institutions.
- The event fires once in the random pool. Later country-to-country interventions are internal stages.
- The current exported catalog type of Minor Repeatable is stale.
- Lawrence's Influence is the only persistent public intervention value.
- Evolution I adds direct revolt capacity.
- Evolution II creates a regional British client system from real participants.
- Evolution III creates British Arabia, an Independent Arab Federation, or the rare Lawrence's Kingdom through a validated formation process.
- The permanent federation alone receives a dedicated country and focus package.

## Deliberate limits

These surfaces are intentionally absent because they would add maintenance without improving the event's core play:

- dedicated scripted GUI
- triggerable scenario
- custom 3D unit
- baseline animation
- full focus trees for every ordinary target
- world-end branch

These are design decisions, not shortcuts.

## File map

### Core specifications

1. `040_lawrence_of_arabia_spec_part_1_core.md`
   - identity, scope, historical premise, target registry, Influence, lifecycle, outcomes, character
2. `040_lawrence_of_arabia_spec_part_2_intervention_loop.md`
   - decisions, missions, costs, intelligence, AI, settlements, exploits
3. `040_lawrence_of_arabia_spec_part_3_evolutions.md`
   - active and pre-fire paths for all three evolutions
4. `040_lawrence_of_arabia_spec_part_4_federation_country_and_focus.md`
   - federation transaction, country package, Federal Authority, focus architecture
5. `040_lawrence_of_arabia_spec_part_5_connections_assets_achievements.md`
   - logs, cross-event bridges, UI, assets, super-events, achievements, documentation

### Research and diagrams

- `research/040_lawrence_of_arabia_historical_research.md`
- `diagrams/040_lawrence_of_arabia_route_maps.md`

### Quality contracts

- `quality/040_lawrence_of_arabia_acceptance_scenarios.md`
- `quality/040_lawrence_of_arabia_probability_scenarios.md`
- `quality/040_lawrence_of_arabia_improvement_loop_review.md`
- `quality/040_lawrence_of_arabia_source_read_manifest.md`

### Catalog

- `catalog/040_lawrence_of_arabia_catalog_alignment.md`

### Implementation prompts

- `prompts/040_lawrence_of_arabia_coding_prompt.md`
- `prompts/040_lawrence_of_arabia_goal_prompt.md`
- `prompts/040_lawrence_of_arabia_scripted_system_prompt.md`
- `prompts/040_lawrence_of_arabia_decision_mission_prompt.md`
- `prompts/040_lawrence_of_arabia_focus_tree_prompt.md`
- `prompts/040_lawrence_of_arabia_asset_prompt.md`
- `prompts/040_lawrence_of_arabia_super_event_prompt.md`
- `prompts/040_lawrence_of_arabia_achievement_prompt.md`
- `prompts/040_lawrence_of_arabia_localisation_prompt.md`
- `prompts/040_lawrence_of_arabia_probability_audit_prompt.md`
- `prompts/040_lawrence_of_arabia_catalog_spreadsheet_prompt.md`

## Source-of-truth order

When files appear to conflict, use this order:

1. current explicit user correction
2. accepted Event 40 specification files in this directory
3. repository rules and system skills
4. final implemented gameplay and validated evidence
5. permanent Event 40 documentation
6. authoritative catalog workbook
7. generated CSV exports
8. older rough prompts and catalog descriptions

## Implementation handoff

Begin with:

`prompts/040_lawrence_of_arabia_coding_prompt.md`

Use the shorter bounded goal prompt when a workflow requires one task objective:

`prompts/040_lawrence_of_arabia_goal_prompt.md`

## Completion rule

Planning completion does not imply gameplay completion. The event remains incomplete until the full implementation, assets, portrait, AI, federation package, super-events, achievements, localisation, documentation, workbook alignment, specialist audits, and named acceptance scenarios are complete.
