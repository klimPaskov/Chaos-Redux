# Chaos Warfare Officer Corps Spirits

## Overview
This adds three doctrine-gated officer corps spirits that become selectable when a country has `chaos_warfare` selected as its land grand doctrine, plus one doctrine-independent academy spirit:

1. Army spirit: `chemical_command_reagent_optimization_spirit`
2. Division command spirit: `chemical_division_contamination_command_spirit`
3. Air spirit: `chemical_air_deep_strike_spirit`
4. Academy spirit: `chemical_operations_academy_spirit` (no `chaos_warfare` requirement)

## Implemented Spirits
### 1. Army Spirit
- Key: `chemical_command_reagent_optimization_spirit`
- Category: `army_spirit`
- Availability gate: `has_doctrine = chaos_warfare`
- Effects:
  - Chemical cylinder abilities refund command power via scripted effect (`20%` of the ability CP cost).
  - Chemical cylinder abilities consume fewer cylinders (`20%` reduction).
  - Chemical sub-unit template design XP cost is set to zero via `unit_<unit>_design_cost_factor = -1` for:
    - All Livens chemical support variants.
    - All light/medium/heavy chemical tank support variants.
    - `chaos_battalion`.

### 2. Division Command Spirit
- Key: `chemical_division_contamination_command_spirit`
- Category: `division_command_spirit`
- Availability gate: `has_doctrine = chaos_warfare`
- Effects:
  - Buffs Livens projector support combat-effect profiles (`dose`, `duration`, `condemnation`) by `20%`.
  - Buffs chemical tank support combat-effect profiles (`dose`, `duration`, `condemnation`) by `20%`.
  - Buffs chaos battalion state contamination, direct enemy damage, and combat condemnation output by `20%`.

### 3. Air Spirit
- Key: `chemical_air_deep_strike_spirit`
- Category: `air_force_command_spirit`
- Availability gate: `has_air_force_command = yes` and `has_doctrine = chaos_warfare`
- Effects:
  - Buffs chemical raid effectiveness by multiplying raid damage and raid contamination potency.
  - Buffs chemical air-bomb effects by increasing dose and contamination duration multipliers.

### 4. Academy Spirit
- Key: `chemical_operations_academy_spirit`
- Category: `academy_spirit`
- Availability gate: no `chaos_warfare` doctrine requirement.
- Effects:
  - Adds a 50% roll on general creation and on general level-up to grant `chemical_operations_commander`.
  - Uses shared scripted effect `chem_try_grant_chemical_operations_trait_from_academy_spirit`.

## Script Integration
### New constants
- File: `common/script_constants/chemical_spirit_constants.txt`
- Constant group: `chem_chaos_warfare_spirit`
  - `army.ability_cylinder_cost_mult = 0.80`
  - `army.ability_cp_refund_factor = 0.20`
  - `division.support_profile_mult = 1.20`
  - `division.chaos_state_effect_mult = 1.20`
  - `division.chaos_damage_mult = 1.20`
  - `division.chaos_condemnation_mult = 1.20`
  - `division.barrage_preferred_weight_factor = 1.00`
  - `academy.chemical_operations_trait_gain_chance = 50`
  - `air.raid_effect_mult = 1.20`
  - `air.air_bomb_dose_mult = 1.20`
  - `air.air_bomb_duration_base_mult = 1.20`
  - `air.air_bomb_duration_per_pressure_mult = 1.20`

### Idea definitions
- File: `common/ideas/cbw_spirits.txt`

### Hook points
- Ability CP refund + cylinder cost reduction:
  - `common/scripted_effects/chemical_warfare_effects.txt`
  - `common/scripted_effects/chemical_ability_effects.txt`
  - `common/abilities/chemical_abilities.txt`
- Division-command chemical subunit amplification:
  - `common/scripted_effects/chemical_warfare_effects.txt`
  - `common/scripted_effects/chemical_livens_support_effects.txt`
  - `common/scripted_effects/chemical_tank_shell_effects.txt`
  - `common/scripted_effects/chemical_infantry_effects.txt`
- Chemical raid and air-bomb amplification:
  - `common/scripted_effects/chemical_warfare_effects.txt`
  - `common/scripted_effects/chemical_air_bomb_effects.txt`

### Localisation
- File: `localisation/english/chaosx_ideas_l_english.yml`

## Icons Needed
No new icon assets are required for this implementation.

- Reason: all three spirits currently use standard officer-corps presentation and scripted effects without new `picture` sprite keys.
- If custom art is later desired, define dedicated spirit icons in an ideas `.gfx` file and bind them to these three spirit keys.

## Future Plans / Suggestions
1. Add dedicated spirit-specific icons and custom UI tooltips that preview exact CP/cylinder savings from current army size.
2. Split the air-spirit raid bonus into separate tunables for direct unit damage vs contamination strength/duration.
3. Add AI preference weights based on cylinder stockpile depth and active chemical airframe deployment share.
