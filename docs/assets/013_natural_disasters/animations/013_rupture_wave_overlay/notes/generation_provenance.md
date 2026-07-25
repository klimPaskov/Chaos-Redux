# Generation provenance

All twelve frames use built-in `image_gen` source art. Each atlas row is a separate drawn state; local processing only split, keyed, resized, and assembled the frames.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`003` | `source_frames/013_rupture_wave_overlay_atlas_a_source.png` | `exec-206131a1-f489-41c7-9ca2-8c2a99c846c6.png` | rows 1-4 |
| `004`-`007` | `source_frames/013_rupture_wave_overlay_atlas_b_source.png` | `exec-0793b51c-8cad-4f1d-a661-0ed8d1c62ab9.png` | rows 1-4 |
| `008`-`011` | `source_frames/013_rupture_wave_overlay_atlas_c_source.png` | `exec-48125e83-45b7-4fdc-b0cd-1436be43d0f4.png` | rows 1-4 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for a whole-earth rupture wave
Primary request: create frames 1 through 4 of a twelve-frame seismic-wave loop in one exact single-column by 4-row atlas, with genuinely redrawn uneven rupture rings expanding across a long map plate
Scene/backdrop: each row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: a fixed jagged black-and-umber fault scar near the horizontal center; hand-painted irregular concentric seismic arcs in pale dust, dull amber, and deep red spread outward across the width; tiny fractured earth flecks are drawn differently in each frame
Style/medium: 1930s scientific hazard-chart illustration blended with HOI4 painted interface art, distressed ink and chalk texture, ominous but readable
Composition/framing: exactly four equal wide horizontal rows, no gutters, no labels, no separators; each frame is a 4.31:1 overlay centered at identical scale and center anchor, filling about 94% of row width while leaving green unused canvas
Frame sequence:
1 dormant fault scar with one tight broken ring;
2 first uneven ring expands around the scar;
3 second wider broken ring appears and the first ring frays;
4 three asymmetrical rings spread across the middle third with new dust flecks
Constraints: every row must be a genuinely distinct drawing of the planned seismic state, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, glow-filtered, or filtered copy; same fixed fault identity, camera, palette, scale, and center anchor; ring topology and dust marks are intentionally redrawn per frame; flat uniform #00ff00 background only; no map labels; no text; no numbers; no watermark; no modern seismograph UI; no white matte; do not use #00ff00 in the overlay
Avoid: clean perfect circles, primitive geometry-only rings, filled background map, photorealism, checkerboard, panel captions, perspective drift
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for a whole-earth rupture wave
Primary request: create frames 5 through 8 of a twelve-frame seismic-wave loop in one exact single-column by 4-row atlas, continuing the same uneven rupture rings from broad expansion through peak shock and early fragmentation
Scene/backdrop: each row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: the same fixed jagged black-and-umber fault scar near horizontal center; hand-painted irregular concentric seismic arcs in pale dust, dull amber, and deep red spread outward across the width; tiny fractured earth flecks redrawn per frame
Style/medium: 1930s scientific hazard-chart illustration blended with HOI4 painted interface art, distressed ink and chalk texture, ominous but readable
Composition/framing: exactly four equal wide horizontal rows, no gutters, no labels, no separators; each frame is a 4.31:1 overlay centered at identical scale and center anchor, filling about 94% row width
Frame sequence:
5 four broken rings span most of the width, outer arcs touching near both sides;
6 peak wave, dense asymmetrical rings and dust bursts cover the full width without becoming clean circles;
7 shock breakup, outermost ring shatters into separate hand-painted arcs while inner rings fray;
8 early decay, only two broad broken rings remain plus scattered earth flecks
Constraints: every row is a genuinely distinct drawing of the planned seismic state, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, glow-filtered, or filtered copy; same fixed fault identity, camera, palette, scale, and center anchor and compatible with the earlier atlas; ring topology and dust marks redrawn per frame; flat uniform #00ff00 background only; no map labels; no text; no numbers; no watermark; no modern seismograph UI; no white matte; do not use #00ff00 in the overlay
Avoid: clean perfect circles, primitive geometry-only rings, filled background map, photorealism, checkerboard, panel captions, perspective drift
```

## Exact atlas C prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent map-overlay animation source atlas for a whole-earth rupture wave
Primary request: create frames 9 through 12 of a twelve-frame seismic-wave loop in one exact single-column by 4-row atlas, returning the same uneven rupture wave from fragmented outer arcs to a dormant fault
Scene/backdrop: each row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: the same fixed jagged black-and-umber fault scar near horizontal center; fading hand-painted seismic arcs in pale dust, dull amber, and deep red; residual fractured earth flecks redrawn per frame
Style/medium: 1930s scientific hazard-chart illustration blended with HOI4 painted interface art, distressed ink and chalk texture, ominous but readable
Composition/framing: exactly four equal wide horizontal rows, no gutters, no labels, no separators; each frame is a 4.31:1 overlay centered at identical scale and center anchor, filling about 94% row width
Frame sequence:
9 one broad shattered outer ring plus faint inner fragments and settling dust;
10 narrow broken arcs retreat toward the fault and the dust field thins;
11 only one tight irregular ring and a few final flecks remain;
12 dormant reset bridge, fixed fault scar with a faint broken ring, visually close to frame 1 for a clean loop
Constraints: every row is a genuinely distinct drawing of the planned seismic state, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, glow-filtered, or filtered copy; same fixed fault identity, camera, palette, scale, and center anchor and compatible with earlier atlases; ring topology and dust marks redrawn per frame; flat uniform #00ff00 background only; no map labels; no text; no numbers; no watermark; no modern seismograph UI; no white matte; do not use #00ff00 in the overlay
Avoid: clean perfect circles, primitive geometry-only rings, filled background map, photorealism, checkerboard, panel captions, perspective drift
```
