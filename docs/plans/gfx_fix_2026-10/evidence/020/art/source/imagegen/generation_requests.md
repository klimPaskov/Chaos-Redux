# Retained ImageGen Request Records

The original workspace was resumed after generation had started, so exact built-in ImageGen request arguments for the already-produced frames were recovered from the active turn and retained here after generation; the inherited carry-forward frame-001 request was unavailable and that candidate is now superseded.

The fresh frame-001 replacement request is stored separately in `source/imagegen/requests/crisis_frame_001.json` and was saved before that generation call.

All listed requests used `transparent_background: true` and the built-in `image_gen.imagegen` route; the tool did not expose a model, quality, size, or destination selector.

Each relative reference path below was passed as an absolute local path under `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\assets\gfx_fix_plague_2026-10\`; no recent-image count was used.

## Crisis seal frame 002

Candidate: `crisis_f002`; retained source: `source/imagegen/crisis/frame_02_upper_left_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-4286d732-2078-446a-8dcc-997bab232545.png`.

Reference image 1 was `source/existing_png/crisis_static.png`, the unchanged identity and palette anchor; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`, a material reference only.

```text
Use case: stylized-concept.
Asset type: one source layer for an eight-frame Hearts of Iron IV animated seal, to be composited over an immutable 64x64 static seal.
Input images: Image 1 is a style and geometry reference only for the original dark bronze finish and circular outer rim; do not reproduce or alter the seal. Image 2 is a glint material reference only for a warm metallic highlight; do not copy its exact shape or placement.
Primary request: Create one standalone warm brass glint layer for frame 002. The highlight is slightly brighter and a little longer than the frame 001 source layer, still confined to the upper-left arc of the same circular outer rim. Keep its visual center around 28% of the canvas width and 28% of its height, with a short diagonal sweep that follows the arc. It must read as a reflected glint on metal when composited over the static seal, not as an independent object.
Style/medium: restrained hand-painted metallic reflection with antique brass, a small pale-gold core, and muted amber edge.
Composition: square 64x64 transparent canvas; one localized curved glint occupying at most 18% of the canvas width and 14% of its height; blank transparent canvas everywhere else.
Background: genuine transparent pixels, native alpha.
Constraints: keep the canvas anchor fixed; no main seal, no skull, no new emblem, no added design detail, no extra lights; only the glint layer.
Avoid: opaque background, checkerboard, matte, halo beyond a tight 2-pixel falloff at native size, text, watermark, border, sparks, particles, second highlight, flares, or any changes to the seed seal.
```

## Crisis seal frame 003

Candidate: `crisis_f003`; retained source: `source/imagegen/crisis/frame_003_upper_arc_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-2bb40bb0-0b2c-4336-b29b-4577274a1c0d.png`.

Reference image 1 was `source/existing_png/crisis_static.png`, the unchanged identity and palette anchor; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`, a material reference only.

```text
Use case: stylized-concept.
Asset type: one source layer for a Hearts of Iron IV animated symbolic seal, composited over an immutable 64x64 static seal.
Input images: Image 1 is only a color and geometry reference for the antique dark-bronze outer ring; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint.
Primary request: Create a single standalone transparent glint layer for frame 003. It is a stronger, clearer reflected highlight on the upper-left outer rim, at the rising-to-peak part of a slow pulse. Place its center near 29% of canvas width and 26% of canvas height; shape it as a short diagonal streak that follows a circular metal arc.
Style/medium: hand-painted antique-brass reflection with a pale gold core and muted amber falloff, matching the static seal metal.
Composition: square 64x64 output canvas; one small localized highlight, at most 18% of canvas width and 12% of its height; all remaining canvas genuinely transparent.
Background: genuine transparent background with native alpha.
Constraints: layer only, no emblem or seal pixels; stable canvas anchor; no added shape except the glint itself.
Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, additional lights, or any changes to the original seal.
```

## Rat King readiness frame 001

Candidate: `readiness_f001`; retained source: `source/imagegen/readiness/frame_001_upper_right_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-f2c9fddd-cad5-4996-bca9-e3ea72cf8bea.png`.

Reference image 1 was `source/existing_png/readiness_static.png`, the unchanged identity and palette anchor; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`, a glint material reference only.

```text
Use case: stylized-concept.
Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal.
Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint.
Primary request: Create a single standalone transparent glint layer for frame 001. It is a faint reflected highlight on the upper-right crown and rim of the static seal, beginning a slow pulse. Place its center near 68% of canvas width and 24% of canvas height, following the curve of the top-right metal edge.
Style/medium: hand-painted, subdued antique-brass light with a tiny pale gold core and a brown-gold edge, restrained enough to preserve the underlying dark emblem.
Composition: square 64x64 transparent canvas; one small localized highlight no larger than 15% of canvas width by 12% of its height; every other pixel area stays genuinely transparent.
Background: genuine transparent background with native alpha.
Constraints: layer only, no emblem or seal pixels; stable canvas anchor; no added object except this glint.
Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, extra light sources, or changes to the original seal.
```

## Crisis seal frame 004

Candidate: `crisis_f004`; retained source: `source/imagegen/crisis/frame_004_upper_arc_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-36b1e2cb-5d24-45e0-af6d-816f24f45b4d.png`.

Reference image 1 was `source/existing_png/crisis_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept.
Asset type: one source layer for a Hearts of Iron IV animated symbolic seal, composited over an immutable 64x64 static seal.
Input images: Image 1 is only a color and geometry reference for the antique dark-bronze outer ring; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint.
Primary request: Create one standalone transparent glint layer for frame 004. The pulse has just passed its brightest point and the small curved reflection has moved toward the top arc, centered near 38% of canvas width and 20% of its height. Make the glint a little softer and shorter than a peak highlight but still clearly visible at native 64x64 size.
Style/medium: hand-painted antique-brass reflection with a pale gold core and muted amber falloff, matching the static seal metal.
Composition: square 64x64 output canvas; one localized highlight occupying at most 16% of the canvas width and 11% of its height; large empty transparent area elsewhere.
Background: genuine transparent background with native alpha.
Constraints: layer only, no seal or symbol pixels; stable canvas anchor; no added detail except this one glint.
Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, additional lights, or any changes to the original seal.
```

## Rat King readiness frame 002

Candidate: `readiness_f002`; retained source: `source/imagegen/readiness/frame_002_upper_right_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-10b9186c-bffb-407a-bd6c-daae35b3afdf.png`.

Reference image 1 was `source/existing_png/readiness_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept.
Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal.
Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint.
Primary request: Create one standalone transparent glint layer for frame 002. The pulse is near its peak, so the reflection across the upper-right crown edge is brighter and slightly longer than frame 001. Keep it centered near 69% of canvas width and 23% of height, following the metal contour.
Style/medium: hand-painted, subdued antique-brass light with a tiny pale gold core and brown-gold edge, restrained enough to preserve the dark emblem.
Composition: square 64x64 output canvas; one small localized highlight no larger than 16% of canvas width by 12% of its height; every other pixel area stays genuinely transparent.
Background: genuine transparent background with native alpha.
Constraints: layer only, no emblem or seal pixels; stable canvas anchor; no added object except the glint.
Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, extra light sources, or changes to the original seal.
```

## Crisis seal frame 005

Candidate: `crisis_f005`; retained source: `source/imagegen/crisis/frame_005_top_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-80144780-942b-40c1-bc08-5c44e591ae56.png`.

Reference image 1 was `source/existing_png/crisis_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the antique dark-bronze outer ring; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint. Primary request: Create one standalone transparent glint layer for frame 005. The glint has moved to the upper-middle arc of the same ring, centered near 51% of canvas width and 14% of its height. It is the fading end of a slow pulse: softer and shorter than the peak, still visible at native 64x64 size. Style/medium: hand-painted antique-brass reflection with a tiny pale-gold core and muted amber edge, matching the static seal metal. Composition: square 64x64 output canvas; one localized curved highlight at most 14% of canvas width and 10% of height; every other pixel genuinely transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no seal or symbol pixels; stable canvas anchor; no added detail besides this one glint. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, other lights, or any changes to the original seal.
```

## Crisis seal frame 006

Candidate: `crisis_f006`; retained source: `source/imagegen/crisis/frame_006_falling_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-04944815-60fc-4c68-9e8b-553c76cf59b2.png`.

Reference image 1 was `source/existing_png/crisis_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the antique dark-bronze outer ring; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint. Primary request: Create one standalone transparent glint layer for frame 006. Place a very small, dim reflection near the upper-right arc of the seal's outer ring, centered around 65% of canvas width and 23% of its height. This is the pulse's falling phase, weaker and shorter than frame 005. Style/medium: restrained hand-painted antique-brass reflection with a dim pale-gold point and muted amber edge, matching the static seal. Composition: square 64x64 output canvas; one localized curved highlight at most 11% of width by 8% of height, with only a tight soft edge; everything else transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no seal or symbol pixels; stable canvas anchor; no added detail except one fading glint. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, additional light sources, or changes to the original seal.
```

## Rat King readiness frame 003

Candidate: `readiness_f003`; retained source: `source/imagegen/readiness/frame_003_peak_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-89041711-594d-4691-80ce-6f9d0dc0d8dd.png`.

Reference image 1 was `source/existing_png/readiness_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter the seal. Image 2 is only a material reference for the generated warm-metal glint. Primary request: Create one standalone transparent glint layer for frame 003. It is the brightest part of a restrained pulse across the upper-right crown edge, slightly longer and clearer than frame 002, centered near 71% of canvas width and 24% of height. Style/medium: hand-painted subdued antique-brass light with a tiny pale gold core and brown-gold edge, matching the static dark metal. Composition: square 64x64 output canvas; one localized highlight no larger than 17% of canvas width by 12% of its height; all remaining canvas genuinely transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no emblem or seal pixels; stable canvas anchor; no additional object. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, extra lights, or changes to the original seal.
```

## Rat King readiness frame 004

Candidate: `readiness_f004`; retained source: `source/imagegen/readiness/frame_004_falling_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-df93b3bc-c363-46dc-8852-7432a457424a.png`.

Reference image 1 was `source/existing_png/readiness_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter the seal. Image 2 is only a material reference for the generated warm-metal glint. Primary request: Create one standalone transparent glint layer for frame 004, just after the pulse peak. The reflection eases from the crown edge toward the top-right arc and becomes shorter and softer than frame 003, centered near 65% of canvas width and 20% of height. Style/medium: hand-painted subdued antique-brass light with a tiny pale gold core and brown-gold edge, matching the static dark metal. Composition: square 64x64 output canvas; one localized highlight no larger than 14% of canvas width by 10% of its height; all remaining canvas genuinely transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no emblem or seal pixels; stable canvas anchor; no additional object. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, extra lights, or changes to the original seal.
```

## Crisis seal frame 007

Candidate: `crisis_f007`; retained source: `source/imagegen/crisis/frame_007_near_rest_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-54dfb6a1-470b-40d2-b07c-c14a04dbb6ad.png`.

Reference image 1 was `source/existing_png/crisis_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the antique dark-bronze outer ring; do not reproduce or alter the seal. Image 2 is only a material reference for a restrained warm-metal glint. Primary request: Create a barely visible final source glint for frame 007, the near-rest end of a slow loop. Put one tiny, dim warm reflection on the upper-right outer rim, centered near 72% of canvas width and 26% of height, much smaller and fainter than frame 006 so it blends back to the static frame. Style/medium: hand-painted antique brass, extremely restrained pale-gold point with a soft amber edge. Composition: square 64x64 canvas; a single mark no larger than 7% of canvas width by 5% of height; all other area genuinely transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no seal or symbol pixels, fixed anchor. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, other lights, or any change to the seal.
```

## Readiness frame 006 first candidate (rejected)

Candidate: `readiness_f006_rejected_halo`; retained source: `source/imagegen/readiness/rejected/frame_006_circular_halo_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-4e724370-a2d5-4527-b383-3d623b42c808.png`.

Reference image 1 was `source/existing_png/readiness_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter it. Image 2 is only a material reference for the generated warm-metal glint. Primary request: Create one standalone transparent glint layer for frame 006. Draw only a tiny faint gold glint at the upper-right crown rim, centered near 67% of canvas width and 22% of height; it should be visibly dimmer and thinner than the frame 005 glint but still visible at 64x64. Style/medium: subdued hand-painted antique-brass reflection with a soft bronze edge, matching the original dark metal. Composition: square 64x64 canvas; one tiny glint at most 8% of width by 6% of height; all other canvas genuinely transparent. Background: genuine transparent background with native alpha. Constraints: layer only, fixed anchor, no seal pixels or other details. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, any additional light, or changes to the seal.
```

The output was rejected because it formed a circular halo instead of one detached glint, and it was replaced before runtime assembly.

## Readiness frame 005

Candidate: `readiness_f005`; retained source: `source/imagegen/readiness/frame_005_falling_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-d0ac4c88-3f08-443b-9b00-f212f7244251.png`.

Reference image 1 was `source/existing_png/readiness_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter it. Image 2 is only a material reference for the generated warm-metal glint. Primary request: Create one standalone transparent glint layer for frame 005, easing down from the peak. Place one short reflection on the upper-right crown rim near 66% of canvas width and 21% of height; make it smaller and softer than frame 004. Style/medium: hand-painted subdued antique-brass light with a tiny gold core and brown-gold edge, matching the static dark metal. Composition: square 64x64 canvas; one curved highlight no larger than 12% of width by 8% of height, rest fully transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no emblem or seal pixels; stable anchor. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, extra lights, or changes to the original seal.
```

## Readiness frame 007

Candidate: `readiness_f007`; retained source: `source/imagegen/readiness/frame_007_near_rest_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-dde5513f-0d50-4f55-9e09-e8b8fd9dd63c.png`.

Reference image 1 was `source/existing_png/readiness_static.png`; reference image 2 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`.

```text
Use case: stylized-concept. Asset type: one source layer for a Hearts of Iron IV animated symbolic rat-king readiness seal, composited over an immutable 64x64 static seal. Input images: Image 1 is only a color and geometry reference for the original dark bronze-and-steel seal; do not reproduce or alter it. Image 2 is only a material reference for the generated warm-metal glint. Primary request: Create the final near-rest source layer for frame 007. Show a hairline-faint antique-gold reflection on the upper-right crown rim, nearly gone as the loop returns to the unchanged static frame. Keep it centered near 67% of canvas width and 22% of height, smaller and fainter than frame 006. Style/medium: very restrained painted metallic glint with native alpha. Composition: square 64x64 canvas; one tiny glint no larger than 6% of width by 4% of height; every other pixel transparent. Background: genuine transparent background with native alpha. Constraints: layer only, no seal pixels, no new marks, fixed anchor. Avoid: opaque background, checkerboard, matte, broad halo, sparks, particles, lens flare, text, watermark, border, extra lights, or changes to the seal.
```

## Readiness frame 006 replacement

Candidate: `readiness_f006`; retained source: `source/imagegen/readiness/frame_006_faint_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-7eedaa04-79d1-431a-941e-f1b055246c23.png`.

Reference image 1 was `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png`, used as a style reference only; the readiness seed was not supplied so the model could not re-create a circular seal.

```text
Use case: stylized-concept.
Asset type: a standalone transparent reflection layer for frame 006 of a tiny 64x64 Hearts of Iron IV readiness-seal animation.
Input image: Image 1 is only a style reference for an antique-brass glint. Transfer only the painted metal material and narrow highlight character; do not copy its location or large size.
Primary request: Create a fresh, very faint, narrow diagonal gold reflection mark near the upper-right, about 67% of canvas width and 22% of height. This is a restrained falling pulse, visibly dimmer and shorter than a peak highlight, but still legible when reduced to 64x64.
Style/medium: subdued hand-painted antique brass, a small pale-gold center and muted brown edge.
Composition: exact square 64x64 canvas; only one small curved glint, at most 7% of canvas width and 5% of its height; tight soft edge, no wider glow.
Background: genuine transparent background with native alpha.
Constraints: standalone layer that will be composited over the unmodified dark readiness seal; no part of that seal should appear in this image.
Avoid: any circle, disk, ring, coin, seal, medallion, emblem, animal, skull, background object, shadow, full-canvas scene, sparks, particles, broad glow, lens flare, checkerboard, matte, text, watermark, border, or second mark.
```

## Superseded prior source request

The superseded crisis frame-001 overlay `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png` and the prior full-seal drift source were created before this task resumed; their original ImageGen prompt records were not present in the named asset package and are not reconstructed here.

## Crisis seal frame 001 refresh

Candidate: `crisis_f001_refresh`; retained source: `source/imagegen/crisis/frame_001_fresh_upper_left_glint_raw.png`; tool output: `C:\Users\klimp\.codex\generated_images\01a10fb9-2576-7140-a001-48eced951570\exec-8998aee3-7d88-45fa-b168-53a0f0ce61aa.png`.

The exact request arguments, including `transparent_background: true`, both absolute `referenced_image_paths`, and the full prompt text, were saved before generation in `source/imagegen/requests/crisis_frame_001.json`.

Image 1 was the immutable `source/existing_png/crisis_static.png` seed; Image 2 was the superseded carry-forward glint layer used only for style and placement.

The selected frame is `animations/crisis_seal/processed_frames/frame_001.png`, and the selected sheet consumer is `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_sheet.dds`.
