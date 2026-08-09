# Event 020 Black Plague decision-category picture handoff

Status: `complete`; parent `.gfx` wiring completed in `interface/020_black_plague_response.gfx`.

## Delivered asset

- Asset: `decision_cat_picture_black_plague_response`
- Surface: static decision-category picture (not the small category icon and not a scripted-GUI background)
- Sprite consumer: `GFX_decision_cat_picture_black_plague_response`
- Runtime DDS: `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds`
- Target canvas: exactly `114x101`, one static frame
- Registered `.gfx`: `interface/020_black_plague_response.gfx`
- Category consumer: `common/decisions/categories/020_black_plague_response_categories.txt`

## Package files

- Source PNG: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/source_png/decision_cat_picture_black_plague_response_imagegen_source.png` (`1188x1324`)
- Exact prompt: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/prompt.md`
- Processed PNG: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/processed_png/decision_cat_picture_black_plague_response_114x101.png` (`114x101`)
- DDS: `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds` (`114x101`, 46184 bytes)
- Visual QA/contact sheet: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/contact_sheets/decision_cat_picture_black_plague_response_contact_sheet.png`
- DDS/header and pixel round-trip QA: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/qa/dds_header_qa.json`
- Decoded DDS round-trip: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/qa/decision_cat_picture_black_plague_response_dds_roundtrip.png`
- Package manifest: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/manifest.md`
- Package GFX handoff: `docs/assets/020_black_plague/decision_category_picture_black_plague_response/gfx_handoff.md`

## Visual direction and source fit

Built-in ImageGen generated a fictional historical scene: two beaked-mask plague doctors/medical workers actively tend a covered patient in a cramped 1930s–WWII makeshift ward. The visual is tightly framed, high-contrast monochrome/sepia archival-news style, humane and determined, and remains legible after the `114x101` crop. It contains no explicit gore, readable text, logos, modern medical equipment, fantasy magic, fake UI controls, meters, buttons, badges, or control-like borders.

Source mode is `$imagegen` built-in generation because this is an invented/alternate-history ward and the requested action-specific composition is not a claim about a real historical person or event. No external source or third-party licence applies. The exact prompt is preserved verbatim in `prompt.md`.

## DDS/header evidence

`qa/dds_header_qa.json` reports `PASS` with:

- `DDS ` magic and header size `124`
- declared width/height `114x101`, pitch `456`
- pixel-format size `32`, flags `65`, fourCC `0`, bit count `32`
- BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`
- `DDSCAPS_TEXTURE = 0x1000`, no mipmaps
- exact file length `128 + 114*101*4 = 46184` bytes
- alpha range `255..255`
- decoded DDS round-trip has `0` differing pixel bytes from the processed PNG

## Ready-to-copy sprite snippet

```text
spriteType = {
	name = "GFX_decision_cat_picture_black_plague_response"
	texturefile = "gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds"
	noOfFrames = 1
}
```

## Remaining risks

- Live category rendering remains user-owned validation; the static DDS header and decoded round-trip are verified.
- The generated scene is fictional ImageGen art; no external historical provenance is claimed.

No placeholders, fallbacks, or unapproved simplifications were used.
