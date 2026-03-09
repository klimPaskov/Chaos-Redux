# Chaos Warfare: Operations Subdoctrine (Integrated Chemical Operations)

## Overview
This mechanic adds the `integrated_chemical_operations` subdoctrine to the Chaos Warfare `operations` track.

Design goal:
- Keep general buffs limited while shifting value into recon/intelligence-led chemical warfare.
- Increase chemical raid impact and contamination potency through progression flags.
- Reduce condemnation growth with staged reductions, ending at `-50%`.
- Add limited air integration so chemical air-bomb contamination scales with doctrine progress.
- Improve biological outbreak strike efficiency and potency while reducing BW condemnation impact.

## Implemented Structure
Primary doctrine file:
- `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt`

Subdoctrine:
- Key: `integrated_chemical_operations`
- Track: `operations`
- Mastery override:
  - `multiplier = 4.0`
  - Categories:
    - `category_all_infantry`
    - `category_tanks`
    - `category_support_battalions`
    - `category_chemical_support_companies`

## Activation Effects
- `planning_speed = 0.10`
- `land_reinforce_rate = 0.05`
- `recon_factor = 0.20`
- `category_chemical_support_companies`:
  - `coordination_bonus = 0.05`
  - `defense = 0.10`
  - `breakthrough = 0.10`

## Mastery Rewards
1. `operational_recon_grids`
- Recon/planning reinforcement.
- Sets `integrated_chemical_operations_operational_recon_grids_unlocked`.
- Applies condemnation reduction stage 1 (`-20%`).

2. `signal_intelligence_fusion`
- Chemical support and chemical tank support reliability gains.
- Adds intel-focused modifiers (`army_intel_factor`, `intel_from_combat_factor`).
- Sets `integrated_chemical_operations_signal_intelligence_fusion_unlocked`.
- Applies raid/contamination stage 1 (`+10%`).
- Applies biological outbreak strike potency stage 1 (`+5%` potency, `+10%` contamination duration).
- Adds biological outbreak strike command power efficiency stage 1 (`+1` CP refund per strike outcome).

3. `countercontamination_routing`
- Chemical logistics sustainment and attrition control.

4. `air_surface_chemical_link`
- Additional chemical support combat gain.
- Sets `integrated_chemical_operations_air_surface_chemical_link_unlocked`.
- Updates condemnation stage to `-35%`.
- Updates raid/contamination stage to `+20%`.
- Adds air-bomb contamination scaling (`+10% dose`, `+20% duration`).
- Updates biological strike condemnation to `-30%`.
- Updates biological outbreak strike potency to `+10%` and contamination duration to `+15%`.
- Updates biological outbreak strike command power efficiency to `+2` CP refund.

5. `theater_intelligence_overmatch`
- Mixed recon/org/reinforce capstone plus chemical support/tank support combat gains.
- Sets `integrated_chemical_operations_theater_intelligence_overmatch_unlocked` (and aligned prior flags).
- Final condemnation stage is `-50%`.
- Final raid/contamination stage is `+30%`.
- Final air-bomb contamination scaling is `+20% dose`, `+30% duration`.
- Final biological strike condemnation is `-50%`.
- Final biological outbreak strike potency is `+15%` and contamination duration is `+20%`.
- Final biological outbreak strike command power efficiency is `+3` CP refund.

## Script Integration
Shared tuning constants:
- `common/script_constants/chemical_warfare_constants.txt`
- New constant group: `chem_integrated_operations`
  - `condemnation_mult`
  - `contamination_mult`
  - `raid_effect_mult`
  - `air_bomb_dose_mult`
  - `air_bomb_duration_mult`
- New constant group: `bio_integrated_operations`
  - `bw_condemnation_mult`
  - `outbreak_potency_mult`
  - `outbreak_duration_mult`
  - `outbreak_command_power_refund`

Shared helper effects:
- `common/scripted_effects/chemical_warfare_effects.txt`
  - `chem_set_integrated_operations_condemnation_mult_from_owner`
  - `chem_set_integrated_operations_condemnation_mult_from_country`
  - `chem_set_integrated_operations_contamination_mult_from_owner_target`
  - `chem_set_integrated_operations_contamination_mult_from_actor_country`
  - `chem_set_integrated_operations_raid_effect_mult_from_actor_country`
  - `chem_set_integrated_operations_air_bomb_mult_from_owner`

Hook points updated:
- `common/scripted_effects/chemical_warfare_effects.txt`
  - Condemnation registration (`chem_warfare_register_attack_use`, `chem_warfare_register_attack_use_no_livens`)
  - Contamination multipliers (owner-target and actor-country paths)
  - Raid damage multipliers
- `common/scripted_effects/chemical_air_bomb_effects.txt`
  - Air-bomb profile scaling
- `common/scripted_effects/biowarfare_effects.txt`
  - `bio_set_integrated_operations_bw_modifiers_from_actor_country`
  - `bio_refund_outbreak_strike_command_power`
  - `bio_apply_outbreak_strike_potency_to_contamination`
  - Integrated into all four bioweapon consequence effects
  - Integrated into all four outbreak contamination effects (base + scaled)
  - Integrated into all four biological raid types across limited/success/critical outcomes

## Localisation and UI
Localisation keys added in:
- `localisation/english/chaosx_doctrines_l_english.yml`

Doctrine icon registration:
- `interface/chaosx_doctrines.gfx`
- Sprite key: `GFX_doctrine_integrated_chemical_operations_medium`
- Current texture mapping: `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`

## Icons Needed
1. Optional dedicated doctrine icon
- Path: `gfx/interface/doctrines/icons/doctrine_integrated_chemical_operations.dds`
- GFX key: `GFX_doctrine_integrated_chemical_operations_medium`
- GFX file: `interface/chaosx_doctrines.gfx`

If no custom icon is provided, the current fallback mapping remains valid.

## Future Plans / Suggestions
1. Add a dedicated operations-track milestone in `chaos_warfare_grand_doctrine.txt` so this subdoctrine has explicit milestone synergy.
2. Split condemnation scaling by source (abilities vs raids vs air-bombs) if finer diplomatic balancing is needed later.
3. Add AI weighting hooks to prioritize this subdoctrine when the country has strong chemical stockpile and active chemical raid use.
