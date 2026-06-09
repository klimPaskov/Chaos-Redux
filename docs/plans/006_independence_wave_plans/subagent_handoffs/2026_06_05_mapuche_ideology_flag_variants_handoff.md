# Event006 MAP Ideology Flag Variants Handoff

## Summary

- Task: create missing ideology flag variants for Event006 tag `MAP`.
- Tag: `MAP`
- Country concept: Mapuche Land Congress.
- Source mode: local-generated-original deterministic raster/vector construction using the approved base MAP visual identity as direction.
- Web use: none.
- Scope honored: only flag assets and asset documentation/handoff were edited. Gameplay, localisation, events, focuses, decisions, scripted files, country history, and `.gfx` files were not edited.
- DDS parity: produced for every TGA output because nearby Event006 custom country flags include DDS siblings.

## Changed Files

Final large flags:

- `gfx/flags/MAP_communism.tga`
- `gfx/flags/MAP_democratic.tga`
- `gfx/flags/MAP_fascism.tga`
- `gfx/flags/MAP_neutrality.tga`
- `gfx/flags/MAP_communism.dds`
- `gfx/flags/MAP_democratic.dds`
- `gfx/flags/MAP_fascism.dds`
- `gfx/flags/MAP_neutrality.dds`

Final medium flags:

- `gfx/flags/medium/MAP_communism.tga`
- `gfx/flags/medium/MAP_democratic.tga`
- `gfx/flags/medium/MAP_fascism.tga`
- `gfx/flags/medium/MAP_neutrality.tga`
- `gfx/flags/medium/MAP_communism.dds`
- `gfx/flags/medium/MAP_democratic.dds`
- `gfx/flags/medium/MAP_fascism.dds`
- `gfx/flags/medium/MAP_neutrality.dds`

Final small flags:

- `gfx/flags/small/MAP_communism.tga`
- `gfx/flags/small/MAP_democratic.tga`
- `gfx/flags/small/MAP_fascism.tga`
- `gfx/flags/small/MAP_neutrality.tga`
- `gfx/flags/small/MAP_communism.dds`
- `gfx/flags/small/MAP_democratic.dds`
- `gfx/flags/small/MAP_fascism.dds`
- `gfx/flags/small/MAP_neutrality.dds`

Asset docs and review files:

- `docs/assets/006_independence_wave/flags/mapuche/manifest.md`
- `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_communism_source.png`
- `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_democratic_source.png`
- `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_fascism_source.png`
- `docs/assets/006_independence_wave/flags/mapuche/source_png/MAP_neutrality_source.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_communism.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_democratic.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_fascism.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/large/MAP_neutrality.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/medium/MAP_communism.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/medium/MAP_democratic.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/medium/MAP_fascism.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/medium/MAP_neutrality.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/small/MAP_communism.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/small/MAP_democratic.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/small/MAP_fascism.png`
- `docs/assets/006_independence_wave/flags/mapuche/processed_png/small/MAP_neutrality.png`
- `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_base_and_ideology_variants_tga_contact.png`
- `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_ideology_variants_large_contact.png`
- `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_ideology_variants_medium_contact.png`
- `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_ideology_variants_small_contact_5x.png`

## Design Notes

- All four variants are fictional Mapuche Land Congress designs, not historical claims.
- The approved base files `gfx/flags/MAP.tga`, `gfx/flags/medium/MAP.tga`, and `gfx/flags/small/MAP.tga` were not replaced or flipped.
- Shared identity motifs: dark hoist, assembly stones, land/forest/river palette, mountains, and congress seal language.
- Variant differentiation:
  - `communism`: red land-congress banner with gold diagonal and non-offensive gold star treatment.
  - `democratic`: multiband council banner with white assembly band and river field.
  - `fascism`: dark angular authoritarian standard with no real-world fascist or offensive symbol.
  - `neutrality`: vertical land-forest-river congress standard.

## Validation

- Reference inspection completed:
  - `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`, flag section.
  - `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`.
  - `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/flags/`.
  - Existing approved MAP base TGA files.
  - Nearby Event006 custom flag DDS/TGA pattern for `ASN`, `AYM`, `KBN`, and `PLM`.
- Final ImageMagick checks:
  - All large TGAs: `82x52`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`.
  - All medium TGAs: `41x26`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`.
  - All small TGAs: `10x7`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`.
  - All DDS parity files: same dimensions as TGA siblings, `8-bit`, `srgba`, `TrueColorAlpha`, `None`.
- Orientation/readability:
  - TGA-derived contact sheet `docs/assets/006_independence_wave/flags/mapuche/contact_sheets/MAP_base_and_ideology_variants_tga_contact.png` was visually inspected.
  - Workspace contact sheets were generated for large, medium, and magnified small variants.
  - Every output is upright; no variant was flipped vertically or horizontally.

## Remaining Risks

- Small `10x7` flags necessarily lose fine seal and mountain detail, but each variant keeps a distinct palette and silhouette.
- The designs are fictional symbolic treatments and do not assert historical Mapuche political flag variants.
- No `.gfx` wiring was done or needed for HOI4 country flags, matching the requested scope.
