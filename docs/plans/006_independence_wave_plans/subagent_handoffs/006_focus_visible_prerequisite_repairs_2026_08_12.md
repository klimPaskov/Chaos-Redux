# Event 006 shared focus visible-prerequisite repairs — 2026-08-12

## Scope

This bounded patch repairs route visibility in `common/national_focus/006_independence_wave_focus.txt` without changing package identity, rewards, AI weights, or decision availability.

The shared tree remains `independence_wave_focus_tree` and the patch applies to its existing Event 006 package branches and AJX neutral route.

## Changes

`independence_wave_ajx_appoint_neutral_commission_focus` now visibly requires `independence_wave_complete_founding_settlement`.

The following fourteen generic route/trunk focuses now visibly require their existing upstream anchors: `independence_wave_map_internal_power_centers`, `independence_wave_establish_emergency_revenue`, `independence_wave_integrate_militia_commands`, `independence_wave_adopt_reclamation_doctrine`, `independence_wave_standardize_with_league`, `independence_wave_establish_foreign_office`, `independence_wave_prepare_first_assembly`, `independence_wave_organize_popular_councils`, `independence_wave_reject_inherited_borders`, `independence_wave_define_former_host_policy`, `independence_wave_inherit_successor_ledger`, `independence_wave_survey_regional_ambition`, `independence_wave_recognize_fellow_new_states`, and `independence_wave_sponsor_further_ruptures`.

The following package branch roots now visibly require `independence_wave_prepare_capital_administration`: `independence_wave_sco_reconnect_central_belt_focus`, `independence_wave_wls_reconnect_north_and_south_focus`, `independence_wave_ajx_keep_mines_breathing_focus`, `independence_wave_bri_charter_ports_fisheries_focus`, `independence_wave_afx_charter_sambre_meuse_authority_focus`, `independence_wave_agx_chart_waterline_authority_focus`, `independence_wave_rhi_establish_corridor_authority_focus`, `independence_wave_bay_broker_civic_settlement_focus`, `independence_wave_arx_reconcile_municipal_ledgers_focus`, and `independence_wave_asx_unify_palermo_port_books_focus`; `independence_wave_ajx_appoint_neutral_commission_focus` now visibly requires `independence_wave_complete_founding_settlement`.

Each affected focus already had the corresponding completed-focus gate in `available`, so the patch adds the visible connector that communicates the existing route contract rather than widening access.

All existing `available`, `bypass`, `mutually_exclusive`, `completion_reward`, and `ai_will_do` logic remains unchanged.

## Validation

A source parser now finds zero Event 006 focus blocks with a `has_completed_focus` availability gate but no visible `prerequisite` block.

`python -B .tools/audit_event6_allocator.py` passes with the current 30-attested / 27-group authority and the 3/4/5/7/10 wave ladder.

`python -B .tools/audit_event6_scenario_matrix.py` passes all 32 declared cells and 8 edge cases.

Current `git diff --check` is clean for the focus patch and the authority documents touched in this tranche.

## Engine evidence and limits

Fresh `hoi4.focus_inspect` and `hoi4.focus_render` calls for `independence_wave_focus_tree` are blocked before source inspection by `ARTIFACT_MANIFEST_INVALID` with the message `Artifact provenance manifest is invalid` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Historical focus artifacts remain historical evidence only and are not used to claim post-patch layout acceptance.

The updated visible edges should be re-inspected and rendered after the MCP provenance manifest is repaired because connector spacing and aggregate layout diagnostics are not source-only facts.

## Remaining risks

The shared tree still carries previously documented workspace-wide vanilla continuous-focus icon diagnostics and any fresh MCP layout result may expose spacing changes caused by these additional visible edges.

This handoff does not promote any new country package or alter the central adapter, content-attestation, normal-preflight, scenario-preflight, or Join lists.
