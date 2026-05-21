# Red Martyrs' Resurrection Cult Package

## Overview

The Red Martyrs' Resurrection Cult is an Event 005 high-chaos successor for the required death or martyr cult slot. It forms from Tambov (`257`) and Lipetsk (`258`) when high-chaos successor spawning is ready, old-movement pressure is high, and Soviet military obedience has fallen below contested-authority levels.

The tag is `RMC`. Its leader is the Council of Red Witnesses, using the generated leader portrait at `gfx/leaders/005_soviet_collapse/RMC_leader.dds`.

## Runtime Flow

1. `SOV` checks `can_soviet_collapse_spawn_rmc`.
2. `soviet_collapse_spawn_rmc_if_enabled` transfers Tambov (`257`) and Lipetsk (`258`) to `RMC`.
3. `soviet_collapse_setup_rmc_successor` applies the breakaway setup, loads `RMC_soviet_collapse_focus_tree`, adds the starting spirits, records the high-chaos event-log stage, and fires `chaosx.nr5_custom.40`.

## Focus Tree

`RMC_soviet_collapse_focus_tree` has 18 focuses. It covers:

- opening martyr-roll authority
- Tambov witness cells
- Lipetsk reliquary workshops
- witness-commune settlement route
- resurrection-cadre hardline route
- reliquary guard and dead volunteer columns
- shrine foundries and requisitions
- mourning-town diplomacy and league preparation
- burial-road claims and procession expansion
- settlement and extreme endgame outcomes

## Decisions And Ideas

Decision category: `soviet_collapse_red_martyrs_resurrection_cult`

Decisions:

- `rmc_collect_martyr_testimonies`
- `rmc_raise_reliquary_guard`
- `rmc_proclaim_resurrection_communes`

Ideas:

- `rmc_red_martyrs_resurrection_cult`
- `rmc_credal_cell_rivalries`
- `rmc_martyr_roll_communes`
- `rmc_reliquary_guard`
- `rmc_resurrection_militias`

## Assets

Existing generated assets are wired:

- Flag set: `gfx/flags/RMC.tga`, `gfx/flags/medium/RMC.tga`, `gfx/flags/small/RMC.tga`, plus ideology variants
- Focus icon: `gfx/interface/goals/soviet_collapse/005_rmc_custom_splinter_focus.dds`
- Idea icon: `gfx/interface/ideas/soviet_collapse/005_rmc_custom_splinter_idea.dds`
- Decision icon: `gfx/interface/decisions/soviet_collapse/005_rmc_custom_splinter_decision.dds`
- Portrait: `gfx/leaders/005_soviet_collapse/RMC_leader.dds`

The current focus tree uses stable per-focus sprite names that all reference the tag-specific RMC focus DDS. Distinct final per-focus art remains an asset-completion task if the final pass requires each focus to use separate DDS art rather than stable sprite keys over shared generated art.

## Validation Notes

Source checks should verify tag registration, history setup, country localisation, ideology localisation, spawn trigger/effect wiring, event-log mapping, focus count, focus localisation, idea localisation, decision localisation, GFX sprite presence, and BOM encoding for localisation files.
