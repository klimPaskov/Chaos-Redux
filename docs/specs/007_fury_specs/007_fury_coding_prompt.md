# Coding Prompt for Event 007 Fury

Implement Chaos Redux Event 007, Fury, according to the full source spec pack under:

- docs/specs/007_fury_specs/007_fury_spec.md
- docs/specs/007_fury_specs/007_fury_focus_tree_spec.md
- docs/specs/007_fury_specs/007_fury_decisions_missions_spec.md
- docs/specs/007_fury_specs/007_fury_country_packages.md
- docs/specs/007_fury_specs/007_fury_ai_matrix.md
- docs/specs/007_fury_specs/007_fury_asset_plan.md

Also follow the prompt files in `prompts/`.

Core implementation requirements:

- Event 7 remains minor repeatable and belongs to the Wars cluster.
- Replace the old expansionism placeholder behavior.
- Select dynamic AI-only small non-island minors with valid AI land neighbors.
- Never make a player country Fury.
- Never select a player country as scripted Fury target.
- Give Fury dynamic starting units and weekly reinforcement while active.
- Make Fury declare without warning on weaker AI land neighbors.
- After each victory, choose another valid weaker AI land neighbor and repeat.
- If no neighbors remain, enter no-neighbor branch.
- If Fury capitulates, clean up flags, decisions, missions, event targets, variables, and pulses.
- Add first-victory news event.
- Add Fury major super-event trigger and world-end super-event trigger.
- Implement three evolutions exactly as the spec defines them.
- Implement the decision and mission layer with dynamic costs, active caps, AI behavior, and cleanup.
- Implement shared focus tree or additive runtime branch with route depth, varied rewards, icons, localisation, route AI, focus filters, and route coverage reporting.
- Implement compliance and coring through staged integration, not instant free core spam.
- Implement Fury Pact and cooperation from Evolution II onward.
- Implement all-front declarations for Evolution III.
- Implement world-end branch only when the required threshold and state conditions are met.
- Update event log, event details, localisation, docs, assets, super-events, achievements, and the event catalog workbook.

Use AGENTS.md and these skills:

- chaos-redux-events
- chaos-redux-event-planning
- hoi4-focus-trees
- hoi4-decisions-missions
- chaos-redux-event-assets
- chaos-redux-super-events
- chaos-redux-subagents
- chaos-redux-improvement-loop if a design gap appears during implementation

Validation:

Run or document checks for player exclusion, target validity, repeatability, unit farming, coring abuse, focus route coverage, AI route validity, event log alignment, localisation, docs, assets, and spreadsheet alignment.

Do not claim completion until every requested surface is implemented or every missing piece is reported under simplifications, omissions, and blockers.
