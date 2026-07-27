# Mountain Pass Census asset handoff

Runtime wiring is owned by the main implementation tranche.

The report card sprite is `GFX_report_event_fallout_mountain_pass_census` in `interface/fallout_world_end.gfx`.

The package source is `source_generated.png`, generated with OpenAI ImageGen. The processed review image is `processed_210x176.png` in RGBA with the deterministic tilted report-card treatment, transparent edge space, paper border, grain, and soft alpha shadow. The runtime file is `gfx/event_pictures/fallout_world_end/report_event_fallout_mountain_pass_census.dds` at 210 by 176 pixels with one mip level and an uncompressed BGRA layout. The bundled report-event processor and event-assets DDS converter produced the file.

Events 635, 637, and 639 use the report picture. The source and preview remain in this candidate package for review and are not reused by another event family. No real person, flag, attested symbol, readable text, or audio is present. Static package checks are complete. Live consumer validation is pending because HOI4 was not run by request.
