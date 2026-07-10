# Source reading manifest

This planning pass fully read every project source file supplied with the task. No supplied source was skipped, summarized from a filename alone, or treated as unread because a preview was truncated.

The files were read from their complete local copies under `/mnt/data`.

| Source | Lines read | Role in this package |
| --- | ---: | --- |
| `AGENTS.md` | 372 | Repository rules, required references, source-of-truth paths, subagent routing, validation, and completion honesty |
| `CHAOS_REDUX_MECHANICS.md` | 973 | Event selection, chaos tiers, event logs, clusters, scenarios, world systems, and shared mechanics |
| `chaos-redux-event-assets.md` | 1046 | Asset coverage, source mode, sizes, manifests, DDS handoff, flags, portraits, icons, and UI assets |
| `chaos-redux-event-planning.md` | 1799 | Full planning standard, country packages, focus architecture, decisions, AI, achievements, prompts, and ZIP packaging |
| `chaos-redux-events.md` | 692 | Event contract, repeatable event behavior, origin handling, cluster integration, logs, scenarios, docs, and catalog alignment |
| `chaos-redux-frame-animation.md` | 483 | Real per-frame animation rules, frame sheets, static fallbacks, preview requirements, and wiring handoff |
| `chaos-redux-improvement-loop.md` | 275 | Depth pass, anti-bloat rules, closure conditions, and design-gap review |
| `chaos-redux-subagents.md` | 288 | Custom subagent ownership, fork-context rules, handoffs, audits, and routing |
| `chaos-redux-super-events.md` | 791 | Super-event role, quote research, cultural remark research, image and audio requirements, and implementation gates |
| `hoi4-decisions-missions.md` | 890 | Active decision design, missions, costs, AI, cleanup, formables, GUI, clutter control, and balance |
| `hoi4-focus-trees.md` | 898 | Branch depth, route interaction, AI, rewards, formable links, shared-tree adaptation, and country identity |
| `chaos_redux_clusters_catalog.csv` | 15 | Liberations cluster definition and Event 5 and Event 6 membership |
| `chaos_redux_events_catalog.csv` | 1035 | Current catalog entries and the existing Event 6 draft. Rows 204 through 1035 were verified as blank CSV tail rows |
| `chaos_redux_scenarios_catalog.csv` | 20 | Existing scenario IDs, type patterns, intensity behavior, and next available scenario slot |
| `chaosx_asset_source_researcher.toml` | 93 | Historical and archival visual sourcing brief |
| `chaosx_country_package_auditor.toml` | 94 | Country package coverage and audit expectations |
| `chaosx_decision_mission_auditor.toml` | 76 | Decision and mission audit and patch boundaries |
| `chaosx_documentation_curator.toml` | 136 | Documentation source-of-truth and plan disposition rules |
| `chaosx_event_completion_auditor.toml` | 54 | Completion evidence and simplification audit expectations |
| `chaosx_focus_tree_auditor.toml` | 68 | Focus route coverage and audit expectations |
| `chaosx_generated_event_art.toml` | 73 | Generated fictional and alternate-history art handoff |
| `chaosx_icon_artist.toml` | 100 | Icon production, animation, transparency, dimensions, and manifests |
| `chaosx_improvement_loop_planner.toml` | 79 | Plan-only expansion and closure handoff behavior |
| `chaosx_localisation_auditor.toml` | 73 | Localisation coverage, dynamic text, and cross-surface consistency |
| `chaosx_repo_explorer.toml` | 190 | Large-task repository mapping and validation handoff rules |
| `chaosx_scripted_system_architect.toml` | 78 | Reusable helper, constants, event targets, and cleanup architecture |
| `chaosx_skill_maintainer.toml` | 50 | Reusable workflow maintenance rules |
| `chaosx_spreadsheet_doc_worker.toml` | 65 | Event catalog workbook ownership and player-facing mirror rules |
| `chaosx_super_event_audio_researcher.toml` | 69 | Licensed audio research and conversion handoff |
| `chaosx_super_event_text_researcher.toml` | 71 | Quote, remark, attribution, and copyright-risk research |

Total source lines read: 10,849.

## Catalog conflict resolved by this source specification

The current Event 6 catalog draft uses variable wave ranges of 4 to 6, 5 to 7, 6 to 9, 8 to 12, and 10 to 16. The user supplied a newer exact baseline of 3, 4, 5, 7, and 10. This package treats the user-supplied ladder as authoritative and records the old catalog wording as stale. The catalog handoff explains how the final in-game wording and workbook row should be updated after implementation.

## Custom subagent execution status

The project files define several custom Codex subagents. This environment did not expose a subagent execution tool, so none of those custom agents were actually spawned. Their full instructions were read and applied to the planning structure. Ready-to-run prompts for the appropriate agents are included under `prompts/independence_wave_subagent_routing_and_briefs.md`.

A manual improvement-loop review is included under `quality/manual_improvement_loop_review.md`. It is a substitute design review, not a claim that `chaosx_improvement_loop_planner` ran.

## Follow-up research completion pass

The follow-up requested after the first package re-read the affected source specifications, matrices, prompt files, quality reports, and the entire original research folder before changing research status. It also inspected the current public Chaos Redux country-tag registry and the Event 5 overlap documentation so Event 6 reuse decisions did not overwrite a distinct identity or inherit Soviet Collapse content.

External research in this pass checked treaty and institutional sources for statehood and league design, academic and heritage sources for signature countries and sensitive packages, and item-level source pages for both selected super-event recordings. The final research register distinguishes direct URL sources from bibliographic and institutional packets. It does not treat a general bibliography as proof of rights for a specific portrait, flag, image, or audio derivative.

The completed follow-up files are listed in `research/006_research_completion_report.md`. They include a resolution row for all 206 candidate packages, 111 map reservation groups, a tag collision audit, signature-country dossiers, sensitive-package dispositions, final super-event text research, final super-event audio research, and a 74-entry source register.

The environment still did not expose a project custom subagent execution tool. No custom subagent was represented as having run. The parent pass performed the research and validation directly and retained the ready-to-run subagent briefs for implementation and production work.
