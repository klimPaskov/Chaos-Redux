# Event 012 Africa narrative-image GFX handoff

The package is ready for parent-owned `.gfx` wiring. Do not add duplicate sprite definitions: the matrix sprite names below are the stable handoff names.

## Report and news event pictures

Target `.gfx`: the Event 012 Africa event-picture definitions selected by the parent implementation.

Each report sprite uses `GFX_report_event_012_africa_<key>` and points to `gfx/event_pictures/012_africa/report_event_012_africa_<key>.dds` at 210x176. Each news sprite uses `GFX_news_event_012_africa_<key>` and points to `gfx/event_pictures/012_africa/news_event_012_africa_<key>.dds` at 397x153.

## Super-events

Target `.gfx`: the parent Event 012 Africa super-event definitions.

Use `GFX_super_event_012_africa_is_one`, `GFX_super_event_012_africa_scramble_response`, `GFX_super_event_012_africa_continental_wars`, and `GFX_super_event_012_africa_the_world` with the matching DDS files in `gfx/super_events/012_africa/` at 457x328. These images are generated, color, and intentionally distinct from the report/news monochrome treatment.

No `.gfx` file was edited in this asset tranche. No audio cue is included or wired here.
