# Dhyana Seal Frame Plan

The loop uses twelve generated source frames. The final source frames were sliced from one `$imagegen` animation-source grid so the seal identity stays consistent across the loop. Motion still comes from distinct generated panel states, not transform-only processing of one still image.

| Frame | State | Notes |
| --- | --- | --- |
| 0 | Quiet rest | Inner flame low and petals dark. |
| 1 | First inhale | Flame brightens slightly. |
| 2 | Ember lift | Slightly stronger core and faint smoke stir. |
| 3 | Petal wake | Inner petals catch more lavender light. |
| 4 | Deeper inhale | Outer petals begin to answer the core. |
| 5 | Held stillness | Breathing light steadies without flare. |
| 6 | Peak stillness | Brightest controlled center and petal response. |
| 7 | Held peak | Peak glow lingers for one frame. |
| 8 | Soft release | Core lowers and smoke starts to thin. |
| 9 | Settling glow | Petal light recedes but remains warm. |
| 10 | Quiet return | Near-rest state with faint remaining halo. |
| 11 | Seam frame | Close match to frame 000 for a clean loop. |

## Processing

- Resize/crop each source to `96x96`, centered on the seal.
- Save frame 000 as the static fallback `holy_realm_dhyana_seal.dds`.
- Assemble the twelve processed frames horizontally into `holy_realm_dhyana_seal_sheet.png`.
- Convert the sheet to `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds`.
- Build a contact sheet and GIF preview for review.
