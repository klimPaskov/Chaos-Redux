# Natural disaster warning pulse brief

- Asset name: `natural_disaster_warning_pulse`.
- Accepted role: auxiliary warning marker for the abnormal map or category header; it does not replace the accepted `540x88` warning card frame.
- Target frame size: `36x36`.
- Frame count: `8`.
- Sheet size: `288x36`.
- Static sprite: `GFX_013_warning_pulse`.
- Animated sprite: `GFX_013_warning_pulse_animated`.
- Animation rate: `25/3 fps` (the retained GIF encodes 120 ms per frame, about `8.33 fps`).
- Looping: `yes`.
- `play_on_show`: `yes`.
- Anchor: center.
- Static fallback: `sheets/natural_disaster_warning_pulse_static.png` and `gfx/interface/animated/013_natural_disasters/natural_disaster_warning_pulse_static.dds`.
- Sheet: `sheets/natural_disaster_warning_pulse_sheet.png` and `gfx/interface/animated/013_natural_disasters/natural_disaster_warning_pulse_sheet.dds`.
- Review-only preview/contact: `previews/natural_disaster_warning_pulse_preview.gif` and `previews/natural_disaster_warning_pulse_contact.png`.
- Source mode: generated `4x2` animation source sheet, then sliced into eight source cells and normalized. The exact original generation prompt and built-in result identifier were not retained; `notes/provenance.md` records the recoverable evidence without inventing history.
- Target `.gfx`: `interface/013_natural_disasters.gfx`.
- Target `.gui`: `interface/013_natural_disasters.gui`, proposed auxiliary element `natural_disaster_warning_pulse_marker`.

