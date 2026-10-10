# Event 085 — Decision and Mission Implementation Prompt

Implement and audit the Ten Plagues decision and mission surface.
Read the README and Parts 2, 5–7, 10, 11, 14 and 15, then follow the repository rules and the `chaos-redux-decisions-missions`, `chaos-redux-events` and `chaos-redux-subagents` skills with the relevant offline wiki and installed documentation.
Tuning values are anchors to place in script constants, not verified engine behavior.

## Required surface

- One event category: Divine Wrath as the only event value, the current plague, the next deadline and the Passover line during Darkness; three to five visible actions, never more than six; at most three urgent Event 085 missions (Part 14).
- The fourteen families in Part 14 with their physically valid variants, each with full, partial and failure results, impossible-target handling, AI weights from Part 15, deadline behavior and cleanup.
- Famine, Migration, outbreak and Natural Disasters actions stay with their owners; link to them, never copy them.

## Costs

- Relief units of 250,000 people of the target state, rounded up; road, sea, rail and local-organization variants offered only where physically valid and never combined.
- Equipment is consumed; there is no reservation or return.
- The local-organization variant is a timed output penalty in the target state plus Political Power; it needs no factory minimum and never removes population or creates manpower.
- At most three displayed cost values with texticons; requirements such as routes shown separately.
- Use the existing stockpile-debit helpers, initializing each removal amount afresh because the helpers negate their input in place; holding exactly the shown amount is enough and nothing is debited when the action cannot start.

## Credit

- One full Wrath credit (−10) per country per phase, and only for a footprint state of the current plague; partial (−5) upgrades by the remaining −5 only.
- Foreign Relief Pledge credits the donor −5 when the recipient's objective completes, at most twice per phase.
- Abandonment of an achievable objective or diversion of its equipment raises Wrath; capture, route destruction and lost access do not.
- Passover: national program 48 hours (36 with a working response network), local preparation 24 hours; completion exactly at the deadline counts; the deadline never moves for a popup.

## Transfers and cleanup

Objectives close as partial or failed for the old controller when their state changes hands, without false completion.
At phase end unfinished objectives close with a result; at episode end only Event 085's own actions and records close.

## Review

Use `chaosx_decision_mission_auditor` for the action audit and `chaosx_ai_probability_auditor` for the Part 15 weights, with self-contained prompts.
An ordinary category needs no custom GUI.
Cover the Part 15 cases for exact-cost affordability, partial credit, donation loops, controller transfers, last-hour Passover and owner cleanup.
Return changed files, identifiers, the action and mission coverage, cost and requirement mapping, result and cleanup contracts, weight evidence and unresolved blockers.
