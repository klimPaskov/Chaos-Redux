# Event 012 Africa Goal Icon Regeneration v3

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v3_2026_06_20/`
- Asset type: `focus/goal icons`
- Target size: `94x86`
- Source mode: generated symbolic focus art through built-in `image_gen` and `chaosx_icon_artist` source outputs, copied into this package and processed with local chroma-key alpha extraction.
- Final DDS folder: `gfx/interface/goals/012_africa/`
- Existing `.gfx` file kept unchanged: `interface/012_africa.gfx`
- Status: `complete` for all 13 live Event 012 Africa goal icons.

No idea or national-spirit icon was used as a source. Goal icons remain a separate focus-size asset family.

## Assets

| Asset | Sprite | Intended use | Final source subject | Source PNG | Processed PNG | Package DDS | Live DDS | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `goal_africa_political_congress` | `GFX_goal_africa_political_congress` | political congress focus routes | circular congress table and Africa mandate seal | `source_png/goal_africa_political_congress_source.png` | `processed_png/goal_africa_political_congress.png` | `dds/goal_africa_political_congress.dds` | `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` | `complete` |
| `goal_africa_charter_league_emblem` | `GFX_goal_africa_charter_league_emblem` | Charter League emblem routes | charter shield, seals, and laurel | `source_png/goal_africa_charter_league_emblem_source.png` | `processed_png/goal_africa_charter_league_emblem.png` | `dds/goal_africa_charter_league_emblem.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` | `complete` |
| `goal_africa_charter_league_diplomacy` | `GFX_goal_africa_charter_league_diplomacy` | Charter League diplomacy routes | hands, charter badge, crossed diplomatic emblems | `source_png/goal_africa_charter_league_diplomacy_source.png` | `processed_png/goal_africa_charter_league_diplomacy.png` | `dds/goal_africa_charter_league_diplomacy.dds` | `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds` | `complete` |
| `goal_africa_industry_logistics` | `GFX_goal_africa_industry_logistics` | industry and logistics routes | rail depot, gear, crates, and logistics yard | `source_png/goal_africa_industry_logistics_source.png` | `processed_png/goal_africa_industry_logistics.png` | `dds/goal_africa_industry_logistics.dds` | `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds` | `complete` |
| `goal_africa_military_forces` | `GFX_goal_africa_military_forces` | military force routes | rifles, globe shield, helmet, and mobilization wings | `source_png/goal_africa_military_forces_source.png` | `processed_png/goal_africa_military_forces.png` | `dds/goal_africa_military_forces.dds` | `gfx/interface/goals/012_africa/goal_africa_military_forces.dds` | `complete` |
| `goal_africa_regional_integration` | `GFX_goal_africa_regional_integration` | regional integration routes | Africa network map, pins, and regional links | `source_png/goal_africa_regional_integration_source.png` | `processed_png/goal_africa_regional_integration.png` | `dds/goal_africa_regional_integration.dds` | `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` | `complete` |
| `goal_africa_authority_atlas` | `GFX_goal_africa_authority_atlas` | Authority Atlas routes | open atlas, Africa map, and compass | `source_png/goal_africa_authority_atlas_source.png` | `processed_png/goal_africa_authority_atlas.png` | `dds/goal_africa_authority_atlas.dds` | `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` | `complete` |
| `goal_africa_archive_old_seats` | `GFX_goal_africa_archive_old_seats` | Archive of Old Seats routes | old stools, tablets, records, and seals | `source_png/goal_africa_archive_old_seats_source.png` | `processed_png/goal_africa_archive_old_seats.png` | `dds/goal_africa_archive_old_seats.dds` | `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds` | `complete` |
| `goal_africa_liberation_war_office` | `GFX_goal_africa_liberation_war_office` | Liberation War Office routes | field radios, sealed folder, banner, and rifles | `source_png/goal_africa_liberation_war_office_source.png` | `processed_png/goal_africa_liberation_war_office.png` | `dds/goal_africa_liberation_war_office.dds` | `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` | `complete` |
| `goal_africa_high_chaos_bestiary` | `GFX_goal_africa_high_chaos_bestiary` | high-chaos Bestiary routes | fictional bestiary mask and warning seal | `source_png/goal_africa_high_chaos_bestiary_source.png` | `processed_png/goal_africa_high_chaos_bestiary.png` | `dds/goal_africa_high_chaos_bestiary.dds` | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `complete` |
| `goal_africa_scramble_for_africa` | `GFX_goal_africa_scramble_for_africa` | Scramble for Africa reversal routes | torn colonial map, broken blades, and seals | `source_png/goal_africa_scramble_for_africa_source.png` | `processed_png/goal_africa_scramble_for_africa.png` | `dds/goal_africa_scramble_for_africa.dds` | `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` | `complete` |
| `goal_africa_sponsor_paths` | `GFX_goal_africa_sponsor_paths` | continent-sponsor routes | compass hub with route cords to other continents | `source_png/goal_africa_sponsor_paths_source.png` | `processed_png/goal_africa_sponsor_paths.png` | `dds/goal_africa_sponsor_paths.dds` | `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` | `complete` |
| `goal_africa_world_order_route` | `GFX_goal_africa_world_order_route` | world-order and terminal routes | dark globe centered on Africa with charter seal | `source_png/goal_africa_world_order_route_source.png` | `processed_png/goal_africa_world_order_route.png` | `dds/goal_africa_world_order_route.dds` | `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` | `complete` |

## Processing

- Source PNGs were copied into `source_png/`; original generated-image cache files were left in place.
- Chroma-key backgrounds were removed into real alpha with the installed imagegen chroma-key helper.
- Icons were centered on transparent `94x86` canvases and transparent pixels were blackened under alpha to prevent matte bleed.
- DDS outputs were converted as uncompressed ARGB8888 through ImageMagick because `.tools/convert_to_dds.py` still hits the known ffmpeg fallback header bug in this environment.
- The live DDS filenames and sprite names did not change.

## Validation

- `validation/all_goal_alpha_metrics.tsv`
- `validation/all_goal_alpha_validation.md`
- `contact_sheets/goal_icons_processed_checker_contact.png`
- `contact_sheets/goal_icons_processed_dark_contact.png`
- `contact_sheets/goal_icons_live_dds_checker_contact.png`
- `contact_sheets/goal_icons_live_dds_dark_contact.png`

All 13 processed PNGs and all 13 live DDS reads are `94x86`, have fully transparent corners, have no fully transparent white-RGB pixels, have no near-white halo pixels adjacent to transparency, and have no border-connected white/off-white matte pixels.

## Blockers

None for this asset family.
