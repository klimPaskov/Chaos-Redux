# Critical Command Border Animation Brief

- Asset: `critical_command_border`.
- In-game use: frames the claimant portrait while revolt risk is in the critical band.
- Surface: Muster Board Command tab portrait overlay; decorative and state-driven.
- Frame size: `156x210`, matching the claimant portrait canvas.
- Frame count: `8`.
- Horizontal sheet size: `1248x210`.
- Playback: `6 FPS`, `looping = yes`, `play_on_show = yes`, no pause.
- Anchor: center; border edges align to the portrait canvas.
- Static sprite: `GFX_019_infantry_spawn_critical_command_border`.
- Animated sprite: `GFX_019_infantry_spawn_critical_command_border_animated`.
- Source mode: eight separate `$imagegen` outputs on a flat chroma-key background, each depicting a different fully painted warning-border state.
- Subject class: symbolic UI-only portrait-frame overlay.
- Visual direction: an austere steel command frame with rivets, torn black staff cloth, red-brown enamel warning insets, and a wrong-direction cast-shadow motif. Authored changes include different rivet reflections, enamel fissures, cloth folds, corner shadows, and filing clips; no source frame is a transformed or filtered duplicate.
- Static fallback: frame `000`, a tense but low-energy complete border.
- Runtime DDS: `gfx/interface/019_infantry_spawn/critical_command_border_static.dds` and `gfx/interface/019_infantry_spawn/critical_command_border_sheet.dds`.
- Working PNG/GIF/contact paths: this animation folder under `processed_frames/`, `sheets/`, and `previews/`.
- Target GFX file: proposed `interface/019_infantry_spawn.gfx`.
- Target GUI file: proposed `interface/019_infantry_spawn.gui`; implementation owns the critical-risk visibility condition.
- References inspected: offline Graphical Asset Modding, Interface Modding, and Scripted GUI Modding pages; vanilla `interface/alerts.gfx`; Chaos Redux Event 007 `156x210` flame-overlay precedent and Event 010 frame-animated warning sprites.

