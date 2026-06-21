# Event 012 Africa Goal Icon Regeneration

Event: `12`
Slug: `africa`
Package root: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v6_2026_06_21/`
Asset type: focus/goal icons
Target size: `94x86`
Source mode: generated symbolic icon source art, reprocessed from the prior generated source PNGs with stricter chroma-key removal, edge decontamination, transparent RGB cleanup, and live DDS replacement.

All assets in this package use transparent unused canvas. The live DDS outputs were written to the existing `gfx/interface/goals/012_africa/` paths and keep the existing `GFX_goal_africa_*` sprite names from `interface/012_africa.gfx`.

| Asset | Sprite | Source PNG | Processed PNG | Package DDS | Live DDS | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `goal_africa_archive_old_seats` | `GFX_goal_africa_archive_old_seats` | `source_png/goal_africa_archive_old_seats_source.png` | `processed_png/goal_africa_archive_old_seats.png` | `dds/goal_africa_archive_old_seats.dds` | `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds` | `complete` |
| `goal_africa_authority_atlas` | `GFX_goal_africa_authority_atlas` | `source_png/goal_africa_authority_atlas_source.png` | `processed_png/goal_africa_authority_atlas.png` | `dds/goal_africa_authority_atlas.dds` | `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` | `complete` |
| `goal_africa_charter_league_diplomacy` | `GFX_goal_africa_charter_league_diplomacy` | `source_png/goal_africa_charter_league_diplomacy_source.png` | `processed_png/goal_africa_charter_league_diplomacy.png` | `dds/goal_africa_charter_league_diplomacy.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds` | `complete` |
| `goal_africa_charter_league_emblem` | `GFX_goal_africa_charter_league_emblem` | `source_png/goal_africa_charter_league_emblem_source.png` | `processed_png/goal_africa_charter_league_emblem.png` | `dds/goal_africa_charter_league_emblem.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` | `complete` |
| `goal_africa_high_chaos_bestiary` | `GFX_goal_africa_high_chaos_bestiary` | `source_png/goal_africa_high_chaos_bestiary_source.png` | `processed_png/goal_africa_high_chaos_bestiary.png` | `dds/goal_africa_high_chaos_bestiary.dds` | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `complete` |
| `goal_africa_industry_logistics` | `GFX_goal_africa_industry_logistics` | `source_png/goal_africa_industry_logistics_source.png` | `processed_png/goal_africa_industry_logistics.png` | `dds/goal_africa_industry_logistics.dds` | `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds` | `complete` |
| `goal_africa_liberation_war_office` | `GFX_goal_africa_liberation_war_office` | `source_png/goal_africa_liberation_war_office_source.png` | `processed_png/goal_africa_liberation_war_office.png` | `dds/goal_africa_liberation_war_office.dds` | `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` | `complete` |
| `goal_africa_military_forces` | `GFX_goal_africa_military_forces` | `source_png/goal_africa_military_forces_source.png` | `processed_png/goal_africa_military_forces.png` | `dds/goal_africa_military_forces.dds` | `gfx/interface/goals/012_africa/goal_africa_military_forces.dds` | `complete` |
| `goal_africa_political_congress` | `GFX_goal_africa_political_congress` | `source_png/goal_africa_political_congress_source.png` | `processed_png/goal_africa_political_congress.png` | `dds/goal_africa_political_congress.dds` | `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` | `complete` |
| `goal_africa_regional_integration` | `GFX_goal_africa_regional_integration` | `source_png/goal_africa_regional_integration_source.png` | `processed_png/goal_africa_regional_integration.png` | `dds/goal_africa_regional_integration.dds` | `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` | `complete` |
| `goal_africa_scramble_for_africa` | `GFX_goal_africa_scramble_for_africa` | `source_png/goal_africa_scramble_for_africa_source.png` | `processed_png/goal_africa_scramble_for_africa.png` | `dds/goal_africa_scramble_for_africa.dds` | `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` | `complete` |
| `goal_africa_sponsor_paths` | `GFX_goal_africa_sponsor_paths` | `source_png/goal_africa_sponsor_paths_source.png` | `processed_png/goal_africa_sponsor_paths.png` | `dds/goal_africa_sponsor_paths.dds` | `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` | `complete` |
| `goal_africa_world_order_route` | `GFX_goal_africa_world_order_route` | `source_png/goal_africa_world_order_route_source.png` | `processed_png/goal_africa_world_order_route.png` | `dds/goal_africa_world_order_route.dds` | `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` | `complete` |

## Review Assets

- Processed checker contact sheet: `contact_sheets/processed_checker_contact.png`
- Live DDS checker contact sheet: `contact_sheets/live_dds_checker_contact.png`
- Processed dark contact sheet: `contact_sheets/processed_dark_contact.png`
- Live DDS dark contact sheet: `contact_sheets/live_dds_dark_contact.png`
- Alpha validation: `validation/validation_summary.md`

## Validation Summary

Every processed PNG and live DDS is `94x86`. All four corners are fully transparent. Transparent pixels have black RGB, not a white matte. The validation found zero transparent white RGB pixels, zero low-alpha bright halo pixels, and zero border-connected opaque light-background pixels for every live DDS.
