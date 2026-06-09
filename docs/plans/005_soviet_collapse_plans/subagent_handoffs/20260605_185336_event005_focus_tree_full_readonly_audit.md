# Event005 Soviet Collapse Focus Tree Read-Only Audit

Timestamp: 2026-06-05 18:53:36 UTC

Role: `chaosx_focus_tree_auditor`

Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Supporting reads only: `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt`, `common/ideas/005_soviet_collapse_ideas.txt`, `common/script_constants/005_soviet_collapse_constants.txt`

No gameplay, localisation, asset, flag, or gfx files were edited. This handoff is the only file written by this audit.

## Required references read

- Skills: `.agents/skills/hoi4-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`
- Offline wiki: National focus modding, Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, AI modding, On actions, Event modding, Decision modding, Idea modding
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/poland.txt`

Key reference points used:

- Focus layout uses grid positions; `relative_position_id` must resolve inside the same tree.
- Repeated `prerequisite = { ... }` blocks are AND. Multiple `focus = ...` entries inside one `prerequisite` block are OR.
- AI focus weights are MTTH blocks. Route behavior should not rely only on flat focus weights when the route changes war, diplomacy, or expansion behavior.
- Ideas are persistent national spirits. Repeated `add_ideas`/same-target `swap_ideas` should be treated as a lifecycle problem unless the branches are mutually exclusive and clearly guarded.

## Inventory by file and tree

| File | Tree | Focuses | Visible route families | Missing or underdeveloped branches |
|---|---|---:|---|---|
| republics | `soviet_collapse_ukraine_focus_tree` | 83 | opening statehood, socialist, cabinet/army, foreign liaison, industry/depot, Black Sea/Romanian corridor, expansion, Bread State, anarchist/double-republic endgame | Strong count but branch clarity is poor because diplomacy, industry, expansion, and Bread State routes cross each other visually and share too many flat stat rewards. Needs cleaner route lanes and stronger mechanical payoffs outside the extreme Bread State branch. |
| republics | `soviet_collapse_breakaway_focus_tree` | 36 | generic breakaway statehood, political route fork, military, foreign liaison, league/neutrality, old underground | Compact tree remains shallow. Industry and diplomacy are mostly support nodes; expansion and special mechanics are weak. |
| republics | `soviet_collapse_internal_republic_focus_tree` | 62 | internal republic presidium, autonomy, regional subroutes, military, trade, old names | Several regional packages are shallow and layout has exact coordinate overlap. Political and regional identity branches need more route-specific decisions and postwar handling. |
| republics | `soviet_collapse_baltic_focus_tree` | 42 | restoration/legal state, foreign protection, ports/customs, Baltic shield, Pan-Baltic resolution | Industry and expansion are thin; diplomacy and military cross heavily in layout. |
| republics | `soviet_collapse_caucasus_focus_tree` | 40 | border/faith/nations fork, oil/security, foreign guarantees, ancient crowns | Oil, political, and mountain autonomy lanes overlap. Expansion branch needs clearer war/coring settlement. |
| republics | `soviet_collapse_central_asia_focus_tree` | 45 | southern route fork, local republic, Basmachi, cotton/rail, league/desert settlement | Several same-row focuses are too close; industry and expansion are mostly small state/equipment rewards. |
| republics | `soviet_collapse_moldova_focus_tree` | 48 | Dniester defense, Bessarabian legal files, Ukrainian/Romanian routes, anti-air/crossing defense | Worst republican crossing count. Industry/air defense and diplomacy are entangled; route payoff clarity is poor. |
| republics | `soviet_collapse_belarus_focus_tree` | 53 | rail map, Minsk junction, Brest foreign aid, partisan/forest, timetable state, League, green border | Duplicate coordinate and many focus-on-line hits around Minsk/Brest route. Political/industry/foreign split is visually unclear. |
| republics | `soviet_collapse_kazakhstan_focus_tree` | 92 | steppe congress, Alash, resource towns, league, oil/security, foreign technical missions, border cavalry, Caspian/Japanese/Turkish/Iranian contacts | Highest focus count but three exact overlaps and 11 too-close pairs. Expansion and diplomacy are broad but hard to read; several rewards are still trucks/support/convoys. |
| custom splinters | `FTH_soviet_collapse_focus_tree` | 47 | commune/opening, internal faction, league/foreign, military, industry, high-chaos commune | Aggressive enough through helpers, but route lanes still read as generic labels in several places. |
| custom splinters | `PRA_soviet_collapse_focus_tree` | 22 | railway authority, decisions, armored train, rail conquest/endgame | Narrow but coherent. Needs deeper political and diplomacy branches if intended as a long-lived country. |
| custom splinters | `TSC_soviet_collapse_focus_tree` | 18 | observatory/science, perimeter, impact zone, starfall mandate | Shallow: political, industry, diplomacy, military, and special mechanic all collapse into a small gimmick tree. |
| custom splinters | `RMC_soviet_collapse_focus_tree` | 18 | martyr cult, reliquary, dead columns, resurrection endgame | Shallow; needs more special mechanic and aggression before the final node. |
| custom splinters | `DSC_soviet_collapse_focus_tree` | 18 | dead soldiers congress, roll call, revenant staff, lost armies, dead army endgame | Mechanically stronger than other 18-focus trees, but one helper has duplicate same-target idea lifecycle and the route is still short. |
| custom splinters | `NRF_soviet_collapse_focus_tree` | 18 | revenant fleet, harbor/salvage, admiralty, White Sea claim | Shallow; navy identity is present, but politics/industry/diplomacy are minimal. |
| custom splinters | `ICD_soviet_collapse_focus_tree` | 18 | absent citizens, commissariat, memorial guard, unburied front | Shallow death-state tree. Needs overpowered aggression and special mechanics before endgame. |
| custom splinters | `BSC_soviet_collapse_focus_tree` | 47 | Basmachi state, caravan/oasis, league/foreign, raiding, settlement, high-chaos | Aggression exists through helpers; route clarity moderate. |
| custom splinters | `TNC_soviet_collapse_focus_tree` | 47 | Turkestan city/oasis, local politics, irrigation/cotton, diplomacy, settlement, extreme path | Direct aggression is weak: only decision/endgame/identity helpers show; needs war-plan and border settlement payloads. |
| custom splinters | `ALA_soviet_collapse_focus_tree` | 47 | Alash/steppe, minority guarantees, diplomacy, industry, settlement, extreme path | Direct aggression is weak; expansion path does not look overpowered. |
| custom splinters | `BBH_soviet_collapse_focus_tree` | 47 | black banner, columns, no masters, borderless endgame | Too soft for a chaos country. Only endgame/identity helpers carry aggression markers. |
| custom splinters | `KRS_soviet_collapse_focus_tree` | 47 | port/sailor assembly, free port, anti-party soviet, naval support, endgame | Too soft for a chaos country. No mid-tree war goal, core, annex, or hostile AI focus found in focus rewards. |
| custom splinters | `UDC_soviet_collapse_focus_tree` | 47 | loyalist command, depots, staff cars, command mediation, hidden doctrine, extreme | Aggressive helper usage is present and route is viable, but still uses generic branch anchors. |
| custom splinters | `SDZ_soviet_collapse_focus_tree` | 47 | archive/security directorate, custody, offices/watchposts, hidden doctrine, extreme | Aggressive helper usage is present; many rewards are still support equipment/offices rather than unique mechanic. |
| custom splinters | `GAC_soviet_collapse_focus_tree` | 47 | village congress, harvest/airstrip, mediation, partisan/green army | Some aggression through high-chaos neighbor helper, but no direct cores/annex chain. |
| custom splinters | `DHC_soviet_collapse_focus_tree` | 47 | Don host, cavalry/remounts, crossings, southern corridors, endgame | Too soft: no direct war goals; only identity/endgame helpers and generic high-chaos identity. |
| custom splinters | `KHC_soviet_collapse_focus_tree` | 47 | Kuban host, crossings, grain corridor, mountain/steppe compact | Some aggression at `KHC_steppe_and_mountain_compact`, but not enough for chaos-country feel. |
| custom splinters | `FEV_soviet_collapse_focus_tree` | 47 | Far Eastern buffer, harbor, rail militia, Pacific diplomacy/Japan, endgame | Under-aggressive: diplomacy with Japan is stronger than expansion. Needs war goals, cores, invasion pressure. |
| custom splinters | `SZA_soviet_collapse_focus_tree` | 47 | Siberian zemstvo, railhead/depth, workshops, station fortress | Too soft: mostly identity/endgame helpers and no direct expansion chain. |
| custom splinters | `UWD_soviet_collapse_focus_tree` | 47 | Ural workers, arsenal/foundry/rail yards, federation/endgame | Too soft for industrial chaos: no direct war goals, conquest AI, or annex/coring route in focus rewards. |
| custom splinters | `MRC_soviet_collapse_focus_tree` | 47 | mountain republic/pass confederation, aul militia, lowland raids | Too soft: only endgame helper marker detected. Needs actual raiding, cores/claims, war-plan route. |
| custom splinters | `IUL_soviet_collapse_focus_tree` | 47 | Idel-Ural, Volga crossings, oilfield, Kazan-Ufa, corridor | Too soft in its own tree; OGB has more direct conflict over IUL than IUL has outward aggression. |
| custom splinters | `BAC_soviet_collapse_focus_tree` | 47 | Birobidzhan, settlement defense, relief, Amur/Far East, autonomy | Too soft: only endgame helper marker detected. |
| custom splinters | `ARD_soviet_collapse_focus_tree` | 47 | Arctic port, Murmansk docks, White Sea, naval infantry, convoy diplomacy | Some high-chaos neighbor helper; needs direct naval war and occupation payoffs. |
| custom splinters | `NLC_soviet_collapse_focus_tree` | 47 | polar commune, weather/science, ice road, tundra watch, extreme path | Aggression and spawn helpers exist; layout still has line hits and route clarity issues. |
| factory | `CFR_soviet_collapse_focus_tree` | 47 | construction trust, committees/contractors/concrete state, city/factory/rail/contract tracks, protectorates | Strong construction identity but not aggressive enough until late protectorate/builder-state helpers. |
| factory | `OGB_soviet_collapse_focus_tree` | 23 | Volga registers, scholar/cleric route, heritage guard, Idel-Ural question, restored Volga empire | Coherent but shallow; OGB is more aggressive than most 23-focus trees but needs more industry and diplomacy depth. |
| factory | `MFR_soviet_collapse_focus_tree` | 58 | arsenal board, military/council/merchant routes, artillery/rifles/tanks/air parts, client arms, eternal arsenal | Stronger than most, but still has repeated flat arsenal/equipment rewards and layout crossings. |
| ancient | `KZR_soviet_collapse_ancient_focus_tree` | 16 | Khazar toll/crossing, Caspian roads, expansionist levy, charter/endgame | Very shallow but aggressive enough for a compact ancient restoration. Needs postwar integration decisions. |
| ancient | `SOG_soviet_collapse_ancient_focus_tree` | 16 | Sogdian city/merchant roads, city claims, charter/endgame | Very shallow; claims/wargoal exist but route is a short ladder. |
| ancient | `KHW_soviet_collapse_ancient_focus_tree` | 16 | Khwarazmian oasis/canal/water claims, charter/endgame | Very shallow; claims/wargoal exist but too many rewards are trains/trucks/support. |
| ancient | `ALN_soviet_collapse_ancient_focus_tree` | 16 | Alan pass/road, mountain claims, charter/endgame | Very shallow; claims/wargoal exist but needs occupation/coring decisions. |

## Idea reward audit

No large direct focus-level idea spam remains in the four focus files. The only same-target duplicate detected by the script is indirect and helper-driven:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3016` `DSC_call_the_dead_soldiers_congress` calls `soviet_collapse_update_dsc_dead_army_idea`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:18332` `soviet_collapse_update_dsc_dead_army_idea` can target `dsc_dead_army_politics` through both `swap_ideas = { add_idea = dsc_dead_army_politics }` and `add_ideas = dsc_dead_army_politics`.
- The current branches are guarded by `if`/`else_if`, so this is not guaranteed double application in one execution. It is still a duplicate same-target lifecycle in one helper and should be simplified to a single helper path or documented as a guarded migration helper.

Other idea application found in `common/scripted_effects/005_soviet_collapse_effects.txt` is mostly startup/setup: `soviet_collapse_republican_startup_disorder`, `cfr_construction_mandates`, `mfr_arsenal_quotas`, `mfr_factory_guard_state`, and one starting idea per custom splinter. I did not find focuses directly stacking several long-lived ideas in their `completion_reward`.

## Shallow and spammy reward audit

The mechanical scan found 744 candidate shallow reward focuses across all four files when counting flat PP/stability/war support/XP, tiny building grants, equipment dumps, and tech bonuses that are not tied to decisions, war goals, units, cores, or route mechanics. The highest-impact repeat offenders are equipment and single-building rewards.

Exact repeated equipment cases:

- `train_equipment_1`: `ukr_soviet_collapse_seal_the_grain_ledgers`, `FTH_supply`, `PRA_armored_train_schools`, `PRA_claim_the_branch_lines`, `PRA_seize_the_junction_cities`, `NLC_ice_road_customs`, `MFR_armored_train_workshops`, `KZR_old_border_files`, `KZR_khazar_charter`, `KHW_expansionist_water_claims`.
- `motorized_equipment_1`: `kaz_soviet_collapse_foreign_trucks_local_drivers`, `KHW_canal_recognition_letters`, `KHW_khwarazmian_water_charter`.
- `support_equipment_1`: `ukr_soviet_collapse_count_the_depot_keys`, `soviet_collapse_military_defense_council`, `soviet_collapse_foreign_liaison_government`, `internal_soviet_collapse_republic_volunteer_standards`, `baltic_soviet_collapse_latvian_port_guard_boards`, `caucasus_soviet_collapse_black_sea_observer_desks`, `caucasus_soviet_collapse_yerevan_relief_networks`, `central_asia_soviet_collapse_pamir_pass_fortresses`, `central_asia_soviet_collapse_the_oasis_arsenal`, `central_asia_soviet_collapse_the_oasis_guard`, `central_asia_soviet_collapse_desert_republic_settlement`, `moldova_soviet_collapse_river_guard_brigades`, `kaz_soviet_collapse_oil_field_protection_orders`, `kaz_soviet_collapse_army_of_the_open_horizon`, `FTH_first_guard`, `FTH_stores`, `FTH_economy`, `FTH_special_arm`, `FTH_anti_puppet_commune_clause`, `FTH_commune_court_registers`, `TSC_perimeter_regiments`, `RMC_lipetsk_reliquary_workshops`, `RMC_blood_oath_requisitions`, `RMC_dead_volunteer_columns`, `DSC_call_the_dead_soldiers_congress`, `DSC_field_hospital_memorials`, `ICD_penza_memorial_workshops`, `ICD_black_seal_requisitions`, `ICD_memorial_battalions`, `ICD_letters_to_grieving_cities`, `BSC_first_guard`, `BSC_caravan_officer_schools`, `BSC_tajik_pass_bargains`, `BSC_raiding_column_oaths`, `TNC_tajik_relief_corridors`, `TNC_city_militia_charter`, `ALA_turkmen_route_bargain`, `ALA_steppe_supply_hubs`, `BBH_column_schools`, `BBH_armored_car_raids`, `BBH_roving_artillery_crews`, `BBH_column_supply_ledgers`, `BBH_red_and_black_depots`, `BBH_borderless_column_schools`, `KRS_port_guard_schools`, `UDC_staff_car_workshops`, `UDC_war_plan`, `SDZ_every_office_a_watchpost`, `SDZ_document_cart_workshops`, `SDZ_archive_bunker_vaults`, `SDZ_witness_protection_cells`, `SDZ_secure_court_dockets`, `SDZ_signal_van_yards`, `DHC_cavalry_remount_yards`, `FEV_railway_militia_charter`, `FEV_winter_rail_columns`, `FEV_siberian_factory_letters`, `SZA_winter_column_registers`, `SZA_baikal_rear_area`, `SZA_ural_factory_letters`, `UWD_perm_field_staff`, `UWD_tagil_machine_tool_ledger`, `UWD_factory_militia_charter`, `mrc_raid_lowland_depots`, `MRC_aul_militia_charter`, `MRC_argun_rear_area`, `IUL_samara_crossing_ledger`, `IUL_kama_workshop_trust`, `BAC_war_plan`, `BAC_observer_relief_conference`, `BAC_birobidzhan_council_records`, `BAC_grain_and_relief_escorts`, `BAC_winter_road_columns`, `BAC_far_eastern_letters`, `BAC_autonomy_statute`, `NLC_heated_workshop_contracts`, `NLC_winter_road_columns`, `NLC_apatity_rear_area`, `SOG_expansionist_merchant_claims`, `KHW_delta_without_a_center`.

Representative exact tiny-building/flat-stat offenders:

- Ukraine: `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_count_the_depot_keys`, `ukr_soviet_collapse_first_republican_line`, `ukr_soviet_collapse_moscows_officers_in_our_barracks`, `ukr_soviet_collapse_workers_congress_in_kharkiv`, `ukr_soviet_collapse_village_soviets_without_requisition`, `ukr_soviet_collapse_re_register_the_party`, `ukr_soviet_collapse_arsenal_cities`, `ukr_soviet_collapse_dnieper_workshops`, `ukr_soviet_collapse_black_sea_port_ledgers`.
- Generic breakaway: `soviet_collapse_assemble_emergency_government`, `soviet_collapse_depot_repair_crews`, `soviet_collapse_home_industry_contracts`, `soviet_collapse_military_defense_council`, `soviet_collapse_foreign_liaison_government`, `soviet_collapse_border_militia_standard`, `soviet_collapse_rail_hub_or_mountain_pass`.
- Internal republic: `internal_soviet_collapse_northern_timber_rail_fund`, `internal_soviet_collapse_karelian_finnish_border_mission`, `internal_soviet_collapse_komi_river_and_mine_committees`, `internal_soviet_collapse_pechora_rail_survival`, `internal_soviet_collapse_ural_cavalry_roads`.
- Custom splinters with many small rewards: `BBH_column_schools`, `BBH_armored_car_raids`, `BBH_roving_artillery_crews`, `BBH_column_supply_ledgers`, `BBH_red_and_black_depots`, `SDZ_document_cart_workshops`, `SDZ_archive_bunker_vaults`, `SDZ_signal_van_yards`, `BAC_winter_road_columns`, `BAC_obluchye_rear_area`, `BAC_far_eastern_letters`, `ARD_ice_watch_boards`, `NLC_heated_workshop_contracts`, `NLC_winter_road_columns`, `NLC_apatity_rear_area`.
- Factory/ancient: `MFR_armored_train_workshops`, `MFR_foundry_line_holds`, `MFR_contracts_with_builders`, `KZR_caspian_patrol_letters`, `KHW_canal_recognition_letters`, `KHW_khwarazmian_water_charter`, `ALN_symbolic_pass_principality`.

Recommended replacements:

- Replace repeated support equipment rewards with route-specific unit templates, timed recruitment decisions, militia/guard battalion spawning, doctrine bonuses, or unlocks to repeatable regional defense decisions.
- Replace trains/trucks with railway/convoy mechanics: targeted railway repair decisions, supply hub missions, rail denial operations, armored train templates, or logistics company template upgrades.
- Replace single `infrastructure = 1`, `arms_factory = 1`, `industrial_complex = 1`, `air_base = 1`, or `radar_station = 1` rewards with named state packages tied to the country identity, decision unlocks, or route-specific construction projects.
- Replace flat PP/stability/war support filler with actual political state changes: route locks, leader/advisor unlocks, law changes, ideology balance, recognition mechanics, decision category expansions, hostile AI strategy, or scripted variable milestones that later content reads.

## Chaos-country aggression audit

One-level helper expansion was included for focus rewards that call `soviet_collapse_* = yes` helpers.

Trees that are still too soft or too late in their aggression:

- `TNC_soviet_collapse_focus_tree`: only `TNC_special_arm`, `TNC_extreme_gate`, `TNC_endgame`, `TNC_extreme_path` show decision/endgame/identity markers. Add direct war-plan claims/wargoals, cores or integration decisions, and hostile AI.
- `ALA_soviet_collapse_focus_tree`: same issue as TNC. `ALA_special_arm`, `ALA_extreme_gate`, `ALA_endgame`, `ALA_extreme_path` are not enough.
- `BBH_soviet_collapse_focus_tree`: only `BBH_banner_without_borders` and `BBH_extreme_path` show helper markers. Black Banner should be much more aggressive: borderless raids, instant neighbor war plan, unit spawning, no-puppet annex/coring decisions, hostile AI.
- `KRS_soviet_collapse_focus_tree`: only `KRS_extreme_path` and `KRS_endgame` show helper markers. Needs port-seizure war goals, naval invasion preparation, anti-SOV aggression, and port occupation decisions.
- `DHC_soviet_collapse_focus_tree`: only `DHC_steppe_watch_posts`, `DHC_endgame`, `DHC_don_endurance`, `DHC_extreme_path` show identity/endgame helpers. Needs direct Don/Kuban/Volga war plan, cavalry columns, and coring/settlement.
- `SZA_soviet_collapse_focus_tree`: only `SZA_station_fortress_line`, `SZA_extreme_path`, `SZA_endgame` show markers. Needs Siberian depth conquest/rail corridor war mechanics.
- `UWD_soviet_collapse_focus_tree`: only `UWD_endgame`, `UWD_extreme_path` show markers. Industrial chaos should add arms-export coercion, factory guard columns, neighbor wargoals, and AI building/attack strategy.
- `MRC_soviet_collapse_focus_tree`: only `MRC_extreme_path` shows an endgame helper. Needs lowland raids, pass claims, mountain coring/occupation decisions, hostile AI.
- `IUL_soviet_collapse_focus_tree`: only `IUL_extreme_path`, `IUL_endgame` show markers. Needs direct Volga-Ural expansion and conflict over OGB/Kazan/Ufa.
- `BAC_soviet_collapse_focus_tree`: only `BAC_extreme_path` shows an endgame helper. Needs Amur/Far East aggression and settlement-defense conquest payoffs.
- `FEV_soviet_collapse_focus_tree`: `FEV_harbor_fortress_line` uses a conflict helper, but the rest leans Japanese/Pacific diplomacy. Needs stronger war and occupation branch.
- `CFR_soviet_collapse_focus_tree`: construction identity is strong, but aggression appears late through `CFR_the_builder_state_marches_east` and `CFR_reconstruction_protectorates`. Add earlier protectorate pressure and hostile AI.

Trees that are comparatively stronger:

- `FTH`, `BSC`, `UDC`, `SDZ`, `DSC`, `NLC`, `OGB`, `MFR`, and ancient restorations all have meaningful aggressive helpers or direct war markers, but several still need clearer route placement and postwar integration.

Missing aggression surfaces to add where absent:

- Direct `create_wargoal` or route-specific helper calls on `war_plan`, not only extreme/endgame.
- Controlled-state coring or annex/coring decisions after conquest.
- Spawned route units tied to doctrine, not only generic assault columns.
- `add_ai_strategy` for `conquer`, `antagonize`, `prepare_for_war`, `building_target`, and template priorities against concrete targets.
- Postwar border settlement decisions and resistance risks.

## Layout audit

Quantitative layout summary from resolved absolute coordinates:

| Tree | Focuses | Duplicates | Too-close | Crossings | Focus-on-line |
|---|---:|---:|---:|---:|---:|
| `soviet_collapse_ukraine_focus_tree` | 83 | 0 | 0 | 19 | 2 |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 0 | 14 | 3 |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 1 | 1 | 11 | 5 |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 0 | 15 | 1 |
| `soviet_collapse_caucasus_focus_tree` | 40 | 1 | 0 | 17 | 5 |
| `soviet_collapse_central_asia_focus_tree` | 45 | 0 | 3 | 15 | 0 |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 2 | 32 | 0 |
| `soviet_collapse_belarus_focus_tree` | 53 | 1 | 0 | 3 | 9 |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 3 | 11 | 0 | 7 |
| `FTH_soviet_collapse_focus_tree` | 47 | 0 | 0 | 1 | 0 |
| `PRA_soviet_collapse_focus_tree` | 22 | 0 | 0 | 1 | 0 |
| `TSC_soviet_collapse_focus_tree` | 18 | 0 | 0 | 3 | 1 |
| `RMC_soviet_collapse_focus_tree` | 18 | 0 | 0 | 3 | 1 |
| `DSC_soviet_collapse_focus_tree` | 18 | 0 | 0 | 1 | 1 |
| `NRF_soviet_collapse_focus_tree` | 18 | 0 | 0 | 1 | 1 |
| `ICD_soviet_collapse_focus_tree` | 18 | 0 | 0 | 1 | 1 |
| `BSC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 4 | 0 |
| `TNC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 5 | 0 |
| `ALA_soviet_collapse_focus_tree` | 47 | 0 | 0 | 1 | 0 |
| `BBH_soviet_collapse_focus_tree` | 47 | 0 | 0 | 1 | 0 |
| `KRS_soviet_collapse_focus_tree` | 47 | 0 | 0 | 2 | 0 |
| `UDC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 16 | 0 |
| `SDZ_soviet_collapse_focus_tree` | 47 | 0 | 0 | 16 | 0 |
| `GAC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 13 | 1 |
| `DHC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 18 | 1 |
| `KHC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 30 | 0 |
| `FEV_soviet_collapse_focus_tree` | 47 | 0 | 0 | 17 | 0 |
| `SZA_soviet_collapse_focus_tree` | 47 | 0 | 0 | 28 | 0 |
| `UWD_soviet_collapse_focus_tree` | 47 | 0 | 0 | 35 | 1 |
| `MRC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 5 | 0 |
| `IUL_soviet_collapse_focus_tree` | 47 | 0 | 0 | 12 | 0 |
| `BAC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 44 | 0 |
| `ARD_soviet_collapse_focus_tree` | 47 | 0 | 0 | 20 | 0 |
| `NLC_soviet_collapse_focus_tree` | 47 | 0 | 0 | 22 | 1 |
| `CFR_soviet_collapse_focus_tree` | 47 | 0 | 0 | 0 | 0 |
| `OGB_soviet_collapse_focus_tree` | 23 | 0 | 0 | 0 | 1 |
| `MFR_soviet_collapse_focus_tree` | 58 | 0 | 1 | 8 | 0 |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | 0 | 0 | 2 | 0 |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | 0 | 0 | 1 | 0 |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | 0 | 0 | 2 | 0 |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | 0 | 0 | 2 | 0 |

High-priority exact layout issues:

- Ukraine crossings:
  - `ukr_soviet_collapse_seal_the_grain_ledgers -> ukr_soviet_collapse_question_of_statehood` crosses `ukr_soviet_collapse_guard_the_telegraph_house -> ukr_soviet_collapse_dnieper_workshops`.
  - `ukr_soviet_collapse_first_republican_line -> ukr_soviet_collapse_war_without_a_declaration` crosses `ukr_soviet_collapse_question_of_statehood -> ukr_soviet_collapse_foreign_courts_notice_kyiv`.
  - `ukr_soviet_collapse_foreign_courts_notice_kyiv -> ukr_soviet_collapse_open_the_liaison_offices` crosses `ukr_soviet_collapse_black_sea_port_ledgers -> ukr_soviet_collapse_romanian_port_route`.
  - `ukr_soviet_collapse_socialist_republic_without_moscow -> ukr_soviet_collapse_workers_congress_in_kharkiv` crosses both `ukr_soviet_collapse_peasant_socialist_congress -> ukr_soviet_collapse_village_soviets_without_requisition` and `ukr_soviet_collapse_elections_under_shellfire -> ukr_soviet_collapse_free_soil_compromise`.
  - Focus-on-line: `ukr_soviet_collapse_german_liaison_question` sits on `ukr_soviet_collapse_black_sea_port_ledgers -> ukr_soviet_collapse_romanian_port_route`; `ukr_soviet_collapse_advisers_without_flags` sits on `ukr_soviet_collapse_romanian_port_route -> ukr_soviet_collapse_anatolian_grain_mission`.
- Belarus:
  - Exact duplicate coordinate `(6,4)`: `blr_soviet_collapse_seal_the_minsk_junction`, `blr_soviet_collapse_foreign_aid_through_brest`.
  - Focus-on-line around the duplicate: `blr_soviet_collapse_the_rail_map_on_the_wall -> blr_soviet_collapse_seal_the_minsk_junction` runs through `blr_soviet_collapse_foreign_aid_through_brest`; `blr_soviet_collapse_western_corridor_switchmen -> blr_soviet_collapse_foreign_aid_through_brest` runs through `blr_soviet_collapse_seal_the_minsk_junction` and `blr_soviet_collapse_depot_cars_without_labels`.
  - Crossings: `blr_soviet_collapse_railway_guard_regiments -> blr_soviet_collapse_rail_war_state` crosses `blr_soviet_collapse_seal_the_minsk_junction -> blr_soviet_collapse_every_track_through_minsk`; `blr_soviet_collapse_guide_companies -> blr_soviet_collapse_swamp_roads_closed` crosses `blr_soviet_collapse_forest_defense_staff -> blr_soviet_collapse_partisans_or_army`.
- Kazakhstan:
  - Exact duplicates: `(26,4)` `kaz_soviet_collapse_the_alash_courts` with `kaz_soviet_collapse_the_resource_towns_demand_seats`; `(16,7)` `kaz_soviet_collapse_foreign_trucks_local_drivers` with `kaz_soviet_collapse_emergency_oil_boards`; `(2,7)` `kaz_soviet_collapse_army_of_the_open_horizon` with `kaz_soviet_collapse_uzbek_supply_delegates`.
  - Too-close pairs: `kaz_soviet_collapse_oasis_and_steppe_congress` with `kaz_soviet_collapse_southern_deputies_demand_seats` and `kaz_soviet_collapse_the_steppe_cannot_be_encircled`; `kaz_soviet_collapse_league_resource_pool` with `kaz_soviet_collapse_foreign_technical_missions`; `kaz_soviet_collapse_league_cavalry_school` with `kaz_soviet_collapse_border_cavalry_schools`; `kaz_soviet_collapse_crush_the_road_militias` with `kaz_soviet_collapse_collective_farm_bargains`; `kaz_soviet_collapse_the_last_caravan_tax` with `kaz_soviet_collapse_kyrgyz_border_cavalry` and `kaz_soviet_collapse_horse_and_truck_columns`; `kaz_soviet_collapse_caspian_security_detachments`, `kaz_soviet_collapse_iranian_caspian_notes`, `kaz_soviet_collapse_japanese_far_east_approaches` form an x-adjacent same-row cluster.
- Other bad layout trees by crossing count: `BAC` 44, `UWD` 35, `moldova` 32, `KHC` 30, `SZA` 28, `NLC` 22, `ARD` 20, `DHC` 18, `FEV` 17, `caucasus` 17, `UDC`/`SDZ` 16 each.

I found no isolated/unconnected focuses in the parsed trees.

## Prioritized implementation plan for parent

1. `005_soviet_collapse_republics.txt`: Fix exact coordinate overlaps and focus-on-line defects first.
   - Belarus duplicate `(6,4)` and line hits around Minsk/Brest.
   - Kazakhstan three duplicate coordinates and same-row clusters.
   - Ukraine foreign/Black Sea/Bread State route crossings.
   - Moldova crossing cleanup if time permits; it has the highest republican crossing count.

2. `005_soviet_collapse_custom_splinters.txt`: Add direct aggression and route-depth patches to the soft chaos trees.
   - First tranche: `BBH`, `KRS`, `UWD`, `MRC`, `BAC`.
   - Second tranche: `TNC`, `ALA`, `DHC`, `SZA`, `IUL`, `FEV`.
   - Keep patches disjoint by tag. Add direct war-plan helpers, unit spawns, conquest AI, claims/cores or integration decisions, and postwar settlement.

3. `005_soviet_collapse_custom_splinters.txt`: Replace repeated support-equipment filler.
   - Group by regional family to avoid giant risky edits: death-state mini trees (`RMC`, `DSC`, `ICD`, `NRF`), steppe/Central Asia (`BSC`, `TNC`, `ALA`, `BBH`), Siberia/Far East (`FEV`, `SZA`, `BAC`, `NLC`), Volga/Ural/Caucasus (`UWD`, `MRC`, `IUL`, `DHC`, `KHC`).

4. `005_soviet_collapse_factory_successors.txt`: Patch `CFR`, `OGB`, `MFR`.
   - `CFR`: move aggression earlier than `CFR_the_builder_state_marches_east`; deepen protectorate and construction-debt mechanics.
   - `OGB`: expand from 23 focuses or add stronger route-specific helper calls.
   - `MFR`: clean crossings and replace train/factory filler with arsenal production decisions or template unlocks.

5. `005_soviet_collapse_ancient_restorations.txt`: Keep compact but deepen postwar handling.
   - Add annex/coring or integration decisions for each ancient restoration, not just claims/wargoals.
   - Replace trains/trucks/support with restoration-specific guard columns, toll decisions, pass/canal/city integration.

6. `005_soviet_collapse_effects.txt`: Simplify `soviet_collapse_update_dsc_dead_army_idea`.
   - Keep the guarded migration behavior if needed, but avoid same-target `swap_ideas` and `add_ideas` appearing as duplicate idea lifecycle from one focus helper.

## Validation commands and limitations

Commands run:

- `sed -n` reads of required skills and wiki pages.
- `sed -n` reads of vanilla docs and `common/national_focus/poland.txt`.
- `wc -l` on all target focus and support files.
- `rg -n` for `focus_tree`, focus ids, `add_ideas`, `swap_ideas`, `add_timed_idea`, equipment, buildings, war goals, cores, claims, AI strategies, unit spawn helpers.
- Python one-off parser over the four focus files plus `005_soviet_collapse_effects.txt`:
  - counted `focus_tree` and `focus = {}` blocks
  - extracted focus ids, line numbers, prerequisites, mutual exclusions, rewards, helper calls
  - resolved absolute x/y coordinates including `relative_position_id`
  - detected duplicate coordinates, same-row x-adjacent pairs, prerequisite line crossings, and focus-on-line hits
  - scanned direct rewards and one-level helper bodies for idea/equipment/aggression markers

Limitations:

- This was a text/static audit only. No game launch, GUI screenshot, or in-game focus rendering was performed.
- Layout crossings are geometric approximations from resolved focus grid coordinates. The game's rendered pathline shape can differ, but duplicate positions and focus-on-line hits are reliable.
- Helper expansion was one level deep. Deep nested helpers may add additional aggression or rewards; the listed gaps are still valid where the focus tree itself does not expose clear direct mechanics.
- The working tree was already dirty before this audit. I did not inspect or revert unrelated changes and did not commit.

## Skills used

- `hoi4-focus-trees`
- `chaos-redux-events`
