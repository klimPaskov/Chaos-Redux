# Event 58 Random Buildings specification package

This package contains the source planning handoff for Event 58, Random Buildings.

The installed package is `docs/specs/058_random_buildings_specs/`.

## Design authority and current workflow

The package attributes its premise to the supplied user brief.
The original user message and claim-level acceptance record are not reproduced here, so approval of expanded mechanics remains unresolved until the implementation owner records the supporting user decision or parent acceptance.
Historical planning reviews, catalog snapshots, and package status labels do not establish approval or current implementation.
Use current [AGENTS.md](../../../AGENTS.md), [event guidance](../../../.claude/skills/chaos-redux-events/SKILL.md), [asset guidance](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [subagent guidance](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for execution.
The source design remains in the files listed below.

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

The specification is complete as a design package. It is not an implementation claim. Exact Clausewitz syntax, live registry identifiers, vanilla building database behavior, railway graph operations, supply-hub placement, facility APIs, and final weights remain implementation evidence gates because those references were unavailable in the original planning environment. Current routes and sources must be discovered again during implementation.

## Open questions

- `unresolved`: remove extermination camps from the Evolution I extreme band. Recommendation: remove them. Camp and genocide paths in Chaos Redux develop from a government's political decisions and camp construction, and a random worldwide construction result cannot respect those conditions even as an empty site. Concentration camps stay in the restricted band as dormant sites only.

## Changelog

### 2026-10-10 spec audit

- A randomly placed concentration camp always arrives as an empty, dormant site with no responsible actor; responsibility begins only if the controller puts it into use through the camp owner's decisions, and the controller can demolish it instead. This prevents the event from assigning atrocity responsibility to a government that never chose it and gives the result a real decision.
- Subagent instructions use the Claude-first wording.
