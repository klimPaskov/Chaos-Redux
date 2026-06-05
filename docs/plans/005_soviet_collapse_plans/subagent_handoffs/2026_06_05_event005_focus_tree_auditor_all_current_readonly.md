# Event005 Soviet Collapse Focus Tree Audit Handoff

Date: 2026-06-05

Subagent role: `chaosx_focus_tree_auditor` style audit using `hoi4-focus-trees` and `hoi4-decisions-missions` guidance.

Scope: read-only audit of Event005 Soviet Collapse focus trees in:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- related scripted effects, scripted triggers, decisions, ideas, and localisation where focus rewards point to them

No focus, localisation, gfx, flag, or binary asset files were patched. This handoff is the only file produced by this pass.

## Required Reference Checks

Consulted required offline wiki snapshot pages before reading Chaos Redux files:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`

Consulted vanilla docs and references:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- Vanilla focus files under `~/projects/Hearts of Iron IV/common/national_focus/`

Key syntax/reference reminders used in this audit:

- A single `prerequisite = { focus = a focus = b }` is OR.
- Multiple `prerequisite = { ... }` blocks are AND.
- Prerequisite parents should be above children for readable path generation.
- `country = { ... }` and `ai_will_do = { ... }` are MTTH-style blocks.
- `relative_position_id` is preferred for branch maintenance, but no Event005 audited focus currently uses it.

## Current Status

Mechanical inventory found 41 Event005 focus trees and 1,698 focus blocks across the four audited files.

No duplicate focus IDs were found in the audited files.

Tree inventory:

| Tree | File lines | Focus count | Status |
| --- | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | republics 18-2343 | 83 | Deep, has political/industry/expansion/League/high-chaos material; layout blockers remain. |
| `soviet_collapse_breakaway_focus_tree` | republics 2345-3155 | 36 | Shared generic breakaway tree; structurally useful but route identity remains broad/generic. |
| `soviet_collapse_internal_republic_focus_tree` | republics 3157-4675 | 62 | Broad shared internal tree; has duplicate coordinate issue and many hidden gates. |
| `soviet_collapse_baltic_focus_tree` | republics 4677-5638 | 42 | Distinct regional lanes; no direct expansion claims/wargoals in focus file. |
| `soviet_collapse_caucasus_focus_tree` | republics 5640-6559 | 40 | Has branch families; one duplicate coordinate issue. |
| `soviet_collapse_central_asia_focus_tree` | republics 6561-7695 | 45 | Has branch families and one direct claim focus; many hidden gates. |
| `soviet_collapse_moldova_focus_tree` | republics 7697-8837 | 48 | Has route families; no direct claims/wargoals/cores in focus file. |
| `soviet_collapse_belarus_focus_tree` | republics 8839-10157 | 53 | Priority tree; strong rail/forest/diplomacy identity, but has coordinate overlap and hidden-gate pathline risks. |
| `soviet_collapse_kazakhstan_focus_tree` | republics 10159-12223 | 92 | Priority tree; deepest tree, but high coordinate/pathline debt and many flat AI weights. |
| `FTH_soviet_collapse_focus_tree` | custom 15-1379 | 47 | Better custom splinter depth; still uses shared tooltip/helper families heavily. |
| `PRA_soviet_collapse_focus_tree` | custom 1381-2019 | 22 | Compact but mechanically connected with many decisions; needs layout risk review. |
| `TSC/RMC/DSC/NRF/ICD_soviet_collapse_focus_tree` | custom 2021-4523 | 18 each | Shallow compact high-chaos/special trees; direct wargoal exists, but branch depth is thin. |
| `BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC_soviet_collapse_focus_tree` | custom 4525-25768 | 47 each | Most have political, logistics, war, diplomacy, industry, expansion, hidden doctrine, and high-chaos lanes; repeated shared reward tooltips/helpers are the main quality risk. |
| `CFR_soviet_collapse_focus_tree` | factory 18-1045 | 47 | Strong construction-state depth and decisions; only one direct building focus in parsed focus file because most reward work is helper-driven. |
| `OGB_soviet_collapse_focus_tree` | factory 1047-1608 | 23 | Compact ancient/factory successor; has direct SOV wargoal and decision hooks; pathline risk remains. |
| `MFR_soviet_collapse_focus_tree` | factory 1610-2994 | 58 | Strong factory-war tree; pathline density risk around war-market and production branches. |
| `KZR/SOG/KHW/ALN_soviet_collapse_ancient_focus_tree` | ancient 13-1641 | 16 each | Very compact but complete minimum lanes: council, toll/law, workshop/market, guard, claim/charter, symbolic vs expansion, endgame. Needs depth if treated as full playable country packages. |

## High-Priority Findings

### Ukraine

Ukraine is content-rich, but two pathline blockers remain where a prerequisite parent is on the same row as the child. The wiki focus page notes prerequisite parents should be placed above children for correct path generation.

Evidence:

- `ukr_soviet_collapse_great_steppe_and_sea_plan` at `common/national_focus/005_soviet_collapse_republics.txt:1930`, `x = 27`, `y = 15`.
- `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map` depends on that focus and is also at `y = 15` according to mechanical scan. Queue a vertical/lane nudge so the parent sits above the endgame.
- `ukr_soviet_collapse_black_banner_takes_the_villages` at `common/national_focus/005_soviet_collapse_republics.txt:2247`, `x = 30`, `y = 18`.
- `ukr_soviet_collapse_the_commune_war` at `common/national_focus/005_soviet_collapse_republics.txt:2301`, `x = 27`, `y = 18`, has `prerequisite = { focus = ukr_soviet_collapse_black_banner_takes_the_villages }` at line 2308, so parent and child share a row.

Reward/depth status:

- Ukraine has 83 focuses, 12 focus blocks with decision unlock tooltips, 79 helper-driven rewards, 6 building reward focuses, 3 direct equipment reward focuses, and 0 direct `add_state_claim`/`create_wargoal`/`add_core_of` calls in the focus file.
- Expansion is mostly driven through helper effects and decisions, not direct focus payloads. This is acceptable if the decisions are fully staged, but it means expansion validation must inspect helper calls such as `soviet_collapse_apply_ukr_great_steppe_and_sea_plan` and Ukraine League decisions, not only the focus file.

Implementation queue:

1. Move the Ukraine endgame/Great Steppe lane so every visible prerequisite parent sits above its child.
2. Move the Black Banner high-chaos fork so `ukr_soviet_collapse_black_banner_takes_the_villages` is above `ukr_soviet_collapse_the_commune_war`.
3. Re-run the pathline overlap audit after moving; avoid isolated one-node nudges that push the line into adjacent high-chaos focuses.

### Belarus

Belarus has strong rail-state identity and good route AI coverage, but it currently has a hard coordinate collision in the rail/diplomacy branch.

Evidence:

- `blr_soviet_collapse_seal_the_minsk_junction` starts at `common/national_focus/005_soviet_collapse_republics.txt:9268`, `x = 6`, `y = 4`.
- `blr_soviet_collapse_foreign_aid_through_brest` starts at `common/national_focus/005_soviet_collapse_republics.txt:9405`, also `x = 6`, `y = 4`.
- Overlap produces edge risks:
  - Edge `blr_soviet_collapse_the_rail_map_on_the_wall` -> `blr_soviet_collapse_seal_the_minsk_junction` crosses/lands on `blr_soviet_collapse_foreign_aid_through_brest`.
  - Edge `blr_soviet_collapse_western_corridor_switchmen` -> `blr_soviet_collapse_foreign_aid_through_brest` crosses/lands on `blr_soviet_collapse_seal_the_minsk_junction` and passes near `blr_soviet_collapse_depot_cars_without_labels` at line 9336.
  - Edge `blr_soviet_collapse_foreign_aid_through_brest` -> `blr_soviet_collapse_brest_is_not_a_gift` passes through `blr_soviet_collapse_timetable_state` at line 9357.

Hidden gate evidence:

- `blr_soviet_collapse_which_road_is_belarus` at line 8941 only has visible prerequisite `blr_soviet_collapse_minsk_emergency_office`, but its `available` block at lines 8950-8966 requires two of three early focuses (`the_rail_map_on_the_wall`, `forest_committees_report_in`, `first_corridor_guard`). This avoids visible line crossings, but the current layout hides the real gate.
- `blr_soviet_collapse_partisans_or_army` at line 9608 hides a 2-of-3 forest route gate behind `available` at lines 9616-9630.
- `blr_soviet_collapse_join_the_league_when_war_comes` at line 9836 hides route gate checks for the political route focuses at lines 9851-9854.

Reward/depth status:

- Belarus has 53 focuses, 7 focus blocks with decision unlock tooltips, 52 helper-driven reward focuses, 5 building reward focuses, 0 direct equipment reward focuses, and 0 direct claim/wargoal/core calls in the focus file.
- This is not direct idea spam, but it does mean the rail/forest/League branch payoff is almost entirely helper-mediated. The rail identity is stronger than most shared trees because `blr_soviet_collapse_apply_rail_map_on_wall`, `blr_soviet_collapse_apply_timetable_state`, `blr_soviet_collapse_apply_every_track_through_minsk`, `blr_soviet_collapse_apply_armored_train_workshops`, and `blr_soviet_collapse_apply_league_depot_at_minsk` exist in `common/scripted_effects/005_soviet_collapse_effects.txt:9414-9608`.

Implementation queue:

1. Resolve the `x=6 y=4` collision between `seal_the_minsk_junction` and `foreign_aid_through_brest`.
2. Re-lane the western corridor so the Brest foreign-aid path does not pass through `depot_cars_without_labels` or the junction focus.
3. Decide whether the 2-of-3 early gate for `which_road_is_belarus` should remain hidden or be represented with cleaner visible prerequisites; if hidden, add clearer custom tooltip localisation.
4. Add at least one direct visible expansion/settlement payoff or decision unlock to the rail/forest late branch if the parent goal expects a distinct expansion branch that players can scan from the focus file itself.

### Kazakhstan

Kazakhstan is the deepest Event005 tree, but it has the most priority layout debt. There are three duplicate coordinate clusters and multiple diagonal pathlines through other route nodes.

Coordinate collision evidence:

- `kaz_soviet_collapse_the_alash_courts` starts at `common/national_focus/005_soviet_collapse_republics.txt:10405`, `x = 26`, `y = 4`.
- `kaz_soviet_collapse_the_resource_towns_demand_seats` starts at `common/national_focus/005_soviet_collapse_republics.txt:11196`, also `x = 26`, `y = 4`.
- `kaz_soviet_collapse_foreign_trucks_local_drivers` starts at line 11292, `x = 16`, `y = 7`.
- `kaz_soviet_collapse_emergency_oil_boards` starts at line 11707, also `x = 16`, `y = 7`.
- `kaz_soviet_collapse_army_of_the_open_horizon` starts at line 11940, `x = 2`, `y = 7`.
- `kaz_soviet_collapse_uzbek_supply_delegates` starts at line 11992, also `x = 2`, `y = 7`.

Pathline risk evidence:

- Edge `kaz_soviet_collapse_alma_ata_emergency_congress` at line 10193 to `kaz_soviet_collapse_the_congress_chooses_a_past` at line 10263 passes near `kaz_soviet_collapse_guard_the_resource_towns` at line 10243.
- Edge `kaz_soviet_collapse_resource_defense_directorate` at line 10384 to `kaz_soviet_collapse_the_resource_towns_demand_seats` at line 11196 lands on `kaz_soviet_collapse_the_alash_courts` at line 10405 and passes near `kaz_soviet_collapse_rail_to_the_mines` at line 10525.
- Edge `kaz_soviet_collapse_foreign_technical_missions` at line 10621 to `kaz_soviet_collapse_foreign_trucks_local_drivers` at line 11292 lands on `kaz_soviet_collapse_emergency_oil_boards` at line 11707.
- Edge `kaz_soviet_collapse_the_congress_chooses_a_past` at line 10263 to `kaz_soviet_collapse_the_steppe_keeps_many_memories` at line 11424 passes near `kaz_soviet_collapse_alash_memory_restored` at line 10346 and `kaz_soviet_collapse_the_written_alash_program` at line 11136.

Hidden gate evidence:

- `kaz_soviet_collapse_the_congress_chooses_a_past` at line 10263 has only visible prerequisite `kaz_soviet_collapse_alma_ata_emergency_congress`, while its `available` block at lines 10271-10283 requires two of the three opening lanes.
- `kaz_soviet_collapse_the_steppe_arsenal` at line 10647 hides a broad industrial/resource gate at lines 10655-10661.
- `kaz_soviet_collapse_steppe_federation_charter` at line 10860 hides a large southern-republic gate at lines 10868-10893.
- `kaz_soviet_collapse_the_steppe_keeps_many_memories` at line 11424 hides a five-focus memory/route gate at lines 11432-11438.
- `kaz_soviet_collapse_the_steppe_stands_between_worlds` at line 12190 hides a large endgame gate at lines 12196-12205.

Reward/AI status:

- Kazakhstan has 92 focuses, 6 focus blocks with decision unlock tooltips, 86 helper-driven reward focuses, 21 building reward focuses, 6 equipment reward focuses, and 0 direct claim/wargoal/core calls in the focus file.
- Its AI weights are the weakest of the three priority trees by current mechanical count: 61 flat `ai_will_do` blocks and 31 with modifiers. Many route focuses still have only `base = 6` or `base = 7`, despite the tree having stateful route variables and southern-breakaway mechanics.

Implementation queue:

1. Fix all three coordinate collisions before further reward work.
2. Re-lane Alash/resource branches so resource-directorate lines do not land on Alash-court nodes.
3. Re-lane foreign/security/resource branches around `foreign_trucks_local_drivers` and `emergency_oil_boards`.
4. Re-lane southern-federation/military branches around `army_of_the_open_horizon` and `uzbek_supply_delegates`.
5. Convert important flat Kazakhstan `ai_will_do` blocks into route/state-aware weights using existing route variables and flags.
6. Validate that expansion payoffs eventually create claims, war goals, regional federation decisions, or settlement decisions through related decisions/effects; the focus file itself has no direct claim/wargoal/core calls.

## Repeated Idea And Helper Spam Evidence

Direct focus-file idea spam is currently not present:

- Mechanical scan found 0 direct `add_ideas`, `swap_ideas`, `remove_ideas`, `add_timed_idea`, or `modify_timed_idea` calls inside the four focus files.

Indirect idea lifecycle is concentrated in scripted effects:

- `common/scripted_effects/005_soviet_collapse_effects.txt:5047-5068` swaps/removes the republican startup disorder idea.
- `common/scripted_effects/005_soviet_collapse_effects.txt:5926-5950` clears staged republic ideas.
- `common/scripted_effects/005_soviet_collapse_effects.txt:12196-12218` ensures CFR/MFR factory-state ideas only if absent.
- `common/scripted_effects/005_soviet_collapse_effects.txt:18332-18346` upgrades/adds the DSC dead-army politics idea through a guarded update effect.
- `common/scripted_effects/005_soviet_collapse_effects.txt:18874-19466` adds many custom-splinter identity ideas, each guarded by `NOT = { has_idea = ... }`.

The repeated-spam problem is helper and tooltip repetition, not direct unguarded idea spam.

Top repeated focus reward helpers across all audited focus files:

- 142 uses: `soviet_collapse_apply_focus_depot_and_supply_control`
- 131 uses: `soviet_collapse_apply_focus_military_consolidation`
- 106 uses: `soviet_collapse_apply_focus_legal_recognition`
- 92 uses: `soviet_collapse_apply_focus_republican_compact_plan`
- 66 uses: `soviet_collapse_apply_focus_foreign_channel`
- 63 uses: `soviet_collapse_apply_focus_security_supply_plan`
- 54 uses: `soviet_collapse_apply_focus_high_chaos_identity`
- 51 uses: `soviet_collapse_apply_focus_league_preparation`
- 46 uses: `soviet_collapse_apply_focus_chaos_assault_plan`

Top repeated focus tooltip keys:

- 84 uses: `soviet_collapse_custom_splinter_political_route_reward_tt`
- 34 uses: `soviet_collapse_custom_splinter_logistics_route_reward_tt`
- 29 uses: `soviet_collapse_custom_splinter_expansion_route_reward_tt`
- 29 uses: `soviet_collapse_custom_splinter_military_route_reward_tt`
- 28 uses: `soviet_collapse_custom_splinter_diplomacy_route_reward_tt`
- 27 uses: `soviet_collapse_custom_splinter_industrial_route_reward_tt`
- 19 uses: `soviet_collapse_custom_splinter_high_chaos_route_reward_tt`
- 14 uses: `soviet_collapse_custom_splinter_league_route_reward_tt`
- 14 uses: `soviet_collapse_custom_splinter_hidden_doctrine_reward_tt`

Conclusion: the no-repeated-idea-tooltip constraint is only partially satisfied. Direct idea churn was consolidated, but many custom splinter focuses still show repeated generic route tooltip keys instead of country/lore-specific tooltip wording.

## Shallow Reward Evidence

The broad issue is not focus count. It is how often focus rewards are abstract helper calls rather than visible direct gameplay changes.

Direct focus-file reward scan:

- Ukraine: 83 focuses, 12 decision-unlock focuses, 6 building focuses, 3 equipment focuses, 0 direct claim/wargoal/core focuses.
- Belarus: 53 focuses, 7 decision-unlock focuses, 5 building focuses, 0 equipment focuses, 0 direct claim/wargoal/core focuses.
- Kazakhstan: 92 focuses, 6 decision-unlock focuses, 21 building focuses, 6 equipment focuses, 0 direct claim/wargoal/core focuses.
- Breakaway shared tree: 36 focuses, 0 decision-unlock focuses, 7 building focuses, 2 equipment focuses, 0 direct claim/wargoal/core focuses.
- Baltic: 42 focuses, 0 decision-unlock focuses, 11 building focuses, 2 equipment focuses, 0 direct claim/wargoal/core focuses.
- Moldova: 48 focuses, 0 decision-unlock focuses, 13 building focuses, 2 equipment focuses, 0 direct claim/wargoal/core focuses.
- Many 47-focus custom splinters have 0-3 decision-unlock focuses and 0 direct claim/wargoal/core focuses in the focus file, despite having nominal expansion branches.
- Ancient restoration trees each have direct claim/wargoal/core payloads, but are only 16 focuses each; they need deeper political/industry/military/expansion branches if intended as full playable successors.

High-chaos aggression status:

- The high-chaos helper is aggressive. `soviet_collapse_apply_high_chaos_focus_payload` at `common/scripted_effects/005_soviet_collapse_effects.txt:9188` grants expansion claims/payloads, neighbor pressure, SOV conquest/antagonize AI, and creates or declares an annexation war goal against SOV under terminal/high-chaos conditions.
- This supports the user constraint that chaos countries should be aggressive and overpowered, but because the payload is shared and often one-time-flagged, individual high-chaos trees can still feel samey.

## Branch And Layout Evidence Across All Files

Global layout facts:

- 0 audited focuses use `relative_position_id`.
- Duplicate coordinate clusters remain:
  - Internal shared tree: `internal_soviet_collapse_sevastopol_road_watch` line 3916 and `internal_soviet_collapse_lena_baikal_relay_posts` line 4120 both at `(17,6)`.
  - Caucasus shared tree: `caucasus_soviet_collapse_council_of_passes` line 5941 and `caucasus_soviet_collapse_oilfield_security_compacts` line 6004 both at `(12,4)`.
  - Belarus: `blr_soviet_collapse_seal_the_minsk_junction` line 9268 and `blr_soviet_collapse_foreign_aid_through_brest` line 9405 both at `(6,4)`.
  - Kazakhstan: three duplicate coordinate clusters listed in the Kazakhstan section.

Examples of pathline overlap risks outside the priority trees:

- `FTH_inner_faction` line 356 -> `FTH_enemy_front` line 453 passes near `FTH_supply` line 417.
- `PRA_omsk_station_guard` line 1434 -> `PRA_switchyard_denial_posts` line 1685 passes near `PRA_repair_crews_without_ministries` line 1602.
- `TSC_the_committee_of_instruments` line 2189 -> `TSC_night_survey_columns` line 2316 passes through/near `TSC_observatory_guard` line 2255.
- `RMC_communes_of_witnesses` line 2635 -> `RMC_hagiographers_of_every_front` line 2799 passes through/near `RMC_reliquary_guard` line 2721.
- `DSC_witness_officers` line 3134 -> `DSC_maps_of_lost_armies` line 3307 passes through/near `DSC_field_hospital_memorials` line 3216.
- `NRF_living_harbor_committees` line 3644 -> `NRF_maps_of_sunken_routes` line 3825 passes through/near `NRF_icebound_marine_guard` line 3741.
- `ICD_commissars_of_last_addresses` line 4152 -> `ICD_archives_of_every_front` line 4314 passes through/near `ICD_funeral_guard` line 4238.
- `UDC_diplomatic_plan` line 10559 -> `UDC_loyalist_statute_guarantees` line 11049 passes near `UDC_staff_car_workshops` line 10892 and `UDC_hidden_doctrine` line 11428.
- `SDZ_diplomatic_plan` line 11770 -> `SDZ_chain_of_custody_statutes` line 12278 passes near `SDZ_archive_bunker_vaults` line 12197 and `SDZ_custody_hospital_blocks` line 12529.
- `GAC_war_plan` line 13633 -> `GAC_industry_plan` line 13826 passes through/near `GAC_settlement` line 13752.
- `NLC_greenhouse_boards` line 25148 -> `NLC_heated_workshop_contracts` line 25277 passes through/near `NLC_settlement` line 25017 and near `NLC_industry_plan` line 25601.
- `CFR_the_state_that_builds` line 809 -> `CFR_buy_peace_with_concrete` line 835 passes near `CFR_the_builder_state_marches_east` line 853.
- `OGB_the_council_takes_the_seal` line 1102 -> `OGB_reopen_volga_trade_tolls` line 1176 passes through/near `OGB_scholars_guard_the_charter` line 1127.
- `MFR_factory_war_cabinet` line 1960 has multiple dense outgoing edge risks around `MFR_artillery_from_broken_foundries`, `MFR_rifles_before_speeches`, `MFR_workers_must_not_flee`, `MFR_builders_waste_steel`, and `MFR_factory_guard_columns`.

These are approximate straight-line/coordinate overlap risks from a mechanical scan, not a rendered in-game screenshot. They should be confirmed in-game or with a focus layout visualizer before final layout claims.

## AI Findings

Every audited focus has an `ai_will_do` block.

Flat-vs-modified AI counts:

- Ukraine: 27 flat, 56 modified.
- Belarus: 12 flat, 41 modified.
- Kazakhstan: 61 flat, 31 modified.
- Ancient KZR/SOG/KHW/ALN: 12 flat, 4 modified each.
- Most 47-focus custom splinter trees have modified AI on every focus, but FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC still have some flat AI.

Priority:

1. Kazakhstan route AI should be upgraded first because it has the deepest route/mechanic surface but the most flat AI.
2. Ancient restorations need more route/state-sensitive AI if they remain playable successors.
3. Custom splinter AI is broadly present, but repeated helper families should be checked to ensure high-chaos tags actually pursue wars rather than only accumulating generic route weights.

## Exact High-Priority Implementation Queue

1. Kazakhstan layout pass:
   - Fix collisions at `(26,4)`, `(16,7)`, and `(2,7)`.
   - Re-lane Alash/resource/foreign/southern branches so prerequisite lines do not cross visible route nodes.
   - Then add route-aware AI to the many flat Kazakhstan focuses.

2. Belarus layout pass:
   - Separate `blr_soviet_collapse_seal_the_minsk_junction` and `blr_soviet_collapse_foreign_aid_through_brest`.
   - Re-lane Brest/rail/timetable nodes to stop line overlap through the junction and `timetable_state`.
   - Add clearer visible or tooltip gate handling for the 2-of-3 opening gate and the forest route gate.

3. Ukraine layout pass:
   - Move same-row parent/child pairs in the Great Steppe endgame and Black Banner high-chaos branch.
   - Recheck the high-chaos lane after movement; current indentation is also visually inconsistent around lines 2247-2308, though the parser still recognized valid focus blocks.

4. Shared/custom-splinter tooltip pass:
   - Replace repeated generic `soviet_collapse_custom_splinter_*_route_reward_tt` usages with tag- or lore-specific tooltip keys for high-priority custom countries.
   - Keep shared helpers, but localise effect meaning per country route so the player does not see the same idea/reward text repeatedly.

5. Expansion payoff validation pass:
   - For every tree with 0 direct focus-file claim/wargoal/core payloads, trace the branch to decisions/effects and verify the expansion branch really unlocks claims, war goals, postwar settlement, regional mandates, federation decisions, or protectorate logic.
   - Start with Ukraine, Belarus, Kazakhstan, Baltic, Moldova, and the 47-focus custom splinters with 0 decision unlocks.

6. Compact tree depth pass:
   - TSC/RMC/DSC/NRF/ICD and the ancient 16-focus restorations should be explicitly classified as compact/special-purpose or deepened into fuller political, industrial, expansion, military, diplomacy, and endgame branch families.

## Validation Commands Used

Reference/documentation checks:

```bash
sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md
sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-decisions-missions/SKILL.md
rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus|Focus'
rg --files '/home/klim/projects/Hearts of Iron IV/documentation' | rg -i 'focus|trigger|effect|localisation|modifier|ai|script|decision|event|idea'
rg --files '/home/klim/projects/Hearts of Iron IV/common/national_focus' | head -40
```

Focus inventory and mechanical scans:

```bash
wc -l common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
rg -n "^\\s*focus_tree|^\\s*focus = \\{|id = |relative_position_id|mutually_exclusive|prerequisite|ai_will_do|completion_reward|add_ideas|swap_ideas|modify_timed_idea|add_timed_idea|load_focus_tree|unlock_decision|activate_decision|set_country_flag|has_completed_focus" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
rg -n "add_ideas|swap_ideas|remove_ideas|add_timed_idea|modify_timed_idea|custom_effect_tooltip|unlock_decision_tooltip|add_state_claim|create_wargoal|declare_war_on|add_core_of|add_ai_strategy|load_focus_tree" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
```

Related system tracing:

```bash
find common/decisions common/scripted_effects common/scripted_triggers common/ideas localisation -type f | rg '005|soviet_collapse|UKR|KAZ|BLR|KZR|SOG|collapse'
rg -n "^\\s*(ukr_|kaz_|blr_|soviet_collapse_apply_focus|soviet_collapse_apply_kazakhstan|soviet_collapse_apply_belarus|ukr_soviet|kaz_soviet|blr_soviet).*=( yes| \\{)|^\\s*soviet_collapse_.*focus.*= \\{" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_*.txt common/decisions/categories/005_soviet_collapse_categories.txt
rg -n "add_ideas|swap_ideas|remove_ideas|add_timed_idea|modify_timed_idea|remove_timed_idea|soviet_collapse_.*tension|idea|soviet_collapse_.*_idea" common/scripted_effects/005_soviet_collapse_effects.txt common/ideas/005_soviet_collapse_ideas.txt localisation/english/005_soviet_collapse*_l_english.yml
```

Recommended next validation after implementation:

```bash
python3 - <<'PY'
from pathlib import Path
import re
files = [Path(p) for p in [
    'common/national_focus/005_soviet_collapse_republics.txt',
    'common/national_focus/005_soviet_collapse_custom_splinters.txt',
    'common/national_focus/005_soviet_collapse_factory_successors.txt',
    'common/national_focus/005_soviet_collapse_ancient_restorations.txt',
]]
ids = []
for path in files:
    for line_no, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        m = re.match(r'\s*id\s*=\s*([A-Za-z0-9_]+)', line)
        if m:
            ids.append((m.group(1), path, line_no))
seen = {}
for focus_id, path, line_no in ids:
    if focus_id in seen:
        print('DUPLICATE', focus_id, seen[focus_id], (path, line_no))
    else:
        seen[focus_id] = (path, line_no)
PY
```

```bash
rg -n "x = .*y =|relative_position_id|prerequisite|available = \\{|has_completed_focus|mutually_exclusive" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
```

## Simplifications, Omissions, And Blockers

- This was a read-only audit. No focus/localisation fixes were applied because the priority layout issues are connected branch clusters, not isolated one-line safe patches.
- No rendered in-game focus tree screenshots were produced, so pathline findings are mechanical coordinate/edge-risk evidence and must be confirmed visually after a layout patch.
- The audit did not inspect gfx/flags/binary assets and did not touch them.
- The worktree was already heavily dirty before this handoff. This pass did not attempt to revert, stage, or commit unrelated work.

## Skills Used

- `hoi4-focus-trees`
- `hoi4-decisions-missions`

