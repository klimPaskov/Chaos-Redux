# Event 015 Advisor Icon HOI4 Style Gap Audit

Date: 2026-07-16  
Role: bounded visual and technical audit  
Scope: the sixteen Event 015 advisor icons, the six canonical vanilla advisor references, the current processor, and the optional `v2` overlay candidates  
Implementation authority: audit only; no runtime assets, scripts, manifests, or skills were edited

## Outcome

**FAIL — complete one-to-one recomposition is required for all sixteen icons.**

The sixteen accepted ImageGen portrait masters are distinct and may remain the identity sources, but none of the current `65x67` compositions passes as a vanilla HOI4 small-advisor portrait. The present family reads as a modern bronze/black framed portrait with a tall sealed parchment attached at the far right. The six vanilla references instead read as a compact, tilted charcoal dossier/photo card with a broad pale memo crossing its lower-right quadrant and substantial transparent corner space.

This is not a dimensions-only problem and cannot be repaired by substituting the `v2` overlays into the existing processor unchanged. Each advisor needs an explicit portrait crop and grade, newly generated visible frame and paper artwork, and recomposition against the canonical vanilla silhouette described below.

## Evidence reviewed

### Canonical vanilla references

All six reference PNGs in `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/` were inspected at native resolution and compared with their original vanilla DDS sources. The decoded DDS pixels match the reference PNGs exactly; all are RGBA `65x67`:

| Reference | Vanilla source |
|---|---|
| `generic_europe_1.png` | `gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds` |
| `generic_female_europe.png` | `gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds` |
| `generic_asia_1.png` | `gfx/interface/ideas/idea_generic_political_advisor_asia_1.dds` |
| `friedrich_paulus.png` | `gfx/interface/ideas/idea_GER_friedrich_paulus.dds` |
| `gunther_von_kluge.png` | `gfx/interface/ideas/idea_GER_gunther_von_kluge.dds` |
| `erwin_rommel.png` | `gfx/interface/ideas/idea_erwin_rommel.dds` |

The linked vanilla definitions were also checked in `interface/ideas.gfx`, `interface/ideas_characters.gfx`, `interface/_leader_portraits.gfx`, and `common/characters/GER.txt`. The small advisor/idea portrait is a dedicated `65x67` asset rather than a blind resize of a leader portrait.

### Event 015 candidates

All sixteen processed icons were inspected individually at their original `65x67` size, together with the native and nearest-neighbour contact sheets and the full-resolution portrait sources:

1. interpreter
2. general provisioner
3. secretary of callings
4. surveyor of shores
5. civic engineer
6. keeper of stores
7. league envoy
8. advocate of limits
9. public auditor
10. constitutional jurist
11. council organizer
12. social workshop planner
13. chief surveyor
14. standards engineer
15. steward of service
16. contract broker

All sixteen currently share the same alpha-channel hash. Their metadata records a full-master crop rather than an advisor-specific head-and-shoulders crop, so the current uniformity is produced by the template rather than by individual composition.

## Concrete failure reasons

### 1. The outer silhouette is the wrong object

The vanilla family shares the same tilted dossier-card row/column envelope. Under the project visible-footprint mask used for native comparison, the six references occupy approximately **0.788 of the canvas**, with the same row/column silhouette family across all six. The current icons form a nearly full-height, nearly full-width upright rectangle and therefore do not share that envelope.

Threshold-specific RGBA measurements make the excess coverage unambiguous:

| Metric on 4,355-pixel canvas | Six vanilla references | All sixteen current icons |
|---|---:|---:|
| Any alpha (`>0`) | 84.52–86.36% | 93.87% |
| Stable visible alpha (`>=32`) | 72.65–72.86% | 92.28% |
| Majority alpha (`>=128`) | 58.78–59.36% | 87.62% |
| Fully opaque | 49.87–50.36% | 75.87% |
| Semi-transparent pixels | 1,488–1,575 | 784 |

At `alpha >=32`, vanilla occupies approximately `x=1..61, y=1..63` while the current template occupies `x=1..64, y=1..66`. At `alpha >=128`, vanilla is approximately `x=4..58, y=4..60`; current is `x=1..62, y=1..66`. The fully opaque vanilla core is about `52x54`, while the current opaque core is about `61x63`.

Transparent corners are consequently missing. Across the four `5x5` corner patches, vanilla retains 78–82 fully transparent pixels out of 100; current retains only 45. Across four `8x8` patches, vanilla retains 144–157 out of 256; current retains 77.

### 2. The dossier card is too large, too tall, and effectively upright

On upper rows not crossed by the paper, the vanilla card spans roughly `x=4..44`, or about 40 pixels. The current card spans roughly `x=1..56`, or about 56 pixels. Vanilla's body visually ends around `y=57`; the current frame continues to `y=64`.

The fitted upper edge of the vanilla card is approximately **-4.35 degrees**. The current template measures approximately **+0.06 degrees**, visually flat. Its scripted `-0.85` degree rotation is insufficient after fitting and compositing.

### 3. The visible frame artwork is not HOI4 dossier artwork

The current frame is a thick black/bronze industrial bezel with gold edging, rivet-like highlights, and modern game-UI construction. Vanilla uses a subdued, irregular charcoal photo/dossier mount with thin cool-gray edge separation and a layered-paper feel. The current frame therefore remains visibly wrong even before portrait content is considered.

Measured frame treatment confirms the visual mismatch:

| Frame characteristic | Vanilla aggregate | Current aggregate |
|---|---:|---:|
| Edge median luminance | 44.0 | 38.9 |
| Edge saturation | 0.051 | 0.294 |
| Warm frame pixels (`R-B > 20`) | 5.6% | 31.2% |

The problem is not merely that current edges are dark. They are approximately 5.8 times as saturated and over five times as likely to read warm/brassy.

### 4. The paper is the wrong shape, placement, and visual hierarchy

Vanilla's pale memo footprint is approximately `x=30..56, y=26..57`, about `27x32` pixels with an aspect ratio near `0.84`. The current paper occupies approximately `x=42..62, y=25..64`, about `21x40` pixels with an aspect ratio near `0.53`.

The current paper is shifted roughly 12 pixels too far right, extends about 8 pixels too low, is too tall and narrow, and crowds the bottom and right edges. Its paperclip and large red wax seal collapse into noisy blobs at native size. Vanilla reads as a broad pale note with faint marks, not a full parchment prop.

The current paper top edge is also around `+3.53` degrees versus vanilla's nearly horizontal `+0.36` degree presentation.

Measured pale-paper luminance and saturation show another material mismatch:

| Paper characteristic | Vanilla aggregate | Current aggregate |
|---|---:|---:|
| Mean luminance | 206.8 | 193.0 |
| Mean saturation | 0.218 | 0.362 |

### 5. The portrait window is too large and carries too much scene information

The current processor fits every source to `48x59`, 73.8% of the canvas width and 88.1% of its height, then places it inside a `56x65` card. The visually varying portrait region is approximately `45x55` with an area of 2,149 pixels. Across the vanilla set, it is approximately `38x54` with an area of 1,350 pixels. Current visible portrait activity is therefore about **59% larger**.

The approximate vanilla inner portrait window is `32–35x46–49`, positioned around `x=9..11, y=8..10`. Individual head sizes in the current sources are not universally excessive; most overlap vanilla's rough `24–29x29–34` facial/head envelope. The failure comes from putting those heads inside a much larger scenic panel, leaving books, sacks, machinery, crowds, instruments, shelves, docks, and architectural backgrounds visible where vanilla would show a compressed painted bust.

Vanilla's invariant bright-paper area is about 742 pixels against 1,350 pixels of varying portrait area, a ratio near `0.55`. Current is about 674 against 2,149, a ratio near `0.314`. The dossier cue is therefore about 43% weaker relative to the portrait field.

### 6. The portrait grade is too dark, warm, and photographic

| Portrait characteristic | Vanilla aggregate | Current aggregate |
|---|---:|---:|
| Mean luminance | 101.3 | 77.5 |
| Median luminance | 103.1 | 78.3 |
| 10th percentile | 48.4 | 39.6 |
| 90th percentile | 148.1 | 115.2 |
| Mean saturation | 0.167 | 0.294 |

The current family loses facial landmarks in warm brown midtones. Vanilla retains cooler neutral shadows, brighter facial highlights, lower chroma, and a compressed painterly read. Current portraits can keep their identities and poses, but every output requires an individual crop and a cooler, brighter, lower-saturation grade.

### 7. The family passes template consistency, not native HOI4 readability

The identical alpha hashes demonstrate mechanical consistency, but at native size the first read is “ornate framed portrait plus attached parchment.” The required first read is “tilted dossier card, pale memo, face.” Existing comparison sheets use only two vanilla examples and magnified presentation; they do not prove native-size equivalence to the full six-reference silhouette family.

## `v2` overlay candidate assessment

The `v2` candidates improve the color direction and make the paper closer to the vanilla width/height ratio, but they **do not pass as replacements without regeneration and processor changes**.

- The frame remains a perfect, upright, thin modern metal rectangle rather than an irregular layered dossier/photo mount.
- The overlays contain baked cast shadows. The processor adds another alpha-derived shadow, creating a double-shadow risk.
- With the current processor, a representative `v2` composition measures approximately 89.0% at any alpha, 84.7% at `alpha >=32`, 78.7% at `alpha >=128`, and 72.0% fully opaque. This remains far above the vanilla threshold envelope.
- Its upper frame span is about 49 pixels and continues to `y=64`, versus vanilla's roughly 40-pixel upper span and termination near `y=57`.
- Its upper edge remains flat at approximately 0 degrees.
- Its paper becomes approximately `28x32`, but lands around `x=38..65, y=27..58`, still about 8 pixels too far right and clipping the canvas at lower-alpha pixels.

The `v2` paper may be retained as prompt/color-direction evidence. Neither its frame nor paper should be treated as approved visible art in the final build.

## Canonical rebuild acceptance contract

All sixteen icons must meet this contract individually and as a family.

### Canvas and source handling

1. Final PNG and DDS are RGBA `65x67`.
2. Retain the sixteen independent ImageGen portrait masters as the identity sources unless a genuine source defect is found.
3. Record an explicit advisor-specific crop box for every master. A full-source-bounds crop is not acceptable.
4. Preserve each subject's identity, pose, age, distinguishing hair, facial hair, eyewear, and expression while excluding scenic props from the small portrait window.

### Scripted geometry and generated visible artwork

5. **The processing script may and should supply the vanilla angle and alpha-derived shadow.** This is explicitly part of the requested implementation. Rotation, restrained perspective, crop, resize, color grade, shadow derivation from alpha, compositing, and export are appropriate scripted operations.
6. **Generated overlays must supply all visible frame, backing-card, paper, fold, mark, pin, and patina artwork.** The script must not procedurally draw a substitute visible frame or paper.
7. Generated overlays must be shadowless. Do not bake a cast shadow, outer glow, or ambient halo into the visible art; derive the final soft shadow from the overlay alpha in the script.
8. Target a dossier body roughly `40–44x54–58`, positioned approximately from `x=4..8, y=3..7`. On upper no-paper rows, its visible span should approximate the vanilla `x=4..44` family. The body should end around `y=57..59`, not at the canvas bottom.
9. Apply a script-supplied card tilt in the approximate **-3.5 to -5.0 degree** range, tuning it against the row/column envelope rather than trusting the numeric angle alone.
10. Use a soft card shadow of roughly 1–2 pixels offset and about 1–1.75 pixels blur as a starting point, then tune it to the alpha contract. Use a smaller paper shadow, approximately 1 pixel offset with less than 1 pixel blur.

### Portrait window and head scale

11. Target a visible portrait window of approximately `32–35x46–49`, located around `x=9..11, y=8..10` before the memo overlap.
12. Target face center around `x=24..29`, with the eye line around `y=22..29` after final composition.
13. Target a head envelope near `24–29x29–34`; intentional hair, hats, or beards may exceed it only when the face remains comparable to the six references.
14. Do not expose identifiable scenic story props merely because they exist in the portrait master. At `65x67`, the portrait must resolve as a painted bust.

### Paper geometry

15. Target the bright paper footprint around `x=30..56/58, y=26..57/59`, approximately `26–29x30–33` with an aspect ratio of `0.78–0.92`.
16. Keep the paper nearly horizontal, approximately **-1 to +2 degrees**.
17. Do not clip the paper against the right or bottom canvas edges.
18. Use faint, illegible marks at native size. No large wax seal, full-size paperclip, readable modern typography, or dominant emblem.

### Alpha and silhouette

19. Use the shared six-reference row/column visible-footprint mask as the primary alpha target: approximately **0.788 visible coverage**, with the same clipped, tilted dossier silhouette family across all six references. A candidate is not accepted merely because its canvas is `65x67`.
20. Under the same threshold definitions used in this audit, target approximately:

    - `alpha >=32`: 72–75%
    - `alpha >=128`: 57–61%
    - fully opaque: 48–52%
    - semi-transparent pixels: 1,400–1,650

21. Retain at least about 75 fully transparent pixels across the four `5x5` corners and at least about 140 across the four `8x8` corners.
22. Compare row-by-row and column-by-column alpha occupancy with all six vanilla references. Large rectangular plateaus, a full-height right edge, or a full-width bottom edge are automatic failures.

### Material, color, and paint treatment

23. Frame target: neutral charcoal/cool gray, edge median luminance approximately 40–55, saturation no higher than 0.10, and warm-frame fraction no higher than 10% under the audit definition. No brass, gold, rivets, ornamental corners, sci-fi bezel, or glossy modern UI edge.
24. Paper target: mean luminance approximately 200–216 and saturation approximately 0.17–0.25.
25. Portrait-family target: mean luminance approximately 95–110, 90th percentile at least 140, and mean saturation approximately 0.14–0.21. Preserve readable eyes, nose, mouth, glasses, and facial hair at native size.
26. Apply a restrained painted/printed dossier grade. Avoid photographic micro-detail, heavy sepia, deep crushed shadows, and orange skin.

### Native-size proof

27. At native `65x67`, the first read must be: **dossier card + paper + face**.
28. Every icon's comparison proof must show the source crop, final PNG, decoded final DDS, and all six vanilla references at native `1x` and nearest-neighbour `4x` or `8x`.
29. Provide one family sheet with all sixteen candidates and all six references. Also show them on transparency checkerboard, dark HOI4 UI charcoal, and a warm/brown politics-panel background.
30. Validate final PNG-to-decoded-DDS pixel equivalence. Asset approval is based on the decoded runtime result, not the pre-export PNG alone.
31. Existing metadata statuses that call the current compositions approved must be superseded after rebuilding. No current approval result carries forward.

## Required generated overlay set

Generate original supporting art in one call per distinct variant; use the vanilla files only as style/geometry references and do not copy or trace vanilla people or exact artwork.

### Shadowless frame/backing variants

Produce at least three closely related variants on a removable flat chroma background:

1. neutral charcoal stacked-card frame with irregular clipped upper corners and a thin cool-gray bevel;
2. slightly worn charcoal photo mount with a restrained offset backing lip;
3. narrow dark dossier mount with subdued steel-gray edge highlights.

All must be shadowless and free of gold, brass, rivets, bolts, ornamental trim, gloss, glow, and perfect modern rectangles. Their family silhouette should remain close enough that the same row/column acceptance envelope applies.

### Shadowless paper variants

Produce at least three pale, wide memo variants:

1. blank paper with faint smudges and fiber variation;
2. two or three short illegible typed or pencil lines;
3. a tiny muted pin, stamp, or crease detail.

Do not include a wax seal, full-size clip, readable text, crest, or dominant red mark. Final visible size must remain within the paper contract above.

### Assignment

Use restrained frame/paper combinations across the sixteen advisors so the family is not sixteen literal clones, but do not vary the silhouette, paper scale, or palette enough to leave the six-reference vanilla family. Preserve generated sources, processed alpha overlays, variant assignment, and prompt provenance in the asset manifest.

## Per-advisor crop and grade handoff

Each row requires a recorded numeric crop box in the rebuilt metadata.

| Advisor | Required individual treatment |
|---|---|
| Interpreter | Crop above the book and crowd; preserve the three-quarter female face slightly left of center. Current head scale is broadly usable. Remove warm cast and lift eye/cheek definition. |
| General provisioner | Remove sacks and background from the window; keep the frontal face and practical expression. Current head scale is broadly usable; lift eyes into the native-readable range. |
| Secretary of callings | Preserve glasses and moustache; crop out ledger and workshop detail. Sharpen eye/glasses separation without photographic crispness. |
| Surveyor of shores | Widen the crop slightly to reduce the head about 1–2 pixels; remove survey instrument and harbor noise. Keep the face clear of the paper overlap. |
| Civic engineer | Head is about 2–3 pixels too large; use a wider crop. Preserve moustache and three-quarter pose, but exclude bridge/tool scenery. |
| Keeper of stores | Crop shelves and apron detail to a painted bust. Keep the older female identity and lift cool facial midtones. |
| League envoy | Crop out station and ledger; preserve the near-frontal moustached face. Neutralize brown suit shadows. |
| Advocate of limits | Remove book and chamber/crowd detail; preserve the stern gaze. Shift the face left as needed when the paper moves to its vanilla position. |
| Public auditor | Crop out the book. Lift the eyes and upper face so the downcast pose does not read as closed eyes at native size. |
| Constitutional jurist | Remove folder and office detail; reduce head about 1 pixel. Preserve glasses and frontal authority. |
| Council organizer | This is the largest current head; widen crop to reduce it about 2–3 pixels. Remove crowd and document while retaining the three-quarter pose. |
| Social workshop planner | Reduce head about 1–2 pixels; remove planning grid and workshop detail. Preserve restrained expression and hair silhouette. |
| Chief surveyor | Crop out calipers and map while preserving the beard silhouette. Current overall scale is usable; lift gray-beard and eye midtones. |
| Standards engineer | Remove gauge and laboratory detail; reduce head about 1–2 pixels. Preserve glasses at native readability. |
| Steward of service | Reduce head about 1–2 pixels; crop out hangar and book. Lift facial values so the older male face does not merge into the frame. |
| Contract broker | Remove briefcase and harbor detail; reduce head about 1 pixel. Keep the three-quarter female face far enough left for the correctly placed memo. |

## Required proof package before approval

The rebuild is ready for approval only when the asset package contains:

- sixteen explicit source crop records;
- generated shadowless frame and paper sources plus processed alpha overlays;
- sixteen final `65x67` PNGs and DDS files;
- decoded-DDS comparison evidence;
- per-icon native and nearest-neighbour sheets against all six references;
- a full-family native comparison sheet on three backgrounds;
- row/column alpha-envelope measurements and threshold metrics;
- updated manifest and validation records that supersede the current approvals.

## Simplifications, omissions, and blockers

- This handoff is an audit, not an asset rebuild. The current sixteen runtime icons remain failed until the complete recomposition is implemented and proven against this contract.
- The sixteen independent portrait masters were treated as accepted identity sources; no replacement generation was requested in this bounded task.
- The optional `v2` overlays were evaluated but not accepted as a fallback or final substitute.
- No fallback or simplification is approved.
- No runtime assets, scripts, manifests, localisation, skills, or spreadsheets were changed.
- No commit was created.

## Skills and references used

- `chaos-redux-event-assets` for advisor-card construction, generated visible-art requirements, DDS handoff, and native-size comparison rules.
- `chaos-redux-subagents` for bounded audit ownership and handoff requirements.
- `imagegen` for generated-supporting-art constraints and variant prompting guidance.
- Required offline Paradox wiki core pages, Portrait Modding, Graphical Asset Modding, Interface Modding, and Scripted GUI Modding.
- Vanilla portrait definitions and relevant official documentation for portrait assignment and character/advisor asset behavior.

No skill was created or updated.
