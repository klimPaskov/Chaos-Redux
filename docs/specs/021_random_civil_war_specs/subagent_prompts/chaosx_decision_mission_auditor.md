# Subagent Prompt: Event 021 Decision and Mission Auditor

Spawn `chaosx_decision_mission_auditor` with `fork_context=false` after the Event 021 decision system is implemented.

Read:

- repository `AGENTS.md`
- `chaos-redux-decisions-missions`
- full Event 021 source-spec folder
- `021_random_civil_war_decision_mission_prompt.md`
- implemented Event 021 decisions, categories, missions, localisation, ideas, helpers, and AI

Audit and apply only small, safe patches.

Check:

- one visible State Authority value
- hidden Fracture Pressure
- standard category and static category picture
- no custom GUI or animation
- three to five primary actions per phase
- six only in a true emergency
- one to three active missions
- no hidden fifth cost
- at most four spendable cost types
- icon-first cost text
- costs beyond political or command power
- named state, rail, depot, capital, port, and corridor objectives
- goal-style auto-completion where appropriate
- success, failure, and partial success
- government, opposition, Event 006, neighbor, settlement, and reconstruction phases
- separate civilian relief and military aid
- multi-front selection and independent settlement
- AI validity and zero weight for impossible actions
- stale target cleanup
- category closure
- recurrence and obligation cleanup
- free-unit, factory, equipment, recognition, and settlement exploits
- duplicate or passive missions
- fairy-dust rewards

Patch only narrow decision, mission, tooltip, visibility, cleanup, cooldown, AI, or existing-helper issues.

Weighted changes require the probability audit, owner patch, and post-patch compare cycle.

Write:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/decision_mission_auditor_handoff.md`
