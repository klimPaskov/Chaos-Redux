# Fury Leader Flame Overlay Asset Manifest

## Asset Record

- Asset name: `fury_leader_flame_overlay`
- Event id: `007`
- Event slug: `fury`
- Asset type: animated scripted GUI leader portrait overlay
- In-game use: decorative flame loop shown over selected Fury country leader portraits in the diplomacy tab
- Source mode: `$imagegen`, built-in tool
- Source prompt: generated as an 8-frame horizontal HOI4-style supernatural fire overlay sheet on a flat `#00ff00` chroma-key background; flame tongues rise from the lower and side edges of a `156x210` leader portrait while keeping the central face area clear; no text, symbols, modern UI, checkerboard, watermark, shadows, or full opaque border.
- Source PNG sheet: `docs/assets/007_fury/leader_flame_overlay/source_png/fury_leader_flame_overlay_source_sheet.png`
- Source frame PNGs: `docs/assets/007_fury/leader_flame_overlay/source_png/fury_leader_flame_overlay_000_source.png` through `fury_leader_flame_overlay_007_source.png`
- Processed frame PNGs: `docs/assets/007_fury/leader_flame_overlay/processed_png/fury_leader_flame_overlay_000.png` through `fury_leader_flame_overlay_007.png`
- Sheet PNG: `docs/assets/007_fury/leader_flame_overlay/sheets/fury_leader_flame_overlay_sheet.png`
- Static fallback PNG: `docs/assets/007_fury/leader_flame_overlay/sheets/fury_leader_flame_overlay_static.png`
- Final sheet DDS: `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_sheet.dds`
- Final static DDS: `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_static.dds`
- Contact sheet: `docs/assets/007_fury/leader_flame_overlay/previews/fury_leader_flame_overlay_contact.png`
- Review GIF: `docs/assets/007_fury/leader_flame_overlay/previews/fury_leader_flame_overlay_preview.gif`
- Target size: `156x210`
- Sheet size: `1248x210`
- Frame count: `8`
- Animation rate: `8 fps`
- Loop behavior: looping, play on show
- Static fallback: frame `000`
- Sprite names: `GFX_fury_leader_flame_overlay_animated`, `GFX_fury_leader_flame_overlay_static`
- `.gfx` file: `interface/007_fury.gfx`
- `.gui` file: `interface/007_fury_leader_overlay.gui`
- Scripted GUI file: `common/scripted_guis/007_fury_scripted_guis.txt`
- Status: `complete`

## Processing Notes

The generated source sheet was larger than the requested final sheet, so the eight generated panels were cropped, resized to exact `156x210` frames, and rebuilt into the final `1248x210` horizontal frame sheet. Local chroma-key removal used ImageMagick with a stronger green tolerance because the installed helper was present but Pillow was unavailable in the active Python environment. The final contact sheet shows no green background field and preserves the intended fire loop.

DDS files were exported with ImageMagick using uncompressed DDS output. `identify` reports both final DDS files with `srgba` channels, with the animated sheet at `1248x210` and the static fallback at `156x210`.
