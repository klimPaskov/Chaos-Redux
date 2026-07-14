# Event 015 Utopia Manifesto focus implementation handoff

## Ownership and outcome

This tranche owns only:

- common/national_focus/015_utopia_manifesto_focus_tree.txt
- common/ai_strategy/015_utopia_manifesto_ai_strategy.txt
- this handoff

The obsolete six-route tree was replaced with a 122-focus implementation of the accepted five-route design. It contains the opening survey, all political readings, all shared institution branches, all three island geographies including Inland Island, the five-way crisis correction, formation proof, and post-formation play. Every focus has an Event 015 icon and ai_will_do.

This handoff does not claim the Event 015 package complete. Localisation, decisions, ideas, helper internals, identity, assets, events, and shared wiring remain parent-owned.

## Focus coverage

| Surface | Count | Stable suffixes (all use utopia_manifesto_) |
| --- | ---: | --- |
| Opening survey | 8 | recover_the_manuscript; a_public_edition; count_houses_and_hands; the_first_common_store; agriculture_for_all; convene_the_interpretive_congress; an_interim_charter; the_country_as_a_question |
| Consent of Households | 10 | household_gives_consent; free_callings; municipal_charters; paid_public_lectures; transparent_store_accounts; independent_need_review; cooperative_land_trusts; constitution_of_provision; voluntary_commonwealth_league; commonwealth_by_consent |
| Common Table | 10 | nothing_private_in_necessity; councils_of_callings; the_common_table; social_workshops; council_property_transition; delegates_under_recall; congress_of_communes; council_autonomy; emergency_central_plan; union_of_tables |
| Guardians of Measure | 10 | country_measured; standard_houses; tables_of_need; board_of_measure; shortage_forecasting; cities_in_series; useful_freedom; exact_obedience; technical_missions; perfect_measure |
| Closed Island | 9 | one_island_one_measure; households_of_service; the_closed_store; penal_works; auxiliary_contracts; natural_right_of_need; assigned_colonies; cut_the_channel; perfect_island |
| The Joke Understood | 8 | read_island_as_a_mirror; institutions_that_can_be_left; a_mixed_commonwealth; sunset_clauses; satire_in_government; public_audit; reform_without_paradise; good_place_that_admits_its_limits |
| Callings and education | 7 | every_hand_knows_the_soil; schools_of_calling; work_where_needed; learn_a_second_trade; emergency_calling_review; six_hours_and_the_evening_lecture; a_nation_of_many_skills |
| Common stores | 7 | the_capital_store; regional_storehouses; useful_industry; rotate_old_stores; release_emergency_stores; two_years_against_hunger; surplus_beyond_the_shore |
| Garden and Island | 9 | homes_near_work; rail_road_and_common_ground; a_ring_of_social_cities; choose_the_island; the_existing_island; the_coastal_refuge; the_inland_island; build_the_island; the_island_made_real |
| Defense | 8 | the_citizen_watch; engineers_before_generals; a_small_army_well_housed; no_glory_in_the_field; foreign_hands_in_our_wars; necessary_victory; end_the_auxiliary_contract; commonwealth_defense_compact |
| Foreign Commonwealth | 7 | show_the_stores; offer_the_first_surplus; houses_across_borders; a_league_of_small_places; common_reserve_council; mutual_defense_without_mastery; the_regional_commonwealth |
| Necessary Ground | 8 | survey_what_we_lack; survey_domestic_alternatives; ask_before_we_demand; ground_held_in_trust; the_limit_of_need; the_natural_right; the_first_associate; a_commonwealth_of_places |
| Stewardship and status | 6 | stewardship_obligations; emergency_provision; restore_the_route; convene_the_local_charter; the_charter_period; status_by_consent |
| Crisis correction | 7 | the_founding_crisis; restore_consent; empower_the_councils; give_the_surveyors_authority; seal_the_island; admit_the_book_was_a_question; a_settled_interim_charter |
| Formation and mature play | 8 | proof_of_the_commonwealth; the_regional_proclamation; integrate_the_ring; the_second_generation; a_rule_for_need; beyond_the_founders_island; the_commonwealth_at_war; plenty_in_an_age_of_chaos |

## Stable helper contracts

### Four-value Ledger

Every completion reward initializes all four temporary inputs and calls the shared effect once:

- utopia_manifesto_need_delta
- utopia_manifesto_plenty_delta
- utopia_manifesto_concord_delta
- utopia_manifesto_assignment_delta
- utopia_manifesto_apply_prepared_ledger_delta = yes

The focus file uses only file-scoped magnitudes 0, 2, 4, and 7, with negative values for relief or movement toward Choice. The helper owns clamping and refresh.

### Routes and hidden reveal

The openers and crisis corrections call:

- utopia_manifesto_set_consent_of_households_route
- utopia_manifesto_set_common_table_route
- utopia_manifesto_set_guardians_of_measure_route
- utopia_manifesto_set_closed_island_route
- utopia_manifesto_set_joke_understood_route

The matching flags are utopia_manifesto_route_consent_of_households, utopia_manifesto_route_common_table, utopia_manifesto_route_guardians_of_measure, utopia_manifesto_route_closed_island, and utopia_manifesto_route_joke_understood.

The direct hidden opener and humanist crisis correction use utopia_manifesto_can_reveal_joke_understood. The tree supplies public_debate_proven, public_education_proven, criticism_permitted, exact_obedience_imposed, and penal_labour_used states. The trigger owns Choice, Concord, levy, unjustified-case, coercive-conduct, and route checks.

### Decision families and phase

The tree calls the seven unlock effects for calling, reserve, district, Necessary Ground, stewardship, League, and formation decisions. It prepares utopia_manifesto_decision_phase_input and calls utopia_manifesto_set_decision_phase. Inputs match the kernel: foundations 1, callings 2, reserves 3, Necessary Ground 5, League 6, formation 7. The kernel advances monotonically.

### Paid growth

The tree never grants free divisions or direct building levels. It uses:

- utopia_manifesto_can_pay_military_growth / utopia_manifesto_apply_paid_military_growth
- utopia_manifesto_can_pay_institutional_growth / utopia_manifesto_apply_paid_institutional_growth

Optional utopia_manifesto_growth_tier_input uses tier 1, 2, or 3. There are 26 institutional calls and 8 military calls.

### Geography

utopia_manifesto_prepare_island_variant sets exactly one of:

- utopia_manifesto_geography_existing_island
- utopia_manifesto_geography_coastal_island
- utopia_manifesto_geography_inland_island

Build the Island records utopia_manifesto_island_project_built. The trigger utopia_manifesto_island_project_proof_met checks capital, geography, and material/reserve proof. The Island Made Real then records utopia_manifesto_island_project_complete.

### Crisis and formation

The crisis branch calls utopia_manifesto_enter_constitutional_crisis and utopia_manifesto_resolve_constitutional_crisis.

Formation uses utopia_manifesto_refresh_formation_proof, utopia_manifesto_can_form_current_route, utopia_manifesto_unlock_formation_decisions, and utopia_manifesto_super_event_network_threshold_met. The formation effect owns utopia_manifesto_commonwealth_formed. The optional regional proclamation does not gate normal post-formation play.

## Additional trigger contracts

The focus and AI files consume these exact names, all present in the Event 015 kernel:

- utopia_manifesto_can_adopt_short_workday
- utopia_manifesto_can_secure_two_year_reserve
- utopia_manifesto_has_exportable_surplus
- utopia_manifesto_island_project_proof_met
- utopia_manifesto_has_valid_auxiliary_source
- utopia_manifesto_has_valid_escalation_case
- utopia_manifesto_has_eligible_league_partner
- utopia_manifesto_has_defense_compact_partner
- utopia_manifesto_can_take_coercive_need_fork
- utopia_manifesto_has_resolved_first_need_case
- utopia_manifesto_has_valid_associate_network
- utopia_manifesto_has_stewardship_obligation
- utopia_manifesto_stewardship_charter_period_met
- utopia_manifesto_stewardship_status_vote_ready
- utopia_manifesto_need_is_high
- utopia_manifesto_plenty_is_low
- utopia_manifesto_concord_is_low

## Proof ownership

Focuses record the five route capstones and domestic proof flags household_councils_proven, city_network_proven, separation_project_complete, defense_proof_complete, mixed_property_proven, and island_project_complete. They also record penal-labour, exact-obedience, Assigned Colony, and auxiliary conduct.

Actual relationship or case outcomes remain decision/mission-owned. Focuses do not grant these simply for opening a branch:

- utopia_manifesto_first_associate_recognized
- utopia_manifesto_small_places_compact
- utopia_manifesto_consensual_partner_proven
- utopia_manifesto_partner_autonomy_retained
- utopia_manifesto_false_cases_resolved
- utopia_manifesto_broad_recognition_proven
- utopia_manifesto_unjustified_enforced_case
- utopia_manifesto_coercive_conduct_used

The First Associate requires a real first_associate_recognized result. A League of Small Places grants only small_places_compact_framework. The Regional Commonwealth requires the configured regional threshold before recording its proof flag.

## Idea touchpoints

The tree references the accepted opening, route, final-route, common-store, garden-network, auxiliary-dependency, and stewardship-burden keys. Route setters/country-package integration must add or swap route-stage ideas so capstone final swaps have a source. The parent must audit the merged lifecycle against the three-simultaneous-spirit cap.

## AI package

common/ai_strategy/015_utopia_manifesto_ai_strategy.txt contains 12 country-generic, abortable strategies: opening restraint; five route behaviors; Closed Island escalation only with a valid case; low Plenty, high Need, and low Concord responses; crisis restraint; and mature commonwealth behavior. No strategy assumes a fixed country tag.

## Icons and localisation

The tree uses 72 unique GFX_goal_utopia_* sprites across 122 focuses. All 72 are registered in interface/015_utopia_manifesto.gfx and every texture exists under gfx/interface/goals/015_utopia_manifesto/.

Missing sprite identifiers required by this focus script: none.

The current Event 015 localisation has 0 matching titles and 0 matching descriptions. Localisation must add 122 keys equal to each focus ID and 122 keys using the focus ID plus _desc. No localisation file was edited because it was outside scope.

## Validation evidence

- 122 blocks, 122 unique IDs, 122 icons, and 122 ai_will_do blocks.
- Every focus prepares all four Ledger inputs and calls the helper exactly once.
- No unresolved prerequisites, non-descending parent links, coordinate collisions, or asymmetric exclusions.
- All 72 used sprite identifiers resolve to existing textures.
- All 42 scripted effect/trigger calls from the focus and AI files resolve in the current Event 015 kernel.
- Pacing is 18 short, 71 standard, and 33 long focuses.
- No Overreach, Vocation Balance, Foreign Suspicion, old route setters, free unit spawners, direct map-building rewards, or whole-world cadence remains.

## Simplifications, omissions, and blockers

No required focus route, shared branch, island variant, crisis choice, formation lane, or post-formation group was omitted.

Remaining integration work is explicit:

- 244 focus localisation keys are missing.
- Route/country-package effects must finish the three-spirit idea lifecycle.
- Decisions/missions must award relationship, case, stewardship, and recognition proof only from successful outcomes.
- Final package audits must verify the merged tree and rendered UI.

No fallback tree, placeholder branch, free military growth, or generic territorial reward was used.
