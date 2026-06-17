# Event 012 Africa Variant Super-Event Image Manifest

Date: `2026-06-17`
Related event: `12`
Slug: `africa`
Package root: `docs/assets/012_africa/super_events/variant_images_batch_forest_root/`
Source mode: generated with built-in `$imagegen`
Status: `handed_off`

## Scope

This package contains final candidate image assets for the two missing solemn high-chaos Event 012 Africa super-event variant roles:

- `Forest Parliament reveal`
- `World Root Mandate`

Both images are generated because the requested scenes are fictional, symbolic, alternate-history, and supernatural-political rather than archival historical material.

## Asset table

| Asset | Role | Asset type | Source mode | Source PNG | Processed PNG | Final DDS | Live DDS | Target size | Prompt summary | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `super_event_012_forest_parliament` | Forest Parliament reveal | super-event image | `$imagegen` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/super_event_012_forest_parliament_source.png` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/super_event_012_forest_parliament_processed.png` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/dds/super_event_012_forest_parliament.dds` | `gfx/super_events/super_event_012_forest_parliament.dds` | `457x328` | solemn impossible constitutional congress in a Central African rainforest with human and nonhuman delegates in one chamber | `converted` |
| `super_event_012_world_root_mandate` | World Root Mandate | super-event image | `$imagegen` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/source_png/super_event_012_world_root_mandate_source.png` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/processed_png/super_event_012_world_root_mandate_processed.png` | `docs/assets/012_africa/super_events/variant_images_batch_forest_root/dds/super_event_012_world_root_mandate.dds` | `gfx/super_events/super_event_012_world_root_mandate.dds` | `457x328` | covenantal baobab-root political order binding maps, seals, charters, and land into one juridical tableau | `converted` |

## Source selection

Generated alternatives retained in this package:

- `forest_parliament_candidate_a_source.png`
- `forest_parliament_candidate_b_source.png`
- `world_root_mandate_candidate_a_source.png`
- `world_root_mandate_candidate_b_source.png`

Selected finals:

- Forest Parliament: `candidate_a`
- World Root Mandate: `candidate_b`

Selection rationale:

- `candidate_a` for Forest Parliament keeps the chamber legible at super-event size and balances human and nonhuman delegates without pushing the scene into caricature.
- `candidate_b` for World Root Mandate avoids readable pseudo-text better than `candidate_a` and gives the baobab-root legal order a stronger central silhouette.

## Generation prompts

### Forest Parliament final

```text
Use case: historical-scene
Asset type: HOI4 super-event image for Chaos Redux Event 012 Africa, final crop 457x328
Primary request: Forest Parliament reveal, solemn high-chaos constitutional congress in a Central African rainforest
Scene/backdrop: impossible parliamentary chamber built into a dense equatorial rainforest canopy and root-vault, carved wood benches, hanging lamps, heavy foliage, humid haze, monumental roots arching above the chamber
Subject: a solemn constitutional congress with symbolic nonhuman delegates and human forest and central authority delegates seated in one chamber; silhouettes or dignified visible forms of gorilla, chimpanzee, and bonobo delegates among human envoys; no caricature, no comedy, no cute animal behavior
Style/medium: painterly documentary realism suitable for a HOI4 super-event image, grounded alternate-history scene, detailed but readable
Composition/framing: wide central composition, congress floor and speaker’s dais visible, delegates arranged in a clear chamber, strong focal point in the center, readable at small size, slight elevated viewpoint
Lighting/mood: solemn, juridical, reverent, filtered forest light with restrained warm highlights and deep green-brown shadows, high contrast
Color palette: deep forest greens, dark wood, bark browns, muted brass, restrained parchment gold
Materials/textures: carved timber benches, woven cloth, bark, roots, humid air, polished wood, leaf canopy
Constraints: no modern logos, no readable text, no real identifiable people, no joke framing, no cartooning, no modern clothing, no modern architecture, no fantasy action battle, no generic globe symbols
Avoid: caricature apes, modern suits, microphones, comic expressions, superhero poses, neon, sci-fi, UI overlays, watermark
```

### World Root Mandate final

```text
Use case: historical-scene
Asset type: HOI4 super-event image for Chaos Redux Event 012 Africa, final crop 457x328
Primary request: alternate candidate for World Root Mandate
Scene/backdrop: monumental baobab tribunal and root-chamber in a living landscape, with carved stelae, wax seals, blank charters, folded maps, root-bound ledgers, and stone plinths
Subject: central giant baobab trunk with descending roots binding sealed documents, maps, and legal objects into a solemn world-order arrangement; no people; no readable writing, use blank parchment, embossed seals, carved symbols, and stitched map textures instead of text
Style/medium: painterly documentary realism, alternate-history constitutional tableau, symbolic but tangible
Composition/framing: frontal centered composition with the baobab and roots dominating the frame, charter table and bound map tablets in foreground, clear readability at small size
Lighting/mood: solemn, juridical, covenantal, still air, shafts of late light, grave and ceremonial
Color palette: deep earth browns, baobab grey, parchment tan, moss green, old bronze, restrained amber
Constraints: no readable text, no identifiable people, no generic globe, no fantasy battle, no modern props, no copied sacred relics, no comic stylization
Avoid: fake calligraphy, modern map labels, sci-fi glow, neon, watermark, UI overlays
```

## Processing and conversion

Processed PNG command:

```bash
convert <source>.png \
  -resize '457x328^' \
  -gravity center \
  -crop 457x328+0+0 +repage \
  -colorspace sRGB \
  -contrast-stretch 0.3%x0.3% \
  -modulate 100,92,100 \
  -unsharp 0x0.8+0.5+0.02 \
  <processed>.png
```

DDS conversion command:

```bash
convert <processed>.png -define dds:compression=dxt1 <output>.dds
```

## Contact sheets

- Source candidates: `docs/assets/012_africa/super_events/variant_images_batch_forest_root/contact_sheets/source_candidates_contact_sheet.png`
- Processed candidates: `docs/assets/012_africa/super_events/variant_images_batch_forest_root/contact_sheets/processed_candidates_contact_sheet.png`
- Final selected pair: `docs/assets/012_africa/super_events/variant_images_batch_forest_root/contact_sheets/final_candidates_contact_sheet.png`

## Notes and risks

- Forest Parliament remains intentionally solemn and parliamentary, but the nonhuman delegates are still visually explicit. This is appropriate for the role, though any later text/audio wiring should keep the same serious register.
- World Root Mandate uses a stitched map surface and seal-table foreground instead of readable charter text. This keeps the no-text rule cleaner than the rejected variant, though the map treatment is still symbolic rather than archival-document literal.
- No `.gfx`, localisation, event, sound, or gameplay files were edited in this asset pass.
