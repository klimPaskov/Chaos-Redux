# Event 12 localisation player-text delta handoff (2026-07-30)

## Scope

This patch covers non-world-order Event 12 English localisation only. The world-order localisation file `localisation/english/012_africa_world_order_l_english.yml` was deliberately left untouched. No gameplay, scripted GUI, scripted localisation, event, decision, focus, country, or asset files were changed.

## Changed files and keys

### `localisation/english/012_africa_achievements_l_english.yml`

- `africa_member_who_said_no_tooltip` now says `Tier A African polity` instead of exposing the internal `Event 12` label.

### `localisation/english/012_africa_charter_gui_l_english.yml`

- `africa_charter_gui_missing_value`
- `africa_charter_gui_overlay_unassigned`
- `africa_charter_gui_protection_unrecorded`
- `africa_charter_gui_rival_pressure_recorded`
- `africa_charter_gui_corridor_unrecorded`
- `africa_charter_gui_settlement_unrecorded`
- `africa_charter_gui_rival_warning_clear`

The status text now describes the current absence or presence of a live record rather than exposing ledger or overlay implementation terms.

### `localisation/english/012_africa_evolutions_l_english.yml`

- `africa_evolution_i_effect_tt` now describes additional regional contacts and living-core capacity rather than an action/target/dossier record.

### `localisation/english/012_africa_rsa_l_english.yml`

- `chaosx.nr12.1206.d`
- `africa_rsa_allied_branch_can_start_tt`
- `africa_rsa_start_allied_civil_war_tt`
- `africa_rsa_continental_coalition_opening_tt`
- `africa_rsa_loyalist_suppression_tt`
- `africa_rsa_exile_custodian_tt`
- `africa_rsa_no_exile_patron_tt`
- `africa_rsa_citizenship_land_milestone_tt`
- `africa_rsa_terminate_base_lease_tt`
- `africa_rsa_reconstitute_exile_council_tt`

These tooltips now use Charter agreements, public identity, lawful custody, and active arrangements instead of relationship rolls, generation lineage, dynamic-host labels, or cleanup instructions.

### `localisation/english/012_african_union_l_english.yml`

The action-card descriptions were rewritten so their closure clauses describe what the player sees in the world rather than clearing flags, state groups, modifiers, tags, missions, or duplicate routes. The changed keys are:

- `africa_charter_council_category_desc`
- `africa_refresh_african_contacts_desc`
- `africa_refresh_external_crisis_targets_desc`
- `africa_select_action_state_target_desc`
- `africa_action_result_mediate_continent_union_full`
- `africa_action_result_form_dynamic_two_continent_union_full`
- `africa_action_name_form_dynamic_two_continent_union`
- `africa_select_form_dynamic_two_continent_union`
- `africa_action_result_declare_the_world_is_one_full`
- `africa_select_declare_the_world_is_one_desc`
- `africa_select_ratify_confederal_emergency_action_desc`
- `africa_select_mediate_continent_union_desc`
- `africa_select_form_dynamic_two_continent_union_desc`
- `africa_select_train_gorilla_heavy_infantry_desc`
- `africa_select_organise_pan_sappers_desc`
- `africa_select_seek_international_recognition_desc`
- `africa_select_prepare_anti_sanctions_network_desc`
- `africa_select_answer_foreign_ultimatum_desc`
- `africa_select_mobilise_continental_defence_desc`
- `africa_select_disrupt_expedition_planning_desc`
- `africa_select_offer_base_withdrawal_treaty_desc`
- `africa_select_call_global_anti_colonial_conference_desc`
- `africa_select_break_intervention_coalition_desc`
- `africa_select_sponsor_continent_unifier_desc`
- `africa_select_prepare_continental_war_desc`
- `africa_select_force_continent_submission_desc`
- `africa_select_administer_world_regions_desc`
- `africa_select_contain_terminal_high_chaos_desc`
- `africa_select_convene_federal_deadlock_conference_desc`
- `africa_select_arbitrate_continental_succession_desc`
- `africa_select_balance_food_and_industrial_plan_desc`
- `africa_select_review_victorious_commander_loyalty_desc`
- `africa_select_review_covenant_obligation_desc`
- `africa_select_hold_postwar_constitutional_review_desc`
- `africa_select_recover_failed_host_proof_desc`
- `africa_select_promote_priority_member_package_desc`

The same action-description family also includes the earlier cleanup keys `africa_select_guarantee_sovereignty_desc`, `africa_select_open_aid_corridor_desc`, `africa_select_dispatch_charter_mission_desc`, `africa_select_deploy_volunteers_desc`, `africa_select_intervene_against_coloniser_desc`, `africa_select_evacuate_leaders_archives_desc`, `africa_select_recognise_provisional_government_desc`, `africa_select_secure_border_sanctuary_desc`, `africa_select_break_blockade_desc`, `africa_select_emergency_relief_column_desc`, `africa_select_offer_defence_charter_desc`, `africa_select_offer_development_charter_desc`, `africa_select_offer_federal_charter_desc`, `africa_select_offer_crown_charter_desc`, `africa_select_offer_peoples_charter_desc`, `africa_select_offer_security_charter_desc`, `africa_select_offer_sacred_ecological_compact_desc`, `africa_select_renegotiate_accession_clauses_desc`, `africa_select_hold_accession_referendum_desc`, `africa_select_admit_member_in_emergency_desc`, `africa_select_convene_regional_congress_desc`, `africa_select_settle_overlapping_claims_desc`, `africa_select_create_regional_charter_desc`, `africa_select_form_regional_federation_desc`, `africa_select_restore_historical_polity_desc`, `africa_select_approve_direct_integration_schedule_desc`, `africa_select_guarantee_regional_representation_desc`, `africa_select_fund_congress_security_desc`, `africa_select_invite_diaspora_delegates_desc`, `africa_select_enforce_congress_settlement_desc`, `africa_select_build_administrative_bridge_desc`, `africa_select_connect_member_capitals_desc`, `africa_select_standardise_customs_desc`, `africa_select_integrate_security_services_desc`, `africa_select_harmonise_officer_corps_desc`, `africa_select_negotiate_autonomy_statute_desc`, `africa_select_launch_local_settlement_programme_desc`, `africa_select_grant_core_recognition_desc`, `africa_select_impose_emergency_administration_desc`, `africa_select_federalise_restored_polities_desc`, `africa_select_survey_continental_resources_desc`, `africa_select_build_regional_rail_spine_desc`, `africa_select_expand_river_transport_desc`, `africa_select_modernise_continental_port_desc`, `africa_select_create_local_processing_chain_desc`, `africa_select_continental_procurement_contract_desc`, `africa_select_food_security_reserve_desc`, `africa_select_resource_sovereignty_review_desc`, `africa_select_charter_development_fund_desc`, `africa_select_continental_industrial_plan_desc`, `africa_select_open_voluntary_return_registry_desc`, `africa_select_charter_passage_programme_desc`, `africa_select_build_returnee_housing_desc`, `africa_select_invite_afro_american_technical_mission_desc`, `africa_select_veterans_and_volunteers_programme_desc`, `africa_select_diaspora_investment_bonds_desc`, `africa_select_citizenship_and_representation_convention_desc`, `africa_select_diaspora_emergency_evacuation_desc`, `africa_select_monitor_rival_bloc_desc`, `africa_select_offer_rival_arbitration_desc`, `africa_select_support_rival_member_defection_desc`, `africa_select_counter_foreign_patronage_desc`, `africa_select_prepare_member_exit_terms_desc`, `africa_select_suspend_disloyal_member_desc`, `africa_select_emergency_leadership_vote_desc`, `africa_select_contain_regional_secession_war_desc`, `africa_select_consult_oracle_network_desc`, `africa_select_bargain_with_the_green_desc`, `africa_select_petition_the_rain_desc`, `africa_select_defy_the_drought_desc`, `africa_select_contain_emergent_disease_desc`, `africa_select_research_disease_countermeasure_desc`, `africa_select_weaponise_fictional_pathogen_desc`, and `africa_select_awaken_stone_cohort_desc`.

## Audit results

- Missing localisation keys: none in the 3,321 Event 12 English keys scanned.
- Duplicate localisation keys: none across all ten Event 12 English YAML files.
- Scripted localisation issues: none. The three Event 12 scripted-localisation files contain 1,138 `localization_key` references and all resolve to English localisation keys.
- Dynamic text opportunities: selected action costs already expose live resource variables, selected targets retain `[GetName]` or `[GetNameDef]`, and event/mission text retains current actor and target names. The rewritten GUI and action descriptions avoid static implementation labels while preserving these dynamic values.
- Cross-surface mismatch notes: the visible `Form Two-Continent Union` label is now aligned with its result and description; the internal localisation key remains stable for gameplay references. The world-order localisation file remains outside this patch. The ten orphan cost/blocked keys and the two RSA branch-start keys recorded by the deep audit remain unresolved because wiring or removal requires gameplay-owner confirmation.
- Exact Afaan Oromoo sensitivity-protocol strings remain absent from runtime localisation and technical identifiers.
- File encoding: all ten Event 12 English YAML files retain UTF-8 BOM. The three Event 12 scripted-localisation files remain UTF-8 without BOM, matching the existing repository convention.

## Validation

- Duplicate-key scan over all ten Event 12 English YAML files: `files=10 keys=3321 duplicate_groups=0`.
- Scripted-localisation reference scan: `scripted_refs=1138 missing=0`.
- BOM scan: all ten Event 12 English YAML files report `BOM=True`; all three Event 12 scripted-localisation files report `BOM=False`.
- Runtime sensitivity-string scan over `localisation` and `common`: `runtime_hits=0`.
- `git diff --check` over the five changed localisation files: clean.

## Unresolved wording and scope decisions

- The deep-audit orphan cost and branch-start keys remain present but unreferenced pending gameplay-owner confirmation; deleting or wiring them would change implementation scope.
- Existing historical terms such as `technical mission` remain where they name an in-world advisory mission rather than an engine concept.
- Live Hearts of Iron IV validation was skipped because agents must not launch the game; the parent owns live consumer verification.

No gameplay fallback or mechanic simplification was introduced. No commit was created.
