# Event 006 focus geometry re-audit v53

Date: 2026-08-01
Status: blocked for a safe coordinate-only repair; source intentionally unchanged.
Scope: `common/national_focus/006_independence_wave_focus.txt`, `independence_wave_focus_tree`.

## Decision

No small semantics-preserving coordinate patch was applied. The MCP layout report resolves all 184 Event 006 focus nodes to explicit fixed positions, and every one of the 45 unsatisfied crossing diagnostics reports `movableFocusIds=[]`. The warnings are distributed across the shared settlement trunk, government branches, league branches, and package overlays; moving one or two nodes would not be a local repair and would risk new crossings, through-node connectors, or branch readability. Prerequisites, mutual exclusions, effects, AI weights, icons, and localisation were not changed.

## MCP evidence

The read-only MCP inspection used workspace `mod_chaos_redux_ea3b2d67c2c0` with revision `8add5bb7bb2aa93d5fe140ec22d0f8775263e8af0d45e9843c360e23bf57b663`, source hash `b04f229a924ca08d8e140663df6bd308d51acdcbf061d3471db8084ed6c900f8`, and layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/052ff48f9c777b4ca83849564cd17106659026c06c616697adf11983b2f7c74c/ab9fece6d41ec2c4810ec4f335ddd9b51c3e42203dab1d2c0a412c8ee256290f/focus-inspect.8add5bb7bb2aa93d.json`.

Render artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d2201888009a94e892bbce4e1f0f56b341f51c7115cf52165ae412da78af2e/2bac9ef02cb85ea0275a6fca044feb2cdd8a7edf39a8b4c6c82c088a9572ea15/independence_wave_focus_tree.focus.html` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa80848370dc34202a4b67c245207b9e28392e1a443ab096f0530f3d0bebd67e/d29b5b9aedc7ea4de1f61cea1df61590b7dac0762489d90ffac331bdc10f0c8c/independence_wave_focus_tree.focus.svg`.

Raster artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f44f54d781969977be230f942e369821dca6be245dc1c818f730d8b644716f5/711ad44c4153d41cf22e5bfaae8b8b7cd257227a56c31b8f66f37e19cbf3bade/independence_wave_focus_tree.focus.png`.

Raster was produced with `horizontalSpacing = 96`, `verticalSpacing = 130`, and `padding = 48`. It confirms the same route-wide geometry pattern; no source file was modified by inspect, render, or raster.

## Route coverage table

| Route surface | Source coverage | Geometry disposition |
| --- | --- | --- |
| Survival and state construction | Lines 76-291, from `independence_wave_prepare_capital_administration` through `independence_wave_broker_internal_power_compromise` | Present; trunk participates in long/crossing diagnostics. |
| Economy and regional infrastructure | Lines 294-413, from `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury` | Present; no route content changed. |
| Army and researched military identity | Lines 417-683, from `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command` | Present; long/crossing diagnostics at military convergence. |
| Diplomacy, recognition, and patrons | Lines 685-830, from `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service` | Present; foreign-office connector crossings remain. |
| Government settlements and patron/radical routes | Lines 834-1286, including constitutional, council, traditional, emergency, patron, and radical branches plus Saar neutral commission | Present; route anchors are fixed. |
| Former-host settlement and regional ambition | Lines 1287-1541 | Present; the `complete_founding_settlement` to `survey_regional_ambition` connector is a 30-column, 6-row span and crosses seven unrelated nodes. |
| Recognition, league, and network routes | Lines 1542-1726 | Present; league convergence crossings remain. |
| Formable preparation and FORM-03 progression | Lines 1727-1920 | Present; no prerequisite or reward edits. |
| Signature and high-chaos routes | Lines 1923-1983 | Present; `survey_regional_ambition` to `sponsor_further_ruptures` is a 20-column span. |
| Package families SCO, WLS, AJX, BRI, AFX, AGX, RHI, BAY, ARX, and ASX | Lines 1987-3137 | Present; package overlay crossings and five same-row spacing warnings remain. |
| Durable sovereignty terminal | Lines 3141-3157 | Present; final six-row convergence has long and crossing connectors. |
| Shared overlays, ICE choices, and COR spur | Lines 3162-3516 | Imported and preserved; no geometry edits. |

MCP reports 184 focus nodes, 223 connectors, and no missing Event 006 route IDs in the inspected tree. This is a geometry audit, not a semantic route redesign.

## Geometry diagnostics

| Diagnostic | Count | Exact disposition |
| --- | ---: | --- |
| `FOCUS_LAYOUT_LONG_CONNECTOR` | 28 | Unchanged; all are fixed-coordinate endpoints. |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | 45 | Unchanged; every entry has `movableFocusIds=[]`. The corresponding render warnings also report 45 `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` entries. |
| `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE` | 7 | Unchanged; all are the founding-settlement to regional-ambition connector crossing unrelated branch nodes. |
| `FOCUS_LAYOUT_SAME_ROW_SPACING_UNSATISFIED` | 5 | Unchanged; each pair is one column apart while the MCP threshold is two. |

Layout metrics are bounds `x=1..101`, `y=0..19`, 20 rows, 101 columns, 223 connectors, 45 crossings, 7 node intersections, 28 long connectors, maximum horizontal span 80, maximum vertical span 6, maximum Manhattan span 81, and five same-row pairs below the required spacing.

### Long connectors (all 28)

- `independence_wave_complete_founding_settlement` -> `independence_wave_map_internal_power_centers`: h17, v1, m18, source lines 238-250.
- `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue`: h12, v1, m13, source lines 298-315.
- `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_militia_commands`: h14, v1, m15, source lines 419-437.
- `independence_wave_confirm_civilian_control` -> `independence_wave_found_professional_defense_institution`: h9, v1, m10, source lines 520-543.
- `independence_wave_preserve_independent_command` -> `independence_wave_found_professional_defense_institution`: h9, v1, m10, source lines 520-543.
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_adopt_reclamation_doctrine`: h9, v1, m10, source lines 643-655.
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_standardize_with_league`: h11, v1, m12, source lines 657-669.
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_preserve_independent_command`: h13, v1, m14, source lines 671-683.
- `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office`: h28, v1, m29, source lines 689-706.
- `independence_wave_complete_founding_settlement` -> `independence_wave_prepare_first_assembly`: h12, v1, m13, source lines 836-854.
- `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus`: h67, v1, m68, source lines 1232-1245.
- `independence_wave_complete_founding_settlement` -> `independence_wave_define_former_host_policy`: h30, v1, m31, source lines 1292-1303.
- `independence_wave_define_former_host_policy` -> `independence_wave_inherit_successor_ledger`: h9, v1, m10, source lines 1443-1455.
- `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition`: h30, v6, m36, source lines 1474-1486.
- `independence_wave_complete_founding_settlement` -> `independence_wave_recognize_fellow_new_states`: h42, v1, m43, source lines 1547-1558.
- `independence_wave_survey_regional_ambition` -> `independence_wave_sponsor_further_ruptures`: h20, v1, m21, source lines 1929-1941.
- `independence_wave_prepare_capital_administration` -> `independence_wave_sco_reconnect_central_belt_focus`: h54, v1, m55, source lines 1989-2001.
- `independence_wave_prepare_capital_administration` -> `independence_wave_wls_reconnect_north_and_south_focus`: h58, v1, m59, source lines 2061-2073.
- `independence_wave_prepare_capital_administration` -> `independence_wave_ajx_keep_mines_breathing_focus`: h62, v1, m63, source lines 2134-2146.
- `independence_wave_prepare_capital_administration` -> `independence_wave_bri_charter_ports_fisheries_focus`: h66, v1, m67, source lines 2219-2231.
- `independence_wave_prepare_capital_administration` -> `independence_wave_afx_charter_sambre_meuse_authority_focus`: h73, v1, m74, source lines 2291-2309.
- `independence_wave_prepare_capital_administration` -> `independence_wave_agx_chart_waterline_authority_focus`: h80, v1, m81, source lines 2475-2497.
- `independence_wave_prepare_capital_administration` -> `independence_wave_rhi_establish_corridor_authority_focus`: h70, v1, m71, source lines 2704-2716.
- `independence_wave_prepare_capital_administration` -> `independence_wave_bay_broker_civic_settlement_focus`: h76, v1, m77, source lines 2822-2834.
- `independence_wave_prepare_capital_administration` -> `independence_wave_arx_reconcile_municipal_ledgers_focus`: h48, v1, m49, source lines 2943-2955.
- `independence_wave_prepare_capital_administration` -> `independence_wave_asx_unify_palermo_port_books_focus`: h52, v1, m53, source lines 3029-3041.
- `independence_wave_create_independent_treasury` -> `independence_wave_secure_durable_sovereignty`: h6, v6, m12, source lines 3143-3156.
- `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty`: h6, v6, m12, source lines 3143-3156.

### Through-node diagnostics (all 7)

The connector `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition` intersects `independence_wave_activate_package_economic_program` (lines 375-392), `independence_wave_preserve_independent_command` (671-683), `independence_wave_focus_build_permanent_foreign_service` (811-829), `independence_wave_establish_emergency_command` (1039-1052), `independence_wave_accept_protected_future` (1108-1120), `independence_wave_mobilize_founding_myth` (1190-1201), and `independence_wave_recognize_the_frontier` (1333-1344).

### Same-row spacing diagnostics (all 5)

The one-column pairs are `independence_wave_bri_convene_celtic_delegation_focus` / `independence_wave_ajx_appoint_neutral_commission_focus` on row 4 (lines 1232-1245), `independence_wave_asx_integrate_straits_garrisons_focus` / `independence_wave_sco_settle_crown_and_convention_focus` on row 2 (2016-2027), `independence_wave_asx_commission_straits_customs_service_focus` / `independence_wave_sco_found_north_atlantic_state_service_focus` on row 4 (2043-2054), `independence_wave_arx_organize_mountain_guards_focus` / `independence_wave_asx_secure_interior_grain_routes_focus` on row 2 (3043-3054), and `independence_wave_sco_charter_north_atlantic_shipping_focus` / `independence_wave_asx_integrate_straits_garrisons_focus` on row 2 (3056-3067).

### Crossing diagnostics (all 45)

Every crossing entry has empty `movableFocusIds` and fixed or relative endpoints.

- `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_provinces_and_councils` × `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue` (lines 298-315).
- `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` × `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` (lines 337-354).
- `independence_wave_complete_founding_settlement` -> `independence_wave_define_former_host_policy` × `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` (lines 337-354).
- `independence_wave_complete_founding_settlement` -> `independence_wave_recognize_fellow_new_states` × `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` (lines 337-354).
- `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` × `independence_wave_secure_national_depots` -> `independence_wave_recall_and_vet_officers` (lines 460-479).
- `independence_wave_complete_founding_settlement` -> `independence_wave_define_former_host_policy` × `independence_wave_secure_national_depots` -> `independence_wave_recall_and_vet_officers` (lines 460-479).
- `independence_wave_complete_founding_settlement` -> `independence_wave_recognize_fellow_new_states` × `independence_wave_secure_national_depots` -> `independence_wave_recall_and_vet_officers` (lines 460-479).
- `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition` × `independence_wave_form_border_guard` -> `independence_wave_adopt_military_archetype_program` (lines 501-518).
- `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty` × `independence_wave_preserve_independent_command` -> `independence_wave_found_professional_defense_institution` (lines 520-543).
- `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty` × `independence_wave_standardize_with_league` -> `independence_wave_found_professional_defense_institution` (lines 520-543).
- `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_militia_commands` × `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office` (lines 689-706).
- `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_provinces_and_councils` × `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office` (lines 689-706).
- `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue` × `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office` (lines 689-706).
- `independence_wave_inventory_the_state` -> `independence_wave_establish_permanent_ministries` × `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office` (lines 689-706).
- `independence_wave_inventory_the_state` -> `independence_wave_integrate_provinces_and_councils` × `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office` (lines 689-706).
- `independence_wave_inventory_the_state` -> `independence_wave_restore_regional_communications` × `independence_wave_name_provisional_authority` -> `independence_wave_establish_foreign_office` (lines 689-706).
- `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` × `independence_wave_send_first_missions` -> `independence_wave_seek_neighbor_recognition` (lines 727-746).
- `independence_wave_complete_founding_settlement` -> `independence_wave_define_former_host_policy` × `independence_wave_send_first_missions` -> `independence_wave_seek_neighbor_recognition` (lines 727-746).
- `independence_wave_complete_founding_settlement` -> `independence_wave_recognize_fellow_new_states` × `independence_wave_send_first_missions` -> `independence_wave_seek_neighbor_recognition` (lines 727-746).
- `independence_wave_ajx_open_cross_border_trade_desk_focus` -> `independence_wave_ajx_send_rhenish_league_delegation_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_ajx_settle_saar_accounts_focus` -> `independence_wave_ajx_send_rhenish_league_delegation_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_arx_convene_island_settlement_focus` -> `independence_wave_arx_authorize_form05_delegation_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_arx_settle_italian_property_focus` -> `independence_wave_arx_authorize_form05_delegation_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_asx_establish_island_administration_focus` -> `independence_wave_asx_commission_straits_customs_service_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_asx_establish_island_administration_focus` -> `independence_wave_asx_settle_italian_state_property_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_bri_settle_french_accounts_focus` -> `independence_wave_bri_convene_celtic_delegation_focus` × `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` (lines 1232-1245).
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_preserve_independent_command` × `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition` (lines 1474-1486).
- `independence_wave_arm_aligned_movements` -> `independence_wave_proclaim_radical_sovereignty` × `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition` (lines 1474-1486).
- `independence_wave_convene_league_congress` -> `independence_wave_propose_armed_liberation` × `independence_wave_survey_regional_ambition` -> `independence_wave_sponsor_further_ruptures` (lines 1929-1941).
- `independence_wave_convene_league_congress` -> `independence_wave_propose_defensive_congress` × `independence_wave_survey_regional_ambition` -> `independence_wave_sponsor_further_ruptures` (lines 1929-1941).
- `independence_wave_convene_league_congress` -> `independence_wave_propose_development_compact` × `independence_wave_survey_regional_ambition` -> `independence_wave_sponsor_further_ruptures` (lines 1929-1941).
- `independence_wave_convene_league_congress` -> `independence_wave_propose_revisionist_charter` × `independence_wave_survey_regional_ambition` -> `independence_wave_sponsor_further_ruptures` (lines 1929-1941).
- `independence_wave_convene_league_congress` -> `independence_wave_propose_sovereign_equality` × `independence_wave_survey_regional_ambition` -> `independence_wave_sponsor_further_ruptures` (lines 1929-1941).
- `independence_wave_asx_unify_palermo_port_books_focus` -> `independence_wave_asx_integrate_straits_garrisons_focus` × `independence_wave_sco_reconnect_central_belt_focus` -> `independence_wave_sco_charter_north_atlantic_shipping_focus` (lines 2003-2014).
- `independence_wave_asx_integrate_straits_garrisons_focus` -> `independence_wave_asx_establish_island_administration_focus` × `independence_wave_sco_charter_north_atlantic_shipping_focus` -> `independence_wave_sco_convene_celtic_maritime_conference_focus` (lines 2029-2041).
- `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` × `independence_wave_sco_convene_celtic_maritime_conference_focus` -> `independence_wave_sco_found_north_atlantic_state_service_focus` (lines 2043-2054).
- `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus` × `independence_wave_wls_secure_mountain_corridors_focus` -> `independence_wave_wls_convene_celtic_council_focus` (lines 2115-2126).
- `independence_wave_bay_bind_rail_and_pass_authorities_focus` -> `independence_wave_bay_seat_landtag_and_court_focus` × `independence_wave_bay_reconcile_landesbank_accounts_focus` -> `independence_wave_bay_entrust_mountain_guardians_focus` (lines 2877-2890).
- `independence_wave_asx_commission_straits_customs_service_focus` -> `independence_wave_asx_prepare_two_sicilies_dossier_focus` × `independence_wave_asx_settle_italian_state_property_focus` -> `independence_wave_asx_commit_mediterranean_republic_focus` (lines 3124-3137).
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_adopt_reclamation_doctrine` × `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty` (lines 3143-3156).
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_confirm_civilian_control` × `independence_wave_create_independent_treasury` -> `independence_wave_secure_durable_sovereignty` (lines 3143-3156).
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_preserve_independent_command` × `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty` (lines 3143-3156).
- `independence_wave_adopt_military_archetype_program` -> `independence_wave_standardize_with_league` × `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty` (lines 3143-3156).
- `independence_wave_adopt_reclamation_doctrine` -> `independence_wave_found_professional_defense_institution` × `independence_wave_focus_build_permanent_foreign_service` -> `independence_wave_secure_durable_sovereignty` (lines 3143-3156).
- `independence_wave_confirm_civilian_control` -> `independence_wave_found_professional_defense_institution` × `independence_wave_create_independent_treasury` -> `independence_wave_secure_durable_sovereignty` (lines 3143-3156).

## Icons, localisation, rewards, and AI

| Surface | MCP result | Disposition |
| --- | --- | --- |
| Event 006 focus icons | 184/184 plan focuses carry an icon reference; no `FOCUS_ICON_REFERENCE_MISSING` diagnostic points into `mod:common/national_focus/006_independence_wave_focus.txt` | Preserved; no icon IDs changed. |
| Event 006 localisation | 184/184 plan focuses have title and description keys; no Event 006 localisation diagnostic | Preserved; no keys changed. |
| Event 006 rewards | 184/184 plan focuses carry completion rewards | Preserved; no reward mismatch was introduced or corrected in this geometry pass. |
| Event 006 AI | 184/184 plan focuses carry AI data and availability | Preserved; no route-aware AI values changed. |

The render/inspect gate still reports 14 blocking diagnostics, but they are outside Event 006: 14 missing generic continuous-focus sprites in `game:common/continuous_focus/generic.txt` (`DEN_undermine_overlord_continuous_focus`, two ETH focuses, two SWI focuses, and nine generic continuous focuses) plus missing `continuous_restrict_freedom_desc`. Those errors are not safe to fix by changing Event 006 coordinates or icons and remain a separate parent-owned asset/localisation issue.

## Missing or simplified content

No Event 006 route, focus ID, prerequisite, mutual exclusion, effect, icon, localisation key, reward, or AI block was removed or simplified. Geometry warnings remain unresolved because a broad coordinate redesign is outside this narrow repair scope and would change the visual route plan materially.

## High-priority follow-up

1. Keep this source unchanged unless the parent explicitly approves a route-wide geometry pass that moves whole branch cohorts and re-runs inspect/render.
2. Resolve the 14 generic continuous-focus icon/localisation errors in their own asset/localisation task if the global focus gate must pass.
3. If geometry warnings must be cleared, treat the founding-settlement trunk, package fan-out, and final sovereignty convergence as coordinated layout cohorts; do not move isolated endpoints.

## Validation and remaining risks

Meaningful validation completed: `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` on the unchanged source; plan counts, icon/localisation/reward/AI coverage, diagnostic counts, and connector details were read from the MCP artifacts. No game launch or live-session validation was performed.

Skipped: no coordinate trial patch or `hoi4.focus_rewrite` dry-run was applied because all crossing diagnostics had empty movable sets and the requested change was explicitly limited to a smallest safe repair.

Remaining risk: the current fixed-coordinate plan is visually dense and retains 85 layout warnings (28 long, 45 crossings, 7 through-node, 5 spacing), while the global validation gate remains blocked by 14 unrelated generic continuous-focus asset/localisation errors. Any future geometry patch must preserve all 184 IDs and semantics and should be reviewed against the linked artifacts.
