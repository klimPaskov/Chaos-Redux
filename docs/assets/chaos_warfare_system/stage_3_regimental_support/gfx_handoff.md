# Stage 3 Regimental Support GFX/path wiring record

Parent integration registered the completed package in the existing GFX files. The identifiers and runtime texture paths below are the final wired values.

Registered targets: division-counter sprites are in `interface/chaosx_subuniticons.gfx`; technology sprites are in `interface/chaosx_techtree.gfx`. Parent wiring is complete and the identifiers below are exact.

## Division large counters

All textures are 152x42 DDS sheets with two horizontal 76x42 frames: active at x=0 and muted at x=76.

| Registered sprite id | Exact texture path |
|---|---|
| `GFX_unit_cbrn_gas_mask_decon_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_gas_mask_decon_detachment_icon.dds` |
| `GFX_unit_cbrn_chemical_recon_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_chemical_recon_detachment_icon.dds` |
| `GFX_unit_cbrn_hazard_pioneer_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_hazard_pioneer_detachment_icon.dds` |
| `GFX_unit_cbrn_chemical_projector_battery_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_chemical_projector_battery_icon.dds` |
| `GFX_unit_cbrn_chemical_ammunition_train_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_chemical_ammunition_train_icon.dds` |
| `GFX_unit_cbrn_light_armored_delivery_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_light_armored_delivery_detachment_icon.dds` |
| `GFX_unit_cbrn_medium_armored_delivery_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_medium_armored_delivery_detachment_icon.dds` |
| `GFX_unit_cbrn_heavy_armored_delivery_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_heavy_armored_delivery_detachment_icon.dds` |
| `GFX_unit_cbrn_nerve_suppression_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_nerve_suppression_detachment_icon.dds` |
| `GFX_unit_cbrn_field_epidemiology_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_field_epidemiology_detachment_icon.dds` |
| `GFX_unit_cbrn_medical_countermeasure_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_medical_countermeasure_detachment_icon.dds` |
| `GFX_unit_cbrn_biosecurity_assault_detachment_icon_medium` | `gfx/interface/counters/divisions_large/unit_cbrn_biosecurity_assault_detachment_icon.dds` |
| `GFX_unit_chaos_battalion_icon_medium` | `gfx/interface/counters/divisions_large/unit_chaos_battalion_icon.dds` |

## Division small/on-map counters

All textures are 60x12 DDS sheets with two horizontal 30x12 frames: active at x=0 and muted at x=30. The active frames use the separately generated white-on-transparent counter masters.

| Registered sprite id | Exact texture path |
|---|---|
| `GFX_unit_cbrn_gas_mask_decon_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_gas_mask_decon_detachment_icon.dds` |
| `GFX_unit_cbrn_chemical_recon_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_chemical_recon_detachment_icon.dds` |
| `GFX_unit_cbrn_hazard_pioneer_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hazard_pioneer_detachment_icon.dds` |
| `GFX_unit_cbrn_chemical_projector_battery_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_chemical_projector_battery_icon.dds` |
| `GFX_unit_cbrn_chemical_ammunition_train_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_chemical_ammunition_train_icon.dds` |
| `GFX_unit_cbrn_light_armored_delivery_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_light_armored_delivery_detachment_icon.dds` |
| `GFX_unit_cbrn_medium_armored_delivery_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_medium_armored_delivery_detachment_icon.dds` |
| `GFX_unit_cbrn_heavy_armored_delivery_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_heavy_armored_delivery_detachment_icon.dds` |
| `GFX_unit_cbrn_nerve_suppression_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_nerve_suppression_detachment_icon.dds` |
| `GFX_unit_cbrn_field_epidemiology_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_field_epidemiology_detachment_icon.dds` |
| `GFX_unit_cbrn_medical_countermeasure_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_medical_countermeasure_detachment_icon.dds` |
| `GFX_unit_cbrn_biosecurity_assault_detachment_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_biosecurity_assault_detachment_icon.dds` |
| `GFX_unit_chaos_battalion_icon_medium_white` | `gfx/interface/counters/divisions_small/onmap_unit_chaos_battalion_icon.dds` |

## Technology icons

All textures are dedicated 64x64 DDS icons with one frame.

| Registered sprite id | Exact texture path |
|---|---|
| `GFX_hazard_pioneer_formation_medium` | `gfx/interface/technologies/cbrn_hazard_pioneer_formation.dds` |
| `GFX_chemical_artillery_shells_medium` | `gfx/interface/technologies/cbrn_chemical_artillery_shells.dds` |
| `GFX_persistent_agent_shell_filling_medium` | `gfx/interface/technologies/cbrn_persistent_agent_shell_filling.dds` |
| `GFX_armored_agent_delivery_medium` | `gfx/interface/technologies/cbrn_armored_agent_delivery.dds` |
| `GFX_sealed_tank_crews_medium` | `gfx/interface/technologies/cbrn_sealed_tank_crews.dds` |
| `GFX_nerve_agent_suppression_formation_medium` | `gfx/interface/technologies/cbrn_nerve_agent_suppression_formation.dds` |
| `GFX_field_epidemiology_teams_medium` | `gfx/interface/technologies/cbrn_field_epidemiology_teams.dds` |
| `GFX_mobile_cbrn_hospitals_medium` | `gfx/interface/technologies/cbrn_mobile_hospitals.dds` |
| `GFX_biological_security_assault_formation_medium` | `gfx/interface/technologies/cbrn_biosecurity_assault_formation.dds` |
| `GFX_chaos_battalion_tech_medium` | `gfx/interface/technologies/chaos_battalion.dds` |
| `GFX_chaos_battalion_1942_medium` | `gfx/interface/technologies/chaos_battalion3.dds` |

Wiring notes:

- Keep the exact runtime texture paths; the two existing Chaos Assault runtime files are intentionally replaced by the new protected-breaching identity.
- Do not treat the large sheets as small-counter sources. The small sheets were generated and composed separately for the 30x12 context.
- Use frame count 2 for every unit counter and frame count 1 for every technology icon.
- No localisation or gameplay identifiers were changed by this asset package.
