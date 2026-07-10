# Generation provenance

All twelve frames use built-in `image_gen` source art. Cells are mapped row-major.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`003` | `source_frames/013_ash_plume_overlay_atlas_a_source.png` | `exec-9e680dbb-e077-4755-ab3d-345af2cbbb51.png` | r1c1-r2c2 |
| `004`-`007` | `source_frames/013_ash_plume_overlay_atlas_b_source.png` | `exec-e838a866-77b9-45fe-b5a8-733d3edaddb6.png` | r1c1-r2c2 |
| `008`-`011` | `source_frames/013_ash_plume_overlay_atlas_c_source.png` | `exec-b1421e79-6e15-41e1-8e2d-5e2c7acd41a1.png` | r1c1-r2c2 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for an eruption plume
Primary request: create frames 1 through 4 of a twelve-frame volcanic ash-plume loop in one exact 2-column by 2-row atlas, row-major order, showing the same vent from a low ash cough into a rising column
Scene/backdrop: every panel uses the same perfectly flat solid #00ff00 chroma-key background
Subject: a fixed dark volcanic vent and narrow broken ridge along the bottom sixth; dense hand-painted charcoal and umber ash masses, rust-red cinders, and pale grey ash edges are separately drawn in each frame, drifting slightly downwind to the right
Style/medium: period 1930s field-report illustration blended with HOI4 painted interface art, rough gouache and dry-brush ash texture, ominous and readable
Composition/framing: exact 2x2 equal grid with no gutters, borders, labels, or separators; one 1.58:1 overlay per cell, same camera, fixed vent, scale, and bottom-center anchor; generous green around the plume
Frame sequence, row-major:
1 low vent with a small dark ash cough and two cinders;
2 compact column rises above the vent with a bulbous redrawn crown;
3 column grows taller and begins leaning right, new ash curls and cinders appear;
4 broad mid-height plume with a darker core and first detached downwind ash lobe
Constraints: every panel is a genuinely distinct drawing of plume contour, internal ash masses, cinders, and detached lobes, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, smoke-scripted, or filtered copy; same vent identity, camera, palette, scale, and anchor in all cells; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no buildings; no people; no white matte; do not use #00ff00 in subjects
Avoid: photorealism, soft generic airbrush cloud, checkerboard, primitive particle dots, identical copied plume, mushroom cloud, nuclear imagery, panel captions, perspective drift
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for an eruption plume
Primary request: create frames 5 through 8 of a twelve-frame volcanic ash-plume loop in one exact 2-column by 2-row atlas, row-major order, continuing the same vent through maximum plume growth and downwind spread
Scene/backdrop: every panel uses the same perfectly flat solid #00ff00 chroma-key background
Subject: the same fixed dark volcanic vent and narrow broken ridge along the bottom sixth; dense hand-painted charcoal and umber ash masses, rust-red cinders, pale grey ash edges, and detached downwind lobes are separately drawn in each frame, drifting right
Style/medium: period 1930s field-report illustration blended with HOI4 painted interface art, rough gouache and dry-brush ash texture, ominous and readable
Composition/framing: exact 2x2 equal grid with no gutters, borders, labels, or separators; one 1.58:1 overlay per cell, same camera, fixed vent, scale, and bottom-center anchor
Frame sequence, row-major:
5 high plume with a heavy dark core and two detached lobes downwind;
6 peak eruption, tallest broad column with a turbulent crown, many cinders, and a long ash tongue to the right;
7 peak begins to shear, crown separates into layered hand-painted masses and cinders thin;
8 early fall, lower column narrows while detached ash lobes continue drifting right
Constraints: every panel is a genuinely distinct drawing of plume contour, internal ash masses, cinders, and detached lobes, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, smoke-scripted, or filtered copy; same vent identity, camera, palette, scale, and anchor and compatible with the earlier atlas; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no buildings; no people; no white matte; do not use #00ff00 in subjects
Avoid: photorealism, soft generic airbrush cloud, checkerboard, primitive particle dots, identical copied plume, mushroom cloud, nuclear imagery, panel captions, perspective drift
```

## Exact atlas C prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for an eruption plume
Primary request: create frames 9 through 12 of a twelve-frame volcanic ash-plume loop in one exact 2-column by 2-row atlas, row-major order, returning the same vent from drifting ash to a low reset state
Scene/backdrop: every panel uses the same perfectly flat solid #00ff00 chroma-key background
Subject: the same fixed dark volcanic vent and narrow broken ridge along the bottom sixth; hand-painted charcoal and umber ash masses, rust-red cinders, and pale grey detached lobes shrink and drift right in distinct drawings
Style/medium: period 1930s field-report illustration blended with HOI4 painted interface art, rough gouache and dry-brush ash texture, ominous and readable
Composition/framing: exact 2x2 equal grid with no gutters, borders, labels, or separators; one 1.58:1 overlay per cell, same camera, fixed vent, scale, and bottom-center anchor
Frame sequence, row-major:
9 low narrow column with three detached downwind ash lobes and sparse cinders;
10 column collapses into broken curls, detached ash thins farther right;
11 only a compact ash cough and two small pale wisps remain above the vent;
12 low reset vent with a small dark ash cough and two cinders, visually close to frame 1 for a clean loop
Constraints: every panel is a genuinely distinct drawing of plume contour, internal ash masses, cinders, and detached lobes, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, smoke-scripted, or filtered copy; same vent identity, camera, palette, scale, and anchor and compatible with earlier atlases; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no buildings; no people; no white matte; do not use #00ff00 in subjects
Avoid: photorealism, soft generic airbrush cloud, checkerboard, primitive particle dots, identical copied plume, mushroom cloud, nuclear imagery, panel captions, perspective drift
```
