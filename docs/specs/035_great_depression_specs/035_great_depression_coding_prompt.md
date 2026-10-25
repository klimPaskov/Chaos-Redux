# Event 35 Great Depression 2.0 coding continuation prompt

Continue the Event 35 implementation in the Chaos Redux repository.
Event 35 already has a substantial runtime implementation; this prompt covers the remaining work only.

## Read first

- The [package README](035_great_depression_spec_index.md), especially Implementation status, Acceptance basis and Decisions.
- The owning spec part for each item you touch; do not rely on this prompt for design detail.
- `docs/events/035_great_depression.md` and the companion `common/scripted_effects/035_great_depression_*.md` files for the implemented contract.
- `docs/plans/035_great_depression_plans/current_requirement_state_2026-10-07.md` for the current evidence boundary.
- `CLAUDE.md` and the skills it names for events, decisions and missions, scripted systems and probability work.

## Remaining work

Work only from the README's pending rows, in this order unless the parent decides otherwise:

1. Build the lasting physical result of Convert Works into Lasting Capacity (part 3, Doctrine 1).
2. Add the disaster adapter as a read-only owner check (part 8, Connections) and join Event 50 to the sanction read when it ships.
3. Produce source-derived probability calculations for the named scenarios that MCP could not evaluate (part 9), including the merged actions.
4. Clean up the asset workspace when the event is otherwise complete (part 10).

The inherited hidden-row work is `rejected`; do not implement it.
Re-run `.tools/tests/test_event035_visible_actions.py` after any change to a decision, its visibility or a phase.

## Rules for this work

- Keep Severity the only public number and respect the player-facing value budget in part 2.
- Use the existing start-or-deepen API, receipts, registries and constants; add tuning only to `common/script_constants/035_great_depression_constants.txt`.
- Keep owner boundaries: famine, migration, Event 21, condemnation, Event 50, disaster and contamination owners keep their own state and deaths.
- Write player-facing text in the style of the `chaos-redux-events` skill.
- Route weighted-logic changes through `chaosx_ai_probability_auditor` and decision changes through `chaosx_decision_mission_auditor`, with fully explicit prompts as the subagent skill requires.
- Update the event doc, the README status table and the plans ledger in the same change, and queue catalog wording in `catalog_changes_pending.md`.

## Report

Return the changed files, identifiers, task-specific validation, and every simplification, omission or blocker.
