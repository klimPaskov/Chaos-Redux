# Decision and mission implementation prompt for Event 011 Secret Alliance

Use `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, and the Event 011 spec files. Implement the decision category, Dossier Board hooks if accepted by the main implementation pass, missions, costs, AI equivalents, dynamic localisation, tooltips, cleanup, and balance checks.

## Source files

- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_decisions_missions.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_decision_map.md`
- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_mechanics.md`

## Non-negotiables

- The category opens only when suspicion, Evolution II, or a serious incident justifies it.
- Decisions are not a political power store.
- Costs use equipment, XP, command power, fuel, trains, trucks, manpower, tied-down divisions, stability, relations, civilian burden, and evidence requirements where appropriate.
- Missions require action on the map or through decisions.
- Active mission count is capped.
- Each action has success, failure, and partial outcomes where useful.
- AI has equivalents and does not rely on a human-only GUI.
- Cleanup removes stale member decisions, selected member flags, active missions, and UI state.
- Dynamic text names current values, known members, and relevant regions without exposing hidden future content.

## Auditor route

After implementation, use `chaosx_decision_mission_auditor` for a targeted audit. It should check decision lifecycle, cost clarity, objective quality, duplicate missions, AI validity, localisation coverage, cleanup, and exploit risk. If it patches anything, it must write a handoff under `docs/plans/011_secret_alliance_plans/subagent_handoffs/`.
