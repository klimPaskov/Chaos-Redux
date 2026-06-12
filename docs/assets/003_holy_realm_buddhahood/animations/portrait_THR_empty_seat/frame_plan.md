# Empty Seat Portrait Frame Plan

The loop uses eight independent generated frames. Motion must come from separate source artwork, not transform-only processing of one still image.

| Frame | State | Notes |
| --- | --- | --- |
| 0 | Still seat | Empty lotus cushion under a dim mandala arch, low ash light. |
| 1 | First dust | Fine ash motes brighten around the throne back. |
| 2 | Bell echo | Small bell and side ornaments catch pale light. |
| 3 | Hollow halo | A thin ring of absence forms behind the empty cushion. |
| 4 | Absence peak | Halo and ash light reach maximum while the throne remains empty. |
| 5 | Witness quiet | Light softens and the black-gold arch becomes more visible. |
| 6 | Fading bell | Bell glint fades; cushion and lotus regain shadow. |
| 7 | Return to stillness | Ash motes settle back toward frame 0. |

## Processing

- Resize/crop each source to `156x210`, centered on the empty throne and mandala arch.
- Save frame 000 as the static fallback `portrait_THR_empty_seat.dds`.
- Assemble the eight processed frames horizontally into `portrait_THR_empty_seat_sheet.png`.
- Convert the sheet to `gfx/leaders/THR/portrait_THR_empty_seat_animated.dds`.
- Build a contact sheet and GIF preview for review.
