# Event 018 arrow repack handoff

Date: 2026-08-21

Status: complete for the bounded technical repack; parent-owned `.gfx` registration remains pending.

## Scope and source

This handoff covers only the two final runtime navigation-control DDS files requested for Event 018. The visual bytes are installed-vanilla reuse, not generated art.

The exact installed sources were:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/arrow_left_small.dds`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/arrow_right_small.dds`

The canonical `assets/vanilla_reference` library README and catalog were inspected. It has no navigation-control/arrow reference family or matching contact sheet, so the exact installed source DDS files above are the authoritative visual references. No project-local visual-reference copy, compatibility shelf, or alternate parent asset directory was used.

## Runtime files and hashes

All hashes below are SHA-256. The processed PNGs were temporary evidence under `.tmp/event018_arrow_repack` and were deleted after this handoff recorded their hashes and validation results.

| Asset | Installed source | Temporary processed PNG | Final runtime DDS | Source DDS SHA-256 | PNG SHA-256 | Final DDS SHA-256 | Decoded RGBA SHA-256 | Alpha min/max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Left arrow | `gfx/interface/arrow_left_small.dds` | `.tmp/event018_arrow_repack/arrow_left_small.png` | `gfx/interface/018_resources_found/resources_found_arrow_left.dds` | `08723324ffe18cee48aef75bd15e6ca71c9c542df6a4a439da509baf5c327eae` | `cc80ff9c794f56bcf8b05fac7ce9d2653b08e990f26ec6f26e37535a60ea7232` | `fd63d147a59fdbeb1eae5c53c66e51f7785c9e001a76fb3776592b782ffa4f66` | `0def2cfdf4e86ba8dbb161f2d967d375fd73c85eb1355643a71e6e3c0cb8674c` | `0 / 255` |
| Right arrow | `gfx/interface/arrow_right_small.dds` | `.tmp/event018_arrow_repack/arrow_right_small.png` | `gfx/interface/018_resources_found/resources_found_arrow_right.dds` | `4e134e823e28b51f97c2493a52973e9fd831aea26bb797567b583dbad0b2e5bb` | `e33935d1eab34e6392354db4665dd5ea5a654e07cb73cf0074c4b7e1798f5ce1` | `43f70bb12782a50f5dffd7c080edcf333fd390ab2b072c4fa1f6e66b6dc135b2` | `b4635bd2a0e9c873946f9c4ad385c3a053ecc9fa2b8b5a62060e0ce186789ae9` | `0 / 255` |

## Processing and validation

- Each installed DDS was decoded losslessly at native `24x24` to an RGBA PNG with Pillow. The source DDS, processed PNG, and final DDS decoded RGBA pixels are byte-equal for each arrow.
- Each final DDS was written only with `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed.png> --output <final.dds> --width 24 --height 24`.
- Both final files are exactly `2432` bytes (`128 + 24 * 24 * 4`).
- Both final files have the exact 128-byte legacy header: magic `DDS `, `DDS_HEADER` size `124`, flags `4111` (`DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PITCH | DDSD_PIXELFORMAT`), width `24`, height `24`, row pitch `96`, and zero mipmaps.
- Both final files have `DDS_PIXELFORMAT` size `32`, flags `65`, fourCC `0`, 32-bit channels, and masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`.
- Both final files have `DDSCAPS_TEXTURE` `0x1000`, zero secondary caps, and full decoded alpha range `0..255`.
- The installed source headers declared an invalid row pitch of `2304`; the repack corrects this header field to the standards-compliant `96` without changing any decoded pixel.
- Temporary decoded PNGs and JSON validation evidence were removed after the durable hashes and checks above were recorded. No temporary event asset workspace remains.

## Ownership and wiring boundary

Only these runtime files and this durable handoff were changed by this subtask. `interface/018_resources_found.gfx`, GUI files, scripts, localisation, and all other gameplay or asset files were not edited. The parent agent must register the two stable runtime texture paths in the existing Event 018 GFX definition and perform any consumer-level validation.

## Blockers and review

No blocker or fallback was used for the technical repack. ImageGen, recolouring, redrawing, resizing, frame creation, background removal, and substitute assets were not used. Parent-owned `.gfx` registration is the only remaining integration step.
