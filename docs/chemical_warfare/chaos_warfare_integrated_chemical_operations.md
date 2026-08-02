# Chaos Warfare: Operations Subdoctrine (Integrated Chemical Operations)

## Overview
This mechanic adds the `integrated_chemical_operations` subdoctrine to the Chaos Warfare `operations` track.

Design goal:
- Make Army Headquarters command, recon, logistics, protection, and chemical support materially stronger as the operations track advances.
- Increase chemical raid impact and contamination potency through progression flags.
- Reduce Condemnation impact only, with the shared ladder `0.75` / `0.55` / `0.35` at operations mastery 1, 4, and 5; evidence, attribution, deaths, contamination, medical saturation, and public-harm floors remain intact.
- Keep air integration selected-state and fail-closed: chemical air raids can use the shared pipeline, while ordinary continuous air activity cannot prove release.
- Keep biological consequence scaling in the dedicated lifecycle and raid systems; the legacy biological adapter values remain neutral compatibility values.

## Implemented Structure
Primary doctrine file:
- `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt`

Subdoctrine:
- Key: `integrated_chemical_operations`
- Track: `operations`
- Mastery override:
  - `multiplier = 14.0`
  - Categories:
    - `category_all_infantry`
    - `category_tanks`
    - `category_support_battalions`
    - `category_chemical_support_companies`

## Activation Effects
- `planning_speed = 0.20`
- `land_reinforce_rate = 0.10`
- `recon_factor = 0.35`
- `coordination_bonus = 0.15`
- `category_chemical_support_companies`:
  - `defense = 0.25`
  - `breakthrough = 0.25`

## Mastery Rewards
1. `operational_recon_grids`
- `recon_factor = 0.35` and `planning_speed = 0.20`.
- Sets `integrated_chemical_operations_operational_recon_grids_unlocked`.
- Applies the first Condemnation-impact stage (`0.75` of the base).

2. `signal_intelligence_fusion`
- Adds `land_reinforce_rate = 0.10`, chemical-support breakthrough and defense of `0.25`, chemical-tank reliability of `0.25`, `army_intel_factor = 0.15`, and `intel_from_combat_factor = 0.35`.
- Sets `integrated_chemical_operations_signal_intelligence_fusion_unlocked`.
- It does not alter the Condemnation ladder; its biological compatibility multipliers and refund remain neutral.

3. `countercontamination_routing`
- Reduces CBRN Headquarters and chemical-tank supply consumption by `20%`, adds `25%` chemical-tank reliability, and reduces attrition by `20%`.

4. `air_surface_chemical_link`
- Adds `coordination_bonus = 0.15` and `soft_attack = 0.25` for chemical support companies.
- Sets `integrated_chemical_operations_air_surface_chemical_link_unlocked`.
- Updates the Condemnation-impact multiplier to `0.55` for accepted chemical and biological callers.
- Enables the selected-state air integration marker; it does not make continuous air missions contaminate states.

5. `theater_intelligence_overmatch`
- Adds `army_org_factor = 0.15`, `coordination_bonus = 0.15`, `land_reinforce_rate = 0.10`, and `recon_factor = 0.35`, plus `0.25` soft attack, breakthrough, and defense for chemical support and chemical-tank companies.
- Sets `integrated_chemical_operations_theater_intelligence_overmatch_unlocked` (and aligned prior flags).
- Final Condemnation-impact multiplier is `0.35`.
- Chemical and biological consequence potency is owned by the active Theater Contamination and Terminal Hazard officer-corps postures, not by these legacy adapter constants.

## Script Integration
Shared tuning constants:
- `common/script_constants/chemical_warfare_constants.txt`
- New constant group: `chem_integrated_operations`
  - `condemnation_mult`
  - `contamination_mult`
  - `raid_effect_mult`
  - `air_bomb_dose_mult`
  - `air_bomb_duration_mult`
- Compatibility group: `bio_integrated_operations`
  - The retained outbreak multiplier and refund entries are neutral or zero so older biological helpers cannot apply a second hidden doctrine bonus.

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
  - Legacy biological adapter helpers remain for save compatibility, but their compatibility multipliers are neutral and do not duplicate the shared biological lifecycle pipeline.

## Localisation and UI
Localisation keys added in:
- `localisation/english/chaosx_doctrines_l_english.yml`

Doctrine icon registration:
- `interface/chaosx_doctrines.gfx`
- Sprite key: `GFX_doctrine_integrated_chemical_operations_medium`
- Final texture: `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds`

## Condemnation Integration

The integrated-operations multiplier is applied only to Condemnation impact for each qualifying chemical or biological record before the value enters the shared bucket. It does not erase the public source, recent-use and repeat-use memory, source context, Air Cleanliness Treaty reaction, or sanction consequences. Chemical air activity uses `chemical_air_strike` only after a selected-state raid proves execution; ordinary continuous air activity remains ineligible. Biological outbreak strikes use `biological_outbreak`, and hostile weaponized-zombie deployment uses `weaponized_zombies`.

The canonical source, tier, participant, decay, and UI behavior is documented in `docs/systems/condemnation_sanctions.md`.

## Icons

The final registered sprite `GFX_doctrine_integrated_chemical_operations_medium` in `interface/cbrn_doctrine.gfx` uses `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds`.

## Future Plans / Suggestions
1. Add a dedicated operations-track milestone in `chaos_warfare_grand_doctrine.txt` so this subdoctrine has explicit milestone synergy.
2. Split the multiplier by source if later balance work needs separate ability, raid, and air-bomb tuning.
3. Add AI weighting hooks to prioritize this subdoctrine when the country has strong chemical stockpile and active chemical raid use.
