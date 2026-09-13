# Event 063 source inventory

## Reading status

Every project file supplied with this task was read in full before the specification package was written. This includes all top-level Markdown files, the TOML configuration, the three CSV catalog exports, and every TOML subagent definition inside the supplied ZIP archive.

The physical line counts below are included to make the review scope explicit. The event CSV contains quoted multiline fields, so its physical line count differs from its logical row count.

## Top-level project files

| File | Physical lines | Review use |
| --- | ---: | --- |
| `AGENTS(10).md` | 417 | Repository rules, research, validation, ownership, and documentation baseline |
| `CHAOS_REDUX_MECHANICS(9).md` | 1164 | Event pacing, Chaos tiers, clusters, scenarios, multiplayer, logs, and the Liberation Release Coordinator |
| `README(20260830-071218).md` | 37 | Project identity and public description |
| `chaos-redux-3d-model-pipeline.md` | 413 | Checked for visible 3D scope and handoff rules |
| `chaos-redux-comfyui.md` | 16 | Checked for image workflow ownership |
| `chaos-redux-debug-playtest.md` | 666 | Validation, playtest, runtime evidence, and cleanup rules |
| `chaos-redux-decisions-missions(1).md` | 1166 | Decision visibility, missions, costs, AI, presentation, and anti-clutter rules |
| `chaos-redux-event-assets.md` | 1519 | Image, icon, achievement, category-picture, faction-emblem, manifest, and DDS rules |
| `chaos-redux-event-planning(1).md` | 2277 | Specification depth, research, AI, achievements, assets, prompt files, and ZIP packaging rules |
| `chaos-redux-events(1).md` | 804 | Event implementation ownership, clusters, logs, workbook, and validation rules |
| `chaos-redux-focus-trees.md` | 1503 | Checked for focus-tree scope and route standards |
| `chaos-redux-frame-animation.md` | 495 | Checked for animated-asset scope and fallback requirements |
| `chaos-redux-improvement-loop.md` | 287 | Near-completion depth and anti-bloat review |
| `chaos-redux-subagents(1).md` | 357 | Subagent routing, scope boundaries, and parent review |
| `chaos-redux-super-events.md` | 793 | Checked for super-event threshold and research rules |
| `chaos_redux_clusters_catalog(4).csv` | 14 | All 13 logical cluster rows reviewed |
| `chaos_redux_events_catalog(4).csv` | 252 | All 165 logical event rows reviewed |
| `chaos_redux_scenarios_catalog(4).csv` | 56 | All 13 logical scenario rows reviewed |
| `chaosx_dynamic_effects.md` | 280 | Shared effect registry and owner-neutral helper boundaries |
| `chaosx_dynamic_triggers.md` | 61 | Shared trigger registry and neutral classifier boundaries |
| `config(2).toml` | 189 | Project agent and tool configuration |
| `subagents(4).zip` | Archive | Extracted and reviewed every file listed below |

## Subagent definitions from the supplied archive

| File | Physical lines | Applied review area |
| --- | ---: | --- |
| `chaosx_3d_model_pipeline.toml` | 187 | Checked visible-model applicability |
| `chaosx_ai_probability_auditor.toml` | 66 | Candidate, settlement, intervention, and evolution probability scenarios |
| `chaosx_asset_source_researcher.toml` | 58 | Historical source-image boundary review |
| `chaosx_country_package_auditor.toml` | 87 | Existing-country preservation and custom-package boundary |
| `chaosx_decision_mission_auditor.toml` | 99 | Decision phases, mission caps, costs, and cleanup |
| `chaosx_documentation_curator.toml` | 131 | Package map, source inventory, catalog handoff, and cross-file consistency |
| `chaosx_event_completion_auditor.toml` | 66 | Acceptance matrix and blocker review |
| `chaosx_event_ui_worker.toml` | 84 | Decision-category presentation and UI restraint |
| `chaosx_focus_tree_auditor.toml` | 80 | Checked focus-tree applicability |
| `chaosx_generated_event_art.toml` | 72 | Report, news, and category-picture directions |
| `chaosx_icon_artist.toml` | 104 | Decision, idea, faction, and achievement icon coverage |
| `chaosx_improvement_loop_planner.toml` | 61 | Depth, overlap, and anti-bloat closure pass |
| `chaosx_localisation_auditor.toml` | 108 | Direction-only localisation and dynamic actor coverage |
| `chaosx_portrait_creator.toml` | 20 | Checked portrait applicability |
| `chaosx_repo_explorer.toml` | 234 | Catalog, registry, ownership, and overlap inspection framework |
| `chaosx_scripted_system_architect.toml` | 74 | Frozen transaction, shared origin contract, and Pact state model |
| `chaosx_skill_maintainer.toml` | 47 | Checked whether the task required a skill change |
| `chaosx_spreadsheet_doc_worker.toml` | 59 | Workbook and CSV export handoff |
| `chaosx_super_event_audio_researcher.toml` | 65 | Checked audio and super-event applicability |
| `chaosx_super_event_text_researcher.toml` | 62 | Checked super-event text applicability |

## Catalog reconciliation

### Event catalog

All 165 logical event rows were read. The closest overlap rows were examined in detail:

- Event 005 Soviet Union Collapse
- Event 006 Independence Wave
- Event 062 Allies Backstab
- Event 063 End Subject Status, the row being reworked
- Event 077 Equipment Aid
- Event 078 Border Conflict
- Event 095 Occupation Revolt
- Event 119 Random New Alliance
- Event 121 The Pact
- Event 127 Warlords
- Event 128 Autonomy
- Event 133 Gandhi
- Event 144 Freedom or Death
- Event 153 Random Guarantee

### Cluster catalog

All 13 logical rows were read. Liberations is registered as Cluster ID 2 with Events 005 and 006. Domestic Unrest is not present in the supplied export, so this package preserves it as the requested secondary classification without assigning an unverified ID.

### Scenario catalog

All 13 logical rows were read. Event 063 does not reuse the Event 006 `Every Banner Rises` scenario because that scenario owns a frozen country-creation and territory-release transaction. The Event 063 design remains an automatic repeatable existing-subject release system.

## Reading and execution distinction

The source-reading requirement was completed. Isolated subagent execution is a separate tooling question and is documented in `quality/063_subjects_break_free_role_reviews.md`.
