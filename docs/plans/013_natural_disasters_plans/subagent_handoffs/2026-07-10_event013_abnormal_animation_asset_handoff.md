# Event 013 abnormal animation asset handoff

> Parent integration closure, 2026-07-10: all eight delivered frame-sheet/static pairs are registered and used by the live abnormal GUI. State-driven visibility, Motion/Static interaction, path cards, warning/impact rims, and chronological movement layers are wired. The meteor shower is intentionally a looping active-state layer; no separate one-shot alias is required.

Date: 2026-07-10

Scope: Event 013 animation assets and animation documentation only. No gameplay, localisation, `.gfx`, `.gui`, achievement, super-event, or spreadsheet file was edited. No commit was created.

## Outcome

All eight animation families requested from the accepted Part 9 abnormal-GUI direction were produced with genuine generated state artwork. The delivered sequences total 86 distinct source frames and 86 distinct processed frames. Local processing only split generated animation atlases, removed chroma, resized to the approved canvas, assembled horizontal sheets, made review GIFs/contact sheets, selected static fallbacks, and wrote uncompressed 32-bit DDS files.

| Package | Frames | Frame size | Sheet size | FPS | Static / animated sprite |
| --- | ---: | --- | --- | ---: | --- |
| `013_disaster_card_frame_warning` | 8 | `540x88` | `4320x88` | 10 | `GFX_013_disaster_card_frame_warning_static` / `GFX_013_disaster_card_frame_warning_animated` |
| `013_disaster_card_frame_impact` | 10 | `540x88` | `5400x88` | 11 | `GFX_013_disaster_card_frame_impact_static` / `GFX_013_disaster_card_frame_impact_animated` |
| `013_impact_pulse_overlay` | 8 | `64x64` | `512x64` | 8 | `GFX_013_map_marker_next_hit_static` / `GFX_013_map_marker_next_hit_animated` |
| `013_rupture_wave_overlay` | 12 | `560x130` | `6720x130` | 8 | `GFX_013_rupture_wave_static` / `GFX_013_rupture_wave_sheet` |
| `013_meteor_rain_overlay` | 12 | `320x210` | `3840x210` | 10 | `GFX_013_meteor_fall_static` / `GFX_013_meteor_fall_sheet` |
| `013_ash_plume_overlay` | 12 | `300x190` | `3600x190` | 8 | `GFX_013_eruption_plume_static` / `GFX_013_eruption_plume_sheet` |
| `013_tsunami_path_ribbon` | 10 | `520x24` | `5200x24` | 8 | `GFX_013_tsunami_train_static` / `GFX_013_tsunami_train_sheet` |
| `013_storm_corridor_path_ribbon` | 14 | `520x24` | `7280x24` | 10 | `GFX_013_storm_corridor_static` / `GFX_013_storm_corridor_sheet` |

The card-frame size was resolved to `540x88`, matching the accepted second-pass motion-lane/card frame direction. Every animation loops and uses `play_on_show = yes`; the card and general overlays use center anchors, meteor and plume use bottom-center anchors, and path ribbons preserve fixed route/coast reference points.

## Package contents

Each new folder under `docs/assets/013_natural_disasters/animations/<package>/` contains:

- `brief.md`
- `frame_plan.md`
- generated source atlas PNGs and separate `*_NNN_source.png` cells
- exact processed `*_NNN.png` frames
- horizontal sheet PNG and DDS
- static fallback PNG and DDS
- review-only GIF and labeled contact sheet
- `notes/generation_provenance.md` with exact retained built-in `image_gen` prompts, output filenames, and per-frame atlas/cell mapping
- `notes/build_metadata.json` with counts, dimensions, timing, selected static frame, hashes, alpha coverage, and paths

Final game-facing DDS pairs were copied to:

```text
gfx/interface/animated/013_natural_disasters/<package>_sheet.dds
gfx/interface/animated/013_natural_disasters/<package>_static.dds
```

Matching package copies exist under each package's `sheets/` directory and `docs/assets/013_natural_disasters/dds/`.

## Existing auxiliary 36x36 packages repaired

The following earlier packages were retained as auxiliary markers rather than misclassified as accepted large overlays:

- `natural_disaster_warning_pulse`
- `natural_disaster_storm_corridor_track`
- `natural_disaster_tsunami_countdown`
- `natural_disaster_eruption_ashfall`
- `natural_disaster_skyfall_alarm`

Their briefs now use the actual static PNG paths, name static and animated sprites, identify the optional `.gui` element, record center anchors and loops, and correct the preview rate from the prior unsupported `9 fps` claim to the measured 120 ms frame duration, about `8.33 fps`. Their frame plans map each source-sheet cell to its visible state. New `notes/provenance.md` files record the retained generated source sheet, SHA-256, frame paths, and known slicing/normalization history.

The exact original prompts and built-in generation result ids for these five historical source sheets are not present in the repository. No reconstructed prompt is represented as historical fact. This is the remaining provenance limit for those earlier packages.

## Documentation changed

- `docs/assets/013_natural_disasters/manifest.md`
  - replaced the blanket `Complete` heading with per-asset status
  - added the eight accepted animation entries as `handed_off`, not `wired`
  - corrected the five auxiliary entries and removed the nonexistent old handoff reference
- `docs/assets/013_natural_disasters/gfx_handoff.md`
  - removed the unsupported claim that Event 013 sprites are already wired
  - added accepted sprite pairs, states, frame counts, FPS, loop/play-on-show behavior, anchors, target `.gfx`/`.gui`, static fallback behavior, and ready-to-copy `frameAnimatedSpriteType` definitions
  - added optional auxiliary marker names and timing
- the eight new package briefs, frame plans, provenance notes, and build metadata
- the five repaired auxiliary briefs, frame plans, and provenance notes

## Meaningful validation

- All 86 processed frames have unique SHA-256 values; no package contains a duplicate processed frame.
- Every processed frame is RGBA at its exact target size, every sheet width equals frame width multiplied by frame count, and every static fallback matches one frame canvas.
- Every GIF contains the expected frame count and encodes timing within 10 ms of its documented FPS.
- No processed frame contains a visible near-pure chroma-green pixel above alpha 16.
- All 16 new sheet/static DDS files use 32-bit RGBA masks with `0xFF000000` alpha, exact dimensions, and byte-identical package, package-root, and live copies.
- The eight contact sheets were visually reviewed for state progression, transparency, anchor stability, and subject continuity. The warning and impact borders grow/decay through drawn rim states; the next-hit marker pressure rises and falls; the rupture rings expand and break; meteor fragments fall and impact; the ash plume grows and drifts; the tsunami train reaches the fixed coast; and the storm core advances along fixed route studs.

## Parent wiring required

The main implementation agent still needs to:

1. Create or update `interface/013_natural_disasters.gfx` with the ready-to-copy definitions in `gfx_handoff.md`.
2. Create or update `interface/013_natural_disasters.gui` and use the proposed element names or update the handoff consistently if implementation names differ.
3. Gate animated and static elements with the actual abnormal card/layer states from Part 9.
4. Decide whether the meteor asset also needs a separate one-shot sprite alias with `looping = no`; the accepted delivered sprite is the looping meteor-shower state.
5. Keep GIFs review-only and point all in-game textures to DDS sheets.

## Simplifications, omissions, and blockers

- No requested one of the eight families was omitted or replaced with a transform/filter-only animation.
- No CLI image-generation fallback was used; all generated source art came from built-in `image_gen` and was copied into the repository.
- The skill-listed decision reference-art directory is absent from this checkout. Existing Event 013 animation contacts plus vanilla alert/map-icon examples were used as the closest available references.
- The audit also lists an additional `013_tornado_track_ribbon` beyond the eight families assigned in this task. It remains outside this handoff and must not be silently treated as covered by the storm-corridor ribbon.
- Exact original prompt/result provenance for the five earlier `36x36` source sheets remains unavailable, as documented above.
- Static abnormal-GUI panels, card bases, badges, and progress assets are outside this animation-only assignment and remain separate asset work.
