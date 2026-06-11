# Fury Achievement Icon Regeneration Manifest

- Related event id: `007`
- Related event slug: `fury`
- Asset package: `achievement icons`
- Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/achievements`
- Source mode summary:
  - 9 base icons: `$imagegen` source art generated earlier and copied into this package
  - 1 base icon: locally derived from the generated Fury dossier/source family as instructed
- Target size: `64x64`
- Final output folder: `gfx/achievements/`
- Contact sheet: `docs/assets/007_fury/achievements_regen/contact_sheets/fury_achievement_regen_sheet.png`
- Sprite references: preserved existing achievement filenames; no `.gfx` changes

## Prompts

- `achievement_fury_fuse_cut`
  - Prompt: HOI4-style achievement icon showing emergency shears cutting a lit artillery fuse over a dark wartime operations map, flare dying out, painterly aged WW2 strategy UI art, bronze/laurel medal framing, readable at small size, no text or neon.
- `achievement_fury_no_minor_major`
  - Prompt: HOI4-style achievement icon showing a small brass map marker halted before becoming a major, with a cracked high-rank insignia over a wartime operations map, painterly medal presentation, subdued WW2 administrative palette.
- `achievement_fury_firebreak`
  - Prompt: HOI4-style achievement icon showing a defensive barricade cutting across a burning border on a war map, containment symbolism, painterly strategy medal art, strong value contrast.
- `achievement_fury_pact_breaker`
  - Prompt: HOI4-style achievement icon showing a broken pact seal on war-office papers, cracked red wax, snapped clasp, torn command ribbon over a dark treaty folder, aged brass frame, readable at `64x64`.
- `achievement_fury_ten_fires`
  - Prompt: HOI4-style achievement icon showing many small outbreak pins across a globe or operations map, maximum spread without text or numbers, painterly bronze-framed war-room medal treatment.
- `achievement_fury_last_neighbor`
  - Prompt: HOI4-style achievement icon showing the last adjacent border file and final neighbor marker on a war-office ledger, quiet administrative finality, painterly medal framing.
- `achievement_fury_world_without_fury`
  - Prompt: HOI4-style achievement icon showing a dark globe with a single cold brass pin and only a faint wisp of smoke, quiet containment, no active flames, aged WW2 UI medal styling.
- `achievement_fury_rivals_burn`
  - Prompt: HOI4-style achievement icon showing two opposing Fury outbreak markers or rival war files turning on each other, painterly bronze-framed administrative conflict symbol.
- `achievement_fury_major_without_faction`
  - Prompt: HOI4-style achievement icon showing a fallen major-power standard or major-rank emblem standing alone without supporting alliance banners, isolated and defeated, painterly medal icon.
- `achievement_fury_no_cores`
  - Prompt/source note: not separately generated. Derived locally from `achievement_fury_last_neighbor_source.png` by adding a crossed denial-stamp treatment over the dossier papers to fit the requested “denied core papers” concept while preserving the same source family.

## Asset Entries

### `achievement_fury_fuse_cut`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_fuse_cut_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_fuse_cut.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_fuse_cut_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_fuse_cut_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_fuse_cut.dds`
  - `gfx/achievements/achievement_fury_fuse_cut_grey.dds`
  - `gfx/achievements/achievement_fury_fuse_cut_not_eligible.dds`
- Target size: `64x64`
- Notes: completed source kept warm and high-contrast; grey and locked variants derived locally from the completed preview
- Asset status: `complete`

### `achievement_fury_no_minor_major`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_no_minor_major_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_minor_major.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_minor_major_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_minor_major_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_no_minor_major.dds`
  - `gfx/achievements/achievement_fury_no_minor_major_grey.dds`
  - `gfx/achievements/achievement_fury_no_minor_major_not_eligible.dds`
- Target size: `64x64`
- Notes: map pin and broken rank badge retained as the central subject
- Asset status: `complete`

### `achievement_fury_firebreak`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_firebreak_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_firebreak.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_firebreak_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_firebreak_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_firebreak.dds`
  - `gfx/achievements/achievement_fury_firebreak_grey.dds`
  - `gfx/achievements/achievement_fury_firebreak_not_eligible.dds`
- Target size: `64x64`
- Notes: strongest flame treatment in the set, but still framed as containment rather than fantasy fire
- Asset status: `complete`

### `achievement_fury_pact_breaker`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_pact_breaker_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_pact_breaker.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_pact_breaker_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_pact_breaker_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_pact_breaker.dds`
  - `gfx/achievements/achievement_fury_pact_breaker_grey.dds`
  - `gfx/achievements/achievement_fury_pact_breaker_not_eligible.dds`
- Target size: `64x64`
- Notes: pact seal and torn ribbon remain the main read after resize
- Asset status: `complete`

### `achievement_fury_ten_fires`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_ten_fires_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_ten_fires.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_ten_fires_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_ten_fires_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_ten_fires.dds`
  - `gfx/achievements/achievement_fury_ten_fires_grey.dds`
  - `gfx/achievements/achievement_fury_ten_fires_not_eligible.dds`
- Target size: `64x64`
- Notes: brighter map-wide spark distribution kept visible without resorting to literal numerals
- Asset status: `complete`

### `achievement_fury_last_neighbor`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_last_neighbor_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_last_neighbor.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_last_neighbor_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_last_neighbor_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_last_neighbor.dds`
  - `gfx/achievements/achievement_fury_last_neighbor_grey.dds`
  - `gfx/achievements/achievement_fury_last_neighbor_not_eligible.dds`
- Target size: `64x64`
- Notes: ledger dossier and single pin act as the central read
- Asset status: `complete`

### `achievement_fury_world_without_fury`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_world_without_fury_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_world_without_fury.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_world_without_fury_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_world_without_fury_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_world_without_fury.dds`
  - `gfx/achievements/achievement_fury_world_without_fury_grey.dds`
  - `gfx/achievements/achievement_fury_world_without_fury_not_eligible.dds`
- Target size: `64x64`
- Notes: subdued globe and extinguished marker intentionally quieter than the rest of the set
- Asset status: `complete`

### `achievement_fury_rivals_burn`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_rivals_burn_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_rivals_burn.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_rivals_burn_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_rivals_burn_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_rivals_burn.dds`
  - `gfx/achievements/achievement_fury_rivals_burn_grey.dds`
  - `gfx/achievements/achievement_fury_rivals_burn_not_eligible.dds`
- Target size: `64x64`
- Notes: the split medallion read was preserved for high readability
- Asset status: `complete`

### `achievement_fury_major_without_faction`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `$imagegen`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_major_without_faction_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_major_without_faction.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_major_without_faction_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_major_without_faction_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_major_without_faction.dds`
  - `gfx/achievements/achievement_fury_major_without_faction_grey.dds`
  - `gfx/achievements/achievement_fury_major_without_faction_not_eligible.dds`
- Target size: `64x64`
- Notes: isolated standard and damaged badge preserved as the dominant read
- Asset status: `complete`

### `achievement_fury_no_cores`

- Asset type: `achievement`
- Intended in-game use: completed/grey/not-eligible Fury achievement icon set
- Source mode: `derived_from_generated`
- Source PNG: `docs/assets/007_fury/achievements_regen/source_png/achievement_fury_no_cores_source.png`
- Processed PNGs:
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_cores.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_cores_grey.png`
  - `docs/assets/007_fury/achievements_regen/processed_png/achievement_fury_no_cores_not_eligible.png`
- Final DDS paths:
  - `gfx/achievements/achievement_fury_no_cores.dds`
  - `gfx/achievements/achievement_fury_no_cores_grey.dds`
  - `gfx/achievements/achievement_fury_no_cores_not_eligible.dds`
- Target size: `64x64`
- Notes: derived from the generated dossier family with a crossed denial stamp to fit the “denied core papers” brief without adding a new unrelated source
- Asset status: `complete`

## Variant Method

- Grey variants were derived locally from the completed processed PNGs using grayscale conversion, restrained retinting, and contrast balancing to keep medal framing readable at `64x64`.
- `not_eligible` variants were derived locally from the grey previews with a bold red crossed-lock overlay to match the established HOI4 achievement pattern.

## Validation

- Confirmed all 30 final DDS files exist under `gfx/achievements/`
- Confirmed every final DDS is `64x64`
- Confirmed processed PNG previews exist for every final DDS filename
- Confirmed source PNG set exists for all 10 completed achievement concepts
- Confirmed final contact sheet exists
