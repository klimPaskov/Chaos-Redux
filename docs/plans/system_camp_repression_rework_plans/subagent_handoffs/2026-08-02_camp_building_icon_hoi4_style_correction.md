# Camp building icon HOI4-style correction

Status: complete; visual review result: HOI4-style PASS.

The runtime strip payload was subsequently recovered by `2026-08-03_building_icon_strip_recovery.md`; this handoff retains the accepted camp-art review and provenance, while its former full-strip checksum is historical.

## Changed runtime files

- `gfx/interface/buildings/building_icon_strip.dds` — 35 frames, 1610x46; only frames 34 and 35 replaced.
- `gfx/interface/buildings/building_concentration_camp.dds` — bespoke standalone 27x23.
- `gfx/interface/buildings/building_extermination_camp.dds` — bespoke standalone 27x23.

## Source mode and prompt evidence

Built-in ImageGen was used for every source. Strip prompts and source PNGs are retained in `docs/assets/system_camp_building_icons_hoi4_style/`. Standalone pair were separately generated on flat green chroma key, cleaned with `remove_chroma_key.py`, and processed independently to 27x23; neither is a crop or resize of strip art.

## Exact references

Inspected canonical `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/buildings/contact_sheet.png` and the matching buildings folder before generation. Decoded installed vanilla strip frames 1, 2, 3, 5, 9, 11, 13, 30, and 31 plus current mod frames 32 and 33. Compared native 46x46 and nearest-neighbour enlargement. Confirmed standalone footprint against vanilla `building_fort_icon.dds` / canonical `fort.png` at 27x23.

## Before and after behavior

The old frame 34 was a transparent tall watchtower/gate render and the old frame 35 a transparent grayscale industrial render, both outside the GFX_buildings_strip visual language. Frame 34 is now a compact charcoal tile with an ochre watchtower/gate and barbed fence. Frame 35 is now a compact charcoal tile with two low furnace halls, a chimney, and a barbed fence. The standalone aliases now use independently generated transparent pictograms with the same ochre/charcoal palette and native 27x23 footprint.

## Checksums and strip preservation

- The accepted camp frame payloads remain the source for frames 34 and 35; the current full-strip checksum is recorded in `2026-08-03_building_icon_strip_recovery.md`.
- Final concentration DDS SHA-256: `c3373e5ab84b931bd9e4a6764c2057d4738890b08b80df4855a1c2c405d2db7a`.
- Final extermination DDS SHA-256: `0cdd6fe3ba7cfa2e6a66553f80872a2607fa7f1b764b67165e4b2e39e322f16b`.
- DDS header validation: all have 128-byte legacy headers, dimensions 1610x46 / 27x23 / 27x23, exact lengths 296368 / 2612 / 2612, BGRA masks, `DDSCAPS_TEXTURE` 0x1000, and alpha extrema 0..255.

## Review evidence

`2026-08-02_camp_building_icon_hoi4_style_correction_contact_sheet.png` in this handoff folder is the permanent corrected comparison sheet, showing direct vanilla reference frames, existing frames 32-33, new frames 34-35, standalone icons at native size and nearest-neighbour 5x, plus an explicit PASS/FAIL rubric. `manifest.json`, `source_atlas_imagegen.png`, processed previews, prompts, and source PNG evidence remain in the temporary workspace.

## Skipped validation and remaining risks

No Hearts of Iron IV launch or live consumer validation was performed; parent/user owns that gate. No `.gfx`, `.gui`, gameplay, localisation, or spreadsheet files were edited. Parent should confirm any intended standalone consumer remains the established 27x23 footprint.

## Parent duties

Keep existing sprite names and `.gfx` paths unchanged. Promote durable facts if needed, review the corrected comparison sheet, and remove the temporary asset workspace only after acceptance.
