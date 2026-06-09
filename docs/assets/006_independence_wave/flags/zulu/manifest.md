# Event 006 Zulu Flag Asset Manifest

## Current Status

Superseded by the 2026-06-08 imagegen regeneration pass. Current ZUL source, processed, and final flag paths are recorded in `docs/assets/006_independence_wave/flags/manifest.md`. The previous concept-sheet notes below are retained only as previous-tranche provenance and are not the current game-facing ZUL flag source.

## Package Summary

- Related event id: 006
- Related event slug: independence_wave
- Asset type: country flag package
- Intended in-game use: country and ideology flags for custom Zulu/Natal local-polity or historical-return package, tag `ZUL`
- Final formats: HOI4 country flag TGAs, 32bpp RGBA, uncompressed, no palette
- Target sizes:
  - Normal: 82x52
  - Medium: 41x26
  - Small: 10x7
- Sprite name: not applicable for HOI4 country flags
- `.gfx` file: not applicable for HOI4 country flags
- Localisation key: not applicable for this asset-only task
- Contact sheet: `docs/assets/006_independence_wave/flags/zulu/contact_sheets/ZUL_contact_sheet.png`
- Asset status: complete

## Source Mode

- Base `ZUL`: `$imagegen` concept source with original simplified local reconstruction for exact HOI4 flag sizes.
- Ideology variants: `$imagegen` concept sheet cropped to the four non-text flag panels, then resized and converted locally.
- Generated base prompt: `docs/assets/006_independence_wave/flags/zulu/prompts/ZUL_flag_prompt.txt`
- Generated ideology prompt: `docs/assets/006_independence_wave/flags/zulu/prompts/ZUL_ideology_variants_prompt.txt`
- Generated ideology concept copy: `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_ideology_variants_generated_concept.png`
- Source link: not applicable
- Source author, archive, or collection: generated concept created for Chaos Redux
- Source date or estimated date range: alternate-history 1936-1945 Event 006 use
- License or public-domain status:
  - Final image files are original Chaos Redux asset work.
  - No modern flag, modern coat of arms, readable text, copyrighted emblem, or source bitmap was copied.
  - The ideology variants avoid traumatic or extremist real symbols; the fascism variant uses a fictional administrative spearhead/fortress motif rather than real-world extremist insignia.

## Assets

### ZUL

- Use: base fallback flag
- Design note: red ochre field, black hoist, pale separator, simplified shield/spear emblem
- Source PNG paths:
  - `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_generated_source.png`
  - `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_source_reconstruction.png`
- Processed PNG paths:
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_medium.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_small.png`
- Final TGA paths:
  - `gfx/flags/ZUL.tga`
  - `gfx/flags/medium/ZUL.tga`
  - `gfx/flags/small/ZUL.tga`
- Status: complete

### ZUL_democratic

- Use: democratic ideology flag
- Design note: blue council field with black/white hoist, bead-ring council seal, hut and shield motif
- Source PNG path: `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_democratic_generated_source.png`
- Processed PNG paths:
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_democratic.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_democratic_medium.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_democratic_small.png`
- Final TGA paths:
  - `gfx/flags/ZUL_democratic.tga`
  - `gfx/flags/medium/ZUL_democratic.tga`
  - `gfx/flags/small/ZUL_democratic.tga`
- Status: complete

### ZUL_neutrality

- Use: neutrality ideology flag
- Design note: tan authority field with dark hoist, cattle-horn/kraal council motif, flanking non-modern spear forms
- Source PNG path: `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_neutrality_generated_source.png`
- Processed PNG paths:
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_neutrality.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_neutrality_medium.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_neutrality_small.png`
- Final TGA paths:
  - `gfx/flags/ZUL_neutrality.tga`
  - `gfx/flags/medium/ZUL_neutrality.tga`
  - `gfx/flags/small/ZUL_neutrality.tga`
- Status: complete

### ZUL_fascism

- Use: fascism ideology flag
- Design note: black and red administrative standard with a fictional spearhead and fortress emblem; no real extremist symbols
- Source PNG path: `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_fascism_generated_source.png`
- Processed PNG paths:
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_fascism.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_fascism_medium.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_fascism_small.png`
- Final TGA paths:
  - `gfx/flags/ZUL_fascism.tga`
  - `gfx/flags/medium/ZUL_fascism.tga`
  - `gfx/flags/small/ZUL_fascism.tga`
- Status: complete

### ZUL_communism

- Use: communism ideology flag
- Design note: red field with black/gold hoist and a communal grain/gear council emblem; no hammer-and-sickle
- Source PNG path: `docs/assets/006_independence_wave/flags/zulu/source_png/ZUL_communism_generated_source.png`
- Processed PNG paths:
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_communism.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_communism_medium.png`
  - `docs/assets/006_independence_wave/flags/zulu/processed_png/ZUL_communism_small.png`
- Final TGA paths:
  - `gfx/flags/ZUL_communism.tga`
  - `gfx/flags/medium/ZUL_communism.tga`
  - `gfx/flags/small/ZUL_communism.tga`
- Status: complete

## Validation

- 2026-06-04 parent correction: after user review reported the generated flags were upside down in game, all final in-game ZUL TGA outputs under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` were vertically flipped and revalidated. Source and processed PNG review files were left unchanged; only the final game-facing TGAs were corrected.
- `file gfx/flags/ZUL*.tga gfx/flags/medium/ZUL*.tga gfx/flags/small/ZUL*.tga`
  - All files report `Targa image data - RGBA`.
  - Normal files report `82 x 52 x 32`.
  - Medium files report `41 x 26 x 32`.
  - Small files report `10 x 7 x 32`.
- `identify -verbose ... | rg 'Filename:|Format:|Class:|Geometry:|Type:|Depth:|Compression:|Orientation:'`
  - All files report `Format: TGA (Truevision Targa image)`.
  - All files report `Class: DirectClass`.
  - All files report `Type: TrueColorAlpha`.
  - All files report `Depth: 8-bit`.
  - All files report `Compression: None`.
  - All files report `Orientation: TopLeft`.
- `identify -format '%f %wx%h %[bit-depth]-bit %[channels] %[type] %[compression]\n' ...`
  - All normal, medium, and small ZUL flags report expected dimensions, `8-bit srgba TrueColorAlpha None`.

## Risks

- The ideology variant source concept was generated as a presentation sheet that included labels outside the flag panels. The final assets were cropped from the non-text flag panels only; no label text is present in the processed PNG/TGA files.
- The 10x7 small variants preserve color identity and broad silhouettes, but fine emblem detail necessarily collapses at vanilla HOI4 small-flag size.
