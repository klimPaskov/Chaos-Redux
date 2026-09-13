# Event 023 generated event-art handoff

Status: needs_user_review after complete bounded asset production; pending parent `.gfx`, event, news, decision-category, and super-event wiring.

## Files created

- `docs/assets/023_sov_nuclear_bombs/manifest.md`
- `docs/assets/023_sov_nuclear_bombs/gfx_handoff.md`
- `docs/assets/023_sov_nuclear_bombs/prompts/*.txt` for all nine ImageGen calls
- `docs/assets/023_sov_nuclear_bombs/source_png/*.png` for all nine native generated masters
- `docs/assets/023_sov_nuclear_bombs/processed_png/*.png` for all nine processed previews
- `docs/assets/023_sov_nuclear_bombs/contact_sheets/event_art_source_contact_sheet.png`
- `docs/assets/023_sov_nuclear_bombs/contact_sheets/event_art_processed_contact_sheet.png`
- `docs/assets/023_sov_nuclear_bombs/contact_sheets/event_art_dds_roundtrip_contact_sheet.png`
- `docs/assets/023_sov_nuclear_bombs/notes/decoded_dds/*_dds_roundtrip.png`
- `gfx/interface/decisions/023_sov_nuclear_bombs/decision_category_sov_nuclear_command_picture.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_arsenal_opening.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_test_report.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_accident_report.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_public_test.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_ultimatum.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_first_use.dds`
- `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_breakaway_custody.dds`
- `gfx/super_events/023_sov_nuclear_bombs/super_event_sov_nuclear_major_exchange.dds`

## Produced assets

| Asset | Final size | Source mode | Runtime path | Proposed sprite | Status |
| --- | ---: | --- | --- | --- | --- |
| `sov_nuclear_command_category_picture` | 114x101 | `$imagegen`, opaque category picture | `gfx/interface/decisions/023_sov_nuclear_bombs/decision_category_sov_nuclear_command_picture.dds` | `GFX_decision_category_sov_nuclear_command_picture` | needs_user_review |
| `sov_nuclear_arsenal_opening` | 210x176 | `$imagegen` source plus report-card processor | `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_arsenal_opening.dds` | `GFX_report_event_sov_nuclear_arsenal_opening` | needs_user_review |
| `sov_nuclear_test_report` | 210x176 | `$imagegen` source plus report-card processor | `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_test_report.dds` | `GFX_report_event_sov_nuclear_test_report` | needs_user_review |
| `sov_nuclear_accident_report` | 210x176 | `$imagegen` source plus report-card processor | `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_accident_report.dds` | `GFX_report_event_sov_nuclear_accident_report` | needs_user_review |
| `sov_nuclear_public_test_news` | 397x153 | `$imagegen`, opaque news picture converted to monochrome | `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_public_test.dds` | `GFX_news_event_sov_nuclear_public_test` | needs_user_review |
| `sov_nuclear_ultimatum_news` | 397x153 | `$imagegen`, opaque news picture converted to monochrome | `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_ultimatum.dds` | `GFX_news_event_sov_nuclear_ultimatum` | needs_user_review |
| `sov_nuclear_first_use_news` | 397x153 | `$imagegen`, opaque news picture converted to monochrome | `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_first_use.dds` | `GFX_news_event_sov_nuclear_first_use` | needs_user_review |
| `sov_nuclear_breakaway_custody_news` | 397x153 | `$imagegen`, opaque news picture converted to monochrome | `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_breakaway_custody.dds` | `GFX_news_event_sov_nuclear_breakaway_custody` | needs_user_review |
| `sov_nuclear_major_exchange_super_event` | 457x328 | `$imagegen`, opaque nonterminal super-event scene | `gfx/super_events/023_sov_nuclear_bombs/super_event_sov_nuclear_major_exchange.dds` | `GFX_super_event_sov_nuclear_major_exchange` | needs_user_review |

## Validation evidence

- Each final DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
- Each DDS was parsed as a one-level legacy BGRA file with the expected 128-byte header, pixel masks, texture caps, exact length, dimensions, and actual alpha range.
- Report DDS files decode with alpha 0..255; the category, news, and super-event DDS files decode with alpha 255..255.
- Decoded DDS PNGs are retained under `docs/assets/023_sov_nuclear_bombs/notes/decoded_dds/` and compared in the round-trip contact sheet.
- The four news images are visibly distinct at 397x153: public test/steppe observation, ultimatum/capital pressure, first-use industrial devastation, and breakaway rail custody.
- The super-event composition is visibly distinct from Fallout and Final Silence because it shows live communications, aircraft/searchlights, evacuation, and an active exchange rather than a terminal empty landscape or occult presentation.

## References inspected

- `event_art/report/contact_sheet.png`, `event_art/news/contact_sheet.png`, and `event_art/super_event/contact_sheet.png` under the canonical reference root.
- `icons/decision_categories/pictures/contact_sheet.png` under the canonical reference root.
- Existing repo precedent `interface/005_soviet_collapse.gfx` for event-scoped decision-category texture paths.
- Existing Event 23 consumers `events/023_soviet_nukes.txt` and `events/_chaosx_news.txt` were read only to identify the current legacy picture names.

## Parent follow-up

- Register the nine proposed sprite names in the chosen Event 23 `.gfx` file.
- Wire the ordinary decision category picture to the Event 23 category definition.
- Replace or alias the current opening picture reference `GFX_report_event_sov_nukes`.
- Assign the four news sprites to the corresponding Event 23 news consumers.
- Route the super-event sprite through the selected nonterminal slot and `GetSuperEventImage`.
- Retain the event-scoped evidence workspace until parent review and runtime wiring are complete.

No gameplay, localisation, GUI, achievement registry, or `.gfx` files were edited by this handoff.
