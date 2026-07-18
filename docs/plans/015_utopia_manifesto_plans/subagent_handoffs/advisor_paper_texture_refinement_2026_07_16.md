# Advisor paper texture refinement handoff — 2026-07-16

## Status

`exec-a4228463-4201-499a-b1e4-aafb79d7b987` is the best clean noncanonical ImageGen candidate from this pass. It is retained for parent review only.

- It is **not approved**.
- It is **not canonical** and does not replace the active advisor paper source or overlay.
- It is **not manifest-wired**.
- No gameplay, skill, processor, canonical asset, prompt-record, or manifest file was edited.
- Current processor layer-level geometry and coverage gates pass.
- Current processor layer-level paper palette gate fails narrowly; exact values are recorded below.

## Retained candidate

- ImageGen handle: `exec-a4228463-4201-499a-b1e4-aafb79d7b987`
- Generation route: OpenAI built-in ImageGen, `precise-object-edit`
- Source: `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_texture_refinement_iteration_exec-a4228463-4201-499a-b1e4-aafb79d7b987_source.png`
- Source dimensions: `1254x1254`
- Source SHA-256: `a68cac5f19b2dc81b8d349b51d81092b86a2d0c739a60b18e89d02f33f93b922`
- Transparent overlay: `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_texture_refinement_iteration_exec-a4228463-4201-499a-b1e4-aafb79d7b987_overlay.png`
- Overlay dimensions: `1254x1254`
- Overlay SHA-256: `4c6ff6274020f24b3ff73b085ba02963737eea26aa988bff31a0b562ab07e7eb`

Rejected refinement attempts were removed from the repository working tree. Their generated-image-store copies were not used as retained project assets.

## Generation inputs

1. Edit target and geometry/palette authority:
   `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_texture_iteration_exec-184ae8ce_source.png`
   
   SHA-256: `530ca1e7eeb24001efecf939f001aa0ba14159ae6e789422b6260b357669538b`
2. Frozen vanilla style-reference contact sheet:
   `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/vanilla_advisor_contact_sheet_imagegen_reference_b26a3d57.png`
   
   SHA-256: `b26a3d57cf1579bbe2c2862ab63c1040b6a0e947ad197ae4f6afbd661930bac6`

The contact sheet was used only as a paper-treatment reference. No visible vanilla portrait, frame, symbol, or RGB artwork was copied into the candidate.

## Exact ImageGen prompt

```text
Use case: precise-object-edit
Asset type: full-resolution source for a Hearts of Iron IV advisor dossier paper overlay, later chroma-keyed and reduced to 25x30 pixels
Input images: Image 1 is the sole edit target and strict authority for the warm pale-cream paper base, canvas, size, centering, proportions, silhouette, ragged edge contour, opacity, and fiber material. Image 2 is a frozen vanilla advisor contact sheet used only as a style reference for the tiny cream dossier-paper slips—do not copy any portrait, person, frame, symbol, or other visible content from Image 2.
Primary request: Starting directly from Image 1, refine only its low-frequency authored paper surface. Add or strengthen exactly 2–3 broad irregular warm gray-beige stain/fiber-cloud patches with soft uneven boundaries. Each cloud must be pale and restrained—only about 5–8 percent darker than the immediately surrounding paper—yet broad enough to remain visible after the sheet is reduced to 25x30 pixels.
Upper-third marks: retain/refine exactly 2–3 compact neutral-gray illegible dossier-mark clusters in the upper third. They must be abstract blurred archival marks, not readable characters, with enough neutral-gray contrast to remain visible at 25x30.
Strict base-color invariant: outside the new broad clouds and compact mark clusters, preserve the exact warm pale-cream yellow-beige base hue, saturation, brightness, and existing fiber texture of Image 1. Do not globally recolor, cool, whiten, pinken, desaturate, darken, or brighten the paper.
Scene/backdrop: preserve the perfectly flat, uniform pure #00FF00 chroma-green isolation background across the full canvas, edge to edge.
Composition/framing invariants: preserve the exact canvas size and exact same single tall upright paper sheet from Image 1. Keep its exact scale, position, centering, proportions, silhouette, ragged edge contour, upright orientation, opacity, continuous material, and generous green clearance.
Lighting: flat shadowless asset isolation; no cast shadow, contact shadow, glow, halo, rim light, gradient, or lighting change.
Constraints: change only the broad low-frequency clouds and compact upper-third dossier-mark clusters. Keep exactly one continuous visually opaque sheet. Keep clean separation from the green background with no green spill.
Avoid: global paper recoloring, cool gray paper, blue cast, pink cast, white paper, dark brown stains, orange stains, high-frequency noise, micro-speckle, dense grain, readable text, letters, words, numbers, signatures, recognizable symbols, seals, stamps, orange ink, red ink, colored ink, borders, clips, pins, frames, folds, holes, additional tears, other objects, duplicate paper sheets, transparency, green contamination on the paper, watermark.
```

## Alpha extraction

The repository event-assets folder has no separate chroma-extraction utility. The installed ImageGen helper used by the current canonical overlay provenance was used instead:

- Tool: `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py`
- Tool SHA-256: `7e51236919203b61d07ddffdc6e0b5f501a28661003f5851f26ffbb64bdec1ea`
- Tool version: unversioned; content hash pinned
- Processing: chroma-key alpha extraction, soft matte, and despill only; no visible paper RGB was drawn, repaired, recoloured, relit, or retouched locally

Invocation:

```powershell
python -B C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py `
	--input .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_texture_refinement_iteration_exec-a4228463-4201-499a-b1e4-aafb79d7b987_source.png `
	--out .agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_paper_shadowless_texture_refinement_iteration_exec-a4228463-4201-499a-b1e4-aafb79d7b987_overlay.png `
	--auto-key border --soft-matte `
	--transparent-threshold 12 --opaque-threshold 220 `
	--despill --force
```

Extraction output:

- Sampled key colour: `#06f705`
- Transparent pixels: `1,154,711 / 1,572,516`
- Partially transparent pixels: `3,004 / 1,572,516`
- Alpha extrema: `[0, 255]`
- Principal alpha component count above `32`: `1`
- Principal component area above `32`: `416,939`
- Visible source/overlay mean RGB delta above alpha `128`: `0.0172`
- Interior paper support is fully opaque after extraction; no keyed holes or detached visible components were found.

ImageGen was prompted for literal `#00FF00`; the emitted raster's border sampler resolved `#06f705`. The source therefore should not be described as byte-uniform `#00FF00`, although the isolation field keyed cleanly and no green spill remained in the retained overlay.

## Geometry and reduction evidence

Source-master comparison against the input overlay at alpha greater than `32`:

- Input visible bbox: `[375, 181, 882, 1033]`
- Candidate visible bbox: `[375, 180, 881, 1033]`
- Candidate/input mask IoU: `0.9974206145062917`

The ImageGen source is therefore not pixel-identical to the input silhouette: the visible master bbox differs by one pixel at the top and right. After the processor's pinned trim, resize, and rotation, the layer normalizes to the required native geometry:

- Native bbox above alpha `32`: `[30, 26, 57, 58]`
- Width/height: `27x32`
- Area above alpha `32`: `750`
- Center: `[43.0, 41.5]`
- Top-edge image slope: `0.076623`
- Top-edge image angle: `4.381634°`
- Native alpha coverage above `32`: `0.17221584385763491` — within the required `0.163–0.175` range

At the ungraded `25x30` reduction, the authored marks and broad clouds remain visible:

- Candidate luminance mean: `205.652`
- Candidate luminance standard deviation: `9.060`
- Candidate p05/p95: `190.468 / 216.736`
- Candidate p05–p95 span: `26.267`
- Input luminance standard deviation: `8.382`

## Current processor layer-level palette gate

The candidate does **not** pass the current palette gate. Exact post-normalization/post-grade metrics:

- Mean luminance: `203.963234` — fails the required `204–214` range by `0.036766`
- Mean saturation: `0.220003` — passes the required `0.190–0.245` range
- Mean RGB: `[225.568, 200.494667, 175.968]`
  - Red: passes `220–231`
  - Green: fails `202–213` by `1.505333`
  - Blue: passes `171–183`
- Red minus green: `25.073333` — fails the required `12–24` range by `1.073333`
- Green minus blue: `24.526667` — passes the required `24–38` range

No processor, grading constant, proxy, canonical source, canonical overlay, or manifest was changed to make this candidate pass. Parent review must decide whether to keep it as rejected iteration history, recalibrate the separate composite work, or request a future authored regeneration.

## Producer boundary

Producer: `/root/advisor_paper_texture_refinement`

The producer does not approve this candidate and does not recommend canonical replacement while the current layer-level palette gate remains failed. Independent parent review is still required for any later promotion.
