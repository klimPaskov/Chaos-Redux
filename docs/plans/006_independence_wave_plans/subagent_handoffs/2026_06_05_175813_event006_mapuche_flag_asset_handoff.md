# Event006 MAP Flag Asset Handoff

## Summary

- Task: create a unique HOI4-ready flag package for Event006 custom country tag `MAP`.
- Tag: `MAP`
- Country concept: Mapuche Land Congress / Araucania Council
- Source mode: local-generated-original deterministic vector/raster construction.
- Web use: none.
- Scope honored: gameplay, localisation, country tags, countries, history, focuses, decisions, scripted files, GUI/GFX, spreadsheets, and non-MAP assets were not edited.

## Changed Files

- `gfx/flags/MAP.tga`
- `gfx/flags/medium/MAP.tga`
- `gfx/flags/small/MAP.tga`
- `docs/assets/006_independence_wave/flags/mapuche/manifest.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_175813_event006_mapuche_flag_asset_handoff.md`

## Design Notes

- Fictional Event006 council emblem inspired by land, mountain, forest, and assembly symbolism.
- Avoids Chilean cosmetic flag structure, copied Chilean symbols, and monarchist Kingdom of Araucania framing.
- Uses a forest-green upper field, dark council/river band, red-ochre land field, dark hoist, gold divider, five assembly stones, and a central round council seal with mountains and meeting stones.

## Validation

- Final TGA files exist at all three requested paths.
- ImageMagick validation:
  - `gfx/flags/MAP.tga`: `82x52`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`
  - `gfx/flags/medium/MAP.tga`: `41x26`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`
  - `gfx/flags/small/MAP.tga`: `10x7`, `8-bit`, `srgba`, `TrueColorAlpha`, `None`, `TopLeft`
- Temporary PNG previews were generated outside the workspace under `/tmp/chaosx_mapuche_flag/` and visually inspected.
- Final orientation was matched against the corrected Event006 ZUL TGA pattern.

## Remaining Risks

- Historical symbol accuracy is not claimed; the manifest identifies this as a fictional Event006 council emblem.
- Source and processed PNG files were not retained in the workspace because the prompt restricted writes to the final TGA files plus manifest/handoff.
- At 10x7, fine emblem detail collapses as expected for HOI4 small flags; the palette, hoist, and central seal remain readable.
