# Chemical Operations Commander Trait

## Overview
Adds a new assignable general trait:

- `chemical_operations_commander`

The trait is intended for corps commanders and does two things:
1. Unlocks all four cylinder barrage abilities.
2. Buffs chemical support companies in general.

## Implementation
### Trait definition
- File: `common/unit_leader/chaosx_traits.txt`
- Type: `corps_commander`
- Trait type: `assignable_trait`
- Cost: `500`
- No earned-trait requirement (directly selectable)
- Trait tree placement:
  - `chemical_operations_commander` sits below core general traits (`gui_row = 15`)
  - `skilled_staffer` and `expert_delegator` moved slightly down (`gui_row = 16`)
- Unlocks abilities via:
  - `enable_ability = chemical_chlorine_attack`
  - `enable_ability = chemical_phosgene_attack`
  - `enable_ability = chemical_mustard_attack`
  - `enable_ability = chemical_lewisite_attack`

### Ability gating
- File: `common/abilities/chemical_abilities.txt`
- Each cylinder ability now requires:
  - `has_trait = chemical_operations_commander`
  - The corresponding gas technology (existing gate retained)

### Chemical support company bonuses from trait
- File: `common/unit_leader/chaosx_traits.txt`
- The trait applies direct `sub_unit_modifiers` to all Livens and chemical tank support company variants.
- Values:
  - Attack: `+20%`
  - Defense: `+20%`

## Tooltip Cleanup
Per requested UI cleanup, the cylinder ability top tooltip no longer shows static:
- duration
- army speed modifier
- urban attack modifier

This was done by removing `duration` and `unit_modifiers` blocks from the four cylinder ability definitions.

## Localisation
- File: `localisation/english/chaosx_abilities_l_english.yml`
- Added:
  - `CHEM_ABILITY_COMMANDER_TRAINING_TT`
  - `chemical_operations_commander`
  - `chemical_operations_commander_desc`
  - `chemical_operations_commander_tt`

## Historical Leaders Pre-assigned
To seed the system at game start with more chemically relevant commanders, this trait is pre-assigned in country history to:

- `SOV_mikhail_tukhachevsky` (`history/countries/SOV - Soviet union.txt`)
- `JAP_yasuji_okamura` (`history/countries/JAP - Japan.txt`)
- `JAP_seishiro_itagaki` (`history/countries/JAP - Japan.txt`)
- `ITA_rodolfo_graziani` (`history/countries/ITA - Italy.txt`)
- `ITA_pietro_badoglio` (`history/countries/ITA - Italy.txt`)

## Icons Needed
No new icon is required for script correctness.

- If you want a dedicated custom trait icon later:
  - Place sprite in: `gfx/interface/traits/chemical_operations_commander.dds`
  - Register in a trait `.gfx` file (for example `interface/chaos_traits.gfx`)
  - Suggested sprite key: `GFX_trait_chemical_operations_commander`

## Future Plans
1. Add an alternate upgrade trait branch for higher cylinder efficiency but higher condemnation risk.
2. Add trait-specific AI selection weighting based on cylinder stockpile depth and active wars.
3. If needed, expose trait multipliers in `script_constants` for centralized balancing.
