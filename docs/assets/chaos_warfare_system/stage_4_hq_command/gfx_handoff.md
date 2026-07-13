# Stage 4 HQ command GFX/path handoff

Parent integration should add these registrations to the existing files; this bounded asset package did not edit `.gfx` files.

Proposed sprite names are stable and follow the exact Stage 3 patterns. Runtime DDS paths and gameplay identifiers are authoritative.

## Large Army HQ counters

Target file: `interface/chaosx_subuniticons.gfx`

Each texture is `152x42`, with two state frames: active at x=0 and muted at x=76. `noOfFrames = 2` is only for the existing counter state-sheet convention; this is not a looping animation.

| Proposed sprite id | Exact texture path | Related subunit |
|---|---|---|
| `GFX_unit_cbrn_hq_operations_section_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_operations_section_icon.dds` | `cbrn_hq_operations_section` |
| `GFX_unit_cbrn_hq_intelligence_weather_cell_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_intelligence_weather_cell_icon.dds` | `cbrn_hq_intelligence_weather_cell` |
| `GFX_unit_cbrn_hq_protective_logistics_section_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_protective_logistics_section_icon.dds` | `cbrn_hq_protective_logistics_section` |
| `GFX_unit_cbrn_hq_mobile_decontamination_column_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_mobile_decontamination_column_icon.dds` | `cbrn_hq_mobile_decontamination_column` |
| `GFX_unit_cbrn_hq_medical_countermeasure_directorate_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_medical_countermeasure_directorate_icon.dds` | `cbrn_hq_medical_countermeasure_directorate` |
| `GFX_unit_cbrn_hq_biological_security_section_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_biological_security_section_icon.dds` | `cbrn_hq_biological_security_section` |

Ready-to-copy pattern:

```text
spriteType = {
	name = "GFX_unit_cbrn_hq_operations_section_icon_medium"
	texturefile = "gfx/interface/counters/divisions_large/unit_cbrn_hq_operations_section_icon.dds"
	noOfFrames = 2
}
```

## Small/on-map Army HQ counters

Target file: `interface/chaosx_subuniticons.gfx`

Each texture is `60x12`, with two independently composed state frames: active at x=0 and muted at x=30. The small source masters are not derived from the large masters.

| Proposed sprite id | Exact texture path | Related subunit |
|---|---|---|
| `GFX_unit_cbrn_hq_operations_section_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_operations_section_icon.dds` | `cbrn_hq_operations_section` |
| `GFX_unit_cbrn_hq_intelligence_weather_cell_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_intelligence_weather_cell_icon.dds` | `cbrn_hq_intelligence_weather_cell` |
| `GFX_unit_cbrn_hq_protective_logistics_section_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_protective_logistics_section_icon.dds` | `cbrn_hq_protective_logistics_section` |
| `GFX_unit_cbrn_hq_mobile_decontamination_column_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_mobile_decontamination_column_icon.dds` | `cbrn_hq_mobile_decontamination_column` |
| `GFX_unit_cbrn_hq_medical_countermeasure_directorate_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_medical_countermeasure_directorate_icon.dds` | `cbrn_hq_medical_countermeasure_directorate` |
| `GFX_unit_cbrn_hq_biological_security_section_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_biological_security_section_icon.dds` | `cbrn_hq_biological_security_section` |

Ready-to-copy pattern:

```text
spriteType = {
	name = "GFX_unit_cbrn_hq_operations_section_icon_medium_white"
	texturefile = "gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_operations_section_icon.dds"
	noOfFrames = 2
}
```

## Commander ability icons

Target file: `interface/chaosx_ability.gfx`, following the existing `GFX_ability_<ability_id>` naming pattern. Each DDS is one dedicated `34x33` frame.

| Proposed sprite id | Exact texture path | Related ability |
|---|---|---|
| `GFX_ability_cbrn_prepare_chemical_offensive` | `gfx/interface/abilitylist/cbrn_prepare_chemical_offensive.dds` | `cbrn_prepare_chemical_offensive` |
| `GFX_ability_cbrn_theater_protective_posture` | `gfx/interface/abilitylist/cbrn_theater_protective_posture.dds` | `cbrn_theater_protective_posture` |
| `GFX_ability_cbrn_decontamination_corridor` | `gfx/interface/abilitylist/cbrn_decontamination_corridor.dds` | `cbrn_decontamination_corridor` |
| `GFX_ability_cbrn_seal_operational_area` | `gfx/interface/abilitylist/cbrn_seal_operational_area.dds` | `cbrn_seal_operational_area` |
| `GFX_ability_cbrn_mass_antidote_response` | `gfx/interface/abilitylist/cbrn_mass_antidote_response.dds` | `cbrn_mass_antidote_response` |
| `GFX_ability_cbrn_seal_infection_corridor` | `gfx/interface/abilitylist/cbrn_seal_infection_corridor.dds` | `cbrn_seal_infection_corridor` |
| `GFX_ability_cbrn_combined_overmatch` | `gfx/interface/abilitylist/cbrn_combined_overmatch.dds` | `cbrn_combined_overmatch` |

Ready-to-copy pattern:

```text
spriteType = {
	name = "GFX_ability_cbrn_prepare_chemical_offensive"
	texturefile = "gfx/interface/abilitylist/cbrn_prepare_chemical_offensive.dds"
	noOfFrames = 1
}
```

## Theater technology

Target file: `interface/chaosx_techtree.gfx`, following the Stage 3 medium technology pattern. The texture is one dedicated `64x64` frame.

| Proposed sprite id | Exact texture path | Related technology |
|---|---|---|
| `GFX_theater_cbrn_headquarters_medium` | `gfx/interface/technologies/cbrn_theater_cbrn_headquarters.dds` | `cbrn_theater_cbrn_headquarters` |

Ready-to-copy pattern:

```text
spriteType = {
	name = "GFX_theater_cbrn_headquarters_medium"
	texturefile = "gfx/interface/technologies/cbrn_theater_cbrn_headquarters.dds"
	noOfFrames = 1
}
```

## Integration confirmation

Parent integration retained every proposed stable name and registered all twenty textures in `interface/chaosx_subuniticons.gfx`, `interface/chaosx_ability.gfx`, and `interface/chaosx_techtree.gfx`. All registered paths resolve, the new identifiers are unique, ability definitions use the registered `GFX_ability_<ability_id>` names, and the technology uses `GFX_theater_cbrn_headquarters_medium`.
