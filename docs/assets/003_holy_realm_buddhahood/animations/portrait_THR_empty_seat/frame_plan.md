# Empty Seat Portrait Frame Plan

The loop uses eight individually generated key-state source portraits expanded into sixteen playback frames by mirrored ordering. Motion comes from separate drawn key states, not from transform-only processing, simple vignettes, zooms, warps, or color filters over one still image.

| Frame | State | Notes |
| --- | --- | --- |
| 0 | Still seat | Empty lotus cushion under a dim mandala arch, low ash light. |
| 1 | First dust | Fine ash motes brighten around the throne back. |
| 2 | Lamp ember | Small lamps and side bowls catch pale light. |
| 3 | Cushion glint | Silk cushion highlights rise while the throne remains empty. |
| 4 | Hollow ring | A thin ring of absence strengthens behind the empty cushion. |
| 5 | Ash intake | Dust and smoke density increase without spectacle. |
| 6 | Bell echo | Bell and side ornaments catch soft ivory-gold light. |
| 7 | Mandala crest | Mandala reaches a controlled bright state, no heavy vignette. |
| 8 | Mirrored bell echo | Returns through key state 6 as the light leaves the ornaments. |
| 9 | Mirrored ash intake | Returns through key state 5 with the smoke density lowering. |
| 10 | Mirrored hollow ring | Returns through key state 4 with the mandala ring thinning. |
| 11 | Mirrored cushion glint | Returns through key state 3 as the cushion light falls. |
| 12 | Mirrored lamp ember | Returns through key state 2 with weaker side-light. |
| 13 | Mirrored first dust | Returns through key state 1 with ash motes near rest. |
| 14 | Still seat | Returns to key state 0. |
| 15 | Stillness hold | Holds key state 0 for a softer loop seam. |

## Processing

- Resize/crop each source to `156x210`, centered on the empty throne and mandala arch.
- Save frame 000 as the static fallback `portrait_THR_empty_seat.dds`.
- Assemble the sixteen processed frames horizontally into `portrait_THR_empty_seat_sheet.png`.
- Convert the sheet to `gfx/leaders/THR/portrait_THR_empty_seat_animated.dds`.
- Build a contact sheet and GIF preview for review.
