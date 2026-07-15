# Event 014 Wendigo Hannibal GFX handoff

The live registrations are in the consolidated `interface/014_cannibalism.gfx` file.

## Static bindings

- `GFX_portrait_ZZZ_hannibal_wendigo` and `GFX_cannibalism_wendigo_portrait_static` use the exact canonical `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` file directly.
- `GFX_cannibalism_wendigo_portrait_static` uses the same static DDS.
- The transformed animated sheet begins with the exact decoded pixels of `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` as frame `000`.

## Animated binding

- Sprite: `GFX_cannibalism_wendigo_portrait_animated`.
- Texture: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`.
- Layout: 16 horizontal 156x210 frames; total 2496x210.
- Playback: 12 fps, looping, play on show, no loop pause.
- Smoothing: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`.

The static fallback remains the exact user-supplied portrait while the animated sprite uses separately generated source states around that canonical frame.
