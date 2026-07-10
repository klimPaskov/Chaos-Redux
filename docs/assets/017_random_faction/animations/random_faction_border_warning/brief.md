# Event 017 Border-Warning Animation Brief

- Asset: `random_faction_border_warning`
- In-game use: animated low-resilience warning icon for `random_faction_reinforce_border_posts` and `random_faction_guarantee_corridor_mission`.
- Gameplay surface: the standard decisions list through `icon = GFX_random_faction_border_warning_animated`; no custom `.gui` surface is required.
- Subject class: fictional symbolic UI art.
- Source mode: built-in `$imagegen` source atlas containing eight separately drawn visual states. The atlas and all eight sliced source frames are preserved.
- Reference inspection: the archived Event 17 reference sheet at `docs/assets/017_random_faction/contact_sheets/reference_contact_sheet.png`, the offline Graphical Asset Modding wiki page, and vanilla `interface/alerts.gfx` frame-animation examples.
- Target frame size: 64x64.
- Frame count: 8.
- Sheet size: 512x64, one horizontal row.
- Static sprite: `GFX_random_faction_border_warning_static`.
- Animated sprite: `GFX_random_faction_border_warning_animated`.
- Timing: 8 FPS, looping, `play_on_show = yes`, `pause_on_loop = 0.0`.
- Anchor: center. Mechanical processing centers each keyed subject and applies one shared sequence scale; the frame-authored lantern, beacon, wire, flag, and red-alert changes remain intact.
- State: state-driven warning art used by the border-post and corridor missions.
- Static fallback behavior: frame 000 at low amber alert.
- Source atlas: `docs/assets/017_random_faction/source/random_faction_border_warning_source_atlas.png`.
- Source frames: `docs/assets/017_random_faction/animations/random_faction_border_warning/source_frames/`.
- Processed frames: `docs/assets/017_random_faction/animations/random_faction_border_warning/processed_frames/`.
- Sheet PNG: `docs/assets/017_random_faction/animations/random_faction_border_warning/sheets/random_faction_border_warning_sheet.png`.
- Review contact sheet: `docs/assets/017_random_faction/animations/random_faction_border_warning/previews/random_faction_border_warning_contact.png`.
- Review-only GIF: `docs/assets/017_random_faction/animations/random_faction_border_warning/previews/random_faction_border_warning_preview.gif`.
- Final static DDS: `gfx/interface/animated/017_random_faction/random_faction_border_warning_static.dds`.
- Final sheet DDS: `gfx/interface/animated/017_random_faction/random_faction_border_warning_sheet.dds`.
- Target GFX registry: `interface/017_random_faction.gfx`.
- Canonical prompt record: `docs/assets/017_random_faction/prompts/icon_and_animation_prompts.md`.

## Static-versus-animated choice

The eight real source states give the low-resilience warning a clear amber-to-red escalation without transform-only motion. This full frame-authored sequence is more informative than a static-only warning border, while frame 000 remains the required static fallback.

## Processing note

The accepted source states were re-keyed with the official imagegen chroma helper using border-key sampling, soft matte, and despill. The sequence is normalized from the individual alpha bounds at a shared scale, and the final sheet copies each RGBA frame exactly without applying alpha a second time.
