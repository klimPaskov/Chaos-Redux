# Decision and Mission Prompt - Event 010 Death

Implement the Event 010 Death decision and mission systems from `010_death_decisions_ui_ai.md`. Follow `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.

Non-negotiables:

- Do not make the system a political-power store.
- Use concrete costs: convoys, fuel, trains, support equipment, infantry equipment, army XP, stability, war support, supply, divisions present, state control, relations, compact cohesion, and time pressure.
- Use goal-style missions for map objectives. Do not require a second click after the player holds the line or controls the target.
- Hide obsolete decisions by phase and route.
- Provide AI behavior for every important family.
- Use custom trigger tooltips and short icon-first cost localisation.
- Clean up missions and flags when Death is defeated, a state is reconsumed, a country becomes Herald, or a target becomes invalid.

Implement categories/phases:

1. Maritime Errata pre-reveal packet decisions.
2. The Death Country post-reveal containment category.
3. Living Containment Compact decisions and missions.
4. Dark Methods necromancy branch if included in this pass. Otherwise queue explicitly and keep hidden.
5. Black Oath Herald branch if included in this pass. Otherwise queue explicitly and keep hidden.
6. World-end emergency decisions.
7. Recaptured wasteland aftermath/rebuild decisions.

Before claiming completion, spawn/use `chaosx_decision_mission_auditor` for a targeted audit of costs, duplicate missions, AI validity, cleanup, exploit risk, and localisation clarity. Place handoff under `docs/plans/010_death_plans/subagent_handoffs/`.
