# Decision and mission audit prompt for Event 028: Asteroid Incoming

Role: `chaosx_decision_mission_auditor`, or the parent acting under the same checklist.
The design is in [Part 6](028_asteroid_incoming_spec_part_6_decisions_and_missions.md), values in the [tuning matrix](028_asteroid_incoming_tuning_matrix.md), source in `common/decisions/028_asteroid_incoming_decisions.txt` and the Event 028 recovery effects and triggers.
Follow `CLAUDE.md` and the `chaos-redux-decisions-missions` skill.

## When to run

Run after any change to the recovery category, including an accepted proposal from README Open question 2 or the Part 4 mitigation revision.
Do not re-audit unchanged source.

## Checks

- The header shows at most the four values in Part 6, and each phase stays within its visible action cap.
- Each state action lists one highest-ranked affordable target, and blocked reasons are specific.
- No action has more than four spendable cost types; displayed cost equals the debit; reserve floors hold for players and AI.
- Every action has an `ai_will_do` path consistent with the Part 6 priority order.
- Missions start only for player governments, respect the two-mission limit and grace window, and fail or cancel exactly as Part 6 states.
- Cleanup and exploit rules in Part 6 hold after control change, annexation and dust clearing.
- Crater actions keep the garrison proxy, perimeter lapse and survey permanence.

Weighted changes go to the [AI prompt](028_asteroid_incoming_ai_probability_prompt.md).

## Handoff

List each decision and mission touched, the finding, any small patch made inside scope, meaningful validation and remaining risk.
Broad design changes return as a plan under `docs/plans/028_asteroid_incoming_plans/`, not as a patch.
