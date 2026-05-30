# Event 005 Soviet Collapse Focus Tree Current Audit

Date: 2026-05-30
Mode: focus-tree subagent audit, narrow-patch capable

## Scope

Audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- relevant event 005 specs/plans and `docs/events/005_soviet_collapse.md`

Explicitly not touched:
- `gfx/flags/`
- flag sprite files
- any `.gfx` flag wiring

## Patch Result

No gameplay patch was made. The current focus files did not show a narrow, unambiguous duplicate same-idea grant inside one focus reward, duplicate focus coordinate, or asymmetric mutual exclusion. The remaining layout and branch-depth problems are broad route-reflow and redesign issues, not safe single-focus edits.

Changed files:
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_095509_event005_soviet_collapse_focus_current_audit.md`

Changed focus ids:
- None.

Route behavior before and after:
- Before: current dirty-worktree Event 005 focus trees.
- After: unchanged.

Localisation keys and icon ids changed:
- None.

## Route Coverage Table

| Required route family | Implemented route or focus branch | Status | Evidence and notes |
| --- | --- | --- | --- |
| Ukraine political, industry, military, diplomacy, expansion, League/Bread-State routes | `soviet_collapse_ukraine_focus_tree`, `005_soviet_collapse_republics.txt:18`, 83 focuses, x 4-34, y 0-18 | Partial | Big tree exists, but route readability is poor and pathline scan finds 4 line-through-node risks plus many edge crossings. Needs full reflow around statehood, Black Banner, army, foreign, and Bread-State branches. |
| Generic breakaway republic tree | `soviet_collapse_breakaway_focus_tree`, `005_soviet_collapse_republics.txt:2370`, 36 focuses, x 2-26, y 0-14 | Simplified | Survival/government/league labels exist, but it plays as a compact baseline tree rather than distinct political, industry, military/diplomacy, and expansion mechanics. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, `005_soviet_collapse_republics.txt:3167`, 62 focuses, x 0-27, y 0-10 | Partial | Has regional sub-branches and many state-building rewards, but limited dedicated expansion/diplomacy payoff and several pathline risks. |
| Baltic shared republics | `soviet_collapse_baltic_focus_tree`, `005_soviet_collapse_republics.txt:4671`, 42 focuses, x 2-30, y 0-9 | Partial | Legal continuity, defense, and League concepts exist. Needs stronger route-specific AI, more distinct diplomacy/League mechanics, and line cleanup. |
| Caucasus shared republics | `soviet_collapse_caucasus_focus_tree`, `005_soviet_collapse_republics.txt:5635`, 40 focuses, x 0-26, y 0-8 | Partial | Oil/ports, border faiths, and foreign corridors exist. Needs deeper oilfield, mountain-pass, and compact mechanics. |
| Central Asia shared republics | `soviet_collapse_central_asia_focus_tree`, `005_soviet_collapse_republics.txt:6562`, 45 focuses, x -2-24, y 0-11 | Partial | Basmachi, cotton, water/rail, and southern shield ideas exist, but still too compressed for the required distinct route families. |
| Moldova | `soviet_collapse_moldova_focus_tree`, `005_soviet_collapse_republics.txt:7707`, 48 focuses, x 2-26, y 0-13 | Partial, layout risk | Dniester, Prut/Romania, Ukraine, and river-state branches exist. Layout scan finds line-through-node risks and heavy crossing clusters. |
| Belarus | `soviet_collapse_belarus_focus_tree`, `005_soviet_collapse_republics.txt:8868`, 53 focuses, x 3-28, y 0-16 | Partial | National council/socialist/transit/foreign paths exist. Corridor, forest, rail, and League branches need stronger mechanics and cleaner line paths. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`, `005_soviet_collapse_republics.txt:10199`, 92 focuses, x 2-35, y 0-12 | Partial, major layout risk | Largest republic tree. Route concepts exist, but scan finds 13 line-through-node risks. Needs broad reflow and clearer Alash/socialist/resource/southern-route payoffs. |
| Full custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` in `005_soviet_collapse_custom_splinters.txt` | Partial | Most are 47-focus templates with country-specific text but many cloned route skeletons. They need OP/specialized country mechanics rather than mostly shared helper rewards. |
| Crisis/special splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` in `005_soviet_collapse_custom_splinters.txt` | Mixed, too short | `PRA`, `DSC`, and `NRF` have stronger hooks than most, but 18-22 focuses is still shallow for campaign-defining chaos actors unless explicitly classified as compact crisis trees. |
| Factory successors | `CFR`, `MFR`, `OGB` in `005_soviet_collapse_factory_successors.txt` | Mixed | `CFR` and `MFR` have larger branch maps. `OGB_soviet_collapse_focus_tree`, `005_soviet_collapse_factory_successors.txt:1171`, 23 focuses, remains shallow for an OP restoration/high-chaos successor. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` in `005_soviet_collapse_ancient_restorations.txt` | Simplified | Each has 16 focuses. They include claims and decision hooks but not enough depth for distinct political, industrial, military/diplomacy, and expansion/mechanic branches. |

## Idea Spam and Repeated Idea Grants

Direct focus reward scan:
- 0 direct `add_ideas` in the four focus files.
- 0 direct `add_timed_idea` in the four focus files.
- 0 exact repeated same-idea grants inside one focus reward after expanding focus-called helpers.

Focus-called helpers that grant ideas:

| Helper id | Definition | Focus calls | Idea evidence | Audit note |
| --- | --- | ---: | --- | --- |
| `soviet_collapse_apply_custom_splinter_doctrine_identity` | `common/scripted_effects/005_soviet_collapse_effects.txt:13112` | 19 | Conditional tag-specific ideas from `fth_internal_factions` at `:13117` through `nlc_scientific_refuge_council` at `:13299` | Each idea is gated by tag and `NOT = { has_idea = ... }`; not an exact duplicate, but this is still one shared doctrine idea-adder across 19 trees. |
| `soviet_collapse_complete_pale_railway_endgame` | `005_soviet_collapse_effects.txt:14721` | 2 | `pra_moving_state_authority` at `:14726`; called by `PRA_rails_over_capitals`, `005_soviet_collapse_custom_splinters.txt:1746`, and `PRA_the_pale_line_endures`, `:1794` | Helper has a country flag guard. The two focus endpoints are mutually exclusive, so no narrow duplicate patch was made. |
| `soviet_collapse_complete_tunguska_star_endgame` | `005_soviet_collapse_effects.txt:14735` | 2 | `tsc_starfall_mandate` at `:14740`; called by `TSC_starfall_mandate`, `:2236`, and `TSC_the_quiet_sky_settlement`, `:2278` | Guarded by `soviet_collapse_tunguska_star_endgame`; no exact duplicate in one path. |
| `soviet_collapse_complete_red_martyrs_endgame` | `005_soviet_collapse_effects.txt:14770` | 2 | `rmc_resurrection_militias` at `:14775`; called by `RMC_resurrection_without_state`, `:2742`, and `RMC_shrine_state`, `:2761` | Guarded and route-separated. |
| `soviet_collapse_complete_dead_soldiers_endgame` | `005_soviet_collapse_effects.txt:14787` | 2 | `dsc_dead_army_politics` at `:14792`; called by `DSC_congress_of_the_dead_army`, `:3321`, and `DSC_memorial_frontier_state`, `:3340` | Guarded and route-separated. |
| `soviet_collapse_complete_northern_revenant_endgame` | `005_soviet_collapse_effects.txt:14824` | 2 | `nrf_fleet_that_does_not_dock` at `:14829`; called by `NRF_northern_revenant_fleet`, `:3843`, and `NRF_memorial_convoy_state`, `:3862` | Guarded and route-separated. |
| `soviet_collapse_complete_iron_commissariat_endgame` | `005_soviet_collapse_effects.txt:14753` | 2 | `icd_citizens_after_death` at `:14758`; called by `ICD_commissariat_without_end`, `:4316`, and `ICD_state_of_last_addresses`, `:4335` | Guarded and route-separated. |
| `soviet_collapse_complete_northern_lights_endgame` | `005_soviet_collapse_effects.txt:14815` | 2 | `nlc_world_after_capitals` at `:14820`; called by `NLC_polar_commune_endurance`, `:25472`, and `NLC_extreme_path`, `:25634` | Guarded and mutually exclusive. |
| Single-call endgame helpers | `005_soviet_collapse_effects.txt:14437-14812` | 1 each | `krs_every_port_a_council`, `bsc_road_beyond_the_steppe`, `tnc_new_turkestan`, `ala_national_modernization`, `udc_purified_union_command`, `sdz_world_in_one_archive`, `gac_land_and_bread_against_the_world`, `dhc_southern_host_command`, `khc_kuban_line_command`, `fev_far_eastern_line_command`, `sza_siberian_depth_command`, `uwd_arsenal_autonomy_directorate`, `mrc_mountain_republic_mandate`, `iul_federal_corridor_authority`, `ogb_restored_volga_empire`, `bac_autonomous_commune_mandate`, `ard_port_neutrality_mandate` | These are not repeated by focus call count, but they confirm that visible idea payoff remains concentrated in helper-led endgame/doctrine effects. |

Issue conclusion:
- The exact "same focus gives the same idea multiple times" class was not present in the current four focus files or their focus-called helper expansion.
- The broader complaint remains valid as a design issue: many trees still depend on helper-led national-spirit payoffs instead of route-specific decisions, units, claims, cores, war goals, factory systems, League mechanics, or AI strategy. This needs a full route reward pass, not a narrow duplicate deletion.

## Structural Layout Audit

Mechanical layout scan:
- Focus blocks parsed: 1,698.
- Focus trees parsed: 41.
- Duplicate focus ids: 0.
- Duplicate coordinates within the same tree: 0.
- Too-close sibling pairs with same parent/same row and x distance under 2: 0.
- Asymmetric mutual exclusions: 0.
- Third focus placed between same-row mutually exclusive endpoints: 0.
- Continuous focus panel positions: all inspected trees set x positions at 1536 or higher; no obvious panel overlap at x < 1000.

Line-through-node risks, exact examples:

| Tree | Prerequisite line | Parent x/y | Child x/y | Intervening focus x/y | Evidence |
| --- | --- | --- | --- | --- | --- |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_question_of_statehood` to `ukr_soviet_collapse_black_banner_compact` | 13/3 | 30/7 | `ukr_soviet_collapse_direct_national_claims` 26/6 | `005_soviet_collapse_republics.txt:273`, intervening focus at `:1763` |
| `soviet_collapse_ukraine_focus_tree` | `ukr_soviet_collapse_army_of_the_republic` to `ukr_soviet_collapse_general_staff_war_college` | 25/4 | 30/6 | `ukr_soviet_collapse_open_the_liaison_offices` 27/5 | `005_soviet_collapse_republics.txt:615`, intervening focus at `:205` |
| `soviet_collapse_breakaway_focus_tree` | `soviet_collapse_assemble_emergency_government` to `soviet_collapse_factory_defense_committees` | 14/0 | 24/1 | `soviet_collapse_secure_ministry_ledgers` 22/1 | `005_soviet_collapse_republics.txt:2436`, intervening focus at `:2416` |
| `soviet_collapse_baltic_focus_tree` | `baltic_soviet_collapse_forest_and_marsh_lines` to `baltic_soviet_collapse_estonian_forest_coast_guard` | 6/2 | 5/8 | `baltic_soviet_collapse_radio_appeals_to_the_north` 6/3 | `005_soviet_collapse_republics.txt:5504`, intervening focus at `:4764` |
| `soviet_collapse_caucasus_focus_tree` | `caucasus_soviet_collapse_protect_the_oil_and_ports` to `caucasus_soviet_collapse_oil_emergency_directorate` | 2/1 | 14/2 | `caucasus_soviet_collapse_the_border_faiths_and_nations` 4/1 | `005_soviet_collapse_republics.txt:5749`, intervening focus at `:5702` |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_alash_memory_restored` to `kaz_soviet_collapse_the_alash_courts` | 35/3 | 22/4 | `kaz_soviet_collapse_lone_steppe_state` 24/4 | `005_soviet_collapse_republics.txt:10455`, intervening focus at `:10933` |
| `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_the_army_that_crosses_distance` to `kaz_soviet_collapse_steppe_federation_charter` | 2/3 | 19/5 | `kaz_soviet_collapse_no_steppe_without_the_south` 10/4; `kaz_soviet_collapse_border_cavalry_schools` 12/4 | `005_soviet_collapse_republics.txt:10882`, intervening focuses at `:11235` and `:11257` |
| `DHC_soviet_collapse_focus_tree` | `DHC_hardline_against_commissars` to `DHC_river_and_steppe_compact` | 2/9 | 12/10 | `DHC_hidden_doctrine` 4/9 | `005_soviet_collapse_custom_splinters.txt:14795`, intervening focus at `:14855` |
| `KHC_soviet_collapse_focus_tree` | `KHC_hardline_against_requisition` to `KHC_steppe_and_mountain_compact` | 2/9 | 12/10 | `KHC_hidden_doctrine` 4/9 | `005_soviet_collapse_custom_splinters.txt:15991`, intervening focus at `:16049` |
| `MFR_soviet_collapse_focus_tree` | `MFR_rifles_against_the_league` to `MFR_german_orders` | 26/8 | 24/10 | `MFR_rifles_for_the_league` 25/9 | `005_soviet_collapse_factory_successors.txt:2472`, intervening focus at `:2411` |

Other exact line-through-node risks found by parser:
- `internal_soviet_collapse_yakut_lena_resource_board` to `internal_soviet_collapse_yakut_aldan_convoy_roads` crosses `internal_soviet_collapse_baikal_pass_fortresses`, `005_soviet_collapse_republics.txt:4220` and `:4375`.
- `moldova_soviet_collapse_bessarabian_legal_files` to `moldova_soviet_collapse_independent_republic_council` crosses `moldova_soviet_collapse_chisinau_radio_watch`, `005_soviet_collapse_republics.txt:7844` and `:8243`.
- `kaz_soviet_collapse_oil_field_protection_orders` to `kaz_soviet_collapse_emergency_oil_boards` crosses `kaz_soviet_collapse_resource_concessions_debate`, `kaz_soviet_collapse_foreign_trucks_local_drivers`, and `kaz_soviet_collapse_rail_guard_brigades`, `005_soviet_collapse_republics.txt:11730`, `:10561`, `:11299`, `:11891`.
- `UWD_propaganda` to `UWD_settlement` crosses `UWD_rail_yard_repair_trust`, `005_soviet_collapse_custom_splinters.txt:19022` and `:19203`.
- `BAC_war_plan` to `BAC_militia_training_yards` crosses `BAC_industry_plan`, `005_soviet_collapse_custom_splinters.txt:22737` and `:22525`.

This is not a safe "move one focus" issue. The worst trees have dense route webs where moving one focus risks creating new crossings or breaking branch readability.

## Icon Coverage Table

| File | Focuses | Missing `icon =` | Unique icon ids | Repeated icon ids | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 436 | 22 | Repeats remain in shared/generic icon families; spec asks every focus to have a unique icon assignment. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 786 | 99 | Template-driven custom splinters still repeat many icon ids. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 102 | 11 | Factory successors still repeat construction/arsenal icon ids. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 36 | 8 | Ancient restorations share many restoration icon ids. |

Sprite-definition scan from prior current-state audit found 0 missing assigned sprite definitions across `interface/005_soviet_collapse*.gfx`; I did not touch `.gfx` or flag files in this pass.

## Localisation and Reward Mismatch List

Mechanical localisation:
- No missing focus title keys were found in the latest current-state audit.
- No missing focus `_desc` keys were found in the latest current-state audit.

Reward or title mismatch examples needing parent follow-up:
- `OGB_kazan_ferry_offices`, `005_soviet_collapse_factory_successors.txt:1321`: named Kazan ferry focus gives random owned/core factory-style construction instead of targeted Kazan/Volga ferry-office mechanics.
- `PRA_claim_the_branch_lines`, `005_soviet_collapse_custom_splinters.txt:1656`: title implies territorial/rail claims; focus lacks `FOCUS_FILTER_ANNEXATION` and should make the rail-junction claim mechanics visible.
- `TSC_claim_the_impact_zone`, `005_soviet_collapse_custom_splinters.txt:2156`: title implies territorial claims; payoff appears delayed to later route/endgame effects.
- Ancient charter focuses `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, and `ALN_alan_pass_charter`: localisation implies foundational restoration politics, but each tree has only 16 focuses and compact rewards.

## Missing or Simplified Content

High-priority broad gaps:
- Shallow ancient restorations: `KZR`, `SOG`, `KHW`, and `ALN` need full political, industry, military/diplomacy, and expansion/mechanic branches or explicit design approval as compact side trees.
- Shallow crisis/high-chaos trees: `TSC`, `RMC`, `ICD`, `NRF`, `DSC`, and `PRA` need deeper special mechanics if they are meant to be long-lived campaign actors.
- `OGB_soviet_collapse_focus_tree` remains too shallow at 23 focuses for an OP restored Volga/old-name successor.
- Full custom splinters still look template-derived in reward structure. Country-specific localisation exists, but the branch mechanics need more local claims, cores, war goals, unit templates, factories, route decisions, and AI strategies.
- Republic trees have the branch labels, but several routes still resolve through shared variable/helper rewards rather than unique route systems.

## AI Behavior Gaps

Current broad behavior:
- Ukraine, Belarus, and Kazakhstan have route-aware AI work compared with other republics.
- High-chaos/special actors have some direct `add_ai_strategy` in endpoint helpers and focus rewards, especially `PRA`, `DSC`, `NRF`, `CFR`, `OGB`, and some endgame helpers.

Remaining gaps:
- Baltic, Caucasus, Central Asia, Moldova, generic breakaway, and internal republic trees need route-specific AI strategy families.
- Most 47-focus custom splinters need AI preferences for political route, industry route, diplomacy route, hidden doctrine/extreme route, and expansion timing.
- Chaos countries are not consistently "extremely overpowered and aggressive." Some endpoints grant strong war goals/AI conquer strategy, but many trees still spend most of their branch depth on generic state rewards, convoy/equipment rewards, or shared helper variables.

## High-Priority Fixes First

1. Full route reflow for Ukraine, Kazakhstan, Moldova, and Belarus before more small pathline patches. These trees have the highest layout risk and user-visible pathline problems.
2. Route reward pass for custom splinters, starting with `TSC`, `RMC`, `ICD`, `NRF`, `PRA`, `DSC`, `OGB`, then the 47-focus templates.
3. Ancient restoration expansion plan for `KZR`, `SOG`, `KHW`, and `ALN`.
4. Replace repeated helper-variable rewards with concrete route mechanics: decision unlocks, route-specific units, state-targeted construction, claims/cores, war goals, factory/rail/port programs, and postwar settlement.
5. Add route-aware AI strategy families outside Ukraine/Belarus/Kazakhstan.
6. Unique focus icon assignment pass after route shapes stabilize; do not edit flags or flag sprites as part of this focus pass.

## Validation Run

Run from `/home/klim/projects/chaos_redux` after writing this handoff:

| Check | Result |
| --- | --- |
| Brace balance on `005_soviet_collapse_republics.txt` | `final_depth=0 min_depth=0` |
| Brace balance on `005_soviet_collapse_custom_splinters.txt` | `final_depth=0 min_depth=0` |
| Brace balance on `005_soviet_collapse_factory_successors.txt` | `final_depth=0 min_depth=0` |
| Brace balance on `005_soviet_collapse_ancient_restorations.txt` | `final_depth=0 min_depth=0` |
| Duplicate focus id scan | `focus_count=1698`, `duplicate_focus_ids=0` |
| Duplicate coordinate scan | `duplicate_coordinate_groups=0` |
| Asymmetric mutual exclusion scan | `asymmetric_mutual_exclusions=0` |
| Direct focus `add_ideas` scan | `direct_add_ideas_focuses=0` |
| Direct repeated same-idea scan | `direct_repeated_same_idea_focuses=0` |
| Focus plus helper repeated same-idea expansion scan | `focuses_with_direct_or_helper_add_ideas=52`, `expanded_repeated_same_idea_focuses=0` |
| `git diff --check` | Passed with no output |

## Skipped Validation

- In-game validation was not run.
- Focus-tree screenshot validation was not run.
- No `.gfx`, flag, or flag sprite validation was run because those files are out of scope.

## Remaining Route Risks

- Current audit is parser-based plus targeted manual inspection. It proves the main mechanical classes above, but it does not replace in-game focus-tree screenshot inspection.
- The worktree was already dirty before this audit. I did not revert or normalize existing edits.
- No broad redesign was attempted. The user complaint about shallow/random branch purpose remains open.

## Plan Handoff Path

Existing broad plan remains applicable:
- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`

This file is the current audit handoff for the parent agent:
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_095509_event005_soviet_collapse_focus_current_audit.md`
