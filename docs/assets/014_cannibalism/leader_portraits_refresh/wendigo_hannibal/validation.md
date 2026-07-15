# Event 014 Wendigo Hannibal portrait validation

## Canonical identity

- The exact live static portrait is `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.
- It reports SHA-256 `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`.
- The decoded static master and frame `000` preserve the supplied 156x210 portrait exactly.

## Frame and package checks

- Source frames: 16 present and 16 unique SHA-256 hashes.
- Processed frames: 16 present and 16 unique SHA-256 hashes; every frame is 156x210.
- Sheet: 2496x210 with all 16 frames in exact `000`-`015` order.
- Preview GIF: 16 frames, 1,330 ms total, approximately 12 fps, infinite loop.
- The contact sheets were reviewed at final portrait scale. The supplied black, bone-white, and red graphic identity remains registered while the eyes, jaw, tongue, fragment, bite, chew, and recovery states change.
- There is no prison, cell, bar, cage, restraint, cultural or sacred motif, extra person, text, or watermark.

## Live texture and registration checks

- Static DDS: the exact supplied 156x210 `hannibal_wendigo.dds`, including its original mip chain.
- Sheet DDS: 2496x210, 16 horizontal 156x210 frames, SHA-256 `f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b`.
- `interface/014_cannibalism.gfx` points both static bindings directly to the exact canonical file.
- The animated binding declares 16 frames at 12 fps and uses the vanilla blend-frames effect.

No placeholder, substitute static, reused portrait, or transform-only animation frame is present in this package.
