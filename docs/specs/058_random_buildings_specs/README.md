# Event 58 Random Buildings specification package

This package contains the accepted planning handoff for Event 58, Random Buildings.

Extract the top-level `058_random_buildings_specs` folder into `docs/specs/`.

## Package map

- `PACKAGE_MANIFEST.md` records extraction, file sizes, line counts, hashes, and the goal-prompt length.
- `specs/058_random_buildings_spec_part_1_core.md` defines the event identity, global transaction, evolution stacking, player flow, cluster role, and Chaos treatment.
- `specs/058_random_buildings_spec_part_2_state_layers.md` defines the baseline and Evolution I state-building pools, weighting safeguards, provider ownership, and special-building initialization.
- `specs/058_random_buildings_spec_part_3_provincial_exceptional.md` defines Evolution II province packages and Evolution III exceptional construction.
- `specs/058_random_buildings_spec_part_4_integration_presentation_balance.md` defines reporting, event-log coverage, multiplayer behavior, system connections, future integration, tuning, and catalog alignment.
- `specs/058_random_buildings_spec_part_5_achievements.md` defines the achievement set and tracking intent.
- `quality/058_random_buildings_probability_scenarios.md` defines the weighted-selection scenarios that must be audited before and after implementation.
- `quality/058_random_buildings_acceptance_matrix.md` defines implementation and live-test acceptance cases.
- `quality/058_random_buildings_improvement_loop_closure.md` records the final depth and anti-bloat review.
- `research/058_random_buildings_source_audit.md` records the supplied sources, catalog discrepancy, and environment limitations.
- `prompts/` contains the asset, achievement, registry, probability, repository exploration, localisation, spreadsheet, completion-audit, improvement-loop, coding, and goal prompts.

## Source-of-truth decision

The user brief is the design authority for Event 58. The supplied event catalog export still assigns ID 58 to the older concept `The Industrial Complex`. That export is stale for this event and must not be blended with Random Buildings. Implementation must update the authoritative XLSX workbook and regenerate the CSV exports.

## Event scope

Random Buildings is a Minor Repeatable global event at Chaos level 1. It belongs to the Positive Economy cluster as a Medium-severity member. Every firing attempts a baseline state-level construction in every world state. Enabled evolutions add their own layers without replacing earlier layers.

The event owns selection, placement dispatch, transaction reporting, event-log coverage, achievement tracking, and its one report image. Every registered special building or facility keeps its original owner system, mechanics, assets, lifecycle, responsibility rules, and cleanup.

## Planning status

The specification is complete as a design package. It is not an implementation claim. Exact Clausewitz syntax, live registry identifiers, vanilla building database behavior, railway graph operations, supply-hub placement, facility APIs, and final weights remain implementation evidence gates because the live repository, offline Paradox wiki snapshot, installed vanilla files, and HOI4 MCP server were not mounted in this environment.
