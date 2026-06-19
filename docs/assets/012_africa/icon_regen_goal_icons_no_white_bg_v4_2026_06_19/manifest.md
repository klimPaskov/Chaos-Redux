# 012 Africa Goal Icon Transparent Reprocess Package

- Event id: `012`
- Event slug: `africa`
- Package: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v4_2026_06_19/`
- Asset type: focus/goal icons
- Target size: `94x86`
- Scope note: this package only reprocessed the live 012 Africa goal-icon asset set and replaced the final DDS files under `gfx/interface/goals/012_africa/`.
- Source separation note: all source PNGs in this package were extracted from the live `goal_*.dds` focus/goal icon set. None were derived from the 012 Africa idea icons.

## Workflow

- Reference folder inspected: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- Source mode: existing goal-icon source art cleanup and alpha-safe reprocess
- Processing note: semi-transparent edge RGB was repacked from nearby painted pixels, fully transparent pixels were zeroed, and stray very-low-alpha fringe pixels were removed to avoid white matte or pale halo artifacts over variable UI backgrounds.
- DDS note: the repo helper `.tools/convert_to_dds.py` hit its known ffmpeg fallback header bug on this checkout, so the processed PNGs were saved to DDS via Pillow for this package instead of patching repo tooling outside the allowed asset scope.

## Assets

| Asset name | Sprite name | Source PNG | Processed PNG | Package DDS | Live DDS | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `goal_africa_political_congress` | `GFX_goal_africa_political_congress` | `source_png/goal_africa_political_congress_source.png` | `processed_png/goal_africa_political_congress.png` | `dds/goal_africa_political_congress.dds` | `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` | `complete` | Congress seat-and-wreath focus icon preserved as focus art with cleaned transparent edge pixels. |
| `goal_africa_charter_league_emblem` | `GFX_goal_africa_charter_league_emblem` | `source_png/goal_africa_charter_league_emblem_source.png` | `processed_png/goal_africa_charter_league_emblem.png` | `dds/goal_africa_charter_league_emblem.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` | `complete` | Central charter seal preserved; transparent unused canvas retained. |
| `goal_africa_charter_league_diplomacy` | `GFX_goal_africa_charter_league_diplomacy` | `source_png/goal_africa_charter_league_diplomacy_source.png` | `processed_png/goal_africa_charter_league_diplomacy.png` | `dds/goal_africa_charter_league_diplomacy.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds` | `complete` | Diplomatic badge focus icon retained and alpha-cleaned. |
| `goal_africa_industry_logistics` | `GFX_goal_africa_industry_logistics` | `source_png/goal_africa_industry_logistics_source.png` | `processed_png/goal_africa_industry_logistics.png` | `dds/goal_africa_industry_logistics.dds` | `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds` | `complete` | Industrial rail-and-cargo focus art retained; matte risk removed from edge pixels. |
| `goal_africa_military_forces` | `GFX_goal_africa_military_forces` | `source_png/goal_africa_military_forces_source.png` | `processed_png/goal_africa_military_forces.png` | `dds/goal_africa_military_forces.dds` | `gfx/interface/goals/012_africa/goal_africa_military_forces.dds` | `complete` | Military crest focus icon reprocessed to preserve transparency and readability. |
| `goal_africa_regional_integration` | `GFX_goal_africa_regional_integration` | `source_png/goal_africa_regional_integration_source.png` | `processed_png/goal_africa_regional_integration.png` | `dds/goal_africa_regional_integration.dds` | `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` | `complete` | Map-chain emblem preserved as focus-sized art, not resized from another icon type. |
| `goal_africa_authority_atlas` | `GFX_goal_africa_authority_atlas` | `source_png/goal_africa_authority_atlas_source.png` | `processed_png/goal_africa_authority_atlas.png` | `dds/goal_africa_authority_atlas.dds` | `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` | `complete` | Open atlas focus icon retained with cleaned transparent fringe. |
| `goal_africa_archive_old_seats` | `GFX_goal_africa_archive_old_seats` | `source_png/goal_africa_archive_old_seats_source.png` | `processed_png/goal_africa_archive_old_seats.png` | `dds/goal_africa_archive_old_seats.dds` | `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds` | `complete` | Archive-city silhouette preserved; no opaque square background remains. |
| `goal_africa_liberation_war_office` | `GFX_goal_africa_liberation_war_office` | `source_png/goal_africa_liberation_war_office_source.png` | `processed_png/goal_africa_liberation_war_office.png` | `dds/goal_africa_liberation_war_office.dds` | `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` | `complete` | War-office plaque focus icon reprocessed for clean alpha. |
| `goal_africa_high_chaos_bestiary` | `GFX_goal_africa_high_chaos_bestiary` | `source_png/goal_africa_high_chaos_bestiary_source.png` | `processed_png/goal_africa_high_chaos_bestiary.png` | `dds/goal_africa_high_chaos_bestiary.dds` | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `complete` | Bestiary mask-and-foliage focus icon retained with darkened fringe pixels to avoid pale haloing. |
| `goal_africa_scramble_for_africa` | `GFX_goal_africa_scramble_for_africa` | `source_png/goal_africa_scramble_for_africa_source.png` | `processed_png/goal_africa_scramble_for_africa.png` | `dds/goal_africa_scramble_for_africa.dds` | `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` | `complete` | Crossed-rifle map focus icon retained; transparent corners and non-square alpha preserved. |
| `goal_africa_sponsor_paths` | `GFX_goal_africa_sponsor_paths` | `source_png/goal_africa_sponsor_paths_source.png` | `processed_png/goal_africa_sponsor_paths.png` | `dds/goal_africa_sponsor_paths.dds` | `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` | `complete` | Compass-and-rifle icon retained and reprocessed to remove matte risk around metallic edges. |
| `goal_africa_world_order_route` | `GFX_goal_africa_world_order_route` | `source_png/goal_africa_world_order_route_source.png` | `processed_png/goal_africa_world_order_route.png` | `dds/goal_africa_world_order_route.dds` | `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` | `complete` | Laurel-globe focus icon preserved with cleaned transparent unused canvas. |

## Validation Artifacts

- `contact_sheets/source_contact_sheet.png`
- `contact_sheets/processed_contact_sheet.png`
- `contact_sheets/live_dds_contact_sheet.png`
- `validation/validation_metrics.json`
- `validation/validation_summary.md`
