# 2026-07-28 GUI Background Rebuild Handoff

## Scope

Replaced the static runtime background for the direct scripted-GUI Infantry Spawn Muster Board. This handoff covers exactly one asset: `GFX_infantry_spawn_muster_board_background`.

## Changed asset files

- `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds` — replaced runtime texture, `1120x760`, legacy one-level uncompressed BGRA DDS.
- `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/source_png/infantry_spawn_muster_board_background_imagegen_1536x1024.png` — retained raw ImageGen output, `1536x1024` RGB.
- `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/processed_png/infantry_spawn_muster_board_background_1120x760.png` — retained processed preview, `1120x760` RGB.
- `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/review/muster_board_background_contact_sheet.png` — visual review sheet showing raw and processed variants.
- `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/manifest.json` — generation, processing, runtime, checksum, and review manifest.
- `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/gfx_handoff.md` — main-agent sprite/path handoff.

No `.gfx`, `.gui`, gameplay, localisation, focus, decision, spreadsheet, or event files were edited.

## Dimensions and processing evidence

The confirmed runtime target is `1120x760` (aspect `1.4736842105`). ImageGen produced a `1536x1024` source. A centered crop box `(13,0)-(1522,1024)` yielded `1509x1024`, then Pillow `Image.Resampling.LANCZOS` resized it to exactly `1120x760` without stretch. The crop removes only 13/14 pixels from the left/right edges and preserves all vertical content.

## Checksums

- Raw ImageGen source PNG SHA-256: `8433e8c518b46c24751b6363d7a80b394927dc2d8351be02a69d206498d46236`.
- Processed `1120x760` PNG SHA-256: `f23e5d1f927639c39845b1d7bc19b53d749ec8bc3b23a5eed822ded40f458d4c`.
- Final runtime DDS SHA-256: `eed2930bcb9717e269f5821a3f13f0e1b8929a73e1db9a0ebfc8393ebbd58502`.
- Final DDS length: `3,404,928` bytes (`128 + 1120 * 760 * 4`).

## Generation and provenance

Source mode is `generated_imagegen` using the official built-in ImageGen workflow, run id `019fa75b-caed-7982-abb4-069b9c91b3fb`. The prompt requested a front-facing HOI4-style painted 1930s–1940s metal-and-wood command dossier board with functional overlay zones, no people or portraits, no readable words or pseudo-text, no buttons, and restrained anomalous registry motifs. The existing project source at `docs/assets/019_infantry_spawn/source_png/gui/infantry_spawn_muster_board_background_source.png` was supplied as a style/layout reference only; it was not copied into the runtime output.

The canonical vanilla reference library contains no dedicated scripted-GUI/UI-panel family. The nearest HOI4 report-art contact sheet was consulted only for restrained period palette and surface treatment. No real person, real place, historical event, or archival source is depicted.

## Visual review notes

- Six stacked left-rail dossier wells are visually distinct and sized for overlay content.
- The central command surface is intentionally divided into overview/map, formation-lot grid, request-list, and history/anomaly sub-zones.
- The right-side registry/command well includes a document map plate, seal slots, a filing pocket, and paper stack for claimant, command, and anomalous surfaces.
- Header plaque, top metric/tab band, and lower action band provide distinct text-safe overlay surfaces.
- Important decoration is kept away from the future close-button area at upper-right.
- The generated panel contains no humans, portraits, readable generated words, pseudo-text, modern props, or interactive button art.

## Validation performed

The standard repository converter was run:

`python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/processed_png/infantry_spawn_muster_board_background_1120x760.png --output gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds --width 1120 --height 760`

The DDS header was checked for `DDS ` magic, header size `124`, declared height/width `760x1120`, `DDS_PIXELFORMAT` `(32,65,0,32,0x00FF0000,0x0000FF00,0x000000FF,0xFF000000)`, texture caps `0x1000`, exact file length, and alpha range `255..255`. All checks passed.

## Remaining risks

- The main agent must verify the GUI's exact content rectangles and close-button placement against this final art at runtime scale.
- The main agent owns `.gfx` and `.gui` wiring; keep the sprite name and stable DDS path unchanged.
