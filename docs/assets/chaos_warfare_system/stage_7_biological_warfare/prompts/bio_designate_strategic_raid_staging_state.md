# Prompt and source record

## Asset

- Stable id: `bio_designate_strategic_raid_staging_state`
- Asset type: HOI4 decision icon
- Final size: `32x32`
- Generation mode: official built-in `$imagegen` workflow
- Transparency workflow: flat `#00ff00` chroma-key source, local `remove_chroma_key.py`, then exact-size RGBA processing

## Reference folder inspected

`.agents/skills/chaos-redux-event-assets/assets/decisions/`

Representative references inspected included `decision_usa_congress.png`, `decision_tungsten.png`, `decision_generic_intelligence_operation.png`, `decision_border_war.png`, and `decisions_generic_counter_infiltration_3.png`.

## Final generation prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV decision icon, final readability at 32x32
Primary request: a bespoke compact decision-icon composition showing a sealed containment canister being transferred beneath an air-base hangar roof with a small aircraft silhouette above it; the canister is the clear central subject, with a distinct locked staging marker integrated into the scene so it reads as controlled, secured preparation
Scene/backdrop: a dark shadowed air-base hangar interior, simplified into a few strong structural beams and a low aircraft underside silhouette; no map, no interface frame
Subject: one heavy sealed industrial containment canister with clamps, tamper seals, and a small padlock marker, being moved on a low transfer trolley beneath the hangar; no people needed
Style/medium: painterly HOI4-style game icon art, aged military texture, compact illustrative rendering, strong silhouette and clean edges, designed specifically as a decision icon and not as a focus or idea icon
Composition/framing: square icon composition, central canister occupying most of the readable area, aircraft and hangar silhouette as secondary context in the upper band, locked staging marker visibly attached to or immediately beside the canister; simple symbolic grouping, no tiny props that disappear at 32x32
Lighting/mood: restrained ominous operational mood, directional overhead hangar light, deep charcoal shadows, controlled highlight on the canister and lock
Color palette: charcoal black, gunmetal grey, muted desaturated teal, restrained amber accents on the sealed container and lock marker; no bright neon green
Materials/textures: worn painted metal, rivets, sealed seams, subtle industrial grime, lightly aged painterly grain
Text (verbatim): none
Constraints: create the subject on a perfectly flat solid #00ff00 chroma-key background for background removal; background must be one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation; keep the subject fully separated from the background with crisp edges and generous padding; do not use #00ff00 anywhere in the subject; no cast shadow, no contact shadow, no reflection; real transparency will be created locally after generation
Avoid: gore, blood, exposed material, casualties, medical imagery, generic biohazard-only symbol, generic hazard triangle as the main subject, empty canister, open container, vapor, cloud, gas, explosion, flames, missiles, target reticles, maps, arrows, text, labels, watermark, UI panel, sticker border, white outline, white halo, fake checkerboard, flat vector-only geometry, generic stock icon, resized cross-type substitute
```

## Generation and processing record

1. The source was generated as a bespoke fictional containment-transfer scene with the aircraft/hangar context and lock marker requested by the parent prompt.
2. The generated PNG was preserved unchanged under `source_png/`.
3. The flat chroma-key background was removed with the installed `remove_chroma_key.py` helper using border auto-keying, soft matte, thresholded transparency, and despill.
4. The transparent cutout was square-cropped around its alpha bounds, padded, and resized with Lanczos to exactly `32x32` RGBA.
5. The processed PNG was converted to the required final DDS with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

The source prompt intentionally uses fictional sealed-containment terminology for image generation while the asset id, package, manifest, and handoff preserve the Stage 7 biological-warfare role.
