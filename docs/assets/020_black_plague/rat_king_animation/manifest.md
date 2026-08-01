# Event 020 Rat King source-frame portrait animation

This package supplies the authored Evolution IV Rat King portrait used by the existing Events Log detail surface. It does not create a new country, tag, unit, model, or disease category. The static `RTA`/`RTX` leader portrait remains the fallback for ordinary country and non-Evolution views.

## Runtime contract

| Consumer | Stable key | Runtime file | Dimensions | Frames | Rate |
| --- | --- | --- | ---: | ---: | ---: |
| Events Log Evolution IV portrait | `GFX_portrait_black_plague_rat_king_animated` | `gfx/leaders/020_black_plague/portrait_rat_king_animated_sheet.dds` | 1560x210 | 10 | 8 fps, looping |
| Static fallback | `GFX_portrait_black_plague_rat_king` | `gfx/leaders/020_black_plague/portrait_rat_king_static.dds` | 156x210 | 1 | n/a |

The sheet is registered in `interface/020_black_plague_rat_identity.gfx`. `GetEventsLogSelectedEvolutionPortrait` selects the animated sprite only for Event 020 Evolution IV, and `has_events_log_selected_evolution_authored_portrait` keeps the existing authored-portrait gate aligned with that selection.

## Source and processing

Frame 01 preserves the canonical static Rat King source at `docs/assets/020_black_plague/source_png/portraits/leader_rat_king_static_imagegen_source.png`. Frames 02 through 10 were generated as separate edits of that identity using the built-in image generation workflow, with prompts limited to authored breathing, blinking, whisker, ear, eye-glint, mantle, and restrained head-motion changes. No frame is a transform-only animation of one still. The generated sources remain in `source_png/` with RGB mode and their native 1080–1082 by 1454–1456 dimensions.

Each source frame is center-fitted with Lanczos resampling to an opaque RGB 156x210 processed portrait. The processed frames are packed left-to-right into `processed_png/black_plague_rat_king_animation_sheet.png` and converted to the uncompressed BGRA DDS consumed by the game. The GIF and contact sheet in `previews/` are review evidence only; the DDS sheet is the runtime asset.

| Item | Evidence |
| --- | --- |
| Source frames | `source_png/black_plague_rat_king_frame_01_source.png` through `black_plague_rat_king_frame_10_source.png` |
| Processed frames | `processed_png/black_plague_rat_king_frame_01.png` through `black_plague_rat_king_frame_10.png` |
| Packed sheet | `processed_png/black_plague_rat_king_animation_sheet.png` (1560x210 RGB) |
| Review GIF | `previews/black_plague_rat_king_animation.gif` |
| Review contact sheet | `previews/black_plague_rat_king_contact_sheet.png` |
| Runtime DDS | `gfx/leaders/020_black_plague/portrait_rat_king_animated_sheet.dds` (1560x210 BGRA, one mip) |

The DDS SHA-256 is `de00bc3f88d2ea4a2b5b126053618b15ab2070cf9906a45374411fef875a4883`. Processed sheet SHA-256 is `16eefc58fa16a60a88381d4ee008227540d81b452237526c2788c184d6cf7eba`.

## Remaining presentation work

The source-frame crisis-seal package remains a separate accepted follow-up. Rat Nation and Rat King 3D unit models and skeletal actions are intentionally outside Event 020 and are not runtime prerequisites.
