# Event 016 KRG 100-focus implementation handoff

Date: 2026-07-16

Owner: `krg_focus_tree_architect`

Status: the bounded focus-tree implementation tranche is implemented. All 180 focus-produced contracts have executable consumers in the Event 016 focus, decision, mission, or event surfaces. The separate decision/event handoff owns the downstream implementation details and route-achievement receipts.

## Scope and changed files

- `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`
- `common/script_constants/016_brilliant_scientist_focus_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_focus_effects.txt`
- `common/ideas/016_brilliant_scientist_focus_ideas.txt`
- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`
- `interface/016_brilliant_scientist_kruger_state_focus.gfx`
- `localisation/english/016_brilliant_scientist_focus_l_english.yml`
- `docs/assets/016_brilliant_scientist/kruger_state_focus_icon_manifest.md`
- `docs/plans/016_brilliant_scientist_plans/016_kruger_state_100_focus_architecture.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_focus_consumer_ledger.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_focus_implementation_handoff.md`

No binary assets, spreadsheets, achievements, super-events, project-force source, country-formation source, or non-016 files were edited.

## Exact architecture implementation

- Exactly 100 manually authored focuses exist in architecture order 001-100.
- All 100 IDs, coordinates, durations, prerequisites, mutual exclusions, route gates, completion semantics, AI weights, and reward contracts were transcribed from the accepted architecture.
- Every focus has an English title, description, and exact effect tooltip. Historical checks use `has_completed_focus = KRG_*`; 100 redundant setter-only `_completed` receipts were removed.
- The source contains no project-stage grant, missing-agent grant, force spawn, unit creation, or formation-history application.
- Project route stages require the live operational project readers. Personal force history cannot independently satisfy an operational gate.
- Project capstones call the canonical runtime rebuild only after their operational gates pass.
- Focus 042, `KRG_recall_the_defector_officers`, remains the intentionally optional officer-recovery/event side focus from 041. The mandatory security spine remains 041 -> 043/044 -> 045 -> 046/047.

## Canonical Event 016 integration

- The project-family gates delegate to the canonical focus-safe operational triggers for Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Biological Weapons, Alien Arms, and Temporal Manipulation.
- High Energy and Rocketry use explicit same-file status-array readers because they are not project-force families.
- Focus 001 rebuilds the project-force runtime package. If formation interrupted a project, it exposes the paid audit contract without repairing or granting the project:
  - `brilliant_scientist_focus_unlock_interrupted_project_audit`
  - `brilliant_scientist_focus_interrupted_project_family`
  - `brilliant_scientist_focus_interrupted_project_stage`
  - `brilliant_scientist_focus_interrupted_project_capacity_delta`
- Former-host planning reads `event_target:brilliant_scientist_kruger_state_former_host_persistent`.
- Live force caps remain authoritative: clone 8, robot 8, paleogenetic 6, xenobiological 6, portal 4, temporal 3, and alien 4. The one-time opening conventional package remains clamped to 1–8; the authoritative live conventional ceiling is 12 and later growth remains paid. Biological Weapons retains its canonical agent/stockpile model rather than a division cap.
- Focus 098 calls `brilliant_scientist_refresh_world_threat_source` only after opening the global-program surfaces. It sets no shared threat, world-end, super-event, submission, conquest, settlement, or disarmament receipt directly.
- Singularity sequencing is safe: an already completed theory stage may commit canonically; otherwise focus 100 unlocks the Singularity program and the canonical theory-completion effect performs the commitment when theory finishes. No pending receipt is required, no theory stage is skipped, and the decision path remains payable.

## Required narrow helpers resolved

- `brilliant_scientist_form_sovereign_directorate` uses the shared route clear, KRG identity, politics, popularities, and leader ideology conventions.
- `brilliant_scientist_can_unlock_synthesis` requires separate operational Paleogenetic and Xenobiological Deployment plus a third eligible carried route.
- `brilliant_scientist_unlock_synthesis` validates political synthesis while preserving the two biological ledgers.
- `brilliant_scientist_refresh_kruger_focus_route_layout` is the focus-owned layout refresh hook.
- Targeted primary-facility and temporal-anchor construction effects validate the live state target and current ownership/control before adding structures.
- Intelligence-agency helpers create or upgrade only with La Résistance enabled. There is no gameplay substitute when the DLC is unavailable.

## Five-liability lifecycle resolution

Focus 001 resolves the five-visible-liability conflict without removing any mechanical penalty or successor bonus:

- Administration, portfolio, and scientific-population mechanics are transferred one-for-one into hidden, mutually exclusive slot mirrors. Their modifiers copy the canonical ideas exactly.
- One modifier-free visible summary represents those three hidden slots.
- Command and supply remain their canonical visible one-per-slot ideas.
- Later transitions call the canonical lifecycle helper first, transfer its resulting idea into the matching hidden mirror, and refresh the visible summary.
- The intended visible result is exactly three lifecycle spirits: one summary, one command spirit, and one supply spirit.

## AI strategy plans

Exactly 19 named KRG plans provide formation-origin, takeover post-audit, identity, project-family, diplomatic, integration, and terminal sequencing:

- `KRG_charter_republic_plan`
- `KRG_rebellion_directorate_plan`
- `KRG_enclave_survival_plan`
- `KRG_takeover_consolidation_plan`
- `KRG_takeover_post_audit_plan`
- `KRG_clone_sovereignty_plan`
- `KRG_machine_ascendancy_plan`
- `KRG_paleogenetic_plan`
- `KRG_xenobiological_plan`
- `KRG_project_synthesis_plan`
- `KRG_portal_plan`
- `KRG_temporal_plan`
- `KRG_alien_arms_plan`
- `KRG_biological_containment_plan`
- `KRG_biological_last_resort_plan`
- `KRG_commonwealth_plan`
- `KRG_submission_plan`
- `KRG_laboratory_world_plan`
- `KRG_singularity_plan`

## Stable icon contract and art blocker

The interface file registers 100 normal and 100 `_shine` sprite IDs. Each focus uses:

- ID: `GFX_goal_<exact KRG focus ID>`
- DDS: `gfx/interface/goals/016_brilliant_scientist/goal_<exact KRG focus ID>.dds`
- Shine ID: `GFX_goal_<exact KRG focus ID>_shine`

All 100 DDS files are currently absent. This is an explicit art-production handoff: no art was fabricated, borrowed, or substituted. The exact one-row-per-focus source, processed, runtime, and sprite contract is recorded in `docs/assets/016_brilliant_scientist/kruger_state_focus_icon_manifest.md`. The focus tree is therefore not visually complete until the exact registered DDS files are supplied.

## Focus-to-downstream contracts

The focus tranche sets 165 precise persistent unlock contracts. Together with ten decision-state constraints and five lifecycle receipts, the focus package produces 180 stable contracts. All 180 have executable `has_country_flag` consumers. Their producer focus/effect and consumer file locations are recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_kruger_state_focus_consumer_ledger.md` rather than being duplicated as inert completion flags.

- `brilliant_scientist_focus_unlock_air_and_missile_warning_missions`
- `brilliant_scientist_focus_unlock_anchor_discovery_missions`
- `brilliant_scientist_focus_unlock_archive_capture_and_safe_dismantlement`
- `brilliant_scientist_focus_unlock_artifact_interface_security`
- `brilliant_scientist_focus_unlock_autonomous_frame_recruitment`
- `brilliant_scientist_focus_unlock_autonomous_nest_containment`
- `brilliant_scientist_focus_unlock_biological_quarantine`
- `brilliant_scientist_focus_unlock_bounded_clone_production`
- `brilliant_scientist_focus_unlock_bounded_exotic_guard_production`
- `brilliant_scientist_focus_unlock_bounded_future_warning_operations`
- `brilliant_scientist_focus_unlock_bounded_paleogenetic_breeding`
- `brilliant_scientist_focus_unlock_bounded_portal_recruitment`
- `brilliant_scientist_focus_unlock_bounded_robotics_production`
- `brilliant_scientist_focus_unlock_bounded_temporal_guard_operations`
- `brilliant_scientist_focus_unlock_bounded_terminal_transit`
- `brilliant_scientist_focus_unlock_bounded_xenobiological_production`
- `brilliant_scientist_focus_unlock_canonical_biological_last_resort_actions`
- `brilliant_scientist_focus_unlock_capped_project_force_board`
- `brilliant_scientist_focus_unlock_captured_domain_audit`
- `brilliant_scientist_focus_unlock_charter_archive_access`
- `brilliant_scientist_focus_unlock_charter_rail_access`
- `brilliant_scientist_focus_unlock_charter_research_access`
- `brilliant_scientist_focus_unlock_charter_truce_monitor`
- `brilliant_scientist_focus_unlock_clone_drift_mission`
- `brilliant_scientist_focus_unlock_clone_identity_pressure_crises`
- `brilliant_scientist_focus_unlock_clone_identity_register`
- `brilliant_scientist_focus_unlock_clone_infrastructure_category`
- `brilliant_scientist_focus_unlock_clone_legal_status_decisions`
- `brilliant_scientist_focus_unlock_clone_personhood_event`
- `brilliant_scientist_focus_unlock_clone_population_transition`
- `brilliant_scientist_focus_unlock_clone_registry_repair`
- `brilliant_scientist_focus_unlock_clone_settlement_and_education`
- `brilliant_scientist_focus_unlock_coalition_counterplay`
- `brilliant_scientist_focus_unlock_coastal_port_alternative`
- `brilliant_scientist_focus_unlock_coercive_science_demonstrations`
- `brilliant_scientist_focus_unlock_compromised_terminal_closure`
- `brilliant_scientist_focus_unlock_constitutional_congress_event`
- `brilliant_scientist_focus_unlock_contamination_response`
- `brilliant_scientist_focus_unlock_continuity_authentication_event`
- `brilliant_scientist_focus_unlock_continuum_government_decisions`
- `brilliant_scientist_focus_unlock_controlled_node_recapture`
- `brilliant_scientist_focus_unlock_conventional_battle_plans`
- `brilliant_scientist_focus_unlock_conventional_garrison_templates`
- `brilliant_scientist_focus_unlock_conventional_recruitment`
- `brilliant_scientist_focus_unlock_conventional_training`
- `brilliant_scientist_focus_unlock_counterintelligence_operations`
- `brilliant_scientist_focus_unlock_delivery_authentication`
- `brilliant_scientist_focus_unlock_delivery_counterintelligence`
- `brilliant_scientist_focus_unlock_delivery_network_design`
- `brilliant_scientist_focus_unlock_direct_appointments`
- `brilliant_scientist_focus_unlock_direct_rule_plan`
- `brilliant_scientist_focus_unlock_economy_lane`
- `brilliant_scientist_focus_unlock_emergency_access_negotiations`
- `brilliant_scientist_focus_unlock_enclave_corridor_or_patron_mission`
- `brilliant_scientist_focus_unlock_engineer_support`
- `brilliant_scientist_focus_unlock_engineered_population_transition`
- `brilliant_scientist_focus_unlock_exact_project_stage_ledger`
- `brilliant_scientist_focus_unlock_facility_budget_ledger`
- `brilliant_scientist_focus_unlock_family_specific_biological_logistics`
- `brilliant_scientist_focus_unlock_finite_handler_recruitment`
- `brilliant_scientist_focus_unlock_finite_interface_specialists`
- `brilliant_scientist_focus_unlock_finite_scientist_roster`
- `brilliant_scientist_focus_unlock_force_cap_readouts`
- `brilliant_scientist_focus_unlock_foreign_intelligence_operations`
- `brilliant_scientist_focus_unlock_foreign_interest_registry`
- `brilliant_scientist_focus_unlock_foreign_policy_lane`
- `brilliant_scientist_focus_unlock_former_host_military_planning`
- `brilliant_scientist_focus_unlock_frame_repair_and_salvage`
- `brilliant_scientist_focus_unlock_global_administration_score`
- `brilliant_scientist_focus_unlock_global_program`
- `brilliant_scientist_focus_unlock_global_scientist_and_facility_targets`
- `brilliant_scientist_focus_unlock_global_submission_integration_administration`
- `brilliant_scientist_focus_unlock_government_lane`
- `brilliant_scientist_focus_unlock_hardened_command_nodes`
- `brilliant_scientist_focus_unlock_host_appointment_review_event`
- `brilliant_scientist_focus_unlock_human_civil_service`
- `brilliant_scientist_focus_unlock_infiltrator_detection`
- `brilliant_scientist_focus_unlock_interrupted_project_audit`
- `brilliant_scientist_focus_unlock_institutional_consolidation_mission`
- `brilliant_scientist_focus_unlock_invalid_foreign_target_cleanup`
- `brilliant_scientist_focus_unlock_kruger_state_administration`
- `brilliant_scientist_focus_unlock_laboratory_decrees`
- `brilliant_scientist_focus_unlock_laboratory_world_program`
- `brilliant_scientist_focus_unlock_machine_command_choice`
- `brilliant_scientist_focus_unlock_machine_network_standing_event`
- `brilliant_scientist_focus_unlock_machine_population_transition`
- `brilliant_scientist_focus_unlock_machine_sabotage_and_schism_crises`
- `brilliant_scientist_focus_unlock_machine_status_decisions`
- `brilliant_scientist_focus_unlock_maintenance_audit_mission`
- `brilliant_scientist_focus_unlock_maintenance_readouts`
- `brilliant_scientist_focus_unlock_medical_fabrication`
- `brilliant_scientist_focus_unlock_military_maturation_priorities`
- `brilliant_scientist_focus_unlock_ministry_replacement_missions`
- `brilliant_scientist_focus_unlock_mixed_administration_and_repair`
- `brilliant_scientist_focus_unlock_multi_family_coordination`
- `brilliant_scientist_focus_unlock_node_repair_convoys`
- `brilliant_scientist_focus_unlock_officer_amnesty_or_purge_event`
- `brilliant_scientist_focus_unlock_origin_specific_former_host_settlement`
- `brilliant_scientist_focus_unlock_paid_facility_repairs`
- `brilliant_scientist_focus_unlock_paid_grid_expansion`
- `brilliant_scientist_focus_unlock_paid_growth_site_and_medical_decisions`
- `brilliant_scientist_focus_unlock_paid_machine_power_nodes`
- `brilliant_scientist_focus_unlock_paid_reserve_and_hatchery_designation`
- `brilliant_scientist_focus_unlock_paid_strategic_insertions`
- `brilliant_scientist_focus_unlock_paid_temporal_calibration`
- `brilliant_scientist_focus_unlock_paid_vat_complex_construction`
- `brilliant_scientist_focus_unlock_paleogenetic_escape_response`
- `brilliant_scientist_focus_unlock_paleogenetic_evacuation_and_recapture`
- `brilliant_scientist_focus_unlock_paleogenetic_shock_pack_recruitment`
- `brilliant_scientist_focus_unlock_paleogenetics_category`
- `brilliant_scientist_focus_unlock_population_and_project_bloc_ledger`
- `brilliant_scientist_focus_unlock_primary_facility_defense_mission`
- `brilliant_scientist_focus_unlock_primary_site_security_mission`
- `brilliant_scientist_focus_unlock_project_board_capacity_investment`
- `brilliant_scientist_focus_unlock_project_replication_standardization`
- `brilliant_scientist_focus_unlock_project_rivalry_crises`
- `brilliant_scientist_focus_unlock_project_synthesis_government`
- `brilliant_scientist_focus_unlock_public_budget_and_inspection`
- `brilliant_scientist_focus_unlock_public_project_demonstrations`
- `brilliant_scientist_focus_unlock_rare_material_procurement`
- `brilliant_scientist_focus_unlock_recognition_patron_and_containment_reactions`
- `brilliant_scientist_focus_unlock_replicated_guard_recruitment`
- `brilliant_scientist_focus_unlock_rights_commission`
- `brilliant_scientist_focus_unlock_rights_respecting_integration`
- `brilliant_scientist_focus_unlock_robotics_maintenance`
- `brilliant_scientist_focus_unlock_robotics_production_category`
- `brilliant_scientist_focus_unlock_rogue_node_containment`
- `brilliant_scientist_focus_unlock_route_specific_integration`
- `brilliant_scientist_focus_unlock_scientific_assembly_event`
- `brilliant_scientist_focus_unlock_security_lane`
- `brilliant_scientist_focus_unlock_single_evidence_backed_recovery_target`
- `brilliant_scientist_focus_unlock_singularity_component_intelligence_event`
- `brilliant_scientist_focus_unlock_singularity_program`
- `brilliant_scientist_focus_unlock_staff_amnesty_and_recruitment`
- `brilliant_scientist_focus_unlock_state_foundation_policy_event`
- `brilliant_scientist_focus_unlock_submission_ultimatums_and_protectorates`
- `brilliant_scientist_focus_unlock_supply_spine_repairs`
- `brilliant_scientist_focus_unlock_surviving_officer_appointments`
- `brilliant_scientist_focus_unlock_targeted_laboratory_corridors`
- `brilliant_scientist_focus_unlock_targeted_prototype_works_repair`
- `brilliant_scientist_focus_unlock_targeted_rail_repair`
- `brilliant_scientist_focus_unlock_targeted_reactor_grid`
- `brilliant_scientist_focus_unlock_temporal_authentication_missions`
- `brilliant_scientist_focus_unlock_temporal_claimant_scar`
- `brilliant_scientist_focus_unlock_temporal_ledger_readouts`
- `brilliant_scientist_focus_unlock_temporal_observer_teams`
- `brilliant_scientist_focus_unlock_temporal_stabilization_mission`
- `brilliant_scientist_focus_unlock_temporal_succession_event`
- `brilliant_scientist_focus_unlock_terminal_audit_category`
- `brilliant_scientist_focus_unlock_terminal_depot_linking`
- `brilliant_scientist_focus_unlock_terminal_fortification`
- `brilliant_scientist_focus_unlock_terminal_shutdown_and_dual_keys`
- `brilliant_scientist_focus_unlock_terminal_supply_links`
- `brilliant_scientist_focus_unlock_transit_breach_missions`
- `brilliant_scientist_focus_unlock_transport_pen_construction`
- `brilliant_scientist_focus_unlock_truck_and_train_depots`
- `brilliant_scientist_focus_unlock_vaccine_and_safe_stockpile_seizure`
- `brilliant_scientist_focus_unlock_valid_production_lanes`
- `brilliant_scientist_focus_unlock_veterinary_support`
- `brilliant_scientist_focus_unlock_voluntary_scientific_compacts`
- `brilliant_scientist_focus_unlock_world_route_decisions`
- `brilliant_scientist_focus_unlock_xeno_control_countertests`
- `brilliant_scientist_focus_unlock_xeno_control_mode_event`
- `brilliant_scientist_focus_unlock_xenobiological_assault_recruitment`
- `brilliant_scientist_focus_unlock_xenobiological_category`

Ten non-unlock flags are retained as binding decision-state constraints, not historical completion receipts:

- `brilliant_scientist_focus_clone_property_prohibited`
- `brilliant_scientist_focus_clone_citizenship_law`
- `brilliant_scientist_focus_clone_cohort_law`
- `brilliant_scientist_focus_human_supervisory_keys_locked`
- `brilliant_scientist_focus_expansion_requires_paid_maintenance`
- `brilliant_scientist_focus_machine_power_burden_registered`
- `brilliant_scientist_focus_temporal_warning_contract_required`
- `brilliant_scientist_focus_biological_consequence_ledger_required`
- `brilliant_scientist_focus_integration_requires_compliance_and_time`
- `brilliant_scientist_focus_continental_network_registered`

## Hardlock repair: observable gates

All 36 never-set focus receipt names identified by the independent audit were removed from the tree, trigger layer, and AI plan. Their replacements are executable derived checks over canonical state:

- Project demonstration and project-family capstones read live deployment/weaponization triggers, not personal history alone.
- Prototype works, campus, secondary laboratory, institution, authority, and network gates read paid Directorate receipts already emitted by the facility and institution decisions.
- Clone, Robotics, Paleogenetics, Xenobiological, Teleportation, Alien Arms, and Temporal physical gates read their exact country/state markers and canonical event targets.
- Maintenance and crisis gates read the project incident ledger; the three bypasses use `brilliant_scientist_cloning_incident_resolved`, `brilliant_scientist_robotics_incident_resolved`, and `brilliant_scientist_teleportation_incident_resolved`.
- Resource burdens use the canonical `brilliant_scientist_can_pay_*_deployment` triggers or exact project-stage cost constants. No focus marks a burden paid.
- Biological delivery requires the weaponized project-force package, canonical delivery package, an exact agent delivery idea, and a containment technology.
- Recognition, recovery, military reach, integration, overextension, and continental supply read actual foreign-framework history, former-host/event-facility evidence, divisions, controlled non-owned facilities, logistics access, war/action state, and paid facility-network receipts.
- Temporal warning readiness reads an authenticated owned/controlled anchor, genuine war, synchronization capacity, debt headroom, and stabilization state. Individual operations still bind and pay for their own semantic target.

The former negative `brilliant_scientist_focus_extreme_submission_lock` check was redundant with the symmetric Commonwealth/Submission mutex and was removed rather than replaced with another inert flag.

## Meaningful source validation

- Focus count: 100; unique IDs: 100; duplicate coordinates: 0.
- Architecture comparison: 100/100 coordinate-duration pairs match.
- Focus references: no missing prerequisite or mutual-exclusion target.
- Mutual exclusions: 64 directed edges; no asymmetric pair.
- Localisation: all 100 title/description/effect-tooltip triplets present; English file retains UTF-8 BOM.
- Icons: all 100 focus icon IDs and all 100 shine IDs registered.
- AI: 15 plans; no missing referenced focus ID.
- Downstream contract audit: 180 focus-produced flags; 180 executable consumers; zero missing. The ledger also maps the three interrupted-project diagnostic variables to their audit consumer.
- Project safety: no project focus lacks its operational gate.
- Scripted calls: no unresolved call across the repository snapshot used for this audit.
- Source hygiene: no unit creation, project-force spawn, formation-history application, unsupported comparison operator, scoped temporary variable, raw status-array index, or unary variable-token negation in the owned source.
- Owned-file `git diff --check` is clean.
- The HOI4 focus-inspection MCP call could not return diagnostics because its artifact store reported `ARTIFACT_STORAGE_LIMIT`. This is a tooling-infrastructure blocker, not a successful render result.

## Simplifications, omissions, and blockers

- No gameplay fallback or reward simplification was used inside the implemented focus tranche.
- The 100 registered bespoke DDS assets are missing; no visual-completion claim is made.
- Engine/MCP render inspection remains outstanding because of `ARTIFACT_STORAGE_LIMIT`.
- No spreadsheet alignment was performed because the parent bounded this tranche away from spreadsheet ownership.

## Skills used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-subagents`
- `chaos-redux-event-assets`
