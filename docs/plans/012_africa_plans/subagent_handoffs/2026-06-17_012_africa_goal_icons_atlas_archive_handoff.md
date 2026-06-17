# 012 Africa Goal Icons Atlas Archive Handoff

Scope completed: regenerate the requested bounded batch of four Africa GOAL/focus icons only, keeping final DDS filenames unchanged and leaving `.gfx`, focus files, localisation, scripts, and other icons untouched.

## Final DDS outputs

- `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds`
- `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds`
- `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds`
- `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds`

## Sprite names

- `GFX_goal_africa_regional_integration`
- `GFX_goal_africa_authority_atlas`
- `GFX_goal_africa_archive_old_seats`
- `GFX_goal_africa_liberation_war_office`

## Evidence package

- manifest: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/manifest.md`
- source PNGs: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/source_png/`
- processed PNGs: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/processed_png/`
- contact sheets: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/contact_sheets/`

## Method

- inspected `.agents/skills/chaos-redux-event-assets/assets/focuses` to match Chaos Redux focus-icon style
- generated symbolic source art with built-in `image_gen`
- requested flat `#00ff00` chroma-key backgrounds to avoid white matte issues
- removed chroma key with `$HOME/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py`
- trimmed, resized, and centered each icon onto a transparent `94x86` canvas
- converted processed PNGs to final DDS with `DXT5` compression

## Validation

- all four DDS files exist
- all four DDS files identify as `94x86`, `TrueColorAlpha`, `DXT5`
- transparent corner samples for every DDS: `0,0`, `93,0`, `0,85`, `93,85` all read `srgba(0,0,0,0)`
- checkerboard and dark-background review sheets show no square white matte behind the icons

## Notes

- no `.gfx` edits were made in this batch
- no uncertainty remains on filenames or sprite names because the final DDS names were fixed by the task
