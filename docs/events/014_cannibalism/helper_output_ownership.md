# Event 014 caller-owned helper outputs

Disposition: `implemented` (round 2, agent decision R2-3 in `docs/plans/014_cannibalism_plans/agent_decisions_2026-10-04.md`).

A temporary variable or temporary array first created inside a scripted effect or trigger may be gone when that helper returns, while storage that already existed before the call keeps the helper's changes (`paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types; `chaos-redux-events` skill, Helper output lifetime).
Every Event 014 caller that reads a helper's output after the call therefore sets that output to the helper's own default before the call, including calls inside `if` limits and scripted-localisation `text.trigger` blocks.
Temporary arrays are owned with `clear_temp_array` in the caller.
Inputs and cursors such as `cannibalism_spread_queue_index` are never reset by this storage, and a value that a helper accumulates or adjusts is owned once by the outer frame instead of before every call.

The inheritance, migration, consumption-parameter and Wendigo anchor outputs keep the contract in `inheritance_storage_contract.md`.
This table lists every other helper whose output is read after it returns.
Each helper definition carries a matching `Caller-owned outputs` comment.

## Output table

| Helper | Caller-owned outputs and defaults |
| --- | --- |
| `cannibalism_activate_current_country_from_external_spread` | `cannibalism_external_activation_result` = `0` |
| `cannibalism_allocate_slot_cba` to `cannibalism_allocate_slot_cbh` | `cannibalism_warlord_creation_result` = `0` |
| `cannibalism_apply_loaded_spread_to_current_country` | `cannibalism_spread_country_arrival_result` = `0` |
| `cannibalism_begin_current_state_recovery` | `cannibalism_recovery_start_allowed` = `0` |
| `cannibalism_calculate_current_counterwar_anchor_score` | `cannibalism_wendigo_counterwar_anchor_score` = `constant:cannibalism_wendigo_decision.selection_base_score` |
| `cannibalism_calculate_current_unification_host_score` | `cannibalism_current_unification_host_score` = `constant:cannibalism_unification.base_host_score` |
| `cannibalism_calculate_current_wendigo_anchor_score` | `cannibalism_current_wendigo_anchor_score` = `constant:cannibalism_wendigo_anchor.base_score` |
| `cannibalism_calculate_current_wendigo_merge_host_score` | `cannibalism_current_wendigo_merge_host_score` = `constant:cannibalism_wendigo_merge.base_host_score` |
| `cannibalism_calculate_wendigo_countdown_progress_change` | `cannibalism_wendigo_countdown_progress_change` = `constant:cannibalism_wendigo_countdown.weekly_base` |
| `cannibalism_capture_current_integration_history_identity` | `cannibalism_integration_donor_generation` = `0`<br>`cannibalism_integration_origin_state` = `0` |
| `cannibalism_check_spread_target_state_availability` | `cannibalism_spread_target_available` = `0`<br>`cannibalism_spread_queue_validation_result` = `0` |
| `cannibalism_clear_loaded_spread_pending_state` | `cannibalism_spread_pending_clear_result` = `0` |
| `cannibalism_clear_prefire_context` | `cannibalism_prefire_evolution` = `0`<br>`cannibalism_prefire_evolution_i_enabled` = `0`<br>`cannibalism_prefire_evolution_ii_enabled` = `0`<br>`cannibalism_prefire_evolution_iii_pending` = `0`<br>`cannibalism_prefire_ready` = `0` |
| `cannibalism_enqueue_spread_entry` | `cannibalism_spread_enqueue_result` = `0` |
| `cannibalism_find_expected_spread_row_for_screening` | `cannibalism_expected_spread_row_found` = `0`<br>`cannibalism_spread_queue_validation_result` = `0` |
| `cannibalism_find_replacement_pulse_anchor` | `cannibalism_replacement_anchor_found` = `0` |
| `cannibalism_get_unified_scored_targets` | `cannibalism_scored_target_countries` = empty array<br>`cannibalism_scored_target_values` = empty array |
| `cannibalism_get_wendigo_scored_targets` | `cannibalism_scored_target_countries` = empty array<br>`cannibalism_scored_target_values` = empty array |
| `cannibalism_handle_state_control_recovery` | `cannibalism_control_change_node_source_generation` = `0`<br>`cannibalism_control_change_recovery_context_valid` = `0` |
| `cannibalism_initialize_current_country` | `cannibalism_actor_register_result` = `0` |
| `cannibalism_invalidate_spread_entries_for_current_state_lifecycle` | `cannibalism_spread_route` = `0` |
| `cannibalism_load_hoard_review_target` | `cannibalism_hoard_target_is_governor` = `constant:cannibalism_hoard.zero`<br>`cannibalism_hoard_target_valid` = `constant:cannibalism_hoard.zero` |
| `cannibalism_load_hoard_seizure_target` | `cannibalism_hoard_target_is_governor` = `constant:cannibalism_hoard.zero`<br>`cannibalism_hoard_target_valid` = `constant:cannibalism_hoard.zero` |
| `cannibalism_load_hoard_target_owner` | `cannibalism_hoard_target_is_governor` = `constant:cannibalism_hoard.zero` |
| `cannibalism_load_spread_entry_context` | `cannibalism_expected_spread_id` = `0`<br>`cannibalism_spread_route` = `0`<br>`cannibalism_spread_source_generation` = `0`<br>`cannibalism_spread_source_country_context_loaded` = `0`<br>`cannibalism_spread_source_state_context_loaded` = `0`<br>`cannibalism_spread_target_country_context_loaded` = `0`<br>`cannibalism_spread_target_state_context_loaded` = `0`<br>`cannibalism_spread_parameters_valid` = `0`<br>`cannibalism_spread_delay_days` = `0`<br>`cannibalism_spread_node_strength` = `0`<br>`cannibalism_spread_node_type` = `constant:cannibalism_node_type.formation`<br>`cannibalism_spread_node_stage` = `constant:cannibalism_state_stage.compromised_garrison` |
| `cannibalism_prepare_consumption_context` | `cannibalism_consumption_result` = `constant:cannibalism_consumption_result.invalid_scope`<br>`cannibalism_population_loss_applied` = `0` |
| `cannibalism_prepare_current_warlord_concealment_share` | `cannibalism_transfer_concealment_share` = `constant:cannibalism_hoard.zero` |
| `cannibalism_prepare_current_warlord_origin_specialist_template` | `cannibalism_warlord_origin_template` = `constant:cannibalism_recruitment_template.scavenger_warband` |
| `cannibalism_prepare_larder_transfer_quote` | `cannibalism_transfer_hoard_amount` = `constant:cannibalism_larder_logistics.zero` |
| `cannibalism_prepare_warlord_creation_context` | `cannibalism_selected_warlord_origin` = `constant:cannibalism_origin.none`<br>`cannibalism_selected_warlord_region` = `constant:cannibalism_region.unknown`<br>`cannibalism_warlord_starting_experience` = `constant:cannibalism_warlord_start.weak_experience`<br>`cannibalism_warlord_starting_frenzy` = `constant:cannibalism_warlord_start.weak_frenzy`<br>`cannibalism_warlord_starting_units` = `constant:cannibalism_warlord_start.weak_units` |
| `cannibalism_prepare_warlord_origin_operation_contract` | `cannibalism_origin_operation_convoy_recovery` = `0`<br>`cannibalism_origin_operation_duration_bonus` = `0`<br>`cannibalism_origin_operation_infantry_recovery` = `0`<br>`cannibalism_origin_operation_larder_recovery` = `0`<br>`cannibalism_origin_operation_support_recovery` = `0`<br>`cannibalism_origin_operation_train_recovery` = `0`<br>`cannibalism_origin_operation_truck_recovery` = `0` |
| `cannibalism_prepare_warlord_recruitment_contract` | `cannibalism_warlord_recruitment_cooldown_days` = `constant:cannibalism_warlord_decision.recruitment_state_cooldown_days`<br>`cannibalism_warlord_unit_start_equipment` = `constant:cannibalism_warlord_decision.unit_start_equipment`<br>`cannibalism_warlord_unit_start_experience` = `constant:cannibalism_warlord_decision.unit_start_experience`<br>`cannibalism_warlord_unit_start_manpower` = `constant:cannibalism_warlord_decision.unit_start_manpower` |
| `cannibalism_refresh_prefire_evolution_state` | `cannibalism_prefire_evolution` = `0`<br>`cannibalism_prefire_evolution_i_enabled` = `0`<br>`cannibalism_prefire_evolution_ii_enabled` = `0`<br>`cannibalism_prefire_evolution_iii_pending` = `0` |
| `cannibalism_register_current_country_actor` | `cannibalism_actor_register_result` = `0` |
| `cannibalism_register_current_wendigo_anchor` | `cannibalism_wendigo_anchor_registration_result` = `0` |
| `cannibalism_register_cxt_test_content` | `chaosx_test_country_extension_registration_added` = `0` |
| `cannibalism_resolve_loaded_spread_arrival` | `cannibalism_spread_arrival_applied` = `0` |
| `cannibalism_retire_current_pulse_callback` | `cannibalism_pulse_callback_retire_result` = `0`<br>`cannibalism_rehome_pulse_days` = `0`<br>`cannibalism_rehome_pulse_immediate` = `0` |
| `cannibalism_retire_current_state_node` | `cannibalism_node_retire_result` = `0` |
| `cannibalism_scenario_build_manual_preflight_plan` | `cannibalism_scenario_preflight_result` = `0`<br>`cannibalism_scenario_use_preflight_plan` = `0`<br>`cannibalism_scenario_planned_actor_countries` = empty array<br>`cannibalism_scenario_planned_island_states` = empty array<br>`cannibalism_scenario_planned_siege_states` = empty array<br>`cannibalism_scenario_planned_march_states` = empty array<br>`cannibalism_scenario_planned_warlord_slots` = empty array |
| `cannibalism_scenario_initialize_current_country` | `cannibalism_scenario_actor_initialization_result` = `0`<br>`cannibalism_scenario_actor_was_new` = `0` |
| `cannibalism_scenario_initialize_required_actors` | `cannibalism_scenario_actor_setup_result` = `0`<br>`cannibalism_scenario_nodes_created` = `0` |
| `cannibalism_scenario_plan_available_warlord_slots` | `cannibalism_scenario_planned_warlord_slot_count` = `0` |
| `cannibalism_scenario_prepare_preflight_requirements` | `cannibalism_scenario_required_island_states` = `0`<br>`cannibalism_scenario_required_island_warlord_states` = `0`<br>`cannibalism_scenario_required_march_states` = `0`<br>`cannibalism_scenario_required_siege_states` = `0`<br>`cannibalism_scenario_required_warlord_slots` = `0` |
| `cannibalism_scenario_prepare_scale` | `cannibalism_prefire_evolution` = `0`<br>`cannibalism_prefire_evolution_i_enabled` = `0`<br>`cannibalism_prefire_evolution_ii_enabled` = `0`<br>`cannibalism_scenario_cell_strength` = `constant:cannibalism_scenario_scale.low_cell_strength`<br>`cannibalism_scenario_command_integrity` = `constant:cannibalism_scenario_scale.low_command_integrity`<br>`cannibalism_scenario_cult_cohesion` = `constant:cannibalism_scenario_scale.low_cult_cohesion`<br>`cannibalism_scenario_field_hunger` = `constant:cannibalism_scenario_scale.low_field_hunger`<br>`cannibalism_scenario_mark_external_route` = `0`<br>`cannibalism_scenario_network_alignment` = `constant:cannibalism_scenario_scale.low_network`<br>`cannibalism_scenario_node_stage` = `constant:cannibalism_state_stage.compromised_garrison`<br>`cannibalism_scenario_selected_intensity` = `0`<br>`cannibalism_scenario_selected_type` = `0`<br>`cannibalism_scenario_target_countries` = `constant:cannibalism_scenario_scale.low_countries`<br>`cannibalism_scenario_target_silent_hosts` = `constant:cannibalism_scenario_scale.low_silent_hosts`<br>`cannibalism_scenario_target_states` = `constant:cannibalism_scenario_scale.low_states`<br>`cannibalism_scenario_target_warlords` = `constant:cannibalism_scenario_scale.low_warlords`<br>`cannibalism_prefire_evolution_iii_pending` = `0` |
| `cannibalism_scenario_seed_current_state` | `cannibalism_scenario_node_setup_result` = `0` |
| `cannibalism_scenario_select_island_state` | `cannibalism_scenario_state_found` = `0` |
| `cannibalism_scenario_select_march_state` | `cannibalism_scenario_state_found` = `0` |
| `cannibalism_scenario_select_siege_state` | `cannibalism_scenario_state_found` = `0` |
| `cannibalism_scenario_select_source_country` | `cannibalism_scenario_source_found` = `0` |
| `cannibalism_score_current_host` | `cannibalism_host_score` = `constant:cannibalism_host_weight.base` |
| `cannibalism_score_current_state` | `cannibalism_state_score` = `constant:cannibalism_state_weight.base` |
| `cannibalism_select_counterwar_anchor` | `cannibalism_wendigo_counterwar_anchor_found` = `0` |
| `cannibalism_select_highest_risk_state` | `cannibalism_state_selected` = `0` |
| `cannibalism_select_warlord_candidate_state` | `cannibalism_warlord_candidate_found` = `0` |
| `cannibalism_set_automatic_spread_route_from_source_state` | `cannibalism_spread_route` = `constant:cannibalism_spread_route.retreat` |
| `cannibalism_set_spread_parameters_from_route` | `cannibalism_spread_parameters_valid` = `0`<br>`cannibalism_spread_delay_days` = `0`<br>`cannibalism_spread_node_strength` = `0`<br>`cannibalism_spread_node_type` = `constant:cannibalism_node_type.formation`<br>`cannibalism_spread_node_stage` = `constant:cannibalism_state_stage.compromised_garrison` |
| `cannibalism_setup_current_warlord_country` | `cannibalism_warlord_setup_result` = `0` |
| `cannibalism_ui_load_continental_target_row` | `cannibalism_ui_target_country` = `0`<br>`cannibalism_ui_target_kind` = `0`<br>`cannibalism_ui_target_date` = `0`<br>`cannibalism_ui_target_generation` = `0` |
| `cannibalism_ui_load_integrated_history_row` | `cannibalism_ui_history_name` = `0`<br>`cannibalism_ui_history_origin` = `0`<br>`cannibalism_ui_history_origin_state` = `0`<br>`cannibalism_ui_history_disposition` = `0`<br>`cannibalism_ui_history_date` = `0` |
| `cannibalism_unified_execute_state_consumption` | `cannibalism_unified_consumption_result` = `0` |
| `cannibalism_validate_spread_queue` | `cannibalism_spread_queue_validation_result` = `0` |

## Values owned once by the outer frame

- `cannibalism_scenario_nodes_created` counts every node the scenario seeds; `cannibalism_scenario_initialize_required_actors` and the scenario setup that calls it own it, and `cannibalism_scenario_seed_current_state` only adds to it.
- `cannibalism_warlord_starting_units` comes from `cannibalism_prepare_warlord_creation_context`, which its caller owns, and `cannibalism_scenario_allocate_next_planned_warlord_slot` only adjusts it.
- The preflight scale values, planned arrays, `cannibalism_scenario_setup_failed` and `cannibalism_scenario_setup_result` are owned by the two scenario entries, `trigger_cannibalism_scenario` and `cannibalism_setup_prefire_evolution_iii_opening`; the setup helpers read and fill them.
- The prefire values are owned by `cannibalism_prepare_random_event_fire` and `cannibalism_begin_from_prefire_context`.

## Spread request context

`cannibalism_validate_spread_queue` audits every stored row by loading it into the shared spread route, route parameters and the four `cannibalism_spread_*` scope targets, so after it returns they describe the last stored row.
`cannibalism_check_spread_target_state_availability` keeps the request's route and four scopes in `cannibalism_spread_request_*` across the audit and restores them before it checks the target state.
A request without all four scopes is never reported available.
`cannibalism_enqueue_spread_entry` computes the route parameters only after that check, so a new route is queued with its own delay and strength while other routes are already in flight.
`cannibalism_process_spread_queue` owns the loaded row context it resolves; the row index stays its own loop cursor.
