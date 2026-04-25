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
- Manual assignment requires the owner country to have `chemical_operations_academy_spirit`
- The same academy spirit also gives new and leveling army leaders a `50%` scripted chance to gain the trait automatically
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
  - `chemical_operations_commander_prerequisite_tt`

## Historical Leaders Pre-assigned
To seed the system at game start with more chemically relevant commanders, this trait is pre-assigned in country history to:

- `SOV_mikhail_tukhachevsky` (`history/countries/SOV - Soviet union.txt`)
- `JAP_yasuji_okamura` (`history/countries/JAP - Japan.txt`)
- `JAP_seishiro_itagaki` (`history/countries/JAP - Japan.txt`)
- `JAP_shunroku_hata` (`history/countries/JAP - Japan.txt`)
- `JAP_naruhiko_higashikuni` (`history/countries/JAP - Japan.txt`)
- `JAP_tadaichi_wakamatsu` (`history/countries/JAP - Japan.txt`)
- `ITA_rodolfo_graziani` (`history/countries/ITA - Italy.txt`)
- `ITA_pietro_badoglio` (`history/countries/ITA - Italy.txt`)
- `ITA_emilio_de_bono` (`history/countries/ITA - Italy.txt`)

### Historical research notes
- `SOV_mikhail_tukhachevsky` remains the Soviet match because he is an in-game army leader and was one of the Red Army commanders in the Tambov campaign where chemical weapons were used.
- `ITA_emilio_de_bono` was added after the wider pass because he is an in-game field marshal and is linked to Italian poison-gas anti-partisan policy in Libya as well as senior command in the Ethiopian campaign.
- Spanish Rif War candidates were reviewed, including `SPA_francisco_franco`, `SPR_jose_millan_astray`, `SPA_emilio_mola`, `SPA_juan_yague`, and Spanish air/advisor characters. They were not assigned the trait because the sources support broad Army of Africa/Rif War participation, while the clearest gas-specific officers are either not represented as corps commanders or are not represented at all.
- `FRA_philippe_petain` was reviewed because of French command in the Rif War, but the vanilla character is not an army leader in the 1936 roster and the chemical-operations link is too indirect for this trait.
- `CAN_charles_foulkes` was reviewed and deliberately excluded. The represented Canadian general is Charles Foulkes, while the First World War British gas-services officer was Charles Howard Foulkes, a different person not represented by this roster token.
- German, British, American, and additional Soviet chemical specialists were reviewed by roster token. The strongest historical names found, such as Charles Howard Foulkes, Amos Fries, and Soviet chemical-troops staff figures, do not map cleanly to recruited in-game generals in this mod.

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
