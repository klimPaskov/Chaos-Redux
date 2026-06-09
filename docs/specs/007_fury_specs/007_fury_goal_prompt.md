/goal Implement Chaos Redux Event 007, Fury, to the fullest extent from the source spec pack.

Read first:
- docs/specs/007_fury_specs/007_fury_spec.md
- docs/specs/007_fury_specs/007_fury_focus_tree_spec.md
- docs/specs/007_fury_specs/007_fury_decisions_missions_spec.md
- docs/specs/007_fury_specs/007_fury_country_packages.md
- docs/specs/007_fury_specs/007_fury_ai_matrix.md
- docs/specs/007_fury_specs/007_fury_asset_plan.md
- docs/specs/007_fury_coding_prompt.md
- docs/specs/007_fury_asset_prompt.md
- docs/specs/007_fury_super_event_prompt.md
- docs/specs/007_fury_achievement_prompt.md
- docs/specs/007_fury_decision_mission_prompt.md
- docs/specs/007_fury_focus_tree_prompt.md

Follow AGENTS.md plus chaos-redux-events, hoi4-focus-trees, hoi4-decisions-missions, chaos-redux-event-assets, chaos-redux-super-events, chaos-redux-subagents, and chaos-redux-improvement-loop if a real design gap appears.

Non-negotiables:
- Event 7 stays minor repeatable and belongs to the Wars cluster.
- Replace the old expansionism placeholder.
- Select dynamic AI-only small non-island minors with valid AI land neighbors.
- The player must never become Fury.
- Player countries must never be selected as scripted Fury targets.
- Fury gets dynamic starting units and weekly reinforcement only while active and valid.
- Fury declares without warning on weaker AI land neighbors, then repeats after victories.
- No valid neighbors means the no-neighbor branch, not fake wars.
- Capitulation must clean up Fury flags, decisions, missions, targets, variables, and pulses.
- First-victory news, Fury major super-event, three evolutions, Fury Pact cooperation, Evolution III all-front declarations, and tightly gated world-end branch must be implemented.
- Shared Fury focus tree or additive branch must have real route depth, route AI, varied rewards, focus-decision integration, icons, localisation, focus filters, and route coverage proof.
- Decisions and missions must use concrete costs and objectives, not political power or command power stores.
- Compliance and coring must be staged and cannot become free core spam.
- Assets, docs, event log, super-event research, achievements, and event catalog workbook must align with final implementation.

Keep iterating until the goal is complete. Do not claim completion until the implemented files satisfy the spec. Final report must list changed files, validations, route coverage, balance and exploit checks, assets, docs, spreadsheet updates, and every simplification, omission, or blocker. If nothing was simplified, say so with evidence.
