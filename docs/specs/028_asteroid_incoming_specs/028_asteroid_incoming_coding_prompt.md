# Coding prompt for Event 028: Asteroid Incoming

Event 028 is implemented and enabled; this prompt covers only the remaining work.
Read the [package README](028_asteroid_incoming_spec_index.md) first: it owns the explicit user requirements, the implementation status table and the open questions.
Then read the [Event 028 overview](../../events/028_asteroid_incoming/overview.md) and the [current resume](../../plans/028_asteroid_incoming_plans/resume_20261007.md) for current source behaviour and open gates.
Follow `CLAUDE.md` and the `chaos-redux-events`, `chaos-redux-decisions-missions` and `chaos-redux-subagents` skills.

## Scope

Work only on items whose status is pending, blocked or proposed and whose proposal the parent or user has accepted.
Do not reopen implemented behaviour that the status table marks as implemented, and do not implement an unaccepted proposal.

| Item | Owning part | Precondition |
| --- | --- | --- |
| Main-crater railway, supply-node and queue handling | Part 3 | User decision on Open question 1 and the live result of validation scenario 15 |
| Remove the temporary `asteroid_incoming_forecast_delivery_count` | Part 8 | Live L1 result |
| Mission failure simplification | Part 6 | Parent acceptance of Open question 2 |
| Global mitigation through the Observation Network only | Part 4 | Parent acceptance |
| Famine adapter call | Parts 1 and 3 | Parent acceptance and a famine-owned adapter |
| Camp-site reconciliation | Part 3 | Parent acceptance and the camp owner's seam |
| Chooser condemnation context | Part 1 | Parent acceptance and the condemnation owner |
| Suitability-weighted country draw | Part 2 | Parent acceptance and a probability check |
| Fragment marker cleanup | Part 5 | Parent acceptance |
| Friendly-ground exposure of guarantees and non-aggression partners | Part 7 | Decision on Open question 5 |
| "on [continent]" wording in `chaosx.news.30.d` and `chaosx.nr28.2.d` | Part 8 | None; localisation fix |
| Event 029 mine reconciliation | Part 3 | Acceptance with the Event 029 owner |

Cross-owner items are implemented by their owners; Event 028 supplies only the documented inputs.

## Rules for every change

- Tuning values go in the Event 028 constants file; idea values stay mirrored as `@` constants.
- Every changed `ai_will_do` or `ai_chance` needs the before-and-after probability comparison described in the [AI prompt](028_asteroid_incoming_ai_probability_prompt.md).
- Keep the nuclear-separation rules in Part 3 intact.
- Update the overview, the status table in the README, and localisation in the same change.
- Use project subagents with self-contained prompts as routed by `chaos-redux-subagents`; the parent owns integration and completion claims.

## Completion

Report files changed, the items closed, task-specific validation, and every remaining blocker or simplification.
Native validation belongs to the user.
