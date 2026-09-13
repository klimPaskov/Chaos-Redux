# Missile lifecycle reference evidence

This exact-token inventory covers current gameplay, event, interface and localisation sources.
It records writers, readers, nested helper owners, and direct callers for manual continuation review.

## missiles_ai_reserve_floor

- `common\scripted_effects\032_missiles_operations_effects.txt:2194` (`missiles_reserve_operation_resources`): `set_temp_variable = { missiles_ai_reserve_floor = constant:missiles_reserve.operation_reservation_floor }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2200` (`missiles_reserve_operation_resources`): `set_temp_variable = { missiles_ai_reserve_floor = constant:missiles_reserve.automatic_reserve_floor }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2208` (`missiles_reserve_operation_resources`): `check_variable = { var = missiles_reserve_after_operation value = missiles_ai_reserve_floor compare = greater_than_or_equals }`

## missiles_annex_site_receipt

- `common\scripted_effects\032_missiles_operations_effects.txt:5271` (`missiles_cleanup_removed_country`): `set_temp_variable = { missiles_annex_site_receipt = ROOT.missiles_removed_reserve_remaining }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5274` (`missiles_cleanup_removed_country`): `set_temp_variable = { missiles_annex_site_receipt = constant:missiles_program_value.zero }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5278` (`missiles_cleanup_removed_country`): `check_variable = { var = missiles_annex_site_receipt value = missiles_site_capacity compare = greater_than }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5280` (`missiles_cleanup_removed_country`): `set_temp_variable = { missiles_annex_site_receipt = missiles_site_capacity }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5283` (`missiles_cleanup_removed_country`): `limit = { check_variable = { var = missiles_annex_site_receipt value = constant:missiles_program_value.zero compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5285` (`missiles_cleanup_removed_country`): `add_to_variable = { missiles_site_captured_reserve = missiles_annex_site_receipt }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5301` (`missiles_cleanup_removed_country`): `add_to_variable = { missiles_captured_reserve_held = missiles_annex_site_receipt }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5310` (`missiles_cleanup_removed_country`): `subtract_from_variable = { missiles_removed_reserve_remaining = missiles_annex_site_receipt }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5311` (`missiles_cleanup_removed_country`): `add_to_variable = { missiles_removed_reserve_distributed = missiles_annex_site_receipt }`

## missiles_captured_reserve_amount

- `common\scripted_effects\032_missiles_operations_effects.txt:798` (`missiles_transfer_captured_reserve`): `set_temp_variable = { missiles_captured_reserve_amount = constant:missiles_program_value.zero }`
- `common\scripted_effects\032_missiles_operations_effects.txt:805` (`missiles_transfer_captured_reserve`): `set_temp_variable = { missiles_captured_reserve_amount = missiles_site_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:806` (`missiles_transfer_captured_reserve`): `set_temp_variable = { missiles_captured_reserve_loss = missiles_captured_reserve_amount }`
- `common\scripted_effects\032_missiles_operations_effects.txt:809` (`missiles_transfer_captured_reserve`): `subtract_from_temp_variable = { missiles_captured_reserve_amount = missiles_captured_reserve_loss }`
- `common\scripted_effects\032_missiles_operations_effects.txt:818` (`missiles_transfer_captured_reserve`): `multiply_temp_variable = { var = missiles_captured_reserve_amount value = missiles_capture_damage_survival }`
- `common\scripted_effects\032_missiles_operations_effects.txt:819` (`missiles_transfer_captured_reserve`): `divide_temp_variable = { var = missiles_captured_reserve_amount value = constant:missiles_program_value.one_hundred if_zero = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:821` (`missiles_transfer_captured_reserve`): `round_temp_variable = missiles_captured_reserve_amount`
- `common\scripted_effects\032_missiles_operations_effects.txt:822` (`missiles_transfer_captured_reserve`): `if = { limit = { check_variable = { var = missiles_captured_reserve_amount value = missiles_site_reserve compare = greater_than } } set_temp_variable = { missiles_captured_reserve_amount = missiles_site_reserve } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4804` (`missiles_handle_site_control_changed`): `limit = { check_variable = { var = missiles_captured_reserve_amount value = FROM.missiles_operational_reserve compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4805` (`missiles_handle_site_control_changed`): `set_temp_variable = { missiles_captured_reserve_amount = FROM.missiles_operational_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4823` (`missiles_handle_site_control_changed`): `limit = { check_variable = { var = missiles_captured_reserve_amount value = constant:missiles_program_value.zero compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4824` (`missiles_handle_site_control_changed`): `subtract_from_variable = { missiles_operational_reserve = missiles_captured_reserve_amount }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4836` (`missiles_handle_site_control_changed`): `set_variable = { missiles_site_captured_reserve = missiles_captured_reserve_amount }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4895` (`missiles_handle_site_control_changed`): `add_to_variable = { missiles_captured_reserve_held = missiles_captured_reserve_amount }`

## missiles_civil_war_child_reserve

- `common\scripted_effects\032_missiles_operations_effects.txt:5111` (`missiles_finalize_civil_war_split_child`): `set_temp_variable = { missiles_civil_war_child_reserve = constant:missiles_program_value.zero }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5119` (`missiles_finalize_civil_war_split_child`): `set_temp_variable = { missiles_civil_war_child_reserve = missiles_civil_war_site_pool }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5120` (`missiles_finalize_civil_war_split_child`): `multiply_temp_variable = { var = missiles_civil_war_child_reserve value = missiles_civil_war_received_capacity }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5121` (`missiles_finalize_civil_war_split_child`): `divide_temp_variable = { var = missiles_civil_war_child_reserve value = event_target:missiles_civil_war_parent.missiles_civil_war_split_original_capacity if_zero = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5122` (`missiles_finalize_civil_war_split_child`): `round_temp_variable = missiles_civil_war_child_reserve`
- `common\scripted_effects\032_missiles_operations_effects.txt:5125` (`missiles_finalize_civil_war_split_child`): `limit = { check_variable = { var = missiles_civil_war_child_reserve value = event_target:missiles_civil_war_parent.missiles_civil_war_split_original_reserve compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5126` (`missiles_finalize_civil_war_split_child`): `set_temp_variable = { missiles_civil_war_child_reserve = event_target:missiles_civil_war_parent.missiles_civil_war_split_original_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5128` (`missiles_finalize_civil_war_split_child`): `set_variable = { missiles_operational_reserve = missiles_civil_war_child_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5131` (`missiles_finalize_civil_war_split_child`): `set_variable = { missiles_civil_war_split_received_reserve = missiles_civil_war_child_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5143` (`missiles_finalize_civil_war_split_child`): `set_variable = { missiles_civil_war_split_child_reserve = missiles_civil_war_child_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5145` (`missiles_finalize_civil_war_split_child`): `subtract_from_variable = { missiles_operational_reserve = missiles_civil_war_child_reserve }`

## missiles_civil_war_site_pool

- `common\scripted_effects\032_missiles_operations_effects.txt:5108` (`missiles_finalize_civil_war_split_child`): `set_temp_variable = { missiles_civil_war_site_pool = event_target:missiles_civil_war_parent.missiles_civil_war_split_original_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5109` (`missiles_finalize_civil_war_split_child`): `multiply_temp_variable = { var = missiles_civil_war_site_pool value = constant:missiles_reserve.site_civil_war_reserve_share_percent }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5110` (`missiles_finalize_civil_war_split_child`): `divide_temp_variable = { var = missiles_civil_war_site_pool value = constant:missiles_program_value.one_hundred if_zero = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:5119` (`missiles_finalize_civil_war_split_child`): `set_temp_variable = { missiles_civil_war_child_reserve = missiles_civil_war_site_pool }`

## missiles_disaster_reserve_loss_calculated

- `common\scripted_effects\032_missiles_operations_effects.txt:3409` (`missiles_natural_disaster_damage_site`): `set_temp_variable = { missiles_disaster_reserve_loss_calculated = missiles_site_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:3410` (`missiles_natural_disaster_damage_site`): `multiply_temp_variable = { var = missiles_disaster_reserve_loss_calculated value = missiles_disaster_reserve_loss_percent }`
- `common\scripted_effects\032_missiles_operations_effects.txt:3411` (`missiles_natural_disaster_damage_site`): `divide_temp_variable = { var = missiles_disaster_reserve_loss_calculated value = constant:missiles_program_value.one_hundred if_zero = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:3412` (`missiles_natural_disaster_damage_site`): `round_temp_variable = missiles_disaster_reserve_loss_calculated`
- `common\scripted_effects\032_missiles_operations_effects.txt:3413` (`missiles_natural_disaster_damage_site`): `if = { limit = { check_variable = { var = missiles_disaster_reserve_loss_calculated value = missiles_site_reserve compare = greater_than } } set_temp_variable = { missiles_disaster_reserve_loss_calculated = missiles_site_reserve } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:3414` (`missiles_natural_disaster_damage_site`): `set_variable = { missiles_disaster_reserve_loss = missiles_disaster_reserve_loss_calculated }`

## missiles_empty_silos_ally_half_threshold

- `common\scripted_effects\032_missiles_operations_effects.txt:3805` (`missiles_record_operation_achievement_receipts`): `set_temp_variable = { missiles_empty_silos_ally_half_threshold = chaosx_032_empty_the_silos_opening_site_count }`
- `common\scripted_effects\032_missiles_operations_effects.txt:3806` (`missiles_record_operation_achievement_receipts`): `divide_temp_variable = { var = missiles_empty_silos_ally_half_threshold value = constant:missiles_program_value.two if_zero = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:3808` (`missiles_record_operation_achievement_receipts`): `limit = { check_variable = { var = chaosx_032_empty_silos_ally_removed_site_count value = missiles_empty_silos_ally_half_threshold compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4880` (`missiles_handle_site_control_changed`): `set_temp_variable = { missiles_empty_silos_ally_half_threshold = chaosx_032_empty_the_silos_opening_site_count }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4881` (`missiles_handle_site_control_changed`): `divide_temp_variable = { var = missiles_empty_silos_ally_half_threshold value = constant:missiles_program_value.two if_zero = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4883` (`missiles_handle_site_control_changed`): `limit = { check_variable = { var = chaosx_032_empty_silos_ally_removed_site_count value = missiles_empty_silos_ally_half_threshold compare = greater_than } }`

## missiles_evolution_selection

- `common\scripted_effects\032_missiles_operations_effects.txt:389` (`missiles_record_evolution_unlock`): `check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.saturation compare = equals }`
- `common\scripted_effects\032_missiles_operations_effects.txt:400` (`missiles_record_evolution_unlock`): `check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.unreliable_guidance compare = equals }`
- `common\scripted_effects\032_missiles_operations_effects.txt:411` (`missiles_record_evolution_unlock`): `check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.special_warheads compare = equals }`
- `common\scripted_effects\032_missiles_operations_effects.txt:422` (`missiles_record_evolution_unlock`): `check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.rogue_commands compare = equals }`
- `common\scripted_effects\032_missiles_operations_effects.txt:433` (`missiles_record_evolution_unlock`): `check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.automatic_retaliation compare = equals }`
- `common\scripted_effects\032_missiles_operations_effects.txt:458` (`missiles_schedule_evolution_track`): `check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.saturation compare = equals }`
- `common\scripted_effects\032_missiles_operations_effects.txt:477` (`missiles_schedule_evolution_track`): `limit = { check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.unreliable_guidance compare = equals } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:495` (`missiles_schedule_evolution_track`): `limit = { check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.special_warheads compare = equals } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:513` (`missiles_schedule_evolution_track`): `limit = { check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.rogue_commands compare = equals } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:531` (`missiles_schedule_evolution_track`): `limit = { check_variable = { var = missiles_evolution_selection value = constant:missiles_evolution.automatic_retaliation compare = equals } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:564` (`missiles_evaluate_evolution_unlocks`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.rogue_commands }`
- `common\scripted_effects\032_missiles_operations_effects.txt:575` (`missiles_evaluate_evolution_unlocks`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.unreliable_guidance }`
- `common\scripted_effects\032_missiles_operations_effects.txt:587` (`missiles_evaluate_evolution_unlocks`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.saturation }`
- `common\scripted_effects\032_missiles_operations_effects.txt:599` (`missiles_evaluate_evolution_unlocks`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.special_warheads }`
- `common\scripted_effects\032_missiles_operations_effects.txt:610` (`missiles_evaluate_evolution_unlocks`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.automatic_retaliation }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:98` (`missiles_scenario_prepare_profile_globals`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.saturation }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:114` (`missiles_scenario_prepare_profile_globals`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.unreliable_guidance }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:124` (`missiles_scenario_prepare_profile_globals`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.special_warheads }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:140` (`missiles_scenario_prepare_profile_globals`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.rogue_commands }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:150` (`missiles_scenario_prepare_profile_globals`): `set_temp_variable = { missiles_evolution_selection = constant:missiles_evolution.automatic_retaliation }`

## missiles_guidance_control_component

- `common\scripted_effects\032_missiles_operations_effects.txt:2377` (`missiles_calculate_operation_guidance`): `set_temp_variable = { missiles_guidance_control_component = missiles_operation_control_snapshot }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2378` (`missiles_calculate_operation_guidance`): `multiply_temp_variable = { var = missiles_guidance_control_component value = constant:missiles_guidance.command_step }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2379` (`missiles_calculate_operation_guidance`): `add_to_variable = { missiles_operation_guidance_score = missiles_guidance_control_component }`

## missiles_guidance_readiness_component

- `common\scripted_effects\032_missiles_operations_effects.txt:2374` (`missiles_calculate_operation_guidance`): `set_temp_variable = { missiles_guidance_readiness_component = missiles_operation_readiness_snapshot }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2375` (`missiles_calculate_operation_guidance`): `multiply_temp_variable = { var = missiles_guidance_readiness_component value = constant:missiles_guidance.readiness_step }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2376` (`missiles_calculate_operation_guidance`): `add_to_variable = { missiles_operation_guidance_score = missiles_guidance_readiness_component }`

## missiles_guidance_stage_component

- `common\scripted_effects\032_missiles_operations_effects.txt:2371` (`missiles_calculate_operation_guidance`): `set_temp_variable = { missiles_guidance_stage_component = missiles_program_stage }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2372` (`missiles_calculate_operation_guidance`): `multiply_temp_variable = { var = missiles_guidance_stage_component value = constant:missiles_guidance.technology_step }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2373` (`missiles_calculate_operation_guidance`): `add_to_variable = { missiles_operation_guidance_score = missiles_guidance_stage_component }`

## missiles_guidance_training_component

- `common\scripted_effects\032_missiles_operations_effects.txt:2382` (`missiles_calculate_operation_guidance`): `set_temp_variable = { missiles_guidance_training_component = missiles_guidance_training }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2383` (`missiles_calculate_operation_guidance`): `multiply_temp_variable = { var = missiles_guidance_training_component value = constant:missiles_guidance.training_step }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2384` (`missiles_calculate_operation_guidance`): `add_to_variable = { missiles_operation_guidance_score = missiles_guidance_training_component }`

## missiles_inherited_reserve_amount

- `common\scripted_effects\032_missiles_operations_effects.txt:4650` (`missiles_finalize_planned_inheritance`): `set_temp_variable = { missiles_inherited_reserve_amount = missiles_site_planned_reserve_receipt }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4656` (`missiles_finalize_planned_inheritance`): `check_variable = { var = missiles_operational_reserve value = missiles_inherited_reserve_amount compare = less_than }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4659` (`missiles_finalize_planned_inheritance`): `if = { limit = { has_variable = missiles_operational_reserve } set_temp_variable = { missiles_inherited_reserve_amount = missiles_operational_reserve } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4660` (`missiles_finalize_planned_inheritance`): `else = { set_temp_variable = { missiles_inherited_reserve_amount = constant:missiles_program_value.zero } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4675` (`missiles_finalize_planned_inheritance`): `limit = { check_variable = { var = missiles_inherited_reserve_amount value = constant:missiles_program_value.zero compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4676` (`missiles_finalize_planned_inheritance`): `subtract_from_variable = { missiles_operational_reserve = missiles_inherited_reserve_amount }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4688` (`missiles_finalize_planned_inheritance`): `set_variable = { missiles_site_captured_reserve = missiles_inherited_reserve_amount }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4705` (`missiles_finalize_planned_inheritance`): `add_to_variable = { missiles_captured_reserve_held = missiles_inherited_reserve_amount }`

## missiles_population_cap

- `common\scripted_effects\032_missiles_operations_effects.txt:2720` (`missiles_register_conventional_deaths`): `set_temp_variable = { missiles_population_cap = state_population_k }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2721` (`missiles_register_conventional_deaths`): `multiply_temp_variable = { var = missiles_population_cap value = constant:missiles_resolution.population_people_per_thousand }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2722` (`missiles_register_conventional_deaths`): `subtract_from_temp_variable = { missiles_population_cap = constant:missiles_operation_damage.population_minimum }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2724` (`missiles_register_conventional_deaths`): `if = { limit = { check_variable = { var = chaos_deaths_change value = missiles_population_cap compare = greater_than } } set_temp_variable = { chaos_deaths_change = missiles_population_cap } }`

## missiles_reach_stage

- `common\scripted_effects\032_missiles_operations_effects.txt:2084` (`missiles_calculate_operation_reach`): `set_temp_variable = { missiles_reach_stage = missiles_program_stage }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2085` (`missiles_calculate_operation_reach`): `multiply_temp_variable = { var = missiles_reach_stage value = constant:missiles_tuning.operation_range_stage_step }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2086` (`missiles_calculate_operation_reach`): `add_to_variable = { missiles_operation_reach_band = missiles_reach_stage }`

## missiles_reserve_after_operation

- `common\scripted_effects\032_missiles_operations_effects.txt:2192` (`missiles_reserve_operation_resources`): `set_temp_variable = { missiles_reserve_after_operation = missiles_operational_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2193` (`missiles_reserve_operation_resources`): `subtract_from_temp_variable = { var = missiles_reserve_after_operation value = missiles_operation_missile_cost }`
- `common\scripted_effects\032_missiles_operations_effects.txt:2208` (`missiles_reserve_operation_resources`): `check_variable = { var = missiles_reserve_after_operation value = missiles_ai_reserve_floor compare = greater_than_or_equals }`

## missiles_scenario_package_control

- `common\scripted_effects\032_missiles_operations_effects.txt:676` (`missiles_initialize_scenario_package`): `if = { limit = { has_variable = missiles_scenario_package_control } set_variable = { missiles_command_control = missiles_scenario_package_control } }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:611` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_control = global.missiles_scenario_control_target }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:649` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_control`
- `common\scripted_effects\032_missiles_scenario_effects.txt:670` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_control`

## missiles_scenario_package_incident_cap

- `common\scripted_effects\032_missiles_scenario_effects.txt:612` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_incident_cap = global.missiles_scenario_incident_cap }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:650` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_incident_cap`
- `common\scripted_effects\032_missiles_scenario_effects.txt:671` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_incident_cap`

## missiles_scenario_package_intensity

- `common\scripted_effects\032_missiles_scenario_effects.txt:605` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_intensity = global.missiles_scenario_intensity }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:643` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_intensity`
- `common\scripted_effects\032_missiles_scenario_effects.txt:664` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_intensity`

## missiles_scenario_package_profile

- `common\scripted_effects\032_missiles_scenario_effects.txt:604` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_profile = global.missiles_scenario_profile }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:642` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_profile`
- `common\scripted_effects\032_missiles_scenario_effects.txt:663` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_profile`

## missiles_scenario_package_readiness

- `common\scripted_effects\032_missiles_operations_effects.txt:674` (`missiles_initialize_scenario_package`): `if = { limit = { has_variable = missiles_scenario_package_readiness } set_variable = { missiles_launch_readiness = missiles_scenario_package_readiness } }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:610` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_readiness = global.missiles_scenario_readiness_target }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:648` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_readiness`
- `common\scripted_effects\032_missiles_scenario_effects.txt:669` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_readiness`

## missiles_scenario_package_reserve

- `common\scripted_effects\032_missiles_operations_effects.txt:657` (`missiles_initialize_scenario_package`): `limit = { check_variable = { var = missiles_scenario_package_reserve value = constant:missiles_program_value.zero compare = greater_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:658` (`missiles_initialize_scenario_package`): `set_variable = { missiles_operational_reserve = missiles_scenario_package_reserve }`
- `common\scripted_effects\032_missiles_operations_effects.txt:665` (`missiles_initialize_scenario_package`): `has_variable = missiles_scenario_package_reserve`
- `common\scripted_effects\032_missiles_operations_effects.txt:666` (`missiles_initialize_scenario_package`): `check_variable = { var = missiles_reserve_cap value = missiles_scenario_package_reserve compare = less_than }`
- `common\scripted_effects\032_missiles_operations_effects.txt:668` (`missiles_initialize_scenario_package`): `set_variable = { missiles_reserve_cap = missiles_scenario_package_reserve }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:608` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_reserve = global.missiles_scenario_reserve_target }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:646` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_reserve`
- `common\scripted_effects\032_missiles_scenario_effects.txt:667` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_reserve`

## missiles_scenario_package_share

- `common\scripted_effects\032_missiles_scenario_effects.txt:606` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_share = global.missiles_scenario_recipient_share }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:644` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_share`
- `common\scripted_effects\032_missiles_scenario_effects.txt:665` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_share`

## missiles_scenario_package_site_capacity

- `common\scripted_effects\032_missiles_operations_effects.txt:685` (`missiles_initialize_scenario_package`): `limit = { has_variable = missiles_scenario_package_site_capacity }`
- `common\scripted_effects\032_missiles_operations_effects.txt:695` (`missiles_initialize_scenario_package`): `limit = { check_variable = { var = missiles_site_level value = PREV.missiles_scenario_package_site_capacity compare = less_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:696` (`missiles_initialize_scenario_package`): `set_variable = { missiles_site_level = PREV.missiles_scenario_package_site_capacity }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:609` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_site_capacity = global.missiles_scenario_site_capacity_target }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:647` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_site_capacity`
- `common\scripted_effects\032_missiles_scenario_effects.txt:668` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_site_capacity`

## missiles_scenario_package_stage

- `common\scripted_effects\032_missiles_operations_effects.txt:634` (`missiles_initialize_scenario_package`): `has_variable = missiles_scenario_package_stage`
- `common\scripted_effects\032_missiles_operations_effects.txt:635` (`missiles_initialize_scenario_package`): `check_variable = { var = missiles_program_stage value = missiles_scenario_package_stage compare = less_than }`
- `common\scripted_effects\032_missiles_operations_effects.txt:637` (`missiles_initialize_scenario_package`): `set_variable = { missiles_program_stage = missiles_scenario_package_stage }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:607` (`missiles_scenario_apply_country_package`): `set_variable = { missiles_scenario_package_stage = global.missiles_scenario_target_stage }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:645` (`missiles_scenario_apply_country_package`): `clear_variable = missiles_scenario_package_stage`
- `common\scripted_effects\032_missiles_scenario_effects.txt:666` (`missiles_scenario_finish_transaction`): `clear_variable = missiles_scenario_package_stage`

## missiles_scenario_requested_count

- `common\scripted_effects\032_missiles_scenario_effects.txt:321` (`missiles_scenario_calculate_selection`): `set_temp_variable = { missiles_scenario_requested_count = global.missiles_scenario_profile_recipients^num }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:322` (`missiles_scenario_calculate_selection`): `multiply_temp_variable = { var = missiles_scenario_requested_count value = global.missiles_scenario_recipient_share }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:323` (`missiles_scenario_calculate_selection`): `round_temp_variable = missiles_scenario_requested_count`
- `common\scripted_effects\032_missiles_scenario_effects.txt:325` (`missiles_scenario_calculate_selection`): `limit = { check_variable = { var = missiles_scenario_requested_count value = constant:missiles_scenario_scale.one compare = less_than } }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:326` (`missiles_scenario_calculate_selection`): `set_temp_variable = { missiles_scenario_requested_count = constant:missiles_scenario_scale.one }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:347` (`missiles_scenario_calculate_selection`): `limit = { check_variable = { var = missiles_scenario_requested_count value = global.missiles_scenario_priority_required compare = less_than } }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:348` (`missiles_scenario_calculate_selection`): `set_temp_variable = { missiles_scenario_requested_count = global.missiles_scenario_priority_required }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:351` (`missiles_scenario_calculate_selection`): `limit = { check_variable = { var = missiles_scenario_requested_count value = global.missiles_scenario_profile_recipients^num compare = greater_than } }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:352` (`missiles_scenario_calculate_selection`): `set_temp_variable = { missiles_scenario_requested_count = global.missiles_scenario_profile_recipients^num }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:354` (`missiles_scenario_calculate_selection`): `set_variable = { global.missiles_scenario_requested_count = missiles_scenario_requested_count }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:363` (`missiles_scenario_select_countries`): `check_variable = { var = global.missiles_scenario_selected_recipients^num value = global.missiles_scenario_requested_count compare = less_than }`
- `common\scripted_effects\032_missiles_scenario_effects.txt:374` (`missiles_scenario_select_countries`): `check_variable = { var = global.missiles_scenario_selected_recipients^num value = global.missiles_scenario_requested_count compare = less_than }`

## missiles_warning_schedule_days

- `common\scripted_effects\032_missiles_operations_effects.txt:4140` (`missiles_schedule_warning_response`): `set_temp_variable = { missiles_warning_schedule_days = missiles_warning_response_date }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4143` (`missiles_schedule_warning_response`): `set_temp_variable = { missiles_warning_schedule_days = missiles_warning_expiry_date }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4145` (`missiles_schedule_warning_response`): `subtract_from_temp_variable = { var = missiles_warning_schedule_days value = global.date }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4147` (`missiles_schedule_warning_response`): `limit = { check_variable = { var = missiles_warning_schedule_days value = constant:missiles_program_value.one compare = less_than } }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4148` (`missiles_schedule_warning_response`): `set_temp_variable = { missiles_warning_schedule_days = constant:missiles_program_value.one }`
- `common\scripted_effects\032_missiles_operations_effects.txt:4151` (`missiles_schedule_warning_response`): `country_event = { id = chaosx.nr32.82 days = missiles_warning_schedule_days }`

## Direct callers of lifecycle owners

- `common\on_actions\032_missiles_on_actions.txt:166`: `FROM.FROM = { missiles_handle_site_control_changed = yes }`
- `common\on_actions\032_missiles_on_actions.txt:187`: `if = { limit = { has_country_flag = missiles_program_initialized } missiles_cleanup_removed_country = yes }`
- `common\scripted_effects\032_missiles_effects.txt:287`: `missiles_evaluate_evolution_unlocks = yes`
- `common\scripted_effects\032_missiles_effects.txt:324`: `missiles_initialize_scenario_package = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:472`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:490`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:508`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:526`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:544`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:567`: `missiles_schedule_evolution_track = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:578`: `missiles_schedule_evolution_track = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:590`: `missiles_schedule_evolution_track = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:601`: `missiles_schedule_evolution_track = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:612`: `missiles_schedule_evolution_track = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:2234`: `missiles_calculate_operation_reach = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:2248`: `missiles_reserve_operation_resources = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:2483`: `missiles_calculate_operation_guidance = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:2794`: `missiles_register_conventional_deaths = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:4164`: `missiles_schedule_warning_response = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:4188`: `missiles_schedule_warning_response = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:4468`: `missiles_record_operation_achievement_receipts = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:4739`: `missiles_finalize_planned_inheritance = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:4802`: `missiles_transfer_captured_reserve = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:4931`: `missiles_handle_site_control_changed = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:5217`: `missiles_finalize_civil_war_split_child = yes`
- `common\scripted_effects\032_missiles_operations_effects.txt:5222`: `missiles_finalize_planned_inheritance = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:99`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:115`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:125`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:141`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:151`: `missiles_record_evolution_unlock = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:724`: `missiles_scenario_calculate_selection = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:725`: `missiles_scenario_select_countries = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:736`: `missiles_scenario_prepare_profile_globals = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:739`: `missiles_scenario_apply_country_package = yes`
- `common\scripted_effects\032_missiles_scenario_effects.txt:779`: `missiles_scenario_finish_transaction = yes`
- `events\032_missile_crisis.txt:316`: `immediate = { missiles_schedule_warning_response = yes }`
