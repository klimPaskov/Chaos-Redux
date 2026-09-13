# Prompt for `chaosx_focus_tree_auditor`

Work with no inherited conversation context. Audit and make only bounded local patches to the implemented Event 38 national focus surfaces.

Read `AGENTS.md`, `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and the complete Event 38 specs, especially `06_focus_tree_architecture.md`, `26_focus_route_matrix.md`, `27_country_package_matrix.md`, and `23_acceptance_scenarios.md`.

Use mandatory `hoi4.focus_inspect`, full-tree `hoi4.focus_render`, lint, and comparison evidence. When a safe bounded rewrite is required, use `hoi4.focus_rewrite`, then inspect and render again. Use the probability auditor rather than changing any weighted AI surface without a baseline and comparison cycle.

Audit:

- correct tree loading for Malta and each relevant cosmetic or shared country package
- lean opening and early route choice
- first-glance branch readability
- all required route families and route payoffs
- clean lane structure, symmetry, spacing, shortest connectors, no overlap, crossings, fake branches, or disconnected nodes
- exact prerequisites, AND and OR semantics, mutual exclusions, bypasses, reveal gates, crisis gates, and hidden-route secrecy
- Focus Navigation and hidden navigation behavior
- focus inlay placement if used
- focus duration and click value
- reward diversity, idea lifecycles, decisions, missions, units, leaders, laws, technologies, buildings, diplomacy, claims, cores, settlements, and map effects
- Holy See and Kingdom of God as normal routes
- Eleventh Crusade reveal and closure
- Teutonic, Atlantis, and Holy World reveal rules
- route-specific AI validity, but route weighted changes must use the probability audit cycle
- accurate search filters and icons
- localisation tone and visible requirement clarity
- branch closure and no weak dead ends
- country and principality route compatibility

Produce the route coverage table from `templates/route_coverage_template.md` and map every row in `26_focus_route_matrix.md` to final focus IDs. Patch small focus-local defects when safe. Write broad missing design as a plan and stop instead of inventing a route.

Write the handoff to `docs/plans/038_malta_crusaders_plans/subagent_handoffs/focus_tree_auditor.md`. Include changed focus IDs, files, MCP evidence, unresolved routes, missing assets, probability follow-up, and parent actions.
