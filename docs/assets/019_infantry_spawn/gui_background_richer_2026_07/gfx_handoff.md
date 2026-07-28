# Event 019 richer Muster Board background handoff

Asset status: complete.

- Package DDS: `docs/assets/019_infantry_spawn/gui_background_richer_2026_07/runtime_dds/infantry_spawn_muster_board_background_richer_960x640.dds`
- Parent replacement path: `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`
- Sprite name to preserve: `GFX_infantry_spawn_muster_board_background`
- Target surface: direct scripted GUI Muster Board background for Event 019 Infantry Spawn.
- Target size: `960x640`.
- Suggested target `.gfx`: the existing Event 019 infantry-spawn interface sprite definition owned by the parent agent. No `.gfx` file was edited in this asset-only pass.
- Source mode: generated ImageGen fictional/symbolic UI panel with retained raw source, prompt record, deterministic processing evidence, review sheet, and exact DDS QA in this package.
- Canonical reference family inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png` for subdued period paper and restrained dossier surface treatment only; no vanilla art was reused.
- Review image: `docs/assets/019_infantry_spawn/gui_background_richer_2026_07/review/infantry_spawn_muster_board_background_richer_contact_sheet.png`.

Ready-to-copy sprite definition snippet for the parent agent, if the existing definition already points at the stable path:

```text
spriteType = {
	name = "GFX_infantry_spawn_muster_board_background"
	texturefile = "gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds"
}
```

Composition handoff: the replacement art is intentionally richer than the previous flat parchment while remaining restrained. It uses a continuous charcoal/brass frame with edge shading and shallow panel bands, muted military paper grain, sparse field-map/grid drafting marks, restrained red/steel traces, and one understated central muster compass seal. The center remains open for parent-owned overlays.

Affordance handoff: the final art has no words, pseudo-text, slots, wells, rails, cards, portraits, people, vehicles, buttons, controls, decorative compartments, corner hardware, or bottom-center inset. The seal is background decoration only and is not a standalone icon.

Processing handoff: ImageGen produced a `1536x1024` RGB source at `docs/assets/019_infantry_spawn/gui_background_richer_2026_07/source_png/infantry_spawn_muster_board_background_richer_imagegen_1536x1024.png`. A targeted ImageGen edit removed the initial bottom-center inset and corner hardware. The full source canvas was resized with Pillow `Image.Resampling.LANCZOS` to the exact `960x640` processed preview without cropping or aspect distortion.

DDS QA: the repository converter produced a 128-byte-header, one-level uncompressed BGRA DDS with declared `960x640` dimensions, exact length `2457728`, pixel format `(32,65,0,32,0x00FF0000,0x0000FF00,0x000000FF,0xFF000000)`, texture caps `0x1000`, mip count `0`, and alpha range `255..255`. The runtime DDS SHA-256 is `758a9ec88a7f329b9a3aaf7a6570135e1e15becb75ef1bfd8f1a8db8439aa849`.

Parent action: promote or copy the package DDS to `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`, leave the sprite identifier unchanged, and verify GUI overlay rectangles against the open central paper field at runtime scale.

Remaining limitations: the package is asset-only and does not edit `.gfx`, `.gui`, gameplay, localisation, or registry files. Functional text, cards, buttons, and close-button placement remain parent-owned GUI layers. The canonical reference root has no dedicated scripted-GUI background family, so `event_art/report` was used only as a restrained period-material style reference.
