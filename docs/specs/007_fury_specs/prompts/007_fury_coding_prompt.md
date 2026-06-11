# Coding prompt for Event 007 Fury

Implement Event ID `7`, Fury, according to this planning package.

Source folder:

`docs/specs/007_fury_specs/`

Primary files:

- `specs/007_fury_spec_part_1_core.md`
- `specs/007_fury_spec_part_2_evolutions_world_end.md`
- `specs/007_fury_focus_tree_spec.md`
- `specs/007_fury_decisions_missions_spec.md`
- `specs/007_fury_triggerable_scenario_spec.md`
- `specs/007_fury_achievements_spec.md`
- `matrices/007_fury_country_package_matrix.md`
- `matrices/007_fury_ai_balance_matrix.md`
- `acceptance/007_fury_acceptance_criteria.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-improvement-loop`.

## Core implementation requirements

- Replace obsolete expansionism behavior with Fury.
- Keep Event 007 as minor repeatable.
- Put Fury in the Wars cluster.
- Select a dynamic small mainland AI minor with few states.
- Exclude player countries from Fury selection.
- Allow ordinary Fury target selection to choose AI or player-controlled countries when they meet the normal target gates.
- Give Fury a national spirit, shared focus tree, decisions, an initial army package, a finite hidden reinforcement reserve, and dynamic target loop.
- Fury attacks weaker eligible neighbors without warning.
- Fury repeats after victory until no valid neighbor remains or Fury capitulates.
- Fire a news event when Fury defeats its first neighbor.
- Fire a super-event when the first Fury country becomes a major.
- Add compliance on captured territory and coring decisions with concrete costs.
- Add active cleanup for capitulation and invalid targets.

## Evolutions

Implement:

- Evolution I, Hardened Fury, with stronger starting units, better reserve-spawned unit quality, a larger capped reserve pool, better idea, and unlocked focus paths.
- Evolution II, Two Fires, with two Fury actors and cooperation or rivalry mechanics.
- Evolution III, All Borders at Once, with three Fury actors, stronger openings, capped reserve-spawned units, and all-neighbor declarations.

Each evolution needs active-event behavior and pre-fire opening behavior.

## Triggerable scenario

Implement scenario `The World in Fury`.

- four intensity stops.
- type choices: Fury Pact and Hostile Fury.
- player always excluded.
- Low creates 2 when safe.
- Medium creates 5 when safe.
- High creates 9 when safe.
- Maximum creates up to 16 when enough safe AI minors exist.
- intensity controls initial army size, reserve pool size, and evolution setup. It must not create infinite spawning.
- type controls pact or hostile behavior.
- scenario has no normal chaos or prior-event prerequisite.

## World-end

Implement terminal Fury branch if world-end systems are in scope.

- separate from triggerable scenario.
- requires terminal eligibility.
- main Fury faction.
- Fury actors seeded in other continents.
- seeded Fury actors join the main Fury faction.
- world-end super-event.
- Fury world threat source.
- player warning before terminal rules can threaten player-linked countries.

## Focus tree

Implement shared Fury focus tree with the required branches:

- opening trunk.
- internal Fury.
- Army of the March.
- expansion.
- occupation and integration.
- cooperation.
- rivalry.
- Evolution I.
- Evolution III.
- world-end.

Use varied rewards, real branch payoffs, AI weights, focus filters, icons, localisation, and decisions. Avoid a linear reward ladder.

## Decisions and missions

Implement Fury War Office and anti-Fury response. Use dynamic costs and map objectives. Avoid political power only designs.

## Assets, super-events, achievements, docs

Use the prompt files in `prompts/`.

- create or wire assets.
- research quote, button text, and audio before final super-event completion.
- implement achievements or report queued items.
- update docs and event catalog spreadsheet.
- produce a completion report with files changed, validation scenarios, and simplifications.

Do not claim completion while any requested route, evolution, scenario option, focus branch, decision family, super-event, achievement, asset, AI behavior, or documentation surface is missing without a clear blocker report.
