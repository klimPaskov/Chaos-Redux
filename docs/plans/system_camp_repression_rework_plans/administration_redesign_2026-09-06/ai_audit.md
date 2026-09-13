# Camp administration redesign AI audit

Audit mode: read-only baseline before owner edits, with a later same-scenario comparison required after the final source notification.

Audit date: 2026-09-06.

Scope: package-owned weighted decision surfaces in `common/decisions/camp_repression_generic_decisions.txt`, `common/decisions/camp_repression_major_country_decisions.txt`, `common/decisions/camp_repression_colonial_country_decisions.txt`, and `common/decisions/genocide_crisis_decisions.txt`, plus the colonial state selectors in `common/scripted_effects/camp_repression_colonial_country_effects.txt`, the Germany/Mengele gate source in `common/scripted_triggers/germany_mengele_triggers.txt`, and the relevant package AI strategy files.

The audit is read-only. No gameplay, AI, effect, trigger, decision, mission, constant, or runtime file was edited.

## Baseline source preservation

The exact pre-owner source blobs are preserved in `TEMP/camp_administration_baseline_20260906`.

The preserved files and SHA-256 hashes are:

- `common/decisions/camp_repression_generic_decisions.txt` — `F0824EB5ECD401727BFCC80E5F2E265A95C2FD9C3A4BA3D353B3980EA085936B`.
- `common/decisions/camp_repression_major_country_decisions.txt` — `DF46D7615156044ABC8C00D8B2F46D65920CFE999CDED4D0FEBDE7845766B8D8`.
- `common/decisions/camp_repression_colonial_country_decisions.txt` — `D43C831B6CDD2FB5ABE7EED04C3F762FC0D5A67C94C1F686B33E530E8A8A0616`.
- `common/decisions/genocide_crisis_decisions.txt` — `5639B7D83A75B87BD53C6AE93A38D0B52D24026921F2A025B7E4B924FA9B2CBE`.
- `common/scripted_effects/camp_repression_colonial_country_effects.txt` — `47A271A763B95341E9D2B8C894311E9F6DFB34C4446294B1D2D4704AC48C2D37`.
- `common/scripted_triggers/germany_mengele_triggers.txt` — `B55D74CBA83C3B03026526F6DF5668AEB93E50AF0CE3E6654101B0144BEAF949`.
- `common/ai_strategy/genocide_crisis_ai_strategy.txt` — `C7B09C1598762206CD3D1FCA0055631960E573D759B1C54AC8F147FA9F6A3433`.
- `common/ai_strategy/germany_mengele_ai_strategy.txt` — `5533D916C5A71AD3BD28BE6FFA1E197EF98EBDAA887FD2B0F3A7ADAACCD3ECD6`.
- `common/decisions/germany_mengele_decisions.txt` — `C9C32F368BAF263B76A013DEE17508463BA330EFB66ED55CF7343BD77C4E31B4`.
- `common/script_constants/germany_mengele_constants.txt` — `BC5D0E7AE05CC4D8B35FBF35E744DB938D5713DF2A7311F5A9ACA0013F212A28`.
- `common/scripted_effects/germany_mengele_effects.txt` — `DE087C508C077F1E66387B5B701FEE9EE7E1BD6EDEFE436AD1DC4C642994F63A`.

The copy was taken before the generic, colonial, major-country, integration, or Mengele owners were notified that legacy visibility could be changed.

The same source blobs and the raw probability evidence are also copied into `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/` for review.

The new owner-created `common/decisions/camp_administration_civil_decisions.txt` did not exist at the 13:48 local snapshot. Its empty pre-change baseline is recorded by `TEMP/camp_administration_baseline_20260906/common__decisions__camp_administration_civil_decisions.txt.absent.md`; the current two AI-only entries therefore require their own post-change inspection and comparison.

## MCP status and provenance

The required workspace is `mod_chaos_redux_ea3b2d67c2c0` and the installed production service is 3.0.8.

The mandatory first call was `hoi4.probability_inspect` with adapter `decision_ai_will_do`, source path `common/decisions/camp_repression_generic_decisions.txt`, `refresh = true`, and the workspace above.

The desktop call returned the exact blocker `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 180s`.

The serialized pinned 3.0.8 stdio retry completed after waiting for server execution capacity. Its raw result is `ai_evidence/mcp/generic_decision_probability_inspect_result.json`; its artifact is `ai_evidence/mcp/generic_decision_probability_inspect_artifact.json` and is also retained in `TEMP/repression_probability_inspect_artifacts/`.

The successful call returned `code = PROBABILITY_SOURCE_INSPECTED`, adapter `decision_ai_will_do`, source revision `9d4d7ede75823ac31f8e86b69ee0ea183f22890ab7b6bb89fa3ae420e239e450`, source hash `1f7081e0cf5d2b8f62cce0133b50d5329b0ddb809b3db47d3335696b3f885168`, artifact SHA-256 `355d973e1647848bbb5acc795ef6476a9c1648a7c8e8ad1c0af47242ee61fe4d`, and no MCP blockers or diagnostics.

The adapter reports `eligibility = true`, `rawScore = true`, `normalizedProbability = false`, `selectionRule = score_only`, `poolComplete = false`, `candidateCount = 14`, and `availableCandidates = 0` for this source inspection. It requires a scenario for the substantive candidates and explicitly disallows inventing a categorical denominator. This is engine-backed structural evidence, but it is not a click probability.

The 14 candidates discovered by the adapter are `camp_repression_close_ledger`, `camp_repression_hide_actions`, `camp_repression_open_ledger`, `camp_repression_show_actions`, `generic_activate_detention_network`, `generic_allocate_additional_guards`, `generic_destroy_evidence_before_retreat`, `generic_expand_labor_quotas`, `generic_inspect_active_site`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_reduce_labor_quotas`, `generic_restricted_contaminated_site_escalation`, and `generic_upgrade_existing_site_to_radicalized_atrocity_site`.

The adapter's source candidate count is lower than the 21 source `ai_will_do` blocks because it indexes active, unshadowed weighted decision candidates for this adapter. The remaining source blocks must remain in the source inventory and be checked through their own category or scenario surface; they cannot be assumed absent from runtime behavior.

## Weighted candidate inventory before owner edits

The source inventory found 21 `ai_will_do` blocks in the generic file, 29 in the major-country file, 62 in the colonial file, and 33 in the genocide-crisis file.

These are willingness-score entries, not click probabilities. The four files are not one normalized selection pool, and the decision adapter must retain every relevant candidate when evaluating a category or country state.

The generic weighted IDs are:

`camp_repression_open_ledger`, `camp_repression_close_ledger`, `camp_repression_show_actions`, `camp_repression_hide_actions`, `generic_activate_detention_network`, `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards`, `generic_reduce_labor_quotas`, `generic_upgrade_existing_site_to_radicalized_atrocity_site`, `generic_restricted_contaminated_site_escalation`, `generic_destroy_evidence_before_retreat`, `generic_inspect_active_site`, `generic_dismantle_detention_network`, `camp_repression_close_dormant_legacy_site`, `generic_labor_project_cycle`, `generic_network_overstretch_crisis`, `generic_retreat_evidence_crisis`, `generic_reform_and_dismantlement`, and `camp_gui_selected_dismantlement_mission`.

The major-country weighted IDs are:

`germany_route_prisoner_labor_to_war_construction`, `germany_redirect_prisoner_labor_to_eastern_fortifications`, `germany_tighten_deportation_logistics`, `germany_increase_guard_allocation_to_ss_sites`, `germany_build_ss_laboratory_annex_at_auschwitz`, `germany_destroy_auschwitz_evidence_before_retreat`, `germany_dismantle_auschwitz_complex`, `japan_establish_pingfang_research_bureau`, `japan_expand_occupation_test_records`, `japan_shield_ishii_from_army_review`, `japan_redirect_records_to_army_medical_control`, `japan_invite_kwantung_army_medical_officers`, `japan_suppress_chinese_resistance_cells`, `japan_route_supplies_to_epidemic_prevention`, `japan_open_epidemic_containment_office`, `japan_destroy_pingfang_records`, `japan_evacuate_pingfang_research_staff`, `japan_submit_to_army_review`, `japan_remove_ishii_from_program_control`, `japan_shut_down_prisoner_experiments`, `sov_transfer_prisoners_to_industrial_camps`, `sov_reinforce_nkvd_authority`, `sov_reduce_paranoia_through_party_review`, `sov_release_prisoners_for_military_service`, `sov_dismantle_overextended_gulags`, `sov_emergency_famine_relief`, `sov_conceal_famine_mortality`, `sov_admit_local_administrative_collapse`, and `sov_authorize_extreme_periphery_repression`.

The colonial weighted IDs are all 62 entries in `camp_repression_colonial_country_decisions.txt`:

- U.K./Raj: `uk_survey_raj_emergency_detention`, `uk_activate_raj_emergency_detention`, `uk_route_colonial_labor_to_military_construction`, `uk_expand_raj_detention_districts`, `uk_demand_indian_manpower_levy`, `uk_tighten_dominion_security_coordination`, `uk_allocate_additional_colonial_guards`, `uk_release_political_prisoners_for_negotiations`, `uk_reform_colonial_labor_administration`, `uk_dismantle_raj_detention_network`, `uk_hold_raj_security_line`, `uk_complete_raj_military_works`, `uk_postwar_raj_review`, and `uk_negotiate_indian_release_terms`.
- U.S.A.: `usa_authorize_emergency_relocation_zones`, `usa_expand_interior_security_camps`, `usa_assign_detainee_labor_to_local_works`, `usa_strengthen_wartime_review_boards`, `usa_allow_court_review`, `usa_release_detainees_under_supervision`, `usa_terminate_relocation_authority`, `usa_establish_redress_commission`, `usa_court_review_period`, `usa_security_authority_sunset`, and `usa_redress_commission_work`.
- France/Vichy: `fr_inspect_camp_legacy`, `fr_close_camp_legacy_sites`, `fr_expand_vichy_internment_administration`, `fr_route_north_africa_labor_to_rail_projects`, `fr_collaboration_transfer_records`, `fr_suppress_refugee_and_rescue_networks`, `fr_support_refugee_and_rescue_networks`, `fr_open_colonial_labor_review`, `fr_dismantle_north_africa_labor_network`, `fr_gurs_legacy_review`, `fr_north_africa_rail_labor_project`, `fr_refugee_pressure_response`, and `fr_post_liberation_reckoning`.
- Italy/Libya: `ita_reopen_desert_camp_administration`, `ita_authorize_homeland_emergency_detention`, `ita_redirect_colonial_labor_to_roads_and_forts`, `ita_force_settlement_of_rebel_districts`, `ita_raise_colonial_security_battalions`, `ita_expand_desert_transport_guard`, `ita_close_desert_camps`, `ita_compensate_local_communities`, `ita_desert_road_labor_project`, `ita_colonial_security_sweep`, `ita_desert_camp_closure`, and `ita_postwar_colonial_compensation`.
- Belgium/Congo: `bel_expand_concession_labor_quotas`, `bel_route_labor_to_rubber_and_minerals`, `bel_build_congo_transport_corridors`, `bel_suppress_colonial_strikes`, `bel_negotiate_colonial_strike_settlement`, `bel_open_international_inspection`, `bel_reform_concession_system`, `bel_recognize_local_administration`, `bel_congo_resource_quota_cycle`, `bel_congo_transport_corridor_project`, `bel_colonial_strike_response`, and `bel_concession_reform_mandate`.

The genocide-crisis weighted IDs are:

`genocide_show_hidden_decisions`, `genocide_hide_hidden_decisions`, `germany_wartime_camp_administration`, `germany_expand_occupied_poland_camp_system`, `germany_expand_extermination_site_network`, `germany_intensify_extermination_policy`, `germany_transfer_prisoners_to_experiment_site`, `genocide_restricted_chemical_site_escalation`, `genocide_build_extermination_camp`, `genocide_intensify_deportations`, `genocide_hide_evidence_from_foreign_observers`, `genocide_suppress_internal_reports`, `genocide_redirect_trains_and_supplies`, `genocide_deal_with_resistance_sabotage`, `genocide_handle_refugee_waves`, `genocide_manage_military_objections`, `genocide_destroy_camp_evidence`, `genocide_cover_up_liberated_camps`, `japan_expand_forced_labor_camps`, `japan_conduct_anti_partisan_reprisals`, `japan_transfer_prisoners_to_experimental_facilities`, `japan_destroy_occupation_records`, `sov_show_gulag_decisions`, `sov_hide_gulag_decisions`, `sov_expand_gulag_network`, `sov_deport_suspected_opposition_groups`, `sov_confiscate_food_from_disloyal_regions`, `sov_purge_camp_administrators`, `sov_raise_forced_labor_quotas`, `sov_destroy_gulag_records`, `genocide_publicize_survivor_testimony`, `genocide_support_resistance_networks`, and `genocide_prepare_tribunal_records`.

No block in the four named files declares `mission_ai_will_do` or `selectable_mission = yes`. Existing auto missions are primarily `selectable_mission = no` lifecycle targets. The `mission_ai_will_do` adapter must still be inspected because the requested surface includes mission behavior, but a zero-candidate or unsupported result will be an MCP adapter finding rather than evidence that mission behavior is absent.

## Existing base constants and strategy surfaces

The baseline constants in `common/script_constants/camp_repression_rework_constants.txt` include `blocked = 0.00`, Germany activation/expansion/experiment/reform bases `80/70/45/2`, Japan `55/45/35/8`, Soviet `55/48/18/40/2`, U.K. `25/18/80`, USA `6/2/90`, France reform `75`, Italy `42/70`, Belgium `38/75`, generic authoritarian/extremist/radicalized/reform `25/45/12/85`, evidence destruction `55`, guard allocation `35`, and global factors for war `1.50`, high resistance `1.35`, low stability `1.25`, high condemnation `0.10`, losing war `0.20`, and postwar reform `2.00`.

The genocide constants include Germany occupied-Poland/extermination/direct-Holocaust bases `55/70/55`, restricted chemical `8`, Japan forced-labor/terror/biowarfare `42/34/28`, Soviet Gulag/deportation/escalation/forced-labor `38/34/12/18`, evidence destruction `60`, cover-up `10`, foreign response `24`, occupation factor `1.40`, retreat factor `1.50`, and collapse factor `0.15`.

The current broad AI strategy surface is in `common/ai_strategy/genocide_crisis_ai_strategy.txt`. Active GER/JAP/SOV crises receive build-army pressure; exposed regimes receive avoid-starting-wars `80` and build-army `60`; countries at the historical camp site cap receive avoid-starting-wars `55`; reform or closure states receive avoid-starting-wars `100`; Japan and Soviet crisis states reserve at least three infantry-equipment factories.

The Mengele strategy surface is in `common/ai_strategy/germany_mengele_ai_strategy.txt`. A laboratory-state country receives build-army `120`, four minimum infantry-equipment factories, and avoid-starting-wars `-60`; a loyalist Germany with an active Mengele faction receives build-army `100` and avoid-starting-wars `80`.

## Structural findings before redesign

The generic file still exposes positive-weight repeat purchases and repeat projects alongside the accepted automatic administration contract. The named legacy candidates are `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards`, `generic_reduce_labor_quotas`, and the generic project/reform routine blocks. Hiding or retiring them changes candidate availability even when numeric weights are preserved, so each such visibility change requires the same-scenario MCP comparison.

The generic activation, inspection, evidence-destruction, dismantlement, crisis, and reform entries remain separate candidate families. The redesign must preserve a valid activation or registered migration route, retain review and closure actions, and prevent an automatic route from creating a positive score for a dead or invalid target.

The colonial selector helper uses a temporary array followed by uniform `random_scope_in_array` selection. The U.K. new-state selector falls back in order from Raj detention, Indian Ocean security, colonial emergency, and core fallback pools, and also traverses subject-controlled states. France and Belgium use controlled and subject-controlled pools with route-specific predicates; Italy excludes core states for colonial selection; USA restricts new sites to wartime/security/interior pools. An empty candidate array clears `camp_selected_state_id`, so downstream AI and effects must treat the missing target as ineligible.

The selector pool is not a weighted probability pool. Its result is a uniform random draw over the filtered array, while the preceding decision `ai_will_do` is a willingness score. Exact target or action probabilities cannot be claimed until the MCP adapter confirms the full candidate pool, filtered eligibility, and external state.

`genocide_crisis_decisions.txt` includes direct Holocaust, extermination, deportation, evidence, cover-up, restricted chemical, Japan biowarfare, and Soviet famine/Gulag routes. Their positive scores are gated by country, regime, site, responsibility, crisis, resistance, war, or cap triggers in source. The proposed rule that genocide must never arise from economic-policy automation requires those positive genocide entries to stay behind their existing authorization and route gates; no automatic development candidate should call these entries.

The Germany/Mengele trigger source requires fascist government, `date > 1940.06.13`, control of state `88`, and absence of rejection/closure/authorization/restricted flags to start the chain. Active programs require authorization, control of state `88`, and an experiment idea or recent expiry; coup eligibility additionally requires `date > 1942.12.31`, war with the Soviet Union, high fascist support, autonomy above the coup threshold, and no coup block. These are external gates for the major-country baseline and must be included in named scenarios rather than inferred from country tags alone.

## Owner handoff after baseline preservation

The integration owner reports visibility retirement behind `NOT camp_admin_civil_initialized` for the generic repeat or routine entries `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards`, `generic_reduce_labor_quotas`, `generic_upgrade_existing_site_to_radicalized_atrocity_site`, `generic_labor_project_cycle`, and `generic_reform_and_dismantlement`, plus the named genocide routine entries `germany_intensify_extermination_policy`, `germany_transfer_prisoners_to_experiment_site`, `genocide_intensify_deportations`, `genocide_redirect_trains_and_supplies`, `japan_transfer_prisoners_to_experimental_facilities`, and `sov_raise_forced_labor_quotas`. Numerical `ai_will_do` weights were reported unchanged; each visibility change still alters the candidate set and must be compared.

The major-country owner reports the following legacy IDs gated after initialization: `germany_route_prisoner_labor_to_war_construction`, `germany_tighten_deportation_logistics`, `germany_increase_guard_allocation_to_ss_sites`, `japan_expand_occupation_test_records`, `japan_invite_kwantung_army_medical_officers`, `japan_route_supplies_to_epidemic_prevention`, `sov_transfer_prisoners_to_industrial_camps`, and `sov_reinforce_nkvd_authority`. The owner also reports the Mengele eligibility date/ideology/control gate change to `germany_mengele_can_start_chain`, `germany_mengele_program_active`, and `germany_mengele_restricted_program_active`, with no numeric AI-weight edits. Exact before blobs for these files remain in the baseline folder above.

The colonial owner reports no random-selector edits. The selectors remain uniform filtered-array draws, so selector behavior is still a target-validity and empty-pool risk rather than a weighted-rank result. These owner reports are implementation handoff facts, not post-change MCP evidence.

## Baseline scenario contract

The named scenario set for the eventual MCP evaluation and comparison is:

- `CA-BASE-GER-1939-FASCIST-SHORTSTOCK`: GER, fascist, 1939-09-01, active or eligible occupation target, short equipment stock, no reserve, below project/site cap.
- `CA-BASE-GER-1941-AUSCHWITZ-FULL`: GER, fascist, 1941-06-22, controls state `88`, authorized Mengele program, full eligible project capacity, sufficient stock and reserves.
- `CA-BASE-GER-1943-HIGHSTRAIN-CAP`: GER, fascist, 1943-05-30, high strain, project/site cap reached, scarce stock, retreat pressure, valid and invalid target alternatives.
- `CA-BASE-JAP-1938-OCCUPIED-CHINA`: JAP, fascist, 1938-07-01, occupied China/Manchuria target, sufficient stock, full project capacity, no reserve.
- `CA-BASE-JAP-1942-SHORTSTOCK-RESERVE`: JAP, fascist, 1942-06-01, occupied target, short stock, reserve present, active Pingfang route.
- `CA-BASE-SOV-1937-PARANOIA`: SOV, communist, 1937-11-01, high paranoia, valid Gulag pool, sufficient stock, full project capacity.
- `CA-BASE-SOV-1942-FAMINE-HIGHSTRAIN`: SOV, communist, 1942-01-01, famine pressure and high strain, short stock, reserves present, reform and closure unavailable.
- `CA-BASE-UK-1936-RAJ-PEACE`: ENG, democratic, 1936-01-01, Raj subject pool, peace, sufficient stock, no active site, no crisis.
- `CA-BASE-UK-1942-RAJ-WAR-SHORT`: ENG, democratic, 1942-08-01, high Raj pressure/Burma threat, short stock, reserve present, full project capacity.
- `CA-BASE-UK-1946-REFORM-CLOSURE`: ENG, democratic, 1946-01-01, exposed or postwar reform route, active sites valid for closure, no new-site pool.
- `CA-BASE-USA-1942-PACIFIC`: USA, democratic, 1942-06-01, valid Pacific or homeland threat, sufficient stock, reserve present, full capacity.
- `CA-BASE-USA-1946-REFORM-CLOSURE`: USA, democratic, 1946-01-01, court/reform/closure route, no active expansion target, sufficient stock.
- `CA-EDGE-SUFFICIENT-FULLPROJECTS`: country-specific eligible country, all required equipment and civilian capacity available, valid target pool non-empty.
- `CA-EDGE-SHORTSTOCK-RESERVE`: same country fixture with one required stock below threshold but reserve available; reserve semantics are unresolved until the adapter binds them.
- `CA-EDGE-HIGHSTRAIN`: eligible country with high resistance/overstretch, low stability, active cap pressure, and valid target.
- `CA-EDGE-REFORM-CLOSURE`: exposed/reform/closure state with valid active site and invalid new-site target.
- `CA-EDGE-INVALIDTARGET`: no target passes responsibility, control, route, state-pool, or cap checks; `camp_selected_state_id` absent.
- `CA-EDGE-GENOCIDE-UNAUTHORIZED-ECONOMIC`: economic policy/capacity and budget are present but genocide authorization, regime, site, or responsibility gates are absent; every genocide route must be ineligible.

External factors to declare in every MCP scenario are regime/ideology, original tag and current tag, date, war and surrender state, control/ownership/subject status, active site arrays, responsible-country variables, finite workforce or population inputs, project/site/experiment/radicalized caps, available civilian capacity, equipment and fuel stock, reserve flags, current mandate and priority, reform/closure/exposure flags, crisis/high-strain variables, active cooldowns or missions, and target pool contents.

Because the MCP adapter has not yet returned its required-input schema, these scenarios are an explicit contract rather than claimed engine fixtures. Any input that the adapter cannot bind remains unresolved.

## Required next pass after owner notification

The final-source pass must first rerun `hoi4.probability_inspect` for `decision_ai_will_do` on each named decision source and for `mission_ai_will_do` on the same files, then run `hoi4.probability_evaluate` over the scenarios above with the complete per-file candidate pools.

Use `hoi4.probability_sweep` for budget/cap/strain/date/reform thresholds and rank reversals, preserving score-only semantics.

Use `hoi4.probability_render` for ranking, matrix, sensitivity, comparison, and unresolved views when returned analysis ids exist.

Use `hoi4.probability_compare` only after the parent announces that the final source is stable, with the exact baseline snapshots and the same scenario ids, candidate pools, and external-factor declarations.

The comparison must test the visibility retirement of generic repeat actions, major-country and Mengele eligibility gates, colonial selector validity, and any touched numeric weight or strategy factor. It must report candidate-pool completeness, availability, raw willingness traces, rank reversals, dominance/starvation, invalid target selection, and unresolved adapter inputs.

No exact click probability, normalized probability, timing distribution, repetition rate, or campaign recurrence may be claimed from `ai_will_do` or from the uniform state selector without complete MCP evidence.

## Unresolved and skipped analyses

The initial desktop `probability_inspect` timed out at 180 seconds before returning an artifact; the serialized 3.0.8 retry later completed and its evidence is archived above.

No `probability_evaluate`, `probability_sweep`, `probability_render`, or `probability_compare` call was made before inspect evidence became available.

No mission score conclusion is made because the source declares no `mission_ai_will_do` block and the mission adapter has not yet been inspected.

No live HOI4 execution was performed.

The source-level candidate inventory, existing constants, strategy factors, selector predicates, baseline copies, and one successful generic adapter inspection are complete for this pre-owner handoff. Engine-level eligibility and ranking for the other files remain unresolved until their serialized inspections and scenario evaluations run.
