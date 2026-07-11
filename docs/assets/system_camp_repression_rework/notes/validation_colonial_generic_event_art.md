# Colonial and Generic Event Art Validation

Package: `system_camp_repression_rework`

Scope: the ten report/news assets listed in `manifest_colonial_generic_event_art.md`.

## Visual review

- The source and processed contact sheets were reviewed at full resolution.
- Every scene has a distinct route identity and distinct source raster.
- The six report-card crops retain the central investigators and physical evidence without clipping the primary subject.
- The four news crops retain their central action band and remain legible as wide press photographs.
- No readable generated text, graphic gore, recognizable historical person, protected-class selector imagery, SS rune, swastika, or Rising Sun imagery is visible in the selected sources or processed outputs.
- No placeholder, map-only composition, title card, or shared-source derivative is present.

## Processor provenance

- Report processor: `C:/Users/klimp/.codex.broken-20260627-113153/worktrees/360d/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.
- Verified SHA-256: `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9`.
- DDS converter: `.tools/convert_to_dds.py` using its BGRA output path with one mip.

## Decoded asset checks

| Asset | Processed PNG | Runtime DDS | DDS SHA-256 |
| --- | --- | --- | --- |
| `report_event_raj_detention_discovery` | `210x176`, RGBA, transparent corners | `210x176`, 32-bit BGRA, pixel-identical | `4f84fb3f07db72af06e7e92145770b60168e4128925c90a7358e5bc5831fa5ff` |
| `report_event_usa_relocation_review` | `210x176`, RGBA, transparent corners | `210x176`, 32-bit BGRA, pixel-identical | `a245da2259aa033996e086c6d18bea21986c6509b215adfbbc72d2a2a97e7001` |
| `report_event_fr_liberated_camp_records` | `210x176`, RGBA, transparent corners | `210x176`, 32-bit BGRA, pixel-identical | `56841e5ead5e0203ad71615edd72a703c16fd9bd9fe544586a7efff9db5fc222` |
| `report_event_libyan_camp_discovery` | `210x176`, RGBA, transparent corners | `210x176`, 32-bit BGRA, pixel-identical | `cc0fffd133efcd13fb4df2f8d07daed39b2f7880800efdaa47ce1a09e3a4730b` |
| `report_event_congo_labor_discovery` | `210x176`, RGBA, transparent corners | `210x176`, 32-bit BGRA, pixel-identical | `6b472b4d0824d0b433680eaebf2d0558fa87430a6cb3eb55df244684bd45425c` |
| `report_event_generic_camp_discovery` | `210x176`, RGBA, transparent corners | `210x176`, 32-bit BGRA, pixel-identical | `4ab8420cd76a637f66ab8972b131ef6467e7a58f23f3340b61d7989ab7587ba5` |
| `news_event_colonial_reckoning` | `397x153`, true grayscale `L` | `397x153`, 32-bit BGRA, pixel-identical | `78300b562e1748e2dd331ea2b812eba2432b5a71f8c0dd5b9e45feb2cc35dccb` |
| `news_event_vichy_reckoning` | `397x153`, true grayscale `L` | `397x153`, 32-bit BGRA, pixel-identical | `af543389b3497967582ac03489458e2420056e3579cf47b4f91784395d0de9f0` |
| `news_event_congo_colonial_reckoning` | `397x153`, true grayscale `L` | `397x153`, 32-bit BGRA, pixel-identical | `c9f64a55ffb600b27b160294603ccbd8a0b5afa9c71b49bf557bb23d24715f09` |
| `news_event_global_atrocity_evidence` | `397x153`, true grayscale `L` | `397x153`, 32-bit BGRA, pixel-identical | `a1e4f6ff8bc20a3a3361871d56e495b2110b76b98c881768803cabeb3b79024b` |

The DDS header check required masks `00FF0000/0000FF00/000000FF/FF000000` on every file. Pillow decoded every runtime DDS and reproduced the matching processed PNG pixels exactly.

## Package integrity

- Distinct source PNG hashes: `10/10`.
- Distinct processed PNG hashes: `10/10`.
- Runtime/package DDS byte identity: `10/10`.
- Runtime DDS readability: `10/10`.
- Source PNG presence: `10/10`.
- Processed PNG presence: `10/10`.
- Final runtime DDS presence: `10/10`.

## Review files

- `docs/assets/system_camp_repression_rework/contact_sheets/colonial_generic_event_art/colonial_generic_event_art_source_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/colonial_generic_event_art/colonial_generic_event_art_processed_contact_sheet.png`

Blocked assets: none.
