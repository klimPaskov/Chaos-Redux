# Event 010 Death report-event regeneration handoff

- Scope: regenerated the active Death report-event image package only
- Date: `2026-06-16`
- Source mode: generated non-icon art via official `image_gen`, then local report-card processing

## Files changed

- `docs/assets/010_death/source_png/report_event_death_missing_island_source.png`
- `docs/assets/010_death/source_png/report_event_death_mail_boat_source.png`
- `docs/assets/010_death/source_png/report_event_death_lighthouse_source.png`
- `docs/assets/010_death/source_png/report_event_death_census_source.png`
- `docs/assets/010_death/processed_png/report_event_death_missing_island.png`
- `docs/assets/010_death/processed_png/report_event_death_mail_boat.png`
- `docs/assets/010_death/processed_png/report_event_death_lighthouse.png`
- `docs/assets/010_death/processed_png/report_event_death_census.png`
- `docs/assets/010_death/contact_sheets/death_report_event_images_contact.png`
- `gfx/event_pictures/010_death/report_event_death_missing_island.dds`
- `gfx/event_pictures/010_death/report_event_death_mail_boat.dds`
- `gfx/event_pictures/010_death/report_event_death_lighthouse.dds`
- `gfx/event_pictures/010_death/report_event_death_census.dds`
- `docs/assets/010_death/generated_art_manifest.md`
- `docs/assets/010_death/generated_art_gfx_handoff.md`

## Stable ids and paths preserved

- `report_event_death_missing_island` -> `gfx/event_pictures/010_death/report_event_death_missing_island.dds` -> `GFX_report_event_death_missing_island`
- `report_event_death_mail_boat` -> `gfx/event_pictures/010_death/report_event_death_mail_boat.dds` -> `GFX_report_event_death_mail_boat`
- `report_event_death_lighthouse` -> `gfx/event_pictures/010_death/report_event_death_lighthouse.dds` -> `GFX_report_event_death_lighthouse`
- `report_event_death_census` -> `gfx/event_pictures/010_death/report_event_death_census.dds` -> `GFX_report_event_death_census`

## Quality notes

- `missing_island`: black surf overruns the quay and the coastline reads wrong rather than merely empty.
- `mail_boat`: the launch now reads as recently returned or adrift, with sacks and cabin light visible but no crew.
- `lighthouse`: the beam and dead sea now dominate the image instead of a quiet village postcard.
- `census`: the office now has human witnesses, shattered storage, and missing-records tension without readable text.

## Validation performed

- Ran `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` with `python3` for all four source PNGs.
- Exported all four final DDS files with `convert -define dds:compression=none`.
- Verified processed PNG dimensions: all four are exactly `210x176`.
- Verified final DDS metadata with `file`: all four report `210 x 176, 32-bit color, ARGB8888`.
- Verified transparent report-card corners with ImageMagick pixel sampling at all four corners for each processed PNG.
- Reviewed the finished package visually through `docs/assets/010_death/contact_sheets/death_report_event_images_contact.png`.

## Blockers

- None.
