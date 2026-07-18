# Fallout World End UI Asset Manifest

## Package scope

This package contains only the dedicated Fallout blackout tile and the dedicated Fallout state-grade modifier icon requested for the transition UI. Both sprites are registered in `interface/fallout_world_end.gfx` and referenced by their dedicated Fallout consumers.

Package status: `registered_and_referenced_runtime_gui_pending`

Reference review:

- the required offline Paradox wiki core pages
- offline Interface modding and Scripted GUI modding pages
- the vanilla idea-picture sprite convention
- the vanilla `10x10` black UI tile precedent
- the Chaos Redux idea-icon reference set in `.agents/skills/chaos-redux-event-assets/assets/ideas/`

## Asset 1: Fallout blackout tile

- Asset name: Fallout blackout tile
- Related system: Fallout world-end transition
- Asset type: functional full-screen UI texture
- Intended in-game use: opaque black texture for the independent full-screen blackout layer
- Source mode: deterministic local utility texture created from the user-specified solid black requirement
- Source PNG path: not retained because the requested deliverable is the DDS utility tile only
- Processed PNG path: not retained because the requested deliverable is the DDS utility tile only
- Final DDS path: `gfx/interface/fallout_world_end/fallout_blackout_tile.dds`
- Target size: `10x10`
- Registered sprite name: `GFX_fallout_blackout_tile`
- Suggested `.gfx` file: `interface/fallout_world_end.gfx`
- Localisation key: not needed
- Source note: a temporary `10x10` RGBA raster with pixel value `(0, 0, 0, 255)` was converted through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and removed after conversion
- DDS format: legacy one-level uncompressed 32-bit BGRA, equivalent to `B8G8R8A8`, with no mipmaps
- Alpha result: all `100` pixels have alpha `255`
- Asset status: `registered_and_referenced_runtime_gui_pending`

## Asset 2: Fallout state-grade modifier icon

- Asset name: Fallout state-grade modifier icon
- Related system: Fallout state grading
- Asset type: idea-style state modifier icon
- Intended in-game use: shared 64x64 visual for Fallout state-grade status presentation
- Source mode: `$imagegen`
- Generation route: Codex built-in image generation tool
- Model record: the built-in tool did not expose a model identifier
- Source PNG path: `docs/assets/fallout_world_end/source_png/idea_fallout_state_grade_source.png`
- Processed PNG path: `docs/assets/fallout_world_end/processed_png/idea_fallout_state_grade.png`
- Final DDS path: `gfx/interface/ideas/fallout_world_end/idea_fallout_state_grade.dds`
- Contact sheet: `docs/assets/fallout_world_end/contact_sheets/fallout_ui_asset_contact_sheet.png`
- Source size: `1254x1254`
- Target size: `64x64`
- Registered sprite name: `GFX_idea_fallout_state_grade`
- Suggested `.gfx` file: `interface/fallout_world_end.gfx`
- Localisation key: not needed for the asset itself
- Source rationale: Fallout is fictional and symbolic, so original generated artwork fits better than a historical source image
- Asset status: `registered_and_referenced`

### Image generation prompt

```text
Use case: stylized-concept
Asset type: original 64x64 Hearts of Iron IV state-modifier icon source artwork
Primary request: create one compact symbolic icon showing a cracked hardened shelter emerging from heavy ash beneath a cold, ruined sky
Scene/backdrop: a perfectly flat solid #00ff00 chroma-key background for later background removal, with no gradient, texture, shadow, floor plane, or lighting variation in the background
Subject: one centered, thick-silhouette concrete shelter entrance or low bunker arch, visibly fractured by one bold crack, ash drifts banked across its base, and a narrow cold blue-grey sky arc contained behind and around the shelter as part of the painted subject
Style/medium: original hand-painted HOI4 national-spirit icon art, aged mid-20th-century wartime illustration, compact painterly brushwork, dark outline, restrained subtle drop shadow, no modern glossy rendering
Composition/framing: square icon, centered single emblem, generous clear padding, bold readable forms designed to survive reduction to 64x64, no border or medallion frame
Lighting/mood: dim polar light, bleak and severe, cold blue highlights against charcoal concrete and pale ash
Color palette: charcoal black, concrete grey, bone ash, muted steel blue, tiny restrained rust-brown accents, absolutely no green in the subject
Materials/textures: cracked concrete, powdery ash, wind-scoured cold sky
Constraints: the subject must be fully separated from the flat chroma background with crisp edges, unused canvas must remain only the uniform key color, no cast shadow on the background, no contact shadow on the background, no text, no letters, no numbers, no watermark, no flags, no people, no skulls, no radiation trefoil, no biohazard mark, no flames, no weapons, no fake checkerboard, no white sticker rim, no glow halo, no opaque square backdrop
Avoid: photorealism, 3D render, cartoon style, modern survival-game UI, tiny interior detail, generic circular badge, source imagery from any existing franchise
```

### Processing record

1. Sampled the generated border key as `#07f907`.
2. Removed the key with the installed imagegen helper using border auto-keying, soft matte, despill, transparent threshold `12`, opaque threshold `220`, and edge contraction `1`.
3. Cropped the alpha bounds from `(69, 143)` to `(1187, 1116)`.
4. Reduced the subject to `60x52` with Lanczos resampling.
5. Applied restrained readability corrections of contrast `1.10`, brightness `1.06`, and sharpness `1.35`.
6. Centered the subject at offset `(2, 6)` on a transparent `64x64` canvas.
7. Converted the processed PNG through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` without resizing beyond the `64x64` target.

### Format and visual validation

- Processed PNG alpha range: `0` through `255`
- Processed PNG transparent pixels: `1507`
- Processed PNG partially transparent pixels: `524`
- Processed PNG fully opaque pixels: `2065`
- Decoded DDS pixels match the processed PNG exactly
- DDS format: legacy one-level uncompressed 32-bit BGRA, equivalent to `B8G8R8A8`, with no mipmaps
- DDS file length: `16512` bytes, matching `128 + 64 * 64 * 4`
- The icon remains readable at `64x64`
- The unused canvas is transparent
- The final edge has no visible green fringe, white matte, sticker rim, or opaque square background
- The contact sheet shows the generated source, processed transparency, decoded DDS, and blackout tile

## Provenance and rights note

The modifier icon is original fictional artwork created with the Codex built-in image generation tool for this package. It uses no external source image, real-person likeness, logo, franchise artwork, or generated text. The blackout tile is a deterministic functional texture specified by the user.

## Risks and remaining wiring

- `GFX_fallout_blackout_tile` is referenced by `interface/fallout_world_end.gui`. Structural all-resolution binding, drawing order, and input blocking remain unresolved engine-sensitive GUI work.
- `GFX_idea_fallout_state_grade` is referenced by all seven Fallout grade dynamic modifiers.
- The literal full-screen draw order and input-blocking behavior remain properties of the future `.gui` and scripted GUI implementation. The tile itself is fully opaque and suitable for that layer.
- The icon is a shared state-grade visual. If distinct grade-specific icons are later required, they need separate source artwork and separate manifest entries.

## Audio package

The dedicated Fallout blackout cue, license evidence, processing record, wrappers, and distribution credit are documented in `audio_manifest.md` and `CREDITS.md`.
