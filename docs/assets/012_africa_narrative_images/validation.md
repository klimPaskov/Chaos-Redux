# Event 012 Africa narrative-image validation

- 20 generated source masters are present in `source_generated/` and mirrored in `source_png/`.
- 10 report previews are exactly 210x176 and use the report-card processor.
- 6 news previews are exactly 397x153, grayscale, and opaque.
- 4 super-event previews are exactly 457x328, RGB, and color.
- All 20 DDS files use the repository converter and the legacy uncompressed 32-bit BGRA header expected by the mod.
- `metadata/dds_validation.json` records dimensions, processed mode, byte length, SHA-256, and header checks; the current error list is empty.
- `comparison/` contains source, processed, and DDS-decoded contact sheets for visual inspection.

Visual review found the scenes distinct, period-grounded, and free of readable generated text or modern props. The first failed-guarantee report is intentionally non-exploitative: civilians and exhausted defenders are shown at a damaged rail defense without forced-return imagery or gore.
