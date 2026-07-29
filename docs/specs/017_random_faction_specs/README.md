# Event 17 Random faction planning package

> Documentation reconciliation, 2026-07-29: the accepted implementation is recorded in [`docs/events/017_random_faction/overview.md`](../../events/017_random_faction/overview.md) and the PASS completion audit under `docs/plans/017_random_faction_plans/subagent_handoffs/`. The catalog's `Needs Testing` status is a live user-validation boundary, not evidence that the static implementation is absent. The planning-only environment note below is retained as historical intake context.

This package contains the full planning handoff for Chaos Redux Event 17 `Random faction`.

## Contents

- `specs/`: four-part source specification
- `matrices/`: AI matrix, decision map, scripted architecture, and catalog handoff
- `prompts/`: asset, achievement, decision, coding, goal, and subagent prompts
- `research/`: historical inspiration notes and source directions
- `source_review/`: manifest of uploaded project files read before writing the package

## Environment note

The custom Codex subagent runtime was not available in this chat environment. The package includes ready-to-use subagent prompts and routing notes for a Codex implementation pass that can spawn those agents with `fork_context=false`.

Historical planning-intake note: no gameplay files were edited while this package was authored. The current gameplay and audit state is documented by the implementation overview and completion handoff cited above.
