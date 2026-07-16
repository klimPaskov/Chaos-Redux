# Air Winter Report-Event GFX Handoff

Status: ten final report-event asset packages are registered and consumed.

## Package summary

- Runtime folder: `gfx/event_pictures/fallout/air_winter/`
- Source folder: `docs/assets/air_cleanliness_fallout/source_png/report_events/`
- Processed folder: `docs/assets/air_cleanliness_fallout/processed_png/report_events/`
- Final contact sheet: `docs/assets/air_cleanliness_fallout/contact_sheets/air_winter_report_events_final_contact_sheet.png`
- Existing event consumers: `events/fallout_world_end_events.txt`
- Phase 1 consumers: `chaosx.fallout.1` through `chaosx.fallout.6`
- Island-refugee consumers: `chaosx.fallout.38` and `chaosx.fallout.39`
- Desert-city consumers: exact-receipt `chaosx.fallout.13` and `chaosx.fallout.49`
- Dead-city salvage consumers: `chaosx.fallout.47` and `chaosx.fallout.48`
- Suggested registry: `interface/air_cleanliness_winter.gfx`
- Source mode: built-in `$imagegen`, fictional 1936 to 1945 period-documentary scenes

The current Desert City tranche registers the dedicated sprite in `interface/air_cleanliness_winter.gfx` and consumes it through the exact event 13 picture route and event 49. It adds no audio or GUI asset.

The existing `GFX_report_event_air_winter_phase_1` asset covers events 1 through 6, including the five regional openings and their shared delayed return. The Phase 1 return adds no asset or audio requirement.

## Stable sprite mapping

| Sprite identifier | Final DDS path | Dimensions | Visual state |
| --- | --- | --- | --- |
| `GFX_report_event_air_winter_phase_1` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_1.dds` | 210x176 | Dim first-stage regional cold in a Norwegian coastal village |
| `GFX_report_event_air_winter_phase_2` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_2.dds` | 210x176 | Bengal crop shock under impossible cold rain |
| `GFX_report_event_air_winter_phase_3` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_3.dds` | 210x176 | Canadian freight transport locked by hard freeze |
| `GFX_report_event_air_winter_phase_4` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_4.dds` | 210x176 | Greek black harvest and dead vegetation |
| `GFX_report_event_air_winter_island_refugee_harbor` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_island_refugee_harbor.dds` | 210x176 | Overloaded civilian boats reaching a small island harbor or improvised anchorage under cold rain |
| `GFX_report_event_air_winter_desert_water_convoy` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_desert_water_convoy.dds` | 210x176 | Frost-split main, stone cistern, railway water tanker, and period truck in a culturally neutral arid city |
| `GFX_report_event_air_winter_dead_city_salvage` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_dead_city_salvage.dds` | 210x176 | Lamp-lit salvage crews beneath collapsed ash and ice covered city blocks |
| `GFX_report_event_air_winter_phase_5` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_5.dds` | 210x176 | Lower Yangtze ash winter and frozen water |
| `GFX_report_event_air_winter_phase_6` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_6.dds` | 210x176 | Terminally dim Central Asian settlement |
| `GFX_report_event_air_winter_recovery` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_recovery.dds` | 210x176 | Andean thaw, meltwater, and recovering soil |

## DDS and alpha contract

- Canvas: 210x176 pixels
- Stored image levels: one
- Compression: uncompressed 32-bit BGRA in the B8G8R8A8 style
- Channel masks: `00FF0000`, `0000FF00`, `000000FF`, and `FF000000`
- Row pitch: 840 bytes
- File size: 147,968 bytes per DDS
- Alpha choice: full 8-bit alpha is retained for the transparent report-card corners, antialiased tilted edges, and soft shadow
- Card treatment: grayscale, sepia tone, grain, four-degree tilt, transparent margins, and soft shadow from the repository report-event processor

Opaque DDS output is not suitable for these assets because it would replace the required transparent card margins with a rectangular matte.

## Ready-to-copy sprite definitions

```text
spriteType = {
	name = "GFX_report_event_air_winter_phase_1"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_1.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_phase_2"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_2.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_phase_3"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_3.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_phase_4"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_4.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_island_refugee_harbor"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_island_refugee_harbor.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_desert_water_convoy"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_desert_water_convoy.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_dead_city_salvage"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_dead_city_salvage.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_phase_5"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_5.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_phase_6"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_6.dds"
}
spriteType = {
	name = "GFX_report_event_air_winter_recovery"
	texturefile = "gfx/event_pictures/fallout/air_winter/report_event_air_winter_recovery.dds"
}
```

## Files created or updated

### Generated source PNGs

- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_1_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_2_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_3_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_4_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_island_refugee_harbor_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_desert_water_convoy_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_dead_city_salvage_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_5_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_6_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_recovery_source.png`

### Processed report-card PNGs

- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_1.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_2.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_3.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_4.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_island_refugee_harbor.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_desert_water_convoy.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_dead_city_salvage.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_5.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_6.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_recovery.png`

### Final runtime DDS files

- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_1.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_2.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_3.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_4.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_island_refugee_harbor.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_desert_water_convoy.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_dead_city_salvage.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_5.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_6.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_recovery.dds`

### Review and provenance files

- `docs/assets/air_cleanliness_fallout/contact_sheets/air_winter_report_events_final_contact_sheet.png`
- `docs/assets/air_cleanliness_fallout/manifest.md`
- `docs/assets/air_cleanliness_fallout/air_winter_report_event_gfx_handoff.md`

## Validation evidence

- All ten generated sources were visually reviewed at their original high resolution and contain distinct regional scenes with no embedded text or modern UI.
- The checkerboard contact sheet uses the processed PNGs after exact pixel-equality checks against all ten final DDS payloads, so its visual review covers the runtime content without relying on the review decoder's alpha display. Its captions identify the pixel-identical runtime payload and do not describe the sheet assembly source.
- Every processed PNG and DDS is exactly 210x176.
- Every final DDS decodes pixel-identically to its processed PNG.
- Every final DDS has four transparent corner pixels, a visible subtle tilt, a soft shadow, and readable source content after the cover crop.
- All ten source file hashes are distinct.
- All ten final DDS file hashes are distinct.
- DDS headers confirm 32-bit BGRA masks, 840-byte pitch, and one stored image level.
- The ten-asset contact sheet SHA-256 is `a46a3ec2acf91e4d6eca9e3c2ed5f75c570f34203a91835835e27a7675a8cc51`.
- The Desert City source, processed PNG, and DDS SHA-256 values are `e86a30ae3955a919e91a3aabc7c3615e7182daa4f78b04bea6f78b0d557f7fad`, `cedeca688fa3053a564aa4311f0bd1c78443857e4cbcda29702536b0770782b7`, and `39d1d3077dcc040c4985dde76dd6791c02c60743aee0e5b490d278427fec0c84`.

## Risks and remaining work

- All ten sprite identifiers are registered in `interface/air_cleanliness_winter.gfx` and consumed by `events/fallout_world_end_events.txt`.
- These are fictional generated documentary scenes. They must not be described as photographs of named real incidents or assigned archival provenance.
- No asset blocker remains.
- No fallback source, substitute art, simplification, or omitted requested phase was used.
