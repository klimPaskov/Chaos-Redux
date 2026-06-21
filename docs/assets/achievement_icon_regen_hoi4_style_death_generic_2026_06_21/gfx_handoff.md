# GFX Handoff

- Scope: replacement art only for the requested achievement DDS families
- Interface edits: none
- Gameplay edits: none
- Localisation edits: none

## Wiring Status

- Existing filenames were preserved exactly, so the current achievement references continue to point to the correct assets.
- Existing `.gfx` file remains `interface/chaosx_achievements.gfx`.
- No sprite rename or texture path change is required.

## Replaced DDS Families

- `gfx/achievements/death_before_the_name.dds`
- `gfx/achievements/death_before_the_name_grey.dds`
- `gfx/achievements/death_before_the_name_not_eligible.dds`
- `gfx/achievements/death_black_apostolate.dds`
- `gfx/achievements/death_black_apostolate_grey.dds`
- `gfx/achievements/death_black_apostolate_not_eligible.dds`
- `gfx/achievements/death_black_tide_reversed.dds`
- `gfx/achievements/death_black_tide_reversed_grey.dds`
- `gfx/achievements/death_black_tide_reversed_not_eligible.dds`
- `gfx/achievements/death_book_burner.dds`
- `gfx/achievements/death_book_burner_grey.dds`
- `gfx/achievements/death_book_burner_not_eligible.dds`
- `gfx/achievements/death_counted_every_name.dds`
- `gfx/achievements/death_counted_every_name_grey.dds`
- `gfx/achievements/death_counted_every_name_not_eligible.dds`
- `gfx/achievements/death_friend_of_zol.dds`
- `gfx/achievements/death_friend_of_zol_grey.dds`
- `gfx/achievements/death_friend_of_zol_not_eligible.dds`
- `gfx/achievements/death_last_ferry.dds`
- `gfx/achievements/death_last_ferry_grey.dds`
- `gfx/achievements/death_last_ferry_not_eligible.dds`
- `gfx/achievements/death_no_one_heard_the_first_boat.dds`
- `gfx/achievements/death_no_one_heard_the_first_boat_grey.dds`
- `gfx/achievements/death_no_one_heard_the_first_boat_not_eligible.dds`
- `gfx/achievements/death_no_witnesses.dds`
- `gfx/achievements/death_no_witnesses_grey.dds`
- `gfx/achievements/death_no_witnesses_not_eligible.dds`
- `gfx/achievements/death_not_on_my_continent.dds`
- `gfx/achievements/death_not_on_my_continent_grey.dds`
- `gfx/achievements/death_not_on_my_continent_not_eligible.dds`
- `gfx/achievements/death_six_continents_one_color.dds`
- `gfx/achievements/death_six_continents_one_color_grey.dds`
- `gfx/achievements/death_six_continents_one_color_not_eligible.dds`
- `gfx/achievements/death_the_living_conference.dds`
- `gfx/achievements/death_the_living_conference_grey.dds`
- `gfx/achievements/death_the_living_conference_not_eligible.dds`
- `gfx/achievements/death_the_names_do_not_come_back.dds`
- `gfx/achievements/death_the_names_do_not_come_back_grey.dds`
- `gfx/achievements/death_the_names_do_not_come_back_not_eligible.dds`
- `gfx/achievements/chaosx_ach_deadline_state.dds`
- `gfx/achievements/chaosx_ach_deadline_state_grey.dds`
- `gfx/achievements/chaosx_ach_deadline_state_not_eligible.dds`
- `gfx/achievements/cr_five_small_flags.dds`
- `gfx/achievements/cr_five_small_flags_grey.dds`
- `gfx/achievements/cr_five_small_flags_not_eligible.dds`
- `gfx/achievements/cr_suppression_failed.dds`
- `gfx/achievements/cr_suppression_failed_grey.dds`
- `gfx/achievements/cr_suppression_failed_not_eligible.dds`

## Notes

- All processed PNGs are exact `64x64`.
- All final DDS outputs are `32-bit ARGB8888`.
- `_grey` and `_not_eligible` were derived from the completed icon to keep each family coherent.
- Candidate generations that produced transparent emblem outputs or unrelated scenes were rejected and kept only in the package review sheet.
