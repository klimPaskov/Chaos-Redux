# Rat King Readiness Seal Frame Plan

Each 64×64 authored frame is assembled from the unchanged static seed and its own ImageGen transparent glint layer, except frame 000, which is the exact static seed.

| Frame | Motion state | Source layer | Visual change | Loop note |
|---|---|---|---|---|
| 000 | Rest | `readiness_static.png` | Original readiness seal without an added glint | Exact static fallback and frame-0 source |
| 001 | Rising | `frame_001_upper_right_glint_raw.png` | Faint glint on the crown's upper-right edge | Begins the pulse |
| 002 | Rising | `frame_002_upper_right_glint_raw.png` | Brighter glint near the same crown edge | Keeps the emblem fixed |
| 003 | Peak | `frame_003_peak_glint_raw.png` | Brightest source glint at the upper-right crown | Remains a small accent |
| 004 | Falling | `frame_004_falling_glint_raw.png` | Shorter and softer glint | Returns toward rest |
| 005 | Falling | `frame_005_falling_glint_raw.png` | Smaller gold reflection on the upper-right rim | Keeps the anchor stable |
| 006 | Fading | `frame_006_faint_glint_raw.png` | Narrow, dim upper-right reflection | Native-alpha source layer |
| 007 | Near rest | `frame_007_near_rest_glint_raw.png` | Very faint final glint | Connects back to frame 000 |

The first frame-006 candidate produced a circular halo and was rejected; it is preserved under `source/imagegen/readiness/rejected/` for lineage, and the accepted replacement is `frame_006_faint_glint_raw.png`.

All accepted generated layers requested genuine transparency in their initial ImageGen call, and each raw layer retains its native alpha.

The generated highlight layer is resized only to fit the exact 64×64 canvas and composited over the immutable static seed; local processing does not synthesize the light state.

The authored master contact sheet is `readiness_seal_contact.png`, the 512×64 master is `sheets/readiness_seal_sheet.png`, and the review-only GIF is `previews/readiness_seal_preview.gif`.

The 34×34 consumer preview contact sheet is `decision_34x34_preview/readiness_decision_34x34_contact.png`; its 272×34 sheet and 34×34 static PNG remain review candidates until parent acceptance.
