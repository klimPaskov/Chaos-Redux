# Event005 Focus Tree Current Depth and Integration Audit

Subagent: Chaos Redux focus-tree audit subagent
Timestamp: 2026-06-04 10:51:48 UTC

## Scope and Constraints

Audited the current worktree as authoritative for Event005 Soviet Collapse focus files. The active parent constraints were:

- Event005 Soviet Collapse overhaul is active.
- Focus trees still need depth.
- Avoid idea spam.
- Political, industrial, and expansion branches should be meaningful.
- Chaos countries should be very strong, aggressive, and connected to mechanics.
- Do not inspect or edit `gfx/flags` or `interface/flags`.

No gameplay patches were made. The issues found are mostly structural and would require parent-owned design or implementation tranches rather than safe bounded edits.

## Required References Consulted

Repo skills:

- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`

Repo rules:

- `AGENTS.md`

Offline Paradox wiki snapshot:

- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
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

Vanilla references:

- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`
- Vanilla Finland focus-tree snippets for `ai_will_do`, `search_filters`, mutually exclusive branches, and prerequisite structure.

## Files Audited

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ai_strategy/005_soviet_collapse.txt`

The audit avoided `gfx/flags` and `interface/flags`.

## Validation Commands Run

- `git status --short`
- `wc -l common/national_focus/005_soviet_collapse_*.txt`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_*.txt`
- Brace-aware parser over all Event005 focus files for focus counts, duplicate ids, missing `search_filters`, missing `ai_will_do`, missing `completion_reward`, missing icons, missing/invalid positions, coordinate overlap, helper repetition, direct idea rewards, and weak reward heuristics.
- Brace-aware parser for search-filter reward mismatch candidates and direct decision/mechanic hooks.
- `rg -n "load_focus_tree|soviet_collapse_.*focus_tree|_focus_tree" common history events`
- Targeted `nl -ba` and `sed -n` reads for focus, scripted effect, and AI strategy references.

Validation result highlights:

- 1,698 focus blocks across 41 Event005 focus trees.
- No duplicate focus ids found.
- No missing `search_filters`, `ai_will_do`, `completion_reward`, icons, or valid position blocks found by parser.
- No `<=` or `>=` operators found in Event005 focus files.
- No computed same-coordinate focus overlap found.
- No direct repeated `completion_reward` or `ai_will_do` blocks found.

## Tree Coverage Snapshot

Major and shared trees:

- `soviet_collapse_ukraine_focus_tree`: 83 focuses, `common/national_focus/005_soviet_collapse_republics.txt:18`
- `soviet_collapse_breakaway_focus_tree`: 36 focuses, `common/national_focus/005_soviet_collapse_republics.txt:2314`
- `soviet_collapse_internal_republic_focus_tree`: 62 focuses, `common/national_focus/005_soviet_collapse_republics.txt:3105`
- `soviet_collapse_baltic_focus_tree`: 42 focuses, `common/national_focus/005_soviet_collapse_republics.txt:4571`
- `soviet_collapse_caucasus_focus_tree`: 40 focuses, `common/national_focus/005_soviet_collapse_republics.txt:5530`
- `soviet_collapse_central_asia_focus_tree`: 45 focuses, `common/national_focus/005_soviet_collapse_republics.txt:6435`
- `soviet_collapse_moldova_focus_tree`: 48 focuses, `common/national_focus/005_soviet_collapse_republics.txt:7555`
- `soviet_collapse_belarus_focus_tree`: 53 focuses, `common/national_focus/005_soviet_collapse_republics.txt:8699`
- `soviet_collapse_kazakhstan_focus_tree`: 92 focuses, `common/national_focus/005_soviet_collapse_republics.txt:9986`

Factory and special successor trees:

- `CFR_soviet_collapse_focus_tree`: 47 focuses, `common/national_focus/005_soviet_collapse_factory_successors.txt:16`
- `OGB_soviet_collapse_focus_tree`: 23 focuses, `common/national_focus/005_soviet_collapse_factory_successors.txt:1094`
- `MFR_soviet_collapse_focus_tree`: 58 focuses, `common/national_focus/005_soviet_collapse_factory_successors.txt:1663`

Ancient restoration trees:

- `KZR_soviet_collapse_ancient_focus_tree`: 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:13`
- `SOG_soviet_collapse_ancient_focus_tree`: 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:408`
- `KHW_soviet_collapse_ancient_focus_tree`: 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:797`
- `ALN_soviet_collapse_ancient_focus_tree`: 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1190`

High-chaos and custom splinter trees:

- `FTH_soviet_collapse_focus_tree`: 47 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:15`
- `PRA_soviet_collapse_focus_tree`: 22 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1200`
- `TSC_soviet_collapse_focus_tree`: 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1800`
- `RMC_soviet_collapse_focus_tree`: 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:2269`
- `DSC_soviet_collapse_focus_tree`: 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:2745`
- `NRF_soviet_collapse_focus_tree`: 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3308`
- `ICD_soviet_collapse_focus_tree`: 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3812`
- `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, and `NLC`: 47 focuses each, beginning respectively at `common/national_focus/005_soviet_collapse_custom_splinters.txt:4280`, `:5401`, `:6532`, `:7644`, `:8839`, `:10064`, `:11254`, `:12494`, `:13664`, `:14863`, `:16052`, `:17217`, `:18381`, `:19568`, `:20741`, `:21881`, `:23014`, and `:24213`.

## Findings

### 1. Compact Chaos and Special Trees Are Still Structurally Shallow

Highest priority. Eleven trees are below 25 focuses:

- `OGB_soviet_collapse_focus_tree`, 23 focuses, `common/national_focus/005_soviet_collapse_factory_successors.txt:1094`
- `KZR_soviet_collapse_ancient_focus_tree`, 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:13`
- `SOG_soviet_collapse_ancient_focus_tree`, 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:408`
- `KHW_soviet_collapse_ancient_focus_tree`, 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:797`
- `ALN_soviet_collapse_ancient_focus_tree`, 16 focuses, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1190`
- `PRA_soviet_collapse_focus_tree`, 22 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1200`
- `TSC_soviet_collapse_focus_tree`, 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1800`
- `RMC_soviet_collapse_focus_tree`, 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:2269`
- `DSC_soviet_collapse_focus_tree`, 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:2745`
- `NRF_soviet_collapse_focus_tree`, 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3308`
- `ICD_soviet_collapse_focus_tree`, 18 focuses, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3812`

These trees have local reward wiring, but they do not yet meet the active parent bar for strong/aggressive chaos countries with meaningful political, industrial, military, diplomatic, and expansion routes. The 16-focus ancient trees are especially thin: their restoration premise needs separate political legitimacy, levy/army, relic/industry, external claim, and end-state payoff chains rather than a compressed trunk.

### 2. Direct Idea Spam Is Controlled, But Indirect Idea Lifecycle Must Stay Centralized

The parser did not find direct focus-level `add_ideas` spam in the Event005 focus files. The idea system is mostly centralized in scripted effects:

- `soviet_collapse_update_consolidated_republic_ideas`, `common/scripted_effects/005_soviet_collapse_effects.txt:5708`
- `soviet_collapse_update_pra_authority_idea`, `common/scripted_effects/005_soviet_collapse_effects.txt:7630`
- `soviet_collapse_update_dsc_dead_army_idea`, `common/scripted_effects/005_soviet_collapse_effects.txt:16744`
- Event-created tree startup effects add initial ideas around `common/scripted_effects/005_soviet_collapse_effects.txt:16996` and later.

This is good directionally. Parent should avoid adding more focus-level idea rewards and should route any future idea changes through staged update effects with cleanup.

### 3. Repeated Helper Rewards Risk Same-Feeling Focuses

No exact duplicated `completion_reward` blocks were found, but repeated helper call patterns are heavy enough to create indirect reward sameness:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 138 call sites. Examples: `ukr_soviet_collapse_seal_the_grain_ledgers`, `common/national_focus/005_soviet_collapse_republics.txt:81`; `ukr_soviet_collapse_appointed_governors`, `:917`; `ukr_soviet_collapse_depot_motor_columns`, `:1019`; `ukr_soviet_collapse_arsenal_cities`, `:1086`.
- `soviet_collapse_apply_focus_military_consolidation`: 132 call sites. Examples: `ukr_soviet_collapse_war_without_a_declaration`, `common/national_focus/005_soviet_collapse_republics.txt:164`; `ukr_soviet_collapse_officers_above_parties`, `:531`; `ukr_soviet_collapse_the_commander_or_the_cabinet`, `:616`; `ukr_soviet_collapse_army_supremacy`, `:642`.
- `soviet_collapse_apply_focus_legal_recognition`: 108 call sites. Examples: `ukr_soviet_collapse_guard_the_telegraph_house`, `common/national_focus/005_soviet_collapse_republics.txt:54`; `ukr_soviet_collapse_question_of_statehood`, `:145`; `ukr_soviet_collapse_elections_under_shellfire`, `:308`; `ukr_soviet_collapse_coalition_of_three_ministries`, `:808`.
- `soviet_collapse_apply_focus_republican_compact_plan`: 80 call sites. Examples: `soviet_collapse_republican_survival_pact`, `common/national_focus/005_soviet_collapse_republics.txt:2830`; `soviet_collapse_a_republic_worth_naming`, `:3087`; `internal_soviet_collapse_idel_ural_congress`, `:3661`; `internal_soviet_collapse_taiga_steppe_self_rule`, `:4028`.
- `soviet_collapse_apply_focus_foreign_channel`: 65 call sites. Examples: `ukr_soviet_collapse_open_the_liaison_offices`, `common/national_focus/005_soviet_collapse_republics.txt:211`; `ukr_soviet_collapse_foreign_advisers_in_plain_coats`, `:1060`; `ukr_soviet_collapse_grain_loan`, `:1239`; `ukr_soviet_collapse_german_liaison_question`, `:1349`.
- `soviet_collapse_apply_focus_high_chaos_identity`: 60 call sites. Examples: `ukr_soviet_collapse_black_banner_compact`, `common/national_focus/005_soviet_collapse_republics.txt:268`; `ukr_soviet_collapse_bread_line_becomes_a_border`, `:1999`; `ukr_soviet_collapse_black_soil_oath`, `:2086`; `ukr_soviet_collapse_grain_census_of_everyone`, `:2143`.

The helper definitions do vary variables and payloads, for example:

- `soviet_collapse_apply_focus_legal_recognition`, `common/scripted_effects/005_soviet_collapse_effects.txt:8457`
- `soviet_collapse_apply_focus_military_consolidation`, `common/scripted_effects/005_soviet_collapse_effects.txt:8546`
- `soviet_collapse_apply_focus_depot_and_supply_control`, `common/scripted_effects/005_soviet_collapse_effects.txt:8566`
- `soviet_collapse_apply_focus_republican_compact_plan`, `common/scripted_effects/005_soviet_collapse_effects.txt:9123`
- `soviet_collapse_apply_focus_security_supply_plan`, `common/scripted_effects/005_soviet_collapse_effects.txt:9149`
- `soviet_collapse_apply_focus_high_chaos_identity`, `common/scripted_effects/005_soviet_collapse_effects.txt:10663`

This is not a syntax issue. It is a design-depth risk: future tranches should wrap common helpers in route-specific payload effects, decisions, timed missions, or state interactions so repeated branches do not all resolve as the same abstract variable ladder.

### 4. Several Trees Have Little Or No Direct Decision Integration

Mechanic helper hooks are widespread, but direct player-facing decision hooks are sparse in many trees.

Trees with zero direct decision hooks in focus rewards:

- `soviet_collapse_breakaway_focus_tree`
- `soviet_collapse_internal_republic_focus_tree`
- `soviet_collapse_baltic_focus_tree`
- `soviet_collapse_moldova_focus_tree`
- `FTH_soviet_collapse_focus_tree`
- `KRS_soviet_collapse_focus_tree`
- `BBH_soviet_collapse_focus_tree`
- `UDC_soviet_collapse_focus_tree`
- `SDZ_soviet_collapse_focus_tree`
- `GAC_soviet_collapse_focus_tree`
- `DHC_soviet_collapse_focus_tree`
- `KHC_soviet_collapse_focus_tree`
- `FEV_soviet_collapse_focus_tree`
- `MRC_soviet_collapse_focus_tree`
- `IUL_soviet_collapse_focus_tree`
- `BAC_soviet_collapse_focus_tree`
- `NLC_soviet_collapse_focus_tree`

Trees with low direct decision hook counts:

- `ICD_soviet_collapse_focus_tree`: 1
- `RMC_soviet_collapse_focus_tree`: 1
- `TSC_soviet_collapse_focus_tree`: 1
- `BSC_soviet_collapse_focus_tree`: 2
- `TNC_soviet_collapse_focus_tree`: 2
- Each ancient restoration tree: 2
- `soviet_collapse_caucasus_focus_tree`: 2
- `soviet_collapse_belarus_focus_tree`: 3
- `soviet_collapse_central_asia_focus_tree`: 3
- `ARD_soviet_collapse_focus_tree`: 3
- `soviet_collapse_kazakhstan_focus_tree`: 4

This is the clearest gameplay integration gap after raw depth. The 47-focus custom splinter trees may look full on paper, but many branches are passive unless they unlock new decisions, timed missions, targeted border actions, resource routes, raids, consolidation tasks, or crisis levers.

### 5. Weak Or Flat Rewards Still Exist

The weak-reward heuristic found 39 focus rewards that are mostly flags plus generic manpower, political power, stability, equipment, or state buildings without obvious variables, decisions, war behavior, or branch-specific mechanics. Review these before broad expansion:

- `ukr_soviet_collapse_first_republican_line`, `common/national_focus/005_soviet_collapse_republics.txt:122`
- `ukr_soviet_collapse_moscows_officers_in_our_barracks`, `common/national_focus/005_soviet_collapse_republics.txt:192`
- `ukr_soviet_collapse_village_granary_guards`, `common/national_focus/005_soviet_collapse_republics.txt:1163`
- `soviet_collapse_assemble_emergency_government`, `common/national_focus/005_soviet_collapse_republics.txt:2330`
- `soviet_collapse_route_consolidation_congress`, `common/national_focus/005_soviet_collapse_republics.txt:2587`
- `baltic_soviet_collapse_the_legal_state_or_the_front_state`, `common/national_focus/005_soviet_collapse_republics.txt:4679`
- `kaz_soviet_collapse_border_cavalry_schools`, `common/national_focus/005_soviet_collapse_republics.txt:11041`
- `kaz_soviet_collapse_guard_the_mine_heads`, `common/national_focus/005_soviet_collapse_republics.txt:11550`
- `OGB_treat_with_idel_ural`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1417`
- `TSC_perimeter_regiments`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:2034`
- `BSC_road_and_well_ledger`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:4782`
- `TNC_cotton_rail_republic`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:5908`
- `ALA_caspian_oil_survey`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:7077`
- `KRS_economy`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:8992`
- `SDZ_document_cart_workshops`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:11816`
- `GAC_blacksmith_carts`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:13193`
- `NLC_tundra_watch_posts`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:24991`

The parent should treat this as a review queue, not as automatic delete/replace proof. Some simple rewards can be acceptable, but the density is high enough to undermine the requested depth.

### 6. Search Filter Mismatch Candidates Need A Pass

The heuristic found 236 search-filter mismatch candidates. Many are mixed rewards and not necessarily bugs, but the following are high-signal examples:

- `KZR_old_border_files`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:177`: `FOCUS_FILTER_ANNEXATION` only, but grants claims plus train equipment and infrastructure.
- `SOG_old_city_border_files`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:571`: annexation-facing focus with political/industry reward pieces.
- `KHW_old_oasis_border_files`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:955`: annexation-facing focus with infrastructure/supply-node reward pieces.
- `ALN_old_pass_border_files`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1348`: annexation-facing focus with command/army XP and fort reward pieces.
- `MFR_no_peace_without_orders`, `common/national_focus/005_soviet_collapse_factory_successors.txt:2932`: filters `FOCUS_FILTER_INDUSTRY` and `FOCUS_FILTER_POLITICAL`, but grants aggressive war behavior.
- `FTH_grain_and_rifle_stores`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:813`: filters industry/army, but includes political stability and power reward pieces.
- `PRA_armored_train_schools`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1513`: army-only filter, but grants supply/rail/building elements.
- `DSC_call_the_dead_soldiers_congress`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:2753`: political/army filters, but grants bunker/infrastructure reward pieces.
- `NRF_signal_from_lost_convoys`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3316`: political/navy filters, but high-chaos payload also gives manpower/equipment/war-support style payoff.
- `ICD_penza_memorial_workshops`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3862`: industry filter only, but includes military/equipment reward pieces.

Filter mismatches are lower risk than shallow routes, but they affect player navigation and should be corrected during reward-depth passes.

### 7. AI Focus Behavior Exists, But Route Strategy Is Uneven

Every audited focus has an `ai_will_do` block. External route strategy is stronger for some major republics than for compact chaos/custom trees.

Useful references:

- Broad custom-splinter signature force strategy, `common/ai_strategy/005_soviet_collapse.txt:157`
- Broad high-chaos signature force strategy, `common/ai_strategy/005_soviet_collapse.txt:222`
- Detailed Ukraine route strategies, `common/ai_strategy/005_soviet_collapse.txt:268`
- Belarus route strategy start, `common/ai_strategy/005_soviet_collapse.txt:438`
- Kazakhstan route strategy start, `common/ai_strategy/005_soviet_collapse.txt:580`

The broad strategies react to special-arm flags and shared route signatures, but most 47-focus custom splinter trees and compact high-chaos trees do not have comparable country-specific route plans. For the active parent goal, chaos countries should not merely have local `ai_will_do`; they should have explicit strategic aggression, consolidation, border pressure, and branch preferences.

### 8. Layout Is Mechanically Clean, But Compact Mutually Exclusive Branches Need Visual Recheck After Expansion

The parser found no coordinate overlap and no missing/invalid focus positions. However, the compact 16/18-focus trees have tight mutually exclusive branch geometry. No immediate patch is required, but any depth expansion should preserve pathline clarity and be screenshot-reviewed.

Examples to watch:

- `KZR_symbolic_crossing_state`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:210`, and `KZR_expansionist_steppe_levy`, `:236`
- `SOG_symbolic_city_league`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:604`, and `SOG_expansionist_merchant_claims`, `:629`
- `KHW_symbolic_oasis_authority`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:988`, and the nearby expansionist branch under the same tree
- `ALN_symbolic_pass_principality`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1382`, and the nearby expansionist branch under the same tree
- `PRA_the_board_overrules_ministers`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:1349`, and `PRA_armored_train_directorate` in the same compact branch family
- `NRF_living_harbor_committees`, `common/national_focus/005_soviet_collapse_custom_splinters.txt:3408`, and `NRF_revenant_admiralty` in the same compact branch family

### 9. Loading/Wiring Appears Present

Focus tree load effects are present:

- `soviet_collapse_load_event_created_focus_tree`, `common/scripted_effects/005_soviet_collapse_effects.txt:7462`
- Ukraine load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7468`
- Belarus load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7475`
- Kazakhstan load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7482`
- Baltic load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7493`
- Caucasus load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7504`
- Central Asia load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7516`
- Moldova load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7523`
- Internal republic load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7530`
- Generic breakaway load branch, `common/scripted_effects/005_soviet_collapse_effects.txt:7555`
- Special/factory/custom focus tree load branches from `common/scripted_effects/005_soviet_collapse_effects.txt:16805` through `:17395`.

This audit did not find missing focus-tree load wiring. The remaining issue is content depth and integration, not registration.

## Top 10 Parent Follow-Ups

1. Expand the compact OGB tree into a real 40+ focus successor tree or explicitly accept it as a compact secondary tree. Highest-value additions: Volga legitimacy decisions, Idel-Ural compact/rivalry branch, trade-city industrial logistics, heritage guard army path, and aggressive border settlement tools.
2. Expand `KZR`, `SOG`, `KHW`, and `ALN` ancient restoration trees from 16-focus sketches into full political, industrial, military, diplomacy, and expansion route families with dedicated decisions or missions.
3. Expand `TSC`, `RMC`, `ICD`, `NRF`, `PRA`, and `DSC` compact high-chaos trees. Each should have a unique mechanic loop matching its identity, not only a short trunk with strong rewards.
4. Add player-facing decision or mission hooks to zero-hook 47-focus custom splinter trees, especially `FTH`, `KRS`, `BBH`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `MRC`, `IUL`, `BAC`, and `NLC`.
5. Add country-specific AI strategy plans for major custom splinters and high-chaos successor routes, with explicit aggression, consolidation, and branch selection behavior beyond shared signature-force strategies.
6. Review the 39 weak/flat reward candidates and upgrade them with variables, targeted state effects, timed missions, unlock decisions, dynamic claims, branch counters, or scripted effects where appropriate.
7. Run a focused search-filter cleanup pass, starting with the high-signal examples listed above. Mixed reward focuses should either add matching filters or split rewards into clearer branch focuses.
8. Reduce the same-feel risk from heavily repeated helpers by adding route-specific wrapper effects or payloads. Keep the central helper layer, but make visible branch outcomes more distinct.
9. Recheck focus tree screenshots/pathlines after any compact-tree expansion, especially ancient restoration and high-chaos mutually exclusive branches.
10. Keep idea changes centralized. Do not add new focus-level idea spam; if an expanded route needs an idea, route it through the staged idea lifecycle and document the cleanup path.

## Simplifications, Omissions, And Blockers

- No gameplay patches were made. The audit found structural issues that are not safe to solve with small bounded edits.
- No flags were inspected or edited, per parent constraint.
- The search-filter mismatch list is heuristic. The examples above should be manually reviewed before patching.
- The audit did not run the game. Validation was static/scripted only.
- No completion claim is made for Event005 focus-tree depth. The audit supports further parent implementation tranches.
