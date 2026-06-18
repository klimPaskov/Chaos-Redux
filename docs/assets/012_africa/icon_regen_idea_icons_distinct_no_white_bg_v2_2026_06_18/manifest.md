# 012 Africa Idea Icon Regeneration V2 Manifest

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v2_2026_06_18/`
- Asset type: idea / national-spirit icons
- Target size: `64x64`
- Final DDS folder: `gfx/interface/ideas/012_africa/`
- Existing sprite file kept unchanged: `interface/012_africa.gfx`
- Source mode: regenerated from the dedicated Event 012 idea-icon source art with stricter alpha and chroma-key cleanup.

## Targets

All live Event 012 Africa idea icons were rebuilt:

- `idea_africa_paper_core_mandate`
- `idea_africa_charter_league`
- `idea_africa_high_chaos_actor`
- `idea_africa_liberation_war_office`
- `idea_africa_rsa_continental_emergency`
- `idea_africa_is_one`
- `idea_africa_authority_atlas`
- `idea_africa_regional_authority`
- `idea_africa_high_chaos_bestiary`

## Distinct-Idea Rule

These are compact national-spirit emblems, not smaller goal icons. The v2 pass uses the dedicated idea source art and does not crop, resize, recolor, or derive any final idea icon from `gfx/interface/goals/012_africa/` or the goal-icon package.

## Processing

- Removed border-connected white/off-white matte pixels.
- Removed border-connected magenta, green, and yellow chroma-key backgrounds found in the idea source art.
- Removed low-alpha bright or chroma edge residue.
- Set fully transparent pixels to black RGB under alpha to avoid white or chroma bleed in DDS consumers.
- Recentered each icon on a transparent `64x64` canvas.
- Reconverted live DDS files as ARGB8888 with unchanged filenames and sprite paths.

## Evidence

- Source PNGs: `source_png/`
- Processed transparent PNGs: `processed_png/`
- DDS copies: `dds/`
- Processed PNG checker sheet: `contact_sheets/idea_icons_v2_checker_contact.png`
- Live DDS checker sheet: `contact_sheets/idea_icons_v2_live_dds_checker_contact.png`
- PNG validation: `validation/png_validation.json`
- Live DDS validation: `validation/live_dds_validation.json`

## Validation Summary

All nine processed PNGs and all nine live DDS files are exactly `64x64`, have transparent corners, have no hidden RGB under fully transparent pixels, and have no detected white/chroma halo pixels touching transparent regions.

No `.gfx`, gameplay, localisation, scripted GUI, focus, idea, decision, or event files were edited for this idea-icon pass.
