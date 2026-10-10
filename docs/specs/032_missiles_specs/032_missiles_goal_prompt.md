# /goal: Finish Event 32, Missiles

Finish Event 32 against `docs/specs/032_missiles_specs/`.
Start with the package README status table and open questions, then `docs/events/032_missiles.md`, `docs/events/032_missiles/systems/`, and the dated decisions in `docs/plans/032_missiles_plans/`.
Follow CLAUDE.md and the skills it routes to.

Most of the event is implemented in source: the global firing transaction, program values, technology adapter, launch sites and custody, operations, special-payload holds, five evolution tracks on native MTTH clocks, the decision category and missions, SCN-015, assets, achievements and Event Logs.
Treat that behaviour as accepted unless an owning spec section says otherwise.

Close the remaining items listed in `032_missiles_coding_prompt.md`, Remaining work: real-distance reach, the territory-scaled site cap, denial exposure, the fuel-crisis slowdown, source-derived probability evidence for every weighted surface, asset workspace cleanup, and the catalog status promotion.
Implement each from its owning spec section.
Do not implement `unresolved` proposals (Chaos budgets, humanitarian aftermath, README open questions) unless the user accepts them.

Keep the explicit user presentation rule: one ordinary category with a static picture and no dedicated scripted GUI.
Keep the scripted operation adapter, the bounded retaliation chain, exact reserve and payload custody, and the ban on recurring all-country scans.
Event 32 owns no world-end branch.

Other sessions may have uncommitted Event 32 edits; preserve them and commit only your own hunks.
Spawn project subagents with fully self-contained prompts and no inherited context.
Use MCP only for concrete questions under the CLAUDE.md retry limit, and never present source review as engine evidence.
Live-game testing belongs to the user.

Update the event doc, README status table, test matrix and workbook with each change, then regenerate the CSV exports with the repository exporter.
Do not claim completion while any listed item remains open, and report every simplification, fallback, blocker and unrun check.
