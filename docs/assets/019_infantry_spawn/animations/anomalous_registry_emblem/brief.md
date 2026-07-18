# Anomalous Registry Emblem Animation Brief

- Asset: `anomalous_registry_emblem`.
- In-game use: indicates an active registered anomalous family or rising Anomalous Saturation.
- Surface: Muster Board Anomalous Registry tab emblem; decorative and state-driven.
- Frame size: `64x64`.
- Frame count: `10`.
- Horizontal sheet size: `640x64`.
- Playback: `5 FPS`, `looping = yes`, `play_on_show = yes`, no pause.
- Anchor: center.
- Static sprite: `GFX_infantry_spawn_anomalous_registry_emblem_static`.
- Animated sprite: `GFX_infantry_spawn_anomalous_registry_emblem_animated`.
- Source mode: one explicit built-in ImageGen animation-source atlas on a flat `#00ff00` chroma-key background. Its `5x2` row-major cells are retained as all ten source frames; the atlas is not a review contact sheet.
- Subject class: symbolic, family-neutral UI art.
- Visual direction: a compact military registry emblem combining a filed brass plate, an empty translucent band, a rough bound-stone segment, and an ordinary stamped rank. Across the loop, authored atlas states alter the physical plate seams, etched non-text marks, translucent folds, stone binding, and interior aperture. It does not simply rotate, pulse, recolor, or translate.
- Static fallback: frame `000`, sealed and lowest-energy.
- Runtime DDS: `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_static.dds` and `gfx/interface/019_infantry_spawn/anomalous_registry_emblem_sheet.dds`.
- Working PNG/GIF/contact paths: this animation folder under `processed_frames/`, `sheets/`, and `previews/`.
- Target GFX file: `interface/019_infantry_spawn.gfx`.
- Target GUI file: `interface/019_infantry_spawn_muster_board.gui`; implementation owns active-family/saturation visibility.
- References inspected: offline Graphical Asset Modding, Interface Modding, and Scripted GUI Modding pages; vanilla `interface/alerts.gfx`; Chaos Redux Event 010 warning/emblem animations and Event 018 generated animation package.

## Source provenance

- Identity reference supplied to built-in ImageGen: the prior `source_frames/anomalous_registry_emblem_000_source.png`, used only to lock the clipped-corner brass plate, top and bottom clasps, side clamps, rivet arrangement, paired stone doors, central seam, ivory band, chevron lock, aperture construction, orthographic camera, and scale.
- Generated source atlas: `source_atlas/anomalous_registry_emblem_animation_source_atlas.png`, `1983x793`, SHA-256 `f634899a432dd8317412de13f8ae31cbf2e47c5d97f2c8e563ced6e1a8f4cd85`.
- Built-in generation record: `C:/Users/klimp/.codex/generated_images/019f670e-9795-74b2-b8d4-8c8262ee6ced/exec-79f5764a-8a4c-4135-9540-7a7fe33d7cbf.png`; the project copy above is the frozen source of truth.
- Prompt contract: an exact `5x2` animation atlas of the same registry plate, with the outer brass geometry, clasps, clamps, rivets, stone doors, ivory band, central lock, palette, camera, framing, and anchor invariant; only the frame-plan aperture depth, plate seams, etched paths, translucent folds, binding tension, filing notches, and containment clamps may change. No text, unrelated emblems, rotation, translation, scale change, filter-only motion, duplicate cells, or green inside the subject.
- Mechanical processing: row-major atlas slicing, official chroma removal, isolated atlas-edge component cleanup, one shared sequence scale, center anchoring, exact-size export, sheet/GIF/contact assembly, and BGRA DDS conversion. These steps do not create the animation's internal motion.

## Continuity validation

- Original-detail atlas and processed contact inspection confirms one continuous emblem identity in all ten cells: the clipped brass perimeter, clasps, side clamps, rivets, paired stone doors, central seam, ivory band, central chevron lock, palette, and camera remain fixed.
- Authored internal changes remain visible after `64x64` reduction: the aperture and etched network deepen through frame `005`, containment clamps and seams physically reconfigure, and the plate settles through frame `009`.
- Processed anchor-center deviation is at most `0.495 px`; minimum nonzero-alpha silhouette intersection-over-union against frame `000` is `0.9278`, including the planned containment hardware changes.
- All ten source hashes and all ten processed hashes are unique. Processed frames have real alpha with zero surviving chroma-green pixels; frame `000` is byte-for-byte the static PNG and the first sheet frame.
