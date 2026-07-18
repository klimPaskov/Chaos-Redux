# Critical Command Border Animation Brief

- Asset: `critical_command_border`.
- In-game use: frames the claimant army/muster identity scene while revolt risk is in the critical band.
- Surface: Muster Board Command tab fixed portrait-slot overlay; decorative and state-driven.
- Frame size: `156x210`, matching the claimant identity-scene canvas.
- Frame count: `8`.
- Horizontal sheet size: `1248x210`.
- Playback: `6 FPS`, `looping = yes`, `play_on_show = yes`, no pause.
- Anchor: center; border edges align to the identity-scene canvas.
- Static sprite: `GFX_infantry_spawn_critical_command_border_static`.
- Animated sprite: `GFX_infantry_spawn_critical_command_border_animated`.
- Source mode: one explicit built-in ImageGen animation-source atlas on a flat `#00ff00` chroma-key background. Its `4x2` row-major cells are retained as all eight source frames; the atlas is not a review contact sheet.
- Subject class: symbolic UI-only fixed-slot frame overlay.
- Visual direction: an austere steel command frame with rivets, torn black staff cloth, red-brown enamel warning insets, and a wrong-direction cast-shadow motif. Authored changes include different rivet reflections, enamel fissures, cloth folds, corner shadows, and filing clips; no source frame is a transformed or filtered duplicate.
- Static fallback: frame `000`, a tense but low-energy complete border.
- Runtime DDS: `gfx/interface/019_infantry_spawn/critical_command_border_static.dds` and `gfx/interface/019_infantry_spawn/critical_command_border_sheet.dds`.
- Working PNG/GIF/contact paths: this animation folder under `processed_frames/`, `sheets/`, and `previews/`.
- Target GFX file: `interface/019_infantry_spawn.gfx`.
- Target GUI file: `interface/019_infantry_spawn_muster_board.gui`; implementation owns the critical-risk visibility condition.
- References inspected: offline Graphical Asset Modding, Interface Modding, and Scripted GUI Modding pages; vanilla `interface/alerts.gfx`; Chaos Redux Event 007 `156x210` flame-overlay precedent and Event 010 frame-animated warning sprites.

## Source provenance

- Identity reference supplied to built-in ImageGen: the prior `source_frames/critical_command_border_000_source.png`, used only to lock the narrow rails, four corner plates, rivet positions, enamel channels, black perimeter cloth, open identity-scene aperture, orthographic camera, and scale.
- Generated source atlas: `source_atlas/critical_command_border_animation_source_atlas.png`, `1470x1070`, SHA-256 `4bbf16da40a7dddae4e16c8b9059609a8e415b6726b25946626c7f3d68d45246`.
- Built-in generation record: `C:/Users/klimp/.codex/generated_images/019f670e-9795-74b2-b8d4-8c8262ee6ced/exec-9a63c43d-4b1a-40c0-bbaf-d8335cba7499.png`; the project copy above is the frozen source of truth.
- Prompt contract: an exact `4x2` animation atlas of the same fixed-slot border, with the rail geometry, corner plates, rivet arrangement, enamel channels, cloth perimeter, open center, palette, camera, framing, and anchor invariant; only the frame-plan fissures, incisions, rivet stress, clips, cloth folds, and wrong-direction border shadow may change. No text, identity-scene contents, rotation, translation, scale change, filter-only motion, duplicate cells, or green inside the frame artwork.
- Mechanical processing: row-major atlas slicing, official chroma removal, isolated atlas-edge component cleanup, one shared sequence scale, center anchoring, exact-size export, sheet/GIF/contact assembly, and BGRA DDS conversion. These steps do not create the animation's internal motion.

## Continuity validation

- Original-detail atlas and processed contact inspection confirms one continuous border identity in all eight cells: all four rails, four corner plates, rivet arrangement, red enamel channels, black cloth perimeter, aperture, palette, and camera remain fixed.
- Authored internal changes remain visible after `156x210` reduction: the top-rail fracture, engraved warning incisions, rivet stress, filing clip, cloth folds, and asymmetric shadow advance and settle without replacing the frame.
- Processed anchor-center deviation is at most `0.438 px`; minimum nonzero-alpha silhouette intersection-over-union against frame `000` is `0.9441`.
- The central aperture region from `x=30..125`, `y=30..179` is fully transparent in every processed frame (`alpha max = 0`). All eight source hashes and all eight processed hashes are unique, with zero surviving chroma-green pixels; frame `000` is byte-for-byte the static PNG and the first sheet frame.
