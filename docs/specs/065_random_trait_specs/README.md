# Event 065 Random Trait Specification Package

## Catalog identity

- Event ID: `65`
- Event name: `Random Trait`
- Event type: `Minor Repeatable`
- Catalog status at planning start: `To Be Reworked`
- Chaos level: `1`
- Cluster: `Randomizations`
- Member severity: `Medium`

## Purpose

This package defines the complete rework of Event 65 as a compact global randomization event.

The event has one clear action.

Every active country leader in the world gains a random country-leader trait, with the number of grants and the weight profile controlled by the highest active Evolution.

The design keeps the event simple for players and rigorous for implementation.

Its main implementation work lies in exhaustive trait discovery, generated pool maintenance, exact duplicate handling, deterministic multiplayer execution, event-log integration, probability validation, and clear reporting.

## Accepted design resolutions

1. The phrase **every trait available in Hearts of Iron IV and Chaos Redux** means every final loaded trait definition accepted by the country-leader trait system and usable by `add_country_leader_trait`.
2. The pool includes political traits, advisor traits, theorist traits, high-command traits, manufacturer traits, country-specific traits, DLC traits, unusual character traits, Chaos Redux traits, and other entries in the same engine database.
3. Unit-leader, operative, Military Industrial Organization, ship-designer, terrain, and other separate trait databases are not part of the country-leader trait pool.
4. No trait is removed because it is harmful, useless, contradictory, country-specific, ideology-specific, route-specific, strange, or likely to interact with another system.
5. The first proposal for every roll uses the complete stage-appropriate distribution.
6. A proposal matching a trait already owned by that leader, previously granted to that leader by Event 65, or selected earlier in the same firing is rejected and redrawn.
7. The gameplay mutation resolves in one authoritative hidden execution path before any player report opens.
8. Visible report events only present results and perform report cleanup.
9. The event uses the existing repeatable-event framework and does not add a separate timer.
10. The highest manifested enabled Evolution remains the event's persistent Evolution state.
11. The current repository snapshot leaves cluster ID `9` free.
12. The preferred cluster constant is therefore `event_cluster_id.randomizations = 9`, subject to a final collision check against the authoritative workbook and current source at implementation time.
13. Random Trait is an optional Randomizations member with Medium danger and a planned 60 percent participation value.
14. The event creates direct Chaos only when a new intensity first produces a successful global mutation.

## Package map

### Core specification

- `specs/065_random_trait_spec_part_1_core_loop_and_evolutions.md`
- `specs/065_random_trait_spec_part_2_trait_pool_and_rolls.md`
- `specs/065_random_trait_spec_part_3_runtime_presentation_and_integration.md`
- `specs/065_random_trait_spec_part_4_cluster_chaos_and_persistence.md`
- `specs/065_random_trait_spec_part_5_completion_contract.md`

### Implementation prompts

- `prompts/065_random_trait_asset_prompt.md`
- `prompts/065_random_trait_coding_prompt.md`
- `prompts/065_random_trait_trait_registry_generator_prompt.md`
- `prompts/065_random_trait_goal_prompt.md`
- `prompts/065_random_trait_repo_explorer_prompt.md`
- `prompts/065_random_trait_scripted_system_architect_prompt.md`
- `prompts/065_random_trait_probability_audit_prompt.md`
- `prompts/065_random_trait_localisation_audit_prompt.md`
- `prompts/065_random_trait_documentation_prompt.md`
- `prompts/065_random_trait_spreadsheet_alignment_prompt.md`
- `prompts/065_random_trait_completion_audit_prompt.md`
- `prompts/065_random_trait_improvement_loop_prompt.md`

### Research and handoffs

- `research/065_random_trait_current_repository_baseline.md`
- `research/065_random_trait_design_resolution_ledger.md`
- `handoffs/065_random_trait_trait_registry_schema.md`
- `handoffs/065_random_trait_implementation_surface_map.md`
- `handoffs/065_random_trait_catalog_alignment.md`
- `handoffs/065_random_trait_subagent_sequence.md`
- `diagrams/065_random_trait_runtime_flow.md`
- `diagrams/065_random_trait_roll_flow.md`

### Quality material

- `quality/065_random_trait_acceptance_matrix.md`
- `quality/065_random_trait_probability_scenario_matrix.md`
- `quality/065_random_trait_manual_design_review.md`
- `quality/065_random_trait_source_reading_manifest.md`
- `quality/065_random_trait_package_manifest.md`

## Reading and research status

Every project file supplied with this task was read in full.

The three CSV catalog exports were read in full.

The supplied subagent archive was extracted and all 20 subagent TOML files were read in full.

The current GitHub repository was inspected through the Event 65 script, localisation, repeatable-event registration, event-name mapping, event picture wiring, asset directory metadata, cluster constants, and related event-system patterns.

This was a targeted repository inspection.

It was not a line-by-line reading of the entire GitHub repository.

The exact source list and SHA-256 hashes are recorded in `quality/065_random_trait_source_reading_manifest.md`.

## Tooling limitation

The custom subagent tool registry was queried so the project subagents could be run.

That query failed with an MCP tunnel `404` response.

The live `chaosx_improvement_loop_planner`, `chaosx_ai_probability_auditor`, `chaosx_scripted_system_architect`, and other project subagents were therefore not executed.

Their complete role definitions were read and applied manually during planning.

Self-contained prompts are included so the required agents can be run later in the repository environment.

The package does not claim that live subagent audits or HOI4 MCP validation have already occurred.

## Extraction

The ZIP is rooted at `docs/`.

Extract it into the Chaos Redux repository root.

The accepted source specification will then appear under:

`docs/specs/065_random_trait_specs/`

The recorded subagent tooling blocker will appear under:

`docs/plans/065_random_trait_plans/blocked_reports/`
