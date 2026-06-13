# Holy Realm Dhyana Seal Asset Rebuild Handoff

Date: `2026-06-13`
Scope: rebuild only the Holy Realm meditation charge / Dhyana seal decision icon asset package

## Result

Rebuilt the Dhyana seal decision icon as painterly shrine-medallion art and expanded the animation loop from `8` to `12` subtle frames while keeping the existing sprite names and DDS paths stable.

## Changed files

- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_000_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_001_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_002_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_003_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_004_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_005_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_006_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_007_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_008_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_009_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_010_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/holy_realm_dhyana_seal_011_source.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_000.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_001.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_002.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_003.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_004.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_005.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_006.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_007.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_008.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_009.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_010.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/holy_realm_dhyana_seal_011.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/sheets/holy_realm_dhyana_seal_sheet.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/previews/holy_realm_dhyana_seal_preview.gif`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/previews/holy_realm_dhyana_seal_contact.png`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/notes/holy_realm_dhyana_seal_source_grid.png`
- `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal.dds`
- `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/brief.md`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/frame_plan.md`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/notes/source_prompts.md`
- `docs/assets/003_holy_realm_buddhahood/manifest.md`
- `docs/assets/003_holy_realm_buddhahood/gfx_handoff.md`

## Validation

- Static fallback DDS exists at `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal.dds` with `96x96` dimensions.
- Animated sheet DDS exists at `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds` with `1152x96` dimensions.
- The rebuilt loop has `12` processed `96x96` frames, a review GIF, and a contact sheet.
- The new art direction replaces the old geometry-heavy medallion with painterly shrine-relief lotus art.

## Parent follow-up

- Completed: `interface/003_holy_realm.gfx` now declares `noOfFrames = 12` for `GFX_decision_holy_realm_dhyana_seal_animated`.
- Keep the existing sprite aliases and DDS texture paths unchanged.

## Notes

- Built-in `$imagegen` direct frame edits drifted too far between frames, so the final animation source used one generated `4x3` grid of twelve coherent breath states, then sliced that grid into per-frame source PNGs.
- No gameplay, localisation, decision, scripted GUI, focus, or `.gfx` files were edited in this handoff.
