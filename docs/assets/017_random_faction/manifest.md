# Event 017 Random Faction Report-Event Asset Manifest

These four report pictures are processed from the recovered Event 17 source frames using the repository report-event pipeline:

`process_report_event_image.py` -> 210x176 transparent tilted card -> `convert_to_dds.py` (BGRA, one mip level).

The processing applies the vanilla-style black-and-white sepia treatment, documentary-card tilt, transparent corners, and soft drop shadow. The source art is retained for reproducibility; the processed PNGs are the reviewable intermediate assets and the DDS files are the runtime copies.

| Sprite | Source | Processed PNG | Runtime DDS | Size |
|---|---|---|---|---|
| `GFX_report_event_random_faction_border` | `source/report_event_random_faction_border_source.png` | `processed_png/report_event_random_faction_border.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_border.dds` | 210x176 |
| `GFX_report_event_random_faction_cabinet` | `source/report_event_random_faction_cabinet_source.png` | `processed_png/report_event_random_faction_cabinet.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_cabinet.dds` | 210x176 |
| `GFX_report_event_random_faction_liaison` | `source/report_event_random_faction_liaison_source.png` | `processed_png/report_event_random_faction_liaison.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_liaison.dds` | 210x176 |
| `GFX_report_event_random_faction_regional_cascade` | `source/report_event_random_faction_regional_cascade_source.png` | `processed_png/report_event_random_faction_regional_cascade.png` | `gfx/event_pictures/017_random_faction/report_event_random_faction_regional_cascade.dds` | 210x176 |

All four runtime sprite names remain unchanged in `interface/017_random_faction.gfx`; no event or localisation references need renaming.
