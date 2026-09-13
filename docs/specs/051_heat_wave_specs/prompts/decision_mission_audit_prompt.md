# Decision and Mission Audit Prompt

Act as `chaosx_decision_mission_auditor` after Event 051 decisions and missions have been implemented.

Use no inherited context. Read:

- `AGENTS.md`
- `chaos-redux-decisions-missions`
- the full Event 051 spec package
- all Event 051 decision, category, helper, scripted localisation, idea, modifier, AI, and event files
- matching vanilla decision and mission precedents

## Audit scope

Audit and make only safe local patches for:

- category lifecycle and cleanup
- header clarity and two-value limit
- phase visibility and primary action cap
- hotspot target selection
- national protection priority switching
- costs, texticons, and four-cost maximum
- dynamic scaling
- mission objective quality
- named targets and exact durations
- success, partial success, and failure separation
- AI-equivalent paths
- invalid target cleanup
- controller change
- annexation and recovery cleanup
- repeated-click, restart, import, transfer, capital-move, and division-disband exploits
- decision localisation and blocked-reason clarity

## Accepted action families

Water rationing, cooling centres, army heat protocols, harvest protection, rail maintenance, night shifts, controlled shutdown, food imports, pumping protection, organized evacuation, and recovery actions.

Accepted mission families are defined in `09_decisions_and_missions.md`.

## Restrictions

Do not add a full scripted GUI, new public meters, a water stockpile, or a new event route. Broad gaps become a plan handoff.

Any AI weight patch requires a baseline probability audit and a post-patch compare under the same scenario IDs.

## Handoff

Write a handoff under:

`docs/plans/051_heat_wave_plans/subagent_handoffs/`

List decision and mission IDs, files, before and after behavior, costs changed, localisation keys changed, validation, unresolved probability work, and remaining design gaps.
