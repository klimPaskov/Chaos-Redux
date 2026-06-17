# Event 012 Africa Achievement Icons - Archive/Bestiary Batch 3

Date: 2026-06-17

## Scope

This package covers four Event 012 Archive/Bestiary achievement icons:

- `ACH_AFR_NO_COUNTERFEIT_CROWNS`
- `ACH_AFR_THE_FOREST_SIGNED_BACK`
- `ACH_AFR_BAOBAB_FILIBUSTER`
- `ACH_AFR_OLD_SEATS_NEW_UNION`

Each achievement has a completed icon, grey icon, and not-eligible icon. The live files are in `gfx/achievements/` and the package copies are in `docs/assets/012_africa/achievement_icons_archive_bestiary_batch_3/dds/`.

## Source and Processing

The `chaosx_icon_artist` subagent produced generated symbolic source sheets under `source_png/`. The parent completed processing after the worker stalled: one source tile was cropped from each sheet, resized to 64x64, sharpened, given a distinct achievement-specific overlay, and exported to DDS.

Icon treatments:

- `ACH_AFR_NO_COUNTERFEIT_CROWNS`: verified crown seal with red slash.
- `ACH_AFR_THE_FOREST_SIGNED_BACK`: forest-leaf treaty mark on a red seal.
- `ACH_AFR_BAOBAB_FILIBUSTER`: baobab canopy and parliamentary scroll.
- `ACH_AFR_OLD_SEATS_NEW_UNION`: old-seat markers around a union globe.

Proofs:

- `contact_sheets/source_check.png`
- `contact_sheets/source_labeled.png`
- `contact_sheets/final_variants.png`

## Live DDS Files

- `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS.dds`
- `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS_grey.dds`
- `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS_not_eligible.dds`
- `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK.dds`
- `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK_grey.dds`
- `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK_not_eligible.dds`
- `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER.dds`
- `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER_grey.dds`
- `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER_not_eligible.dds`
- `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION.dds`
- `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION_grey.dds`
- `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION_not_eligible.dds`

## Validation

All live DDS files are 64x64 sRGBA DXT5. `interface/chaosx_achievements.gfx` registers normal, `_grey`, and `_not_eligible` sprites for all four IDs.

No white matte or white background was introduced; the icons use dark full-frame achievement backplates with distinct symbolic overlays.
