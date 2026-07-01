# Event 013 Natural Disasters Animation Alpha Cleanup Handoff

## Scope

Regenerated the five existing Event 013 animated sprite packages to remove green chroma-key alpha/matte contamination. No `.gfx`, gameplay, GUI, localisation, master manifest, event docs, or spreadsheet files were edited.

Existing sprite names preserved from `interface/013_natural_disasters.gfx`:

| Package | Static sprite | Animated sprite |
| --- | --- | --- |
| `natural_disaster_warning_pulse` | `GFX_natural_disaster_warning_pulse_static` | `GFX_natural_disaster_warning_pulse_animated` |
| `natural_disaster_storm_corridor_track` | `GFX_natural_disaster_storm_corridor_track_static` | `GFX_natural_disaster_storm_corridor_track_animated` |
| `natural_disaster_tsunami_countdown` | `GFX_natural_disaster_tsunami_countdown_static` | `GFX_natural_disaster_tsunami_countdown_animated` |
| `natural_disaster_eruption_ashfall` | `GFX_natural_disaster_eruption_ashfall_static` | `GFX_natural_disaster_eruption_ashfall_animated` |
| `natural_disaster_skyfall_alarm` | `GFX_natural_disaster_skyfall_alarm_static` | `GFX_natural_disaster_skyfall_alarm_animated` |

## Package Outputs

All packages use the existing `.gfx` metadata: 8 frames, 8 fps, 36x36 frame size, 288x36 horizontal sheet size, looping review GIF.

| Package | Source frames | Processed frames | Sheet PNG | Static DDS | Sheet DDS |
| --- | --- | --- | --- | --- | --- |
| `natural_disaster_warning_pulse` | `docs/assets/013_natural_disasters/animations/natural_disaster_warning_pulse/source_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_warning_pulse/processed_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_warning_pulse/sheets/natural_disaster_warning_pulse_sheet.png` | `gfx/interface/animated/013_natural_disasters/natural_disaster_warning_pulse_static.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_warning_pulse_sheet.dds` |
| `natural_disaster_storm_corridor_track` | `docs/assets/013_natural_disasters/animations/natural_disaster_storm_corridor_track/source_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_storm_corridor_track/processed_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_storm_corridor_track/sheets/natural_disaster_storm_corridor_track_sheet.png` | `gfx/interface/animated/013_natural_disasters/natural_disaster_storm_corridor_track_static.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_storm_corridor_track_sheet.dds` |
| `natural_disaster_tsunami_countdown` | `docs/assets/013_natural_disasters/animations/natural_disaster_tsunami_countdown/source_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_tsunami_countdown/processed_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_tsunami_countdown/sheets/natural_disaster_tsunami_countdown_sheet.png` | `gfx/interface/animated/013_natural_disasters/natural_disaster_tsunami_countdown_static.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_tsunami_countdown_sheet.dds` |
| `natural_disaster_eruption_ashfall` | `docs/assets/013_natural_disasters/animations/natural_disaster_eruption_ashfall/source_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_eruption_ashfall/processed_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_eruption_ashfall/sheets/natural_disaster_eruption_ashfall_sheet.png` | `gfx/interface/animated/013_natural_disasters/natural_disaster_eruption_ashfall_static.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_eruption_ashfall_sheet.dds` |
| `natural_disaster_skyfall_alarm` | `docs/assets/013_natural_disasters/animations/natural_disaster_skyfall_alarm/source_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_skyfall_alarm/processed_frames/` | `docs/assets/013_natural_disasters/animations/natural_disaster_skyfall_alarm/sheets/natural_disaster_skyfall_alarm_sheet.png` | `gfx/interface/animated/013_natural_disasters/natural_disaster_skyfall_alarm_static.dds` | `gfx/interface/animated/013_natural_disasters/natural_disaster_skyfall_alarm_sheet.dds` |

Package DDS copies were also written under:

- `docs/assets/013_natural_disasters/dds/<slug>_static.dds`
- `docs/assets/013_natural_disasters/dds/<slug>_sheet.dds`

Review assets were updated in each package's `previews/` folder:

- `<slug>_preview.gif`
- `<slug>_contact.png`

Additional copied contact sheets for quick review:

- `docs/assets/013_natural_disasters/contact_sheets/<slug>_contact.png`

Static fallback PNGs were added in each package's `sheets/` folder as `<slug>_static.png`.

## Cleanup Method

- Preserved the existing real per-frame source artwork and frame order.
- Cleaned source-frame alpha in place by removing chroma-key green pixels and forcing fully transparent pixels to RGB `0,0,0`.
- Reprocessed existing 36x36 frames with package-specific despill:
  - warning pulse: warm amber/gold
  - storm corridor track: cool blue-gray
  - tsunami countdown: muted blue-gray
  - eruption ashfall: ash/orange
  - skyfall alarm: orange-red
- Rebuilt horizontal sheet PNGs from the cleaned processed frames.
- Re-exported uncompressed 32-bit DDS files for both package copies and in-game copies.
- Regenerated review GIFs and checker-background contact sheets.

## Validation

Validated with Python/Pillow after export:

- Every package has 8 source frames and 8 processed frames.
- Every processed frame is exactly 36x36.
- Every sheet PNG and sheet DDS is exactly 288x36.
- Every static DDS is exactly 36x36.
- Both `docs/assets/013_natural_disasters/dds/` and `gfx/interface/animated/013_natural_disasters/` DDS copies were checked.
- DDS header masks match the existing uncompressed 32-bit RGBA-style output: `0xff0000`, `0xff00`, `0xff`, `0xff000000`.
- Key-green alpha-bearing pixels: `0` in all processed frames and all exported DDS files.
- Nonzero RGB under fully transparent alpha: `0` in all source frames, processed frames, and exported DDS files.
- DDS corner pixels are fully transparent `0,0,0,0` for all statics and sheets.
- Contact sheets were visually inspected over a checker background.

## Remaining Risks

- The source frames were salvaged from the existing generated frame art rather than replaced with new `$imagegen` outputs because the real per-frame artwork was usable once chroma contamination was removed.
- No `.gfx` changes were made by request. The parent should keep the existing `noOfFrames = 8` and `animation_rate_fps = 8` entries.
- Master manifest and event documentation were not updated because they were outside this subagent's write scope.
