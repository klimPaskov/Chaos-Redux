# `fm_pic_displacement` GFX Handoff

## Final asset

- Final DDS: `gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds`
- Dimensions: 114×101 pixels.
- Format: opaque, one-level uncompressed BGRA8 DDS with no mipmaps.
- Proposed sprite name: `GFX_fm_pic_displacement`.
- Target GFX file: `interface/famine_and_migration_system.gfx`.
- Decision-category consumer: the shared famine and migration category's `picture` field, parent-owned.

## Copy-ready sprite definition

```text
spriteType = { name = "GFX_fm_pic_displacement" texturefile = "gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds" }
```

This handoff does not edit `interface/famine_and_migration_system.gfx`. The existing `GFX_fm_cat_displacement` sprite is the separate 52×40 category button icon and must not be used for the 114×101 picture surface.

## Review evidence

Source, processed preview, prompt record, manifest, and contact sheet are in `docs/assets/famine_and_migration_system/category_picture/`. The canonical reference family and live vanilla/Chaos consumer evidence are recorded in `manifest.md`.
