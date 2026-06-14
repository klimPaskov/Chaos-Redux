# Coding Prompt: Implement Event 008 Tensions Rising

Implement the Event 008 `Tensions Rising` rework according to the source spec package:

- `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_spec.md`
- `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_evolutions_and_hidden_effects.md`
- `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_event_log_and_localisation.md`
- `docs/specs/008_tensions_rising_specs/matrices/008_tensions_rising_constants_and_helpers.md`
- `docs/specs/008_tensions_rising_specs/matrices/008_tensions_rising_ai_matrix.md`
- `docs/specs/008_tensions_rising_specs/matrices/008_tensions_rising_cluster_and_achievements.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-event-assets`, and the relevant offline HOI4 wiki/vanilla docs for implementation syntax.

## Required behavior

- Event ID remains `8` and type remains Minor Repeatable.
- Baseline Calm World firing: `+100` world tension and only fires while world tension is below `100%`.
- Stage I at Gathering Storm: `+10 chaos`, `+100` world tension, can fire at `100%` WT, adds light hidden side effects.
- Stage II: `+15 chaos`, `+200` world tension, stronger hidden side effects.
- Stage III: `+25 chaos`, `+500` world tension, heavy hidden side effects.
- Stage IV: `+50 chaos`, `+1000` world tension, severe hidden side effects.
- No super-event or world-end scenario. Never set `world_end` from Event 8.

## Hidden systems

Implement or cleanly plan:

- capped temporary Tension Pulse integrated with existing event timer logic, no new global daily/weekly/monthly loop
- relation-pair selection with timed opinion modifiers and cooldowns
- delayed follow-up report/news events
- optional `Diplomatic Panic` cluster if it can be fully registered and logged with the current member note: for now one member, Event 8, required, medium severity
- AI posture pressure via valid existing routes only, no direct forced wars

## Presentation

- Wire event log name, debug name, event detail, evolution detail, history, and evolution rows.
- Add stage-aware popup/report text and delayed follow-up text.
- Route assets through the asset prompt and wire final DDS files only after handoff.
- Implement achievements from the achievement prompt if the achievement system is in scope, otherwise queue them explicitly.

## Validation and completion

Use task-specific validation, not boilerplate claims. Verify stage gating, WT=100 behavior, pulse replacement/cap, timed opinion cooldowns, delayed report non-recursion, event log/evolution details, and absence of super-event, world-end, or direct war-goal behavior.

Before claiming completion, run a completion audit or equivalent review. Report files changed, systems touched, implemented vs queued pieces, asset status, spreadsheet status, validation evidence, and every simplification or blocker. Do not claim completion with missing localisation, unwired assets, skipped achievements, unlogged evolutions, or unreported queued cluster work.
