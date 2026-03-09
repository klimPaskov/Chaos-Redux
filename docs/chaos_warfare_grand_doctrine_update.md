Summary: This document explains the Chaos Warfare grand doctrine update that buffs chemical support companies, cylinder abilities, and chemical air-bomb profiles, and adds chemical-specific combat tactics.

# Chaos Warfare Grand Doctrine Update

## Overview

This update expands the gameplay impact of selecting `chaos_warfare` as a grand doctrine.

It adds:

1. A doctrine stat buff for all chemical support companies.
2. A doctrine multiplier for cylinder ability effectiveness.
3. A doctrine multiplier for chemical air-bomb contamination profile strength.
4. A new defensive tactic unlocked by gas-mask research.
5. A weaker chemical offensive tactic unlocked by first usable chemical weapon techs.
6. A stronger chemical offensive tactic unlocked by the Chaos Warfare doctrine.
7. A dedicated doctrine icon sprite registration.

## Step by Step Behavior

1. Country selects the `chaos_warfare` grand doctrine.
2. Doctrine grants category-based stat bonuses to units in `category_chemical_support_companies`.
3. `basic_gas_masks` technology unlocks `tactic_gas_mask_defense` for defensive anti-chemical counterplay.
4. Any first researched usable chemical weapon tech (`chlorine_gas`, `phosgene`, `mustard_gas`, `lewisite`, `sarin`, or `soman`) grants `tactic_chemical_shelling` as the baseline offensive chemical tactic.
5. Doctrine unlocks `tactic_chemical_barrage` as the stronger offensive chemical tactic.
6. If a country with `chaos_warfare` uses cylinder abilities, the final applied values are multiplied by `constant:chem_chaos_warfare_doctrine.cylinder_ability.mult`.
7. Preview math for cylinder abilities uses the same multiplier, so tooltip values match applied combat values.
8. If a country with `chaos_warfare` has an active chemical air-bomb profile, dose and duration profile variables are multiplied by doctrine constants.

## Tactics and Counters

### `tactic_gas_mask_defense`

- Role: defensive anti-chemical tactic.
- Unlock: `basic_gas_masks` technology.
- Scaling: gains extra weight from `improved_gas_masks` and `advanced_gas_masks`.
- Battlefield effect: strong attacker penalties intended to represent filtration and prepared anti-gas posture.

### `tactic_chemical_shelling`

- Role: baseline offensive chemical tactic.
- Unlock: first researched usable chemical attack tech (`chlorine_gas`, `phosgene`, `mustard_gas`, `lewisite`, `sarin`, or `soman`).
- Trigger profile: attacker-side and chemical-tech gated; no doctrine requirement.
- Battlefield effect: weaker pressure profile than doctrine barrage.
- Counter profile: countered by `tactic_gas_mask_defense` and `tactic_elastic_defense`.

### `tactic_chemical_barrage`

- Role: advanced offensive chemical assault tactic.
- Unlock: `chaos_warfare` grand doctrine.
- Trigger profile: attacker-side, doctrine + chemical-tech gated.
- Battlefield effect: improved attacker pressure and stronger defender suppression than `tactic_chemical_shelling`.
- Counter profile: explicitly countered by `tactic_gas_mask_defense` (hard counter behavior) and also linked against `tactic_elastic_defense` as a conventional defensive response.

## Integration with Existing Systems

- Doctrine file: `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`
- Tech unlock: `common/technologies/chaosx_technologies.txt`
- Combat tactics DB: `common/combat_tactics.txt`
- Save migration tactic sync: `common/on_actions/chaosx_on_actions_chemical_warfare.txt`
- Cylinder ability math: `common/scripted_effects/chemical_ability_effects.txt`
- Air-bomb profile math: `common/scripted_effects/chemical_air_bomb_effects.txt`
- Shared tuning values: `common/script_constants/chemical_warfare_constants.txt`
- Chemical sub-unit category registry: `common/unit_tags/chaos_categories.txt`
- Chemical support unit categorization:
  - `common/units/livens_projector_support.txt`
  - `common/units/chemical_tank_support.txt`

## Tuning Values

Doctrine-tuning constants are centralized in:

- `constant:chem_chaos_warfare_doctrine.cylinder_ability.mult`
- `constant:chem_chaos_warfare_doctrine.air_bomb.*`
- Doctrine file constants for support-company stats:
  - `@CHEM_SUPPORT_COMPANY_SOFT_ATTACK`
  - `@CHEM_SUPPORT_COMPANY_BREAKTHROUGH`
  - `@CHEM_SUPPORT_COMPANY_DEFENSE`

This keeps balancing in one place and avoids magic numbers spread across script files.

## Unlock Implementation Notes

- Tech-based tactic unlocks are executed through `on_research_complete = { unlock_tactic = ... }` in the relevant chemical and gas-mask technologies.
- Doctrine-based barrage unlock remains on doctrine selection via `enable_tactic = tactic_chemical_barrage`.
- Existing saves are synchronized through a guarded unlock pass in `on_army_leader_daily`, so countries that already have the required tech/doctrine receive missing tactics automatically.

## Icon and Sprite Wiring

### Implemented

- Texture file used by doctrine:
  - `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`
- Sprite registration:
  - File: `interface/chaosx_doctrines.gfx`
  - Sprite key: `GFX_doctrine_chaos_warfare_medium`
- Doctrine icon reference:
  - File: `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`
  - Key: `icon = GFX_doctrine_chaos_warfare_medium`
- Livens texticon sprite registrations (small icon tokens used in UI):
  - File: `interface/chaosx_texticons.gfx`
  - Sprite keys:
    - `GFX_unit_livens_projector_support_chlorine_icon_small`
    - `GFX_unit_livens_projector_support_phosgene_icon_small`
    - `GFX_unit_livens_projector_support_mustard_icon_small`
    - `GFX_unit_livens_projector_support_lewisite_icon_small`
    - `GFX_unit_livens_projector_support_sarin_icon_small`
    - `GFX_unit_livens_projector_support_soman_icon_small`
  - Current implementation note: these are aliased to existing chemical tank support small texticon textures so missing-texticon runtime errors are resolved immediately.

## Requested Art Assets

1. Doctrine icon:
   - Texture path: `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`
   - Sprite file: `interface/chaosx_doctrines.gfx`
   - Sprite name used in script: `GFX_doctrine_chaos_warfare_medium`
2. Optional dedicated Livens small texticon textures (to replace current aliases later):
   - Texture folder: `gfx/texticons/`
   - Filenames:
     - `unit_livens_projector_support_chlorine_icon_small.dds`
     - `unit_livens_projector_support_phosgene_icon_small.dds`
     - `unit_livens_projector_support_mustard_icon_small.dds`
     - `unit_livens_projector_support_lewisite_icon_small.dds`
     - `unit_livens_projector_support_sarin_icon_small.dds`
     - `unit_livens_projector_support_soman_icon_small.dds`
   - Sprite file to keep wired: `interface/chaosx_texticons.gfx`

### Icon Naming Rule

- Keep this exact sprite key in script: `GFX_doctrine_chaos_warfare_medium`
- Keep this exact texture path: `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`

## Future Plans

1. Add dedicated tactic tooltip localisation with explicit counter text and battlefield intent.
2. Add optional doctrine-conditional AI preferred tactic weights for more reliable AI use of `tactic_chemical_barrage`.
3. Add doctrine-conditional mitigation on opponent side when high-tier gas-mask tech is detected, to deepen tactical back-and-forth.
4. Add balance pass hooks for multiplayer presets (reduced multipliers) versus single-player presets (current multipliers).
