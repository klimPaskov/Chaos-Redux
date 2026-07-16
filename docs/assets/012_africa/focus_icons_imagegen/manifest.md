# Event 012 Africa Focus-Family Icon Manifest

## Scope and result

This package supplies the 13 unique static focus-family textures referenced by `common/national_focus/012_africa_continental_focus_tree.txt`. Those sprite IDs appear 276 times in the current tree and were undefined when production began.

Each icon has its own generated source master, transparent intermediate, processed 94 x 86 PNG, and final engine-ready DDS. The package does not edit gameplay, `.gfx`, `.gui`, localisation, spreadsheets, specifications, or existing Event 012 asset sources.

## Package layout

| Surface | Location | Purpose |
| --- | --- | --- |
| Source masters | `source_png/` | Unchanged high-resolution image-generation outputs |
| Alpha intermediates | `alpha_png/` | Soft-matte chroma removals retained for audit and reprocessing |
| Processed masters | `processed_png/` | Final 94 x 86 transparent PNGs before DDS conversion |
| Live textures | `gfx/interface/goals/012_africa/` | Final HOI4 DDS files |
| Prompt ledger | `prompts/focus_icon_prompts.md` | Shared contract, per-icon prompt direction, and rights record |
| Coverage proof | `coverage_crosswalk.md` | Matrix-to-consumer-to-texture mapping |
| Sprite handoff | `gfx_handoff.md` | Ready-to-copy regular and `_shine` definitions |
| Review sheets | `contact_sheets/` | Source, checkerboard, and decoded-DDS contact sheets |
| Validation ledger | `validation/focus_icon_validation.tsv` | Dimensions, alpha, key-color, hashes, DDS, and pixel-equality checks |
| Rebuild script | `process_focus_icons.py` | Deterministic chroma, layout, outline, DDS, contact-sheet, and audit pipeline |

## Format contract

- Final dimensions: 94 x 86 pixels
- Final container: legacy DDS
- Pixel format: uncompressed 32-bit BGRA 8:8:8:8 with explicit alpha
- Mipmaps: none
- DDS caps: `DDSCAPS_TEXTURE`
- Per-file DDS size: 32,464 bytes
- Transparency: real alpha with fully transparent corners; no flat key-color background remains
- Button state: static texture shared by regular and `_shine` sprite definitions; shine uses `gfx/FX/buttonstate.lua`

Rebuild from the mod root with:

```powershell
python -B docs/assets/012_africa/focus_icons_imagegen/process_focus_icons.py
```

The script uses the repository's required DDS converter at `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

## Asset index

For every row below, the file stem is identical across:

- source: `source_png/<stem>_source.png`
- alpha: `alpha_png/<stem>_alpha.png`
- processed: `processed_png/<stem>.png`
- final: `gfx/interface/goals/012_africa/<stem>.dds`

| Live sprite ID | Matrix asset key | Current uses | File stem | Primary read | Package status |
| --- | --- | ---: | --- | --- | --- |
| `GFX_goal_africa_focus_family_host_proclamation` | `focus_family_host_proclamation` | 12 | `goal_africa_focus_family_host_proclamation` | public lectern, microphones, charter | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_host_legitimacy` | `focus_family_host_legitimacy` | 34 | `goal_africa_focus_family_host_legitimacy` | civic chair, ballot box, mandate | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_charter_law` | `focus_family_charter_law` | 25 | `goal_africa_focus_family_charter_law` | open charter, seal, legal scales | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_continental_representation` | `focus_family_continental_representation` | 36 | `goal_africa_focus_family_continental_representation` | equal congress chamber and seats | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_protection_guarantee` | `focus_family_protection_guarantee` | 32 | `goal_africa_focus_family_protection_guarantee` | paired shields and sealed guarantee | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_volunteer_intervention` | `focus_family_volunteer_intervention` | 1 | `goal_africa_focus_family_volunteer_intervention` | volunteer arm, medical satchel, field kit | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_aid_and_relief` | `focus_family_aid_and_relief` | 23 | `goal_africa_focus_family_aid_and_relief` | relief crate, food, water, medicine | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_regional_congress` | `focus_family_regional_congress` | 33 | `goal_africa_focus_family_regional_congress` | round table and equal seats | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_road_corridor` | `focus_family_road_corridor` | 1 | `goal_africa_focus_family_road_corridor` | paved road, bridge, equal gates | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_rail_corridor` | `focus_family_rail_corridor` | 32 | `goal_africa_focus_family_rail_corridor` | locomotive, bridge, converging rails | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_army_common_reserve` | `focus_family_army_common_reserve` | 23 | `goal_africa_focus_family_army_common_reserve` | shared helmets, supply, transport | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_resource_sovereignty` | `focus_family_resource_sovereignty` | 23 | `goal_africa_focus_family_resource_sovereignty` | public resource ledger and revenue scales | asset handed off; registration pending |
| `GFX_goal_africa_focus_family_rival_bloc` | `focus_family_rival_bloc` | 1 | `goal_africa_focus_family_rival_bloc` | opposing equal shields and broken compact | asset handed off; registration pending |

## Matrix reconciliation

All 13 assets are direct matches to exact rows in `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`. There are zero derived assets and zero unmatched requirements in this tranche.

The matrix's suggested names use `<focus_slug>` and its `required_variants` field calls for one distinct icon per final focus. The live tree currently references family-level sprite IDs instead. These 13 textures are therefore the complete baseline package for the current live consumers, not completion of the matrix's broader per-focus icon-family expansion. The matrix was intentionally not edited and its source rows remain `planned`.

## Visual and technical review

The processed checkerboard contact sheet was reviewed at enlarged nearest-neighbour scale. The 13 icons have separate silhouettes and immediately distinguish proclamation, legitimacy, law, representation, mutual protection, intervention, relief, congress, road, rail, reserve, public resources, and bloc rivalry.

The visual pass also confirmed:

- no readable text, real flag, real political emblem, colonial insignia, protected medical emblem, tribal-mask shorthand, animal or safari motif, or ethnic caricature;
- dignified institutional, civilian, relief, and military symbolism;
- no icon is a recolour or transform-only duplicate of another;
- strong edges and central subjects remain readable at focus-icon scale;
- no visible magenta fringe on the transparent result.

The validation ledger records unique normalized pixel hashes for every icon, PNG/DDS pixel equality, alpha extrema and corners, zero visible key-color pixels, exact DDS header fields, no mipmaps, and all source/processed/DDS SHA-256 hashes.

## Provenance and rights

All source masters were generated specifically for this package with the built-in OpenAI image-generation tool. No external image, photograph, emblem, flag, or third-party mod asset was used in a final composition. Vanilla focus icons were inspected only as a technical and stylistic precedent and were not copied, traced, modified, or redistributed here.

There are therefore no third-party attribution, creator-credit, or source-license obligations attached to these 13 files. The unchanged generated source PNGs remain in `source_png/`; the project owner retains responsibility for the repository's overall distribution terms.

## Remaining integration boundary

Texture production is complete. Parent integration still needs to register the 13 regular sprites and 13 `_shine` sprites using `gfx_handoff.md`. That registration is outside this asset-only task's edit boundary, so runtime status remains `registration pending` until the `.gfx` block is added.
