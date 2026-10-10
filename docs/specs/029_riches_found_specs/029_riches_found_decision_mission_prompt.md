# Event 029 decision and mission prompt

Use this prompt for the `chaosx_decision_mission_auditor` pass and for any agent continuing the Event 029 decision surface.

The design is owned by [Part 3](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md); this prompt only says what to check and what to hand back.

## Read first

- `CLAUDE.md` and `.claude/skills/chaos-redux-decisions-missions/SKILL.md`.
- `common/decisions/029_riches_found_decisions.txt`, its category file, the Event 029 triggers, cost triggers, and effects, and the two Event 029 decision localisation files.
- [Part 1, Presentation](029_riches_found_spec_part_1_core_loop.md#presentation), [Part 3](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md) in full, and the exploit rules in [Part 5](029_riches_found_spec_part_5_ai_balance_interactions.md#exploit-prevention).
- The cost contracts under `docs/events/029_riches_found/`.

## What to check

1. Layer budget: walk the nine layers in Part 3 and confirm no reachable flag combination shows more than six counted decisions or more than three missions, and that obsolete actions disappear when their layer, contract, target, controller, or crisis ends.
2. Header: the category description matches Part 1 and carries no deposit, policy, or revenue line.
3. Costs: at most four spendable types, construction committing civilian factories, inline rows of at most three values, full tooltips listing every cost and output loss, one shared affordability trigger for display, availability, payment, and AI, and exact refunds of discrete resources when a delayed result loses its mine.
4. Requirements: every flag and scripted trigger in an `available` block has a player label, and implementation-only checks are hidden behind a stated requirement.
5. Missions: each needs action after it starts, cannot complete from a condition already true at start, names its state or route, cancels or transfers safely on control loss, and cannot run twice for one mine and objective.
6. Transfer and cleanup: control loss cancels the old controller's missions and selections, removes its contribution, and keeps local values, damage, contracts, and history.
7. Exploits: the Part 3 exploit list, with special attention to closure and reopening loops, contract cycling, audit and compensation farming, and passive mission completion.
8. Tooltips follow [Part 6, Decision and mission writing direction](029_riches_found_spec_part_6_assets_localisation_achievements.md#decision-and-mission-writing-direction).

Route weighted surfaces to `chaosx_ai_probability_auditor` with the [named scenarios](029_riches_found_ai_probability_scenarios.md).

## Handoff

Write the handoff under `docs/plans/029_riches_found_plans/subagent_handoffs/` with:

- files changed and identifiers touched;
- the layer map with the largest reachable visible count per layer;
- the cost-type count and refund check per paid action;
- the mission objective, duration, and cleanup table;
- transfer, cleanup, and exploit findings with source lines;
- remaining blockers and what would resolve them.
