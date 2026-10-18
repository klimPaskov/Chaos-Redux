# Fresh consumption receipt skill handoff

Disposition: implemented skill guidance, pending main-agent final review.
Acceptance basis: the requesting agent explicitly authorized this narrow reusable lesson and supplied the audited transaction failure and owner fix.

Changed paths:

- `.agents\skills\chaos-redux-events\SKILL.md`, one paragraph under `Helper output lifetime`, beginning at line 188.
- `docs\plans\039_murder_mystery_plans\subagent_handoffs\fresh_receipt_skill_handoff_2026_10_07.md`, this handoff.

The existing skill covered helper output lifetime, frozen transaction inputs, receipt identity, and repeated closure, but did not distinguish an already-consumed validator status from proof of consumption by the current invocation.
Updated `chaos-redux-events` rather than creating a separate skill, following `skill-creator` guidance for a narrow correction to an existing workflow.

Exact added rule:

> For record-consumption transactions, keep validator status such as "already used" or "tombstoned" distinct from a fresh receipt proving that this invocation consumed the exact row.
> Clear the fresh receipt immediately before the consumption attempt, set it only on the exact row mutation, and gate irreversible effects and compensation on that receipt so rejection cannot undo a pre-existing tombstone.
> Actual-source fixtures must exercise already-used or tombstoned rows, transitions to used or tombstoned between validation and consumption, and stale receipts from earlier calls, asserting no irreversible effect or rollback of prior state on rejection and exactly one authorized effect on fresh consumption.

Validation: the official `skill-creator\scripts\quick_validate.py` accepted the skill.
Removing only the added paragraph reproduced the captured pre-edit skill bytes exactly, including existing shared edits and line endings.
The skill's index entry remained `f8b342a6c106eae7af63e442ef1588a1aabd6364`, and this worker performed no index mutations or commits.
The paragraph contains no event identifiers, names, or implementation history.

No new skills were created, and all other skills, routing, AGENTS.md, gameplay files, and broad documentation were left untouched by this worker.
No simplifications, omissions, or blockers apply to this skill maintenance request.
The supplied gameplay audit was the basis for the lesson, and this worker did not independently validate the owner fix, execute transaction fixtures, or claim engine behavior proof.
The main agent owns final review, gameplay validation, and the isolated commit.
No AGENTS.md or subagent-routing update is needed.
