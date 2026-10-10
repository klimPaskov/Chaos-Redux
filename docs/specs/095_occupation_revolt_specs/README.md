# Occupation revolt specification package

Event 095 | Minor Repeatable | Chaos 1 | Liberations | Medium

**Status: detailed gameplay specification and implementation handoff, planned 5 October 2026 and audited 10 October 2026. Not implemented.**

The package expands the user's Occupation revolt brief into 14 specification parts.
It preserves the real displaced country, a dynamic authentic homeland, resource-based armed restoration, surviving government and leaders, dormant claimant fallback, spread, support, defeat and later return.
All four user-supplied evolutions have both new-opening and active-revolt paths.
The original brief is retained unchanged as a separate source.

The 5 October 2026 planning pass read the 46 supplied text files but not every transitive installed reference, and launched no specialists; the [source reading report](095_occupation_revolt_source_reading_report.md) lists the gaps.
Implementation plans and specialist handoffs belong under `docs/plans/095_occupation_revolt_plans/`.

## Specification index

| Part | Subject |
|---|---|
| 01 | [a country returns from occupation](095_occupation_revolt_spec_part_01_core.md) |
| 02 | [claimants and the homeland](095_occupation_revolt_spec_part_02_claimants_and_homelands.md) |
| 03 | [the underground before the front](095_occupation_revolt_spec_part_03_underground_and_preparation.md) |
| 04 | [the opening army and the first campaign](095_occupation_revolt_spec_part_04_forces_and_opening.md) |
| 05 | [who governs the restored country](095_occupation_revolt_spec_part_05_government_and_country_package.md) |
| 06 | [spread and the occupier's response](095_occupation_revolt_spec_part_06_spread_and_occupation_response.md) |
| 07 | [foreign assistance and the restoration settlement](095_occupation_revolt_spec_part_07_foreign_support_and_settlements.md) |
| 08 | [the four evolutions](095_occupation_revolt_spec_part_08_evolutions.md) |
| 09 | [national development after the opening](095_occupation_revolt_spec_part_09_focus_paths.md) |
| 10 | [decisions, missions and political programs](095_occupation_revolt_spec_part_10_decisions_and_missions.md) |
| 11 | [connections to the wider mod](095_occupation_revolt_spec_part_11_connections_and_consequences.md) |
| 12 | [AI behavior and balance](095_occupation_revolt_spec_part_12_ai_and_balance.md) |
| 13 | [presentation, assets and achievements](095_occupation_revolt_spec_part_13_presentation_and_achievements.md) |
| 14 | [lifecycle, invariants and acceptance](095_occupation_revolt_spec_part_14_lifecycle_and_acceptance.md) |

## Production and implementation prompts

| Prompt | Role |
|---|---|
| [Goal](095_occupation_revolt_goal_prompt.md) | Compact implementation goal, bounded to 4,000 characters including heading and final newline |
| [Coding](095_occupation_revolt_coding_prompt.md) | Full source, implementation, specialist, native capability and completion contract |
| [Decision Mission](095_occupation_revolt_decision_mission_prompt.md) | Exact actions, costs, missions, counterpart access and lifecycle |
| [Asset](095_occupation_revolt_asset_prompt.md) | Source-checked visual production and country-identity workflow |
| [Achievement](095_occupation_revolt_achievement_prompt.md) | Six demanding achievements, triplet assets and anti-farming proof |
| [Super Event](095_occupation_revolt_super_event_prompt.md) | One justified cascade moment, separate quote and licensed audio research |

## Supporting registers

| File | Purpose |
|---|---|
| [Source Decision Register](095_occupation_revolt_source_decision_register.md) | Separates original user requirements, authored expansions and historical source observations |
| [Implementation Architecture](095_occupation_revolt_implementation_architecture.md) | Proposed current-source ownership, logical contracts and native proof gates |
| [Country Package Matrix](095_occupation_revolt_country_package_matrix.md) | Country activation fields and 11 claimant archetypes |
| [National Program Registry](095_occupation_revolt_national_program_registry.md) | 23 program variants and focus/decision payoff parity |
| [Requirement Coverage](095_occupation_revolt_requirement_coverage.md) | 36 original gameplay requirements mapped to specification files |
| [Validation Scenarios](095_occupation_revolt_validation_scenarios.md) | 101 acceptance scenarios for implementation review and the user's live tests |
| [Asset Coverage Matrix](095_occupation_revolt_asset_coverage_matrix.md) | 49 asset families and consumer-specific production requirements |
| [Specialist Execution Map](095_occupation_revolt_specialist_execution_map.md) | Which specialist roles apply, when, and their Event 095 checks |
| [Research Notes](095_occupation_revolt_research_notes.md) | Bounded primary-source historical inspiration with evidence limits |
| [Source Reading Report](095_occupation_revolt_source_reading_report.md) | Historical supplied-source inventory, external gaps and execution status of the planning pass |

Machine-readable counterparts are included for requirement coverage, validation scenarios, asset coverage and the source inventory.
The [package manifest](095_occupation_revolt_package_manifest.json) records current local documentation membership and hashes.

## Preserved inputs

[Original user brief](095_occupation_revolt_original_user_brief.md) is the current design authority.
The supplied outer archive was removed at the user's request in commit `6a2ebc838`; its historical SHA-256 is `0f13352a0bbf4c657fcb82ac6ec549a1ac208f2624b23489c25dc9bd85105d3e`.
The archived catalog CSVs remain untouched snapshots and do not override the current Liberations/Medium assignment.

## Open questions

- **Super-event presentation slot.** The [shared identifier registry](../shared_identifier_registry.md) reserves no `super_event_visible` slot for the regional occupation-collapse presentation in Part 13; orchestrator decision, 10 October 2026: reserve it when Event 095 is implemented.
- **Owner predicates.** The grievance-state reads and the liberation predicate for migration's hostile-capture adapter (Part 11) were accepted as owner seams by the orchestrator on 10 October 2026; the famine, migration and camp owners publish the triggers when Event 095 is implemented, and until then the connections stay specified but unwired.
- **Catalog row.** The catalog still carries the older exile-only description and a blank cluster; the Liberations Medium membership and four evolution names wait for the workbook workflow.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Merged Organize Base and Prepare Region into one Organize Region action used before and after the opening (Parts 03, 06, 09, 10).
- Removed the event's own Restore Services, Humanitarian Access and Civilian Return decisions; relief, evacuation, reception and return use the famine and migration actions, so Event 095 has 21 operations instead of 25 and no humanitarian duplicates (Parts 07, 10).
- Defined grievance states from famine, requisition, concealment, camp and violent-border facts: one band of breakaway assessment, removed by real relief, giving the occupier a feed-or-squeeze choice (Parts 06, 11, 12).
- A claimant's capture of its own home state requests no war flight, the occupier's recapture does, and settlement returns use Help Families Return; sanction participants against a condemned occupier are natural sponsors (Parts 11, 12, 14).
- Readiness and Cohesion tooltips show the value, next threshold and at most three causes (Part 01).
- Added validation scenarios V098-V101 and renamed the recovery decision icon to reconstruction.
- Replaced the twenty per-role assignment files and their status JSON with a single specialist execution map table that keeps each role's Event 095 checks; deleted the skills application matrix, parent consistency review, package-integrity report and results, and the archive-dependent `validate_package.py`, which were historical process evidence with no remaining consumer; regenerated the package manifest.
- Replaced `AGENTS.md`, `collaboration.spawn_agent` and `fork_turns` instructions in the prompts with `CLAUDE.md`, `.claude/skills/` and `chaos-redux-subagents` routing; agents no longer run live tests, and mandatory-tool gates follow the repository retry rules; the goal prompt is 3,868 characters.
