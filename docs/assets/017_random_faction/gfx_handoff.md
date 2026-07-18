# Event 017 Random Faction Report-Event GFX Handoff

`interface/017_random_faction.gfx` already registers the four stable report-event sprite names. The regenerated runtime files are:

- `GFX_report_event_random_faction_border` -> `gfx/event_pictures/017_random_faction/report_event_random_faction_border.dds`
- `GFX_report_event_random_faction_cabinet` -> `gfx/event_pictures/017_random_faction/report_event_random_faction_cabinet.dds`
- `GFX_report_event_random_faction_liaison` -> `gfx/event_pictures/017_random_faction/report_event_random_faction_liaison.dds`
- `GFX_report_event_random_faction_regional_cascade` -> `gfx/event_pictures/017_random_faction/report_event_random_faction_regional_cascade.dds`

Each DDS is RGBA/BGRA, one mip level, and exactly 210x176. The four event-picture references in `events/017_join_faction.txt` and the liaison news event continue to resolve to these names.
