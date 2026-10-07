# Event 006 Regional Framework Focus A Handoff

**Disposition:** implemented at source level. The parent owns shared-tree registration, paid-decision interlocks, cleanup wiring, probability comparison, and final integration review.

**Acceptance basis:** the parent task authorized the first 22 admitted Event 006 Level 2 regional packages only. The parent accepted the five-node contract for three-project rows, the four-project adaptation, the 70-day paid former-host support step, and the regional congress cap under the user's Event 006 implementation authorization. The future-plan bullet in the package overview is evidence of queued design scope, not independent approval.

## Files changed

- `common/national_focus/006_independence_wave_regional_focus_a.txt` contains 110 root-level `shared_focus` definitions, five per assigned country.
- `localisation/english/006_independence_wave_regional_focus_a_l_english.yml` contains all focus title, description, and effect-tooltip keys, plus readable requirement and implementation-flag labels.
- `common/scripted_effects/006_independence_wave_regional_focus_a_effects.txt` contains the paid host-support transaction and one cleanup helper. The parent explicitly expanded my ownership to this file.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/regional_focus_a_20261006.md` is this handoff.

The exact country set is CUX, IMO, LEB, PAL, RIF, DSX, DUX, UGA, RWA, BRD, HAR, SOM, TIG, BAR, MAD, FDX, SIN, BLC, PSH, KAS, HYD and MYS. No country outside this set is defined in the file.

## Shared-focus structure and paid-project mapping

Every node requires the full Event 006 framework, `is_independence_wave_regional_framework_live = yes`, and the country's exact `original_tag`. Project completions also require the current controlled-capital project-ready trigger. The live trigger checks the regional package, current runtime generation, completed setup receipt and non-ended origin. No static X-tag runtime scope is used.

The common three-project route has a country-specific council or assembly opener, two compatible sibling project focuses, a 70-day host-support focus after both branches and a 70-day regional congress cap. The four-project rows IMO, LEB, RIF and DSX map all four existing project completion helpers into the group and add the congress cap. Sibling projects remain compatible except for the already-mutually-exclusive IMO Treaty of Seeb/coast-road and LEB Great Offices/Civic Charter choices.

A project focus calls the exact package completion helper used by its matching paid decision and bypasses when the existing completion receipt is present. Its availability blocks while the matching decision is in progress. For the IMO and LEB alternative pairs, the matching sibling decision is also checked while either focus is in progress. The parent must add the reverse decision-side lock for each matching focus. Other sibling projects receive no added mutual exclusion.

The LEB focus route uses the Pact/Charter fork as two equal roots, followed by Mandate Accounts, the Free Port, and the regional congress cap. This order exists only in the focus path to keep the shared-focus fork and convergence clean. The paid decisions retain their accepted availability rules and remain usable in their original order.

### Paid-project focus, decision, helper, and receipt crosswalk

| Tag | Focus ID | Existing paid decision | Shared completion helper | Existing completion receipt |
| --- | --- | --- | --- | --- |
| CUX | `independence_wave_cux_focus_seat_consultative_council` | `independence_wave_cux_seat_consultative_council` | `independence_wave_cux_complete_consultative_council` | `independence_wave_cux_council_seated` |
| CUX | `independence_wave_cux_focus_guarantee_hajj_routes` | `independence_wave_cux_guarantee_hajj_routes` | `independence_wave_cux_complete_hajj_routes` | `independence_wave_cux_hajj_routes_guaranteed` |
| CUX | `independence_wave_cux_focus_reopen_jeddah_customs` | `independence_wave_cux_reopen_jeddah_customs` | `independence_wave_cux_complete_jeddah_customs` | `independence_wave_cux_jeddah_customs_reopened` |
| IMO | `independence_wave_imo_focus_convene_shaykhs_at_nizwa` | `independence_wave_imo_convene_shaykhs_at_nizwa` | `independence_wave_imo_complete_shaykhs_council` | `independence_wave_imo_shaykhs_convened` |
| IMO | `independence_wave_imo_focus_renew_the_treaty_of_seeb` | `independence_wave_imo_renew_treaty_of_seeb` | `independence_wave_imo_complete_treaty_of_seeb` | `independence_wave_imo_seeb_settled` |
| IMO | `independence_wave_imo_focus_close_the_coast_road` | `independence_wave_imo_close_the_coast_road` | `independence_wave_imo_complete_coast_road_closure` | `independence_wave_imo_seeb_settled` |
| IMO | `independence_wave_imo_focus_open_interior_caravan_routes` | `independence_wave_imo_open_caravan_routes` | `independence_wave_imo_complete_caravan_routes` | `independence_wave_imo_caravan_routes_open` |
| LEB | `independence_wave_leb_focus_apportion_the_great_offices` | `independence_wave_leb_apportion_great_offices` | `independence_wave_leb_complete_great_offices` | `independence_wave_leb_pact_settled` |
| LEB | `independence_wave_leb_focus_open_offices_to_every_citizen` | `independence_wave_leb_open_offices_to_every_citizen` | `independence_wave_leb_complete_civic_charter` | `independence_wave_leb_pact_settled` |
| LEB | `independence_wave_leb_focus_settle_mandate_accounts` | `independence_wave_leb_settle_mandate_accounts` | `independence_wave_leb_complete_mandate_accounts` | `independence_wave_leb_mandate_accounts_settled` |
| LEB | `independence_wave_leb_focus_proclaim_the_free_port_of_beirut` | `independence_wave_leb_proclaim_free_port_of_beirut` | `independence_wave_leb_complete_free_port` | `independence_wave_leb_free_port_proclaimed` |
| PAL | `independence_wave_pal_focus_convene_the_legislative_council` | `independence_wave_pal_convene_legislative_council` | `independence_wave_pal_complete_legislative_council` | `independence_wave_pal_council_convened` |
| PAL | `independence_wave_pal_focus_appoint_the_land_registry_commission` | `independence_wave_pal_appoint_land_commission` | `independence_wave_pal_complete_land_commission` | `independence_wave_pal_land_commission_sat` |
| PAL | `independence_wave_pal_focus_guarantee_the_holy_places` | `independence_wave_pal_seek_holy_places_guarantee` | `independence_wave_pal_complete_holy_places_guarantee` | `independence_wave_pal_holy_places_guaranteed` |
| RIF | `independence_wave_rif_focus_convene_the_rif_national_assembly` | `independence_wave_rif_convene_national_assembly` | `independence_wave_rif_complete_national_assembly` | `independence_wave_rif_assembly_convened` |
| RIF | `independence_wave_rif_focus_unify_the_tribal_levies` | `independence_wave_rif_unify_tribal_levies` | `independence_wave_rif_complete_regular_army` | `independence_wave_rif_levies_unified` |
| RIF | `independence_wave_rif_focus_fortify_the_mountain_redoubts` | `independence_wave_rif_fortify_mountain_redoubts` | `independence_wave_rif_complete_mountain_redoubts` | `independence_wave_rif_redoubts_fortified` |
| RIF | `independence_wave_rif_focus_restore_the_ajdir_network` | `independence_wave_rif_restore_ajdir_network` | `independence_wave_rif_complete_ajdir_network` | `independence_wave_rif_ajdir_network_restored` |
| DSX | `independence_wave_dsx_focus_seat_the_oyo_mesi` | `independence_wave_dsx_seat_oyo_mesi` | `independence_wave_dsx_complete_oyo_mesi` | `independence_wave_dsx_oyo_mesi_seated` |
| DSX | `independence_wave_dsx_focus_reconcile_ibadan` | `independence_wave_dsx_reconcile_ibadan` | `independence_wave_dsx_complete_ibadan` | `independence_wave_dsx_ibadan_reconciled` |
| DSX | `independence_wave_dsx_focus_raise_the_alaafins_horse_guard` | `independence_wave_dsx_raise_horse_guard` | `independence_wave_dsx_complete_horse_guard` | `independence_wave_dsx_horse_guard_raised` |
| DSX | `independence_wave_dsx_focus_convene_the_yoruba_towns` | `independence_wave_dsx_convene_yoruba_towns` | `independence_wave_dsx_complete_yoruba_towns` | `independence_wave_dsx_yoruba_towns_convened` |
| DUX | `independence_wave_dux_focus_seat_the_shehus_council` | `independence_wave_dux_seat_shehus_council` | `independence_wave_dux_complete_shehus_council` | `independence_wave_dux_shehus_council_seated` |
| DUX | `independence_wave_dux_focus_reopen_the_lake_chad_routes` | `independence_wave_dux_reopen_lake_chad_routes` | `independence_wave_dux_complete_lake_routes` | `independence_wave_dux_lake_routes_reopened` |
| DUX | `independence_wave_dux_focus_raise_the_kanembu_horse` | `independence_wave_dux_raise_kanembu_horse` | `independence_wave_dux_complete_kanembu_horse` | `independence_wave_dux_kanembu_horse_raised` |
| UGA | `independence_wave_uga_focus_convene_the_great_lukiiko` | `independence_wave_uga_convene_great_lukiiko` | `independence_wave_uga_complete_great_lukiiko` | `independence_wave_uga_lukiiko_convened` |
| UGA | `independence_wave_uga_focus_settle_the_mailo_land_claims` | `independence_wave_uga_settle_mailo_claims` | `independence_wave_uga_complete_mailo_claims` | `independence_wave_uga_mailo_claims_settled` |
| UGA | `independence_wave_uga_focus_open_the_port_bell_wharf` | `independence_wave_uga_open_port_bell_wharf` | `independence_wave_uga_complete_port_bell` | `independence_wave_uga_wharf_opened` |
| RWA | `independence_wave_rwa_focus_convene_the_mwamis_council` | `independence_wave_rwa_convene_mwami_council` | `independence_wave_rwa_complete_mwami_council` | `independence_wave_rwa_council_convened` |
| RWA | `independence_wave_rwa_focus_abolish_the_ubuhake_contracts` | `independence_wave_rwa_abolish_ubuhake` | `independence_wave_rwa_complete_ubuhake` | `independence_wave_rwa_ubuhake_abolished` |
| RWA | `independence_wave_rwa_focus_open_lake_kivu_trade` | `independence_wave_rwa_open_kivu_trade` | `independence_wave_rwa_complete_kivu_trade` | `independence_wave_rwa_kivu_trade_opened` |
| BRD | `independence_wave_brd_focus_reconcile_the_bezi_and_batare` | `independence_wave_brd_reconcile_bezi_and_batare` | `independence_wave_brd_complete_bezi_batare` | `independence_wave_brd_princes_reconciled` |
| BRD | `independence_wave_brd_focus_settle_the_mandate_accounts` | `independence_wave_brd_settle_mandate_accounts` | `independence_wave_brd_complete_mandate_accounts` | `independence_wave_brd_accounts_settled` |
| BRD | `independence_wave_brd_focus_build_the_usumbura_lake_port` | `independence_wave_brd_build_usumbura_port` | `independence_wave_brd_complete_usumbura` | `independence_wave_brd_port_built` |
| HAR | `independence_wave_har_focus_seat_the_merchants_council` | `independence_wave_har_seat_merchants_council` | `independence_wave_har_complete_merchants_council` | `independence_wave_har_council_seated` |
| HAR | `independence_wave_har_focus_reopen_the_zeila_caravan_road` | `independence_wave_har_reopen_zeila_road` | `independence_wave_har_complete_zeila_road` | `independence_wave_har_zeila_road_open` |
| HAR | `independence_wave_har_focus_raise_the_city_guard` | `independence_wave_har_raise_highland_guard` | `independence_wave_har_complete_highland_guard` | `independence_wave_har_guard_raised` |
| SOM | `independence_wave_som_focus_convene_the_sultans_council` | `independence_wave_som_convene_sultans_council` | `independence_wave_som_complete_sultans_council` | `independence_wave_som_council_convened` |
| SOM | `independence_wave_som_focus_open_berbera_to_gulf_trade` | `independence_wave_som_open_berbera_trade` | `independence_wave_som_complete_berbera_trade` | `independence_wave_som_berbera_open` |
| SOM | `independence_wave_som_focus_divide_the_grazing_wells` | `independence_wave_som_divide_grazing_wells` | `independence_wave_som_complete_grazing_wells` | `independence_wave_som_wells_divided` |
| TIG | `independence_wave_tig_focus_convene_the_council_at_mekele` | `independence_wave_tig_convene_mekele_council` | `independence_wave_tig_complete_mekele_council` | `independence_wave_tig_council_convened` |
| TIG | `independence_wave_tig_focus_settle_the_church_lands_of_aksum` | `independence_wave_tig_settle_aksum_church_lands` | `independence_wave_tig_complete_church_lands` | `independence_wave_tig_church_lands_settled` |
| TIG | `independence_wave_tig_focus_garrison_the_highland_passes` | `independence_wave_tig_garrison_highland_passes` | `independence_wave_tig_complete_highland_passes` | `independence_wave_tig_passes_garrisoned` |
| BAR | `independence_wave_bar_focus_convene_the_national_kuta` | `independence_wave_bar_convene_national_kuta` | `independence_wave_bar_complete_national_kuta` | `independence_wave_bar_kuta_convened` |
| BAR | `independence_wave_bar_focus_restore_the_floodplain_canals` | `independence_wave_bar_restore_floodplain_canals` | `independence_wave_bar_complete_canals` | `independence_wave_bar_canals_restored` |
| BAR | `independence_wave_bar_focus_regulate_the_mine_labour_contracts` | `independence_wave_bar_regulate_mine_contracts` | `independence_wave_bar_complete_mine_contracts` | `independence_wave_bar_contracts_regulated` |
| MAD | `independence_wave_mad_focus_convene_the_malagasy_assembly` | `independence_wave_mad_convene_malagasy_assembly` | `independence_wave_mad_complete_assembly` | `independence_wave_mad_assembly_convened` |
| MAD | `independence_wave_mad_focus_open_the_tamatave_line` | `independence_wave_mad_open_tamatave_line` | `independence_wave_mad_complete_tamatave` | `independence_wave_mad_tamatave_open` |
| MAD | `independence_wave_mad_focus_recall_the_vvs_exiles` | `independence_wave_mad_recall_vvs_exiles` | `independence_wave_mad_complete_vvs_exiles` | `independence_wave_mad_vvs_recalled` |
| FDX | `independence_wave_fdx_focus_seat_the_punjab_assembly` | `independence_wave_fdx_seat_punjab_assembly` | `independence_wave_fdx_complete_assembly` | `independence_wave_fdx_assembly_seated` |
| FDX | `independence_wave_fdx_focus_settle_the_canal_water_shares` | `independence_wave_fdx_settle_canal_water_shares` | `independence_wave_fdx_complete_water_shares` | `independence_wave_fdx_water_shares_settled` |
| FDX | `independence_wave_fdx_focus_charter_the_punjab_regiments` | `independence_wave_fdx_charter_punjab_regiments` | `independence_wave_fdx_complete_regiments` | `independence_wave_fdx_regiments_chartered` |
| SIN | `independence_wave_sin_focus_seat_the_sind_assembly` | `independence_wave_sin_seat_sind_assembly` | `independence_wave_sin_complete_assembly` | `independence_wave_sin_assembly_seated` |
| SIN | `independence_wave_sin_focus_allot_the_barrage_lands` | `independence_wave_sin_allot_barrage_lands` | `independence_wave_sin_complete_barrage_lands` | `independence_wave_sin_barrage_lands_allotted` |
| SIN | `independence_wave_sin_focus_open_karachi_trade` | `independence_wave_sin_open_karachi_trade` | `independence_wave_sin_complete_karachi_trade` | `independence_wave_sin_karachi_open` |
| BLC | `independence_wave_blc_focus_convene_the_kalat_assemblies` | `independence_wave_blc_convene_kalat_assemblies` | `independence_wave_blc_complete_assemblies` | `independence_wave_blc_assemblies_convened` |
| BLC | `independence_wave_blc_focus_secure_the_bolan_pass` | `independence_wave_blc_secure_bolan_pass` | `independence_wave_blc_complete_bolan` | `independence_wave_blc_bolan_secured` |
| BLC | `independence_wave_blc_focus_open_the_makran_road` | `independence_wave_blc_open_makran_road` | `independence_wave_blc_complete_makran` | `independence_wave_blc_makran_open` |
| PSH | `independence_wave_psh_focus_convene_the_grand_jirga` | `independence_wave_psh_convene_grand_jirga` | `independence_wave_psh_complete_jirga` | `independence_wave_psh_jirga_convened` |
| PSH | `independence_wave_psh_focus_recognize_the_khudai_khidmatgar` | `independence_wave_psh_recognize_khudai_khidmatgar` | `independence_wave_psh_complete_khidmatgar` | `independence_wave_psh_khidmatgar_recognized` |
| PSH | `independence_wave_psh_focus_garrison_the_khyber` | `independence_wave_psh_garrison_khyber` | `independence_wave_psh_complete_khyber` | `independence_wave_psh_khyber_garrisoned` |
| KAS | `independence_wave_kas_focus_widen_the_praja_sabha` | `independence_wave_kas_expand_praja_sabha` | `independence_wave_kas_complete_praja_sabha` | `independence_wave_kas_praja_sabha_expanded` |
| KAS | `independence_wave_kas_focus_open_the_banihal_road` | `independence_wave_kas_open_banihal_road` | `independence_wave_kas_complete_banihal` | `independence_wave_kas_banihal_open` |
| KAS | `independence_wave_kas_focus_settle_the_weavers_wages` | `independence_wave_kas_settle_weavers_wages` | `independence_wave_kas_complete_weavers` | `independence_wave_kas_weavers_settled` |
| HYD | `independence_wave_hyd_focus_reform_the_legislative_council` | `independence_wave_hyd_reform_legislative_council` | `independence_wave_hyd_complete_council` | `independence_wave_hyd_council_reformed` |
| HYD | `independence_wave_hyd_focus_abolish_the_jagir_levies` | `independence_wave_hyd_abolish_jagir_levies` | `independence_wave_hyd_complete_jagir_levies` | `independence_wave_hyd_jagir_levies_abolished` |
| HYD | `independence_wave_hyd_focus_expand_osmania_university` | `independence_wave_hyd_expand_osmania_university` | `independence_wave_hyd_complete_osmania` | `independence_wave_hyd_osmania_expanded` |
| MYS | `independence_wave_mys_focus_seat_the_representative_assembly` | `independence_wave_mys_seat_representative_assembly` | `independence_wave_mys_complete_assembly` | `independence_wave_mys_assembly_seated` |
| MYS | `independence_wave_mys_focus_expand_the_bhadravati_works` | `independence_wave_mys_expand_bhadravati_works` | `independence_wave_mys_complete_bhadravati` | `independence_wave_mys_bhadravati_expanded` |
| MYS | `independence_wave_mys_focus_open_the_krishnaraja_sagara_canals` | `independence_wave_mys_open_krishnaraja_sagara_canals` | `independence_wave_mys_complete_krs_canals` | `independence_wave_mys_canals_open` |

### Host-support and regional-cap focus IDs

The three-project packages have a paid host-support focus after both project branches. The four-project packages use their fourth paid-project focus as the local support/payoff step and then reach the regional congress cap.

| Tag | Host-support focus | Regional congress cap |
| --- | --- | --- |
| CUX | `independence_wave_cux_focus_secure_pilgrim_transit` | `independence_wave_cux_focus_call_the_arabian_congress` |
| IMO | — | `independence_wave_imo_focus_prepare_regional_integration_authority` |
| LEB | — | `independence_wave_leb_focus_prepare_regional_integration_authority` |
| PAL | `independence_wave_pal_focus_secure_shared_municipal_passage` | `independence_wave_pal_focus_prepare_regional_integration_authority` |
| RIF | — | `independence_wave_rif_focus_prepare_regional_integration_authority` |
| DSX | — | `independence_wave_dsx_focus_prepare_regional_integration_authority` |
| DUX | `independence_wave_dux_focus_secure_lake_chad_market_routes` | `independence_wave_dux_focus_prepare_regional_integration_authority` |
| UGA | `independence_wave_uga_focus_secure_mailo_boundary_accounts` | `independence_wave_uga_focus_prepare_regional_integration_authority` |
| RWA | `independence_wave_rwa_focus_secure_lake_kivu_access` | `independence_wave_rwa_focus_prepare_regional_integration_authority` |
| BRD | `independence_wave_brd_focus_secure_usumbura_lakeshore_transit` | `independence_wave_brd_focus_prepare_regional_integration_authority` |
| HAR | `independence_wave_har_focus_protect_the_zeila_caravan_accounts` | `independence_wave_har_focus_prepare_regional_integration_authority` |
| SOM | `independence_wave_som_focus_protect_the_grazing_well_compact` | `independence_wave_som_focus_prepare_regional_integration_authority` |
| TIG | `independence_wave_tig_focus_secure_the_mekele_highland_passage` | `independence_wave_tig_focus_prepare_regional_integration_authority` |
| BAR | `independence_wave_bar_focus_settle_the_lozi_mine_labour_accounts` | `independence_wave_bar_focus_prepare_regional_integration_authority` |
| MAD | `independence_wave_mad_focus_secure_the_tamatave_export_route` | `independence_wave_mad_focus_prepare_regional_integration_authority` |
| FDX | `independence_wave_fdx_focus_settle_the_canal_colony_boundary` | `independence_wave_fdx_focus_prepare_regional_integration_authority` |
| SIN | `independence_wave_sin_focus_protect_the_barrage_lands_and_wharves` | `independence_wave_sin_focus_prepare_regional_integration_authority` |
| BLC | `independence_wave_blc_focus_settle_bolan_and_makran_transit` | `independence_wave_blc_focus_prepare_regional_integration_authority` |
| PSH | `independence_wave_psh_focus_settle_the_khyber_transit_terms` | `independence_wave_psh_focus_prepare_regional_integration_authority` |
| KAS | `independence_wave_kas_focus_protect_the_banihal_road_agreements` | `independence_wave_kas_focus_prepare_regional_integration_authority` |
| HYD | `independence_wave_hyd_focus_settle_the_deccan_railway_accounts` | `independence_wave_hyd_focus_prepare_regional_integration_authority` |
| MYS | `independence_wave_mys_focus_secure_bhadravati_and_canal_transit` | `independence_wave_mys_focus_prepare_regional_integration_authority` |

## Paid host-support transaction

The 18 three-project support focuses cost 10 focus weeks, or 70 nominal days at standard speed. Their completion payment uses the existing diplomatic-standard cost trigger and effect, requiring 20 command power and either 10 convoys or 10 trains. The payment and all rewards are guarded inside one effect, and the focus remains invalid if affordability is lost during progress.

The effect uses the one host route already selected by the player. It calls exactly one matching existing negotiation, guarded-frontier, association, or reclamation helper. It then applies one package-specific Statehood delta pair. If no living former host remains, it does not scope the former host and applies the domestic boundary settlement pair instead. It declares no war and creates no claims.

| Tag | Living former host: additional country deltas | No living former host: domestic deltas |
| --- | --- | --- |
| CUX | Capacity +10, Recognition +5 | Capacity +10, Legitimacy +5 |
| PAL | Legitimacy +10, Recognition +5 | Legitimacy +10, Instability -5 |
| UGA | Legitimacy +10, Capacity +5 | Legitimacy +10, Capacity +5 |
| RWA | Legitimacy +10, Capacity +5 | Legitimacy +10, Instability -5 |
| BRD | Recognition +10, Security +5 | Legitimacy +10, Security +5 |
| HAR | Capacity +10, Recognition +5 | Capacity +10, Legitimacy +5 |
| SOM | Capacity +10, Instability -5 | Capacity +10, Security +5 |
| TIG | Security +10, Legitimacy +5 | Legitimacy +10, Security +5 |
| DUX | Capacity +10, Security +5 | Capacity +10, Legitimacy +5 |
| BAR | Capacity +10, Legitimacy +5 | Capacity +10, Instability -5 |
| MAD | Capacity +10, Recognition +5 | Capacity +10, Legitimacy +5 |
| FDX | Security +10, Capacity +5 | Security +10, Instability -5 |
| SIN | Capacity +10, Recognition +5 | Capacity +10, Instability -5 |
| BLC | Security +10, Capacity +5 | Security +10, Legitimacy +5 |
| PSH | Legitimacy +10, Security +5 | Legitimacy +10, Instability -5 |
| KAS | Legitimacy +10, Recognition +5 | Legitimacy +10, Capacity +5 |
| HYD | Capacity +10, Legitimacy +5 | Legitimacy +10, Instability -5 |
| MYS | Capacity +10, Recognition +5 | Capacity +10, Security +5 |

The single per-country-scope completion marker is `independence_wave_regional_focus_a_host_support_completed`. The parent must call `independence_wave_regional_focus_a_clear_support_receipt = yes` from the existing generic cleanup while the released country is in scope, before a later regional framework generation can reuse that country.

The congress cap opens the existing regional-ambition path if it is still closed and sets `independence_wave_regional_congress_called` to unlock the existing postwar integration-authority branch. It grants no diplomatic-step or generic Statehood bonus. The parent must guard or bypass `independence_wave_survey_regional_ambition` and `independence_wave_call_regional_congress` against those existing flags so completing either route cannot pay the shared focus reward twice. `independence_wave_support_local_committees` remains a separate requirement for the postwar authority.

## Icons, filters, and AI

No art or sprite registration was added. The focuses reuse registered Event 006 sprites: `GFX_goal_independence_wave_founding_administration`, `GFX_goal_independence_wave_popular_councils`, `GFX_goal_independence_wave_infrastructure_authority`, `GFX_goal_independence_wave_army_integration`, `GFX_goal_independence_wave_military_emergency`, `GFX_goal_independence_wave_former_host_settlement`, `GFX_goal_independence_wave_recognition_diplomacy`, and `GFX_goal_independence_wave_league_congress`. Search filters are the installed political, stability, industry, manpower, war-support, and research filters.

Focus weights use existing constants only: the opener uses `independence_wave_focus_ai.urgent`, package project nodes use `high`, and support and congress nodes use `standard`. The identical baseline and after-source campaign fixtures requested for the parent probability auditor are:

| Tag | Baseline scenario | Desired after-source scenario |
| --- | --- | --- |
| CUX | `E6_REGIONAL_FOCUS_A_CUX_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_CUX_ACTIVE_20261006` |
| IMO | `E6_REGIONAL_FOCUS_A_IMO_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_IMO_ACTIVE_20261006` |
| LEB | `E6_REGIONAL_FOCUS_A_LEB_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_LEB_ACTIVE_20261006` |
| PAL | `E6_REGIONAL_FOCUS_A_PAL_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_PAL_ACTIVE_20261006` |
| RIF | `E6_REGIONAL_FOCUS_A_RIF_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_RIF_ACTIVE_20261006` |
| DSX | `E6_REGIONAL_FOCUS_A_DSX_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_DSX_ACTIVE_20261006` |
| DUX | `E6_REGIONAL_FOCUS_A_DUX_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_DUX_ACTIVE_20261006` |
| UGA | `E6_REGIONAL_FOCUS_A_UGA_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_UGA_ACTIVE_20261006` |
| RWA | `E6_REGIONAL_FOCUS_A_RWA_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_RWA_ACTIVE_20261006` |
| BRD | `E6_REGIONAL_FOCUS_A_BRD_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_BRD_ACTIVE_20261006` |
| HAR | `E6_REGIONAL_FOCUS_A_HAR_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_HAR_ACTIVE_20261006` |
| SOM | `E6_REGIONAL_FOCUS_A_SOM_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_SOM_ACTIVE_20261006` |
| TIG | `E6_REGIONAL_FOCUS_A_TIG_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_TIG_ACTIVE_20261006` |
| BAR | `E6_REGIONAL_FOCUS_A_BAR_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_BAR_ACTIVE_20261006` |
| MAD | `E6_REGIONAL_FOCUS_A_MAD_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_MAD_ACTIVE_20261006` |
| FDX | `E6_REGIONAL_FOCUS_A_FDX_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_FDX_ACTIVE_20261006` |
| SIN | `E6_REGIONAL_FOCUS_A_SIN_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_SIN_ACTIVE_20261006` |
| BLC | `E6_REGIONAL_FOCUS_A_BLC_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_BLC_ACTIVE_20261006` |
| PSH | `E6_REGIONAL_FOCUS_A_PSH_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_PSH_ACTIVE_20261006` |
| KAS | `E6_REGIONAL_FOCUS_A_KAS_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_KAS_ACTIVE_20261006` |
| HYD | `E6_REGIONAL_FOCUS_A_HYD_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_HYD_ACTIVE_20261006` |
| MYS | `E6_REGIONAL_FOCUS_A_MYS_BASELINE_20261006` | `E6_REGIONAL_FOCUS_A_MYS_ACTIVE_20261006` |

The baseline candidates must include the active regional group and existing paid-decision pool for the exact tag. The after-source pool must also include imported shared focuses after the parent registers them. These scenario names describe requested fixtures and have not been executed by this subagent.

## Evidence and validation limits

The offline wiki sections used were `National focus modding - Hearts of Iron 4 Wiki.md:405-429` (focus availability, bypass, load-time branch visibility and cancellation), `:455-512` (search filters), `:604-626` (focus AI scoring), and `:818-838` (root-level `shared_focus` definitions and imports), at offline snapshot revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`. The last targeted MCP search/read routes returned `Transport closed`, so I read the relevant local offline wiki sections directly. The installed documentation search returned no national-focus syntax section, and the installed documentation directory contains no focus-tree documentation file. I inspected vanilla's root-level shared-focus precedent at `game:common/national_focus/baltic_shared.txt:44-93`, source revision `a5880d9ef39b5450d2ff520e428b2e5f2aec161a5c69f67867ee730e86d380e44`. The matched source is `BALTIC_rejoin_the_railways` and reuses vanilla infrastructure icon, offsets, cost, AI and a normal focus reward.

The initial CUX-only `script_validate` accepted focus syntax and 107 commands but warned that several new completion flags had no player-readable label while the localization file still had a literal escaped BOM prefix. I replaced that prefix with the actual EF BB BF BOM and added readable labels. The same first validation found an unclosed support-effect block, which I corrected and normalized. An intermediate whole-effect validation returned `SCRIPT_CHECK_PARTIAL` with 90 argument blocks unchecked and no remaining syntax diagnostic. Final `script_validate` attempts for the 110-focus source and support-effect file failed at the MCP transport with `Transport closed`, so this handoff does not claim final MCP script validation.

The live `hoi4.focus_inspect` and `hoi4.focus_render` routes returned `FOCUS_TREE_NOT_FOUND` for this file because it contains only root-level `shared_focus` blocks and no `focus_tree`. The parent owns adding the 110 IDs to the full-tree import. The existing direct-tree inspector omitted imported shared-focus nodes in its baseline result (184 direct focuses, layout hash `ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb`, source revision `7727618d1a0f0a049c584696d3b34c3ef7048a9d06fdf254766b4087fd8d3e42`). This is no post-change attachment or layout evidence. The installed focus tool list exposes no standalone `hoi4.focus_lint` route, and `hoi4.focus_rewrite` targets a complete focus tree or palette rather than a shared-focus-only source. No rewrite of the parent-owned main tree was attempted.

A final local source inventory found 110 unique focus IDs, exactly five for each assigned tag, 330 present title/description/effect-tooltip keys, no missing focus keys, no duplicate localization keys, and one actual BOM. These source checks do not replace the imported-node MCP layout review, parent decision interlocks, probability comparison, parent audits or user-run live-game validation.

## Parent integration still required

- Import these exact 110 shared-focus IDs into `independence_wave_focus_tree` in the parent-owned main focus file.
- For each crosswalk row, patch the matching existing paid decision to block while its focus is active or completed, and preserve existing focus-vs-project in-flight locks. Add the sibling cross-lock only for the Treaty of Seeb/coast-road and National Pact/Civic Charter pairs.
- Wire `independence_wave_regional_focus_a_clear_support_receipt` into the generic regional framework generation cleanup.
- After capturing the probability baseline, run the same-scenario comparison with the imported shared-focus candidates and review the equal-score existing alternatives.
- Run the post-registration focus inspect/render/rewrite workflow if the tool becomes capable of resolving imported shared-focus definitions, then record the current engine evidence and limits in the parent handoff.
- The user remains responsible for live-game validation. No game was launched for this source task.

No accepted Level 2 package project or assigned country group was omitted. The unresolved items above are integration and evidence gates, not implementation fallbacks.
