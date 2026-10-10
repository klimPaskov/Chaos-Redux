# Event 32 coding-agent prompt

## Goal

Finish Event 32, Missiles, against the design in `docs/specs/032_missiles_specs/`.
Most of the event is already implemented in source; this prompt covers the remaining work and the rules for touching what exists.

## Read first

1. `README.md` in this package: status table, acceptance basis, open questions.
2. `docs/events/032_missiles.md`, `docs/events/032_missiles/overview.md` and the notes in `docs/events/032_missiles/systems/`.
3. `docs/plans/032_missiles_plans/agent_decisions_2026-10-04.md` and the later dated plan files, which record accepted implementation decisions.
4. The spec part that owns the surface you will change.
5. `CLAUDE.md` and the skills it routes to for the surface (`chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`).

Other sessions may have uncommitted edits in Event 32 files; read the working tree, keep their changes, and commit only your own hunks (`chaos-redux-shared-git-commit`).

## Remaining work

Each item names its owning section; implement the owning section, not this summary.

- Reach against real distance: part 3, Reach.
- Territory-scaled site cap from the unused `site_count_*` constants: part 2, Site count cap.
- Denial exposure when attribution is later confirmed: part 5, Deny responsibility.
- Event 52 fuel-crisis slowdown: system connections, Event 52.
- Probability evidence by source-derived calculation for every weighted surface in part 6, Required audit surfaces, using the named scenarios; MCP probability routes are `blocked` by repeated `INTERNAL_ERROR`.
- Asset workspace cleanup: part 7, Asset paths.
- Catalog status promotion once the above close: `docs/plans/032_missiles_plans/catalog_changes_pending.md`.

Do not implement the `unresolved` items (Chaos budgets, humanitarian aftermath, the README open questions) until the user or parent accepts them.

## Rules for existing behaviour

- Preserve accepted implemented behaviour unless the owning section changes it; record any new decision with its basis in the plans folder.
- Keep the one-category presentation with no dedicated scripted GUI (explicit user instruction).
- Keep the scripted operation adapter; do not add a native raid route or raid icon (part 8, Operation adapter).
- Keep every bound: no recurring all-country scan, bounded retaliation chains, exact reserve and payload custody, no direct recursive launch.
- Event 32 owns no world-end branch and grants no payload, technology or stockpile beyond its missile line.

## Validation and reporting

Use MCP routes only when they answer a concrete question, under the CLAUDE.md retry limit.
Source review and the `.tools/test_event32_*.py` suites support completion; never report them as live engine evidence.
Live-game testing belongs to the user; add new live cases to `032_missiles_test_matrix.md`.
Update the event doc, the README status table and the workbook (then run `python .tools/export_event_catalog_csv.py`) in the same change as the behaviour.
Report every simplification, fallback, blocker and unrun check.
