# Event 019 Muster Board compact background handoff

Asset status: complete.

- Package DDS: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/runtime_dds/infantry_spawn_muster_board_background_compact_960x640.dds`
- Parent replacement path: `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`
- Sprite name to preserve: `GFX_infantry_spawn_muster_board_background`
- Target surface: direct scripted GUI Muster Board background for Event 019 Infantry Spawn.
- Target size: `960x640`.
- Suggested target `.gfx`: the existing Infantry Spawn interface sprite definition owned by the parent agent. No `.gfx` file was edited in this asset-only pass.
- Source mode: generated ImageGen fictional/symbolic UI panel with retained raw source, exact prompt record, deterministic processing evidence, and review sheet in this package.
- Canonical reference family inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png` for subdued period paper and restrained dossier surface treatment only; no vanilla art was reused.
- Review image: `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/review/infantry_spawn_muster_board_background_compact_contact_sheet.png`.

Ready-to-copy sprite definition snippet for the parent agent, if the existing definition already points at the stable path:

```text
spriteType = {
	name = "GFX_infantry_spawn_muster_board_background"
	texturefile = "gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds"
}
```

Composition handoff: the replacement art is intentionally compact and quiet. It uses only a thin charcoal/brass outer frame, one shallow top header strip, one broad uninterrupted paper field, and one narrow bottom action strip. The center remains open for parent-owned overlays. There are no slots, repeated wells, rails, cards, portraits, humans, readable words, pseudo-text, seals, emblems, icons, grids, filing pockets, stacked documents, tactical map marks, button-like boxes, or implied interactive affordances.

Processing handoff: ImageGen produced a `1536x1024` RGB source at `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/source_png/infantry_spawn_muster_board_background_compact_imagegen_1536x1024.png`. The full source canvas was resized with Pillow `Image.Resampling.LANCZOS` to the exact `960x640` processed preview without cropping or aspect distortion.

DDS QA: the repository converter produced a 128-byte-header, one-level uncompressed BGRA DDS with declared `960x640` dimensions, exact length `2457728`, pixel format `(32,65,0,32,0x00FF0000,0x0000FF00,0x000000FF,0xFF000000)`, texture caps `0x1000`, and alpha range `255..255`.

Parent action: copy or promote the package DDS to `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`, leave the sprite identifier unchanged, and verify GUI overlay rectangles against the deliberately open central paper field at runtime scale.

Remaining uncertainty: the background is neutral by design; functional text, cards, buttons, and close-button placement remain parent-owned GUI layers.
