# Dhyana Seal Frame Plan

The loop uses eight independent generated source frames. Motion must come from separate source artwork, not transform-only processing of one still image.

| Frame | State | Notes |
| --- | --- | --- |
| 0 | Closed breath | Dim blue-violet lotus seal, pale center quiet. |
| 1 | First inhale | Inner orb brightens slightly, outer rim stays thin. |
| 2 | Petal opening | Lotus geometry expands visually with more lavender light. |
| 3 | Held attention | Inner orb steadies, gold rim brightens. |
| 4 | Dhyana peak | Center and petals reach strongest glow without flare. |
| 5 | Soft release | Gold rim recedes and petal light softens. |
| 6 | Settling seal | Blue-violet tones deepen, inner orb fades. |
| 7 | Return breath | Seal returns close to frame 0. |

## Processing

- Resize/crop each source to `96x96`, centered on the seal.
- Save frame 000 as the static fallback `holy_realm_dhyana_seal.dds`.
- Assemble the eight processed frames horizontally into `holy_realm_dhyana_seal_sheet.png`.
- Convert the sheet to `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds`.
- Build a contact sheet and GIF preview for review.
