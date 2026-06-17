# 012 Africa Goal Icon Regeneration Handoff

## Scope completed

Only `goal_africa_political_congress` was completed in this narrowed pass.

Completed file:

- `gfx/interface/goals/012_africa/goal_africa_political_congress.dds`

Evidence package:

- `docs/assets/012_africa/icon_regen_goals/source_png/goal_africa_political_congress_source.png`
- `docs/assets/012_africa/icon_regen_goals/source_png/goal_africa_political_congress_selected_tile.png`
- `docs/assets/012_africa/icon_regen_goals/processed_png/goal_africa_political_congress_tile_cutout.png`
- `docs/assets/012_africa/icon_regen_goals/processed_png/goal_africa_political_congress.png`
- `docs/assets/012_africa/icon_regen_goals/contact_sheets/goal_africa_political_congress_checker_preview.png`
- `docs/assets/012_africa/icon_regen_goals/manifest.md`
- `docs/assets/012_africa/icon_regen_goals/gfx_handoff.md`

## Production notes

- Source mode remained `imagegen` as requested.
- In this session, imagegen returned the congress concept as a variant sheet rather than a single isolated export.
- One congress-emblem tile was selected from the generated sheet and processed into the final transparent focus icon.
- The old opaque white matte problem was removed by cutting the selected tile to alpha and rebuilding the 94x86 focus canvas with transparent unused pixels.

## Validation

- Final DDS exists at `gfx/interface/goals/012_africa/goal_africa_political_congress.dds`.
- Final DDS dimensions verified: `94x86`.
- Final processed PNG dimensions verified: `94x86`.
- Corner alpha verified on the processed PNG: all four corners were `0`.
- Checker preview created to verify transparent edges and confirm there is no white square matte.

## Reassigned / not touched here

The remaining Africa goal icons were reassigned to other subagents and were not generated, processed, or replaced in this pass.

- `goal_africa_archive_old_seats.dds`
- `goal_africa_authority_atlas.dds`
- `goal_africa_charter_league_diplomacy.dds`
- `goal_africa_charter_league_emblem.dds`
- `goal_africa_high_chaos_bestiary.dds`
- `goal_africa_industry_logistics.dds`
- `goal_africa_liberation_war_office.dds`
- `goal_africa_military_forces.dds`
- `goal_africa_regional_integration.dds`
- `goal_africa_scramble_for_africa.dds`
- `goal_africa_sponsor_paths.dds`
- `goal_africa_world_order_route.dds`

## Files not edited

- No idea icons were edited.
- No script, localisation, `.gfx`, or other gameplay files were edited.
- No git commit or staging actions were performed.

## Parent follow-up, 2026-06-17

The live `goal_africa_political_congress.dds` was superseded after parent review. The narrowed-pass source removed the matte but read as an ornate seal rather than a political congress. The parent regenerated a congress-table source, processed it through `docs/assets/012_africa/icon_regen_parent_cleanup/`, and replaced the DDS in place while keeping `GFX_goal_africa_political_congress` and the existing `.gfx` path unchanged.
