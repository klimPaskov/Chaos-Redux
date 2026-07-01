# Coding prompt for Event 015, `utopia_manifesto`

Implement Event ID 15 as `utopia_manifesto`, replacing the old `World Tension Subsides` identity completely.

Read all files in `docs/specs/015_utopia_manifesto_specs/` first. Treat them as the source design. Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` as applicable.

## Non-negotiables

- Event ID 15 becomes Minor Fire-Once.
- It targets only eligible minors and eligible player countries.
- Majors and strong industry countries are blocked.
- AI always accepts when targeted.
- Human players can accept or reject.
- Acceptance replaces the focus tree only for the accepting country.
- Rejection cleanly ends the route and does not add hidden punishment.
- The event log and event details show the new identity and `N/A` when no valid target exists.
- The Utopian Ledger values are visible and drive decisions, focuses, AI, claims, and integration.
- The replacement focus tree is full, non-linear, and route-rich.
- The tree has opening trunk, political interpretation routes, industry, vocation, military, diplomacy, expansion, geography adaptation, hidden Marked Bounds, and late proclamation content.
- Decisions and missions use concrete costs and map objectives, not political power purchases.
- Needful land claims require Need proof, arbitration, or hardline route risk.
- Occupation and integration never grant instant free cores on large regions.
- AI gets route, focus, decision, claim, integration, and League safety logic.
- Achievements are implemented with difficult conditions, disqualifiers, tracking, icons, and docs.
- Assets are created through the proper asset workflow. Do not use placeholders as complete assets.
- Late super-events require researched titles, quotes, button remarks, image, audio, source notes, and unique final audio before being marked complete.

## Subagent cadence

Use `chaosx_scripted_system_architect` before duplicating Ledger, target, integration, or relationship logic. Use `chaosx_focus_tree_auditor`, `chaosx_decision_mission_auditor`, `chaosx_localisation_auditor`, and `chaosx_event_completion_auditor` before claiming completion. Use asset and super-event subagents for actual assets and researched super-event material.

## Completion report

Report files changed, systems touched, implemented routes, decision families, ideas, AI behavior, assets, super-events, achievements, docs, spreadsheet status, validation, and every simplification or blocker. Do not claim completion while any spec requirement is missing, simplified, placeholder, unwired, or unaudited.

