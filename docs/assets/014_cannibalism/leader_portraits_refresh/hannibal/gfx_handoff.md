# Event 014 Revealed Hannibal GFX Handoff

No `.gfx` edit is required. The existing registrations in `interface/014_cannibalism.gfx` were inspected and deliberately preserved.

## Static bindings

- `GFX_portrait_CBL_hannibal` uses `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds`.
- `GFX_cannibalism_revealed_portrait_static` uses the same static DDS.

## Animated binding

- Sprite: `GFX_cannibalism_revealed_portrait_animated`.
- Texture: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`.
- Frames: 12.
- Rate: 6 fps.
- Playback: looping, play on show, no loop pause.
- Sheet layout: horizontal, left-to-right, 12 frames of 156x210, total 1872x210.

The static and sheet DDS files were replaced at their exact live paths. No interface source, gameplay source, localisation, or unrelated Hannibal texture was edited.

