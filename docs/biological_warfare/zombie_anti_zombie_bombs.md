# Anti-Zombie Bombs

## Overview

This mechanic implements the containment half of the zombie special-project spec from `docs/events/002_zombie_special_project_spec.md`.

`zombie_cure_bomb` now unlocks a dedicated biological raid, `zombie_cure_strike`, instead of pretending to be a general bioweapon payload. The raid is bomber-launched and follows the same air-raid structure as the existing special chemical strikes.

## How it works

1. Completing the project sets `anti_zombie_bomb_available`.
2. The raid appears in the existing `biological_raids` category.
3. The raid can only be prepared when any country currently has `cure_activated`.
4. Valid target states must be zombie-controlled or adjacent to a zombie-controlled state.
5. Valid target countries are:
   self,
   faction members,
   zombie outbreak countries at war with the actor.
6. A successful raid applies `zombie_decontaminated_state`.
7. The modifier does not stack because already-treated states are filtered out at targeting time and the scripted effect is idempotent.

## Current Balance

- `zombie_cure_bomb` requires `0` breakthrough.
- Its project resource cost is now only `1` rubber.
- Anti-Zombie League members reduce cure decision research times through shared league coordination.
- League members also share a stronger `cure_sharing` research group than before.
- The League itself now uses the vanilla faction framework with a dedicated template, manifest, visible faction rules, and cure-focused faction goals.

## State Modifier Behavior

`zombie_decontaminated_state` is designed to hurt zombie control specifically:

- It only enables while the state is controlled by a zombie outbreak country.
- It cuts local manpower heavily, so the state becomes a poor manpower source for zombies.
- It reduces local supplies and movement for the controller.
- It increases controller attrition.
- It grants more local supplies to enemies in the same state.
- It blocks strategic redeployment for the controller.

The modifier has no scripted day timer. It removes itself automatically once no country still has `cure_activated`.

## Files

- `common/special_projects/projects/biowarfare_main_projects.txt`
- `common/factions/templates/anti_zombie_league.txt`
- `common/factions/goals/anti_zombie_league_goals.txt`
- `common/factions/rules/anti_zombie_league_rules.txt`
- `common/collections/anti_zombie_league_collections.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `common/raids/biological_raids.txt`
- `common/script_constants/zombie_special_project_constants.txt`
- `common/script_constants/zombie_constants.txt`
- `common/scripted_triggers/002_zombie_outbreak_triggers.txt`
- `common/scripted_effects/002_zombie_outbreak_effects.txt`
- `common/scripted_effects/zombie_special_project_effects.txt`
- `common/dynamic_modifiers/zombie_state_modifiers.txt`

## Icons

Current placeholder wiring:

- Raid map icon:
  `gfx/interface/military_raids/map_icons/raid_type_icon_zombie_cure_strike.dds`
  Referenced by `interface/chaosx_raids.gfx` as `GFX_raid_type_icon_zombie_cure_strike`.
- State modifier icon:
  `gfx/interface/ideas/idea_zombie_decontamination.dds`
  Referenced by `interface/chaosx_ideas.gfx` as `GFX_idea_zombie_decontamination`.
- Raid equipment icon:
  `gfx/interface/technologies/zombie_cure_bomb_equipment.dds`
  Referenced by `interface/chaosx_equipment.gfx` as `GFX_zombie_cure_bomb_equipment_medium`.
- Special project icon already in use:
  `gfx/interface/special_project/project_icons/sp_zombie_cure_bomb.dds`
  Referenced by `interface/special_projects/biowarfare.gfx` as `GFX_sp_zombie_cure_bomb`.

The Anti-Zombie League faction-system layer currently reuses vanilla faction UI art:

- Faction logo:
  vanilla `GFX_faction_logo_generic_democratic`
- Goal filter groups:
  vanilla `FOCUS_FILTER_INDUSTRY`
  vanilla `FOCUS_FILTER_POLITICAL_CHARACTER`

So this pass does not require any new custom faction GFX files.

## Future Work

- Add a dedicated raid payload equipment archetype if the zombie project is later expanded into stockpile-based deployment.
- Add AI weighting based on cure ownership, zombie front urgency, and faction support priorities once the offensive zombie project exists.
- Replace placeholder art with distinct anti-zombie containment visuals for the raid icon, the state modifier, and the equipment panel icon.
