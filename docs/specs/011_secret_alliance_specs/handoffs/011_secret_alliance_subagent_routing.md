# Event 011 Secret Alliance subagent routing handoff

This handoff maps the provided project subagents to the implementation pass. Subagents should be spawned with `fork_context=false` and given the relevant spec paths explicitly.

## Planning and architecture

| Subagent | Use |
| --- | --- |
| `chaosx_scripted_system_architect` | Design reusable helpers for candidate scoring, member arrays, reveal logic, dynamic costs, cleanup, event targets, and script constants |
| `chaosx_improvement_loop_planner` | Use only after a meaningful implementation tranche if the event still feels thin or disconnected |
| `chaosx_repo_explorer` | Use only if actual repo file locations or existing patterns are unclear |

## Gameplay audits

| Subagent | Use |
| --- | --- |
| `chaosx_decision_mission_auditor` | Audit and patch decision category, missions, costs, tooltips, AI, cleanup, and exploit risk |
| `chaosx_localisation_auditor` | Audit visible text, dynamic localisation, missing keys, duplicate keys, hidden route spoilers, and event-detail alignment |
| `chaosx_event_completion_auditor` | Read-only completion audit before final completion claim |
| `chaosx_focus_tree_auditor` | Not a primary route unless implementation adds focus hooks |
| `chaosx_country_package_auditor` | Use only if implementation adds country-specific route identities or modifies existing country packages |

## Assets and super-event research

| Subagent | Use |
| --- | --- |
| `chaosx_icon_artist` | Decision icons, idea icons, category icon, achievement icons, UI badges, and small animated icon packages |
| `chaosx_generated_event_art` | Generated report images, news image, super-event image, faction emblem, and Dossier Board UI art |
| `chaosx_asset_source_researcher` | Use only if a sourced historical or archival image is chosen during implementation |
| `chaosx_super_event_text_researcher` | Reveal super-event title direction, quote, cultural remark, attribution, and source confidence |
| `chaosx_super_event_audio_researcher` | Reveal super-event licensed audio research, download, `.ogg` conversion, and audio notes |

## Documentation and spreadsheet

| Subagent | Use |
| --- | --- |
| `chaosx_documentation_curator` | Reconcile specs, docs, plans, handoffs, manifests, and accepted design after implementation tranches |
| `chaosx_spreadsheet_doc_worker` | Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` only after final in-game wording exists |
| `chaosx_skill_maintainer` | Use only if implementation reveals a reusable workflow missing from existing skills |

## Required handoff placement

Subagent patch handoffs should go under:

`docs/plans/011_secret_alliance_plans/subagent_handoffs/`

Plan-only addenda should go under:

`docs/plans/011_secret_alliance_plans/`

Accepted design changes should be folded back into:

`docs/specs/011_secret_alliance_specs/`
