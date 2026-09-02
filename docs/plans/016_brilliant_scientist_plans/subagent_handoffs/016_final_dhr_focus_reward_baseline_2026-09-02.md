# Event016 DHR Focus Reward Baseline and Enclave Closure Handoff

Date: 2026-09-02.

Scope: Read-only baseline audit of the existing 88-focus D’Rhondan tree and its reward, decision, scripted trigger, scripted effect, idea, landing API, localisation, icon, and AI consumers, plus the parent-authorized narrow enclave-crisis closure patch.

Status: The enclave focus gate, guarded clear helper, and max-infrastructure paid bridge closure are applied in place. The broader reward and receipt findings remain recommendations for a later parent-owned patch. No new focus, route, country, event, GUI, decision, cohort, equipment grant, icon, or AI weight was added.

## Priority findings

1. DHR_resolve_the_enclave_crisis requires dhrondan_country_is_active = yes and dhrondan_all_disconnected_enclaves_supported = yes at common/national_focus/016_dhrondan_focus_tree.txt:1228-1243. The parent-clarified custom tooltip key DHR_enclave_crisis_resolution_requirements_tt at localisation/english/016_dhrondan_focus_l_english.yml:20 states that all controlled, disconnected landing enclaves need completed supply bridges.

2. dhrondan_focus_clear_enclave_crisis now applies the same active-DHR plus all-disconnected-supported guard before clearing dhrondan_enclave_crisis_active and setting dhrondan_enclave_crisis_resolved at common/scripted_effects/016_dhrondan_focus_effects.txt:143-151. The helper is therefore idempotent for supported state and cannot clear an unsupported crisis through a direct or repeated call.

3. The final supply decision had a real at-cap deadlock. dhrondan_all_disconnected_enclaves_supported at common/scripted_triggers/016_dhrondan_country_triggers.txt:67-76 requires the bridge receipt, while the target trigger previously required infrastructure < constant:dhrondan_decision_limit.maximum_infrastructure at :79-86. An otherwise-valid DHR-owned, DHR-controlled, off-home, unbridged landing state at infrastructure 5 could never become a target and could never receive its bridge receipt.

4. The adjacent deadlock is fixed within the existing action family. dhrondan_state_can_receive_enclave_support now rejects only infrastructure above the existing maximum with NOT = { infrastructure > constant:dhrondan_decision_limit.maximum_infrastructure } at common/scripted_triggers/016_dhrondan_country_triggers.txt:79-86. The existing bridge decision at common/decisions/016_dhrondan_country_decisions.txt:72-123 conditionally adds one infrastructure level only below the maximum and always writes dhrondan_enclave_supply_bridge_completed after the paid decision completes. Cost, 30-day duration, cancellation, target ownership/control, route, crisis, and AI requirements are unchanged.

5. Six focus reward helpers are repeated generic ladders rather than distinct route consequences. dhrondan_focus_add_diplomatic_credit is called by DHR_seat_the_human_delegates, DHR_ratify_the_two_world_covenant, DHR_open_the_translation_bureaus, DHR_exchange_maps_for_access, DHR_choose_our_terrestrial_partners, and DHR_invite_the_enclave_congress at six call sites in common/national_focus/016_dhrondan_focus_tree.txt; its implementation at common/scripted_effects/016_dhrondan_focus_effects.txt:284-287 only sets dhrondan_diplomatic_credit_established and adds a small political-power reward. No credit variable or decision consumer was found.

6. dhrondan_focus_add_civilian_complex is called four times at DHR_beneath_an_alien_sky, DHR_assign_merit_by_projection, DHR_convert_terrestrial_workshops, and DHR_trade_in_impossible_materials; its helper at common/scripted_effects/016_dhrondan_focus_effects.txt:205-221 picks a random eligible owned state and adds one industrial complex. dhrondan_focus_expand_laser_production is called three times at DHR_recover_the_laser_forges, DHR_standardize_alien_components, and the existing laboratory production sequence around DHR_convert_terrestrial_workshops; its helper at :186-203 picks a random eligible state, adds one arms factory, and sets a shared flag. These are concrete reward ladders but do not expose route-specific consumers.

7. dhrondan_focus_add_ground_logistics is called three times at DHR_supply_before_the_order, DHR_link_airfields_to_the_relay, and DHR_subordinate_borders_to_need; its helper at common/scripted_effects/016_dhrondan_focus_effects.txt:223-231 adds infrastructure at the capital. dhrondan_focus_add_orbital_support is called by DHR_reassemble_the_orbital_office and DHR_make_near_space_ours plus the existing orbital support sequence; its helper at :278-281 only sets a flag and adds air/navy experience. dhrondan_focus_mark_origin_host_reclamation is called four times at DHR_proclaim_the_right_of_return, DHR_calculate_the_reclamation_zones, DHR_subordinate_borders_to_need, and DHR_federate_the_two_worlds; it sets the same reclamation flag each time. These remain recommendations because no parent authorization was given to redesign the reward families.

8. A bounded common-code scan found no reader outside the focus tree for the following focus-set flags. Treat them as candidate receipt/history markers rather than delete them automatically because generated achievements, external content, or future consumers may exist: dhrondan_borders_subordinate_to_need, dhrondan_command_nodes_audited, dhrondan_command_without_surprise, dhrondan_covenant_route_complete, dhrondan_crystal_growth_chambers_active, dhrondan_decree_replaced_by_prediction, dhrondan_dual_citizenship_code_written, dhrondan_enclave_congress_invited, dhrondan_enclave_empire_crowned, dhrondan_enclave_intelligence_network_active, dhrondan_enclave_reconciliation_chosen, dhrondan_exoplanetary_materials_board_active, dhrondan_expeditionary_cadres_rebuilt, dhrondan_extraterrestrial_embassy_established, dhrondan_field_calculants_delegated, dhrondan_first_calculants_elevated, dhrondan_focus_tree_complete, dhrondan_homeworld_corridor_reopened, dhrondan_human_airwaves_monitored, dhrondan_human_delegates_seated, dhrondan_human_signal_teams_trained, dhrondan_imperial_reaches_claimed, dhrondan_imperial_route_complete, dhrondan_imperial_service_codified, dhrondan_impossible_materials_trade_open, dhrondan_landing_councils_elected, dhrondan_landing_lords_bound, dhrondan_laser_forges_recovered, dhrondan_merit_projection_active, dhrondan_ninth_diadem_restored, dhrondan_optimal_order_administration_ready, dhrondan_political_convention_complete, dhrondan_predictive_staff_restored, dhrondan_right_to_depart_guaranteed, dhrondan_scattered_laboratories_joined, dhrondan_shuttle_docks_salvaged, dhrondan_subject_world_protocol_ready, dhrondan_supply_forecast_active, dhrondan_synod_route_complete, dhrondan_terrestrial_air_corridors_charted, dhrondan_terrestrial_partner_selection_open, dhrondan_terrestrial_workshops_converted, dhrondan_translation_bureaus_open, dhrondan_twenty_element_substitution_mastered, dhrondan_two_world_covenant_ratified, dhrondan_two_world_federation_ready, and dhrondan_two_world_operatives_available.

9. dhrondan_enclave_crisis_resolved is set by the enclave decision and the guarded focus helper, but no common-code reader was found in the bounded consumer search. It may be an external receipt, but it is currently not a gameplay consumer.

10. The three focus-created spirit families are lifecycle-safe. common/ideas/016_dhrondan_focus_ideas.txt defines the political settlement ladder, predictive command ladder, and off-world corridor ladder. dhrondan_focus_clear_homeworld_lifecycle, dhrondan_focus_clear_predictive_lifecycle, and dhrondan_focus_clear_offworld_lifecycle remove the prior family stage before each replacement at common/ideas/016_dhrondan_focus_ideas.txt:13-119. At most three family spirits can coexist through the focus helper path, with no stacking breach found.

11. The paid landing boundary is intact. DHR_feed_the_landing_reserve at common/national_focus/016_dhrondan_focus_tree.txt:599-608 calls dhrondan_focus_prepare_landing_cohort, which only enables the network through common/scripted_effects/016_dhrondan_focus_effects.txt:121-129. The helper sets dhrondan_landing_network_enabled, preserves dhrondan_alien_infantry_training_forbidden, and stores constant:alien_infantry_landing.reserve_equipment. The actual API at common/scripted_effects/016_alien_infantry_api_effects.txt:461-505 debits the reserve cost and creates the normal landing cohort. No focus reward creates a unit, grants laser equipment, trains alien infantry, or starts a stockpile loop.

## Route coverage table

| Existing route | Exact source anchors | Count | Consumer and route result |
| --- | --- | ---: | --- |
| Survival | DHR_beneath_an_alien_sky through DHR_convene_the_two_world_throne | 8 | Common survival and throne setup. |
| Imperial | DHR_vael_ix_takes_the_throne through DHR_the_unbroken_imperial_line | 8 | Imperial regime family and world-order convergence. |
| Synod | DHR_sera_qel_presents_the_calculus through DHR_the_government_of_certainties | 8 | Synod regime family and world-order convergence. |
| Covenant | DHR_ilyr_ren_opens_the_chamber through DHR_the_chamber_of_two_skies | 8 | Covenant regime family and world-order convergence. |
| Laboratory | DHR_relight_the_field_laboratories through DHR_a_two_world_research_complex | 10 | Laboratory route enables enclave support decision eligibility. |
| Army | DHR_restore_the_predictive_staff through DHR_perfect_predictive_warfare | 12 | Predictive warfare route supports reclamation decision eligibility. |
| Orbital | DHR_reassemble_the_orbital_office through DHR_make_near_space_ours | 8 | Off-world relay and corridor progression. |
| Diplomacy | DHR_open_the_translation_bureaus through DHR_the_embassy_beyond_the_stars | 8 | Diplomatic network and partner route preparation. |
| Expansion | DHR_define_the_two_worlds_question through DHR_a_place_in_the_world_order | 12 | World-order route unlocks reclamation, integration, and compact decisions. |
| Crisis closure | DHR_the_enclaves_refuse_the_ledger through DHR_the_century_beyond_exile | 6 | Crisis resolution and final off-world corridor closure. |
| Total | Existing tree dhrondan_focus_tree | 88 | Exactly 88 IDs and no additional route family. |

The Imperial, Synod, and Covenant regime roots remain mutually exclusive at their existing focus blocks. DHR_define_the_two_worlds_question uses one intentional OR prerequisite block over the three regime capstones. DHR_begin_postwar_integration uses one intentional OR prerequisite block over the route-specific world-order branches. DHR_resolve_the_enclave_crisis uses one intentional OR prerequisite block over DHR_offer_a_shared_horizon and DHR_break_the_separatist_ciphers. Separate prerequisite blocks remain AND semantics where the tree requires both conditions.

## Adjacent closure scenario review

| Scenario | dhrondan_state_can_receive_enclave_support | Completion effect | Result |
| --- | --- | --- | --- |
| Below-cap, unbridged, DHR-owned and controlled landing state | Passes when all existing landing, off-home, ownership, control, and route/crisis gates pass. | Adds the existing one infrastructure level and always writes dhrondan_enclave_supply_bridge_completed. | Existing paid bridge behavior is preserved. |
| At-cap, unbridged, DHR-owned and controlled landing state | Passes because only values above the maximum are rejected. | Skips infrastructure construction because the state is already at the maximum and always writes the bridge receipt. | The previous deadlock is closed without overbuilding. |
| Already bridged state | Fails NOT = { has_state_flag = dhrondan_enclave_supply_bridge_completed }. | No decision target or duplicate bridge receipt. | Idempotent receipt behavior is preserved. |
| Lost control after decision start | Fails is_controlled_by = ROOT when completion is rechecked. | Existing cancel_trigger = { NOT = { dhrondan_enclave_decision_can_complete = yes } } remains in force. | No bridge receipt is written after loss of control. |
| Non-DHR-owned state | Fails is_owned_by = ROOT; the target remains unavailable. | No infrastructure or bridge flag is added. | No free bridge is created. |
| DHR loses ownership of an enclave | The target fails, while dhrondan_all_disconnected_enclaves_supported scans only currently owned states. | No target-side write occurs. | The lost enclave is no longer counted by the existing owned-state predicate; this remains a design decision for the parent if lost enclaves should continue blocking closure. |

The decision still requires dhrondan_country_is_active, dhrondan_world_order_route_is_complete, dhrondan_enclave_crisis_active, and the existing laboratory-route availability before a state target can be selected. The focus gate intentionally does not require the active crisis flag, so a crisis already closed by the final paid supply decision remains completable and cannot be reopened by the focus.

## Consumer coverage

| Focus-owned state or reward | Producer | Consumer evidence | Assessment |
| --- | --- | --- | --- |
| dhrondan_reclamation_declared | Four existing expansion focus rewards call dhrondan_focus_mark_origin_host_reclamation at common/national_focus/016_dhrondan_focus_tree.txt:264,1057,1083,1135. | common/decisions/016_dhrondan_country_decisions.txt:10-70 and dhrondan_reclamation_decision_can_complete at common/scripted_triggers/016_dhrondan_country_triggers.txt:143-156. | Connected, but repeated producer rewards are candidates for differentiation. |
| dhrondan_integration_started | DHR_begin_postwar_integration calls dhrondan_focus_mark_postwar_integration at common/national_focus/016_dhrondan_focus_tree.txt:1153-1161. | Integration and Covenant compact decisions at common/decisions/016_dhrondan_country_decisions.txt:125-203 and trigger dhrondan_integration_decision_can_complete at common/scripted_triggers/016_dhrondan_country_triggers.txt:166-173. | Connected. |
| dhrondan_enclave_crisis_active | DHR_the_enclaves_refuse_the_ledger calls dhrondan_focus_mark_enclave_crisis at common/national_focus/016_dhrondan_focus_tree.txt:1181-1190. | Supply decision target root and completion trigger at common/decisions/016_dhrondan_country_decisions.txt:72-123 and common/scripted_triggers/016_dhrondan_country_triggers.txt:158-164. | Connected; focus gate now also checks the supported-state predicate. |
| dhrondan_enclave_crisis_resolved | Paid bridge decision and guarded focus helper. | No bounded common-code reader found. | Candidate receipt with no current consumer. |
| dhrondan_world_order_decisions_unlocked and dhrondan_world_order_claim_contract_ready | Existing dhrondan_focus_open_world_order helper at common/scripted_effects/016_dhrondan_focus_effects.txt:288-293. | World-order triggers and country decisions at common/scripted_triggers/016_dhrondan_country_triggers.txt:120-170 and common/decisions/016_dhrondan_country_decisions.txt:10-203. | Connected. |
| Paid landing reservation | dhrondan_focus_enable_landing_network at common/scripted_effects/016_dhrondan_focus_effects.txt:121-129. | Alien infantry landing decisions and API at common/decisions/016_alien_infantry_landing_decisions.txt and common/scripted_effects/016_alien_infantry_api_effects.txt:461-505. | Connected; exact reserve cost remains API-owned. |

## Missing or simplified content list

- The six repeated helper families listed above are mechanically valid but shallow and route-generic; a later patch should add distinct existing action-family consumers or replace the shared helper calls in place without increasing focus count.
- The bounded scan found many focus-set receipts without a common-code consumer; parent review should decide which are achievement/history receipts and which need a decision, idea, advisor, claim, core, war-goal, event, or formable consumer.
- dhrondan_enclave_crisis_resolved has no common-code reader in the bounded scan.
- The owned-state scope in dhrondan_all_disconnected_enclaves_supported means a lost or transferred enclave is omitted from the remaining-support test; this was not changed under the authorized ownership.
- No new free infrastructure, free cohort, equipment stockpile, training path, event, GUI, country, route, or achievement was added.
- No broad reward redesign was attempted because the parent explicitly reserved repeated reward findings for a later bounded patch.

## Icon coverage table

| Route family | Focus references | MCP result |
| --- | ---: | --- |
| Survival | 8 | Existing icon references resolved with no DHR icon diagnostic. |
| Imperial | 8 | Existing icon references resolved with no DHR icon diagnostic. |
| Synod | 8 | Existing icon references resolved with no DHR icon diagnostic. |
| Covenant | 8 | Existing icon references resolved with no DHR icon diagnostic. |
| Laboratory | 10 | Existing icon references resolved with no DHR icon diagnostic. |
| Army | 12 | Existing icon references resolved with no DHR icon diagnostic. |
| Orbital | 8 | Existing icon references resolved with no DHR icon diagnostic. |
| Diplomacy | 8 | Existing icon references resolved with no DHR icon diagnostic. |
| Expansion | 12 | Existing icon references resolved with no DHR icon diagnostic. |
| Crisis closure | 6 | Existing icon references resolved with no DHR icon diagnostic. |

No icon ID or DDS path was changed. MCP returned resolvedTitleCount = 88 and no missing DHR focus icon diagnostic. The only localisation warning was the unrelated vanilla continuous_restrict_freedom description at game:common/continuous_focus/generic.txt:498-525.

## Localisation and reward mismatch list

- Added DHR_enclave_crisis_resolution_requirements_tt at localisation/english/016_dhrondan_focus_l_english.yml:20 for the new focus availability body.
- Existing DHR_enclave_crisis_resolved_effect remains the focus completion effect description and is still accurate after the guarded helper.
- MCP resolved all 88 DHR focus titles.
- The repeated diplomatic-credit, civilian-complex, laser-production, ground-logistics, orbital-support, and reclamation markers are the principal reward variety mismatches because multiple route-specific focus names map to the same generic helper result.
- The localisation file retains its UTF-8 BOM.

## AI behavior gaps

Every existing DHR focus retains an inline ai_will_do block in common/national_focus/016_dhrondan_focus_tree.txt, and route strategy definitions remain in common/ai_strategy_plans/016_dhrondan_focus_ai.txt. The enclave decision keeps its existing urgent, laboratory-route, and enclave-readiness AI factors at common/decisions/016_dhrondan_country_decisions.txt:118-123. No AI weight was changed.

A probability audit was not run because this patch changed no probability-bearing focus or decision weights. Any future AI weight or route-probability change must be routed through chaosx_ai_probability_auditor with named scenarios and a before/after probability comparison. Source weights are not probability proof.

## MCP evidence

Workspace: mod_chaos_redux_ea3b2d67c2c0.

Baseline pre-patch hoi4.focus_inspect was status ok with 88 focuses, layout hash cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87, zero crossings, zero node intersections, zero long connectors, and no blocking diagnostics. Baseline inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9691500ced3b88289bece2427e82d69b0b49eab93c9cd56ae4b69cb47c3c4d74/a3f78b9b293d1e3baa60ab943a368d58fd8bb98a3450e52446a4caaf653e8b39/focus-inspect.96ca0295b0288279.json.

The worker reported successful baseline render and raster calls, but supplied only abbreviated artifact paths in this handoff.
Those incomplete paths are not durable retrievable evidence; the full baseline inspect URI above and complete final artifact URIs below are the retained evidence.

Final hoi4.focus_inspect after the focus patch and adjacent closure patch was status ok with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4552d422de938b3589fb936291478272ddf89b33d5dbb9d012810a5b9b01fa0b/03157ec3eb9d0d219c3fdf4f553597065dbc7a9fbd3bc08e8e9ca216de572524/focus-inspect.5c94923a4611fc69.json. It reported focus count 88, resolved title count 88, diagnostic count 0, unchanged layout hash cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87, bounds x2..40/y0..22, 102 connectors, zero crossings, zero node intersections, zero long connectors, and dimensions 6992x2788.

Final hoi4.focus_render returned status ok with HTML artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cc3549bcbc5bb72bd1a7ce5e1dda18179b49a57f81659d3a58ee580b70e4550/ffeaaae4cf574c2f2b49750ca78a7816e8f371112769f6f78a919f8a31da0235/dhrondan_focus_tree.focus.html and SVG artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/da102ab6621298acaaf3ca4dd7a3cc23a17967a2c25ab7570bdf16006491f07b/dhrondan_focus_tree.focus.svg.

Final hoi4.focus_raster returned status ok with PNG artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/823adc423fa5aff63c1a89d8fbbd8b0e25bac7aee6d408c5927730f3b41beb70/f2db3130ef76167878552adf658b57e01b6cd1d82f29a43ae76395bcf0f06886/dhrondan_focus_tree.focus.png.

The required focus rewrite route produced these exact partials and errors during review. layoutMode = authored without a plan returned MCP error -32602: Input validation error: Invalid arguments for tool hoi4.focus_rewrite: plan is required unless layoutMode is compact at plan. Passing {} or the current artifact plan returned MCP error -32602: Input validation error: Invalid arguments for tool hoi4.focus_rewrite: Invalid input at plan. The first compact attempt returned structured REWRITE_SOURCE_STALE with status = error, execution = failed, automaticRecovery = incomplete, and no changed files. A later compact call returned FOCUS_CHANGES_APPLIED and wrote a source plus untracked planning sidecar, but reflowed all 88 coordinates to layout hash 353262d940e72744480fc1fb532b294a30b39383769449440002d438a78f20c3; that broad reflow was rolled back with apply_patch, the generated sidecar was deleted, and final inspect/render/raster prove the authored layout is unchanged. The successful rewrite validation artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65e7629f53263b02c4e82fe8ea669e30b2a7d38651bce79d73ac7316189c0400/b842174786bc5916eac78713d976b1291d7e288d091e0a0f0755e9a41226f6fc/focus-plan-changes.execution-validation.json. The generated source diff artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4072a9e5.../05c5.../016_dhrondan_focus_tree.txt.diff, and the generated plan diff artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe7d6b6.../21de.../016_dhrondan_focus_tree.focus-plan.json.diff.

No focus compare endpoint was exposed in the installed MCP tool inventory; ALL_TOOLS.filter(/focus.*compare|compare.*focus/) returned []. The exact compare blocker is retained rather than treating inspect/render/raster as a compare substitute. Decision-specific MCP inspect/render/rewrite endpoints were also absent from the installed tool inventory.

All final focus MCP calls reported the same unrelated warnings: MCP_INLINE_FILES_TRUNCATED with total 109 or 110 paths and 64 returned inline paths, and FOCUS_LOCALISATION_REFERENCE_MISSING for vanilla continuous_restrict_freedom_desc. No DHR blocking diagnostic was returned.

## Changed files and identifiers

- common/national_focus/016_dhrondan_focus_tree.txt:1228-1243 changed DHR_resolve_the_enclave_crisis availability only.
- common/scripted_effects/016_dhrondan_focus_effects.txt:143-151 guarded dhrondan_focus_clear_enclave_crisis.
- common/scripted_triggers/016_dhrondan_country_triggers.txt:79-86 changed dhrondan_state_can_receive_enclave_support to allow at-cap states while rejecting above-cap states.
- common/decisions/016_dhrondan_country_decisions.txt:98-114 made infrastructure addition conditional and preserved the bridge receipt write.
- localisation/english/016_dhrondan_focus_l_english.yml:20 added DHR_enclave_crisis_resolution_requirements_tt.
- This handoff is the only new documentation artifact.

The decision and trigger files already contained unrelated dirty changes from the shared worktree. Those hunks were preserved; only the exact trigger line and existing bridge completion block were modified for this closure.

Parent disposition: the support predicate intentionally covers currently owned and controlled landing enclaves, not lost territory or third-party occupation.
Those territories remain reclamation and war objectives rather than forcing an impossible peacetime supply construction target.
The focus tooltip names that controlled-territory boundary explicitly.
Repeated reward ladders and unused receipt consumers remain queued to the DHR reward-completion tranche; this commit closes only the paid enclave-resolution defects.

## Validation and remaining risks

Meaningful validation was the final focus inspect/render/raster trio, exact focus-ID count, source diff review, icon/localisation diagnostics review, and static scenario matrix for below-cap, at-cap, already-bridged, lost-control, and disconnected-owner states. The final focus tree remains exactly 88 focuses with unchanged layout and no blocking diagnostics.

No HOI4 launch, save test, log search, live gameplay validation, broad event inspection, decision MCP comparison, focus compare, AI probability audit, or parent-owned reward redesign was performed. Live consumer testing remains outside this subtask.

The remaining risks are the owner-scope behavior for lost enclaves, the candidate receipt flags without common-code readers, generic repeated reward ladders, and the unrelated vanilla continuous-focus localisation warning. These are explicitly queued for parent review and are not silently presented as resolved.

No commit or staging was performed.
