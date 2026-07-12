# Event 018 Raster Validation

Command:

```text
python docs/assets/018_resources_found/_tooling/process_event_018_raster_assets.py
```

Verified report-card processor SHA-256:

```text
5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9
```

Validated results:

- 10 report cards at `210x176`, including transparent corner pixels.
- 6 news images at `397x153` in true grayscale `L` before DDS conversion.
- 3 super-event images at `457x328`, also reviewed through the repository super-event template aperture.
- 4 large portraits at `156x210` and 3 commander small portraits at `50x67`.
- 8 distinct generated Vhorruk source frames and 8 distinct normalized frames; `1248x210` sheet; 8-frame GIF; static portrait pixel-identical to frame 1 after normalization.
- 6 distinct flag identities at `82x52`, `41x26`, and `10x7`.
- 18 flag TGAs with image type 2, 32-bit pixels, descriptor 8, and bottom-left origin.
- All 27 DDS files have one mip, 32-bit BGRA channel masks, exact required dimensions, and pixel identity to their processed PNGs.
- No obsolete `DHO_WORLD_END.tga` exists. The delivered cosmetic family is `DHO_WORLD_BELOW`.

Visual review contacts:

- `contact_sheets/event_018_report_processed_contact_sheet.png`
- `contact_sheets/event_018_news_processed_contact_sheet.png`
- `contact_sheets/event_018_super_event_processed_contact_sheet.png`
- `contact_sheets/event_018_super_event_ui_mask_preview_contact_sheet.png`
- `contact_sheets/event_018_portrait_processed_contact_sheet.png`
- `contact_sheets/event_018_vhorruk_animation_processed_contact_sheet.png`
- `contact_sheets/event_018_flag_final_sizes_contact_sheet.png`

Rejected and replaced before final export:

- `rejected_report_event_018_first_evidence_recognizable_insignia.png`
- `rejected_DHO_communism_saltire_source.png`
