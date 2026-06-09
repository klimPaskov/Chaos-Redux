# Event005 Soviet Collapse Focus Tree Full Current Audit

Timestamp: 2026-06-04 10:37:22 UTC

Subagent role: `chaosx_focus_tree_auditor`

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Directly adjacent focus helpers, localisation, icons, and decision tooltip references only for audit evidence.

Constraints honored:
- No flag work. No `gfx/flags`, `interface/flags`, `.tga`, flag art, or flag sprite files were touched.
- No release/scenario systems, decisions, country setup, or sprites were edited.
- No gameplay focus patch was made in this pass. This handoff is the only file added.
- Worktree was already dirty with parent changes before this audit, so no commit was made.

Skills and references used:
- `hoi4-focus-trees`
- `chaos-redux-subagents`
- Offline wiki pages consulted before auditing the focus files: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation consulted from `~/projects/Hearts of Iron IV/documentation/`: effects, triggers, modifiers, script concepts, localisation objects, localisation formatters.
- Vanilla focus precedents inspected from `~/projects/Hearts of Iron IV/common/national_focus/`, especially `soviet.txt` and other major-tree focus files for focus shape, filters, prerequisites, and AI precedent.

## Files Changed

| File | Change |
| --- | --- |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_103722_event005_focus_tree_full_current_audit.md` | New audit handoff only. |

Changed focus ids: none.

Changed helper ids: none.

Changed localisation keys: none.

Changed gameplay behavior: none.

## Current Focus Surface

Current parser counts:

| File | Trees | Focuses | Notes |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 9 | 501 | Ukraine, generic breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan. |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | FTH, PRA, five compact crisis trees, and nineteen larger custom splinter trees. |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | CFR, OGB, MFR. |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | KZR, SOG, KHW, ALN. |
| Total | 41 | 1698 | Current workspace state. |

Smallest trees:
- 16 focuses: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`.
- 18 focuses: `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`.
- 22 focuses: `PRA_soviet_collapse_focus_tree`.
- 23 focuses: `OGB_soviet_collapse_focus_tree`.
- 36 focuses: `soviet_collapse_breakaway_focus_tree`.

## Global Findings

Structural integrity is mostly good:
- No duplicate focus ids.
- No duplicate same-tree coordinates.
- No missing prerequisite or mutual-exclusion focus targets.
- No missing focus title or description localisation.
- No missing focus icon sprite names against repo and vanilla `.gfx` text lookup.
- No missing `unlock_decision_tooltip` targets.
- No `<=` or `>=` operators in the four Event005 focus files.

The remaining problems are design-depth and presentation problems:
- Reward rhythm is still dominated by repeated helper packages. Top repeated helpers are `soviet_collapse_apply_focus_depot_and_supply_control` at 141 calls, `soviet_collapse_apply_focus_military_consolidation` at 132, `soviet_collapse_apply_focus_legal_recognition` at 108, `soviet_collapse_apply_focus_republican_compact_plan` at 80, `soviet_collapse_apply_focus_foreign_channel` at 65, `soviet_collapse_apply_focus_high_chaos_identity` at 60, `soviet_collapse_apply_focus_security_supply_plan` at 58, and `soviet_collapse_apply_focus_league_preparation` at 52.
- Many branches are named as political, industrial, diplomatic, war, or high-chaos choices, but their payoffs often converge into the same variables, helper packets, and generic decision unlock style.
- Focus filters are present everywhere, but many do not match the full reward payload. Parser heuristics found 647 likely filter mismatches, mostly because mixed political/industry/military/diplomacy rewards are tagged with only two of those categories.
- The biggest visual issue is no longer duplicate coordinates. It is crossing prerequisite lines and dense convergence around route forks and late endpoints.
- Direct focus-level idea spam is largely gone, but a few focus-called helpers still remove or stage ideas indirectly. These are listed below.

## Idea-Spam and Helper Audit

Direct focus rewards:
- `add_ideas`: no direct focus reward calls found.
- `swap_ideas`: no direct focus reward calls found.
- `add_timed_idea`: no direct focus reward calls found.
- `remove_ideas`: no direct focus reward calls found.

Indirect focus-called helpers that touch ideas:

| Helper | Focus call sites | Idea behavior | Audit note |
| --- | ---: | --- | --- |
| `soviet_collapse_add_republic_focus_recovery_progress` | 11 | Removes `soviet_collapse_republican_startup_disorder` and `soviet_collapse_republican_startup_disorder_mitigated` when recovery reaches threshold. | This is cleanup/progression, not spam, but several unrelated branches call it as a generic reward kicker. |
| `soviet_collapse_clear_focus_starting_tension_ideas` | 7 | Removes compact-tree starting tension ideas such as `pra_dispatcher_court_tensions`, `tsc_field_station_rivalries`, `rmc_credal_cell_rivalries`, `dsc_grave_regiment_rivalries`, `nrf_drowned_crew_disputes`, `icd_grave_commissar_rivalries`, `ogb_disputed_restored_name`. | This is cleanup, but it marks the compact trees' early political payoff as "remove the starting idea" rather than a deep route system. |
| `soviet_collapse_update_pra_authority_idea` | 4 | Adds one of `pra_moving_state_authority`, `pra_corridor_toll_authority`, `pra_railway_guard`, `pra_timetable_sovereignty_board`. | PRA still relies on staged authority spirits as the main identity progression. |
| `soviet_collapse_apply_cfr_raise_factory_city_belt` | 1 | Adds `cfr_construction_mandates`. | CFR has one focus-called helper that adds a mandate spirit directly. |

Exact focus sites for these helpers:
- `soviet_collapse_add_republic_focus_recovery_progress`: `internal_soviet_collapse_volga_crossing_militias`, `internal_soviet_collapse_bashkir_cavalry_oath`, `FTH_village_delegate_roads`, `DHC_manych_rear_area`, `DHC_winter_road_columns`, `KHC_laba_rear_area`, `SZA_tomsk_omsk_switchyards`, `NLC_ration_and_signal_escorts`, `NLC_winter_road_columns`, `NLC_apatity_rear_area`, `NLC_extreme_gate`.
- `soviet_collapse_clear_focus_starting_tension_ideas`: `PRA_the_board_overrules_ministers`, `TSC_the_committee_of_instruments`, `RMC_communes_of_witnesses`, `DSC_witness_officers`, `NRF_living_harbor_committees`, `ICD_commissars_of_last_addresses`, `OGB_the_council_takes_the_seal`.
- `soviet_collapse_update_pra_authority_idea`: `PRA_the_timetable_declares_authority`, `PRA_armored_train_directorate`, `PRA_passport_of_the_moving_state`, `PRA_league_transit_bargain`.
- `soviet_collapse_apply_cfr_raise_factory_city_belt`: `CFR_pour_the_final_foundation`.

## Republic Focus Trees

### Ukraine

Tree: `soviet_collapse_ukraine_focus_tree`, 83 focuses.

Current state:
- This is one of the deepest republic trees and has real political, industrial, military, foreign, Black Sea, League, high-chaos, and late-game lanes.
- It is still visually messy. The opening and political fork area has many diagonal dependencies and several crossing lines around statehood, grain, industry, foreign recognition, and military authority.
- It is still too helper-heavy for a flagship republic. Many route rewards feel like variable bundles rather than country-specific mechanics.

Exact ids needing attention:
- Branch-depth and lore payoff: `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_protectorate_debate`, `ukr_soviet_collapse_breadbasket_empire`, `ukr_soviet_collapse_bread_state_whispers`.
- Filter mismatches: `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_guard_the_telegraph_house`, `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_first_republican_line`, `ukr_soviet_collapse_army_supremacy`, `ukr_soviet_collapse_romanian_port_route`, `ukr_soviet_collapse_breadbasket_empire`.
- Layout/pathline risk: `ukr_soviet_collapse_guard_the_telegraph_house -> ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_foreign_courts_notice_kyiv -> ukr_soviet_collapse_army_supremacy`, and the route selector cluster around `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`.

Needed fix:
- Treat Ukraine as a flagship rewrite target: spread the early fork, reduce crossing lines, make the statehood routes alter distinct decision families and postwar claims/settlements, and make the Black Sea/grain/high-chaos routes visibly affect map, diplomacy, war plans, or faction behavior.

### Generic Breakaway

Tree: `soviet_collapse_breakaway_focus_tree`, 36 focuses.

Current state:
- This is no longer a tiny fallback tree, but it remains generic for countries that are expected to be playable.
- The political fork exists, but the three main routes mostly become standard sovereignty, military, and foreign bundles.
- Expansion and postwar consequences are still thin.

Exact ids needing attention:
- Generic anchors: `soviet_collapse_the_republic_defines_itself`, `soviet_collapse_route_consolidation_congress`, `soviet_collapse_rail_hub_or_mountain_pass`, `soviet_collapse_armed_neutrality`, `soviet_collapse_the_republic_endures`, `soviet_collapse_a_republic_worth_naming`.
- Route fork: `soviet_collapse_socialist_sovereignty_committee`, `soviet_collapse_military_defense_council`, `soviet_collapse_foreign_liaison_government`.
- Filter/reward mismatches: `soviet_collapse_assemble_emergency_government`, `soviet_collapse_guard_the_radio_stations`, `soviet_collapse_secure_ministry_ledgers`, `soviet_collapse_home_industry_contracts`, `soviet_collapse_border_militia_standard`, `soviet_collapse_sponsor_aid_audit`.

Needed fix:
- Add regional identity overlays or variant mechanics, or clearly document this tree as temporary/minor-only. For important releases, it should not be the final playable identity.

### Internal Republics

Tree: `soviet_collapse_internal_republic_focus_tree`, 62 focuses.

Current state:
- Good breadth across northern, Volga/Ural, Siberian, Yakut, Buryat, Tuvan, and old-name surfaces.
- Branches are more route clusters than true country-specific trees. Many are two to four focuses with similar reward language and shared helpers.
- Expansion and external settlement hooks exist in places but are not robust enough for large released actors.

Exact ids needing attention:
- Branch-depth: `internal_soviet_collapse_northern_republic_accord`, `internal_soviet_collapse_volga_oil_and_workshops`, `internal_soviet_collapse_ufa_emergency_authority`, `internal_soviet_collapse_siberian_rail_authorities`, `internal_soviet_collapse_yakut_lena_resource_board`, `internal_soviet_collapse_tuvan_steppe_guard`, `internal_soviet_collapse_old_names_under_guard`.
- Expansion/postwar gaps: `internal_soviet_collapse_forest_border_guard_posts`, `internal_soviet_collapse_karelian_finnish_border_mission`, `internal_soviet_collapse_tannu_border_roads`.
- Filter mismatches: `internal_soviet_collapse_map_union_property`, `internal_soviet_collapse_northern_timber_rail_fund`, `internal_soviet_collapse_forest_border_guard_posts`, `internal_soviet_collapse_komi_river_and_mine_committees`, `internal_soviet_collapse_volga_crossing_militias`, `internal_soviet_collapse_tannu_border_roads`.

Needed fix:
- Convert the regional clusters into either bespoke trees for important tags or add visible regional mechanics: northern border mission, Volga oil authority, Siberian rail authority, Yakut resource board, and Tuvan frontier settlement.

### Baltic

Tree: `soviet_collapse_baltic_focus_tree`, 42 focuses.

Current state:
- Has legal continuity, foreign protection, military border government, Baltic League, port economy, and national sublanes.
- The regional route concept is clear, but the branch payoffs are compact and similar across the three Baltic identities.
- Pathline risk remains in the main selector area.

Exact ids needing attention:
- Branch-depth: `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_foreign_protection_council`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_the_port_economy`.
- National adaptation: `baltic_soviet_collapse_tallinn_harbor_customs`, `baltic_soviet_collapse_estonian_forest_coast_guard`, `baltic_soviet_collapse_riga_corridor_switchyards`, `baltic_soviet_collapse_vilnius_border_statutes`.
- Filter mismatches: `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_british_naval_observers`, `baltic_soviet_collapse_sponsor_fleet_rights`, `baltic_soviet_collapse_coastal_defense_batteries`, `baltic_soviet_collapse_forest_and_marsh_lines`.

Needed fix:
- Separate Estonia/Latvia/Lithuania payoffs more clearly. Add postwar border settlement and league-member behavior, not only port/forest/military bundles.

### Caucasus

Tree: `soviet_collapse_caucasus_focus_tree`, 40 focuses.

Current state:
- Strong geographic identity around oil, Black Sea, Caspian, mountain defense, and border war cabinet.
- Underdeveloped diplomatic consequences and postwar settlement for a region where outside sponsors and neighboring wars should matter.
- Several military/industry/diplomacy rewards are cross-tag helper bundles.

Exact ids needing attention:
- Branch-depth: `caucasus_soviet_collapse_oil_emergency_directorate`, `caucasus_soviet_collapse_black_sea_or_caspian_routes`, `caucasus_soviet_collapse_tbilisi_black_sea_authority`, `caucasus_soviet_collapse_caspian_oil_diplomacy`, `caucasus_soviet_collapse_the_border_war_cabinet`.
- Expansion/postwar: `caucasus_soviet_collapse_ararat_border_fortresses`, `caucasus_soviet_collapse_the_border_war_cabinet`, `caucasus_soviet_collapse_the_caucasus_stands`.
- Filter mismatches: `caucasus_soviet_collapse_protect_the_oil_and_ports`, `caucasus_soviet_collapse_black_sea_or_caspian_routes`, `caucasus_soviet_collapse_black_sea_observer_desks`, `caucasus_soviet_collapse_caspian_oil_diplomacy`, `caucasus_soviet_collapse_ararat_border_fortresses`.

Needed fix:
- Add sponsor competition, oil-for-arms, mountain settlement, and postwar border mechanics. War goals alone are not enough.

### Central Asia

Tree: `soviet_collapse_central_asia_focus_tree`, 45 focuses.

Current state:
- Has emergency majlis, irrigation/bread, local republic, border patronage, Turkestan city congress, pass defense, and regional sublanes.
- The route selector geometry remains wide and diagonal.
- Many branch rewards are generic local-authority, recognition, depot, and military helper bundles.

Exact ids needing attention:
- Branch-depth: `central_asia_soviet_collapse_southern_emergency_majlis`, `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_military_border_authority`, `central_asia_soviet_collapse_foreign_border_patronage`, `central_asia_soviet_collapse_turkestan_city_congress`.
- Geographic mechanics: `central_asia_soviet_collapse_irrigation_and_bread_councils`, `central_asia_soviet_collapse_cotton_rail_republic`, `central_asia_soviet_collapse_southern_pass_reserve`, `central_asia_soviet_collapse_desert_scout_columns`, `central_asia_soviet_collapse_dushanbe_mountain_sovereignty`.
- Filter mismatches: `central_asia_soviet_collapse_southern_emergency_majlis`, `central_asia_soviet_collapse_irrigation_and_bread_councils`, `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_tashkent_emergency_ministries`, `central_asia_soviet_collapse_turkestan_city_congress`.

Needed fix:
- Add irrigation, cotton, pass control, and patron pressure as visible mechanics or staged decision families. Spread the main selector and reduce diagonal crossings.

### Moldova

Tree: `soviet_collapse_moldova_focus_tree`, 48 focuses.

Current state:
- Has river guard, Romanian aid, union question, neutrality, Prut relief, rail, customs, and soil recovery content.
- The union/anti-union/neutral bridge routes exist but do not yet have enough postwar or diplomatic consequence.
- Layout is better than Ukraine/Belarus but still has selector readability risks.

Exact ids needing attention:
- Branch-depth: `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_conditional_union`, `moldova_soviet_collapse_reject_the_union_question`, `moldova_soviet_collapse_neutral_bridge_statute`.
- Mechanics hooks: `moldova_soviet_collapse_romanian_aid_without_annexation`, `moldova_soviet_collapse_southern_rail_timetables`, `moldova_soviet_collapse_border_customs_shares`, `moldova_soviet_collapse_prut_relief_depots`.
- Filter mismatches: `moldova_soviet_collapse_river_guard_brigades`, `moldova_soviet_collapse_romanian_aid_without_annexation`, `moldova_soviet_collapse_neutral_bridge_statute`, `moldova_soviet_collapse_border_customs_shares`, `moldova_soviet_collapse_river_command_reserve`.

Needed fix:
- Make the union question branch alter Romanian relations, border settlement, aid dependency, and postwar integration rather than mostly using shared diplomatic/industry/military packages.

### Belarus

Tree: `soviet_collapse_belarus_focus_tree`, 53 focuses.

Current state:
- Belarus is improved but still visibly compressed in concept and layout. The rail identity is good; the focus flow still risks feeling like a dense rail/forest/corridor checklist.
- The main rail/forest/League/corridor branches need more purpose and stronger endpoint consequences.
- Focus spacing is better than older versions but several forks still converge through narrow line clusters.

Exact ids needing attention:
- Branch-depth: `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_every_track_through_minsk`, `blr_soviet_collapse_the_league_depot_at_minsk`, `blr_soviet_collapse_red_without_the_center`, `blr_soviet_collapse_timetable_state`, `blr_soviet_collapse_last_train_east`.
- Layout/pathline risk: `blr_soviet_collapse_the_rail_map_on_the_wall`, `blr_soviet_collapse_evacuation_choice`, `blr_soviet_collapse_western_corridor_switchmen`, `blr_soviet_collapse_league_supply_timetables`, `blr_soviet_collapse_foreign_aid_through_brest`.
- Filter mismatches: `blr_soviet_collapse_the_rail_map_on_the_wall`, `blr_soviet_collapse_evacuation_choice`, `blr_soviet_collapse_red_without_the_center`, `blr_soviet_collapse_nationalize_the_rail_schedules`, `blr_soviet_collapse_timetable_state`, `blr_soviet_collapse_last_train_east`.

Needed fix:
- Give Belarus a real rail-state mechanic or staged rail decision family: evacuation schedules, supply leverage, corridor tolls, League depot obligations, and eastern/western strategic choices. Spread forks more horizontally and avoid late line convergence.

### Kazakhstan

Tree: `soviet_collapse_kazakhstan_focus_tree`, 92 focuses.

Current state:
- Largest republic tree and has strong surface breadth: steppe federation, resource sovereignty, Caspian security, old-state memory, Basmachi routes, border/rail/resource/military families.
- It is powerful on paper but still needs sharper post-expansion integration and faction/diplomacy consequences.
- Route density creates some pathline clutter in late regional branches.

Exact ids needing attention:
- Branch-depth: `kaz_soviet_collapse_steppe_federation_charter`, `kaz_soviet_collapse_lone_steppe_state`, `kaz_soviet_collapse_resource_sovereignty`, `kaz_soviet_collapse_caspian_security_detachments`, `kaz_soviet_collapse_the_steppe_remembers_old_states`, `kaz_soviet_collapse_basmachi_roads_reopen`.
- Filter mismatches: parser found the highest count in this tree. Prioritize `kaz_soviet_collapse_guard_the_resource_towns`, `kaz_soviet_collapse_a_state_across_distances`, `kaz_soviet_collapse_resource_sovereignty`, `kaz_soviet_collapse_caspian_security_detachments`, `kaz_soviet_collapse_steppe_federation_charter`.
- Layout: route density around old-state and Basmachi routes needs in-game visual review.

Needed fix:
- Add postwar settlement, federation member rules, resource leverage, Caspian diplomacy, and old-state consequences as visible mechanics. Kazakhstan should be one of the overpowered chaos-country exemplars, not just a large generic reward tree.

## Factory Successors

### CFR

Tree: `CFR_soviet_collapse_focus_tree`, 47 focuses.

Current state:
- CFR has a real industrial mandate identity, reconstruction decisions, and late aggression.
- The biggest remaining issue is visual geometry. It has several crossing clusters in the mid and late tree.
- Reward repetition still leans on construction/public works/housing helpers.

Exact ids needing attention:
- Layout/pathline blockers: `CFR_the_board_becomes_the_cabinet -> CFR_cities_first` crossing `CFR_rails_first -> CFR_apartment_blocks_for_loyalty`; `CFR_the_board_becomes_the_cabinet -> CFR_contracts_first` crossing `CFR_contracts_with_the_league -> CFR_client_city_charters`; `CFR_the_first_new_district -> CFR_buy_peace_with_concrete` crossing `CFR_the_state_that_builds -> CFR_the_builder_state_marches_east`.
- Reward/helper repetition: `CFR_the_trust_office_takes_the_seal`, `CFR_emergency_cement_accounts`, `CFR_the_unfinished_city_speaks`, `CFR_rails_first`, `CFR_factories_first`, `CFR_pour_the_final_foundation`.
- Idea helper: `CFR_pour_the_final_foundation` calls `soviet_collapse_apply_cfr_raise_factory_city_belt`, which adds `cfr_construction_mandates`.

Needed fix:
- Redraw the mid-tree factory/city/contract forks. Keep CFR powerful, but make cities-first, rails-first, factories-first, and contracts-first visibly different.

### OGB

Tree: `OGB_soviet_collapse_focus_tree`, 23 focuses.

Current state:
- OGB remains the weakest factory successor by size and branch depth.
- Scholar versus cleric split is present but too shallow.
- Volga/Idel-Ural relations need a second-stage settlement, war, or restoration mechanic.
- Starting idea cleanup is indirect through `soviet_collapse_clear_focus_starting_tension_ideas`.

Exact ids needing attention:
- Weak branch anchors: `OGB_scholars_guard_the_charter`, `OGB_clerics_guard_the_charter`, `OGB_treat_with_idel_ural`, `OGB_the_volga_cannot_have_two_seals`, `OGB_claim_the_old_trade_cities`, `OGB_future_bulgaria_file`, `OGB_volga_restoration_state`, `OGB_the_old_name_survives_modern_war`.
- Idea cleanup site: `OGB_the_council_takes_the_seal` removes `ogb_disputed_restored_name` through `soviet_collapse_clear_focus_starting_tension_ideas`.
- Missing mechanics: scholar/cleric authority, Volga legitimacy, Idel-Ural settlement, postwar trade-city integration, old-name restoration diplomacy.

Needed fix:
- OGB needs a broad rewrite, not a small patch: 35 to 45 focus target, expanded Volga legitimacy mechanic, scholar/cleric fork consequences, Idel-Ural diplomacy/war settlement, and a true restoration endpoint.

### MFR

Tree: `MFR_soviet_collapse_focus_tree`, 58 focuses.

Current state:
- Strongest factory successor by depth. Has arms quotas, rifle/artillery/steel paths, inspection/black-market routes, guard columns, and late aggression.
- Main problem is pathline crossing in the production/factory-war section and repeated factory guard/arsenal helpers.

Exact ids needing attention:
- Layout/pathline blockers: `MFR_factory_war_cabinet -> MFR_artillery_from_broken_foundries` crossing `MFR_rifles_before_speeches -> MFR_standardize_the_rifle_line`; `MFR_standardize_the_rifle_line -> MFR_plate_steel_rationing` crossing `MFR_unsafe_production_surge -> MFR_red_warning_lamps`; `MFR_no_shell_without_obedience -> MFR_armored_train_workshops` crossing `MFR_factory_guard_columns -> MFR_gates_sirens_rifles`.
- Reward cleanup: `MFR_factory_war_cabinet`, `MFR_rifles_before_speeches`, `MFR_standardize_the_rifle_line`, `MFR_quota_above_life`, `MFR_output_is_victory`.

Needed fix:
- Move the rifle/artillery/steel fork into clear vertical lanes. Add more production-line or arms-market decisions so factory power is not only offsite factories, stockpiles, and helpers.

## Ancient Restorations

Trees: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`, 16 focuses each.

Current state:
- These trees are compact and readable, and they now include stronger high-chaos aggression hooks.
- They remain too short for long-lived playable countries unless the design intent is "compact high-chaos actors."
- Branch payoff is still symbolic restoration, old borders, workshops, league bargain, and endgame. That is not enough for a major chaos-country power fantasy.

Exact ids needing attention:
- Shallow endpoint ids: `KZR_restoration_survives_modern_war`, `SOG_restoration_survives_modern_war`, `KHW_restoration_survives_modern_war`, `ALN_restoration_survives_modern_war`.
- Strong but compact aggression ids: `KZR_returned_names_endgame`, `KZR_road_beyond_the_caspian`, `SOG_returned_names_endgame`, `SOG_cities_beyond_the_desert`, `KHW_returned_names_endgame`, `KHW_delta_without_a_center`, `ALN_returned_names_endgame`, `ALN_every_pass_a_border`.
- Layout crossings: `KZR_caspian_road_markets -> KZR_league_transit_bargain` crosses `KZR_customs_workshop_compact -> KZR_old_border_files`; equivalent compact diamond crossings exist for SOG/KHW/ALN.

Needed fix:
- Either document them as intentionally compact high-chaos countries, or expand each to 25 to 35 focuses with distinct restoration law, levy, ancient border, modern industry, sponsor reaction, and endgame conquest/federation mechanics.

## Custom Splinters

### Compact Crisis Trees

Trees: `TSC`, `RMC`, `DSC`, `NRF`, `ICD` at 18 focuses each; `PRA` at 22 focuses.

Current state:
- These are still the clearest branch-depth blockers.
- They have a strong concept, but the playable tree is compact and often resolves with one identity pivot, one military path, one logistics path, and one endpoint.
- Direct starting-tension idea cleanup occurs through `soviet_collapse_clear_focus_starting_tension_ideas`.

Exact ids needing attention:
- PRA: `PRA_rails_over_capitals`, `PRA_the_pale_line_endures`, `PRA_the_board_overrules_ministers`, `PRA_the_timetable_declares_authority`, `PRA_armored_train_directorate`, `PRA_passport_of_the_moving_state`, `PRA_league_transit_bargain`.
- TSC: `TSC_starfall_mandate`, `TSC_the_committee_of_instruments`, `TSC_observatory_guard`, `TSC_perimeter_regiments`.
- RMC: `RMC_resurrection_without_state`, `RMC_communes_of_witnesses`, `RMC_reliquary_guard`, `RMC_dead_volunteer_columns`.
- DSC: `DSC_grave_ordnance_claims`, `DSC_witness_officers`, `DSC_dead_regiment_columns`, `DSC_maps_of_lost_armies`.
- NRF: `NRF_northern_revenant_fleet`, `NRF_living_harbor_committees`, `NRF_icebound_marine_guard`, `NRF_maps_of_sunken_routes`.
- ICD: `ICD_commissariat_without_end`, `ICD_commissars_of_last_addresses`, `ICD_funeral_guard`, `ICD_archives_of_every_front`.

Needed fix:
- Expand each compact crisis tree into a 30 to 40 focus package with a real internal mechanic, overpowered high-chaos payoff, and at least one expansion/postwar route. PRA especially needs railway-state decisions beyond staged authority spirits.

### Larger 47-Focus Custom Splinters

Trees: `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`.

Current state:
- These are much better than compact trees and usually include political, supply, industry, diplomacy, war, settlement, high-chaos, and endgame families.
- The recurring skeleton is still obvious: `*_industry_plan`, `*_hidden_doctrine`, `*_extreme_gate`, `*_extreme_path`, `*_war_plan`, `*_enemy_front`, `*_diplomatic_plan`, `*_endgame`.
- Several trees have severe pathline crossings where mid-tree logistics, settlement, war, and endgame branches converge.
- Repeated helper identities from `soviet_collapse_apply_custom_splinter_*_identity` create template feel even when names are local.

Exact high-risk layout clusters:
- `UDC`: crossings around `UDC_supply`, `UDC_loyal_depot_ledgers`, `UDC_staff_car_workshops`, `UDC_civil_rule`, `UDC_propaganda`, `UDC_radical_turn`, `UDC_war_plan`, `UDC_industry_plan`.
- `SDZ`: same pattern around `SDZ_supply`, `SDZ_sealed_depot_ledgers`, `SDZ_document_cart_workshops`, `SDZ_civil_rule`, `SDZ_propaganda`, `SDZ_radical_turn`, `SDZ_war_plan`, `SDZ_industry_plan`.
- `DHC`: `DHC_enemy_front`, `DHC_southern_crossing_batteries`, `DHC_don_river_customs`, `DHC_river_port_tolls`, `DHC_league_passage_bargain`, `DHC_winter_road_columns`, `DHC_industry_plan`.
- `KHC`: `KHC_enemy_front`, `KHC_mountain_crossing_batteries`, `KHC_kuban_river_customs`, `KHC_river_port_tolls`, `KHC_league_corridor_bargain`, `KHC_winter_corridor_columns`, `KHC_industry_plan`.
- `FEV`: `FEV_industry_plan`, `FEV_hidden_doctrine`, `FEV_extreme_gate`, `FEV_vladivostok_harbor_board`, `FEV_settlement`, `FEV_endgame`.
- `SZA`: `SZA_industry_plan`, `SZA_hidden_doctrine`, `SZA_extreme_gate`, `SZA_siberian_staff_map`, `SZA_baikal_rear_area`, `SZA_authority_from_the_railhead`, `SZA_endgame`.
- `UWD`: `UWD_supply`, `UWD_blast_furnace_guard_posts`, `UWD_chelyabinsk_airwatch_yards`, `UWD_shift_council_mediation`, `UWD_workers_canteen_compact`, `UWD_war_plan`, `UWD_industry_plan`.
- `BAC`: `BAC_settlement`, `BAC_industry_plan`, `BAC_war_plan`, `BAC_militia_training_yards`, `BAC_radical_turn`, `BAC_hardline_against_border_troops`, `BAC_extreme_path`, `BAC_endgame`.
- `ARD`: `ARD_white_sea_customs`, `ARD_murmansk_dockyard_contracts`, `ARD_white_sea_port_tolls`, `ARD_arctic_port_endurance`, `ARD_winter_convoy_columns`, `ARD_directorate_staff_map`, `ARD_endgame`.
- `NLC`: `NLC_station_mediation`, `NLC_winter_guarantees`, `NLC_heated_workshop_contracts`, `NLC_settlement`, `NLC_polar_neutrality_statute`, `NLC_war_plan`, `NLC_industry_plan`, `NLC_endgame`.

Needed fix:
- Use one layout pass on the shared 47-focus architecture before deeper content. Then pick the most important tags for bespoke mechanics: `FTH`, `UDC`, `SDZ`, `DHC`, `KHC`, `SZA`, `UWD`, `BAC`, `ARD`, `NLC`.
- For each full custom splinter, replace at least one generic helper route with a country-specific visible mechanic or staged decision family.

## Priority Fix Queue

### Critical Gameplay-Depth Blockers

1. `OGB_soviet_collapse_focus_tree`: expand the 23-focus tree with Volga legitimacy, scholar/cleric route consequences, Idel-Ural settlement, trade-city integration, and restoration endpoint.
2. Compact crisis trees: expand `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` or document them as intentionally compact. Current 18 to 22 focus trees are shallow for the complaint.
3. Ukraine: convert flagship statehood, grain, Black Sea, and high-chaos routes from helper bundles into visible mechanics and stronger expansion/diplomacy consequences.
4. Belarus: add rail-state mechanics and staged rail/corridor/League depot decisions; reduce checklist feel.
5. Ancient restorations: either expand KZR/SOG/KHW/ALN beyond 16 focuses or explicitly treat them as compact high-chaos actors.
6. Kazakhstan: add postwar federation/resource/Caspian/old-state consequences so the large tree feels as strong as its size.

### Layout and Pathline Blockers

1. Ukraine early/statehood selector and political route geometry.
2. Belarus rail/evacuation/corridor/League convergence.
3. CFR mid-tree board/city/rail/factory/contract crossings.
4. MFR rifle/artillery/steel production crossings.
5. UDC/SDZ/DHC/KHC/FEV/SZA/UWD/BAC/ARD/NLC late convergence crossings.
6. Ancient restoration compact diamond crossings.

### Reward Cleanup

1. Reduce reliance on `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_republican_compact_plan`, `soviet_collapse_apply_focus_foreign_channel`, and `soviet_collapse_apply_focus_high_chaos_identity`.
2. Convert repeated flat variable/equipment/factory packages into route-specific decision unlocks, targeted state construction, named integration missions, claims/cores with conditions, AI strategies, or visible mechanic values.
3. Audit helper-called idea changes. Current indirect idea use is not spam, but `PRA` authority staging and compact-tree starting idea cleanup should become part of deeper mechanics.
4. Revisit focus filter labels after reward redesign. Current parser found 647 likely mismatches, too many for a one-off patch.

### AI and Localisation Cleanup

1. AI route behavior exists broadly through `ai_will_do`, but many route choices still use generic pressure/stability/war checks. Add route-specific validity checks for expansion, sponsor, league, settlement, and high-chaos branches.
2. Improve localisation tone where ids still read as route skeletons: `*_industry_plan`, `*_hidden_doctrine`, `*_extreme_gate`, `*_extreme_path`, `*_war_plan`, `*_enemy_front`, `*_diplomatic_plan`, `*_endgame`.
3. Keep focus descriptions aligned with visible mechanics after branch rewrites. Avoid update-history phrasing.
4. Add or revise custom focus filters only after reward cleanup, otherwise filter churn will be repeated.

## Validation Run

Static validation performed:
- Brace balance for all four Event005 focus files: OK (`brace_delta = 0` each).
- Unsupported `<=` or `>=` in all four Event005 focus files: none.
- Duplicate focus ids across all 1,698 Event005 focuses: none.
- Missing prerequisite or mutual-exclusion focus targets: none.
- Duplicate same-tree coordinates: none.
- Missing focus title or description localisation keys: none.
- Localisation `:0` usage in Event005 English localisation files checked: none found in files matching `*005_soviet*english.yml`.
- Focus icon sprite-name text lookup against repo and vanilla `.gfx`: 1,498 unique icon names, 0 missing.
- `unlock_decision_tooltip` targets: 117 references, 62 unique ids, 0 missing.
- Helper idea audit in `common/scripted_effects/005_soviet_collapse_effects.txt`: 763 top-level helpers scanned; 4 focus-called helpers touch ideas or idea cleanup.

Skipped validation:
- No live HOI4 launch or in-game focus-tree UI validation was run from this environment.
- No full Clausewitz engine parser is available in the repo.
- No gameplay patch was made, so no before/after behavior test was applicable.
- No flag or sprite validation beyond focus icon text lookup was run because flags and sprites were explicitly out of scope.

## Completion Status

This audit is complete as a current-state handoff. It does not complete the parent Event005 focus-tree goal because the remaining issues require broad layout and route-depth implementation. No simplification patch was made.
