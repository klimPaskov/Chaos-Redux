# Event 014 Report and News Asset Manifest

Status: complete for this eight-image aftermath and Wendigo tranche (2026-07-12).

These are independently generated fictional wartime scenes. The two custody reports are post-reveal surfaces. The Wendigo material is fictional body-horror imagery with no borrowed sacred symbols, ceremonial objects, or claims about living Indigenous traditions. No image uses a real actor's likeness.

| Asset | Type | Source | Processed PNG | Runtime DDS | Size | Sprite |
|---|---|---|---|---|---:|---|
| `report_event_cannibalism_captured_warlord` | Report | `source_png/report_event_cannibalism_captured_warlord_source.png` | `processed_png/report_event_cannibalism_captured_warlord.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_captured_warlord.dds` | 210x176 | `GFX_report_event_cannibalism_captured_warlord` |
| `report_event_cannibalism_captured_hannibal` | Report | `source_png/report_event_cannibalism_captured_hannibal_source.png` | `processed_png/report_event_cannibalism_captured_hannibal.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_captured_hannibal.dds` | 210x176 | `GFX_report_event_cannibalism_captured_hannibal` |
| `report_event_cannibalism_wendigo_reveal` | Report | `source_png/report_event_cannibalism_wendigo_reveal_source.png` | `processed_png/report_event_cannibalism_wendigo_reveal.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_wendigo_reveal.dds` | 210x176 | `GFX_report_event_cannibalism_wendigo_reveal` |
| `report_event_cannibalism_wendigo_winter_network` | Report | `source_png/report_event_cannibalism_wendigo_winter_network_source.png` | `processed_png/report_event_cannibalism_wendigo_winter_network.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_wendigo_winter_network.dds` | 210x176 | `GFX_report_event_cannibalism_wendigo_winter_network` |
| `report_event_cannibalism_wendigo_countdown` | Report | `source_png/report_event_cannibalism_wendigo_countdown_source.png` | `processed_png/report_event_cannibalism_wendigo_countdown.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_wendigo_countdown.dds` | 210x176 | `GFX_report_event_cannibalism_wendigo_countdown` |
| `report_event_cannibalism_wendigo_transformation_broken` | Report | `source_png/report_event_cannibalism_wendigo_transformation_broken_source.png` | `processed_png/report_event_cannibalism_wendigo_transformation_broken.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_wendigo_transformation_broken.dds` | 210x176 | `GFX_report_event_cannibalism_wendigo_transformation_broken` |
| `report_event_cannibalism_wendigo_anchor_assault` | Report | `source_png/report_event_cannibalism_wendigo_anchor_assault_source.png` | `processed_png/report_event_cannibalism_wendigo_anchor_assault.png` | `gfx/event_pictures/014_cannibalism/report_event_cannibalism_wendigo_anchor_assault.dds` | 210x176 | `GFX_report_event_cannibalism_wendigo_anchor_assault` |
| `news_cannibalism_wendigo_reveal` | News | `source_png/news_cannibalism_wendigo_reveal_source.png` | `processed_png/news_cannibalism_wendigo_reveal.png` | `gfx/event_pictures/014_cannibalism/news_cannibalism_wendigo_reveal.dds` | 397x153 | `GFX_news_cannibalism_wendigo_reveal` |

## Production and verification

- Processor: `process_report_news_assets.py`
- Source contact: `contact_sheets/report_news_source_contact_sheet.png`
- Final contact: `contact_sheets/report_news_processed_contact_sheet.png`
- Runtime decode contact: `contact_sheets/report_news_dds_decoded_contact_sheet.png`
- Hashes, dimensions, opacity, DDS channel masks, uniqueness, and monochrome-news proof: `validation/report_news_asset_validation.tsv`
- Sprite handoff: `validation/report_news_gfx_handoff.tsv`
- Prompt/output audit: `prompts/generation_ledger.md`

All eight runtime textures are opaque, one-level, uncompressed BGRA DDS files. The news image is true monochrome rather than a merely desaturated color image. Package and runtime DDS hashes match.

## Rejected source

`rejected_attempts/report_event_cannibalism_wendigo_countdown_rejected_too_futuristic.png` is retained as provenance only. It was rejected because the machinery read as science-fiction equipment instead of a grounded 1940s vacuum-tube and rail-depot system. It is not processed, registered, or copied into runtime assets.

## Simplifications, omissions, and blockers

None within this eight-image tranche.
