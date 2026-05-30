# Soviet Collapse Focus Primary Files Audit Handoff

Timestamp: 2026-05-30 06:17 UTC

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Mode: audit only. No gameplay patch was applied in this pass because the current worktree already contains broad concurrent edits in the target files, direct idea spam has already been removed, and the remaining issues require route design rather than a safe local fix.

## References read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla focus precedent from `~/projects/Hearts of Iron IV/common/national_focus/`, especially focus `prerequisite`, `mutually_exclusive`, `relative_position_id`, `search_filters`, and `ai_will_do`.
- Soviet Collapse focus spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`.
- Recent Soviet Collapse focus handoffs, especially the 2026-05-30 all-tree audit, were checked as prior context; this report recounts the three primary files from the current worktree.

## High-priority fixes first

1. `OGB_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_factory_successors.txt`
   - Evidence: 23 focuses, no decision unlocks, only 10 mechanic-helper calls, 18 flat reward focuses in prior full audit style, 1 layout-risk signal in this primary-file pass.
   - Required rewrite: turn the restored office concept into a playable overpowered successor with a political operating model, bureaucracy/security/industry branches, direct decision hooks, war/core/claim or postwar integration logic, and a real endgame.

2. `TSC_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 18 focuses, 0 decision hooks, 1 wargoal, 2 AI strategy entries, 26 mechanic-helper calls.
   - Required rewrite: add observatory/instrument-state route depth, decisions/missions, expansion consequences, and high-chaos AI behavior beyond a short crisis ladder.

3. `RMC_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 18 focuses, 0 decision hooks, 1 wargoal, 2 AI strategy entries, 25 mechanic-helper calls, 2 flat direct equipment-only focuses.
   - Required rewrite: make martyrology/relic authority into a dangerous recruitment, legitimacy, and expansion loop rather than repeated requisitions.

4. `ICD_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 18 focuses, 0 decision hooks, 1 wargoal, 2 AI strategy entries, 21 mechanic-helper calls, 3 flat direct equipment/building-only focuses.
   - Required rewrite: add dead-roll bureaucracy decisions, memorial mobilization missions, route-specific conquest behavior, and postwar integration/coring consequences.

5. `NRF_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 18 focuses, 4 decision unlocks, 1 wargoal, 6 AI strategy entries, 21 mechanic-helper calls, 2 flat direct equipment-only focuses.
   - Required rewrite: deepen the northern revenant naval route with port-control missions, convoy/escort mechanics, dockyard priorities, coastal war goals, and captured-port settlement.

6. `DSC_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 18 focuses, 5 decision unlocks, 2 wargoals, 10 AI strategy entries, 27 mechanic-helper calls, 1 flat direct equipment/building-only focus.
   - Required rewrite: keep the aggressive dead-army hooks, but add route branches for hierarchy, recruitment, conquered-state memorial integration, and very overpowered end-state mechanics.

7. `PRA_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 22 focuses, 11 decision unlocks, 1 wargoal, 2 AI strategy entries, 35 mechanic-helper calls.
   - Required rewrite: it is the strongest of the shallow special trees, but still needs a longer rail-state route family, armored-train/rail junction missions, and late-game expansion payoff.

8. `FEV_soviet_collapse_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Evidence: 47 focuses, 0 direct decision/war/core/unit/template hooks, 62 mechanic-helper calls, 3 flat direct equipment-only focuses, 4 layout-risk signals.
   - Required rewrite: turn Far Eastern/Pacific labels into port, border, customs, ferry, and foreign-observer mechanics with direct decision and expansion hooks.

9. `soviet_collapse_kazakhstan_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_republics.txt`
   - Evidence: 92 focuses, 6 direct hard hooks, 127 mechanic-helper calls, 1 flat direct equipment-only focus, 24 layout-risk signals.
   - Required rewrite: reduce pathline width/tangles, distinguish Alash/socialist/resource-town/federation routes, and convert repeated broad rewards into oil, rail, steppe, Caspian, and border-state mechanics.

10. `soviet_collapse_ukraine_focus_tree`
   - File: `common/national_focus/005_soviet_collapse_republics.txt`
   - Evidence: 83 focuses, 14 direct hard hooks, 127 mechanic-helper calls, 14 layout-risk signals, 2 exact same-row dx=1 focus crowding pairs.
   - Required rewrite: solve pathline readability around route selectors and make socialist, black-banner, democratic, officer, protectorate, grain, and dead-fields paths produce visibly different governments and mechanics.

## Current audit totals

| File | Trees | Focuses | Focuses adding ideas | Duplicate same idea in same focus | Flat direct equipment/building-only rewards | Missing `ai_will_do` | Focuses with no player-visible meaningful effect | Trees with no mechanic hooks at all | Trees with no direct decision/war/core/unit/template hooks | Suspicious layout/pathline risks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `005_soviet_collapse_republics.txt` | 9 | 501 | 0 | 0 | 1 | 0 | 15 | 0 | 4 | 83 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 0 | 0 | 34 | 0 | 2 | 0 | 18 | 46 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 32 |
| Total | 37 | 1634 | 0 | 0 | 37 | 0 | 19 | 0 | 22 | 161 |

Definitions:
- "Focuses adding ideas" counts direct `add_ideas` calls inside focus rewards. Current value is 0, so direct focus idea spam is gone in the three primary files.
- "Duplicate same idea" counts repeated direct `add_ideas` to the same idea inside one focus. Current value is 0.
- "Flat direct equipment/building-only rewards" means a focus reward contains direct equipment/building reward calls and no direct hard hook or `soviet_collapse_*` helper call. Flags and variable increments may still be present.
- "No player-visible meaningful effect" means the completion reward is only a custom tooltip/hidden helper surface from the focus file perspective. These are not necessarily no-ops, but they are opaque and need manual tooltip/reward review.
- "No direct decision/war/core/unit/template hooks" does not count shared helper effects as direct hooks. Every tree has at least some Soviet Collapse mechanic helper calls.
- Layout/pathline risks are coordinate heuristics: crowded same-row dx=1 pairs, wide shallow prerequisite lines, wide multi-parent tangles, and crowded/wide mutual exclusions.

## Route coverage table

| Required route/tree | Implemented branch surface | Status | Notes |
|---|---|---|---|
| Ukraine republic | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Needs rework | Strong route breadth, but two exact crowding pairs and multiple wide prerequisite/mutual-exclusion risks remain. Rewards rely heavily on shared helpers. |
| Generic breakaway republic | `soviet_collapse_breakaway_focus_tree`, 36 focuses | Simplified | No direct decision/war/core/unit/template hooks; works as a skeleton but not enough for a long-lived major tag. |
| Internal republic | `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Simplified | No direct decision/war/core/unit/template hooks; mostly helper-based state consolidation. |
| Baltic republic | `soviet_collapse_baltic_focus_tree`, 42 focuses | Simplified | Regional identity exists, but no direct decision/war/core/unit/template hooks and only helper-level postwar/diplomacy payoff. |
| Caucasus republic | `soviet_collapse_caucasus_focus_tree`, 40 focuses | Partial | Has decision unlocks, oil/mountain identity, and helper hooks. Needs expansion/postwar depth. |
| Central Asia republic | `soviet_collapse_central_asia_focus_tree`, 45 focuses | Partial | Has decision unlocks and claims, but layout risk and route payoff remain weak. |
| Moldova republic | `soviet_collapse_moldova_focus_tree`, 48 focuses | Simplified | No direct decision/war/core/unit/template hooks; route labels need direct union, bridge, corridor, and border mechanics. |
| Belarus republic | `soviet_collapse_belarus_focus_tree`, 53 focuses | Partial | Has decision/faction hooks, but corridor/forest/transit routes need stronger direct payoffs. |
| Kazakhstan republic | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses | Partial, high risk | Largest tree; too wide and route-heavy. Needs layout cleanup and distinct Alash/socialist/resource/federation outcomes. |
| FTH | `FTH_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| PRA | `PRA_soviet_collapse_focus_tree`, 22 focuses | Partial but shallow | Strong rail decision hook count, but too short for requested OP chaos-country standard. |
| TSC | `TSC_soviet_collapse_focus_tree`, 18 focuses | Shallow | No decision hooks; needs full high-chaos route depth. |
| RMC | `RMC_soviet_collapse_focus_tree`, 18 focuses | Shallow | No decision hooks; repeated flat requisition rewards remain. |
| DSC | `DSC_soviet_collapse_focus_tree`, 18 focuses | Shallow but promising | Has decision, wargoal, and AI hooks; needs more dead-army route depth. |
| NRF | `NRF_soviet_collapse_focus_tree`, 18 focuses | Shallow but promising | Has naval-flavored hooks; needs port/convoy/war loop. |
| ICD | `ICD_soviet_collapse_focus_tree`, 18 focuses | Shallow | No decision hooks; death-state bureaucracy needs mechanics. |
| BSC | `BSC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| TNC | `TNC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| ALA | `ALA_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| BBH | `BBH_soviet_collapse_focus_tree`, 47 focuses | Simplified | Anarchist identity exists, but no direct decision/war/core/unit/template hooks. |
| KRS | `KRS_soviet_collapse_focus_tree`, 47 focuses | Simplified | Naval/free-port identity exists, but no direct decision/war/core/unit/template hooks. |
| UDC | `UDC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| SDZ | `SDZ_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| GAC | `GAC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| DHC | `DHC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks; two opaque hidden-helper focuses. |
| KHC | `KHC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| FEV | `FEV_soviet_collapse_focus_tree`, 47 focuses | Simplified, high priority | No direct decision/war/core/unit/template hooks despite Pacific/Far Eastern route promise. |
| SZA | `SZA_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| UWD | `UWD_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks and high flat reward density. |
| MRC | `MRC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| IUL | `IUL_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks. |
| BAC | `BAC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks and 6 layout-risk signals. |
| ARD | `ARD_soviet_collapse_focus_tree`, 47 focuses | Partial | Has decision unlocks, but lacks direct expansion/postwar mechanics. |
| NLC | `NLC_soviet_collapse_focus_tree`, 47 focuses | Simplified | No direct decision/war/core/unit/template hooks despite polar/science/port promise. |
| CFR | `CFR_soviet_collapse_focus_tree`, 47 focuses | Partial | Decision and wargoal hooks exist; governance and strategy forks need distinct operating models and less pathline clutter. |
| OGB | `OGB_soviet_collapse_focus_tree`, 23 focuses | Shallow, high priority | No decision hooks and too little branch depth for a factory successor. |
| MFR | `MFR_soviet_collapse_focus_tree`, 58 focuses | Partial | Arsenal identity and hooks exist; route forks need more distinct war/industry mechanics and spacing cleanup. |

## Missing or simplified content

- Direct focus idea spam is currently removed in the three primary files: 0 direct `add_ideas` focus rewards and 0 duplicate same-idea calls.
- The remaining reward problem is flatness, not direct idea duplication. There are 200 direct equipment reward focuses, 5 direct building reward focuses, and 37 direct equipment/building-only focuses without direct hard hooks or helper calls.
- Every tree has at least one Soviet Collapse mechanic helper hook, but 22 of 37 trees have no direct decision, war, core, unit, or template hook in the focus file.
- The high-chaos/special tags `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` are 18-focus trees. `PRA` has 22 focuses. These do not satisfy the requested full, overpowered, lore-specific playable-country standard.
- Most full custom splinter trees have 47 focuses but no direct decision/war/core/unit/template hooks. They read as route labels plus shared helper rhythm rather than bespoke country play.
- Ukraine and Kazakhstan have broad route surfaces but remain layout-risk-heavy and reward-repetitive.
- CFR and MFR have stronger surfaces than most, but still show pathline risk and route fork flattening. OGB remains a shallow 23-focus successor.

## Flat direct equipment/building-only focus evidence

Representative high-priority examples:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2051` `TSC_perimeter_regiments`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2339` `RMC_lipetsk_reliquary_workshops`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2452` `RMC_blood_oath_requisitions`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2950` `DSC_grave_ordnance_claims`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3511` `NRF_salvage_the_dark_berths`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3592` `NRF_ghost_convoy_escorts`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3902` `ICD_penza_memorial_workshops`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:4013` `ICD_black_seal_requisitions`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:4091` `ICD_memorial_battalions`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:16493` `FEV_customs_house_ledger`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:16985` `FEV_razdolnoye_rear_area`
- `common/national_focus/005_soviet_collapse_republics.txt:10512` `kaz_soviet_collapse_oil_field_protection_orders`
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2648` `MFR_builders_waste_steel`
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2673` `MFR_civilian_factory_rivalry`

## Opaque or no player-visible meaningful reward evidence

These focuses have rewards that are only visible as custom tooltip plus hidden helper from the focus-file perspective. They are not confirmed no-ops, but they need tooltip/reward review because the player cannot see a normal concrete reward.

- `common/national_focus/005_soviet_collapse_republics.txt:579` `ukr_soviet_collapse_officer_patronage_lists`
- `common/national_focus/005_soviet_collapse_republics.txt:608` `ukr_soviet_collapse_general_staff_war_college`
- `common/national_focus/005_soviet_collapse_republics.txt:846` `ukr_soviet_collapse_rural_deputy_bloc`
- `common/national_focus/005_soviet_collapse_republics.txt:878` `ukr_soviet_collapse_minority_autonomy_statutes`
- `common/national_focus/005_soviet_collapse_republics.txt:907` `ukr_soviet_collapse_provincial_governors_or_elected_radas`
- `common/national_focus/005_soviet_collapse_republics.txt:2925` `soviet_collapse_capital_committee_or_field_committee`
- `common/national_focus/005_soviet_collapse_republics.txt:4996` `baltic_soviet_collapse_baltic_recognition_dossier`
- `common/national_focus/005_soviet_collapse_republics.txt:5018` `baltic_soviet_collapse_the_legal_front_abroad`
- `common/national_focus/005_soviet_collapse_republics.txt:5081` `baltic_soviet_collapse_pan_baltic_war_room`
- `common/national_focus/005_soviet_collapse_republics.txt:5103` `baltic_soviet_collapse_baltic_shield_doctrine`
- `common/national_focus/005_soviet_collapse_republics.txt:5706` `caucasus_soviet_collapse_caucasus_route_fork`
- `common/national_focus/005_soviet_collapse_republics.txt:6636` `central_asia_soviet_collapse_southern_route_fork`
- `common/national_focus/005_soviet_collapse_republics.txt:7782` `moldova_soviet_collapse_moldova_route_fork`
- `common/national_focus/005_soviet_collapse_republics.txt:8952` `blr_soviet_collapse_which_road_is_belarus`
- `common/national_focus/005_soviet_collapse_republics.txt:10286` `kaz_soviet_collapse_the_congress_chooses_a_past`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:14462` `DHC_stanitsa_mediation`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:14485` `DHC_stanitsa_oath_boards`
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2648` `MFR_builders_waste_steel`
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2673` `MFR_civilian_factory_rivalry`

## Icon coverage table

| File | Missing icon assignment | Missing `.gfx` definition | Repeated icon groups | Top repeated icons |
|---|---:|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 0 | 0 | 22 | `GFX_focus_soviet_collapse_guard_the_radio_stations` x4; `GFX_ukr_soviet_collapse_democratic` x4; `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` x4; `GFX_focus_soviet_collapse_steppe_supply_congress` x4 |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 0 | 99 | `GFX_focus_FEV_diplomatic_plan` x4; `GFX_focus_SZA_diplomatic_plan` x4; `GFX_focus_MRC_civil_rule` x4; `GFX_focus_MRC_foreign` x4 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 0 | 11 | `GFX_focus_CFR_municipal_board_elections` x3; `GFX_focus_CFR_concrete_republic` x3; `GFX_focus_CFR_the_builder_state` x3; `GFX_focus_CFR_civilian_hegemony_project` x3 |

Icon conclusion: there are no load-breaking missing icon references in the three primary files. The unique-icon standard is still not met because repeated icon families remain, especially in custom splinters.

## Localisation and reward mismatch list

- Missing focus title localisation: 0.
- Missing focus description localisation: 0.
- Direct idea add/swap/timed focus spam: 0 direct `add_ideas`; 0 duplicate same direct idea in a focus.
- Reward mismatch risk remains because many lore-heavy names still resolve to direct equipment/building grants or the same helper rhythm.
- High-risk mismatch examples:
  - `TSC_perimeter_regiments`: perimeter identity, but direct manpower/equipment/air XP/building reward only from focus-file perspective.
  - `RMC_lipetsk_reliquary_workshops` and `RMC_blood_oath_requisitions`: relic/martyrology concept, but direct stockpile/workshop rewards dominate.
  - `ICD_penza_memorial_workshops`, `ICD_black_seal_requisitions`, `ICD_memorial_battalions`: dead-roll bureaucracy needs a decision/mobilization loop rather than flat stores.
  - `FEV_customs_house_ledger` and `FEV_razdolnoye_rear_area`: customs/Pacific route text should unlock border, port, ferry, or observer mechanics.
  - `MFR_builders_waste_steel` and `MFR_civilian_factory_rivalry`: tooltip-hidden effects need review and clearer visible reward variety.

## AI behavior gaps

- Missing `ai_will_do`: 0. Every focus in the three files has an `ai_will_do` block.
- Route-aware AI is still incomplete. Many blocks use flat bases or basic local conditions; broad route strategy is not consistently tied to the Soviet Collapse variables after route selection.
- `TSC`, `RMC`, `ICD`, `FEV`, and most full-size custom splinters lack direct decision/war/core/unit/template hooks, so AI focus completion often has no direct follow-on behavior visible in these files.
- Naval and port actors (`NRF`, `ARD`, `KRS`, `NLC`, `FEV`) need AI strategies for port defense, dockyard priorities, convoy escort/raiding, coastal war targets, and naval invasion/landing behavior.
- Aggressive high-chaos actors (`DSC`, `RMC`, `ICD`, `TSC`, `NRF`) need stronger endpoint AI strategies and limits so they do not choose normal diplomatic consolidation when chaos tier, war state, or concept says conquest or rupture.
- Major republics need route-choice AI around defensive consolidation, League leadership, foreign protectorate play, regional expansion, and internal faction payoff.

## Suspicious layout/pathline risks

Mechanical safety checks:
- Duplicate focus IDs across the three primary files: 0.
- Duplicate exact focus positions inside the same tree: 0.
- Missing focus coordinates: 0.
- Prerequisite pointing to missing focus IDs: 0.
- Mutual exclusion pointing to missing focus IDs: 0.
- Prerequisite parent at same/lower row than child: 0.

Coordinate-risk heuristic totals:
- Total suspicious layout/pathline signals: 161.
- `wide_shallow_prereq_line`: 70.
- `multi_parent_tangle`: 64.
- `wide_mutual_exclusive_same_row`: 16.
- `mutual_exclusive_crowded_pair`: 6.
- `crowded_same_row_dx1`: 5.

Highest-risk trees:
- `soviet_collapse_kazakhstan_focus_tree`: 24 signals.
- `CFR_soviet_collapse_focus_tree`: 17 signals.
- `soviet_collapse_ukraine_focus_tree`: 14 signals.
- `MFR_soviet_collapse_focus_tree`: 14 signals.
- `soviet_collapse_moldova_focus_tree`: 9 signals.
- `UWD_soviet_collapse_focus_tree`: 9 signals.
- `soviet_collapse_caucasus_focus_tree`: 8 signals.
- `soviet_collapse_central_asia_focus_tree`: 8 signals.

Exact same-row dx=1 crowding pairs:
- `common/national_focus/005_soviet_collapse_republics.txt:956` `ukr_soviet_collapse_republic_of_laws` at `(17,6)` and `ukr_soviet_collapse_socialist_republic_without_moscow` at `(18,6)`.
- `common/national_focus/005_soviet_collapse_republics.txt:657` `ukr_soviet_collapse_army_supremacy` at `(19,7)` and `ukr_soviet_collapse_civilian_command_over_the_army` at `(20,7)`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2091` `MFR_artillery_from_broken_foundries` at `(4,10)` and `MFR_workers_must_not_flee` at `(5,10)`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2648` `MFR_builders_waste_steel` at `(9,10)` and `MFR_standardize_the_rifle_line` at `(10,10)`.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2188` `MFR_standardize_the_rifle_line` at `(10,10)` and `MFR_unsafe_production_surge` at `(11,10)`.

## Direct hook coverage

Trees with no direct decision/war/core/unit/template hooks in the focus file, although they do have shared Soviet Collapse helper calls:
- `soviet_collapse_breakaway_focus_tree`
- `soviet_collapse_internal_republic_focus_tree`
- `soviet_collapse_baltic_focus_tree`
- `soviet_collapse_moldova_focus_tree`
- `FTH_soviet_collapse_focus_tree`
- `BSC_soviet_collapse_focus_tree`
- `TNC_soviet_collapse_focus_tree`
- `ALA_soviet_collapse_focus_tree`
- `BBH_soviet_collapse_focus_tree`
- `KRS_soviet_collapse_focus_tree`
- `UDC_soviet_collapse_focus_tree`
- `SDZ_soviet_collapse_focus_tree`
- `GAC_soviet_collapse_focus_tree`
- `DHC_soviet_collapse_focus_tree`
- `KHC_soviet_collapse_focus_tree`
- `FEV_soviet_collapse_focus_tree`
- `SZA_soviet_collapse_focus_tree`
- `UWD_soviet_collapse_focus_tree`
- `MRC_soviet_collapse_focus_tree`
- `IUL_soviet_collapse_focus_tree`
- `BAC_soviet_collapse_focus_tree`
- `NLC_soviet_collapse_focus_tree`

Trees with direct hard hooks:
- `soviet_collapse_ukraine_focus_tree`: 14 direct hard hooks, including 13 decision unlocks and 1 cosmetic tag hook.
- `soviet_collapse_caucasus_focus_tree`: 4 decision unlocks.
- `soviet_collapse_central_asia_focus_tree`: 6 decision unlocks and 7 state-claim calls.
- `soviet_collapse_belarus_focus_tree`: 6 decision unlocks and 1 faction hook.
- `soviet_collapse_kazakhstan_focus_tree`: 6 decision unlocks.
- `PRA_soviet_collapse_focus_tree`: 11 decision unlocks, 1 wargoal, 2 AI strategy calls.
- `TSC_soviet_collapse_focus_tree`: 1 wargoal and 2 AI strategy calls.
- `RMC_soviet_collapse_focus_tree`: 1 wargoal and 2 AI strategy calls.
- `DSC_soviet_collapse_focus_tree`: 5 decision unlocks, 2 wargoals, 10 AI strategy calls.
- `NRF_soviet_collapse_focus_tree`: 4 decision unlocks, 1 wargoal, 6 AI strategy calls.
- `ICD_soviet_collapse_focus_tree`: 1 wargoal and 2 AI strategy calls.
- `ARD_soviet_collapse_focus_tree`: 3 decision unlocks.
- `CFR_soviet_collapse_focus_tree`: 4 decision unlocks, 2 wargoals, 6 AI strategy calls.
- `OGB_soviet_collapse_focus_tree`: 2 wargoals, 3 state claims, 6 AI strategy calls.
- `MFR_soviet_collapse_focus_tree`: 4 decision unlocks, 1 wargoal, 10 AI strategy calls.

## Patch status

No patch applied.

Reason:
- Direct focus idea spam and duplicate same-idea focus rewards are already at 0 in the current worktree.
- The remaining issues are route-depth and reward-design gaps affecting many trees. Bulk patching them would exceed the bounded focus-tree subagent scope.
- The exact crowding pairs are clear, but moving them safely needs route-layout review because Ukraine, CFR, and MFR have dense mutual-exclusion/pathline structures and concurrent edits are already present.

Changed files:
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_061736_soviet_collapse_focus_primary_files_audit_handoff.md`

Changed focus ids:
- None.

Route behavior before/after:
- No gameplay route behavior changed.

Localisation keys and icon ids changed:
- None.

## Validation run

Commands/checks run:
- Parsed focus trees/focus blocks in the three primary files.
- Counted direct `add_ideas`, duplicate same-idea calls, direct equipment/building rewards, `completion_reward`, and `ai_will_do`.
- Checked focus ID duplication, missing prerequisites, missing mutual-exclusion targets, missing coordinates, duplicate positions, same-row crowding, wide pathline heuristics, and reverse/same-row prerequisite direction.
- Compared focus title and `_desc` keys against localisation files.
- Compared focus icon references against mod and vanilla `.gfx` sprite definitions.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`
- Brace balance parser over the three focus files.
- `rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`

Validation results:
- Brace balance: final depth 0 and no negative-depth lines for all three files.
- Unsupported operators `<=` / `>=`: none found.
- `git diff --check`: no output.
- Focus counts equal `completion_reward` and `ai_will_do` counts in all three files:
  - republics: 501 focuses, 501 rewards, 501 AI blocks.
  - custom splinters: 1005 focuses, 1005 rewards, 1005 AI blocks.
  - factory successors: 128 focuses, 128 rewards, 128 AI blocks.
- Missing focus localisation entries: 0.
- Missing focus icon assignments or `.gfx` definitions: 0.

Skipped validation:
- No in-game visual screenshot validation. This subagent pass used parser/coordinate heuristics only.
- No full HOI4 launch validation. Scope was audit/handoff and syntax-level checks.
- No decision/idea/helper behavior validation beyond identifier-pattern counting, because the user scoped this pass primarily to focus files.

## Remaining route risks

- The parent objective is not complete. This handoff is an actionable audit for the three primary focus files, not a full Soviet Collapse focus-tree rework.
- High-chaos and factory-successor trees still need deliberate route design. Small isolated patches would not satisfy the requested overpowered, lore-specific, politically/industrially/expansion-deep trees.
- Repeated icon families are load-safe but fail the unique-icon standard.
- Shared helper effects keep the focus files connected to Soviet Collapse mechanics, but many trees still lack direct decision/war/core/unit/template hooks and therefore do not expose enough route-specific gameplay in the focus tree.
- Ukraine, Kazakhstan, CFR, and MFR should get layout work after route redesign, not before, because route movement may invalidate any small coordinate patch.
