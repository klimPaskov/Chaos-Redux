# Zol World-End Portrait Frame Plan

The loop uses eight individually generated portrait frames. Motion comes from separate full-frame renders, not from moving, scaling, warping, blurring, recoloring, or pulsing a single still image.

| Frame | State | Notes |
| --- | --- | --- |
| 00 | Rest | Hooded void face, low eye glow, minimal crown silhouette. |
| 01 | First stir | Crown sharpens and eye glow rises slightly. |
| 02 | Gathering end | Eclipse ring appears and ash drift increases. |
| 03 | Advancing dominion | Shroud tears and crown height intensify. |
| 04 | World-end crest | Brightest halo and strongest ash movement. |
| 05 | Lingering crest | Halo stays bright while the cloth settles slightly. |
| 06 | Ebbing aftermath | Halo thins and the eyes dim from the peak. |
| 07 | Return to dread | Near-rest state for the loop seam, with sparse ash and reduced halo. |

## Processing

- Resize and center each source frame to `156x210`.
- Use frame `04` as the static fallback portrait export.
- Assemble the eight processed frames horizontally into `portrait_DTH_zol_world_end_sheet.png`.
- Convert the static PNG and sheet PNG to DDS.
- Build a contact sheet and GIF preview for review.
