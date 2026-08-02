# 006 localisation style cleanup handoff

Scope: all `localisation/english/006_*.yml` files. The pass preserved localisation keys, dynamic tokens, format codes, gameplay meaning, and the pre-existing collection labels in `006_independence_wave_l_english.yml`.

## Changed files and keys

- `006_independence_wave_l_english.yml`: `chaosx.nr6.2.d`.
- `006_independence_wave_brittany_l_english.yml`: `independence_wave_bri_convene_celtic_delegation_desc`.
- `006_independence_wave_evolution_incidents_l_english.yml`: `chaosx.nr6.360.d`, `chaosx.nr6.362.d`, `chaosx.nr6.363.d`.
- `006_independence_wave_focus_l_english.yml`: `independence_wave_proclaim_radical_sovereignty_desc`, `independence_wave_propose_armed_liberation_desc`, `independence_wave_sponsor_further_ruptures_tt`.
- `006_independence_wave_form01_02_04_l_english.yml`: `independence_wave_form01_congress_category_desc`, `independence_wave_form01_rotate_congress_session_desc`, `independence_wave_form01_coordinate_maritime_defence_desc`, `independence_wave_form01_ratify_celtic_compact_desc`, `independence_wave_form02_build_air_warning_chain_desc`, `independence_wave_form04_ratify_rhenish_charter_desc`, `chaosx.nr6.341.d`.
- `006_independence_wave_form03_l_english.yml`: `chaosx.nr6.300.d`, `chaosx.nr6.302.b.tt`.
- `006_independence_wave_formable_registry_l_english.yml`: `independence_wave_choose_controlled_settlement_desc`, `independence_wave_form03_join_as_autonomous_member_desc`, `independence_wave_form39_dissolve_federation_desc`.
- `006_independence_wave_ice_l_english.yml`: `independence_wave_ice_negotiate_north_atlantic_compact_desc`, `ice_exposed_north_atlantic_charter_desc`.
- `006_independence_wave_iw005_flanders_l_english.yml`: `independence_wave_iw005_flanders_category_desc`.
- `006_independence_wave_iw043_iw058_decisions_l_english.yml`: `independence_wave_iw058_ratify_aramean_self_identification_desc`.
- `006_independence_wave_iw043_iw058_events_l_english.yml`: `chaosx.nr006.4301.desc`, `chaosx.nr006.4302.tatar.desc`, `chaosx.nr006.4302.resident.desc`, `chaosx.nr006.4303.desc`, `chaosx.nr006.4307.t`, `chaosx.nr006.4307.desc`, `chaosx.nr006.4309.desc`, `chaosx.nr006.4311.a.tt`, `chaosx.nr006.5802.assyrian.desc`, `chaosx.nr006.5802.chaldean.desc`, `chaosx.nr006.5809.desc`, `chaosx.nr006.5811.desc`.
- `006_independence_wave_iw043_iw058_focus_l_english.yml`: `independence_wave_iw043_confirm_kazan_mandate_desc`, `independence_wave_iw043_negotiate_volga_ural_accessions_desc`, `independence_wave_iw043_organize_the_river_guard`, `independence_wave_iw058_assemble_provisional_national_council_desc`, `independence_wave_iw058_bind_diaspora_experts_to_public_service_desc`, `independence_wave_iw058_seat_church_civic_and_village_delegates_desc`, `independence_wave_iw058_convene_concordat_council_desc`.
- `006_independence_wave_iw093_iw098_decisions_l_english.yml`: `independence_wave_iw093_train_forest_guard_desc`.
- `006_independence_wave_pacific_l_english.yml`: `fsm_scattered_island_authority_desc`, `independence_wave_hbx_prepare_pacific_maritime_congress_desc`, `independence_wave_haw_delegation_project_tt`, `independence_wave_fsm_delegation_project_tt`, `independence_wave_haw_ratify_autonomous_pacific_mandate_focus_tt`, `independence_wave_haw_dispatch_pacific_delegation_focus_tt`, `independence_wave_form48_invitation_category_desc`, `independence_wave_form48_accept_autonomous_membership_tt`, `independence_wave_form48_federal_coordination_desc`.
- `006_independence_wave_rhineland_bavaria_l_english.yml`: `chaosx.nr6.13.d`.
- `006_independence_wave_rival_bloc_l_english.yml`: `independence_wave_rival_bloc_category_desc`.
- `006_independence_wave_scenario_l_english.yml`: `independence_wave_scenario_summary_outcome_failed`, `independence_wave_scenario_ledger_category_desc`, `independence_wave_scenario_reject_unbound_current_map`, `independence_wave_scenario_reject_unknown`.
- `006_independence_wave_scotland_wales_l_english.yml`: `wls_divided_valleys_administration_desc`.
- `006_independence_wave_wallonia_frisia_l_english.yml`: `independence_wave_afx_mandate_meuse_conference_focus_desc`, `independence_wave_agx_mandate_north_sea_coastal_conference_focus_desc`, `chaosx.nr6.20.d`.

The collection-label additions already present in `006_independence_wave_l_english.yml` were not rewritten or removed.

## Audit results

Missing player-facing keys: none found in explicit title, description, tooltip, option, category, or name slots after excluding script identifiers and UI window identifiers. The three apparent scan hits are `independence_wave_industrial_administration_bonus`, `independence_wave_professional_defense_bonus`, and `independence_wave_status_window`. They are effect or GUI identifiers, not localisation keys.

Duplicate keys: none across the 006 files after excluding the `l_english` language marker.

Scripted localisation issues: no missing `localization_key` targets in 006 scripted-localisation files. The four scenario intensity labels resolve from the shared `chaosx_gui_l_english.yml` file, so they are intentional cross-file references.

Dynamic text opportunities: existing status and category surfaces already expose live values through `[?...]` formatters and scripted localisation. No new dynamic localisation was needed for this prose-only pass. Static route names and historical labels remain static because they identify fixed content rather than changing state.

Cross-surface mismatch notes: the changed keys retain their original namespaces and identifiers. Event descriptions, focus descriptions, decision tooltips, scenario ledgers, and formable category text now use direct wording while preserving the same route, cost, guarantee, sovereignty, and integration meaning. The pre-existing collection-label insertions were preserved.

Encoding: every 006 localisation file retains a UTF-8 BOM. Touched files currently use LF line endings, while Git reports its normal CRLF conversion warning. No BOM loss was detected.

## Remaining wording review

The targeted contrast and process rewrites are complete. The final four keys covered in the last retry were `chaosx.nr006.5811.desc`, `chaosx.nr6.20.d`, `chaosx.nr6.302.b.tt`, and `independence_wave_scenario_reject_unknown`.

## Validation

The style scan found no em dash or semicolon in 006 localisation values. No colon-zero keys were found. Duplicate-key and BOM checks passed. A token comparison against `HEAD` found no changes to format, currency, bracketed dynamic-value, or scripted-reference tokens. Static scripted-localisation references were checked against the full English localisation set. No in-game launch was performed because live consumer validation belongs to the parent and user.

Unresolved wording decision: no route or mechanic wording decisions remain. Proper-name hyphens such as `Kazan-Cheboksary` and `Araucania-Patagonia` were retained because they are geographic names and are not em dashes.

Plan handoff path: `docs/plans/player_facing_text_style_cleanup/subagent_handoffs/loc_006_localisation_style_cleanup_handoff_2026-08-02.md`.
