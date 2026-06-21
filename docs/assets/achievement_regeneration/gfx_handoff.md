# Achievement Regeneration Handoff

Date: `2026-06-21`

Scope:

- Replaced only the live achievement DDS families named in the task.
- Kept all existing filenames and existing achievement wiring unchanged.
- Did not propose any new sprite names or `.gfx` edits.

## Files Changed

- Live DDS families under `gfx/achievements/` for:
  - `ACH_AFR_ANANSE_WROTE_THE_ORDERS`
  - `ACH_AFR_BAOBAB_FILIBUSTER`
  - `ACH_AFR_BIGGER_CARAVAN`
  - `ACH_AFR_BIRD_WAS_RIGHT`
  - `ACH_AFR_COMMAND_OVER_CONGRESS`
  - `ACH_AFR_CONGRESS_OVER_COMMAND`
  - `ACH_AFR_ELEPHANTS_REMEMBER`
  - `ACH_AFR_FOREST_GUARDIAN_PACT`
  - `ACH_AFR_GENTLE_VETO`
  - `ACH_AFR_NO_COUNTERFEIT_CROWNS`
  - `ACH_AFR_NOT_A_MAP_COLOUR`
  - `ACH_AFR_OLD_SEATS_NEW_UNION`
  - `ACH_AFR_OLD_THRONES_VOTE`
  - `ACH_AFR_THE_ALLIES_SIGN`
  - `ACH_AFR_THE_FOREST_SIGNED_BACK`
  - `ACH_AFR_TIDE_TOOK_THE_PORT`
  - `ACH_AFR_WHO_GAVE_THEM_A_MICROPHONE`
  - `ACH_AFRICA_TERRACOTTA_LINE`
  - `death_before_the_name`
  - `death_black_apostolate`
  - `death_black_tide_reversed`
  - `death_book_burner`
  - `death_counted_every_name`
  - `death_friend_of_zol`
  - `death_last_ferry`
  - `death_no_one_heard_the_first_boat`
  - `death_no_witnesses`
  - `death_not_on_my_continent`
  - `death_six_continents_one_color`
  - `death_the_living_conference`
  - `death_the_names_do_not_come_back`
  - `ACH_ND_ASH_ON_THE_RUNWAY`
  - `ACH_ND_DISASTER_LEDGER_CLOSED`
  - `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
  - `ACH_ND_GRAIN_AGAINST_THE_DUST`
  - `ACH_ND_NO_PORT_LEFT_BEHIND`
  - `ACH_ND_NO_WORLD_END_REQUIRED`
  - `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
  - `ACH_ND_RING_THE_BELL`
  - `ACH_ND_SKY_ARTILLERY_SURVIVOR`
  - `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`
  - `ACH_ND_THE_SEA_WALKED_BACK`
  - `ACH_ND_THE_TRAINS_ARRIVED`
  - `chaosx_ach_deadline_state`
  - `cr_suppression_failed`
  - `cr_five_small_flags`
- Consolidated task docs:
  - `docs/assets/achievement_regeneration/manifest.md`
  - `docs/assets/achievement_regeneration/gfx_handoff.md`

Each changed family includes:

- `gfx/achievements/<ID>.dds`
- `gfx/achievements/<ID>_grey.dds`
- `gfx/achievements/<ID>_not_eligible.dds`

## Source Packages Used

- Africa: `docs/assets/012_africa/achievement_icon_regen_hoi4_style_africa_2026_06_21/`
- Death and generic: `docs/assets/achievement_icon_regen_hoi4_style_death_generic_2026_06_21/`
- Natural Disasters: `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/`

Each family kept its reviewed source PNG and processed PNG history inside those package folders. The consolidated manifest records the exact path for every family.

## Dimensions And Presentation

- All final live DDS outputs: `64x64`
- All final live DDS outputs: opaque full-tile achievement presentation
- `_grey` variants: derived from the completed icon
- `_not_eligible` variants: derived from the grey icon family and exported as fully opaque HOI4-style red-cross tiles

## Validation Performed

- Confirmed the reviewed contact sheets existed for the three source packages.
- Re-exported every requested live DDS family from its reviewed processed PNG source.
- Validated `138` live DDS files with Pillow after export.
- Confirmed all `138` live DDS files decode to `64x64`.
- Confirmed all `138` live DDS files are fully opaque after a correction pass on the Natural Disasters `_not_eligible` families.
- Parent review re-exported the Natural Disasters `_not_eligible` DDS families with explicit opaque alpha and confirmed they report as 32-bit `ARGB8888`.
- Spot-checked representative live files with `file`:
  - `gfx/achievements/ACH_AFR_ANANSE_WROTE_THE_ORDERS.dds`
  - `gfx/achievements/death_before_the_name.dds`
  - `gfx/achievements/ACH_ND_ASH_ON_THE_RUNWAY.dds`
  - `gfx/achievements/chaosx_ach_deadline_state_not_eligible.dds`

## Blocked Assets

- None.

## Simplifications

- None.
