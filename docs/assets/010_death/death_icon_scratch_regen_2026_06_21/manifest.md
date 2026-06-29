# Event 010 Death Icon Scratch Regeneration Manifest

Date: `2026-06-21`

Scope:

- Regenerated the eight user-reported Death focus icons from fresh generated source artwork.
- Regenerated all thirteen Death achievement icon families from fresh generated source artwork.
- Preserved every existing live DDS filename and sprite reference.
- Did not edit gameplay, localisation, `.gfx`, GUI, focus, decision, event, or spreadsheet files.

Source rules followed:

- No existing Death DDS or PNG icon was used as an edit target, resize base, recolor base, cleanup base, or source composite.
- Focus icons and achievement icons were generated and processed as separate asset types.
- Achievement `_grey` and `_not_eligible` variants were derived only after the completed achievement icon existed.
- Final focus icons use transparent unused canvas; final achievement icons use opaque HOI4-style full tiles.

Reference inspection:

- `.agents/skills/chaos-redux-event-assets/assets/focuses/`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/goals/`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/achievements/`

Contact sheets:

- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/contact_sheets/scratch_focus_sources.png`
- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/contact_sheets/scratch_focus_processed_checker_contact_sheet.png`
- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/contact_sheets/scratch_achievement_source_contact_sheet.png`
- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/contact_sheets/scratch_achievement_final_variants.png`

Validation:

- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/validation/focus_processing_summary.txt`
- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/validation/achievement_processing_summary.txt`
- All live focus DDS files decode to `94x86`, have transparent corners, and have zero opaque-white pixels.
- All live achievement DDS files decode to `64x64` with fully opaque alpha.
- Source PNG byte comparisons against the older Death focus and achievement source packages were all `False`.

## Focus Icons

| Asset | Sprite | Source PNG | Processed PNG | Package DDS | Live DDS | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `focus_death_empty_supply` | `GFX_focus_death_empty_supply` | `source_png/focus_death_empty_supply_source.png` | `processed_png/focus_death_empty_supply.png` | `dds/focus_death_empty_supply.dds` | `gfx/interface/goals/death/focus_death_empty_supply.dds` | `complete` |
| `focus_death_every_road_slows` | `GFX_focus_death_every_road_slows` | `source_png/focus_death_every_road_slows_source.png` | `processed_png/focus_death_every_road_slows.png` | `dds/focus_death_every_road_slows.dds` | `gfx/interface/goals/death/focus_death_every_road_slows.dds` | `complete` |
| `focus_death_last_shores` | `GFX_focus_death_last_shores` | `source_png/focus_death_last_shores_source.png` | `processed_png/focus_death_last_shores.png` | `dds/focus_death_last_shores.dds` | `gfx/interface/goals/death/focus_death_last_shores.dds` | `complete` |
| `focus_death_mourning_host` | `GFX_focus_death_mourning_host` | `source_png/focus_death_mourning_host_source.png` | `processed_png/focus_death_mourning_host.png` | `dds/focus_death_mourning_host.dds` | `gfx/interface/goals/death/focus_death_mourning_host.dds` | `complete` |
| `focus_death_orders_without_breath` | `GFX_focus_death_orders_without_breath` | `source_png/focus_death_orders_without_breath_source.png` | `processed_png/focus_death_orders_without_breath.png` | `dds/focus_death_orders_without_breath.dds` | `gfx/interface/goals/death/focus_death_orders_without_breath.dds` | `complete` |
| `focus_death_ruin_host` | `GFX_focus_death_ruin_host` | `source_png/focus_death_ruin_host_source.png` | `processed_png/focus_death_ruin_host.png` | `dds/focus_death_ruin_host.dds` | `gfx/interface/goals/death/focus_death_ruin_host.dds` | `complete` |
| `focus_death_state_without_state` | `GFX_focus_death_state_without_state` | `source_png/focus_death_state_without_state_source.png` | `processed_png/focus_death_state_without_state.png` | `dds/focus_death_state_without_state.dds` | `gfx/interface/goals/death/focus_death_state_without_state.dds` | `complete` |
| `focus_death_world_consumed` | `GFX_focus_death_world_consumed` | `source_png/focus_death_world_consumed_source.png` | `processed_png/focus_death_world_consumed.png` | `dds/focus_death_world_consumed.dds` | `gfx/interface/goals/death/focus_death_world_consumed.dds` | `complete` |

## Achievement Icons

Each achievement has a completed, `_grey`, and `_not_eligible` DDS in `gfx/achievements/`.

| Asset | Source PNG | Processed PNG family | Package DDS family | Live DDS family | Status |
| --- | --- | --- | --- | --- | --- |
| `death_before_the_name` | `source_png/achievement_death_before_the_name_source.png` | `processed_png/achievement_death_before_the_name{,_grey,_not_eligible}.png` | `dds/death_before_the_name{,_grey,_not_eligible}.dds` | `gfx/achievements/death_before_the_name{,_grey,_not_eligible}.dds` | `complete` |
| `death_black_apostolate` | `source_png/achievement_death_black_apostolate_source.png` | `processed_png/achievement_death_black_apostolate{,_grey,_not_eligible}.png` | `dds/death_black_apostolate{,_grey,_not_eligible}.dds` | `gfx/achievements/death_black_apostolate{,_grey,_not_eligible}.dds` | `complete` |
| `death_black_tide_reversed` | `source_png/achievement_death_black_tide_reversed_source.png` | `processed_png/achievement_death_black_tide_reversed{,_grey,_not_eligible}.png` | `dds/death_black_tide_reversed{,_grey,_not_eligible}.dds` | `gfx/achievements/death_black_tide_reversed{,_grey,_not_eligible}.dds` | `complete` |
| `death_book_burner` | `source_png/achievement_death_book_burner_source.png` | `processed_png/achievement_death_book_burner{,_grey,_not_eligible}.png` | `dds/death_book_burner{,_grey,_not_eligible}.dds` | `gfx/achievements/death_book_burner{,_grey,_not_eligible}.dds` | `complete` |
| `death_counted_every_name` | `source_png/achievement_death_counted_every_name_source.png` | `processed_png/achievement_death_counted_every_name{,_grey,_not_eligible}.png` | `dds/death_counted_every_name{,_grey,_not_eligible}.dds` | `gfx/achievements/death_counted_every_name{,_grey,_not_eligible}.dds` | `complete` |
| `death_friend_of_zol` | `source_png/achievement_death_friend_of_zol_source.png` | `processed_png/achievement_death_friend_of_zol{,_grey,_not_eligible}.png` | `dds/death_friend_of_zol{,_grey,_not_eligible}.dds` | `gfx/achievements/death_friend_of_zol{,_grey,_not_eligible}.dds` | `complete` |
| `death_last_ferry` | `source_png/achievement_death_last_ferry_source.png` | `processed_png/achievement_death_last_ferry{,_grey,_not_eligible}.png` | `dds/death_last_ferry{,_grey,_not_eligible}.dds` | `gfx/achievements/death_last_ferry{,_grey,_not_eligible}.dds` | `complete` |
| `death_no_one_heard_the_first_boat` | `source_png/achievement_death_no_one_heard_the_first_boat_source.png` | `processed_png/achievement_death_no_one_heard_the_first_boat{,_grey,_not_eligible}.png` | `dds/death_no_one_heard_the_first_boat{,_grey,_not_eligible}.dds` | `gfx/achievements/death_no_one_heard_the_first_boat{,_grey,_not_eligible}.dds` | `complete` |
| `death_no_witnesses` | `source_png/achievement_death_no_witnesses_source.png` | `processed_png/achievement_death_no_witnesses{,_grey,_not_eligible}.png` | `dds/death_no_witnesses{,_grey,_not_eligible}.dds` | `gfx/achievements/death_no_witnesses{,_grey,_not_eligible}.dds` | `complete` |
| `death_not_on_my_continent` | `source_png/achievement_death_not_on_my_continent_source.png` | `processed_png/achievement_death_not_on_my_continent{,_grey,_not_eligible}.png` | `dds/death_not_on_my_continent{,_grey,_not_eligible}.dds` | `gfx/achievements/death_not_on_my_continent{,_grey,_not_eligible}.dds` | `complete` |
| `death_six_continents_one_color` | `source_png/achievement_death_six_continents_one_color_source.png` | `processed_png/achievement_death_six_continents_one_color{,_grey,_not_eligible}.png` | `dds/death_six_continents_one_color{,_grey,_not_eligible}.dds` | `gfx/achievements/death_six_continents_one_color{,_grey,_not_eligible}.dds` | `complete` |
| `death_the_living_conference` | `source_png/achievement_death_the_living_conference_source.png` | `processed_png/achievement_death_the_living_conference{,_grey,_not_eligible}.png` | `dds/death_the_living_conference{,_grey,_not_eligible}.dds` | `gfx/achievements/death_the_living_conference{,_grey,_not_eligible}.dds` | `complete` |
| `death_the_names_do_not_come_back` | `source_png/achievement_death_the_names_do_not_come_back_source.png` | `processed_png/achievement_death_the_names_do_not_come_back{,_grey,_not_eligible}.png` | `dds/death_the_names_do_not_come_back{,_grey,_not_eligible}.dds` | `gfx/achievements/death_the_names_do_not_come_back{,_grey,_not_eligible}.dds` | `complete` |

## Blockers And Simplifications

- Blockers: none.
- Simplifications: none. Every listed focus icon and every listed Death achievement family has fresh source artwork, processed PNG output, package DDS output, and live DDS output.
