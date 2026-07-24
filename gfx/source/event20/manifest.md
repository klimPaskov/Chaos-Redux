# Event20 Black Plague visual asset manifest

Generation date: 2026-07-24. Source mode for all rows: `$imagegen` built-in official ImageGen. All source PNGs are retained under `gfx/source/event20/source_png/`; processed previews are under `gfx/source/event20/processed_png/`; runtime DDS files are in engine-facing folders. The source family was selected because Event20 is fictional, alternate-history, and high-chaos; no archival image could represent the invented Rat King scenes without losing the requested specificity.

## Requirement-to-runtime crosswalk

| Requirement | Asset key / sprite name | Intended use | Source PNG | Processed PNG | Runtime DDS | Size / format | Target `.gfx` | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Event20 report image | `GFX_report_event_020_black_plague_unbound` | `chaosx.nr020.1` report/event detail image | `gfx/source/event20/source_png/report_event_020_black_plague_unbound_source.png` | `gfx/source/event20/processed_png/report_event_020_black_plague_unbound.png` | `gfx/event_pictures/020_black_plague/report_event_020_black_plague_unbound.dds` | 210x176 RGBA PNG; 32-bit uncompressed BGRA DDS; transparent corners; sepia B&W card | `interface/020_black_plague_event_pictures.gfx` (main-agent wiring) | converted / handed_off |
| Super-event 85 coronation | `GFX_super_event_085_rat_king_coronation` | Super-event slot 85 Rat King coronation | `gfx/source/event20/source_png/super_event_085_rat_king_coronation_source.png` | `gfx/source/event20/processed_png/super_event_085_rat_king_coronation.png` | `gfx/super_events/020_black_plague/super_event_085_rat_king_coronation.dds` | 457x328 RGB PNG; 32-bit uncompressed BGRA DDS | `interface/020_black_plague_super_events.gfx` (main-agent wiring) | converted / handed_off |
| Super-event 86 terminal takeover | `GFX_super_event_086_rat_king_takeover` | Super-event slot 86 terminal Rat King takeover | `gfx/source/event20/source_png/super_event_086_rat_king_takeover_source.png` | `gfx/source/event20/processed_png/super_event_086_rat_king_takeover.png` | `gfx/super_events/020_black_plague/super_event_086_rat_king_takeover.dds` | 457x328 RGB PNG; 32-bit uncompressed BGRA DDS | `interface/020_black_plague_super_events.gfx` (main-agent wiring) | converted / handed_off |

Review evidence: `gfx/source/event20/contact_sheets/event20_black_plague_contact_sheet.png`. Prompts: `gfx/source/event20/prompts/event20_prompts.md`.

## Processing and QA notes

- The report source was processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` using deterministic seed `20020`; the result is exactly `210x176`, RGBA, sepia black-and-white, with transparent corners and a soft shadow.
- Super-event sources were resized with Pillow Lanczos to exactly `457x328` RGB before DDS conversion; no text or watermark was present.
- All DDS outputs were created with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and validated as one-level uncompressed BGRA: 128-byte header, pixel format size 32, flags 65, fourCC 0, 32-bit masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`, and exact payload length.
- Optional Doctor Wu/weaponization report art was not requested as a required row and was not generated.
- No custom country flag, Rat King leader/commander/operative portrait, idea/national-spirit icon, focus icon, or decision icon was created in this non-icon package. Route those families to the icon-artist or source-research handoff if Event20 gameplay consumes them.
