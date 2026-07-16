# Air Winter Report-Event GFX Handoff

Status: eight final report-event asset packages are registered and consumed.

## Package summary

- Runtime folder: `gfx/event_pictures/fallout/air_winter/`
- Source folder: `docs/assets/air_cleanliness_fallout/source_png/report_events/`
- Processed folder: `docs/assets/air_cleanliness_fallout/processed_png/report_events/`
- Final contact sheet: `docs/assets/air_cleanliness_fallout/contact_sheets/air_winter_report_events_final_contact_sheet.png`
- Existing event consumers: `events/fallout_world_end_events.txt`
- Island-refugee consumers: `chaosx.fallout.38` and `chaosx.fallout.39`
- Suggested registry: `interface/air_cleanliness_winter.gfx`
- Source mode: built-in `$imagegen`, fictional 1936 to 1945 period-documentary scenes

No `.gfx`, event, localisation, gameplay, GUI, or audio file was edited by this asset handoff.

## Stable sprite mapping

| Sprite identifier | Final DDS path | Dimensions | Visual state |
| --- | --- | --- | --- |
| `GFX_report_event_air_winter_phase_1` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_1.dds` | 210x176 | Dim first-stage regional cold in a Norwegian coastal village |
| `GFX_report_event_air_winter_phase_2` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_2.dds` | 210x176 | Bengal crop shock under impossible cold rain |
| `GFX_report_event_air_winter_phase_3` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_3.dds` | 210x176 | Canadian freight transport locked by hard freeze |
| `GFX_report_event_air_winter_phase_4` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_4.dds` | 210x176 | Greek black harvest and dead vegetation |
| `GFX_report_event_air_winter_island_refugee_harbor` | `gfx/event_pictures/fallout/air_winter/report_event_air_winter_island_refugee_harbor.dds` | 210x176 | Overloaded civilian boats reaching a small island harbor or improvised anchorage under cold rain |
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
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_5_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_phase_6_source.png`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_recovery_source.png`

### Processed report-card PNGs

- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_1.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_2.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_3.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_4.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_island_refugee_harbor.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_5.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_phase_6.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_recovery.png`

### Final runtime DDS files

- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_1.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_2.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_3.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_4.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_island_refugee_harbor.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_5.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_phase_6.dds`
- `gfx/event_pictures/fallout/air_winter/report_event_air_winter_recovery.dds`

### Review and provenance files

- `docs/assets/air_cleanliness_fallout/contact_sheets/air_winter_report_events_final_contact_sheet.png`
- `docs/assets/air_cleanliness_fallout/manifest.md`
- `docs/assets/air_cleanliness_fallout/air_winter_report_event_gfx_handoff.md`

## Validation evidence

- All eight generated sources were visually reviewed at 1536x1024 and contain distinct regional scenes with no embedded text or modern UI.
- All eight final DDS decodes were visually reviewed together on the checkerboard contact sheet.
- Every processed PNG and DDS is exactly 210x176.
- Every final DDS decodes pixel-identically to its processed PNG.
- Every final DDS has four transparent corner pixels, a visible subtle tilt, a soft shadow, and readable source content after the cover crop.
- All eight source file hashes are distinct.
- All eight final DDS file hashes are distinct.
- DDS headers confirm 32-bit BGRA masks, 840-byte pitch, and one stored image level.

## Risks and remaining work

- All eight sprite identifiers are registered in `interface/air_cleanliness_winter.gfx` and consumed by `events/fallout_world_end_events.txt`.
- These are fictional generated documentary scenes. They must not be described as photographs of named real incidents or assigned archival provenance.
- No asset blocker remains.
- No fallback source, substitute art, simplification, or omitted requested phase was used.
