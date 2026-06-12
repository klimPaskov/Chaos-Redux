# Empty Seat Portrait Frame Plan

The loop uses sixteen generated source frames split from a generated animation source sheet. Motion must come from separate drawn frame states, not from transform-only processing, simple vignettes, zooms, warps, or color filters over one still image.

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
| 8 | Absence peak | Halo and ash light peak subtly around the vacant throne. |
| 9 | Witness quiet | Halo softens and the black-gold arch becomes more visible. |
| 10 | Seat shadow | Cushion and lower carvings regain shadow. |
| 11 | Fading bell | Bell glint fades and side vessels darken. |
| 12 | Smoke thinning | Smoke and dust trails recede behind the backrest. |
| 13 | Arch return | Mandala texture lowers toward the resting state. |
| 14 | Last ember | One final low ember remains in the side lamps. |
| 15 | Return to stillness | Ash motes settle back toward frame 0. |

## Processing

- Resize/crop each source to `156x210`, centered on the empty throne and mandala arch.
- Save frame 000 as the static fallback `portrait_THR_empty_seat.dds`.
- Assemble the sixteen processed frames horizontally into `portrait_THR_empty_seat_sheet.png`.
- Convert the sheet to `gfx/leaders/THR/portrait_THR_empty_seat_animated.dds`.
- Build a contact sheet and GIF preview for review.
