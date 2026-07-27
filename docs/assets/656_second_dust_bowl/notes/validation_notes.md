# Validation notes

Validated on 2026-07-27 in the mod workspace without launching Hearts of Iron IV.

- Source PNG decodes as `1370x1148 RGB`.
- Processed PNG decodes as `210x176 RGBA` with alpha extrema `(0, 255)` and non-empty alpha bounding box `(4, 5, 210, 176)`.
- DDS header has `DDS ` magic, `DDS_HEADER` size `124`, declared width `210`, declared height `176`, `DDS_PIXELFORMAT` size `32`, flags `65` (`RGB | ALPHAPIXELS`), fourCC `0`, bit count `32`, masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, and `DDSCAPS_TEXTURE` `0x1000`.
- DDS file length is `147968` bytes, exactly `128 + (210 * 176 * 4)`; decoded pixel payload length is `147840` bytes.
- DDS alpha-byte extrema are `(0, 255)`, preserving the processed transparent corners and opaque card body.
- SHA-256 hashes are recorded in `manifest.md`.
- Contact sheet `contact_sheets/report_event_fallout_second_dust_bowl_contact_sheet.png` is review-only and is not a runtime asset; SHA-256 `42920209E1BAEC8A607B0AA476908458A64476D8C1CC0D5CEFF72E94157AB81B`.
- Processing command: `python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py docs/assets/656_second_dust_bowl/source_png/report_event_fallout_second_dust_bowl_source.png docs/assets/656_second_dust_bowl/processed_png/report_event_fallout_second_dust_bowl.png`.
- DDS command: `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input docs/assets/656_second_dust_bowl/processed_png/report_event_fallout_second_dust_bowl.png --output gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds --width 210 --height 176`.
- No `.gfx`, localisation, event, gameplay, or spreadsheet files were edited by this package. Parent-owned wiring is still required.
