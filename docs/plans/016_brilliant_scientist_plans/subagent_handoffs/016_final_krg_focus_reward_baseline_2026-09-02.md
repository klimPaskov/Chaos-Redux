# Event 016 KRG focus reward and consumer baseline

Date: 2026-09-02.

Status: read-only bounded baseline audit for the existing 100-focus tree, its focus-owned rewards, and their existing decision, mission, event, idea, scripted, and terminal consumers.

This is not a completion claim and it does not include gameplay, localisation, asset, AI-weight, or source patches.

## Scope and constraints

Audited the KRG focus tree and linked consumer surfaces only: common/national_focus/016_brilliant_scientist_kruger_state_focus.txt, common/scripted_effects/016_brilliant_scientist_focus_effects.txt, common/scripted_effects/016_brilliant_scientist_effects.txt, common/scripted_effects/016_brilliant_scientist_country_effects.txt, common/scripted_effects/016_brilliant_scientist_project_force_effects.txt, common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt, common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt, common/scripted_triggers/016_brilliant_scientist_triggers.txt, common/script_constants/016_brilliant_scientist_constants.txt, common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt, common/ideas/016_brilliant_scientist_focus_ideas.txt, common/ideas/016_brilliant_scientist_country_ideas.txt, common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt, localisation/english/016_brilliant_scientist_focus_l_english.yml, the Event 016 decision files, and their categories.

The binding design reference was docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md. The offline national-focus reference was paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md, whose prerequisite rule at the interaction-with-other-focuses section states that multiple focus entries in one prerequisite block are OR and separate prerequisite blocks are AND.

No new focus, country, branch, GUI, evolution, achievement, superevent, technology family, or geometry was proposed.

## Priority disposition

### P1 findings

None confirmed in static source review.

There is no focus-set reward with zero consumer in common. The 100-focus tree has 173 unique directly set brilliant_scientist_focus_* flags; 160 occur in exactly one concrete decision block, 10 occur in two concrete decision blocks, and three are category-only visibility seeds. The category-only seeds are brilliant_scientist_focus_unlock_paleogenetics_category, brilliant_scientist_focus_unlock_xenobiological_category, and brilliant_scientist_focus_unlock_biological_quarantine.

Do not reopen the withdrawn KRG_sustainable_project_capacity dead-gate finding. Its source block at common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1033-1060 contains one prerequisite block with four mutually exclusive supply focuses, which is correct OR syntax. Its separate available OR repeats the same route acceptance and the reward flags feed the existing capped project-force board and maintenance-audit decisions.

### P2 findings and owner follow-up

1. The three category-only seeds can produce an empty or nearly empty category on the first completion frame because every KRG category is declared visible_when_empty = yes. This is a first-glance/readability risk, not a dead reward. The paleogenetics seed is set by KRG_open_the_restoration_ledger at focus source lines 1528-1548 and its concrete existing actions are brilliant_scientist_krg_designate_paleogenetic_reserve and brilliant_scientist_krg_construct_paleogenetic_hatchery at common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt:14-73. The xenobiology seed is set by KRG_open_the_designed_organism_dossier at lines 1678-1698 and its existing actions are brilliant_scientist_krg_construct_xenobiological_vat_complex and brilliant_scientist_krg_establish_xenobiological_medical_fabrication at common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt:306-366. The biological quarantine seed is set with two concrete safeguards by KRG_make_containment_the_first_doctrine at lines 2222-2245; the existing downstream action is brilliant_scientist_krg_activate_quarantine_and_lockdown_response at common/decisions/016_brilliant_scientist_kruger_state_safeguard_decisions.txt:207-280. If owner review requires an immediate visible action, tighten the existing category visibility to a concrete child-unlock flag or align the existing child unlock in place; do not invent a new decision family.

2. The diplomacy, integration, and terminal tail is shorter in node count than the broad architecture target: KRG_a_state_without_friends through KRG_settle_accounts_with_the_former_host are five focuses, KRG_secure_the_laboratory_corridors through KRG_integrate_by_project are four focuses, and KRG_evolution_four_sovereign_science through the two terminal commitments are three focuses. Each row has an existing concrete consumer and the prior depth follow-up explicitly deferred count-only expansion. Treat this as a P2 continuation/readability question only. If the owner chooses to strengthen it without changing the 100-focus contract, strengthen the existing foreign-interest, recognition, corridor, recovery, integration, global-administration, and terminal decisions rather than adding nodes.

3. Origin AI plans put the four mutually exclusive supply focuses at the same origin factor in the charter, rebellion, and enclave plans at common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:34-40, 67-74, and 98-104. This is static nondifferentiation, not proof of bad AI behavior. Any owner weight change requires the named scenario audit and a before/after probability comparison through the probability auditor. The enclave plan intentionally zeros the submission and singularity focuses and hands off through the commonwealth plan; do not call that a dead route without a live sequencing fixture.

4. The lifecycle contract has two valid counting interpretations. The visible focus lifecycle count is exactly three on every route: one no-modifier summary carrier, one command idea, and one supply idea. Hidden one-per-slot mirrors preserve the former administration, portfolio, and scientific-population modifiers, so the literal active idea-object count can be six while only three are visible focus-created spirits. If the acceptance metric counts hidden ideas literally, the owner must decide whether hidden mirrors are excluded by contract; no same-slot modifier duplication was found.

The former numeric biological stockpile/debit ledger is intentionally retired by the current Event 016 contract. Native raids and separate production, staging, and decision-led deployment transactions own their own receipts. Its absence is not a KRG focus consumer defect and should not be replaced with a free payload fallback.

## Focus MCP evidence

The mandatory focus inspection used workspace mod_chaos_redux_ea3b2d67c2c0, relative path common/national_focus/016_brilliant_scientist_kruger_state_focus.txt, tree brilliant_scientist_kruger_state_focus_tree, and national mode.

hoi4.focus_inspect returned status ok and code FOCUS_INSPECTED with focusCount 100, resolvedTitleCount 100, diagnosticCount 0, crossingCount 0, nodeIntersectionCount 0, longConnectorCount 0, and layoutHash 7a0f5017eea9a6d0a7131d07075d2bd848eeb092f5e870f3dc4bda605ec5ea39. Its sole warning was FOCUS_LOCALISATION_REFERENCE_MISSING for the unrelated vanilla continuous_restrict_freedom entry.

Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2844a32298eccfe04fa1d21e3a3ffa065b28cc626ffc86f6eae4e5cd0a01a0bf/60f1676b3e2d6b70bc6b852339ebf8b39cadc6dd50299fb0649f90f224c49ae6/focus-inspect.6b89499802012141.json.

hoi4.focus_render returned status ok and code FOCUS_RENDERED with the same layout hash and no KRG blocking diagnostics. It produced a 9456 by 2556 render.

Rendered HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d516088b64605a3850f3c4aa434b5abd686095193e25bf76ce27d58c413423d1/a539c3bf3ac085aa36703aeac6395216fcee28a9b30c767f1d6e4573817a5b15/brilliant_scientist_kruger_state_focus_tree.focus.html.

Rendered SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47ce06cd96e1426329b76afeda9aab2f9b7d3a3355239a976ebbf9490f2cb3d9/f67980b751d44b7f89980b0502188ac5cd21a3814d2c75c14a61ec6b7a3bd862/brilliant_scientist_kruger_state_focus_tree.focus.svg.

Rendered JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58486f227fc4a55173a06ccceb2f3e546c528f774971399e1f0bb47edb4a2db7/b422a92ebc9519153dfb8fe18bedab1078aacae02ef125222b4c54d560fdd9a1/brilliant_scientist_kruger_state_focus_tree.focus.json.

hoi4.focus_raster returned status ok and code FOCUS_RASTERIZED for the same layout and dimensions.

Raster PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecc018518cabe95c0543811619f1e950311400a2be3992413999a1a028dba885f/197f6d73605ed8f623af39092bea439757e6ed1e2a8de106a97cda46591c4968/brilliant_scientist_kruger_state_focus_tree.focus.png.

No focus_rewrite was used because this was a read-only audit.

## Route coverage table

| Route surface | Focus IDs and source range | Reward and consumer coverage | Disposition |
| --- | --- | --- | --- |
| Opening and formation origins | KRG_audit_inherited_portfolio through KRG_complete_the_founding_audit, lines 35-290 | Foundation category, charter transfer, rebellion defense, enclave corridor, takeover consolidation, finite staff, facility security, supply repair, command, and founding-policy decisions in the 016 foundation decision file. | Covered; no unconsumed opening reward. |
| Governance and identity | KRG_define_the_states_purpose through KRG_the_project_synthesis, lines 293-813 | Existing constitutional, directorate, human, clone, machine, temporal, xenobiological, and synthesis event/decision consumers; route forms use existing scripted form effects. | Covered; identity lock and route mutex behavior are source-valid. |
| Economy and supply | KRG_stabilize_the_laboratory_economy through KRG_sustainable_project_capacity, lines 816-1060 | Existing budget, power, rail/port, stage-ledger, prototype-repair, production-lane, four mutually exclusive supply, capped-board, and maintenance-audit decisions. | Covered; sustainable capacity prerequisite is intentionally OR. |
| Conventional security | KRG_restore_the_ordinary_chain_of_command through KRG_a_council_of_project_commanders, lines 1063-1221 | Existing paid recruitment/training/garrison, officer amnesty event, facility repairs, counterintelligence, airspace warning, general-staff, and project-council/rivalry consumers. | Covered; command choices are mutually exclusive or reset through existing helpers. |
| Cloning | KRG_audit_the_growth_halls through KRG_the_replicated_host, lines 1224-1372 | Existing clone category, paid growth/medical, identity, drift, registry, recruitment, and bounded production decisions; capstone rebuild is runtime-only. | Covered; no focus-owned free unit. |
| Robotics | KRG_wake_the_assembly_lines through KRG_an_army_of_machines, lines 1375-1525 | Existing robotics category, paid power, repair/salvage, command, rogue-node, recruitment, and bounded production decisions; capstone rebuild is runtime-only. | Covered; no focus-owned free unit. |
| Paleogenetics | KRG_open_the_restoration_ledger through KRG_the_dinosaur_host, lines 1528-1675 | Existing paleogenetics category, paid reserve/hatchery, handlers/veterinary, transport, evacuation, and bounded breeding decisions. The category seed itself is category-only. | Covered with P2 empty-category readability risk. |
| Xenobiology | KRG_open_the_designed_organism_dossier through KRG_the_engineered_legion, lines 1678-1830 | Existing xenobiology category, paid vat/medical, control mode, assault recruitment, red-team, containment, and bounded production decisions. The category seed itself is category-only. | Covered with P2 empty-category readability risk. |
| Portal and strategic transit | KRG_recover_the_transit_logs through KRG_the_strategic_transit_corps, lines 1833-1958 | Existing terminal audit, hardening, depot/supply, breach mission, bounded portal recruitment, and paid insertion decisions. | Covered; prior portal recruitment focus gate is present. |
| Temporal continuity | KRG_authenticate_the_temporal_ledger through KRG_the_continuity_guard, lines 1961-2114 | Existing anchor discovery/authentication, observer, ledger/calibration, named future-warning, stabilization mission, and bounded guard decisions. | Covered; stabilization is intentionally debt-fed, not dead-gated. |
| High-energy, alien, and biological safeguards | KRG_build_an_independent_reactor_grid through KRG_authorize_agents_of_last_resort, lines 2117-2272 | Existing reactor, delivery, interface, laser, biological ledger, dual-key, authentication, segregation, quarantine, and last-resort consumers. Biological quarantine seed is category-only; safeguards remain concrete and paid. | Covered with P2 category/readability risk; no free payload. |
| Diplomacy and former host | KRG_a_state_without_friends through KRG_settle_accounts_with_the_former_host, lines 2275-2339 | Existing foreign-interest registry, recognition/patron/containment, invalid-target cleanup, foreign intelligence, and origin-specific former-host settlement decisions. | Covered; short branch count is deferred P2 only. |
| Expansion and integration | KRG_open_the_scientific_commonwealth through KRG_integrate_by_project, lines 2342-2474 | Existing commonwealth and submission wrappers, voluntary compacts, ultimatums/protectorates, targeted corridors, recovery, and route-specific integration decisions. | Covered; exact existing consumers exist. |
| Continental payoff and terminals | KRG_the_continental_laboratory_network through KRG_commit_to_the_strategic_singularity, lines 2477-2602 | Existing global administration, Evolution IV world route, coalition counterplay, Laboratory World administration/audit, Singularity program/component intelligence/arming/disarmament, and terminal event handoffs. | Covered; late node count is a deferred P2 question, not a missing payoff. |

## Focus-by-focus disposition

The following is a complete 100-focus ledger. C means a concrete existing decision, mission, event, category, or scripted consumer was found. L means the focus also performs an existing lifecycle, form, route, or runtime handoff. S marks a category seed whose exact flag is intentionally consumed by category visibility and whose child actions are unlocked by later existing focus flags. No row below is a confirmed P1 defect.

| Focus | Disposition and existing consumer |
| --- | --- |
| KRG_audit_inherited_portfolio | C/L: calls the existing project-force runtime rebuild, lifecycle audit, foundation category, and route-layout refresh at focus source lines 45-51. |
| KRG_ratify_the_charter_transfer | C: sets four charter receipts consumed by the existing ratify_charter_transfer decision in the foundation decisions. |
| KRG_hold_the_rebellion_perimeter | C/L: fortifies the primary facility and exposes primary-defense and former-host military planning decisions. |
| KRG_keep_the_enclave_alive | C: exposes the enclave corridor/patron mission and emergency-access negotiation decisions. |
| KRG_secure_the_captured_ministries | C: exposes institutional consolidation, captured-domain audit, and host-appointment review event consumers. |
| KRG_count_the_surviving_staff | C: exposes the finite roster and staff-amnesty/recruitment consumers. |
| KRG_secure_the_laboratory_heartland | C/L: repairs the valid primary facility and exposes the primary-site security mission. |
| KRG_repair_the_supply_spine | C: exposes targeted supply-spine repair decisions. |
| KRG_form_the_provisional_command | C: exposes surviving-officer, force-cap readout, and maintenance-readout consumers. |
| KRG_complete_the_founding_audit | C/L: refreshes route layout and exposes state-foundation, government, economy, security, and foreign-policy lanes. |
| KRG_define_the_states_purpose | C: exposes the constitutional congress event and population/project bloc ledger. |
| KRG_preserve_the_directorate | C: exposes direct appointments and laboratory decrees. |
| KRG_rule_by_demonstration | C: exposes public and coercive project-demonstration decisions. |
| KRG_the_sovereign_directorate | C/L: forms the sovereign directorate through brilliant_scientist_focus_form_sovereign_directorate and exposes direct-rule planning. |
| KRG_restore_human_government | C: exposes human civil service, rights commission, and clone-property policy decisions. |
| KRG_convene_the_scientific_assembly | C: exposes the scientific assembly event and public budget/inspection decisions. |
| KRG_the_human_scientific_republic | C/L: forms the human scientific republic and exposes rights-respecting integration. |
| KRG_hear_the_replicated_petition | C: exposes the clone personhood event and clone legal-status decisions. |
| KRG_clones_are_citizens | C: sets the citizenship law and exposes settlement/education decisions. |
| KRG_clones_are_cohorts | C: sets the cohort law and exposes maturation priorities and identity-pressure crises. |
| KRG_replicated_sovereignty | C/L: forms the replicated state and exposes the existing clone population-transition decision. |
| KRG_hear_the_machine_network | C: exposes the machine network standing event and machine-status decisions. |
| KRG_human_machine_partnership | C: locks supervisory keys and exposes mixed administration/repair consumers. |
| KRG_the_replacement_protocol | C: exposes ministry replacement missions and machine sabotage/schism crises. |
| KRG_machine_ascendancy | C/L: forms the machine state and exposes machine population transition. |
| KRG_authenticate_krugers_continuity | C: exposes the continuity-authentication event. |
| KRG_settle_the_succession_paradox | C: exposes temporal succession settlement and claimant-scar consumers. |
| KRG_the_temporal_continuum | C/L: forms the Temporal Continuum and exposes continuum-government decisions. |
| KRG_xenobiological_ascendancy | C/L: forms xenobiological ascendancy and exposes engineered-population transition. |
| KRG_the_project_synthesis | C/L: validates the existing synthesis ledger and exposes synthesis-government decisions. |
| KRG_stabilize_the_laboratory_economy | C: exposes the facility-budget ledger and paid-maintenance requirement. |
| KRG_restore_the_power_grid | C/L: restores the primary power grid and exposes paid grid expansion. |
| KRG_reconnect_rail_and_port | C: exposes targeted rail repair and coastal-port alternative decisions. |
| KRG_document_the_carried_portfolio | C/L: records the documented portfolio and exposes exact stage-ledger and replication-standardization decisions. |
| KRG_reopen_the_prototype_works | C: exposes targeted prototype repair, board-capacity investment, and valid production lanes. |
| KRG_conventional_supply_corps | C/L: selects the existing conventional supply idea and exposes truck/train depots. |
| KRG_automated_supply_network | C/L: selects the existing automated supply idea and exposes node-repair convoys. |
| KRG_portal_supply_network | C/L: selects the existing portal supply idea and exposes terminal depot linking. |
| KRG_biological_supply_network | C/L: selects the existing biological supply idea and exposes family-specific logistics. |
| KRG_sustainable_project_capacity | C: exposes the capped project-force board and maintenance-audit mission; its single four-entry prerequisite block is correct OR syntax. |
| KRG_restore_the_ordinary_chain_of_command | C: exposes paid conventional recruitment, training, and garrison templates. |
| KRG_recall_the_defector_officers | C: grants the bounded Army Experience amount and exposes the officer amnesty/purge event. |
| KRG_laboratory_engineer_battalions | C: exposes engineer support and paid facility repairs. |
| KRG_found_the_counterintelligence_bureau | C/L: establishes the existing counterintelligence agency and exposes its operations. |
| KRG_shield_the_laboratory_airspace | C/L: shields the primary airspace and exposes air/missile warning missions. |
| KRG_a_general_staff_for_the_state | C/L: selects the existing general-staff command idea and battle-plan decisions. |
| KRG_a_council_of_project_commanders | C/L: selects the existing project-council command idea and rivalry/crisis decisions. |
| KRG_audit_the_growth_halls | C: exposes the clone infrastructure category; later paid growth consumers are present. |
| KRG_secure_the_nutrient_chain | C: exposes paid growth-site and medical decisions. |
| KRG_write_the_identity_register | C: exposes the clone identity register and infiltrator detection. |
| KRG_field_the_clone_cadres | C/L: rebuilds runtime and exposes replicated-guard recruitment. |
| KRG_stabilize_replication_drift | C: exposes clone-drift mission and registry repair. |
| KRG_the_replicated_host | C/L: rebuilds runtime and exposes bounded clone production; the route also resets the clone officer command choice. |
| KRG_wake_the_assembly_lines | C: exposes the robotics production category. |
| KRG_secure_the_machine_power_backbone | C: exposes paid machine power nodes and records the machine-power burden. |
| KRG_standardize_frame_repair | C: exposes frame repair/salvage and robotics maintenance. |
| KRG_write_the_machine_command_protocol | C/L: rebuilds runtime and exposes autonomous-frame recruitment and machine command choice. |
| KRG_air_gap_the_rogue_nodes | C: exposes rogue-node containment and controlled node recapture. |
| KRG_an_army_of_machines | C/L: rebuilds runtime and exposes bounded robotics production; the route also resets the machine command choice. |
| KRG_open_the_restoration_ledger | S: category-only paleogenetics seed at source lines 1528-1548; concrete reserve/hatchery actions follow from KRG_designate_breeding_reserves. |
| KRG_designate_breeding_reserves | C: exposes paid reserve designation and paleogenetic hatchery construction. |
| KRG_train_handlers_and_veterinarians | C: exposes finite handler recruitment and veterinary support. |
| KRG_build_the_transport_pens | C/L: rebuilds runtime and exposes paleogenetic shock-pack recruitment and transport-pen construction. |
| KRG_drill_for_the_great_escape | C: exposes paleogenetic escape response and evacuation/recapture. |
| KRG_the_dinosaur_host | C/L: rebuilds runtime and exposes bounded paleogenetic breeding. |
| KRG_open_the_designed_organism_dossier | S: category-only xenobiology seed at source lines 1678-1698; concrete vat and medical actions follow from KRG_build_the_vat_complexes. |
| KRG_build_the_vat_complexes | C: exposes paid xenobiological vat construction and medical fabrication. |
| KRG_lock_the_control_channel | C: exposes the xenobiological control-mode event. |
| KRG_seal_the_containment_cells | C/L: rebuilds runtime and exposes xenobiological assault recruitment. |
| KRG_red_team_the_autonomous_nest | C: exposes xeno control countertests and autonomous-nest containment. |
| KRG_the_engineered_legion | C/L: rebuilds runtime and exposes bounded xenobiological production. |
| KRG_recover_the_transit_logs | C: exposes the terminal audit category. |
| KRG_harden_the_terminal_rings | C: exposes terminal fortification and shutdown/dual-key decisions. |
| KRG_link_the_depot_network | C: exposes bounded terminal transit and terminal supply links. |
| KRG_close_the_transit_breach | C: exposes transit-breach missions and compromised-terminal closure. |
| KRG_the_strategic_transit_corps | C/L: rebuilds runtime and exposes bounded portal recruitment and paid strategic insertions. |
| KRG_authenticate_the_temporal_ledger | C: exposes temporal authentication and anchor-discovery missions. |
| KRG_fortify_the_anchor | C/L: fortifies the authenticated temporal anchor and exposes observer teams. |
| KRG_found_the_synchronization_bureau | C: exposes temporal ledger readouts and paid calibration. |
| KRG_issue_bounded_future_warnings | C: exposes the named warning action and marks the temporal warning contract. |
| KRG_accept_the_stabilization_window | C/L: calls the existing stabilization helper and exposes its timed supervision mission after the debt gate is met. |
| KRG_the_continuity_guard | C/L: rebuilds runtime and exposes bounded temporal guard operations. |
| KRG_build_an_independent_reactor_grid | C: exposes targeted reactor, contamination-response, and rare-material procurement decisions. |
| KRG_prepare_strategic_delivery_architecture | C: exposes delivery-network, hardened-command, and delivery-counterintelligence decisions. |
| KRG_train_the_interface_specialists | C: exposes finite interface-specialist recruitment and artifact-interface security. |
| KRG_arm_the_alien_cohorts | C/L: rebuilds runtime and exposes bounded alien laser production through the existing exotic category. |
| KRG_make_containment_the_first_doctrine | C/S: exposes consequence-ledger, safe-stockpile/vaccine, and delivery-authentication decisions; its biological-quarantine flag is category-only. |
| KRG_authorize_agents_of_last_resort | C: exposes the canonical biological last-resort authority and records its consequence-ledger requirement. |
| KRG_a_state_without_friends | C: exposes foreign-interest, recognition/patron/containment, and invalid-target cleanup consumers. |
| KRG_found_the_foreign_intelligence_bureau | C/L: establishes foreign intelligence and exposes its operations. |
| KRG_settle_accounts_with_the_former_host | C: exposes origin-specific former-host settlement. |
| KRG_open_the_scientific_commonwealth | C/L: opens the existing commonwealth population/lifecycle route and exposes voluntary scientific compacts. |
| KRG_build_the_submission_network | C/L: opens the existing submission route and exposes ultimatums and protectorates. |
| KRG_secure_the_laboratory_corridors | C: exposes targeted laboratory-corridor operations after sustainable capacity and one command choice. |
| KRG_recover_the_stolen_facilities | C: exposes one evidence-backed recovery target and archive capture/safe dismantlement. |
| KRG_integrate_by_project | C: exposes route-specific integration and compliance/time requirements. |
| KRG_the_continental_laboratory_network | C: registers the network and exposes the global administration score. |
| KRG_evolution_four_sovereign_science | C/L: records Evolution IV world-program, route, scientist/facility, and coalition-counterplay consumers and refreshes world-threat source. |
| KRG_commit_to_the_laboratory_world | C/L: commits through brilliant_scientist_commit_to_lab_world and exposes the existing Laboratory World administration/audit terminal decisions. |
| KRG_commit_to_the_strategic_singularity | C/L: calls brilliant_scientist_focus_commit_to_singularity_doctrine, which sets the existing singularity-program flag and component-intelligence consumer; terminal arming/disarmament decisions remain downstream. |

## Reward consumer ledger

The direct focus reward scan found 173 unique brilliant_scientist_focus_* flags set by focus completion rewards.

160 flags map to exactly one concrete decision block.

The following 10 shared flags map to two concrete decision blocks each and are intentionally shared gates rather than duplicate rewards: brilliant_scientist_focus_clone_citizenship_law, brilliant_scientist_focus_clone_cohort_law, brilliant_scientist_focus_unlock_canonical_biological_last_resort_actions, brilliant_scientist_focus_unlock_global_submission_integration_administration, brilliant_scientist_focus_unlock_laboratory_world_program, brilliant_scientist_focus_unlock_paid_reserve_and_hatchery_designation, brilliant_scientist_focus_unlock_project_synthesis_government, brilliant_scientist_focus_unlock_recognition_patron_and_containment_reactions, brilliant_scientist_focus_unlock_singularity_component_intelligence_event, and brilliant_scientist_focus_unlock_terminal_depot_linking.

The following three exact flags have no matching concrete decision block and are used as category visibility seeds: brilliant_scientist_focus_unlock_biological_quarantine at common/decisions/categories/016_brilliant_scientist_kruger_state_categories.txt:72-80, brilliant_scientist_focus_unlock_paleogenetics_category at lines 42-49, and brilliant_scientist_focus_unlock_xenobiological_category at lines 51-58. All three categories contain later child decisions gated by their own concrete focus receipts, and all categories explicitly use visible_when_empty = yes. Therefore these are UI seeds with a first-glance risk, not unconsumed focus rewards.

The singularity helper adds one additional consumer flag that is not a direct set_country_flag line in the focus source: brilliant_scientist_focus_commit_to_singularity_doctrine sets brilliant_scientist_focus_unlock_singularity_program at common/scripted_effects/016_brilliant_scientist_focus_effects.txt:384-389. The existing terminal category and component/arming/disarmament decisions consume that flag at common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt:155-200 and common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:434-515.

Representative concrete consumer chains are as follows.

- Opening charter flags feed brilliant_scientist_krg_ratify_charter_transfer at common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt:47-68.
- Opening enclave flags feed brilliant_scientist_krg_secure_enclave_corridor at lines 71-88.
- Takeover flags feed brilliant_scientist_krg_begin_ministry_consolidation at lines 117-155.
- Defense flags feed brilliant_scientist_krg_begin_primary_facility_defense at lines 511-542.
- Project council and maintenance flags feed brilliant_scientist_krg_coordinate_project_commanders and brilliant_scientist_krg_begin_maintenance_audit at lines 611-650.
- Portal capstone flags feed brilliant_scientist_krg_fabricate_portal_transit_batch and the paid strategic insertion decision in common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt.
- Route-specific integration and network flags feed the map-targeted foreign/integration decisions at common/decisions/016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt:210-390.
- Evolution and terminal flags feed the existing terminal category and terminal program decisions at common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt:19-200 and :355-416.

## Project gates and route consumers

No invalid project gate was confirmed.

The focus triggers explicitly delegate to authoritative project history and physical-site readers in common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt and common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt. Examples are cloning deployment requiring a carried deployment record, the growth-site country flag, and an owned growth site; paleogenetic deployment requiring deployment history, sites-ready state, and reserve plus hatchery; xenobiological deployment requiring deployment history, exact control, sites-ready state, vat, and control center; and portal/temporal deployment requiring their corresponding history, facilities, authentication, and control records.

The synthesis focus uses Paleo Deployment, Xeno Deployment, and an OR third-route operational requirement, which matches the contract and is not simplified into a focus-only receipt.

The Evolution IV focus uses one identity completion OR and one project-capstone OR, then the terminal focuses use their dedicated scenario readiness triggers. No focus-only receipt was treated as proof of a project stage.

The temporal chain is intentionally staged. Host initialization sets temporal debt to the zero constant at common/scripted_effects/016_brilliant_scientist_effects.txt:496-498. KRG_issue_bounded_future_warnings exposes a paid named-target action. Its decision trigger is at common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:63-86, and its commit effect sets warning_debt_gain = 40 at common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:388-418; the authoritative warning threshold is 40 in common/script_constants/016_brilliant_scientist_constants.txt:890-902. This crosses the warning threshold in one successful warning action, allowing KRG_accept_the_stabilization_window at focus source lines 2064-2086. The source contains no setter for brilliant_scientist_temporal_stabilization_required; KRG_settle_the_succession_paradox at lines 700-722 therefore remains available without a stabilization requirement. The temporal chain is a paid-action dependency, not a dead gate.

The sustainable-capacity focus has one prerequisite block with four focus entries at focus source lines 1042-1048 and a separate available OR at lines 1046-1058. Per the offline national-focus reference, the prerequisite is OR. Do not split it into four AND blocks or reduce it to one supply focus.

## Unit causality and maximum focus-created forces

The focus-owned effects file declares at common/scripted_effects/016_brilliant_scientist_focus_effects.txt:4-6 that focus effects never grant a project stage, fabricate an agent, spawn a force, or create a unit.

The runtime rebuild at common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:426-546 is explicitly idempotent and never spawns units. Focus capstones call this rebuild for the clone, robotics, paleogenetic, xenobiological, portal, temporal, and alien routes.

The only create_unit calls are the bounded setup/history materializers at common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:601-831. The one-time history dispatcher at lines 848-900 calls only eligible family materializers, behind its transaction and persistent receipt guards. It is invoked by formation setup and history transfer, not by focus completion. The alien-arms path reconciles the source-counted contact API at lines 802-806 and creates no project-force unit.

Disposition: focus-created units max out at zero. A formation setup may materialize at most one bounded opening formation per eligible project family, but that is history/setup-owned and must not be described as a focus reward. Subsequent clone, robotics, paleogenetic, xenobiological, portal, temporal, and alien production/recruitment decisions are paid and capped. No noncausal free-unit or free-stockpile focus reward was found.

## Focus-created spirit lifecycle trace

The visible summary layer is defined at common/ideas/016_brilliant_scientist_focus_ideas.txt:27-75 and has no modifiers. The hidden administration, portfolio, and scientific-population mirrors are invisible and carry the old modifiers at lines 77-222.

brilliant_scientist_focus_refresh_visible_lifecycle_summary at common/scripted_effects/016_brilliant_scientist_focus_effects.txt:27-76 clears all visible summaries before adding exactly one summary according to the current population or route state. brilliant_scientist_focus_clear_hidden_administration, brilliant_scientist_focus_clear_hidden_portfolio, and brilliant_scientist_focus_clear_hidden_scientific_population at lines 79-100 remove prior mirrors before a new slot is written. brilliant_scientist_focus_hide_original_lifecycle_mechanics at lines 106-120 removes the original modifier idea before adding its hidden one-per-slot mirror.

Every route has the same visible maximum: one summary carrier, one command idea, and one supply idea, for three visible focus-created spirits. The command setters at lines 143-200 remove competing command ideas before writing one canonical command idea, and the four supply setters are mutually exclusive in the focus tree and replace competing supply ideas through the existing country helpers.

The literal active idea-object maximum can be six: three visible carriers plus one hidden administration, one hidden portfolio, and one hidden scientific-population mirror. The hidden copies are not additional visible spirits and their source modifiers are not duplicated by the no-modifier visible summaries. This distinction must be resolved against the contract's wording if the owner uses a raw idea count.

Route trace:

- Opening and unformed KRG: setup carries the original liabilities; focus 001 hides their modifiers and writes one summary while command and supply remain one each.
- Sovereign directorate, human republic, replicated state, machine state, Temporal Continuum, xenobiological ascendancy, and synthesis: one route-specific hidden administration mirror plus one hidden portfolio and one hidden population mirror may coexist, while the visible count remains three.
- Scientific Commonwealth and submission network: the population helper clears the former hidden population slot, writes the existing center/network modifier, and refreshes the one visible summary; no additional visible spirit is added.
- Evolution IV and both terminal focuses add no lifecycle spirit; they set world and terminal receipts only.

No duplicate same-slot original-plus-hidden modifier path was found. The sovereign wrapper adds its hidden mirror and then refresh_visible_lifecycle_summary removes/re-adds the no-modifier visible summary, so it does not double the original route modifiers.

## Icon coverage

The focus source has 100 icon references and 100 unique intended focus icon IDs.

interface/016_brilliant_scientist_kruger_state_focus.gfx contains 200 GFX_goal_KRG_ sprite mentions, representing 100 normal/shine pairs.

gfx/interface/goals/016_brilliant_scientist contains 100 goal_KRG_*.dds textures, matching the 100 focus IDs.

No duplicate or missing KRG focus icon ID was found. The focus raster decoded successfully. The only focus MCP localisation warning concerns unrelated vanilla continuous_restrict_freedom, not a KRG icon or title.

## Localisation and reward mismatch list

No static KRG title, description, or effect-tooltip key is missing: 100 focus IDs have 100 titles, 100 descriptions, and 100 effect tooltips in localisation/english/016_brilliant_scientist_focus_l_english.yml.

The localisation file has a UTF-8 BOM. Static key presence and sampled reward text match the source effects, including the no-free-output wording for project-force and conventional-recruitment rewards, the capped-board wording for sustainable capacity, and the debt/action wording for temporal warnings and stabilization.

No focus name or description was found to contradict its reward. No reward-tooltip mismatch was confirmed without live UI state.

## AI behavior gaps and probability evidence

The AI plan file contains 19 KRG plans covering origins, takeover post-audit, project routes, biological safeguards, commonwealth/submission, and both terminal commitments. All 100 focus IDs occur in at least one plan, and all 100 focus blocks have an ai_will_do block.

Static plan risks are limited to same-factor origin supply choices at lines 34-40, 67-74, and 98-104, and the intentional enclave handoff that zeros submission and singularity in the enclave plan at lines 98-106. Source weights do not prove AI behavior.

The direct mandatory probability route used adapter national_focus_ai_will_do, the exact 100 actual focus IDs, the focus source, and workspace mod_chaos_redux_ea3b2d67c2c0. hoi4.probability_inspect returned status ok and code PROBABILITY_SOURCE_INSPECTED with poolComplete = true, candidates = 100, availableCandidates = 0 without a live state, unresolved = 0 at inspection, sourceHash 6751d47ca56404bb7e1ce23cf2eb4836f15c96079ba41baabbc68f4b81a69e8c, and sourceRevision a646df40fb54999ea3a8fbaaee54c60b72ce27f202d5a7488394c30ebf41b44f.

Probability inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77e74f2db0a5dc5a63c1bef8f007d1eda1540020ed8a35904f8df26c2b25f036/636a41c9c19ff324a76856dbe94b4455a3b2091cd02e4c5af23332e1c02e4717/probability-inspect-6751d47ca564.json.

The named read-only fixture evaluation used KRG_BASE_EMPTY_2026_09_02, KRG_CHARTER_ORIGIN_2026_09_02, KRG_CLONE_ROUTE_2026_09_02, and KRG_LATE_COMMONWEALTH_2026_09_02. hoi4.probability_evaluate returned status ok and code PROBABILITY_ANALYZED_PARTIAL with analysisId probability-59a69b5ffcac541a53e2faa0, candidates = 400, unresolved = 1391, diagnostics = 100, and four visual resources. The tool kept uncertainty visible and withheld normalized probabilities because the fixtures do not provide complete campaign state. Its NEVER_ELIGIBLE outcomes are fixture/input incompleteness, not runtime dead-route evidence.

Probability evaluation artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1789e218a604b85682860301050ce0a9c0b0035f3d8a24d79a55e94004e0344/4f448ca17aae13927660eff967742d5897636ea7f2ad7e9d5d901d35f33e6146/probability-59a69b5ffcac541a53e2faa0.json.

Ranking raster: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d923a95c353fa8112843dc11eab6bb857fb661b8f66e581cac903d1d6cd4096/857b0e9e86c0df4f734e12c5ab13fed17eb097c4e7080dbf58359ad2026ec619/probability-probability-59a69b5ffcac541a53e2faa0-ranking.png.

Unresolved raster: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64ee4fbd9f1b8b5aef1ec8630e3fae6a193009f02db4e52da5d9a51b790082c0/35a27aa68b3e1092b7f88fc22dcdef251841e3c89188daf8fdf9e00524af9c57/probability-probability-59a69b5ffcac541a53e2faa0-unresolved.png.

The custom chaosx_ai_probability_auditor route was not exposed as a callable tool in this runtime. Direct HOI4 probability inspect/evaluate was used instead. No probability sweep was run because no approved numeric scenario dimension was declared, and no before/after owner weight patch existed for probability_compare.

Exact exploratory MCP errors retained for traceability:

- A probability source request that included identifier brilliant_scientist_kruger_state_focus_tree returned status ok, code PROBABILITY_SOURCE_DISCOVERED, identifier_not_found, candidates = 0, and candidatePoolMatches = 100. It was discarded in favor of the exact source-path and exact-ID inspect.
- An early evaluate request using placeholder IDs KRG_001 through KRG_100 returned status error, code PROBABILITY_SURFACE_EMPTY, and blocker “No weighted blocks matched this request” with candidatePoolMatchCount = 0. It was discarded and rerun with the 100 actual focus IDs.

## Missing, simplified, and blocked content

No missing focus ID, focus AI block, focus localisation key, KRG focus icon, direct focus-set consumer, or concrete route consumer was confirmed.

The only source simplification visible in this bounded audit is the intentional category-only seed behavior for paleogenetics, xenobiology, and biological quarantine. It is already represented by existing category and child-decision architecture and does not justify a new family.

The shorter diplomacy, integration, and terminal tails remain the accepted 100-focus architecture and prior count-only depth follow-up; they are not a newly proven consumer gap.

The retired numeric CBRN stockpile/debit ledger and the absence of focus-owned unit spawning are contract decisions, not omissions.

No gameplay file, localisation file, asset, AI plan, or other gameplay source was changed. No commit was created.

## Recommended owner actions

1. Keep KRG_sustainable_project_capacity unchanged unless a new design decision changes the route model; its one prerequisite block is correct OR syntax under the offline national-focus reference.

2. Decide whether empty category visibility is acceptable at the first focus completion frame. If not, use the existing child decision flags and category visibility blocks in place; do not add a new category or focus branch.

3. If origin AI differentiation is required, run the custom probability-auditor workflow on the same named origin and route scenarios, patch only the existing plan factors, and run probability_compare before claiming improved AI behavior. This baseline's partial fixture result is not an AI behavior claim.

4. Confirm the spirit-cap accounting convention: visible focus-created spirits are three per route, while hidden one-per-slot mirrors can make six active idea objects. No duplicate modifier carrier was found.

## Validation limits

This handoff records source scans, required offline wiki and vanilla documentation review, focus inspect/render/raster evidence, consumer tracing, icon/localisation counts, and partial probability evidence.

No game launch, log search, live campaign test, or live UI acceptance was performed.
