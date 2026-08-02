# Large division-counter GFX handoff

No `.gfx` file was edited in this subtask.

The final DDS files remain at the existing exact runtime paths under `gfx/interface/counters/divisions_large/`. Existing sprite names and the required two-frame `noOfFrames = 2` definitions in `interface/chaosx_subuniticons.gfx` remain the parent-owned wiring contract.

For every requested file, the parent should retain the existing large-counter sprite pattern:

```text
spriteType = { name = "GFX_<basename>_medium"
    textureFile = "gfx/interface/counters/divisions_large/<basename>.dds" noOfFrames = 2 }
```

The active frame is the left 76x42 slot with restrained orange accents. The neutral frame is the right 76x42 slot in monochrome ivory/charcoal. Small/on-map white textures were intentionally not changed.
