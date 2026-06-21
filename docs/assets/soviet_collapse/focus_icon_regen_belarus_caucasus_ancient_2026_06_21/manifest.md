# Belarus, Caucasus, and Ancient Focus Icon Regeneration

Date: 2026-06-21

Scope: regenerate the 19 requested Soviet Collapse focus icons so they use HOI4-style focus medallion composition, consistent centering, and transparent focus-icon corners.

## Live Outputs

The final DDS files were copied to `gfx/interface/goals/soviet_collapse/` with these filenames:

- `ancient_aln_every_pass_border.dds`
- `ancient_aln_mountain_claims.dds`
- `ancient_khw_delta_without_center.dds`
- `ancient_khw_water_claims.dds`
- `ancient_kzr_road_beyond_caspian.dds`
- `ancient_kzr_steppe_levy.dds`
- `ancient_sog_cities_beyond_desert.dds`
- `ancient_sog_merchant_claims.dds`
- `blr_soviet_collapse_forest_can_govern.dds`
- `blr_soviet_collapse_national_council_minsk.dds`
- `blr_soviet_collapse_quiet_recognition_letters.dds`
- `caucasus_soviet_collapse_ancient_caucasus_crowns.dds`
- `caucasus_soviet_collapse_ancient_thrones_mountains.dds`
- `caucasus_soviet_collapse_border_faiths_nations.dds`
- `caucasus_soviet_collapse_caucasus_stands.dds`
- `caucasus_soviet_collapse_civilian_oil_oversight.dds`
- `caucasus_soviet_collapse_national_restoration_councils.dds`
- `caucasus_soviet_collapse_oil_not_government.dds`
- `caucasus_soviet_collapse_route_fork.dds`

## Package Contents

- `source_png/`: generated source candidates retained for audit.
- `processed_png/`: final processed PNGs at focus-icon size.
- `dds/`: package copy of final DDS exports.
- `contact_sheets/final_icons.png`: final visual review sheet.
- `manifest.md`: this package manifest.
- `gfx_handoff.md`: wiring and validation handoff.

## Validation

- Checked all 19 live DDS files exist.
- Checked all 19 live DDS files are `94x86`.
- Checked all 19 package DDS files are `94x86`.
- Checked live icon corner alpha values remain transparent.

## Notes

This package contains only static focus icons. No interface `.gfx`, focus-tree, localisation, or gameplay wiring changes were needed because the regenerated assets reuse existing filenames.

No fallback assets or placeholder icons were used.
