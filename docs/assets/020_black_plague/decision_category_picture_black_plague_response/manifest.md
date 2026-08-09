# Event 020 Black Plague — decision category picture manifest

Status: `complete` / runtime sprite and category consumer wired.

This package contains one static decision-category picture, classified separately from the small decision-category icon family and from any scripted-GUI panel. It is intended for the dedicated Black Plague response/cure decision category and uses the exact consumer name supplied by the parent.

| Asset | Event / slug | Asset type and intended use | Source mode | Source PNG | Processed PNG | Final DDS | Target size | Sprite / target `.gfx` | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `decision_cat_picture_black_plague_response` | Event 020 / `black_plague` | Static decision-category picture; dedicated Black Plague response/cure category showing plague doctors tending a patient | `$imagegen` built-in; fictional generated historical scene | `source_png/decision_cat_picture_black_plague_response_imagegen_source.png` (`1188x1324`) | `processed_png/decision_cat_picture_black_plague_response_114x101.png` (`114x101`) | `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds` (`114x101`) | `114x101` | `GFX_decision_cat_picture_black_plague_response` / `interface/020_black_plague_response.gfx` | `wired` |

## Generation and fit

The source is a fictional ImageGen scene because the requested plague ward is invented/alternate-history and needs a specific humane treatment action that a verifiable archival source cannot guarantee. The scene is period-authentic 1930s–WWII documentary-news styling: two beaked-mask plague doctors in a makeshift ward, actively tending a covered patient, with no gore, readable text, modern props, UI controls, or border treatment. The exact prompt is preserved in [`prompt.md`](prompt.md).

## Processing

The source was cover-cropped from `(0,145,1188,1198)` to preserve both masks, treatment hands, patient, and period ward props, then resized with Pillow Lanczos to the canonical `114x101` family canvas and given restrained contrast enhancement (`1.10`) for native-size readability. No source art was traced, recoloured into a substitute, or derived from the vanilla references.

## QA evidence

- Visual review sheet: [`contact_sheets/decision_cat_picture_black_plague_response_contact_sheet.png`](contact_sheets/decision_cat_picture_black_plague_response_contact_sheet.png)
- DDS header, dimensions, alpha, byte-length, and pixel round-trip report: [`qa/dds_header_qa.json`](qa/dds_header_qa.json)
- Decoded DDS round-trip PNG: [`qa/decision_cat_picture_black_plague_response_dds_roundtrip.png`](qa/decision_cat_picture_black_plague_response_dds_roundtrip.png)
- DDS is legacy uncompressed BGRA: `DDS ` magic, 124-byte header, 32-bit RGB|ALPHAPIXELS flags 65, fourCC 0, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE 0x1000`, one level, exact file length `46184` bytes, declared `114x101`, alpha range `255..255`, and zero decoded pixel-byte differences from the processed PNG.

## Provenance and licensing

Source mode is built-in ImageGen generation; there is no external archive, photographer, or third-party licence to cite. The source PNG and generation record are retained in this package. This generated scene is not a portrait and does not represent a real person or historical event.

## Runtime wiring

The final DDS is in the requested runtime folder, `interface/020_black_plague_response.gfx` defines `GFX_decision_cat_picture_black_plague_response`, and `common/decisions/categories/020_black_plague_response_categories.txt` assigns it to the dedicated category. No scripted-GUI asset or fallback picture is used.
