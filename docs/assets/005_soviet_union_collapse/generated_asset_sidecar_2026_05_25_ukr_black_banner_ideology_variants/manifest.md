# Event 005 Generated Asset Sidecar Manifest

Event id: `005`

Event slug: `soviet_union_collapse`

Package: `generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants`

Scope: docs-only generated source coverage for `UKR_BLACK_BANNER` ideology route flags. This sidecar did not edit gameplay, localisation, interface `.gfx`, GUI, history, country, focus, decision, event, spreadsheet, active `gfx/flags`, or active leader files.

## Reference And Current-State Audit

- Required repo instructions and the Event 005 asset skill were read before asset work.
- Matching flag references were inspected from `.agents/skills/chaos-redux-event-assets/assets/flags/`.
- Existing Event 005 generated handoff inspected: `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25/manifest.md`.
- Existing flag correction package inspected: `docs/assets/005_soviet_union_collapse/remaining_custom_flag_correction/manifest.md`.
- Current leader directory check found `47` `gfx/leaders/005_soviet_collapse/*_leader.dds` files, with basic source-sidecar coverage for all checked tags.
- Current active `UKR_BLACK_BANNER` flag files already exist in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`; they were not overwritten.

## Why Generation Is Appropriate

`UKR_BLACK_BANNER` is a fictional route/cosmetic flag identity for a high-chaos Ukrainian black-banner branch. It is not a vanilla `UKR` default override and does not require historical sourcing. Generation is appropriate because the requested coverage is fictional, alternate-history, symbolic route-flag art.

## Generated Assets

Status: `handed_off`

| Asset | Type | Source mode | Source PNG | Processed PNG previews | Sidecar TGA outputs | Active final path if parent accepts later replacement | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `UKR_BLACK_BANNER_communism` | fictional route ideology flag | `image_gen` | `source_png/ukr_black_banner_ideology_variants_source_sheet.png` | `processed_png/UKR_BLACK_BANNER_communism_normal.png`, `processed_png/UKR_BLACK_BANNER_communism_medium.png`, `processed_png/UKR_BLACK_BANNER_communism_small.png` | `tga/UKR_BLACK_BANNER_communism.tga`, `tga/UKR_BLACK_BANNER_communism_medium.tga`, `tga/UKR_BLACK_BANNER_communism_small.tga` | `gfx/flags/UKR_BLACK_BANNER_communism.tga`, `gfx/flags/medium/UKR_BLACK_BANNER_communism.tga`, `gfx/flags/small/UKR_BLACK_BANNER_communism.tga` | Worker council, forge, and sheaf motif. |
| `UKR_BLACK_BANNER_democratic` | fictional route ideology flag | `image_gen` | `source_png/ukr_black_banner_ideology_variants_source_sheet.png` | `processed_png/UKR_BLACK_BANNER_democratic_normal.png`, `processed_png/UKR_BLACK_BANNER_democratic_medium.png`, `processed_png/UKR_BLACK_BANNER_democratic_small.png` | `tga/UKR_BLACK_BANNER_democratic.tga`, `tga/UKR_BLACK_BANNER_democratic_medium.tga`, `tga/UKR_BLACK_BANNER_democratic_small.tga` | `gfx/flags/UKR_BLACK_BANNER_democratic.tga`, `gfx/flags/medium/UKR_BLACK_BANNER_democratic.tga`, `gfx/flags/small/UKR_BLACK_BANNER_democratic.tga` | Village assembly, sun, and sheaf motif. |
| `UKR_BLACK_BANNER_fascism` | fictional route ideology flag | `image_gen` | `source_png/ukr_black_banner_ideology_variants_source_sheet.png` | `processed_png/UKR_BLACK_BANNER_fascism_normal.png`, `processed_png/UKR_BLACK_BANNER_fascism_medium.png`, `processed_png/UKR_BLACK_BANNER_fascism_small.png` | `tga/UKR_BLACK_BANNER_fascism.tga`, `tga/UKR_BLACK_BANNER_fascism_medium.tga`, `tga/UKR_BLACK_BANNER_fascism_small.tga` | `gfx/flags/UKR_BLACK_BANNER_fascism.tga`, `gfx/flags/medium/UKR_BLACK_BANNER_fascism.tga`, `gfx/flags/small/UKR_BLACK_BANNER_fascism.tga` | Militarized spear and wheat motif; no real extremist symbol. |
| `UKR_BLACK_BANNER_neutrality` | fictional route ideology flag | `image_gen` | `source_png/ukr_black_banner_ideology_variants_source_sheet.png` | `processed_png/UKR_BLACK_BANNER_neutrality_normal.png`, `processed_png/UKR_BLACK_BANNER_neutrality_medium.png`, `processed_png/UKR_BLACK_BANNER_neutrality_small.png` | `tga/UKR_BLACK_BANNER_neutrality.tga`, `tga/UKR_BLACK_BANNER_neutrality_medium.tga`, `tga/UKR_BLACK_BANNER_neutrality_small.tga` | `gfx/flags/UKR_BLACK_BANNER_neutrality.tga`, `gfx/flags/medium/UKR_BLACK_BANNER_neutrality.tga`, `gfx/flags/small/UKR_BLACK_BANNER_neutrality.tga` | Field committee, saber, grain, and open-field motif. |

## Contact Sheet

- `contact_sheets/ukr_black_banner_ideology_variants_contact.png`

## Validation Summary

- Normal previews: `82x52`.
- Medium previews: `41x26`.
- Small previews: `10x7`.
- Sidecar TGA outputs: uncompressed type `2`, `32` bpp, descriptor `8`.
- Orientation: generated sheet and processed previews visually decode upright.
- Active files: no active `gfx/flags` file was modified by this sidecar.

## Remaining Blocked Or Approval-Gated Items

- `PRA` flag visual-quality redo remains approval-gated because active `gfx/flags/PRA*.tga` files are dirty and this is a design-quality call rather than a deterministic missing-file blocker.
- `MFR` ideology-variant polish remains approval-gated because active `gfx/flags/MFR_*.tga` files are dirty and replacement would overwrite active work.
- `OGB` ideology variants remain blocked without explicit parent approval because prior manifest notes say the repository-preferred/restored OGB set should be preserved.
- No new leader portrait package was generated because current active Event 005 leader DDS files and basic source sidecars are present.
