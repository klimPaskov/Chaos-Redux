# Event 021 Random Civil War Package Manifest

## Package identity

- Event ID: `21`
- Slug: `random_civil_war`
- Intended install target: `docs/specs/021_random_civil_war_specs/`
- Main specification: ten numbered parts
- Compiled convenience copy: one
- Main implementation prompts: five
- Subagent prompts: 16
- Files before this manifest and checksum file: 40
- Logical lines before this manifest and checksum file: 13,136
- Bytes before this manifest and checksum file: 412,868
- Goal prompt length: 3,998 characters

## Accepted design summary

The package defines:

- country-specific generic civil wars
- hidden Fracture Pressure
- one visible State Authority value
- dynamic territory, capital, supply, force, and stockpile planning
- ideological, legal, regional, command, Event 006, and same-tag actor routes
- multi-front wars
- Event 006 independence-package reuse
- neighboring Regional Exposure
- rare bounded strange incidents
- nonterminal Global Fracture
- bounded due-country review and Critical queue
- theater and generation caps
- settlement, reconstruction, successor memory, and recurrence
- Wars cluster integration
- a manual global fracture scenario
- role-specific AI
- six achievements
- static report, news, category-picture, icon, idea, mission, and achievement assets
- full event-log, Event Details, evolution, cluster, scenario, documentation, workbook, probability, performance, and completion requirements

## Explicitly absent

The accepted design does not include:

- custom event-owned scripted GUI
- focus inlay window
- animated fracture seal
- animated category picture
- animated portrait
- new generic claimant flag
- new generic claimant portrait
- super-event
- world-end branch
- 3D asset
- custom skeletal animation

## File inventory

| File | Lines | Bytes | Purpose |
| --- | ---: | ---: | --- |
| `021_random_civil_war_achievement_prompt.md` | 145 | 4,408 | Six-achievement implementation and asset prompt. |
| `021_random_civil_war_asset_prompt.md` | 214 | 6,306 | Authorized static asset production prompt and exclusion boundary. |
| `021_random_civil_war_coding_prompt.md` | 325 | 10,759 | Full implementation prompt across all gameplay, AI, log, asset, scenario, cluster, documentation, and audit surfaces. |
| `021_random_civil_war_country_package_matrix.md` | 78 | 6,849 | Actor-type, identity, force, tree, leader, origin, reinforcement, and disposition matrix. |
| `021_random_civil_war_decision_mission_prompt.md` | 251 | 6,565 | Bounded decision and mission implementation prompt. |
| `021_random_civil_war_goal_prompt.md` | 23 | 3,999 | Condensed implementation goal prompt under 4,000 characters. |
| `021_random_civil_war_master_spec.md` | 5,268 | 151,806 | Compiled convenience copy of the ten numbered source-spec parts. |
| `021_random_civil_war_overlap_and_catalog_reconciliation.md` | 122 | 5,164 | Boundaries with specialized events, catalog status, cluster proposal, and scenario distinction. |
| `021_random_civil_war_probability_scenario_matrix.md` | 151 | 8,418 | Named weighted-logic and timing scenarios for baseline and post-patch comparison. |
| `021_random_civil_war_research_notes.md` | 172 | 9,799 | External research sources, direct design translations, historical policy, strange-incident limits, and research gaps. |
| `021_random_civil_war_revision_notes.md` | 124 | 5,075 | Reconciliation with the July 25 package and list of retained, revised, and superseded design. |
| `021_random_civil_war_role_review.md` | 149 | 6,284 | Skill application, subagent routing, conditional roles, and unavailable-runtime disclosure. |
| `021_random_civil_war_source_read_ledger.md` | 130 | 8,833 | Complete supplied-source inventory, hashes, catalog parsing, prior-package review, and unavailable-source disclosure. |
| `021_random_civil_war_spec_part_10_acceptance_and_implementation_handoff.md` | 584 | 14,344 | Preflight, tranches, MCP gates, acceptance scenarios, validation, audits, docs, workbook, and completion proof. |
| `021_random_civil_war_spec_part_1_core.md` | 180 | 9,337 | Event identity, ownership, availability, evolution structure, exclusions, and completion boundary. |
| `021_random_civil_war_spec_part_2_targeting_and_baseline.md` | 371 | 17,109 | Hidden Fracture Pressure, severity, archetypes, territory, forces, State Authority, ideas, and baseline outcomes. |
| `021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md` | 591 | 16,382 | Affected-side actions, missions, costs, settlements, reconstruction, recurrence, and cleanup. |
| `021_random_civil_war_spec_part_4_evolution_i.md` | 374 | 12,735 | Multi-front wars, majors, Event 006 independence fronts, prevention, front relations, and separate outcomes. |
| `021_random_civil_war_spec_part_5_evolution_ii.md` | 608 | 15,904 | Regional Exposure, neighbor actions, sponsors, political spread, side adaptation, strange incidents, and cleanup. |
| `021_random_civil_war_spec_part_6_evolution_iii.md` | 526 | 16,846 | Global Fracture risk bands, bounded scheduler, Critical queue, caps, nested crises, global reactions, and high-chaos scaling. |
| `021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md` | 570 | 16,518 | Ordinary claimant and Event 006 contracts, focus handling, forces, identities, event boundaries, and permanent disposition. |
| `021_random_civil_war_spec_part_8_cluster_scenario_ai_balance.md` | 669 | 15,406 | Wars cluster, manual scenario, AI profiles, probability intent, balance, performance, and multiplayer. |
| `021_random_civil_war_spec_part_9_presentation_assets_achievements.md` | 720 | 16,061 | Writing direction, static asset inventory, six achievements, and asset limits. |
| `README.md` | 53 | 3,723 | Package identity, reading order, design boundary, and implementation status. |
| `subagent_prompts/README.md` | 28 | 840 | Subagent prompt index, shared paths, fork rule, and excluded roles. |
| `subagent_prompts/chaosx_ai_probability_auditor.md` | 54 | 1,909 | Context-complete implementation handoff for `chaosx_ai_probability_auditor`. |
| `subagent_prompts/chaosx_asset_source_researcher_conditional.md` | 46 | 1,180 | Context-complete implementation handoff for `chaosx_asset_source_researcher_conditional`. |
| `subagent_prompts/chaosx_country_package_auditor.md` | 60 | 1,848 | Context-complete implementation handoff for `chaosx_country_package_auditor`. |
| `subagent_prompts/chaosx_decision_mission_auditor.md` | 48 | 1,739 | Context-complete implementation handoff for `chaosx_decision_mission_auditor`. |
| `subagent_prompts/chaosx_documentation_curator.md` | 38 | 1,197 | Context-complete implementation handoff for `chaosx_documentation_curator`. |
| `subagent_prompts/chaosx_event_completion_auditor.md` | 49 | 1,842 | Context-complete implementation handoff for `chaosx_event_completion_auditor`. |
| `subagent_prompts/chaosx_focus_tree_auditor_conditional.md` | 38 | 1,465 | Context-complete implementation handoff for `chaosx_focus_tree_auditor_conditional`. |
| `subagent_prompts/chaosx_generated_event_art.md` | 41 | 1,207 | Context-complete implementation handoff for `chaosx_generated_event_art`. |
| `subagent_prompts/chaosx_icon_artist.md` | 57 | 1,446 | Context-complete implementation handoff for `chaosx_icon_artist`. |
| `subagent_prompts/chaosx_improvement_loop_planner.md` | 62 | 1,627 | Context-complete implementation handoff for `chaosx_improvement_loop_planner`. |
| `subagent_prompts/chaosx_localisation_auditor.md` | 42 | 1,593 | Context-complete implementation handoff for `chaosx_localisation_auditor`. |
| `subagent_prompts/chaosx_repo_explorer.md` | 47 | 1,900 | Context-complete implementation handoff for `chaosx_repo_explorer`. |
| `subagent_prompts/chaosx_scripted_system_architect.md` | 57 | 2,101 | Context-complete implementation handoff for `chaosx_scripted_system_architect`. |
| `subagent_prompts/chaosx_skill_maintainer_conditional.md` | 32 | 1,008 | Context-complete implementation handoff for `chaosx_skill_maintainer_conditional`. |
| `subagent_prompts/chaosx_spreadsheet_doc_worker.md` | 39 | 1,336 | Context-complete implementation handoff for `chaosx_spreadsheet_doc_worker`. |

## Source status

Every directly supplied project file and every extracted custom subagent TOML file was read in full.

The live repository, offline wiki, installed vanilla files, Workshop references, authoritative XLSX, live MCP routes, and custom subagent runtime were unavailable. Their review is required during implementation and is not represented as completed.

## Package status

This is a complete planning and implementation-handoff package.

It does not claim that Event 021 is implemented.
