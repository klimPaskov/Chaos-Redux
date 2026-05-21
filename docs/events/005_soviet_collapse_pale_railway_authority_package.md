# Event 005 Pale Railway Authority Package

## Overview

The Pale Railway Authority is a high-chaos rail sovereignty splinter for Event 005. It appears as `PRA` when Soviet collapse pressure has made depots and old movement networks unstable enough for a rail state to claim authority around Novosibirsk and Omsk.

## Runtime Flow

1. `SOV` runs `soviet_collapse_maybe_spawn_high_chaos_successors`.
2. `can_soviet_collapse_spawn_pra` requires high-chaos successor readiness, no existing `PRA`, high depot vulnerability, high old movement pressure, and Soviet ownership/control of states 570 and 571.
3. `soviet_collapse_spawn_pra_if_enabled` transfers Novosibirsk and Omsk, records the high-chaos evolution stage, and calls `soviet_collapse_setup_pra_successor`.
4. Setup loads `PRA_soviet_collapse_focus_tree`, seeds `pra_rail_authority` and `pra_rolling_stock`, adds the timetable board and dispatcher tension ideas, records the event-log evolution, and fires `chaosx.nr5_custom.37`.

## Gameplay

The focus tree has political, industrial, military, diplomatic, and expansion branches:

- Political branch: station courts, timetable law, civilian board authority, and moving-state identity.
- Military branch: Omsk station guards, switchyard denial posts, armored train schools, and junction-city pressure.
- Industry branch: locomotive inventory, repair crews, fuel and spare parts, and mobile workshops.
- Diplomacy branch: corridor letters, safe-passage tolls, and local league transit bargaining.
- Endgame branch: either the settlement route `PRA_the_pale_line_endures` or the extreme route `PRA_rails_over_capitals`.

The decision category adds three repeatable/state-defining actions:

- `pra_consolidate_timetable_courts`
- `pra_mobilize_station_guard`
- `pra_declare_the_moving_state`

## Variables And Flags

- `pra_rail_authority`: grows through court, law, and branch-line focuses and gates AI preference for consolidation.
- `pra_rolling_stock`: tracks train and yard control from setup, decisions, and logistics focuses.
- `soviet_collapse_pale_railway_successor`: marks the spawned country.
- `soviet_collapse_pale_railway_endgame`: marks completion of either final route.

## Assets

Required and wired assets:

- Flags: `gfx/flags/PRA.tga`, `gfx/flags/medium/PRA.tga`, `gfx/flags/small/PRA.tga`
- Focus icon source DDS: `gfx/interface/goals/soviet_collapse/005_pra_custom_splinter_focus.dds`
- Idea icon source DDS: `gfx/interface/ideas/soviet_collapse/005_pra_custom_splinter_idea.dds`
- Decision icon source DDS: `gfx/interface/decisions/soviet_collapse/005_pra_custom_splinter_decision.dds`
- Leader portrait: `gfx/leaders/005_soviet_collapse/PRA_leader.dds`
- Sprite definitions: `interface/005_soviet_collapse_custom_icons.gfx`

## Remaining Work

The gameplay package is wired, but the focus icons currently use the tag-specific generated PRA emblem for every PRA focus. This matches the current custom-splinter emblem workflow, but the final merged objective still calls for distinct focus icons on long-lived playable trees.
