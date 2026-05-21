# Iron Commissariat of the Dead Package

## Overview

The Iron Commissariat of the Dead is an Event 005 high-chaos successor for the required rogue Soviet death-state authority slot. It forms from Ryazan and Penza when high-chaos successor spawning is ready, old-movement pressure is high, and Soviet military obedience has fallen below contested-authority levels.

The tag is `ICD`. Its leader is the Dead Roll Commissariat, using the generated leader portrait at `gfx/leaders/005_soviet_collapse/ICD_leader.dds`.

## Runtime Flow

1. `SOV` checks `can_soviet_collapse_spawn_icd`.
2. `soviet_collapse_spawn_icd_if_enabled` transfers Ryazan (`254`) and Penza (`255`) to `ICD`.
3. `soviet_collapse_setup_icd_successor` applies the breakaway setup, loads `ICD_soviet_collapse_focus_tree`, adds the starting spirits, records the high-chaos event-log stage, and fires `chaosx.nr5_custom.39`.
4. `soviet_collapse_complete_iron_commissariat_endgame` marks the high-chaos doctrine endpoint and increases Soviet collapse pressure through military obedience failure and old-movement pressure.

## Focus Tree

`ICD_soviet_collapse_focus_tree` has 18 focuses:

- Political route: dead-roll authority, Ryazan grave offices, absent-citizen census, and a settlement fork around last-address commissars.
- Industry route: Penza memorial workshops, black-seal requisitions, and the Dead Roll Supply Bureau.
- Military route: funeral guard, memorial battalions, front archives, unburied-front claims, and grave columns.
- Diplomacy and league route: letters to grieving cities and the League of Last Addresses.
- Endgame route: `Citizens After Death` for a bounded settlement or `Commissariat Without End` for the extreme doctrine.

The tree uses route-specific AI weights, focus flags, idea lifecycle cleanup through hidden effects, and existing shared Soviet Collapse focus helper effects for recognition, high-chaos identity, military consolidation, league preparation, foreign contacts, and depot/supply control.

## Decisions and Ideas

Decision category: `soviet_collapse_iron_commissariat_of_the_dead`.

Decisions:

- `icd_audit_the_dead_rolls`
- `icd_mobilize_memorial_battalions`
- `icd_declare_citizens_after_death`

Ideas:

- `icd_iron_commissariat_of_the_dead`
- `icd_grave_commissar_rivalries`
- `icd_dead_roll_bureau`
- `icd_memorial_guard`
- `icd_citizens_after_death`

## Assets

The package uses existing final generated assets:

- Flags: `gfx/flags/ICD.tga`, `gfx/flags/medium/ICD.tga`, `gfx/flags/small/ICD.tga`
- Focus icon: `gfx/interface/goals/soviet_collapse/005_icd_custom_splinter_focus.dds`
- Idea icon: `gfx/interface/ideas/soviet_collapse/005_icd_custom_splinter_idea.dds`
- Decision icon: `gfx/interface/decisions/soviet_collapse/005_icd_custom_splinter_decision.dds`
- Portrait: `gfx/leaders/005_soviet_collapse/ICD_leader.dds`

Sprite wiring is in `interface/005_soviet_collapse_custom_icons.gfx`. The asset manifest row is in `docs/assets/005_soviet_union_collapse/manifest.md`.

## Remaining Work

The gameplay package is wired, but the focus tree currently reuses the tag-specific generated focus emblem across all 18 focuses. A final art pass can replace those sprite definitions with distinct per-focus DDS files without changing focus IDs or gameplay script.
