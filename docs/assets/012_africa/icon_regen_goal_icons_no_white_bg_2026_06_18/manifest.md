# 012 Africa Focus/Goal Icon Reprocess Manifest

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_2026_06_18/`
- Asset type: `focus` / `goal` icons only
- Target size: `94x86`
- Final DDS folder: `gfx/interface/goals/012_africa/`
- Existing sprite file kept unchanged: `interface/012_africa.gfx`
- Reference folders inspected before reprocessing:
  - `.agents/skills/chaos-redux-event-assets/assets/focuses`
  - vanilla focus examples under `~/projects/Hearts of Iron IV/gfx/interface/goals`
- Source mode for all assets: `cleaned high-quality source reused from prior dedicated generated focus-source artwork`
- Distinction rule note: this package contains focus/goal icons only. No idea or national-spirit icons were created from these files.
- Contact sheet:
  - `contact_sheets/all_goal_icons_dark_checker_contact.png`

## Assets

| Asset | In-game use | Source PNG | Processed PNG | Final DDS | Sprite name | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `goal_africa_political_congress` | political congress focus family | `source_png/goal_africa_political_congress_source.png` | `processed_png/goal_africa_political_congress.png` | `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` | `GFX_goal_africa_political_congress` | `complete` |
| `goal_africa_charter_league_emblem` | Charter League emblem focus family | `source_png/goal_africa_charter_league_emblem_source.png` | `processed_png/goal_africa_charter_league_emblem.png` | `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` | `GFX_goal_africa_charter_league_emblem` | `complete` |
| `goal_africa_charter_league_diplomacy` | Charter League diplomacy focus family | `source_png/goal_africa_charter_league_diplomacy_source.png` | `processed_png/goal_africa_charter_league_diplomacy.png` | `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds` | `GFX_goal_africa_charter_league_diplomacy` | `complete` |
| `goal_africa_industry_logistics` | industry and logistics focus family | `source_png/goal_africa_industry_logistics_source.png` | `processed_png/goal_africa_industry_logistics.png` | `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds` | `GFX_goal_africa_industry_logistics` | `complete` |
| `goal_africa_military_forces` | military forces focus family | `source_png/goal_africa_military_forces_source.png` | `processed_png/goal_africa_military_forces.png` | `gfx/interface/goals/012_africa/goal_africa_military_forces.dds` | `GFX_goal_africa_military_forces` | `complete` |
| `goal_africa_regional_integration` | regional integration focus family | `source_png/goal_africa_regional_integration_source.png` | `processed_png/goal_africa_regional_integration.png` | `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` | `GFX_goal_africa_regional_integration` | `complete` |
| `goal_africa_authority_atlas` | Authority Atlas focus family | `source_png/goal_africa_authority_atlas_source.png` | `processed_png/goal_africa_authority_atlas.png` | `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` | `GFX_goal_africa_authority_atlas` | `complete` |
| `goal_africa_archive_old_seats` | Archive of Old Seats focus family | `source_png/goal_africa_archive_old_seats_source.png` | `processed_png/goal_africa_archive_old_seats.png` | `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds` | `GFX_goal_africa_archive_old_seats` | `complete` |
| `goal_africa_liberation_war_office` | Liberation War Office focus family | `source_png/goal_africa_liberation_war_office_source.png` | `processed_png/goal_africa_liberation_war_office.png` | `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` | `GFX_goal_africa_liberation_war_office` | `complete` |
| `goal_africa_high_chaos_bestiary` | high-chaos Bestiary focus family | `source_png/goal_africa_high_chaos_bestiary_source.png` | `processed_png/goal_africa_high_chaos_bestiary.png` | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `GFX_goal_africa_high_chaos_bestiary` | `complete` |
| `goal_africa_scramble_for_africa` | Scramble for Africa focus family | `source_png/goal_africa_scramble_for_africa_source.png` | `processed_png/goal_africa_scramble_for_africa.png` | `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` | `GFX_goal_africa_scramble_for_africa` | `complete` |
| `goal_africa_sponsor_paths` | continent-sponsor focus family | `source_png/goal_africa_sponsor_paths_source.png` | `processed_png/goal_africa_sponsor_paths.png` | `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` | `GFX_goal_africa_sponsor_paths` | `complete` |
| `goal_africa_world_order_route` | world-order focus family | `source_png/goal_africa_world_order_route_source.png` | `processed_png/goal_africa_world_order_route.png` | `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` | `GFX_goal_africa_world_order_route` | `complete` |

## Validation notes

- Final processed PNGs are exactly `94x86` RGBA with transparent corners.
- Final DDS files were reconverted in place with `convert -define dds:compression=none`.
- Strict bright-rim scan found `0` opaque white corners and `0` white-halo hits adjacent to transparent pixels across all 13 final processed PNGs.
- No `.gfx`, localisation, focus, idea, event, decision, or scripted files were edited for this icon pass.
- Blocked assets: none.
