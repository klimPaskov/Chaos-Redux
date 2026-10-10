# Event 033 Acid Rain decision and AI resume prompt

The Acid Rain Response category is implemented in `common/decisions/033_acid_rain_decisions.txt` and `common/scripted_effects/033_acid_rain_preparedness_effects.txt`.
Part 5 owns the category, projects, urgent operations and recovery; the decision cost matrix owns every cost and duration and matches `common/script_constants/033_acid_rain_constants.txt`; Part 8 and the AI acceptance matrix own AI behavior and the probability workflow.

Read [the decisions skill](../../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md) and agent decisions D6 to D15 in the plans folder before editing.
Use `chaosx_decision_mission_auditor` for the category audit and `chaosx_ai_probability_auditor` for any weight change.

## Remaining decision work

- Implement README open question 2 only if the parent accepts it, then update the matrix, Part 5 and the constants together.
- Complete the pending named-scenario probability comparison for the useful-window guard (Part 8).
- Keep every decision's displayed cost on the same quote the affordability trigger and the debit use (D7).

## Checks that must stay true

- Exact stock is enough and one item short blocks the decision.
- Reserved manpower and factory commitments return once; consumed resources never refund.
- Land and island variants never charge trains and convoys together.
- AI pays player costs, keeps the Part 8 reserves and never buys an action that cannot affect a remaining pulse.
