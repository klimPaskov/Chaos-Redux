# Event 014 unified focus remediation handoff - 2026-07-12

## Scope and outcome

This tranche replaces the unified tree's generic capacity-only facade with live command, Larder, army, navy, air, cell, expansion, counterwar, and hostility consumers. All 208 focus-created domain flags have a concrete downstream cost, gate, duration, modifier, receipt, target rule, mission value, or terminal proof consumer. The eight non-domain final/package flags remain consumed by the existing terminal triggers and focus effects.

World Hostility is a three-tier persistent pressure system at 25/50/75. It adds paid-operation surcharges, applies national penalties, and gives operation targets temporary counterpressure. It refreshes on focus completion and paid outcomes; no daily, weekly, or monthly world scan was added. Counterwar operations and conversion reduce or convert Hostility.

The exact terminal proof remains:

- Larder: 5 successful paid Larder operations.
- Army: 5 Cannibal Legions, 1 Bone Guard, and 5 paid army operations.
- Expansion: 5 prepared campaigns, 3 postwar integrations, and 5 paid cell operations.
- Counterwar: 5 paid counterwar operations.
- Final focuses: strict global Chaos greater than 1000 remains required.

Post-reveal focus cadence is documented as 21/35/56 days for short/normal/terminal focuses, with the operational gates serving as hard pressure.

## Changed files

- `common/scripted_effects/014_cannibalism_unified_decision_effects.txt`
- `common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt`
- `common/decisions/014_cannibalism_unified_decisions.txt`
- `common/dynamic_modifiers/014_cannibalism_unified_decision_modifiers.txt`
- `common/script_constants/014_cannibalism_unified_decision_constants.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/events/014_cannibalism.md`
- this handoff

## Key mechanics

- `cannibalism_unified_record_distinct_enemy_capitulation` deduplicates `event_target:cannibalism_defeated_country` in `cannibalism_unified_defeated_enemy_entries`, counts distinct enemy-country capitulations, and issues bounded battlefield receipts. Root integrated this helper into the existing bounded enemy loop in `on_capitulation`.
- Battlefield processing spends capitulation receipts; rout processing spends receipts earned by paid Continental Hunts; convoy processing spends receipts earned by paid Continental Naval Hunts. Each receipt family has a cap and a cooldown/target lock.
- Four independently selectable origin decisions recruit Island Reavers, Siege Eaters, March Predation Columns, and Lockhouse Columns. Wrapper effects are `cannibalism_unified_execute_island_specialist_recruitment`, `cannibalism_unified_execute_siege_specialist_recruitment`, `cannibalism_unified_execute_march_specialist_recruitment`, and `cannibalism_unified_execute_prison_specialist_recruitment`. Each uses an independent knowledge flag, raised counter, and cap.
- Every recruited formation still uses the exact Deaths-backed transaction and is created at zero starting manpower and zero starting equipment. No equipment or units are granted for free.
- Inherited route-history consumers are explicit: personal tyranny changes command authority and purge cost; feast council changes alignment and governor support; pack confederacy changes network yield and command duration; rapid/managed/mobile history changes the matching Larder costs/results; alignment/manipulation/defiance history changes the matching cell, campaign, and counterwar results.
- New paid decisions cover captured workshops, exhausted-frontier abandonment, rout collapse, silent anchorages, convoy receipts, terror ultimata, border incidents, counterwar conversion, Legion surges, and each learned origin formation.

## Integration dependencies

- Root has already wired `cannibalism_unified_record_distinct_enemy_capitulation = yes` after saving the defeated-country event target.
- Root owns later-warlord absorption and must accumulate every newly absorbed origin/route knowledge flag. The four decision gates will expose each accumulated origin independently.
- This tranche does not edit focus definitions, warlord files, on-actions, unification effects, assets, or spreadsheets.
- Existing registered Event 014 icons are reused. No new DDS or `.gfx` registration is required.

## Localisation keys touched

The shared localisation edit is confined to the following exact surfaces:

- Focus tooltips: `CBL_preserve_the_origin_commands_tt`, `CBL_map_the_origin_templates_tt`, `CBL_abolish_the_old_supply_ceiling_tt`, `CBL_the_army_that_does_not_end_tt`, `CBL_host_theaters_without_borders_tt`, `CBL_consume_the_counterwar_tt`.
- Existing dynamic-cost/mission keys: `cannibalism_unified_command_category_desc`; `cannibalism_unified_absorb_warlord_requirements_tt`, `cannibalism_unified_absorb_warlord_cost_text`; `cannibalism_unified_appoint_governor_requirements_tt`, `cannibalism_unified_appoint_governor_cost_text`; `cannibalism_unified_purge_rival_requirements_tt`, `cannibalism_unified_purge_rival_cost_text`; `cannibalism_unified_command_operation_requirements_tt`, `cannibalism_unified_command_operation_cost_text`; all five `cannibalism_unified_command_mission_*` outcome/description keys; `cannibalism_unified_storage_requirements_tt`, `cannibalism_unified_storage_cost_text`; `cannibalism_unified_feeding_capital_requirements_tt`, `cannibalism_unified_feeding_capital_cost_text`; the requirements/cost keys for rapid, managed, mobile, and battlefield consumption plus `cannibalism_unified_battlefield_consumption_effect_tt`; all five Larder mission description/outcome keys; air-foundation requirements/cost; Legion requirements/cost/effect; Bone Guard requirements/cost; army, naval, and air operation requirements/cost/effect; all five War Machine mission description/outcome keys; cell, campaign, postwar-integration, and counterwar requirements/cost/effect keys; all five Counterwar mission description/outcome keys.
- New decision keys: every name/description/requirements/cost/effect key under `cannibalism_unified_convert_captured_workshop`, `cannibalism_unified_abandon_exhausted_frontier`, `cannibalism_unified_surge_cannibal_legion`, `cannibalism_unified_recruit_island_reavers`, `cannibalism_unified_recruit_siege_eaters`, `cannibalism_unified_recruit_march_predation_column`, `cannibalism_unified_recruit_lockhouse_column`, `cannibalism_unified_collapse_enemy_front`, `cannibalism_unified_process_convoy_harvest`, `cannibalism_unified_build_silent_anchorage`, `cannibalism_unified_issue_terror_ultimatum`, `cannibalism_unified_provoke_border_incident`, and `cannibalism_unified_convert_counterwar_pressure`.
- New modifier keys: name/description pairs for `cannibalism_unified_enemy_front_disruption`, `cannibalism_unified_managed_district`, `cannibalism_unified_battlefield_processing`, `cannibalism_unified_captured_workshop`, `cannibalism_unified_silent_anchorage`, `cannibalism_unified_frontier_abandoned`, all three `cannibalism_unified_world_hostility_*` tiers, and all three `cannibalism_unified_enemy_counterpressure_*` tiers.

No warlord/captured-warlord localisation key was edited.

## Exact focus-flag consumer table

The consumer names below are the live profile variables altered by each focus flag. Those variables are then read by scripted triggers, paid effects, dynamic modifiers, mission logic, localisation, or terminal proof.

| Focus-created flag | Concrete profile consumer(s) |
|---|---|
| `cannibalism_unified_air_front_collapse_package_pending` | `cannibalism_unified_war_machine_mission_days` |
| `cannibalism_unified_air_interdiction_targets_open` | `cannibalism_unified_air_superiority` |
| `cannibalism_unified_air_network_capstone` | `cannibalism_unified_air_superiority` |
| `cannibalism_unified_air_recovery_signals_open` | `cannibalism_unified_air_airframe_cost` |
| `cannibalism_unified_air_target_marking_open` | `cannibalism_unified_air_mission_efficiency` |
| `cannibalism_unified_airborne_cell_insertion_open` | `cannibalism_unified_air_transport_cost` |
| `cannibalism_unified_airframe_repair_projects_open` | `cannibalism_unified_air_airframe_cost` |
| `cannibalism_unified_airframe_stockpile_costs_required` | `cannibalism_unified_air_support_cost` |
| `cannibalism_unified_amphibious_column_decisions_open` | `cannibalism_unified_naval_fuel_cost` |
| `cannibalism_unified_anchorage_discovery_risk` | `cannibalism_unified_naval_hostility_gain` |
| `cannibalism_unified_archipelago_command_missions_open` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_battlefield_harvest_caps_required` | `cannibalism_unified_battlefield_receipt_cap` |
| `cannibalism_unified_battlefield_larder_capstone` | `cannibalism_unified_battlefield_receipt_cap`, `cannibalism_unified_larder_mission_success_authority` |
| `cannibalism_unified_battlefield_processing_projects_open` | `cannibalism_unified_battlefield_resistance`, `cannibalism_unified_battlefield_support_cost` |
| `cannibalism_unified_battlefield_yield_decisions_open` | `cannibalism_unified_battlefield_support_cost` |
| `cannibalism_unified_bone_guard_breach_package_pending` | `cannibalism_unified_army_breakthrough` |
| `cannibalism_unified_bone_guard_cap_active` | `cannibalism_unified_bone_guard_cap` |
| `cannibalism_unified_bone_guard_cap_upgraded` | `cannibalism_unified_bone_guard_cap` |
| `cannibalism_unified_bone_guard_recruitment_open` | `cannibalism_unified_bone_guard_larder_cost` |
| `cannibalism_unified_bone_officer_assignments_open` | `cannibalism_unified_purge_authority_gain` |
| `cannibalism_unified_border_incident_decisions_open` | `cannibalism_unified_border_incident_command_cost` |
| `cannibalism_unified_caliber_standardization_projects_open` | `cannibalism_unified_bone_guard_artillery_reserve` |
| `cannibalism_unified_campaign_category_open` | `cannibalism_unified_campaign_operation_duration` |
| `cannibalism_unified_cannibal_legion_recruitment_open` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_capital_assault_missions_open` | `cannibalism_unified_army_attack` |
| `cannibalism_unified_capital_projects_open` | `cannibalism_unified_command_operation_duration` |
| `cannibalism_unified_captain_arbitration_open` | `cannibalism_unified_command_alignment_gain` |
| `cannibalism_unified_captured_equipment_conversion_open` | `cannibalism_unified_air_foundation_support_cost` |
| `cannibalism_unified_captured_hospital_conversion_open` | `cannibalism_unified_battlefield_local_supply` |
| `cannibalism_unified_captured_hull_conversion_open` | `cannibalism_unified_naval_convoy_cost` |
| `cannibalism_unified_captured_industry_projects_open` | `cannibalism_unified_workshop_local_supply` |
| `cannibalism_unified_cell_category_open` | `cannibalism_unified_cell_operation_duration` |
| `cannibalism_unified_central_accounting_open` | `cannibalism_unified_larder_mission_success_authority` |
| `cannibalism_unified_central_command_decisions_open` | `cannibalism_unified_command_planning` |
| `cannibalism_unified_central_quota_decisions_open` | `cannibalism_unified_command_larder_cost` |
| `cannibalism_unified_chained_dominion_open` | `cannibalism_unified_command_authority_gain`, `cannibalism_unified_command_network_gain` |
| `cannibalism_unified_coalition_command_operations_open` | `cannibalism_unified_counterwar_command_cost` |
| `cannibalism_unified_coalition_officer_targets_open` | `cannibalism_unified_counterwar_enemy_organization` |
| `cannibalism_unified_command_category_open` | `cannibalism_unified_command_org_regain` |
| `cannibalism_unified_command_dissolution_open` | `cannibalism_unified_purge_target_organization` |
| `cannibalism_unified_confederation_capstone` | `cannibalism_unified_command_alignment_gain`, `cannibalism_unified_command_org_regain` |
| `cannibalism_unified_consumption_stage_decisions_open` | `cannibalism_unified_storage_duration` |
| `cannibalism_unified_continental_supply_regions_open` | `cannibalism_unified_storage_supply` |
| `cannibalism_unified_convoy_harvest_caps_required` | `cannibalism_unified_convoy_harvest_receipt_cap`, `cannibalism_unified_naval_experience_cost` |
| `cannibalism_unified_convoy_hunt_missions_open` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_corridor_target_pool_open` | `cannibalism_unified_counterwar_enemy_defence` |
| `cannibalism_unified_corruption_exposure_missions_open` | `cannibalism_unified_cell_hostility_gain` |
| `cannibalism_unified_counterwar_capstone` | `cannibalism_unified_counterwar_relief` |
| `cannibalism_unified_counterwar_category_open` | `cannibalism_unified_counterwar_operation_duration` |
| `cannibalism_unified_counterwar_conversion_open` | `cannibalism_unified_counterwar_conversion_command_cost` |
| `cannibalism_unified_cured_country_reactivation_missions_open` | `cannibalism_unified_cell_network_gain` |
| `cannibalism_unified_direct_authority_open` | `cannibalism_unified_command_authority_gain` |
| `cannibalism_unified_disconnected_region_management_open` | `cannibalism_unified_governor_resistance` |
| `cannibalism_unified_disposition_break` | `cannibalism_unified_command_authority_gain`, `cannibalism_unified_command_hostility_gain` |
| `cannibalism_unified_disposition_chain` | `cannibalism_unified_command_network_gain` |
| `cannibalism_unified_disposition_keep` | `cannibalism_unified_command_alignment_gain` |
| `cannibalism_unified_disposition_routes_open` | `cannibalism_unified_command_mission_days` |
| `cannibalism_unified_distant_governor_management_open` | `cannibalism_unified_command_operation_duration` |
| `cannibalism_unified_distant_theater_priority_open` | `cannibalism_unified_command_planning` |
| `cannibalism_unified_district_recovery_missions_open` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_dormant_cell_missions_open` | `cannibalism_unified_cell_command_cost` |
| `cannibalism_unified_dynamic_campaign_scoring_open` | `cannibalism_unified_campaign_planning` |
| `cannibalism_unified_enemy_collapse_decisions_open` | `cannibalism_unified_enemy_front_defence` |
| `cannibalism_unified_exhausted_state_abandonment_open` | `cannibalism_unified_frontier_abandon_command_cost` |
| `cannibalism_unified_external_reinfection_open` | `cannibalism_unified_cell_target_stability` |
| `cannibalism_unified_false_surrender_decisions_open` | `cannibalism_unified_cell_target_war_support` |
| `cannibalism_unified_false_surrender_failure_risk` | `cannibalism_unified_cell_hostility_gain` |
| `cannibalism_unified_fear_bombing_escalation_risk` | `cannibalism_unified_air_hostility_gain` |
| `cannibalism_unified_fear_bombing_missions_open` | `cannibalism_unified_air_mission_efficiency` |
| `cannibalism_unified_fear_pressure_tracking_open` | `cannibalism_unified_army_hostility_gain` |
| `cannibalism_unified_feeding_law_decisions_open` | `cannibalism_unified_command_larder_cost` |
| `cannibalism_unified_feeding_rotation_decisions_open` | `cannibalism_unified_managed_local_supply` |
| `cannibalism_unified_foreign_cell_target_pool_open` | `cannibalism_unified_cell_target_lock_days` |
| `cannibalism_unified_front_cascade_missions_open` | `cannibalism_unified_enemy_front_duration` |
| `cannibalism_unified_frontier_exhaustion_missions_open` | `cannibalism_unified_larder_mission_days` |
| `cannibalism_unified_global_campaigns_open` | `cannibalism_unified_campaign_justify` |
| `cannibalism_unified_global_courier_decisions_open` | `cannibalism_unified_cell_larder_cost` |
| `cannibalism_unified_global_mechanic_open` | `cannibalism_unified_command_planning` |
| `cannibalism_unified_global_naval_corridors_open` | `cannibalism_unified_naval_speed` |
| `cannibalism_unified_governor_loyalty_missions_open` | `cannibalism_unified_command_mission_progress` |
| `cannibalism_unified_herd_revolt_missions_open` | `cannibalism_unified_larder_mission_days` |
| `cannibalism_unified_hidden_hoard_investigations_open` | `cannibalism_unified_absorb_larder_cost` |
| `cannibalism_unified_hierarchy_many_jaws` | `cannibalism_unified_command_alignment_gain` |
| `cannibalism_unified_hierarchy_one_command` | `cannibalism_unified_command_authority_gain` |
| `cannibalism_unified_hierarchy_ritual` | `cannibalism_unified_command_network_gain` |
| `cannibalism_unified_hoard_seizure_missions_open` | `cannibalism_unified_purge_larder_cost` |
| `cannibalism_unified_host_charters_open` | `cannibalism_unified_governor_support_cost` |
| `cannibalism_unified_host_conflict_missions_open` | `cannibalism_unified_command_mission_failure_hostility` |
| `cannibalism_unified_hostage_defection_risk` | `cannibalism_unified_command_hostility_gain` |
| `cannibalism_unified_hostage_governance_open` | `cannibalism_unified_governor_authority_gain` |
| `cannibalism_unified_hostage_heir_missions_open` | `cannibalism_unified_command_mission_progress` |
| `cannibalism_unified_hostage_rotation_open` | `cannibalism_unified_governor_support_cost` |
| `cannibalism_unified_hostage_tribute_open` | `cannibalism_unified_command_larder_cost` |
| `cannibalism_unified_hulk_escort_missions_open` | `cannibalism_unified_naval_support_cost` |
| `cannibalism_unified_incident_escalation_missions_open` | `cannibalism_unified_border_incident_support_cost` |
| `cannibalism_unified_internal_front_capstone` | `cannibalism_unified_cell_target_war_support` |
| `cannibalism_unified_island_integration_open` | `cannibalism_unified_anchorage_convoy_cost` |
| `cannibalism_unified_joint_army_operations_open` | `cannibalism_unified_army_fuel_cost` |
| `cannibalism_unified_landing_corridor_missions_open` | `cannibalism_unified_naval_operation_duration` |
| `cannibalism_unified_larder_audit_missions_open` | `cannibalism_unified_larder_mission_days` |
| `cannibalism_unified_larder_category_open` | `cannibalism_unified_command_operation_duration` |
| `cannibalism_unified_larder_column_escort_open` | `cannibalism_unified_mobile_support_cost` |
| `cannibalism_unified_larder_method_battlefield` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_larder_method_managed` | `cannibalism_unified_managed_local_supply` |
| `cannibalism_unified_larder_method_mobile` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_larder_method_rapid` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_larder_method_routes_open` | `cannibalism_unified_larder_mission_days` |
| `cannibalism_unified_larder_route_projects_open` | `cannibalism_unified_storage_duration` |
| `cannibalism_unified_larder_tradeoff_missions_open` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_law_enforcement_missions_open` | `cannibalism_unified_command_mission_progress` |
| `cannibalism_unified_leader_protection_missions_open` | `cannibalism_unified_army_org_regain` |
| `cannibalism_unified_legion_cap_active` | `cannibalism_unified_legion_cap` |
| `cannibalism_unified_legion_cap_upgraded` | `cannibalism_unified_legion_cap` |
| `cannibalism_unified_legion_deaths_accounting_required` | `cannibalism_unified_legion_support_reserve` |
| `cannibalism_unified_legion_reinforcement_open` | `cannibalism_unified_legion_larder_cost` |
| `cannibalism_unified_legion_surge_decisions_open` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_legion_theaters_open` | `cannibalism_unified_army_operation_duration` |
| `cannibalism_unified_lieutenant_governance_open` | `cannibalism_unified_governor_authority_gain` |
| `cannibalism_unified_lieutenant_registry_open` | `cannibalism_unified_absorb_command_cost` |
| `cannibalism_unified_lieutenant_rivalry_missions_open` | `cannibalism_unified_command_mission_failure_hostility` |
| `cannibalism_unified_long_campaign_horizon` | `cannibalism_unified_larder_mission_days`, `cannibalism_unified_storage_duration` |
| `cannibalism_unified_long_harvest_policing_open` | `cannibalism_unified_managed_hostility_gain`, `cannibalism_unified_managed_support_cost` |
| `cannibalism_unified_loyal_officer_training_open` | `cannibalism_unified_command_army_experience_cost` |
| `cannibalism_unified_major_victory_receipts_open` | `cannibalism_unified_battlefield_receipts_per_victory` |
| `cannibalism_unified_managed_herd_decisions_open` | `cannibalism_unified_managed_resistance` |
| `cannibalism_unified_managed_larder_capstone` | `cannibalism_unified_larder_mission_success_authority`, `cannibalism_unified_managed_resistance` |
| `cannibalism_unified_marked_battlefield_missions_open` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_mobile_global_routes_open` | `cannibalism_unified_larder_mission_success_authority`, `cannibalism_unified_mobile_hostility_gain` |
| `cannibalism_unified_mobile_larder_capstone` | `cannibalism_unified_mobile_command_cost`, `cannibalism_unified_mobile_truck_cost` |
| `cannibalism_unified_mutual_predation_votes_open` | `cannibalism_unified_command_alignment_gain` |
| `cannibalism_unified_network_anchor_capitals_open` | `cannibalism_unified_storage_duration` |
| `cannibalism_unified_ocean_crossing_package_pending` | `cannibalism_unified_naval_operation_duration` |
| `cannibalism_unified_oceanic_hulk_routes_open` | `cannibalism_unified_mobile_convoy_cost`, `cannibalism_unified_mobile_fuel_cost` |
| `cannibalism_unified_officer_corruption_decisions_open` | `cannibalism_unified_cell_target_stability` |
| `cannibalism_unified_organized_resistance_risk` | `cannibalism_unified_managed_hostility_gain` |
| `cannibalism_unified_origin_specialist_recruitment_open` | `cannibalism_unified_origin_specialist_larder_cost` |
| `cannibalism_unified_origin_specialists_preserved` | `cannibalism_unified_command_alignment_gain` |
| `cannibalism_unified_origin_template_mapping_open` | `cannibalism_unified_origin_specialist_support_reserve` |
| `cannibalism_unified_postwar_integration_open` | `cannibalism_unified_integration_resistance` |
| `cannibalism_unified_prewar_cell_operations_open` | `cannibalism_unified_cell_operation_duration` |
| `cannibalism_unified_prison_administration_projects_open` | `cannibalism_unified_command_network_gain` |
| `cannibalism_unified_prison_hulk_decisions_open` | `cannibalism_unified_naval_convoy_cost` |
| `cannibalism_unified_prison_hulk_transport_open` | `cannibalism_unified_larder_mission_progress`, `cannibalism_unified_mobile_convoy_cost` |
| `cannibalism_unified_prison_port_cell_missions_open` | `cannibalism_unified_cell_support_cost` |
| `cannibalism_unified_prisoner_train_decisions_open` | `cannibalism_unified_mobile_train_cost` |
| `cannibalism_unified_public_command_established` | `cannibalism_unified_command_planning` |
| `cannibalism_unified_punishment_table_decisions_open` | `cannibalism_unified_command_authority_gain`, `cannibalism_unified_command_hostility_gain` |
| `cannibalism_unified_purge_resistance_risk` | `cannibalism_unified_purge_hostility_gain` |
| `cannibalism_unified_raider_construction_costs_required` | `cannibalism_unified_naval_support_cost` |
| `cannibalism_unified_raider_flotilla_decisions_open` | `cannibalism_unified_naval_raiding` |
| `cannibalism_unified_rank_standardization_open` | `cannibalism_unified_command_army_experience_cost` |
| `cannibalism_unified_rapid_consumption_decisions_open` | `cannibalism_unified_rapid_command_cost` |
| `cannibalism_unified_rapid_larder_capstone` | `cannibalism_unified_larder_mission_success_authority`, `cannibalism_unified_rapid_command_cost` |
| `cannibalism_unified_rapid_recruitment_cost_scaling_open` | `cannibalism_unified_bone_guard_larder_cost`, `cannibalism_unified_legion_larder_cost`, `cannibalism_unified_rapid_hostility_gain` |
| `cannibalism_unified_recovery_battalion_missions_open` | `cannibalism_unified_larder_mission_days` |
| `cannibalism_unified_regional_army_compacts_open` | `cannibalism_unified_command_army_experience_cost` |
| `cannibalism_unified_regional_governor_assignments_open` | `cannibalism_unified_governor_local_supply` |
| `cannibalism_unified_regional_host_votes_open` | `cannibalism_unified_command_mission_progress` |
| `cannibalism_unified_regional_recruitment_open` | `cannibalism_unified_command_operation_duration` |
| `cannibalism_unified_regional_theater_missions_open` | `cannibalism_unified_command_mission_days` |
| `cannibalism_unified_relief_corridor_attack_missions_open` | `cannibalism_unified_counterwar_mission_progress` |
| `cannibalism_unified_remote_command_missions_open` | `cannibalism_unified_command_operation_duration` |
| `cannibalism_unified_retained_host_council_open` | `cannibalism_unified_command_org_regain` |
| `cannibalism_unified_retreat_cell_preservation_open` | `cannibalism_unified_cell_operation_duration` |
| `cannibalism_unified_retreat_disruption_open` | `cannibalism_unified_enemy_front_organization` |
| `cannibalism_unified_ritual_administration_open` | `cannibalism_unified_command_authority_gain` |
| `cannibalism_unified_ritual_census_open` | `cannibalism_unified_governor_command_cost` |
| `cannibalism_unified_ritual_state_capstone` | `cannibalism_unified_command_authority_gain`, `cannibalism_unified_command_network_gain`, `cannibalism_unified_command_org_regain` |
| `cannibalism_unified_rival_purges_open` | `cannibalism_unified_purge_target_defence` |
| `cannibalism_unified_rout_harvest_caps_required` | `cannibalism_unified_enemy_front_support_cost`, `cannibalism_unified_enemy_front_target_lock_days`, `cannibalism_unified_rout_harvest_receipt_cap` |
| `cannibalism_unified_rout_harvest_missions_open` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_route_interdiction_missions_open` | `cannibalism_unified_larder_mission_days`, `cannibalism_unified_mobile_hostility_gain` |
| `cannibalism_unified_shipyard_projects_open` | `cannibalism_unified_anchorage_manpower_cost` |
| `cannibalism_unified_short_campaign_horizon` | `cannibalism_unified_larder_mission_failure_hostility`, `cannibalism_unified_larder_mission_goal` |
| `cannibalism_unified_silent_anchorage_projects_open` | `cannibalism_unified_anchorage_support_cost` |
| `cannibalism_unified_single_will_capstone` | `cannibalism_unified_command_org_regain`, `cannibalism_unified_command_planning` |
| `cannibalism_unified_standard_training_missions_open` | `cannibalism_unified_command_mission_goal` |
| `cannibalism_unified_state_classification_open` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_state_exhaustion_risk` | `cannibalism_unified_rapid_hostility_gain` |
| `cannibalism_unified_state_ledger_open` | `cannibalism_unified_command_mission_days` |
| `cannibalism_unified_storage_projects_open` | `cannibalism_unified_storage_supply` |
| `cannibalism_unified_submission_decisions_open` | `cannibalism_unified_absorb_authority_gain` |
| `cannibalism_unified_supply_ceiling_package_pending` | `cannibalism_unified_larder_mission_days` |
| `cannibalism_unified_supply_interdiction_missions_open` | `cannibalism_unified_air_operation_duration` |
| `cannibalism_unified_synchronized_uprising_missions_open` | `cannibalism_unified_cell_network_gain` |
| `cannibalism_unified_template_conversion_missions_open` | `cannibalism_unified_legion_infantry_reserve` |
| `cannibalism_unified_terminal_army_gate` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_terminal_army_package_active` | `cannibalism_unified_army_operation_duration` |
| `cannibalism_unified_terminal_counterwar_gate` | `cannibalism_unified_counterwar_mission_progress` |
| `cannibalism_unified_terminal_expansion_gate` | `cannibalism_unified_integration_local_supply` |
| `cannibalism_unified_terminal_larder_gate` | `cannibalism_unified_larder_mission_progress` |
| `cannibalism_unified_territorial_integration_open` | `cannibalism_unified_governor_local_supply` |
| `cannibalism_unified_terror_reconnaissance_missions_open` | `cannibalism_unified_war_machine_mission_progress` |
| `cannibalism_unified_terror_ultimata_open` | `cannibalism_unified_ultimatum_larder_cost` |
| `cannibalism_unified_theater_command_assignments_open` | `cannibalism_unified_command_operation_duration` |
| `cannibalism_unified_three_army_coordination_open` | `cannibalism_unified_army_command_cost` |
| `cannibalism_unified_transport_aircraft_costs_required` | `cannibalism_unified_air_fuel_cost` |
| `cannibalism_unified_transport_escort_burden` | `cannibalism_unified_mobile_support_cost` |
| `cannibalism_unified_tribute_failure_missions_open` | `cannibalism_unified_command_mission_failure_hostility` |
| `cannibalism_unified_ultimatum_refusal_missions_open` | `cannibalism_unified_campaign_hostility_gain` |
| `cannibalism_unified_uprising_target_cap_active` | `cannibalism_unified_cell_target_lock_days` |
| `cannibalism_unified_victory_harvest_scaling_open` | `cannibalism_unified_battlefield_receipts_per_victory` |
| `cannibalism_unified_warband_integration_open` | `cannibalism_unified_legion_population_cost_k` |
| `cannibalism_unified_warlord_audit_open` | `cannibalism_unified_purge_army_experience_cost` |
| `cannibalism_unified_warlord_response_resolution_open` | `cannibalism_unified_absorb_authority_gain` |
| `cannibalism_unified_warlord_settlement_category_open` | `cannibalism_unified_command_mission_success_authority` |
| `cannibalism_unified_workshop_conversion_open` | `cannibalism_unified_storage_factory_output`, `cannibalism_unified_workshop_resistance` |
| `cannibalism_unified_world_hostility_breakdown_open` | `cannibalism_unified_counterwar_relief` |

Audit result: **208/208 domain flags mapped; unresolved flags: none.**

## Validation and risks

- All 39 unified decisions have name localisation; all 117 referenced unified tooltip/cost keys resolve.
- The three receipt systems have bounded variables and spend paths; battlefield receipts are deduplicated by defeated-country array.
- Local script-constant references resolve; the localisation file remains UTF-8 with BOM and uses no `:0` suffixes.
- Braces are balanced in all five gameplay files.
- The meaningful external dependency is later-warlord origin/route accumulation in root-owned unification effects. The decision surface is already multi-origin safe once those flags are supplied.

## Simplifications, omissions, and blockers

No simplification or fallback was used in the owned unified decision surface. No focus-created domain flag remains capacity-only. The only cross-file dependency is the root-owned accumulation of later absorbed origins/routes described above.


