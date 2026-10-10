# Asset Prompt: Event 008 Tensions Rising

Use [chaos-redux-event-assets](../../../../.claude/skills/chaos-redux-event-assets/SKILL.md) for provenance, processing, manifest, durable-record, and parent-wiring requirements.
Do not edit gameplay, localisation, GUI, GFX, event, scripted, or spreadsheet files.

## Installed assets

| Asset | Sprite and file | Status |
| --- | --- | --- |
| Report image, 210x176 | `GFX_report_event_tensions_rising`, `gfx/event_pictures/008_tensions_rising/report_event_tensions_rising.dds` | wired on the root, batch report, and incidents |
| News image, 397x153 black-and-white | `GFX_news_event_tensions_red_line`, `gfx/event_pictures/008_tensions_rising/news_event_tensions_red_line.dds` | registered and cropped on 6 October (`docs/plans/gfx_fix_2026-10/008_report.md`); no consumer |
| Five achievement triplets, 64x64 | `GFX_achievement_008_tensions_rising_*` in `interface/chaosx_achievements.gfx` | wired |

Do not regenerate these assets.
The optional animated event-detail pulse is not needed because no accepted UI surface exists.

## Open item: provenance

The historical source archive `docs/assets/008_tensions_rising/` was deleted without a replacement record; the overview cites deletion commit `87d441ac758d515e1abca34167fcd45b51acf028`, which is not present in the current repository history.
Recover whatever durable source and generation evidence still exists into `docs/assets/008_tensions_rising/manifest.md`, keeping any unrecoverable fact explicitly unresolved rather than regenerating approved art.

The visual identity for any future replacement is diplomatic pressure before the break: embassy lights at night, telegraph rooms, sealed cables, press bundles, staff offices, blackout curtains, side entrances, guards, and shipping ledgers, with maps only as secondary props and no readable generated text.
