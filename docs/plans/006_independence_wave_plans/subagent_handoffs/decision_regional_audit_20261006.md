# Event 006 Regional Decision Audit and Factory Reservation

Date: 2026-10-06.

Disposition: Implemented for the bounded civilian-factory reservation repair; the AI probability pass and the missing Level 2 focus groups remain unresolved dependencies.

Acceptance basis: G4 delegated regional decision audit and small-patch authority in the parent task; the parent explicitly accepted the factory reservation repair and specified the native timed modifier on 2026-10-06.

The supplied inbox/006.txt was absent from the repository and no matching file was found in the checkout. The audit used the supplied phase history, the current D25-D34 decision record, the accepted event package specifications, and the newest region package documents.

## Changed files and behavior

The same narrow modifier was added to every D25-D33 regional decision whose existing administration-standard or strategic cost profile checks for two available civilian factories.

| Decision file | Administration-standard actions | Strategic-standard actions |
| --- | --- | --- |
| common/decisions/006_independence_wave_levant_arabia_decisions.txt | independence_wave_cux_seat_consultative_council, independence_wave_imo_convene_shaykhs_at_nizwa, independence_wave_leb_apportion_great_offices, independence_wave_pal_convene_legislative_council | independence_wave_imo_open_caravan_routes, independence_wave_leb_open_offices_to_every_citizen, independence_wave_pal_appoint_land_commission |
| common/decisions/006_independence_wave_north_africa_decisions.txt | independence_wave_rif_convene_national_assembly, independence_wave_rif_restore_ajdir_network | independence_wave_rif_fortify_mountain_redoubts |
| common/decisions/006_independence_wave_west_africa_decisions.txt | independence_wave_dsx_seat_oyo_mesi, independence_wave_dux_seat_shehus_council | independence_wave_dsx_convene_yoruba_towns |
| common/decisions/006_independence_wave_east_africa_decisions.txt | independence_wave_uga_convene_great_lukiiko, independence_wave_rwa_convene_mwami_council, independence_wave_brd_reconcile_bezi_and_batare, independence_wave_har_seat_merchants_council, independence_wave_som_convene_sultans_council, independence_wave_tig_convene_mekele_council | independence_wave_uga_settle_mailo_claims, independence_wave_rwa_abolish_ubuhake, independence_wave_brd_build_usumbura_port, independence_wave_som_divide_grazing_wells, independence_wave_tig_settle_aksum_church_lands |
| common/decisions/006_independence_wave_southern_africa_decisions.txt | independence_wave_bar_convene_national_kuta, independence_wave_mad_convene_malagasy_assembly | independence_wave_bar_restore_floodplain_canals, independence_wave_mad_recall_vvs_exiles |
| common/decisions/006_independence_wave_south_asia_decisions.txt | independence_wave_fdx_seat_punjab_assembly, independence_wave_sin_seat_sind_assembly, independence_wave_blc_convene_kalat_assemblies, independence_wave_psh_convene_grand_jirga, independence_wave_kas_expand_praja_sabha, independence_wave_hyd_reform_legislative_council, independence_wave_mys_seat_representative_assembly, independence_wave_mys_open_krishnaraja_sagara_canals, independence_wave_ras_proclaim_temple_entry, independence_wave_ras_seat_sree_mulam_assembly, independence_wave_fox_seat_assam_assembly, independence_wave_mpu_convene_durbar_with_hill_chiefs | independence_wave_fdx_settle_canal_water_shares, independence_wave_sin_allot_barrage_lands, independence_wave_psh_recognize_khudai_khidmatgar, independence_wave_kas_settle_weavers_wages, independence_wave_hyd_abolish_jagir_levies, independence_wave_mys_expand_bhadravati_works, independence_wave_ras_expand_cochin_harbour, independence_wave_fox_reform_tea_garden_contracts, independence_wave_mpu_fund_hill_schools |
| common/decisions/006_independence_wave_east_asia_oceania_decisions.txt | independence_wave_atj_convene_council_of_notables, independence_wave_fux_join_adat_and_ulama, independence_wave_bli_convene_paruman_agung, independence_wave_gcx_bind_federal_council, independence_wave_iax_seat_council_at_moulmein, independence_wave_ibx_convene_duwas_at_myitkyina, independence_wave_lao_unite_provinces_under_crown, independence_wave_gmx_convene_oasis_delegates, independence_wave_men_convene_autonomy_council, independence_wave_okn_seat_assembly_at_shuri, independence_wave_sam_convene_fono_of_faipule | independence_wave_atj_fund_madrasah_reform, independence_wave_fux_charter_thawalib_schools, independence_wave_bli_restore_subak_courts, independence_wave_gcx_regulate_bawdwin_mines, independence_wave_iax_open_mon_schools, independence_wave_ibx_open_jade_mines_road, independence_wave_lao_fund_buddhist_institute, independence_wave_men_settle_banner_pastures, independence_wave_okn_relieve_sugar_debts, independence_wave_sam_return_reparation_estates |
| common/decisions/006_independence_wave_americas_decisions.txt | independence_wave_que_seat_legislative_assembly, independence_wave_que_charter_caisses_populaires, independence_wave_gzx_restore_responsible_government, independence_wave_hcx_seat_legislature_at_austin, independence_wave_yuc_seat_yucatan_congress | independence_wave_que_nationalise_power_trusts, independence_wave_gzx_found_fisheries_board, independence_wave_hcx_empower_railroad_commission, independence_wave_yuc_turn_haciendas_into_ejidos |
| common/decisions/006_independence_wave_europe_caucasus_decisions.txt | independence_wave_atx_convene_assembly_of_venice, independence_wave_clx_convene_the_khase, independence_wave_cin_convene_mekhk_khel, independence_wave_dag_seat_federal_assembly | independence_wave_atx_charter_marghera_works, independence_wave_cin_take_over_grozny_oil, independence_wave_dag_fix_languages_of_state |

The exact shared modifier is civilian_factory_use = constant:independence_wave_decision_cost.civilian_factory_standard. It sits beside the unchanged days_remove field and reserves two factories for that decision's existing 120-day or 180-day timer.

Before the patch, the availability gate required two unassigned factories, but the payment helper only debited the stated political, manpower, stability, experience, equipment, and transport resources. No regional package effect in the nine files reserved factories, so several projects could start against the same available-factory count.

After the patch, the displayed two-factory commitment has a native timed reservation. A project started with exactly two free factories holds both until its existing timer ends; another factory-using project must wait. Four free factories support two such projects at once. The reservation profile and availability threshold both use the standard value of two.

No decision name, localisation key, cost amount, completion effect, cancellation trigger, duration, or AI weight was changed. There are 48 administration-standard reservations and 38 strategic-standard reservations, for 86 added modifiers.

## Findings sorted by severity

1. Resolved: 86 factory-using actions did not reserve the factory capacity their cost row and affordability helper required. The timer modifier closes the parallel-project overcommit path while preserving the existing project length and all other costs.

2. Parent-owned follow-up: the shared security-standard blocked-cost string omits manpower even though the payment effect and affordability trigger both charge and check 5,000 manpower. The normal security tooltip includes manpower, but localisation/english/006_independence_wave_decisions_l_english.yml:105 does not. This affects 17 regional actions using independence_wave_cost_security_standard. Add a clear manpower shortage indicator in the shared blocked presentation while keeping the inline cost row compact.

3. Unresolved focus integration: none of the 44 D25-D33 Level 2 rows has a package-specific five-node focus group or its mutually exclusive project-versus-focus routes in common/national_focus/006_independence_wave_focus.txt. The groups are recorded as future work in docs/events/006_independence_wave/regional_framework_packages.md, and the phase history says the D25-D33 focus groups are not built. D25-D33 Level 2 rows affected are CUX, IMO, LEB, PAL, RIF, DSX, DUX, UGA, RWA, BRD, HAR, SOM, TIG, BAR, MAD, FDX, SIN, BLC, PSH, KAS, HYD, MYS, RAS, FOX, MPU, ATJ, FUX, BLI, GCX, IAX, IBX, LAO, GMX, MEN, OKN, SAM, QUE, GZX, HCX, YUC, ATX, CLX, CIN, and DAG. No new focus route was designed or patched.

4. Queued signature modules verified against the current sources and spec themes:
   - Oyo (IW-097, DSX): D27 labels the Alaafin Siyanbola Ladigbolu I portrait, Oyo Mesi balance layer, and city-state relations as accepted and queued. Part 4 gives Oyo's focus themes. Current Event 006 code has the Level 2 Oyo Mesi Deadlock, its council and horse-guard ideas, and four paid projects, but no Ladigbolu character or portrait, dedicated Oyo balance system, city-state relations module, or Oyo focus nodes.
   - Aceh (IW-150, ATJ): D31 records the Level 3 signature module as queued. Part 4 and the research dossier specify sultanate legacy, Islamic law and regional institutions, ports, resistance, patron competition and federation ambitions; the dossier says PUSA content must be date-gated to 1939. Current Event 006 code has the Level 2 uleebalang-and-ulama problem, council, madrasah reform and pepper-port projects, but no Daud Beureueh character or signature focus/module and no PUSA date gate.
   - Mon State (IW-161, IAX): D31 records the signature module as queued. Part 4 and the research dossier specify monastic and cultural institutions, language, river-border geography, Burma/Thailand relations, autonomy and federation paths, while excluding post-1947 groups from the 1936 opening. Current Event 006 code has its Level 2 starting issue, provisional council, schools, port and three paid projects, but no separate Mon signature focus/module or cross-border relationship branch.

5. Low text-density note: all 44 country categories show three or four primary actions, with no category over the six-action budget. Category descriptions are one narrative paragraph and peak at 52 words; action descriptions and effect tooltips peak at 30 words. The prose check found no update-history wording. I made no style-only rewrite.

## Lifecycle, cognitive load, and mission quality

The nine files contain 44 country-specific categories and 136 ordinary delayed decisions: 40 categories have three actions and four have four. All 136 actions have visible, available, custom-cost trigger/text, completion, removal, cancellation, timer, and AI blocks.

The duration distribution is 94 standard timers of 120 days, 40 long timers of 180 days, and two short timers of 75 days. None is a timed mission, so mission owner/category/region/deadline/success/failure/duplicate fields are not applicable.

The cost is debited in complete_effect when the player selects the action. Its result applies in remove_effect when the timer ends. If the package becomes invalid, the package-only cancel_trigger ends the timer without running remove_effect; there is no cancel_effect or refund. The package docs and D34 record the generation cleanup that removes each layer's decisions, ideas, and flags. No live-game cancellation test was run.

Oman's Treaty of Seeb and coast-road closure alternatives are mutually exclusive while a project is active because each checks has_decision for the sibling; both resolve the same seeb_settled flag. Lebanon's National Pact and Civic Charter alternatives use the same sibling lock and shared pact-settled flag. The other actions are one-time completion-flag projects, not repeatable political-power exchanges.

Starting problems and outcomes are concrete and regional in the current package documents: the Oyo Mesi deadlock and Ibadan relations; Oman's unsettled coastal treaty; Lebanon's unwritten pact; the Rif levies; provincial councils, roads, ports, schools, mines, grazing and trade disputes across the other regions. The decision tooltips name the direction of change to Legitimacy, Capacity, Recognition, Security, Instability and package ideas. The decisions do not expose raw internal value dumps or long trigger lists.

No report/news event call is present in the regional decision definitions, so the report/news color and duplicate-popup checks do not apply to this surface. Package-incident event text and popup cadence remain outside this decision audit.

## Cost and requirement arithmetic

| Profile | Actions | Immediate spendable payment | Timed factory capacity | Spendable cost-type count |
| --- | ---: | --- | --- | ---: |
| Administration standard | 48 | 20 command power and 5,000 manpower | 2 factories reserved | 2 |
| Diplomatic standard | 33 | 20 command power and either 10 convoys or 10 trains | None | 2 |
| Security standard | 17 | 5,000 manpower, 20 army XP, 500 infantry equipment, and 100 support equipment | None | 4 |
| Strategic standard | 38 | 10 percentage points of stability, 20 command power, and either 10 convoys or 10 trains | 2 factories reserved | 3 |

The standard values come from common/script_constants/006_independence_wave_constants_registry.txt: manpower 5,000; command power 20; stability 0.10; train 10; convoy 10; army XP 20; infantry equipment 500; support equipment 100; civilian_factory_standard 2.

The dynamic diplomatic selector and payer agree: at least 10 convoys selects and spends 10 convoys; otherwise at least 10 trains selects and spends 10 trains. The affordability OR accepts equality at either threshold. Factory use is retained project capacity during the timer, not an upfront stockpile debit. Administration therefore has two spent resource types plus a factory commitment, and strategic has three spent resource types plus that commitment. Security standard is the maximum at four spendable types.

The iconized cost profiles use the corresponding icons for command power, manpower, civilian factory use, stability, train, convoy, army experience, infantry equipment, and support equipment. The timed reservation now makes the existing civilian-factory commitment truthful. No regional action exceeds four spendable cost types.

The source cost key for security standard lists manpower, army XP, infantry equipment and support equipment in its tooltip, while its blocked variant omits manpower. The shared row needs the parent-owned correction listed above.

## AI, cleanup, and exploit limits

All 136 actions have ai_will_do blocks, but this audit did not evaluate their weights or modify them. The parent should route these in-scope decision weights through chaosx_ai_probability_auditor after a slot is available.

The decision inspector was called for independence_wave_imo_renew_treaty_of_seeb with actor IMO and scenario imo_1936_unreleased_baseline dated 1936.1.1. It returned DECISION_ANALYZED_PARTIAL, complete=false, 100 unresolved definitions and an inline source inventory limited to 64 of 6,855 paths. The candidate was ineligible with raw value zero and score_only support because the scenario did not declare independence_wave_former_host, capital_scope, or command_power. The report artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82244b626c931fb2b3efa155ca1b12457099294efbf9b381a5bae71824286582/8c4716c3595bc96a49f5d426dd56514b3feae70b2d3b5e5de63b40e8325a7edd/decision-9076427f3263cba018adcabc.json. This is source/scenario evidence only, not campaign-state proof.

The factory modifier reduces overcommit risk by reserving capacity during the native decision timer. One-time flags and sibling-decision guards prevent repeated purchases or paying both accepted branch alternatives. No free-unit, war-goal, core, or equipment-farming loop appears in these decision definitions.

## Source and MCP evidence

- Decision context: workspace mod_chaos_redux_ea3b2d67c2c0; offline wiki Decision modding revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162; installed decision documentation revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.
- Timer behavior: offline Decision modding, Timer upon selection, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, lines 337-356; complete_effect starts the timer, remove_effect runs when it ends, and cancel_trigger ends it without remove_effect.
- Factory modifier: offline Modifiers wiki, civilian_factory_use, revision fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f, line 686; installed modifier documentation, revision 00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e, lines 2202-2206. The installed entry specifies an integer country/war_production modifier; the offline wiki describes its project use.
- Capacity gate: installed dynamic_variables_documentation.md revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda, lines 608-611; installed triggers_documentation.md revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, lines 6757-6765. Both define num_of_civilian_factories_available_for_projects as the amount available for a new project.
- Vanilla precedent: game:common/decisions/AST.txt, AST_union_strike, lines 2-42, source_lookup revision 7c75f9a603a32adcfb04788a11d4247185d0a30c0a46738e5c931c4968d45708. It pairs days_remove with a timed modifier containing civilian_factory_use.
- Current regional source: source_lookup revision 6345e994f9c68910e497c5a07005df64d566d1640b048b8bdaea8fadfb220abf. It confirmed the new modifier in independence_wave_imo_open_caravan_routes and independence_wave_dsx_seat_oyo_mesi.
- Payment helpers: source_lookup revision c493af03776dd448f89ab1b0a866e1539eb67b2123241797f3c4b624c82fb45f for standard administration, diplomatic, security and strategic payers; strategic affordability trigger revision 3c233298e200459c48f7148fefefe002de0a146a563ad8af87cb6f29c7e41adb.
- Script validation: hoi4.script_validate checked all nine changed regional decision files against installed game documentation; all nine returned SCRIPT_CHECKED with syntax, native command-kind, and declared-scope checks passed.
- Focus cross-check: hoi4.focus_inspect for common/national_focus/006_independence_wave_focus.txt returned FOCUS_INSPECTED with no blocking diagnostics; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbdb6282476e1e5af2c588224429530673cbd2e7d6d779161056832259e2caa4/bea964b232b7e0991cb976610b719c78183773bc14efebd64500b4a3cdbaa3a5/focus-inspect.7d97346d2bebcbe2.json.
- Focus render: hoi4.focus_render for independence_wave_focus_tree returned FOCUS_RENDERED with no blocking diagnostics; SVG artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65038c84aafa45b0dedf8601921c47fde21d986764e0ee05922593b0020b7bce/b9bc94428ba845fa09e1c2c7d0bfe87b8a41d6a0318949e906ae59d742a0d12a/independence_wave_focus_tree.focus.svg.

## Skipped validation and remaining work

No HOI4 game launch, desktop session, or live-save test was performed; the repository assigns live gameplay checks to the user. The expected in-game scenario is one two-factory project started, two factories reserved during its existing timer, and a second project becoming available after those factories are released.

The AI probability pass remains pending parent routing because all agent slots were occupied. No AI weights changed in this patch.

The decision inspector did not have a released-package scenario with a former-host scope, capital state, resource values, and setup flags, so it did not validate live availability or the timer reservation in an active campaign.

The supplied inbox/006.txt could not be read because it is absent from the repository. No spreadsheet, CSV, localization, event, focus, effect, trigger, GUI, asset, or formable files were changed.

No separate plan handoff was written. Parent-owned follow-ups are the shared security blocked-cost manpower text and the later focus-group and Oyo/Aceh/Mon signature-module work.
