# Event 020 report and news art handoff

Status: complete for the bounded three-asset request. This handoff covers generated 2D report/news art only; no GFX, gameplay, localisation, event, or 3D files were edited.

## Runtime assets

| Sprite name | Final DDS | Size | Surface | Suggested target `.gfx` |
| --- | --- | --- | --- | --- |
| `GFX_report_event_020_black_plague_origin` | `gfx/event_pictures/020_black_plague/report_event_020_black_plague_origin.dds` | 210x176 | report event picture | `interface/020_black_plague_event_pictures.gfx` |
| `GFX_report_event_020_rat_emergence` | `gfx/event_pictures/020_black_plague/report_event_020_rat_emergence.dds` | 210x176 | report event picture | `interface/020_black_plague_event_pictures.gfx` |
| `GFX_news_event_020_black_plague_overseas` | `gfx/event_pictures/020_black_plague/news_event_020_black_plague_overseas.dds` | 397x153 | black-and-white news event picture | `interface/020_black_plague_event_pictures.gfx` |

Ready-to-copy sprite definitions:

```text
spriteType = { name = "GFX_report_event_020_black_plague_origin" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_black_plague_origin.dds" }
spriteType = { name = "GFX_report_event_020_rat_emergence" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_rat_emergence.dds" }
spriteType = { name = "GFX_news_event_020_black_plague_overseas" texturefile = "gfx/event_pictures/020_black_plague/news_event_020_black_plague_overseas.dds" }
```

## Evidence

- Source PNGs: `docs/assets/020_black_plague/event_art/source/`.
- Processed previews: `docs/assets/020_black_plague/event_art/processed/`.
- ImageGen prompt record: `docs/assets/020_black_plague/event_art/prompts/event20_report_news_prompts.md`.
- Contact sheet: `docs/assets/020_black_plague/event_art/contact_sheet.png`.
- Detailed manifest with SHA-256 hashes and DDS header facts: `docs/assets/020_black_plague/event_art/manifest.md`.

The report source scenes are a neglected mainland care station and an organized rat emergence from a bomb-damaged sewer. The news strip is a high-contrast overseas port quarantine with a period steamship held offshore. All generated imagery is fictional, period-authentic, text-free, and distinct; no placeholder or cross-type resize was used.

## Validation and remaining owner work

- Report PNGs are exact 210x176 RGBA cards with transparent corners and alpha range 0-255.
- News PNG is exact 397x153 grayscale and retains the requested black-and-white press treatment.
- All three DDS files were created with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and validated as one-level 32-bit uncompressed BGRA with the expected header masks, `DDSCAPS_TEXTURE`, and exact byte lengths.
- Main agent must add the three sprites to the existing target `.gfx` file and connect the relevant report/news consumers.
- No blocker or needs-user-review item remains for this bounded package.
