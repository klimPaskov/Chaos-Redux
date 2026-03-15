# US Special Chemical Projects

## Overview

This mechanic adds two United States-only special projects under the existing chemical warfare specialization:

1. `sp_cw_malodor_bomb_program`
2. `sp_cw_aphrodisiac_bomb_program`

Both projects unlock bomber-delivered chemical raids rather than frontline chemical support tools.

These are implemented as short-duration disruption weapons, not high-casualty killers. The malodor concept is meant to break cohesion and foul operations, while the aphrodisiac concept is meant to destabilize discipline, coordination, and planning inside the target zone.

Unlike lethal chemical raids, both special-project payloads are tuned to add no international condemnation.

## Gameplay Flow

1. USA researches into the chemical branch normally.
2. `Lewisite` unlocks the `Malodor Bomb Program`.
3. `Tabun (GA)` plus completion of the malodor project unlocks the `Aphrodisiac Bomb Program`.
4. Completing a project immediately enables production of its dedicated bomb payload.
5. The payload is then consumed by a raid in the existing `Chemical Raids` category.

## Implemented Effects

### Malodor Bomb

- Raid key: `chemical_malodor_strike`
- Equipment key: `malodor_bomb_1`
- Immediate hit:
  - province-level organization damage with no strength loss
- Temporary state disruption:
  - `-20%` attack
  - `-30%` defense
  - `-35%` movement
  - `-20%` breakthrough
  - `-30%` org recovery
  - `-60%` max entrenchment
  - strong dig-in-speed penalty
  - occupation disruption through `required_garrison_factor` and `resistance_target`
  - sortie disruption through `air_mission_efficiency` and `air_accidents_factor`
- Contamination:
  - only a very small short-lived contamination layer

### Aphrodisiac Bomb

- Raid key: `chemical_aphrodisiac_strike`
- Equipment key: `aphrodisiac_bomb_1`
- Temporary state disruption:
  - `+10%` attack
  - `+15%` breakthrough
  - `-25%` defense
  - `-50%` coordination
  - `-50%` reinforce rate
  - `-60%` max planning
  - `-50%` max entrenchment
  - `-40%` org recovery
  - minor occupation disruption

## Engine Limits And Approximations

- Direct province/state combat retreat forcing is not exposed cleanly through raid outcomes.
- Canceling an already-running attack from the struck province is not exposed as a reliable raid/script effect.
- Because of that, the current implementation approximates these requests through:
  - large immediate org shock for the malodor bomb
  - short-duration entrenchment, defense, reinforce, planning, and org-recovery penalties

If you want the retreat/cancel behavior pushed harder later, the best follow-up is probably a more aggressive org-shock pass or a combat-event approximation, but that should be discussed first rather than added as a hidden fallback.

## Files Added Or Updated

- `common/script_constants/chemical_warfare_constants.txt`
- `common/dynamic_modifiers/chemical_special_raid_modifiers.txt`
- `common/scripted_effects/chemical_warfare_effects.txt`
- `common/special_projects/projects/chemical_special_projects.txt`
- `common/units/equipment/chemical_special_bombs.txt`
- `common/raids/chemical_special_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `common/script_enums.txt`
- `interface/special_projects/biowarfare.gfx`
- `interface/chaosx_equipment.gfx`
- `interface/chaosx_ideas.gfx`
- `localisation/english/chaosx_special_projects_l_english.yml`
- `localisation/english/chaosx_raids_l_english.yml`
- `localisation/english/chaosx_equipment_l_english.yml`
- `localisation/english/chaosx_abilities_l_english.yml`

## Icon Wiring

The following custom assets are required by this feature set. Final art can overwrite the placeholder files in place without renaming any code keys:

- Special project icon, malodor:
  - file: `gfx/interface/special_project/project_icons/sp_malodor_bomb.dds`
  - registered in: `interface/special_projects/biowarfare.gfx`
  - sprite: `GFX_sp_malodor_bomb`
  - status: placeholder already created
- Special project icon, aphrodisiac:
  - file: `gfx/interface/special_project/project_icons/sp_aphrodisiac_bomb.dds`
  - registered in: `interface/special_projects/biowarfare.gfx`
  - sprite: `GFX_sp_aphrodisiac_bomb`
  - status: placeholder already created
- Equipment icon, malodor:
  - file: `gfx/interface/technologies/malodor_bomb_equipment.dds`
  - registered in: `interface/chaosx_equipment.gfx`
  - sprite: `GFX_malodor_bomb_equipment_medium`
  - used by: raid equipment icon and equipment UI
  - status: placeholder already created
- Equipment icon, aphrodisiac:
  - file: `gfx/interface/technologies/aphrodisiac_bomb_equipment.dds`
  - registered in: `interface/chaosx_equipment.gfx`
  - sprite: `GFX_aphrodisiac_bomb_equipment_medium`
  - used by: raid equipment icon and equipment UI
  - status: placeholder already created
- State modifier icon, malodor:
  - file: `gfx/interface/ideas/idea_malodor_raid_state.dds`
  - registered in: `interface/chaosx_ideas.gfx`
  - sprite: `GFX_idea_malodor_raid_state`
  - used by: `chem_state_malodor_disruption`
  - status: placeholder already created
- State modifier icon, aphrodisiac:
  - file: `gfx/interface/ideas/idea_aphrodisiac_raid_state.dds`
  - registered in: `interface/chaosx_ideas.gfx`
  - sprite: `GFX_idea_aphrodisiac_raid_state`
  - used by: `chem_state_aphrodisiac_disruption`
  - status: placeholder already created

No additional custom art is currently required for the prototype reward popups. Those reward entries intentionally use the vanilla generic `GFX_PLACEHOLDER_sp_project_picture`.

## Future Work

1. Decide whether these projects should remain USA-only forever or become unlockable for a tiny set of late-game chemical powers through espionage or capture.
2. Revisit raid AI so the USA values these payloads differently against entrenched fronts, occupied territory, and air-base-heavy regions.
3. If the engine surface proves reliable, test whether the sortie disruption should move from general `air_mission_efficiency` into a more airbase-specific state penalty set.
4. If you want stronger battlefield identity, add dedicated raid pictures, sounds, and event/news hooks for first use.
