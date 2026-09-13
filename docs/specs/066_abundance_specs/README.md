# Event 066 Abundance Specification Pack

## Catalog identity

- Event ID: `66`
- Event name: Abundance
- Event type: Minor Repeatable
- Minimum Chaos level: `1`
- Cluster: Sudden Abundance
- Logical cluster slots: Low, Medium, High
- Specification folder: `docs/specs/066_abundance_specs/`

## Accepted design

Every valid country receives four independently generated choices.
Each choice names one value at baseline, while later evolutions can combine two or three values.
The selected value or bundle becomes absurdly abundant through the owning system's safe abundance operation.
Helpful, harmful, strange, rare, country-specific, DLC-specific, and Chaos Redux values remain eligible when they are valid for that country.

The event core does not maintain a favored resource list.
It consumes an extensible provider registry in which each system publishes the semantic values it owns, the conditions under which each value is valid, how it is displayed, how excess is applied, and how AI evaluates it.
This is the practical meaning of full dynamic coverage in HOI4, whose script environment cannot be treated as a reflective database of every raw variable.

## Reading order

1. `specs/066_abundance_spec_part_1_core.md`
2. `specs/066_abundance_spec_part_2_dynamic_value_space.md`
3. `specs/066_abundance_spec_part_3_choice_generation.md`
4. `specs/066_abundance_spec_part_4_abundance_application.md`
5. `specs/066_abundance_spec_part_5_evolutions_and_cluster.md`
6. `specs/066_abundance_spec_part_6_global_flow_ai_multiplayer.md`
7. `specs/066_abundance_spec_part_7_presentation_logs_connections.md`
8. `specs/066_abundance_spec_part_8_achievements_assets.md`
9. `specs/066_abundance_spec_part_9_acceptance_criteria.md`

The `research/` folder contains provider coverage, catalog, and probability matrices.
The `prompts/` folder contains implementation handoffs.
The `quality/` folder records design decisions, source reading, tooling limits, and specialist-role review.

## Source conflict resolved by this pack

The supplied event catalog export still lists Event 66 as `CIC`, with a random-major international-market grant and no cluster assignment.
The user's Event 66 brief supersedes that old planning row.
The authoritative workbook was not supplied, so this pack records the required workbook changes without editing the export-only CSV files.

## Core non-negotiables

- Four choices are generated independently for each country.
- Candidate generation never scores whether a value helps the country.
- AI utility affects the AI's choice after generation, not the contents of its four cards.
- Every selected value is applied through its owner callback.
- Raw hidden implementation variables are not candidates unless their owner exposes a spoiler-safe semantic value.
- Pair and triple cards contain independently drawn values, with no authored packages or thematic combinations.
- Rolls are stored before display and cannot change through reopening, save loading, or tooltip refresh.
- Cluster duplicate slots coalesce into one Event 66 wave per cluster firing.
- The event creates one global pacing and history transaction per firing, not one transaction per recipient country.
- Event 66 uses the standard event interface with four dynamic option shells.

## Status

This package is a source specification and implementation handoff.
It does not claim that Event 66 has been implemented, tested in HOI4, added to the authoritative workbook, or validated through the HOI4 MCP tools.
