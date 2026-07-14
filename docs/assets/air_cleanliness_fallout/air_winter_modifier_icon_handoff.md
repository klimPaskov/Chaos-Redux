# Air Winter State Modifier Icon Handoff

Status: asset production complete and ready for main-agent wiring.

This handoff covers seven original Fallout and Air Winter state dynamic-modifier icons. It does not edit the existing asset manifest, `.gfx` files, gameplay, localisation, specifications, or audio.

## Package inventory

| Asset | Stable sprite | Visual identity | Source PNG | Processed PNG | Final DDS |
| --- | --- | --- | --- | --- | --- |
| Air Winter phase 1 | `GFX_air_winter_phase_1` | Dim frost | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_phase_1_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_phase_1.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_1.dds` |
| Air Winter phase 2 | `GFX_air_winter_phase_2` | Failed season and crop shock | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_phase_2_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_phase_2.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_2.dds` |
| Air Winter phase 3 | `GFX_air_winter_phase_3` | Hard freeze and infrastructure winter | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_phase_3_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_phase_3.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_3.dds` |
| Air Winter phase 4 | `GFX_air_winter_phase_4` | Black harvest | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_phase_4_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_phase_4.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_4.dds` |
| Air Winter phase 5 | `GFX_air_winter_phase_5` | Ash winter and dead sky | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_phase_5_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_phase_5.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_5.dds` |
| Air Winter phase 6 | `GFX_air_winter_phase_6` | Terminal fallout night | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_phase_6_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_phase_6.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_6.dds` |
| Air Winter disease pressure | `GFX_air_winter_disease_pressure_state` | Winter disease and exposure medical mark | `docs/assets/air_cleanliness_fallout/source_png/modifiers/air_winter_disease_pressure_state_source.png` | `docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_disease_pressure_state.png` | `gfx/interface/air_cleanliness_winter/modifiers/air_winter_disease_pressure_state.dds` |

Review contact sheet:

`docs/assets/air_cleanliness_fallout/processed_png/modifiers/air_winter_modifier_icons_contact_sheet.png`

## Dimensions and formats

- Source mode: built-in `$imagegen` using the `stylized-concept` taxonomy.
- Source PNGs: 1254x1254 RGB PNGs with a model-rendered flat magenta chroma field prompted as `#ff00ff`.
- Processed PNGs: 32x32 RGBA PNGs with transparent unused canvas.
- Final DDS files: 32x32, one image level, uncompressed 32-bit BGRA or B8G8R8A8, 128-byte pitch, canonical masks `00FF0000`, `0000FF00`, `000000FF`, and `FF000000`.
- Final DDS byte size: 4,224 bytes per icon.
- Contact sheet: 1040x500 RGB PNG with each accepted 32x32 icon shown at 5x scale over a checker field.

The 32x32 target follows the vanilla state dynamic-modifier precedent in `common/dynamic_modifiers/GoE_dynamic_modifiers.txt`, `interface/countrystateview.gfx`, and `gfx/interface/state_modifiers/modifiers_RAJ_famine_state.dds`. The wider idea-icon family was reviewed for painted language, but the final canvas follows the state-modifier surface rather than the national-spirit surface.

## Processing record

The installed image generation chroma-removal helper was used with border auto-key sampling, soft matte, threshold values 12 and 220, and despill. The model rendered near-magenta border colors rather than byte-exact `#ff00ff`, so border sampling was retained as required by the official image generation workflow.

Phase 3 showed a one-pixel magenta edge during the first alpha review. It was processed again with `--edge-contract 1`. The second cutout removed the fringe without clipping the pole, wires, rails, or icicles.

After alpha review, each icon received an individually selected crop, mild identity-specific grading, Lanczos reduction, a restrained final-size sharpen, and a subtle one-pixel black shadow. The source artwork already carried a painted dark outline, so no white or colored sticker rim was added.

| Asset | Manual crop box | Brightness | Contrast | Colour | Final fitted subject |
| --- | --- | ---: | ---: | ---: | --- |
| Phase 1 | `199,129,1017,1105` | 0.82 | 1.08 | 0.75 | 25x30 |
| Phase 2 | `274,143,1012,1114` | 0.92 | 1.10 | 0.92 | 23x30 |
| Phase 3 | `177,137,1072,1097` | 0.88 | 1.08 | 0.85 | 28x30 |
| Phase 4 | `260,117,1033,1105` | 0.82 | 1.12 | 0.65 | 23x30 |
| Phase 5 | `223,91,1017,1127` | 0.82 | 1.15 | 0.50 | 23x30 |
| Phase 6 | `176,152,1078,1079` | 0.86 | 1.12 | 0.80 | 29x30 |
| Disease pressure | `248,155,1007,1062` | 0.90 | 1.08 | 0.75 | 25x30 |

DDS conversion used `.tools/convert_to_dds.py` with the approved DirectXTex May 2026 backend at `C:/Users/klimp/AppData/Local/Temp/chaos_redux_tools/texconv-may2026.exe`.

Approved backend SHA-256:

`dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06`

## Prompt provenance

Phase 1 used no input image. Phase 2 through phase 6 and the disease mark used phase 1 only as an internal style reference for outline weight, paint texture, value contrast, padding, and chroma presentation. Every later prompt explicitly prohibited reuse of the phase 1 subject and required a new composition.

### Phase 1 prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Primary request: Create an original symbolic icon for the dim frost opening phase of a post-nuclear Air Winter. Show one frost-coated bare twig crossed in front of a small dim pale sun disc. The image must communicate the first weak cold settling over the land, not a blizzard.
Style/medium: compact painted grand-strategy UI icon, aged 1940s poster and engraved metal character, restrained painterly texture, original artwork
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels
Color palette: icy pale blue, muted steel, charcoal, a tiny touch of desaturated amber in the sun
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. No cast shadow, no contact shadow, no glow, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, skulls, maps, flags, arrows, radiation trefoils, complex scenery, photorealism, modern UI, white sticker outlines.
```

### Phase 2 prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Input images: Image 1 is a style reference for outline weight, painted texture, value contrast, padding, and chroma-key presentation only. Do not reuse its twig or sun composition.
Primary request: Create an original symbolic icon for the failed season and crop-shock phase of a post-nuclear Air Winter. Show one snapped wheat stalk with a broken seed head gripped by two hard frost shards. The image must communicate the first harvest failure and sudden crop death.
Style/medium: match Image 1's compact painted grand-strategy UI icon language, aged 1940s poster and engraved metal character, original subject and composition
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels
Color palette: dead straw gold, cold white, icy blue, charcoal, no living green
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. No cast shadow, no contact shadow, no glow, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, skulls, maps, flags, arrows, radiation trefoils, sickles, harvest baskets, complex scenery, photorealism, modern UI, white sticker outlines.
```

### Phase 3 prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Input images: Image 1 is a style reference for outline weight, painted texture, value contrast, padding, and chroma-key presentation only. Do not reuse its twig or sun composition.
Primary request: Create an original symbolic icon for the hard freeze and infrastructure-winter phase of a post-nuclear Air Winter. Show a short broken iron railway section and one bent telegraph pole locked together inside thick angular blue ice. The image must communicate transport and utility systems seized by severe cold.
Style/medium: match Image 1's compact painted grand-strategy UI icon language, aged 1940s poster and engraved metal character, original subject and composition
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels
Color palette: dark iron, cold blue ice, dirty white frost, muted rust accents
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. No cast shadow, no contact shadow, no glow, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, skulls, maps, flags, arrows, radiation trefoils, wheat, trees, city skylines, complex scenery, photorealism, modern UI, white sticker outlines.
```

### Phase 4 prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Input images: Image 1 is a style reference for outline weight, painted texture, value contrast, padding, and chroma-key presentation only. Do not reuse its twig or sun composition.
Primary request: Create an original symbolic icon for the Black Harvest phase of a post-nuclear Air Winter. Show a compact bound sheaf of completely charred black grain crossed by one old harvest scythe, with a few dirty frost chips clinging to the stalks. The image must communicate a harvest turned to soot and hunger, distinct from a newly snapped crop.
Style/medium: match Image 1's compact painted grand-strategy UI icon language, aged 1940s poster and engraved metal character, original subject and composition
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels
Color palette: soot black grain, tarnished iron, rust brown, sickly dark ochre, dirty blue-white frost accents
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. No cast shadow, no contact shadow, no glow, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, skulls, maps, flags, arrows, radiation trefoils, hammers, political emblems, intact golden wheat, ice mountains, city skylines, complex scenery, photorealism, modern UI, white sticker outlines.
```

### Phase 5 prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Input images: Image 1 is a style reference for outline weight, painted texture, value contrast, padding, and chroma-key presentation only. Do not reuse its twig composition or warm sun treatment.
Primary request: Create an original symbolic icon for the Ash Winter and dead-sky phase of a post-nuclear Air Winter. Show one upright leafless black tree with visible roots in front of a large pale grey sun disc, with several hard-edged black ash flakes falling around it. The image must communicate a sky choked dead by ash and a landscape without life.
Style/medium: match Image 1's compact painted grand-strategy UI icon language, aged 1940s poster and engraved metal character, original subject and composition
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels
Color palette: soot black, dead grey, cold slate blue, dirty white, no amber and no living green
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. Render ash as distinct opaque flakes, not translucent smoke. No cast shadow, no contact shadow, no glow, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, skulls, maps, flags, arrows, radiation trefoils, wheat, scythes, rails, buildings, smoke clouds, complex scenery, photorealism, modern UI, white sticker outlines.
```

### Phase 6 prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Input images: Image 1 is a style reference for outline weight, painted texture, value contrast, padding, and chroma-key presentation only. Do not reuse its twig composition or pale daylight.
Primary request: Create an original symbolic icon for the terminal Fallout Night phase of a post-nuclear Air Winter. Show a large nearly black eclipsed sun with a thin icy cyan rim above a low jagged silhouette of three frozen ruined buildings. Add one narrow dying red line at the horizon. The image must communicate final darkness, fallout cold, and the end of habitable daylight.
Style/medium: match Image 1's compact painted grand-strategy UI icon language, aged 1940s poster and engraved metal character, original subject and composition
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels. Keep the skyline low and the black sun dominant.
Color palette: near black, midnight navy, cold cyan, dirty ice white, one restrained dark red horizon accent
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. No cast shadow, no contact shadow, no outer glow beyond the painted cyan eclipse rim, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, skulls, maps, flags, arrows, radiation trefoils, wheat, scythes, trees, stars, moon crescents, detailed city scenes, explosions, photorealism, modern UI, white sticker outlines.
```

### Disease pressure prompt

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV state dynamic-modifier UI icon source art
Input images: Image 1 is a style reference for outline weight, painted texture, value contrast, padding, and chroma-key presentation only. Do not reuse its twig or sun composition.
Primary request: Create an original winter disease and exposure medical mark. Show a compact pair of blue-grey lungs coated with sharp frost at the edges, crossed diagonally by one cracked old glass thermometer. Place a small muted ivory medical cross behind the lungs. The image must communicate cold injury, respiratory disease, and exposure pressure without gore.
Style/medium: match Image 1's compact painted grand-strategy UI icon language, aged 1940s medical-poster and engraved metal character, original subject and composition
Composition/framing: one centered emblem, generous padding, bold dark outline, very few large shapes, readable when reduced to 32 by 32 pixels
Color palette: blue-grey lungs, dirty ice white, charcoal, muted ivory, one small dark red thermometer bulb
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local removal
Constraints: background is one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation. Keep the whole emblem fully separated from the background with crisp edges. Do not use #ff00ff anywhere in the emblem. No cast shadow, no contact shadow, no glow, no frame, no border, no opaque square backdrop, no fake checkerboard, no text, no numbers, no watermark.
Avoid: zombies, people, faces, hands, skulls, gore, blood splatter, maps, flags, arrows, radiation trefoils, wheat, trees, buildings, snakes, caduceus symbols, modern hospital UI, photorealism, white sticker outlines.
```

## Manual review notes

| Asset | Accepted visual read | Final-size review |
| --- | --- | --- |
| Phase 1 | Frosted twig against a muted weak sun | Reads as the first dim cold state without implying full crop collapse or terminal darkness |
| Phase 2 | Snapped wheat held between two frost shards | The straw and ice remain distinct at 32x32 and do not reuse the Black Harvest scythe language |
| Phase 3 | Broken rails and a bent utility pole trapped in angular ice | The infrastructure silhouette survives reduction. The alpha edge was corrected after targeted fringe review |
| Phase 4 | Charred grain bundle crossed by a worn scythe | The dark grade and black crop mass clearly separate it from the gold crop-shock phase |
| Phase 5 | Leafless rooted tree before a pale dead sun with hard ash flakes | Reads as dead sky and ash fall without translucent smoke or a generic snowflake emblem |
| Phase 6 | Black eclipsed sun over frozen ruins with a narrow red horizon | The cyan rim, black disc, and low ruin line form the terminal state without a radiation trefoil |
| Disease pressure | Frosted lungs, cracked thermometer, and muted medical cross | Reads as winter respiratory and exposure pressure. It is medically distinct from the six environmental phases and contains no gore |

The accepted processed set has transparent corners, no opaque square backdrops, no visible chroma remnants, no text, no zombie imagery, no copied art, no white sticker rim, and no accidental transparent holes inside the painted forms. The seven processed PNGs contain zero visible magenta-key or green-key pixels. All final DDS files decode pixel-identically to their matching processed PNGs.

## SHA-256 inventory

| Asset | Source PNG SHA-256 | Processed PNG SHA-256 | Final DDS SHA-256 |
| --- | --- | --- | --- |
| Phase 1 | `4470c05544e68596607e2fd6e670ae7718b18709e3ed2a86c188cd22717663c4` | `d2e913b7ab872515d8774b739bcffe8f6be31f6013dca543ab9bc03cbb394710` | `2234b4f737860534b6f77e12483e24dcab29007e5205656f20382cf698618a41` |
| Phase 2 | `ca53e96f62c444d66020609fc1317715873323263638b8be32c0f6ea1d392953` | `cecb3fdaccb89d49c967915ff28da2d6b02549779cffde970d4d535926b163cc` | `6da79c6d3a7e7554c56d8584fe0730ea84a7b574a67535176405a1f7bf10f186` |
| Phase 3 | `5d9fe63ca61c270f38c1fae177ac47f7309e327163268324c6b9dbad0f46ee4d` | `bdfc232b578e56535dfe97640eb7d215e6869b7a46308c9e095bc648a9d515c5` | `f703003024ea529aa062c2c3ab51e392cdbeb1092ba5c3452953dc363684dbf9` |
| Phase 4 | `0bbe9e37dc065636f444c3144591b35643dfa7aea31fe05ce186044d91bc941f` | `650d550d269d09c03864a398c3d0a642473f1b1110c7d1fa3f91a995b2ccddbf` | `3fe8eff6fc19c68c5f398ce7970e0a871b3c1f8c55d522b05dd316a5aed6eb92` |
| Phase 5 | `1d785300208caa50fd57d12b306270a8b678b83194fd9eef0edb4e59061fc916` | `2cf828d85d4634f5645e3c14ad7200ee9016e0a03d61e3f680aa79a62b0be99f` | `dff2944a7829d863b3f6319886fe56d512dfa7d899f6a2fc1712997c61a4baa6` |
| Phase 6 | `6dd9985415045a4d2a8236c96b977b657fa0b429fc7c62e919ab7add9af9300f` | `02c6ef7bdc74354c9c8aa456d7df1be7fdcb5cee0890aec83d841dfc5f852cb9` | `ad88ec5920e4180c17b49a777aad41f1a6bdaabcc97a313547ff1370f8e7d8f5` |
| Disease pressure | `3689240fa1378a0ff3fd2653f662eacdae31d7ccc86f0aff7f328b5247f4e2ce` | `984558d2b69b3a36da890a99c0f204c0f4393b598e44b201ef3a310432cca541` | `e02dabd4945b21a7f1ad454499b364dcc2784fa40b9a042f18d71abbdd48d000` |

Contact sheet SHA-256:

`e0b9694bf5a918ece1fe8c2f08205dac85da8f9f3fde5f5725fe997cd5f87a0b`

## Ready-to-copy sprite registration

Suggested target file: `interface/air_cleanliness_winter.gfx`.

The target file was not created or edited by this asset-only task.

```text
spriteTypes = {
	spriteType = {
		name = "GFX_air_winter_phase_1"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_1.dds"
	}
	spriteType = {
		name = "GFX_air_winter_phase_2"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_2.dds"
	}
	spriteType = {
		name = "GFX_air_winter_phase_3"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_3.dds"
	}
	spriteType = {
		name = "GFX_air_winter_phase_4"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_4.dds"
	}
	spriteType = {
		name = "GFX_air_winter_phase_5"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_5.dds"
	}
	spriteType = {
		name = "GFX_air_winter_phase_6"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_phase_6.dds"
	}
	spriteType = {
		name = "GFX_air_winter_disease_pressure_state"
		texturefile = "gfx/interface/air_cleanliness_winter/modifiers/air_winter_disease_pressure_state.dds"
	}
}
```

## Dynamic-modifier icon mapping

| Existing dynamic modifier block | Icon line to add |
| --- | --- |
| `air_winter_phase_1` | `icon = GFX_air_winter_phase_1` |
| `air_winter_phase_2` | `icon = GFX_air_winter_phase_2` |
| `air_winter_phase_3` | `icon = GFX_air_winter_phase_3` |
| `air_winter_phase_4` | `icon = GFX_air_winter_phase_4` |
| `air_winter_phase_5` | `icon = GFX_air_winter_phase_5` |
| `air_winter_phase_6` | `icon = GFX_air_winter_phase_6` |
| `air_winter_disease_pressure_state` | `icon = GFX_air_winter_disease_pressure_state` |

## Simplifications, omissions, and blockers

None. All seven requested source PNGs, processed PNGs, final DDS files, stable sprite handoffs, prompt records, hashes, and the contact sheet are present. No borrowed asset, placeholder, visual fallback, copied art, zombie path, audio asset, `.gfx` edit, gameplay edit, localisation edit, specification edit, or manifest edit was used.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`
