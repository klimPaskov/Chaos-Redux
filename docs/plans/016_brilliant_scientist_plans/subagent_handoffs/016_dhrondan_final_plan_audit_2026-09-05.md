# Event 016 D’Rhondan final-plan focus audit

Status: bounded read-only audit completed on 2026-09-05. No gameplay source file was changed by this audit, no file was staged, and no commit was created. Existing concurrent edits in the DHR focus tree, focus effects, and DHR localisation were preserved exactly.

## Scope and closure invariants

The audit covered common/national_focus/016_dhrondan_focus_tree.txt, common/ai_strategy_plans/016_dhrondan_focus_ai.txt, common/ai_strategy/016_dhrondan_country_strategies.txt, common/scripted_effects/016_dhrondan_focus_effects.txt, common/scripted_triggers/016_dhrondan_focus_triggers.txt, common/script_constants/016_dhrondan_focus_constants.txt, common/ideas/016_dhrondan_focus_ideas.txt, localisation/english/016_dhrondan_focus_l_english.yml, and the DHR focus icon registry at interface/016_dhrondan_focus_icons.gfx.

The current source contains exactly 88 unique DHR focus IDs and the existing three regime roots: DHR_vael_ix_takes_the_throne, DHR_sera_qel_presents_the_calculus, and DHR_ilyr_ren_opens_the_chamber. No branch, country, project, public meter, GUI, super-event, achievement, event, unit definition, portrait, catalog workbook, or alien-landing transaction-core file was changed.

The shared landing contract remains outside this audit’s ownership. common/script_constants/016_alien_infantry_api_constants.txt:30 defines reserve_equipment = 2000; the shared API performs the exact debit/refund and owns the seven-day reservation, one-pending-landing, and thirty-day cooldown behavior. DHR focus effects only enable the network, persist the cost variable, and keep alien infantry training forbidden; no DHR focus reward creates a division, trains alien infantry, grants equipment, or grants a free cohort.

## Route coverage

| Route family | Focus count | Entry or anchor | Endpoint | Observed consequence coverage |
|---|---:|---|---|---|
| Survival and landing-network trunk | 8 | DHR_beneath_an_alien_sky | DHR_convene_the_two_world_throne | Landing-state/enclave inventory, beacons, cohesion, orbital channel, and paid landing-reserve preparation. |
| Imperial Continuity under Vael IX | 8 | DHR_vael_ix_takes_the_throne | DHR_the_unbroken_imperial_line | Imperial regime installer, war-support pressure, palace-guard laser capacity, reclamation declaration, and Imperial mandate spirit. |
| Predictive Synod under Sera Qel | 8 | DHR_sera_qel_presents_the_calculus | DHR_the_government_of_certainties | Predictive administration, research/command consequences, laboratory-linked planning, reclamation, and Synod calculus spirit. |
| Two-World Covenant under Ilyr Ren | 8 | DHR_ilyr_ren_opens_the_chamber | DHR_the_chamber_of_two_skies | Covenant regime installer, paid human-delegate advisor receipt, dual citizenship, councils, diplomacy, and Covenant compact spirit. |
| Laboratory economy | 10 | DHR_relight_the_field_laboratories | DHR_a_two_world_research_complex | Laboratory route, laser-forge recovery, terrestrial workshop conversion, crystal/substitution chain, component standardization, reserve supply, and research capacity. |
| Predictive warfare | 12 | DHR_restore_the_predictive_staff | DHR_perfect_predictive_warfare | Probability mapping, signal teams, expeditionary cadres, forecast fire control, logistics, wargame, field calculants, surprise reduction, and predictive lifecycle progression. |
| Orbital support | 8 | DHR_reassemble_the_orbital_office | DHR_make_near_space_ours | Air corridors, gravity fighters, shuttle docks, relay infrastructure, exile flotilla, descent-window protection, and near-space landing readiness. |
| Diplomacy and intelligence | 8 | DHR_open_the_translation_bureaus | DHR_the_embassy_beyond_the_stars | Paid translation-bureau advisor receipt, human-airwave intelligence, materials trade, map access, enclave network, operatives, partner selection, and embassy hook. |
| Expansion and world order | 12 | DHR_define_the_two_worlds_question | DHR_federate_the_two_worlds | Imperial reach, origin-host demand, subject-world protocol, reclamation zones, border administration, optimal order, enclave congress, settlement, federation, integration, and world-order hooks. |
| Enclave crisis and late game | 6 | DHR_the_enclaves_refuse_the_ledger | DHR_the_century_beyond_exile | Reconciliation or counterintelligence mutual exclusion, guarded crisis resolution, corridor reopening, and late-game order continuation. |

The route inventory totals 88 and covers the closure-plan themes of landing cadence, laser production, homeworld cohesion, predictive tactics, diplomacy, intelligence, expansion, origin-host relations/reclamation, enclave crises, integration, and late-game order. No route family is absent at the tree level.

## Structural, navigation, and MCP evidence

The required national-focus inspection used hoi4.focus_inspect with treeId = dhrondan_focus_tree, relativePath = common/national_focus/016_dhrondan_focus_tree.txt, laneSpacing = 80, and nodeSpacing = 60 in workspace mod_chaos_redux_ea3b2d67c2c0.

The inspect result reported focusCount = 88, resolvedTitleCount = 88, connectors = 102, crossingCount = 0, nodeIntersectionCount = 0, longConnectorCount = 0, bounds x = 2..40 and y = 0..22, layout hash cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87, maximum horizontal span 7, maximum vertical span 3, and maximum Manhattan span 9. The inspector reported zero asymmetric sibling cohorts and zero asymmetry, but also reported zero recognized sibling cohorts, so the symmetry result is not a strong proof of visual parity.

The inspector returned 70 non-blocking FOCUS_LAYOUT_SAME_ROW_SPACING_UNSATISFIED warnings because the authored row gaps are commonly 2–14 while the requested MCP spacing was 60. This is the current dense cross-lane authored layout under the inspection settings, not a discovered crossing or overlap. The warnings remain recorded for parent review rather than being suppressed.

Prerequisite semantics were spot-checked against the offline focus documentation and vanilla precedent. Separate prerequisite blocks are AND, as in DHR_convene_the_two_world_throne (DHR_bind_the_enclaves plus DHR_reopen_the_orbital_channel) and DHR_standardize_alien_components (crystal growth plus twenty-element substitution). Multiple focus entries inside one prerequisite block are OR, as in DHR_define_the_two_worlds_question, DHR_begin_postwar_integration, and DHR_resolve_the_enclave_crisis. All referenced focus IDs resolved in the MCP graph and source scan.

There are five mutually_exclusive blocks: the three regime roots pairwise exclude the other two regime roots, and DHR_offer_a_shared_horizon and DHR_break_the_separatist_ciphers exclude each other. There are no authored bypass blocks. No bypass promise is present in the accepted DHR closure contract, so this is recorded as a route-skip limitation rather than a confirmed defect.

All 88 focuses have search_filters and inline ai_will_do blocks. The initial position is DHR_beneath_an_alien_sky, and all ten shortcuts target valid focus IDs: survival, Imperial, Synod, Covenant, laboratory, army, orbital, diplomacy, expansion, and crisis anchors. No navigation or search-filter reference was missing.

hoi4.focus_raster completed at horizontalSpacing = 80, verticalSpacing = 60, padding = 1, and reviewScale = 1, producing a normal-zoom 3186x1398 PNG with the same layout hash and no DHR-specific diagnostics. The raster’s only diagnostics were an inline-file truncation information item and an unrelated vanilla continuous_restrict_freedom_desc localisation warning.

Raster artifacts: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47ec89cbd98ed765b56a40d152d4da5f66ef2af8532b74c49c5d1f08259b3f23/4bfc755d9c1aa14968e6b466747b121092bec901a14caf6c18e4099cf6cdbfa4/dhrondan_focus_tree.focus.html; hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94ad232f4d7cef4907b99f0a7f99ca03a964163948c1af89e0ccf96c43070651/bb89c2c64c1ad0ba06ea142828674088dca57f2480f87598869ea7c6108730cd/dhrondan_focus_tree.focus.svg; hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f9adedcf517fee4bf4abf8715e38526135cc64b5c50b55de88c80146be644fa/c336ae4e22d4d44ca5dc3dedcb16fb6f05be1d0e6f14172f4313b5e33017f47c/dhrondan_focus_tree.focus.png; hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/424d134b212a6a1e72765c9b6ca546ff49aeb8f86971b619bf3e43c6b45537cc/bc822e05bc69e602120721ab6e092a6c51462ad0ee1a7139b8e2c669a776ae6f/dhrondan_focus_tree.focus.json; hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fe92f97e96229e6d3d81e71c65ce15200a49a8bfb6e7409a7d47895f544d72/7bd35fe67995fbe6ef8077f7ea44e32d6a8d8cc8fdb06520d45b477ffec46b05/dhrondan_focus_tree.focus.source-map.json; hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0e2c9142474b96575d52ddcc3b79ce2784060893730aa59af717fa4838676d7/bc8a2ac55710bf85af140f4ba4fc3dafce94c480e4a0decb34f20960af9b1c02/dhrondan_focus_tree.focus.plan.json.

Valid hoi4.focus_render calls using the same source and normal-zoom spacing repeatedly timed out after 180 seconds. The exact service blocker was tool call failed for hoi4_agent_tools/hoi4.focus_render: timed out awaiting tools/call after 180s. No renderer output was substituted for this missing evidence. No hoi4.focus_compare route is exposed in the current MCP tool inventory; the available compare routes are event, technology, and probability compare. This is an exact MCP package blocker, not a source-level comparison claim.

## Icon coverage

| Route family | Base icons | Shine icons | Texture result |
|---|---:|---:|---|
| All DHR focus routes | 88 | 88 | 88 unique GFX_goal_DHR_* base references, 88 matching _shine sprites, and all referenced DDS paths present. |

The registry interface/016_dhrondan_focus_icons.gfx contains one unique base and one unique shine definition for every focus ID. No icon reference, shine pair, or texture path was missing. No icon was changed by this audit.

## Localisation and reward mismatch list

The DHR localisation file contains the UTF-8-BOM marker, all 88 focus title keys, all 88 description keys, and all nine custom tooltip/effect keys referenced by the current focus source. No missing localisation key or focus-name/reward contradiction was found. DHR_human_delegates_effect correctly describes the paid 100 Political Power Harmonic Envoy receipt consumed by common/characters/016_dhrondan_characters.txt; DHR_translation_bureaus_effect correctly describes the paid 100 Political Power Shadow Listener receipt. The guarded crisis tooltip DHR_enclave_crisis_resolution_requirements_tt matches the new availability predicate.

The current reward surface is materially varied: DHR_restore_the_landing_beacons, DHR_feed_the_landing_reserve, and DHR_make_near_space_ours expose landing-support hooks; DHR_recover_the_laser_forges, DHR_raise_the_palace_guard, and DHR_standardize_alien_components improve laser capacity; route roots and capstones replace the homeworld spirit; predictive, laboratory, orbital, diplomatic, reclamation, integration, crisis, and world-order effects are represented by existing helpers, flags, buildings, research, XP, and ideas.

The following repeated helper families remain weak or generic and are broad design follow-ups, not small confirmed defects that this audit could safely invent in place:

| Helper family | Current count | Focus IDs |
|---|---:|---|
| dhrondan_focus_add_civilian_complex | 4 | DHR_inventory_the_expedition_stores, DHR_assign_merit_by_projection, DHR_convert_terrestrial_workshops, DHR_trade_in_impossible_materials |
| dhrondan_focus_add_diplomatic_credit | 4 | DHR_ratify_the_two_world_covenant, DHR_exchange_maps_for_access, DHR_choose_our_terrestrial_partners, DHR_invite_the_enclave_congress |
| dhrondan_focus_add_ground_logistics | 3 | DHR_supply_before_the_order, DHR_link_airfields_to_the_relay, DHR_subordinate_borders_to_need |
| dhrondan_focus_add_orbital_support | 3 | DHR_reopen_the_orbital_channel, DHR_reassemble_the_orbital_office, DHR_make_near_space_ours |
| dhrondan_focus_expand_laser_production | 3 | DHR_raise_the_palace_guard, DHR_recover_the_laser_forges, DHR_standardize_alien_components |
| dhrondan_focus_mark_origin_host_reclamation | 4 | DHR_proclaim_the_right_of_return, DHR_demand_the_origin_host, DHR_calculate_the_reclamation_zones, DHR_negotiate_the_origin_settlement |
| dhrondan_focus_open_world_order | 2 | DHR_define_the_two_worlds_question, DHR_a_place_in_the_world_order |

The exact helper repetition is documented so the parent can route each focus to an accepted decision, mission, event, production, intelligence, or diplomatic consumer. This audit did not create new consumers or pretend that a repeated factory/flag helper was a completed mechanic.

A repository-wide read-only receipt scan found existing downstream consumers for landing beacons, landing reserve priority, near-space security, map exchange readiness, standardised components, expedition-store audit, human delegates, translation bureaus, and the major world-order/laboratory route triggers. Several focus-set flags remain history markers without a common-code reader, including dhrondan_enclave_crisis_resolved, dhrondan_enclave_congress_invited, dhrondan_enclave_intelligence_network_active, dhrondan_human_airwaves_monitored, dhrondan_two_world_operatives_available, dhrondan_optimal_order_administration_ready, dhrondan_terrestrial_partner_selection_open, dhrondan_subject_world_protocol_ready, and dhrondan_two_world_federation_ready. These are broad cross-system gaps and should not be solved by invented focus-only modifiers in this bounded pass.

## AI route audit

All 88 focuses contain inline ai_will_do. The three political roots remain route-aware: DHR_vael_ix_takes_the_throne is doubled in wartime and at high war support; DHR_sera_qel_presents_the_calculus is doubled in peace and at high stability; DHR_ilyr_ren_opens_the_chamber is doubled in peace and at low stability. Crisis selection favors DHR_offer_a_shared_horizon for Covenant and DHR_break_the_separatist_ciphers for Imperial or Synod. These source weights were not changed.

| Plan | Allowed/enabled lock | Declared focus pool | Explicit priority factors |
|---|---|---:|---|
| DHR_focus_opening_plan (common/ai_strategy_plans/016_dhrondan_focus_ai.txt:13) | original_tag = DHR, enabled before a political route, aborts after one is selected | 8 | DHR_beneath_an_alien_sky urgent; DHR_convene_the_two_world_throne preferred |
| DHR_focus_imperial_plan (common/ai_strategy_plans/016_dhrondan_focus_ai.txt:39) | original_tag = DHR, enabled only by dhrondan_focus_is_imperial, aborts otherwise | 25 | DHR_restore_the_predictive_staff preferred; DHR_restore_the_imperial_reaches urgent; DHR_break_the_separatist_ciphers preferred |
| DHR_focus_synod_plan (common/ai_strategy_plans/016_dhrondan_focus_ai.txt:83) | original_tag = DHR, enabled only by dhrondan_focus_is_synod, aborts otherwise | 27 | DHR_relight_the_field_laboratories urgent; DHR_restore_the_predictive_staff preferred; DHR_calculate_the_reclamation_zones urgent |
| DHR_focus_covenant_plan (common/ai_strategy_plans/016_dhrondan_focus_ai.txt:129) | original_tag = DHR, enabled only by dhrondan_focus_is_covenant, aborts otherwise | 28 | DHR_open_the_translation_bureaus urgent; DHR_invite_the_enclave_congress urgent; DHR_offer_a_shared_horizon preferred |

The route plans use valid, unique IDs and rely on focus prerequisites and availability for route locks. The remaining AI design gap is state sensitivity: the plans do not explicitly declare the complete contact/arrival/facility surface, and they omit optional support nodes such as DHR_relight_the_field_laboratories, DHR_feed_the_landing_reserve, and DHR_a_two_world_research_complex in the Imperial pool; DHR_reassemble_the_orbital_office in the Synod pool; and DHR_restore_the_predictive_staff, DHR_fire_control_by_forecast, and DHR_standardize_alien_components in the Covenant pool. These omissions are tuning risks, not invalid-ID or confirmed prerequisite defects, because every focus still has inline selection weight and engine prerequisites.

common/ai_strategy/016_dhrondan_country_strategies.txt keeps the three route-specific role surfaces: Imperial infantry 90 and armor 5; Synod infantry 75 and armor 10; Covenant infantry 70, mountaineers 8, and marines 6. Each strategy requires original_tag = DHR plus its route flag and uses abort_when_not_enabled = yes. No alien cohort is assigned to a role ratio.

## Probability evidence and blockers

hoi4.probability_inspect was run with adapter national_focus_ai_will_do against the current DHR source. It found 88 candidates, source revision 4f580b10a9b20eb8b8a0eb564449756f701ae38dad9414a9d6d97528b01efb35, source hash 73a2e4be2fc959c6c44b1c263859833b6699c19b94feb85fcdc97361c13f6c15, seven required inputs, and no parser-unresolved inputs. Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/893dfaef1c7694255a4f6bb918462f351d275291340296d29073ca59a7988d04/36a9a3986eae6bfeb1bf7f05c40abaaed28d3ac4d66016535eb685cb8fcd9198/probability-inspect-73a2e4be2fc9.json.

A direct hoi4.probability_evaluate pass used the full 88-focus candidate pool and four named scenarios: dhr_opening_peace_no_contact, dhr_imperial_wartime_contact, dhr_synod_peace_laboratory, and dhr_covenant_crisis_expansion. It produced 352 candidate/scenario rows, 34 diagnostics, and 131 unresolved outcomes with status PROBABILITY_ANALYZED_PARTIAL. Primary artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6fc2c0c1c012b56552818704690833695b6fefedda4e50ee9c20b7e980a2b25/64d625acc0f8c4270cfb382606310f66361b808be9a72d8a7c41b5d0815d028f/probability-c1e3a526dd5b67bb8617728d.json.

The partial diagnostics include PROBABILITY_OUTCOME_NEVER_ELIGIBLE for route-gated candidates such as DHR_administer_the_optimal_order, DHR_assign_merit_by_projection, DHR_audit_every_command_node, DHR_bind_the_landing_lords, DHR_break_the_separatist_ciphers, DHR_calculate_the_reclamation_zones, DHR_codify_imperial_service, DHR_crown_the_enclave_empire, DHR_demand_the_origin_host, DHR_elect_the_landing_councils, DHR_elevate_the_first_calculants, DHR_enthrone_the_synod, DHR_federate_the_two_worlds, DHR_guarantee_the_right_to_depart, DHR_invite_the_enclave_congress, DHR_negotiate_the_origin_settlement, and DHR_offer_a_shared_horizon; it also reported unsatisfied route modifiers for the crisis choices. These results are not campaign probabilities because the evaluator fixture could not express the full external-factor/prerequisite history surface.

The adapter documents a uniform_score_race selection rule and states that normalized probability is only valid with a complete eligible pool and declared external factors. Because eligibility and external factors remained incomplete, this audit deliberately withholds normalized probabilities and makes no balance inference from raw rankings. A callable chaosx_ai_probability_auditor subagent route was not exposed in this runtime; the direct MCP inspect/evaluate artifacts are evidence and an explicit blocker for the parent’s required auditor-mediated baseline/compare pass, not a substitute for that pass.

The first direct evaluator attempt also confirmed the schema blocker: scenario-level externalFactors, focusesCompleted, and facilities keys are rejected, and state-level external factor declaration was not recognized by the adapter. The parent should obtain the auditor’s supported fixture format before changing any AI weight and then run the same four scenarios through hoi4.probability_compare if weights are altered.

## High-priority parent follow-ups

1. Route the repeated helper families above to accepted downstream consumers, beginning with diplomatic credit and origin-host reclamation, while preserving the 88-ID graph and three regimes.
2. Decide which history-only receipt flags need real readers, especially dhrondan_enclave_crisis_resolved, dhrondan_enclave_congress_invited, dhrondan_enclave_intelligence_network_active, dhrondan_human_airwaves_monitored, and dhrondan_two_world_operatives_available.
3. Obtain a valid chaosx_ai_probability_auditor route and scenario fixture for contact, arrival, facilities, war, route, and prerequisite state before any AI-weight patch; compare identical scenarios after a patch.
4. Retry hoi4.focus_render and discover or restore a focus-compare endpoint before claiming final visual or before/after evidence. The current normal-zoom raster is usable review evidence but does not replace the blocked renderer/compare calls.
5. Reassess the 70 spacing warnings under an accepted DHR layout policy; no crossing, overlap, long-connector, ownership, prerequisite, icon, localisation, or count defect was confirmed in this pass.

## Validation and skipped work

Completed task-specific validation included source ID/count checks, MCP focus inspect, normal-zoom focus raster, prerequisite/mutual-exclusion/shortcut/filter checks, icon base/shine/texture resolution, localisation key and BOM checks, route-plan ID/count checks, read-only landing-cost and untrainable-cohort checks, and inspection of the vanilla focus/AI precedent and offline wiki/documentation required by AGENTS.md and the focus-tree skills.

Skipped or blocked validation is limited to the repeated 180-second hoi4.focus_render timeout, the unavailable hoi4.focus_compare route, and the incomplete probability external-factor scenario schema. Hearts of Iron IV was not launched, and no live-game validation was claimed; live acceptance remains the user’s responsibility.

No simplifications were implemented by this audit. Broad reward repetition, history-only flags, optional AI-pool omissions, spacing warnings, and the MCP probability/render/compare blockers are explicitly carried forward rather than hidden behind invented content.

