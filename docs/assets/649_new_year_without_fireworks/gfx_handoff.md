# GFX handoff: The New Year Without Fireworks

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds`
- Registered sprite: `GFX_report_event_fallout_new_year_without_fireworks`
- Target `.gfx`: `interface/fallout_world_end.gfx`, registered by the main agent.
- Target dimensions: `210x176`
- Asset surface: static HOI4 report event picture.
- Related event: `649_new_year_without_fireworks` (East Asia Fallout report, “The New Year Without Fireworks”).
- Suggested texture line: `texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds"`
- Source mode: `$imagegen`, fictional alternate-history documentary scene. No real person, real place, real flag, archive item, or historical identity is represented.
- Visual fit: cold, ash-darkened East Asian community at the year’s turning with covered lamps, a ration table, memorial ribbons, civilians, and unmarked guards beneath an empty sky. Faces are small or turned away and no readable script, flags, religious markers, modern branding, fireworks, zombies, animation, or audio are present.
- Processing: `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` produced the 210x176 sepia documentary card with transparent corners, subtle tilt, border, grain, and soft shadow.
- Wiring: `interface/fallout_world_end.gfx` registers the sprite, and `events/fallout_world_end_events.txt` references it for events `649` through `655`. Do not point runtime paths into `docs/assets/`.
- Status: complete and statically registered for generated source, processed PNG, DDS, `.gfx`, and event references. Live presentation remains unproven.
