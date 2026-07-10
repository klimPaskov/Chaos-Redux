# Event 017 Bloc-Pressure Seal Animation Brief

- Asset: `random_faction_bloc_pressure_seal`
- In-game use: animated decision icon for `random_faction_convene_neutrality_council`.
- Gameplay surface: the standard decisions list through `icon = GFX_random_faction_bloc_pressure_seal_animated`; no custom `.gui` surface is required.
- Subject class: fictional symbolic UI art.
- Source mode: built-in `$imagegen` source atlas containing eight separately drawn visual states. The atlas and all eight sliced source frames are preserved.
- Reference inspection: the archived Event 17 reference sheet at `docs/assets/017_random_faction/contact_sheets/reference_contact_sheet.png`, the offline Graphical Asset Modding wiki page, and vanilla `interface/alerts.gfx` frame-animation examples.
- Target frame size: 64x64.
- Frame count: 8.
- Sheet size: 512x64, one horizontal row.
- Static sprite: `GFX_random_faction_bloc_pressure_seal_static`.
- Animated sprite: `GFX_random_faction_bloc_pressure_seal_animated`.
- Timing: 8 FPS, looping, `play_on_show = yes`, `pause_on_loop = 0.0`.
- Anchor: center. Mechanical processing centers each keyed subject and applies one shared sequence scale; the intended frame-specific cloth, cable, paper, seal-light, and spark changes remain in the source art.
- State: decorative active-state art used while the country can interact with the neutrality-council decision.
- Static fallback behavior: frame 000 at rest.
- Source atlas: `docs/assets/017_random_faction/source/random_faction_bloc_pressure_seal_source_atlas.png`.
- Source frames: `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/source_frames/`.
- Processed frames: `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/processed_frames/`.
- Sheet PNG: `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/sheets/random_faction_bloc_pressure_seal_sheet.png`.
- Review contact sheet: `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/previews/random_faction_bloc_pressure_seal_contact.png`.
- Review-only GIF: `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/previews/random_faction_bloc_pressure_seal_preview.gif`.
- Final static DDS: `gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_static.dds`.
- Final sheet DDS: `gfx/interface/animated/017_random_faction/random_faction_bloc_pressure_seal_sheet.dds`.
- Target GFX registry: `interface/017_random_faction.gfx`.
- Canonical prompt record: `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md`.

## Processing note

The accepted source states were re-keyed with the official imagegen chroma helper using border-key sampling, soft matte, and despill. The sequence is normalized from the individual alpha bounds at a shared scale, and the final sheet copies each RGBA frame exactly without applying alpha a second time.
