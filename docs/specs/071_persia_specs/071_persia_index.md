# 071 Persia: planning package

## Start here

This package expands the attached Persia brief into eighteen sequential specification parts. It is a planning handoff, not implemented mod content. New labels are working design labels. Final localisation, exact native focus coordinates, map IDs, and game assets are owned by the verified implementation workflow.

Keep future working plans and specialist reports in `docs/plans/071_persia_plans/`.

For implementation, read this index and the full design, then use the [coding prompt](071_persia_coding_prompt.md). The [goal prompt](071_persia_goal_prompt.md) is the compact `/goal` entry point. It points back to the complete handoff and is not a replacement for reading it.

## Design overview

Event 071 is Persia, a Minor Fire-Once event, Chaos level 1, in Formables as a Medium member. Root `chaosx.nr71.1` transforms the existing Iranian state into a restored empire without automatically replacing its government.

The opening delivers real troops, equipment, aircraft, reserves, and logistics. Proposed minimum formation counts are 20, 35, 55, and 80 across the baseline and three evolutions, before campaign scaling. Guard formations are smaller, bounded formations, so division count alone is not a measure of total strength. Part 9 owns the composition, manpower, capacity, equipment, and placement contract.

The three routes develop different institutions: an Achaemenid charter network, a Sasanian command system, and a modern industrial bloc. Shared development supports actual replacement production, railways, army training, air power, Gulf access, a navy, and the Immortals. Legitimacy is the main meter. Guard capacity is the second public custom numerical reading. The tree owns at most three staged national spirit slots.

The full Persepolis project, territorial settlements, specialized satrapies, guarantees, command disputes, contract failures, fragmentation, and recovery create the longer campaign. Evolution thresholds are 200, 400, and 600. Later evolution unlocks never repeat the opening army.

## Sequential specifications

| Part | Subject |
|---|---|
| 01 | [Core specification](071_persia_spec_part_1_core.md) |
| 02 | [Government, identity, and legitimacy](071_persia_spec_part_2_identity_and_legitimacy.md) |
| 03 | [Territorial restoration and wars](071_persia_spec_part_3_territories_and_wars.md) |
| 04 | [Focus-tree architecture](071_persia_spec_part_4_focus_architecture.md) |
| 05 | [The Achaemenid Legacy](071_persia_spec_part_5_achaemenid_legacy.md) |
| 06 | [The Sasanian Restoration](071_persia_spec_part_6_sasanian_restoration.md) |
| 07 | [The New Persian Empire](071_persia_spec_part_7_new_persian_empire.md) |
| 08 | [Shared development branches](071_persia_spec_part_8_shared_development.md) |
| 09 | [Opening army and the Immortals](071_persia_spec_part_9_opening_army_and_immortals.md) |
| 10 | [Satrapies and imperial diplomacy](071_persia_spec_part_10_satrapies_and_imperial_diplomacy.md) |
| 11 | [Imperial centers and the Persian Gulf](071_persia_spec_part_11_capitals_and_gulf.md) |
| 12 | [Evolutions, crises, and collapse](071_persia_spec_part_12_evolutions_and_collapse.md) |
| 13 | [Decisions and missions](071_persia_spec_part_13_decisions_and_missions.md) |
| 14 | [Interface and information design](071_persia_spec_part_14_interface.md) |
| 15 | [AI and balance review](071_persia_spec_part_15_ai_and_balance.md) |
| 16 | [Presentation, visual assets, and 3D brief](071_persia_spec_part_16_presentation_and_assets.md) |
| 17 | [Achievement design](071_persia_spec_part_17_achievements.md) |
| 18 | [Integration and acceptance contracts](071_persia_spec_part_18_integration_and_acceptance.md) |

## Required prompt files

| Prompt | Purpose |
|---|---|
| [Coding](071_persia_coding_prompt.md) | Full implementation contract and evidence gates |
| [Assets](071_persia_asset_prompt.md) | Identity, icons, art, portraits, GUI assets, guard models, audio routing, and conversion |
| [Super-events](071_persia_super_event_prompt.md) | Separate text and audio research, source checks, presentation, and wiring |
| [Achievements](071_persia_achievement_prompt.md) | All eight achievements, tracking, difficulty, tests, and icon triplets |
| [Decisions and missions](071_persia_decision_mission_prompt.md) | Costs, transactions, targets, staged guard recruitment, missions, and persistence |
| [Goal](071_persia_goal_prompt.md) | Compact ready-to-use `/goal` instruction |

## Diagrams

The overview and three route sketches are kept as editable Graphviz DOT sources with rendered SVGs.

[Overview SVG](071_persia_focus_overview.svg) | [Achaemenid SVG](071_persia_achaemenid_route.svg) | [Sasanian SVG](071_persia_sasanian_route.svg) | [Modern SVG](071_persia_modern_route.svg)

The diagrams are branch sketches, not exact engine prerequisites or native game renders. The relevant specification defines alternatives, cumulative requirements, route locks, and conditional failure. Shared systems remain available even where a route sketch omits them to stay readable.

## Review and source companions

[Country-package matrix](071_persia_country_package_matrix.md) defines identity and transition boundaries. [Research notes](071_persia_research_notes.md) separate historical support from authored game design. [Source-reading receipt](071_persia_source_reading_receipt.md) and [source manifest](071_persia_source_manifest.json) record all supplied texts and unavailable dependencies. The [original user brief](071_persia_original_user_brief.md) is preserved unchanged for comparison.

[Subagent handoffs](071_persia_subagent_handoffs.md) cover all twenty supplied roles. These are future prompts, not agent reports. [Parent review](071_persia_parent_review.md) records the design checks, corrected issues, and outstanding evidence gates. [Package validation](071_persia_package_validation.json) records automated file-level checks. [Package manifest](071_persia_package_manifest.json) records the current files and hashes.

## Original planning record

Availability and passed-check claims in the source receipts, parent review and package validation describe the 2026-09-20 authoring run.
They do not certify the current checkout.
Use [AGENTS.md](../../../AGENTS.md) and [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for current workflow and capability discovery.
The original brief supplies user requirements, while expansion and tuning require attributable adoption before implementation.

## What was and was not done during authoring

All 42 supplied project texts and the attached brief were read. The archive did not include the actual script checkout, mandatory offline wiki, installed vanilla or DLC files, exact map, canonical asset references, or authoritative workbook. No actual subagent runner or HOI4 MCP validation was available in this session.

The design, handoff prompts, source records, and planning diagrams are delivered. Exact state mapping, installed-tree carryover, final characters, engine support, final assets and localisation, independent subagent reviews, and runtime validation remain explicit implementation gates. The CSV snapshots and catalog status were not changed.

## Changelog

### 2026-10-10 spec audit

- The four PNG renders and the HTML diagram viewer are removed; the DOT sources and SVG renders hold the same diagrams. The PNGs duplicated the SVGs as Git LFS objects, and LFS is reserved for assets visible in game.
- Event-owned Chaos is rescaled to the Chaos Meter: the root shock is +5, +7, +9, or +12 by tier (was +10 to +25), later milestones +2 to +5, and reversals -3. A restoration with a strong army is a regional shock, while the wars and annexations it leads to already pay through shared sources.
- The obsolete extraction instruction is removed. Subagent instructions use the Claude-first wording; the historical package-validation record is unchanged.
- The design itself was already disciplined (one meter plus guard capacity, qualitative satrapy states, a shared completion rule for map, focuses, and achievements) and is otherwise unchanged.
