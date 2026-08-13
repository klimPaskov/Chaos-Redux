# Prompt for chaosx_decision_mission_auditor

Use `fork_context=false`. Audit and patch the Event 17 Bloc Pressure decision category after implementation. Read `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and the Event 17 spec package.

Check:

- decisions and missions match `matrices/017_random_faction_decision_map.md`
- costs are concrete and not only political power or command power
- border missions require real state or unit objectives
- faction leader decisions validate targets
- AI can use every meaningful action
- category visibility and cleanup are safe
- no duplicate mission loops or free influence farming exist
- localisation and blocked requirement tooltips are readable

Patch small local issues if safe. Write a handoff with changed ids, before and after behavior, validation, and remaining issues.
