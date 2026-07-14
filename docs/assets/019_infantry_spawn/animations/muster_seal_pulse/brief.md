# Muster Seal Pulse Animation Brief

- Asset: `muster_seal_pulse`
- In-game use: signals unresolved formation lots on the Event 19 decision category or Muster Board Overview tab.
- Surface: scripted GUI / decision-category decoration; decorative state communication, not a button hitbox.
- Frame size: `64x64`.
- Frame count: `8`.
- Horizontal sheet size: `512x64`.
- Playback: `8 FPS`, `looping = yes`, `play_on_show = yes`, no pause.
- Anchor: center.
- Static sprite: `GFX_019_infantry_spawn_muster_seal`.
- Animated sprite: `GFX_019_infantry_spawn_muster_seal_animated`.
- Source mode: eight separate `$imagegen` outputs on a flat chroma-key background, one for each authored seal state.
- Subject class: symbolic UI-only military registry art.
- Visual direction: a dented 1930s military muster seal whose wax, stamped ranks, paper fibers, and inset metal respond in distinct drawn states as unresolved lots accumulate. The motion comes from changed cracks, impressions, raised paper, tiny filing tabs, and light-bearing grooves, not from translating, scaling, rotating, recoloring, or filtering one still.
- Static fallback: frame `000`, the lowest-energy but fully readable seal state.
- Runtime DDS: `gfx/interface/019_infantry_spawn/muster_seal_pulse_static.dds` and `gfx/interface/019_infantry_spawn/muster_seal_pulse_sheet.dds`.
- Working PNG/GIF/contact paths: this animation folder under `processed_frames/`, `sheets/`, and `previews/`.
- Target GFX file: proposed `interface/019_infantry_spawn.gfx`.
- Target GUI file: proposed `interface/019_infantry_spawn.gui`; implementation owns exact placement and visibility trigger.
- References inspected: offline Graphical Asset Modding, Interface Modding, and Scripted GUI Modding pages; vanilla `interface/alerts.gfx`; Chaos Redux `interface/007_fury.gfx`, `interface/010_death.gfx`, and the Event 018 eight-frame generated animation package.

