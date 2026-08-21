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
| `processed/cxt_flag_preview.png` | Cropped and resized review preview | `820x520`, RGB PNG |
| `processed/cxt_flag_preview.dds` | Repository-standard BGRA DDS conversion of the processed review preview | `820x520`, legacy uncompressed one-level BGRA DDS |
| `contact_sheet.png` | Review sheet containing source, processed preview, and all runtime sizes | `1100x820`, RGB PNG |
| `gfx/flags/CXT.tga` | Runtime normal flag | `82x52`, uncompressed 32-bit true-color TGA |
| `gfx/flags/medium/CXT.tga` | Runtime medium flag | `41x26`, uncompressed 32-bit true-color TGA |
| `gfx/flags/small/CXT.tga` | Runtime small flag | `10x7`, uncompressed 32-bit true-color TGA |

The source was center-cropped from `1774x887` to `1399x887` to match the required `82:52` runtime aspect ratio, then resized mechanically. No local vector trace, palette swap, primitive redraw, or generated-art replacement was used.

## Format and origin validation

Installed Vanilla `USA_communism.tga` was inspected before export at the normal, medium, and small ladders. Its precedent is TGA image type `2` (uncompressed true color), `32` bits per pixel, descriptor `0x08` (8 alpha bits, bottom-left origin), with exact byte lengths `17074`, `4282`, and `298` for `82x52`, `41x26`, and `10x7` respectively. The CXT TGAs match that convention and exact lengths:

- `gfx/flags/CXT.tga`: `17074` bytes; header `000002000000000000000000520034002008`; origin bit `0`.
- `gfx/flags/medium/CXT.tga`: `4282` bytes; header `00000200000000000000000029001a002008`; origin bit `0`.
- `gfx/flags/small/CXT.tga`: `298` bytes; header `0000020000000000000000000a0007002008`; origin bit `0`.

The DDS preview was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. Its header validates as a 128-byte legacy uncompressed BGRA header: `DDS ` magic, header size `124`, dimensions `820x520`, pixel-format size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks, texture caps `0x1000`, and exact length `1,705,728` bytes.

## Colour and design notes

The design uses a dark charcoal field (dominant sampled RGB approximately `31,31,34`), a vivid toxic-chartreuse diagonal band (approximately `181,221,7`), pure white calibration geometry, and a restrained crimson warning wedge (approximately `207,18,53`). The central white calibration reticle is enclosed by a gear-like ring, with three asymmetric cardinal markers and the separate crimson warning accent. The silhouette remains visible in the normal and medium exports; the small export intentionally retains the strongest band/ring/marker contrast available at `10x7`.

The source and all runtime exports are flat, orthographic flag graphics. There are no readable letters, numbers, text, watermarks, flagpoles, fabric folds, lighting, shadows, gradients as a design element, historical insignia, or real-world flag references.

## Provenance and licensing

This is original fictional art generated for Chaos Redux with the built-in OpenAI ImageGen tool. No external image, historical flag, real person, real place, or third-party emblem was used. The work is intended for the Chaos Redux mod's fictional test country `CXT`; retain the source and this manifest with the package for provenance.

## SHA-256 evidence

- `source/cxt_flag_imagegen.png`: `BF509E0DF259B509861727ED73439A9D69B43D90F04C98A5029AF565A1B5FBC5`
- `processed/cxt_flag_preview.png`: `86185A76316235D29EEC4234F9A68D7F346FD6D7481A3F9944839A115FFD3488`
- `processed/cxt_flag_preview.dds`: `BEF5DFD1675300D4DF85C141F76384A846BFC8312DF6C0D43EB666B480576A7F`
- `contact_sheet.png`: `AF15125CB29C2CA79EEED9416ED9E8A42D91E4ACD1720ACD7F9D5F6DA271C4EF`
- `gfx/flags/CXT.tga`: `900685181AD5104EE93CE91E81BCD5F166A3BE74F19530EE279272CECC4DD31F`
- `gfx/flags/medium/CXT.tga`: `7CB5854D1BA3B0D06D1BC128003486FA24E9EFFEE6D2FD6D283F97FCD5CCC418`
- `gfx/flags/small/CXT.tga`: `B6ECC3A9A8EF2F5253926AAF5DB7C78B500CF148B537FB6FBE5B8636B40FDFC6`
