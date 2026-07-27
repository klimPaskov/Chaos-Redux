# Mountain Pass Census assets

This package belongs only to candidate 635 and events 635, 637, and 639. It does not reuse the Canal Schedule, Rail Spine Vote, Metro Republic Below, Tunnel Ward Committees, or zombie source, preview, DDS, sprite, audio, or path.

The fictional report scene was generated through OpenAI ImageGen because the chain is an alternate Fallout-era highland settlement and does not require a real person, real place, real flag, attested symbol, or archival photograph. The prompt is retained in `prompt.md`, and the generated source is retained as `source_generated.png` with its SHA-256 in `manifest.json`.

The reviewed preview is `processed_210x176.png`. It is RGBA and uses the approved local report-card treatment with a subtle tilt, transparent edge space, a paper border, grain, and a soft alpha shadow. The runtime DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` and `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, checked as one-level uncompressed BGRA, and copied to `gfx/event_pictures/fallout_world_end/report_event_fallout_mountain_pass_census.dds`.

The sprite `GFX_report_event_fallout_mountain_pass_census` is owned by `interface/fallout_world_end.gfx`. The crosswalk in `manifest.json` maps it to the opening, result, and thaw callback pictures. Live consumer validation is still pending because the user requested no HOI4 run. The normal-map cold-weather route remains gameplay-owned and is not represented by this report card.
