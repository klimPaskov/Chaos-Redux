# Generation provenance

All ten frames use built-in `image_gen` source art. Each atlas row is a separate drawn state.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`004` | `source_frames/013_tsunami_path_ribbon_atlas_a_source.png` | `exec-885988f7-f57a-4fcf-a15c-163ea19e8e5c.png` | rows 1-5 |
| `005`-`009` | `source_frames/013_tsunami_path_ribbon_atlas_b_source.png` | `exec-8bd09566-1117-45b2-b699-3453ac85adf3.png` | rows 1-5 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent path-ribbon animation source atlas for a delayed tsunami train
Primary request: create frames 1 through 5 of a ten-frame tsunami-arrival loop in one exact single-column by 5-row atlas, showing a hand-painted train of separate wave pulses advancing from left toward the same coast marker at far right
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: one very long thin ocean-path ribbon per row, made from dark navy water, dirty teal undertow, pale foam crests, and a fixed small ochre coastline/port tick at the far right; the crest shapes and foam breaks are genuinely redrawn in each frame
Style/medium: 1930s naval-chart brush illustration blended with HOI4 painted interface art, distressed ink and gouache, readable at 520x24
Composition/framing: exactly five equal horizontal rows with no gutters, labels, borders, or separators; each row contains one ultra-wide 21.7:1 ribbon centered at the same scale and vertical center anchor, spanning about 94% of image width and remaining slender, with ample green above and below
Frame sequence:
1 three small offshore wave crests clustered near the left quarter, coast quiet;
2 crest train advances slightly right, foam breaks redrawn and first arrival dot appears;
3 leading crest reaches center-left, following crests stretch behind;
4 leading crest crosses center, undertow darkens and foam is stronger;
5 leading crest enters right half, second crest reaches center and coast tick begins a faint pale splash
Constraints: every row is a genuinely distinct drawing of crest contours, foam, undertow, and arrival marks, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; same coast identity, camera, palette, scale, and center anchor; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no ships; no people; no modern map UI; no white matte; do not use #00ff00 in subjects
Avoid: primitive sine waves, clean vector geometry, identical copied wave shapes, filled ocean background, photorealism, checkerboard, panel captions, thick tall waves, perspective drift
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent path-ribbon animation source atlas for a delayed tsunami train
Primary request: create frames 6 through 10 of a ten-frame tsunami-arrival loop in one exact single-column by 5-row atlas, continuing the same wave train through coast arrival, retreat, and a new offshore reset
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: one very long thin ocean-path ribbon per row, made from dark navy water, dirty teal undertow, pale foam crests, and the same fixed small ochre coastline/port tick at far right; crest shapes, foam breaks, coast splashes, and retreat ripples are genuinely redrawn per frame
Style/medium: 1930s naval-chart brush illustration blended with HOI4 painted interface art, distressed ink and gouache, readable at 520x24
Composition/framing: exactly five equal horizontal rows with no gutters, labels, borders, or separators; each row contains one ultra-wide 21.7:1 ribbon centered at the same scale and vertical center anchor, spanning about 94% of image width and remaining slender
Frame sequence:
6 leading crest reaches the coast with a compact pale splash, two following crests occupy the right half;
7 second crest arrives with a different stronger foam burst while the first becomes a thin retreat line;
8 last crest reaches the coast, offshore surface settles into broken dark ripples;
9 coast splash fades, a long low retreat ripple runs left and three tiny new offshore bumps appear;
10 three new small offshore crests gather near the left quarter, visually close to frame 1 for a clean loop
Constraints: every row is a genuinely distinct drawing of crest contours, foam, undertow, coast splash, and retreat marks, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; same coast identity, camera, palette, scale, and center anchor and compatible with the earlier atlas; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no ships; no people; no modern map UI; no white matte; do not use #00ff00 in subjects
Avoid: primitive sine waves, clean vector geometry, identical copied wave shapes, filled ocean background, photorealism, checkerboard, panel captions, thick tall waves, perspective drift
```
