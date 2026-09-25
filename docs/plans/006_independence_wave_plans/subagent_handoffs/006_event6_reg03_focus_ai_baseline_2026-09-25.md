# Event 006 REG-03 Focus AI Baseline

**Disposition:** Read-only baseline audit completed with quantitative conclusions unresolved. The accepted REG-03 scope was explicitly approved on 2026-09-25. This handoff records the current pre-expansion source and the limits of the live analyzer.

## Audited surface and source files

The weighted surface is the next-focus `ai_will_do` selection in `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, for the planned packages IW-023 TRA, IW-029 BOS, and IW-026 MAC. Current source contains the package-gated reward adapters described in the accepted scope. The REG-03 country focus groups and their AI weights have not been added.

The package and carrier conditions were reviewed in `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, and `common/scripted_triggers/006_independence_wave_focus_triggers.txt`. Setup outputs and branch assignment were reviewed in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt`. The source constants were reviewed in `common/script_constants/006_independence_wave_constants_registry.txt`, and package AI strategy profiles were reviewed in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`.

The accepted design inputs reviewed were `docs/specs/006_independence_wave_specs/matrices/006_ai_strategy_matrix.csv`, `docs/specs/006_independence_wave_specs/diagrams/006_focus_tree_lane_map.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`, and `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`. The historical handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_probability_audit_2026-09-25.md` was read only to identify its empty-state fixtures as historical failures; its source revision and fixtures were not reused.

The AI strategy matrix and focus lane map describe qualitative profiles and route lanes. They do not provide complete tag-specific campaign states, focus completion histories, or former-host scope values for these packages. I did not assign AI-02 or another matrix profile to an actor because its full inputs cannot be represented from the accepted material.

## Current MCP identity and semantics

The mandatory first call was `hoi4.probability_inspect` with adapter `national_focus_ai_will_do`, source `common/national_focus/006_independence_wave_focus.txt`, `refresh=true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. It found 184 candidates, 17 required input categories, and no unsupported constructs. Its `poolComplete=false` and zero available candidates describe the inspection without a scenario; neither is used as a campaign result.

The MCP inspect source revision is `b2e5a1add2e7f9aebd648af90d287a8e29f300dc8509300d792f01f8775fa815` and its source hash is `29ff69e8774c0bc8875416b112c560dc036e7b8b2be38239804a5169fa2db9a0`. The raw local file SHA-256 is `5E3782F0BA496FC8C5FBBF491E05F8FA227867DB76FCE15E9DEB8B7369704440`. The evaluator reported source revision `1f1304c279436a09bcc62fe4e31a32a91ed2d2f054ea9736b60c16d44317702c` with the same MCP source hash `29ff69e8774c0bc8875416b112c560dc036e7b8b2be38239804a5169fa2db9a0`; both MCP source identities are preserved here.

The adapter version is `hoi4-1.19.2.v1`, targeting Operation Postern 1.19.2.0 (d245). Its selection rule is `uniform_score_race` at next-focus cadence. It compares eligible scores in a uniform maximum-score race. A conditional selection probability requires a complete eligible pool and declared external factors. The adapter supports raw scores and normalized probabilities, while sequence and time-distribution output are unsupported. An `ai_will_do` score is a willingness score; it is not a click percentage. The adapter states that ordered AI strategy plans may override weighted selection and that prerequisite completion and external focus factors require scenario inputs.

## Source-derived package setup facts

These values are source facts, not AI weight recommendations, and were not injected into the evaluator's flat primitive state map as Clausewitz variables.

| Package | Package id constant | Region, depth, archetype | Setup anchor state | Source initialized values |
| --- | --- | --- | --- | --- |
| IW-023 TRA | `independence_wave_package_id.iw_023 = 23` | `balkans_danube = 3`, `regional = 2`, `mountain_or_frontier = 5` | State 84 | `independence_wave_transylvania_pressure.frontier_start = 38`; `federal_start = 44` |
| IW-029 BOS | `independence_wave_package_id.iw_029 = 29` | `balkans_danube = 3`, `regional = 2`, `mountain_or_frontier = 5` | State 104 | `independence_wave_bosnia_pressure.civic_start = 32`; `defence_start = 44` |
| IW-026 MAC | `independence_wave_package_id.iw_026 = 26` | `balkans_danube = 3`, `regional = 2`, `mountain_or_frontier = 5` | State 106 | `independence_wave_macedonia_pressure.civic_start = 36`; `defence_start = 42` |

The setup triggers require the matching package id, region, depth, archetype, and the named anchor and former-host event targets. BOS requires the former host to be YUG and its protected release state to be owned by the package country. TRA and MAC require an existing former host distinct from the package country and a protected release state owned by the package country; the former-host identity is dynamic.

TRA setup chooses additive assignment when `has_focus_tree = austro_hungarian_releasable_focus` and full-framework assignment otherwise. The assignment constants are `full_framework = 1` and `additive_overlay = 2`. BOS also branches on the Austro-Hungarian carrier; MAC assigns the full framework. The fixture flags below record source output flags for those branches. They do not prove the branch's input trigger, country tree identity, setup variables, or event-target state.

## Repeatable evaluator scenario set

The exact `scenarioSet` sent to `hoi4.probability_evaluate` is below. Its id and scenario ids are intended to remain unchanged for a later comparison. These are schema-valid, repeatable probes, not complete typed campaign fixtures. The early scenarios represent the post-setup/pre-group checkpoint. The three named mid-route checkpoints represent the current shared founding-settlement focus in the full-framework branch; they do not assert a package-specific route choice. The accepted specs do not define a numeric per-package mid-route state.

```json
{
  "id": "event006_reg03_pre_patch_campaign_fixtures_2026_09_25",
  "scenarios": [
    {
      "id": "reg03_tra_early_generic_framework_pre_group",
      "actor": "TRA",
      "state": {
        "exists": true
      },
      "flags": [
        "independence_wave_iw_023_lifecycle_initialized",
        "independence_wave_iw_023_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_tra_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_full_focus_framework",
        "independence_wave_generic_focus_tree_assigned"
      ],
      "scopes": {}
    },
    {
      "id": "reg03_tra_early_austro_hungarian_carrier_pre_group",
      "actor": "TRA",
      "state": {
        "exists": true
      },
      "flags": [
        "independence_wave_iw_023_lifecycle_initialized",
        "independence_wave_iw_023_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_tra_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_additive_focus_overlay",
        "independence_wave_generic_focus_overlay_assigned"
      ],
      "scopes": {}
    },
    {
      "id": "reg03_tra_midroute_generic_after_founding_settlement",
      "actor": "TRA",
      "state": {
        "exists": true,
        "has_completed_focus": "independence_wave_complete_founding_settlement"
      },
      "flags": [
        "independence_wave_iw_023_lifecycle_initialized",
        "independence_wave_iw_023_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_tra_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_full_focus_framework",
        "independence_wave_generic_focus_tree_assigned",
        "independence_wave_founding_settlement_complete"
      ],
      "scopes": {}
    },
    {
      "id": "reg03_bos_early_generic_framework_pre_group",
      "actor": "BOS",
      "state": {
        "exists": true
      },
      "flags": [
        "independence_wave_iw_029_lifecycle_initialized",
        "independence_wave_iw_029_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_bos_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_full_focus_framework",
        "independence_wave_generic_focus_tree_assigned"
      ],
      "scopes": {}
    },
    {
      "id": "reg03_bos_midroute_generic_after_founding_settlement",
      "actor": "BOS",
      "state": {
        "exists": true,
        "has_completed_focus": "independence_wave_complete_founding_settlement"
      },
      "flags": [
        "independence_wave_iw_029_lifecycle_initialized",
        "independence_wave_iw_029_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_bos_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_full_focus_framework",
        "independence_wave_generic_focus_tree_assigned",
        "independence_wave_founding_settlement_complete"
      ],
      "scopes": {}
    },
    {
      "id": "reg03_mac_early_generic_framework_pre_group",
      "actor": "MAC",
      "state": {
        "exists": true
      },
      "flags": [
        "independence_wave_iw_026_lifecycle_initialized",
        "independence_wave_iw_026_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_mac_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_full_focus_framework",
        "independence_wave_generic_focus_tree_assigned"
      ],
      "scopes": {}
    },
    {
      "id": "reg03_mac_midroute_generic_after_founding_settlement",
      "actor": "MAC",
      "state": {
        "exists": true,
        "has_completed_focus": "independence_wave_complete_founding_settlement"
      },
      "flags": [
        "independence_wave_iw_026_lifecycle_initialized",
        "independence_wave_iw_026_setup_complete",
        "independence_wave_package_setup_complete",
        "independence_wave_focus_carrier_registered",
        "independence_wave_mac_ai_profile",
        "independence_wave_generic_ai_profile",
        "independence_wave_full_focus_framework",
        "independence_wave_generic_focus_tree_assigned",
        "independence_wave_founding_settlement_complete"
      ],
      "scopes": {}
    }
  ]
}
```

For each scenario the evaluator received the complete 184-id source pool below, in this exact order. Its MCP candidate-pool hash is `ec8dcb61ef79eaa9a07d32cce752841d0ef10ee0d0346ab793ef177ca090bee2`. The list is complete for the current inspected source tree. Scenario-specific eligibility remains unresolved, so it is not a proven complete eligible-focus pool.

```json
[
  "independence_wave_accept_advisers_and_credits",
  "independence_wave_accept_foreign_arms",
  "independence_wave_accept_protected_future",
  "independence_wave_activate_package_economic_program",
  "independence_wave_adopt_border_defense",
  "independence_wave_adopt_military_archetype_program",
  "independence_wave_adopt_reclamation_doctrine",
  "independence_wave_afx_bind_mines_rails_furnaces_focus",
  "independence_wave_afx_charter_sambre_meuse_authority_focus",
  "independence_wave_afx_codify_basin_government_focus",
  "independence_wave_afx_integrate_industrial_reserve_focus",
  "independence_wave_afx_mandate_meuse_conference_focus",
  "independence_wave_afx_open_meuse_network_office_focus",
  "independence_wave_afx_prepare_low_countries_dossier_focus",
  "independence_wave_afx_settle_industrial_succession_focus",
  "independence_wave_agx_bind_dikes_pumps_harbors_focus",
  "independence_wave_agx_chart_waterline_authority_focus",
  "independence_wave_agx_codify_water_board_government_focus",
  "independence_wave_agx_integrate_coastal_guard_focus",
  "independence_wave_agx_mandate_north_sea_coastal_conference_focus",
  "independence_wave_agx_open_north_sea_network_office_focus",
  "independence_wave_agx_prepare_low_countries_dossier_focus",
  "independence_wave_agx_settle_water_board_succession_focus",
  "independence_wave_ajx_appoint_neutral_commission_focus",
  "independence_wave_ajx_bind_security_to_commission_focus",
  "independence_wave_ajx_charter_coal_rail_authority_focus",
  "independence_wave_ajx_codify_municipal_neutrality_focus",
  "independence_wave_ajx_entrench_neutral_commission_focus",
  "independence_wave_ajx_keep_mines_breathing_focus",
  "independence_wave_ajx_open_cross_border_trade_desk_focus",
  "independence_wave_ajx_screen_industrial_security_companies_focus",
  "independence_wave_ajx_send_rhenish_league_delegation_focus",
  "independence_wave_ajx_settle_saar_accounts_focus",
  "independence_wave_arm_aligned_movements",
  "independence_wave_arm_public_guard",
  "independence_wave_arx_authorize_form05_delegation_focus",
  "independence_wave_arx_convene_island_settlement_focus",
  "independence_wave_arx_organize_mountain_guards_focus",
  "independence_wave_arx_reconcile_municipal_ledgers_focus",
  "independence_wave_arx_restore_cagliari_shipping_office_focus",
  "independence_wave_arx_settle_italian_property_focus",
  "independence_wave_asx_commission_straits_customs_service_focus",
  "independence_wave_asx_commit_mediterranean_republic_focus",
  "independence_wave_asx_establish_island_administration_focus",
  "independence_wave_asx_integrate_straits_garrisons_focus",
  "independence_wave_asx_prepare_two_sicilies_dossier_focus",
  "independence_wave_asx_secure_interior_grain_routes_focus",
  "independence_wave_asx_settle_italian_state_property_focus",
  "independence_wave_asx_unify_palermo_port_books_focus",
  "independence_wave_balance_the_first_patrons",
  "independence_wave_bay_bind_rail_and_pass_authorities_focus",
  "independence_wave_bay_broker_civic_settlement_focus",
  "independence_wave_bay_convene_south_german_settlement_focus",
  "independence_wave_bay_entrust_mountain_guardians_focus",
  "independence_wave_bay_open_alpine_network_office_focus",
  "independence_wave_bay_ratify_german_host_compact_focus",
  "independence_wave_bay_reconcile_landesbank_accounts_focus",
  "independence_wave_bay_seat_landtag_and_court_focus",
  "independence_wave_become_bargaining_client",
  "independence_wave_become_loyal_guarantor_state",
  "independence_wave_become_treaty_backed_state",
  "independence_wave_bind_court_and_ministries",
  "independence_wave_bind_the_first_oath",
  "independence_wave_bri_charter_ports_fisheries_focus",
  "independence_wave_bri_convene_celtic_delegation_focus",
  "independence_wave_bri_establish_breton_gallo_services_focus",
  "independence_wave_bri_integrate_sailors_guards_focus",
  "independence_wave_bri_settle_french_accounts_focus",
  "independence_wave_broker_internal_power_compromise",
  "independence_wave_build_cooperative_administration",
  "independence_wave_build_military_economy",
  "independence_wave_build_postwar_integration_authority",
  "independence_wave_build_professional_core",
  "independence_wave_build_regional_transport_authority",
  "independence_wave_call_regional_congress",
  "independence_wave_complete_founding_settlement",
  "independence_wave_confirm_civilian_control",
  "independence_wave_consolidate_constitutional_state",
  "independence_wave_convene_association_conference",
  "independence_wave_convene_league_congress",
  "independence_wave_create_independent_treasury",
  "independence_wave_crown_the_restored_state",
  "independence_wave_declare_entrenched_neutrality",
  "independence_wave_define_equal_citizenship",
  "independence_wave_define_former_host_policy",
  "independence_wave_demand_recognition_or_conflict",
  "independence_wave_document_unsettled_claims",
  "independence_wave_draft_league_charter",
  "independence_wave_entrench_emergency_state",
  "independence_wave_establish_aid_corridor",
  "independence_wave_establish_armed_coexistence",
  "independence_wave_establish_customs_service",
  "independence_wave_establish_emergency_command",
  "independence_wave_establish_emergency_revenue",
  "independence_wave_establish_foreign_office",
  "independence_wave_establish_integration_commission",
  "independence_wave_establish_permanent_ministries",
  "independence_wave_exchange_civil_servants",
  "independence_wave_favor_first_power_center",
  "independence_wave_favor_second_power_center",
  "independence_wave_focus_build_permanent_foreign_service",
  "independence_wave_focus_coordinate_reclamation_fronts",
  "independence_wave_focus_discover_regional_identity",
  "independence_wave_form03_build_federal_appeals_and_examinations",
  "independence_wave_form03_define_public_service_guarantees",
  "independence_wave_form03_establish_delta_works_board",
  "independence_wave_form03_harmonize_corridor_standards",
  "independence_wave_form03_open_charter_convention",
  "independence_wave_form03_submit_low_countries_compact",
  "independence_wave_form_border_guard",
  "independence_wave_fortify_former_host_frontier",
  "independence_wave_found_professional_defense_institution",
  "independence_wave_fund_domestic_arsenals",
  "independence_wave_gather_founding_members",
  "independence_wave_grant_military_autonomy",
  "independence_wave_inherit_successor_ledger",
  "independence_wave_integrate_militia_commands",
  "independence_wave_integrate_provinces_and_councils",
  "independence_wave_inventory_the_state",
  "independence_wave_limit_emergency_powers",
  "independence_wave_map_internal_power_centers",
  "independence_wave_mobilize_founding_myth",
  "independence_wave_name_provisional_authority",
  "independence_wave_open_guarantor_talks",
  "independence_wave_open_separation_talks",
  "independence_wave_open_signature_extension",
  "independence_wave_organize_popular_councils",
  "independence_wave_prepare_capital_administration",
  "independence_wave_prepare_first_assembly",
  "independence_wave_prepare_reclamation_command",
  "independence_wave_prepare_traditional_confirmation",
  "independence_wave_prepare_union_congress",
  "independence_wave_preserve_independent_command",
  "independence_wave_proclaim_council_commonwealth",
  "independence_wave_proclaim_open_sovereignty",
  "independence_wave_proclaim_radical_sovereignty",
  "independence_wave_propose_armed_liberation",
  "independence_wave_propose_defensive_congress",
  "independence_wave_propose_development_compact",
  "independence_wave_propose_network_arbitration",
  "independence_wave_propose_revisionist_charter",
  "independence_wave_propose_sovereign_equality",
  "independence_wave_raise_mass_reserve",
  "independence_wave_ratify_constitution",
  "independence_wave_recall_and_vet_officers",
  "independence_wave_recognize_fellow_new_states",
  "independence_wave_recognize_the_frontier",
  "independence_wave_recruit_regional_notables",
  "independence_wave_reject_inherited_borders",
  "independence_wave_restore_legitimate_authority",
  "independence_wave_restore_regional_communications",
  "independence_wave_rewrite_charter_of_borders",
  "independence_wave_rhi_arm_customs_guard_focus",
  "independence_wave_rhi_authorize_form04_delegation_focus",
  "independence_wave_rhi_charter_network_transit_office_focus",
  "independence_wave_rhi_establish_corridor_authority_focus",
  "independence_wave_rhi_proclaim_neutral_corridor_focus",
  "independence_wave_rhi_ratify_host_transit_compact_focus",
  "independence_wave_rhi_secure_industrial_belt_focus",
  "independence_wave_rhi_unify_rail_dispatch_focus",
  "independence_wave_sco_charter_north_atlantic_shipping_focus",
  "independence_wave_sco_convene_celtic_maritime_conference_focus",
  "independence_wave_sco_found_north_atlantic_state_service_focus",
  "independence_wave_sco_reconnect_central_belt_focus",
  "independence_wave_sco_settle_crown_and_convention_focus",
  "independence_wave_secure_durable_sovereignty",
  "independence_wave_secure_food_and_fuel",
  "independence_wave_secure_national_depots",
  "independence_wave_seek_neighbor_recognition",
  "independence_wave_send_first_missions",
  "independence_wave_settle_empty_claim",
  "independence_wave_settle_property_and_citizenship",
  "independence_wave_sponsor_further_ruptures",
  "independence_wave_standardize_with_league",
  "independence_wave_submit_union_question",
  "independence_wave_subordinate_militias",
  "independence_wave_support_local_committees",
  "independence_wave_survey_regional_ambition",
  "independence_wave_wls_charter_coal_and_rail_focus",
  "independence_wave_wls_convene_celtic_council_focus",
  "independence_wave_wls_establish_bilingual_service_focus",
  "independence_wave_wls_reconnect_north_and_south_focus",
  "independence_wave_wls_secure_mountain_corridors_focus",
  "independence_wave_write_formation_terms"
]
```

Source-derived `exists=true` is included for the root actor because the package-content and setup gates require an existing country. Actor carries the root package tag. The flags are exact output identifiers set by current setup and focus-assignment effects. Mid-route scenarios use the current focus id `independence_wave_complete_founding_settlement` and its source output flag `independence_wave_founding_settlement_complete`. The string value is a primitive comparison probe under the accepted flat-state schema, not a typed completed-focus history. The focus's source prerequisites `independence_wave_establish_permanent_ministries` and `independence_wave_restore_regional_communications` are not represented as a complete history.

No simulation, numeric state assumptions, or invented trigger values were supplied. The `scopes` objects are empty because the live scenario schema's generic `{id,state}` scope records were not sufficient evidence for encoding the package event-target state, variable ownership chain, and campaign country existence without inventing values. The output branch flags in the TRA additive probe are source-defined results; they do not establish the required Austro-Hungarian tree input. Missing flags or state entries are unresolved, not asserted false.

The early checkpoint is before the planned group focus completion. The groups do not exist in the current source, so there are no current group focus ids or completion markers to encode. The additive TRA carrier is included as an early branch probe. A carrier-specific mid-route scenario was not declared because this adapter inspection did not expose a typed active-focus-tree input or a typed carrier focus-completion history.

## Probability evaluation and rendered evidence

The evaluator call used `hoi4.probability_evaluate`, adapter `national_focus_ai_will_do`, the current source path, `refresh=true`, the complete candidate pool above, the exact scenario set above, metrics `raw_value` and `conditional_probability`, and outputs `json`, `ranking`, and `unresolved`.

The result was `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-5406605a565d6eae5bf72dac`, scenario hash `dccf52aa30df08c40b93e1a7f201bd7b1022cd5f275dfe262897b4e3e3d16e89`, 7 scenarios, 1,288 candidate-scenario rows, 2,634 unresolved items, and 225 diagnostics. The candidate row count is 184 candidates multiplied across seven scenarios. Tool validation marked uncertainty visible; it did not certify campaign input completeness.

The evaluator emitted `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` and unsatisfied-modifier diagnostics for candidates including `independence_wave_accept_advisers_and_credits`, `independence_wave_accept_foreign_arms`, and `independence_wave_adopt_border_defense`. These diagnostics are artifacts of the incomplete fixtures and cannot establish that any focus is dead, invalid, starved, or impossible. No evaluator route error occurred; the route ran and returned partial analysis.

No numeric scenario score, base/modifier trace, rank, normalized selection probability, threshold, or timing result is admitted as a baseline fact. The ranking visualization is retained for provenance only and should not be used to infer a campaign ordering. Since the source and required context are incomplete, no candidate dominance, starvation, rank reversal, or exact probability claim is supported.

The matching structural calls were `hoi4.focus_inspect` and `hoi4.focus_render` for `independence_wave_focus_tree` and the same current source path. Inspect reported 184 focuses and 196 connectors, structural revision `2481cdbe9f03f38152699849acca481609a81bf4f5bc53e684bd6605512c6ecf`, and layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. Structural evidence confirms the current tree shape; it does not resolve weighted eligibility.

### MCP artifacts

- Probability inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab10ddaba5f940b8a0ffcf13b1aa78adcdfeee24c3b89169985580472c018411/911b3dd4277dec3f5f45354110d67f97d9d6963bd233ed324269f24377949419/probability-inspect-29ff69e8774c.json`.
- Focus inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dffdeca346570ec3553819ea9e73a20a776ee6997a01029cc899d2da21e2dd8a/b539e3e0fc6eedd872722b45534a19444c30a2a549a6520188e8c1ab5e08ed86/focus-inspect.2481cdbe9f03f381.json`.
- Focus render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce7d6ab4862487592b507f96885fc8948b6e22f58cc376a4a3ecced94a00d85a/62e0e5480842260639cf22b1ccf6f8bb35f69e9b7b32ba4bc5fa5c62415266ad/independence_wave_focus_tree.focus.html`.
- Focus render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/df6e96ef882d15bd4d4bbe89af66050415ed93e67d2b68f15838bb5463374ab9/independence_wave_focus_tree.focus.svg`.
- Focus render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07ebcec39da9808d4953634bd4f91505b3ce09d59fa01bb1844dfd500062c4fb/05e64c609ea085557c27bffecbe902975c3bab14ed76c954ca016f7b306d7bee/independence_wave_focus_tree.focus.json`.
- Probability evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc252d236720b3ff98e05fe67e60ad6718928279aa2ddbbc78268e1397e5763d/382291c7d9bfc3994ab7a941dcd447f45aa441a92cfe2a71e3e8b107e1f297ce/probability-5406605a565d6eae5bf72dac.json`.
- Probability ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59fa062a48134a9f45a2d217c340bcd478d774928f643ebf71efc1594886f001/95b8174c7d97a2762801f7a4155a7e205cb02cd025031eb39e896e9dcb044980/probability-probability-5406605a565d6eae5bf72dac-ranking.svg`.
- Probability unresolved SVG from evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efd47d4ad591e8d8fc538c62fb5fb258676141333387ce9c160b64349a54bfb7/8a2d74df55fa35c9522b2844004f8d0b0a2d3f2cd9dfacf1f9f5840bbf65c077/probability-probability-5406605a565d6eae5bf72dac-unresolved.svg`.
- Probability unresolved render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c26569691c93a8ca635d53438d38ee44f433913d9639dd4aefa5c108f9b95888/419db3895cdc2cec9cf17d80054e05f5a221ebd64c78b4b4ef7df5cd48ef1f0a/probability-probability-5406605a565d6eae5bf72dac-unresolved.html`.
- Probability unresolved render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efd47d4ad591e8d8fc538c62fb5fb258676141333387ce9c160b64349a54bfb7/c0c8f7a32cdac537c130e544c603201b257465b488276ea7a559ca80d36b59ee/probability-probability-5406605a565d6eae5bf72dac-unresolved.svg`.
- Probability unresolved render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59a8a0a4f78183ba298a167096618ece12182c4a2d43c1ace25d55058799378b/15082b2ed37c0f11cf6c9424daa8ce3295069b47de2e0f06eead0a1b1b304219/probability-probability-5406605a565d6eae5bf72dac-unresolved.png`.

## Coverage blockers and unresolved findings

The inspect identified these 17 required input categories: `BEL`, `HOL`, `LUX`, `capital_scope`, `check_variable`, `custom_trigger_tooltip`, `event_target:independence_wave_setup_anchor_state`, `event_target:independence_wave_setup_former_host`, `exists`, `focus.external_factors_complete`, `has_completed_focus`, `has_cosmetic_tag`, `has_variable`, `has_war`, `is_in_array`, `original_tag`, and `var:independence_wave_former_host`.

The root actor and tag are represented by `actor`; root existence is set true; exact source output flags are provided; the mid-route probe gives one exact focus id as a primitive string. This does not cover the full `has_completed_focus` history or make the flat state map a typed Clausewitz variable store. The fixtures leave package variables and compound `check_variable` expressions unbound, omit both package event-target scopes and their ownership chains, omit `capital_scope`, and do not establish scope existence for the dynamic former host or the BEL/HOL/LUX checks. They also do not resolve `has_cosmetic_tag`, `has_variable`, `has_war`, `is_in_array`, or `custom_trigger_tooltip` results.

`focus.external_factors_complete` is not declared. No REG-03-specific `ai_national_focuses` or `focus_factors` block was found in the inspected `common/ai_strategy_plans/` files or Event 006 AI strategy registry. The adapter's general ordered-plan override limitation remains, and the full external focus factor context is unresolved. The AI strategy registry's package strategies do not supply the missing country, event-target, and focus-history fixture.

The current source has no planned group focus ids or group completion flags, so the before-group-completion state cannot carry an explicit negative completion record. The AI matrix and Parts 4 and 5 do not specify a unique package-specific mid-route focus path and corresponding complete history. The additive carrier branch lacks a typed active focus tree and focus-history input. These limits prevent the named probes from serving as exact campaign fixtures.

## Validity, balance, and exploit findings

No positive weight on an impossible focus, duplicate or contradictory score, unbounded score, starvation, dominance, rank reversal, timing drift, repetition rate, or exploit risk is established by this run. The analyzer's never-eligible warnings are bounded to the seven incomplete probes and are unresolved for campaign validity. There is no score trace that supports a base-value or modifier comparison across the three packages.

The source adapter describes score competition rather than probability-proportional sampling. A normalized selection result is conditional on the complete eligible candidate pool and external factors. The current run cannot establish that pool per scenario. Repetition and cadence analysis are unavailable because the adapter reports no sequence or time-distribution capability.

## Recommended follow-up, without source changes

Do not tune numeric weights from this baseline. Before using a later `hoi4.probability_compare`, keep scenarioSet id `event006_reg03_pre_patch_campaign_fixtures_2026_09_25` and its seven scenario ids unchanged, and supply a typed, source-derived campaign fixture for package variables, focus completion history, carrier tree identity, country and state scopes, event targets, former-host ownership, and external focus factors. The post-change comparison must use the complete candidate pool for the compared source, including any newly introduced group focus ids. If the live adapter cannot encode those inputs, record the specific adapter limitation and keep package ranking unresolved.

## Skipped analyses and completion record

`hoi4.probability_sweep` was skipped because no fully specified numeric scenario or sensitivity dimension is available; supplying sweep ranges would require invented campaign state. `hoi4.probability_compare` was skipped because this is the before-change baseline and there is no after-change source. `hoi4.probability_simulate` was skipped because no uncertain input distributions or seeds were declared. `hoi4.probability_sequence` was skipped because this is not a declared custom weighted pool and this focus adapter does not support sequence or timing analysis.

The offline Paradox wiki AI and focus pages, the required core wiki pages, and the vanilla Hearts of Iron IV documentation files were consulted alongside the named source and accepted planning files. The `chaos-redux-subagents`, `chaos-redux-focus-trees`, and `chaos-redux-event-planning` skills were applied. This audit changed no gameplay or AI source, ran no tests or live game, and created no commit. The only output from this task is this handoff.

