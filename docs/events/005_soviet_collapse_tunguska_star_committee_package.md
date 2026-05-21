# Event 005 Tunguska Star Committee Package

## Overview

The Tunguska Star Committee is a high-chaos Siberian strange-science splinter for Event 005. It appears as `TSC` when the Soviet collapse has produced enough old-movement pressure and foreign appetite for remote field stations to become a political authority.

## Runtime Flow

1. `SOV` runs `soviet_collapse_maybe_spawn_high_chaos_successors`.
2. `can_soviet_collapse_spawn_tsc` requires high-chaos successor readiness, no existing `TSC`, high old movement pressure, foreign appetite above the league threat gate, and Soviet ownership/control of states 575 and 576.
3. `soviet_collapse_spawn_tsc_if_enabled` transfers Kirensk and Yeniseisk, records the high-chaos evolution stage, and calls `soviet_collapse_setup_tsc_successor`.
4. Setup loads `TSC_soviet_collapse_focus_tree`, seeds `tsc_signal_authority` and `tsc_anomaly_research`, adds the committee and field-station rivalry ideas, records the event-log evolution, and fires `chaosx.nr5_custom.38`.

## Gameplay

The focus tree has political, science-industrial, military, diplomatic, and high-chaos branches:

- Political branch: the Tura observation presidium, the Committee of Instruments, and the Committee of Signs.
- Science-industrial branch: Kirensk field stations, burned-glass recovery, radio towers, and portable laboratory trains.
- Military branch: observatory guards, perimeter regiments, and night survey columns.
- Diplomatic branch: letters to academies and league signal bargaining.
- Endgame branch: either the quiet observatory-state settlement route or the high-chaos Starfall Mandate route.

The decision category adds three actions:

- `tsc_secure_the_observation_posts`
- `tsc_mobilize_field_station_guard`
- `tsc_declare_the_starfall_mandate`

## Variables And Flags

- `tsc_signal_authority`: tracks the committee's ability to make readings and station orders politically binding.
- `tsc_anomaly_research`: tracks control over samples, radio records, and strange-science offices.
- `soviet_collapse_tunguska_star_successor`: marks the spawned country.
- `soviet_collapse_tunguska_star_endgame`: marks completion of either final route.

## Assets

Required and wired assets:

- Flags: `gfx/flags/TSC.tga`, `gfx/flags/medium/TSC.tga`, `gfx/flags/small/TSC.tga`
- Focus icon source DDS: `gfx/interface/goals/soviet_collapse/005_tsc_custom_splinter_focus.dds`
- Idea icon source DDS: `gfx/interface/ideas/soviet_collapse/005_tsc_custom_splinter_idea.dds`
- Decision icon source DDS: `gfx/interface/decisions/soviet_collapse/005_tsc_custom_splinter_decision.dds`
- Leader portrait: `gfx/leaders/005_soviet_collapse/TSC_leader.dds`
- Sprite definitions: `interface/005_soviet_collapse_custom_icons.gfx`

## Remaining Work

The gameplay package is wired, but the focus icons currently use the tag-specific generated TSC emblem for every TSC focus. This matches the current custom-splinter emblem workflow, but the final merged objective still calls for distinct focus icons on long-lived playable trees.
