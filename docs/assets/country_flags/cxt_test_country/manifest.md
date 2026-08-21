# CXT test-country flag asset manifest

## Requirement and identity

- Intended tag: `CXT`.
- Asset type: fictional flat country flag, normal/medium/small ladder.
- Source mode: `$imagegen` native generation through the built-in ImageGen tool.
- Background mode: `consumer_opaque`; HOI4 country flags use a full painted canvas, so no alpha-backed treatment or background-removal fallback was used.
- Status: `complete` for the requested source, preview, review DDS, contact sheet, and three runtime TGAs.
- Collision evidence: the parent task supplied completed exact-tag collision checks for the Chaos Redux repository, installed vanilla common files, Workshop `1521695605`, Workshop `2265420196`, and sibling local mods. Workshop `1458561226` was not installed.

## Generation evidence

The source was generated on 2026-08-21 with the built-in `image_gen` tool (`imagegen__imagegen`), not the CLI fallback. The built-in tool did not expose a separate model name in its result; the source PNG retains the provider-generated PNG/C2PA metadata envelope. The original generated artifact was copied from the tool's reported output into `source/cxt_flag_imagegen.png` without repainting or tracing.

Prompt:

> Use case: logo-brand. Asset type: fictional Hearts of Iron IV country flag, flat rectangular state flag. Create one original, orthographic, cleanly designed 2:1 flag for the fictional Chaos Redux testing country tag CXT, an artificial state laboratory and military proving authority. Full opaque canvas, no transparency. Design: dark charcoal field; a vivid toxic-chartreuse diagonal band running from upper hoist toward lower fly with crisp hard edges; centered high-contrast white calibration reticle / gear-like ring emblem with a strong readable outer silhouette; exactly three asymmetric cardinal markers around the ring; one restrained crimson warning accent integrated as a small wedge or marker. The emblem should evoke a calibration reticle, industrial gear, and testing sigil without any readable text. Keep the composition heraldic, intentional, flat, and legible as a tiny 10x7 flag. Style/medium: flat graphic flag design, screen-printed vector-like color blocks rendered as a clean bitmap. Composition/framing: entire flag fills the canvas, straight-on, no perspective. Palette: charcoal black, toxic chartreuse, white, small crimson accent. Constraints: no readable text, numbers, letters, gradients, photographic texture, fabric folds, flagpole, sky, lighting, shadows, bevels, glow, grunge, watermark, UI artifacts, meme styling, historical insignia, copyrighted emblems, or resemblance to any existing real-world flag; no extra symbols beyond the central ring and three asymmetric markers. Preserve crisp geometry and strong contrast.

## File inventory

| File | Purpose | Dimensions / format |
|---|---|---|
| `source/cxt_flag_imagegen.png` | Untouched native ImageGen source master | `1774x887`, RGB PNG |
| `processed/cxt_flag_preview.png` | Cropped, hard-edged, controlled four-colour review derivative | `820x520`, RGB PNG |
| `processed/cxt_flag_preview.dds` | Repository-standard BGRA DDS conversion of the flat processed review derivative | `820x520`, legacy uncompressed one-level BGRA DDS |
| `contact_sheet.png` | Review sheet containing source, processed preview, and all runtime sizes | `1100x820`, RGB PNG |
| `gfx/flags/CXT.tga` | Runtime normal flag | `82x52`, uncompressed 32-bit true-color TGA |
| `gfx/flags/medium/CXT.tga` | Runtime medium flag | `41x26`, uncompressed 32-bit true-color TGA |
| `gfx/flags/small/CXT.tga` | Runtime small flag | `10x7`, uncompressed 32-bit true-color TGA |

The source was center-cropped from `1774x887` to `1399x887` to match the required `82:52` runtime aspect ratio. The derivative was then deterministically classified into exactly four fixed RGB colours — charcoal `(31,32,35)`, toxic chartreuse `(184,224,4)`, white `(255,255,255)`, and crimson `(207,20,53)` — before nearest-neighbour export, producing hard colour-block edges with no gradient or vignette. No local vector trace, primitive emblem redraw, or generated-art replacement was used. The `10x7` ladder was manually simplified from the classified raster so a compact white reticle/diamond and two crimson warning pixels remain visible.

## Format and origin validation

Installed Vanilla `USA_communism.tga` was inspected before export at the normal, medium, and small ladders. Its precedent is TGA image type `2` (uncompressed true color), `32` bits per pixel, descriptor `0x08` (8 alpha bits, bottom-left origin), with exact byte lengths `17074`, `4282`, and `298` for `82x52`, `41x26`, and `10x7` respectively. The CXT TGAs match that convention and exact lengths:

- `gfx/flags/CXT.tga`: `17074` bytes; header `000002000000000000000000520034002008`; origin bit `0`.
- `gfx/flags/medium/CXT.tga`: `4282` bytes; header `00000200000000000000000029001a002008`; origin bit `0`.
- `gfx/flags/small/CXT.tga`: `298` bytes; header `0000020000000000000000000a0007002008`; origin bit `0`.

The DDS preview was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. Its header validates as a 128-byte legacy uncompressed BGRA header: `DDS ` magic, header size `124`, dimensions `820x520`, pixel-format size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks, texture caps `0x1000`, and exact length `1,705,728` bytes.

## Colour and design notes

The flat derivative uses exactly four colours: dark charcoal `(31,32,35)`, vivid toxic chartreuse `(184,224,4)`, white `(255,255,255)`, and restrained crimson `(207,20,53)`. The central white calibration reticle is enclosed by a gear-like ring, with three asymmetric cardinal markers and the separate crimson warning accent. The normal and medium exports preserve the generated emblem silhouette with crisp block edges. The manually simplified small export uses a compact white reticle/diamond mark at the centre and a two-pixel crimson warning wedge at the lower-right of the mark.

The source remains the untouched native ImageGen master; the processed preview and runtime ladder are the controlled flat derivative. The processed/runtime files contain no gradient, vignette, shading, readable letters, numbers, text, watermarks, flagpoles, fabric folds, lighting, shadows, historical insignia, or real-world flag references.

## Provenance and licensing

This is original fictional art generated for Chaos Redux with the built-in OpenAI ImageGen tool. No external image, historical flag, real person, real place, or third-party emblem was used. The work is intended for the Chaos Redux mod's fictional test country `CXT`; retain the source and this manifest with the package for provenance.

## SHA-256 evidence

- `source/cxt_flag_imagegen.png`: `BF509E0DF259B509861727ED73439A9D69B43D90F04C98A5029AF565A1B5FBC5`
- `processed/cxt_flag_preview.png`: `5C5D0EA6905683D50EFE339B68392626FBBBDBA59E143BC8F4F17A804C900B50`
- `processed/cxt_flag_preview.dds`: `8EFEF3F100CDE0FD2EB3ABD70DB038A4686E783E7776D37825ACC8C72E5D5FF3`
- `contact_sheet.png`: `3CEAD75F2F3A7B4F4843C281E6A03BF6C9B42400A60479EF29B545E73ABE4BE3`
- `gfx/flags/CXT.tga`: `668F84FB3AEDD878E17FFCFA0B8738B9134D261B3959B2BEE7591A50C663328E`
- `gfx/flags/medium/CXT.tga`: `1DA1903266605501E3D9656A63ADF5A97F24C51B0191E9BB8C32F0AE692E7162`
- `gfx/flags/small/CXT.tga`: `25E4766458B4785710EB36679D5C34B19C14B1A351644F7753C98EEF01AA6C48`
