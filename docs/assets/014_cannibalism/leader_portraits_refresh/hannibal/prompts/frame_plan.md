# Hannibal Lecter canonical portrait and 12-frame animation plan

## Canonical source contract

- Canonical user-supplied portrait: `gfx/leaders/014_cannibalism/hannibal.dds`.
- The live static fallback is the canonical `gfx/leaders/014_cannibalism/hannibal.dds` file itself.
- The decoded PNG of that DDS is the identity, crop, clothing, palette, backdrop, and registration reference for every generated frame.
- Frame `000` is the exact decoded canonical portrait. Frames `001` through `011` are separate built-in image-generation edits; no final frame may be a local transform, filter, recolour, overlay, warp, or optical-flow interpolation.
- Preserve the same fictional Hannibal Lecter shown by the canonical portrait: dark-skinned adult man, black dinner jacket, white shirt, red bow tie, red painted backdrop, and the same black branching silhouette behind his head.
- Do not introduce a prison, cell, bars, cage, detention corridor, restraints, recognisable actor likeness, text, insignia, watermark, or extra person.

## Animation contract

- Frame size: 156x210.
- Frame count: 12 genuine source states.
- Sheet size: 1872x210, horizontal, left to right.
- Playback: 12 fps, looping, `play_on_show = yes`, `pause_on_loop = 0.0`.
- Smoothing: `effectFile = "gfx/FX/buttonstate_blendframes.lua"`, following the vanilla frame-animation precedent.
- Static sprite: `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static`.
- Animated sprite: `GFX_cannibalism_revealed_portrait_animated`.
- Anchor: bottom-centre; eyes, bow tie, shoulders, and red backdrop remain registered.
- Action: Hannibal raises a blood-darkened silver dinner fork, slowly licks the tines, bites the morsel, chews with manic composure, and returns to the canonical pose.
- Gore boundary: painted blood on fork, mouth, and morsel is visible; the face and identity remain readable at 156x210.

## Shared image-generation edit instruction

Treat the canonical decoded PNG as binding. Preserve the exact same face, skin tone, hairline, expression structure, tuxedo, bow tie, background, branching silhouette, camera, crop, lighting, and Hearts of Iron IV painted portrait finish. Redraw only the requested anatomical expression, hand, fork, and morsel state. Keep the hand anatomically coherent and the silver fork consistent across adjacent frames. The result must remain a vertical 156:210 leader portrait, not a film still, action poster, prison scene, or wide illustration.

## Frame ledger

| Frame | Motion state | Required generated state |
| --- | --- | --- |
| `000` | Canonical rest | Exact decoded canonical DDS; no generated alteration. |
| `001` | Attention shifts | Eyes widen slightly and track downward; the end of a silver fork begins entering at lower camera-right. |
| `002` | Fork rises | A gloved hand raises the same fork to lower-chest height with a small blood-darkened morsel; Hannibal studies it. |
| `003` | Appraisal | Fork reaches bow-tie height; grin tightens and the tongue tip becomes visible. |
| `004` | Approach | Fork nears the mouth; lips part and the tongue extends toward the stained tines. |
| `005` | First contact | Tongue touches the fork; the blood-darkened morsel and manic eyes remain readable. |
| `006` | Deliberate lick | Tongue travels along the fork tines; one narrow painted blood smear changes position. |
| `007` | Bite | Teeth close around the morsel while the hand holds the fork steady; expression becomes openly delighted. |
| `008` | Chew | Fork withdraws a short distance; jaw and cheek show the first chewing state, with a small stain at one lip. |
| `009` | Savour | Fork turns between the fingers while Hannibal chews and fixes the viewer with direct eye contact. |
| `010` | Lower | Fork lowers toward the bottom edge; mouth closes after the final chew and the bow tie returns to its canonical registration. |
| `011` | Loop bridge | Utensil leaves frame; face, shoulders, lighting, and background settle very close to frame `000`, with lips closed for a clean blended loop. |

## Output contract

- Canonical decoded source: `source_png/leader_CBL_hannibal_static_source.png`.
- Source frames: `source_frames/leader_CBL_hannibal_000_source.png` through `_011_source.png`.
- Processed frames: `processed_frames/leader_CBL_hannibal_000.png` through `_011.png`.
- Static PNG: `sheets/leader_CBL_hannibal_static.png`.
- Sheet PNG: `sheets/leader_CBL_hannibal_sheet.png`.
- Static DDS: `gfx/leaders/014_cannibalism/hannibal.dds`.
- Sheet DDS: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`.
- Preview: `previews/leader_CBL_hannibal_preview.gif` at 12 fps.
- Contact sheets: source and processed contact sheets under `previews/`.
