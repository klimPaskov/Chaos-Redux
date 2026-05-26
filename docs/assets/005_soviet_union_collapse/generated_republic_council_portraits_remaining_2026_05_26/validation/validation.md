# Event 005 Remaining Republic Council Portrait Validation

Date: 2026-05-26

## Checks Run

- Inspected Event 005 country-package handoff and current generated-art handoffs for leader/flag gaps.
- Confirmed the remaining ordinary/internal release portrait gap from `docs/plans/005_soviet_collapse_plans/subagent_handoffs/country_package_gap_report_2026_05_26.md`.
- Generated ten fictional council portrait source PNGs with Codex built-in `$imagegen`.
- Copied generated sources into the Event 005 sidecar package.
- Cropped/resized processed previews to `156x210`.
- Converted processed PNGs through `.tools/convert_to_dds.py` with `--width 156 --height 210`.
- Created source and processed contact sheets for visual review.
- Parsed DDS headers for width and height.
- Compared final DDS SHA-256 hashes within the package, against live Event 005 leader DDS files, and against the previous generated republic portrait package.

## Results

- Final DDS files: `10`.
- All final DDS files are `156x210`.
- Duplicate final DDS hashes within this package: `0`.
- Final DDS hashes matching live `gfx/leaders/005_soviet_collapse/*.dds`: `0`.
- Final DDS hashes matching `generated_republic_council_portraits_2026_05_26/final_dds/*.dds`: `0`.
- No gameplay, localisation, `.gfx`, GUI, focus, decision, history, country, script, spreadsheet, live leader DDS, or flag files were edited.

## Generated Outputs

- Processed contact sheet: `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_remaining_2026_05_26/contact_sheets/republic_council_remaining_processed_contact.png`
- Source contact sheet: `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_remaining_2026_05_26/contact_sheets/republic_council_remaining_sources_contact.png`
- DDS header audit: `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_remaining_2026_05_26/validation/dds_header_dimensions.tsv`
- ImageMagick identify report: `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_remaining_2026_05_26/validation/dds_identify_after_repo_converter.txt`
- Source origin order: `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_remaining_2026_05_26/validation/source_origin_order.txt`
- SHA-256 ledger: `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_remaining_2026_05_26/validation/sha256sums.txt`

## Skipped Validation

- No in-game validation was run.
- No Photoshop processing was required because these are leader/council portraits, not report-event images.
- No flag generation or re-export was performed because the current scoped active custom/high-chaos flag sets already have complete normal, medium, and small outputs and no existing-country route flags were explicitly required for this sidecar.
