# Event 011 raster validation

Verified report processor: `C:\Users\klimp\.codex.broken-20260627-113153\worktrees\360d\chaos_redux\.agents\skills\chaos-redux-event-assets\tools\process_report_event_image.py`
Report processor SHA-256: `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9`

- `docs\assets\011_secret_alliance\processed_png\report_event_first_pattern.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_first_pattern.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\report_event_missing_courier.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_missing_courier.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\report_event_machine_sabotage.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_machine_sabotage.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\report_event_safehouse_raid.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_safehouse_raid.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\report_event_border_survey.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_border_survey.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\report_event_political_attack.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_political_attack.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\report_event_turned_channel.png`: 210x176, mode RGBA; `gfx\event_pictures\011_secret_alliance\report_event_turned_channel.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\news_event_public_coalition.png`: 397x153, mode L; `gfx\event_pictures\011_secret_alliance\news_event_public_coalition.dds`: 32-bit BGRA masks and pixel identity verified
- `docs\assets\011_secret_alliance\processed_png\super_event_public_reveal.png`: 457x328, mode RGB; `gfx\super_events\011_secret_alliance\super_event_public_reveal.dds`: 32-bit BGRA masks and pixel identity verified

- All seven report cards have transparent corner pixels.
- The public-coalition news image is true grayscale (`L`) before DDS conversion.
- The reveal image was reviewed through `gfx/super_events/super_event_template.psd` at the verified aperture.
- All nine source rasters have distinct SHA-256 hashes; no source raster is reused.
