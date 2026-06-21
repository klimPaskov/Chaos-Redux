# Event 010 Death Focus Icon Regeneration Manifest

- Related event id: `010`
- Related event slug: `death`
- Asset type: focus icons
- Package path: `docs/assets/010_death/focus_icon_regen_white_artifact_2026_06_21/`
- Source mode: existing Chaos Redux live DDS extracted to PNG, then deterministically rebuilt
- Target size: `94x86`
- Final live DDS folder: `gfx/interface/goals/death/`
- Existing `.gfx` file: `interface/010_death.gfx`
- Reference inspection:
  - `.agents/skills/chaos-redux-event-assets/assets/focuses/`
  - `~/projects/Hearts of Iron IV/gfx/interface/goals/`
- User-reported issue addressed: opaque square / white-artifact presentation around Death focus icons
- Processing summary:
  - extracted each live DDS to `source_png/`
  - removed edge-connected matte/background pixels while preserving the painted circular focus badge
  - recentered each cleaned icon on a transparent `94x86` focus canvas
  - exported package DDS copies under `dds/` and replaced the owned live DDS files in `gfx/interface/goals/death/`
- Contact sheets:
  - `contact_sheets/source_contact_sheet.png`
  - `contact_sheets/processed_contact_sheet.png`
  - `contact_sheets/processed_checker_contact_sheet.png`
- Validation: `validation/validation_summary.md`

| Asset | Sprite | Source PNG | Processed PNG | Package DDS | Live DDS | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `focus_death_empty_supply` | `GFX_focus_death_empty_supply` | `source_png/focus_death_empty_supply_source.png` | `processed_png/focus_death_empty_supply.png` | `dds/focus_death_empty_supply.dds` | `gfx/interface/goals/death/focus_death_empty_supply.dds` | `complete` | Removed opaque square background and preserved the circular supply-medallion composition. |
| `focus_death_every_road_slows` | `GFX_focus_death_every_road_slows` | `source_png/focus_death_every_road_slows_source.png` | `processed_png/focus_death_every_road_slows.png` | `dds/focus_death_every_road_slows.dds` | `gfx/interface/goals/death/focus_death_every_road_slows.dds` | `complete` | Rebuilt as transparent-canvas focus art without the old matte. |
| `focus_death_last_shores` | `GFX_focus_death_last_shores` | `source_png/focus_death_last_shores_source.png` | `processed_png/focus_death_last_shores.png` | `dds/focus_death_last_shores.dds` | `gfx/interface/goals/death/focus_death_last_shores.dds` | `complete` | Circular badge retained; unused canvas is now transparent. |
| `focus_death_mourning_host` | `GFX_focus_death_mourning_host` | `source_png/focus_death_mourning_host_source.png` | `processed_png/focus_death_mourning_host.png` | `dds/focus_death_mourning_host.dds` | `gfx/interface/goals/death/focus_death_mourning_host.dds` | `complete` | Edge-connected backdrop removed and focus icon recentered. |
| `focus_death_orders_without_breath` | `GFX_focus_death_orders_without_breath` | `source_png/focus_death_orders_without_breath_source.png` | `processed_png/focus_death_orders_without_breath.png` | `dds/focus_death_orders_without_breath.dds` | `gfx/interface/goals/death/focus_death_orders_without_breath.dds` | `complete` | Transparent canvas restored around the existing Death badge art. |
| `focus_death_ruin_host` | `GFX_focus_death_ruin_host` | `source_png/focus_death_ruin_host_source.png` | `processed_png/focus_death_ruin_host.png` | `dds/focus_death_ruin_host.dds` | `gfx/interface/goals/death/focus_death_ruin_host.dds` | `complete` | Replaced the old full-tile backing with clean alpha. |
| `focus_death_state_without_state` | `GFX_focus_death_state_without_state` | `source_png/focus_death_state_without_state_source.png` | `processed_png/focus_death_state_without_state.png` | `dds/focus_death_state_without_state.dds` | `gfx/interface/goals/death/focus_death_state_without_state.dds` | `complete` | Clean transparent focus canvas; no white/off-white border artifact remains. |
| `focus_death_world_consumed` | `GFX_focus_death_world_consumed` | `source_png/focus_death_world_consumed_source.png` | `processed_png/focus_death_world_consumed.png` | `dds/focus_death_world_consumed.dds` | `gfx/interface/goals/death/focus_death_world_consumed.dds` | `complete` | Final icon keeps the original world-end badge while removing the square matte. |

Validation summary: all eight processed PNGs and owned live DDS files are `94x86`, all four corners are fully transparent, and the validation recorded `0` transparent white RGB pixels, `0` guide-green pixels, and `0` border-connected light matte pixels across the batch.
