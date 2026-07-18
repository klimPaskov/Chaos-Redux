# Muster Seal Pulse Animation Brief

- Asset: `muster_seal_pulse`
- In-game use: signals unresolved formation lots on the Event 19 decision category or Muster Board Overview tab.
- Surface: scripted GUI / decision-category decoration; decorative state communication, not a button hitbox.
- Frame size: `64x64`.
- Frame count: `8`.
- Horizontal sheet size: `512x64`.
- Playback: `8 FPS`, `looping = yes`, `play_on_show = yes`, no pause.
- Anchor: center.
- Static sprite: `GFX_infantry_spawn_muster_seal_static`.
- Animated sprite: `GFX_infantry_spawn_muster_seal_animated`.
- Source mode: one explicit built-in ImageGen animation-source atlas on a flat `#00ff00` chroma-key background. Its `4x2` row-major cells are retained as all eight source frames; the atlas is not a review contact sheet.
- Subject class: symbolic UI-only military registry art.
- Visual direction: a dented 1930s military muster seal whose wax, stamped ranks, paper fibers, and inset metal respond in distinct drawn states as unresolved lots accumulate. The motion comes from changed cracks, impressions, raised paper, tiny filing tabs, and light-bearing grooves, not from translating, scaling, rotating, recoloring, or filtering one still.
- Static fallback: frame `000`, the lowest-energy but fully readable seal state.
- Runtime DDS: `gfx/interface/019_infantry_spawn/muster_seal_pulse_static.dds` and `gfx/interface/019_infantry_spawn/muster_seal_pulse_sheet.dds`.
- Working PNG/GIF/contact paths: this animation folder under `processed_frames/`, `sheets/`, and `previews/`.
- Target GFX file: `interface/019_infantry_spawn.gfx`.
- Target GUI file: `interface/019_infantry_spawn_muster_board.gui`; implementation owns exact placement and visibility trigger.
- References inspected: offline Graphical Asset Modding, Interface Modding, and Scripted GUI Modding pages; vanilla `interface/alerts.gfx`; Chaos Redux `interface/007_fury.gfx`, `interface/010_death.gfx`, and the Event 018 eight-frame generated animation package.

## Source provenance

- Identity reference supplied to built-in ImageGen: the prior `source_frames/muster_seal_pulse_000_source.png`, used only to lock the four-point brass mount, four rivets, torn paper silhouette, burgundy wax disk, camera, materials, and scale.
- Generated source atlas: `source_atlas/muster_seal_pulse_animation_source_atlas.png`, `1774x887`, SHA-256 `58456dfdbf1bf3e7a877bee6e178547f3bda5dffb3f7e856a188c5b165bccad1`.
- Built-in generation record: `C:/Users/klimp/.codex/generated_images/019f670e-9795-74b2-b8d4-8c8262ee6ced/exec-ef5cd7e6-9bf5-443c-9f09-9af093799240.png`; the project copy above is the frozen source of truth.
- Prompt contract: an exact `4x2` animation atlas of the same seal, with the outer mount, rivets, paper silhouette, palette, orthographic camera, framing, and anchor invariant; only the frame-plan wax fissures, rank relief, ledger groove, paper fibers, and filing tabs may change. No text, rotation, translation, scale change, filter-only motion, duplicate cells, or green inside the subject.
- Mechanical processing: row-major atlas slicing, official chroma removal, isolated atlas-edge component cleanup, one shared sequence scale, center anchoring, exact-size export, sheet/GIF/contact assembly, and BGRA DDS conversion. These steps do not create the animation's internal motion.

## Continuity validation

- Original-detail atlas and processed contact inspection confirms one continuous seal identity in all eight cells: the same mount points, rivet placement, wax ring, central stamp family, paper backing, palette, and camera remain fixed.
- Authored internal changes remain visible after `64x64` reduction: rank relief builds through frame `004`, cracks and paper tension advance, then relief and grooves physically settle through frame `007`.
- Processed anchor-center deviation is at most `0.455 px`; minimum nonzero-alpha silhouette intersection-over-union against frame `000` is `0.8838`, including the intentionally lifted paper fibers and filing tab.
- All eight source hashes and all eight processed hashes are unique. Processed frames have real alpha with zero surviving chroma-green pixels; frame `000` is byte-for-byte the static PNG and the first sheet frame.
