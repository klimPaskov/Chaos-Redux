# Event 023 breakaway custody report asset handoff

Status: needs_user_review. The generated source, processed report-card PNG, final DDS, decoded review, manifest entry, package validation note, and sprite handoff are complete. Parent-owned `.gfx` registration and live event wiring remain outstanding.

## Asset identity

- Event: `023_sov_nuclear_bombs`.
- Asset: `sov_nuclear_breakaway_custody_report`.
- Runtime sprite: `GFX_report_event_sov_nuclear_breakaway_custody`.
- Target `.gfx`: `interface/023_sov_nuclear_bombs.gfx`.
- Final DDS: `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_breakaway_custody.dds`.
- Target canvas: `210x176`.
- Intended consumer: the existing Event 23 report picture for guarded breakaway custody review.
- Source provenance: generated with the built-in official ImageGen workflow; no internet or archival source was used.
- ImageGen output captured from `C:\Users\klimp\.codex\generated_images\01a06eaa-62ab-74a1-925c-575f63c83e31\exec-186ace8b-3b2b-4c56-a33b-2b99d6f3c915.png` and retained in the package as the source PNG.

The composition is a sober 1940s alternate-history Soviet depot inspection: sealed cylindrical and rectangular device containers, wax seals, tied custody folders, keys, ledgers, three anonymous inspectors, two background guards, and railway tracks beyond the loading doors. It is distinct from the existing breakaway-custody news picture, which is a wide exterior rail-loading scene dominated by a large cylindrical device and a larger guard detail.

## Files changed by this handoff

- `docs/assets/023_sov_nuclear_bombs/prompts/sov_nuclear_breakaway_custody_report.txt`
- `docs/assets/023_sov_nuclear_bombs/source_png/sov_nuclear_breakaway_custody_report_source.png`
- `docs/assets/023_sov_nuclear_bombs/processed_png/report_event_sov_nuclear_breakaway_custody.png`
- `docs/assets/023_sov_nuclear_bombs/notes/decoded_dds/report_event_sov_nuclear_breakaway_custody_dds_roundtrip.png`
- `docs/assets/023_sov_nuclear_bombs/contact_sheets/report_event_sov_nuclear_breakaway_custody_review.png`
- `docs/assets/023_sov_nuclear_bombs/manifest.md`
- `docs/assets/023_sov_nuclear_bombs/notes/validation.md`
- `docs/assets/023_sov_nuclear_bombs/gfx_handoff.md`
- `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_breakaway_custody.dds`
- `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_breakaway_report_asset.md`

No `.gfx`, event, gameplay, localisation, GUI, portrait, flag, icon, animation, or 3D-model file was edited.

## Dimensions and hashes

| File | Dimensions/mode | SHA-256 |
| --- | --- | --- |
| `source_png/sov_nuclear_breakaway_custody_report_source.png` | `1537x1023`, RGB, opaque source | `1376e6841bbab30ffddd6f9a32e13cdf36c283920c5d511072e6586928896930` |
| `processed_png/report_event_sov_nuclear_breakaway_custody.png` | `210x176`, RGBA, report-card alpha | `0397ef1182ef8bd774f4ef84d4905f867e66a8c79ec290827f5071093210b7db` |
| `notes/decoded_dds/report_event_sov_nuclear_breakaway_custody_dds_roundtrip.png` | `210x176`, RGBA, decoded DDS | `0397ef1182ef8bd774f4ef84d4905f867e66a8c79ec290827f5071093210b7db` |
| `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_breakaway_custody.dds` | `210x176`, legacy BGRA DDS, `147968` bytes | `324a455d691f010963471cfed4948d548a8b379b4768a8cb66a586a12e021f4d` |

## Processing and conversion commands

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py `
    docs/assets/023_sov_nuclear_bombs/source_png/sov_nuclear_breakaway_custody_report_source.png `
    docs/assets/023_sov_nuclear_bombs/processed_png/report_event_sov_nuclear_breakaway_custody.png

python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py `
    --input docs/assets/023_sov_nuclear_bombs/processed_png/report_event_sov_nuclear_breakaway_custody.png `
    --output gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_breakaway_custody.dds `
    --width 210 --height 176
```

The report processor supplied the standard black-and-white/sepia treatment, subtle tilt, paper edge, grain, soft shadow, and transparent outer canvas corners. No background-removal fallback was used.

## Validation evidence

- Source PNG opened as `1537x1023` RGB and is fully opaque as an input photograph.
- Processed PNG opened as exactly `210x176` RGBA with alpha range `0..255`; all four canvas corners have alpha `0`.
- Final DDS is exactly `147968` bytes, equal to `128 + 210*176*4`.
- DDS header: magic `DDS `; `DDS_HEADER` size `124`; `DDS_PIXELFORMAT` at byte `76` with size `32`, flags `65`, fourCC `0`, RGB bit count `32`, masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`; `DDSCAPS_TEXTURE` set; mipmap count `0` for the one-level texture.
- Decoded DDS alpha range is `0..255`, with `2932` zero-alpha pixels and `27544` fully opaque pixels; all four corners decode to alpha `0`.
- Decoded visible alpha bounds are `[4, 5, 209, 175]` on the `210x176` canvas.
- Decoded DDS pixels are byte-for-byte identical to the processed PNG after BGRA-to-RGBA decode.
- The individual decoded review is `docs/assets/023_sov_nuclear_bombs/notes/decoded_dds/report_event_sov_nuclear_breakaway_custody_dds_roundtrip.png`.
- The bounded visual comparison is `docs/assets/023_sov_nuclear_bombs/contact_sheets/report_event_sov_nuclear_breakaway_custody_review.png`; it shows the generated source, processed card, and decoded DDS on a checkerboard behind the transparent corners.
- Visual review found the requested custody evidence and restrained period atmosphere, with no readable generated text, watermark, UI artifact, modern equipment, gore, or mushroom-cloud spectacle.

The asset remains `needs_user_review` until the parent reviews the bounded sheet, registers `GFX_report_event_sov_nuclear_breakaway_custody` in the selected Event 23 `.gfx`, and wires the existing report consumer.
