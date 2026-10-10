# 069 Boxer Rebellion

## Delivery status

This is a proposed event specification package, not an implemented mod update.
The requirement to read every required source fully and use the named project subagents was not met.
In the original 2026-09-19 planning run, several supporting files remained partly read or unread, installed vanilla and Workshop sources were unavailable, and no named subagent or HOI4 MCP validation ran.
Discover current tools and local sources through [AGENTS.md](../../../AGENTS.md) and [the current subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).
The exact reading and execution record is in [Source review](research/source_review.md).

The full planning skill and several major project sources were read through the end.
The design preserves the supplied event concept and expands it into a local uprising, a foreign crisis, a possible intervention, and a continuing Chinese political game.
All new tuning values and route details are proposals awaiting implementation review and balance evidence.
The reviewed catalog snapshot records **To Be Reworked**.
Read the authoritative workbook during implementation before asserting current status.

## Package contents

The package contains 16 specification parts, 42 action families, 18 missions, 9 focus branch families, 3 political routes, all 3 requested evolutions, 12 achievement designs, 4 scenario types with 4 intensity profiles each, and 40 implementation acceptance fixtures.
It also contains 6 implementation or production prompts and one prepared specialist-handoff document.
The prompts are instructions for future work, not evidence that their tools or workers ran.

Only two persistent custom values are exposed: Boxer Strength and Intervention Pressure.
Existing Chinese countries retain their meaningful trees and identity.
A dedicated Boxer country must earn territorial institutions and a sustainable army.
Foreign participation follows actual interests and commitments, and intervention membership does not automatically replace existing factions.
Settlements have limited goals, finite obligations, and explicit withdrawal rules.
No Boxer-owned world-end branch is proposed.

## Reading order

Read Parts 1–4 for the main campaign structure.
Parts 5–7 define player actions, objectives, and evolutions.
Parts 8–10 cover the country, focus routes, and aftermath.
Parts 11–16 define balance expectations, shared integration, presentation, achievements, manual setup, and the implementation sequence.
Consult the source-review record before relying on an engine-dependent statement.

| Part | Subject |
| --- | --- |
| 01 | [Core design and catalog identity](069_boxer_rebellion_spec_part_1_core.md) |
| 02 | [Geography, participants, and state binding](069_boxer_rebellion_spec_part_2_geography_and_actors.md) |
| 03 | [Movement development and incidents](069_boxer_rebellion_spec_part_3_movement_and_incidents.md) |
| 04 | [Foreign interests and intervention](069_boxer_rebellion_spec_part_4_foreign_intervention.md) |
| 05 | [Decision catalog and cost contracts](069_boxer_rebellion_spec_part_5_decisions.md) |
| 06 | [Mission catalog and objective ownership](069_boxer_rebellion_spec_part_6_missions.md) |
| 07 | [All three evolutions](069_boxer_rebellion_spec_part_7_evolutions.md) |
| 08 | [Boxer country package](069_boxer_rebellion_spec_part_8_country_package.md) |
| 09 | [Focus-tree architecture and political routes](069_boxer_rebellion_spec_part_9_focus_tree.md) |
| 10 | [Victory, settlements, and aftermath](069_boxer_rebellion_spec_part_10_settlements.md) |
| 11 | [AI scenarios and balance targets](069_boxer_rebellion_spec_part_11_ai_and_balance.md) |
| 12 | [Shared systems and event integration](069_boxer_rebellion_spec_part_12_integrations.md) |
| 13 | [Presentation, asset requirements, and super-events](069_boxer_rebellion_spec_part_13_presentation_and_assets.md) |
| 14 | [Achievement requirements](069_boxer_rebellion_spec_part_14_achievements.md) |
| 15 | [Triggerable scenarios](069_boxer_rebellion_spec_part_15_triggerable_scenarios.md) |
| 16 | [Implementation sequence and acceptance fixtures](069_boxer_rebellion_spec_part_16_implementation_and_acceptance.md) |

## Ready prompts

The compact goal prompt is designed for a 3,500–4,000-character goal field.
The separate coding and specialist prompts contain more context.
Use the source package as the authority for the proposed content and preserve its unresolved-status notes when delegating.

| Prompt |
| --- |
| [Compact implementation goal](prompts/069_boxer_rebellion_goal_prompt.md) |
| [Main coding handoff](prompts/069_boxer_rebellion_coding_prompt.md) |
| [Decision and mission implementation](prompts/069_boxer_rebellion_decision_mission_prompt.md) |
| [Asset production handoff](prompts/069_boxer_rebellion_asset_prompt.md) |
| [Super-event research and production](prompts/069_boxer_rebellion_super_event_prompt.md) |
| [Achievement implementation](prompts/069_boxer_rebellion_achievement_prompt.md) |
| [Prepared specialist routing and handoff scopes](prompts/069_boxer_rebellion_subagent_handoffs.md) |

## Source and review documents

| Document | Purpose |
| --- | --- |
| [User brief](research/user_brief.md) | The supplied concept and required process |
| [Source review](research/source_review.md) | Full, partial, unread, and unavailable source coverage, plus actual tool execution |
| [Source locators](research/sources.json) | Repository paths, blob identities when returned, reference revision, and primary historical source |
| [Historical grounding](research/historical_grounding.md) | Narrow historical basis and its limits |
| [Design decisions](research/design_decisions.md) | User requirements versus proposed expansions |
| [Package checks](review/package_checks.md) | Checks actually performed on these files, distinct from future game tests |
| [Manifest](package_manifest.json) | File inventory and SHA-256 hashes |


Use `docs/plans/069_boxer_rebellion_plans/` for implementation handoffs and audit notes.

The runtime entry remains `chaosx.nr69.1`, while filenames use `069`.
The package includes no game scripts, runtime art, audio, catalog workbook changes, or repository commit.
Unresolved tag, state, character, treaty, local-effect, and source-dependent asset requirements must be resolved before those surfaces can be claimed complete.

## Repository reference

Repository: `klimPaskov/Chaos-Redux`.
Review reference commit: `879b3007d3b6bf75c726c11635473fccda45c569`.
Delivery date: 2026-09-19.
The early discovery calls used the default branch, and subsequent reads used the pinned reference where available.
Reconcile a newer checkout with this package before implementation.

## Reserved scenario identifier

The [shared identifier registry](../shared_identifier_registry.md) reserves one Boxer challenge entry as `SCN-029`, raw integer `29`.
Its four types and sixteen intensity profiles share that entry.
The reservation does not approve broader design or implement content.

## Changelog

### 2026-10-10 spec audit

- Action families fall from 46 to 42. Suppress, Tolerate, and Support became three stances of one D01 policy decision; narrowing and expanding a mandate became one D32 Revise the mandate decision; and reparation installments pay automatically on their due date instead of through a D40 button, with D41 moratorium kept for a payer who cannot pay. Each merged pair was the same choice split across several buttons, and a scheduled payment held no decision.
- The Boxer country records its origin with an event-owned flag instead of the shared special-country classification, because every special Chaos country is excluded from Famine and Migration by `humanitarian_country_is_valid`; the old instruction would have contradicted the package's own rule that the Boxer government keeps civilian consequences.
- The obsolete ZIP placement section is removed. Subagent instructions use the Claude-first wording.
