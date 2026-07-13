# Chaos Warfare Stage 4 HQ command asset manifest

Package: `docs/assets/chaos_warfare_system/stage_4_hq_command/`

Date: 2026-07-13

System: `chaos_warfare_system`

Stage: 4 Army Headquarters companies, commander abilities, and Theater CBRN Headquarters technology

## Source and processing contract

- Source mode: built-in `$imagegen` for fictional symbolic artwork.
- Raw generated captures are retained with `_source.png` in `source_png/`; the editable alpha-bearing source masters are retained with `_master.png` in the same asset-type folder.
- Green-background captures were processed with the official `$CODEX_HOME/skills/.system/imagegen/scripts/remove_chroma_key.py` helper using border auto-key, soft matte, threshold 12/220, and despill. One medical capture that arrived as a baked checkerboard and one logistics capture containing unintended skull markings were rejected and regenerated before processing.
- Exact-size processing, independent frame composition, contact sheets, and DDS export are recorded in `notes/process_stage_4_assets.py`. The script performs no artwork generation and does not create frame motion.
- All final PNGs and DDS files use real alpha with transparent unused pixels. Contact sheets use a checkerboard only for review.
- DDS format matches Stage 3: uncompressed 32-bit BGRA/RGBA-style DDS; header flags `135183`, pixel-format flags `65`, fourcc `0`, bit count `32`, masks `00FF0000/0000FF00/000000FF/FF000000`; no mipmaps.
- Large sheets are `[active 76x42][muted 76x42]` at `152x42`. Small sheets are `[active 30x12][muted 30x12]` at `60x12`. These are state sheets, not GIF animations; timing and looping are not applicable.
- Ability icons are one-frame `34x33` DDS files. The technology icon is one-frame `64x64` DDS.
- Sprite identifiers below are proposed because the parent handoff supplied exact gameplay IDs and runtime paths but no pre-registered sprite names. They follow Stage 3 and existing Chaos Redux naming patterns. `.gfx` files were not edited.

## Large Army HQ counters

| Gameplay ID | Source captures and masters | Processed PNGs | Final DDS | Size / alpha / frames | Proposed sprite / `.gfx` | Confidence / status |
|---|---|---|---|---|---|---|
| `cbrn_hq_operations_section` | `source_png/unit_large/cbrn_hq_operations_section_frame_{000,001}_source.png` -> matching `_master.png` | `processed_png/unit_large/cbrn_hq_operations_section_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_operations_section_icon.dds` | `152x42`, RGBA alpha, 2 state frames of `76x42` | `GFX_unit_cbrn_hq_operations_section_icon_medium` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_intelligence_weather_cell` | `source_png/unit_large/cbrn_hq_intelligence_weather_cell_frame_{000,001}_source.png` -> matching `_master.png` | `processed_png/unit_large/cbrn_hq_intelligence_weather_cell_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_intelligence_weather_cell_icon.dds` | `152x42`, RGBA alpha, 2 state frames of `76x42` | `GFX_unit_cbrn_hq_intelligence_weather_cell_icon_medium` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_protective_logistics_section` | `source_png/unit_large/cbrn_hq_protective_logistics_section_frame_{000,001}_source.png` -> matching `_master.png` | `processed_png/unit_large/cbrn_hq_protective_logistics_section_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_protective_logistics_section_icon.dds` | `152x42`, RGBA alpha, 2 state frames of `76x42` | `GFX_unit_cbrn_hq_protective_logistics_section_icon_medium` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_mobile_decontamination_column` | `source_png/unit_large/cbrn_hq_mobile_decontamination_column_frame_{000,001}_source.png` -> matching `_master.png` | `processed_png/unit_large/cbrn_hq_mobile_decontamination_column_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_mobile_decontamination_column_icon.dds` | `152x42`, RGBA alpha, 2 state frames of `76x42` | `GFX_unit_cbrn_hq_mobile_decontamination_column_icon_medium` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_medical_countermeasure_directorate` | `source_png/unit_large/cbrn_hq_medical_countermeasure_directorate_frame_{000,001}_source.png` -> matching `_master.png` | `processed_png/unit_large/cbrn_hq_medical_countermeasure_directorate_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_medical_countermeasure_directorate_icon.dds` | `152x42`, RGBA alpha, 2 state frames of `76x42` | `GFX_unit_cbrn_hq_medical_countermeasure_directorate_icon_medium` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_biological_security_section` | `source_png/unit_large/cbrn_hq_biological_security_section_frame_{000,001}_source.png` -> matching `_master.png` | `processed_png/unit_large/cbrn_hq_biological_security_section_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_large/unit_cbrn_hq_biological_security_section_icon.dds` | `152x42`, RGBA alpha, 2 state frames of `76x42` | `GFX_unit_cbrn_hq_biological_security_section_icon_medium` / `interface/chaosx_subuniticons.gfx` | High; complete |

## Small on-map HQ counters

| Gameplay ID | Source captures and masters | Processed PNGs | Final DDS | Size / alpha / frames | Proposed sprite / `.gfx` | Confidence / status |
|---|---|---|---|---|---|---|
| `cbrn_hq_operations_section` | `source_png/unit_small/cbrn_hq_operations_section_frame_{000,001}_source.png` -> matching `_master.png`; independently composed small masters | `processed_png/unit_small/cbrn_hq_operations_section_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_operations_section_icon.dds` | `60x12`, RGBA alpha, 2 state frames of `30x12` | `GFX_unit_cbrn_hq_operations_section_icon_medium_white` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_intelligence_weather_cell` | `source_png/unit_small/cbrn_hq_intelligence_weather_cell_frame_{000,001}_source.png` -> matching `_master.png`; independently composed small masters | `processed_png/unit_small/cbrn_hq_intelligence_weather_cell_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_intelligence_weather_cell_icon.dds` | `60x12`, RGBA alpha, 2 state frames of `30x12` | `GFX_unit_cbrn_hq_intelligence_weather_cell_icon_medium_white` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_protective_logistics_section` | `source_png/unit_small/cbrn_hq_protective_logistics_section_frame_{000,001}_source.png` -> matching `_master.png`; independently composed small masters | `processed_png/unit_small/cbrn_hq_protective_logistics_section_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_protective_logistics_section_icon.dds` | `60x12`, RGBA alpha, 2 state frames of `30x12` | `GFX_unit_cbrn_hq_protective_logistics_section_icon_medium_white` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_mobile_decontamination_column` | `source_png/unit_small/cbrn_hq_mobile_decontamination_column_frame_{000,001}_source.png` -> matching `_master.png`; independently composed small masters | `processed_png/unit_small/cbrn_hq_mobile_decontamination_column_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_mobile_decontamination_column_icon.dds` | `60x12`, RGBA alpha, 2 state frames of `30x12` | `GFX_unit_cbrn_hq_mobile_decontamination_column_icon_medium_white` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_medical_countermeasure_directorate` | `source_png/unit_small/cbrn_hq_medical_countermeasure_directorate_frame_{000,001}_source.png` -> matching `_master.png`; independently composed small masters | `processed_png/unit_small/cbrn_hq_medical_countermeasure_directorate_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_medical_countermeasure_directorate_icon.dds` | `60x12`, RGBA alpha, 2 state frames of `30x12` | `GFX_unit_cbrn_hq_medical_countermeasure_directorate_icon_medium_white` / `interface/chaosx_subuniticons.gfx` | High; complete |
| `cbrn_hq_biological_security_section` | `source_png/unit_small/cbrn_hq_biological_security_section_frame_{000,001}_source.png` -> matching `_master.png`; independently composed small masters | `processed_png/unit_small/cbrn_hq_biological_security_section_frame_{active,muted}.png`, `..._sheet.png` | `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_biological_security_section_icon.dds` | `60x12`, RGBA alpha, 2 state frames of `30x12` | `GFX_unit_cbrn_hq_biological_security_section_icon_medium_white` / `interface/chaosx_subuniticons.gfx` | High; complete |

## Commander ability icons

| Gameplay ID | Source / master | Processed PNG | Final DDS | Size / alpha / frames | Proposed sprite / `.gfx` | Confidence / status |
|---|---|---|---|---|---|---|
| `cbrn_prepare_chemical_offensive` | `source_png/abilities/cbrn_prepare_chemical_offensive_source.png` -> `_master.png` | `processed_png/abilities/cbrn_prepare_chemical_offensive.png` | `gfx/interface/abilitylist/cbrn_prepare_chemical_offensive.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_prepare_chemical_offensive` / `interface/chaosx_ability.gfx` | High; complete |
| `cbrn_theater_protective_posture` | `source_png/abilities/cbrn_theater_protective_posture_source.png` -> `_master.png` | `processed_png/abilities/cbrn_theater_protective_posture.png` | `gfx/interface/abilitylist/cbrn_theater_protective_posture.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_theater_protective_posture` / `interface/chaosx_ability.gfx` | High; complete |
| `cbrn_decontamination_corridor` | `source_png/abilities/cbrn_decontamination_corridor_source.png` -> `_master.png` | `processed_png/abilities/cbrn_decontamination_corridor.png` | `gfx/interface/abilitylist/cbrn_decontamination_corridor.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_decontamination_corridor` / `interface/chaosx_ability.gfx` | High; complete |
| `cbrn_seal_operational_area` | `source_png/abilities/cbrn_seal_operational_area_source.png` -> `_master.png` | `processed_png/abilities/cbrn_seal_operational_area.png` | `gfx/interface/abilitylist/cbrn_seal_operational_area.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_seal_operational_area` / `interface/chaosx_ability.gfx` | High; complete |
| `cbrn_mass_antidote_response` | `source_png/abilities/cbrn_mass_antidote_response_source.png` -> `_master.png` | `processed_png/abilities/cbrn_mass_antidote_response.png` | `gfx/interface/abilitylist/cbrn_mass_antidote_response.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_mass_antidote_response` / `interface/chaosx_ability.gfx` | High; complete |
| `cbrn_seal_infection_corridor` | `source_png/abilities/cbrn_seal_infection_corridor_source.png` -> `_master.png` | `processed_png/abilities/cbrn_seal_infection_corridor.png` | `gfx/interface/abilitylist/cbrn_seal_infection_corridor.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_seal_infection_corridor` / `interface/chaosx_ability.gfx` | High; complete |
| `cbrn_combined_overmatch` | `source_png/abilities/cbrn_combined_overmatch_source.png` -> `_master.png` | `processed_png/abilities/cbrn_combined_overmatch.png` | `gfx/interface/abilitylist/cbrn_combined_overmatch.dds` | `34x33`, RGBA alpha, 1 frame | `GFX_ability_cbrn_combined_overmatch` / `interface/chaosx_ability.gfx` | High; complete |

## Technology icon

| Gameplay ID | Source / master | Processed PNG | Final DDS | Size / alpha / frames | Proposed sprite / `.gfx` | Confidence / status |
|---|---|---|---|---|---|---|
| `cbrn_theater_cbrn_headquarters` | `source_png/technology/cbrn_theater_cbrn_headquarters_source.png` -> `_master.png` | `processed_png/technology/cbrn_theater_cbrn_headquarters.png` | `gfx/interface/technologies/cbrn_theater_cbrn_headquarters.dds` | `64x64`, RGBA alpha, 1 frame | `GFX_theater_cbrn_headquarters_medium` / `interface/chaosx_techtree.gfx` | High; complete |

## Review assets

- `contact_sheets/unit_large_contact_sheet_checker.png`
- `contact_sheets/unit_small_contact_sheet_checker.png`
- `contact_sheets/abilities_contact_sheet_checker.png`
- `contact_sheets/technology_contact_sheet_checker.png`
- `notes/visual_inspection.md`
- `gfx_handoff.md`

No requested asset is blocked or marked `needs_user_review`. Asset production did not edit `.gfx`, `.gui`, gameplay, localisation, plan, or unrelated asset files; parent integration subsequently registered the final DDS files in the existing subunit, ability, and technology GFX registries.
