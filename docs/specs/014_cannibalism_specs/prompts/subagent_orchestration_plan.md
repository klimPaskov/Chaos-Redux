# Event 014 Subagent Orchestration Plan

> Historical build contract (spec audit 2026-10-10): this prompt drove the implemented Event 014 build and is kept as provenance.
> Do not re-run it; current status and open work are in `../quality/package_status.md` and the package README.
> Its `AGENTS.md`, `.agents/skills/` and `fork_turns="none"` references map to the current `CLAUDE.md`, `.claude/skills/<name>/SKILL.md` and the routing in `chaos-redux-subagents`.

All project custom subagents must use `fork_turns="none"`.

| Stage | Subagent | Bounded task | Required handoff |
| --- | --- | --- | --- |
| Pre-implementation mapping | `chaosx_repo_explorer` | Find Event 14 touchpoints, existing Wendigo implementation, tag capacity, UI patterns, and reference files | Repo map under Event 14 plans |
| Script architecture | `chaosx_scripted_system_architect` | Design values, actor arrays, state nodes, Larder, consumption, spread, cleanup, and helper map | Helper and constants plan or patch handoff |
| Decision implementation | `chaosx_decision_mission_auditor` | Audit and patch phased categories, missions, costs, AI, cleanup, and exploit controls | Decision handoff |
| Focus implementation | `chaosx_focus_tree_auditor` | Audit and patch local, unified, and Wendigo focus surfaces | Route coverage handoff |
| Country implementation | `chaosx_country_package_auditor` | Audit all warlord slots, unified host, Wendigo merge, forces, leaders, flags, and AI | Country package handoff |
| Localisation | `chaosx_localisation_auditor` | Check keys, dynamic text, tooltips, encoding, and Hannibal secrecy | Key-level audit and patch handoff |
| Portrait packages | `chaosx_portrait_creator` | Warlord and supplied Hannibal portrait packages, animation, processing, portrait wiring, and provenance | Portrait manifest and scoped handoff |
| Generated event art | `chaosx_generated_event_art` | Report, news, super-event, flag, and GUI art | Asset manifest and GFX handoff |
| Icons and animation | `chaosx_icon_artist` | Focus, idea, decision, achievement, unit, route, and warning icons | Icon and animation package handoff |
| Super-event text | `chaosx_super_event_text_researcher` | Quotes, titles, descriptions, remarks, sources, and risk | Research note |
| Super-event audio | `chaosx_super_event_audio_researcher` | Unique licensed track per role and final WAV preparation under `chaos-redux-super-events` | Audio manifest and files |
| Improvement pass | `chaosx_improvement_loop_planner` | Depth, connection, anti-bloat, and closure review | Addendum or closure handoff |
| Documentation | `chaosx_documentation_curator` | Source-of-truth map and plan disposition cleanup | Resume and cleanup handoff |
| Spreadsheet | `chaosx_spreadsheet_doc_worker` | Update Event 14 catalog workbook from final in-game wording | Workbook change report |
| Completion | `chaosx_event_completion_auditor` | Full spec-versus-implementation audit | Completion audit report |

The parent implementation agent owns final integration, event direction, gameplay edits outside narrow subagent patches, GFX and GUI wiring, final validation, and completion claims.
