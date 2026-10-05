# Shared UI audit evidence

The production visual gate is blocked.
The calls below returned no GUI artifacts or validation result, so this folder contains requests and failure evidence rather than before/after PNGs.
No source image is presented as a production MCP render.

`mcp/connection.json` identifies the local stdio server as HOI4 agent tools 3.8.1.
`mcp/tools.json` preserves the live schemas.
`mcp/gui_context.json` is a successful GUI reference context bundle with source revisions, paths and line spans.
The subsequent reference search did not respond before its client timeout.
The focused History inspect and render returned no result after 120 and 180 seconds.

`audit_attempt/` preserves one inspect request and two separate resolution requests for each of the following main window families.
Each scenario explicitly selects 1920 by 1080 or 2560 by 1440 at scale 1, so the scenario's default resolution cannot replace the requested matrix.
Generated exploratory scenarios are disabled.
The changed Event Logs GUI requests include the exact pre-edit `.gui` source as `sourceBaseline`.

| Family | Window name | Request and result prefix |
| --- | --- | --- |
| Event Logs | `events_log_popup_window` | `event_logs` |
| Cluster Details | `events_log_cluster_details_window` | `cluster_details` |
| Event Details | `events_log_event_details_window` | `event_details` |
| Settings | `chaosx_settings_window` | `settings` |
| Chaos Meter | `chaos_meter_popup_window` | `chaos_meter` |
| Triggerable Scenarios | `chaosx_scenarios_window` | `scenarios` |
| Help | `chaosx_help_window` | `help` |

All seven inspections timed out after 60 seconds and all fourteen renders timed out after 90 seconds.
The raw request files are the authoritative call shapes.
There is no source hash, render provenance, hierarchy, click-region, cropped image, annotated image, `validation.json`, or matched image comparison from those calls.
The full tab, overlay, hover, disabled, crowded, long-text and maximum-value matrix remains open.
The supplied live screenshots were reviewed separately and do not fill the missing MCP evidence.

`feedback_colour_audit.json` records the scoped report-colour audit with no reached coloured title or description.
The detailed native reference results and event-tool blockers for the failure hook are archived with its handoff under `docs/plans/shared_interface_plans/subagent_handoffs/forced_feedback_mcp_20261005/`.

The implementation decisions, changed files, source checks, remaining blockers and exact orchestrator live checks are in `docs/plans/shared_interface_plans/completion_report_20261005.md` and `agent_decisions_2026-10-05.md`.
