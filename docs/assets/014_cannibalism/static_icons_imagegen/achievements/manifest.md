# Superseded Event 014 Achievement Icon Manifest

Status: inactive and superseded by `docs/assets/014_cannibalism/achievements_imagegen/manifest.md`. These 13 historical IDs are not the current 18-achievement contract and must not be used as Event 014 completion evidence. The current package owns all 54 registered runtime textures, including a newly generated `014_cannibalism_no_second_table` triplet.

Runtime cleanup (2026-07-12): the 36 DDS files belonging to the twelve obsolete IDs were removed from `gfx/achievements/`. The overlapping `014_cannibalism_no_second_table` triplet at that path is the independently generated current-package version. Every `Final DDS paths` entry below is historical provenance; it is not a current ownership or existence claim.

Date: `2026-07-01`

Scope:

- Regenerated completed achievement icons for the 13 requested Event 014 Cannibalism achievement ids using `$imagegen`.
- Created `_grey` and `_not_eligible` variants derived from each completed icon after the completed icon existed.
- Exported final DDS triplets directly under `gfx/achievements/` as the achievement root-only engine exception.
- Did not edit `.gfx`, `.gui`, gameplay, localisation, achievements script, history, country, focus, decision, spreadsheet, or docs outside this asset package and the requested handoff.
- Did not touch or replace `gfx/leaders/014_cannibalism/hannibal.dds`.

Reference inspection:

- `.agents/skills/chaos-redux-event-assets/assets/achievements/`
- Reference contact sheet: `docs/assets/014_cannibalism/static_icons_imagegen/achievements/contact_sheets/reference_achievements_contact_sheet.png`

Prompt evidence:

- `docs/assets/014_cannibalism/static_icons_imagegen/achievements/prompts/achievement_prompts.md`

Contact sheets:

- Source sheet: `docs/assets/014_cannibalism/static_icons_imagegen/achievements/contact_sheets/achievement_source_contact_sheet.png`
- Processed PNG variants: `docs/assets/014_cannibalism/static_icons_imagegen/achievements/contact_sheets/achievement_final_variants_contact_sheet.png`
- Decoded final DDS variants: `docs/assets/014_cannibalism/static_icons_imagegen/achievements/contact_sheets/achievement_dds_decoded_contact_sheet.png`

Validation:

- `docs/assets/014_cannibalism/static_icons_imagegen/achievements/validation_summary.txt`
- All 39 final DDS files validated as `64x64`, 32-bit BGRA-style DDS, fully opaque alpha.
- Completed icons are distinct achievement-specific `$imagegen` artwork, not resized focus, idea, or decision icons.
- No primitive-shape, local procedural, placeholder-chart, or non-imagegen completed final was used.

## Achievement Triplets

| Achievement id | Source mode | Source PNG | Processed PNGs | Final DDS paths | Target | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `014_cannibalism_clean_mess` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_clean_mess_source.png` | `processed_png/014_cannibalism_clean_mess.png`, `processed_png/014_cannibalism_clean_mess_grey.png`, `processed_png/014_cannibalism_clean_mess_not_eligible.png` | `gfx/achievements/014_cannibalism_clean_mess.dds`, `gfx/achievements/014_cannibalism_clean_mess_grey.dds`, `gfx/achievements/014_cannibalism_clean_mess_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_no_second_table` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_no_second_table_source.png` | `processed_png/014_cannibalism_no_second_table.png`, `processed_png/014_cannibalism_no_second_table_grey.png`, `processed_png/014_cannibalism_no_second_table_not_eligible.png` | `gfx/achievements/014_cannibalism_no_second_table.dds`, `gfx/achievements/014_cannibalism_no_second_table_grey.dds`, `gfx/achievements/014_cannibalism_no_second_table_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_silent_island` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_silent_island_source.png` | `processed_png/014_cannibalism_silent_island.png`, `processed_png/014_cannibalism_silent_island_grey.png`, `processed_png/014_cannibalism_silent_island_not_eligible.png` | `gfx/achievements/014_cannibalism_silent_island.dds`, `gfx/achievements/014_cannibalism_silent_island_grey.dds`, `gfx/achievements/014_cannibalism_silent_island_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_do_not_feed_the_front` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_do_not_feed_the_front_source.png` | `processed_png/014_cannibalism_do_not_feed_the_front.png`, `processed_png/014_cannibalism_do_not_feed_the_front_grey.png`, `processed_png/014_cannibalism_do_not_feed_the_front_not_eligible.png` | `gfx/achievements/014_cannibalism_do_not_feed_the_front.dds`, `gfx/achievements/014_cannibalism_do_not_feed_the_front_grey.dds`, `gfx/achievements/014_cannibalism_do_not_feed_the_front_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_trial_without_panic` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_trial_without_panic_source.png` | `processed_png/014_cannibalism_trial_without_panic.png`, `processed_png/014_cannibalism_trial_without_panic_grey.png`, `processed_png/014_cannibalism_trial_without_panic_not_eligible.png` | `gfx/achievements/014_cannibalism_trial_without_panic.dds`, `gfx/achievements/014_cannibalism_trial_without_panic_grey.dds`, `gfx/achievements/014_cannibalism_trial_without_panic_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_black_larder` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_black_larder_source.png` | `processed_png/014_cannibalism_black_larder.png`, `processed_png/014_cannibalism_black_larder_grey.png`, `processed_png/014_cannibalism_black_larder_not_eligible.png` | `gfx/achievements/014_cannibalism_black_larder.dds`, `gfx/achievements/014_cannibalism_black_larder_grey.dds`, `gfx/achievements/014_cannibalism_black_larder_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_last_ship_home` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_last_ship_home_source.png` | `processed_png/014_cannibalism_last_ship_home.png`, `processed_png/014_cannibalism_last_ship_home_grey.png`, `processed_png/014_cannibalism_last_ship_home_not_eligible.png` | `gfx/achievements/014_cannibalism_last_ship_home.dds`, `gfx/achievements/014_cannibalism_last_ship_home_grey.dds`, `gfx/achievements/014_cannibalism_last_ship_home_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_burn_the_cookbooks` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_burn_the_cookbooks_source.png` | `processed_png/014_cannibalism_burn_the_cookbooks.png`, `processed_png/014_cannibalism_burn_the_cookbooks_grey.png`, `processed_png/014_cannibalism_burn_the_cookbooks_not_eligible.png` | `gfx/achievements/014_cannibalism_burn_the_cookbooks.dds`, `gfx/achievements/014_cannibalism_burn_the_cookbooks_grey.dds`, `gfx/achievements/014_cannibalism_burn_the_cookbooks_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_hunger_of_hannibal` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_hunger_of_hannibal_source.png` | `processed_png/014_cannibalism_hunger_of_hannibal.png`, `processed_png/014_cannibalism_hunger_of_hannibal_grey.png`, `processed_png/014_cannibalism_hunger_of_hannibal_not_eligible.png` | `gfx/achievements/014_cannibalism_hunger_of_hannibal.dds`, `gfx/achievements/014_cannibalism_hunger_of_hannibal_grey.dds`, `gfx/achievements/014_cannibalism_hunger_of_hannibal_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_the_living_are_not_cattle` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_the_living_are_not_cattle_source.png` | `processed_png/014_cannibalism_the_living_are_not_cattle.png`, `processed_png/014_cannibalism_the_living_are_not_cattle_grey.png`, `processed_png/014_cannibalism_the_living_are_not_cattle_not_eligible.png` | `gfx/achievements/014_cannibalism_the_living_are_not_cattle.dds`, `gfx/achievements/014_cannibalism_the_living_are_not_cattle_grey.dds`, `gfx/achievements/014_cannibalism_the_living_are_not_cattle_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_empty_larder` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_empty_larder_source.png` | `processed_png/014_cannibalism_empty_larder.png`, `processed_png/014_cannibalism_empty_larder_grey.png`, `processed_png/014_cannibalism_empty_larder_not_eligible.png` | `gfx/achievements/014_cannibalism_empty_larder.dds`, `gfx/achievements/014_cannibalism_empty_larder_grey.dds`, `gfx/achievements/014_cannibalism_empty_larder_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_table_for_one` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_table_for_one_source.png` | `processed_png/014_cannibalism_table_for_one.png`, `processed_png/014_cannibalism_table_for_one_grey.png`, `processed_png/014_cannibalism_table_for_one_not_eligible.png` | `gfx/achievements/014_cannibalism_table_for_one.dds`, `gfx/achievements/014_cannibalism_table_for_one_grey.dds`, `gfx/achievements/014_cannibalism_table_for_one_not_eligible.dds` | `64x64` | `complete` |
| `014_cannibalism_after_the_feast` | `$imagegen` completed icon; variants derived | `source_png/achievement_014_cannibalism_after_the_feast_source.png` | `processed_png/014_cannibalism_after_the_feast.png`, `processed_png/014_cannibalism_after_the_feast_grey.png`, `processed_png/014_cannibalism_after_the_feast_not_eligible.png` | `gfx/achievements/014_cannibalism_after_the_feast.dds`, `gfx/achievements/014_cannibalism_after_the_feast_grey.dds`, `gfx/achievements/014_cannibalism_after_the_feast_not_eligible.dds` | `64x64` | `complete` |

## Blockers And Simplifications

- Blockers: none.
- Simplifications: none. Every requested achievement id has a completed source PNG, processed completed PNG, processed grey PNG, processed not-eligible PNG, and final DDS triplet.
