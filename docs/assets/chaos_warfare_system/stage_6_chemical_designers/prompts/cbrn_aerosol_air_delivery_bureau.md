# cbrn_aerosol_air_delivery_bureau

Source mode: `$imagegen` built-in generation, independent source render.

```text
Use case: logo-brand
Asset type: Hearts of Iron IV Chaos Redux Stage 6 MIO designer idea icon, intended for a compact 64x64 manufacturer slot.
Primary request: a restrained 1930s-1940s technical bureau emblem for a fictional generic aerosol air-delivery organization. Combine one winged sealed dispersal rack with a precision manifold/nozzle and a controlled fan of aerosol, arranged as one compact heraldic technical silhouette. The emblem should read instantly at tiny game size as a specialized aerial dispersal engineering bureau, with no text.
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background only, no gradients, texture, shadow, floor, reflection, vignette, or border in the background.
Subject: centered, front-facing technical emblem; a sealed rack or cartridge body as the core, small stylized wings integrated into the sides, a precise manifold/nozzle beneath, and a restrained controlled aerosol fan represented by a few distinct pale vapor blades; keep the silhouette bold and uncluttered.
Style/medium: hand-painted HOI4-style idea icon, period industrial technical insignia, aged enamel and brushed metal, compact circular manufacturer-slot readability, crisp dark charcoal outline and subtle internal shading, not modern aerospace branding and not vector-flat.
Composition/framing: single central emblem, generous padding, roughly 78% canvas coverage, no separate objects drifting apart, no circular painted backdrop beyond the emblem's own metal forms.
Lighting/mood: sober institutional, precise and controlled, low-key workshop lighting translated into strong readable highlights and shadows.
Color palette: slate blue, brass, muted silver, charcoal outline, restrained cool highlights.
Materials/textures: worn brass fittings, slate-painted steel, muted silver nozzle and vapor, small period machining marks; preserve readable silhouette at 64x64.
Text (verbatim): ""
Constraints: create the requested subject as a real generated raster source image; the #00ff00 background must be perfectly uniform and must not appear in the subject; keep the emblem isolated and fully inside the canvas; no cast shadow, no white halo, no white outline, no sticker border, no watermark.
Avoid: any text or letters, national flag, company logo, national emblem, skull, generic reused bomb-lock art, generic bomb silhouette, generic explosion, modern biohazard symbol, radiation trefoil, medical cross, contemporary aircraft, UI labels, frame, checkerboard, gradient background, opaque non-green square background.
```

Processing record: source PNG preserved at native generated size, green chroma removed with `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` using border auto-key, soft matte, despill, and thresholds 12/220; final preview resized to 64x64 with FFmpeg Lanczos RGBA encoding; DDS converted with the repository `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` workflow.
