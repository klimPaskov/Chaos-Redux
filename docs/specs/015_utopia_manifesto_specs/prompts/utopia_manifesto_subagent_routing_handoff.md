# Subagent routing handoff for Event 015, `utopia_manifesto`

All custom subagents must be spawned with `fork_context=false` and must receive explicit paths and scope.

## Recommended subagent use

| Need | Subagent | Timing |
| --- | --- | --- |
| Scripted helpers for Ledger values, target checks, integration, relationship cleanup, and constants | `chaosx_scripted_system_architect` | before broad implementation duplicates logic |
| Focus tree quality and small route fixes | `chaosx_focus_tree_auditor` | after focus tree implementation |
| Decision costs, missions, AI, cleanup, and exploit risk | `chaosx_decision_mission_auditor` | after decision implementation |
| Localisation keys, dynamic text, tooltips, duplicate keys | `chaosx_localisation_auditor` | after visible text exists |
| Country package, cosmetics, flags, leaders, names, focus loading | `chaosx_country_package_auditor` | if late identities or leaders are implemented |
| Generated report images, super-event images, fictional flags, collective portraits, UI panels | `chaosx_generated_event_art` | asset production stage |
| Focus, idea, decision, achievement, category, and animated icon assets | `chaosx_icon_artist` | asset production stage |
| Quotes, title references, button remarks for late super-events | `chaosx_super_event_text_researcher` | before super-event localisation |
| Licensed or public domain audio for late super-events | `chaosx_super_event_audio_researcher` | before audio wiring |
| Documentation cleanup after long implementation | `chaosx_documentation_curator` | before final audit if docs drift |
| Completion audit | `chaosx_event_completion_auditor` | before final completion claim |
| Event catalog workbook alignment | `chaosx_spreadsheet_doc_worker` | after final in-game wording exists |

## Planner note

This package already acts as the initial improvement and planning output. Do not spawn another improvement-loop planner for this event until this spec is implemented, folded into source specs, queued with a reason, or rejected with a reason.

## Report path convention

Subagent handoffs should use:

`docs/plans/015_utopia_manifesto_plans/subagent_handoffs/`

Each patch-capable subagent must report changed files, changed ids, before and after behavior, meaningful validation, skipped validation, remaining issues, and follow-up required by the parent.

