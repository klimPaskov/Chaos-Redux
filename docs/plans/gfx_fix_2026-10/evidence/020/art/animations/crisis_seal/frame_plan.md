# Crisis Seal Frame Plan

Each frame is a separate 64×64 output assembled from the unchanged static seed and its own ImageGen transparent glint layer, except frame 000, which is the exact static seed.

| Frame | Motion state | Source layer | Visual change | Loop note |
|---|---|---|---|---|
| 000 | Rest | `crisis_static.png` | Original seal with no added glint | Exact static fallback and frame-0 source |
| 001 | Rising | `frame_001_fresh_upper_left_glint_raw.png` | Fresh narrow warm glint on the upper-left rim | Request saved before generation; supersedes the carry-forward candidate |
| 002 | Rising | `frame_02_upper_left_glint_raw.png` | Brighter curved glint in the same rim region | Keeps the seal design fixed |
| 003 | Near peak | `frame_003_upper_arc_glint_raw.png` | Clearer glint climbs slightly toward the top arc | Remains within the outer ring |
| 004 | Falling | `frame_004_upper_arc_glint_raw.png` | Shorter highlight approaches the top arc | No silhouette movement |
| 005 | Falling | `frame_005_top_glint_raw.png` | Soft short highlight at the top-middle rim | Begins return toward rest |
| 006 | Fading | `frame_006_falling_glint_raw.png` | Small dim glint on the upper-right rim | Tightly localized |
| 007 | Near rest | `frame_007_near_rest_glint_raw.png` | Faint final glint at the upper-right rim | Connects back to frame 000 |

All final generated source layers requested a genuine transparent background in their initial ImageGen call, and every raw source layer retains that alpha.

The exact frame-001 replacement request was saved before generation in `source/imagegen/requests/crisis_frame_001.json`; the earlier carry-forward layer and composite are retained under `source/imagegen/crisis/superseded/` with superseded status.

The generated highlight layer is resized only to fit the exact 64×64 canvas and composited over the immutable static seed; the script does not add, move, pulse, recolour, blur, or otherwise synthesize the visual change.

The per-frame contact sheet is `crisis_seal_contact.png`, the final sheet is `sheets/crisis_seal_sheet.png`, and the review-only GIF is `previews/crisis_seal_preview.gif`.
