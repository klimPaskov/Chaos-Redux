# Event005 Soviet Collapse Focus Tree Audit Handoff

Audit role: `chaosx_focus_tree_auditor`  
Timestamp: 2026-06-05 06:13 UTC  
Scope: Event005 Soviet Collapse focus trees plus directly referenced reward helpers, ideas, and decisions for evidence.  
Patch status: no gameplay patch made. The working tree was already dirty across the audited files, so I kept this pass to evidence and parent patch planning.

## References Consulted

- Repo skill: `hoi4-focus-trees`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`
- Vanilla precedent: `common/national_focus/generic.txt` for prerequisite OR/AND patterns, `relative_position_id`, mutual exclusions, `ai_will_do`, focus reward ideas, and branch spacing

## Current Tree Shape

Parsed 41 focus trees and 1,698 focuses across the four requested focus files. Brace balance is clean in the audited Clausewitz files.

Major/deeper republic trees:

- `soviet_collapse_ukraine_focus_tree`: 83 focuses, x 4..41, y 0..20, continuous panel at `x = 4416 y = 180`.
- `soviet_collapse_kazakhstan_focus_tree`: 92 focuses, x 2..33, y 0..12.
- Belarus, Moldova, internal republic, Baltic, Caucasus, Central Asia trees sit in the 40-62 focus range and have political, military, industry, and diplomacy surfaces.

Custom splinters:

- Most custom splinters are 47-focus packages with political, industry, military, foreign/league, special-route, and endgame lanes.
- Compact fixed-purpose splinters are smaller: `TSC`, `RMC`, `DSC`, `NRF`, `ICD` are 18 focuses each. They have identity payoffs, but only one short political spine and limited diplomacy/industry depth.
- `PRA` is 22 focuses and now has strong railway-specific identity, rail/supply rewards, rail guard columns, and authority idea handling, but it still leans on repeated generic helper stacks.

Factory and ancient successors:

- `CFR` has 47 focuses and a construction-directorate identity, but its direct visible map reward count is low in the focus file because most output is hidden in helpers.
- `MFR` has 58 focuses and a strong factory/arsenal identity with industry, military, market, foreign, and expansion lanes.
- `OGB` has 23 focuses and is moderate depth.
- `KZR`, `SOG`, `KHW`, `ALN` have 16 focuses each. They cover symbolic politics, industry/support, expansion, claims/wargoals, and endgame, but they remain shallow compared with the requested "real depth" standard.

## Worst Idea And Helper Spam

Direct duplicate `add_ideas` inside a single focus reward: none found.

Same visible idea added multiple times without an in-helper guard: none found in the parsed focus rewards.

Worst repeated visible-idea helper:

- `PRA_the_timetable_declares_authority` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1227`
- `PRA_armored_train_directorate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1403`
- `PRA_passport_of_the_moving_state` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1572`
- `PRA_league_transit_bargain` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1638`

These all call `soviet_collapse_update_pra_authority_idea`. The helper at `common/scripted_effects/005_soviet_collapse_effects.txt:7956` clears one of four visible PRA authority ideas and adds a replacement: `pra_moving_state_authority`, `pra_corridor_toll_authority`, `pra_railway_guard`, or `pra_timetable_sovereignty_board`. This is guarded and does not stack multiple visible spirits, but the player-facing reward shape is still "focus updates the authority spirit again" rather than distinct gameplay in multiple focuses.

Worst generic helper/reward clutter examples:

- `moldova_soviet_collapse_romanian_aid_without_annexation` at `common/national_focus/005_soviet_collapse_republics.txt:7881`: five direct helper calls in one reward.
- `blr_soviet_collapse_military_transit_directorate` at `common/national_focus/005_soviet_collapse_republics.txt:9005`: four direct helpers, including unit-template/deployment unlock and neighbor conflict plan.
- `PRA_armored_train_directorate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1403`: four direct helpers plus authority idea update.
- `PRA_seize_the_junction_cities` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1689`: four direct helpers including expansion claims and pressure delta.
- `DSC_grave_ordnance_claims` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3002`: five direct helpers, several aggressive/core/claim payloads.
- `DSC_claim_the_soldiers_road` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:3210`: five direct helpers, same issue.
- `NLC_extreme_gate` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:25525`: four direct helpers.
- Ancient expansion/endgame focuses such as `KZR_expansionist_steppe_levy`, `KZR_road_beyond_the_caspian`, `SOG_expansionist_merchant_claims`, `KHW_expansionist_water_claims`, and `ALN_every_pass_a_border` each call four generic aggressive helpers.

These are not necessarily broken, but they are the reward clutter hotspots. Parent should collapse generic tooltip output behind a route-specific wrapper per family, so the player sees one country-specific payoff and the implementation still reuses helper internals.

## Branch Depth Findings

- Ukraine: real depth exists. It has political routes, military, foreign/league, industry/grain, Black Sea, direct national claims, and high-chaos/commune material. The main problem is not depth; it is messy cross-branch routing and too-wide layout.
- Kazakhstan: real depth exists and is probably the strongest republic tree by focus count and branch variety. It still has several long cross-tree lines in the Alash/resource/southern-republic areas.
- Belarus: identity is now railway/corridor-heavy and meaningfully connected to decisions and rail rewards. Remaining issue is layout, especially long rail/foreign/depot crosslinks.
- Moldova/Central Asia/Baltic/Caucasus/internal republic: generally have political, industry, military, diplomacy, and expansion surfaces, but a few branches are still payoff-light and resolve through generic helper stacks rather than bespoke country mechanics.
- Generic `soviet_collapse_breakaway_focus_tree`: usable moderate tree, but still mostly a generic fallback package. It should not be treated as fully equivalent to bespoke country trees.
- `PRA`: country-specific railway logic is present and strong: rail authority, rolling stock, rail/supply construction, rail guard columns, and rail decisions. Needs less repeated authority-idea presentation.
- `DSC`: aggressive/death-state logic exists: war goals, claims/cores, manpower and high-chaos helper payloads. This meets the intended direction, but the 18-focus tree has limited non-expansion depth.
- `NRF`: naval identity exists via navy filters, convoys/dockyards, and port rewards. Still shallow at 18 focuses.
- `CFR`: construction directorate identity is clear, but direct focus rewards hide too much behind helpers. Parent should expose construction power more concretely in the focus rewards/tooltips.
- `MFR`: factory successor depth is strong and more robust than `CFR`.
- Ancient restorations: all four have a clear symbolic/expansion path and claims/wargoals, but 16 focuses each is not enough for full political/industrial/expansion/military/diplomacy depth.

## Layout And Pathline Findings

Ukraine:

- Continuous focus panel is probably not covering the current tree: max focus x is 41, panel starts at 4416 px, about x 46 in focus-coordinate terms. This leaves a visible buffer.
- The tree is still very wide, x 4..41, and has many long pathlines.
- `ukr_soviet_collapse_appointed_governors` `(15,14)` requires both `ukr_soviet_collapse_provincial_governors_or_elected_radas` `(15,12)` and `ukr_soviet_collapse_the_ukrainian_commune_debate` `(17,13)`. This visually and logically ties democratic provincial governance to the socialist commune line.
- `ukr_soviet_collapse_officers_above_parties` `(22,5)` from `ukr_soviet_collapse_question_of_statehood` `(13,3)` creates a dx 9 pathline.
- `ukr_soviet_collapse_dnieper_workshops` `(7,3)` from `ukr_soviet_collapse_seal_the_grain_ledgers` `(15,1)` creates a dx -8 line.
- `ukr_soviet_collapse_black_sea_defense_staff` `(25,3)` from `ukr_soviet_collapse_moscows_officers_in_our_barracks` `(17,2)` creates a dx 8 line.
- `ukr_soviet_collapse_the_commune_war` `(34,19)` from `ukr_soviet_collapse_black_banner_takes_the_villages` `(41,16)` creates a dx -7 line late in the tree.
- `ukr_soviet_collapse_foreign_advisers_in_plain_coats` at line 1046 is top-level but has over-indented `focus = {` and inner fields. This is cosmetic but worth cleaning while touching the Ukraine layout.

Other high-priority pathlines:

- `caucasus_soviet_collapse_oil_emergency_directorate` `(14,2)` from `caucasus_soviet_collapse_protect_the_oil_and_ports` `(2,1)`, dx 12.
- `caucasus_soviet_collapse_baku_oilfield_guard` `(24,4)` from `caucasus_soviet_collapse_pipeline_guard_corps` `(12,3)`, dx 12.
- `blr_soviet_collapse_eastern_line_watch` `(21,3)` from `blr_soviet_collapse_the_rail_map_on_the_wall` `(10,1)`, dx 11.
- `blr_soviet_collapse_foreign_corridor_administration` `(26,6)` from `blr_soviet_collapse_which_road_is_belarus` `(16,3)`, dx 10.
- `blr_soviet_collapse_timetable_state` `(16,8)` from `blr_soviet_collapse_eastern_line_watch` `(21,3)`, dy 5.
- `blr_soviet_collapse_minsk_central_dispatch` `(7,9)` from `blr_soviet_collapse_timetable_state` `(16,8)`, dx -9.
- `moldova_soviet_collapse_the_river_state` `(18,14)` from `moldova_soviet_collapse_ukrainian_grain_road` `(15,5)`, dy 9.
- `moldova_soviet_collapse_republic_of_crossings` `(21,12)` from `moldova_soviet_collapse_league_observer_table` `(24,5)`, dy 7.
- `kaz_soviet_collapse_the_steppe_keeps_many_memories` `(32,8)` from `kaz_soviet_collapse_the_alash_courts` `(22,4)`, dx 10 dy 4.
- `kaz_soviet_collapse_emergency_oil_boards` `(10,8)` from `kaz_soviet_collapse_oil_field_protection_orders` `(19,3)`, dx -9 dy 5.
- `kaz_soviet_collapse_industrial_settlement_compacts` `(22,10)` from `kaz_soviet_collapse_emergency_oil_boards` `(10,8)`, dx 12.
- `kaz_soviet_collapse_tajik_pass_agreements` `(21,8)` from `kaz_soviet_collapse_call_the_steppe_congress` `(9,6)`, dx 12.
- `CFR_the_concrete_committee` `(27,6)` from `CFR_the_unfinished_city_speaks` `(17,4)`, dx 10.
- `CFR_the_debt_map` `(23,12)` from `CFR_the_concrete_republic` `(31,7)`, dx -8 dy 5.
- `MFR_officers_chair_the_board` `(2,6)` from `MFR_who_owns_the_rifle` `(15,5)`, dx -13.
- `MFR_artillery_from_broken_foundries` `(4,10)` from `MFR_factory_war_cabinet` `(13,8)`, dx -9.
- `UWD_kama_foundry_contracts` `(3,8)` from `UWD_workers_canteen_compact` `(16,7)`, dx -13.
- `FEV_endgame`, `SZA_endgame`, `BAC_endgame`, and `ARD_endgame` each have multiple long converging prerequisites and likely produce line clutter.

Too-close same-row pairs to review:

- Internal tree: `internal_soviet_collapse_crimean_tatar_councils` `(20,5)` and `internal_soviet_collapse_taiga_steppe_self_rule` `(21,5)`.
- Central Asia: `central_asia_soviet_collapse_desert_scout_columns` `(7,6)` and `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` `(6,6)`; `central_asia_soviet_collapse_bishkek_pass_council` `(8,8)` and `central_asia_soviet_collapse_khwarazm_restoration_debate` `(9,8)`; `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` `(4,4)` and `central_asia_soviet_collapse_the_cotton_question` `(3,4)`.
- Moldova: `moldova_soviet_collapse_river_guard_brigades` `(14,5)` and `moldova_soviet_collapse_ukrainian_grain_road` `(15,5)`; `moldova_soviet_collapse_reject_the_union_question` `(15,7)` and `moldova_soviet_collapse_tiraspol_depot_belt` `(14,7)`.
- Belarus: `blr_soviet_collapse_council_bargains_with_forests` `(6,7)` and `blr_soviet_collapse_railway_guard_regiments` `(5,7)`; `blr_soviet_collapse_orders_printed_like_timetables` `(24,8)` and `blr_soviet_collapse_the_green_rail_pact` `(23,8)`; `blr_soviet_collapse_liaison_hotels` `(25,7)` and `blr_soviet_collapse_village_warning_bells` `(26,7)`.
- Kazakhstan: five same-row adjacent pairs around the Alash/resource/league lanes, including `kaz_soviet_collapse_league_resource_pool` `(23,8)` and `kaz_soviet_collapse_local_notable_compacts` `(24,8)`.

## Prioritized Parent Patch Plan

1. Ukraine layout cleanup first. Keep the continuous panel position unless visual testing proves overlap, but reduce the x 4..41 spread. Split the military/foreign/Black Sea right wing into closer vertical lanes and remove the cross-route prerequisite from `ukr_soviet_collapse_appointed_governors` unless there is a design reason for democratic governance to require the socialist commune debate.
2. Replace direct generic-helper stacks with route-specific wrapper helpers and route-specific tooltips. Start with `moldova_soviet_collapse_romanian_aid_without_annexation`, `blr_soviet_collapse_military_transit_directorate`, `PRA_armored_train_directorate`, `PRA_seize_the_junction_cities`, `DSC_grave_ordnance_claims`, `DSC_claim_the_soldiers_road`, and the ancient expansion/endgame focuses.
3. For `PRA`, keep the single-authority-idea lifecycle, but make later focus rewards visibly about rail corridors, supply hubs, rail guard columns, transit decisions, and war/claim behavior. Avoid presenting repeated "authority spirit updated" as the main reward.
4. Expand or explicitly classify the 16-18 focus fixed-purpose trees. `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, and the ancient restoration trees should each either gain deeper political/industry/diplomacy/special mechanics or be documented as compact fixed-purpose packages with deliberately narrow scope.
5. Patch the worst non-Ukraine long pathlines: Caucasus oil, Belarus rail/corridor, Moldova river-state, Kazakhstan Alash/resource/southern lines, CFR/MFR factory successor crosslines, and FEV/SZA/BAC/ARD endgame convergence.
6. Re-run a focus-layout audit after every layout tranche. Long edges are not automatically wrong, but the current density means pathlines will plausibly cross unrelated branches.

## Validation

- Brace balance passed on all seven audited Clausewitz files:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/ideas/005_soviet_collapse_ideas.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
- `rg -n "<=|>="` returned no hits in the seven audited Clausewitz files.

No flags were edited.
