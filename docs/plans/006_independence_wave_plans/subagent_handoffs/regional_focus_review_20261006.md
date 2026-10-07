# Event 006 Level 2 Regional Focus Adversarial Review

Date: 2026-10-06.

Disposition: bounded source review complete. This reviewer made no gameplay, focus, decision, localisation, icon, or AI edits and created no commit. The parent applied a narrow focus/decision interlock hardening during the review; a post-edit source count is recorded below.

## Accepted scope and route coverage

Part 5 of the accepted Event 006 spec requires one country-specific focus group for every Level 2 featured regional package. The parent task accepted the five-node group contract and the shared-tree import model. This review covers the 44 Level 2 tags named in the parent task, the 220 A/B shared focuses, their English localisation files, A/B helper effects and B triggers, the nine named regional decision files, and the main tree's imports, generic survey/congress guards, and focus cleanup calls.

The three signature modules and four formable contracts authored by other workers were excluded as instructed. This review does not certify whole Event 006 completion.

## Priority findings

1. The 44 source groups, 220 definitions/imports, 136 project mappings, and four opposed choices are present and internally cross-locked. The parent’s defensive cancel and completion guards now cover all 136 project nodes.
2. Imported-node layout remains unresolved because the connected focus tools expose only the 184 direct tree nodes and reject the A/B shared-focus fragments as standalone trees. Do not claim rendered layout coverage for the new groups.
3. Focus AI weights exist, but the probability handoff could not evaluate the imported candidates or their country-specific pools. No numeric route-selection or balance claim is supported.
4. A direct complete_national_focus call is an out-of-band hardening question. No such caller exists in the scoped Event 006 focus, decision, or effect files. The available documentation does not say which parent prerequisites are re-evaluated by that effect, so a bypass of the five-node route is an inference, not an engine-confirmed defect.

Focus ids in the table use the exact suffix after independence_wave_<lowercase tag>_focus_. A and B refer to common/national_focus/006_independence_wave_regional_focus_a.txt and common/national_focus/006_independence_wave_regional_focus_b.txt. All 44 groups define five nodes and have five corresponding imports in common/national_focus/006_independence_wave_focus.txt. IMO, LEB, RIF, and DSX contain four project-focus definitions and one congress capstone without a separate host-support node. The other 40 groups contain three project focuses, one host-support focus, and one capstone.

| Tag | File | Five-node route suffixes | Pattern |
| --- | --- | --- | --- |
| BAR | A | convene_the_national_kuta; restore_the_floodplain_canals; regulate_the_mine_labour_contracts; settle_the_lozi_mine_labour_accounts; prepare_regional_integration_authority | 3 projects + support + cap |
| BLC | A | convene_the_kalat_assemblies; secure_the_bolan_pass; open_the_makran_road; settle_bolan_and_makran_transit; prepare_regional_integration_authority | 3 projects + support + cap |
| BRD | A | reconcile_the_bezi_and_batare; settle_the_mandate_accounts; build_the_usumbura_lake_port; secure_usumbura_lakeshore_transit; prepare_regional_integration_authority | 3 projects + support + cap |
| CUX | A | seat_consultative_council; guarantee_hajj_routes; reopen_jeddah_customs; secure_pilgrim_transit; call_the_arabian_congress | 3 projects + support + cap |
| DSX | A | seat_the_oyo_mesi; reconcile_ibadan; raise_the_alaafins_horse_guard; convene_the_yoruba_towns; prepare_regional_integration_authority | 4 projects + cap |
| DUX | A | seat_the_shehus_council; reopen_the_lake_chad_routes; raise_the_kanembu_horse; secure_lake_chad_market_routes; prepare_regional_integration_authority | 3 projects + support + cap |
| FDX | A | seat_the_punjab_assembly; settle_the_canal_water_shares; charter_the_punjab_regiments; settle_the_canal_colony_boundary; prepare_regional_integration_authority | 3 projects + support + cap |
| HAR | A | seat_the_merchants_council; reopen_the_zeila_caravan_road; raise_the_city_guard; protect_the_zeila_caravan_accounts; prepare_regional_integration_authority | 3 projects + support + cap |
| HYD | A | reform_the_legislative_council; abolish_the_jagir_levies; expand_osmania_university; settle_the_deccan_railway_accounts; prepare_regional_integration_authority | 3 projects + support + cap |
| IMO | A | convene_shaykhs_at_nizwa; renew_the_treaty_of_seeb OR close_the_coast_road; open_interior_caravan_routes; prepare_regional_integration_authority | 4 projects + cap |
| KAS | A | widen_the_praja_sabha; open_the_banihal_road; settle_the_weavers_wages; protect_the_banihal_road_agreements; prepare_regional_integration_authority | 3 projects + support + cap |
| LEB | A | apportion_the_great_offices OR open_offices_to_every_citizen; settle_mandate_accounts; proclaim_the_free_port_of_beirut; prepare_regional_integration_authority | 4 projects + cap |
| MAD | A | convene_the_malagasy_assembly; open_the_tamatave_line; recall_the_vvs_exiles; secure_the_tamatave_export_route; prepare_regional_integration_authority | 3 projects + support + cap |
| MYS | A | seat_the_representative_assembly; expand_the_bhadravati_works; open_the_krishnaraja_sagara_canals; secure_bhadravati_and_canal_transit; prepare_regional_integration_authority | 3 projects + support + cap |
| PAL | A | convene_the_legislative_council; appoint_the_land_registry_commission; guarantee_the_holy_places; secure_shared_municipal_passage; prepare_regional_integration_authority | 3 projects + support + cap |
| PSH | A | convene_the_grand_jirga; recognize_the_khudai_khidmatgar; garrison_the_khyber; settle_the_khyber_transit_terms; prepare_regional_integration_authority | 3 projects + support + cap |
| RIF | A | convene_the_rif_national_assembly; unify_the_tribal_levies; fortify_the_mountain_redoubts; restore_the_ajdir_network; prepare_regional_integration_authority | 4 projects + cap |
| RWA | A | convene_the_mwamis_council; abolish_the_ubuhake_contracts; open_lake_kivu_trade; secure_lake_kivu_access; prepare_regional_integration_authority | 3 projects + support + cap |
| SIN | A | seat_the_sind_assembly; allot_the_barrage_lands; open_karachi_trade; protect_the_barrage_lands_and_wharves; prepare_regional_integration_authority | 3 projects + support + cap |
| SOM | A | convene_the_sultans_council; open_berbera_to_gulf_trade; divide_the_grazing_wells; protect_the_grazing_well_compact; prepare_regional_integration_authority | 3 projects + support + cap |
| TIG | A | convene_the_council_at_mekele; settle_the_church_lands_of_aksum; garrison_the_highland_passes; secure_the_mekele_highland_passage; prepare_regional_integration_authority | 3 projects + support + cap |
| UGA | A | convene_the_great_lukiiko; settle_the_mailo_land_claims; open_the_port_bell_wharf; secure_mailo_boundary_accounts; prepare_regional_integration_authority | 3 projects + support + cap |
| ATJ | B | convene_council_of_notables; fund_madrasah_reform; reopen_pepper_ports; confirm_aceh_port_and_succession_terms; call_sumatran_maritime_congress | 3 projects + support + cap |
| ATX | B | convene_assembly_of_venice; charter_marghera_works; restore_the_arsenale; settle_venetian_port_guarantees; call_adriatic_congress | 3 projects + support + cap |
| BLI | B | convene_paruman_agung; restore_subak_courts; open_island_steamers; guarantee_subak_and_village_rights; call_bali_maritime_congress | 3 projects + support + cap |
| CIN | B | convene_mekhk_khel; take_over_grozny_oil_fields; raise_mountain_guard; confirm_chechen_mountain_terms; call_chechen_federal_congress | 3 projects + support + cap |
| CLX | B | convene_the_khase; invite_diaspora_home; raise_kabardian_horse; settle_homeland_and_diaspora_claims; call_northwest_caucasian_congress | 3 projects + support + cap |
| DAG | B | seat_federal_assembly; fix_the_languages_of_state; open_caspian_ports; guarantee_constituent_rights; call_dagestani_federal_congress | 3 projects + support + cap |
| FOX | B | seat_assam_assembly; reform_tea_garden_contracts; open_brahmaputra_steamers; ratify_assam_provincial_guarantees; call_northeast_congress | 3 projects + support + cap |
| FUX | B | join_adat_and_ulama; charter_thawalib_schools; take_over_ombilin_mines; settle_adat_revenue_claims; call_minangkabau_federation_congress | 3 projects + support + cap |
| GCX | B | bind_federal_council; extend_lashio_railway; regulate_bawdwin_mines; ratify_shan_federal_safeguards; call_shan_federal_congress | 3 projects + support + cap |
| GMX | B | convene_oasis_delegates; reopen_caravan_roads; raise_oasis_guards; confirm_oasis_frontier_terms; call_turkestan_congress | 3 projects + support + cap |
| GZX | B | restore_responsible_government; settle_the_bondholders; found_fisheries_board; confirm_newfoundland_dominion_terms; call_north_atlantic_congress | 3 projects + support + cap |
| HCX | B | seat_legislature_at_austin; empower_railroad_commission; muster_ranger_companies; confirm_texas_border_settlement; call_gulf_congress | 3 projects + support + cap |
| IAX | B | seat_council_at_moulmein; open_mon_language_schools; reopen_moulmein_port; guarantee_mon_language_and_port_terms; call_mon_federal_congress | 3 projects + support + cap |
| IBX | B | convene_duwas_at_myitkyina; raise_kachin_levies; open_jade_mines_road; secure_kachin_frontier_guarantees; call_kachin_highland_congress | 3 projects + support + cap |
| LAO | B | unite_provinces_under_crown; open_mekong_route; fund_buddhist_institute; settle_the_royal_boundary_question; call_lan_xang_congress | 3 projects + support + cap |
| MEN | B | convene_autonomy_council; settle_banner_pastures; raise_banner_cavalry; ratify_banner_self_government; call_mongolic_congress | 3 projects + support + cap |
| MPU | B | convene_durbar_with_hill_chiefs; open_imphal_road; fund_hill_schools; confirm_valley_hill_guarantees; call_manipur_federation_congress | 3 projects + support + cap |
| OKN | B | seat_assembly_at_shuri; relieve_sugar_debts; open_emigrant_bank; settle_sugar_and_maritime_accounts; call_ryukyu_island_congress | 3 projects + support + cap |
| QUE | B | seat_legislative_assembly; nationalise_power_trusts; charter_caisses_populaires; ratify_quebec_federal_terms; call_saint_lawrence_congress | 3 projects + support + cap |
| RAS | B | proclaim_temple_entry; seat_sree_mulam_assembly; expand_cochin_harbour; ratify_madras_host_terms; call_dravidian_congress | 3 projects + support + cap |
| SAM | B | convene_fono_of_faipule; return_reparation_estates; open_apia_copra_market; honor_the_fono_land_compact; call_polynesian_congress | 3 projects + support + cap |
| YUC | B | seat_yucatan_congress; turn_haciendas_into_ejidos; open_port_of_progreso; ratify_yucatan_local_settlement; call_yucatan_regional_congress | 3 projects + support + cap |

All table rows have source coverage. The imported-tree visual status remains unresolved for each row for the same MCP boundary described below.

## Route, decision, and pacing checks

The source inventory found 220 unique shared-focus definitions, 220 unique main-tree imports, no duplicate ids, and no missing or unimported ids. Each of the 44 tags has five definitions. All groups are package-gated through exact original-tag or package triggers, active framework generation, and current capital control. There are no static X-tag scopes in the A/B focus helper effects.

All 136 project focuses map to one existing paid decision, and each focus calls the same completion helper used in that decision's remove_effect. The exact source crosswalk found 136/136 helper matches. Each paid decision checks its matching focus progress and completion in the reverse direction. The focus-side available gates check their paid decision. The only four directed mutual-exclusion declarations are the symmetric IMO Treaty of Seeb/coast-road pair and LEB Great Offices/Civic Charter pair. Both alternatives' decisions also block the opposing focus and active decision.

During this review, the parent added explicit cancel_if_invalid = yes, continue_if_invalid = no, and matching completion_reward has_decision rechecks to the 69 project nodes that had relied on native focus defaults. A bounded post-edit source check found 136/136 project focuses with both explicit cancellation fields and 136/136 completion rewards rechecking every matching active decision id. This closes the source-level zero-progress consistency edge. The same-frame native UI/effect ordering remains untested.

The forty ordinary groups use three short project focuses, a long host-support focus, and a long regional-congress capstone. Focus cost tokens are short=5, standard=7, and long=10, which are 35, 49, and 70 days under the seven-day focus point. The ordinary group subtotal is 245 days before main-tree prerequisites. Across the 220 nodes the source uses 133 short, 3 standard, and 84 long cost tokens.

Host support uses the existing diplomatic-standard cost: 20 command power plus either 10 convoys or 10 trains. Its reward calls the selected host-policy continuation when that host is alive, or package-specific domestic boundary deltas after collapse. A has one recipient-owned support receipt; B also records and checks the current generation. Both cleanup functions are called from independence_wave_clear_focus_runtime, used on generation reset and origin end.

The parent clarified that the dual-lock contract is the 136 focus/decision mappings in both directions plus the four bilateral IMO/LEB alternative checks. It does not add paid-decision gates to the 40 host-support nodes; their accepted child-focus prerequisites already represent resolved or bypassed project actions. This review found no extra host-support gate defect.

The two main survey/congress focus rewards retain existing-open and existing-called guards. Their bypass conditions use the same persistent flags, so a country-specific capstone or earlier branch that opens/calls the shared system does not repeat the generic reward. The generic postwar integration authority still requires both independence_wave_support_local_committees and independence_wave_call_regional_congress, preserving the Local Committees route.

## Icon and filter coverage

All 220 focuses set search_filters. Reviewed tags map to political/stability for councils and settlements, industry for infrastructure or commerce, manpower/war support for force projects, and research for schools or universities. No missing or misleading filter was found.

All focus icons resolve to existing sprites in interface/006_independence_wave.gfx and DDS assets in gfx/interface/goals/006_independence_wave/. The same eight role icons are reused across packages, consistent with the shared-tree contract. This is visible repetition but no broken or mismatched icon reference was found.

| Sprite id | Uses | Runtime resolution |
| --- | ---: | --- |
| GFX_goal_independence_wave_army_integration | 14 | Defined and DDS present |
| GFX_goal_independence_wave_former_host_settlement | 43 | Defined and DDS present |
| GFX_goal_independence_wave_founding_administration | 43 | Defined and DDS present |
| GFX_goal_independence_wave_infrastructure_authority | 31 | Defined and DDS present |
| GFX_goal_independence_wave_league_congress | 45 | Defined and DDS present |
| GFX_goal_independence_wave_military_emergency | 2 | Defined and DDS present |
| GFX_goal_independence_wave_popular_councils | 28 | Defined and DDS present |
| GFX_goal_independence_wave_recognition_diplomacy | 14 | Defined and DDS present |

## Localisation and reward matching

All 220 focus title and description keys exist in the A/B English files. All 242 custom_effect_tooltip references resolve. The 136 project-result tooltip values use nested-localisation aliases to the matching paid decision result key: 136/136 targets exist across the nine regional decision locale files and 136/136 aliases exactly match the focus's source decision id. The 136 focus completion helper calls also match the corresponding paid decision's remove_effect helper.

No source key, id, or helper mismatch remained in the reviewed CUX, IMO, LEB, MPU, IAX, and RAS samples; the 136-row source-to-decision alias check found no target mismatch. This proves that the focuses reuse the existing decision text and result helper, not that every older decision tooltip has been independently re-authored against every modifier. The probability handoff records that the 43 A-side raw-flag localisation warnings were resolved with dedicated keys and the subsequent script_validate response returned zero findings for that file.

The four opposed focus bypasses use the distinct project outcome flags set by their matching helpers: IMO treaty renewed vs coast road closed, and LEB offices apportioned vs offices opened. Each pair's shared completion receipt remains separate from its mutually exclusive branch marker. This avoids one decision's shared receipt bypassing both alternative focus nodes.

## AI, MCP evidence, and limits

All 220 nodes contain ai_will_do and all 220 have search filters. The weights use the shared urgent, high, and standard score constants. The Event 006 AI strategy registry contains no focus_factors or ai_national_focuses entry for these new groups, so current focus-file behavior is static availability-gated scoring, not country-state route weighting.

The parent probability handoff at subagent_handoffs/regional_focus_probability_20261006.md is partial. It reports zero discovered focus candidates for the A/B shared-focus fragments, no complete country-specific five-candidate pools for the 44 groups, and no numeric selection result. The generic survey/congress and Levant/Arabia compares had zero eligible candidates and unresolved inputs. I did not repeat the same failed probability calls or choose new weights. This evidence cannot support a numeric balance or AI route-selection claim.

The focus context and targeted reference routes were available. Installed documentation had no dedicated focus-tree syntax page, so offline National focus modding sections were read alongside installed focus-related effects/triggers documentation and an exact vanilla shared-focus precedent.

| Reference | Lines or section | Revision |
| --- | --- | --- |
| Offline wiki National focus modding: Focus tree and shared focuses | 43-94 and 818-838 | bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203 |
| Offline wiki National focus modding: prerequisites, mutual exclusions, bypass, available, and allow_branch | 275-296 and 405-429 | bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203 |
| Offline wiki National focus modding: focus rewards, cost, AI, and search filters | 430-454, 297-302, 604-626, and 455-502 | bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203 |
| Offline wiki Localisation: nesting strings | 244-259 | 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064 |
| Offline wiki Triggers: focus_progress and has_decision | 704 and 647 | abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64f9c0c0ce06 |
| Installed triggers documentation: focus_progress, has_decision, and has_focus_tree | 2882-2891, 3693-3701, and 3948-3956 | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| Installed effects documentation: complete_national_focus and load_focus_tree | 2870-2878 and 4771-4789 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Vanilla shared focus definition and import | game:common/national_focus/china_shared.txt:38 and game:common/national_focus/china_nationalist.txt:58 | 545c16f62a0511d0c4bc62e1b9bf4284cfbe6edb9eebef7108003b2412e78958 |

The read-only focus_inspect call on independence_wave_focus_tree returned one tree with 184 direct nodes, 196 connectors, zero tree-layout diagnostics, and bounds x=1..121/y=0..19. The artifact revision was f20a8917bc4e3e54412122d8f901e23e9f20e2f947d9446ae1e0def6770627b4 and the direct-tree layout hash was ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb. The same call emitted an unrelated game-source parser diagnostic at game:common/national_focus/TSR_lingguang_incident_joint_branch.txt:469 and an inline inventory truncation notice (64 of 209 paths); neither identifies an error in the task-owned focus sources.

The read-only focus_render call returned a 21,424 by 2,440 render of the same 184 direct nodes. The HTML, SVG, and JSON artifacts are available at:

- [Direct-tree SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65038c84aafa45b0dedf8601921c47fde21d986764e0ee05922593b0020b7bce/46f47ba6a8f3752730b43afda9e1a2bedb28b32e245122b93628752a64a9aed1/independence_wave_focus_tree.focus.svg)
- [Direct-tree HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d36d63b3e9dc4b31c633730602e07b98dc28d8f043ddd7bb6f3137c6cd4bd806/cada47d385e759dad0af23e4b9cd110ab0ac6b47062393f5c7a5cc136e3d34df/independence_wave_focus_tree.focus.html)
- [Direct-tree source map](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3fa49c14ea1895253ad24f62120f0ba3bebe434bee8242647e0876e1a42fec2/f0d9ab9c16f98c9a990f9396b9116f7ec831487907d16c31336fee45cc5b307a/independence_wave_focus_tree.focus.source-map.json)

Focus inspection and rendering returned FOCUS_TREE_NOT_FOUND for the A and B fragment files because neither fragment contains a focus_tree block. The main focus file imports the 220 shared ids, but the inspector still reports only the 184 direct nodes. The render therefore cannot prove placement, overlap, or connector behavior for any new group. The parent probability handoff additionally records that narrow raster attempts could not render the 21,424-pixel-wide direct tree within the 16,384-pixel limit. No focus_rewrite or raster retry was made in this read-only pass.

The parent reports that the later main focus validator transport is closed. The post-hardening source count is not accompanied by a post-edit MCP focus comparison or native engine execution; the parent owns that remaining validation disposition.

## Forced-completion boundary

The installed complete_national_focus documentation and offline wiki describe completing the focus and running its completion reward. No direct complete_national_focus caller for any of these 220 nodes was found in the scoped Event 006 focus, decision, or scripted-effect files. The retrieved documentation does not specify whether available triggers and parent prerequisites are re-evaluated by a direct call, so the possible bypass is an inference rather than confirmed engine behavior.

A deliberate external complete_national_focus call may skip the normal UI selection sequence. Reward limits recheck package, generation/readiness, result receipt, active decisions, payment, or host policy as relevant, but they do not repeat every parent-focus prerequisite. If the parent wants scripted or console forced completion to preserve the five-node route order, add parent-focus checks to the relevant reward limits and prior-result receipt checks to support/capstone rewards. For example, the CUX host-support node can check its Hajj and Jeddah receipts before paying; the Arabian Congress cap can check the host-support receipt. Four-project capstones need receipt conditions for compatible projects and an OR across the accepted IMO/LEB alternative pair. This is an out-of-band hardening recommendation, not a normal-route defect or an implemented change.

## Simplifications, omissions, and blockers

No accepted Level 2 group, focus node, project helper, paid decision mapping, or route capstone was omitted or replaced. The shared five-node group contract is the accepted L2 design, not a simplified substitute for a full national tree. The unresolved items are imported-node MCP layout and numeric AI selection evidence, not source route coverage.

Source coverage passes for the 44 accepted Level 2 groups, 220 root-tree imports, 136 focus/decision/helper mappings, the four bilateral opposing choices, localisation key coverage, filter assignments, and existing icon sprite/DDS paths. The two material evidence limits are imported-node MCP layout and numeric AI selection. A later direct-tree source validation call was reported as Transport closed by the parent. No in-game or debug test was run by this reviewer. No improvement plan was written because no new route family or broader redesign is within this audit's scope.

Skills applied: chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, and chaos-redux-improvement-loop. No skill was created or updated.

Parent-facing handoffs reviewed: subagent_handoffs/regional_focus_a_20261006.md, subagent_handoffs/regional_focus_b_20261006.md, and subagent_handoffs/regional_focus_probability_20261006.md.

Files changed by this reviewer: docs/plans/006_independence_wave_plans/subagent_handoffs/regional_focus_review_20261006.md only.

No focus ids or localisation keys were changed by this reviewer. No in-game test, source patch, or commit was performed.
