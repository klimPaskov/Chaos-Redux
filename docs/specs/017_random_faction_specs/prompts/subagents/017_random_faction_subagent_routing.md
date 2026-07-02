# Subagent routing plan for Event 17

This chat environment cannot spawn the custom Codex subagents directly. These prompts are ready for a Codex implementation agent to use with `fork_context=false`.

| Subagent | Use for Event 17 | Timing |
| --- | --- | --- |
| `chaosx_repo_explorer` | map existing event files, event log patterns, faction helpers, decision category patterns, and cluster registration before implementation | before editing if repo file paths are uncertain |
| `chaosx_scripted_system_architect` | design or patch reusable triggers, effects, constants, option targets, and cleanup helpers | before duplicating faction option logic |
| `chaosx_decision_mission_auditor` | audit and patch Bloc Pressure decisions, missions, costs, tooltips, AI, cleanup, and exploit risk | after decision implementation |
| `chaosx_localisation_auditor` | audit final event, decision, scripted localisation, event detail, evolution detail, and tooltip text | after broad text is written |
| `chaosx_icon_artist` | create decision icons, idea icons, achievement icons, animated seal frames, static fallbacks, manifests, and `gfx_handoff.md` | before final GFX wiring |
| `chaosx_spreadsheet_doc_worker` | update the event catalog workbook row for ID 17 from final in-game wording | after implementation and localisation are final |
| `chaosx_documentation_curator` | reconcile spec, docs, handoffs, manifests, and any accepted addenda | after several implementation handoffs |
| `chaosx_event_completion_auditor` | read-only completion audit against specs, prompts, assets, docs, spreadsheet, and implementation | before completion claim |
| `chaosx_improvement_loop_planner` | write a new addendum only if implementation creates a broader design gap not already covered | after a meaningful tranche if needed |

Subagents not scheduled by default: focus tree, country package, generated non-icon event art, sourced visual researcher, super-event text, and super-event audio. Event 17 does not create country packages, focus trees, real historical visual sourcing needs, or super-events in this source spec.
