# Event 020 shared oversized rat counter handoff

Status: `needs_user_review`.

Scope: bounded shared counter audit and package completion for the one oversized rat model used by the reusable `RTA` Rat Nation carrier, separate `RTX` Rat King, and every internal rat subtype. Model geometry, rigging, skeletal animation, audio, gameplay, GFX definitions, country files, and localisation were out of scope and were not edited.

## Result

The pre-existing runtime strips were not visually acceptable against the exact vanilla family because the large normal frame used pale mint values around `#ACC6AC` instead of the sampled vanilla green anchors `#496A49`, `#4A6B4A`, `#537253`, and `#648064`. The prior alternate frames were also sparse line artifacts rather than a clearly readable pale state glyph. The old DDS bytes remain preserved under `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/qa/preexisting_runtime/`.

The selected package reuses the parent-provided original native-alpha ImageGen source atlases, isolates the rat subjects by alpha bounding boxes, smoothly scales them to the exact vanilla canvases, maps the large normal frame to the sampled vanilla-green ramp, maps the land-map pair to the inspected white/grey family, and preserves two adjacent frames with no gap. No canonical reference image was copied, traced, or shipped, and no background-removal fallback was used.

## Exact consumers and runtime paths

| Surface | Existing sprite token(s) | Existing `.gfx` path | Runtime DDS | Canvas and frames |
| --- | --- | --- | --- | --- |
| Large land counter | `GFX_unit_black_plague_rat_shared_base_icon_medium`, `GFX_unit_black_plague_rat_icon_medium` | `interface/chaosx_subuniticons.gfx:461-466` | `gfx/interface/counters/divisions_large/unit_black_plague_rat_shared_base_icon.dds` | `152x42`, two adjacent `76x42` frames, `noOfFrames = 2` |
| Land map counter | `GFX_unit_black_plague_rat_shared_base_icon_medium_white`, `GFX_unit_black_plague_rat_icon_medium_white` | `interface/chaosx_subuniticons.gfx:463-468` | `gfx/interface/counters/divisions_small/onmap_unit_black_plague_rat_shared_base_icon.dds` | `60x12`, two adjacent `30x12` frames, `noOfFrames = 2` |

Frame 0 is the normal state and frame 1 is the alternate/template state. The large normal frame is an original oversized rat silhouette in the sampled muted vanilla-green family. The large alternate frame is a separate pale rat schematic source and is not a white repaint of frame 0. Both map frames use the installed land-map white/grey treatment.

## Package evidence

| Surface | Source | Processed PNG | Evidence DDS | Processed SHA-256 | DDS SHA-256 |
| --- | --- | --- | --- | --- | --- |
| Large land counter | `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/source/rat_large_imagegen_native.png` | `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/processed_png/unit_black_plague_rat_shared_base_icon_152x42.png` | `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/dds/gfx/interface/counters/divisions_large/unit_black_plague_rat_shared_base_icon.dds` | `e5278a3fe40b11152615d66b6ef3c1eccb5a327c870011683be775f86bf4e96c` | `7375b2f472daf60adb98a71c031d178df9fec1936aa0f378a9be20ee84a85ba6` |
| Land map counter | `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/source/rat_map_imagegen_native.png` | `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/processed_png/onmap_unit_black_plague_rat_shared_base_icon_60x12.png` | `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/dds/gfx/interface/counters/divisions_small/onmap_unit_black_plague_rat_shared_base_icon.dds` | `9a0ff0dc3a2f75daad1092a6eefd4d24ae3185a322a0ecdd6e671e13a412fa7d` | `81d6d6b881bf10e5367ae32d0f51708fc044f0434701ba4db16af35ddb30f91` |

Per-frame source crops are retained under `counters/source/frames/`. The processing recipe, alpha-edge rule, palette mapping, and conversion command are recorded in `counters/processing_recipe.md`. Source hashes and crop boxes are recorded in `counters/source/source_manifest.json`.

## Installed-vanilla inspection

The canonical contact sheets were inspected first at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`. The individual reference PNGs were then inspected at `unit_infantry_icon.png` and `onmap_infantry.png` in those same canonical folders.

The exact installed definitions are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx#GFX_unit_infantry_icon_medium` and `#GFX_unit_infantry_icon_medium_white`. Their DDS sources are `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`, both with `noOfFrames = 2`, and their SHA-256 values are recorded in `counters/validation/installed_definition_audit.json`.

The inspected large family uses a `152x42` two-frame strip with a compact muted green normal silhouette and a separate pale alternate glyph. The inspected map family uses a `60x12` two-frame strip with white/grey map-counter treatment. The exact per-frame alpha bounds, RGB extrema, dominant colours, DDS headers, and source hashes are recorded in `counters/validation/installed_definition_audit.json` and `counters/validation/reference_stats.json`.

## DDS and visual evidence

`counters/contact_sheet.png` shows both canonical families, the unchanged source atlases, processed native strips with frame labels, smooth enlarged previews, decoded DDS round-trips, and the superseded runtime strips over checkerboard review backgrounds. The checkerboard is review-only and is absent from all source, processed, and runtime files.

`counters/qa/dds_roundtrip.json` records valid legacy one-level BGRA headers, exact dimensions, exact file lengths, alpha extrema `0..255`, and `pixel_equal = true`, `different_pixels = 0`, `max_channel_difference = 0` for both selected strips. Decoded DDS PNGs are retained at `counters/qa/roundtrip/large_decoded.png` and `counters/qa/roundtrip/map_decoded.png`.

The final DDS files were produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using `--width 152 --height 42` and `--width 60 --height 12`. The installed runtime copies are byte-identical to the evidence DDS files.

## Changed files

- Replaced `gfx/interface/counters/divisions_large/unit_black_plague_rat_shared_base_icon.dds` with the selected bespoke strip.
- Replaced `gfx/interface/counters/divisions_small/onmap_unit_black_plague_rat_shared_base_icon.dds` with the selected bespoke strip.
- Updated `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/manifest.md` and `history.md` with the selected counter status and old-runtime comparison.
- Added `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/counters/manifest.md`, `gfx_handoff.md`, `contact_sheet.png`, `processing_recipe.md`, and `source/imagegen_provenance.md`.
- Added immutable source-frame crops, processed frame PNGs and strips, evidence DDS copies, pre-existing runtime copies, decoded round-trip PNGs, `dds_roundtrip.json`, `installed_definition_audit.json`, `reference_stats.json`, and `source_manifest.json` under the counter package.
- Added this handoff at `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-24_event020_rat_counter_handoff.md`.

No `.gfx`, gameplay, 3D model, animation, audio, country, event, focus, decision, localisation, or spreadsheet file was changed. No copied vanilla counter, flag, third rat tag, subtype-specific counter, or generic placeholder was introduced.

## Remaining review

The package is complete for source, processing, conversion, and local evidence, but remains `needs_user_review` until the parent visually accepts `counters/contact_sheet.png` and the user validates the live HOI4 consumer. This handoff does not claim in-game completion, model completion, animation completion, or audio completion.
