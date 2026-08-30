# Event 34 inherited-crash achievement icon handoff

Status: art package complete and ready for parent integration review; parent visual acceptance and final runtime wiring remain outside this subtask.

## Scope and consumer

- Achievement id: `chaos_redux_034_the_long_fall`.
- Consumer: inherited Event 34 Evolution III crash into Event 35 Great Depression recovery.
- Runtime root: `gfx/achievements/`.
- Existing sprite names observed without editing the GFX file: `GFX_achievement_034_the_long_fall`, `GFX_achievement_034_the_long_fall_grey`, and `GFX_achievement_034_the_long_fall_not_eligible` in `interface/035_great_depression.gfx`.
- Suggested target GFX file: `interface/035_great_depression.gfx`.
- The parent owns final sprite/achievement definition review and live consumer validation.

## Runtime files and state semantics

| State | Runtime DDS | Source layer | Processed review PNG | Sprite name |
| --- | --- | --- | --- | --- |
| Completed | `gfx/achievements/chaos_redux_034_the_long_fall.dds` | `docs/assets/035_great_depression/source/achievements/eligible/chaos_redux_034_the_long_fall.png` | `docs/assets/035_great_depression/processed/achievements/chaos_redux_034_the_long_fall_eligible.png` | `GFX_achievement_034_the_long_fall` |
| Grey | `gfx/achievements/chaos_redux_034_the_long_fall_grey.dds` | `docs/assets/035_great_depression/source/achievements/grey/chaos_redux_034_the_long_fall.png` | `docs/assets/035_great_depression/processed/achievements/chaos_redux_034_the_long_fall_grey.png` | `GFX_achievement_034_the_long_fall_grey` |
| Not eligible | `gfx/achievements/chaos_redux_034_the_long_fall_not_eligible.dds` | `docs/assets/035_great_depression/source/achievements/not_eligible/chaos_redux_034_the_long_fall.png` | `docs/assets/035_great_depression/processed/achievements/chaos_redux_034_the_long_fall_not_eligible.png` | `GFX_achievement_034_the_long_fall_not_eligible` |

All runtime files are exact 64x64 root-only achievement DDS files.

## Visual direction and source provenance

The original composition is a distinct industrial skyline descending into broken, idle works, with a single amber relit plant and a repaired gold rail line as the recovery thread.

The completed master was generated through the official built-in ImageGen route with a genuine transparent background in the initial call and is retained at `docs/assets/035_great_depression/generated_sources/achievement_034_the_long_fall_native.png`.

Grey is the same composition in steel-grey and charcoal with extinguished lights and an integrated steel shutter/lock emblem.

Not eligible is the grey composition with a dark-crimson X.

The grey and not-eligible first edits returned opaque checkerboards and were rejected; those untouched failed attempts remain at `generated_sources/achievement_034_the_long_fall_grey_checkerboard_rejected.png` and `generated_sources/achievement_034_the_long_fall_not_eligible_checkerboard_rejected.png`.

The accepted transparent repairs remain at `generated_sources/achievement_034_the_long_fall_grey_transparency_edit.png` and `generated_sources/achievement_034_the_long_fall_not_eligible_transparency_edit.png`.

Full prompts, ImageGen output lineage, and all source hashes are recorded in `docs/assets/035_great_depression/notes/achievement_034_the_long_fall_imagegen_prompts.md`.

## Checksums and alpha evidence

| State | Source SHA-256; size; alpha; visible bbox | Processed PNG SHA-256; size; alpha; visible bbox | Runtime DDS SHA-256; size; alpha; bytes |
| --- | --- | --- | --- |
| Completed | `82571581C4F745DCC85BE6204DF4CEC9227DA101FD6967518D8DB0B62CC55CE6`; 64x64; 0-255; `(2, 4, 62, 60)` | `D53335E2E9E3DEFD1C1EF77A441765FD81706830E3A95B6E1A3D8DCEDE5E8E18`; 64x64; 254-255; `(0, 0, 64, 64)` | `051CFB1A74B7C8B1FCDA27FE25AC3377E7FD600E6BD96E8112944F0C38A8D44A`; 64x64; 254-255; 16512 |
| Grey | `0903A69A33328A6F76BE2FEC428CCFD2FB3CF68058F8C6C30AC9B29651C06CE3`; 64x64; 0-255; `(2, 3, 62, 60)` | `DA7F3CE8FC55F0989F7287B68A5D5C2C916ABF36DAD677271D85F6923B6B821B`; 64x64; 254-255; `(0, 0, 64, 64)` | `56883C069FBAC210D3BA507F72D81D77FA078189825E070A9E7B5373A9C3B909`; 64x64; 254-255; 16512 |
| Not eligible | `B2B86DE66A873501CE5CEBEED3FEFD264E76A49863B05167BB7170248D1B6555`; 64x64; 0-255; `(2, 4, 62, 59)` | `86E55EF7955546ED0E9A404815393A49F89E2BBAA7D6E2A0BB3F083AA5CDAC97`; 64x64; 254-255; `(0, 0, 64, 64)` | `7F0B53DEFA05C5FBA672DEF63AC3D1B2C5469848255E3C689CAD383BA83EFA9D`; 64x64; 254-255; 16512 |

Achievement templates used unchanged by `process_achievement_icons.py` were `achievement_template.png` SHA-256 `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` and `achievement_template_grey.png` SHA-256 `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`.

The unchanged workflow overlay was inspected but not used to derive the not-eligible source layer; its SHA-256 is `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`.

The strict DDS checks passed for every runtime file: legacy header size 124, pixel-format size 32, flags 65, fourCC 0, 32-bit BGRA masks `(0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)`, `DDSCAPS_TEXTURE` `0x1000`, one level, pitch 256, exact length 16512, decoded size 64x64, and decoded pixels equal to the processed PNG.

Native source layers have transparent unused corners and no fake checkerboard; template-backed processed and runtime outputs intentionally cover the full canvas with alpha range 254-255.

## Review evidence

The native-size review sheet is `docs/assets/035_great_depression/contact_sheets/achievement_034_the_long_fall_review.png`, SHA-256 `9D2FF3B06B60292A04ADBB008D080C76359209CD12227E71BC35CC02186FD0A5`.

The sheet was visually inspected at source scale, native 64x64 scale, smooth 4x enlargement, light/dark checker contrast, and decoded DDS round-trip scale.

The completed state reads as a falling industrial works with one warm recovery line, the grey state reads as locked collapse, and the not-eligible state adds an unambiguous red X without clipping or opaque background spill.

## Files changed by this package

- Runtime DDS: `gfx/achievements/chaos_redux_034_the_long_fall.dds`, `gfx/achievements/chaos_redux_034_the_long_fall_grey.dds`, and `gfx/achievements/chaos_redux_034_the_long_fall_not_eligible.dds`.
- Source state PNGs: the three paths in the runtime table.
- Processed state PNGs: the three paths in the runtime table.
- Processor evidence DDS: `docs/assets/035_great_depression/processed/achievement_dds/chaos_redux_034_the_long_fall.dds`, `_grey.dds`, and `_not_eligible.dds`.
- Processor review PNGs: `docs/assets/035_great_depression/processed/achievement_dds/review/chaos_redux_034_the_long_fall.png`, `_grey.png`, and `_not_eligible.png`.
- ImageGen source evidence: the five `achievement_034_the_long_fall*.png` files under `docs/assets/035_great_depression/generated_sources/`.
- Review sheet: `docs/assets/035_great_depression/contact_sheets/achievement_034_the_long_fall_review.png`.
- Documentation: `docs/assets/035_great_depression/icon_manifest.json`, `icon_manifest.md`, `icon_gfx_handoff.md`, `notes/achievement_034_the_long_fall_imagegen_prompts.md`, and this handoff.

No gameplay, localisation, interface, spreadsheet, or GFX files were edited by this package.

## Blockers and follow-up

- No art-production or file-format blocker remains.
- Parent review is still required for visual acceptance and live achievement consumer validation.
- Existing sprite and achievement-definition entries were observed in the workspace but were not modified by this package.
- No simplification, vanilla-art reuse, resized cross-type substitute, or opaque-background final was used.
