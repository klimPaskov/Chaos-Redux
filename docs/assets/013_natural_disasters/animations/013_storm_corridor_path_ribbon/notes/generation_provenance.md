# Generation provenance

All fourteen frames use built-in `image_gen` source art. Each atlas row is a separate drawn state.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`006` | `source_frames/013_storm_corridor_path_ribbon_atlas_a_source.png` | `exec-9e7c7f4a-278b-41f5-bd09-0814360ee3e7.png` | rows 1-7 |
| `007`-`013` | `source_frames/013_storm_corridor_path_ribbon_atlas_b_source.png` | `exec-2d4a70c8-0918-419d-a965-db58cbd7343a.png` | rows 1-7 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent path-ribbon animation source atlas for a moving storm corridor
Primary request: create frames 1 through 7 of a fourteen-frame storm-corridor loop in one exact single-column by 7-row atlas, showing the same hand-painted storm core advancing from left toward the middle along a fixed damaged route
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: one very long thin corridor ribbon per row: a fixed broken ochre route line with small iron marker studs and faint dark terrain scuffs; a compact charcoal-blue storm core, white-grey gust arcs, tiny amber lightning forks, rain hatching, and scattered debris are genuinely redrawn in each frame
Style/medium: 1930s military weather-map brush illustration blended with HOI4 painted interface art, distressed ink and gouache, readable at 520x24
Composition/framing: exactly seven equal horizontal rows with no gutters, labels, borders, or separators; each row contains one ultra-wide 21.7:1 ribbon centered at the same scale and vertical center anchor, spanning about 94% of image width and remaining slender
Frame sequence:
1 small storm core at route origin near far left, quiet route ahead;
2 core advances to first marker, new gust arc and one lightning fork;
3 core moves between first and second markers, rain hatching lengthens;
4 core reaches second marker, debris marks and path flicker appear behind;
5 core advances into left-center, darker hand-painted cloud mass and two gust arcs;
6 core approaches center, lightning redrawn below the leading edge;
7 core reaches center, strongest mid-route pressure with broken ochre path flicker
Constraints: every row is a genuinely distinct drawing of storm contour, gust arcs, lightning, rain, debris, and path flicker, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; route line and marker positions stay fixed; same camera, palette, scale, and center anchor; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no tornado funnel; no buildings; no people; no modern radar UI; no white matte; do not use #00ff00 in subjects
Avoid: primitive moving dot, clean vector geometry, identical copied cloud, filled landscape, photorealism, checkerboard, panel captions, thick tall storm, perspective drift
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI transparent path-ribbon animation source atlas for a moving storm corridor
Primary request: create frames 8 through 14 of a fourteen-frame storm-corridor loop in one exact single-column by 7-row atlas, continuing the same hand-painted storm core from center toward the route exit and returning a new core to origin
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background
Subject: one very long thin corridor ribbon per row: the same fixed broken ochre route line with small iron marker studs and faint dark terrain scuffs; a compact charcoal-blue storm core, white-grey gust arcs, tiny amber lightning forks, rain hatching, and scattered debris are genuinely redrawn in each frame
Style/medium: 1930s military weather-map brush illustration blended with HOI4 painted interface art, distressed ink and gouache, readable at 520x24
Composition/framing: exactly seven equal horizontal rows with no gutters, labels, borders, or separators; each row contains one ultra-wide 21.7:1 ribbon centered at the same scale and vertical center anchor, spanning about 94% of image width and remaining slender
Frame sequence:
8 core leaves center toward center-right, fresh gust arcs and fading debris behind;
9 core crosses third marker, one lightning fork and denser rain hatching;
10 core moves through right-center, path flicker follows behind;
11 core nears final marker, cloud contour stretches downwind and debris thins;
12 core reaches final marker near far right, compact strong gust and small lightning;
13 core exits beyond right edge, only trailing rain and path flicker remain, while a tiny new dark cloud gathers at far left;
14 new small storm core rests at route origin near far left, visually close to frame 1 for a clean loop
Constraints: every row is a genuinely distinct drawing of storm contour, gust arcs, lightning, rain, debris, and path flicker, not a translated, scaled, rotated, warped, recolored, blurred, opacity-changed, particle-scripted, or filtered copy; route line and marker positions stay fixed; same camera, palette, scale, and center anchor and compatible with the earlier atlas; flat uniform #00ff00 background only; no readable text; no numbers; no watermark; no tornado funnel; no buildings; no people; no modern radar UI; no white matte; do not use #00ff00 in subjects
Avoid: primitive moving dot, clean vector geometry, identical copied cloud, filled landscape, photorealism, checkerboard, panel captions, thick tall storm, perspective drift
```
