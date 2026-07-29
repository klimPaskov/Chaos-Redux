# Runtime GFX Handoff

## Consumer contract

HOI4 loads country flags from the base tag filenames in `gfx/flags/` and its `medium/` and `small/` subdirectories.

No `.gfx` sprite registration is needed for these country-flag consumers.

## Delivered runtime files

| Tag | Normal | Medium | Small |
|---|---|---|---|
| `DOX` | `gfx/flags/DOX.tga` | `gfx/flags/medium/DOX.tga` | `gfx/flags/small/DOX.tga` |
| `DSX` | `gfx/flags/DSX.tga` | `gfx/flags/medium/DSX.tga` | `gfx/flags/small/DSX.tga` |
| `DUX` | `gfx/flags/DUX.tga` | `gfx/flags/medium/DUX.tga` | `gfx/flags/small/DUX.tga` |
| `DYX` | `gfx/flags/DYX.tga` | `gfx/flags/medium/DYX.tga` | `gfx/flags/small/DYX.tga` |
| `DZX` | `gfx/flags/DZX.tga` | `gfx/flags/medium/DZX.tga` | `gfx/flags/small/DZX.tga` |
| `EMX` | `gfx/flags/EMX.tga` | `gfx/flags/medium/EMX.tga` | `gfx/flags/small/EMX.tga` |
| `EQX` | `gfx/flags/EQX.tga` | `gfx/flags/medium/EQX.tga` | `gfx/flags/small/EQX.tga` |

## Format

- Normal: `82x52`
- Medium: `41x26`
- Small: `10x7`
- Encoding: uncompressed true-color 32-bit TGA
- Channel payload: BGRA
- Alpha: opaque
- Origin: bottom-left

## Visual acceptance evidence

The [contact sheet](contact_sheets/africa_revival_flag_ladders_contact_sheet.png) shows the source, flattened master, and decoded runtime ladder for every tag.

The small variants deliberately prioritize a bold surviving silhouette over fine ornament.

The full machine-readable validation is stored in [notes/validation.json](notes/validation.json).

## Historical-status note

`DOX` uses the approved public-domain Asante source design.

`DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` are original fictional 1936 revival flags and must not be documented as historical reconstructions.
