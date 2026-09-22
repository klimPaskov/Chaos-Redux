# Event 077. Parliament of Fear

A full planning specification for a repeatable political crisis built around a changing chamber, uncertain accusations, investigations, protection, removals, appointments, and lasting institutional consequences.

## Start here

Read the numbered design parts in order. They contain approximately 18,176 words of gameplay and presentation specification. For implementation, use the coding prompt and the specialist prompts after reading the source parts. The copy-ready goal prompt is 3,936 characters including its slash command and trailing newline.

| Part | Design file |
|---|---|
| 1 | [Core experience and opening](077_parliament_of_fear_spec_part_1_core.md) |
| 2 | [Seats, blocs, characters and evidence](077_parliament_of_fear_spec_part_2_chamber_and_evidence.md) |
| 3 | [Government-specific political behavior](077_parliament_of_fear_spec_part_3_government_profiles.md) |
| 4 | [Paranoia, incidents and pressure](077_parliament_of_fear_spec_part_4_paranoia_and_incidents.md) |
| 5 | [Four action families, costs and objectives](077_parliament_of_fear_spec_part_5_actions_and_objectives.md) |
| 6 | [Evolutions and organized resistance](077_parliament_of_fear_spec_part_6_evolutions_and_conspiracies.md) |
| 7 | [Great Purge, leadership crises and recovery](077_parliament_of_fear_spec_part_7_great_purge_and_endings.md) |
| 8 | [Connections and the global Chaos impact map](077_parliament_of_fear_spec_part_8_connections_and_chaos.md) |
| 9 | [Chamber interface and feedback](077_parliament_of_fear_spec_part_9_interface_and_feedback.md) |
| 10 | [Assets and severe-outcome super-event](077_parliament_of_fear_spec_part_10_assets_and_super_event.md) |
| 11 | [Localisation and narrative direction](077_parliament_of_fear_spec_part_11_writing_direction.md) |
| 12 | [Eight multi-condition achievements](077_parliament_of_fear_spec_part_12_achievements.md) |
| 13 | [AI behavior and balance targets](077_parliament_of_fear_spec_part_13_ai_and_balance.md) |

## Ready prompts

| File |
|---|
| [Coding-agent implementation prompt](077_parliament_of_fear_coding_prompt.md) |
| [Visual asset production prompt](077_parliament_of_fear_asset_prompt.md) |
| [Super-event research and production prompt](077_parliament_of_fear_super_event_prompt.md) |
| [Achievement implementation and icon prompt](077_parliament_of_fear_achievement_prompt.md) |
| [Decision and mission implementation prompt](077_parliament_of_fear_decision_mission_prompt.md) |
| [Copy-ready /goal prompt](077_parliament_of_fear_goal_prompt.md) |

## Package organization

Extract this event folder into `docs/specs/`. The resulting source location is `docs/specs/077_parliament_of_fear_specs/`. Numbered specification parts remain the canonical event design. Prompts are separate files and do not become part of the event narrative.

The `supporting_material/` directory holds the source record, research limits, proposed tuning, asset manifest, validation matrices, and standalone reference checks. These support the design and document its evidence status.

The `implementation_handoff/` directory contains implementation contracts, future subagent work packets, catalog changes, country-outcome checks, and the parent's design review. Move that directory to `docs/plans/077_parliament_of_fear_plans/` for implementation work. Its contents are plans and audit instructions, not completed implementation evidence.

No original source file, source workbook, CSV export, live gameplay file, or shared project skill was edited.

## Important design decisions

The chamber contains 100 abstract influence seats. Support, evidence status, and occupancy are separate. An accused seat can still support the government, and a cleared opposition bloc does not automatically become loyal. Vacancies do not reduce the 51-seat majority threshold.

The system uses three persistent readouts and four action families. Slow preliminary inquiries, negotiated support, and institutional restoration keep recovery possible when political power or governing support is low. They carry time, capacity, or political-control costs.

Original case truth persists. An innocent bloc can later organize resistance under Evolution II, but that produces a new causal plot and does not make an earlier false accusation true. Coups and civil wars require actual organization and backing.

The Great Purge has warnings, bounded waves, and containment opportunities. Permanent losses remain after closure. Repeated firings use surviving people and current institutions without resetting the country's history.

## Supporting material

| Material | Purpose |
|---|---|
| [Source coverage](supporting_material/077_source_coverage.md) | Exactly what was read, authored, checked and not executed |
| [Source manifest](supporting_material/077_source_read_manifest.json) | All 42 supplied text files with hashes and full-read records |
| [Research and reference gates](supporting_material/077_research_and_reference_gates.md) | Narrow source claims and missing full-read references |
| [Design decision register](supporting_material/077_design_decision_register.md) | User-fixed direction, parent-authored choices and unresolved evidence |
| [Proposed tuning](supporting_material/077_proposed_tuning.json) | Numerical design anchors, explicitly not engine-validated |
| [Asset manifest](supporting_material/077_asset_manifest.csv) | 48 planned production records, including conditional and multi-state families |
| [Asset notes](supporting_material/077_asset_manifest_notes.md) | Native-family handling and production requirements |
| [Validation matrix](supporting_material/077_validation_matrix.csv) | 93 implementation acceptance scenarios, all unrun in HOI4 |
| [Probability scenarios](supporting_material/077_probability_scenarios.csv) | 18 audit families awaiting actual source and MCP |
| [Validation guide](supporting_material/077_validation_guide.md) | Separation of packaging checks, reference tests and runtime evidence |
| [Reference model](supporting_material/077_reference_model.py) | Small abstract model of selected design invariants |
| [Reference tests](supporting_material/077_reference_model_tests.py) | 22 standalone tests, not a game simulator |
| [Actual reference-test output](supporting_material/077_reference_test_results.txt) | The recorded successful test run |
| [Package QA](supporting_material/077_package_qa.json) | File, link, content, manifest and prompt-length checks |

## Implementation handoffs

| File | Purpose |
|---|---|
| [Integration contract](implementation_handoff/077_integration_contract.md) | Identity, migration, state ownership, actions, callbacks and completion gates |
| [Catalog request](implementation_handoff/077_catalog_change_request.md) | Authorized future workbook changes and export procedure |
| [Country outcome matrix](implementation_handoff/077_country_outcome_matrix.md) | Leadership and civil-war identity and asset conservation |
| [Probability handoff](implementation_handoff/077_probability_handoff.md) | Required source-based MCP analysis |
| [Subagent packets](implementation_handoff/077_subagent_handoffs.md) | All 20 role definitions assessed with bounded future assignments |
| [Parent review](implementation_handoff/077_parent_design_review.md) | Applied design corrections and remaining independent-review gate |

These links are correct inside the delivered archive. After moving the handoff directory into `docs/plans/`, update the local handoff links or follow the new directory directly.

## Evidence status

All 42 supplied text files were read fully. Required external material was not all available in complete form. The full live repository, installed vanilla references, relevant complete offline wiki pages, actual workbook, and absent local tool resources remain reference gates.

No subagents were executed. The supplied role definitions were read, but the session did not expose a usable spawning runtime. No HOI4 MCP operation, native GUI render, asset or audio production, gameplay implementation, live playtest, or workbook edit is claimed.

The 22 standalone reference tests passed. They check only a small planning abstraction. They cannot certify actual game scripting, balance, character behavior, probabilities, or multiplayer execution. The source coverage and package QA distinguish those limits explicitly.
