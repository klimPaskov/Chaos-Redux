# Event 006 FORM-48 official ImageGen prompt log

Date: 2026-07-18
Scope: `HBX`, `PFX`, and the FORM-48 Pacific Federation emblem

Every final visual in this package retains an official ImageGen source. Flag
flattening, chroma removal, target-size PNGs, TGAs, DDS conversion, and contact
sheets are deterministic post-processing; none substitutes locally drawn
geometry for the generated design.

## `HBX` California civic carrier — selected result

- Ordered input:
  `reference_inputs/california_flag_public_domain_960px.png`
- Input role: public-domain California-flag geometry and historical motif
  reference; the official California statute controls the comparison.
- Original ImageGen output:
  `C:/Users/klimp/.codex/generated_images/019f7443-2dfc-76e3-8d2b-3e5b6617e8e3/exec-d5fc25e1-9d41-4799-9b98-9281a1be2b6d.png`
- Retained copy:
  `source_png/flags/HBX_california_civic_imagegen_selected.png`

```text
Use case: precise-object-edit
Asset type: Hearts of Iron IV country-flag source master for HBX California
Input images: Image 1 is the authoritative public-domain flat California flag reference. Preserve its exact star, walking grizzly, green ground, lower red stripe, proportions, and orthographic presentation.
Primary request: Create one clean flat reconstruction of the 1911 California Bear Flag. Preserve exactly one red five-point star in the upper hoist, exactly one left-facing walking brown grizzly on one green grass strip, and one solid red lower stripe. Retain the exact visible legend CALIFORNIA REPUBLIC in dark brown block lettering, spelled precisely with no extra letters, numbers, punctuation, or words, centered below the bear and above the lower stripe.
Style/medium: clean flat historical civic flag; hard edges and solid fills; exact 3:2 edge-to-edge flag face.
Constraints: one flag only; keep the documented star, bear direction, grass line, stripe, legend, and proportions; no watermark.
Avoid: gradients, lighting, texture, fabric, folds, waving, flagpole, perspective, mockup, scene, shadow, bevel, gloss, painterly background, extra stars, altered bear direction, new seals, ideology symbols, alternate versions, unreadable/fake lettering, contact sheet.
```

The prior textless HBX source was superseded because the historical legend is
required for this real California civic identity. Five earlier HBX attempts are
retained under
`source_png/flags/rejected/` for selection provenance and are not runtime inputs.

## `PFX` Pacific Federation — selected result

### Initial original design

- Original ImageGen output:
  `C:/Users/klimp/.codex/generated_images/019f6d0c-b703-7900-814b-d269940903f3/exec-8fd21756-c94a-443e-93cb-a47a77d3aab2.png`
- Retained selection-history copy:
  `source_png/flags/rejected/PFX_attempt_01.png`

```text
Use case: logo-brand
Asset type: Hearts of Iron IV country-flag source master for PFX Pacific Federation
Primary request: Create one original edge-to-edge 3:2 federal flag for a negotiated Pacific federation linking California, Hawaii, and Micronesia. Use a deep navy field crossed by one broad turquoise horizontal band edged above and below by narrow gold lines. Center one gold rope ring on the band. Inside the ring place exactly three bold ivory curling ocean currents arranged with balanced rotational symmetry around one compact gold eight-point compass rose. The three currents represent the three founding Pacific constituencies; the compass, rope, and corridor represent common navigation, ports, and federal obligations.
Style/medium: clean flat vector-like civic vexillology with hard crisp edges and solid fills only, designed to remain recognizable at 10x7 pixels.
Composition/framing: exact orthographic 3:2 rectangle; perfectly centered band and charge; thick shapes and generous negative space.
Color palette: only deep Pacific navy, turquoise, warm gold, and ivory.
Constraints: exactly one band, one rope ring, three currents, and one eight-point compass; no text; no watermark; one flag face only.
Avoid: gradients, highlights, shadows, glow, texture, fabric, folds, waving, flagpole, perspective, scene, mockup, California bear or red star, Hawaii Union Jack, horizontal eight-stripe imitation, Federated States of Micronesia four-star circle, Pacific Community logo, sail, palm tree, canoe, member-star circle, national-flag fragments, letters, dates, ideology symbols, alternate versions, contact sheet.
```

### Selected exact-colour edit

- Ordered input: the preceding original ImageGen PFX result.
- Original ImageGen output:
  `C:/Users/klimp/.codex/generated_images/019f6d0c-b703-7900-814b-d269940903f3/exec-dc4d48b5-ea11-4fbe-95a7-bc8496725941.png`
- Retained copy:
  `source_png/flags/PFX_pacific_federation_imagegen_selected.png`

```text
Use case: precise-object-edit
Asset type: exact flat-colour correction of the PFX Pacific Federation flag
Input images: Image 1 is the selected original PFX design. Preserve its complete geometry: exact field, band, two edging lines, rope ring, three wave curls, and eight-point compass.
Primary request: Replace all tonal variation with four uniform civic spot colours only: deep navy #0B2D4D, turquoise #159A9C, warm gold #E4B33B, and ivory #F5F1DE. Keep every boundary and proportion unchanged.
Constraints: zero gradients, zero shading, zero texture, zero highlights, no lettering, no added or removed symbols, one edge-to-edge 3:2 flag face.
Avoid: redesign, simplification, glow, bevel, shadows, fabric, perspective, mockup, alternate version, contact sheet.
```

The selected output retained subtle generator tonal variation despite the edit.
The build script therefore performs one documented no-dither mapping to the
same four requested spot colours. It preserves the ImageGen geometry and is
colour management, not a locally authored substitute.

## FORM-48 emblem — selected result

- Original ImageGen output:
  `C:/Users/klimp/.codex/generated_images/019f6d0c-b703-7900-814b-d269940903f3/exec-17de5a50-6c50-4e49-b800-36de14026e79.png`
- Retained copy:
  `source_png/emblems/independence_wave_formable_form_48_imagegen_raw.png`

```text
Use case: logo-brand
Asset type: transparent Hearts of Iron IV UI emblem for FORM-48 Pacific Regional Federation
Primary request: Create a compact heraldic federal emblem centered on an open ivory charter. Lay one large aged-gold eight-point compass rose over the charter, place one compact gold rising sun behind the upper edge, and link exactly three turquoise circular wave medallions across the lower edge with small gold links. Complete the lower silhouette with one dark navy rope arc connecting the medallions. The meaning is negotiated charter, common navigation, a Pacific dawn, and three founding constituencies.
Scene/backdrop: perfectly uniform solid #ff00ff chroma-key background for background removal.
Style/medium: polished Hearts of Iron IV painted heraldic UI emblem, 1930s civic character, crisp silhouette, restrained period patina, strong dark outline, controlled internal material detail; no enclosing shield or square plaque.
Composition/framing: centered near-square crest with generous padding, readable at 128x128.
Color palette: aged gold, ivory parchment, turquoise, deep navy, near-black outline; never use #ff00ff in the emblem.
Constraints: exactly one charter, one eight-point compass, one rising sun, three linked wave medallions, and one rope arc; no people; no text; no letters; no numbers; no watermark; fully separated from the background.
Avoid: copying either flag charge verbatim, crown, eagle, national coats of arms, ideological symbols, California bear or star, Hawaii flag fragments, Micronesian star circle, Pacific Community logo, sail, modern logo gloss, neon, glow, white sticker border, fake checkerboard, opaque square, scenery, faces, text.
The #ff00ff background must be one uniform color with no shadows, gradients, texture, reflections, floor plane, or lighting variation.
```

## Selection history

| Retained rejected file | Disposition |
|---|---|
| `source_png/flags/rejected/HBX_attempt_01.png` | rejected: illustrative bear and field treatment did not preserve the controlling reference closely enough |
| `source_png/flags/rejected/HBX_attempt_02_flatten_edit.png` | rejected: residual generator shading and weaker historical geometry |
| `source_png/flags/rejected/HBX_attempt_03_spot_edit.png` | rejected: residual tonal variation and less faithful mark placement |
| `source_png/flags/rejected/HBX_attempt_04_pixel.png` | rejected: source became a pixel-art reinterpretation rather than a flag master |
| `source_png/flags/rejected/HBX_attempt_05_stencil.png` | rejected: bear was oversimplified and visually inferior at normal size |
| `source_png/flags/rejected/PFX_attempt_01.png` | retained only as the generated parent of the selected exact-colour edit |

## Deterministic post-processing

- The emblem chroma source was processed with the official ImageGen
  `remove_chroma_key.py` helper using `--key-color #ff00ff --soft-matte
  --transparent-threshold 18 --opaque-threshold 165 --edge-contract 1
  --despill`.
- Flag sources were mapped without dithering to the exact palettes recorded in
  `manifest.md`, reduced to 82x52, 41x26, and 10x7, and mapped back to those
  palettes so no interpolation gradient survives.
- TGAs were written as uncompressed 32-bit BGRA pixel streams with bottom-left
  origin and eight alpha bits.
- The emblem DDS was created only with the repository's
  `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` legacy
  uncompressed BGRA converter.
