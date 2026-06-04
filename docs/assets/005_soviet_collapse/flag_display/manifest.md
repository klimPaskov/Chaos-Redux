# Soviet Collapse Flag Display Manifest

## Purpose

Some Soviet Collapse country flag TGAs use image-origin metadata that can display inverted when custom scripted GUI icon properties resolve flags through `[GetFlag]`. The actual country flag files under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` are intentionally left unchanged.

This display package provides 41x26 DDS UI copies for custom Chaos Redux panels that need stable upright rendering.

## Final Assets

- Final display DDS folder: `gfx/interface/flags/soviet_collapse_display/`
- Sprite registry: `interface/005_soviet_collapse_flag_display.gfx`
- Scripted localisation routing: `common/scripted_localisation/005_soviet_collapse_flag_display_scripted_localisation.txt`
- Custom GUI consumers:
  - `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
  - `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt`

## Scope

The display set covers Soviet Collapse custom flag tags and ideology variants present in `gfx/flags/medium/` at generation time. Non-Soviet Collapse flag packages such as Event 006 Zulu and Darfur are not routed through this package.

## Validation

- Display DDS files are 41x26 DXT5 assets matching the vanilla `GFX_flag_small2` texture size.
- `gfx/flags/**` country flag TGAs are not modified by this package.
