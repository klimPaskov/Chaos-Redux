# Event 012 Africa achievement icon manifest

## Scope

This evidence package covers the 44 achievement keys in `docs/specs/012_africa_specs/matrices/012_africa_achievement_matrix.csv`.

Each row has an existing 1254x1254 RGB source master, a 1254x1254 RGBA keyed intermediate, and deterministic 64x64 RGBA processed previews for normal, grey, and not-eligible states.

The source masters are retained unchanged.

The normal, grey, and not-eligible previews are converted to matching runtime DDS triplets under `gfx/achievements/`.

The expected runtime triplets are `<key>.dds`, `<key>_grey.dds`, and `<key>_not_eligible.dds` directly under `gfx/achievements/`.

The runtime DDS triplets are installed under the root `gfx/achievements/` folder and were validated against their matching processed PNGs.

## Package layout

| Surface | Path | Count | Contract |
| --- | --- | ---: | --- |
| Source masters | `source_png/<key>.png` | 44 | Existing 1254x1254 RGB chroma-key masters |
| Keyed intermediates | `validation/keyed/<key>.png` | 44 | Existing or deterministically completed 1254x1254 RGBA cutouts |
| Processed previews | `processed_png/<key>{,_grey,_not_eligible}.png` | 132 | Exact 64x64 RGBA normal, grey, and not-eligible previews |
| Runtime DDS | `gfx/achievements/<key>{,_grey,_not_eligible}.dds` | 132 | Exact 64x64 uncompressed BGRA DDS triplets |
| Review sheets | `contact_sheets/` | 4 | Source, processed, triplet, and decoded-DDS contact sheets |
| Per-file QA | `validation/asset_validation.tsv` | 44 rows | Dimensions, alpha, key-color, and SHA-256 evidence |
| DDS QA | `validation/dds_validation.tsv` | 132 rows | DDS headers, dimensions, pixel equality, grayscale, and overlay relation |
| Hash inventory | `validation/hashes.sha256` | 352 entries | Source, keyed, processed PNG, and runtime DDS hashes |
| Runtime handoff | `gfx_handoff.md` | 1 | Parent-facing root DDS naming and status |

## Asset index

| # | Achievement key | Source | Keyed | Processed | Expected runtime triplet | Evidence status |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `africa_guardians_without_borders` | `source_png/africa_guardians_without_borders.png` | `validation/keyed/africa_guardians_without_borders.png` | `processed_png/africa_guardians_without_borders{,_grey,_not_eligible}.png` | `gfx/achievements/africa_guardians_without_borders{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 2 | `africa_last_convoy_home` | `source_png/africa_last_convoy_home.png` | `validation/keyed/africa_last_convoy_home.png` | `processed_png/africa_last_convoy_home{,_grey,_not_eligible}.png` | `gfx/achievements/africa_last_convoy_home{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 3 | `africa_no_empty_promises` | `source_png/africa_no_empty_promises.png` | `validation/keyed/africa_no_empty_promises.png` | `processed_png/africa_no_empty_promises{,_grey,_not_eligible}.png` | `gfx/achievements/africa_no_empty_promises{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 4 | `africa_the_interveners_left` | `source_png/africa_the_interveners_left.png` | `validation/keyed/africa_the_interveners_left.png` | `processed_png/africa_the_interveners_left{,_grey,_not_eligible}.png` | `gfx/achievements/africa_the_interveners_left{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 5 | `africa_archive_of_the_living_state` | `source_png/africa_archive_of_the_living_state.png` | `validation/keyed/africa_archive_of_the_living_state.png` | `processed_png/africa_archive_of_the_living_state{,_grey,_not_eligible}.png` | `gfx/achievements/africa_archive_of_the_living_state{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 6 | `africa_twelve_empty_chairs_filled` | `source_png/africa_twelve_empty_chairs_filled.png` | `validation/keyed/africa_twelve_empty_chairs_filled.png` | `processed_png/africa_twelve_empty_chairs_filled{,_grey,_not_eligible}.png` | `gfx/achievements/africa_twelve_empty_chairs_filled{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 7 | `africa_the_clause_is_the_country` | `source_png/africa_the_clause_is_the_country.png` | `validation/keyed/africa_the_clause_is_the_country.png` | `processed_png/africa_the_clause_is_the_country{,_grey,_not_eligible}.png` | `gfx/achievements/africa_the_clause_is_the_country{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 8 | `africa_exit_without_war` | `source_png/africa_exit_without_war.png` | `validation/keyed/africa_exit_without_war.png` | `processed_png/africa_exit_without_war{,_grey,_not_eligible}.png` | `gfx/achievements/africa_exit_without_war{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 9 | `africa_no_second_capital` | `source_png/africa_no_second_capital.png` | `validation/keyed/africa_no_second_capital.png` | `processed_png/africa_no_second_capital{,_grey,_not_eligible}.png` | `gfx/achievements/africa_no_second_capital{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 10 | `africa_every_region_speaks` | `source_png/africa_every_region_speaks.png` | `validation/keyed/africa_every_region_speaks.png` | `processed_png/africa_every_region_speaks{,_grey,_not_eligible}.png` | `gfx/achievements/africa_every_region_speaks{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 11 | `africa_confidence_is_contagious` | `source_png/africa_confidence_is_contagious.png` | `validation/keyed/africa_confidence_is_contagious.png` | `processed_png/africa_confidence_is_contagious{,_grey,_not_eligible}.png` | `gfx/achievements/africa_confidence_is_contagious{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 12 | `africa_federation_by_consent` | `source_png/africa_federation_by_consent.png` | `validation/keyed/africa_federation_by_consent.png` | `processed_png/africa_federation_by_consent{,_grey,_not_eligible}.png` | `gfx/achievements/africa_federation_by_consent{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 13 | `africa_republic_of_many_capitals` | `source_png/africa_republic_of_many_capitals.png` | `validation/keyed/africa_republic_of_many_capitals.png` | `processed_png/africa_republic_of_many_capitals{,_grey,_not_eligible}.png` | `gfx/achievements/africa_republic_of_many_capitals{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 14 | `africa_crowns_at_one_table` | `source_png/africa_crowns_at_one_table.png` | `validation/keyed/africa_crowns_at_one_table.png` | `processed_png/africa_crowns_at_one_table{,_grey,_not_eligible}.png` | `gfx/achievements/africa_crowns_at_one_table{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 15 | `africa_union_of_work_and_land` | `source_png/africa_union_of_work_and_land.png` | `validation/keyed/africa_union_of_work_and_land.png` | `processed_png/africa_union_of_work_and_land{,_grey,_not_eligible}.png` | `gfx/achievements/africa_union_of_work_and_land{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 16 | `africa_order_without_partition` | `source_png/africa_order_without_partition.png` | `validation/keyed/africa_order_without_partition.png` | `processed_png/africa_order_without_partition{,_grey,_not_eligible}.png` | `gfx/achievements/africa_order_without_partition{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 17 | `africa_confederation_that_endured` | `source_png/africa_confederation_that_endured.png` | `validation/keyed/africa_confederation_that_endured.png` | `processed_png/africa_confederation_that_endured{,_grey,_not_eligible}.png` | `gfx/achievements/africa_confederation_that_endured{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 18 | `africa_covenant_with_the_impossible` | `source_png/africa_covenant_with_the_impossible.png` | `validation/keyed/africa_covenant_with_the_impossible.png` | `processed_png/africa_covenant_with_the_impossible{,_grey,_not_eligible}.png` | `gfx/achievements/africa_covenant_with_the_impossible{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 19 | `africa_kings_of_the_savanna` | `source_png/africa_kings_of_the_savanna.png` | `validation/keyed/africa_kings_of_the_savanna.png` | `processed_png/africa_kings_of_the_savanna{,_grey,_not_eligible}.png` | `gfx/achievements/africa_kings_of_the_savanna{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 20 | `africa_nile_has_many_memories` | `source_png/africa_nile_has_many_memories.png` | `validation/keyed/africa_nile_has_many_memories.png` | `processed_png/africa_nile_has_many_memories{,_grey,_not_eligible}.png` | `gfx/achievements/africa_nile_has_many_memories{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 21 | `africa_ports_of_the_monsoon` | `source_png/africa_ports_of_the_monsoon.png` | `validation/keyed/africa_ports_of_the_monsoon.png` | `processed_png/africa_ports_of_the_monsoon{,_grey,_not_eligible}.png` | `gfx/achievements/africa_ports_of_the_monsoon{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 22 | `africa_walls_courts_and_caravans` | `source_png/africa_walls_courts_and_caravans.png` | `validation/keyed/africa_walls_courts_and_caravans.png` | `processed_png/africa_walls_courts_and_caravans{,_grey,_not_eligible}.png` | `gfx/achievements/africa_walls_courts_and_caravans{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 23 | `africa_the_old_gold_roads` | `source_png/africa_the_old_gold_roads.png` | `validation/keyed/africa_the_old_gold_roads.png` | `processed_png/africa_the_old_gold_roads{,_grey,_not_eligible}.png` | `gfx/achievements/africa_the_old_gold_roads{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 24 | `africa_member_who_said_no` | `source_png/africa_member_who_said_no.png` | `validation/keyed/africa_member_who_said_no.png` | `processed_png/africa_member_who_said_no{,_grey,_not_eligible}.png` | `gfx/achievements/africa_member_who_said_no{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 25 | `africa_return_without_compulsion` | `source_png/africa_return_without_compulsion.png` | `validation/keyed/africa_return_without_compulsion.png` | `processed_png/africa_return_without_compulsion{,_grey,_not_eligible}.png` | `gfx/achievements/africa_return_without_compulsion{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 26 | `africa_tools_books_and_ballots` | `source_png/africa_tools_books_and_ballots.png` | `validation/keyed/africa_tools_books_and_ballots.png` | `processed_png/africa_tools_books_and_ballots{,_grey,_not_eligible}.png` | `gfx/achievements/africa_tools_books_and_ballots{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 27 | `africa_four_oceans_homeward` | `source_png/africa_four_oceans_homeward.png` | `validation/keyed/africa_four_oceans_homeward.png` | `processed_png/africa_four_oceans_homeward{,_grey,_not_eligible}.png` | `gfx/achievements/africa_four_oceans_homeward{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 28 | `africa_capital_without_capture` | `source_png/africa_capital_without_capture.png` | `validation/keyed/africa_capital_without_capture.png` | `processed_png/africa_capital_without_capture{,_grey,_not_eligible}.png` | `gfx/achievements/africa_capital_without_capture{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 29 | `africa_rails_rivers_roads_and_ports` | `source_png/africa_rails_rivers_roads_and_ports.png` | `validation/keyed/africa_rails_rivers_roads_and_ports.png` | `processed_png/africa_rails_rivers_roads_and_ports{,_grey,_not_eligible}.png` | `gfx/achievements/africa_rails_rivers_roads_and_ports{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 30 | `africa_ore_leaves_as_machines` | `source_png/africa_ore_leaves_as_machines.png` | `validation/keyed/africa_ore_leaves_as_machines.png` | `processed_png/africa_ore_leaves_as_machines{,_grey,_not_eligible}.png` | `gfx/achievements/africa_ore_leaves_as_machines{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 31 | `africa_bread_before_banners` | `source_png/africa_bread_before_banners.png` | `validation/keyed/africa_bread_before_banners.png` | `processed_png/africa_bread_before_banners{,_grey,_not_eligible}.png` | `gfx/achievements/africa_bread_before_banners{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 32 | `africa_development_without_overstretch` | `source_png/africa_development_without_overstretch.png` | `validation/keyed/africa_development_without_overstretch.png` | `processed_png/africa_development_without_overstretch{,_grey,_not_eligible}.png` | `gfx/achievements/africa_development_without_overstretch{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 33 | `africa_common_reserve_answers` | `source_png/africa_common_reserve_answers.png` | `validation/keyed/africa_common_reserve_answers.png` | `processed_png/africa_common_reserve_answers{,_grey,_not_eligible}.png` | `gfx/achievements/africa_common_reserve_answers{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 34 | `africa_no_foreign_boot_remains` | `source_png/africa_no_foreign_boot_remains.png` | `validation/keyed/africa_no_foreign_boot_remains.png` | `processed_png/africa_no_foreign_boot_remains{,_grey,_not_eligible}.png` | `gfx/achievements/africa_no_foreign_boot_remains{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 35 | `africa_beasts_but_not_caricatures` | `source_png/africa_beasts_but_not_caricatures.png` | `validation/keyed/africa_beasts_but_not_caricatures.png` | `processed_png/africa_beasts_but_not_caricatures{,_grey,_not_eligible}.png` | `gfx/achievements/africa_beasts_but_not_caricatures{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 36 | `africa_elephants_crossed_the_desert` | `source_png/africa_elephants_crossed_the_desert.png` | `validation/keyed/africa_elephants_crossed_the_desert.png` | `processed_png/africa_elephants_crossed_the_desert{,_grey,_not_eligible}.png` | `gfx/achievements/africa_elephants_crossed_the_desert{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 37 | `africa_the_forest_kept_its_word` | `source_png/africa_the_forest_kept_its_word.png` | `validation/keyed/africa_the_forest_kept_its_word.png` | `processed_png/africa_the_forest_kept_its_word{,_grey,_not_eligible}.png` | `gfx/achievements/africa_the_forest_kept_its_word{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 38 | `africa_rain_on_command` | `source_png/africa_rain_on_command.png` | `validation/keyed/africa_rain_on_command.png` | `processed_png/africa_rain_on_command{,_grey,_not_eligible}.png` | `gfx/achievements/africa_rain_on_command{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 39 | `africa_disease_made_and_unmade` | `source_png/africa_disease_made_and_unmade.png` | `validation/keyed/africa_disease_made_and_unmade.png` | `processed_png/africa_disease_made_and_unmade{,_grey,_not_eligible}.png` | `gfx/achievements/africa_disease_made_and_unmade{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 40 | `africa_stone_walks_into_parliament` | `source_png/africa_stone_walks_into_parliament.png` | `validation/keyed/africa_stone_walks_into_parliament.png` | `processed_png/africa_stone_walks_into_parliament{,_grey,_not_eligible}.png` | `gfx/achievements/africa_stone_walks_into_parliament{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 41 | `africa_another_continent_stood_up` | `source_png/africa_another_continent_stood_up.png` | `validation/keyed/africa_another_continent_stood_up.png` | `processed_png/africa_another_continent_stood_up{,_grey,_not_eligible}.png` | `gfx/achievements/africa_another_continent_stood_up{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 42 | `africa_two_continents_one_name` | `source_png/africa_two_continents_one_name.png` | `validation/keyed/africa_two_continents_one_name.png` | `processed_png/africa_two_continents_one_name{,_grey,_not_eligible}.png` | `gfx/achievements/africa_two_continents_one_name{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 43 | `africa_war_between_worlds` | `source_png/africa_war_between_worlds.png` | `validation/keyed/africa_war_between_worlds.png` | `processed_png/africa_war_between_worlds{,_grey,_not_eligible}.png` | `gfx/achievements/africa_war_between_worlds{,_grey,_not_eligible}.dds` | complete and DDS-validated |
| 44 | `africa_the_world_is_one` | `source_png/africa_the_world_is_one.png` | `validation/keyed/africa_the_world_is_one.png` | `processed_png/africa_the_world_is_one{,_grey,_not_eligible}.png` | `gfx/achievements/africa_the_world_is_one{,_grey,_not_eligible}.dds` | complete and DDS-validated |

## Runtime boundary

This package does not edit `.gfx`, achievements, localisation, gameplay, or runtime DDS files.

The parent agent must reconcile the 44 completed previews with the runtime triplets and confirm that each normal, grey, and not-eligible DDS decodes to 64x64 before claiming runtime completion.
