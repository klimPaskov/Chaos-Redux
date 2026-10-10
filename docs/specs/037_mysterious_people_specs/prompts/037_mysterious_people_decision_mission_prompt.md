# Prompt: Event 037 decisions and mission

Implement, then audit through `chaosx_decision_mission_auditor`, the Event 037 category from [Part 4](../specs/037_mysterious_people_spec_part_4_decisions_missions_and_ai.md).
Part 4 owns the category lifecycle, stances, actions, costs, mission, visibility budget, AI, and cleanup, and this prompt adds only the implementation and audit focus.
Use the `chaos-redux-decisions-missions` skill and the famine category's selected-state pattern as the local precedent.

## Implementation focus

- The header reads three values from the ledger variables in Part 2 and Part 3 and computes nothing itself.
- The hotspot list comes from the ledger's stored hotspots, never from a scan in the category.
- Civilian-factory commitment uses the vanilla timed-decision `civilian_factory_use` modifier, scaled between the Part 4 bounds by the target's unsettled newcomers.
- Project completion calls the ledger's settlement effects and never edits population.
- Requisition's stability cost and the mission failure use timed modifiers with localised names.
- Stances and actions with a blocked reason show one short custom tooltip, and implementation flags sit in `hidden_trigger`.

## Audit focus

- The visibility budget holds in every pressure stage and evolution.
- No action duplicates a Famine, Migration, or camp action, and none targets people by origin.
- Every cost has its texticon, and no action uses more than two spendable cost types.
- Projects fail closed on owner or controller change and on loss of normal civilian systems, without refunds.
- AI weights match the Part 4 rules, and the probability scenarios run before and after any weight change.
- Tooltips describe consequences in player language with no raw variables.

The auditor writes its handoff to `docs/plans/037_mysterious_people_plans/` with changed files, identifiers, before and after behaviour, checks, and remaining issues.
