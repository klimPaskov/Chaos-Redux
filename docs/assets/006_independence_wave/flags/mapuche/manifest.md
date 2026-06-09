# Event006 MAP Flag Asset Manifest

## Current Status

Superseded by the 2026-06-08 imagegen regeneration pass. Current MAP source, processed, and final flag paths are recorded in `docs/assets/006_independence_wave/flags/manifest.md`. The previous vector/raster notes below are retained only as previous-tranche provenance and are not the current game-facing MAP flag source.

## Package Summary

- Related event id: 006
- Related event slug: independence_wave
- Asset type: country flag package
- Tag: `MAP`
- Country concept: Mapuche Land Congress / Araucania Council
- Intended in-game use: base and ideology country flags for Event006 tag `MAP`
- Final formats: HOI4 country flag TGAs plus DDS parity, 32bpp RGBA, uncompressed, no palette
- Target sizes:
  - Normal: 82x52
  - Medium: 41x26
  - Small: 10x7
- Sprite name: not applicable for HOI4 country flags
- `.gfx` file: not applicable for HOI4 country flags
- Localisation key: not applicable for this asset-only package
- Asset status: complete

## Source Mode

- Source mode: locally generated original deterministic vector/raster construction, rendered with ImageMagick.
- Source link: not applicable; web was not used.
- Source author, archive, or collection: original Chaos Redux asset work.
- Source date or estimated date range: fictional Event006 alternate-history country flag.
- License or public-domain status: original project asset; no copied modern national flag, Chilean cosmetic flag, Kingdom of Araucania monarchist flag, coat of arms, text, or sourced bitmap was used.
- Base source PNG path: not retained from the prior base-flag tranche.
- Ideology variant source PNG paths: `docs/assets/006_independence_wave/flags/mapuche/source_png/`
- Ideology variant processed PNG paths: `docs/assets/006_independence_wave/flags/mapuche/processed_png/`
- Contact sheets: `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/`

## Design

- Design note: fictional Event006 council emblem inspired by land, mountain, forest, and assembly symbolism.
- Base visual language: forest-green upper field, dark council/river band, red-ochre land field, dark hoist for assembly continuity, gold divider, five assembly stones, and a central round council seal with mountains and meeting stones.
- Ideology variant visual language: distinct layouts using land, forest, mountain, river, assembly-stone, and congress-seal motifs; no real-world offensive political symbols.
- Cultural framing: respectful land congress / Araucania council direction; not a Chile cosmetic flag and not a monarchist Araucania joke flag.
- Orientation note: final TGA-derived previews were inspected, not only the PNG sources, to avoid the prior upside-down output issue.
- Readability note: the 10x7 small flags preserve distinct palette and block structure; fine mountain, seal, and assembly-stone detail necessarily collapses at vanilla HOI4 small-flag size.

## Assets

### MAP

- Use: base custom country flag
- Source mode: local-generated-original
- Final TGA paths:
  - `gfx/flags/MAP.tga`
  - `gfx/flags/medium/MAP.tga`
  - `gfx/flags/small/MAP.tga`
- Target sizes:
  - `gfx/flags/MAP.tga`: 82x52
  - `gfx/flags/medium/MAP.tga`: 41x26
  - `gfx/flags/small/MAP.tga`: 10x7
- Status: complete

### MAP Ideology Variants

| variant | source_png | processed_large | final_tga | final_dds | notes |
| --- | --- | --- | --- | --- | --- |
| `communism` | `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_communism_source.png` | `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_communism.png` | `gfx/flags/MAP_communism.tga` | `gfx/flags/MAP_communism.dds` | Red land-congress banner with dark hoist, gold diagonal, assembly stones, mountain seal, and non-offensive gold star treatment. |
| `democratic` | `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_democratic_source.png` | `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_democratic.png` | `gfx/flags/MAP_democratic.tga` | `gfx/flags/MAP_democratic.dds` | Multi-band congress flag with white council band, river field, mountain seal, and four assembly marks. |
| `fascism` | `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_fascism_source.png` | `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_fascism.png` | `gfx/flags/MAP_fascism.tga` | `gfx/flags/MAP_fascism.dds` | Dark authoritarian variant with angular mountain/standard geometry and no real-world fascist or offensive symbol. |
| `neutrality` | `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_neutrality_source.png` | `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_neutrality.png` | `gfx/flags/MAP_neutrality.tga` | `gfx/flags/MAP_neutrality.dds` | Vertical land-forest-river congress standard with central seal and assembly stones. |

Each ideology variant also has medium and small processed PNG/TGA/DDS siblings in:

- `docs/assets/006_independence_wave/flags/mapuche/processed_png/medium/`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/small/`
- `gfx/flags/medium/`
- `gfx/flags/small/`

## Validation

- `identify -format '%f %wx%h %[bit-depth]-bit %[channels] %[type] %[compression] %[orientation]\n' gfx/flags/MAP.tga gfx/flags/medium/MAP.tga gfx/flags/small/MAP.tga`
  - `MAP.tga 82x52 8-bit srgba TrueColorAlpha None TopLeft`
  - `MAP.tga 41x26 8-bit srgba TrueColorAlpha None TopLeft`
  - `MAP.tga 10x7 8-bit srgba TrueColorAlpha None TopLeft`
- `identify -format '%f %m %wx%h %[bit-depth]-bit %[channels] %[type] %[compression] %[orientation]\n'` was run against all 24 ideology variant TGA/DDS outputs.
  - Large TGA outputs are `82x52`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`.
  - Medium TGA outputs are `41x26`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`.
  - Small TGA outputs are `10x7`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`.
  - DDS parity outputs are `DDS`, same dimensions as their TGA siblings, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `Undefined` orientation.
- TGA-derived contact preview was generated at `/tmp/chaosx_mapuche_flag_review/MAP_base_and_variants_from_tga.png`.
- Workspace contact sheets:
  - `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_base_and_ideology_variants_tga_contact.png`
  - `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_ideology_variants_large_contact.png`
  - `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_ideology_variants_medium_contact.png`
  - `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_ideology_variants_small_contact_5x.png`
- Visual inspection confirmed every final game-facing TGA ideology variant is upright.

## Risks

- Historical symbol accuracy was intentionally not claimed because no web sourcing was used; this is a fictional Event006 council emblem.
- The approved base `MAP.tga` files were not replaced or flipped.
- Small-flag detail is necessarily reduced at 10x7, but each ideology keeps a distinguishable palette and silhouette.
