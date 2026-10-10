# Decision and mission prompt

Implement the Event 036 decision category and missions exactly as [09](../09_decisions_missions_costs_and_visibility.md) defines them, using [the decisions and missions skill](../../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md).

Event-specific points to verify:

- the header shows three lines and nothing internal
- no more than five primary decisions and three Event 036 missions are visible at once
- publishing evidence, demanding inspections, sending decontamination aid, and setting use policy reuse the existing CBRN actions, with Event 036 adding only eligibility adapters
- every country-targeted action reuses existing target selection
- each exploit control in [09](../09_decisions_missions_costs_and_visibility.md#exploit-controls) has a test from [the acceptance matrix](../matrices/acceptance_scenarios.md)
- every decision has an AI path, checked against [the AI matrix](../matrices/ai_probability_scenarios.md)

After implementation, run `chaosx_decision_mission_auditor` with a self-contained prompt and fix its findings.
