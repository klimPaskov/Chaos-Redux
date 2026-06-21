# Achievement Regeneration Manifest

Date: `2026-06-21`

Supersession note:

- The Death achievement families in this consolidated package were superseded by `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/`, because the Death icons required fresh source artwork rather than reused or modified package output. The Africa, Natural Disasters, and generic achievement notes in this file remain historical for their own batches.

Scope:

- Regenerated only the listed achievement icon families.
- Preserved every live DDS filename exactly as requested.
- Overwrote the live DDS outputs in `gfx/achievements/` from reviewed HOI4-style processed PNG packages.
- Did not edit gameplay, `.gfx`, localisation, focus, decision, event, or spreadsheet files.

Reference inspection completed before overwrite:

- Chaos Redux achievement references: `.agents/skills/chaos-redux-event-assets/assets/achievements/`
- Reviewed package contact sheets:
  - `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/contact_sheets/final_variants_compact.png`
  - `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/contact_sheets/final_variants.png`
  - `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/contact_sheets/family_variants_contact_sheet.png`

Workflow used:

- Reused already-reviewed same-day HOI4-style achievement regeneration packages for the exact listed IDs.
- Used the package `processed_png/<ID>.png` families as the regeneration source of truth.
- Re-exported the live DDS families with the repository's established ImageMagick DDS route:
  - `convert <processed_png> -define dds:compression=none DDS:<live_dds>`
- Corrected the Natural Disasters `_not_eligible` DDS families to be fully opaque after export.
- Parent review re-exported the Natural Disasters `_not_eligible` DDS families with an explicit opaque alpha channel so those variants also report as 32-bit `ARGB8888`.

Live overwrite summary:

- Families overwritten: `46`
- Live DDS files overwritten: `138`
- Final DDS format confirmed by `file`: `64 x 64`, `32-bit color`, `ARGB8888`

## Africa Set

Source package:

- `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/`

| ID | Source PNG | Processed PNG family | Final DDS family | Size | Status |
| --- | --- | --- | --- | --- | --- |
| `ACH_AFR_ANANSE_WROTE_THE_ORDERS` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_ANANSE_WROTE_THE_ORDERS_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_ANANSE_WROTE_THE_ORDERS{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_ANANSE_WROTE_THE_ORDERS{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_BAOBAB_FILIBUSTER` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_BAOBAB_FILIBUSTER_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_BAOBAB_FILIBUSTER{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_BAOBAB_FILIBUSTER{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_BIGGER_CARAVAN` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_BIGGER_CARAVAN_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_BIGGER_CARAVAN{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_BIGGER_CARAVAN{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_BIRD_WAS_RIGHT` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_BIRD_WAS_RIGHT_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_BIRD_WAS_RIGHT{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_BIRD_WAS_RIGHT{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_COMMAND_OVER_CONGRESS` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_COMMAND_OVER_CONGRESS_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_COMMAND_OVER_CONGRESS{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_COMMAND_OVER_CONGRESS{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_CONGRESS_OVER_COMMAND` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_CONGRESS_OVER_COMMAND_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_CONGRESS_OVER_COMMAND{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_CONGRESS_OVER_COMMAND{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_ELEPHANTS_REMEMBER` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_ELEPHANTS_REMEMBER_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_ELEPHANTS_REMEMBER{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_ELEPHANTS_REMEMBER{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_FOREST_GUARDIAN_PACT` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_FOREST_GUARDIAN_PACT_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_FOREST_GUARDIAN_PACT{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_FOREST_GUARDIAN_PACT{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_GENTLE_VETO` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_GENTLE_VETO_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_GENTLE_VETO{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_GENTLE_VETO{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_NO_COUNTERFEIT_CROWNS` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_NO_COUNTERFEIT_CROWNS_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_NO_COUNTERFEIT_CROWNS{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_NO_COUNTERFEIT_CROWNS{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_NOT_A_MAP_COLOUR` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_NOT_A_MAP_COLOUR_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_NOT_A_MAP_COLOUR{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_NOT_A_MAP_COLOUR{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_OLD_SEATS_NEW_UNION` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_OLD_SEATS_NEW_UNION_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_OLD_SEATS_NEW_UNION{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_OLD_SEATS_NEW_UNION{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_OLD_THRONES_VOTE` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_OLD_THRONES_VOTE_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_OLD_THRONES_VOTE{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_OLD_THRONES_VOTE{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_THE_ALLIES_SIGN` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_THE_ALLIES_SIGN_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_THE_ALLIES_SIGN{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_THE_ALLIES_SIGN{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_THE_FOREST_SIGNED_BACK` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_THE_FOREST_SIGNED_BACK_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_THE_FOREST_SIGNED_BACK{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_THE_FOREST_SIGNED_BACK{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_TIDE_TOOK_THE_PORT` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_TIDE_TOOK_THE_PORT_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_TIDE_TOOK_THE_PORT{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_TIDE_TOOK_THE_PORT{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_AFRICA_TERRACOTTA_LINE` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/source_png/ACH_AFRICA_TERRACOTTA_LINE_source.png` | `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/processed_png/ACH_AFRICA_TERRACOTTA_LINE{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_AFRICA_TERRACOTTA_LINE{,_grey,_not_eligible}.dds` | `64x64` | `complete` |

## Death And Generic Set

Source package:

- `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/`

| ID | Source PNG | Processed PNG family | Final DDS family | Size | Status |
| --- | --- | --- | --- | --- | --- |
| `death_before_the_name` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_before_the_name.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_before_the_name{,_grey,_not_eligible}.png` | `gfx/achievements/death_before_the_name{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_black_apostolate` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_black_apostolate.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_black_apostolate{,_grey,_not_eligible}.png` | `gfx/achievements/death_black_apostolate{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_black_tide_reversed` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_black_tide_reversed.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_black_tide_reversed{,_grey,_not_eligible}.png` | `gfx/achievements/death_black_tide_reversed{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_book_burner` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_book_burner.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_book_burner{,_grey,_not_eligible}.png` | `gfx/achievements/death_book_burner{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_counted_every_name` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_counted_every_name.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_counted_every_name{,_grey,_not_eligible}.png` | `gfx/achievements/death_counted_every_name{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_friend_of_zol` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_friend_of_zol.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_friend_of_zol{,_grey,_not_eligible}.png` | `gfx/achievements/death_friend_of_zol{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_last_ferry` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_last_ferry.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_last_ferry{,_grey,_not_eligible}.png` | `gfx/achievements/death_last_ferry{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_no_one_heard_the_first_boat` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_no_one_heard_the_first_boat.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_no_one_heard_the_first_boat{,_grey,_not_eligible}.png` | `gfx/achievements/death_no_one_heard_the_first_boat{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_no_witnesses` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_no_witnesses.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_no_witnesses{,_grey,_not_eligible}.png` | `gfx/achievements/death_no_witnesses{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_not_on_my_continent` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_not_on_my_continent.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_not_on_my_continent{,_grey,_not_eligible}.png` | `gfx/achievements/death_not_on_my_continent{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_six_continents_one_color` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_six_continents_one_color.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_six_continents_one_color{,_grey,_not_eligible}.png` | `gfx/achievements/death_six_continents_one_color{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_the_living_conference` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_the_living_conference.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_the_living_conference{,_grey,_not_eligible}.png` | `gfx/achievements/death_the_living_conference{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `death_the_names_do_not_come_back` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/death_the_names_do_not_come_back.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/death_the_names_do_not_come_back{,_grey,_not_eligible}.png` | `gfx/achievements/death_the_names_do_not_come_back{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `chaosx_ach_deadline_state` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/chaosx_ach_deadline_state.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/chaosx_ach_deadline_state{,_grey,_not_eligible}.png` | `gfx/achievements/chaosx_ach_deadline_state{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `cr_five_small_flags` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/cr_five_small_flags.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/cr_five_small_flags{,_grey,_not_eligible}.png` | `gfx/achievements/cr_five_small_flags{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `cr_suppression_failed` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/source_png/cr_suppression_failed.png` | `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/processed_png/cr_suppression_failed{,_grey,_not_eligible}.png` | `gfx/achievements/cr_suppression_failed{,_grey,_not_eligible}.dds` | `64x64` | `complete` |

## Natural Disasters Set

Source package:

- `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/`

| ID | Source PNG | Processed PNG family | Final DDS family | Size | Status |
| --- | --- | --- | --- | --- | --- |
| `ACH_ND_ASH_ON_THE_RUNWAY` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_ASH_ON_THE_RUNWAY_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_ASH_ON_THE_RUNWAY{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_ASH_ON_THE_RUNWAY{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_DISASTER_LEDGER_CLOSED` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_DISASTER_LEDGER_CLOSED_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_DISASTER_LEDGER_CLOSED{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_DISASTER_LEDGER_CLOSED{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_ENGINEERS_OF_THE_RUBBLE` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_ENGINEERS_OF_THE_RUBBLE{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_GRAIN_AGAINST_THE_DUST` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_GRAIN_AGAINST_THE_DUST_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_GRAIN_AGAINST_THE_DUST{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_GRAIN_AGAINST_THE_DUST{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_NO_PORT_LEFT_BEHIND` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_NO_PORT_LEFT_BEHIND_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_NO_PORT_LEFT_BEHIND{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_NO_PORT_LEFT_BEHIND{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_NO_WORLD_END_REQUIRED` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_NO_WORLD_END_REQUIRED_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_NO_WORLD_END_REQUIRED{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_NO_WORLD_END_REQUIRED{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_NOT_ONE_MORE_AFTERSHOCK` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_NOT_ONE_MORE_AFTERSHOCK{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_RING_THE_BELL` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_RING_THE_BELL_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_RING_THE_BELL{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_RING_THE_BELL{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_SKY_ARTILLERY_SURVIVOR` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_SKY_ARTILLERY_SURVIVOR_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_SKY_ARTILLERY_SURVIVOR{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_SKY_ARTILLERY_SURVIVOR{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_THE_SEA_WALKED_BACK` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_THE_SEA_WALKED_BACK_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_THE_SEA_WALKED_BACK{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_THE_SEA_WALKED_BACK{,_grey,_not_eligible}.dds` | `64x64` | `complete` |
| `ACH_ND_THE_TRAINS_ARRIVED` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/source_png/ACH_ND_THE_TRAINS_ARRIVED_source.png` | `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/processed_png/ACH_ND_THE_TRAINS_ARRIVED{,_grey,_not_eligible}.png` | `gfx/achievements/ACH_ND_THE_TRAINS_ARRIVED{,_grey,_not_eligible}.dds` | `64x64` | `complete` |

## Validation

- `46` requested families were mapped to reviewed processed PNG sources and overwritten in place.
- `138` live DDS files were validated with Pillow after overwrite.
- All live DDS outputs decode to exactly `64x64`.
- All live DDS outputs are fully opaque after the Natural Disasters `_not_eligible` correction pass.
- The Natural Disasters `_not_eligible` variants were rechecked after parent review and now report as 32-bit `ARGB8888`.
- Spot-checked `file` output confirms `Microsoft DirectDraw Surface (DDS): 64 x 64, 32-bit color, ARGB8888`.

## Blocked Assets

- None.

## Simplifications

- None. No listed family was skipped, renamed, or left without its normal, `_grey`, or `_not_eligible` DDS variant.
