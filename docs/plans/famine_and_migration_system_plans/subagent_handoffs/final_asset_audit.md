# Final famine and migration asset audit

> **Superseded historical snapshot (2026-08-25):** This standalone audit records the pre-split asset package and is retained as provenance only. Its combined GFX paths, sprite names, asset breakdown, and unqualified closure claim are not current. Use [source_of_truth_map.md](../source_of_truth_map.md) and [completion_report.md](../completion_report.md) for current status; the declared 58 DDS assets have a 61-file physical inventory with manifest, provenance, and edge-cleanup blockers still open.

Audit date: 2026-08-24.

Scope: final static asset and consumer audit for the shared famine and migration system. This audit covers the decision category icon and picture, every decision and mission icon, every famine/displacement/reception state-modifier icon, all eight achievement triplets, the compact report-header image family, the two dedicated scripted state-mapmode button families, and the two currently consumer-backed Deaths reason texticons.

Result: the accepted static package is complete and uniquely wired. No new binary art was required. The stale manifest and handoff metadata were corrected to reflect the installed package registries. No gameplay, mapmode logic, decisions, missions, dynamic modifiers, achievements, localisation, event pool, event, GUI, workbook, or unrelated asset was edited.

## Registry and consumer crosswalk

The package-owned icon and achievement sprites are registered in interface/famine_and_migration_system.gfx.

The seven report sprites are registered in interface/famine_and_migration_system_event_pictures.gfx.

The four dedicated mapmode button sprites are registered in interface/mapmodes_interface.gfx.

The category consumes GFX_fm_cat_displacement and GFX_fm_pic_displacement in common/decisions/categories/famine_migration_categories.txt.

The ten decision and mission icon consumers resolve to the ten GFX_fm_dec_* sprites in common/decisions/famine_migration_decisions.txt. Six missions intentionally reuse this decision-icon family: fm_mission_secure_relief_route, fm_mission_hold_humanitarian_corridor, fm_mission_protect_evacuation_transport, fm_mission_deliver_relief_before_reserves_fail, fm_mission_prevent_reception_collapse, and fm_mission_prepare_safe_return_route.

The nine dynamic state modifiers resolve to the nine GFX_fm_state_* sprites in common/dynamic_modifiers/famine_migration_state_modifiers.txt.

The eight achievement IDs are declared in common/achievements/chaos_redux_achievements.txt. HOI4 achievement filename lookup and the package GFX aliases provide the completed, grey, and not-eligible states.

The seven compact report-header icon slots in interface/famine_migration_report_header.gui resolve to the seven GFX_report_event_famine_migration_* sprites.

The only dedicated famine/migration mapmode definitions are famine_state_map_mode and migration_state_map_mode in common/map_modes/chaosx_state_map_modes.txt. There are exactly four dedicated button textures, selected and deselected for those two identities.

## Category assets

| Asset | Final DDS | Source PNG and provenance | Processed PNG | Consumer and sprite | Technical properties | Status |
| --- | --- | --- | --- | --- | --- | --- |
| fm_cat_displacement | gfx/interface/decisions/famine_and_migration_system/fm_cat_displacement.dds | docs/assets/famine_and_migration_system/source/category/fm_cat_displacement.png; original native-alpha ImageGen icon | docs/assets/famine_and_migration_system/processed/category/fm_cat_displacement.png | Category icon field; GFX_fm_cat_displacement in interface/famine_and_migration_system.gfx | 52x40, RGBA source, native alpha, legacy uncompressed BGRA8 DDS, no mipmaps, alpha 0-255 | Complete |
| fm_pic_displacement | gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds | docs/assets/famine_and_migration_system/category_picture/source_png/fm_pic_displacement_source.png; original generated opaque decision-category scene | docs/assets/famine_and_migration_system/category_picture/processed_png/fm_pic_displacement.png | Category picture field; GFX_fm_pic_displacement in interface/famine_and_migration_system.gfx | 114x101, opaque full-canvas RGB/RGBA scene, legacy uncompressed BGRA8 DDS, no mipmaps, alpha 255-255 | Complete |

The category picture remains a separate 114x101 scene surface and is not a resized substitute for the 52x40 category button icon.

## State and dynamic modifier icons

All nine rows are bespoke state-specific art from the matching state-modifier reference family. Each final DDS is 32x32, legacy uncompressed BGRA8, no mipmaps, and native alpha with runtime alpha range 0-255.

| Asset | Final DDS | Source PNG | Processed PNG | Consumer and sprite | Status |
| --- | --- | --- | --- | --- | --- |
| fm_state_supply_strain | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_supply_strain.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_supply_strain.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_supply_strain.png | famine_migration_state_supply_strain; GFX_fm_state_supply_strain | Complete |
| fm_state_acute_shortage | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_acute_shortage.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_acute_shortage.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_acute_shortage.png | famine_migration_state_acute_shortage; GFX_fm_state_acute_shortage | Complete |
| fm_state_famine | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_famine.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_famine.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_famine.png | famine_migration_state_famine; GFX_fm_state_famine | Complete |
| fm_state_catastrophic_famine | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_catastrophic_famine.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_catastrophic_famine.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_catastrophic_famine.png | famine_migration_state_catastrophic_famine; GFX_fm_state_catastrophic_famine | Complete |
| fm_state_exodus | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_exodus.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_exodus.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_exodus.png | famine_migration_state_exodus; GFX_fm_state_exodus | Complete |
| fm_state_reception | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_reception.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_reception.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_reception.png | famine_migration_state_reception; GFX_fm_state_reception | Complete |
| fm_state_overcrowded | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_overcrowded.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_overcrowded.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_overcrowded.png | famine_migration_state_overcrowded; GFX_fm_state_overcrowded | Complete |
| fm_state_trapped_border | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_trapped_border.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_trapped_border.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_trapped_border.png | famine_migration_state_trapped_border; GFX_fm_state_trapped_border | Complete |
| fm_state_return | gfx/interface/state_modifiers/famine_and_migration_system/fm_state_return.dds | docs/assets/famine_and_migration_system/source/state_modifiers/fm_state_return.png | docs/assets/famine_and_migration_system/processed/state_modifiers/fm_state_return.png | famine_migration_state_return; GFX_fm_state_return | Complete |

## Decision and mission icon family

All ten rows are bespoke 32x32 decision icons from the matching decisions reference family. Each final DDS is legacy uncompressed BGRA8, no mipmaps, and native alpha with runtime alpha range 0-255.

| Asset | Final DDS | Source PNG | Processed PNG | Consumer and sprite | Status |
| --- | --- | --- | --- | --- | --- |
| fm_dec_release_reserves | gfx/interface/decisions/famine_and_migration_system/fm_dec_release_reserves.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_release_reserves.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_release_reserves.png | Decision and mission uses; GFX_fm_dec_release_reserves | Complete |
| fm_dec_relief_convoy | gfx/interface/decisions/famine_and_migration_system/fm_dec_relief_convoy.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_relief_convoy.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_relief_convoy.png | Decision and mission uses; GFX_fm_dec_relief_convoy | Complete |
| fm_dec_airlift | gfx/interface/decisions/famine_and_migration_system/fm_dec_airlift.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_airlift.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_airlift.png | Decision uses; GFX_fm_dec_airlift | Complete |
| fm_dec_evacuate | gfx/interface/decisions/famine_and_migration_system/fm_dec_evacuate.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_evacuate.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_evacuate.png | Decision and mission uses; GFX_fm_dec_evacuate | Complete |
| fm_dec_open_border | gfx/interface/decisions/famine_and_migration_system/fm_dec_open_border.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_open_border.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_open_border.png | Decision and mission uses; GFX_fm_dec_open_border | Complete |
| fm_dec_close_border | gfx/interface/decisions/famine_and_migration_system/fm_dec_close_border.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_close_border.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_close_border.png | Decision uses; GFX_fm_dec_close_border | Complete |
| fm_dec_quarantine | gfx/interface/decisions/famine_and_migration_system/fm_dec_quarantine.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_quarantine.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_quarantine.png | Decision uses; GFX_fm_dec_quarantine | Complete |
| fm_dec_distribute | gfx/interface/decisions/famine_and_migration_system/fm_dec_distribute.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_distribute.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_distribute.png | Decision and mission uses; GFX_fm_dec_distribute | Complete |
| fm_dec_integrate | gfx/interface/decisions/famine_and_migration_system/fm_dec_integrate.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_integrate.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_integrate.png | Decision uses; GFX_fm_dec_integrate | Complete |
| fm_dec_return | gfx/interface/decisions/famine_and_migration_system/fm_dec_return.dds | docs/assets/famine_and_migration_system/source/decisions/fm_dec_return.png | docs/assets/famine_and_migration_system/processed/decisions/fm_dec_return.png | Decision and mission uses; GFX_fm_dec_return | Complete |

## Achievement icons

All eight required achievement IDs have final, uniquely named completed, grey, and not-eligible DDS states.

For each ID below, the final files are gfx/achievements/ID.dds, gfx/achievements/ID_grey.dds, and gfx/achievements/ID_not_eligible.dds. The original source/provenance is docs/assets/famine_and_migration_system/source/achievements/ID.png, an untouched native-alpha ImageGen master. The processed state layers are docs/assets/famine_and_migration_system/processed/achievements/ID.png, ID_grey.png, and ID_not_eligible.png. The package registry aliases are GFX_achievement_ID, GFX_achievement_ID_grey, and GFX_achievement_ID_not_eligible in interface/famine_and_migration_system.gfx.

The processed achievement PNGs are transparent state layers rather than standalone final composites. The final DDS states are produced by the official process_achievement_icons.py composition contract over the canonical achievement template, preserving the required template treatment while retaining the original generated motif. This is why the final achievement DDS alpha range is 254-255 instead of matching the transparent source-layer alpha range.

| Achievement ID | Source master | Processed state layers | Final DDS triplet | Consumer aliases | Status |
| --- | --- | --- | --- | --- | --- |
| famine_migration_break_the_blockade | docs/assets/famine_and_migration_system/source/achievements/famine_migration_break_the_blockade.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_break_the_blockade.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_break_the_blockade.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_break_the_blockade, _grey, _not_eligible | Complete |
| famine_migration_no_one_left_at_the_gate | docs/assets/famine_and_migration_system/source/achievements/famine_migration_no_one_left_at_the_gate.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_no_one_left_at_the_gate.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_no_one_left_at_the_gate.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_no_one_left_at_the_gate, _grey, _not_eligible | Complete |
| famine_migration_roads_home | docs/assets/famine_and_migration_system/source/achievements/famine_migration_roads_home.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_roads_home.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_roads_home.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_roads_home, _grey, _not_eligible | Complete |
| famine_migration_bread_across_the_front | docs/assets/famine_and_migration_system/source/achievements/famine_migration_bread_across_the_front.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_bread_across_the_front.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_bread_across_the_front.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_bread_across_the_front, _grey, _not_eligible | Complete |
| famine_migration_hungry_not_contagious | docs/assets/famine_and_migration_system/source/achievements/famine_migration_hungry_not_contagious.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_hungry_not_contagious.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_hungry_not_contagious.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_hungry_not_contagious, _grey, _not_eligible | Complete |
| famine_migration_a_place_at_the_table | docs/assets/famine_and_migration_system/source/achievements/famine_migration_a_place_at_the_table.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_a_place_at_the_table.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_a_place_at_the_table.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_a_place_at_the_table, _grey, _not_eligible | Complete |
| famine_migration_the_grain_stayed_home | docs/assets/famine_and_migration_system/source/achievements/famine_migration_the_grain_stayed_home.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_the_grain_stayed_home.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_the_grain_stayed_home.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_the_grain_stayed_home, _grey, _not_eligible | Complete |
| famine_migration_the_country_did_not_empty | docs/assets/famine_and_migration_system/source/achievements/famine_migration_the_country_did_not_empty.png | docs/assets/famine_and_migration_system/processed/achievements/famine_migration_the_country_did_not_empty.png, _grey.png, _not_eligible.png | gfx/achievements/famine_migration_the_country_did_not_empty.dds, _grey.dds, _not_eligible.dds | GFX_achievement_famine_migration_the_country_did_not_empty, _grey, _not_eligible | Complete |

The eight achievement triplets are all present and uniquely wired. The strict audit command was run as: python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --audit --input docs/assets/famine_and_migration_system/processed/achievements --output-dir gfx/achievements. It returned AUDIT OK for all eight IDs.

## Compact report-header art

All seven accepted report-art rows have original generated source PNGs, processed transparent-card previews, final DDS files, unique sprites, and compact report-header icon consumers.

All seven final DDS files are 210x176 legacy uncompressed BGRA8, no mipmaps, with alpha range 0-255 and transparent card margins. The processed report PNGs and decoded DDS payloads match after RGBA-to-BGRA channel conversion.

| Report row | Final DDS | Source PNG | Processed PNG | Sprite and compact GUI consumer | Status |
| --- | --- | --- | --- | --- | --- |
| fm_report_generic_famine | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_generic_famine.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_generic_famine_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_generic_famine.png | GFX_report_event_famine_migration_generic_famine; famine_migration_report_generic_famine iconType | Complete |
| fm_report_island_blockade | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_island_blockade.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_island_blockade_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_island_blockade.png | GFX_report_event_famine_migration_island_blockade; famine_migration_report_island_blockade iconType | Complete |
| fm_report_wartime_evacuation | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_wartime_evacuation.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_wartime_evacuation_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_wartime_evacuation.png | GFX_report_event_famine_migration_wartime_evacuation; famine_migration_report_wartime_evacuation iconType | Complete |
| fm_report_closed_border | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_closed_border.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_closed_border_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_closed_border.png | GFX_report_event_famine_migration_closed_border; famine_migration_report_closed_border iconType | Complete |
| fm_report_relief_arrival | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_relief_arrival.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_relief_arrival_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_relief_arrival.png | GFX_report_event_famine_migration_relief_arrival; famine_migration_report_relief_arrival iconType | Complete |
| fm_report_nuclear_evacuation | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_nuclear_evacuation.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_nuclear_evacuation_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_nuclear_evacuation.png | GFX_report_event_famine_migration_nuclear_evacuation; famine_migration_report_nuclear_evacuation iconType | Complete |
| fm_report_return | gfx/event_pictures/famine_and_migration_system/report_event_famine_migration_return.dds | docs/assets/famine_and_migration_system/report_art/source_png/report_event_famine_migration_return_source.png | docs/assets/famine_and_migration_system/report_art/processed_png/report_event_famine_migration_return.png | GFX_report_event_famine_migration_return; famine_migration_report_return iconType | Complete |

## Dedicated mapmode buttons

Exactly two dedicated mapmode identities are present: famine_state_map_mode and migration_state_map_mode.

Exactly four final button DDS files are present, with no third famine/migration mapmode texture.

| Mapmode identity | State | Final DDS | Source PNG and provenance | Processed PNG | Installed sprite and consumer | Technical properties | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| famine_state_map_mode | selected | gfx/interface/mapmode/custom/famine_state_map_mode_selected.dds | docs/assets/famine_and_migration_system/mapmode/source/famine_state_map_mode_selected_source.png; native-alpha ImageGen source | docs/assets/famine_and_migration_system/mapmode/processed/famine_state_map_mode_selected.png | GFX_mapmode_buttons_selected_small_famine_state_map_mode in interface/mapmodes_interface.gfx; selected mapmode button | 20x18, legacy uncompressed BGRA8, no mipmaps, alpha 0-255 | Complete |
| famine_state_map_mode | deselected | gfx/interface/mapmode/custom/famine_state_map_mode_deselected.dds | docs/assets/famine_and_migration_system/mapmode/source/famine_state_map_mode_deselected_source.png; native-alpha ImageGen source | docs/assets/famine_and_migration_system/mapmode/processed/famine_state_map_mode_deselected.png | GFX_mapmode_buttons_deselected_small_famine_state_map_mode in interface/mapmodes_interface.gfx; deselected mapmode button | 20x18, legacy uncompressed BGRA8, no mipmaps, alpha 0-255 | Complete |
| migration_state_map_mode | selected | gfx/interface/mapmode/custom/migration_state_map_mode_selected.dds | docs/assets/famine_and_migration_system/mapmode/source/migration_state_map_mode_selected_source.png; native-alpha ImageGen source | docs/assets/famine_and_migration_system/mapmode/processed/migration_state_map_mode_selected.png | GFX_mapmode_buttons_selected_small_migration_state_map_mode in interface/mapmodes_interface.gfx; selected mapmode button | 20x18, legacy uncompressed BGRA8, no mipmaps, alpha 0-255 | Complete |
| migration_state_map_mode | deselected | gfx/interface/mapmode/custom/migration_state_map_mode_deselected.dds | docs/assets/famine_and_migration_system/mapmode/source/migration_state_map_mode_deselected_source.png; native-alpha ImageGen source | docs/assets/famine_and_migration_system/mapmode/processed/migration_state_map_mode_deselected.png | GFX_mapmode_buttons_deselected_small_migration_state_map_mode in interface/mapmodes_interface.gfx; deselected mapmode button | 20x18, legacy uncompressed BGRA8, no mipmaps, alpha 0-255 | Complete |

The four decoded mapmode DDS payloads match their processed PNGs byte-for-byte. Separate selected and deselected source art was generated for each family; no transform-only recolour, offset, or shared strip substitution was used.

## Deaths reason texticons

These two rows are consumer-backed optional extensions present in the current system and were included in the static audit.

| Asset | Final DDS | Source PNG | Processed PNG | Consumer and sprite | Technical properties | Status |
| --- | --- | --- | --- | --- | --- | --- |
| fm_deaths_famine | gfx/texticons/fm_deaths_famine.dds | docs/assets/famine_and_migration_system/source/deaths/fm_deaths_famine.png; native-alpha ImageGen source | docs/assets/famine_and_migration_system/processed/deaths/fm_deaths_famine.png | chaos_meter.deaths.cause.famine through GFX_fm_deaths_famine in interface/chaosx_texticons.gfx | 18x18, legacy uncompressed BGRA8, no mipmaps, alpha 0-255 | Complete |
| fm_deaths_displacement | gfx/texticons/fm_deaths_displacement.dds | docs/assets/famine_and_migration_system/source/deaths/fm_deaths_displacement.png; native-alpha ImageGen source | docs/assets/famine_and_migration_system/processed/deaths/fm_deaths_displacement.png | chaos_meter.deaths.cause.forced_displacement through GFX_fm_deaths_displacement in interface/chaosx_texticons.gfx | 18x18, legacy uncompressed BGRA8, no mipmaps, alpha 0-255 | Complete |

## DDS and provenance validation

The runtime package contains 58 final DDS files: 1 category icon, 1 category picture, 9 state modifiers, 10 decision/mission icons, 24 achievement states, 7 report cards, 4 mapmode buttons, and 2 Deaths texticons.

The corrected DDS header audit verified every output as a legacy 128-byte DDS header with declared dimensions matching its consumer canvas, DDS pixel-format size 32, flags 65, fourCC 0, 32-bit BGRA masks 0x00FF0000/0x0000FF00/0x000000FF/0xFF000000, texture caps 0x1000, zero mipmap count, and exact file length 128 plus width times height times four.

The exact file sizes by family are 8448 bytes for 52x40, 46184 bytes for 114x101, 4224 bytes for 32x32, 16512 bytes for 64x64, 147968 bytes for 210x176, 1568 bytes for 20x18, and 1424 bytes for 18x18.

All expected processed PNGs exist at their recorded paths and decode at the exact consumer dimensions. The raw source inventory is retained for every family; achievements intentionally retain eight raw 1254x1254 masters and 24 processed 64x64 state layers.

Native transparency was requested in the initial ImageGen call for every alpha-backed family and was preserved through processing, round-trip review, and DDS conversion. The opaque category picture is the only full-canvas exception because its inspected decision-category picture consumer requires a painted canvas.

The source logs and contact sheets under docs/assets/famine_and_migration_system/ record the matching canonical vanilla reference family, original prompts, native-alpha provenance, and visual review. No chroma-key background, fake checkerboard, matte spill, clipped edge, or placeholder marker was found in the final static package.

## Coverage and uniqueness checks

The package icon GFX file contains 45 unique sprite names and 45 existing texture references: 2 category surfaces, 9 state modifiers, 10 decision/mission icons, and 24 achievement aliases.

The report GFX file contains 7 unique sprite names and 7 existing texture references.

All 10 decision/mission icon references resolve to package sprites, all 9 dynamic modifier icon references resolve to package sprites, both category fields resolve to package sprites, all 7 report-header slots resolve to package sprites, and all 24 achievement aliases resolve to existing root DDS files.

The four famine/migration mapmode sprite names occur once each and point to the four existing dedicated DDS files. The source mapmode census finds exactly the two requested mapmode definitions and no third famine/migration identity.

The static asset directories and package GFX files contain no placeholder, TODO, TBD, stub, or dummy marker. No required family is satisfied by a generic fallback or an unrelated resized icon.

## Changes made by this audit

The root asset manifest target_gfx fields now point to the actual package registries rather than stale historical registry names. Category, state, decision, and achievement rows point to interface/famine_and_migration_system.gfx; Deaths texticons remain correctly pointed to interface/chaosx_texticons.gfx.

docs/assets/famine_and_migration_system/gfx_handoff.md now records the installed registries, all 58 final DDS outputs, achievement composition semantics, report-header wiring, and exactly two mapmode identities.

The category-picture manifest and handoff now mark GFX_fm_pic_displacement as installed and consumer-resolved.

The mapmode handoff and mapmode icon-artist handoff now record that all four sprite definitions already exist exactly once in interface/mapmodes_interface.gfx, so no parent GFX patch is requested.

The report-art manifest now marks all seven rows complete and records the installed report GFX and compact report-header consumers.

The required audit handoff is this file. No binary art or runtime GFX source needed a patch because the consumer coverage and final DDS outputs were already complete.

## Blockers, simplifications, and ownership gates

No famine/migration asset-specific blocker remains. All required static assets are complete, sourced, processed, converted, documented, and uniquely wired.

All eight achievements have final and uniquely wired completed, grey, and not-eligible assets.

Both dedicated mapmodes have final and uniquely wired selected and deselected assets, exactly four DDS files total, and no third mapmode identity.

Parent-owned live in-game visual approval remains a runtime gate. This audit does not claim engine-rendered GUI/mapmode proof because the hardcoded mapmodes presentation route does not expose dynamic map colors or linked raster payloads.

interface/mapmodes_interface.gfx retains unrelated pre-existing references to other vanilla/shared mapmode textures that are absent from this repository snapshot. Those references are outside famine/migration asset ownership and were not changed; the four famine/migration references are present and valid.

No simplification, placeholder, fallback, third mapmode, reused vanilla counter, or unrelated consumer wiring was added.
