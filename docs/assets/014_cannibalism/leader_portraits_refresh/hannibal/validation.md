# Event 014 Hannibal Lecter portrait validation

## Canonical identity

- The exact live static portrait is `gfx/leaders/014_cannibalism/hannibal.dds`.
- It reports SHA-256 `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88`.
- The decoded static master and frame `000` preserve the supplied 156x210 portrait exactly.

## Frame and package checks

- Source frames: 12 present and 12 unique SHA-256 hashes.
- Processed frames: 12 present and 12 unique SHA-256 hashes; every frame is 156x210.
- Sheet: 1872x210 with all 12 frames in exact `000`-`011` order.
- Preview GIF: 12 frames, 1,000 ms total, 12 fps stream rate, infinite loop.
- The contact sheets were reviewed at final portrait scale. Hannibal's face, formal clothing, red backdrop, and black branching silhouette remain registered while the fork, tongue, bite, chew, and recovery states change.
- There is no prison, cell, bar, cage, restraint, extra person, text, or watermark.

## Live texture and registration checks

- Static DDS: the exact supplied 156x210 `hannibal.dds`, including its original mip chain.
- Sheet DDS: 1872x210, 12 horizontal 156x210 frames, SHA-256 `f67a1b33a1d4f9b9b1b5ec0d6fb716ad1f2342083e9992550b5dd7356f590587`.
- `interface/014_cannibalism.gfx` points both static bindings directly to the exact canonical file.
- The animated binding declares 12 frames at 12 fps and uses the vanilla blend-frames effect.

No placeholder, substitute static, reused portrait, or transform-only animation frame is present in this package.
