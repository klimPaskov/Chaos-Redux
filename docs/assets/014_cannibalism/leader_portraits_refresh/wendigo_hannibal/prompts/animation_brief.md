# Wendigo Hannibal canonical portrait animation brief

- Canonical user-supplied portrait: `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.
- The live static fallback is the canonical `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` file itself.
- The decoded canonical PNG binds the black-and-white graphic style, red accents, skull-mask face, branching crown silhouette, crop, and registration.
- Frame `000` is the exact decoded canonical portrait. Frames `001` through `015` are separate built-in image-generation edits of that identity.
- Frame size: 156x210. Sheet size: 2496x210. Frame count: 16.
- Playback: 12 fps, looping, `play_on_show = yes`, `pause_on_loop = 0.0`.
- Smoothing: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`.
- Action: the graphic skull jaw opens beyond human range, a black tongue coils around a red-streaked skull fragment, the mouth bites and crushes it, and the silhouette settles back into the supplied portrait.
- Every frame must contain newly redrawn semantic motion. No shipped frame may be a transform-only, filter-only, recolour-only, warp-only, overlay-only, or optical-flow result.
- Treat the imagery as wholly fictional graphic horror. Add no cultural label, sacred motif, real-world ritual sign, prison imagery, text, watermark, modern object, or extra person.
