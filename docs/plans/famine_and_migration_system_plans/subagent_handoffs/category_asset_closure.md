# Category Asset Closure Handoff

Status: complete pending parent visual/runtime review.

## Scope

This handoff closes the provenance gap for the four installed famine/migration decision-category DDS consumers without changing gameplay or GFX source files.

The exact consumers inspected were `GFX_famine_category` and `GFX_famine_category_picture` in `interface/famine_system.gfx`, `GFX_migration_category` and `GFX_migration_category_picture` in `interface/migration_system.gfx`, and their matching `famine_decision_category` and `migration_decision_category` definitions.

The category icon canvas is 52x40 with native transparency, and the category picture canvas is 114x101 with an opaque full-canvas background matching the inspected canonical `vanilla_reference/icons/decision_categories` and `icons/decision_categories/pictures` families.

## Completed assets

- `famine_category`: generated with official built-in ImageGen using a native transparent background, archived at `docs/assets/famine_and_migration_system/source/category/famine_category.png`, processed at `docs/assets/famine_and_migration_system/processed/category/famine_category.png`, and installed at `gfx/interface/decisions/famine/famine_category.dds`.
- `famine_category_picture`: generated with official built-in ImageGen as an opaque grain-depot and ration-distribution scene, archived at `docs/assets/famine_and_migration_system/category_picture/source_png/famine_category_picture_source.png`, processed at `docs/assets/famine_and_migration_system/category_picture/processed_png/famine_category_picture.png`, and installed at `gfx/interface/decisions/famine/famine_category_picture.dds`.
- `migration_category`: existing source and final output were retained, and its installed icon is now counted alongside the famine icon in the authoritative manifest and icon contact sheet.
- `migration_category_picture`: existing source, processed preview, and final DDS were retained without regeneration, then reconciled with a DDS-decoded round-trip PNG, the shared category-picture contact sheet, and the four-consumer manifest.

## Provenance

The famine icon source was copied unchanged from `C:\Users\klimp\.codex\generated_images\01a03995-ad38-71d3-b1cd-3f563d03790d\exec-f6c786c4-6eba-4b3f-9238-6ef0678d0ba5.png` after native-alpha inspection.

The famine picture source was copied unchanged from `C:\Users\klimp\.codex\generated_images\01a03995-ad38-71d3-b1cd-3f563d03790d\exec-08bc4292-1535-4193-ab0f-d876413702e5.png` after confirming it was an opaque RGB full-canvas scene.

The complete prompt and processing records are retained in `docs/assets/famine_and_migration_system/category_picture/prompts/prompts.md` and `docs/assets/famine_and_migration_system/prompts/imagegen_source_log.md`.

## Validation evidence

The exact checks are recorded in `docs/assets/famine_and_migration_system/category_validation.md`.

All four final DDS files are legacy BGRA8, uncompressed, one-mip outputs with a 128-byte header and exact payload length.

The icon DDS files are 52x40, have alpha extrema 0..255, and have fully transparent corners.

The picture DDS files are 114x101, have alpha extrema 255..255, and have opaque corners.

Pillow DDS decodes for all four outputs are byte-identical to their processed RGBA PNGs after channel conversion.

Round-trip PNGs are retained at `docs/assets/famine_and_migration_system/dds_roundtrip/category/` and `docs/assets/famine_and_migration_system/category_picture/dds_roundtrip/`.

The refreshed review sheets are `docs/assets/famine_and_migration_system/contact_sheets/category_source_processed_roundtrip.png`, `docs/assets/famine_and_migration_system/contact_sheets/category_processed_4x.png`, and `docs/assets/famine_and_migration_system/category_picture/contact_sheets/category_picture_contact_sheet.png`.

## Changed files

- `gfx/interface/decisions/famine/famine_category.dds`
- `gfx/interface/decisions/famine/famine_category_picture.dds`
- `docs/assets/famine_and_migration_system/source/category/famine_category.png`
- `docs/assets/famine_and_migration_system/processed/category/famine_category.png`
- `docs/assets/famine_and_migration_system/category_picture/source_png/famine_category_picture_source.png`
- `docs/assets/famine_and_migration_system/category_picture/processed_png/famine_category_picture.png`
- `docs/assets/famine_and_migration_system/dds_roundtrip/category/famine_category.png`
- `docs/assets/famine_and_migration_system/category_picture/dds_roundtrip/famine_category_picture.png`
- `docs/assets/famine_and_migration_system/category_picture/dds_roundtrip/migration_category_picture.png`
- `docs/assets/famine_and_migration_system/manifest.csv`
- `docs/assets/famine_and_migration_system/gfx_handoff.md`
- `docs/assets/famine_and_migration_system/category_picture/manifest.md`
- `docs/assets/famine_and_migration_system/category_picture/gfx_handoff.md`
- `docs/assets/famine_and_migration_system/category_picture/prompts/prompts.md`
- `docs/assets/famine_and_migration_system/prompts/imagegen_source_log.md`
- `docs/assets/famine_and_migration_system/category_validation.md`
- `docs/assets/famine_and_migration_system/contact_sheets/category_source_processed_roundtrip.png`
- `docs/assets/famine_and_migration_system/contact_sheets/category_processed_4x.png`
- `docs/assets/famine_and_migration_system/category_picture/contact_sheets/category_picture_contact_sheet.png`

No gameplay, decision, localisation, or GFX definition files were edited. No fallback background-removal step was used.

## Hashes

- `famine_category` source: `1dc24ee9225827e0d6d21f793012c9d0005c0cf369185b8f3016d4de29ecacce`.
- `famine_category` processed: `e4a096900323e2fe17c0f3e288139068f2a20afbab79740ab6483fa1fb55e307`.
- `famine_category` final DDS: `2576c06d55fb39573d3353d358165bed6104d1891534be5a7aa97af5c8dc443b`.
- `famine_category_picture` source: `824d567b58fef9f9a6a9a56ce1ef99a60cc5c90d9be11f5ee99cf5f596bda9a9`.
- `famine_category_picture` processed and DDS round-trip PNG: `22f7bd4287006e654314a85bef2733d5ccedd1c9e7f9ef1d5ade32fca2b1c341`.
- `famine_category_picture` final DDS: `369e5d9761d872ccc67d915eab9d162af720f6e9f255212237d54eeb0a8c83fe`.
- `migration_category_picture` retained DDS: `8c6d70b2b110e9b312d123fd358b1f800aa3cc561557067fc88bf18948db089d`.

## Blockers

No production blockers remain. Parent review should confirm the contact-sheet appearance and final in-game category presentation; no source, processing, alpha, dimension, or provenance exception is outstanding.
