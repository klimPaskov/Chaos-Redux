# Event 41 implementation subagent routing

Every project subagent must receive a complete self-contained prompt and no inherited thread context. In the Codex runtime, use `fork_context=false`.

## Required implementation specialists

### chaosx_scripted_system_architect

Use for the bounded episode ledger, active-country registry, affected-node registry, sick and convalescent accounting, military death adapter, cross-border generation proof, civilian spillover request and receipt contract, script constants, and reusable validation helpers.

The architect can implement narrow reusable helpers and direct call sites. It should not redesign the event.

### chaosx_decision_mission_auditor

Use after the event-owned decision category and mission family are implemented.

Audit and patch:

- phased visibility
- maximum visible action budget
- target-sector mission validity
- costs and texticons
- mission success and failure
- posture cooldowns
- AI use
- cleanup
- exploit risk

### chaosx_ai_probability_auditor

Use before any weighted AI or probability patch to establish baseline evidence. Use again after implementation with `hoi4.probability_compare` against the same scenario IDs.

Audit:

- target-country selection
- hidden profile selection
- decision AI weights
- operational posture weights
- evolution pacing
- cross-border target selection
- civilian spillover request chance

### chaosx_generated_event_art

Use for the generated documentary report image and generated static decision category picture. The prompt must name exact sizes, paths, source mode, period constraints, and handoff path.

### chaosx_icon_artist

Use for the event's decision, category, pressure, formation-status, idea, modifier, and achievement icons. Require the correct reference family for each icon type and native transparent generation for alpha-backed assets.

### chaosx_localisation_auditor

Use after final event, decision, tooltip, Event Details, Event Logs, achievement, Chaos History, and scripted-localisation text is written.

Audit and patch:

- key coverage
- player-facing clarity
- dynamic country, state, sector, and pressure text
- blocked cost text
- stage and trend wording
- cluster and catalog alignment
- forbidden implementation or rework language

### chaosx_spreadsheet_doc_worker

Use only after implementation facts and final player-facing wording are stable.

Update the canonical workbook and run the exporter. Do not edit CSV files directly.

### chaosx_event_completion_auditor

Use before any completion claim. Compare the full spec pack with the implemented event, decisions, AI, assets, achievements, documentation, cluster row, catalog row, Chaos map, Deaths integration, and civilian adapter.

### chaosx_improvement_loop_planner

Use near completion after the main implementation tranche. Resolve its addendum or closure handoff before claiming completion. Do not run another planner pass while an earlier addendum remains unresolved.

## Conditional specialists

### chaosx_repo_explorer

Use only if the file map, existing military casualty helper, biological outbreak adapter, or comparable event pattern remains unclear after direct inspection. It is not a ritual preflight.

### chaosx_documentation_curator

Use if long implementation creates conflicting specs, plans, handoffs, or temporary asset notes. It can reconcile documentation only.

## Parent ownership

The parent implementation agent retains responsibility for:

- final event direction
- cross-system wiring
- source and vanilla inspection
- event and GUI MCP evidence where applicable
- final asset wiring
- event log and Event Details integration
- workbook alignment
- acceptance scenarios
- completion report
- honest blocker and simplification reporting
