# Coding Prompt for Event 018 Resources Found

Implement Event 018 according to the full planning package in `docs/specs/018_resources_found_specs/`.

Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `hoi4-decisions-missions`, `hoi4-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents`. Before editing, inspect the actual Chaos Redux repository, relevant offline Paradox wiki pages, vanilla HOI4 documentation, and vanilla precedents.

## Source files

Use all spec files, matrices, diagrams, prompts, research notes, and handoff files in this package as the source spec. Part 7 is the Cave Host focus blueprint. Part 8 is the scripted GUI wireframe. Part 9 is the super-event research handoff. Part 10 is the repo and spreadsheet handoff.

## Non-negotiables

- Baseline Event 018 remains Minor Repeatable and simple: a random valid state gets around 100 of one random resource.
- The owning country receives a popup and a decision category.
- The event belongs to economy positive cluster with medium severity.
- Diplomacy, trade interest, concessions, smuggling, and border crisis logic must exist.
- A border war can transfer the state when valid.
- The decision category must use meaningful costs, missions, values, staged visibility, AI, and cleanup.
- Evolution I adds larger deposits and international pressure.
- Evolution II adds sickness, worker deaths, corrosion, and cave incidents.
- Evolution III adds public monster attacks, evacuation, hunts, population loss, and closure.
- The site can still be closed before Evolution IV, removing event-added resources and preventing the Cave Host.
- Evolution IV creates the Cave Host, a nonhuman cave monster country with leader, flags, country package, focus tree, unique divisions, AI, and wars against neighbours.
- Cave Host divisions do not use manpower or equipment. They spawn automatically from captured resources: every 10 total resources in a controlled non-origin state gives 1 division, capped at 10 per state. Initial origin divisions are based on exploitation and capped around 30.
- Cave monster units are slow, heavily armored, and countered by severe hard attack.
- Cave Host must be registered as special chaos country and actual nonhuman country.
- Cave Host integrates with the shared world threat framework.
- World-end triggers when Cave Host owns enough of a continent at chaos over 1000, then stronger Cave Host appearances begin on other continents.
- Cave Host reveal, world-end, and conditional defeat aftermath need full super-event packages with researched text and licensed audio.
- Achievements, assets, docs, event log, evolutions, event details, and spreadsheet alignment must be completed.
- The Cave Host focus tree must map final focus ids to the Part 7 blueprint or report accepted renames, merges, or omissions.
- If the Part 8 scripted GUI is implemented, GUI buttons must call real decision logic and have AI equivalents.

## Required subagent and audit use

Use `chaosx_repo_explorer` if file locations or precedents are unclear. Use `chaosx_scripted_system_architect` for reusable resource field helpers, cave capacity refresh, event targets, dynamic resource addition, cleanup, and constants. Use asset and super-event subagents for visual and audio packages. Use decision, country, focus, localisation, and completion auditors before claiming completion. Use `chaosx_improvement_loop_planner` near completion with `fork_context=false` and resolve its addendum, queue it with reason, reject it with reason, or record closure before completion.

## Text and research rules

Write final localisation from the direction in the spec. Do not paste working labels as final player-facing text. Do not expose hidden cave mechanics in baseline event details. Treat unresearched super-event titles, button remarks, quotes, cultural allusions, slogans, and audio as blockers until the super-event workflow verifies them.

## Completion

Do not claim completion until the implementation satisfies the spec to the fullest extent. Report every simplification, omission, blocker, skipped asset, unresolved addendum, missing audit, or validation gap. Provide route coverage, decision coverage, country package coverage, asset coverage, super-event coverage, achievement coverage, AI coverage, and spreadsheet update status in the completion report.

## Canonical continuation addendum

Before implementation, read `specs/018_resources_found_spec_part_11_repo_confirmed_implementation_addendum.md`, `specs/018_resources_found_spec_part_12_verified_super_event_research.md`, and `research/018_resources_found_public_repo_exploration_handoff.md`.

The public GitHub pass found an old Event 018 implementation in `events/018_random_resource.txt` that adds 200 of one resource. Do not copy that old value as the baseline. The canonical baseline is around 100 of one random resource in one valid state. Treat 200-level and larger values as evolved, repeated, or exploited states only when the spec calls for them.

The local repo, offline Paradox wiki, vanilla HOI4 docs, final workbook, and subagent runner were not available to the planning environment. Repeat those checks locally before editing. Use the public repo handoff only as a map of likely current paths and risks.
