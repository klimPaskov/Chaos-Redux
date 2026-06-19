# Event 012 Africa Idea Icon Rebuild v3

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v3_2026_06_19/`
- Asset type: idea / national-spirit icons
- Target size: `64x64`
- Final DDS folder: `gfx/interface/ideas/012_africa/`
- Existing sprite file kept unchanged: `interface/012_africa.gfx`
- Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- Source mode: dedicated Event 012 idea-icon source art, then local alpha cleanup, white/chroma matte removal, compact spirit-icon fit, and DDS rebuild
- Status: `complete`

## Distinct-Idea Rule

These nine icons are compact idea / national-spirit icons and are not smaller goal icons.

No v3 idea asset was cropped, resized, recolored, padded, or lightly edited from `gfx/interface/goals/012_africa/` or any goal-icon package. The `goal_vs_idea_distinctness_sheet.png` contact sheet exists only as validation proof and was not used as source art.

## Processing Summary

- Rebuilt all nine live Event 012 Africa idea icons from dedicated idea source PNGs in `source_png/`.
- Removed border-connected chroma-key backgrounds and white/off-white matte residue.
- Cleared white edge highlights adjacent to transparent pixels.
- Recentered each subject onto a transparent `64x64` idea-icon canvas sized for national-spirit readability, not focus-icon composition.
- Zeroed RGB under `alpha=0` to prevent hidden white or chroma bleed in DDS consumers.
- Converted package and live files to `64x64` `ARGB8888` DDS with unchanged filenames and sprite names.

## Asset List

| Asset | Source note | Source PNG | Processed PNG | Package DDS | Live DDS | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `idea_africa_authority_atlas` | compact atlas/compass spirit emblem | `source_png/idea_africa_authority_atlas_source.png` | `processed_png/idea_africa_authority_atlas.png` | `dds/idea_africa_authority_atlas.dds` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | `GFX_idea_africa_authority_atlas` | `complete` |
| `idea_africa_charter_league` | compact treaty ribbon and Charter League seal | `source_png/idea_africa_charter_league_source.png` | `processed_png/idea_africa_charter_league.png` | `dds/idea_africa_charter_league.dds` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `GFX_idea_africa_charter_league` | `complete` |
| `idea_africa_high_chaos_actor` | compact uncanny mask and court-token spirit emblem | `source_png/idea_africa_high_chaos_actor_source.png` | `processed_png/idea_africa_high_chaos_actor.png` | `dds/idea_africa_high_chaos_actor.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` | `GFX_idea_africa_high_chaos_actor` | `complete` |
| `idea_africa_high_chaos_bestiary` | compact clawed bestiary book and eye emblem | `source_png/idea_africa_high_chaos_bestiary_source.png` | `processed_png/idea_africa_high_chaos_bestiary.png` | `dds/idea_africa_high_chaos_bestiary.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | `GFX_idea_africa_high_chaos_bestiary` | `complete` |
| `idea_africa_is_one` | compact joined continent ring and unity emblem | `source_png/idea_africa_is_one_source.png` | `processed_png/idea_africa_is_one.png` | `dds/idea_africa_is_one.dds` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` | `GFX_idea_africa_is_one` | `complete` |
| `idea_africa_liberation_war_office` | compact field dispatch, broken chain, and shield emblem | `source_png/idea_africa_liberation_war_office_source.png` | `processed_png/idea_africa_liberation_war_office.png` | `dds/idea_africa_liberation_war_office.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | `GFX_idea_africa_liberation_war_office` | `complete` |
| `idea_africa_paper_core_mandate` | compact stamped parchment and paper-core seal | `source_png/idea_africa_paper_core_mandate_source.png` | `processed_png/idea_africa_paper_core_mandate.png` | `dds/idea_africa_paper_core_mandate.dds` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` | `GFX_idea_africa_paper_core_mandate` | `complete` |
| `idea_africa_regional_authority` | compact regional keys, ledger, and authority seal | `source_png/idea_africa_regional_authority_source.png` | `processed_png/idea_africa_regional_authority.png` | `dds/idea_africa_regional_authority.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | `GFX_idea_africa_regional_authority` | `complete` |
| `idea_africa_rsa_continental_emergency` | compact cracked shield and emergency flare emblem | `source_png/idea_africa_rsa_continental_emergency_source.png` | `processed_png/idea_africa_rsa_continental_emergency.png` | `dds/idea_africa_rsa_continental_emergency.dds` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` | `GFX_idea_africa_rsa_continental_emergency` | `complete` |

## Validation Evidence

- Processed PNG contact sheets:
  - `contact_sheets/processed_checker_sheet.png`
  - `contact_sheets/processed_dark_sheet.png`
- Package DDS roundtrip contact sheets:
  - `contact_sheets/dds_roundtrip_checker_sheet.png`
  - `contact_sheets/dds_roundtrip_dark_sheet.png`
- Live DDS roundtrip contact sheets:
  - `contact_sheets/live_dds_roundtrip_checker_sheet.png`
  - `contact_sheets/live_dds_roundtrip_dark_sheet.png`
- Distinctness proof sheet:
  - `contact_sheets/goal_vs_idea_distinctness_sheet.png`
- Validation files:
  - `validation/processed_png_validation.json`
  - `validation/live_dds_validation.json`
  - `validation/validation_notes.md`
  - `validation/validation_summary.txt`

## Validation Summary

All nine processed PNGs and all nine live DDS files:

- exist at the exact `64x64` target size
- report transparent corners
- have fully transparent unused canvas
- have RGB cleared under `alpha=0`
- have no non-transparent border pixels
- have no detected white/off-white edge matte pixels in the live DDS audit
- remain wired through existing `GFX_idea_africa_*` sprite names in `interface/012_africa.gfx`

No `.gfx`, localisation, gameplay, focus, idea, decision, event, GUI, script, history, spreadsheet, or unrelated asset files were edited during this pass.
