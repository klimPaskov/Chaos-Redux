# Event 15 Utopia Manifesto Localisation Implementation Handoff

## Scope completed

This tranche implements the final English localisation for every stable, non-decision Event 15 surface available during the assignment. It covers the entry and follow-up events, the restored 122-focus tree, current ideas, the Commonwealth Ledger and scripted localisation, country identities, parties, institutional leaders, advisors, achievements, opinion modifiers, evolutions, super-event variants, and shared Event Details mappings.

The current decision, mission, and additional category package was intentionally preserved for its owning implementer. Its exact missing localisation inventory appears below.

## Files changed

- `localisation/english/015_utopia_manifesto_l_english.yml`
  - Preserved the entry event, availability reasons, Ledger, scripted-localisation strings, and the current deferred decision block.
  - Removed stale recovered country identities, the obsolete focus architecture, obsolete idea strings, eight obsolete focus tooltips, and retired super-event slots 151 and 152.
  - Replaced semicolons in preserved player-facing decision strings without changing their meaning.
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
  - Added all stable event titles, descriptions, and options after the entry event.
- `localisation/english/015_utopia_manifesto_focus_l_english.yml`
  - Added the tree name and description plus all 122 focus name and description pairs.
- `localisation/english/015_utopia_manifesto_ideas_l_english.yml`
  - Added coverage for all 50 current ideas.
- `localisation/english/015_utopia_manifesto_country_package_l_english.yml`
  - Added all route identities, party names, leaders, advisors, achievements, and opinion modifiers.
- `localisation/english/015_utopia_manifesto_evolutions_l_english.yml`
  - Aligned the five public evolution titles to the accepted specifications.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/localisation_implementation_handoff.md`
  - Records coverage, integration findings, validation, and deferred dependencies.

No gameplay, interface, asset, or spreadsheet file was edited by this localisation tranche. The existing `localisation/english/015_utopia_manifesto_super_event_l_english.yml` wording and canonical slots 96 through 100 were preserved.

## Machine-readable coverage

```yaml
event_15_localisation:
  events:
    visible_windows: 79
    title_keys_covered: 79
    description_keys_covered: 79
    option_keys_covered: 250
    missing_stable_keys: 0
  focus_tree:
    focus_blocks: 122
    focus_name_refs_covered: 122
    focus_description_refs_covered: 122
    tree_header_keys: 2
    missing_stable_keys: 0
  ideas:
    scripted_idea_ids: 50
    idea_name_refs_covered: 50
    idea_description_refs_covered: 50
    direct_definition_pairs: 49
    shared_definition_pairs: 1
    shared_key: utopia_manifesto_perfect_measure
    missing_stable_keys: 0
  scripted_localisation:
    localisation_key_references: 137
    unique_localisation_keys: 108
    unique_keys_covered: 108
    missing_stable_keys: 0
  ledger:
    direct_gui_text_and_tooltip_refs: 25
    category_name_and_description_keys: 2
    total_ledger_keys_covered: 27
    missing_stable_keys: 0
  country_identities:
    cosmetic_tags: 5
    generic_and_ideology_specific_keys: 75
    missing_stable_keys: 0
  parties:
    short_and_long_name_keys: 10
    missing_stable_keys: 0
  characters:
    institutional_leaders_and_advisors: 24
    name_refs_covered: 24
    description_refs_covered: 24
    direct_definition_pairs: 23
    shared_definition_pairs: 1
    shared_key: utopia_manifesto_board_of_measure
    missing_stable_keys: 0
  achievements:
    achievements: 14
    name_keys: 14
    description_keys: 14
    requirement_tooltips: 14
    total_keys: 42
    missing_stable_keys: 0
  opinion_modifiers:
    modifiers: 5
    keys_covered: 5
    missing_stable_keys: 0
  evolutions:
    evolutions: 5
    localisation_keys: 18
    missing_stable_keys: 0
  super_events:
    variants: 5
    canonical_slots: [96, 97, 98, 99, 100]
    title_quote_button_description_keys: 20
    missing_stable_keys: 0
  shared_event_mappings:
    event_name_keys: 1
    event_details_keys: 1
    missing_stable_keys: 0
  event_15_files:
    total_unique_localisation_definitions: 1290
    duplicate_keys: 0
    malformed_localisation_lines: 0
  deferred_decision_package:
    decision_and_mission_ids_missing_name_and_description: 128
    additional_categories_missing_name_and_description: 8
    explicit_cost_and_effect_tooltip_refs_missing: 197
```

## Integration finding resolved

Twenty-four event windows originally reused `chaosx.nr15.<id>.d` for both the event description and the fourth option. One localisation key cannot represent both strings. The event owner changed every affected fourth option to `chaosx.nr15.<id>.option_d`, and this localisation tranche changed the corresponding option keys. Event descriptions remain `.d`.

Affected event IDs:

```yaml
fourth_option_key_migration:
  old_suffix: .d
  new_suffix: .option_d
  event_ids: [3, 4, 12, 15, 20, 22, 23, 30, 31, 32, 40, 43, 51, 53, 62, 63, 64, 71, 72, 73, 82, 84, 210, 114]
```

Two identifiers are intentionally shared across UI systems because one wording fits both surfaces:

- `utopia_manifesto_board_of_measure` is both a focus and an institutional character. Its single name and description describe the collective board, its appointments, standards, and accountability.
- `utopia_manifesto_perfect_measure` is both a focus and a national spirit. Its single present-tense name and description describe the measured commonwealth in either surface.

## Voice and terminology

- The five routes use distinct institutional language: households and charters, common tables and recallable councils, measurement and appeals, sealed service and assigned colonies, or criticism and revision.
- Focus descriptions state a public action and its institutional direction without exposing hidden thresholds or achievement routing.
- Event options describe the choice in the voice of the current world state.
- Player-facing text contains no implementation-history language.
- Exact accepted evolution titles are `Glosses in the Margin`, `Necessary Shores`, `Cities of One Measure`, `Nowhere Made Law`, and `The Perfect Island`.
- The accepted Thomas More quotation package and the five route-specific super-event descriptions remain in slots 96 through 100.

## Validation evidence

- All 122 restored focus IDs resolve to one name and one description.
- All 79 visible event titles, 79 descriptions, and 250 option references resolve after the `.option_d` migration.
- All 50 idea IDs, 24 character IDs, 14 achievements, 10 party references, 5 opinion modifiers, and 108 unique scripted-localisation keys resolve.
- The Event 15 localisation files contain 1,290 unique definitions with no duplicate key.
- All seven Event 15 English localisation files use UTF-8 with BOM.
- Player-facing Event 15 strings contain no `:0`, em dash, or semicolon.
- Super-event selectors and localisation use 96 through 100, with no Event 15 references to 85 through 89.

## Deferred decision localisation dependency

The decision implementer owns the current 128 decision and mission IDs, eight additional categories, and 197 explicit cost or effect tooltip references. None of those current references has final localisation in the preserved Event 15 localisation set. The older recovered decision strings remain in `015_utopia_manifesto_l_english.yml` only because the parent explicitly required the current decision package to be preserved during this tranche. They do not cover the current identifiers and must be reconciled by the decision owner before Event 15 can be declared globally complete.

### Decision and mission IDs missing both name and description

- `decision_utopia_count_houses_and_hands`
- `mission_utopia_count_houses_and_hands`
- `decision_utopia_recount_the_country`
- `decision_utopia_publish_the_accounts`
- `decision_utopia_establish_capital_store`
- `mission_utopia_establish_capital_store`
- `decision_utopia_fill_seasonal_reserve`
- `mission_utopia_fill_seasonal_reserve`
- `decision_utopia_rotate_old_stores`
- `decision_utopia_release_emergency_stores`
- `decision_utopia_two_years_against_hunger`
- `mission_utopia_two_years_against_hunger`
- `decision_utopia_select_provisioning_calling`
- `decision_utopia_select_workshops_calling`
- `decision_utopia_select_civic_works_calling`
- `decision_utopia_select_learning_and_care_calling`
- `decision_utopia_select_maritime_and_settlement_calling`
- `decision_utopia_select_defense_and_watches_calling`
- `decision_utopia_issue_open_call`
- `decision_utopia_guarantee_placement`
- `decision_utopia_set_assignment_quota`
- `decision_utopia_emergency_calling_levy`
- `mission_utopia_fill_unpopular_calling`
- `decision_utopia_learn_second_trade`
- `mission_utopia_learn_second_trade`
- `decision_utopia_suspend_the_short_day`
- `mission_utopia_short_day_suspension`
- `decision_utopia_register_public_land`
- `mission_utopia_register_public_land`
- `decision_utopia_convert_estate_to_land_trust`
- `decision_utopia_transfer_factory_to_worker_council`
- `decision_utopia_assign_productive_tenure`
- `decision_utopia_revoke_idle_grant`
- `mission_utopia_property_transition`
- `decision_utopia_survey_district_site`
- `mission_utopia_survey_district_site`
- `decision_utopia_found_market_garden_district`
- `decision_utopia_found_industrial_housing_district`
- `decision_utopia_found_rail_junction_town`
- `decision_utopia_found_refugee_municipality`
- `mission_utopia_build_garden_district`
- `decision_utopia_complete_district_charter`
- `mission_utopia_complete_district_charter`
- `decision_utopia_prepare_national_island_variant`
- `decision_utopia_adopt_existing_island_capital`
- `decision_utopia_adopt_coastal_refuge`
- `decision_utopia_adopt_inland_island`
- `decision_utopia_secure_island_site`
- `decision_utopia_build_common_harbor`
- `decision_utopia_build_inland_terminal`
- `decision_utopia_complete_capital_provision_ring`
- `decision_utopia_fortify_without_sealing`
- `decision_utopia_close_the_gates`
- `mission_utopia_build_island_stage`
- `decision_utopia_make_an_island`
- `mission_utopia_make_an_island`
- `decision_utopia_select_necessary_ground_target`
- `decision_utopia_clear_necessary_ground_target`
- `decision_utopia_survey_domestic_alternatives`
- `mission_utopia_survey_domestic_alternatives`
- `decision_utopia_draft_need_case`
- `decision_utopia_select_need_case_state`
- `mission_utopia_need_case_expiry`
- `decision_utopia_offer_purchase`
- `decision_utopia_offer_long_supply_contract`
- `decision_utopia_request_lease`
- `decision_utopia_propose_joint_administration`
- `decision_utopia_invite_associate_municipality`
- `mission_utopia_wait_for_need_answer`
- `decision_utopia_revise_need_offer`
- `decision_utopia_issue_need_ultimatum`
- `decision_utopia_enforce_need_case`
- `decision_utopia_renounce_need_case`
- `decision_utopia_convert_case_to_lease`
- `decision_utopia_convert_case_to_joint_administration`
- `decision_utopia_confirm_stewardship_obligation`
- `decision_utopia_begin_emergency_provision`
- `mission_utopia_emergency_provision`
- `decision_utopia_restore_stewardship_route`
- `mission_utopia_restore_stewardship_route`
- `decision_utopia_convene_local_charter`
- `decision_utopia_impose_assigned_administration`
- `decision_utopia_hold_charter_period`
- `mission_utopia_hold_charter_period`
- `decision_utopia_hold_stewardship_status_vote`
- `decision_utopia_offer_stewardship_autonomy`
- `decision_utopia_return_stewardship`
- `decision_utopia_begin_long_integration`
- `mission_utopia_long_integration`
- `decision_utopia_clean_up_stewardship_revolt`
- `decision_utopia_initialize_league`
- `decision_utopia_send_surplus_abroad`
- `decision_utopia_send_technical_mission`
- `mission_utopia_technical_mission`
- `decision_utopia_open_reserve_compact`
- `mission_utopia_reserve_compact_answer`
- `decision_utopia_invite_to_league`
- `mission_utopia_league_invitation_answer`
- `decision_utopia_prove_league_not_mask`
- `mission_utopia_prove_league_not_mask`
- `decision_utopia_pool_reconstruction_brigades`
- `decision_utopia_call_mutual_defense_council`
- `decision_utopia_accept_league_sponsorship`
- `decision_utopia_expel_exploitative_member`
- `decision_utopia_guard_the_common_stores`
- `mission_utopia_guard_the_common_stores`
- `decision_utopia_raise_a_citizen_watch`
- `mission_utopia_raise_a_citizen_watch`
- `decision_utopia_form_engineer_companies`
- `mission_utopia_form_engineer_companies`
- `decision_utopia_hire_auxiliary_contracts`
- `decision_utopia_end_the_auxiliary_contract`
- `mission_utopia_end_the_auxiliary_contract`
- `decision_utopia_open_constitutional_correction`
- `mission_utopia_constitutional_correction`
- `decision_utopia_call_a_household_referendum`
- `decision_utopia_convene_the_calling_councils`
- `decision_utopia_request_a_new_forecast`
- `decision_utopia_extend_the_service_register`
- `decision_utopia_add_a_sunset_clause`
- `decision_utopia_publish_corrected_tenure_tables`
- `decision_utopia_negotiate_district_appeals`
- `decision_utopia_prove_the_commonwealth`
- `mission_utopia_prove_the_commonwealth`
- `decision_utopia_proclaim_the_commonwealth`
- `decision_utopia_integrate_post_formation_institutions`
- `decision_utopia_reinforce_post_formation_defense`
- `decision_utopia_refresh_post_formation_charters`

### Additional category IDs missing both name and description

- `utopia_manifesto_district_category`
- `utopia_manifesto_island_category`
- `utopia_manifesto_necessary_ground_category`
- `utopia_manifesto_stewardship_category`
- `utopia_manifesto_league_category`
- `utopia_manifesto_defense_category`
- `utopia_manifesto_governance_category`
- `utopia_manifesto_formation_category`

### Explicit cost and effect tooltip keys missing localisation

- `utopia_manifesto_cost_survey_transport`
- `decision_utopia_count_houses_and_hands_effect_tt`
- `mission_utopia_count_houses_and_hands_success_tt`
- `utopia_manifesto_cost_recount_transport`
- `decision_utopia_recount_the_country_effect_tt`
- `decision_utopia_publish_the_accounts_effect_tt`
- `utopia_manifesto_cost_store_construction`
- `decision_utopia_establish_capital_store_effect_tt`
- `mission_utopia_establish_capital_store_success_tt`
- `utopia_manifesto_cost_seasonal_reserve`
- `decision_utopia_fill_seasonal_reserve_effect_tt`
- `mission_utopia_fill_seasonal_reserve_success_tt`
- `utopia_manifesto_cost_store_rotation`
- `decision_utopia_rotate_old_stores_effect_tt`
- `decision_utopia_release_emergency_stores_effect_tt`
- `utopia_manifesto_cost_two_year_reserve`
- `decision_utopia_two_years_against_hunger_effect_tt`
- `mission_utopia_two_years_against_hunger_success_tt`
- `utopia_manifesto_cost_open_call`
- `decision_utopia_issue_open_call_effect_tt`
- `utopia_manifesto_cost_guaranteed_placement`
- `decision_utopia_guarantee_placement_effect_tt`
- `utopia_manifesto_cost_assignment_quota`
- `decision_utopia_set_assignment_quota_effect_tt`
- `utopia_manifesto_cost_emergency_levy`
- `decision_utopia_emergency_calling_levy_effect_tt`
- `mission_utopia_fill_unpopular_calling_outcome_tt`
- `utopia_manifesto_cost_second_trade`
- `decision_utopia_learn_second_trade_effect_tt`
- `mission_utopia_learn_second_trade_success_tt`
- `utopia_manifesto_cost_short_day_suspension`
- `decision_utopia_suspend_the_short_day_effect_tt`
- `mission_utopia_short_day_suspension_end_tt`
- `utopia_manifesto_cost_land_register`
- `decision_utopia_register_public_land_effect_tt`
- `mission_utopia_register_public_land_success_tt`
- `utopia_manifesto_cost_land_trust`
- `decision_utopia_convert_estate_to_land_trust_effect_tt`
- `utopia_manifesto_cost_worker_council`
- `decision_utopia_transfer_factory_to_worker_council_effect_tt`
- `utopia_manifesto_cost_productive_tenure`
- `decision_utopia_assign_productive_tenure_effect_tt`
- `utopia_manifesto_cost_idle_grant`
- `decision_utopia_revoke_idle_grant_effect_tt`
- `mission_utopia_property_transition_success_tt`
- `utopia_manifesto_cost_district_survey`
- `decision_utopia_survey_district_site_effect_tt`
- `mission_utopia_survey_district_site_success_tt`
- `utopia_manifesto_cost_market_garden`
- `decision_utopia_found_market_garden_district_effect_tt`
- `utopia_manifesto_cost_industrial_housing`
- `decision_utopia_found_industrial_housing_district_effect_tt`
- `utopia_manifesto_cost_rail_junction`
- `decision_utopia_found_rail_junction_town_effect_tt`
- `utopia_manifesto_cost_refugee_municipality`
- `decision_utopia_found_refugee_municipality_effect_tt`
- `mission_utopia_build_garden_district_success_tt`
- `utopia_manifesto_cost_district_charter`
- `decision_utopia_complete_district_charter_effect_tt`
- `mission_utopia_complete_district_charter_success_tt`
- `decision_utopia_prepare_national_island_variant_effect_tt`
- `utopia_manifesto_cost_island_plan`
- `decision_utopia_adopt_existing_island_capital_effect_tt`
- `utopia_manifesto_cost_coastal_plan`
- `decision_utopia_adopt_coastal_refuge_effect_tt`
- `utopia_manifesto_cost_inland_plan`
- `decision_utopia_adopt_inland_island_effect_tt`
- `utopia_manifesto_cost_secure_island_site`
- `decision_utopia_secure_island_site_effect_tt`
- `utopia_manifesto_cost_common_harbor`
- `decision_utopia_build_common_harbor_effect_tt`
- `utopia_manifesto_cost_inland_terminal`
- `decision_utopia_build_inland_terminal_effect_tt`
- `utopia_manifesto_cost_provision_ring`
- `decision_utopia_complete_capital_provision_ring_effect_tt`
- `utopia_manifesto_cost_open_fortification`
- `decision_utopia_fortify_without_sealing_effect_tt`
- `utopia_manifesto_cost_close_gates`
- `decision_utopia_close_the_gates_effect_tt`
- `mission_utopia_build_island_stage_success_tt`
- `utopia_manifesto_cost_make_island`
- `decision_utopia_make_an_island_effect_tt`
- `mission_utopia_make_an_island_success_tt`
- `decision_utopia_select_necessary_ground_target_effect_tt`
- `decision_utopia_clear_necessary_ground_target_effect_tt`
- `utopia_manifesto_cost_domestic_alternatives`
- `decision_utopia_survey_domestic_alternatives_effect_tt`
- `mission_utopia_survey_domestic_alternatives_outcome_tt`
- `utopia_manifesto_cost_need_case_draft`
- `decision_utopia_draft_need_case_effect_tt`
- `decision_utopia_select_need_case_state_effect_tt`
- `mission_utopia_need_case_expiry_failure_tt`
- `utopia_manifesto_cost_purchase_offer`
- `decision_utopia_offer_purchase_effect_tt`
- `utopia_manifesto_cost_long_supply_offer`
- `decision_utopia_offer_long_supply_contract_effect_tt`
- `utopia_manifesto_cost_lease_request`
- `decision_utopia_request_lease_effect_tt`
- `utopia_manifesto_cost_joint_administration`
- `decision_utopia_propose_joint_administration_effect_tt`
- `utopia_manifesto_cost_associate_offer`
- `decision_utopia_invite_associate_municipality_effect_tt`
- `mission_utopia_wait_for_need_answer_refusal_tt`
- `utopia_manifesto_cost_revised_offer`
- `decision_utopia_revise_need_offer_effect_tt`
- `utopia_manifesto_cost_need_ultimatum`
- `decision_utopia_issue_need_ultimatum_effect_tt`
- `utopia_manifesto_cost_enforce_case`
- `decision_utopia_enforce_need_case_effect_tt`
- `decision_utopia_renounce_need_case_effect_tt`
- `utopia_manifesto_cost_case_conversion`
- `decision_utopia_convert_case_to_lease_effect_tt`
- `decision_utopia_convert_case_to_joint_administration_effect_tt`
- `decision_utopia_confirm_stewardship_obligation_effect_tt`
- `utopia_manifesto_cost_stewardship_provision`
- `decision_utopia_begin_emergency_provision_effect_tt`
- `mission_utopia_emergency_provision_success_tt`
- `utopia_manifesto_cost_restore_route`
- `decision_utopia_restore_stewardship_route_effect_tt`
- `mission_utopia_restore_stewardship_route_success_tt`
- `utopia_manifesto_cost_local_charter`
- `decision_utopia_convene_local_charter_effect_tt`
- `utopia_manifesto_cost_assigned_administration`
- `decision_utopia_impose_assigned_administration_effect_tt`
- `utopia_manifesto_cost_charter_period`
- `decision_utopia_hold_charter_period_effect_tt`
- `mission_utopia_hold_charter_period_success_tt`
- `utopia_manifesto_cost_status_vote`
- `decision_utopia_hold_stewardship_status_vote_effect_tt`
- `decision_utopia_offer_stewardship_autonomy_effect_tt`
- `decision_utopia_return_stewardship_effect_tt`
- `utopia_manifesto_cost_long_integration`
- `decision_utopia_begin_long_integration_effect_tt`
- `mission_utopia_long_integration_success_tt`
- `utopia_manifesto_cost_revolt_cleanup`
- `decision_utopia_clean_up_stewardship_revolt_effect_tt`
- `utopia_manifesto_cost_league_founding`
- `decision_utopia_initialize_league_effect_tt`
- `utopia_manifesto_cost_surplus_aid`
- `decision_utopia_send_surplus_abroad_effect_tt`
- `utopia_manifesto_cost_technical_mission`
- `decision_utopia_send_technical_mission_effect_tt`
- `mission_utopia_technical_mission_success_tt`
- `utopia_manifesto_cost_reserve_compact`
- `decision_utopia_open_reserve_compact_effect_tt`
- `mission_utopia_reserve_compact_answer_failure_tt`
- `utopia_manifesto_cost_league_invitation`
- `decision_utopia_invite_to_league_effect_tt`
- `mission_utopia_league_invitation_answer_failure_tt`
- `utopia_manifesto_cost_league_legitimacy`
- `decision_utopia_prove_league_not_mask_effect_tt`
- `mission_utopia_prove_league_not_mask_success_tt`
- `utopia_manifesto_cost_reconstruction_brigade`
- `decision_utopia_pool_reconstruction_brigades_effect_tt`
- `utopia_manifesto_cost_defense_council`
- `decision_utopia_call_mutual_defense_council_effect_tt`
- `decision_utopia_accept_league_sponsorship_effect_tt`
- `decision_utopia_expel_exploitative_member_effect_tt`
- `utopia_manifesto_cost_store_guard`
- `decision_utopia_guard_the_common_stores_effect_tt`
- `mission_utopia_guard_the_common_stores_outcome_tt`
- `decision_utopia_raise_a_citizen_watch_effect_tt`
- `mission_utopia_raise_a_citizen_watch_outcome_tt`
- `utopia_manifesto_cost_engineer_company_transport`
- `decision_utopia_form_engineer_companies_effect_tt`
- `mission_utopia_form_engineer_companies_outcome_tt`
- `utopia_manifesto_cost_auxiliary_contract`
- `decision_utopia_hire_auxiliary_contracts_effect_tt`
- `utopia_manifesto_cost_auxiliary_demobilization`
- `decision_utopia_end_the_auxiliary_contract_effect_tt`
- `mission_utopia_end_the_auxiliary_contract_outcome_tt`
- `utopia_manifesto_cost_constitutional_correction`
- `decision_utopia_open_constitutional_correction_effect_tt`
- `mission_utopia_constitutional_correction_failed_tt`
- `utopia_manifesto_cost_household_referendum`
- `decision_utopia_call_a_household_referendum_effect_tt`
- `utopia_manifesto_cost_calling_councils`
- `decision_utopia_convene_the_calling_councils_effect_tt`
- `utopia_manifesto_cost_new_forecast`
- `decision_utopia_request_a_new_forecast_effect_tt`
- `utopia_manifesto_cost_service_register`
- `decision_utopia_extend_the_service_register_effect_tt`
- `utopia_manifesto_cost_sunset_clause`
- `decision_utopia_add_a_sunset_clause_effect_tt`
- `utopia_manifesto_cost_corrected_tenure_tables`
- `decision_utopia_publish_corrected_tenure_tables_effect_tt`
- `utopia_manifesto_cost_district_appeals`
- `decision_utopia_negotiate_district_appeals_effect_tt`
- `utopia_manifesto_cost_formation_proof`
- `decision_utopia_prove_the_commonwealth_effect_tt`
- `mission_utopia_prove_the_commonwealth_outcome_tt`
- `utopia_manifesto_cost_commonwealth_proclamation`
- `decision_utopia_proclaim_the_commonwealth_effect_tt`
- `decision_utopia_integrate_post_formation_institutions_effect_tt`
- `decision_utopia_reinforce_post_formation_defense_effect_tt`
- `utopia_manifesto_cost_post_formation_charters`
- `decision_utopia_refresh_post_formation_charters_effect_tt`

## Simplifications, omissions, and blockers

- No stable non-decision localisation surface was simplified or omitted.
- Decision, mission, and additional category localisation remains incomplete by explicit ownership boundary. The exact inventory above is the only known localisation blocker from this tranche.
- No assets were created or changed.
- No spreadsheet or presentation alignment was performed.
- No Git staging or commit was performed.

## Skills used

- `chaos-redux-events` for event voice, key alignment, Event Details boundaries, evolution language, and handoff standards.
- `chaos-redux-super-events` for the accepted quotation package, route-specific super-event language, and slot preservation.

