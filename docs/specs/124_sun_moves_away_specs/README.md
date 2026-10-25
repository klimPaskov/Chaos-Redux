# Sun Moves Away: complete Event 124 planning package

This package expands the supplied brief into a complete design and implementation handoff for Event 124.
It contains eight specification parts, twenty response action families, fourteen incident families with six rare variants, six achievement proposals, three super-event research briefs, a manual setup family and fifty-nine planned acceptance cases.
The specifications preserve the entire-world darkness, all-hour night combat, indefinite duration, three evolutions, real surviving-creature interactions, strict Heat Wave exclusion and immediate Return cleanup required by the brief.

The planning work is complete.
Gameplay implementation and native engine validation have not been performed.
Two central implementation mechanisms remain unproven in the inspected sources: reversible whole-map darkness during ordinary daytime and normal native nighttime combat behavior at every hour.
The specifications retain both as required behavior, with explicit capability investigation and acceptance conditions.
They do not silently substitute a different presentation or combat effect.

## Read the design

| File | What it defines |
| --- | --- |
| [Part 1: Core](124_sun_moves_away_spec_part_1_core.md) | Global environmental changes, Sunlight Deprivation, two national values, initial service assessment, three priorities and ordinary lifecycle |
| [Part 2: Evolutions and Return](124_sun_moves_away_spec_part_2_evolutions_and_return.md) | Deep Freeze, regional predators, sustained refuges, evolved openings, positive Return hazard, immediate cleanup, recovery and manual setup |
| [Part 3: Incidents and countries](124_sun_moves_away_spec_part_3_incidents_and_countries.md) | Everyday consequences, rescue and attack branches, rare variants, notification limits and different country situations |
| [Part 4: Decisions and missions](124_sun_moves_away_spec_part_4_decisions_missions.md) | All twenty actions, dynamic material quotes, low-capacity options, service intervals, upkeep, mission outcomes and interruption rules |
| [Part 5: AI and balance](124_sun_moves_away_spec_part_5_ai_balance.md) | AI validity and priorities, representative country cases, exact arithmetic, full opening pools, Return probabilities and balance evidence |
| [Part 6: Integrations and Chaos](124_sun_moves_away_spec_part_6_integrations_and_chaos.md) | Heat Wave arbitration, food/death/migration ownership, living creature contracts, transaction safety, bounded processing and complete Chaos map |
| [Part 7: Presentation](124_sun_moves_away_spec_part_7_presentation.md) | Native panel, paused updates, state and cost information, asset inventory, narrative direction and three consequence-gated super-events |
| [Part 8: Achievements](124_sun_moves_away_spec_part_8_achievements.md) | Six exact success contracts, difficulty and visibility, frozen cohorts, abuse prevention and eighteen icon-state outputs |

## Design at a glance

Civilian Protection measures actual essential services for residents, constrained by the weakest local service.
Lifeline Reliability measures actual delivery through essential corridors.
These are the only two persistent national values created by this event.
The compact management window presents six primary action rows and at most three concurrent missions.

Distributed civilian relief, strategic continuity and concentrated refuge support direct real allocation choices.
Each can provide warmth, food access, rest, security and evacuation while carrying a different opportunity cost.
Existing wars and country identities remain consequential.
Paid work cannot purchase daylight or change the Return hazard.

| Active evolution | Required Chaos | New problem | Proposed Return median when highest active |
| --- | ---: | --- | ---: |
| Baseline | Ordinary event eligibility | Global cold, night combat and disrupted civilian routines | 240 days |
| Deep Freeze | 400+ | Severe heating and transport deficits, including deserts and tropics | 360 days |
| Things in the Darkness | 600+ | Organized regional attacks and stronger actual nocturnal survivors | 540 days |
| The Endless Night | 800+ | Sustained refuge operation consuming fuel, equipment and construction capacity | 810 days |

The medians are proposed probability-model targets, with no fixed expiry or maximum-duration cutoff.
Each evolution reduces the future Return hazard while preserving elapsed history.
Actual Return immediately removes temporary Sun effects and preserves casualties, damage, famine and displacement.

All player-facing wording is direction-only.
Final quotations, cultural references, music and assets require the later research and production handoffs.
Numeric balance values are proposed tuning, with the brief's thresholds and source-owned constraints identified separately.

## Use the implementation companions

| Companion | Purpose |
| --- | --- |
| [Subagent Usage Map](124_sun_moves_away_subagent_usage_map.md) | Canonical specialist names, ownership, sequence, required inputs, outputs, restrictions and parent review |
| [MCP Usage Map](124_sun_moves_away_mcp_usage_map.md) | Available-tool discovery, named checks, comparison evidence, retry boundaries and proof limits |
| [Acceptance matrix](124_sun_moves_away_acceptance_matrix.md) | Fifty-nine P0/P1 scenarios, all marked planned and unrun |
| [Research and sources](124_sun_moves_away_research_and_sources.md) | Full source-reading statement, pinned repository findings, contextual research, conflicts and unresolved capabilities |
| [Source coverage ledger](../../plans/124_sun_moves_away_plans/imported_review/124_sun_moves_away_source_coverage.csv) | All 152 unique supplied texts, complete reading coverage, hashes, reader assignments and 260 verified aliases |
| [Closed design review](../../plans/124_sun_moves_away_plans/imported_review/124_sun_moves_away_design_review.md) | Concrete review findings, corrections, accepted depth and remaining implementation obligations |

The complete supplied-source reading was shared across root and three generic readers before design and repository research.
It covered 3,213,650 source bytes, including current and older skills, catalogs, instructions, helper references and provided project-agent definitions.
Identical copies were verified through hashes, and every truncated initial source read was repaired.
The record distinguishes those complete supplied sources from targeted repository reads and unavailable installed game references.

## Final handoff prompts

The prompts were written after the specifications and bounded design review settled.
Start with the coding prompt for full implementation, or the goal prompt when a compact persistent task description is needed.
The other prompts are coordinated specialist assignments governed by the full specifications.

| Prompt | Assignment |
| --- | --- |
| [Coding](124_sun_moves_away_coding_prompt.md) | Complete integration, source authority, catalog identity confirmation, core capability gates, validation and closure |
| [Goal](124_sun_moves_away_goal_prompt.md) | Persistent completion objective, 3,984 characters including heading and final newline |
| [Assets](124_sun_moves_away_asset_prompt.md) | Complete consumer-specific visual production and evidence |
| [Super-events](124_sun_moves_away_super_event_prompt.md) | Final text and audio research, rights, unique IDs, consequence gates and current OGG wiring |
| [Achievements](124_sun_moves_away_achievement_prompt.md) | Six grant contracts, persistent proof, mode eligibility and icon triplets |
| [Decisions and missions](124_sun_moves_away_decision_mission_prompt.md) | All twenty paid responses, exact owner transactions, mission lifecycle, AI and cleanup |

## Placement and completion boundary

The original ZIP contained one top-level folder, `124_sun_moves_away_specs/`, and held 22 members.
The package is installed at `docs/specs/124_sun_moves_away_specs/`.
The historical source coverage CSV, package manifest and closed design review are in `docs/plans/124_sun_moves_away_plans/imported_review/`.
The import handoff is `docs/plans/124_sun_moves_away_plans/subagent_handoffs/import_review_2026-10-24.md`.
Implementation plans and handoffs belong under `docs/plans/124_sun_moves_away_plans/`.
The permanent event document will be created at closure under `docs/events/` with the catalog identity 124, and the parent decides its exact name at closure.
It is not present now, and the current shared-owner documentation remains authoritative for shared systems.

The package contains no repository mutation, workbook update, final asset production or game launch.
The parent's catalog, workbook, registry and index migration happens outside this package and is recorded in the import handoff.
Reading the provided worker definitions does not mean the named project workers ran.
The future maps preserve those roles without misrepresenting the generic readers used here.
Unavailable optional observations limit claims, while missing requested behavior remains an implementation gap.
124 is the catalog identity (former catalog ID 136); the exact mixed-family carrier and other owner capabilities require their documented implementation review.

The local packaging checks cover links, required files, action and achievement counts, numerical consistency, the goal length, source-ledger totals and archive integrity.
The manifest records the final packaged files and their SHA256 hashes.
The fifty-nine gameplay acceptance cases remain unrun until the appropriate future evidence exists.
