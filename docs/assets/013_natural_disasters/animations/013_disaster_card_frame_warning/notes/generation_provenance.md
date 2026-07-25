# Generation provenance

Source mode for every frame: built-in `image_gen`. No CLI fallback, internet source, user-provided source, local drawing, or transform-generated motion was used.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`003` | `source_frames/013_disaster_card_frame_warning_atlas_a_source.png` | `exec-bf6bc379-11c0-4025-a4a1-d12c28dd8159.png` | rows 1-4 |
| `004`-`007` | `source_frames/013_disaster_card_frame_warning_atlas_b_source.png` | `exec-ff92026c-2cea-4c46-a9a0-19575e288452.png` | rows 1-4 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI animation source atlas for a warning-state disaster card frame
Primary request: create four genuinely redrawn sequential warning-rim frames in one exact single-column by 4-row atlas, row-major order, for the same long empty hazard card border
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background, including the empty interior of the card frame
Subject: a long 1930s civil-defense dossier frame made from dark gunmetal, aged brass corner brackets, narrow amber enamel warning filaments, and worn paper-edge texture; the border is decorative only and the entire center stays flat green for transparency
Style/medium: HOI4 painted interface art, tactile period metal and paper, restrained amber warning light, no modern screen graphics
Composition/framing: exactly four equal wide horizontal rows with no gutters, no labels, no separators; one identical 6.14:1 card frame centered in each row at the same scale and center anchor, filling about 92% of row width with ample green outside and inside
Frame sequence:
1 quiet warning rim, only faint amber hairline at lower corners;
2 amber signal begins at both lower corners and crawls partway up the sides;
3 uneven hand-painted light reaches upper corners with a few small drawn sparks;
4 strong pre-peak warning rim, most of border alive but top center still dark
Constraints: each row must be a genuinely distinct drawing of the planned light state, not a translated, scaled, rotated, recolored, blurred, opacity-changed, glow-filtered, or otherwise filtered copy; same frame identity, camera, palette, dimensions, scale, and center anchor in all rows; the amber filaments and sparks must be drawn into each source state; flat uniform #00ff00 background and center only; no cast shadow; no readable text; no numbers; no watermark; no people; no symbols; no white matte; do not use #00ff00 in the frame itself
Avoid: photorealistic scene, full UI mockup, solid filled card, checkerboard transparency, primitive rectangle-only art, labels, uneven row heights, perspective drift
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI animation source atlas for a warning-state disaster card frame
Primary request: create the final four genuinely redrawn sequential warning-rim frames in one exact single-column by 4-row atlas, continuing the same long empty hazard card border from a strong warning peak down to rest
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background, including the empty interior of the card frame
Subject: the same long 1930s civil-defense dossier frame made from dark gunmetal, aged brass corner brackets, narrow amber enamel warning filaments, and worn paper-edge texture; the border is decorative only and the entire center stays flat green
Style/medium: HOI4 painted interface art, tactile period metal and paper, restrained amber warning light, no modern screen graphics
Composition/framing: exactly four equal wide horizontal rows with no gutters, no labels, no separators; one identical 6.14:1 card frame centered in each row at the same scale and center anchor, filling about 92% of row width with ample green outside and inside
Frame sequence:
5 peak warning, full uneven amber rim alive with a few hand-painted sparks at upper corners;
6 warning recedes, top-center goes dark and the outer filaments break into segments;
7 low warning, light remains only along side brackets and lower corners;
8 near-rest, one faint amber trace at lower corners, visually close to the opening frame for a clean loop
Constraints: each row must be a genuinely distinct drawing of the planned light state, not a translated, scaled, rotated, recolored, blurred, opacity-changed, glow-filtered, or otherwise filtered copy; same exact frame identity, camera, palette, dimensions, scale, and center anchor in all rows and compatible with the earlier four-frame atlas; the amber filaments and sparks must be drawn into each source state; flat uniform #00ff00 background and center only; no cast shadow; no readable text; no numbers; no watermark; no people; no symbols; no white matte; do not use #00ff00 in the frame itself
Avoid: photorealistic scene, full UI mockup, solid filled card, checkerboard transparency, primitive rectangle-only art, labels, uneven row heights, perspective drift
```
