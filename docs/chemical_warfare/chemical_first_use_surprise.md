# Chemical First-Use Surprise

## Overview

This mechanic adds a one-time, temporary combat spike when a country first uses chemical weapons in real combat.

- On first eligible chemical combat use, the country gains `chemical_first_use_surprise_idea` for 30 days.
- The idea grants:
  - `+5%` `army_attack_factor`
  - `+5%` `breakthrough_factor`
- While the idea is active:
  - Cylinder ability final values are multiplied by `1.5` (offense, breakthrough, defense, org damage, str damage, war support damage).
  - Cylinder preview values are multiplied by the same `1.5` so UI matches actual behavior.
  - Chemical tank-shell and Livens support profile values are multiplied by `1.5` (dose, duration, condemnation base, condemnation per-unit).
- The effect is strictly one-time per country and can never be earned again after expiration.

## Trigger Logic

The surprise is granted by `chem_grant_first_use_surprise` and guarded by a permanent country flag:

- `chem_first_use_surprise_consumed` (set permanently on first grant)

Grant is attempted from combat-use paths only:

1. `on_army_leader_won_combat` / `on_army_leader_lost_combat` when:
   - `num_units_offensive_combats > 0`, and
   - leader has an active chemical cylinder trait (`chlorine`, `phosgene`, `mustard`, `lewisite`).
2. `chem_tank_shell_register_combat_condemnation_won/lost` when guaranteed chemical tank support offensive participation is greater than zero.
3. `chem_livens_support_register_combat_condemnation_won/lost` when guaranteed Livens support offensive participation is greater than zero.

## Files Changed

- `common/scripted_effects/chemical_warfare_effects.txt`
  - Added `chem_grant_first_use_surprise` and duration constant.
- `common/on_actions/chaosx_on_actions_chemical_warfare.txt`
  - Added cylinder-active combat grant checks in won/lost combat hooks.
- `common/scripted_effects/chemical_tank_shell_effects.txt`
  - Added active-idea support profile multiplier and surprise grant calls.
- `common/scripted_effects/chemical_livens_support_effects.txt`
  - Added active-idea support profile multiplier and surprise grant calls.
- `common/scripted_effects/chemical_ability_effects.txt`
  - Added active-idea `1.5x` multiplier to both preview and final cylinder bonus functions.
- `common/ideas/chaosx_ideas.txt`
  - Added `chemical_first_use_surprise_idea`.
- `localisation/english/chaosx_ideas_l_english.yml`
  - Added name/description localisation for `chemical_first_use_surprise_idea`.

## Icons

### Current implementation

- Idea icon uses existing vanilla icon token: `generic_infantry_bonus`.
- No new sprite or texture registration is required for this implementation.

### Optional future custom icon

If you want a custom icon later:

1. Place texture in: `gfx/interface/ideas/`
2. Register sprite in an ideas `.gfx` file (for example an existing Chaos Redux interface gfx file).
3. Update `picture = ...` in `chemical_first_use_surprise_idea` to the new sprite token.

## Future Extensions

1. Split surprise into two tiers based on delivery mode (cylinder-only first use vs support-company first use).
2. Add AI caution memory to reduce repeated risky assaults immediately after enemy surprise proc.
3. Add defender-side temporary adaptation event chain after first exposure.
