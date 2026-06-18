# 012 Africa Goal Icon Regeneration V2 Manifest

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v2_2026_06_18/`
- Asset type: focus / goal icons
- Target size: `94x86`
- Final DDS folder: `gfx/interface/goals/012_africa/`
- Existing sprite file kept unchanged: `interface/012_africa.gfx`
- Source mode: regenerated from the dedicated Event 012 goal-icon source art with a stricter alpha cleanup pass.

## Targets

All live Event 012 Africa goal icons were rebuilt:

- `goal_africa_charter_league_emblem`
- `goal_africa_authority_atlas`
- `goal_africa_scramble_for_africa`
- `goal_africa_high_chaos_bestiary`
- `goal_africa_political_congress`
- `goal_africa_charter_league_diplomacy`
- `goal_africa_liberation_war_office`
- `goal_africa_regional_integration`
- `goal_africa_industry_logistics`
- `goal_africa_sponsor_paths`
- `goal_africa_world_order_route`
- `goal_africa_archive_old_seats`
- `goal_africa_military_forces`

## Processing

- Removed border-connected white and off-white matte pixels.
- Removed low-alpha bright edge residue.
- Set fully transparent pixels to black RGB under alpha to avoid white bleed in DDS consumers.
- Recentered each icon on a transparent `94x86` canvas.
- Reconverted live DDS files as ARGB8888 with unchanged filenames and sprite paths.

## Evidence

- Source PNGs: `source_png/`
- Processed transparent PNGs: `processed_png/`
- DDS copies: `dds/`
- Processed PNG checker sheet: `contact_sheets/goal_icons_v2_checker_contact.png`
- Live DDS checker sheet: `contact_sheets/goal_icons_v2_live_dds_checker_contact.png`
- PNG validation: `validation/png_validation.json`
- Live DDS validation: `validation/live_dds_validation.json`

## Validation Summary

All 13 processed PNGs and all 13 live DDS files are exactly `94x86`, have transparent corners, have no hidden RGB under fully transparent pixels, and have no detected white/chroma halo pixels touching transparent regions.

No `.gfx`, gameplay, localisation, scripted GUI, focus, idea, decision, or event files were edited for this goal-icon pass.
