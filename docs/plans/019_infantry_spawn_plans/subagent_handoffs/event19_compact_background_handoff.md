# Event 019 compact Muster Board background handoff

Status: complete.

## Deliverables

- Source PNG: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/source_png/infantry_spawn_muster_board_background_compact_imagegen_1536x1024.png`
- Processed PNG: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/processed_png/infantry_spawn_muster_board_background_compact_960x640.png`
- DDS: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/runtime_dds/infantry_spawn_muster_board_background_compact_960x640.dds`
- Prompt: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/prompt.md`
- Manifest: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/manifest.json`
- Review contact sheet: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/review/infantry_spawn_muster_board_background_compact_contact_sheet.png`
- GFX handoff: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/gfx_handoff.md`

## Parent-owned runtime wiring

- Preserve the runtime sprite identifier `GFX_infantry_spawn_muster_board_background`.
- Replace the current runtime texture at `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds` with the package DDS during parent-owned wiring.
- No `.gfx`, GUI, gameplay, localisation, event, or spreadsheet files were edited by this asset-only pass.

## Visual direction delivered

The new panel is a completely new generated surface intended to correct the rejected board's remaining density. It has a restrained charcoal/brass outer frame, one shallow top header band, one broad uninterrupted paper field, and one narrow bottom action band. The center is deliberately open and quiet.

The source and processed views contain no slots, wells, rails, cards, portraits, people, army scenes, readable text, icons, tactical grids, buttons, repeated compartments, stacked documents, filing pockets, map-dominant diagrams, or extra information.

## Generation and processing evidence

- Source mode: OpenAI built-in `image_gen`.
- Generation run folder: `019faa5f-1fc7-7d11-ae1d-4dc94e4137e5`.
- Source dimensions and mode: `1536x1024`, RGB.
- Source SHA-256: `ad859d60046d8795fa1ea092dd97b99e8438380c4563f0d3e98aee41533f5600`.
- Deterministic processing: full-canvas Pillow `Image.Resampling.LANCZOS` resize to `960x640`, no crop and no aspect distortion.
- Processed SHA-256: `8002ef761d1632a79c6f8057d35e5555ee14f0cfea0c58a83c32c2a593320fdd`.
- DDS SHA-256: `b14d371f5805d911f8db07d7ae6f0fd4255b4042c26bf38b94bc5fe6c61355bb`.
- Contact-sheet SHA-256: `5ee25f97b82a5f3c22775afb6120927748f3fe78416e43f985c007fbff3b5fcf`.

## DDS conversion evidence

The repository-standard converter at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced the final DDS.

The DDS has a `128` byte legacy header, declared `960x640` dimensions, exact file length `2457728` bytes, one-level uncompressed BGRA pixel format with masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`, texture caps `0x1000`, and alpha range `255..255`.

## Reference and limitations

The canonical reference root has no dedicated scripted-GUI background family. The matching `event_art/report` contact sheet was inspected only for subdued period paper and restrained dossier surface treatment; no reference art was reused.

The package DDS remains under `docs/assets/` until the parent agent promotes it to the runtime path. Functional overlay rectangles, text, controls, and close-button placement remain parent-owned and should be checked against the open central field.
