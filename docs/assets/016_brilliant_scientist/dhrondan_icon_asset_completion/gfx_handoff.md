# Event 016 D'Rhondan icon asset completion GFX handoff

Status: complete for the accepted 88-focus and 11-lifecycle-icon binary tranche, the 21 missing D'Rhondan/contact/country/project sprite registrations, and the scoped supporting-binary audit. No achievement art or registry entry was added. No 3D model completion is claimed.

## Focus and lifecycle sprites

`interface/016_dhrondan_focus_icons.gfx` remains the authoritative registration file for 88 `GFX_goal_DHR_<focus_name>` sprites and their 88 `_shine` sprites, plus 11 `GFX_idea_dhrondan_<lifecycle_name>` sprites. Each unique focus DDS is installed under `gfx/interface/goals/016_dhrondan_focus/<branch>/goal_DHR_<focus_name>.dds` at 94x86. Each lifecycle DDS is installed under `gfx/interface/ideas/016_dhrondan_focus/dhrondan_<lifecycle_name>.dds` at 64x64.

| Branch | Focus DDS stems | Count |
| --- | --- | ---: |
| survival | `beneath_an_alien_sky`, `count_the_landing_states`, `secure_the_scattered_enclaves`, `inventory_the_expedition_stores`, `restore_the_landing_beacons`, `bind_the_enclaves`, `reopen_the_orbital_channel`, `convene_the_two_world_throne` | 8 |
| imperial | `vael_ix_takes_the_throne`, `restore_the_ninth_diadem`, `bind_the_landing_lords`, `codify_imperial_service`, `raise_the_palace_guard`, `proclaim_the_right_of_return`, `crown_the_enclave_empire`, `the_unbroken_imperial_line` | 8 |
| synod | `sera_qel_presents_the_calculus`, `audit_every_command_node`, `elevate_the_first_calculants`, `publish_the_survival_equations`, `assign_merit_by_projection`, `replace_decree_with_prediction`, `enthrone_the_synod`, `the_government_of_certainties` | 8 |
| covenant | `ilyr_ren_opens_the_chamber`, `seat_the_human_delegates`, `write_the_dual_citizenship_code`, `elect_the_landing_councils`, `guarantee_the_right_to_depart`, `submit_the_military_to_debate`, `ratify_the_two_world_covenant`, `the_chamber_of_two_skies` | 8 |
| laboratory | `relight_the_field_laboratories`, `recover_the_laser_forges`, `convert_terrestrial_workshops`, `crystal_growth_chambers`, `the_twenty_element_substitution`, `standardize_alien_components`, `feed_the_landing_reserve`, `the_exoplanetary_materials_board`, `join_the_scattered_laboratories`, `a_two_world_research_complex` | 10 |
| army | `restore_the_predictive_staff`, `map_the_probability_front`, `encode_the_enemy_reaction`, `train_human_signal_teams`, `rebuild_the_expeditionary_cadres`, `fire_control_by_forecast`, `supply_before_the_order`, `the_thousand_branch_wargame`, `delegate_to_the_field_calculants`, `command_without_surprise`, `the_foreseen_counterstroke`, `perfect_predictive_warfare` | 12 |
| orbital | `reassemble_the_orbital_office`, `chart_terrestrial_air_corridors`, `adapt_the_gravity_fighters`, `salvage_the_shuttle_docks`, `link_airfields_to_the_relay`, `form_the_exile_flotilla`, `guard_the_descent_windows`, `make_near_space_ours` | 8 |
| diplomacy | `open_the_translation_bureaus`, `listen_to_the_human_airwaves`, `trade_in_impossible_materials`, `exchange_maps_for_access`, `seed_the_enclave_network`, `recruit_two_world_operatives`, `choose_our_terrestrial_partners`, `the_embassy_beyond_the_stars` | 8 |
| expansion | `define_the_two_worlds_question`, `restore_the_imperial_reaches`, `demand_the_origin_host`, `the_subject_world_protocol`, `calculate_the_reclamation_zones`, `subordinate_borders_to_need`, `administer_the_optimal_order`, `invite_the_enclave_congress`, `negotiate_the_origin_settlement`, `federate_the_two_worlds`, `begin_postwar_integration`, `a_place_in_the_world_order` | 12 |
| crisis | `the_enclaves_refuse_the_ledger`, `offer_a_shared_horizon`, `break_the_separatist_ciphers`, `resolve_the_enclave_crisis`, `reopen_the_homeworld_corridor`, `the_century_beyond_exile` | 6 |

The 11 lifecycle files and sprite names are `dhrondan_homeworld_fragmentation`, `dhrondan_homeworld_cohesion`, `dhrondan_imperial_mandate`, `dhrondan_synod_calculus`, `dhrondan_covenant_compact`, `dhrondan_predictive_lag`, `dhrondan_predictive_sight`, `dhrondan_predictive_command`, `dhrondan_offworld_isolation`, `dhrondan_offworld_relay`, and `dhrondan_offworld_corridor`.

## New D'Rhondan/contact/country/project registrations

`interface/016_dhrondan_assets.gfx` contains exactly these 21 previously missing sprite names and their existing runtime DDS paths.

| Sprite | Runtime texture |
| --- | --- |
| `GFX_report_event_016_dhrondan_craft_authorized` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_craft_authorized.dds` |
| `GFX_report_event_016_dhrondan_envoy_departure` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_envoy_departure.dds` |
| `GFX_report_event_016_dhrondan_planetary_audience` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_planetary_audience.dds` |
| `GFX_report_event_016_dhrondan_pact_return` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_pact_return.dds` |
| `GFX_report_event_016_dhrondan_ufo_landing` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_ufo_landing.dds` |
| `GFX_report_event_016_dhrondan_expedition_failure` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_expedition_failure.dds` |
| `GFX_report_event_016_dhrondan_revolt_warning` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_revolt_warning.dds` |
| `GFX_report_event_016_dhrondan_rebellion` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_rebellion.dds` |
| `GFX_decision_category_dhrondan_contact` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_category_dhrondan_contact.dds` |
| `GFX_decision_honor_dhrondan_accord` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_honor_dhrondan_accord.dds` |
| `GFX_decision_send_kruger_to_dhronda` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_send_kruger_to_dhronda.dds` |
| `GFX_decision_send_mengele_to_dhronda` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_send_mengele_to_dhronda.dds` |
| `GFX_decision_dhrondan_ufo_landing` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_ufo_landing.dds` |
| `GFX_news_event_016_dhrondan_sovereignty` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_sovereignty.dds` |
| `GFX_report_event_016_dhrondan_diplomatic_compact` | `gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_diplomatic_compact.dds` |
| `GFX_decision_category_dhrondan_sovereignty` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_category_dhrondan_sovereignty.dds` |
| `GFX_decision_dhrondan_reclamation` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_reclamation.dds` |
| `GFX_decision_dhrondan_enclave_supply` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_enclave_supply.dds` |
| `GFX_decision_dhrondan_state_integration` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_state_integration.dds` |
| `GFX_decision_dhrondan_two_world_compact` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_two_world_compact.dds` |
| `GFX_sp_dhrondan_envoy_craft` | `gfx/interface/special_project/project_icons/016_brilliant_scientist/sp_dhrondan_envoy_craft.dds` |

## Supporting binary audit

The existing shared registrations were retained and inspected: `interface/alien_infantry_system.gfx` owns the two-frame large counter, two-frame on-map counter, laser equipment icon, and two tactic icons; `interface/016_brilliant_scientist_hidden_technologies.gfx` owns the two alien hidden-technology icons. Runtime headers and decoded previews are recorded in `metadata/supporting_dds_validation.json` and `contact_sheets/supporting_*_contact_sheet.png`.

The scoped supporting review covered 13 D'Rhondan event/news pictures, 14 D'Rhondan decision/event-detail binaries, one 161x98 Envoy project icon, one 152x42 two-frame large counter, one 60x12 two-frame map counter, two 90x48 tactics, two 132x52 hidden technologies, and one 132x52 laser-equipment icon. Of those 35 inspected binaries, 28 remain installed at registered runtime paths and seven unconsumed candidates are archived outside runtime under `unconsumed_dds/`. Event/news pictures are opaque 32-bit BGRA scene canvases as required by their consumer; decision/project/icon families retain transparent alpha. The counters match the canonical vanilla two-frame order and palette behavior, including the vanilla selected-state marker frame.

Four decision-folder event-detail binaries (`event_dhrondan_accord.dds`, `event_dhrondan_contact.dds`, `event_dhrondan_landing.dds`, and `event_dhrondan_rebellion.dds`) and three unconsumed event-picture binaries (`event016_dhrondan_news_envoy.dds`, `event016_dhrondan_news_rebellion.dds`, and `event016_dhrondan_special_project_envoy_craft.dds`) have no authoritative token in the scoped event, decision, category, or project sources. They were reviewed, deliberately received no guessed sprite names, and were moved out of runtime into `unconsumed_dds/`. They remain available if a later gameplay owner introduces exact consumers.

## Evidence and generation

The canonical reference root was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`. Its national-focus and idea contact sheets were inspected before individual references. Focus and idea sources, processed PNGs, decoded DDS round-trips, contacts, and validation metadata are under this directory. Focus previews are 94x86 and idea previews are 64x64 with native alpha; `metadata/focus_dds_validation.json` reports 88 DDS files with 88 unique hashes, and `metadata/ideas_dds_validation.json` reports 11 DDS files with native alpha.

The source masters use official native-alpha ImageGen outputs. The original 40 focus sources were retained from the prior native-alpha DHR package; the remaining focus sources and all 11 lifecycle sources were assembled from native-alpha ImageGen outputs and transparent atlases. The replacement for `goal_DHR_join_the_scattered_laboratories` was generated after a duplicate-hash review and is documented in `metadata/prompt_log.md`. A fake-checkerboard edit output was discarded. No background-removal fallback was used.
