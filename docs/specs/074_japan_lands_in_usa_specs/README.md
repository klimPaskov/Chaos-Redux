# Event 074: Japan Lands in USA

A Japanese army suddenly establishes a real Pacific mainland front during an existing war with the United States.
California is preferred, Japan does not need to be winning, and the opening includes actual combat-ready formations and finite logistical preparation.
The war continues through normal fighting and peace rules.

**Plan-only package. No gameplay, assets, catalogue workbook or repository files were modified by this delivery.**

## Start here

Extract the ZIP into `docs/specs/` so that this folder becomes:

`docs/specs/074_japan_lands_in_usa_specs/`

Read the eight design parts in order, then use the coding prompt and its seven stage cards.
The separate goal prompt is ready to copy into a `/goal` workflow.
Implementation plans, specialist handoffs, test evidence and audits belong under:

`docs/plans/074_japan_lands_in_usa_plans/`

| Handoff | File |
| --- | --- |
| Main coding contract | [Coding prompt](prompts/074_japan_lands_in_usa_coding_prompt.md) |
| Compact goal | [Goal prompt](prompts/074_japan_lands_in_usa_goal_prompt.md) |
| Ordered implementation | [Stage 0](prompts/stages/00_read_and_prove_core.md), followed by stages 1 through 6 |
| Visual production | [Asset prompt](prompts/074_japan_lands_in_usa_asset_prompt.md) |
| Tier III presentation research | [Super-event prompt](prompts/074_japan_lands_in_usa_super_event_prompt.md) |
| Achievements | [Achievement prompt](prompts/074_japan_lands_in_usa_achievement_prompt.md) |
| Player operations | [Decision and mission prompt](prompts/074_japan_lands_in_usa_decision_mission_prompt.md) |
| Context-complete role instructions | [Specialist task cards](prompts/074_japan_lands_in_usa_specialist_tasks.md) |

## Design parts

1. [Event 074: Japan Lands in USA](design/074_japan_lands_in_usa_spec_part_1_core.md)
2. [Part 2: Landing geography and operational objectives](design/074_japan_lands_in_usa_spec_part_2_landing_and_objectives.md)
3. [Part 3: The army, stockpiles, and limited special support](design/074_japan_lands_in_usa_spec_part_3_army_and_logistics.md)
4. [Part 4: Japanese operations and American emergency defense](design/074_japan_lands_in_usa_spec_part_4_decisions_and_campaign.md)
5. [Part 5: Evolutions and the end of special support](design/074_japan_lands_in_usa_spec_part_5_evolutions_and_outcomes.md)
6. [Part 6: AI direction and shared systems](design/074_japan_lands_in_usa_spec_part_6_ai_and_shared_systems.md)
7. [Part 7: Presentation and asset direction](design/074_japan_lands_in_usa_spec_part_7_presentation_and_assets.md)
8. [Part 8: Achievements and replay value](design/074_japan_lands_in_usa_spec_part_8_achievements_and_replay.md)

## Main proposed tuning

| Tier | Chaos threshold | Immediate divisions | Lifetime division ceiling | Maximum special-support age |
| --- | ---: | ---: | ---: | ---: |
| Baseline | Below the next enabled threshold | 30 | 40 | 180 days |
| Pacific Army | 200 | 60 | 75 | 240 days |
| The Western Invasion | 400 | 100 | 125 | 300 days |
| Invasion of America | 600 | 150 | 180 | 360 days |

These are proposed balance anchors, not playtested results.
A frozen factor of 1.00 to 1.50 provides a bounded adjustment for very large American armies.
Part 3 defines its rounding and resource accounting.
Higher tiers can start directly or develop through the supplied delayed-evolution framework.
An active upgrade strengthens the existing expedition through retained access and does not create another surprise territorial seizure.

The package includes four Japanese action families, five paid American response families, five mission definitions, five compound achievements, one researched tier III super-event contract and 43 planned runtime images when all proposed consumers are used.
It uses ordinary decision categories, existing countries and ordinary unit families.
There is no new country, focus-tree replacement, separate resource wallet, unique 3D model or scripted peace.

## What was read and what remains unverified

**All 42 supplied text files were read in full, including all 20 supplied subagent definitions.**
Three additional repository files were read in full: the existing Event 074, the Portal Raider API document and the MTTH skill.
The supplied archive and text-file hashes are recorded in the [source manifest](reference/074_supplied_source_manifest.json).
The [reading register](reference/074_sources_and_reading_register.md) records the complete inventory, partial repository searches, limited primary research and external gaps.

**The requirement to fully read every externally referenced must-read file was not completed.**
The installed vanilla game, full relevant wiki articles, full shared implementation surfaces and native asset reference library still require reading in the implementation environment.
No executable subagent interface was available, so none of the 20 roles ran.
The required independent improvement and completion reviews remain pending.
No HOI4 MCP probability, map, technology, GUI or live-game test was run.
No art, audio or final player-facing localisation was produced.

The source specs were not shortened into a quick outline.
Final wording is intentionally supplied as direction, in accordance with the planning skill.
Unknown engine behavior is identified as a gate instead of filled with an invented effect or an untested claim.
The most important gates are safe defended-coast control changes, actual local supply under Pacific isolation, complete unit issue, legal air support, AI retention and exact native presentation consumers.

## Supporting contracts

| Reference | Purpose |
| --- | --- |
| [Capability and probability gates](reference/074_capability_and_probability_gates.md) | Map worksheet, transaction rules, country preservation and twelve named probability scenarios |
| [Requirements and routes](reference/074_requirements_and_route_coverage.md) | User requirement coverage and every planned campaign route |
| [Acceptance matrix](reference/074_acceptance_matrix.md) | Concrete static, runtime, save, multiplayer, AI, asset and achievement cases, all initially marked Not run |
| [Sources and reading register](reference/074_sources_and_reading_register.md) | Source authority, full/partial reading status and missing dependencies |

## Repository and catalog handoff

The inspected legacy event uses `chaosx.nr74.1`, transfers state 378 to Japan and creates twelve divisions.
The new design preserves the canonical root while replacing that ownership transfer and limited force behavior.
The source register gives the exact inspected file and blob identity.
Do not assume a historical map ID or the inspected default-branch file is unchanged in the implementation checkout.

The supplied CSVs are source snapshots.
The editable event catalog is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
Only after verified mechanics and final wording exist should the spreadsheet specialist update it and regenerate the CSV through `.tools/export_event_catalog_csv.py`.
The event remains **Minor Fire-Once, Chaos level 1, Wars Medium, To Be Reworked** until implementation evidence supports a status change.

## Delivery boundary

This is the complete authored planning handoff, with technical and research blockers stated openly.
It is not an implemented mod or a claim that the mandatory independent planning review has already passed.
Follow the stage cards, resolve the capability gates, obtain the required specialist findings and run the acceptance cases before calling the event complete.
The package intentionally excludes the supplied source archive, private configuration contents, temporary reading helpers and chat continuation prompts.
