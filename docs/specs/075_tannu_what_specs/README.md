# Event 075 · Tannu What?

## Package

**Main file:** `075_tannu_what_planning_package.zip`  
**Top-level folder:** `075_tannu_what_specs/`  
**Intended location:** `docs/specs/075_tannu_what_specs/`  
**Catalog:** Minor Fire-Once, To Be Reworked, Chaos level 1, Diplomacy Low.

Extract the main ZIP into `docs/specs/`.
This package contains the full source design, focus-path sketches, source research, 16 probability-evaluation scenarios, 72 implementation acceptance scenarios, six planned achievements and six separate production or implementation prompts.
The meaningful subfolders separate aid, focus-tree paths, campaign systems, decisions, presentation and playtesting.

TAN builds a military from worldwide defensive aid, breaks protection during its sudden all-neighbor reveal, then expands across actual borders.
An earned continent and a valid 1000-Chaos world-end start open the final overseas campaign.
The paid force depends on real completed assistance and preparation.
No timer grants the missing army when sponsors refuse.

## Read the full source design

The specification is path-based design, not final HOI4 syntax or an exact laid-out focus-node graph.
The implementation owner creates the complete final node layout and supporting code from these paths.
User-provided focus anchors are retained.
Other titles, copy, numerical tuning and achievement IDs are proposed directions until their required review and collision checks.

| Part | Source file |
|---|---|
| 1 | [Tannu What?](075_tannu_what_spec_part_1_core.md) |
| 2 | [Protection and the worldwide appeals](aid/075_tannu_what_spec_part_2_diplomacy.md) |
| 3 | [Aid packages and ownership](aid/075_tannu_what_spec_part_3_aid_packages.md) |
| 4 | [Turning aid into lasting strength](aid/075_tannu_what_spec_part_4_industry_and_mobilization.md) |
| 5 | [Focus-tree architecture](focus_tree/075_tannu_what_spec_part_5_architecture.md) |
| 6 | [Buildup and political paths](focus_tree/075_tannu_what_spec_part_6_buildup_paths.md) |
| 7 | [The defensive military program](focus_tree/075_tannu_what_spec_part_7_military_paths.md) |
| 8 | [Conquest and the Tuvan state](focus_tree/075_tannu_what_spec_part_8_conquest_paths.md) |
| 9 | [The final global focus family](focus_tree/075_tannu_what_spec_part_9_world_campaign_paths.md) |
| 10 | [The reveal and outward wars](campaign/075_tannu_what_spec_part_10_reveal_and_wars.md) |
| 11 | [Evolutions](campaign/075_tannu_what_spec_part_11_evolutions.md) |
| 12 | [Continental victory and the world-end campaign](campaign/075_tannu_what_spec_part_12_continental_and_world_end.md) |
| 13 | [Donor reactions, resistance, and defeat](campaign/075_tannu_what_spec_part_13_donors_and_containment.md) |
| 14 | [Country identity, institutions, and forces](campaign/075_tannu_what_spec_part_14_country_identity_and_forces.md) |
| 15 | [Chaos consequences and cross-event connections](campaign/075_tannu_what_spec_part_15_chaos_and_connections.md) |
| 16 | [Decisions and missions](decisions/075_tannu_what_spec_part_16_actions_and_missions.md) |
| 17 | [Interface and localisation direction](presentation/075_tannu_what_spec_part_17_interface_and_localisation.md) |
| 18 | [Visual assets and the two super-events](presentation/075_tannu_what_spec_part_18_assets_and_super_events.md) |
| 19 | [Achievement design](presentation/075_tannu_what_spec_part_19_achievements.md) |
| 20 | [AI behavior and balance intent](playtesting/075_tannu_what_spec_part_20_ai_and_balance.md) |
| 21 | [Play scenarios and acceptance](playtesting/075_tannu_what_spec_part_21_play_scenarios.md) |

[Research notes and source boundaries](075_tannu_what_research_notes.md) distinguish the user brief, supplied project rules, bounded repository inspection, external context and unresolved production research.

## Separate prompts

| Handoff | File |
|---|---|
| Whole implementation | [Coding prompt](075_tannu_what_coding_prompt.md) |
| Compact implementation goal | [Goal prompt](075_tannu_what_goal_prompt.md) |
| Visual production | [Asset prompt](075_tannu_what_asset_prompt.md) |
| Two super-events | [Super-event prompt](075_tannu_what_super_event_prompt.md) |
| All six achievements | [Achievement prompt](075_tannu_what_achievement_prompt.md) |
| Decisions and missions | [Decision and mission prompt](075_tannu_what_decision_mission_prompt.md) |

The goal prompt is constrained to 3500-4000 characters including its heading and final newline.
It points to the complete source package and does not replace its reading requirement.

## Important added design choices

The expansion requires an existing functioning independent TAN and preserves its present ideology, ruler and tag.
The opening reveal ends protective faction membership so that former protectors on the border are included in the first wars.
It explicitly proposes releasing a pre-existing adjacent TAN subject before that universal opening and warning the player in advance.
Later genuine allies and loyal subjects remain exempt from the recurring non-allied-neighbor rule.

Paid reserve custody, physical delivery, funded dense industrial capacity, three sponsorship institutions, one public Readiness summary, donor audits, quantified continental certification, bounded additional Chaos and six achievement challenges are added design choices.
They are not attributed to the original brief as if every detail were supplied there.
Numerical targets are provisional and have not been balanced through the required tools.

## Read coverage and limits

All 43 supplied text files were read in full before drafting: 22 outer archive text files, 20 nested role TOMLs and the user brief.
The nested ZIP was extracted.
Not every linked external dependency was supplied or inspected.
The missing set includes the MTTH skill, local offline wiki, installed vanilla and consumer files, companion templates, the authoritative workbook, complete current repository implementation and CXT companion documentation.

The only fully fetched implementation file was the existing root event at commit `879b3007d3b6bf75c726c11635473fccda45c569`.
No current-HEAD claim, repository modification, workbook edit, art generation, final audio selection or live game test was made.
No agent-spawning tool was available, so none of the 20 supplied roles ran independently.
The mandatory probability and near-completion improvement-loop reviews remain unrun.

## Critical production gates

Before production completion, prove actual transfer coverage, equipment variants, paid reserve deployment, foreign-force recall, dense-industry output, opening-war legality, provenance and achievement predicates in the installed game.
Obtain current technology, event, focus, decision, interface and probability evidence.
Resolve final source-checked super-event text and item-level audio rights, then produce and inspect every native asset consumer.
Review user-owned live evidence for the runtime cases.
A coherent source file or local arithmetic check is not a substitute for these results.

The separate `075_tannu_what_review_handoff.zip` contains the source manifest, added-choice map, unresolved-capability review, 20 prepared UNRUN role handoffs and local package-check evidence under `075_tannu_what_plans/`.
It is intended for `docs/plans/`.
The main source package already states every essential design and production gate and can be read without that supplementary review archive.

## Catalog update

The supplied event CSV still uses the old faction-entry name and details, and its Diplomacy cluster export does not include 075.
The user's newer brief controls this proposed rework.
The production workbook owner must update the authoritative event and cluster records, assign any necessary scenario registry record through the real workflow, and regenerate exports.
No arbitrary new scenario ID or direct CSV-only edit is supplied here.
