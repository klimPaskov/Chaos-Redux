# Startup focus repair handoff

Date: 2026-09-13.

Scope: repair the main-menu startup loader errors attributed to national focus icons and malformed focus fields, while preserving existing focus layout, rewards, routes, icons, and AI weights.

Parent task: `/root/startup_focus`.

## Baseline and root causes

Baseline log: `docs/testing/live_qa/20260913_main_menu_startup/logs/cycle_01/error.log`.

The baseline contains 107 `nationalfocus.cpp:642` missing-shine errors: 24 in `common/national_focus/012_africa_continental_focus_tree.txt` and 83 in `common/national_focus/039_murder_mystery_assassin_focus.txt`.

Each affected focus already had a regular `icon = GFX_...` assignment and an existing DDS texture, but no matching `GFX_..._shine` SpriteType was registered.

The same baseline also contains five `Unexpected token: desc` parser errors in the Murder Mystery tree because `desc = ...` is not a valid national focus field; the standard `<focus_id>_desc` localisation keys already exist.

## Changes

Added `interface/startup_focus_shine.gfx` with 91 explicit animated shine registrations: 8 Gods of Africa aliases and 83 Murder Mystery aliases.

Every shine uses the exact regular icon DDS as both `texturefile` and `animationmaskfile`, plus the vanilla `gfx/interface/goals/shine_overlay.dds` with the two scrolling passes at `-90.0` and `90.0` degrees, `0.75` seconds, additive blending, and `legacy_lazy_load = no`.

Removed five invalid `desc = ...` lines from `common/national_focus/039_murder_mystery_assassin_focus.txt` at the affected focus blocks; the existing standard localisation keys remain in `localisation/english/039_murder_mystery_l_english.yml`.

Pre-edit bytes for the changed focus source are backed up at `docs/testing/live_qa/20260913_main_menu_startup/baseline/focus/common/national_focus/039_murder_mystery_assassin_focus.txt`.

Backup SHA-256: `8630B43531EF8820C0E89FD2CF4D3B62F4CE4A9F19155403F574125D6C0711DE`.

Current focus-source SHA-256: `FF920EB947D9929E863119141EB4DC04C53507935077066A38870104F432E74F`.

No focus IDs, regular icon assignments, prerequisites, routes, rewards, layout coordinates, or AI weights were changed.

## Route coverage

| Tree | Existing focus count | Route/layout result |
| --- | ---: | --- |
| `africa_continental_focus_tree` | 300 | Existing route graph preserved; MCP layout hash remains `a6eac361886709d8b616eb52b616b81f404d9640784b91c74f956efd7b942e2d`. |
| `murder_mystery_assassin_focus_tree` | 83 | Existing route graph preserved; MCP layout hash remains `01a9c1080d3a8864a208b3bea5dec6de405b10c4e15e8b29ab339bcbf3d0c9e9`. |

The focus-repair tranche adds no route, branch, prerequisite, reward, or layout content.

## Missing or simplified content

No simplifications were introduced.

No focus content, reward, route, icon art, or AI behavior was removed or replaced.

The existing Africa layout and repeated generic reward diagnostics remain outside this loader-error scope.

## Icon coverage

| Source | Baseline affected focuses | Existing regular aliases | New shine aliases |
| --- | ---: | ---: | ---: |
| `012_africa_continental_focus_tree.txt` Gods of Africa section | 24 | 8 | 8 |
| `039_murder_mystery_assassin_focus.txt` | 83 | 83 | 83 |

Static mapping check: all 107 baseline focus IDs map to a registered shine alias, with zero unregistered mappings.

New Africa aliases:
- `GFX_goal_012_africa_gods_proclamation_institution_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_proclamation_institution.dds`
- `GFX_goal_012_africa_gods_reciprocal_doctrine_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_reciprocal_doctrine.dds`
- `GFX_goal_012_africa_gods_extractive_doctrine_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_extractive_doctrine.dds`
- `GFX_goal_012_africa_gods_provision_logistics_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_provision_logistics.dds`
- `GFX_goal_012_africa_gods_oaths_diplomacy_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_oaths_diplomacy.dds`
- `GFX_goal_012_africa_gods_protection_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_protection.dds`
- `GFX_goal_012_africa_gods_judgment_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_judgment.dds`
- `GFX_goal_012_africa_gods_continental_settlement_shine` → `gfx/interface/goals/012_africa/gods_of_africa/goal_012_africa_gods_continental_settlement.dds`

New Murder Mystery aliases:
- `GFX_goal_039_murder_mystery_secure_the_empty_chair_shine` → `gfx/interface/goals/039_murder_mystery/secure_the_empty_chair.dds`
- `GFX_goal_039_murder_mystery_guard_the_constitution_shine` → `gfx/interface/goals/039_murder_mystery/guard_the_constitution.dds`
- `GFX_goal_039_murder_mystery_inventory_the_captured_state_shine` → `gfx/interface/goals/039_murder_mystery/inventory_the_captured_state.dds`
- `GFX_goal_039_murder_mystery_ration_the_front_shine` → `gfx/interface/goals/039_murder_mystery/ration_the_front.dds`
- `GFX_goal_039_murder_mystery_organize_first_cadres_shine` → `gfx/interface/goals/039_murder_mystery/organize_first_cadres.dds`
- `GFX_goal_039_murder_mystery_protect_the_case_team_shine` → `gfx/interface/goals/039_murder_mystery/protect_the_case_team.dds`
- `GFX_goal_039_murder_mystery_establish_case_command_shine` → `gfx/interface/goals/039_murder_mystery/establish_case_command.dds`
- `GFX_goal_039_murder_mystery_open_brotherhood_operations_shine` → `gfx/interface/goals/039_murder_mystery/open_brotherhood_operations.dds`
- `GFX_goal_039_murder_mystery_map_the_first_routes_shine` → `gfx/interface/goals/039_murder_mystery/map_the_first_routes.dds`
- `GFX_goal_039_murder_mystery_choose_the_public_mask_shine` → `gfx/interface/goals/039_murder_mystery/choose_the_public_mask.dds`
- `GFX_goal_039_murder_mystery_write_revocable_orders_shine` → `gfx/interface/goals/039_murder_mystery/write_revocable_orders.dds`
- `GFX_goal_039_murder_mystery_leadership_is_a_crime_shine` → `gfx/interface/goals/039_murder_mystery/leadership_is_a_crime.dds`
- `GFX_goal_039_murder_mystery_settle_the_command_dispute_shine` → `gfx/interface/goals/039_murder_mystery/settle_the_command_dispute.dds`
- `GFX_goal_039_murder_mystery_protect_the_first_knife_shine` → `gfx/interface/goals/039_murder_mystery/protect_the_first_knife.dds`
- `GFX_goal_039_murder_mystery_mandate_the_subjects_shine` → `gfx/interface/goals/039_murder_mystery/mandate_the_subjects.dds`
- `GFX_goal_039_murder_mystery_three_answers_to_power_shine` → `gfx/interface/goals/039_murder_mystery/three_answers_to_power.dds`
- `GFX_goal_039_murder_mystery_choose_hidden_hand_shine` → `gfx/interface/goals/039_murder_mystery/choose_hidden_hand.dds`
- `GFX_goal_039_murder_mystery_centralize_the_directorate_shine` → `gfx/interface/goals/039_murder_mystery/centralize_the_directorate.dds`
- `GFX_goal_039_murder_mystery_secure_the_inner_circle_shine` → `gfx/interface/goals/039_murder_mystery/secure_the_inner_circle.dds`
- `GFX_goal_039_murder_mystery_strengthen_the_first_knife_shine` → `gfx/interface/goals/039_murder_mystery/strengthen_the_first_knife.dds`
- `GFX_goal_039_murder_mystery_command_the_subjects_shine` → `gfx/interface/goals/039_murder_mystery/command_the_subjects.dds`
- `GFX_goal_039_murder_mystery_choose_cells_without_masters_shine` → `gfx/interface/goals/039_murder_mystery/choose_cells_without_masters.dds`
- `GFX_goal_039_murder_mystery_federate_the_cell_councils_shine` → `gfx/interface/goals/039_murder_mystery/federate_the_cell_councils.dds`
- `GFX_goal_039_murder_mystery_arm_local_autonomy_shine` → `gfx/interface/goals/039_murder_mystery/arm_local_autonomy.dds`
- `GFX_goal_039_murder_mystery_share_the_case_file_shine` → `gfx/interface/goals/039_murder_mystery/share_the_case_file.dds`
- `GFX_goal_039_murder_mystery_survive_without_a_chair_shine` → `gfx/interface/goals/039_murder_mystery/survive_without_a_chair.dds`
- `GFX_goal_039_murder_mystery_choose_necessary_mask_shine` → `gfx/interface/goals/039_murder_mystery/choose_necessary_mask.dds`
- `GFX_goal_039_murder_mystery_formalize_the_ministries_shine` → `gfx/interface/goals/039_murder_mystery/formalize_the_ministries.dds`
- `GFX_goal_039_murder_mystery_recognize_the_public_state_shine` → `gfx/interface/goals/039_murder_mystery/recognize_the_public_state.dds`
- `GFX_goal_039_murder_mystery_negotiate_the_contracts_shine` → `gfx/interface/goals/039_murder_mystery/negotiate_the_contracts.dds`
- `GFX_goal_039_murder_mystery_return_the_mask_shine` → `gfx/interface/goals/039_murder_mystery/return_the_mask.dds`
- `GFX_goal_039_murder_mystery_build_clandestine_workshops_shine` → `gfx/interface/goals/039_murder_mystery/build_clandestine_workshops.dds`
- `GFX_goal_039_murder_mystery_disperse_the_tools_shine` → `gfx/interface/goals/039_murder_mystery/disperse_the_tools.dds`
- `GFX_goal_039_murder_mystery_local_repair_corps_shine` → `gfx/interface/goals/039_murder_mystery/local_repair_corps.dds`
- `GFX_goal_039_murder_mystery_hide_the_supply_lines_shine` → `gfx/interface/goals/039_murder_mystery/hide_the_supply_lines.dds`
- `GFX_goal_039_murder_mystery_workshop_economy_shine` → `gfx/interface/goals/039_murder_mystery/workshop_economy.dds`
- `GFX_goal_039_murder_mystery_seize_state_industry_shine` → `gfx/interface/goals/039_murder_mystery/seize_state_industry.dds`
- `GFX_goal_039_murder_mystery_capture_the_depots_shine` → `gfx/interface/goals/039_murder_mystery/capture_the_depots.dds`
- `GFX_goal_039_murder_mystery_rebuild_the_rail_grid_shine` → `gfx/interface/goals/039_murder_mystery/rebuild_the_rail_grid.dds`
- `GFX_goal_039_murder_mystery_convert_the_heavy_shops_shine` → `gfx/interface/goals/039_murder_mystery/convert_the_heavy_shops.dds`
- `GFX_goal_039_murder_mystery_industry_board_shine` → `gfx/interface/goals/039_murder_mystery/industry_board.dds`
- `GFX_goal_039_murder_mystery_pragmatic_contracts_shine` → `gfx/interface/goals/039_murder_mystery/pragmatic_contracts.dds`
- `GFX_goal_039_murder_mystery_neutral_imports_shine` → `gfx/interface/goals/039_murder_mystery/neutral_imports.dds`
- `GFX_goal_039_murder_mystery_vehicle_licenses_shine` → `gfx/interface/goals/039_murder_mystery/vehicle_licenses.dds`
- `GFX_goal_039_murder_mystery_production_board_shine` → `gfx/interface/goals/039_murder_mystery/production_board.dds`
- `GFX_goal_039_murder_mystery_trade_without_recognition_shine` → `gfx/interface/goals/039_murder_mystery/trade_without_recognition.dds`
- `GFX_goal_039_murder_mystery_cadre_training_shine` → `gfx/interface/goals/039_murder_mystery/cadre_training.dds`
- `GFX_goal_039_murder_mystery_night_doctrine_shine` → `gfx/interface/goals/039_murder_mystery/night_doctrine.dds`
- `GFX_goal_039_murder_mystery_saboteur_cells_shine` → `gfx/interface/goals/039_murder_mystery/saboteur_cells.dds`
- `GFX_goal_039_murder_mystery_shadow_companies_shine` → `gfx/interface/goals/039_murder_mystery/shadow_companies.dds`
- `GFX_goal_039_murder_mystery_silent_guard_shine` → `gfx/interface/goals/039_murder_mystery/silent_guard.dds`
- `GFX_goal_039_murder_mystery_conventional_adaptation_shine` → `gfx/interface/goals/039_murder_mystery/conventional_adaptation.dds`
- `GFX_goal_039_murder_mystery_force_standards_shine` → `gfx/interface/goals/039_murder_mystery/force_standards.dds`
- `GFX_goal_039_murder_mystery_master_cadre_shine` → `gfx/interface/goals/039_murder_mystery/master_cadre.dds`
- `GFX_goal_039_murder_mystery_mechanized_infiltration_shine` → `gfx/interface/goals/039_murder_mystery/mechanized_infiltration.dds`
- `GFX_goal_039_murder_mystery_elite_force_caps_shine` → `gfx/interface/goals/039_murder_mystery/elite_force_caps.dds`
- `GFX_goal_039_murder_mystery_intelligence_registry_shine` → `gfx/interface/goals/039_murder_mystery/intelligence_registry.dds`
- `GFX_goal_039_murder_mystery_secure_comms_shine` → `gfx/interface/goals/039_murder_mystery/secure_comms.dds`
- `GFX_goal_039_murder_mystery_evidence_exchange_shine` → `gfx/interface/goals/039_murder_mystery/evidence_exchange.dds`
- `GFX_goal_039_murder_mystery_foreign_contacts_shine` → `gfx/interface/goals/039_murder_mystery/foreign_contacts.dds`
- `GFX_goal_039_murder_mystery_foreign_cells_shine` → `gfx/interface/goals/039_murder_mystery/foreign_cells.dds`
- `GFX_goal_039_murder_mystery_counterintelligence_shine` → `gfx/interface/goals/039_murder_mystery/counterintelligence.dds`
- `GFX_goal_039_murder_mystery_cell_immunity_shine` → `gfx/interface/goals/039_murder_mystery/cell_immunity.dds`
- `GFX_goal_039_murder_mystery_international_operations_shine` → `gfx/interface/goals/039_murder_mystery/international_operations.dds`
- `GFX_goal_039_murder_mystery_insurgency_preparation_shine` → `gfx/interface/goals/039_murder_mystery/insurgency_preparation.dds`
- `GFX_goal_039_murder_mystery_recognize_movement_shine` → `gfx/interface/goals/039_murder_mystery/recognize_movement.dds`
- `GFX_goal_039_murder_mystery_provisional_administration_shine` → `gfx/interface/goals/039_murder_mystery/provisional_administration.dds`
- `GFX_goal_039_murder_mystery_subject_compact_shine` → `gfx/interface/goals/039_murder_mystery/subject_compact.dds`
- `GFX_goal_039_murder_mystery_campaign_sectors_shine` → `gfx/interface/goals/039_murder_mystery/campaign_sectors.dds`
- `GFX_goal_039_murder_mystery_protect_derivatives_shine` → `gfx/interface/goals/039_murder_mystery/protect_derivatives.dds`
- `GFX_goal_039_murder_mystery_central_demands_shine` → `gfx/interface/goals/039_murder_mystery/central_demands.dds`
- `GFX_goal_039_murder_mystery_staged_integration_shine` → `gfx/interface/goals/039_murder_mystery/staged_integration.dds`
- `GFX_goal_039_murder_mystery_host_archive_shine` → `gfx/interface/goals/039_murder_mystery/host_archive.dds`
- `GFX_goal_039_murder_mystery_host_capital_shine` → `gfx/interface/goals/039_murder_mystery/host_capital.dds`
- `GFX_goal_039_murder_mystery_necessary_compromise_shine` → `gfx/interface/goals/039_murder_mystery/necessary_compromise.dds`
- `GFX_goal_039_murder_mystery_prepare_world_collapse_shine` → `gfx/interface/goals/039_murder_mystery/prepare_world_collapse.dds`
- `GFX_goal_039_murder_mystery_command_settlement_v_shine` → `gfx/interface/goals/039_murder_mystery/command_settlement_v.dds`
- `GFX_goal_039_murder_mystery_terminal_recruitment_shine` → `gfx/interface/goals/039_murder_mystery/terminal_recruitment.dds`
- `GFX_goal_039_murder_mystery_leadership_dossiers_shine` → `gfx/interface/goals/039_murder_mystery/leadership_dossiers.dds`
- `GFX_goal_039_murder_mystery_synchronize_uprisings_shine` → `gfx/interface/goals/039_murder_mystery/synchronize_uprisings.dds`
- `GFX_goal_039_murder_mystery_dismantle_governments_shine` → `gfx/interface/goals/039_murder_mystery/dismantle_governments.dds`
- `GFX_goal_039_murder_mystery_terminal_logistics_shine` → `gfx/interface/goals/039_murder_mystery/terminal_logistics.dds`
- `GFX_goal_039_murder_mystery_activate_world_of_anarchy_shine` → `gfx/interface/goals/039_murder_mystery/activate_world_of_anarchy.dds`

Affected focus IDs from the baseline log:

Africa, 24:
- `gods_of_africa_focus_prepare_proclamation` at source line 7324.
- `gods_of_africa_focus_office_voices` at source line 7356.
- `gods_of_africa_focus_continental_proclamation` at source line 7387.
- `gods_of_africa_focus_reciprocal_covenant` at source line 7422.
- `gods_of_africa_focus_sovereign_exaction` at source line 7461.
- `gods_of_africa_focus_measure_needs` at source line 7503.
- `gods_of_africa_focus_continental_arsenals` at source line 7533.
- `gods_of_africa_focus_rails_ports_fuel` at source line 7565.
- `gods_of_africa_focus_continental_reserve` at source line 7595.
- `gods_of_africa_focus_recognize_voice` at source line 7629.
- `gods_of_africa_focus_return_soil` at source line 7658.
- `gods_of_africa_focus_end_sponsorship` at source line 7690.
- `gods_of_africa_focus_security_oaths` at source line 7722.
- `gods_of_africa_focus_shelter_faithful` at source line 7755.
- `gods_of_africa_focus_relief_beyond` at source line 7785.
- `gods_of_africa_focus_expedition` at source line 7814.
- `gods_of_africa_focus_final_council` at source line 7846.
- `gods_of_africa_focus_record_refusal` at source line 7878.
- `gods_of_africa_focus_reach_beyond_coast` at source line 7907.
- `gods_of_africa_focus_let_world_answer` at source line 7936.
- `gods_of_africa_focus_hand_judgment` at source line 7968.
- `gods_of_africa_focus_no_sanctuary` at source line 8000.
- `gods_of_africa_focus_last_sentence` at source line 8030.
- `gods_of_africa_focus_africa_speaks_for_itself` at source line 8070.

Murder Mystery, 83:
- `murder_mystery_secure_the_empty_chair` at source line 80.
- `murder_mystery_guard_the_constitution` at source line 91.
- `murder_mystery_inventory_the_captured_state` at source line 103.
- `murder_mystery_ration_the_front` at source line 115.
- `murder_mystery_organize_first_cadres` at source line 127.
- `murder_mystery_protect_the_case_team` at source line 139.
- `murder_mystery_establish_case_command` at source line 151.
- `murder_mystery_open_brotherhood_operations` at source line 164.
- `murder_mystery_map_the_first_routes` at source line 176.
- `murder_mystery_choose_the_public_mask` at source line 188.
- `murder_mystery_write_revocable_orders` at source line 205.
- `murder_mystery_leadership_is_a_crime` at source line 217.
- `murder_mystery_settle_the_command_dispute` at source line 230.
- `murder_mystery_protect_the_first_knife` at source line 242.
- `murder_mystery_mandate_the_subjects` at source line 254.
- `murder_mystery_three_answers_to_power` at source line 266.
- `murder_mystery_choose_hidden_hand` at source line 283.
- `murder_mystery_centralize_the_directorate` at source line 297.
- `murder_mystery_secure_the_inner_circle` at source line 309.
- `murder_mystery_strengthen_the_first_knife` at source line 321.
- `murder_mystery_command_the_subjects` at source line 333.
- `murder_mystery_choose_cells_without_masters` at source line 346.
- `murder_mystery_federate_the_cell_councils` at source line 360.
- `murder_mystery_arm_local_autonomy` at source line 372.
- `murder_mystery_share_the_case_file` at source line 384.
- `murder_mystery_survive_without_a_chair` at source line 396.
- `murder_mystery_choose_necessary_mask` at source line 409.
- `murder_mystery_formalize_the_ministries` at source line 423.
- `murder_mystery_recognize_the_public_state` at source line 435.
- `murder_mystery_negotiate_the_contracts` at source line 447.
- `murder_mystery_return_the_mask` at source line 459.
- `murder_mystery_build_clandestine_workshops` at source line 476.
- `murder_mystery_disperse_the_tools` at source line 488.
- `murder_mystery_local_repair_corps` at source line 500.
- `murder_mystery_hide_the_supply_lines` at source line 512.
- `murder_mystery_workshop_economy` at source line 524.
- `murder_mystery_seize_state_industry` at source line 537.
- `murder_mystery_capture_the_depots` at source line 549.
- `murder_mystery_rebuild_the_rail_grid` at source line 561.
- `murder_mystery_convert_the_heavy_shops` at source line 573.
- `murder_mystery_industry_board` at source line 585.
- `murder_mystery_pragmatic_contracts` at source line 598.
- `murder_mystery_neutral_imports` at source line 610.
- `murder_mystery_vehicle_licenses` at source line 622.
- `murder_mystery_production_board` at source line 634.
- `murder_mystery_trade_without_recognition` at source line 646.
- `murder_mystery_cadre_training` at source line 663.
- `murder_mystery_night_doctrine` at source line 675.
- `murder_mystery_saboteur_cells` at source line 687.
- `murder_mystery_shadow_companies` at source line 699.
- `murder_mystery_silent_guard` at source line 711.
- `murder_mystery_conventional_adaptation` at source line 723.
- `murder_mystery_force_standards` at source line 735.
- `murder_mystery_master_cadre` at source line 747.
- `murder_mystery_mechanized_infiltration` at source line 759.
- `murder_mystery_elite_force_caps` at source line 772.
- `murder_mystery_intelligence_registry` at source line 789.
- `murder_mystery_secure_comms` at source line 801.
- `murder_mystery_evidence_exchange` at source line 813.
- `murder_mystery_foreign_contacts` at source line 825.
- `murder_mystery_foreign_cells` at source line 837.
- `murder_mystery_counterintelligence` at source line 849.
- `murder_mystery_cell_immunity` at source line 861.
- `murder_mystery_international_operations` at source line 873.
- `murder_mystery_insurgency_preparation` at source line 885.
- `murder_mystery_recognize_movement` at source line 902.
- `murder_mystery_provisional_administration` at source line 914.
- `murder_mystery_subject_compact` at source line 926.
- `murder_mystery_campaign_sectors` at source line 938.
- `murder_mystery_protect_derivatives` at source line 950.
- `murder_mystery_central_demands` at source line 962.
- `murder_mystery_staged_integration` at source line 974.
- `murder_mystery_host_archive` at source line 986.
- `murder_mystery_host_capital` at source line 998.
- `murder_mystery_necessary_compromise` at source line 1010.
- `murder_mystery_prepare_world_collapse` at source line 1027.
- `murder_mystery_command_settlement_v` at source line 1039.
- `murder_mystery_terminal_recruitment` at source line 1051.
- `murder_mystery_leadership_dossiers` at source line 1063.
- `murder_mystery_synchronize_uprisings` at source line 1075.
- `murder_mystery_dismantle_governments` at source line 1088.
- `murder_mystery_terminal_logistics` at source line 1100.
- `murder_mystery_activate_world_of_anarchy` at source line 1112.

## Localisation and reward mismatch list

The five invalid fields were `murder_mystery_focus_establish_case_command_desc`, `murder_mystery_focus_leadership_is_a_crime_desc`, `murder_mystery_focus_mechanized_infiltration_desc`, `murder_mystery_focus_synchronize_uprisings_desc`, and `murder_mystery_focus_activate_world_of_anarchy_desc`.

The standard keys `murder_mystery_establish_case_command_desc`, `murder_mystery_leadership_is_a_crime_desc`, `murder_mystery_mechanized_infiltration_desc`, `murder_mystery_synchronize_uprisings_desc`, and `murder_mystery_activate_world_of_anarchy_desc` are present, so removing the invalid field preserves the intended descriptions.

No reward or focus-name mismatch was changed.

## AI behavior gaps

No AI weights or probability-bearing syntax changed.

All existing `ai_will_do` blocks remain byte-for-byte in their original focus source positions apart from the five removed invalid `desc` lines.

No probability target was applied, so no baseline/compare run was required for this tranche.

## MCP evidence

Pre-edit `hoi4.focus_inspect` artifacts:
- Africa: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3fe28bf0e334ee6941e46818fe48a9f24664f8ac78a1d68e519f7ca19c748c0f/62efd3211eb976f983406ab1602784ec7f82c59203a64fad706862106b2759b6/focus-inspect.55b58c4294e18877.json`.
- Murder Mystery: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f1dd762ca2d59123e4658e6876dbeb300d4a6420ff9aef58815753b0940c173/c8e88f1bc4c93a0c180afdb8d0d657c3f07550255a1571a610da20c177dc18c4/focus-inspect.55b58c4294e18877.json`.

Post-edit `hoi4.focus_inspect` artifacts:
- Africa: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f838e116c0cf0fbb94cba095e0ba8910520b9e5bd1dc1f032fdad6d6b8faa3cb/157f15c0ab317e62738df8743c8878258dc3d60db97f67dbf0277afd715c85ea/focus-inspect.5d73fcced5a4e65d.json`.
- Murder Mystery: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5201301f5f2386c9cf07240315c5f430310187f6a723eadcb3b9ce44e4299dbf/f81b290319b8541524ab4ad6dcd4c0f72d5181a68497aebe2421a0532f38651f/focus-inspect.5d73fcced5a4e65d.json`.

Post-edit `hoi4.focus_render` artifacts:
- Africa HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42b1ce91b3b3857f0794093d449618b76654fd3e7f2f301e7833df527766c600/6b036d7eac694c068382bef6785e2db92f737eeccef48d1d37ddab3b9e04c2af/africa_continental_focus_tree.focus.html`.
- Murder Mystery HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c11193a86592046d605d5ece2e70aa3854dead99edf135ce54cdca6894b7333/e67afaacf6ddc498db9dbdf845883fd508ce6c34d565d6db9fe84c19bf648bf9/murder_mystery_assassin_focus_tree.focus.html`.

Both post-edit MCP inspect/render calls returned `status = ok` with `validation.passed = true` and unchanged layout hashes.

MCP diagnostics still report only pre-existing Africa spacing/crossing/repeated-reward warnings and the unrelated generic continuous-focus localisation warning.

## Validation and limits

Static GFX validation found 91 `SpriteType` definitions, 91 unique shine names, 182 animation blocks, 91 `legacy_lazy_load = no` entries, zero duplicate names, and zero missing focus DDS paths.

Static source validation found zero remaining `desc =` fields in the Murder Mystery focus file and all five standard description keys present.

The parent-owned cycle02 fresh-start validation log is `docs/testing/live_qa/20260913_main_menu_startup/logs/cycle_02/error.log`; this subagent did not launch Hearts of Iron IV or use desktop control.

Cycle02 contains zero `nationalfocus.cpp:642` lines, zero `Missing icon shine for focus` lines, and zero `Unexpected token: desc` lines.

Cycle02 still contains 446 total error-log lines outside this focus scope, led by `effectimplementation.cpp` 128, `persistent.cpp` 112, `trigger.cpp` 73, `database_scoped_variables.cpp` 51, `triggerimplementation.cpp` 44, asset texture lines 12, and `pdxmeshtype.cpp` 1.

Cycle02 `result.txt` records: `Main menu visually verified; process stopped for repairs.`

The installed focus MCP does not expose a standalone SpriteType/GFX parser, so GFX syntax confidence comes from the exact vanilla `interface/goals_shine.gfx` precedent plus static structure/path checks.

## Changed files

- `interface/startup_focus_shine.gfx`.
- `common/national_focus/039_murder_mystery_assassin_focus.txt`.
- `docs/testing/live_qa/20260913_main_menu_startup/baseline/focus/common/national_focus/039_murder_mystery_assassin_focus.txt` (exact pre-edit backup).
- `docs/testing/live_qa/20260913_main_menu_startup/focus_repair_handoff.md` (this handoff).

No commit was created.
