# First Red Line GFX handoff

The runtime sprite is registered in `interface/fallout_world_end.gfx` as `GFX_report_event_fallout_first_red_line`.

The sprite points to `gfx/event_pictures/fallout_first_red_line/report_event_fallout_first_red_line.dds`.

The event source uses `picture = GFX_report_event_fallout_first_red_line` for the human opening, result, and callback surfaces. The hidden AI events use the same dedicated picture only through the event family definition and do not introduce a second asset path.
