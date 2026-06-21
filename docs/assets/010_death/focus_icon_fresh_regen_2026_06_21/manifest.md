# Event 010 Death Fresh Focus Icon Regeneration Manifest

- Related event id: `010`
- Related event slug: `death`
- Asset type: focus icons
- Package path: `docs/assets/010_death/focus_icon_fresh_regen_2026_06_21/`
- Source mode: `$imagegen` fresh generated source artwork on chroma-key background
- Target size: `94x86`
- Final live DDS folder: `gfx/interface/goals/death/`
- Existing `.gfx` file: `interface/010_death.gfx`
- Supersedes: `docs/assets/010_death/focus_icon_regen_white_artifact_2026_06_21/`
- Reference inspection:
  - `.agents/skills/chaos-redux-event-assets/assets/focuses/`
  - `~/projects/Hearts of Iron IV/gfx/interface/goals/`
- User-reported issue addressed: the prior Death icon pass modified existing icon art; this package replaces the eight requested icons with fresh source artwork.
- Processing summary:
  - generated one independent source PNG per icon on a flat `#00ff00` chroma-key background
  - removed the key background with the imagegen chroma-key helper
  - cropped each alpha subject to its real bounds and centered it on a transparent `94x86` focus canvas
  - converted package DDS copies and replaced the owned live DDS files in `gfx/interface/goals/death/`
- Contact sheets:
  - `contact_sheets/fresh_source_contact_sheet.png`
  - `contact_sheets/fresh_processed_checker_contact_sheet.png`
- Validation:
  - `validation/processing_summary.txt`

| Asset | Sprite | Source PNG | Alpha PNG | Processed PNG | Package DDS | Live DDS | Status | Prompt summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `focus_death_empty_supply` | `GFX_focus_death_empty_supply` | `source_png/focus_death_empty_supply_source.png` | `alpha_png/focus_death_empty_supply_alpha.png` | `processed_png/focus_death_empty_supply.png` | `dds/focus_death_empty_supply.dds` | `gfx/interface/goals/death/focus_death_empty_supply.dds` | `complete` | Empty military supply crate with ration tins, cracked fuel can, and bandages. |
| `focus_death_every_road_slows` | `GFX_focus_death_every_road_slows` | `source_png/focus_death_every_road_slows_source.png` | `alpha_png/focus_death_every_road_slows_alpha.png` | `processed_png/focus_death_every_road_slows.png` | `dds/focus_death_every_road_slows.dds` | `gfx/interface/goals/death/focus_death_every_road_slows.dds` | `complete` | Broken road, rail spur, chain barrier, and fog-bound logistics route. |
| `focus_death_last_shores` | `GFX_focus_death_last_shores` | `source_png/focus_death_last_shores_source.png` | `alpha_png/focus_death_last_shores_alpha.png` | `processed_png/focus_death_last_shores.png` | `dds/focus_death_last_shores.dds` | `gfx/interface/goals/death/focus_death_last_shores.dds` | `complete` | Broken lighthouse lens, abandoned ferry, black tide, and final shoreline. |
| `focus_death_mourning_host` | `GFX_focus_death_mourning_host` | `source_png/focus_death_mourning_host_source.png` | `alpha_png/focus_death_mourning_host_alpha.png` | `processed_png/focus_death_mourning_host.png` | `dds/focus_death_mourning_host.dds` | `gfx/interface/goals/death/focus_death_mourning_host.dds` | `complete` | Funeral war standard, veiled banner, ruined battlefield, and spectral host. |
| `focus_death_orders_without_breath` | `GFX_focus_death_orders_without_breath` | `source_png/focus_death_orders_without_breath_source.png` | `alpha_png/focus_death_orders_without_breath_alpha.png` | `processed_png/focus_death_orders_without_breath.png` | `dds/focus_death_orders_without_breath.dds` | `gfx/interface/goals/death/focus_death_orders_without_breath.dds` | `complete` | Sealed order book, field telephone, dead hand, and wax seal. |
| `focus_death_ruin_host` | `GFX_focus_death_ruin_host` | `source_png/focus_death_ruin_host_source.png` | `alpha_png/focus_death_ruin_host_alpha.png` | `processed_png/focus_death_ruin_host.png` | `dds/focus_death_ruin_host.dds` | `gfx/interface/goals/death/focus_death_ruin_host.dds` | `complete` | Shattered army standard, ruined masonry, broken helmets, and spectral march. |
| `focus_death_state_without_state` | `GFX_focus_death_state_without_state` | `source_png/focus_death_state_without_state_source.png` | `alpha_png/focus_death_state_without_state_alpha.png` | `processed_png/focus_death_state_without_state.png` | `dds/focus_death_state_without_state.dds` | `gfx/interface/goals/death/focus_death_state_without_state.dds` | `complete` | Empty government seal, cracked columns, blank ledger, and hollow state emblem. |
| `focus_death_world_consumed` | `GFX_focus_death_world_consumed` | `source_png/focus_death_world_consumed_source.png` | `alpha_png/focus_death_world_consumed_alpha.png` | `processed_png/focus_death_world_consumed.png` | `dds/focus_death_world_consumed.dds` | `gfx/interface/goals/death/focus_death_world_consumed.dds` | `complete` | Dark globe swallowed by black surf and ash beneath a skull eclipse. |

All eight final live DDS files are `94x86`. The processed PNG validation recorded transparent corner alpha for every icon and the checker contact sheet shows no white or mint square backing.
