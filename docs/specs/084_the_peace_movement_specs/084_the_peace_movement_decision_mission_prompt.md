# Implement and audit Event 84 decisions and missions

Use the source package under `docs/specs/084_the_peace_movement_specs/`, especially Parts 2, 3, 4, 5, 6, 8, 9, 10, 11, and 12, the modifier precedence, the [decision and mission matrix](084_the_peace_movement_decision_and_mission_matrix.md), the AI matrix, and the acceptance scenarios.
Read `CLAUDE.md` and the current `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-subagents` skills, then the existing helpers and consumers before writing code.

## Contract

- 33 actions and 17 mission types on contextual native category pages.
  At most six primary actions and three active Event 84 missions per country across all categories.
  Navigation spends nothing and changes nothing.
- The retired choices listed in the matrix stay inside their owning events or start automatically; do not reintroduce them as buttons.
- Two public values only, Influence and Reaction.
  At most four spend types per action, CP at most 50, capacity-scaled commitments frozen at acceptance, and no negative stockpiles.
- Missions complete when their objective is met, or after their stated maintenance period.
  Full success, partial success, failure, and cancellation are distinct; partial success is a real delivered subset.
  Use the matrix durations: 90-day local reform, 120-day convention, 150-day supply charter, 180-day major programs, 30-day command crisis.
- Material is consumed or reserved once.
  Cancellation releases only undelivered commitments and preserves spent PP, delivered equipment, losses, completed infrastructure, legal reforms, and population.
  Posture cycling, appointments, conversions, case reopening, leadership rotation, and same-cause suppression cannot farm rewards.
- The four special unit families stay behind Armed Peace except the explicit manual setup.
- Character cases follow evidence and consent; no orientation-based penalty or unsupported real-person private identity.
- Foreign projects share the mission budget and a bounded contact slot.
  Asylum and relief use the migration and famine decisions named in Part 12 rather than parallel transactions.
- Terminal checks keep the strict >1000 Chaos and >50% living population tests; manual previews and seeds pay no achievements or retrospective Chaos.

## Checks

Route `chaosx_decision_mission_auditor` and `chaosx_ai_probability_auditor` through `chaos-redux-subagents` with self-contained prompts.
Use `hoi4.probability_*` where it supports the script and calculations from the actual script otherwise; `ai_will_do` is a score, not a click probability.
Review every page at maximum simultaneous eligibility, every cost band and shortage boundary, partial, failed, and canceled outcomes, 30-day review proration, three simultaneous missions, target loss, government transfer, save and reload, and multiplayer commitments.
Return a route coverage table, the changed files, and remaining blockers; a listed action or mission result with only a placeholder path is not complete.
