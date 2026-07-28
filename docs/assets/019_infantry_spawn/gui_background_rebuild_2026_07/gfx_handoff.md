# Infantry Spawn Muster Board Background Handoff

Asset status: complete.

- Runtime DDS: `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`
- Sprite name: `GFX_infantry_spawn_muster_board_background`
- Target surface: direct scripted GUI Muster Board background for Event 019 Infantry Spawn.
- Target size: `1120x760`.
- Suggested target `.gfx`: the existing Infantry Spawn interface sprite definition owned by the main agent. No `.gfx` file was edited in this asset-only pass.
- Source mode: generated ImageGen fictional/symbolic UI panel, with the retained raw source and deterministic crop/resize evidence in this package.
- Review image: `docs/assets/019_infantry_spawn/gui_background_rebuild_2026_07/review/muster_board_background_contact_sheet.png`.

Ready-to-copy sprite definition snippet for the main agent:

```text
spriteType = {
	name = "GFX_infantry_spawn_muster_board_background"
	texturefile = "gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds"
}
```

Composition handoff: the art deliberately reserves a header title plaque, top tab/metric band, six left dossier wells, four central command zones (overview, formation lots, requests, history), a right registry/command well for claimant/command/anomalous surfaces, and a lower action band. The panel is front-facing, subdued, and text-safe; it contains no interactive buttons or readable in-image labels.

Runtime note: the source was centered-cropped from `1536x1024` to `1509x1024` at source box `(13,0)-(1522,1024)` and resized to the confirmed `1120x760` canvas with Pillow LANCZOS. The final DDS is opaque RGB data carried in the repository-standard 32-bit BGRA DDS format.

Remaining uncertainty: the main agent should check the GUI's exact overlay rectangles and close-button position in the live layout. Do not move or rename the final DDS without updating the consumer wiring.
