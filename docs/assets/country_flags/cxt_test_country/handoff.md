# CXT test-country flag handoff

## Runtime files

- Normal: `gfx/flags/CXT.tga` (`82x52`).
- Medium: `gfx/flags/medium/CXT.tga` (`41x26`).
- Small: `gfx/flags/small/CXT.tga` (`10x7`).
- Canonical engine identity: country tag `CXT` and the three tag-named TGA files above.

## Sprite and GFX ownership

- Sprite name: not applicable for standard country flags; HOI4 resolves the tag-named files from the flag ladders.
- Target `.gfx`: none. Do not add a custom `.gfx` sprite or a DDS display copy for the flag consumer.
- If a later custom UI explicitly requires a flag sprite, the parent agent should register it from the runtime TGA path and keep the tag identity `CXT` stable.

## Changed files in this package

- `docs/assets/country_flags/cxt_test_country/source/cxt_flag_imagegen.png`
- `docs/assets/country_flags/cxt_test_country/processed/cxt_flag_preview.png`
- `docs/assets/country_flags/cxt_test_country/processed/cxt_flag_preview.dds`
- `docs/assets/country_flags/cxt_test_country/contact_sheet.png`
- `docs/assets/country_flags/cxt_test_country/manifest.md`
- `docs/assets/country_flags/cxt_test_country/handoff.md`
- `docs/assets/country_flags/cxt_test_country/gfx_handoff.md`
- `gfx/flags/CXT.tga`
- `gfx/flags/medium/CXT.tga`
- `gfx/flags/small/CXT.tga`

## Validation

- Canonical flat-flag references were inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/`, including its ladder contact sheet.
- Installed Vanilla `USA_communism.tga` normal, medium, and small files were inspected for TGA type, bit depth, descriptor, origin, and exact lengths.
- All three CXT TGAs are type `2`, uncompressed, 32-bit, descriptor `0x08`, bottom-left origin, and exact required dimensions/lengths.
- The processed preview was converted with the repository-standard DDS converter and its legacy BGRA header, dimensions, caps, and exact file length were checked.
- `contact_sheet.png` visually compares the ImageGen source, processed crop, and all three decoded runtime ladders.
- No `.gfx`, gameplay, localisation, country, event, spreadsheet, or shared documentation files were edited.

## Use notes and remaining risk

The flag is deliberately artificial and symbolic: charcoal field, chartreuse proving band, white calibration/gear sigil, and one crimson warning marker. The normal and medium exports retain the emblem's outer silhouette. At `10x7`, the generated emblem necessarily compresses into a compact high-contrast mark; the contact sheet documents the native result.

No in-game validation is claimed. The parent agent should perform the normal CXT consumer check in its own runtime validation pass.
