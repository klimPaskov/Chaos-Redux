# Generation provenance

All twelve frames use built-in `image_gen` source art. Cells are mapped row-major.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`003` | `source_frames/013_meteor_rain_overlay_atlas_a_source.png` | `exec-179149d9-91bb-4a0b-aa16-67e3e61989b7.png` | r1c1-r2c2 |
| `004`-`007` | `source_frames/013_meteor_rain_overlay_atlas_b_source.png` | `exec-2e3f1215-7a30-4019-9212-0566baafadd3.png` | r1c1-r2c2 |
| `008`-`011` | `source_frames/013_meteor_rain_overlay_atlas_c_source.png` | `exec-487833dd-33f2-4931-83b4-d5ecb380ff74.png` | r1c1-r2c2 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for meteor fall
Primary request: create frames 1 through 4 of a twelve-frame meteor-shower loop in one exact 2-column by 2-row atlas, row-major order, showing separate rocky fragments descending toward the same low crater belt
Scene/backdrop: every panel uses the same perfectly flat solid #00ff00 chroma-key background
Subject: a fixed narrow silhouette of dark cratered earth along the bottom fifth; three distinct rough meteor fragments with ember-orange heads, hand-painted smoky tails, and tiny sparks appear higher then lower in each successive frame; no stars or sky fill
Style/medium: period 1930s scientific apocalypse illustration blended with HOI4 painted interface art, rough gouache, distressed edges, restrained charcoal and ember palette
Composition/framing: exact 2x2 equal grid with no gutters, borders, labels, or separators; one 1.52:1 overlay per cell, same camera, horizon, scale, and bottom-center anchor; broad green unused canvas around subjects
Frame sequence, row-major:
1 three small distant fragments near the upper edge, crater belt quiet;
2 fragments lower, tails longer and separately redrawn, one tiny ground ember;
3 one leading fragment reaches mid-height while two trail behind, faint dust wakes on ground;
4 leading fragment approaches the horizon, two others fan apart, first small hand-painted ground flash begins
Constraints: every panel is a genuinely distinct drawing of fragment positions, tail shapes, sparks, and ground response, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; same ground identity, camera, palette, scale, and anchor in all cells; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no modern city; no aircraft; no weapons; no white matte; do not use #00ff00 in subjects
Avoid: photorealism, filled sky, checkerboard, primitive line animation, identical copied meteors, giant planet, world-ending explosion, panel captions, perspective drift
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for meteor fall
Primary request: create frames 5 through 8 of a twelve-frame meteor-shower loop in one exact 2-column by 2-row atlas, row-major order, continuing the same crater belt through separate impacts and rebound flashes
Scene/backdrop: every panel uses the same perfectly flat solid #00ff00 chroma-key background
Subject: the same fixed narrow silhouette of dark cratered earth along the bottom fifth; three distinct rough meteor fragments with ember-orange heads, independently hand-painted smoky tails, ground flashes, dirt splinters, and dust bursts redrawn per frame
Style/medium: period 1930s scientific apocalypse illustration blended with HOI4 painted interface art, rough gouache, distressed edges, restrained charcoal and ember palette
Composition/framing: exact 2x2 equal grid with no gutters, borders, labels, or separators; one 1.52:1 overlay per cell, same camera, horizon, scale, and bottom-center anchor
Frame sequence, row-major:
5 first fragment strikes left of center with a small sharp flash while two fragments remain airborne;
6 second fragment strikes right of center, first flash becomes a low dust crown, third fragment descends;
7 third fragment strikes near center with the brightest compact ground flash and separate dirt splinters;
8 all fragments gone, three small uneven ground flashes and drifting dust marks remain
Constraints: every panel is a genuinely distinct drawing of fragment positions, tail shapes, sparks, flashes, dirt, and dust, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; same ground identity, camera, palette, scale, and anchor and compatible with the earlier atlas; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no modern city; no aircraft; no weapons; no white matte; do not use #00ff00 in subjects
Avoid: photorealism, filled sky, checkerboard, primitive line animation, identical copied meteors, giant planet, world-ending explosion, panel captions, perspective drift
```

## Exact atlas C prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for meteor fall
Primary request: create frames 9 through 12 of a twelve-frame meteor-shower loop in one exact 2-column by 2-row atlas, row-major order, returning the same crater belt from settling impacts to a new distant shower
Scene/backdrop: every panel uses the same perfectly flat solid #00ff00 chroma-key background
Subject: the same fixed narrow silhouette of dark cratered earth along the bottom fifth; cooling ground flashes, settling dirt, fading hand-painted smoke, then three new small distant rocky fragments with ember-orange heads and distinct tails
Style/medium: period 1930s scientific apocalypse illustration blended with HOI4 painted interface art, rough gouache, distressed edges, restrained charcoal and ember palette
Composition/framing: exact 2x2 equal grid with no gutters, borders, labels, or separators; one 1.52:1 overlay per cell, same camera, horizon, scale, and bottom-center anchor
Frame sequence, row-major:
9 three low dust crowns with tiny fading embers, no airborne fragments;
10 dust thins into separate hand-painted wisps and ground embers cool;
11 crater belt nearly quiet with one ember and three tiny distant fragment specks entering high above;
12 three small distant fragments with short fresh tails, visually close to frame 1 for a clean shower loop
Constraints: every panel is a genuinely distinct drawing of dust, embers, fragment positions, and tail shapes, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; same ground identity, camera, palette, scale, and anchor and compatible with earlier atlases; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no modern city; no aircraft; no weapons; no white matte; do not use #00ff00 in subjects
Avoid: photorealism, filled sky, checkerboard, primitive line animation, identical copied meteors, giant planet, world-ending explosion, panel captions, perspective drift
```
