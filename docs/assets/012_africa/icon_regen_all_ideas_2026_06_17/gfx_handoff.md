# 012 Africa Idea Icon GFX Handoff

This package replaced only the existing Event 012 idea/national-spirit DDS files under `gfx/interface/ideas/012_africa/`. No gameplay files, `.gfx` files, GUI files, localisation, scripts, focus files, or spreadsheets were edited.

## Files changed

- `gfx/interface/ideas/012_africa/idea_africa_is_one.dds`
- `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds`
- `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds`
- `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds`
- `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds`
- `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds`
- `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds`
- `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds`
- `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds`

## Sprite handoff

- Existing `.gfx` file retained unchanged: `interface/012_africa.gfx`
- Existing sprite names preserved exactly:
  - `GFX_idea_africa_is_one`
  - `GFX_idea_africa_paper_core_mandate`
  - `GFX_idea_africa_charter_league`
  - `GFX_idea_africa_authority_atlas`
  - `GFX_idea_africa_liberation_war_office`
  - `GFX_idea_africa_high_chaos_bestiary`
  - `GFX_idea_africa_regional_authority`
  - `GFX_idea_africa_high_chaos_actor`
  - `GFX_idea_africa_rsa_continental_emergency`

## Source and distinction note

Every icon in this package was generated as its own dedicated source artwork for `64x64` idea-icon use, then locally processed to alpha PNG and DDS. None of these idea icons were resized, cropped, padded, recolored, or lightly edited from Event 012 focus/goal icons.

Goal-family comparison proof is included at:

- `contact_sheets/idea_vs_goal_comparison.png`

Transparency proof sheets are included at:

- `contact_sheets/ideas_transparency_checker_sheet.png`
- `contact_sheets/ideas_transparency_dark_sheet.png`

## Validation run

Reference inspection:

- inspected `.agents/skills/chaos-redux-event-assets/assets/ideas`
- inspected current `gfx/interface/ideas/012_africa/*.dds`
- inspected current `gfx/interface/goals/012_africa/*.dds` for family distinction only

Processing and export:

- copied generated source PNGs into `source_png/`
- removed flat chroma-key backgrounds with:
  - `python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`
- resized processed finals to `64x64`
- exported DDS with:
  - `convert <processed_png> -define dds:compression=none DDS:<final_dds>`

DDS validation:

- `file gfx/interface/ideas/012_africa/idea_africa_*.dds`
- `python3` Pillow check for each final DDS:
  - size exactly `64x64`
  - alpha channel extrema `(0, 255)`
  - all four corners `(0, 0, 0, 0)`

Parent review follow-up:

- `idea_africa_high_chaos_actor` and `idea_africa_rsa_continental_emergency` were re-centered and reconverted after parent validation found nonzero alpha on the outer DDS border.
- The checker, dark, and goal-family comparison proof sheets were rebuilt after that correction.

## Blocked assets

- none

## Residual concerns

- `idea_africa_high_chaos_actor` and `idea_africa_high_chaos_bestiary` intentionally keep denser supernatural silhouettes than the administrative icons, but both remain readable at final size and preserve clean transparent corners.
