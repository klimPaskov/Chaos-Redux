# Generation provenance

Source mode for every frame: built-in `image_gen`. No CLI fallback or transform-created motion was used.

| Frames | Project atlas | Built-in output filename | Cells |
| --- | --- | --- | --- |
| `000`-`003` | `source_frames/013_disaster_card_frame_impact_atlas_a_source.png` | `exec-6644244e-5bba-4655-992d-df8516c68d39.png` | rows 1-4 |
| `004`-`007` | `source_frames/013_disaster_card_frame_impact_atlas_b_source.png` | `exec-5227935b-e540-48f2-8f41-7e42d65a6185.png` | rows 1-4 |
| `008`-`009` | `source_frames/013_disaster_card_frame_impact_atlas_c_source.png` | `exec-c0c7c454-0744-4053-ad7b-0522c4912f99.png` | rows 1-2 |

## Exact atlas A prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI animation source atlas for an impact-state disaster card frame
Primary request: create the first four genuinely redrawn frames of a ten-frame impact-border cycle in one exact single-column by 4-row atlas, showing the same long empty disaster card border from tense rest into a violent impact flash
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background, including the empty interior
Subject: a long 1930s emergency dossier frame built from scorched black steel, dented copper corner plates, chipped red enamel, hairline cracks, torn paper-edge texture, and hand-painted impact sparks; center remains flat green
Style/medium: HOI4 painted interface art, period industrial metal, disaster damage, restrained ember red and hot orange, no modern electronics
Composition/framing: exactly four equal wide horizontal rows with no gutters, no labels, no separators; one identical 6.14:1 border centered per row at the same scale and center anchor, about 92% row width, with green outside and inside
Frame sequence:
1 tense dark border with one hairline crack at lower left;
2 first impact stress, two cracks spread from lower corners and a few embers appear;
3 flash rises, copper corners brighten, cracks reach the side rails, small debris flecks are redrawn;
4 pre-impact burst, a hot uneven orange-red flash races along the lower and side borders while the top rail begins to fracture
Constraints: every row is a genuinely distinct redrawing of its damage and flash state, not a translated, scaled, rotated, recolored, blurred, opacity-changed, glow-filtered, or filtered copy; same border identity, camera, palette, dimensions, scale, and center anchor in all rows; cracks, sparks, chips, and light are drawn into each source frame; flat uniform #00ff00 background and interior only; no cast shadow; no readable text; no numbers; no watermark; no people; no symbols; no white matte; do not use #00ff00 in the border
Avoid: photorealistic scene, filled UI card, checkerboard, primitive rectangle-only art, labels, perspective drift, fire filling the center
```

## Exact atlas B prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI animation source atlas for an impact-state disaster card frame
Primary request: create middle frames five through eight of a ten-frame impact-border cycle in one exact single-column by 4-row atlas, continuing the same long empty scorched disaster card border through peak impact and early decay
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background, including the empty interior
Subject: the same long 1930s emergency dossier frame built from scorched black steel, dented copper corner plates, chipped red enamel, hairline cracks, torn paper-edge texture, and hand-painted impact sparks; center remains flat green
Style/medium: HOI4 painted interface art, period industrial metal, disaster damage, restrained ember red and hot orange, no modern electronics
Composition/framing: exactly four equal wide horizontal rows with no gutters, no labels, no separators; one identical 6.14:1 border centered per row at the same scale and center anchor, about 92% row width, with green outside and inside
Frame sequence:
5 peak impact, the full irregular border is fractured and incandescent at several stress points with drawn sparks and a few suspended chips;
6 immediate aftermath, flash still strong but broken into separate hot seams, more dark steel visible;
7 decay, glowing seams cool to deep orange, debris has fallen, major cracks remain visible;
8 late decay, only several red embers and two orange crack tips remain while the damaged border darkens
Constraints: every row is a genuinely distinct redrawing of its damage and flash state, not a translated, scaled, rotated, recolored, blurred, opacity-changed, glow-filtered, or filtered copy; same border identity, camera, palette, dimensions, scale, and center anchor in all rows and compatible with the first four-frame atlas; cracks, sparks, chips, and light are drawn into each source frame; flat uniform #00ff00 background and interior only; no cast shadow; no readable text; no numbers; no watermark; no people; no symbols; no white matte; do not use #00ff00 in the border
Avoid: photorealistic scene, filled UI card, checkerboard, primitive rectangle-only art, labels, perspective drift, fire filling the center
```

## Exact atlas C prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV scripted-GUI animation source atlas for an impact-state disaster card frame
Primary request: create the final two genuinely redrawn frames of a ten-frame impact-border cycle in one exact single-column by 2-row atlas, returning the same long empty scorched disaster card border from late decay toward tense rest
Scene/backdrop: every row uses the same perfectly flat solid #00ff00 chroma-key background, including the empty interior
Subject: the same long 1930s emergency dossier frame built from scorched black steel, dented copper corner plates, chipped red enamel, cooled cracks, torn paper-edge texture, and a few hand-painted embers; center remains flat green
Style/medium: HOI4 painted interface art, period industrial metal, disaster damage, restrained deep red and dull orange, no modern electronics
Composition/framing: exactly two equal wide horizontal rows with no gutters, no labels, no separators; one identical 6.14:1 border centered per row at the same scale and center anchor, about 92% row width, with green outside and inside
Frame sequence:
9 cooled aftermath, damaged cracks stay visible but only one dull ember remains near the lower rail;
10 reset bridge, the border is mostly dark with settled damage and one hairline orange crack, visually close to the opening frame for a clean loop
Constraints: each row is a genuinely distinct redrawing of its damage and ember state, not a translated, scaled, rotated, recolored, blurred, opacity-changed, glow-filtered, or filtered copy; same border identity, camera, palette, dimensions, scale, and center anchor in both rows and compatible with the earlier atlases; damage and ember states are drawn into each source frame; flat uniform #00ff00 background and interior only; no cast shadow; no readable text; no numbers; no watermark; no people; no symbols; no white matte; do not use #00ff00 in the border
Avoid: photorealistic scene, filled UI card, checkerboard, primitive rectangle-only art, labels, perspective drift, bright peak flash
```
