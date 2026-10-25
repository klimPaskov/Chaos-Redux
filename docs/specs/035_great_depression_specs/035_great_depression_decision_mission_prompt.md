# Event 35 Great Depression 2.0 decision and mission audit prompt

Audit the implemented Event 35 decision category for `chaosx_decision_mission_auditor` or a parent acting as reviewer.
Use the `chaos-redux-decisions-missions` skill.

## Sources

- Source: `common/decisions/035_great_depression_decisions.txt`, `common/decisions/categories/035_great_depression_categories.txt`, the decision effects and surface triggers, and `common/scripted_localisation/035_great_depression_cost_localisation.txt`.
- Design: part 3 (doctrines, presentation, decision-surface budget, missions), the [decision map](035_great_depression_decision_map.md), part 2 (player-facing value budget) and part 9 (AI and exploits).
- Implemented contract: `docs/events/035_great_depression.md`, Recovery doctrines and decisions.

## Questions to answer

1. Do the counts from `.tools/tests/test_event035_visible_actions.py` still stay within the part 3 budget after the change?
2. Which visible actions repeat one idea under different names after the merges recorded in the README decisions?
3. Does every paid action use one affordability predicate for availability and display, spend at most four resource types and charge exactly once?
4. Do missions respect one main and two supporting slots, and do cancellation and timeout avoid a second charge or a stale reward?
5. Does every tooltip describe the player's outcome in plain words without printing internal component values beyond what the value budget allows?
6. Do AI weights prefer the actions part 9 names for each scenario, and does any action receive weight while invalid?

## Boundaries

Small local fixes inside the current task scope are allowed under the subagent skill.
Do not merge or remove decisions, change doctrine design or alter costs beyond tuning without an accepted decision.
Return the counts, findings with file and line, changed files and remaining risks.
