# Event 013 Natural Disasters report and news validation

Validation scope: only the 14 report images and 5 news images from this art pass.

- Processed PNG dimension check passed.
  - Report images: `210x176`
  - News images: `397x153`
- Report-card transparency check passed.
  - All four corner alpha values are `0` for every processed report image.
- DDS export check passed.
  - Report DDS files in both `docs/assets/013_natural_disasters/dds/` and `gfx/event_pictures/013_natural_disasters/` are `210x176`.
  - News DDS files in both `docs/assets/013_natural_disasters/dds/` and `gfx/event_pictures/013_natural_disasters/` are `397x153`.
- Visual review performed.
  - Contact sheets:
    - `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_report_contact_sheet.png`
    - `docs/assets/013_natural_disasters/contact_sheets/013_natural_disasters_news_contact_sheet.png`
  - Spot review confirmed the family reads remain distinct after crop and processing.

Known risk:

- The DDS export path available in this environment writes news images as `24-bit RGB888` because those processed PNGs do not use alpha. That is acceptable for these news pictures, but the main agent should keep the export path in mind if a future wiring surface expects alpha on news art.
