# Event 005 Northern Revenant Fleet Package

Audit date: 2026-05-21

## Overview

The Northern Revenant Fleet (`NRF`) is the direct high-chaos Arctic naval splinter required by the final clean merged Part 6 specification. It covers the port, fleet, naval militia, and revenant identity that the Arctic Naval Directorate (`ARD`) could only partially approximate.

## Gameplay Flow

`can_soviet_collapse_spawn_nrf` requires the high-chaos successor spawn gate, the northern port directorate setup flag, contested military obedience, high foreign appetite, and Soviet ownership/control of Murmansk (`213`) and Arkhangelsk (`214`). `soviet_collapse_spawn_nrf_if_enabled` transfers those states to `NRF`, cores them, applies collapse pressure, and calls `soviet_collapse_setup_nrf_successor`.

The setup effect marks `NRF` as a high-chaos successor, loads `NRF_soviet_collapse_focus_tree`, initializes revenant fleet authority and port muster variables, applies starting ideas, records the high-chaos event-log stage, and fires `chaosx.nr5_custom.42`. `NRF` is attempted before `ARD`, and `ARD` is gated against existing `NRF`, so the direct required package wins when both would otherwise qualify.

## Focus And Decision Content

The `NRF_soviet_collapse_focus_tree` has 18 focuses with political, industry, naval/military, diplomacy, expansion, and endgame branches. It splits between living harbor committees and a revenant admiralty, then develops icebound marines, ghost convoy escorts, sailor-town diplomacy, White Sea lane claims, and settlement or dead-fleet endgames.

The `soviet_collapse_northern_revenant_fleet` category includes:

- `nrf_recover_drowned_ship_logs`
- `nrf_raise_icebound_marines`
- `nrf_call_the_revenant_fleet`

The living harbor route hides raw `remove_ideas` output behind `nrf_living_harbor_committees_settle_drowned_crews_tt`.

## Icons And Assets

Required asset wiring:

- Flags: `gfx/flags/NRF.tga`, ideology variants, `medium/`, and `small/`.
- Leader portrait: `gfx/leaders/005_soviet_collapse/NRF_leader.dds`, sprite `GFX_portrait_NRF_dead_convoy_admiralty`.
- Focus icon package: `gfx/interface/goals/soviet_collapse/005_nrf_custom_splinter_focus.dds`, sprites `GFX_focus_NRF_*` and `GFX_focus_NRF_*_shine`.
- Idea icon package: `gfx/interface/ideas/soviet_collapse/005_nrf_custom_splinter_idea.dds`, sprites `GFX_idea_nrf_*`.
- Decision icon package: `gfx/interface/decisions/soviet_collapse/005_nrf_custom_splinter_decision.dds`, sprites `GFX_decision_nrf_*`.

The current DDS files are wired and present. The package still uses one generated tag emblem across the NRF focus tree, so distinct final per-focus art remains pending if final acceptance requires unique rendered art rather than unique sprite assignments that share one source texture.

## Validation Notes

Source validation for this package covers tag registration, country/history files, country localisation, setup/spawn effects, event-log stage mapping, custom event `chaosx.nr5_custom.42`, decision category and decisions, ideas, focus IDs, focus rewards, AI weights, localisation, sprite keys, and asset existence.

## Future Plans

- Replace the shared NRF focus-emblem texture with distinct final focus icons for each focus identity.
- Add deeper interaction between `NRF`, `KRS`, and `ARD` if the naval-council evolution is expanded.
- Add postwar White Sea lane settlement events for `215` and `722` if the broader high-chaos route pass expands Arctic border handling.
