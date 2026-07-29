# Event 012 Africa achievement icon validation report

## Result

The source-to-preview evidence package is complete for all 44 matrix keys.

| Check | Result |
| --- | --- |
| Matrix keys audited | 44/44 |
| Source PNGs | 44/44 present at 1254x1254 RGB |
| Keyed intermediates | 44/44 present at 1254x1254 RGBA |
| Processed previews | 132/132 present at exact 64x64 RGBA for normal, grey, and not-eligible states |
| Processed alpha range | 132/132 state previews use 0-255 alpha |
| Processed transparent corners | 132/132 state previews have four transparent corners |
| Visible near-green key pixels at alpha >=16 | 0 across all 44 previews |
| Per-file hash rows | 44 rows in `asset_validation.tsv` |
| Hash inventory | 352 source, keyed, processed PNG, and runtime DDS entries in `hashes.sha256` |
| Review sheets | Source, processed, triplet, and decoded-DDS sheets inspected |
| Runtime DDS triplets | 132/132 installed under `gfx/achievements/` |
| DDS decode and dimensions | 132/132 decode as exact 64x64 uncompressed BGRA DDS |
| DDS-to-PNG pixel equality | 132/132 exact pixel matches |
| Grey-state relation | 44/44 are grayscale with source alpha preserved |
| Not-eligible relation | 44/44 are grey states composited with the canonical red overlay |

## Files and commands

The detailed per-file ledger is `asset_validation.tsv`.

The SHA-256 inventory is `hashes.sha256`.

The source review sheet is `../contact_sheets/africa_achievement_source_contact_sheet.png`.

The processed review sheet is `../contact_sheets/africa_achievement_processed_contact_sheet.png`.

The triplet review sheet is `../contact_sheets/africa_achievement_variants_contact_sheet.png`.

The decoded-DDS review sheet is `../contact_sheets/africa_achievement_dds_decoded_contact_sheet.png`.

The canonical vanilla achievement reference sheet reviewed before processing is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/contact_sheet.png`.

Keyed intermediates were completed with the installed helper at `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` using border auto-key, soft matte, thresholds 12 and 220, and despill.

Processed previews were created by deterministic square 64x64 LANCZOS resizing of the keyed RGBA images.

## Runtime result

The runtime files are the normal, grey, and not-eligible DDS triplets under `gfx/achievements/` using each exact achievement key.

All 132 `africa_*` DDS files are present under `gfx/achievements/`.

The DDS parser confirmed the 124-byte header, 64x64 dimensions, 32-bit BGRA pixel format, one-level payload length, exact processed-PNG pixel equality, grayscale grey states, and canonical red-overlay not-eligible states.

No `.gfx`, gameplay, localisation, or runtime asset file was edited.
