# Chaos Redux AI weights and probability audit

Audit date: 2026-08-21.

Audit status: incomplete as an engine-backed probability audit because the required HOI4 MCP probability and structural routes timed out and then closed their transport. The source inventory and static modifier trace are complete enough to identify candidate risks, but all conclusions that require native candidate enumeration, normalized probabilities, score races, timing distributions, or target resolution remain unresolved unless explicitly classified as score-only or source-only.

This is a fictional HOI4 script audit. It discusses only game-script identifiers and abstract game-state scenarios and does not discuss real-world procedures.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, scripted effect, scripted trigger, localization, documentation/specification, asset, spreadsheet, runtime, or other repository file was edited. The only permitted write is this handoff file. No staging, reverting, or commit was performed.

## Scope and result classifications

The inspected identifier families were cbrn_, chem_, bio_, chemical_, biological_, condemnation_, and chaos_warfare_. The weighted surfaces in scope were ai_will_do, ai_chance, MTTH, AI strategy factors, research selection, production choice, target weights, doctrine selection, special-project selection, native raid choice weights, and nested random-list selection where those surfaces were owned by the inspected families.

The only analyzed scenario ids requested by the parent were prepared_route, unprepared_route, defensive_route, no_valid_target, low_stock, high_penalty, special_excluded_tag, and mastery_route. Those are the only scenario ids used in this report.

Result classifications used below:

- Exact means the MCP adapter returned a complete candidate pool and an engine trace for the named scenario.
- Bounded means the MCP adapter returned a proven interval or threshold range with a complete declared pool.
- Sampled means probability_simulate returned seeded samples from explicitly declared uncertain inputs.
- Score-only means the source exposes a static ai_will_do, ai_chance base/factor, weight, or factor trace, but no native selection probability or timing result was returned.
- Unresolved means the candidate pool, external factors, adapter route, or MCP result is incomplete, unavailable, or unsupported.

There are no exact, bounded, or sampled probability results in this handoff. No exact selection probability is stated for any incomplete pool.

## Required references consulted

The complete repository instructions in AGENTS.md were read before source inspection.

The complete repository skills .agents\skills\chaos-redux-subagents\SKILL.md and .agents\skills\chaos-redux-mtth\SKILL.md were read and applied. The audit remained read-only as required by the parent.

The complete parent-named specification files were read:

- docs\specs\chaos_warfare_system_specs\handoffs\implementation_surface_map.md
- docs\specs\chaos_warfare_system_specs\matrices\ai_behavior_matrix.md

The required offline Paradox wiki snapshot pages consulted under paradox_wiki\ were Data structures - Hearts of Iron 4 Wiki.md, Triggers - Hearts of Iron 4 Wiki.md, Effects - Hearts of Iron 4 Wiki.md, Modifiers - Hearts of Iron 4 Wiki.md, Localisation - Hearts of Iron 4 Wiki.md, Scopes - Hearts of Iron 4 Wiki.md, On actions - Hearts of Iron 4 Wiki.md, Event modding - Hearts of Iron 4 Wiki.md, Decision modding - Hearts of Iron 4 Wiki.md, Idea modding - Hearts of Iron 4 Wiki.md, AI modding - Hearts of Iron 4 Wiki.md, Doctrine modding - Hearts of Iron 4 Wiki.md, Technology modding - Hearts of Iron 4 Wiki.md, Equipment modding - Hearts of Iron 4 Wiki.md, and Division modding - Hearts of Iron 4 Wiki.md.

The relevant installed vanilla documentation consulted under C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\ was script_concept_documentation.md, effects_documentation.md, triggers_documentation.md, modifiers_documentation.md, dynamic_variables_documentation.md, and script_collection_operator.md. The documentation confirms that script constants are injected values with field-specific support, that ai_will_do is a score race, that ai_chance is a probability-proportional event-option surface, and that MTTH starts from a base and applies factors.

## HOI4 MCP evidence and blockers

The required read-only MCP workflow was attempted before treating source inspection as evidence. The installed probability schema was also inspected so the source object used a valid path/identifier/inlineClausewitz shape rather than silently substituting a source-only audit.

| Required route | Adapter/source attempted | Result |
| --- | --- | --- |
| hoi4.probability_inspect | ai_strategy_factor with common\ai_strategy\cbrn_country_profiles.txt | The first attempt with source.relativePath was rejected with the exact schema error Unrecognized key: "relativePath" at source. A string source was rejected with expected object, received string at source. |
| hoi4.probability_inspect | ai_strategy_factor with source.path common\ai_strategy\cbrn_country_profiles.txt, source.identifier cbrn_ai_profile_britain_research, and an inlineClausewitz probe | Each schema-valid form ran until the exact error tool call failed for hoi4_agent_tools/hoi4.probability_inspect Caused by: timed out awaiting tools/call after 180s. Subsequent inspect calls returned the exact error tool call failed for hoi4_agent_tools/hoi4.probability_inspect Caused by: Transport closed. |
| hoi4.probability_evaluate | decision_ai_will_do with common\decisions\cbrn_battlefield_operation_decisions.txt and the four local battlefield choices | The call returned the exact error tool call failed for hoi4_agent_tools/hoi4.probability_evaluate Caused by: Transport closed. No score trace, ranking, candidate validity, or scenario hash was returned. |
| hoi4.probability_sweep | ai_strategy_factor with common\ai_strategy\chemical_warfare_livens.txt and sensitivity paths for enemy use, route gate, and original tag | The call returned the exact error tool call failed for hoi4_agent_tools/hoi4.probability_sweep Caused by: Transport closed. No threshold, sensitivity, rank-reversal, or scenario hash was returned. |
| hoi4.event_inspect | file selector with sourcePath events\cbrn_protection_events.txt | Selector probing established that the required field is selector.sourcePath, but the schema-valid inspection returned the exact error Transport closed. No event analysis id or structural artifact was returned. |
| hoi4.event_render | Not advanced after event inspection failed | No analysis id or revision existed to render, so no event-render artifact was available. |
| hoi4.focus_inspect and hoi4.focus_render | Not advanced after the transport closed | No focus analysis id or revision existed to render. |
| hoi4.tech_inspect and hoi4.tech_render | Not advanced after the transport closed | No technology/doctrine analysis id or revision existed to render. |
| hoi4.probability_render | Not advanced after inspect/evaluate/sweep failed | No analysis id, scenario hash, ranking, matrix, timing, sensitivity, or unresolved-view artifact existed to render. |

The probability tool advertised adapters event_mean_time_to_happen, event_option_ai_chance, decision_ai_will_do, mission_ai_will_do, national_focus_ai_will_do, technology_ai_will_do, doctrine_ai_will_do, direct_random, random_list, ai_strategy_factor, and custom_weighted_pool. The transport failure prevented a successful inspect for each affected adapter after the initial ai_strategy_factor route failed. The tool set did not advertise a dedicated operation_ai_will_do, raid target-weight, MIO selection, equipment-module selection, or native target-pool adapter, so those surfaces are additionally unresolved rather than silently mapped to an unrelated adapter.

No MCP artifact URI, revision, scenario hash, comparison id, analysis id, or rendered evidence path/URI was produced. This is an MCP availability blocker, not evidence that the weights are balanced.

hoi4.probability_compare was correctly not used because the parent supplied no source patch and requested comparison only for an actual before/after or candidate comparison. hoi4.probability_simulate was not used because no uncertain input distribution and seed were declared. hoi4.probability_sequence was not used because no complete custom-pool manifest with cadence, state transitions, cooldown, recovery, cap, removal, reset, timers, and terminal states was available. These are deliberate skips, not missing evidence.

## Audited weighted surfaces and exact source inventory

### AI strategy factors, research, and production

The central strategy-factor sources were:

- common\ai_strategy\cbrn_country_profiles.txt, containing cbrn_ai_profile_britain_research, cbrn_ai_profile_france_research, cbrn_ai_profile_germany_research, cbrn_ai_profile_soviet_research, cbrn_ai_profile_usa_research, cbrn_ai_profile_italy_research, cbrn_ai_profile_japan_research, cbrn_ai_profile_commonwealth_research, cbrn_ai_profile_frontier_research, cbrn_ai_profile_scandinavian_research, cbrn_ai_profile_chinese_research, cbrn_ai_profile_limited_research, the corresponding *_support_production blocks, and the corresponding *_regimental_roles blocks.
- common\ai_strategy\cbrn_protection_production.txt, containing cbrn_mask_production_base, cbrn_mask_production_mass_civil_profile, cbrn_mask_production_prepared_profile, cbrn_mask_production_military_first_profile, cbrn_mask_production_industrial_profile, cbrn_mask_production_civil_network_profile, cbrn_mask_production_exposed_profile, cbrn_mask_production_limited_profile, cbrn_mask_production_urgent, and the cbrn_mask_production_10_to_24, cbrn_mask_production_25_to_49, cbrn_mask_production_50_to_74, cbrn_mask_production_75_to_99, and cbrn_mask_production_100_plus factory bands.
- common\ai_strategy\cbrn_regimental_support.txt, containing cbrn_ai_protected_formation_ratio, cbrn_ai_chemical_assault_ratio, cbrn_ai_chemical_artillery_ratio, cbrn_ai_armored_assault_ratio, cbrn_ai_containment_formation_ratio, cbrn_ai_decontamination_equipment_production, cbrn_ai_instrument_equipment_production, cbrn_ai_urgent_decontamination_equipment_production, and cbrn_ai_urgent_instrument_equipment_production.
- common\ai_strategy\chemical_warfare_research.txt, containing cbrn_research_protective_foundation, cbrn_research_known_chemical_threat, cbrn_research_chemical_emergency, cbrn_research_force_protection, cbrn_research_force_protection_upgrade, cbrn_research_lewisite_countermeasure, cbrn_research_biological_emergency, cbrn_research_british_retaliatory_agents, cbrn_research_french_artillery_agents, cbrn_research_german_nerve_agents, cbrn_research_soviet_artillery_agents, cbrn_research_american_lewisite_agents, cbrn_research_italian_battlefield_agents, cbrn_research_japanese_theater_agents, and cbrn_research_generic_authorized_agents.
- common\ai_strategy\chemical_warfare_livens.txt, containing chem_livens_research_major_base, chem_livens_research_major_threat, chem_livens_research_major_force, chem_livens_research_upgrade_weights, chem_livens_research_upgrade_force, chem_livens_research_japan_bonus, chem_livens_production_major_base, chem_livens_production_major_threat_low, chem_livens_production_major_threat_med, chem_livens_production_japan_bonus, chem_livens_production_china_bonus, chem_livens_template_design_focus, and chem_livens_template_design_japan_focus.
- common\ai_strategy\chemical_warfare_cylinders.txt, containing cbrn_payload_pressure_retaliatory, cbrn_payload_pressure_battlefield, cbrn_payload_pressure_strategic, cbrn_payload_pressure_desperate, the country-specific cbrn_payload_*_reserve blocks, the generic strategic and battlefield payload reserve blocks, cbrn_shell_lot_battlefield_production, and cbrn_shell_lot_strategic_production.
- common\ai_strategy\chemical_warfare_tank_shells.txt, containing chem_tank_shell_production_major_base, chem_tank_shell_production_major_threat_low, chem_tank_shell_production_major_threat_med, chem_tank_template_design_focus, chem_tank_production_japan_bonus, and chem_tank_template_design_japan_focus.
- common\ai_strategy\biological_warfare_production.txt, containing cbrn_bio_tularemia_payload_safe, cbrn_bio_anthrax_payload_safe, cbrn_bio_plague_payload_safe, cbrn_bio_smallpox_payload_safe, cbrn_bio_japan_china_anthrax, cbrn_bio_japan_china_plague, cbrn_bio_smallpox_payload_desperate, cbrn_bio_plague_payload_desperate, cbrn_bio_anthrax_payload_desperate, and cbrn_bio_tularemia_payload_desperate.

The source constants include country profile research values of defensive90, medical120, field_response110, artillery85, delivery75, biological95, and biological_japan125; production profile values of defensive30, medical40, field_response35, and biological_response45; role ratios of protected6, assault2, artillery1, armored1, and containment2; and support production factors of decontamination25 and instruments20 with urgent variants40. These are strategy scores or factor contributions, not click probabilities.

The protection production file uses mask production factors base50, mass_civil40, prepared30, military_first25, industrial35, civil_network30, exposed15, limited5, and urgent70. Its factory bands use one factory for 10 to 24 military factories, two for 25 to 49, four for 50 to 74, six for 75 to 99, and eight at 100 or more, with cbrn_country_should_produce_masks as the common gate.

The chemical research strategy constants are foundation15, known_threat60, emergency150, force100, agent_primary80, secondary40, and countermeasure120. The research blocks add those factors to basic_gas_masks, improved_gas_masks, advanced_gas_masks, field_decontamination_kits, chemical_detection_paper, portable_anemometer, military_filter_standardization, rapid_filter_replacement, mobile_wash_columns, mobile_sampling_laboratories, mobile_cbrn_hospitals, meteorological_stations, dimercaprol, pathogen_handling_protocols, sealed_containment_laboratories, and field_epidemiology_teams under their stated gates.

The Livens research factors are base25, enemy-use threat100, force research_tech100, upgrade factors25, and Japan40. Its production factors are base1, threat_low2, threat_med3, Japan2, and China2. The tank-shell production factors are base1, threat_low2, threat_med3, Japan1, and template experience30 with Japan30. The chemical cylinder pressure factors are retaliatory20, battlefield50, strategic80, and desperate100, with shell pressure40, strategic shell70, and payload reserve additions of 4, 7, 10, or 14 depending on route.

The biological production factors are battlefield1, retaliatory1, strategic3, severe2, Japan anthrax1, Japan plague2, and desperate5, with stockpile thresholds of 120, 160, 300, 180, 220, 300, and 400 for the corresponding blocks.

### Decisions, missions, and target-weighted choices

The principal decision files were:

- common\decisions\cbrn_battlefield_operation_decisions.txt with cbrn_battlefield_cycle_agent, cbrn_battlefield_cylinder_release, cbrn_battlefield_projector_barrage, cbrn_battlefield_artillery_fire_plan, and cbrn_battlefield_armored_delivery.
- common\decisions\cbrn_protection_decisions.txt with cbrn_establish_national_respirator_reserve, cbrn_register_and_fit_population, cbrn_issue_masks_to_field_army, cbrn_replace_military_mask_filters, cbrn_recondition_old_masks, cbrn_convert_civilian_mask_industry, cbrn_simplify_filters_for_mass_issue, cbrn_export_protective_equipment, cbrn_import_protective_equipment, cbrn_license_foreign_respirator_design, cbrn_priority_state_mask_issue, cbrn_full_state_mask_distribution, cbrn_emergency_state_mask_distribution, cbrn_replace_state_mask_filters, cbrn_supply_occupied_population, cbrn_protect_hospitals_and_utilities, cbrn_move_civilians_to_shelters, cbrn_sound_chemical_alarm, and cbrn_keep_industry_operating.
- common\decisions\cbrn_doctrine_decisions.txt with cbrn_convene_institutional_review, cbrn_chaos_warfare_establishment_mission, cbrn_complete_delayed_establishment, cbrn_begin_hazard_assault_training, cbrn_hazard_assault_training_mission, cbrn_assign_decontamination_corridor, cbrn_claim_protective_foundation, cbrn_claim_delivery_integration, cbrn_claim_theater_exploitation, cbrn_claim_terminal_command, cbrn_set_defensive_preparation_policy, cbrn_set_retaliation_authority_policy, cbrn_set_limited_battlefield_policy, cbrn_set_strategic_release_policy, cbrn_set_unrestricted_policy, cbrn_commission_sealed_tank_crews, cbrn_commission_persistent_agent_shell_filling, cbrn_commission_nerve_suppression, and cbrn_commission_biological_security_assault.
- common\decisions\cbrn_occupation_decisions.txt with cbrn_authorize_coercive_security, cbrn_adopt_protected_occupation, cbrn_nerve_suppression_sarin, cbrn_nerve_suppression_soman, cbrn_deploy_protective_aid, cbrn_seal_state, cbrn_destroy_contaminated_records, cbrn_admit_accidental_release, and cbrn_permit_inspection.
- common\decisions\cbrn_diplomacy_decisions.txt with cbrn_demand_inspections, cbrn_share_forensic_evidence, and cbrn_sponsor_decontamination_mission.
- common\decisions\biological_sabotage_decisions.txt with the twelve bio_sabotage_anthrax_base, bio_sabotage_anthrax_theater, bio_sabotage_anthrax_terminal, bio_sabotage_plague_base, bio_sabotage_plague_theater, bio_sabotage_plague_terminal, bio_sabotage_tularemia_base, bio_sabotage_tularemia_theater, bio_sabotage_tularemia_terminal, bio_sabotage_smallpox_base, bio_sabotage_smallpox_theater, and bio_sabotage_smallpox_terminal choices.
- common\decisions\biological_raid_staging_decisions.txt with bio_designate_strategic_raid_staging_state.
- common\decisions\biological_stockpile_safety_decisions.txt with bio_designate_national_biological_arsenal.
- common\decisions\chemical_warfare_decisions.txt with the chemical doomsday decision and bio_unleash_stockpiled_pathogens.
- common\decisions\condemnation_sanctions_decisions.txt with the condemnation and sanction response choices that use condemnation_sanctions_constants.

The battlefield-operation source gives base scores cylinder .85, projector1.10, artillery1.40, and armored1.20, with route, retaliation, first-use, contamination, conventional-deficit, losing-war, and country-profile factors. It also has source-level target-state validity, visibility, availability, cooldown, cancellation, and cleanup logic. The four local operation choices are a complete local choice pool only if the category adapter excludes every other decision and every target instance is supplied; neither condition was proven by MCP.

The protection decisions use base scores of 1 for reserve, population registration, filter replacement, reconditioning, conversion, simplified filters, export, import, licensing, state targeting, state distribution, occupied supply, and several response choices; 2 for field issue and military filter replacement; and 8 for emergency state distribution and several emergency response choices. Static factor traces include major1.50, at_war1.50, enemy4, mass_civil3, prepared2, alert5, contamination3, low_stock3, frontline_shortage4, capital3, high_population2, industrial_state2, export_surplus1.50, export_shortage0, military_first_civilian.55, home_shortage.35, and field_shortage_civilian.10.

The doctrine decisions use base1000 for cbrn_convene_institutional_review, 20 for cbrn_complete_delayed_establishment, 8 for cbrn_begin_hazard_assault_training, 40 for cbrn_assign_decontamination_corridor, and 100 for milestone claims. Policy bases are 8 for defensive preparation, 4 for retaliation authority, and 0 for limited battlefield, strategic release, and unrestricted policy, with route-specific additions of 20, 40, and terminal40 plus zero factors for unavailable or nonhuman states.

The biological sabotage choices use agent bases anthrax1, plague1, tularemia.85, and smallpox1, then apply disabled0, retaliation4, first-use2, unrestricted2.50, desperate3, defensive.20, prepared1.50, theater1.25, terminal1.50, target factors, Japan-China4, active outbreak.10, sanction and import-vulnerability factors, and target validity through bio_sabotage_*_target_state and bio_sabotage_actor_can_operate. The theater and terminal variants contain unconditional route multiplier blocks, which is a static dominance concern if the surrounding choice identity does not itself enforce route exclusivity.

The occupation choices use base scores coercive25, protected80, sarin20, soman30, protective aid40, seal20, destroy10, admit15, and inspection25, with own-core, allied-core, trauma, defensive, democratic, first-use, unrestricted, and condemnation factors. Target and agreement validity are source-gated, but no target-weight MCP trace was available.

### Events, ai_chance, random lists, and MTTH

events\cbrn_protection_events.txt contains cbrn_protection.2 with the sole option cbrn_protection.2.a and ai_chance base constant:cbrn_math.percent_divisor. Its local option pool is complete at one candidate, but the exact runtime interpretation of the percent divisor was not confirmed by the failed event/probability adapter.

events\chemical_warfare_events.txt contains chaosx_contamination.9 with the local two-option pool chaosx_contamination.9.a and chaosx_contamination.9.b. The accept option uses air_cleanliness_treaty_lifecycle_ai.join_base = 1, with democratic3, minor without stock2.5, stockpile.55, used unconventional0, war with founder.7, and major.75 factors. The decline option uses decline_base = 1 with no listed modifiers. The local pool is complete, but event targets, flags, treaty state, stockpile state, and the event engine’s final option normalization were not returned by MCP.

events\biological_stockpile_safety_events.txt contains cbrn_bio_safety.1, scheduled at a 30-day interval after its initial delay, and an outer random_list between bio_stockpile_safety_monitor_no_incident_weight and bio_stockpile_safety_monitor_incident_weight. common\scripted_effects\biological_stockpile_safety_effects.txt selects from the four accident agents anthrax, plague, tularemia, and smallpox, then from five incident severities contained, lab_contamination, local_outbreak, major_domestic_outbreak, and international_exposure.

common\scripted_effects\biological_stockpile_safety_effects.txt statically prepares outer weights controlled1/9999, strained1/199, dangerous4/96, and critical15/85 for incident/no-incident. Severity weights are controlled 100/2/0/0/0, strained70/25/5/0/0, dangerous15/30/35/18/2, and critical2/8/25/40/25 in the five severity order above. Agent choices are zeroed when the respective stockpile accident cooldown is active, and the cooldown constant is 730 days. The local candidate lists are complete, but the dynamic risk band, cooldown flags, live stockpile availability, and nested state transitions were not complete scenario inputs. No sequence timing result is therefore claimed.

No direct MTTH entry with an identifier beginning cbrn_, chem_, chemical_, bio_, biological_, condemnation_, or chaos_warfare_ was found in the inspected source. The adjacent common\mtth\chaosx_mtth_variables.txt entry zombie_outbreak_chance is used by the broader biological prevention surface and has base and modifier tiers for outbreak state, hygiene, migration, quarantine, borders, postwar vigilance, bio outbreak prevention, population, research slots, factories, rear/front proximity, island status, major status, state count, and zombie collapse. events\002_zombie_outbreak.txt contains the corresponding MTTH blocks. This adjacent timing surface is source-only and unresolved because the event_mean_time_to_happen adapter did not return an analysis.

### Raids and operations

common\raids\cbrn_chemical_air_raids.txt contains eleven native raid choices with ai_will_do: chemical_chlorine_strike, chemical_phosgene_strike, chemical_mustard_strike, chemical_lewisite_strike, chemical_tabun_strike, chemical_sarin_strike, chemical_soman_strike, chemical_malodor_strike, chemical_aphrodisiac_strike, chemical_sarin_rocket_strike, and chemical_soman_rocket_strike. Each has base1 and source factors for cbrn_chemical_air_raid_ai_may_target_from, treaty membership, retaliation, aggressive profile, desperate profile, target major status, dense state population, and supply hub presence. Native visible, available, launchable, target-type, agent-tech, rack, bomber, payload, and airbase triggers are separate validity gates.

common\raids\biological_raids.txt contains four strategic choices anthrax_strike, plague_strike, tularemia_strike, and smallpox_strike, each with bio strategic base1 and factors for target validity, treaty state, retaliation, first use, unrestricted route, desperate persistence, defensive/prepared route, shared border, surveillance, rapid response, integrated control, major target, density, capital, industry, active outbreak, condemnation, import vulnerability, and sanction state.

common\raids\biological_battlefield_raids.txt contains four battlefield choices anthrax_battlefield_dissemination, plague_battlefield_dissemination, tularemia_battlefield_dissemination, and smallpox_battlefield_dissemination, with bases 1, .60, 1.50, and .40 and factors for target validity, treaty, retaliation, first use, unrestricted route, desperation, losing state, defensive/prepared route, supply hub, fortified and concentrated target state, active outbreak, and sanctions.

common\raids\biological_facility_recovery_raids.txt contains bio_facility_secure_preserve_raid and bio_facility_destroy_safely_raid, while common\raids\biological_zombie_cure_raid.txt contains zombie_cure_strike as an adjacent biological choice. Their target validity and recovery gates were inspected but no target-pool adapter returned a result.

common\operations\chaosx_bioweapon_operations.txt contains bioweapon_plant_outbreak_anthrax, bioweapon_plant_outbreak_plague, bioweapon_plant_outbreak_tularemia, bioweapon_plant_outbreak_smallpox, and bioweapon_plant_outbreak_zombie. Their operation ai_will_do bases are anthrax1, plague1, tularemia.85, smallpox1, and zombie.5, with the same route, target, sanction, and persistence families as the raid choices. The installed MCP tool set has no operation_ai_will_do adapter, so these are unresolved source-only scores.

### Technology, doctrine, special projects, abilities, templates, and other adjacent weighted surfaces

The technology sources were common\technologies\chaosx_technologies.txt, common\technologies\cbrn_regimental_support_technologies.txt, common\technologies\cbrn_hq_technologies.txt, and common\technologies\cbrn_aerosol_module_variant_technologies.txt. AI-enabled research choices include protection, detection, meteorological, decontamination, sampling, hospital, and field-epidemiology technologies with bases .75, 1.25, or 1 and factors for emergency4, shortage3, contamination4, program1.75, doctrine1.50, mass civil2.50, prepared2, military-first3, and limited/minimal .60. Doctrine-only or special-project-only technologies have explicit ai_will_do factor0, including chaos_battalion_tech, chaos_battalion_tech_1939, chaos_battalion_tech_1942, chemical_artillery_shells, persistent_agent_shell_filling, armored_agent_delivery, sealed_tank_crews, nerve_agent_suppression_formation, biological_security_assault_formation, mobile_decontamination_columns, chemical_air_interdiction, theater_cbrn_headquarters, and the delivery technology identifiers anthrax_bomb_delivery_systems, plague_bomb_delivery_systems, tularemia_bomb_delivery_systems, and smallpox_bomb_delivery_systems. The aerosol module variants have allow = always no and no independent AI score. Whether the native technology candidate pool excludes every locked entry before applying strategy contributions was not proven.

The doctrine sources were common\doctrines\grand_doctrines\chaos_warfare_grand_doctrine.txt and the land subdoctrines common\doctrines\subdoctrines\land\chaos_warfare_infantry_subdoctrines.txt, common\doctrines\subdoctrines\land\chaos_warfare_armor_subdoctrines.txt, common\doctrines\subdoctrines\land\chaos_warfare_combat_support_subdoctrines.txt, and common\doctrines\subdoctrines\land\chaos_warfare_operations_subdoctrines.txt. The grand-doctrine score has base.20, viable-program4, prepared2, military2.50, industrial1.75, enemy3, war1.50, ordinary-democratic.25, minimal.15, and nonhuman0. The subdoctrine choices use base1, unavailable0, committed2, and mastery multipliers ranging from 12 to 16, with cbrn_profile_is_prepared_power, cbrn_profile_is_military_first, cbrn_profile_is_industrial_reserve, and other route gates. These are ai_will_do scores and are not normalized selection probabilities.

common\special_projects\projects\biowarfare_main_projects.txt contains anthrax_bomb, plague_bomb, tularemia_bomb, and smallpox_bomb, with project AI bases anthrax3, plague4, tularemia2, and smallpox2, disabled0, route-specific enable factors, Japan factors, and desperate smallpox4. zombie_cure_bomb is adjacent. common\special_projects\projects\chemical_special_projects.txt contains sp_cw_malodor_bomb_program and sp_cw_aphrodisiac_bomb_program. common\special_projects\projects\chemical_warfare_nerve_projects.txt contains sp_cw_sarin_program and sp_cw_soman_program. common\special_projects\projects\japan_ishii_projects.txt contains sp_japan_pingfang_records_office, sp_japan_kwantung_medical_intelligence, sp_japan_occupation_test_ledger, sp_japan_epidemic_mapping_bureau, and sp_japan_cherry_blossom_dossier. The generic chemical and biological prototype reward files contain their respective reward choice pools with base2 and repeat.25 for most rewards and lower resource/failure/interference weights.

common\abilities\chemical_abilities.txt and common\abilities\cbrn_hq_abilities.txt contain ability-level ai_will_do or priority surfaces. common\ai_templates\cbrn_regimental_support.txt and common\ai_templates\cbrn_hq_support.txt contain unit-template role and priority weights. common\military_industrial_organization\organizations\cbrn_protection_biological_organizations.txt and common\military_industrial_organization\organizations\cbrn_organizations.txt contain MIO ai_will_do surfaces. common\units\equipment\modules\chemical_air_bomb_variant_modules.txt, common\units\equipment\modules\chemical_air_bomb_modules.txt, common\units\equipment\cylinders.txt, common\units\equipment\cbrn_protective_equipment.txt, and common\units\equipment\cbrn_payload_equipment.txt contain equipment/module weight or priority fields. The installed MCP adapters did not expose native ability, template, MIO, equipment-module, or target-pool analyzers, so these are inventoried as unsupported or unresolved rather than converted into probabilities.

The implementation surface map names common\ai_strategy\cbrn_warfare_ai.txt as a recommended strategy path, but that file does not exist in the current repository. The actual strategy logic is split among the eight strategy files listed above. This source/spec mismatch should be reconciled by the owner; it was not edited.

## Candidate-pool and external-factor completeness

The following table records the pool discipline used for every weighted family. Complete means complete only for the explicitly stated local choice set, not complete for the native engine unless the engine candidate enumeration was returned.

| Surface | Declared candidate pool | External factors required | Completeness and classification |
| --- | --- | --- | --- |
| Battlefield decision ai_will_do | cbrn_battlefield_cylinder_release, cbrn_battlefield_projector_barrage, cbrn_battlefield_artillery_fire_plan, cbrn_battlefield_armored_delivery | Stable protective base, route, terminal doctrine, retaliation, first use, contamination, conventional deficit, losing state, target state, target validity, cooldown, costs, and all other decisions in the category | Four local choices complete only for the named source category; native category and target instances were not returned. Score-only and unresolved. |
| Protection, doctrine, occupation, diplomacy, sabotage, and staging decisions | The exact identifiers listed in the decision inventory above | Country profile, route flags, ideas, war state, stock, factories, target arrays, costs, prerequisites, cooldowns, agreements, condemnation, import vulnerability, and every competing decision | Incomplete native candidate pools and external state. Static score-only; exact probability unresolved. |
| Event cbrn_protection.2 | Sole option cbrn_protection.2.a | Trigger source, event scope, and engine interpretation of cbrn_math.percent_divisor | Local pool complete; external engine trace unavailable. Score-only/unresolved. |
| Event chaosx_contamination.9 | chaosx_contamination.9.a and chaosx_contamination.9.b | Founder relation, democratic status, faction status, major status, stockpile state, unconventional-use flag, treaty state, event scope | Local pool complete; external state incomplete. Normalized ai_chance unresolved. |
| Stockpile safety outer random_list | no-incident and incident branches | Risk band, monitor variables, schedule, and live safety state | Two local branches complete; external state incomplete. Static weights only. |
| Stockpile safety agent random_list | anthrax, plague, tularemia, smallpox | Stockpile presence, agent cooldown flags, prepared agent weights, and total-positive condition | Four local candidates complete; live availability incomplete. Static weights only. |
| Stockpile safety severity random_list | contained, lab_contamination, local_outbreak, major_domestic_outbreak, international_exposure | Risk band and severity helper state | Five local candidates complete; live risk state incomplete. Static weights only. |
| Chemical air raids | Eleven chemical raid identifiers listed above | Agent tech, rack, target type, target validity, bomber and payload state, treaty, route, major/density/hub target state, and all native raid candidates | Eleven local choices complete; target pool and native validity incomplete. Score-only/unresolved. |
| Strategic biological raids | anthrax_strike, plague_strike, tularemia_strike, smallpox_strike | Strategic target validity, airbase/equipment, treaty, route, surveillance, response, target density/industry/capital, sanctions, condemnation, import vulnerability | Four local choices complete; target pool incomplete. Score-only/unresolved. |
| Biological battlefield raids | anthrax_battlefield_dissemination, plague_battlefield_dissemination, tularemia_battlefield_dissemination, smallpox_battlefield_dissemination | Battlefield target validity, airbase/equipment, cooldown, supply hub, fortification/concentration, treaty, route, sanctions | Four local choices complete; target pool incomplete. Score-only/unresolved. |
| Operation ai_will_do | Five bioweapon_plant_outbreak operation identifiers | Operation target state, route, preparation, phase state, persistence, sanctions, cooldown, and all competing operations | Adapter unsupported. Source-only and unresolved. |
| Research selection | Native research candidates plus cbrn_ai_profile_*_research and chemical_warfare_research contributions | Research slots, prerequisites, availability, ahead-of-time penalties, doctrine/program state, enemy capability, war, contamination, outbreak, and all non-CBRN research candidates | Incomplete native pool. Strategy factors are score-only; selection probability and timing unresolved. |
| Production choice | Native equipment lines plus mask, support, payload, shell, Livens, and tank-shell factor blocks | Equipment unlocks, archetype validity, factories, production law, resources, stockpile, profile, route, and all competing production lines | Incomplete native pool. Score-only/unresolved. |
| Doctrine selection | Chaos Warfare grand and land subdoctrine choices | Doctrine availability, XP, committed/unavailable state, mastery, route, profile, and all competing doctrines | Local source factors complete; native candidate pool and structural MCP result unavailable. Score-only/unresolved. |
| Special-project selection and rewards | Bio projects, chemical projects, Japan projects, generic chemical rewards, and generic bio rewards listed above | Project visibility, facility, specialization, prerequisite, scientist, repeat state, reward pool membership, route, and terminal state | Native project/reward pool incomplete. Score-only/unresolved. |
| MTTH | No direct prefixed CBRN MTTH; adjacent zombie_outbreak_chance | Full event trigger scope, MTTH base, all modifiers, schedule, and event chain state | No direct in-scope entry; adjacent surface unresolved. |
| Target weights | Target-state factors embedded in decision, raid, sabotage, occupation, diplomacy, and operation scripts | Complete target list, own/faction/subject exclusions, route validity, target state, treaty, condemnation, import vulnerability, supply, and hidden native filters | No target-weight adapter was available. Unresolved. |

## Static base values, modifier traces, and findings

### Score versus probability and timing

The ai_will_do and AI strategy values above are willingness or priority scores. They may affect a highest-score race, a randomized AI choice within a score range, or a strategy-factor multiplication depending on the native consumer, but they are not click probabilities.

The event ai_chance values are the only directly probability-bearing choice surface found in the inspected event files. The two-option chaosx_contamination.9 pool is locally complete, but its normalized probability remains unresolved because the MCP event/probability trace failed and external state was not supplied.

The stockpile safety random_list weights are probability-proportional at the random-list consumer, but their timing is controlled by a scheduled monitor and cooldown state. The 30-day monitor cadence and 730-day agent cooldown are source facts, not an engine-derived timing distribution.

The adjacent zombie_outbreak_chance MTTH is a timing surface, not a selection race. Its base and modifiers were source-inspected but no MTTH engine trace or timing distribution was returned.

### Validity and impossible-choice findings

No source-only finding can prove that a positive candidate is impossible in the native engine because the MCP candidate-validity route failed. The following gates are visible in source and should be validated with a successful adapter:

- Battlefield decisions use cbrn_battlefield_*_target_state, stable protective-base checks, target visibility/availability, cooldowns, and cleanup effects, which is consistent with the no_valid_target failsafe but not engine-proven.
- Biological sabotage, strategic biological raids, battlefield biological raids, chemical air raids, and occupation choices use target validity, target-type, agreement, route, airbase, essential-equipment, and cooldown checks in separate triggers.
- Biological safe-production blocks exclude nonhuman countries, desperate states, Japan-specific paths, excluded agent combinations, and unsafe containment routes, while desperate blocks have their own strongest-tech exclusions.
- Doctrine-only and special-project-only technology identifiers have factor0 or allow = always no, but the native research adapter must prove that locked candidates are removed before any external strategy contribution is considered.

The most important unresolved validity risk is positive base ai_will_do on a choice whose source-level target gate is not part of the same score block. A successful target-aware MCP evaluation is required for no_valid_target, special_excluded_tag, and defensive_route before declaring the failsafes safe.

### Dominance, starvation, and rank-reversal findings

The following are source-backed risks, not engine-proven rankings:

- chem_livens_production_major_threat_low and chem_livens_production_major_threat_med use the same has_enemy_used_chemical_weapons gate, with factors 2 and 3. The corresponding research threat and force blocks also use the same enemy-use condition. If both are additive in the native strategy consumer, the medium threat contribution is not a mutually exclusive tier and can produce unintended dominance.
- chem_tank_shell_production_major_threat_low and chem_tank_shell_production_major_threat_med use the same enemy-use gate, while the major base block remains active. The same additive-tier risk exists for light, medium, and heavy flame chassis production.
- cbrn_set_limited_battlefield_policy, cbrn_set_strategic_release_policy, cbrn_set_unrestricted_policy, cbrn_chaos_warfare_establishment_mission, and cbrn_hazard_assault_training_mission have base0 or route-dependent positive additions. This can be intentional route locking, but it can also starve a score race if the expected route factor is absent or if the native decision pool requires a positive score.
- The special-project constants in common\special_projects\projects\biowarfare_main_projects.txt are tularemia2, anthrax3, plague4, and smallpox2, with desperate smallpox4. The implementation-surface comments and country-profile role ladders imply a progression toward stronger late agents, but smallpox has the lowest nonzero base among the four. This is a likely rank inversion or intentional locked-project behavior that must be settled with a complete project candidate pool and a candidate comparison after any owner patch.
- bio_sabotage_*_theater and bio_sabotage_*_terminal include unconditional multiplier blocks. If route eligibility is not enforced outside the score expression, a route variant may dominate its base sibling or accumulate route factors unexpectedly.
- cbrn_export_protective_equipment contains export_surplus1.50 and export_shortage0. If the surplus and shortage trigger partitions overlap, a zero factor can suppress an otherwise eligible export choice. The strict state partition was not engine-tested.
- The mask production factory bands are written as strict lower and upper conditions and appear intended to be non-overlapping for integer factory counts. Boundary behavior and the external production candidate pool remain unresolved.

### Repetition, timing, and exploit-risk findings

The stockpile safety system has explicit 30-day cadence, 730-day agent cooldown, zeroing of unavailable agents, risk-band outer weights, and five severity candidates. This is a stronger source-level anti-repetition design than a flat random list, but it is not a complete sequence proof because the risk-band transition, cooldown recovery, stockpile removal, reset, and terminal behavior were not declared as one custom pool for hoi4.probability_sequence.

The raid and operation weights use route, treaty, target density, major status, supply hub, condemnation, import vulnerability, and response factors, but no returned target matrix proves exclusion of own, allied, subject, hidden, or route-incompatible targets. This leaves an unresolved exploit risk around target selection, payload expenditure, and repeated operation attempts.

The AI behavior matrix calls for no operation without a valid target, no ally/subject/own target, no idle aircraft contamination, no biological operation below containment unless desperate, no nerve suppression if the state is likely lost, and no offensive support with zero payload. Source gates cover parts of this list, but the absent native target and operation adapters prevent a complete proof.

### Scenario-specific source findings

| Scenario id | Static trace expectation | Pool/external completeness | Result |
| --- | --- | --- | --- |
| prepared_route | Prepared-profile factors are positive in doctrine, protection, production, payload, biological production, and project gates where the corresponding route triggers are true. Mastery and committed factors can increase doctrine/subdoctrine willingness. | Route, profile, target, stock, prerequisites, and all competing candidates were not returned by MCP. | Score-only source pressure; rank, probability, and timing unresolved. |
| unprepared_route | Stable-base, preparation, route, and containment gates should suppress or zero offensive choices while protective groundwork remains eligible. | Native availability, target validity, and the full competing decision/research/production pool are incomplete. | Failsafe intent visible; engine result unresolved. |
| defensive_route | Defensive doctrine/profile factors and protective emergency factors should dominate offensive route factors; biological and sabotage defensive factors include .20. | Complete candidate pool, country profile, enemy state, stock, and native target filters incomplete. | Bounded direction is not justified without MCP; source-only directional expectation. |
| no_valid_target | Target-state triggers should set raid, operation, sabotage, occupation, diplomacy, and battlefield target choices to unavailable or zero. | No target matrix or target-aware MCP adapter returned. | Unresolved validity and exploit risk; no probability claim. |
| low_stock | low_stock3, frontline_shortage4, emergency response, mask production, payload reserve thresholds, and selected support production factors increase protective or replenishment pressure. | Stockpile values, factory count, equipment validity, and every competing production/decision line incomplete. | Score-only source pressure; no ranking or threshold proof. |
| high_penalty | Treaty, condemnation, import-vulnerability, sanction, used-unconventional, and public/strategic penalty factors can reduce or zero offensive choices, including .10, .20, .25, .50, or 0 factors in the inspected constants. | Penalty source, target relation, treaty state, route, and all native candidates incomplete. | Static factor trace only; no exact bounded penalty response. |
| special_excluded_tag | Nonhuman, Japan/China-specific, strongest-tech exclusion, excluded-agent, doctrine-only, and allow = always no gates should remove incompatible choices or route branches. | Tag, country role, project pool, tech availability, and native candidate enumeration incomplete. | Unresolved positive-weight-on-excluded-choice risk. |
| mastery_route | Doctrine mastery multipliers, committed factors, terminal policy additions, and special-project/project-reward terminal states may increase late-route scores. | Mastery state, route flags, terminal state, candidate pool, and competing doctrines/projects incomplete. | Score-only source pressure; rank reversal and repetition unresolved. |

No ranking, threshold, sensitivity, rank reversal, timing distribution, or exact probability is reported for any scenario because no MCP result was returned.

## Recommended fixes for the owner; none applied

These are concrete recommendations for a later owner-applied patch and a mandatory same-scenario probability_compare pass. They are not changes made by this audit.

- In common\ai_strategy\chemical_warfare_livens.txt, make chem_livens_production_major_threat_low and chem_livens_production_major_threat_med mutually exclusive tiers, or document and test the intended additive behavior. Apply the same review to chem_livens_research_major_threat and chem_livens_research_major_force.
- In common\ai_strategy\chemical_warfare_tank_shells.txt, make chem_tank_shell_production_major_threat_low and chem_tank_shell_production_major_threat_med mutually exclusive or explicitly document the intended cumulative pressure, then compare light, medium, and heavy chassis rankings.
- In common\special_projects\projects\biowarfare_main_projects.txt, reconcile the tularemia2, anthrax3, plague4, and smallpox2 AI bases with the intended project ladder. If smallpox is intentionally locked until a terminal/desperate route, encode that route distinction explicitly instead of leaving a lower base that can invert the declared progression.
- In common\decisions\cbrn_doctrine_decisions.txt, verify that every zero-base policy or mission has a guaranteed positive route path when it is visible, and that a route-incompatible zero-base choice is not presented as an eligible score-race candidate.
- In common\decisions\biological_sabotage_decisions.txt, verify that base, theater, and terminal choices are mutually exclusive at the candidate level or that their unconditional multiplier blocks cannot stack across route variants.
- In common\raids\cbrn_chemical_air_raids.txt, common\raids\biological_raids.txt, and common\raids\biological_battlefield_raids.txt, expose explicit target, own/faction/subject, payload, protection, condemnation, and route validity in the same audit surface that supplies ai_will_do, or document the native trigger that guarantees those exclusions before scoring.
- In common\operations\chaosx_bioweapon_operations.txt, provide an operation-specific probability/score adapter or an equivalent declared custom pool so the route, target, preparation, phase, cooldown, and terminal states can be analyzed rather than inferred from raid weights.
- In common\ai_strategy\cbrn_protection_production.txt, verify the integer boundary partitions at 10, 25, 50, 75, and 100 factories and test that export_surplus and export_shortage cannot overlap in cbrn_export_protective_equipment.
- In common\technologies\chaosx_technologies.txt, common\technologies\cbrn_regimental_support_technologies.txt, and common\technologies\cbrn_hq_technologies.txt, keep doctrine-only and special-project-only technologies excluded from the native research candidate pool, not merely assigned factor0, and compare research ranks with a complete non-CBRN candidate pool.
- Reconcile docs\specs\chaos_warfare_system_specs\handoffs\implementation_surface_map.md with the actual split strategy files instead of relying on the absent common\ai_strategy\cbrn_warfare_ai.txt path.
- For any owner patch affecting a weighted surface, rerun hoi4.probability_inspect, hoi4.probability_evaluate, hoi4.probability_sweep, and the same-scenario hoi4.probability_compare after the patch, then render the changed ranking, matrix, timing, sensitivity, or unresolved view.

## Skipped analyses, blockers, uncertainty, and omissions

- The primary blocker is the exact MCP failure sequence recorded above: schema rejection for invalid source shapes, 180-second timeout for schema-valid probability_inspect calls, and Transport closed for later inspect, evaluate, sweep, and structural inspection.
- No MCP artifact URI, revision, scenario hash, analysis id, comparison id, or rendered evidence path/URI exists to preserve.
- No exact or bounded selection probability was calculated because native candidate pools and external factors were incomplete.
- No probability_simulate was run because the parent did not declare uncertain input distributions or seeds.
- No probability_sequence was run because the nested stockpile pool did not have a complete declared state-transition manifest.
- No probability_compare was run because there was no source patch or candidate comparison.
- No event, focus, technology, or doctrine render was run because the corresponding read-only inspection did not produce a renderable analysis id. Event inspection itself reached the transport blocker.
- No dedicated target-weight, operation, raid, MIO, ability, unit-template, or equipment-module analyzer was available in the installed MCP tool set.
- No direct in-scope CBRN/chemical/biological/condemnation/Chaos Warfare MTTH entry was found. The adjacent zombie_outbreak_chance MTTH was inventoried but not engine-evaluated.
- The strategy, research, production, technology, doctrine, special-project, raid, and decision candidate pools are incomplete at the native-engine level even where a local source list is complete. This is why all such results remain score-only or unresolved.
- The source map’s absent common\ai_strategy\cbrn_warfare_ai.txt path is recorded as a repository/specification mismatch, not silently substituted.
- No gameplay simplification or fallback was applied. The simplification is analytical only: source-only findings are reported where MCP evidence was unavailable, and each such finding is explicitly prevented from being presented as an engine balance conclusion.

## Handoff conclusion

The current source contains substantial route, validity, stockpile, cooldown, treaty, condemnation, containment, and profile gating, but the mandatory engine-backed audit could not establish whether those gates remove candidates before scoring, whether repeated factor blocks are additive, whether native pools contain hidden or incompatible choices, or how the scores translate into selection probability and timing.

The highest-priority owner checks are the duplicated enemy-use threat tiers in Livens and tank-shell strategy, the low non-desperate smallpox special-project base, unconditional theater/terminal sabotage multipliers, zero-base route decisions, and target/payload exclusions on raid and operation choices. These are concrete source risks only; they require the blocked MCP workflow before balance or exploit-safety claims can be closed.
