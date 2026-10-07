# Event 17 Random faction planning package

> Documentation reconciliation, 2026-07-29: the accepted implementation is recorded in [`docs/events/017_random_faction/overview.md`](../../events/017_random_faction/overview.md) and the [2026-07-11 completion audit](../../plans/017_random_faction_plans/subagent_handoffs/017_random_faction_event_completion_audit_handoff.md).
> Its `PASS` is dated checkpoint evidence, not fresh engine or asset validation. The catalog's `Needs Testing` status is a live user-validation boundary, not evidence that the static implementation is absent. The planning-only environment note below is retained as historical intake context.

This package contains the full planning handoff for Chaos Redux Event 17 `Random faction`.

## Contents

- `specs/`: four-part source specification
- `matrices/`: AI matrix, decision map, scripted architecture, and catalog handoff
- `prompts/`: original asset, achievement, decision, coding, goal, and subagent task contracts.
  Choose continuation from the dated implementation overview and audit cited above before scheduling work.
  These contracts do not authorize repeating completed tranches.
- `research/`: historical inspiration notes and source directions
- `source_review/`: manifest of uploaded project files read before writing the package

## Historical planning environment

The original planning environment lacked the custom subagent runtime.
That limitation does not establish current service health or outstanding implementation work.
Use [the routing owner skill](../../../.agents/skills/chaos-redux-subagents/SKILL.md) for any new bounded pass, with `fork_turns="none"` and explicit inputs in Codex.

Historical planning-intake note: no gameplay files were edited while this package was authored. The current gameplay and audit state is documented by the implementation overview and completion handoff cited above.
