# Zol World-End Portrait Frame Plan

The loop uses eight individually edited portrait frames built from the approved static fallback portrait. Each source frame intentionally represents a small eye-glow state while keeping the portrait locked in place.

| Frame | State | Notes |
| --- | --- | --- |
| 00 | Rest | Static fallback match with the faintest extra eye bloom. |
| 01 | First rise | Eyes brighten slightly, no other portrait change. |
| 02 | Low pulse | Eyes brighten again with the same face, hood, and background. |
| 03 | Mid pulse | Slightly stronger eye bloom, still confined to the eye area. |
| 04 | Peak | Strongest eye glow in the loop, still restrained and local. |
| 05 | Fall | Eyes return from peak with no silhouette drift. |
| 06 | Low fall | Near-rest brightness, same locked portrait. |
| 07 | Seam return | Very low glow for a clean return to frame `00`. |

## Processing

- Source and processed frames both stay at `156x210` because the static fallback seed is already final-size.
- Reuse the existing static fallback portrait export unchanged.
- Assemble the eight processed frames horizontally into `portrait_DTH_zol_world_end_sheet.png`.
- Convert the static PNG and sheet PNG to DDS.
- Build a contact sheet and GIF preview for review.

## Validation

- Contact sheet review: same portrait in all 8 frames, only eye-glow intensity changes.
- Identity drift check: non-eye difference mean is `0` for frames `00`, `01`, `02`, `06`, `07` and effectively zero (`3.59118e-07` to `5.9853e-07`) for frames `03`, `04`, `05` when measured outside the eye mask.
- Sheet and final DDS remain `1248x210`.
