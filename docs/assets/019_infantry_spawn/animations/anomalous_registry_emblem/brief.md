# Anomalous Registry Emblem Animation Brief

- Asset: `anomalous_registry_emblem`.
- In-game use: indicates an active registered anomalous family or rising Anomalous Saturation.
- Surface: Muster Board Anomalous Registry tab emblem; decorative and state-driven.
- Frame size: `64x64`.
- Frame count: `10`.
- Horizontal sheet size: `640x64`.
- Playback: `5 FPS`, `looping = yes`, `play_on_show = yes`, no pause.
- Anchor: center.
- Static sprite: `GFX_019_infantry_spawn_anomalous_registry_emblem`.
- Animated sprite: `GFX_019_infantry_spawn_anomalous_registry_emblem_animated`.
- Source mode: ten separate `$imagegen` outputs on a flat chroma-key background, one for each authored registry state.
- Subject class: symbolic, family-neutral UI art.
- Visual direction: a compact military registry emblem combining a filed brass plate, an empty translucent band, a rough bound-stone segment, and an ordinary stamped rank. Across the loop, separate generated states alter the physical plate seams, etched non-text marks, translucent folds, stone binding, and interior aperture. It does not simply rotate, pulse, recolor, or translate.
- Static fallback: frame `000`, sealed and lowest-energy.
- Runtime DDS: `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_static.dds` and `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_sheet.dds`.
- Working PNG/GIF/contact paths: this animation folder under `processed_frames/`, `sheets/`, and `previews/`.
- Target GFX file: proposed `interface/019_infantry_spawn.gfx`.
- Target GUI file: proposed `interface/019_infantry_spawn.gui`; implementation owns active-family/saturation visibility.
- References inspected: offline Graphical Asset Modding, Interface Modding, and Scripted GUI Modding pages; vanilla `interface/alerts.gfx`; Chaos Redux Event 010 warning/emblem animations and Event 018 generated animation package.

