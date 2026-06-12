# Buddha Mandate Portrait Frame Plan

The loop uses sixteen generated source frames split from a generated animation source sheet. Motion must come from separate drawn frame states, not from transform-only processing, simple vignettes, zooms, warps, or color filters over one still image.

| Frame | State | Notes |
| --- | --- | --- |
| 0 | Resting radiance | Calm golden portrait, halo low, crown jewels quiet. |
| 1 | First breath | Halo brightens slightly behind the crown; brow light warms. |
| 2 | Lamp reflection | Side lamp and cheek highlights rise without changing pose. |
| 3 | Crown shimmer | Crown points and side ornaments catch restrained gold light. |
| 4 | Forehead jewel | Forehead jewel brightens; eyes remain calm. |
| 5 | Mandala intake | Mandala ring grows denser behind the crown. |
| 6 | Eye glint | Eye light increases by a small step, still readable at portrait size. |
| 7 | Golden crest | Halo reaches a controlled crest, with no heavy vignette. |
| 8 | Full mandate | Jewel and halo light peak subtly; robe shadows remain detailed. |
| 9 | Settling breath | Face light softens and lower ornaments regain shadow. |
| 10 | Robe echo | Saffron robe highlights move into a quieter gold state. |
| 11 | Jewel recession | Crown glints recede from the peak. |
| 12 | Mandala thinning | Halo texture thins while the head alignment stays steady. |
| 13 | Temple darkening | Background shadows return and lamp reflections lower. |
| 14 | Quiet jewel echo | Eye and forehead light return toward rest. |
| 15 | Return to rest | Halo dims close to frame 0 intensity while preserving alignment. |

## Processing

- Resize/crop each source to `156x210`, centered on the face and crown.
- Assemble the sixteen processed frames horizontally into `portrait_THR_buddha_mandate_sheet.png`.
- Convert the sheet to `gfx/leaders/THR/portrait_THR_buddha_mandate_animated.dds`.
- Build a contact sheet and GIF preview for review.
