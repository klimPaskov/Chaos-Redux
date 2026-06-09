# Event 006 Super-Event Image Handoff

Status: `complete`

Asset package: `The Rump That Endures`

## Deliverables

- source PNG: `docs/assets/006_independence_wave/super_events/rump_that_endures/source_png/super_event_independence_wave_rump_that_endures_source.png`
- processed PNG preview: `docs/assets/006_independence_wave/super_events/rump_that_endures/processed_png/super_event_independence_wave_rump_that_endures_457x328.png`
- final DDS: `gfx/super_events/super_event_independence_wave_rump_that_endures.dds`
- prompts record: `docs/assets/006_independence_wave/super_events/rump_that_endures/prompts/super_event_independence_wave_rump_that_endures_prompts.md`
- manifest: `docs/assets/006_independence_wave/super_events/rump_that_endures/manifest.md`
- package gfx handoff: `docs/assets/006_independence_wave/super_events/rump_that_endures/gfx_handoff.md`
- contact sheet: `docs/assets/006_independence_wave/super_events/rump_that_endures/contact_sheets/super_event_independence_wave_rump_that_endures_contact_sheet.png`

## Final sprite handoff

- final DDS path: `gfx/super_events/super_event_independence_wave_rump_that_endures.dds`
- sprite name: `GFX_super_event_independence_wave_rump_that_endures`
- suggested `.gfx` file: `interface/chaos_super_events.gfx`
- target size: `457x328`

## Selection note

Variant B was selected. It communicates the design rule cleanly: the host has lost most of its territory, but one guarded office, one seal, and one exhausted cabinet still answer in law. The tone stays sober and diminished rather than apocalyptic.

## Validation

- inspected the super-event reference folder before generation
- generated three candidate source images with `$imagegen`
- copied all candidate sources into the package
- resized the selected source to `457x328`
- converted the processed PNG to DDS
- verified the processed PNG dimensions are `457x328`
- verified the DDS exists at the requested final path and identifies as `457x328`

## Notes

- no `.gfx`, localisation, event, or gameplay files were edited
- local processing and DDS conversion used ImageMagick
- no placeholder asset was created
