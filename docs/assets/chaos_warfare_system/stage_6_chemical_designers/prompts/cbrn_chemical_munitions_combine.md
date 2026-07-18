# cbrn_chemical_munitions_combine

Source mode: `$imagegen` built-in generation, independent source render.

```text
Use case: logo-brand
Asset type: Hearts of Iron IV Chaos Redux Stage 6 MIO designer idea icon, intended for a compact 64x64 manufacturer slot.
Primary request: a restrained 1930s-1940s industrial institution emblem for a fictional generic chemical munitions combine. Combine one clear capped chemical shell or shell-filling carousel with a sealed reagent canister and a heavy factory gear, arranged as one compact heraldic mechanical silhouette. The emblem should read instantly at tiny game size as a chemical-munitions manufacturing organization, with no text.
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background only, no gradients, texture, shadow, floor, reflection, vignette, or border in the background.
Subject: centered, front-facing or slight three-quarter emblem; capped shell and sealed canister nested inside or in front of a heavy gear, with a restrained shell-filling carousel suggestion; keep the silhouette bold and uncluttered.
Style/medium: hand-painted HOI4-style idea icon, period industrial insignia, aged enamel and brushed metal, compact circular manufacturer-slot readability, crisp dark charcoal outline and subtle internal shading, not a modern logo and not vector-flat.
Composition/framing: single central emblem, generous padding, roughly 78% canvas coverage, no separate objects drifting apart, no circular painted backdrop beyond the emblem's own gear/shell forms.
Lighting/mood: sober institutional, low-key workshop lighting translated into strong readable highlights and shadows.
Color palette: amber brass, oxidized steel, muted olive, charcoal outline, restrained warm highlights.
Materials/textures: worn brass, oxidized steel, enamel, small period machining marks; preserve readable silhouette at 64x64.
Text (verbatim): ""
Constraints: create the requested subject as a real generated raster source image; the #00ff00 background must be perfectly uniform and must not appear in the subject; keep the emblem isolated and fully inside the canvas; no cast shadow, no white halo, no white outline, no sticker border, no watermark.
Avoid: any text or letters, national flag, company logo, national emblem, skull, modern biohazard symbol, radiation trefoil, medical cross, contemporary PPE, generic bomb-lock icon, UI labels, frame, checkerboard, gradient background, opaque non-green square background.
```

Processing record: source PNG preserved at native generated size, green chroma removed with `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` using border auto-key, soft matte, despill, and thresholds 12/220; final preview resized to 64x64 with FFmpeg Lanczos RGBA encoding; DDS converted with the repository `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` workflow.
