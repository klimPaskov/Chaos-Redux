# Event 014 Hannibal Lecter GFX handoff

The live registrations are in the consolidated `interface/014_cannibalism.gfx` file.

## Static bindings

- `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static` use the exact canonical `gfx/leaders/014_cannibalism/hannibal.dds` file directly.
- `GFX_cannibalism_revealed_portrait_static` uses the same static DDS.
- The ordinary animated sheet begins with the exact decoded pixels of `gfx/leaders/014_cannibalism/hannibal.dds` as frame `000`.

## Animated binding

- Sprite: `GFX_cannibalism_revealed_portrait_animated`.
- Texture: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`.
- Layout: 12 horizontal 156x210 frames; total 1872x210.
- Playback: 12 fps, looping, play on show, no loop pause.
- Smoothing: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`.

The static fallback remains the exact user-supplied portrait while the animated sprite uses separately generated source states around that canonical frame.
