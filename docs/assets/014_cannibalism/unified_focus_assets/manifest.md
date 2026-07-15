# Event 014 Unified Focus Icon Manifest

All 108 focuses in `common/national_focus/014_cannibalism_unified_focus.txt` have a distinct generated icon package and a final runtime texture.

## Contract

- Generated sources: `source_png/goal_<focus_id>_source.png`
- Chroma-cleaned intermediates: `alpha_png/goal_<focus_id>_alpha.png`
- Exact processed masters: `processed_png/goal_<focus_id>.png`
- Package DDS copies: `dds/goal_<focus_id>.dds`
- Runtime DDS: `gfx/interface/goals/014_cannibalism/goal_<focus_id>.dds`
- Final size: 94x86
- Final format: uncompressed one-image-level 32-bit BGRA with true alpha

The processor derives the authoritative list directly from the 108 unique `CBL_` focus IDs, refuses missing sources, rejects duplicate normalized artwork, removes visible key green, validates transparent corners and partial-alpha edges, confirms the DDS masks and dimensions, and verifies that package/runtime DDS files are hash-identical.

## Proof and review

- Per-asset paths, source/intermediate/final hashes, alpha counts, DDS sizes, and normalized uniqueness: `validation/unified_focus_asset_validation.tsv`
- Exact sprite/path handoff: `validation/unified_focus_gfx_handoff.tsv`
- Generated-source review: `contact_sheets/unified_focus_sources_contact_sheet.png`
- Processed-alpha review: `contact_sheets/unified_focus_processed_checker_contact_sheet.png`
- Runtime DDS decode review: `contact_sheets/unified_focus_dds_decoded_contact_sheet.png`

The terminal icons for `CBL_consume_the_counterwar`, `CBL_final_global_mobilization`, and `CBL_dismantle_the_ordinary_world` were generated after the first 105-source tranche and are documented in `prompts/final_additions.md`. They are not substitutes or reused art.
