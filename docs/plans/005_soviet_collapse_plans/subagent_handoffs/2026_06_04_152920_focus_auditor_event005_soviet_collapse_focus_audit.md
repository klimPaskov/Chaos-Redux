# Event005 Soviet Collapse Focus Audit Handoff

Audit mode: read-only. No focus files, flags, `gfx/flags`, `interface/flags`, or sprite definitions were edited.

## Scope and Reference

Audited these focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Reference files opened before auditing:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- Vanilla focus precedents sampled from `common/national_focus/finland.txt`, `france.txt`, `spain.txt`

## Current-State Validation Summary

- Parsed 41 focus trees and 1698 focus blocks across the four Event005 focus files.
- No duplicate focus IDs found.
- No focus blocks missing `search_filters`.
- No focus blocks missing `ai_will_do`.
- No direct `add_ideas`, `add_timed_idea`, `swap_ideas`, `modify_idea`, or `remove_ideas` calls remain in the four focus files.
- No `<=` or `>=` operators found in the four focus files.
- Current issue is not direct duplicate `add_ideas` in focuses. It is repeated generic helper/tooltips, large batches of flat/stat rewards, helper-driven idea lifecycle risk, missing route-specific decisions/payoffs, and remaining layout conflicts.

## Top 20 Issues To Patch First

1. **Generic custom-splinter route rewards are still the dominant design surface.** `soviet_collapse_custom_splinter_political_route_reward_tt` appears on 115 focuses, e.g. `FTH_legitimacy` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:99`, `FTH_rival` at line 122, `UDC_legitimacy` at line 10162, and `UDC_rival` at line 10184. Replace repeated generic tooltip/helper calls with route-specific focus effects and localised tooltips that name the actual institution, decision unlock, war route, construction mandate, rail authority, or death-state payoff.

2. **FTH tree is a 47-focus generic scaffold with no decision unlocks and no direct war/claim/core payoff.** Examples: `FTH_first_guard` line 52, `FTH_stores` line 76, `FTH_legitimacy` line 99, `FTH_enemy_front` line 307, `FTH_hidden_doctrine` line 891, `FTH_extreme_gate` line 915. Replace at least one political branch, one expansion branch, and one special branch with concrete decisions/wargoals/cores/units/map changes, not only shared custom-splinter helper calls.

3. **UDC tree repeats the same generic custom-splinter scaffold despite being a union-defense actor.** `UDC_birth` line 10100, `UDC_first_guard` line 10122, `UDC_stores` line 10144, `UDC_legitimacy` line 10162, `UDC_doctrine` line 10206. It has 47 focuses, 0 decision unlocks, 0 direct wargoals/claims/cores, and only 6 direct building effects. Add command-state decisions, front supply missions, conscription/war plans, and route-specific AI strategy.

4. **Many 47-focus custom splinter trees have zero decision unlocks.** Affected tree starts include `BBH_soviet_collapse_focus_tree` line 7680, `KRS_soviet_collapse_focus_tree` line 8875, `UDC_soviet_collapse_focus_tree` line 10100, `SDZ_soviet_collapse_focus_tree` line 11290, `GAC_soviet_collapse_focus_tree` line 12530, `DHC_soviet_collapse_focus_tree` line 13700, `KHC_soviet_collapse_focus_tree` line 14899, `FEV_soviet_collapse_focus_tree` line 16088, `SZA_soviet_collapse_focus_tree` line 17256, `UWD_soviet_collapse_focus_tree` line 18420, `MRC_soviet_collapse_focus_tree` line 19607, `IUL_soviet_collapse_focus_tree` line 20780, `BAC_soviet_collapse_focus_tree` line 21920. Give each concept at least a small decision family tied to its identity.

5. **High-chaos helper can double-apply generic expansion payloads to red-martyr and iron-commissariat successors.** In `common/scripted_effects/005_soviet_collapse_effects.txt:10703`, `soviet_collapse_apply_high_chaos_focus_identity_payload` has explicit RMC/ICD blocks but the final fallback `NOT = { OR = { ... } }` list excludes neither `soviet_collapse_red_martyrs_successor` nor `soviet_collapse_iron_commissariat_successor`. Add those flags to the fallback exclusion or guard the fallback with a one-time payload flag.

6. **Ukraine still has same-row crowding in the diplomacy/naval lane.** `ukr_soviet_collapse_open_the_liaison_offices` at `common/national_focus/005_soviet_collapse_republics.txt:210` sits at `(25,5)`, one x-step from `ukr_soviet_collapse_black_sea_port_ledgers` at line 1204 `(24,5)`. Shift the naval/port branch down or right so the pathline and icons do not read as one branch.

7. **Ukraine socialist/military route cluster is too tight.** `ukr_soviet_collapse_peasant_socialist_congress` line 333 `(15,7)` is one step from `ukr_soviet_collapse_coalition_of_three_ministries` line 805 `(14,7)`, and `ukr_soviet_collapse_workers_congress_in_kharkiv` line 351 `(16,8)` is one step from `ukr_soviet_collapse_army_supremacy` line 639 `(15,8)`. Shift the socialist branch left/up or the army branch right/down; also replace repeated socialist helper calls with distinct worker/peasant decision unlocks.

8. **Ukraine black-banner/bread-state area is visually tangled.** `ukr_soviet_collapse_the_ukrainian_commune_debate` line 481 `(22,13)` is one step from `ukr_soviet_collapse_the_bread_line_becomes_a_border` line 1998 `(23,13)` and `ukr_soviet_collapse_black_banner_takes_the_villages` line 2204 `(21,13)`. Separate the high-chaos bread-state route from the commune route, and make the bread branch unlock/upgrade bread-state decisions instead of only flags, stability, and generic high-chaos helpers.

9. **Ukraine has route focuses that still feel like stat stamps.** `ukr_soviet_collapse_moscows_officers_in_our_barracks` line 191 only sets `soviet_collapse_ukraine_officer_question_open` and grants army XP. Replace with officer-purge/patronage decisions, a commander/advisor unlock, or a civil-military pressure value change visible in later focuses.

10. **Moldova has a concrete pathline blocker.** `moldova_soviet_collapse_moldova_route_fork` line 7636 `(12,2)` links vertically to `moldova_soviet_collapse_river_guard_brigades` line 7759 `(12,5)`, crossing `moldova_soviet_collapse_ukrainian_border_compact` line 7736 `(12,3)`. Move `river_guard_brigades` to x 10 or 14, or make it branch from the specific route focus instead of from the route fork.

11. **Belarus has a concrete long pathline blocker.** `blr_soviet_collapse_state_between_armies` line 8853 `(19,4)` links vertically to `blr_soviet_collapse_join_the_league_when_war_comes` line 9688 `(19,10)`, crossing `blr_soviet_collapse_orders_printed_like_timetables` line 9043 `(19,9)`. Move the league focus to x 17/21 or split the prerequisite through the timetable branch.

12. **Belarus rail/political lanes are still too close.** `blr_soviet_collapse_socialist_autonomy_without_moscow` line 8899 `(14,5)` is one step from `blr_soviet_collapse_last_train_east` line 9358 `(15,5)`. `blr_soviet_collapse_railway_guard_regiments` line 9285 `(4,7)` is one step from `blr_soviet_collapse_every_track_through_minsk` line 9811 `(3,7)`. Shift the rail lane away from political route locks; add route-specific rail decisions for guard regiments and corridor control.

13. **Central Asia has remaining same-row crowding.** `central_asia_soviet_collapse_desert_scout_columns` line 6810 `(7,6)` is one step from `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` line 7326 `(6,6)`. `central_asia_soviet_collapse_bishkek_pass_council` line 6892 `(8,8)` is one step from `central_asia_soviet_collapse_khwarazm_restoration_debate` line 7374 `(9,8)`. `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` line 7067 `(4,4)` is one step from `central_asia_soviet_collapse_the_cotton_question` line 7153 `(3,4)`. Shift the restoration/Basmachi/cotton lanes apart.

14. **Internal republic tree still has too-close route nodes.** `internal_soviet_collapse_border_and_rail_liaisons` line 3255 `(10,5)` is one step from `internal_soviet_collapse_ural_cavalry_roads` line 3580 `(9,5)`. `internal_soviet_collapse_crimean_tatar_councils` line 3821 `(20,5)` is one step from `internal_soviet_collapse_taiga_steppe_self_rule` line 4022 `(21,5)`. Move side branches so internal breakaways read as separate options.

15. **Custom splinter UDC has a same-row spacing issue.** `UDC_radio_command_posts` line 10505 `(2,9)` is one step from `UDC_signal_truck_yards` line 10995 `(3,9)`. Shift one branch and use the opportunity to give the signal-truck focus an actual mobile-command decision or unit spawn.

16. **Generic breakaway tree is still under-mechanised.** `soviet_collapse_route_consolidation_congress` at `common/national_focus/005_soviet_collapse_republics.txt:2581` only sets a flag and gives PP/stability. The whole `soviet_collapse_breakaway_focus_tree` has 36 focuses, 0 decision unlocks, 0 direct wargoals/cores/claims, and only 2 direct equipment effects. Add route-specific consolidation decisions, defensive league missions, and postwar settlement hooks.

17. **Ukraine expansion branch has almost no direct map payload in focus file.** The Ukraine tree has 83 focuses, 13 decision unlocks, but 0 direct wargoals, cores, or claims. Examples that should carry map payoff: `ukr_soviet_collapse_direct_national_claims` line 1721, `ukr_soviet_collapse_breadbasket_empire` line 1777, `ukr_soviet_collapse_great_steppe_and_sea_plan` line 1889. Add visible claim/core/war-goal decisions or hidden effects with custom tooltip describing exact target regions.

18. **Belarus concept payoffs are not strong enough for a rail/corridor state.** The tree has 53 focuses but 0 direct equipment, 0 wargoal/claim/core effects, and only 12 direct building effects. Strengthen `blr_soviet_collapse_the_corridor_everyone_wants` line 9760, `blr_soviet_collapse_prepare_league_freight_tables` line 9637, and `blr_soviet_collapse_minsk_supplies_the_front` line 9737 with rail/supply decisions, train equipment, supply hub/rail construction, and AI building strategies.

19. **Kazakhstan is large but still under-connected to map/war decisions.** The tree has 92 focuses, 6 decision unlocks, 0 direct wargoals/cores/claims, and 28 flat stat effects. `kaz_soviet_collapse_the_congress_chooses_a_past` line 10089 is a key route identity focus but still mostly custom tooltip + generic payoff. Add Alash/steppe/cosmodrome route decisions, claims or settlement missions, and route-specific AI.

20. **Filters and AI are present but too generic in many custom splinters.** Validation found every focus has `search_filters` and `ai_will_do`, but most custom splinter AI is only `base` plus broad war/chaos/SOV pressure modifiers. Trees with 0 `add_ai_strategy` include FTH line 31, BSC line 4316, TNC line 5437, ALA line 6568, BBH line 7680, KRS line 8875, UDC line 10100, SDZ line 11290, and most other 47-focus splinters. Add route-specific AI strategies for construction actors, rail actors, naval actors, and death/war actors.

## Duplicate / Spam Ideas

- Direct duplicate focus idea application was not found in the four focus files. `rg` found no `add_ideas`, `add_timed_idea`, `swap_ideas`, `modify_idea`, or `remove_ideas` in these focus files.
- Remaining idea-lifecycle risk is helper-side. `soviet_collapse_clear_republic_staged_ideas` in `common/scripted_effects/005_soviet_collapse_effects.txt:5559` removes a very large list of staged republic ideas, and `soviet_collapse_update_pra_authority_idea` at line 7795 swaps among PRA authority ideas. This is better than focus-level spam but should be reviewed when a route focus calls the same staged helper repeatedly.
- Concrete replacement direction: keep one staged idea per institution family, update it through one documented scripted effect, and make focus tooltips say the institution evolves rather than exposing raw repeated idea changes.

## Shallow / Generic Rewards

- Generic custom-splinter tooltip reuse remains very high: political 115 uses, logistics 41, industrial 40, expansion 39, military 38, diplomacy 38, high-chaos 24, doctrine 19, league 19, hidden doctrine 19.
- Many custom splinter focuses are concept-labeled but resolve to the same helper pattern. Examples: `FTH_first_guard` line 52, `FTH_stores` line 76, `FTH_legitimacy` line 99, `UDC_first_guard` line 10122, `UDC_stores` line 10144, `UDC_doctrine` line 10206.
- Replacement direction: use shared helpers only as payload primitives. Each focus should add at least one concrete identity-facing thing: unlock a decision, spawn a unit, add train/ship/equipment stockpile, add a named building package, create a claim/core/wargoal path, alter a visible variable, change leader/advisor/law, or define AI strategy.

## Branches Disconnected From Mechanics

- The worst disconnect is custom splinter decision scarcity. Many 47-focus trees have 0 decision unlocks despite existing decision categories for splinter authorities.
- Republic examples: the generic breakaway tree has 0 decisions; internal republic has 0 decisions; Baltic has 0 decisions; Moldova has 0 decisions despite route category support elsewhere.
- Replacement direction: each route family should unlock a staged decision family. Political routes unlock legitimacy/recognition decisions; industry routes unlock construction or factory mandates; rail routes unlock rail/supply decisions; naval routes unlock shipyard/fleet actions; death/war routes unlock coring, war, recruitment, and unit-spawning decisions.

## Layout / Pathline Conflicts

- Exact blockers: Moldova route fork to river guard crosses Ukrainian border compact; Belarus state-between-armies to league focus crosses orders-printed-like-timetables.
- Same-row close pairs found: 17 within-tree one-x-step conflicts. Worst user-visible clusters are Ukraine, Belarus, Central Asia, Moldova, Internal Republic, and UDC.
- Replacement direction: shift branches by at least two x units or one y layer, and avoid long vertical prerequisite lines through unrelated focuses. For pathline-through-route-lock cases, make the route-specific focus a real prerequisite instead of drawing through it.

## Missing Chaos-Country Concept Payoffs

- Construction/civilian factory actors need more repeated civilian industry and construction mandate decisions. CFR has 47 focuses and 12 decisions, but only 3 direct building effects in the focus file; confirm helper-side payload is enough or add visible public works/building decisions to more focuses.
- Death-state actors are better than before in DSC/NRF, but RMC and ICD still show only 1 decision unlock each and depend heavily on helper payloads. They should get visible recruitment, assault-column, cores/claims, and neighbor-war decision chains.
- Rail actors should be judged against PRA: PRA has 14 decisions and 23 building effects; Belarus and many rail-adjacent splinters are weaker and should borrow PRA-style rail/supply decision staging.
- Naval actors should build ships and naval bases directly. NRF has 6 decisions and 10 building effects; other coastal/naval splinters should be checked against it.

## Filters / Localisation / AI Concerns

- Filters: technically present everywhere.
- Localisation: repeated generic tooltip keys make many custom splinter focuses read alike even when focus IDs are distinct.
- AI: `ai_will_do` exists everywhere, but route-specific `add_ai_strategy` is absent in most custom splinter trees. Add explicit `building_target`, `conquer`, `antagonize`, `support`, `alliance`, or faction strategies where route identity demands it.

## Commands Run

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `sed -n` reads for `AGENTS.md`, `hoi4-focus-trees/SKILL.md`, offline wiki pages, vanilla docs, and sampled focus blocks.
- `find '/home/klim/projects/Hearts of Iron IV/common/national_focus' -maxdepth 1 -type f | head -20`
- `rg -n "search_filters|mutually_exclusive|ai_will_do|custom_effect_tooltip|unlock_decision_tooltip|unlock_decision_category_tooltip"` on vanilla focus examples.
- `wc -l` on the four Event005 focus files.
- Python parser over the four focus files for focus-tree counts, duplicate IDs, filters, AI, reward metrics, repeated tooltip keys, same-coordinate overlaps, close same-row pairs, and vertical blockers.
- `rg -n "add_ideas|add_timed_idea|swap_ideas|modify_idea|remove_ideas"` on the four focus files.
- `rg -n "<=|>="` on the four focus files.
- `git status --short`

## Simplifications, Omissions, And Blockers

- No patches were made; this is an audit handoff only.
- I did not inspect flags or flag sprites and did not touch `gfx/flags` or `interface/flags`.
- I did not claim Event005 focus work is complete. This report identifies current blockers for the parent rework.
