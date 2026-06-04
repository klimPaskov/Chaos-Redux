# Event005 Soviet Collapse Focus Tree Full Rework Audit

Audit role: `chaosx_focus_tree_auditor`

Timestamp: `2026_06_04_085234` UTC

Scope reviewed:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Hard asset constraint followed: no flag assets, `.tga` files, `gfx/flags`, or flag sprite assets were read, written, or modified. This handoff is the only file added by this audit.

## Required Reading Completed

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- Offline wiki:
  - `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
  - plus AGENTS-required core pages for Modifiers, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Vanilla docs consulted:
  - `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- Vanilla focus precedents checked:
  - `/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt`
  - `/home/klim/projects/Hearts of Iron IV/common/national_focus/mexico.txt`
- Event005 design context checked:
  - `docs/events/005_soviet_collapse.md`
  - `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`

## Summary

The four scoped files currently contain 1,698 focuses across 43 focus trees. All parsed focus blocks have `ai_will_do`, and direct visible idea spam in the four focus files appears largely removed: no direct `add_ideas`, `remove_ideas`, `swap_ideas`, or `show_ideas_tooltip` calls were found in parsed `completion_reward` blocks. The remaining problem is not basic focus count or missing AI blocks. It is route quality, helper homogenization, tooltip/reward repetition, shallow capstones, and layout readability.

The broad pattern is:

- Major republic trees now have many focuses, but many branches still resolve into repeated helper families instead of unique branch mechanics.
- Custom splinter trees reuse the same copied route skeleton heavily. The 47-focus variants are larger, but many still feel like renamed generic rows unless their tag-specific helper output is very strong.
- `CFR` and `MFR` are large but still depend on repeated construction/arsenal helper rhythms; they should be visibly overpowered construction and factory successor states, not normal minors with many factory-flavored focuses.
- `OGB` and all ancient restoration trees remain compact relative to the requested political/industrial/military/diplomacy/expansion branch depth.
- Ukraine and Belarus have real content, but their layouts are hard to read due to many long one-row jumps and branches spread across wide coordinate spans.
- There are no occupied coordinate cells or same-row `dx = 1` collisions in the current resolved coordinates, but pathline quality remains poor because many prerequisites jump horizontally by 5-14 cells in one row.

This is an audit and implementation handoff only. It does not complete the user's requested full rework.

## Focus Counts

| File | Tree id | Focuses |
| --- | --- | ---: |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 83 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 36 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | 62 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | 42 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 40 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 45 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 48 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | 53 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | 92 |
| `005_soviet_collapse_custom_splinters.txt` | `FTH_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | 22 |
| `005_soviet_collapse_custom_splinters.txt` | `TSC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `DSC_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `ICD_soviet_collapse_focus_tree` | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `BSC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `TNC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ALA_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BBH_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KRS_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UDC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SDZ_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `GAC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KHC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `FEV_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SZA_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UWD_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `MRC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `IUL_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BAC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ARD_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `NLC_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 47 |
| `005_soviet_collapse_factory_successors.txt` | `OGB_soviet_collapse_focus_tree` | 23 |
| `005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 58 |
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `SOG_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `ALN_soviet_collapse_ancient_focus_tree` | 16 |

Per-file totals:

- `005_soviet_collapse_republics.txt`: 501 focuses.
- `005_soviet_collapse_custom_splinters.txt`: 1,005 focuses.
- `005_soviet_collapse_factory_successors.txt`: 128 focuses.
- `005_soviet_collapse_ancient_restorations.txt`: 64 focuses.

## Repeated Reward and Helper Usage

Direct parsed idea calls in focus rewards:

- `add_ideas`: 0
- `remove_ideas`: 0
- `swap_ideas`: 0
- `show_ideas_tooltip`: 0

This is good relative to earlier idea-spam complaints. The remaining reward spam has moved into repeated helper calls and repeated custom tooltips.

Most repeated helper calls in parsed focus rewards:

| Count | Helper |
| ---: | --- |
| 141 | `soviet_collapse_apply_focus_depot_and_supply_control` |
| 132 | `soviet_collapse_apply_focus_military_consolidation` |
| 108 | `soviet_collapse_apply_focus_legal_recognition` |
| 80 | `soviet_collapse_apply_focus_republican_compact_plan` |
| 65 | `soviet_collapse_apply_focus_foreign_channel` |
| 63 | `soviet_collapse_apply_objective_source_pressure_delta` |
| 60 | `soviet_collapse_apply_focus_high_chaos_identity` |
| 58 | `soviet_collapse_apply_focus_security_supply_plan` |
| 52 | `soviet_collapse_apply_focus_league_preparation` |
| 38 | `soviet_collapse_apply_custom_splinter_league_identity` |
| 37 | `soviet_collapse_apply_focus_foreign_recognition_plan` |
| 36 | `soviet_collapse_apply_custom_splinter_enemy_front_identity` |
| 29 | `soviet_collapse_apply_focus_foreign_league_plan` |
| 29 | `soviet_collapse_apply_focus_chaos_assault_plan` |
| 28 | `soviet_collapse_apply_custom_splinter_expansion_claims` |
| 23 | `soviet_collapse_apply_focus_socialist_sovereignty` |
| 22 | `soviet_collapse_spawn_custom_splinter_assault_columns` |
| 21 | `soviet_collapse_apply_focus_chaos_legitimacy_plan` |
| 21 | `soviet_collapse_apply_focus_league_security_plan` |
| 21 | `soviet_collapse_apply_focus_lawful_supply_plan` |

Most repeated custom effect tooltips:

| Count | Tooltip |
| ---: | --- |
| 115 | `soviet_collapse_custom_splinter_political_route_reward_tt` |
| 41 | `soviet_collapse_custom_splinter_logistics_route_reward_tt` |
| 40 | `soviet_collapse_custom_splinter_industrial_route_reward_tt` |
| 39 | `soviet_collapse_custom_splinter_expansion_route_reward_tt` |
| 38 | `soviet_collapse_custom_splinter_military_route_reward_tt` |
| 38 | `soviet_collapse_custom_splinter_diplomacy_route_reward_tt` |
| 24 | `soviet_collapse_custom_splinter_high_chaos_route_reward_tt` |
| 19 | `soviet_collapse_custom_splinter_doctrine_identity_reward_tt` |
| 19 | `soviet_collapse_custom_splinter_league_route_reward_tt` |
| 19 | `soviet_collapse_custom_splinter_hidden_doctrine_reward_tt` |

Interpretation: helper reuse is not automatically wrong. Shared helpers are appropriate when they implement real shared systems. But the current distribution means many focus routes read and behave similarly unless the tag-specific wrapper helper gives a substantial unique effect. The 115 repeated `political_route_reward` tooltip is especially visible evidence of the copied custom-splinter template.

## Duplicate Same Helper or Effect Inside One Reward Block

Only three duplicate same-effect cases were found in parsed `completion_reward` blocks:

| File | Focus | Duplicate |
| --- | --- | --- |
| `005_soviet_collapse_republics.txt:7380` | `central_asia_soviet_collapse_khwarazm_restoration_debate` | `add_state_claim = 405` twice and `add_state_claim = 585` twice |
| `005_soviet_collapse_custom_splinters.txt:3133` | `DSC_claim_the_soldiers_road` | `has_country_flag = dsc_focus_revenant_staff_line` appears twice inside reward logic |
| `005_soviet_collapse_factory_successors.txt:1600` | `OGB_claim_the_old_trade_cities` | `is_controlled_by = ROOT` three times and `add_core_of = ROOT` three times; likely per-state scoped repeats, but parent should verify tooltip/result clarity |

No tiny safe patch was made because this audit was requested as read-only and the duplicates require design confirmation rather than an obvious typo-only fix.

## Route and Mechanic Depth Gaps

The spec requires every real branch to have a mechanical unlock, a meaningful choice, interaction with decisions/missions/ideas/leaders/units/buildings/diplomacy/map/AI/events, and a payoff. Current gaps:

- `soviet_collapse_breakaway_focus_tree`: 36 focuses, no direct decision unlocks or war goals in parsed focus rewards. It has repeated depot, military, legal, and compact helpers, but too many focuses are still generic statehood consolidation. It needs expansion, diplomacy, industry, and league/foreign decision surfaces.
- `soviet_collapse_baltic_focus_tree`: 42 focuses but many branch payoffs are helper-only and layout lines are long. Needs sharper split between legal continuity, military border state, port economy, foreign protection, and Pan-Baltic formation.
- `soviet_collapse_caucasus_focus_tree`: 40 focuses, only 4 direct decision unlocks. It has oil/pass themes but needs stronger postwar/pass settlement, oil-state consequences, sponsor risk, and mountain/federal branch payoffs.
- `soviet_collapse_moldova_focus_tree`: 48 focuses but no direct decision unlocks found in parsed rewards. It needs Romanian alignment, Dniester bridge, buffer, and small-state diplomacy mechanics rather than only helpers and one news event.
- `soviet_collapse_belarus_focus_tree`: 53 focuses and 6 decision unlocks. It is promising but fragmented. Railway/corridor, forest, League depot, foreign corridor, and military transit should become distinct branch systems.
- `CFR_soviet_collapse_focus_tree`: 47 focuses, 10 decision unlocks and 2 war goals, but 34 focuses were flagged as likely flat/helper-heavy by the heuristic. It should become an overpowered construction directorate with a map-building economy, not a normal industry tree.
- `MFR_soviet_collapse_focus_tree`: 58 focuses, 4 decision unlocks and 1 war goal, but 46 focuses flagged as likely flat/helper-heavy. It needs arsenal-client, unsafe output, arms market, factory war cabinet, and armored train systems with visible military consequences.
- `OGB_soviet_collapse_focus_tree`: 23 focuses. It has claims/cores and war goals, but not enough branch families for the requested political/industrial/military/diplomacy/expansion depth.
- `PRA_soviet_collapse_focus_tree`: 22 focuses. It has the best compact mechanics among the small chaos trees, but the Pale Railway Authority should be far more dangerous: rail-corridor control, armored train deployment, rail-state war goals, and moving-state diplomacy.
- `TSC`, `RMC`, `NRF`, `ICD`: 18 focuses each. These are compact special actors and still not deep enough for long-lived playable chaos-country trees. They need route-specific overpowered crisis mechanics.
- 47-focus custom splinter variants: despite higher counts, the copied branch structure is too visible. Reused route skeletons should be converted into tag-specific mechanic branches for at least the largest/most dangerous actors.
- Ancient restorations: 16 focuses each. They now contain claims/cores/war goal surfaces, but their symbolic, league, expansionist, and endgame routes are still too compact for the requested full rework.

## Layout Risks

Coordinate scan results:

- Occupied cells: none detected in resolved tree-local coordinates.
- Too-close same-row focuses at `dx = 1`: none detected.
- Continuous focus panel interference: no coordinate-derived top-row panel overlap detected. Continuous focus positions are far to the right in pixel coordinates for these trees.
- Focus sitting directly on a vertical prerequisite line: 1 detected in Moldova:
  - `moldova_soviet_collapse_alliance_not_union -> moldova_soviet_collapse_western_training_mission` has `moldova_soviet_collapse_southern_rail_timetables` sitting on the vertical segment at `(20, 7)`.
- Mutual exclusion long/midpoint risks:
  - `baltic_soviet_collapse_legal_continuity_government` vs `baltic_soviet_collapse_military_border_government`: `dx = 12`, same row.
  - `central_asia_soviet_collapse_local_republic_council` vs `central_asia_soviet_collapse_military_border_authority`: `dx = 8`, same row.
  - `blr_soviet_collapse_decentralized_detachments` vs `blr_soviet_collapse_regular_forest_brigades`: `dx = 6`, same row.
  - `kaz_soviet_collapse_league_resource_pool` vs `kaz_soviet_collapse_foreign_technical_missions`: `dx = 7`, same row.
  - `PRA_rails_over_capitals` vs `PRA_the_pale_line_endures`: `dx = 6`, `dy = 1`.
  - `UDC_settlement` vs `UDC_radical_turn`, `SDZ_settlement` vs `SDZ_radical_turn`, `DHC_settlement` vs `DHC_radical_turn`, `KHC_settlement` vs `KHC_radical_turn`, `ARD_settlement` vs `ARD_radical_turn`: copied long same-row mutual-exclusion patterns.
  - All four ancient symbolic-vs-expansionist pairs have `dx = 6`, same row.

High-volume long or awkward prerequisite line counts:

- Ukraine: 33 flagged long/upward/awkward prerequisite links.
- Belarus: 36 flagged.
- Kazakhstan: 43 flagged.
- Moldova: 30 flagged.
- Baltic: 21 flagged.
- Central Asia: 18 flagged.
- Caucasus: 16 flagged.
- Internal republic tree: 16 flagged.
- Many 47-focus custom splinters have 10-22 flagged long one-row jumps because they inherit the same copied layout grammar.

The main visual problem is not coordinate collision. It is that many focuses are placed as wide same-row fans with prerequisites jumping 4-14 cells sideways in one row, which produces ugly diagonal or long horizontal pathlines and makes mutually exclusive relationships hard to read.

## Ukraine Layout and Readability

`soviet_collapse_ukraine_focus_tree` has 83 focuses and enough route material to become a strong tree, but the layout is not readable enough for that size.

Specific coordinate/pathline problems:

- Opening row fans too widely:
  - `ukr_soviet_collapse_emergency_rada -> ukr_soviet_collapse_count_the_depot_keys`: `dx = 4`, `dy = 1`.
  - `ukr_soviet_collapse_count_the_depot_keys -> ukr_soviet_collapse_first_republican_line`: `dx = 6`, `dy = 1`.
- Foreign branch backtracks upward in file order and crosses the central political area:
  - `ukr_soviet_collapse_foreign_courts_notice_kyiv -> ukr_soviet_collapse_open_the_liaison_offices`: `dx = 5`, `dy = 1`.
  - `ukr_soviet_collapse_question_of_statehood -> ukr_soviet_collapse_foreign_courts_notice_kyiv`: `dx = 7`, `dy = 1`.
- Army and cabinet branch is tangled:
  - `ukr_soviet_collapse_foreign_courts_notice_kyiv -> ukr_soviet_collapse_army_supremacy`: `dx = -12`, `dy = 3`.
  - `ukr_soviet_collapse_army_supremacy` and `ukr_soviet_collapse_mixed_emergency_cabinet` are mutually exclusive but embedded among other central-route lines.
- Western/Black Sea/external expansion chain is spread very wide:
  - `ukr_soviet_collapse_depot_motor_columns -> ukr_soviet_collapse_arsenal_cities`: `dx = 7`, `dy = 3`.
  - `ukr_soviet_collapse_direct_national_claims`, `ukr_soviet_collapse_breadbasket_empire`, `ukr_soviet_collapse_black_sea_hegemony`, `ukr_soviet_collapse_great_steppe_and_sea_plan`, and `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map` should be a visually coherent expansion branch instead of interleaving through other route families.
- Black Banner/high-chaos Ukraine has a strong thematic chain, but it is visually mixed into bread/grain and statehood routes:
  - `ukr_soviet_collapse_bread_state_whispers`
  - `ukr_soviet_collapse_black_soil_oath`
  - `ukr_soviet_collapse_the_bread_line_becomes_a_border`
  - `ukr_soviet_collapse_dead_fields_living_columns`
  - `ukr_soviet_collapse_no_one_leaves_the_bread_line`
  - `ukr_soviet_collapse_the_commune_war`
  - `ukr_soviet_collapse_the_double_republic`
  - `ukr_soviet_collapse_last_harvest_plan`

Parent rework recommendation: rebuild Ukraine around vertical branch bands with an opening statehood/survival trunk, then separate political, military, League/diplomacy, industry/grain, foreign patron, territorial expansion, and Black Banner/high-chaos branches. Avoid wide one-row fans from `question_of_statehood`.

## Belarus Layout and Readability

`soviet_collapse_belarus_focus_tree` has 53 focuses and a clear identity set: rail corridor, forests, foreign corridor, League depot, military transit, and green/forest state. The readability problem is that those identities cross each other spatially.

Specific coordinate/pathline problems:

- Opening fan is too wide:
  - `blr_soviet_collapse_minsk_emergency_office -> blr_soviet_collapse_the_rail_map_on_the_wall`: `dx = -4`, `dy = 1`.
  - `blr_soviet_collapse_minsk_emergency_office -> blr_soviet_collapse_forest_committees_report_in`: `dx = 6`, `dy = 1`.
  - `blr_soviet_collapse_the_rail_map_on_the_wall -> blr_soviet_collapse_which_road_is_belarus`: `dx = 6`, `dy = 1`.
- Central route choices jump into distant branch areas:
  - `blr_soviet_collapse_which_road_is_belarus -> blr_soviet_collapse_national_council_of_minsk`: `dx = -9`, `dy = 3`.
  - `blr_soviet_collapse_which_road_is_belarus -> blr_soviet_collapse_foreign_corridor_administration`: `dx = 9`, `dy = 4`.
- Forest branch crosses from far right to left:
  - `blr_soviet_collapse_forest_defense_staff -> blr_soviet_collapse_council_bargains_with_forests`: `dx = -22`, `dy = 4`.
- Railway branch jumps across rows:
  - `blr_soviet_collapse_the_rail_map_on_the_wall -> blr_soviet_collapse_seal_the_minsk_junction`: `dx = -7`, `dy = 4`.
  - `blr_soviet_collapse_eastern_line_watch -> blr_soviet_collapse_timetable_state`: `dx = -7`, `dy = 3`.
  - `blr_soviet_collapse_timetable_state -> blr_soviet_collapse_league_supply_timetables`: `dx = 6`, `dy = 2`.
- Mutual exclusion line is long:
  - `blr_soviet_collapse_decentralized_detachments` vs `blr_soviet_collapse_regular_forest_brigades`: `dx = 6`, same row.

Parent rework recommendation: make Belarus a three-axis tree: rail/corridor on one side, forest/partisan-state on the other, and diplomacy/League depot in the middle or lower bridge. The current route ideas are good enough to preserve, but coordinates should be rebuilt rather than locally nudged.

## Chaos-Country Identity Gaps

Construction directorate / `CFR`:

- Current count is 47, but 34 focuses were flagged as likely flat/helper-heavy.
- It should become overpowered through a construction mandate economy: instant civilian factories, infrastructure, supply hubs, railways, forts, and factory-city state modifiers from decisions unlocked by focus depth.
- Patch surface: `CFR_count_the_cranes`, `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_the_concrete_committee`, `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`, `CFR_the_board_becomes_the_cabinet`, `CFR_the_builder_state`, `CFR_civilian_hegemony_project`.

Dead Soldiers' Congress / `DSC`:

- Current count is 18. It has the right hooks: front-road claims, core-controlled front-road states, dead-army wars, assault columns.
- It should become more overpowered by making casualty/death-state logic escalate manpower, attack planning, cores, claims, and recurring dead-army offensives.
- Patch surface: `DSC_maps_of_lost_armies`, `DSC_claim_the_soldiers_road`, `DSC_armies_that_do_not_demobilize`, `DSC_congress_of_the_dead_army`, `DSC_the_dead_army_votes_forward`, `soviet_collapse_dsc_claim_front_road_states`, `soviet_collapse_dsc_core_controlled_front_road_states`, `soviet_collapse_dsc_launch_dead_army_neighbor_wars`.

Railway country / `PRA`:

- Current count is 22. It has 14 decision unlocks, 1 war goal, and rail-specific helpers, so it is mechanically healthier than most compact chaos trees.
- It should still be much stronger: rail authority should create a moving state, armored train school, rail war goals, supply-node sprawl, and corridor coercion.
- Patch surface: `PRA_count_the_locomotives`, `PRA_switchyard_denial_posts`, `PRA_armored_train_schools`, `PRA_claim_the_branch_lines`, `PRA_seize_the_junction_cities`, `PRA_rails_over_capitals`, `PRA_the_pale_line_endures`, plus `soviet_collapse_update_pra_authority_idea` and `soviet_collapse_build_pra_corridor_network`.

Factory successors / `MFR`, `OGB`, `CFR`:

- `MFR` is big at 58 focuses but reward rhythm remains mostly helper/stat/construction. It should become an arms-market and client-war engine.
- `OGB` is only 23 focuses and remains underbuilt for a restored Volga/Bolghar country. It needs real political, religious/legal, trade, military, diplomacy, and expansion branches.
- `CFR` should be the construction counterpart to `MFR`, with map-altering construction power.

Special splinters:

- The 47-focus trees should not share the same route feel. The copied branch IDs (`*_first_guard`, `*_stores`, `*_legitimacy`, `*_doctrine`, `*_league`, `*_foreign`, `*_inner_faction`, `*_enemy_front`, `*_civil_rule`, `*_propaganda`, `*_settlement`, `*_industry_plan`, `*_hidden_doctrine`, `*_extreme_gate`, `*_endgame`) are too visible.
- Make the largest or most thematic splinters OP first: `UDC`, `SDZ`, `UWD`, `FEV`, `SZA`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`, `DHC`, `KHC`.

Ancient restorations:

- Each ancient tree has only 16 focuses. They have claims, cores, SOV war goals, and high-chaos neighbor plans, but still lack full branch families.
- They should become overpowered through old-border claims, symbolic legitimacy, cultural/legal restoration decisions, rapid coring/integration, old route/road control, and neighbor expansion.
- Patch surface: `KZR_*`, `SOG_*`, `KHW_*`, `ALN_*` symbolic-vs-expansionist pairs, charter focuses, and returned-names endgames.

## Ranked Next 20 Parent Patch Targets

1. `common/national_focus/005_soviet_collapse_republics.txt` - `soviet_collapse_ukraine_focus_tree` full coordinate rebuild. Anchor around `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_army_of_the_republic`, and `ukr_soviet_collapse_open_the_liaison_offices`; reduce the 33 long prerequisite lines and isolate Black Banner/high-chaos branch.

2. `common/national_focus/005_soviet_collapse_republics.txt` - Ukraine political branch payoffs. Targets: `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_protectorate_debate`, `ukr_soviet_collapse_the_directory_state`. Add mutually visible route locks, leader/cosmetic/decision consequences, and route-specific AI.

3. `common/national_focus/005_soviet_collapse_republics.txt` - Ukraine League/external expansion branch. Targets: `ukr_soviet_collapse_league_founding_charter`, `ukr_soviet_collapse_kyiv_leads_the_front`, `ukr_soviet_collapse_external_border_arbitration`, `ukr_soviet_collapse_league_security_zone_mandates`, `ukr_soviet_collapse_great_steppe_and_sea_plan`. Tie rewards to League decisions, external security war goals, postwar settlement, and Black Sea route consequences.

4. `common/national_focus/005_soviet_collapse_republics.txt` - Ukraine Black Banner/high-chaos route. Targets: `ukr_soviet_collapse_bread_state_whispers`, `ukr_soviet_collapse_black_soil_oath`, `ukr_soviet_collapse_dead_fields_living_columns`, `ukr_soviet_collapse_no_one_leaves_the_bread_line`, `ukr_soviet_collapse_the_commune_war`, `ukr_soviet_collapse_the_double_republic`, `ukr_soviet_collapse_last_harvest_plan`. Make it visibly overpowered and dangerous with assault columns, neighbor wars, food-state penalties, and route-specific failure costs.

5. `common/national_focus/005_soviet_collapse_republics.txt` - `soviet_collapse_belarus_focus_tree` coordinate rebuild. Targets: `blr_soviet_collapse_the_rail_map_on_the_wall`, `blr_soviet_collapse_which_road_is_belarus`, `blr_soviet_collapse_forest_defense_staff`, `blr_soviet_collapse_timetable_state`, `blr_soviet_collapse_foreign_corridor_administration`. Remove 36 long prerequisite jumps.

6. `common/national_focus/005_soviet_collapse_republics.txt` - Belarus rail/corridor branch. Targets: `blr_soviet_collapse_seal_the_minsk_junction`, `blr_soviet_collapse_timetable_state`, `blr_soviet_collapse_every_track_through_minsk`, `blr_soviet_collapse_minsk_central_dispatch`, `blr_soviet_collapse_armored_train_workshops`, `blr_soviet_collapse_the_league_depot_at_minsk`. Add rail authority, armored train, supply network, and corridor-control decisions.

7. `common/national_focus/005_soviet_collapse_republics.txt` - Belarus forest-state branch. Targets: `blr_soviet_collapse_forest_committees_report_in`, `blr_soviet_collapse_forest_defense_staff`, `blr_soviet_collapse_partisans_or_army`, `blr_soviet_collapse_regular_forest_brigades`, `blr_soviet_collapse_decentralized_detachments`, `blr_soviet_collapse_the_forest_general_staff`, `blr_soviet_collapse_a_forest_that_can_govern`. Add forest decisions, ambush/defense modifiers, hidden stockpiles, and a real forest-government end state.

8. `common/national_focus/005_soviet_collapse_republics.txt` - `soviet_collapse_breakaway_focus_tree` route depth. Targets: `soviet_collapse_the_republic_defines_itself`, `soviet_collapse_socialist_sovereignty_committee`, `soviet_collapse_route_consolidation_congress`, `soviet_collapse_republican_survival_pact`, `soviet_collapse_a_republic_worth_naming`. Add generic but meaningful expansion, diplomacy, industry, and League/foreign decision unlocks.

9. `common/national_focus/005_soviet_collapse_republics.txt` - `soviet_collapse_internal_republic_focus_tree` branch family split. Targets: `internal_soviet_collapse_write_the_autonomy_statute`, `internal_soviet_collapse_forest_republic_committees`, `internal_soviet_collapse_volga_oil_and_workshops`, `internal_soviet_collapse_siberian_rail_authorities`, `internal_soviet_collapse_trade_oaths_with_neighbors`. Create regional branch payoffs instead of one broad internal-republic helper rhythm.

10. `common/national_focus/005_soviet_collapse_republics.txt` - Kazakhstan layout and fork cleanup. Targets: `kaz_soviet_collapse_the_congress_chooses_a_past`, `kaz_soviet_collapse_alash_memory_restored`, `kaz_soviet_collapse_socialist_steppe_republic`, `kaz_soviet_collapse_resource_defense_directorate`, `kaz_soviet_collapse_turkestan_federation_mandate`. Reduce 43 long links and make each route family visually distinct.

11. `common/national_focus/005_soviet_collapse_republics.txt` - Baltic mutual-exclusion layout. Targets: `baltic_soviet_collapse_legal_continuity_government`, `baltic_soviet_collapse_military_border_government`, `baltic_soviet_collapse_foreign_protection_council`, `baltic_soviet_collapse_baltic_league_first`. Fix the `dx = 8-12` mutual-exclusion lines and deepen legal/military/foreign branch payoff.

12. `common/national_focus/005_soviet_collapse_republics.txt` - Moldova vertical pathline collision. Targets: `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_western_training_mission`, `moldova_soviet_collapse_southern_rail_timetables`. Move or reroute so the focus no longer sits on the vertical prerequisite line; add Dniester/Romanian/Western decision mechanics.

13. `common/national_focus/005_soviet_collapse_factory_successors.txt` - `CFR_soviet_collapse_focus_tree` overpowered construction directorate. Targets: `CFR_count_the_cranes`, `CFR_the_unfinished_city_speaks`, `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`, `CFR_the_builder_state`, `CFR_civilian_hegemony_project`. Add map-building decisions, mandate scaling, and route-specific construction programs.

14. `common/national_focus/005_soviet_collapse_factory_successors.txt` - `MFR_soviet_collapse_focus_tree` arsenal state. Targets: `MFR_who_owns_the_rifle`, `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, `MFR_eternal_arsenal`, `MFR_arm_the_new_russia`, `MFR_factory_war_cabinet`. Add client arms contracts, production-line consequences, war goals, and unsafe-output escalation.

15. `common/national_focus/005_soviet_collapse_factory_successors.txt` - `OGB_soviet_collapse_focus_tree` full branch expansion. Targets: `OGB_restore_the_bolghar_name`, `OGB_scholars_guard_the_charter`, `OGB_clerics_guard_the_charter`, `OGB_reopen_volga_trade_tolls`, `OGB_claim_the_old_trade_cities`, `OGB_answer_the_idel_ural_question`. Expand from 23 focuses toward real politics, trade, military, diplomacy, and expansion.

16. `common/national_focus/005_soviet_collapse_custom_splinters.txt` - `PRA_soviet_collapse_focus_tree` rail-country power pass. Targets: `PRA_armored_train_schools`, `PRA_claim_the_branch_lines`, `PRA_seize_the_junction_cities`, `PRA_rails_over_capitals`, `PRA_the_pale_line_endures`; helpers `soviet_collapse_update_pra_authority_idea`, `soviet_collapse_build_pra_corridor_network`. Add rail war goals, moving-state authority, and stronger rail infrastructure sprawl.

17. `common/national_focus/005_soviet_collapse_custom_splinters.txt` - `DSC_soviet_collapse_focus_tree` dead-army escalation. Targets: `DSC_claim_the_soldiers_road`, `DSC_armies_that_do_not_demobilize`, `DSC_congress_of_the_dead_army`, `DSC_the_dead_army_votes_forward`; helpers `soviet_collapse_dsc_claim_front_road_states`, `soviet_collapse_dsc_core_controlled_front_road_states`, `soviet_collapse_dsc_launch_dead_army_neighbor_wars`. Remove duplicate condition clutter while making route more dangerous.

18. `common/national_focus/005_soviet_collapse_custom_splinters.txt` - compact special trees `TSC`, `RMC`, `NRF`, `ICD`. Targets: their `*_endgame`, `*_hidden_doctrine`, and high-chaos route focuses. Add unique overpowered mechanics: observatory shock/network for `TSC`, martyr/death manpower for `RMC`, revenant naval raids for `NRF`, death-commissariat repression/war for `ICD`.

19. `common/national_focus/005_soviet_collapse_custom_splinters.txt` - copied 47-focus custom splinter template de-duplication. Targets: repeated route ids `*_political_route_reward_tt`, `*_first_guard`, `*_stores`, `*_legitimacy`, `*_doctrine`, `*_league`, `*_enemy_front`, `*_industry_plan`, `*_hidden_doctrine`, `*_extreme_gate`. Convert at least the first pass for `UDC`, `SDZ`, `UWD`, `FEV`, `SZA`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`, `DHC`, `KHC` into tag-specific mechanics.

20. `common/national_focus/005_soviet_collapse_ancient_restorations.txt` - ancient restorations branch expansion. Targets: `KZR_symbolic_crossing_state`, `KZR_expansionist_steppe_levy`, `SOG_symbolic_city_league`, `SOG_expansionist_merchant_claims`, `KHW_symbolic_oasis_authority`, `KHW_expansionist_water_claims`, `ALN_symbolic_pass_principality`, `ALN_expansionist_mountain_claims`, plus all `*_returned_names_endgame`. Expand beyond 16-focus compact trees and make old-border restoration mechanically excessive.

## Validation Commands Run

```bash
sed -n '1,260p' AGENTS.md
sed -n '1,260p' .agents/skills/hoi4-focus-trees/SKILL.md
sed -n '1,260p' .agents/skills/chaos-redux-events/SKILL.md
sed -n '1,220p' 'paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md'
sed -n '1,220p' 'paradox_wiki/Effect - Hearts of Iron 4 Wiki.md'
sed -n '1,220p' 'paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md'
sed -n '1,220p' 'paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md'
sed -n '1,220p' 'paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md'
sed -n '1,180p' 'paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md'
sed -n '1,180p' 'paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md'
sed -n '1,160p' 'paradox_wiki/On actions - Hearts of Iron 4 Wiki.md'
sed -n '1,140p' 'paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md'
sed -n '1,140p' 'paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md'
sed -n '1,160p' 'paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md'
sed -n '1,180p' 'paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md'
rg -n "national_focus|load_focus_tree|mark_focus_tree_layout_dirty|focus = \\{|ai_will_do|script constants|script_constants" '/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md' '/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md' '/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md' '/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md'
sed -n '1,160p' '/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt'
sed -n '6300,6460p' '/home/klim/projects/Hearts of Iron IV/common/national_focus/mexico.txt'
wc -l common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
python3 - <<'PY'
# Parsed the four scoped focus files for focus_tree ids, focus ids, completion_reward helper usage, duplicates, ai_will_do presence, prerequisites, mutual exclusions, and resolved relative coordinates.
PY
python3 - <<'PY'
# Brace-depth validation on the four scoped focus files.
PY
rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
git status --short
```

Validation results:

- Brace depth check passed for all four focus files:
  - `005_soviet_collapse_republics.txt`: `final_depth=0`, `min_depth=0`, `negatives=0`
  - `005_soviet_collapse_custom_splinters.txt`: `final_depth=0`, `min_depth=0`, `negatives=0`
  - `005_soviet_collapse_factory_successors.txt`: `final_depth=0`, `min_depth=0`, `negatives=0`
  - `005_soviet_collapse_ancient_restorations.txt`: `final_depth=0`, `min_depth=0`, `negatives=0`
- Unsupported operator scan for `<=` and `>=`: no matches in the four scoped focus files.
- Parsed focus count: 1,698.
- Parsed focus trees: 43.
- Parsed focuses missing `ai_will_do`: 0.
- Coordinate scan found no occupied resolved cells and no same-row `dx = 1` focus pairs.

No HOI4 runtime launch, screenshot validation, or in-game focus-tree validation was run in this read-only audit.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`

No skills were created or updated.

## Completion Status

This handoff is a current-state audit and parent-agent implementation plan. It does not complete the requested full rework of Event005 focus trees. No focus files, localisation files, decision files, scripted effects, assets, or flag files were modified by this audit.
