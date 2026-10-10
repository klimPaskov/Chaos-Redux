# Event 31 Random Terror decision and mission prompt

## Task

Finish the remaining Event 31 government-response and territorial-actor decision work.
Every decision and mission in the [matrix](031_random_terror_decision_mission_matrix.md) already exists in source.
This prompt names what is still open and where its requirement lives.

Read `CLAUDE.md`, the `chaos-redux-decisions-missions` skill, [Part 3](031_random_terror_spec_part_3_government_response_decisions_and_missions.md), the matrix, and the decision rows of [the completion audit](../../plans/031_random_terror_plans/subagent_handoffs/031_current_completion_audit_20261007.md).

## Open work

1. Terminal access (Part 8 World-end transition, C01): the government category and the Terminal Counteroffensive must stay visible after `world_end`. Keep the paid preflight checks of Security Surge and Targeted Raid as they are.
2. Hostage approach (Part 3 The Hostage Deadline): add the three approach options to the hostage report and feed them into the existing surge, raid and deadline outcomes. Add no decision.
3. Scaled costs (Part 3 Cost design, C09): costs that are fixed constants today should scale with country size, active-state count and pressure through the existing affordability triggers, so each cost line still matches one debit.
4. Maintained commitments (C09): Military Reinforcement, Isolate the Enclave, Protect Critical Transport and Secure Relief Corridor need a commitment that ends when its forces or access are gone, not only a timed flag.
5. Collective punishment through camps (Part 3 Coercive response): read camp facts for the government's crisis states.
6. Supply Collapse (Part 5): rename the actor economy failure form and wire Force Extraction to famine's extraction request.
7. Leadership contest (C05): compare the challenger with the current leader.
8. Absorption (C08): reconcile stockpiles, compatible technology and troops once.

## Rules that stay fixed

- Visible-action budgets and the six-action ceiling per phase from the matrix.
- At most four spendable cost types per action, icon-first cost text, and one inclusive affordability trigger per costed decision.
- One target row per decision through the priority crisis state (D8).
- Consent for any outcome that spends or changes another country's resources.
- No dedicated Event 31 GUI.

## Checks

Route changed weights through `chaosx_ai_probability_auditor` with before and after evidence on the matrix scenarios.
Run `chaosx_decision_mission_auditor` on the changed families before any completion claim.
Write subagent handoffs under `docs/plans/031_random_terror_plans/subagent_handoffs/`.
