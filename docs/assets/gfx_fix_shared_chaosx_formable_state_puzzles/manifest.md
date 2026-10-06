# Shared formable state-puzzle asset manifest

Status: 272 approved texture repairs, eight parent-applied GUI positions, nine canonical manifests, and all 382 declared processed-PNG paths are reconciled.

The source review plan is `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md`, section `shared_chaosx_formable_state_puzzles` at lines 1206-1216.

Parent approval on 2026-10-06 covers the 272 v3 candidate PNGs, the nine registered-coordinate puzzle mosaics, all 15 paired texture sheets, and the eight island-marker details.

The original authored source PNGs for the 272 changed runtime textures were absent, so the pre-repair DDS files were frozen under `source_runtime/` and decoded to lossless RGBA PNG sources under `source_runtime_png/` before palette or ring processing. The pre-write snapshot found all 382 processed-PNG paths referenced by the nine manifests absent, with zero canonical processed PNGs available to preserve.

The five palette families contain 260 textures across 130 states: 28 in `form_baltic_federation_category`, 82 in `form_baltic_sea_empire_category`, 56 in `form_north_sea_category`, 58 in `form_scandinavia_category`, and 36 in `form_sweden_hungary_category`.

Their unresolved and qualifying variants preserve their own original alpha planes while using the accepted shared puzzle palette from `.tools/repair_event6_state_puzzle_assets.py`: unresolved fill RGB `(98, 101, 108)`, hatch `(66, 69, 75)`, outline `(151, 154, 161)`, period 6; qualifying fill `(70, 148, 103)`, outline `(25, 56, 45)`, and keyline `(155, 216, 165)`.

Eight states have 12px status-colored transparent rings and 16 affected variants; four variants are already included in the 260 palette outputs, so the combined runtime promotion contains 272 unique textures.

The eight state canvases are North Sea 932 `15x15`, Scandinavia 910 `15x15`, GOE Hindustan 320 `15x15`, GOE Hindustan 321 `15x16`, GOE Hindustan 985 `15x16`, Maghreb 783 `15x15`, Greater Italy 116 `15x16`, and Latin Africa 796 `16x16`.

Each palette candidate preserves the exact binary state silhouette and its own variant alpha plane; each ring candidate preserves its processed core byte-for-byte after padding, and the added ring occupies the exterior transparent canvas.

The two severity-2 Event006 findings are already implemented by commit `1cb4d061f` and were reused unchanged: four FORM11 textures for states 234 and 245, plus six FORM18 textures for states 413, 676, and 1001.

All 382 processed-PNG paths declared by the five palette-family manifests and the Maghreb, Greater Italy, and Latin Africa manifests now exist. The 266 affected paths contain the parent-approved v3 candidates, and the other 116 contain pixel-identical decodes of their unchanged runtime DDS files; their provenance explicitly says they are not original source layers. The three custom manifests now have per-variant `png_sha256` maps for all 61 path-backed states. The GOE Hindustan manifest has no processed-PNG field, so its six candidate PNGs remain in this asset workspace without a fabricated canonical path.

The Friesland FORM03 state 36 twins remain byte-identical to their baseline and were accepted as real islets for provinces 6336, 9335, and 11318.

## Evidence files

- `input_inventory_v2.json` records all pre-promotion source snapshots, runtime baseline hashes, exact dimensions, masks, and ring-state GUI positions.
- `processed_v3/puzzle_candidates_v3.json` enumerates the 272 processed PNGs and their sources.
- `processed_v3/candidate_audit_v3.json` verifies source hashes, candidate hashes, exact per-variant alpha planes, exact ring cores, and accepted palette output.
- `processed_v3/dds_conversion_v3.json` records the standard converter and exact BGRA DDS headers for all 272 outputs.
- `processed_v3/dds_roundtrip_v3.json` records exact DirectXTex DDS-to-PNG pixel equality for all 272 outputs.
- `processed_v3/promotion_v3.json` is the authoritative per-texture runtime path, current sprite name, target GFX file, before hash, final hash, dimensions, and repair type.
- `processed_v3/contact_sheet_inventory_v3.json` hashes all 99 baseline, approved-candidate, and post-promotion review sheets.
- `canonical_manifest_validation_v2.json` verifies all nine canonical digests and all 382 processed-PNG paths and hashes.
- `owned_changed_paths_v1.json` enumerates exact owned runtime, manifest, processed-PNG, report, and provenance paths; parent-owned GUI edits and untouched Event006 files are excluded from the worker-owned list.
- `canonical_manifest_reconcile_final_v1.json` is the final handoff index for runtime DDS hashes, canonical manifest validation, all eight current GUI coordinates, and MCP transport results.
- `canonical_prewrite_snapshot_v1.json` records the nine original manifests and the absence of all original canonical processed PNGs before this repair.
- `canonical_manifest_patch_v3.patch` and `canonical_preview_restore_v1/manifest_hash_patch.patch` show the surgical manifest updates.
- `canonical_preview_restore_v1/preview_restore_candidates.json` records the 116 preview decode candidates before they were installed.
- `canonical_preview_restore_v2.json` records the installed 116 DDS-derived previews and final manifest hashes.
- `mosaics_v3/mosaic_review_index_v3.json` links the nine before/candidate mosaics at registered coordinates and the eight-state detail sheet.
- `contact_sheets/candidate_pairs_v3/index.json` links the 15 pages covering all 130 palette state pairs.
- `contact_sheets/after_dds_runtime_v3/` contains the narrowed `.tools/gfx/gfx.py sheet` output for the promoted runtime group.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/graphics_icons_20261006.md` and `docs/assets/006_independence_wave/takeover_20261006_icons/` contain the accepted FORM11/FORM18 and state-36 evidence.

## Processing and validation

All 272 changed assets use the repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` with DirectXTex, one mip level, and uncompressed BGRA32.

The post-conversion audit passed 272 of 272 file headers, dimensions, lengths, alpha ranges, and exact pixel roundtrips.

The approved mosaics use only the registered masks and positions from the existing puzzle manifests; no geography was generated or moved.

Native ImageGen was not used for these pixel-exact map pieces because it would alter verified state silhouettes; palette and marker work was deterministic and source-derived.

All eight parent-applied GUI positions match the approved padded-origin offsets in the local `.gui` sources. The parent attempted before/after MCP inspection and render for all six windows, and every route returned `Transport closed`; no live GUI render is claimed.

All 382 processed-PNG paths declared by the five palette families and the Maghreb, Greater Italy, and Latin Africa manifests now exist. The first 266 are approved v3 candidate outputs; the other 116 are pixel-identical PNG decodes of unchanged current runtime DDS files. The GOE Hindustan manifest has no processed-PNG fields, so its six ring candidate PNGs remain in the asset workspace without invented canonical paths.

The canonical `source_png` files were absent and remain absent; the 116 restored previews are explicitly DDS-derived and are not original source layers.

No commit was made by this asset worker.
