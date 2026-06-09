# Event 005 Soviet Collapse Focus Tree Audit - Read-Only Handoff

Subagent: `chaosx_focus_tree_auditor`
Date: 2026-06-05 07:36 UTC
Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- relevant `localisation/english/005_soviet_collapse*_l_english.yml` focus/localisation evidence

Mode: read-only audit. No gameplay, localisation, gfx, flag, or docs files were edited except this handoff. No commit was made.

Required references consulted before inspection:
- Repo skill: `hoi4-focus-trees`
- Offline wiki snapshot: National focus modding, Data structures, Trigger, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`.
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`.

## Executive blockers

1. The requested "full rework toward clear political, industry, military/security, diplomacy, and expansion branches" is still not achieved uniformly. Ukraine, Belarus, and Kazakhstan have many focuses, but several branches are overconnected, diagonal, and reward-led rather than route-led. CFR and MFR have stronger identity but still rely on repeated helper calls and flat reward stacking. PRA has a clear rail identity but is only 22 focuses. TSC, RMC, DSC, NRF, and ICD are only 18 focuses each and read as compressed identity sidecars instead of full overpowered country trees.
2. The worst reward/plumbing exposure is in the high-chaos custom splinters, especially `DSC_revenant_staff_line` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2974`, which directly chains eight helpers including multiple `_payload` helpers, neighbor war helpers, idea update, claims/cores, unit spawn, AI strategy, stockpile rewards, and a tooltip in one focus.
3. Layout/pathline issues remain statically provable in Ukraine, Belarus, Kazakhstan, PRA, TSC, RMC, DSC, NRF, ICD, and MFR. The worst cases are Belarus and Kazakhstan, where long diagonal prerequisite lines cross many other prerequisite lines; the small 18-focus custom splinter templates also have repeatable mid-tree line-through-node problems.
4. No direct `add_ideas`, `add_timed_idea`, `swap_ideas`, or `remove_ideas` calls exist in the four audited focus files. Therefore I found no direct duplicate idea additions in the audited focus files. Idea work is routed through helper effects such as `soviet_collapse_ensure_cfr_construction_mandates_idea` and `soviet_collapse_update_pra_authority_idea`; those helpers should still be reviewed during implementation because they hide idea churn from the focus surface.
5. Localisation coverage for the audited focus files is currently complete across `localisation/english/005_soviet_collapse*_l_english.yml`: 1,698 focus blocks checked, 0 missing focus names/descriptions, 0 missing referenced tooltip keys, 0 duplicate localisation keys. Weak tooltip wording is not the main blocker; mechanics/layout/reward structure is.
6. Flag/sprite files were not touched or audited for flipping. If any flag issue appears in game, likely non-sprite causes to inspect are cosmetic tag assignment, tag/original_tag loading, focus-tree country score, or release/load effects, not flag file orientation.

## Branch-depth assessment by tree

### Major republic trees

- Ukraine: `common/national_focus/005_soviet_collapse_republics.txt:17`, `soviet_collapse_ukraine_focus_tree`, 83 focuses, max depth 14, average depth 6.4, 16 leaves. It has political, military, industry, diplomacy, League, expansion, and high-chaos surfaces, but the structure still feels like a dense reward web. Multiple diplomacy/industry/military lines cross. Many high-value focuses set 4-5 flags in a single reward, for example `ukr_soviet_collapse_league_founding_charter` at line 1505, `ukr_soviet_collapse_league_of_equals` at line 1545, and `ukr_soviet_collapse_border_states_accept_kyiv` at line 1811.
- Belarus: `common/national_focus/005_soviet_collapse_republics.txt:8820`, `soviet_collapse_belarus_focus_tree`, 53 focuses, max depth 10, average depth 5.0, 13 leaves. It has a strong corridor/rail/forest concept, but the branch layout crosses heavily and the tree is not yet a clean political/industry/security/diplomacy/expansion split. It has many generic shared helpers and only 12 decision unlock tooltips; rail identity should become a system with transit, armored train, supply, and border-control decisions rather than mostly focus rewards.
- Kazakhstan: `common/national_focus/005_soviet_collapse_republics.txt:10162`, `soviet_collapse_kazakhstan_focus_tree`, 92 focuses, max depth 9, average depth 5.2, 30 leaves. It has the broadest scope and good identity surfaces: Alash memory, socialist steppe, resource directorate, Turkestan federation, foreign vectors, rail/resource towns. The current issue is branch sprawl and crossings around the early congress/resource/rail layer; many leaves are depth 6-9 support endpoints rather than route-defining end states.

### Factory successors

- CFR: `common/national_focus/005_soviet_collapse_factory_successors.txt:17`, `CFR_soviet_collapse_focus_tree`, 47 focuses, max depth 18, average depth 9.3, 8 leaves. Identity is strong: construction mandates, unfinished cities, reconstruction contracts. However, a construction directorate meant to be extremely overpowered still has too few direct factories/building outputs in the focus surface: only one direct `add_building_construction` in focus rewards, with most map power hidden in helpers/decisions. It should have more visible civilian factory, building-slot, construction-speed, state buildout, and client-city mechanics.
- MFR: `common/national_focus/005_soviet_collapse_factory_successors.txt:1569`, `MFR_soviet_collapse_focus_tree`, 58 focuses, max depth 19, average depth 10.5, 12 leaves. It has strong arsenal/factory identity and more direct building effects than CFR, but it is still reward-stack heavy and has the worst mutual-exclusion/pathline geometry in factory successors. It needs a factory gameplay system: quotas, unsafe output, client orders, production missions, templates, artillery/tank line conversion, and route-specific AI.

### Required custom splinters

- PRA: `common/national_focus/005_soviet_collapse_custom_splinters.txt:1221`, 22 focuses, max depth 10, average depth 4.9, 3 leaves. Best small-tree identity: timetable courts, rail guard, corridor network, armored train path, moving state. Still shallow for a rail country; it needs real rail/supply-hub gameplay, corridor decisions, railway denial, armored-train templates/units, and supply-node map play.
- TSC: `common/national_focus/005_soviet_collapse_custom_splinters.txt:1836`, 18 focuses, max depth 8, average depth 4.8, 3 leaves. Observatory/impact-zone identity is present but not enough branch depth. It needs research/radar/air/secret-project mechanics or anomaly decisions, not mostly political+army filters.
- RMC: `common/national_focus/005_soviet_collapse_custom_splinters.txt:2347`, 18 focuses, max depth 8, average depth 4.8, 3 leaves. Martyr/resurrection identity is present, but it lacks the requested dead-congress/zombie-style overpowered aggression. Needs many cores/wargoals/immediate coring/neighbor aggression and death-state recruitment mechanics.
- DSC: `common/national_focus/005_soviet_collapse_custom_splinters.txt:2823`, 18 focuses, max depth 8, average depth 4.8, 3 leaves. It is the most aggressive of the 18-focus set, but that aggression is concentrated into reward-spam focuses (`DSC_revenant_staff_line`, `DSC_claim_the_soldiers_road`, `DSC_congress_of_the_dead_army`) instead of a readable branch. It should become the template for dead-congress military mechanics, but with helper plumbing hidden behind cleaner scripted effects and decision systems.
- NRF: `common/national_focus/005_soviet_collapse_custom_splinters.txt:3414`, 18 focuses, max depth 8, average depth 4.8, 3 leaves. It has correct naval filters and navy XP, but the naval north actor still lacks actual ship/fleet gameplay in focus rewards: no `create_ship` in audited focus rewards. It should get ships, naval invasion/convoy/port defense decisions, dockyards, admirals, and convoy war AI.
- ICD: `common/national_focus/005_soviet_collapse_custom_splinters.txt:3918`, 18 focuses, max depth 8, average depth 4.8, 3 leaves. Identity is distinct from DSC/RMC in text, but mechanically it overlaps: high-chaos identity, custom splinter expansion claims, assault columns, endgame. Needs commissariat-specific conscription, coring, internal security, last-address census, and immediate neighbor aggression.

### Shallow custom splinters outside the named list

- Ancient restorations are the shallowest: `KZR`, `SOG`, `KHW`, and `ALN` each have 16 focuses in `common/national_focus/005_soviet_collapse_ancient_restorations.txt` at lines 12, 422, 826, and 1234. They have symbolic identity and claims, but not enough branch breadth for full political/industry/military/diplomacy/expansion play.
- `OGB_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_factory_successors.txt:1008` has only 23 focuses. It is still closer to a compact side-tree than a full overpowered custom actor.
- Most other custom splinters in `005_soviet_collapse_custom_splinters.txt` have 47 focuses and are less shallow than the 18-focus set, but their repeated template structure should still be reviewed after the named blockers.

## Top idea/reward spam offenders

Direct idea additions in the four audited focus files:
- None. `rg -n "add_ideas|add_timed_idea|swap_ideas|remove_ideas"` returned no matches in the scoped focus files.
- No duplicate direct idea additions were present in audited focus rewards.

Relevant helper idea gates outside the focus files:
- `common/scripted_effects/005_soviet_collapse_effects.txt:11635` `soviet_collapse_ensure_cfr_construction_mandates_idea` gates `cfr_construction_mandates`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:12407` `soviet_collapse_apply_mfr_audit_arsenal_orders` gates `mfr_arsenal_quotas`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:12421` `soviet_collapse_apply_mfr_convert_depots_to_arms_lines` gates `mfr_factory_guard_state`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:8053` `soviet_collapse_update_pra_authority_idea` clears/updates PRA authority ideas.
- `common/scripted_effects/005_soviet_collapse_effects.txt:17640` `soviet_collapse_update_dsc_dead_army_idea` clears old DSC ideas and adds `dsc_dead_army_politics`.

Worst focus reward/plumbing offenders by static score:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2974` `DSC_revenant_staff_line`: 38 reward lines, score 18. Calls `soviet_collapse_apply_focus_high_chaos_identity`, `soviet_collapse_update_dsc_dead_army_idea`, `soviet_collapse_dsc_claim_front_road_states_payload`, `soviet_collapse_dsc_core_controlled_front_road_states_payload`, `soviet_collapse_spawn_custom_splinter_assault_columns_payload`, `soviet_collapse_apply_custom_splinter_expansion_claims_payload`, `soviet_collapse_dsc_launch_dead_army_neighbor_wars_payload`, and `soviet_collapse_apply_objective_source_pressure_delta`; also adds war support, 3 stockpile effects, 2 AI strategies, a variable bump, a tooltip, and a decision unlock. This exposes helper plumbing and compresses too much gameplay into one focus.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3374` `DSC_memorial_frontier_state`: 24 reward lines, score 13. Stacks endgame completion, lawful supply plan, 2 building effects, 2 AI strategies, 2 variables, stability, command power, manpower, and army XP. Should be split into an end-state plus postwar/settlement mechanics.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1696` `PRA_seize_the_junction_cities`: 26 reward lines, score 12. Mixes rail guard spawn, military consolidation, expansion claims, objective pressure, buildings, manpower, equipment, tooltip, and decision unlock. Good identity, but should become rail-corridor seizure decisions and supply-hub play.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3856` `NRF_northern_revenant_fleet`: 25 reward lines, score 11. It has navy XP, wargoal, AI strategies, expansion/spawn/endgame helpers, but no direct ships or fleet construction. Should become a naval branch with ships/dockyards/convoy warfare.
- `common/national_focus/005_soviet_collapse_republics.txt:9812` `blr_soviet_collapse_prepare_league_freight_tables`: 18 reward lines, score 11. It stacks 2 decision unlocks, rail construction helper, rail authority, League preparation, variables, temp variable, and building. This should become a logistics/League freight decision chain.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3514` `NRF_living_harbor_committees`: 17 reward lines, score 11. Stacks 2 buildings, 3 variables, 2 equipment additions, idea cleanup, tooltip, and decision unlock. Should feed harbor committee/naval supply mechanics instead.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3238` `DSC_claim_the_soldiers_road`: 32 reward lines, score 10. Calls claim/core/spawn/neighbor-war payloads and high-chaos helpers. It is exactly the kind of focus that should unlock a dead-army road campaign decision system.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3334` `DSC_congress_of_the_dead_army`: 25 reward lines, score 10. It both creates and declares a war and unlocks two decisions. For a zombie/dead-congress actor this should become a route capstone plus scripted war-plan/neighbor-aggression system, not a one-shot dump.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2847` `MFR_no_peace_without_orders`: 23 reward lines, score 10. It mixes unsafe output, wargoal, AI strategy, war support, equipment, decision unlock, and tooltip. Should become arms-market war economy mechanics.
- `common/national_focus/005_soviet_collapse_republics.txt:1505` `ukr_soviet_collapse_league_founding_charter`, `:1545` `ukr_soviet_collapse_league_of_equals`, and `:1811` `ukr_soviet_collapse_border_states_accept_kyiv`: each sets 5 flags and multiple decision/tooltips in one reward. These are route milestones and should set a single route state plus call a clean scripted effect.

## Exact layout/pathline/mutual-exclusion problems

Provable pathline crossings and line-through-node issues:
- Ukraine:
  - `ukr_soviet_collapse_open_the_liaison_offices -> ukr_soviet_collapse_foreign_advisers_in_plain_coats` line `(31,5) -> (37,7)` passes through `ukr_soviet_collapse_german_liaison_question` at `(34,6)`.
  - Crossings include `ukr_soviet_collapse_question_of_statehood -> ukr_soviet_collapse_foreign_courts_notice_kyiv` `(13,3)->(29,4)` crossing `ukr_soviet_collapse_depot_motor_columns -> ukr_soviet_collapse_arsenal_cities` `(21,3)->(24,6)` and `ukr_soviet_collapse_black_sea_defense_staff -> ukr_soviet_collapse_black_sea_port_ledgers` `(25,3)->(27,5)`.
  - Grain/high-chaos late branch crossings include `ukr_soviet_collapse_no_one_leaves_the_bread_line -> ukr_soviet_collapse_last_harvest_plan` `(36,18)->(36,20)` crossing `ukr_soviet_collapse_black_banner_takes_the_villages -> ukr_soviet_collapse_the_commune_war` `(41,17)->(34,19)`.
- Belarus:
  - `blr_soviet_collapse_timetable_state -> blr_soviet_collapse_league_supply_timetables` `(16,8)->(0,12)` passes through `blr_soviet_collapse_red_without_the_center` `(12,9)` and crosses multiple rail-war links.
  - `blr_soviet_collapse_forest_committees_report_in -> blr_soviet_collapse_which_road_is_belarus` `(20,1)->(16,3)` crosses `blr_soviet_collapse_first_corridor_guard -> blr_soviet_collapse_evacuation_choice` `(16,1)->(23,3)` and `blr_soviet_collapse_the_rail_map_on_the_wall -> blr_soviet_collapse_eastern_line_watch` `(10,1)->(21,3)`.
  - `blr_soviet_collapse_which_road_is_belarus -> blr_soviet_collapse_military_transit_directorate` `(16,3)->(24,6)` crosses `blr_soviet_collapse_eastern_line_watch -> blr_soviet_collapse_orders_printed_like_timetables` `(21,3)->(24,8)`.
- Kazakhstan:
  - `kaz_soviet_collapse_the_congress_chooses_a_past -> kaz_soviet_collapse_a_state_across_distances` `(23,2)->(23,4)` passes through `kaz_soviet_collapse_rail_to_the_mines` `(23,3)`.
  - `kaz_soviet_collapse_the_congress_chooses_a_past -> kaz_soviet_collapse_socialist_steppe_republic` `(23,2)->(27,4)` passes through `kaz_soviet_collapse_alash_memory_restored` `(25,3)`.
  - `kaz_soviet_collapse_rail_to_the_mines -> kaz_soviet_collapse_the_steppe_arsenal` `(23,3)->(23,5)` passes through `kaz_soviet_collapse_a_state_across_distances` `(23,4)`.
  - `kaz_soviet_collapse_alash_memory_restored -> kaz_soviet_collapse_restore_alash_names` `(25,3)->(25,6)` passes through `kaz_soviet_collapse_the_resource_towns_demand_seats` `(25,5)`.
  - `kaz_soviet_collapse_socialist_steppe_republic -> kaz_soviet_collapse_soviets_of_the_steppe` `(27,4)->(31,6)` passes through `kaz_soviet_collapse_aul_councils_and_red_teachers` `(29,5)`.
- PRA:
  - `PRA_omsk_station_guard -> PRA_armored_train_directorate` `(8,1)->(4,5)` crosses `PRA_count_the_locomotives -> PRA_repair_crews_without_ministries` `(6,2)->(10,3)`.
- TSC/RMC/DSC/NRF/ICD repeat the same small-template defect:
  - `TSC_the_committee_of_instruments -> TSC_night_survey_columns` `(2,3)->(6,5)` passes through `TSC_observatory_guard` `(4,4)`.
  - `RMC_communes_of_witnesses -> RMC_hagiographers_of_every_front` `(2,3)->(6,5)` passes through `RMC_reliquary_guard` `(4,4)`.
  - `DSC_witness_officers -> DSC_maps_of_lost_armies` `(2,3)->(6,5)` passes through `DSC_field_hospital_memorials` `(4,4)`.
  - `NRF_living_harbor_committees -> NRF_maps_of_sunken_routes` `(2,3)->(6,5)` passes through `NRF_icebound_marine_guard` `(4,4)`.
  - `ICD_commissars_of_last_addresses -> ICD_archives_of_every_front` `(2,3)->(6,5)` passes through `ICD_funeral_guard` `(4,4)`.
- MFR:
  - `MFR_merchants_of_ammunition -> MFR_officers_chair_the_board` `(24,6)->(2,6)` passes through `MFR_armorers_elect_delegates` `(12,6)`.
  - MFR mutual-exclusion lines cross through the route cluster: `MFR_who_owns_the_rifle -> MFR_eternal_arsenal` `(15,5)->(20,7)` crosses the mutual-exclusion lines among `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, and `MFR_officers_chair_the_board`.
  - `MFR_rifles_before_speeches -> MFR_standardize_the_rifle_line` `(7,9)->(10,10)` crosses three factory-war links from `MFR_factory_war_cabinet`.

Meaningless or weak mutual exclusions:
- The 18-focus custom splinter trees often use two mid-tree route choices and two endpoint route choices, but the endpoints are mostly labels rather than fully different mechanics. Examples: `TSC_starfall_mandate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2264` mutually excludes `TSC_observatory_state`; `NRF_northern_revenant_fleet` at line 3856 mutually excludes `NRF_port_republic_of_the_living`; `ICD_commissariat_without_end` at line 4325 mutually excludes `ICD_citizens_after_death`; `RMC_resurrection_without_state` at line 2763 mutually excludes `RMC_republic_of_witnesses`; `DSC_congress_of_the_dead_army` at line 3334 mutually excludes `DSC_republic_of_roll_calls`.
- MFR has a four-way route split at `MFR_who_owns_the_rifle` with `MFR_officers_chair_the_board` line 1700, `MFR_armorers_elect_delegates` line 1729, `MFR_merchants_of_ammunition` line 1757, and `MFR_eternal_arsenal` line 1788. The split is meaningful in concept, but the geometry is bad and later payoff still overlaps heavily through generic output/security/client arms helpers.

Bad or noisy filter examples:
- `TSC_starfall_mandate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:2264` uses `{ FOCUS_FILTER_POLITICAL FOCUS_FILTER_ARMY_XP FOCUS_FILTER_ANNEXATION }`; for an observatory/impact-zone route it should probably include air/research/special-project or be narrower.
- `NRF_northern_revenant_fleet` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3856` uses `{ FOCUS_FILTER_POLITICAL FOCUS_FILTER_NAVY_XP FOCUS_FILTER_ANNEXATION }`, which is directionally right but hides that the reward lacks direct naval build/ship mechanics.
- `MFR_the_arsenal_state` at `common/national_focus/005_soviet_collapse_factory_successors.txt:2634` uses `{ FOCUS_FILTER_POLITICAL FOCUS_FILTER_INDUSTRY FOCUS_FILTER_ARMY_XP }`; conceptually fine, but it is a symptom of MFR overloading nearly every major focus with all three filters.
- CFR has 34 political and 30 industry filters across 47 focuses, causing the tree to read as one broad political/industry lane rather than separate branch families.

## Focuses where rewards should become mechanics

Priority conversion targets:
- CFR construction directorate:
  - `CFR_rails_first` at `common/national_focus/005_soviet_collapse_factory_successors.txt:329`: convert to rail/supply-hub construction decisions and route-specific AI.
  - `CFR_a_civilian_factory_in_every_capital` at line 515: should be the visible civilian-factory/building-slot expansion engine, not just a flag/helper milestone.
  - `CFR_the_first_new_district` at line 493, `CFR_the_state_that_builds` at line 779, `CFR_rebuild_russia_without_moscow` at line 989: convert to staged construction network, client city, protectorate, and coring/claim settlement mechanics.
- MFR factory successor:
  - `MFR_the_arsenal_state` at line 2634, `MFR_no_peace_without_orders` at line 2847, `MFR_war_market_never_sleeps` at line 2720, `MFR_every_order_a_rifle` at line 2897: convert to production quota missions, arms-client ledger decisions, unsafe output risks, AI factory-target strategy, and equipment/template unlocks.
  - `MFR_repair_the_tank_lines` at line 1988 and `MFR_aircraft_parts_in_secret_workshops` at line 2014: convert to actual armor/air production bonuses, templates, variants, or equipment stockpile mechanics.
- PRA rail country:
  - `PRA_count_the_locomotives` at line 1300, `PRA_armored_train_directorate` at line 1409, `PRA_coal_water_and_spare_parts` at line 1467, `PRA_claim_the_branch_lines` at line 1670, `PRA_rails_over_capitals` at line 1739: convert to railway/supply-node build decisions, armored-train units/templates, route denial, corridor tolls, and rail-coring logic.
- Dead/zombie-style actors:
  - `DSC_revenant_staff_line` at line 2974, `DSC_claim_the_soldiers_road` at line 3238, `DSC_congress_of_the_dead_army` at line 3334: convert to dead-army campaign decisions with immediate coring of controlled road states, recurring neighbor war targets, spawned dead regiments, and route AI.
  - `RMC_resurrection_without_state` at line 2763, `ICD_commissariat_without_end` at line 4325: convert to revival/commissariat mechanics, claims/cores, unit spawns, and permanent aggression.
- Naval north:
  - `NRF_living_harbor_committees` at line 3514, `NRF_revenant_admiralty` at line 3546, `NRF_maps_of_sunken_routes` at line 3693, `NRF_northern_revenant_fleet` at line 3856: convert to direct ships, dockyards, convoy raiding/escort decisions, naval commander/admiralty unlocks, and naval AI strategy.
- TSC observatory:
  - `TSC_the_committee_of_instruments` at line 2004, `TSC_starfall_mandate` at line 2264: convert to radar/air/research/anomaly mechanics, special-project-style decisions, and air/recon AI.
- Ukraine:
  - `ukr_soviet_collapse_league_founding_charter` line 1505, `ukr_soviet_collapse_league_of_equals` line 1545, `ukr_soviet_collapse_border_states_accept_kyiv` line 1811, `ukr_soviet_collapse_league_security_zone_mandates` line 1868: convert the flag clusters into one clean League state plus decision categories for arbitration, security zones, grain relief, arms quotas, and motor/rifle cadre deployment.
- Belarus:
  - `blr_soviet_collapse_prepare_league_freight_tables` line 9812, `blr_soviet_collapse_every_track_through_minsk` line 9971, `blr_soviet_collapse_the_league_depot_at_minsk` line 10129: convert to freight table decisions, railway neutrality, depot seizure, armored train, supply route, and League logistics mechanics.
- Kazakhstan:
  - `kaz_soviet_collapse_the_steppe_arsenal` line 10624, `kaz_soviet_collapse_industrial_settlement_compacts` line 11750, `kaz_soviet_collapse_resource_sovereignty` line 11791, `kaz_soviet_collapse_army_of_the_open_horizon` line 11921, `kaz_soviet_collapse_call_the_steppe_congress` line 11952: convert to resource-town authority, rail-to-mines, Caspian/security detachments, Turkestan federation, and steppe defense decisions.

## Recommended implementation order

1. Fix the worst pathline/layout blockers first in Belarus and Kazakhstan, then Ukraine. These are player-facing and make rework harder to judge.
2. Normalize helper plumbing in DSC and PRA. Replace `_payload` helper calls in focus rewards with clear wrapper scripted effects and move repeatable claims/cores/war/unit work into decisions/missions.
3. Rebuild the 18-focus custom splinters into real overpowered identity trees, in this order: DSC, NRF, PRA, ICD/RMC, TSC. DSC and NRF are highest value because they map directly to user-stated dead-congress and naval-north examples.
4. Upgrade CFR and MFR mechanics. CFR needs visible massive civilian construction/factory expansion; MFR needs production quota/client order/factory gameplay.
5. Convert Ukraine/Belarus/Kazakhstan route milestones into clean mechanics and decision categories rather than dense flag/helper bundles.
6. Audit filters after mechanical rework. Filters should reflect real branch families, not compensate for overloaded rewards.
7. Run localisation audit after each tranche. Current coverage is complete, so future missing keys should be treated as regressions.

## Validation and audit commands used

- `sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md`
- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `sed -n '1,220p' 'paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md'`
- `sed -n '1,180p' 'paradox_wiki/Effect - Hearts of Iron 4 Wiki.md'`
- Core wiki smoke-read loop for Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- `sed -n '1,220p' '/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md'`
- `sed -n '1,180p' '/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md'`
- `sed -n '1,180p' '/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md'`
- `sed -n '1,220p' '/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt'`
- `wc -l common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `rg -n "add_ideas|add_timed_idea|swap_ideas|remove_ideas" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `rg -n "add_ideas|add_timed_idea|swap_ideas|remove_ideas" common/scripted_effects/005_soviet_collapse_effects.txt common/ideas/005* common/ideas/*soviet*`
- Static Python parsers for focus-tree/focus block extraction, branch depth, reward effect counts, helper call counts, direct idea additions, absolute focus coordinates, prerequisite/mutex crossing detection, and Event005 localisation coverage.

## Completion status

Audit complete. No simplifications in scope: all four requested focus files were inspected, all named trees were assessed, localisation coverage was checked across Event005 localisation files, and the requested blockers were reported with exact focus ids and file lines where statically provable.
