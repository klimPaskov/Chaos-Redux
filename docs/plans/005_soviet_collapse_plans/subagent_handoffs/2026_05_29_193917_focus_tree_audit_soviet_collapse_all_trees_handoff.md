# Soviet Collapse Focus Tree Audit Handoff - 2026-05-29 19:39 UTC

Subagent role: `chaosx_focus_tree_auditor` style audit, patch-capable but broad redesign was out of scope.

## Scope Inspected

Focus files inspected:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No `common/national_focus/005_soviet_collapse_league.txt` exists in the current repo state. League content is embedded in the republic/custom/factory trees and shared helpers.

Required references consulted before focus inspection:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs/examples: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`, `common/ai_strategy/_documentation.md`, `common/decisions/_documentation.md`, and focus examples from `soviet.txt` and `baltic_shared.txt`.

No gameplay patch was made. The focus files are dirty and the issues are mostly broad route design, reward architecture, AI strategy, and layout cleanup rather than one isolated safe fix.

## Route Coverage Table

| Required route family | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine major republic political routes | `soviet_collapse_ukraine_focus_tree` with democratic, socialist, military, foreign/protectorate, black-banner routes | Partial | Large tree exists, but path lines are heavily crossed and rewards still lean on generic helper/idea updates. Expansion and chaos routes need stronger OP map outcomes. |
| Ukraine industry/logistics | `ukr_soviet_collapse_arsenal_cities`, `ukr_soviet_collapse_dnieper_workshops`, `ukr_soviet_collapse_ports_need_soldiers`, etc. | Partial | Many industry nodes are one-time factories/rail/building rewards; needs state programs and decisions that remain active. |
| Ukraine expansion | `ukr_soviet_collapse_direct_national_claims`, `ukr_soviet_collapse_breadbasket_empire`, `ukr_soviet_collapse_great_steppe_and_sea_plan`, black-banner chain | Partial | Present but not cleanly separated visually or mechanically from politics/diplomacy; OP conquest identity should be explicit. |
| Belarus major republic routes | `soviet_collapse_belarus_focus_tree` with national council, socialist rail, military transit, foreign corridor, forest route | Partial | Good thematic skeleton, but reward variety and AI end-states are weaker than Ukraine/Kazakhstan. |
| Kazakhstan major republic routes | `soviet_collapse_kazakhstan_focus_tree` with Alash, socialist, resource, steppe/federation, foreign technical routes | Partial | Largest tree and best decision integration, but has severe line crossing and needs clearer aggressive expansion/federation payoff. |
| Shared breakaway republic tree | `soviet_collapse_breakaway_focus_tree` | Partial | 36 focuses, usable compact surface, but generic route helpers dominate and expansion is not a distinct branch. |
| Internal republic shared tree | `soviet_collapse_internal_republic_focus_tree` | Partial | 62 focuses, multiple regional lanes, but many are OR-gated route shortcuts and generic rewards; needs route-specific mechanics. |
| Baltic shared tree | `soviet_collapse_baltic_focus_tree` | Partial | Political/diplomatic identity exists; expansion and special mechanics are thin. Path crossing is visible in the legal/defense/port branches. |
| Caucasus shared tree | `soviet_collapse_caucasus_focus_tree` | Partial | Oil/pass/mountain identity exists; needs stronger claims, compact mechanics, local wars, and postwar handling. |
| Central Asia shared tree | `soviet_collapse_central_asia_focus_tree` | Partial | Southern/Turkestan/Basmachi design exists; still lacks a full regional mechanic and has line crossing around the route fork. |
| Moldova shared tree | `soviet_collapse_moldova_focus_tree` | Partial | Strong geography, but the Romanian/Dniester/Ukraine branches overlap heavily and need cleaner route logic and payoff. |
| Full custom splinters | `BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC/FTH` 47-focus trees | Partial | Most have branch skeletons but many share the same route rhythm: legitimacy, stores, rival, league, civil/radical, industry, endgame. Needs more bespoke mechanics. |
| Crisis/custom shallow splinters | `PRA` 22 focuses; `TSC/RMC/DSC/NRF/ICD` 18 focuses each | Fails depth target | These are too shallow for chaos countries. They have strong concepts but not full political, industrial, military, diplomatic, expansion, special mechanic, and endgame branches. |
| Factory successors | `CFR` 47, `MFR` 58, `OGB` 23 | Mixed | CFR/MFR have structure; OGB is shallow. CFR has overconstrained industry mutual exclusions. MFR aggression exists but should become route-aware, not only endpoint spikes. |
| Ancient restorations | `KZR/SOG/KHW/ALN` 16 focuses each | Fails depth target | Compact ancient trees are not large-country routes. They need political restoration, economy, army, diplomacy, expansion, special mechanic, and final identity families. |

## High-Priority Findings

| Priority | Issue | Exact files and identifiers | Why it matters |
| --- | --- | --- | --- |
| High | Shallow chaos countries do not meet the user request that chaos countries become overpowered and aggressive. | `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `PRA_soviet_collapse_focus_tree` (22), `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree` (18 each). | These trees are conceptually interesting but too short to support politics, economy, military, diplomacy, expansion, special mechanics, OP escalation, and postwar handling. |
| High | `OGB` is too shallow for a high-chaos/factory-successor identity. | `common/national_focus/005_soviet_collapse_factory_successors.txt`: `OGB_soviet_collapse_focus_tree`, especially `OGB_open_the_volga_registers` through `OGB_the_old_name_survives_modern_war`. | It has a council fork, trade, heritage guard, Idel-Ural choice, claims, and an end state, but lacks full industrial/military/diplomacy/expansion depth and needs a stronger OP Volga empire route. |
| High | Ancient restoration trees are compact placeholders compared to required route depth. | `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`. | 16 focuses each cannot support restoration politics, state economy, restoration army, diplomatic recognition, expansion pressure, and final restoration identity. |
| High | Helper-led idea lifecycle creates idea-spam feel even without duplicate direct `add_ideas` in focus rewards. | Focus files call `soviet_collapse_apply_focus_legal_recognition` 305 times, `soviet_collapse_apply_focus_depot_and_supply_control` 257 times, `soviet_collapse_apply_focus_military_consolidation` 252 times, `soviet_collapse_apply_focus_league_preparation` 220 times, `soviet_collapse_apply_focus_foreign_channel` 176 times, `soviet_collapse_update_consolidated_republic_ideas` 111 times. These helpers feed `common/scripted_effects/005_soviet_collapse_effects.txt:5461` `soviet_collapse_update_consolidated_republic_ideas`, which adds tiered republic/league/foreign/local-authority ideas. | This avoids duplicate direct focus rewards, but still makes many routes feel like the same idea-tier updater plus small numeric rewards. |
| High | Pathline crossings are severe in several major trees. | `common/national_focus/005_soviet_collapse_republics.txt`: `soviet_collapse_ukraine_focus_tree` 153 detected crossings, `soviet_collapse_kazakhstan_focus_tree` 120, `soviet_collapse_moldova_focus_tree` 91, `soviet_collapse_belarus_focus_tree` 33. Samples: `ukr_soviet_collapse_question_of_statehood` crossing with `ukr_soviet_collapse_elections_under_shellfire`/`ukr_soviet_collapse_republic_of_laws`; `kaz_soviet_collapse_the_congress_chooses_a_past` crossing `kaz_soviet_collapse_guard_the_resource_towns` branches; `moldova_soviet_collapse_moldova_route_fork` crossing Dniester/Ukraine grain routes. | The user specifically reported overlapping lines and nonsensical structure; these are not isolated cosmetic bugs. They need layout redesign. |
| High | Route-aware AI strategy is incomplete. | `common/ai_strategy/005_soviet_collapse.txt` has Ukraine lines 268-434, Belarus 438-576, Kazakhstan 580-720, generic custom splinter lines 157-219, and generic high-chaos lines 222-245. No equivalent route-specific AI strategy families exist for Baltic, Caucasus, Central Asia, Moldova, internal republics, CFR, MFR, OGB, ancient restorations, or each custom splinter identity. | Focus-level `ai_will_do` exists, but countries do not get route-specific aggression, production, target, faction, and expansion strategies for most trees. |

## Repeated Same Idea in One Focus

Mechanical check result: no direct duplicate `add_ideas = <same_idea>` occurrences were found inside any single `focus = { ... }` completion reward in the four inspected focus files.

Important caveat: idea-spam still exists through helper calls. Exact helper-side idea updater:

- `common/scripted_effects/005_soviet_collapse_effects.txt:5461` `soviet_collapse_update_consolidated_republic_ideas`
- Adds tier ideas at lines 5477-5540: `soviet_collapse_republic_institutions_1..4`, `soviet_collapse_republic_league_coordination_1..4`, `soviet_collapse_republic_foreign_support_1..4`, `soviet_collapse_republic_local_authority_pressure_1..4`.

Focus ids that visibly call both a route helper and the updater and should be reviewed first:

- `common/national_focus/005_soviet_collapse_republics.txt:65` `ukr_soviet_collapse_seal_the_grain_ledgers`
- `common/national_focus/005_soviet_collapse_republics.txt:1430` `ukr_soviet_collapse_british_caution`
- `common/national_focus/005_soviet_collapse_republics.txt:5702` `caucasus_soviet_collapse_oilfield_security_compacts`
- `common/national_focus/005_soviet_collapse_republics.txt:6414` `caucasus_soviet_collapse_oil_state_command`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:44` `FTH_first_guard`
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1202` `OGB_the_council_takes_the_seal`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:343` `KZR_league_transit_bargain`

## Generic Reward and Idea-Spam Routes

Representative exact focus ids with generic equipment/factory/truck/train/building/stat rewards that should be replaced or supplemented with route mechanics:

| File | Focus id | Current pattern |
| --- | --- | --- |
| `005_soviet_collapse_republics.txt:94` | `ukr_soviet_collapse_count_the_depot_keys` | Equipment stockpile reward plus generic depot mechanics. |
| `005_soviet_collapse_republics.txt:114` | `ukr_soviet_collapse_first_republican_line` | Manpower, buildings, war support. |
| `005_soviet_collapse_republics.txt:1105` | `ukr_soviet_collapse_arsenal_cities` | Factory construction reward. |
| `005_soviet_collapse_republics.txt:1202` | `ukr_soviet_collapse_dnieper_workshops` | Factory construction reward. |
| `005_soviet_collapse_republics.txt:2552` | `soviet_collapse_military_defense_council` | Equipment and buildings rather than a lasting command system. |
| `005_soviet_collapse_custom_splinters.txt:1295` | `PRA_count_the_locomotives` | Train stockpile, infrastructure, railway. |
| `005_soviet_collapse_custom_splinters.txt:1434` | `PRA_coal_water_and_spare_parts` | Train stockpile, supply node, railway, infrastructure. |
| `005_soviet_collapse_custom_splinters.txt:1462` | `PRA_mobile_workshops` | Arms factory, support equipment. |
| `005_soviet_collapse_custom_splinters.txt:1995` | `TSC_observatory_guard` | XP, manpower, equipment, depot variable. |
| `005_soviet_collapse_factory_successors.txt:1240` | `OGB_reopen_volga_trade_tolls` | Generic depot/liaison variables plus rail/supply construction. |
| `005_soviet_collapse_factory_successors.txt:1287` | `OGB_kazan_ferry_offices` | One civilian factory. |
| `005_soviet_collapse_ancient_restorations.txt:173` | `KZR_old_border_files` | Claims plus train/infrastructure stockpile pattern. |

Recommendation: keep a few one-time rewards, but each family should convert the main branch rewards into unlocks: targeted state missions, route decisions, advisor/commander unlocks, special units, claims/cores with integration, timed objectives, construction programs, patron/rival decisions, and route-specific AI strategies.

## Missing or Weak Branch Depth

| Tree/family | Exact identifiers | Missing or weak content |
| --- | --- | --- |
| Pale Railway Authority | `PRA_the_timetable_declares_authority`, `PRA_novosibirsk_dispatcher_court`, `PRA_armored_train_directorate`, `PRA_rails_over_capitals`, `PRA_the_pale_line_endures` | Needs a full moving-state mechanic: rail control meter, junction targets, mobile capital decisions, armored train templates, border-warp claims, logistics overdrive, and escalating conquest missions. |
| Tunguska Signal Committee | `TSC_the_committee_of_instruments`, `TSC_the_committee_of_signs`, `TSC_starfall_mandate`, `TSC_observatory_state` | Needs anomaly/research mechanic visible to the player, radar/site state targets, signal events, aerial/rocket/special-project hooks, and OP starfall expansion. |
| Resurrection Martyr Commune | `RMC_communes_of_witnesses`, `RMC_cadres_of_resurrection`, `RMC_procession_columns`, `RMC_resurrection_without_state` | Needs resurrection/recruitment mechanic, martyr levy units, state-conversion pressure, and aggressive pilgrimage-front expansion. |
| Dead Soldiers' Congress | `DSC_witness_officers`, `DSC_revenant_staff_line`, `DSC_congress_of_the_dead_army` | Needs dead-army command hierarchy, battlefield recovery missions, old-front claims, commander/advisor effects, and war-goal chain. |
| Northern Revenant Fleet | `NRF_living_harbor_committees`, `NRF_revenant_admiralty`, `NRF_northern_revenant_fleet` | Needs naval/port control mechanic, convoy raiding AI, White Sea/Baltic ambitions, special marines, shipyard/port decisions. |
| Immortal Commissariat | `ICD_commissars_of_last_addresses`, `ICD_commissars_who_do_not_die`, `ICD_commissariat_without_end` | Needs dead-roll bureaucracy mechanic, purges/integration, occupied-state claims, commissar units/advisors, and relentless conquest AI. |
| OGB Old Volga Bulgaria | `OGB_scholars_guard_the_charter`, `OGB_clerics_guard_the_charter`, `OGB_treat_with_idel_ural`, `OGB_the_volga_cannot_have_two_seals`, `OGB_volga_restoration_state` | Needs full cleric/scholar/notable route, Volga trade economy, heritage army, diplomacy with IUL/KAZ/SOV, staged old-city integration, and OP Volga restoration route. |
| Ancient restorations | `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, `ALN_alan_pass_charter` | End-state charters should cap multi-branch routes, not appear after 16-focus compact chains. |

## Meaningless or Overused Mutual Exclusions

Reciprocity check found no missing reciprocal mutual exclusions. The problem is meaning, not syntax.

Questionable overuse:

- `common/national_focus/005_soviet_collapse_factory_successors.txt:364-474`: `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, and `CFR_contracts_first` all mutually exclude each other. These are industry priorities, not incompatible identities; they would work better as staged priorities, modifiers, or decision specializations rather than permanent hard locks.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: repeated `*_settlement` versus `*_radical_turn` pairs across many 47-focus splinter trees (`FTH_settlement`/`FTH_radical_turn`, `BSC_settlement`/`BSC_radical_turn`, `TNC_settlement`/`TNC_radical_turn`, `ALA_settlement`/`ALA_radical_turn`, `BBH_settlement`/`BBH_radical_turn`, etc.) are structurally repetitive. They can be valid, but the repeated pattern makes countries feel cloned.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1214-1234`: `OGB_scholars_guard_the_charter` versus `OGB_clerics_guard_the_charter` is meaningful, but it currently gates only a shallow tree. It needs different follow-up content, not just two minor popularity/stability variants.

## Prerequisite Semantics and Nonsensical Route Structure

Multi-focus prerequisite blocks are OR, not AND. Several appear intentionally OR-gated, but they create route shortcuts and confusing linework when used as broad branch joins without visible/clear availability.

High-risk examples:

- `common/national_focus/005_soviet_collapse_republics.txt:3075` `soviet_collapse_armed_neutrality` has one OR prerequisite block with seven focus ids: `soviet_collapse_rail_hub_or_mountain_pass`, `soviet_collapse_road_and_rail_repair_board`, `soviet_collapse_neutrality_under_pressure`, `soviet_collapse_league_reserve_table`, `soviet_collapse_free_republics_observer_seat`, `soviet_collapse_high_chaos_local_strongman`, `soviet_collapse_border_militia_standard`.
- `common/national_focus/005_soviet_collapse_republics.txt:5332` `baltic_soviet_collapse_the_baltic_question_resolved` OR-joins six route endpoints, increasing line-crossing risk.
- `common/national_focus/005_soviet_collapse_republics.txt:8748` `moldova_soviet_collapse_republic_of_crossings` OR-joins eight focus ids.
- `common/national_focus/005_soviet_collapse_republics.txt:8791` `moldova_soviet_collapse_the_river_state` OR-joins nine focus ids.
- `common/national_focus/005_soviet_collapse_republics.txt:17282` `FEV_endgame` OR-joins nine focus ids.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:18462` `SZA_endgame` OR-joins nine focus ids.

Recommendation: use visible route funnel nodes or separate route end focuses instead of many-endpoint OR joins. Where OR is intentional, move the focus to a neutral endpoint area and add clear route tooltip localisation.

## Pathline Overlap and Too-Close Layout Risks

Detected line crossing counts from focus coordinate/prerequisite geometry:

| Tree | Crossings detected | Example crossings |
| --- | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 153 | `ukr_soviet_collapse_guard_the_telegraph_house -> ukr_soviet_collapse_question_of_statehood` crosses `ukr_soviet_collapse_seal_the_grain_ledgers -> ukr_soviet_collapse_village_granary_guards`; multiple `ukr_soviet_collapse_foreign_courts_notice_kyiv -> ukr_soviet_collapse_open_the_liaison_offices` crossings. |
| `soviet_collapse_kazakhstan_focus_tree` | 120 | `kaz_soviet_collapse_the_congress_chooses_a_past` crosses resource and Alash/resource branch lines repeatedly. |
| `soviet_collapse_moldova_focus_tree` | 91 | `moldova_soviet_collapse_moldova_route_fork` crosses Dniester, Ukrainian border, grain, and neutrality paths. |
| `soviet_collapse_belarus_focus_tree` | 33 | `blr_soviet_collapse_which_road_is_belarus` crosses rail/evacuation/forest lines. |
| `soviet_collapse_central_asia_focus_tree` | 24 | `central_asia_soviet_collapse_local_republic_council` crossings around Basmachi/oasis choices. |
| `soviet_collapse_caucasus_focus_tree` | 18 | Oil directorate and route fork crossings around `caucasus_soviet_collapse_oilfield_security_compacts`. |
| `soviet_collapse_baltic_focus_tree` | 14 | Legal/defense/port branch crossings around `baltic_soviet_collapse_the_baltic_question_resolved`. |
| `UWD_soviet_collapse_focus_tree` | 35 | `UWD_supply`/industry/radical/settlement branch crossings. |
| `BAC_soviet_collapse_focus_tree` | 44 | `BAC_industry_plan`, `BAC_war_plan`, `BAC_radical_turn`, and diplomatic branches cross repeatedly. |
| `SZA_soviet_collapse_focus_tree` | 29 | `SZA_extreme_gate`, `SZA_settlement`, `SZA_endgame`, and infrastructure branches cross. |

Too-close vertical spine examples:

- `common/national_focus/005_soviet_collapse_factory_successors.txt`: `CFR_count_the_cranes` -> `CFR_the_unfinished_city_speaks` at x=17 y=0..4.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: `MFR_orders_outlive_ministries` -> `MFR_who_owns_the_rifle` at x=15 y=0..5.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: `OGB_open_the_volga_registers` -> `OGB_clerics_guard_the_charter` at x=6 y=0..3.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: the 18-focus crisis trees often stack decisive endpoints at x=6 y=10..11 (`TSC_observatory_state`, `TSC_the_quiet_sky_settlement`, `RMC_republic_of_witnesses`, `RMC_shrine_state`, `NRF_port_republic_of_the_living`, `NRF_memorial_convoy_state`, `ICD_citizens_after_death`, `ICD_state_of_last_addresses`).

## Icon Coverage Table

| File | Missing icons | Repeated icon ids | Notes |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 0 | 22 repeated ids | Repeats include `GFX_ukr_soviet_collapse_democratic`, `GFX_moldova_soviet_collapse_ukrainian_corridor`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_central_asia_soviet_collapse_steppe_federation`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`. |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 99 repeated ids | Repeated route-template icons dominate, including `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_foreign`, `GFX_focus_MRC_civil_rule`, `GFX_focus_IUL_war_plan`, `GFX_focus_IUL_supply`, `GFX_focus_FEV_diplomatic_plan`. |
| `005_soviet_collapse_factory_successors.txt` | 0 | 11 repeated ids | Repeats include `GFX_focus_CFR_the_builder_state`, `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, `GFX_focus_CFR_civilian_hegemony_project`. |
| `005_soviet_collapse_ancient_restorations.txt` | 0 | 8 repeated ids | Ancient trees reuse shared icons such as `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_returned_names_endgame`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`. |

Icon recommendation: repeated route-template icons are acceptable for placeholders, but the requested redesign needs unique route-family icons for chaos countries, factory successors, ancient restorations, and major route endpoints.

## Localisation and Reward Mismatch List

Mechanical localisation check result: every inspected focus id has a title key and `_desc` key in `localisation/english/005_soviet_collapse*_l_english.yml`.

Reward/localisation mismatch and weak-match risks:

- `common/national_focus/005_soviet_collapse_factory_successors.txt:958` `CFR_build_the_border_bend_the_border`: uses `FOCUS_FILTER_ANNEXATION`, follows an aggressive eastward focus, and the title implies border manipulation, but the reward only calls `soviet_collapse_apply_cfr_focus_border_permit_network = yes`. It needs a direct border/claim/war/settlement decision payoff or a filter change.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1650` `PRA_claim_the_branch_lines`: title implies map claims; reward mainly increments `pra_rail_authority`, unlocks `pra_drive_the_junction_columns`, and applies depot control. If the decision grants the map action, the focus tooltip should make that clear; otherwise it needs direct rail-junction claims.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2152` `TSC_claim_the_impact_zone`: title implies a territorial claim, but the visible reward is authority/high-chaos identity and field station depth. Needs explicit claims/targeted decisions or a clearer title.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1287` `OGB_kazan_ferry_offices`: title is geographically strong but the reward is only a random owned/core civilian factory. It should target Kazan/Volga states if available.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:268` `KZR_khazar_charter`, and equivalent `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, `ALN_alan_pass_charter`: charter end-states read larger than their 16-focus mechanical base.

## Focus Filters That Do Not Match Rewards

- `CFR_build_the_border_bend_the_border` (`005_soviet_collapse_factory_successors.txt:958`): `FOCUS_FILTER_ANNEXATION` risk as above.
- `PRA_claim_the_branch_lines` (`005_soviet_collapse_custom_splinters.txt:1650`): should include `FOCUS_FILTER_ANNEXATION` if the route is a territorial rail-junction claim, or should be renamed/retuned as a logistics focus.
- `TSC_claim_the_impact_zone` (`005_soviet_collapse_custom_splinters.txt:2152`): should include `FOCUS_FILTER_ANNEXATION` only if it receives explicit claims/war/target decisions; otherwise use political/army/special-mechanic filters.
- `OGB_kazan_ferry_offices` (`005_soviet_collapse_factory_successors.txt:1287`): `FOCUS_FILTER_INDUSTRY` is technically correct, but the random-state reward does not match a named Kazan focus.

## AI Behavior Gaps

Current AI strengths:

- All inspected focuses have `ai_will_do`.
- `common/ai_strategy/005_soviet_collapse.txt` has general Soviet crisis behavior, generic breakaway survival, generic League support, generic custom-splinter signature force behavior, generic high-chaos signature force behavior, and detailed Ukraine/Belarus/Kazakhstan route blocks.
- Several endpoint focuses add direct `add_ai_strategy` toward `SOV` or `IUL`, for example `PRA_rails_over_capitals`, `TSC_starfall_mandate`, `OGB_the_volga_cannot_have_two_seals`, `CFR_the_builder_state_marches_east`, `MFR_no_peace_without_orders`.

Gaps:

- No route-specific AI strategy family for `soviet_collapse_baltic_focus_tree`, `soviet_collapse_caucasus_focus_tree`, `soviet_collapse_central_asia_focus_tree`, `soviet_collapse_moldova_focus_tree`, or `soviet_collapse_internal_republic_focus_tree`.
- No bespoke AI strategy family for `PRA/TSC/RMC/DSC/NRF/ICD`; they share `soviet_collapse_high_chaos_signature_force_route`, which only boosts army/equipment and does not set concrete expansion targets, local rivals, faction behavior, state priorities, naval/air behavior, or special mechanic use.
- No bespoke AI strategy family for `CFR/MFR/OGB`; aggression is mostly endpoint hidden effects.
- No bespoke AI strategy family for ancient restorations `KZR/SOG/KHW/ALN`; each expansionist endpoint gets generic SOV conquest/antagonize but not region-specific claim, alliance, or invasion behavior.

## Recommended Full Route Architecture

### Major Republics

Ukraine:

- Opening survival: emergency Rada, depot control, grain ledgers, telegraph/radio, officer question.
- Political routes: democratic Rada, peasant socialist, military Directory, foreign protectorate, black-banner bread-state.
- Industry/logistics: Dnieper arsenal decisions, Black Sea port logistics, grain requisition/relief, rail/river supply missions.
- Military: republican army, Black Sea defense, armored/mobile columns, officer purge/vetting, port guards.
- Diplomacy/League: Free Republics League leadership, foreign courts, Anatolian grain mission, sponsor risks.
- Expansion: west question, Black Sea hegemony, steppe and sea plan, breadbasket empire, black-banner compulsory grain frontier.
- Mechanic hooks: grain authority, officer loyalty, League command, foreign dependency, famine/breadline pressure.
- OP chaos identity: black-banner route should create coercive grain frontier decisions, forced integration of breadbasket states, war goals on SOV and border republic rivals, and severe stability/diplomacy tradeoffs.

Belarus:

- Opening survival: Minsk rail map, evacuation choice, forest committees, corridor guard.
- Political: national council, socialist rail authority, military transit directorate, foreign corridor administration, forest state.
- Industry/logistics: rail timetables, swamp roads, Brest/Minsk hub repairs, depot redirection.
- Military: guide companies, forest brigades, rail-war state, green-border defense.
- Diplomacy: corridor neutrality, Polish/Baltic/League access, foreign aid through Brest.
- Expansion: corridor seizure, rail chokepoint ultimatums, Pripet/Smolensk/Brest border decisions.
- Mechanic hooks: corridor leverage, rail obedience, forest legitimacy, foreign traffic.
- OP chaos identity: forest/rail route should make Belarus an unavoidable transit predator with war goals, forced access, and supply-denial missions.

Kazakhstan:

- Opening survival: Alma-Ata congress, resource towns, southern wires, steppe districts.
- Political: Alash, socialist steppe, resource directorate, steppe federation, foreign technical route.
- Industry/resources: Karaganda coal, oil boards, copper/chrome, rail to mines, concession audits.
- Military: steppe cavalry, mobile army, thousand-kilometer defense, southern shield.
- Diplomacy: Central Asian federation, League resource pool, foreign engineers with dependency risk.
- Expansion: Basmachi roads, Kyrgyz/Uzbek/Turkestan frontier, resource protectorates, old steppe claims.
- Mechanic hooks: resource legitimacy, foreign dependency, steppe cohesion, southern frontier pressure.
- OP chaos identity: resource directorate should buy/force protectorates and generate war goals around mines/oil/rail corridors.

Baltic/Caucasus/Central Asia/Moldova/Internal shared trees:

- Each needs a regional mechanic, not only shared helper variables.
- Baltic: legal continuity, port customs, forest resistance, Pan-Baltic defense, foreign recognition, League compact, anti-SOV claims/guarantees.
- Caucasus: pass control, oil authority, mountain councils, Black Sea/Caspian route choice, ancient crown pressure, pipeline war.
- Central Asia: majlis legitimacy, Basmachi route, cotton/irrigation economy, Turkestan federation, southern shield, border-band missions.
- Moldova: Prut/Dniester balancing, Romanian question, Ukraine grain road, river-state customs, neutrality corridor, Transnistrian defense.
- Internal republics: regional modules should become separate mini-route overlays: northern forest, Volga-Ural, Crimea/Black Sea, Siberian/Baikal/Far East, each with claims and local mechanics.

### Custom Splinter Full Trees

Every 47-focus custom splinter should use this route frame, but with country-specific mechanics:

- Political: civil council, radical route, legal/settlement route, identity shift.
- Industrial: named state economy, rail/ports/mines/farms/workshops tied to actual regions.
- Military: signature force branch with special templates, commanders, defense/offense decisions.
- Diplomacy: League route, foreign patron route, anti-puppet guarantees, local rival settlements.
- Expansion: direct target regions, claims, ultimatums, war goals, integration decisions, postwar penalties.
- Special mechanic: one visible country-specific value that focuses and decisions change.
- Endgame: either regional compact, formable/cosmetic identity, or OP conquest identity.

### Chaos/Overpowered Country Identities

- `PRA`: Pale Railway Authority. Overpowered identity: moving state that controls rail junctions. Hooks: rail authority meter, mobile capital, armored trains, junction-seizure decisions, war goals on SOV/rail hubs, supply denial and forced access.
- `TSC`: Tunguska Signal Committee. Overpowered identity: anomaly observatory state. Hooks: anomaly research, radar/signal sites, signal-weapon missions, air/radar bonuses, starfall claims, SOV destabilization.
- `RMC`: Resurrection Martyr Commune. Overpowered identity: martyr processions and resurrection cadres. Hooks: martyr levy, casualty-to-manpower conversion, reliquary state targets, pilgrimage-war claims.
- `DSC`: Dead Soldiers' Congress. Overpowered identity: dead army command. Hooks: battlefield recovery, old-front claims, commander ghosts/councils, endless mobilization with industry/stability costs.
- `NRF`: Northern Revenant Fleet. Overpowered identity: drowned fleet and port-state. Hooks: convoy raiding, icebound marines, White Sea/Baltic claims, naval AI, port integration.
- `ICD`: Immortal Commissariat. Overpowered identity: bureaucracy that records everyone into service. Hooks: death roll authority, commissar units, occupation/integration pressure, purge events, relentless SOV conquest.
- `CFR`: Concrete Factory Republic. Overpowered identity: construction state that annexes by rebuilding. Hooks: reconstruction contracts, debt-map subjects, forced construction protectorates, concrete war machine.
- `MFR`: Militarized Foundry Republic. Overpowered identity: arsenal state. Hooks: arms export/client network, armored train/tank line, war-economy AI, conquer for foundry inputs, client wars.
- `OGB`: Old Volga Bulgaria. Overpowered identity: restored Volga empire. Hooks: Bolghar legitimacy, river tolls, heritage guard, Idel-Ural rivalry, Kazan/Ufa integration, old trade-city claims.
- `KZR/SOG/KHW/ALN`: Ancient restoration states. Overpowered identity: returned old-name polities. Hooks: restoration legitimacy, museum/archive claims, old-border surveys, restoration levies, ancient-charter formables, SOV/Russia-region claims.

### Factory Successors

CFR:

- Political route: site committees, planners, foreign contract board, concrete committee.
- Industry route: cities/rails/factories/contracts should be staged priorities, not mutually exclusive hard locks.
- Military route: sappers, builder-state march, fortification/reconstruction corps.
- Expansion route: debt-map, concrete protectorates, eastward march, rebuilding-for-annexation decisions.
- Diplomacy: League contracts, German/British/Japanese/foreign cement bids with dependency.

MFR:

- Political route: officers, armorers, merchants, eternal arsenal.
- Industry route: rifle line, artillery, plate steel, unsafe surge, red warning lamps.
- Military route: factory guard, armored trains, gates/sirens/rifles.
- Expansion route: arm all clients, no peace without orders, every order a rifle.
- Diplomacy: arms export, buyer flags, German/British/Japanese order chains, betrayal/embargo risks.

OGB:

- Political route: scholars, clerics, notables, restored society.
- Industry: Volga tolls, ferries, caravans, workshops, river trade.
- Military: heritage guard, cavalry, Volga crossings, Kazan/Ufa guard.
- Diplomacy: Idel-Ural compact versus rivalry, Kazakh/steppe letters, League/foreign recognition.
- Expansion: old trade cities, Idel-Ural war/compact, old capital, restored Volga state.

### Ancient Restorations

Each ancient tree should expand from 16-focus compact to 35-50 focus real tree:

- Opening restoration council and legitimacy debate.
- Legal/symbolic route versus expansionist restoration route.
- Economy tied to the old polity's geography.
- Military route with signature levies/guards.
- Diplomacy route with League, nearby republics, and foreign observers.
- Archive/museum/old-border decision family.
- Integration/postwar route after taking claimed states.
- Final charter route with cosmetic identity, flag/leader/advisor hooks, and AI strategy.

## Implementation-Ready Fix Order

1. Rewrite layout of the four worst crossing trees first: Ukraine, Kazakhstan, Moldova, Belarus.
2. Expand `PRA/TSC/RMC/DSC/NRF/ICD` and `OGB` before polishing larger trees; these fail the user's depth/aggression requirement most clearly.
3. Convert repeated helper/idea updater reward rhythm into route mechanics. Keep the updater, but it should support route-specific decisions, claims, units, laws, advisors, and state programs rather than being the main reward.
4. Add route-specific AI strategies for Baltic, Caucasus, Central Asia, Moldova, internal republics, factory successors, ancient restorations, and each chaos country.
5. Rework `CFR_cities_first`/`CFR_rails_first`/`CFR_factories_first`/`CFR_contracts_first` from hard mutual exclusions into staged priorities or decision choices.
6. Audit `CFR_build_the_border_bend_the_border`, `PRA_claim_the_branch_lines`, and `TSC_claim_the_impact_zone` for filter/reward/title alignment.
7. Replace repeated icon ids for chaos endpoints and route-family capstones.

## Validation Run

Commands run:

- Mechanical duplicate direct `add_ideas` per focus: custom parser over all four inspected focus files. Result: no direct duplicate same-idea-in-one-focus cases.
- Duplicate helper calls per focus: custom parser over all four inspected focus files. Result: no duplicated same helper call inside a single focus.
- Focus count, missing icon, repeated icon, missing localisation, missing AI, repeated helper, generic reward, mutual exclusion reciprocity, multi-focus prerequisite, coordinate closeness, and pathline crossing checks: custom parser over all four inspected focus files.
- `rg --files common/national_focus | rg '005|soviet|collapse|league|factory|splinter|successor|republic'`
- `rg -n "add_ai_strategy|ai_strategy" common/national_focus/005_soviet_collapse_*.txt common/scripted_effects/005_soviet_collapse_effects.txt`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`: no matches.
- Brace-depth check over all four inspected focus files: final depth `0`, minimum depth `0` for each file.
- `git diff --check --no-index /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_193917_focus_tree_audit_soviet_collapse_all_trees_handoff.md`: no whitespace-error output. The command exits non-zero because the file is new compared with `/dev/null`.

Validation still required after this handoff:

- If parent patches gameplay, run `git diff --check` for touched files.

## Skipped Patches and Why

- No focus-file patch: current failures are broad tree redesign and layout architecture issues, not one isolated fix.
- No localisation patch: focus title/description keys are mechanically present.
- No icon patch: missing icons were not found; repeated icon identity needs design/art pass rather than arbitrary swaps.
- No AI patch: route-aware AI gaps require a planned strategy matrix, not small numeric focus-weight edits.

## Remaining Route Risks

- The current trees are not completion-grade for the user's stated standard.
- Existing direct focus-level `ai_will_do` may mask missing country-level AI strategy because every focus technically has a weight.
- Many focus names now imply concrete map/route effects that are only delivered through helpers or tooltips; parent should inspect decision availability before deciding whether to patch the focus or the decision.
- Large OR prerequisite joins can be intentional, but they are a major source of layout clutter and confusing route structure.
- Worktree was dirty before this audit; no unrelated changes were reverted.
