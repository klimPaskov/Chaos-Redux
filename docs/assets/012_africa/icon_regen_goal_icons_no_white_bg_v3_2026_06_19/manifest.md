# Event 012 Africa Goal Icon Rebuild v3

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v3_2026_06_19/`
- Asset type: focus / goal icons
- Target size: `94x86`
- Final DDS folder: `gfx/interface/goals/012_africa/`
- Existing sprite file kept unchanged: `interface/012_africa.gfx`
- Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- Source mode: dedicated Event 012 goal-icon source art, then local alpha cleanup, white-matte removal, fit-to-focus canvas, and DDS rebuild
- Status: `complete`

## Processing Summary

- Rebuilt all 13 live Event 012 Africa focus icons from the dedicated high-resolution goal source PNGs in `source_png/`.
- Removed border-connected white/off-white matte and chroma residue.
- Cleared white edge highlights adjacent to transparent pixels and aged remaining near-white subject highlights so they do not read as square white backplates.
- Recentered each subject on a transparent `94x86` focus canvas.
- Zeroed RGB under `alpha=0` to prevent hidden matte bleed in DDS consumers.
- Converted package and live files to `94x86` `ARGB8888` DDS with unchanged filenames and sprite names.
- No idea icons were used as source artwork.

## Asset List

| Asset | Source note | Source PNG | Processed PNG | Package DDS | Live DDS | Sprite | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `goal_africa_archive_old_seats` | stone seats, archive ledgers, old authority markers | `source_png/goal_africa_archive_old_seats_source.png` | `processed_png/goal_africa_archive_old_seats.png` | `dds/goal_africa_archive_old_seats.dds` | `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds` | `GFX_goal_africa_archive_old_seats` | `complete` |
| `goal_africa_authority_atlas` | atlas book, compass, and authority route pins | `source_png/goal_africa_authority_atlas_source.png` | `processed_png/goal_africa_authority_atlas.png` | `dds/goal_africa_authority_atlas.dds` | `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` | `GFX_goal_africa_authority_atlas` | `complete` |
| `goal_africa_charter_league_diplomacy` | treaty instruments, diplomacy hands, and league seal | `source_png/goal_africa_charter_league_diplomacy_source.png` | `processed_png/goal_africa_charter_league_diplomacy.png` | `dds/goal_africa_charter_league_diplomacy.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds` | `GFX_goal_africa_charter_league_diplomacy` | `complete` |
| `goal_africa_charter_league_emblem` | Charter League seal and bronze wreath | `source_png/goal_africa_charter_league_emblem_source.png` | `processed_png/goal_africa_charter_league_emblem.png` | `dds/goal_africa_charter_league_emblem.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` | `GFX_goal_africa_charter_league_emblem` | `complete` |
| `goal_africa_high_chaos_bestiary` | dark bestiary pages and occult animal-court mask | `source_png/goal_africa_high_chaos_bestiary_source.png` | `processed_png/goal_africa_high_chaos_bestiary.png` | `dds/goal_africa_high_chaos_bestiary.dds` | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `GFX_goal_africa_high_chaos_bestiary` | `complete` |
| `goal_africa_industry_logistics` | industrial sphere, rails, and logistics metalwork | `source_png/goal_africa_industry_logistics_source.png` | `processed_png/goal_africa_industry_logistics.png` | `dds/goal_africa_industry_logistics.dds` | `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds` | `GFX_goal_africa_industry_logistics` | `complete` |
| `goal_africa_liberation_war_office` | field dispatch tent, orders, and liberation administration | `source_png/goal_africa_liberation_war_office_source.png` | `processed_png/goal_africa_liberation_war_office.png` | `dds/goal_africa_liberation_war_office.dds` | `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` | `GFX_goal_africa_liberation_war_office` | `complete` |
| `goal_africa_military_forces` | shield, spears, and mobilization emblem | `source_png/goal_africa_military_forces_source.png` | `processed_png/goal_africa_military_forces.png` | `dds/goal_africa_military_forces.dds` | `gfx/interface/goals/012_africa/goal_africa_military_forces.dds` | `GFX_goal_africa_military_forces` | `complete` |
| `goal_africa_political_congress` | continental delegates around a congress table | `source_png/goal_africa_political_congress_source.png` | `processed_png/goal_africa_political_congress.png` | `dds/goal_africa_political_congress.dds` | `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` | `GFX_goal_africa_political_congress` | `complete` |
| `goal_africa_regional_integration` | linked continental regions and integration nodes | `source_png/goal_africa_regional_integration_source.png` | `processed_png/goal_africa_regional_integration.png` | `dds/goal_africa_regional_integration.dds` | `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` | `GFX_goal_africa_regional_integration` | `complete` |
| `goal_africa_scramble_for_africa` | torn map and broken scramble weapons | `source_png/goal_africa_scramble_for_africa_source.png` | `processed_png/goal_africa_scramble_for_africa.png` | `dds/goal_africa_scramble_for_africa.dds` | `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` | `GFX_goal_africa_scramble_for_africa` | `complete` |
| `goal_africa_sponsor_paths` | compass and external sponsor-route instruments | `source_png/goal_africa_sponsor_paths_source.png` | `processed_png/goal_africa_sponsor_paths.png` | `dds/goal_africa_sponsor_paths.dds` | `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` | `GFX_goal_africa_sponsor_paths` | `complete` |
| `goal_africa_world_order_route` | continent globe, laurels, and world-order seal | `source_png/goal_africa_world_order_route_source.png` | `processed_png/goal_africa_world_order_route.png` | `dds/goal_africa_world_order_route.dds` | `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` | `GFX_goal_africa_world_order_route` | `complete` |

## Validation Evidence

- Processed PNG contact sheets:
  - `contact_sheets/goal_icons_v3_processed_checker_contact.png`
  - `contact_sheets/goal_icons_v3_processed_dark_contact.png`
- Live DDS roundtrip contact sheets:
  - `contact_sheets/goal_icons_v3_live_dds_checker_contact.png`
  - `contact_sheets/goal_icons_v3_live_dds_dark_contact.png`
- Validation file:
  - `validation/goal_icons_v3_validation.json`

## Validation Summary

All 13 processed PNGs and all 13 live DDS files:

- exist at the exact `94x86` target size
- report transparent corners
- have fully transparent unused canvas
- have RGB cleared under `alpha=0`
- have no non-transparent border pixels
- have no detected white/off-white edge matte pixels in the live DDS audit
- remain wired through existing `GFX_goal_africa_*` sprite names in `interface/012_africa.gfx`

No `.gfx`, localisation, gameplay, focus, idea, decision, event, GUI, script, history, spreadsheet, or unrelated asset files were edited during this pass.
