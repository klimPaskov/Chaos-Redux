# Event 018 decision cost profile patch handoff

Disposition: implemented for the bounded Event 018 cost cleanup approved by the parent on 2026-10-05. The acceptance basis is the parent's explicit profile map and three-file ownership grant in the current task thread.

## Changed files

- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/script_constants/018_resources_found_decision_constants.txt`
- `localisation/english/018_resources_found_decisions_l_english.yml`

No commit was created. No other gameplay file was edited.

## Behavior before and after

The affected decisions used shared project profiles that assigned between five and nine spendable fee types in addition to non-debited factory-capacity gates. Their custom cost strings printed the full eleven-channel preview vector, including zero-valued channels, on multiple lines. The four-cost maximum was exceeded by the industry, transport, security, containment, full-seal, and anti-cave profiles.

Each profile now assigns only the approved resource fields. The existing country, field, and wartime cost multipliers, duration multipliers, rounding, clamping, project-start guards, and single payment helper remain in place. The native inline row shows at most three spendable amounts. Its blocked alias shows the same values with a red `Unavailable` status. The matching tooltip lists every actual fee for that profile, labels factory capacity separately as a requirement, and states the selected project duration or immediate execution and conflict limit.

Security and anti-cave are the two retained profiles with four spendable fees; their fourth fee appears in the full tooltip while the inline row stays within the three-amount limit.

The payment helper debits political power, command power, army experience, manpower, equipment, trains, convoys, and fuel from the exact prepared quote. It does not debit civilian or military factory counts. Factory amounts remain availability gates where their profile retains them and are not counted as spendable fees. The tooltip does not describe those requirements as payments.

## Profile coverage and retained baselines

All counts below exclude factory-capacity requirements because they are not debited by `resources_found_pay_decision_project_cost`. “Before” counts reflect the old profile assignments; “after” counts reflect the patched assignments.

| Profile | Spendable fee types before → after | Retained fee baselines | Retained capacity requirement |
| --- | ---: | --- | --- |
| Administration | 1 → 1 | 35 political power | 2 civilian factories |
| Survey | 4 → 3 | 50 support equipment, 40 trucks, 500 fuel | 2 civilian factories |
| Industry | 5 → 3 | 200 support equipment, 150 trucks, 2,000 fuel | 5 civilian factories |
| Transport | 5 → 3 | 200 trucks, 10 trains, 1,500 fuel | 6 civilian factories |
| Labor | 2 → 2 | 25 political power, 3,000 manpower | 2 civilian factories |
| Security | 5 → 4 | 8 command power, 5,000 manpower, 500 rifles, 100 support equipment | None |
| Diplomacy | 1 → 1 | 40 political power | 2 civilian factories |
| Containment | 8 → 3 | 5,000 manpower, 300 support equipment, 180 trucks | 6 civilian factories |
| Full seal | 9 → 3 | 10,000 manpower, 600 support equipment, 6,000 fuel | 12 civilian factories |
| Cave | 2 → 2 | 25 political power, 15 command power | None |
| Anti-cave | 9 -> 4 | 15 command power, 300 anti-tank equipment, 120 trucks, 300 support equipment | None |

The source assignments are grouped in `resources_found_decision_profile` branches in `common/scripted_effects/018_resources_found_decision_effects.txt:149`. The retained fixed-point baselines are in `common/script_constants/018_resources_found_decision_constants.txt:250`. Cost scaling and duration scaling remain active at `common/scripted_effects/018_resources_found_decision_effects.txt:68-146,220-247`.

Factory fields are non-consumed gates in the inspected payment path. Security no longer asks for civilian factory capacity, and full-seal and anti-cave no longer ask for military factory capacity. This follows the approved profile map. The inspection did not include external idea or modifier files, so it makes no claim about any factory reservation outside the decision payment helper.

The `anti_cave_support = 300` key is retained as both an approved anti-cave profile fee and an aid-package payload. The anti-cave aid mission no longer grants a fixed baseline: after the successful project payment, its donor stores the exact anti-tank and support equipment values charged by the active quote and sends those captured values to the selected partner. This keeps the shipment aligned with project scaling and Black Friday discounts. The removed `anti_cave_army_xp` fee constant has no remaining consumer. A search across `common` and `localisation/english` found no external uses of the deleted profile fee fields. The only related price-table match, `common/scripted_effects/026_black_friday_price_table_effects.txt:3212-3217`, refreshes the Event 018 preview cache and does not construct additional resource keys.

The shared project-start helpers are explicitly documented as serving Event 018 event options as well as decisions at `common/scripted_effects/018_resources_found_decision_effects.txt:664-666`. Those event-option consumers inherit the same approved profile reductions. Their source call sites were outside the authorized file scope and are not enumerated in this handoff.

## Anti-cave aid shipment trace

The accepted anti-cave profile is command power, anti-tank equipment, trucks, and support equipment. The retained fixed-point baselines are 15 command power, 300 anti-tank equipment, 120 trucks, and 300 support equipment. Existing project cost and duration scales still apply.

`resources_found_send_anti_cave_aid` sets the selected partner and calls `resources_found_start_decision_project`. After that helper passes its dynamic-input guard and pays `resources_found_pay_decision_project_cost`, it stores the actual prepared anti-tank and support equipment debit in donor-country variables `resources_found_anti_cave_aid_shipment_anti_tank` and `resources_found_anti_cave_aid_shipment_support`. At mission completion, the donor scopes into its saved partner and grants those exact values through `PREV` variable reads. The recipient flags are set only when both captured fields exist, so a missing shipment record cannot create free equipment. The aid mission's existing cancel path clears the pending partner and calls `resources_found_clear_decision_project_runtime`; that common cleanup now clears both shipment fields. Successful completion uses the same runtime cleanup after the transfer.

The installed effect documentation defines `add_equipment_to_stockpile` for country scopes and allows a variable amount (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:1252-1266`). The repository's support-equipment removal helper uses the `support_equipment` archetype (`common/scripted_effects/chaosx_dynamic_effects.txt:750-752`), and Event 019's exact transfer ledger uses the `anti_tank_equipment` archetype for grants and payments (`common/scripted_effects/019_infantry_spawn_management_effects.txt:2802`). Event 018 pays these same two archetypes. The focused `hoi4.script_validate` check accepted the country-scope command kind but returned `SCRIPT_CHECK_PARTIAL` with both argument blocks unchecked and `parametersChecked=false`; it does not prove an in-game equipment-level result.

Changed ids: `resources_found_send_anti_cave_aid`, `resources_found_anti_cave_aid_shipment_anti_tank`, `resources_found_anti_cave_aid_shipment_support`, and the `resources_found_project_estimate_c12_*` tooltip family. No decision definitions or mission timers were changed.

## Affected decisions

Each identifier below selects the named shared cost profile in its `complete_effect`.

- Administration: `resources_found_establish_national_authority`, `resources_found_charter_domestic_operators`, `resources_found_unify_compound_authority`, `resources_found_compensate_affected_families`, `resources_found_regulated_output`, `resources_found_reserve_output_domestic`, `resources_found_review_transferred_field`.
- Survey: `resources_found_commission_geological_appraisal`, `resources_found_drill_deeper_test`, `resources_found_map_surrounding_basin`, `resources_found_test_air_water`.
- Industry: `resources_found_open_primary_works`, `resources_found_install_heavy_machinery`, `resources_found_build_local_processing`, `resources_found_reinforce_shafts_ventilation`, `resources_found_reactivate_suspended_field`, `resources_found_concession_surge`, `resources_found_stabilize_restricted_workings`, `resources_found_seal_access_network`.
- Transport: `resources_found_extend_rail_road_corridor`, `resources_found_build_integrated_processing_corridor`, `resources_found_evacuate_lower_workings`, `resources_found_secure_transport_corridor`, `resources_found_evacuate_field_settlements`, `resources_found_evacuate_state_center`.
- Labor: `resources_found_expand_worker_settlement`, `resources_found_recruit_regional_labor`, `resources_found_shorten_shifts_rotate_crews`, `resources_found_establish_field_hospital`, `resources_found_maximum_shifts`.
- Security: `resources_found_place_field_in_strategic_reserve`, `resources_found_conceal_casualty_reports`, `resources_found_wartime_requisition`, `resources_found_emergency_suspension`, `resources_found_nationalize_field`, `resources_found_organize_field_guards`, `resources_found_counter_foreign_survey_teams`, `resources_found_break_smuggling_network`, `resources_found_reinforce_field_administration`, `resources_found_secure_frontier_corridor`, `resources_found_foreign_offer_access_guarantee`, `resources_found_foreign_open_smuggling`, `resources_found_foreign_sabotage`.
- Diplomacy: `resources_found_split_resource_concessions`, `resources_found_grant_foreign_concession`, `resources_found_invite_strategic_bids`, `resources_found_sign_long_term_export_contract`, `resources_found_balance_competing_buyers`, `resources_found_renegotiate_concession`, `resources_found_settle_compensation`, `resources_found_complete_contract_review`, `resources_found_name_border_claimant`, `resources_found_invite_border_arbitration`, `resources_found_create_international_commission`, `resources_found_negotiate_demilitarized_field`, `resources_found_restore_commission_compliance`, `resources_found_dissolve_international_commission`, `resources_found_foreign_request_purchase_agreement`, `resources_found_foreign_offer_development_assistance`, `resources_found_foreign_request_exclusive_rights`, `resources_found_foreign_press_field`, `resources_found_request_foreign_hard_attack_aid`.
- Containment: `resources_found_prepare_controlled_demolition`, `resources_found_start_limited_border_war`, `resources_found_escalate_limited_border_war`, `resources_found_armed_underground_sweep`, `resources_found_scientific_military_survey`, `resources_found_reinforce_perimeter`, `resources_found_hunt_surface_packs`, `resources_found_clear_urban_district`.
- Full seal: `resources_found_close_ordinary_field_exactly`.
- Cave: `resources_found_cave_mark_rich_state`, `resources_found_cave_activate_resource_anchor`, `resources_found_cave_accelerate_critical_anchor`, `resources_found_cave_guard_feeding_chamber`, `resources_found_cave_replace_origin_brood`, `resources_found_cave_consolidate_unfed_broods`, `resources_found_cave_deepen_tunnel_link`, `resources_found_cave_prepare_phalanx_assault`, `resources_found_cave_prepare_burrow_approach`, `resources_found_cave_release_raiding_broods`, `resources_found_cave_convert_industrial_district`, `resources_found_cave_refresh_brood_queue`, `resources_found_cave_fortify_origin`, `resources_found_cave_refresh_continent_objectives`, `resources_found_cave_begin_continent_verification`, `resources_found_cave_prepare_world_end_ruptures`.
- Anti-cave: `resources_found_issue_emergency_anti_armor_contracts`, `resources_found_deny_resource_state`, `resources_found_liberate_activating_anchor`, `resources_found_clear_mature_anchor`, `resources_found_share_hard_attack_intelligence`, `resources_found_open_anti_cave_evacuation_corridor`, `resources_found_form_threat_cooperation`, `resources_found_send_anti_cave_aid`, `resources_found_restore_liberated_resource_state`, `resources_found_join_reconstruction_compact`.

## Localisation keys changed

All 40 `resources_found_project_estimate_*` bases below have their `_blocked` and `_tooltip` companions; the patch changed all 120 rows.

```text
resources_found_project_estimate_c1_d3
resources_found_project_estimate_c1_d4
resources_found_project_estimate_c10_d11
resources_found_project_estimate_c11_d11
resources_found_project_estimate_c11_d12
resources_found_project_estimate_c11_d15
resources_found_project_estimate_c12_d11
resources_found_project_estimate_c12_d13
resources_found_project_estimate_c12_d14
resources_found_project_estimate_c12_d16
resources_found_project_estimate_c13_d11
resources_found_project_estimate_c2_d3
resources_found_project_estimate_c2_d4
resources_found_project_estimate_c2_d5
resources_found_project_estimate_c3_d4
resources_found_project_estimate_c3_d5
resources_found_project_estimate_c3_d7
resources_found_project_estimate_c3_d8
resources_found_project_estimate_c3_immediate
resources_found_project_estimate_c4_d4
resources_found_project_estimate_c4_d5
resources_found_project_estimate_c4_d8
resources_found_project_estimate_c4_d9
resources_found_project_estimate_c5_d4
resources_found_project_estimate_c5_d7
resources_found_project_estimate_c6_d3
resources_found_project_estimate_c6_d5
resources_found_project_estimate_c6_d6
resources_found_project_estimate_c6_d7
resources_found_project_estimate_c7_d4
resources_found_project_estimate_c7_d5
resources_found_project_estimate_c7_immediate
resources_found_project_estimate_c8_border_limit
resources_found_project_estimate_c8_d3
resources_found_project_estimate_c8_d4
resources_found_project_estimate_c8_d7
resources_found_project_estimate_c8_d9
resources_found_project_estimate_c8_immediate
resources_found_project_estimate_c9_d10
resources_found_project_estimate_c9_d2
```

## Evidence and validation

The profile audit checked each active assignment against the parent's approved set and verified every retained baseline constant is positive. It counted factory capacity separately from debited resources and confirmed the payment helper omits both civilian and military factory values. It also checked all 40 inline strings for a maximum of three resource amounts, all 40 blocked aliases and tooltips, full payment variables per profile, capacity and duration coverage, and the UTF-8 BOM.

Source review confirmed the same `resources_found_decision_has_base_*_inputs` helper is called from both `available` and `custom_cost_trigger` in all 100 Event 018 custom-cost decisions. Those predicates use negated `< quoted_amount` checks, so the source comparison accepts an amount equal to the quote and rejects an amount below it. Project start recalculates the dynamic quote and compares each fee and duration to the preview before calling `resources_found_pay_decision_project_cost` once. The debit body uses the prepared variables for political power, command power, army experience, manpower, equipment, trains, convoys, and fuel; the factory capacity fields are not debited. A source-only audit checked all 40 full tooltips against their profile fee sets, including the four-fee security and anti-cave profiles.

The offline wiki citation used for custom cost localisation is `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:308-321`; it specifies the base, `_blocked`, and `_tooltip` key selection. The installed game's `common/decisions/_documentation.md:1-24` was read for decision trigger scopes and refresh behavior; it contains no custom-cost-specific section. A vanilla precedent was read directly at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/ITA.txt:2553-2555`, which pairs a custom cost trigger with a localised two-resource cost key.

`hoi4.script_validate` returned `SCRIPT_CHECK_PARTIAL` for the country-scope profile effect snippet with `validation.passed: false`, `data.valid: null`, `parametersChecked: false`, 20 unchecked argument blocks, 30 unresolved items, and 54 omitted findings. It reported the existing `else_if` branches as unresolved and left nested `set_variable`, `check_variable`, and `multiply_variable` arguments unchecked. The cited installed docs were read directly for `multiply_variable` (`documentation/effects_documentation.md:5028-5040`), `set_variable` (`effects_documentation.md:7888-7898`), and `check_variable` (`documentation/triggers_documentation.md:2110-2135`). This partial result is not an engine syntax pass.

`hoi4.reference_context` for the decision surface, `hoi4.decision_inspect` for `random_faction_stabilize_alignment` under `GER-baseline`, and `hoi4.gui_inspect` for `resources_found_field_window` under a normal state scenario each timed out after 600 seconds. The parent reports that the dedicated Event 018 and Event 020 GUI workers own their inspection and render evidence; this patch made no GUI change.

No `.tools` or `.tools/validation` test covers the Event 018 decision cost profiles, equality boundaries, or anti-cave shipment transfer. The existing Event 018 field-value-slot and Event 020 outbreak-entry tests cover different GUI and trigger surfaces and were not run. This source check does not prove engine display or runtime behavior. No AI weights changed, so probability comparison remains with the separate auditor.

## Remaining issues and limits

This handoff covers the Event 018 cost-profile patch only. The separate read-only audit of Events 017, 019, and 020 is not represented as complete here. Exact engine evaluation of the equality boundaries and player-facing render behavior remains unverified because the relevant MCP routes timed out. GUI evidence for Event 018 and Event 020 is owned by the dedicated GUI workers and still requires parent review.
