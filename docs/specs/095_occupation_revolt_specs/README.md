# Occupation revolt specification package

Event 095 | Minor Repeatable | Chaos 1 | Liberations | Medium

**Status: detailed full-concept gameplay draft and implementation handoff. External source and execution gates remain incomplete.**

The package expands the supplied Occupation revolt concept into 14 specification parts with 23,972 words of gameplay, lifecycle, presentation and implementation-facing requirements.
It preserves the real displaced country, a dynamic authentic homeland, resource-based armed restoration, surviving government and leaders, dormant claimant fallback, spread, support, defeat and later return.
All four user-supplied evolutions have both new-opening and active-revolt paths.
The original brief is retained unchanged as a separate source.

## Reading and execution status

All 46 supplied text files were fully read before drafting, including all 17 skills and all 20 subagent definitions.
The archive contains 26 top-level text files and a nested archive containing 20 agent definitions.
External transitive references were not all read, and the external MTTH file was read only through line 170.
The named source protocol was not located in the supplied archive or the scoped searches, so its unknown requirements are not claimed as fulfilled.
Actual isolated agents executed: **0**.
Actual HOI4 MCP, native game inspection, live tests and implementation runs: **0**.
Actual final art, localisation, quote/audio production and catalog edits: **0**.

Read the [source reading and execution report](095_occupation_revolt_source_reading_report.md) before treating any requirement as verified engine behavior.
The [parent consistency review](095_occupation_revolt_parent_consistency_review.md) records real author-side corrections, not an independent specialist pass.
The [package-integrity report](095_occupation_revolt_package_integrity_report.md) checks artifact structure only.

## Where this folder belongs

The ZIP has one top-level folder, `095_occupation_revolt_specs/`.
Extract that folder under `docs/specs/` in the intended repository.
This is documentation, not runtime mod code.
Do not install the archived source snapshot as active configuration or overwrite current skills from it.
Future actual specialist results belong under `docs/plans/095_occupation_revolt_plans/subagent_handoffs/`, as specified in each assignment.

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

These six prompts are complete handoffs, not evidence of production or execution.

| Prompt | Role |
|---|---|
| [Goal](095_occupation_revolt_goal_prompt.md) | Compact implementation goal, 3,998 characters including heading and final newline |
| [Coding](095_occupation_revolt_coding_prompt.md) | Full source, implementation, specialist, native capability and completion contract |
| [Decision Mission](095_occupation_revolt_decision_mission_prompt.md) | Exact actions, costs, missions, counterpart access and lifecycle |
| [Asset](095_occupation_revolt_asset_prompt.md) | Source-checked visual production and country-identity workflow |
| [Achievement](095_occupation_revolt_achievement_prompt.md) | Six demanding achievements, triplet assets and anti-farming proof |
| [Super Event](095_occupation_revolt_super_event_prompt.md) | One justified cascade moment, separate quote and licensed audio research |

## Supporting registers

| File | Purpose |
|---|---|
| [Source Decision Register](095_occupation_revolt_source_decision_register.md) | Separates original user requirements, accepted expansion and current-source facts |
| [Implementation Architecture](095_occupation_revolt_implementation_architecture.md) | Proposed current-source ownership, logical contracts and native proof gates |
| [Country Package Matrix](095_occupation_revolt_country_package_matrix.md) | Country activation fields and 11 claimant archetypes |
| [National Program Registry](095_occupation_revolt_national_program_registry.md) | 23 meaningful program variants and complete focus/decision payoff parity |
| [Requirement Coverage](095_occupation_revolt_requirement_coverage.md) | 36 original gameplay requirements mapped to specification files |
| [Validation Scenarios](095_occupation_revolt_validation_scenarios.md) | 97 planned runtime scenarios, all explicitly NOT_RUN |
| [Asset Coverage Matrix](095_occupation_revolt_asset_coverage_matrix.md) | 49 asset families and consumer-specific production requirements |
| [Skills Application Matrix](095_occupation_revolt_skills_application_matrix.md) | All 17 read skills and their direct or conditional application |
| [Specialist Execution Map](095_occupation_revolt_specialist_execution_map.md) | 20 prepared assignments, role boundaries and required review sequence |
| [Research Notes](095_occupation_revolt_research_notes.md) | Bounded primary-source historical inspiration with evidence limits |
| [Parent Consistency Review](095_occupation_revolt_parent_consistency_review.md) | Concrete design fixes and unresolved validation requirements |
| [Source Reading Report](095_occupation_revolt_source_reading_report.md) | Full supplied-source inventory, recovered reads, external gaps and actual execution status |

Machine-readable counterparts are included for requirement coverage, validation scenarios, asset coverage, specialist status and source inventory.
[Package manifest](095_occupation_revolt_package_manifest.json) records output hashes.
Run `python validate_package.py` to check package structure and unchanged manifest entries.
This validator does not execute HOI4, prove a source was understood or replace the required specialists.

## Preserved inputs

[Original user brief](095_occupation_revolt_original_user_brief.md) is the current design authority.
The supplied outer archive is preserved byte-for-byte in `source_snapshot/` for provenance.
Its SHA-256 is `0f13352a0bbf4c657fcb82ac6ec549a1ac208f2624b23489c25dc9bd85105d3e`.
The archived catalog CSVs remain untouched snapshots and do not override the current Liberations/Medium assignment.

## Completion boundary

The intended gameplay is specified rather than reduced to a short rough idea.
Exact native country activation, unit transfer, selective peace, focus preservation, shared API wiring and resource transactions still require current source and engine evidence.
Do not mark the event implemented or independently reviewed from the existence of these documents.
Resolve the external reading gaps, execute the actual specialist workflow and produce the missing runtime content before making that claim.
