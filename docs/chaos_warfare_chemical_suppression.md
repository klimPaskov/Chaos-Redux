# Chaos Warfare: Chemical Suppression (Armor Track)

## Overview
This mechanic adds one Chaos Warfare armor-track subdoctrine:

- `chemical_suppression`

The subdoctrine is only available while `chaos_warfare` is the active grand doctrine.  
Its design focus is occupation control through armored chemical pressure, with explicit separation between:

- generic chemical support (`category_chemical_support_companies`)
- chemical tank support only (`category_chemical_tank_support_companies`)

This prevents Livens projector companies from inheriting tank-only suppression bonuses.

## Implementation Summary
Files added/updated:

- `common/doctrines/subdoctrines/land/chaos_warfare_armor_subdoctrines.txt`
- `common/unit_tags/chaosx_categories.txt`
- `common/units/chemical_tank_support.txt`
- `common/occupation_laws/chaosx_occupation_laws.txt`
- `localisation/english/chaosx_doctrines_l_english.yml`
- `localisation/english/chaosx_occupation_laws_l_english.yml`

## Subdoctrine Progression
`chemical_suppression` contains five mastery rewards:

1. `adamsite_emission_cells`
2. `armored_chemical_support_liaison`
3. `zyklon_b_saturation_drills` (large chemical tank support suppression increase + concentration law unlock)
4. `sealed_pressure_logistics`
5. `catastrophic_shock_breakthrough`

Mastery 3 sets `concentration_occupation_law_unlocked`, enabling the new occupation law `concentration`.

## Occupation Law
`concentration` is defined in `common/occupation_laws/chaosx_occupation_laws.txt`.

Behavior:
- highest suppression profile (`resistance_target` pushed beyond vanilla harsh laws)
- high control cost (`required_garrison_factor` up)
- near-zero/negative compliance growth plus severe economic/local manpower penalties

Availability gate:
- requires country flag `concentration_occupation_law_unlocked`

## GFX Wiring
Doctrine, tech, raid, special project, and drum icon wiring was normalized to avoid missing-GFX errors.

### Added/updated GFX files
- `interface/chaosx_doctrines.gfx`
- `interface/chaosx_techtree.gfx`
- `interface/chaosx_raids.gfx`
- `interface/special_projects/biowarfare.gfx`
- `interface/chaosx_equipment.gfx`

### New/updated sprite tokens
- Doctrine:
  - `GFX_doctrine_chemical_suppression_medium` (placeholder mapped)
- Nerve tech:
  - `GFX_sarin_medium` -> `gfx/interface/technologies/sarin_gas_tech.dds`
  - `GFX_soman_medium` -> `gfx/interface/technologies/soman_gas_tech.dds`
- Raid aliases:
  - `GFX_raid_type_icon_sarin_strike`
  - `GFX_raid_type_icon_soman_strike`
  - `GFX_raid_unit_icon_cw_raids`
  - `GFX_raid_category_small_cw_raids`
- Special projects:
  - `GFX_sp_cw_sarin_program` -> `sp_sarin_bomb.dds`
  - `GFX_sp_cw_soman_program` -> `sp_soman_bomb.dds`
  - `GFX_sp_sarin_bomb`
  - `GFX_sp_soman_bomb`
- Drums/payload cylinders:
  - `GFX_chemical_*_payload_cylinder(_1)_medium` for chlorine/phosgene/mustard/lewisite/tabun/sarin/soman
  - non-medium aliases `GFX_chemical_*_payload_cylinder`

## Sprite Placeholder Notes
Where dedicated art is not yet finalized, tokens are mapped to stable existing textures so the game does not log missing GFX entries.

## Future Extension Ideas
1. Add a second armor subdoctrine with maneuver/attrition identity instead of suppression identity.
2. Add custom milestone effects for `chaos_warfare` armor track (currently empty milestones in grand doctrine file).
3. Add dedicated cylinder/drum atlas textures and replace temporary mappings in `interface/chaosx_equipment.gfx`.
