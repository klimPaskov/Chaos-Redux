# Event005 Soviet Collapse Focus Tree Full-Rework Gap Audit

Subagent: `chaosx_focus_tree_auditor`
Date: 2026-06-05
Scope: audit only, no gameplay patch

## References Consulted

- Repo skill: `hoi4-focus-trees`
- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`
- Current Event005 focus files and helpers under `common/national_focus/`, `common/scripted_effects/`, `common/scripted_triggers/`, `common/ideas/`, and Event005 decisions

## Patch Decision

No gameplay patch was made.

The current focus files do not directly call `add_ideas`, `add_timed_idea`, `swap_ideas`, or `remove_ideas`. The old-looking "same idea spam" problem is now mostly repeated scripted reward helper use and long bundled reward effects, not direct duplicate idea additions inside focus rewards. Coordinate-only fixes are technically possible, but the visible pathline problems are broad and interconnected across route forks, branch capstones, and mutually exclusive lanes. A small coordinate edit in one hotspot would likely move crossings into adjacent branches while the parent is actively reworking release/scenario/chaos progression.

No flag sprites were touched.

## Priority Findings

### 1. Ukraine

File: `common/national_focus/005_soviet_collapse_republics.txt`
Tree: `soviet_collapse_ukraine_focus_tree`
Current size: 83 focuses

Ukraine has all required branch families now: political route locks, depot/industry, military, foreign/diplomacy, League/expansion, and high-chaos bread-state mechanics. The issue is not missing content. It is cluttered layout, repeated helper rewards, and too many cross-branch convergence lines.

| Focus ids | Current issue | Recommended replacement or rework | Safe for parent to patch now |
|---|---|---|---|
| `ukr_soviet_collapse_guard_the_telegraph_house`, `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_village_granary_guards`, `ukr_soviet_collapse_dnieper_workshops` | Early trunk pathlines cut through the grain/depot branch. `question_of_statehood` acts as a political fork but visually crosses industrial child lines. | Move political trunk and depot children into separate vertical lanes, or add a visible converger before `question_of_statehood` if it is meant to represent control over both telegraph and grain ledgers. | Yes, coordinate-only batch after focus file freeze. |
| `ukr_soviet_collapse_first_republican_line`, `ukr_soviet_collapse_war_without_a_declaration`, `ukr_soviet_collapse_foreign_courts_notice_kyiv`, `ukr_soviet_collapse_depot_motor_columns`, `ukr_soviet_collapse_arsenal_cities`, `ukr_soviet_collapse_army_of_the_republic` | Military, foreign recognition, and depot lines cross each other. The player cannot scan the tree as separate army, industry, and diplomacy branches. | Reserve one clear military lane for officer/army focuses, one depot lane for arsenal/workshop focuses, and one diplomacy lane for recognition/adviser focuses. Avoid diagonal prerequisite lines between those lanes unless the focus is a deliberate capstone. | Yes for coordinates. Reward changes should wait for route design. |
| `ukr_soviet_collapse_open_the_liaison_offices`, `ukr_soviet_collapse_foreign_advisers_in_plain_coats`, `ukr_soviet_collapse_black_sea_port_ledgers`, `ukr_soviet_collapse_romanian_port_route`, `ukr_soviet_collapse_advisers_without_flags`, `ukr_soviet_collapse_equipment_corridor_authority`, `ukr_soviet_collapse_romanian_grain_and_river_bargain`, `ukr_soviet_collapse_carpathian_security_belt`, `ukr_soviet_collapse_ports_need_soldiers` | Foreign/port/protectorate pathlines cross. The lane also repeats `soviet_collapse_apply_focus_foreign_channel` many times, making several rewards feel mechanically similar. | Collapse the diplomacy lane into staged payoffs: liaison offices, port corridor, equipment corridor, protectorate or independent foreign line. Replace some helper-only rewards with existing Ukraine external mandate or Black Sea security decision unlocks. | No for reward rewrite. Yes for a coordinated layout pass. |
| `ukr_soviet_collapse_bread_state_whispers`, `ukr_soviet_collapse_black_soil_oath`, `ukr_soviet_collapse_dead_fields_living_columns`, `ukr_soviet_collapse_grain_census_of_everyone`, `ukr_soviet_collapse_no_one_leaves_the_bread_line`, `ukr_soviet_collapse_last_harvest_plan`, `ukr_soviet_collapse_black_banner_takes_the_villages`, `ukr_soviet_collapse_the_double_republic`, `ukr_soviet_collapse_the_commune_war` | The high-chaos bread-state route is conceptually strong, but it sits near other late branches and adds scan pressure. | Keep the route. Give bread-state its own vertical late-game column, with black-banner/commune outcomes offset into clear mutually exclusive lanes. | Yes for coordinates. No content patch needed. |

Repeated helper hotspots:

- `soviet_collapse_apply_focus_foreign_channel` appears heavily in Ukraine foreign focuses.
- `soviet_collapse_apply_focus_military_consolidation` repeats through army focuses.
- `soviet_collapse_apply_focus_depot_and_supply_control` repeats through depot/industry focuses.

The repeated helpers are not invalid, but they make rewards feel like a stack of similar incremental modifiers. Ukraine would benefit from fewer helper-only focuses and more branch-specific unlocks, missions, claims, guarantees, divisions, factories, or external mandate decisions.

### 2. Kazakhstan

File: `common/national_focus/005_soviet_collapse_republics.txt`
Tree: `soviet_collapse_kazakhstan_focus_tree`
Current size: 92 focuses

Kazakhstan has a large tree with political identity, resource industry, southern federation, diplomacy, military, and expansion elements. It is the clearest example of "large but cluttered": too many branches converge into hidden gates, and several reward lanes repeat the same helper families.

| Focus ids | Current issue | Recommended replacement or rework | Safe for parent to patch now |
|---|---|---|---|
| `kaz_soviet_collapse_the_congress_chooses_a_past` | The focus has several early prerequisites represented in one prerequisite block, while availability logic models "two of three" behavior. This produces misleading pathlines and a route fork that appears to cut across unrelated early lanes. | Split the fork into visible combination focuses, such as resource congress, steppe congress, and security congress, or place the fork directly below the relevant early converger. Use focus layout to show the intended two-of-three requirement. | No without route-layout design approval. |
| `kaz_soviet_collapse_the_steppe_arsenal` | This focus behaves like a major military-industrial capstone but is gated by resource, foreign, and federation conditions. The pathing makes it feel like a hidden cross-branch checkpoint rather than a clean army branch payoff. | Make it a visible military-industrial capstone reached from rail/resource industry. Move southern federation and foreign concession checks into optional bonuses, decisions, or separate focuses. | No, reward and route semantics would change. |
| `kaz_soviet_collapse_the_steppe_outlives_the_union` | This final capstone requires route identity, southern republic diplomacy, defense council, multi-vector recognition, arsenal, army, and resource sovereignty. It over-converges the whole tree. | Split into three late capstones: resource sovereignty, steppe federation, and mobile army. Then gate the final endgame on two or three clearly visible capstones. | No, broad route rewrite. |
| `kaz_soviet_collapse_league_resource_pool`, `kaz_soviet_collapse_foreign_technical_missions`, `kaz_soviet_collapse_call_the_steppe_congress`, `kaz_soviet_collapse_steppe_defense_council`, `kaz_soviet_collapse_multi_vector_recognition` | Diplomacy, League, and federation rewards are present but visually interwoven with resource and military lanes. | Separate diplomacy/federation into a right-side branch. Keep foreign technical missions as diplomacy/industry bridge, but avoid making it a hidden prerequisite for military payoff. | Yes for coordinates only. |
| `kaz_soviet_collapse_karaganda_coal_accounting`, `kaz_soviet_collapse_emergency_oil_boards`, `kaz_soviet_collapse_copper_and_chrome_ledgers`, `kaz_soviet_collapse_industrial_settlement_compacts`, `kaz_soviet_collapse_resource_sovereignty` | Resource branch is thematically strong but reward cadence relies on repeated depot/supply and resource helper patterns. | Replace some generic helper-only rewards with existing Kazakhstan decisions such as minehead guard contracts, foreign concession audits, steppe supply plans, or Alash court commissions where appropriate. | No until parent chooses which route gets which mechanic. |

Repeated helper hotspots:

- `soviet_collapse_apply_focus_depot_and_supply_control` appears about a dozen times.
- `soviet_collapse_apply_focus_military_consolidation` appears about a dozen times.
- `soviet_collapse_apply_focus_league_preparation` appears heavily in the southern federation lane.

Kazakhstan should remain large, but the final rework should reduce convergence and make "resource state", "steppe army", "southern federation", and "multi-vector recognition" independently readable.

### 3. Belarus

File: `common/national_focus/005_soviet_collapse_republics.txt`
Tree: `soviet_collapse_belarus_focus_tree`
Current size: 53 focuses

Belarus has enough branch material, but it is visually noisy and several mutually exclusive route locks are not as meaningful or legible as the skill guidance expects.

| Focus ids | Current issue | Recommended replacement or rework | Safe for parent to patch now |
|---|---|---|---|
| `blr_soviet_collapse_which_road_is_belarus` | This focus uses multiple prerequisite sources and availability logic that behaves like a combination gate. The pathlines imply broader direct dependency than the player can easily parse. | Replace with visible combination/converger focuses or move the fork directly under the intended route-preparation lane. | No without route-layout design approval. |
| `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, `blr_soviet_collapse_foreign_corridor_administration` | Mutually exclusive structure is partially visible but not symmetrical. Some exclusions appear lore/mechanically meaningful, while others rely on route flags instead of clear visual exclusivity. | Make the four choices a clean meaningful route fork, or split them into two meaningful pairs: national vs socialist legitimacy and military corridor vs foreign corridor. Tooltips should explain route consequences. | No for behavior. Yes if parent only adjusts positions. |
| `blr_soviet_collapse_the_rail_map_on_the_wall`, `blr_soviet_collapse_eastern_line_watch`, `blr_soviet_collapse_timetable_state`, `blr_soviet_collapse_rail_war_state`, `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_minsk_supplies_the_front` | Rail, forest, and League/logistics lanes cross and repeat depot/security helpers. Belarus feels less like distinct political, industry/logistics, military/diplomacy, and expansion branches and more like a braided rail corridor. | Make three clear lanes: forest legitimacy and militia, rail/logistics state, foreign/League corridor. Use League freight and rail war as separate branch capstones. | Yes for coordinated layout. Reward changes should wait. |
| `blr_soviet_collapse_forest_committees_report_in`, `blr_soviet_collapse_first_corridor_guard`, `blr_soviet_collapse_western_corridor_switchmen`, `blr_soviet_collapse_foreign_aid_through_brest` | Early forest/corridor pathlines cross before the player has a clear route identity. | Keep early focuses compact and vertical until the main route fork. Push corridor/foreign aid to a clean right-side diplomacy lane. | Yes for coordinates only. |

Repeated helper hotspots:

- `soviet_collapse_apply_focus_depot_and_supply_control` is overused in rail/logistics focuses.
- `soviet_collapse_apply_focus_security_supply_plan` and `soviet_collapse_apply_focus_legal_recognition` repeat through route branches.

Belarus needs the most careful "meaningful mutex" cleanup among the three priority republics.

## Chaos Country Findings

### CFR - Construction/Civilian Factory Actor

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`
Tree: `CFR_soviet_collapse_focus_tree`
Current size: 47 focuses

CFR is close to the requested standard. It has a clear construction-state concept, strong industry rewards, expansion hooks, and late aggressive capstones such as `CFR_the_state_that_builds`, `CFR_the_builder_state_marches_east`, `CFR_build_the_border_bend_the_border`, `CFR_factories_as_embassies`, `CFR_reconstruction_protectorates`, `CFR_pour_the_final_foundation`, and `CFR_nothing_but_foundations`.

Recommended action: do not replace this tree wholesale. Review layout and make sure construction branch capstones visibly separate civilian construction, border building, and expansion/protectorate mechanics.

Safe for parent to patch now: yes for layout, no urgent reward patch.

### MFR - Military Factory Actor

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`
Tree: `MFR_soviet_collapse_focus_tree`
Current size: 58 focuses

MFR also mostly meets the target. It has a strong arsenal-board trunk, meaningful route split around `MFR_who_owns_the_rifle`, and aggressive factory-war capstones including `MFR_the_arsenal_state`, `MFR_a_rifle_in_every_treaty`, `MFR_every_border_needs_guns`, `MFR_war_market_never_sleeps`, `MFR_workers_own_the_arsenal`, `MFR_state_as_one_arms_order`, `MFR_output_is_victory`, `MFR_arm_all_clients`, and `MFR_no_peace_without_orders`.

Recommended action: keep the concept and rebalance reward presentation. The four ownership routes should each have a distinct payoff, not just more arsenal/factory output.

Safe for parent to patch now: yes for layout and tooltip/reward presentation, no wholesale rewrite.

### OGB

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`
Tree: `OGB_soviet_collapse_focus_tree`
Current size: 23 focuses

OGB has meaningful content but is too small for the requested full-rework standard. It includes scholar vs cleric charter choices and Idel-Ural diplomacy vs conquest, but industry/logistics and military branches are shallow compared with CFR/MFR.

Key focus ids:

- `OGB_open_the_volga_registers`
- `OGB_restore_the_bolghar_name`
- `OGB_scholars_guard_the_charter`
- `OGB_clerics_guard_the_charter`
- `OGB_reopen_volga_trade_tolls`
- `OGB_raise_the_heritage_guard`
- `OGB_treat_with_idel_ural`
- `OGB_the_volga_cannot_have_two_seals`
- `OGB_the_old_name_survives_modern_war`

Recommended action: add a bounded 8-12 focus tranche later: Volga toll logistics, heritage army, Idel-Ural diplomacy/conquest, and future Bulgaria expansion.

Safe for parent to patch now: no, this is new content.

### PRA - Railway Country

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
Tree: `PRA_soviet_collapse_focus_tree`
Current size: 22 focuses

PRA has a strong railway identity but not a full branch structure. It uses the rail authority helper repeatedly and has a meaningful choice between `PRA_the_board_overrules_ministers` and `PRA_armored_train_directorate`, but diplomacy and expansion are too thin for the requested aggressive chaos-country standard.

Key focus ids:

- `PRA_the_timetable_declares_authority`
- `PRA_count_the_locomotives`
- `PRA_timetable_law`
- `PRA_ticket_courts_for_every_platform`
- `PRA_the_board_overrules_ministers`
- `PRA_armored_train_directorate`
- `PRA_repair_crews_without_ministries`
- `PRA_claim_the_branch_lines`

Recommended action: add distinct political/legal, rail logistics, armored train military, and corridor expansion branches. Use rail corridor claims, supply-node control, armored train deployment, and protectorate demands instead of generic helper repetition.

Safe for parent to patch now: no, this is a content expansion.

### DSC - Dead Soldiers Congress

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
Tree: `DSC_soviet_collapse_focus_tree`
Current size: 18 focuses

DSC is mechanically powerful at the opening, especially `DSC_call_the_dead_soldiers_congress`, but it remains a narrow tree. The concept deserves separate political terror, logistics/recovery, military, diplomacy/intimidation, and expansion branches.

Key focus ids:

- `DSC_call_the_dead_soldiers_congress`
- `DSC_stalingrad_roll_call`
- `DSC_voronezh_rearguard_archives`
- `DSC_vote_by_regimental_dead`
- `DSC_witness_officers`
- `DSC_revenant_staff_line`

Recommended action: retain the overpowered opening, then expand with field-hospital logistics, oath courts, front-road claims, and intimidation diplomacy. Make `witness_officers` vs `revenant_staff_line` a major route fork with different military and political consequences.

Safe for parent to patch now: no, broad route expansion.

### NRF - Naval/Revenant Fleet Actor

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
Tree: `NRF_soviet_collapse_focus_tree`
Current size: 18 focuses

NRF is too small for an "extremely overpowered and mechanically aggressive" naval chaos country. Helper use suggests high-chaos identity rewards, but the focus count does not support full political, logistics, navy/diplomacy, and expansion branches.

Recommended action: build a naval directorate branch with port seizures, convoy/submarine warfare, Arctic or northern coast claims, amphibious-raiding bonuses, and maritime terror diplomacy. Existing startup idea wiring is a good foundation; the tree needs dedicated branch depth.

Safe for parent to patch now: no, new content.

### KRS and Other Naval/Port Custom Trees

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
Tree: `KRS_soviet_collapse_focus_tree`
Current size: 47 focuses

KRS has more depth than PRA/DSC/NRF, but reward helper use is heavy and its military/depot lanes need stronger concept separation. If KRS is meant to be the main naval directorate, it should visibly own port assembly, fleet doctrine, maritime diplomacy, and coastal expansion lanes rather than presenting as another generic 47-focus custom skeleton.

Recommended action: keep the 47-focus base but re-label and rewire rewards into port, fleet, diplomacy, and conquest capstones.

Safe for parent to patch now: yes for layout and reward text cleanup, no for route rewrite.

### FEV

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
Tree: `FEV_soviet_collapse_focus_tree`
Current size: 47 focuses

FEV has the expected branch families, but layout is visibly tangled. Known crossing examples include:

- `FEV_settlement` to `FEV_diplomatic_plan` crossing industry and port lines.
- `FEV_hidden_doctrine` to `FEV_extreme_gate` crossing harbor authority and settlement/endgame lines.

Recommended action: make FEV read as a Far Eastern buffer regime: one Vladivostok/port lane, one Trans-Siberian logistics lane, one Japan/China diplomacy lane, and one border-buffer expansion lane. Keep high-chaos assault mechanics for the extreme path.

Safe for parent to patch now: yes for coordinates, no for content.

### NLC

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
Tree: `NLC_soviet_collapse_focus_tree`
Current size: 47 focuses

NLC is powerful but visually cluttered. Known crossing examples include:

- `NLC_league` to `NLC_diplomatic_plan` crossing foreign/enemy-front lines.
- `NLC_inner_faction` to `NLC_special_arm` and `NLC_civil_rule` crossing greenhouse and workshop lines.
- `NLC_station_mediation` to `NLC_winter_guarantees` crossing several adjacent route lines.

Recommended action: split into survival industry, polar diplomacy, special arm/military, and high-chaos endgame lanes. The extreme gate should be a late visible branch, not a diagonal line through mid-tree governance.

Safe for parent to patch now: yes for coordinates, no for content.

## Shared Regional Trees

File: `common/national_focus/005_soviet_collapse_republics.txt`

These trees generally have branch families, but they inherit the same visual problem: wide route forks, diagonal capstones, and pathlines crossing through mutually exclusive or adjacent lanes.

| Tree | Current size | Issue | Recommended action | Safe for parent to patch now |
|---|---:|---|---|---|
| `soviet_collapse_breakaway_focus_tree` | 36 | Smaller shared tree, fewer distinct branch payoffs than priority republics. | If retained as shared tree, keep it simple and avoid pretending every branch is bespoke. Add only regional-specific capstones where tags need them. | Yes for layout, no broad content. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | Volga, Black Sea, Far East, and other identity lanes cross and compete for space. | Split regional identity sub-branches into clearly separated columns with one common trunk. | Yes for coordinates. |
| `soviet_collapse_baltic_focus_tree` | 42 | Legal-state/front-state and port/fleet branches cross. | Separate legality, port logistics, foreign guarantee, and defense front lanes. | Yes for coordinates. |
| `soviet_collapse_caucasus_focus_tree` | 40 | Oil, pipeline guard, foreign guarantees, and route fork lines cross. | Put oil/pipeline logistics in one lane, mountain defense in another, and foreign guarantees at the edge. | Yes for coordinates. |
| `soviet_collapse_central_asia_focus_tree` | 45 | Basmachi, oasis, local republic, and southern route fork lines cross. | Split local republic politics, oasis logistics, Basmachi military, and southern diplomacy. | Yes for coordinates. |
| `soviet_collapse_moldova_focus_tree` | 48 | Highest visible clutter among shared regional trees; Dniester, Prut, Ukraine road, route fork, and diplomacy branches cross repeatedly. | Moldova needs a dedicated layout pass before reward work. Keep Dniester, Prut, Ukraine road, and internal politics in separate lanes. | Yes for coordinates, but should be a focused batch. |

## Reward-Spam Finding

The duplicate idea spam target is not direct `add_ideas` inside focus files. Instead, repeated helper effects create similar-feeling focus rewards:

- `soviet_collapse_apply_focus_foreign_channel`
- `soviet_collapse_apply_focus_military_consolidation`
- `soviet_collapse_apply_focus_depot_and_supply_control`
- `soviet_collapse_apply_focus_legal_recognition`
- `soviet_collapse_apply_focus_league_preparation`
- `soviet_collapse_apply_focus_security_supply_plan`
- `soviet_collapse_apply_focus_high_chaos_identity`
- `soviet_collapse_apply_focus_rail_authority_reward`

These helpers are useful and often contain strong mechanical payloads. The problem is overuse without enough identity-specific payoffs. For the full rework, prefer this pattern:

1. Early branch focus: one helper effect plus route flag/progress.
2. Mid-branch focus: existing decision unlock, state modifier, unit spawn, targeted factories, claims, cores, or foreign relation shift.
3. Branch capstone: route-specific scripted effect with a clear strategic identity.
4. Endgame focus: expansion, war goal, League entry, protectorate system, or high-chaos aggressive mechanic.

## Recommended Patch Queue

Safe coordinate batches after parent freezes focus edits:

1. Ukraine early trunk and Black Sea/foreign lane cleanup.
2. Belarus route fork, forest/rail/corridor separation, and visible mutually exclusive lane cleanup.
3. Kazakhstan route fork and late-capstone visual separation.
4. FEV and NLC high-chaos custom tree pathline cleanup.
5. Moldova shared regional tree pathline cleanup.

Content patches that should wait for parent design:

1. Kazakhstan final capstone split.
2. Belarus meaningful route mutex rewrite.
3. PRA railway country expansion.
4. DSC dead soldiers congress expansion.
5. NRF naval/revenant fleet expansion.
6. OGB Volga/Bolghar expansion tranche.
7. KRS naval-directorate branch identity pass.

## Validation

- No gameplay files were edited.
- No brace-balance check was required for gameplay files because no Clausewitz files were patched.
- No `git diff --check` result is claimed for gameplay files.
- No commit was made, per subagent instructions.

## Simplifications, Omissions, and Blockers

- No broad focus-tree replacement was attempted.
- No coordinate patch was attempted because the crossings are systemic and adjacent to active parent work.
- No duplicate idea reward patch was made because no direct focus-file duplicate `add_ideas` hotspot exists in the current files.
- No flag or sprite changes were made.
- The audit does not claim the Event005 focus tree rework is complete. It identifies patchable gaps for the parent implementation.

## Skills Used

- `hoi4-focus-trees`

No skills were created or updated.
