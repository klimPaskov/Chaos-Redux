# Prompt for `chaosx_localisation_auditor`

Spawn with `fork_context=false` after Event 53 gameplay and Event Details text are implemented.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the complete Event 53 source specification, every Event 53 localisation and scripted-localisation file, Event Details and evolution selectors, event-log mappings, and the relevant event MCP artifacts.

Audit and patch the complete Event 53 player-facing text set:

- initial and recurring appearance titles and descriptions
- payment, refusal, and inability-to-pay options and tooltips
- payment and direct consequence reports
- target-loss and evolution reports
- Event History name and actor text
- Event Details premise and status
- Evolution I, II, and III detail text
- resource, amount, location, target, and consequence scripted localisation
- asset-facing titles or descriptions if any
- mirrored documentation wording that is in scope

Preserve all dynamic tokens and gameplay meaning. The man must remain unexplained. Remove registry IDs, formulas, update-history wording, developer labels, raw trigger text, hidden mechanics, and accidental source-event claims.

Enforce direct readable prose with no em dashes, semicolons, staccato chains, dialectical hedging, staged contrast formulas, generic dramatic filler, or pasteable prompt language. Keep tooltips concise while stating exact costs, thresholds, consequences, and blocked reasons.

Use `hoi4.event_inspect` and `hoi4.event_render` to verify source locations and visible flow. Use GUI renders only if the normal popup or Event Details surface is actually in scope and resolvable.

Write the handoff to:

`docs/plans/053_mysterious_man_plans/subagent_handoffs/localisation_audit_handoff.md`

List changed files and keys, prose issues fixed, dynamic text preserved, unresolved wording, meaningful validation, and blockers.
