# Event 010 Death focus icon batch handoff

Date: `2026-06-16`
Scope: regenerate only the assigned 8 Death national focus icons as new HOI4-style focus art

## Files changed

- `docs/assets/010_death/source_png/focus_death_black_census_source.png`
- `docs/assets/010_death/source_png/focus_death_no_graves_needed_source.png`
- `docs/assets/010_death/source_png/focus_death_first_ghost_muster_source.png`
- `docs/assets/010_death/source_png/focus_death_public_death_source.png`
- `docs/assets/010_death/source_png/focus_death_tide_learns_roads_source.png`
- `docs/assets/010_death/source_png/focus_death_another_shoreline_source.png`
- `docs/assets/010_death/source_png/focus_death_no_ferry_returns_source.png`
- `docs/assets/010_death/source_png/focus_death_wasteland_roads_source.png`
- `docs/assets/010_death/processed_png/focus_death_black_census.png`
- `docs/assets/010_death/processed_png/focus_death_no_graves_needed.png`
- `docs/assets/010_death/processed_png/focus_death_first_ghost_muster.png`
- `docs/assets/010_death/processed_png/focus_death_public_death.png`
- `docs/assets/010_death/processed_png/focus_death_tide_learns_roads.png`
- `docs/assets/010_death/processed_png/focus_death_another_shoreline.png`
- `docs/assets/010_death/processed_png/focus_death_no_ferry_returns.png`
- `docs/assets/010_death/processed_png/focus_death_wasteland_roads.png`
- `gfx/interface/goals/010_death/focus_death_black_census.dds`
- `gfx/interface/goals/010_death/focus_death_no_graves_needed.dds`
- `gfx/interface/goals/010_death/focus_death_first_ghost_muster.dds`
- `gfx/interface/goals/010_death/focus_death_public_death.dds`
- `gfx/interface/goals/010_death/focus_death_tide_learns_roads.dds`
- `gfx/interface/goals/010_death/focus_death_another_shoreline.dds`
- `gfx/interface/goals/010_death/focus_death_no_ferry_returns.dds`
- `gfx/interface/goals/010_death/focus_death_wasteland_roads.dds`
- `docs/assets/010_death/contact_sheets/death_focus_icons_batch_2026_06_16_regen.png`

## Asset notes

- All 8 icons were regenerated from new source compositions through `image_gen`, not from prior Death focus assets.
- The batch was pushed away from repeated medallion/same-symbol reads by keeping each center subject distinct:
- `focus_death_black_census`: black ledger with erased-name rows
- `focus_death_no_graves_needed`: sealed ossuary door with ledgers replacing graves
- `focus_death_first_ghost_muster`: pale host silhouettes mustering under a dead banner
- `focus_death_public_death`: mainland map with black spread border and public alarm bell
- `focus_death_tide_learns_roads`: black tide overtaking road lines
- `focus_death_another_shoreline`: second coast surf and landing
- `focus_death_no_ferry_returns`: empty ferry approach under dark harbor light
- `focus_death_wasteland_roads`: ruined road and broken milestones in wasteland

## Validation

- Verified all 8 processed PNGs exist and are exactly `94x86`.
- Verified all 8 DDS files exist and are exactly `94x86` `ARGB8888`.
- Verified chroma-key removal produced real transparency for the processed PNG set.
- Verified the batch contact sheet exists at `docs/assets/010_death/contact_sheets/death_focus_icons_batch_2026_06_16_regen.png`.
- Verified scope stayed bounded to the assigned 8 icons, one batch contact sheet, and this handoff.

## Blockers

- None.

## Intentionally untouched

- Shared `generated_art_manifest.md`
- Shared `generated_art_gfx_handoff.md`
- Shared all-icons contact sheets
- Gameplay, localisation, `.gfx`, and focus tree files
