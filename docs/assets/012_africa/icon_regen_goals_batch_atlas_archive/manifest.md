# 012 Africa Goal Icon Regeneration Batch

Event id: `012`
Event slug: `africa`
Batch scope: regenerate four existing focus/goal icons with transparent backgrounds and no white matte or halo.
Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/focuses`

## Assets

### `goal_africa_regional_integration`

- asset name: `goal_africa_regional_integration`
- related event id: `012`
- related event slug: `africa`
- asset type: `focus/goal icon`
- intended in-game use: Africa GOAL icon for regional integration route
- source mode: `imagegen`
- prompt summary: stitched regional map fragments connected by route nodes, rails or roads, and bridge spans as one painterly HOI4-style emblem on chroma-key background for alpha removal
- source PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/source_png/goal_africa_regional_integration_source.png`
- processed PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/processed_png/goal_africa_regional_integration.png`
- final DDS: `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds`
- target size: `94x86`
- sprite name: `GFX_goal_africa_regional_integration`
- .gfx file: `existing sprite definition expected; no .gfx edit in this batch`
- related focus: `regional_integration`
- notes: transparent background removed via chroma-key workflow; centered for HOI4 focus icon readability
- asset status: `complete`

### `goal_africa_authority_atlas`

- asset name: `goal_africa_authority_atlas`
- related event id: `012`
- related event slug: `africa`
- asset type: `focus/goal icon`
- intended in-game use: Africa GOAL icon for authority atlas route
- source mode: `imagegen`
- prompt summary: open atlas or ledger with route pins, brass survey instruments, and wax map seals as one painterly HOI4-style emblem on chroma-key background for alpha removal
- source PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/source_png/goal_africa_authority_atlas_source.png`
- processed PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/processed_png/goal_africa_authority_atlas.png`
- final DDS: `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds`
- target size: `94x86`
- sprite name: `GFX_goal_africa_authority_atlas`
- .gfx file: `existing sprite definition expected; no .gfx edit in this batch`
- related focus: `authority_atlas`
- notes: transparent background removed via chroma-key workflow; book angle retained for depth without filling the canvas
- asset status: `complete`

### `goal_africa_archive_old_seats`

- asset name: `goal_africa_archive_old_seats`
- related event id: `012`
- related event slug: `africa`
- asset type: `focus/goal icon`
- intended in-game use: Africa GOAL icon for archive old seats route
- source mode: `imagegen`
- prompt summary: stone stools or thrones, archive ruins, and locked records as one painterly HOI4-style emblem on chroma-key background for alpha removal
- source PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/source_png/goal_africa_archive_old_seats_source.png`
- processed PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/processed_png/goal_africa_archive_old_seats.png`
- final DDS: `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds`
- target size: `94x86`
- sprite name: `GFX_goal_africa_archive_old_seats`
- .gfx file: `existing sprite definition expected; no .gfx edit in this batch`
- related focus: `archive_old_seats`
- notes: transparent background removed via chroma-key workflow; resized to keep throne silhouettes readable
- asset status: `complete`

### `goal_africa_liberation_war_office`

- asset name: `goal_africa_liberation_war_office`
- related event id: `012`
- related event slug: `africa`
- asset type: `focus/goal icon`
- intended in-game use: Africa GOAL icon for liberation war office route
- source mode: `imagegen`
- prompt summary: liberation field office with broken chain, dispatch papers, rifle, and radio as one painterly HOI4-style emblem on chroma-key background for alpha removal
- source PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/source_png/goal_africa_liberation_war_office_source.png`
- processed PNG: `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/processed_png/goal_africa_liberation_war_office.png`
- final DDS: `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds`
- target size: `94x86`
- sprite name: `GFX_goal_africa_liberation_war_office`
- .gfx file: `existing sprite definition expected; no .gfx edit in this batch`
- related focus: `liberation_war_office`
- notes: transparent background removed via chroma-key workflow; diagonal rifle preserved as a structural accent without leaving a matte edge
- asset status: `complete`

## Batch Validation

- DDS conversion: `DXT5`, `94x86`, `TrueColorAlpha` for all four final files
- alpha validation: all four DDS corner samples are `srgba(0,0,0,0)`
- transparency review sheets:
  - `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/contact_sheets/processed_on_dark.png`
  - `docs/assets/012_africa/icon_regen_goals_batch_atlas_archive/contact_sheets/processed_on_checker.png`
- source mode note: generated with built-in `image_gen`, then alpha-cleaned locally with the official chroma-key removal helper
