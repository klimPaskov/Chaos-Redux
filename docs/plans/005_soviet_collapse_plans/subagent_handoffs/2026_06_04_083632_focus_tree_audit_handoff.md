# Event005 Soviet Collapse Focus Tree Audit Handoff

Timestamp: 2026-06-04 08:36:32 UTC
Agent role: chaosx_focus_tree_auditor
Mode: read-only audit

## Scope and No-Flag Guarantee

Audited the Event005 Soviet Collapse focus tree surface only. I did not edit gameplay, localisation, gfx, flag, TGA, DDS, or asset files. I did not inspect anything under `gfx/flags/`; flags were explicitly excluded from scope.

The requested `common/national_focus/005_soviet_collapse_ukraine.txt` and `common/national_focus/005_soviet_collapse_factory_ancient.txt` files are not present. Ukraine content is in `common/national_focus/005_soviet_collapse_republics.txt`. Ancient restoration content is in `common/national_focus/005_soviet_collapse_ancient_restorations.txt`; factory successor content is in `common/national_focus/005_soviet_collapse_factory_successors.txt`.

## Required References Used

- Read `AGENTS.md`.
- Used the `hoi4-focus-trees` skill before inspecting focus files.
- Consulted the required offline wiki pages in `paradox_wiki/`, including Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.
- Consulted vanilla documentation under `~/projects/Hearts of Iron IV/documentation/`, especially effects/triggers docs and focus inlay documentation.
- Consulted vanilla focus precedents in `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt` and `baltic_shared.txt`.
- No web access was used.

## Commands and Scripts Used

- `rg --files common/national_focus | rg '005_soviet_collapse|soviet_collapse'`
- `wc -l common/national_focus/005_soviet_collapse_*.txt`
- `rg -n` over focus files for specific focus ids, helper names, filters, and reward effects.
- Read-only Python parsers that counted focus blocks, focus ids, tree ids, filters, completion reward helper calls, repeated reward signatures, decision unlocks, annexation/wargoal/core/claim effects, x/y coordinates, prerequisites, and mutual exclusions.
- Read-only brace-depth check over all four focus files; all ended at depth 0.

## Coverage Summary

Parsed 1,698 focuses across:

- `005_soviet_collapse_ancient_restorations.txt`: KZR, SOG, KHW, ALN; 16 focuses each.
- `005_soviet_collapse_custom_splinters.txt`: 26 custom splinter trees; most large splinters use a 47-focus template, with PRA/TSC/RMC/DSC/NRF/ICD smaller variants.
- `005_soviet_collapse_factory_successors.txt`: CFR 47, OGB 23, MFR 58.
- `005_soviet_collapse_republics.txt`: Ukraine 83, generic breakaway 36, internal republic 62, Baltic 42, Caucasus 40, Central Asia 45, Moldova 48, Belarus 53, Kazakhstan 92.

## Finding 1: Repeated Helper and Idea-Bundle Rewards

No direct focus-level `add_ideas` spam was found in the audited focus files. The spam pattern is helper-bundle repetition: many focuses only set a flag, add a small flat modifier, and call the same scripted helper. Existing ideas are mainly introduced through setup/scripted-effect helpers, not directly in focus rewards.

Most repeated completion reward helpers:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 141 uses.
- `soviet_collapse_apply_focus_military_consolidation`: 132 uses.
- `soviet_collapse_apply_focus_legal_recognition`: 108 uses.
- `soviet_collapse_apply_focus_republican_compact_plan`: 80 uses.
- `soviet_collapse_apply_focus_foreign_channel`: 65 uses.
- `soviet_collapse_apply_objective_source_pressure_delta`: 63 uses.
- `soviet_collapse_apply_focus_high_chaos_identity`: 60 uses.
- `soviet_collapse_apply_focus_security_supply_plan`: 58 uses.
- `soviet_collapse_apply_focus_league_preparation`: 52 uses.
- `soviet_collapse_apply_custom_splinter_league_identity`: 38 uses.
- `soviet_collapse_apply_focus_foreign_recognition_plan`: 37 uses.
- `soviet_collapse_apply_custom_splinter_enemy_front_identity`: 36 uses.

High-confidence repeated bundle examples:

- Depot/supply bundle: `add_building_construction`, `set_country_flag`, `soviet_collapse_apply_focus_depot_and_supply_control`; 25 identical reward signatures. Examples include `FTH_free_rail_communes`, `ALA_rail_spine_to_south`, `BBH_scorched_prison_roads`, `BBH_captured_rail_stores`, `KRS_red_fleet_signal_posts`, `DHC_grain_convoy_escorts`, `KHC_winter_corridor_columns`, `UWD_rail_yard_repair_trust`, `MRC_caucasus_pack_train_board`, `IUL_oilfield_security_cordon`, `ARD_fuel_and_convoy_escorts`, `internal_soviet_collapse_pechora_rail_survival`, `internal_soviet_collapse_kazan_ufa_workshop_board`, and `internal_soviet_collapse_sevastopol_road_watch`.
- Enemy-front identity bundle: `set_country_flag`, `soviet_collapse_apply_custom_splinter_enemy_front_identity`; 20 matching signatures. Examples include `FTH_enemy_front`, `BSC_enemy_front`, `TNC_enemy_front`, `ALA_enemy_front`, `BBH_enemy_front`, `KRS_enemy_front`, `UDC_enemy_front`, `SDZ_enemy_front`, `GAC_enemy_front`, `DHC_enemy_front`, `KHC_enemy_front`, `FEV_enemy_front`, `SZA_enemy_front`, `UWD_enemy_front`, `MRC_enemy_front`, `IUL_enemy_front`, `BAC_enemy_front`.
- Legal-recognition bundle: `add_stability`, `set_country_flag`, `soviet_collapse_apply_focus_legal_recognition`; 19 matching signatures. Examples include `ukr_soviet_collapse_question_of_statehood` at `005_soviet_collapse_republics.txt:146`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_republic_of_laws`, `soviet_collapse_neutrality_under_pressure`, `internal_soviet_collapse_write_the_autonomy_statute`, `caucasus_soviet_collapse_mountain_federal_compact`, `moldova_soviet_collapse_bessarabian_legal_files`, `blr_soviet_collapse_minsk_emergency_office`, and `kaz_soviet_collapse_lone_steppe_state`.
- Custom splinter identity bundles repeat almost one-for-one across large splinters: `soviet_collapse_apply_custom_splinter_first_guard_identity`, `stores_identity`, `legitimacy_identity`, `rival_identity`, `doctrine_identity`, `foreign_identity`, `inner_faction_identity`, `special_arm_identity`, `supply_identity`, `civil_rule_identity`, `propaganda_identity`, `settlement_identity`, `industry_plan_identity`, and `hidden_doctrine_identity`. Each appears around 19 times.

## Finding 2: Trees and Branches Lacking Depth

The major systemic issue is that many trees have the visual size of a bespoke focus tree but the reward behavior of a template. Several trees lack one or more distinct political, industrial, military, diplomatic, expansion, or mechanic branches.

- `soviet_collapse_breakaway_focus_tree`: 36 focuses, 0 decision unlocks, 0 claim/core/wargoal packages, about 29 generic helper/flat-only rewards. Early examples include `soviet_collapse_assemble_emergency_government`, `soviet_collapse_guard_the_radio_stations`, `soviet_collapse_secure_ministry_ledgers`, `soviet_collapse_factory_defense_committees`, and `soviet_collapse_foreign_liaison_government`.
- `soviet_collapse_internal_republic_focus_tree`: 62 focuses, 0 decision unlocks, 0 claim/core/wargoal packages, about 33 generic helper/flat-only rewards. It has named settlement/diplomatic content but little direct map or decision payoff.
- `soviet_collapse_baltic_focus_tree`: 42 focuses, 0 decision unlocks, 0 claim/core/wargoal packages, about 31 generic rewards. Focuses such as `baltic_soviet_collapse_pan_baltic_war_room` and `baltic_soviet_collapse_baltic_shield_doctrine` read like mechanic hooks but mostly route through helper effects.
- `soviet_collapse_moldova_focus_tree`: 48 focuses, 0 decision unlocks, 0 claim/core/wargoal packages, about 35 generic rewards. Dniester, Romanian alignment, and independent republic paths lack a matching decision or map system.
- `soviet_collapse_kazakhstan_focus_tree`: 92 focuses, only 4 decision unlocks, 0 claim/core/wargoal packages, about 70 generic rewards. The tree is large, but the steppe empire/high-chaos routes are not mechanically overpowered or aggressive enough.
- `ukr_soviet_collapse_focus_tree`: 83 focuses, 7 decision unlocks, 3 claim/core/wargoal packages, about 69 generic rewards. Ukraine has better route identity than most republics, but many focuses still resolve to legal/depot/military helper calls.
- Custom 47-focus splinters such as BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, and BAC have 0 decision unlocks and usually 0-2 claim/core/wargoal packages. Most of their content is the repeated identity-helper template.
- TSC, RMC, and ICD have only 18 focuses each, 1 decision unlock, 1 wargoal/claim/core package, and 12-13 generic rewards.
- Ancient restoration trees KZR/SOG/KHW/ALN have 16 focuses each. They have some conquest/restoration hooks, but the political/industrial/military/diplomatic layers are too thin for the concept.
- Factory successors are stronger than most but uneven: CFR has 47 focuses and 8 decisions yet starts with a flat root ladder; OGB has only 23 focuses; MFR has 58 focuses but about 47 generic rewards.

## Finding 3: Layout and Pathline Risks

These are geometric risks inferred from focus x/y coordinates, prerequisite links, and mutual exclusions. They should be verified visually in the focus view.

Ancient restoration trees repeat the same convergence problem:

- KZR: `KZR_caspian_road_markets` (`x=0 y=3`) to `KZR_league_transit_bargain` (`x=6 y=4`, line 162) likely passes through `KZR_customs_workshop_compact` (`x=3 y=3`, line 85). `KZR_caspian_patrol_letters` (`x=12 y=3`, line 130) to `KZR_league_transit_bargain` likely passes through `KZR_guard_the_crossings` (`x=8 y=3`, line 116). Convergence into `KZR_old_border_files` (`x=6 y=5`, line 177) likely passes through `KZR_league_transit_bargain`.
- SOG: same pattern around `SOG_oasis_merchant_roads`, `SOG_bazaar_workshop_compact`, `SOG_scholar_envoy_rooms`, `SOG_oasis_checkpoint_guard`, `SOG_league_city_bargain`, and `SOG_old_city_border_files`.
- KHW: same pattern around `KHW_caravan_well_compact`, `KHW_oasis_workshop_compact`, `KHW_guard_the_pumps`, `KHW_canal_recognition_letters`, `KHW_league_irrigation_bargain`, and `KHW_old_oasis_border_files`.
- ALN: same pattern around `ALN_darial_road_offices`, `ALN_mountain_workshop_compact`, `ALN_guard_the_pass_line`, `ALN_mountain_envoy_guarantees`, `ALN_league_pass_bargain`, and `ALN_old_pass_border_files`.

Custom splinter template risks:

- `FTH_rival` (line 123) to `FTH_foreign` (line 215) likely crosses or visually collides with `FTH_league` (line 192).
- `FTH_inner_faction` (line 238) to `FTH_special_arm` (line 261) likely passes near or through `FTH_civil_rule` (line 333).
- `FTH_inner_faction` to `FTH_enemy_front` (line 308) likely passes near or through `FTH_supply` (line 285).
- These same template relationships likely repeat across the 47-focus custom splinter family because the branch coordinates and ids are generated from the same pattern.
- PRA has long diagonals from `PRA_omsk_station_guard` (line 1251) toward `PRA_armored_train_directorate` (line 1381) and `PRA_switchyard_denial_posts` (line 1492); these likely cross the central rail column around `PRA_novosibirsk_dispatcher_court` (line 1229) and `PRA_mobile_workshops` (line 1465). `PRA_mobile_workshops` to `PRA_flags_on_every_station` (line 1745) may collide with `PRA_neutral_corridor_letters` (line 1571).

Factory successor risks:

- CFR root is a vertical ladder at `x=17 y=0..4`: `CFR_count_the_cranes` (line 33), `CFR_the_trust_office_takes_the_seal` (line 51), `CFR_ration_cards_for_workers` (line 72), `CFR_emergency_cement_accounts` (line 91), and `CFR_the_unfinished_city_speaks` (line 111). This is not a line-crossing bug, but it makes the tree read as a narrow root rather than a major successor state.
- CFR governance fork has four mutually exclusive focuses with the same prerequisite: `CFR_elect_the_site_committees` (`x=9 y=6`, line 134), `CFR_publish_the_planners_charter` (`x=14 y=7`, line 164), `CFR_invite_the_foreign_contract_board` (`x=20 y=6`, line 196), and `CFR_the_concrete_committee` (`x=25 y=7`, line 227). The distance and stagger create route-clarity risk.
- CFR strategy fork repeats the issue: `CFR_cities_first` (`x=8 y=9`, line 357), `CFR_rails_first` (`x=12 y=10`, line 389), `CFR_factories_first` (`x=16 y=9`, line 431), and `CFR_contracts_first` (`x=20 y=10`, line 466).

## Finding 4: Focus Filter Mismatches

Likely mismatches:

- `internal_soviet_collapse_ukraine_settlement_commission` (`005_soviet_collapse_republics.txt:3904`) uses `FOCUS_FILTER_ANNEXATION`, but the reward appears to be `soviet_collapse_apply_focus_foreign_recognition_plan` plus a flag rather than a direct claim/core/wargoal/annexation payoff.
- `ukr_soviet_collapse_black_sea_hegemony` (`005_soviet_collapse_republics.txt:1754`) uses political/army filters but no annexation filter despite being a hegemony route with map-facing implications.
- `ukr_soviet_collapse_breadbasket_empire` (`005_soviet_collapse_republics.txt:1780`) uses political/industrial filters but no annexation filter despite empire framing.
- `ukr_soviet_collapse_great_steppe_and_sea_plan` (`005_soviet_collapse_republics.txt:1892`) uses political/army filters but no annexation filter despite direct expansion framing.
- `kaz_soviet_collapse_oil_field_protection_orders` (`005_soviet_collapse_republics.txt:10317`) has a manpower filter but no manpower reward in the focus block.
- `kaz_soviet_collapse_mobile_steppe_staff` (`005_soviet_collapse_republics.txt:10505`) has a manpower filter but no manpower reward.
- `kaz_soviet_collapse_aul_horse_registers` (`005_soviet_collapse_republics.txt:10525`) has an army XP filter but no army XP/helper reward.
- `kaz_soviet_collapse_league_cavalry_school` (`005_soviet_collapse_republics.txt:10598`) has an army XP filter but no army XP/helper reward.
- `kaz_soviet_collapse_foreign_trucks_local_drivers` (`005_soviet_collapse_republics.txt:11092`) has a manpower filter but no manpower reward.
- `kaz_soviet_collapse_red_nomad_committees` (`005_soviet_collapse_republics.txt:11433`) has a manpower filter but no manpower reward.
- `kaz_soviet_collapse_army_of_the_open_horizon` (`005_soviet_collapse_republics.txt:11746`) has a manpower filter but no manpower reward.

## Finding 5: Focuses That Should Connect to Soviet Collapse Mechanics

These focuses or branches read as event/mechanic hooks but currently mostly provide flat equipment, flags, ideas through helper bundles, or generic helper calls:

- Generic breakaway government formation: `soviet_collapse_assemble_emergency_government`, `soviet_collapse_guard_the_radio_stations`, `soviet_collapse_secure_ministry_ledgers`, `soviet_collapse_factory_defense_committees`, and `soviet_collapse_foreign_liaison_government`.
- Internal republic settlement/diplomacy: `internal_soviet_collapse_convene_republic_presidium`, `internal_soviet_collapse_secure_autonomous_capital`, `internal_soviet_collapse_map_union_property`, `internal_soviet_collapse_form_republic_guard`, and `internal_soviet_collapse_ukraine_settlement_commission`.
- Baltic military/diplomatic route: `baltic_soviet_collapse_pan_baltic_war_room`, `baltic_soviet_collapse_baltic_shield_doctrine`, and related shield/border focuses should unlock border defense, joint command, or anti-Soviet league decisions.
- Moldova Dniester/Romanian route: `moldova_soviet_collapse_guard_the_dniester_crossings`, `moldova_soviet_collapse_the_romanian_question`, `moldova_soviet_collapse_romanian_alignment_office`, `moldova_soviet_collapse_independent_republic_council`, and `moldova_soviet_collapse_dniester_defense_directorate` should connect to Dniester control, Romanian alignment, breakaway pressure, or claims.
- Kazakhstan high-chaos route: `kaz_soviet_collapse_the_southern_republics_do_not_kneel` should do more than league/security/high-chaos helper calls; it should create aggressive steppe-map pressure, claims, puppet demands, border-war decisions, or chaos escalation.
- Ukraine empire/hegemony route: `ukr_soviet_collapse_black_sea_hegemony`, `ukr_soviet_collapse_breadbasket_empire`, and `ukr_soviet_collapse_great_steppe_and_sea_plan` should tie into Soviet Collapse objective pressure, expansion decisions, naval/Black Sea control, grain leverage, or route-specific wars.
- Custom splinter identity routes: repeated `*_first_guard`, `*_stores`, `*_legitimacy`, `*_rival`, `*_doctrine`, `*_foreign`, `*_league`, `*_enemy_front`, `*_settlement`, and `*_industry_plan` focuses should produce country-specific mechanics, target choices, decisions, or neighbor pressure rather than only identity helpers.
- Ancient restorations KZR/SOG/KHW/ALN should have stronger restoration mechanics: old-border claims, legitimacy contests, caravan/pass/canal control decisions, and aggressive high-chaos conquest loops.

## Top 20 Actionable Fixes for Parent

### `005_soviet_collapse_republics.txt`

1. Ukraine: reduce the legal-recognition/depot/military helper repetition in early and mid-tree focuses such as `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_elections_under_shellfire`, and `ukr_soviet_collapse_republic_of_laws`; convert at least some into route-specific election, legitimacy, army command, or oblast-control mechanics.
2. Ukraine: add annexation filters and stronger map-facing payoffs to `ukr_soviet_collapse_black_sea_hegemony`, `ukr_soviet_collapse_breadbasket_empire`, and `ukr_soviet_collapse_great_steppe_and_sea_plan`.
3. Ukraine: connect Black Sea, breadbasket, Dnieper, and steppe focuses to Soviet Collapse objective pressure, expansion decisions, naval/coastal control, grain leverage, or route-specific wars instead of mostly flat helpers.
4. Generic breakaway tree: add distinct political, industrial, military, diplomacy, and expansion branches; it currently has 36 focuses with no decision unlocks and no claim/core/wargoal packages.
5. Internal republic tree: add settlement and autonomy mechanics, especially for `internal_soviet_collapse_ukraine_settlement_commission`; either provide an annexation/map payoff or remove the annexation filter.
6. Baltic tree: add pan-Baltic defense, league, border, and anti-Soviet decision mechanics; it currently has 42 focuses, 0 decisions, and 0 claim/core/wargoal packages.
7. Moldova tree: add Dniester/Romanian alignment mechanics and expansion/settlement decisions; it currently has 48 focuses, 0 decisions, and 0 claim/core/wargoal packages.
8. Belarus tree: replace generic forest/governance helper rewards with partisan corridor, Minsk legitimacy, Polish/Lithuanian border, and anti-Soviet resistance mechanics; current count is about 45 generic rewards out of 53 focuses.
9. Kazakhstan tree: make high-chaos and steppe empire routes overpowered and aggressive enough with claims, timed demands, border raids, puppet pressure, or league-subjugation decisions; current count is 92 focuses with 0 claim/core/wargoal packages.
10. Kazakhstan tree: fix filter mismatches on `kaz_soviet_collapse_oil_field_protection_orders`, `kaz_soviet_collapse_mobile_steppe_staff`, `kaz_soviet_collapse_aul_horse_registers`, `kaz_soviet_collapse_league_cavalry_school`, `kaz_soviet_collapse_foreign_trucks_local_drivers`, `kaz_soviet_collapse_red_nomad_committees`, and `kaz_soviet_collapse_army_of_the_open_horizon`.

### `005_soviet_collapse_custom_splinters.txt`

11. Large 47-focus splinters: break the repeated identity-template chain. Focuses named `*_first_guard`, `*_stores`, `*_legitimacy`, `*_rival`, `*_doctrine`, `*_foreign`, `*_league`, `*_enemy_front`, `*_settlement`, and `*_industry_plan` should not all resolve to the same helper families.
12. Large custom splinters: add real decision/mechanic/map payoff. Most BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC-style trees have 0 decision unlocks and 0-2 expansion packages.
13. High-chaos custom splinters: make aggressive countries meaningfully dangerous. Add claims, wargoals, raids, destabilization, puppet demands, objective pressure, or scripted escalation rather than only `soviet_collapse_apply_focus_high_chaos_identity`.
14. TSC/RMC/ICD: deepen the 18-focus death/revenant trees with distinct political, military, industrial, diplomacy, and expansion routes; they currently read like short variants with 12-13 generic rewards.
15. Custom splinter layout: re-lay the repeated 47-focus template around `FTH_rival`/`FTH_league`/`FTH_foreign`, `FTH_inner_faction`/`FTH_special_arm`/`FTH_civil_rule`, and `FTH_inner_faction`/`FTH_enemy_front`/`FTH_supply`; this likely repeats across sibling splinters.
16. PRA layout: review and re-lay long rail-state diagonals around `PRA_omsk_station_guard`, `PRA_armored_train_directorate`, `PRA_switchyard_denial_posts`, `PRA_mobile_workshops`, `PRA_neutral_corridor_letters`, and `PRA_flags_on_every_station`.

### `005_soviet_collapse_factory_successors.txt`

17. CFR: replace the narrow five-focus root ladder from `CFR_count_the_cranes` through `CFR_the_unfinished_city_speaks` with more distinct early industrial, political, and security choices.
18. CFR: clean up the four-way governance and strategy mutual-exclusion layouts around `CFR_elect_the_site_committees`/`CFR_publish_the_planners_charter`/`CFR_invite_the_foreign_contract_board`/`CFR_the_concrete_committee` and `CFR_cities_first`/`CFR_rails_first`/`CFR_factories_first`/`CFR_contracts_first`.
19. OGB and MFR: broaden OGB beyond 23 focuses and reduce MFR helper-only arsenal rewards. OGB should get a fuller politics/industry/military/diplomacy structure; MFR should turn its arsenal concept into more route-specific decisions and expansion pressure.

### `005_soviet_collapse_ancient_restorations.txt`

20. KZR/SOG/KHW/ALN: deepen each 16-focus ancient restoration tree and re-lay the repeated crossing-prone convergence pattern around road/workshop/guard/envoy/league/old-border focuses. Add old-border restoration, pass/canal/caravan control, legitimacy contest, and aggressive high-chaos mechanics.

## Remaining Risks

- Layout findings are coordinate-based and should be visually confirmed in-game or with a focus-tree renderer before patching.
- Helper internals were inspected by name/signature rather than exhaustively simulating gameplay outcomes. Some helper effects may have deeper side effects, but the focus-level reward surface still repeats heavily.
- Localisation was not audited beyond focus ids and reward intent, because this task was scoped to focus-tree structure and mechanics.
- No flag, TGA, DDS, or asset files were inspected.
- No commit was made, per instruction.
