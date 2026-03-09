# Chaos Warfare: Combat Support Subdoctrine (Contaminant Firebases)

## Overview
This mechanic adds the `contaminant_firebases` subdoctrine to the Chaos Warfare `combat_support` track.

Design goal:
- Improve Livens projector support and artillery support performance.
- Increase chemical raid impact.
- Increase chemical contamination potency (stronger contamination and longer persistence).
- Avoid special unlocks (no unit/law/tactic unlocks tied to this subdoctrine).

## Implemented Structure
Primary doctrine file:
- `common/doctrines/subdoctrines/land/chaos_warfare_combat_support_subdoctrines.txt`

Subdoctrine:
- Key: `contaminant_firebases`
- Track: `combat_support`
- Mastery override:
  - `multiplier = 10.0`
  - Categories:
    - `category_line_artillery`
    - `category_artillery`
    - `category_support_battalions`
    - `category_chemical_support_companies`

## Activation Effects
- `category_chemical_support_companies`:
  - `soft_attack = 0.10`
  - `breakthrough = 0.10`
  - `defense = 0.10`
- `category_line_artillery`:
  - `soft_attack = 0.10`
- `category_support_artillery`:
  - `soft_attack = 0.10`
  - `breakthrough = 0.15`

## Mastery Rewards
1. `livens_fire_control_cells`
- Chemical support soft attack and organization gains.
- Support artillery soft attack gain.

2. `counterbattery_gas_synchronization`
- Line artillery soft attack and breakthrough gains.
- Support artillery soft attack gain.
- Chemical support defense gain.

3. `raid_targeting_teams`
- Chemical support coordination gain.
- Sets `contaminant_firebases_raid_targeting_teams_unlocked`.
- Increases chemical nerve raid unit damage.

4. `persistent_agent_distribution`
- Line artillery soft attack gain.
- Sets `contaminant_firebases_persistent_agent_distribution_unlocked`.
- Increases contamination strength and contamination duration.

5. `deep_contamination_fireplans`
- Additional chemical support and support artillery combat gains.
- Sets `contaminant_firebases_deep_contamination_fireplans_unlocked` (and keeps reward 3/4 flags aligned).
- Further increases both raid damage and contamination potency.

## Script Integration
Shared tuning constants:
- `common/script_constants/chemical_warfare_constants.txt`
- New constant group: `chem_contaminant_firebases`
  - `contamination_mult.persistent_agent_distribution = 1.20`
  - `contamination_mult.deep_contamination_fireplans = 1.40`
  - `raid_damage_mult.raid_targeting_teams = 1.20`
  - `raid_damage_mult.deep_contamination_fireplans = 1.40`

Shared helper effects:
- `common/scripted_effects/chemical_warfare_effects.txt`
  - `chem_set_contaminant_firebases_contamination_mult_from_owner_target`
  - `chem_set_contaminant_firebases_contamination_mult_from_actor_country`
  - `chem_set_contaminant_firebases_raid_damage_mult_from_actor_country`

Hook points updated:
- `common/scripted_effects/chemical_ability_effects.txt`
- `common/scripted_effects/chemical_livens_support_effects.txt`
- `common/scripted_effects/chemical_tank_shell_effects.txt`
- `common/scripted_effects/chemical_infantry_effects.txt`
- `common/scripted_effects/chemical_warfare_effects.txt` (nerve raid state + unit damage functions)

## Localisation and UI
Localisation keys added in:
- `localisation/english/chaosx_doctrines_l_english.yml`

Doctrine icon registration:
- `interface/chaosx_doctrines.gfx`
- Sprite key: `GFX_doctrine_contaminant_firebases_medium`
- Current texture mapping: `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`

## Icons Needed
1. Optional dedicated doctrine icon
- Path: `gfx/interface/doctrines/icons/doctrine_contaminant_firebases.dds`
- GFX key: `GFX_doctrine_contaminant_firebases_medium`
- GFX file: `interface/chaosx_doctrines.gfx`

If no custom icon is provided, the current fallback mapping remains valid.

## Future Plans / Suggestions
1. Split raid impact into two tunables (direct unit damage and war support shock) for finer balancing.
2. Add an AI preference modifier for countries with high chemical stockpiles to prioritize this subdoctrine in combat-support track selection.
3. Add track milestone effects in `chaos_warfare_grand_doctrine.txt` so this subdoctrine can sync with future combat-support milestones.
