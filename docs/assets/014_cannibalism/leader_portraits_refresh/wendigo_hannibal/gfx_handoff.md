# Event 014 Wendigo Hannibal GFX handoff

No interface edit is required. `interface/014_cannibalism.gfx` already contains the exact static and animated registrations at lines 547-549:

```txt
spriteType = { name = "GFX_portrait_ZZZ_hannibal_wendigo" texturefile = "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds" }
spriteType = { name = "GFX_cannibalism_wendigo_portrait_static" texturefile = "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds" }
frameAnimatedSpriteType = { name = "GFX_cannibalism_wendigo_portrait_animated" texturefile = "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds" noOfFrames = 16 animation_rate_fps = 6 looping = yes play_on_show = yes pause_on_loop = 0.0 }
```

## Texture contract

- Static: 156x210, opaque 32-bit BGRA DDS.
- Sheet: 2496x210, opaque 32-bit BGRA DDS.
- Layout: one horizontal row, frame 000 at x=0 through frame 015 at x=2340.
- Frame width: 156.
- Frame height: 210.
- Frame count: 16.
- Playback: 6 fps, looping, play on show.
- Static and animated texture paths preserve the existing filenames.

The archival `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` is not part of this sprite contract and remains untouched.
