# Soviet Collapse Focus Tree Current-State Audit Handoff

Date: 2026-05-30
Subagent: Chaos Redux focus tree subagent
Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

User request: full current-state audit of all Soviet Collapse focus trees, with narrow safe patches only where they reduce idea spam or obvious pathline/mutual-exclusion problems. No full bulk rewrite attempted.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `~/projects/Hearts of Iron IV/common/script_constants/documentation.md`.
- Vanilla focus precedent inspected through `~/projects/Hearts of Iron IV/common/national_focus/`, especially focus layout, `prerequisite`, `mutually_exclusive`, `relative_position_id`, `ai_will_do`, and focus icon patterns.
- Soviet Collapse source design: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`.

## Current Audit Totals

Definitions:
- `flat reward focuses` means focus blocks with direct flat stat/equipment/building rewards such as `add_equipment_to_stockpile`, `add_building_construction`, `add_stability`, `add_political_power`, `add_manpower`, XP, or command power.
- `tiny equipment/factory focuses` means focuses with one or two direct equipment/building rewards and no direct decision/claim/core/wargoal in the same focus block. This is a heuristic for low-impact reward ladders; helper effects may still add more.
- `weak trees` means trees that are too short, have no decision hooks, or lack enough direct expansion/postwar mechanics for the requested political/industrial/expansion depth standard.
- `pathline risks` are coordinate heuristics: crowded same-row focus pairs, wide shallow prerequisite lines, multi-parent convergence tangles, and crowded/wide mutual-exclusion lines.

| File | Trees | Focuses | Add idea focuses | Remove idea focuses | Swap idea focuses | Timed idea focuses | Duplicate same idea calls in one focus | Flat reward focuses | Tiny equipment/factory focuses | Weak trees | Pathline risks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `005_soviet_collapse_republics.txt` | 9 | 501 | 0 | 0 | 0 | 0 | 0 | 305 | 105 | 4 | 73 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 0 | 7 | 0 | 0 | 0 | 550 | 266 | 24 | 42 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | 0 | 1 | 0 | 0 | 0 | 53 | 10 | 1 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | 0 | 0 | 0 | 0 | 0 | 29 | 10 | 4 | 0 |
| Total | 41 | 1698 | 0 | 8 | 0 | 0 | 0 | 937 | 391 | 33 | 115 |

Direct idea add/swap/timed spam is currently gone. The remaining problem is not direct duplicate idea stacking; it is flat reward density, repeated helper rhythm, and shallow route payoff.

Direct `remove_ideas` cleanup is limited to these eight focus blocks:
- `OGB_the_council_takes_the_seal` removes `ogb_disputed_restored_name`.
- `PRA_the_board_overrules_ministers` removes `pra_dispatcher_court_tensions`.
- `TSC_the_committee_of_instruments` removes `tsc_field_station_rivalries`.
- `RMC_communes_of_witnesses` removes `rmc_credal_cell_rivalries`.
- `DSC_witness_officers` removes `dsc_grave_regiment_rivalries`.
- `NRF_living_harbor_committees` removes `nrf_drowned_crew_disputes`.
- `ICD_commissars_of_last_addresses` removes `icd_grave_commissar_rivalries`.
- `mrc_protect_village_autonomy` removes `mrc_pass_confederation_rivalries`.

## Flat Reward Call Counts

| File | Direct flat reward calls |
|---|---|
| `005_soviet_collapse_republics.txt` | `add_building_construction` 161, `add_stability` 90, `add_command_power` 45, `add_political_power` 37, `army_experience` 34, `add_manpower` 33, `add_equipment_to_stockpile` 30, `add_extra_state_shared_building_slots` 28, `add_war_support` 15, `navy_experience` 4 |
| `005_soviet_collapse_custom_splinters.txt` | `add_building_construction` 379, `add_equipment_to_stockpile` 212, `add_stability` 132, `add_command_power` 102, `army_experience` 92, `add_manpower` 80, `add_political_power` 79, `add_war_support` 54, `add_extra_state_shared_building_slots` 52, `navy_experience` 39, `air_experience` 13 |
| `005_soviet_collapse_factory_successors.txt` | `add_stability` 19, `add_building_construction` 16, `add_political_power` 9, `add_extra_state_shared_building_slots` 8, `army_experience` 6, `add_war_support` 6, `add_offsite_building` 5, `add_manpower` 4, `add_equipment_to_stockpile` 3, `air_experience` 1, `add_command_power` 1 |
| `005_soviet_collapse_ancient_restorations.txt` | `add_building_construction` 27, `add_equipment_to_stockpile` 8, `add_war_support` 8, `add_stability` 6, `add_command_power` 6, `army_experience` 5, `add_extra_state_shared_building_slots` 5, `add_manpower` 4, `add_political_power` 4, `navy_experience` 1 |

Repeated helper calls remain high:
- `soviet_collapse_apply_focus_legal_recognition`: 305 calls across the four files.
- `soviet_collapse_apply_focus_depot_and_supply_control`: 258 calls.
- `soviet_collapse_apply_focus_military_consolidation`: 254 calls.
- `soviet_collapse_apply_focus_league_preparation`: 220 calls.
- `soviet_collapse_apply_focus_foreign_channel`: 176 calls.
- `soviet_collapse_update_consolidated_republic_ideas`: 111 calls.
- `soviet_collapse_apply_focus_high_chaos_identity`: 96 calls.

## Route Coverage Table

| Tree | File line | Focuses | Decision hooks | Direct expansion mechanics | Flat reward focuses | Tiny equipment/factory focuses | Current status |
|---|---:|---:|---:|---:|---:|---:|---|
| `soviet_collapse_ukraine_focus_tree` | `005_soviet_collapse_republics.txt:18` | 83 | 7 | 0 | 52 | 6 | Broad route surface exists, but layout and payoff clarity still need a parent pass. |
| `soviet_collapse_breakaway_focus_tree` | `005_soviet_collapse_republics.txt:2356` | 36 | 0 | 0 | 21 | 8 | Generic shared skeleton; weak for any long-lived major breakaway. |
| `soviet_collapse_internal_republic_focus_tree` | `005_soviet_collapse_republics.txt:3153` | 62 | 0 | 1 | 42 | 28 | Large enough, but decision integration and route payoffs are weak. |
| `soviet_collapse_baltic_focus_tree` | `005_soviet_collapse_republics.txt:4657` | 42 | 0 | 0 | 20 | 10 | Regional shape exists; lacks decisions and postwar settlement depth. |
| `soviet_collapse_caucasus_focus_tree` | `005_soviet_collapse_republics.txt:5621` | 40 | 2 | 0 | 21 | 8 | Oil/mountain identity exists; needs stronger postwar handling. |
| `soviet_collapse_central_asia_focus_tree` | `005_soviet_collapse_republics.txt:6550` | 45 | 3 | 1 | 28 | 15 | Has hooks, but still reward-heavy and line-risky. |
| `soviet_collapse_moldova_focus_tree` | `005_soviet_collapse_republics.txt:7699` | 48 | 0 | 0 | 31 | 11 | Compact route labels exist; no decision unlocks and weak expansion. |
| `soviet_collapse_belarus_focus_tree` | `005_soviet_collapse_republics.txt:8867` | 53 | 3 | 0 | 33 | 2 | Improved early spacing; corridor/forest routes still need payoffs. |
| `soviet_collapse_kazakhstan_focus_tree` | `005_soviet_collapse_republics.txt:10199` | 92 | 4 | 0 | 57 | 17 | Largest republic tree; too wide, reward-heavy, and high pathline risk. |
| `FTH_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:15` | 47 | 0 | 0 | 26 | 15 | Small layout patch applied; still lacks decision/formable/war payoff depth. |
| `PRA_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:1219` | 22 | 11 | 1 | 18 | 4 | Rail identity is strongest among shallow trees; still short. |
| `TSC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:1814` | 18 | 0 | 1 | 13 | 5 | Shallow crisis tree; needs full identity mechanics. |
| `RMC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:2291` | 18 | 0 | 3 | 12 | 4 | Has aggressive mechanics but no depth or decision loop. |
| `DSC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:2775` | 18 | 5 | 3 | 14 | 3 | Dangerous endpoint exists; dead-army state still too short. |
| `NRF_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:3351` | 18 | 4 | 3 | 15 | 8 | Naval theme exists; needs real naval war and port control loop. |
| `ICD_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:3854` | 18 | 0 | 3 | 13 | 5 | Shallow death-state tree with no decision loop. |
| `BSC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:4328` | 47 | 0 | 0 | 28 | 15 | Full-size but templated; no decision hooks or expansion mechanics. |
| `TNC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:5458` | 47 | 0 | 0 | 26 | 14 | Full-size but templated; no decision hooks or expansion mechanics. |
| `ALA_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:6596` | 47 | 0 | 0 | 24 | 8 | Full-size but templated; needs lore-specific payoffs. |
| `BBH_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:7716` | 47 | 0 | 0 | 25 | 11 | Stronger theme than most, but no decision hooks or expansion mechanics. |
| `KRS_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:8920` | 47 | 0 | 0 | 27 | 17 | Port/sailor theme exists; no decision hooks or expansion mechanics. |
| `UDC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:10162` | 47 | 0 | 0 | 23 | 8 | Loyalist/military theme exists; no decision hooks or expansion mechanics. |
| `SDZ_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:11363` | 47 | 0 | 0 | 23 | 7 | Security theme exists; no decision hooks or expansion mechanics. |
| `GAC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:12608` | 47 | 0 | 0 | 25 | 9 | Peasant route labels exist; no decision hooks or expansion mechanics. |
| `DHC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:13791` | 47 | 0 | 0 | 23 | 12 | Host route labels exist; no decision hooks or expansion mechanics. |
| `KHC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:14997` | 47 | 0 | 0 | 25 | 12 | Host route labels exist; no decision hooks or expansion mechanics. |
| `FEV_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:16196` | 47 | 0 | 0 | 22 | 12 | Far Eastern route labels exist; no decision hooks or expansion mechanics. |
| `SZA_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:17371` | 47 | 0 | 0 | 21 | 13 | Siberian administration labels exist; no decision hooks or expansion mechanics. |
| `UWD_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:18551` | 47 | 0 | 0 | 25 | 19 | Industrial theme, but heavy tiny factory rewards and no decision hooks. |
| `MRC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:19756` | 47 | 0 | 0 | 23 | 15 | Mountain confederation labels exist; no decision hooks or expansion mechanics. |
| `IUL_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:20932` | 47 | 0 | 0 | 22 | 11 | Volga/Ural identity exists; no decision hooks or expansion mechanics. |
| `BAC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:22089` | 47 | 0 | 0 | 23 | 12 | Amur/Birobidzhan identity exists; no decision hooks or expansion mechanics. |
| `ARD_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:23235` | 47 | 3 | 0 | 28 | 16 | Naval directorate has some hooks, but lacks expansion/postwar mechanics. |
| `NLC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt:24433` | 47 | 0 | 0 | 26 | 11 | Polar/science theme exists; no decision hooks or expansion mechanics. |
| `CFR_soviet_collapse_focus_tree` | `005_soviet_collapse_factory_successors.txt:16` | 47 | 4 | 2 | 18 | 4 | Better than most; needs governance/strategy operating-model depth. |
| `OGB_soviet_collapse_focus_tree` | `005_soviet_collapse_factory_successors.txt:1136` | 23 | 0 | 3 | 18 | 3 | Shallow successor tree; no decision hooks. |
| `MFR_soviet_collapse_focus_tree` | `005_soviet_collapse_factory_successors.txt:1713` | 58 | 3 | 1 | 17 | 3 | Better arsenal identity; expansion/special mechanics still thin. |
| `KZR_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:13` | 16 | 2 | 3 | 7 | 2 | Ancient restoration stub; too shallow. |
| `SOG_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:385` | 16 | 2 | 3 | 7 | 2 | Ancient restoration stub; too shallow. |
| `KHW_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:758` | 16 | 2 | 3 | 7 | 3 | Ancient restoration stub; too shallow. |
| `ALN_soviet_collapse_ancient_focus_tree` | `005_soviet_collapse_ancient_restorations.txt:1134` | 16 | 2 | 3 | 8 | 3 | Ancient restoration stub; too shallow. |

## Ranked Trees Needing Full Rework

1. `TSC`, `RMC`, `ICD`, `DSC`, `NRF`: 18-focus crisis/high-chaos trees cannot satisfy the requested OP, lore-specific, playable-country standard. `DSC` and `NRF` have useful hooks but are still too small.
2. Ancient restorations `KZR`, `SOG`, `KHW`, `ALN`: all four are 16-focus stubs with repeated ancient icon families and claim/endgame payoffs, not living restoration politics.
3. Full-size custom splinters with zero decision hooks and zero direct expansion mechanics: `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `NLC`.
4. Major republics needing payoff/layout cleanup: `soviet_collapse_kazakhstan_focus_tree`, `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_belarus_focus_tree`, `soviet_collapse_moldova_focus_tree`.
5. Factory successors: `OGB` needs full successor depth; `CFR` and `MFR` need targeted route specialization rather than a full reset.
6. `PRA` should be deepened, but it is already the best shallow special tree because it has 11 decision hooks and a rail identity.

## Concrete Route Redesign Recommendations

Political branches:
- Give every major republic and full-size chaos tag at least two incompatible political end states that change leader, ruling party, party names, law/advisor access, cosmetic identity, or country flags used by decisions.
- Replace generic recognition/legal helper repetition with route-specific governing institutions: Ukraine should distinguish socialist, directory, officer, democratic, black-banner, and protectorate states; Belarus should distinguish national council, socialist autonomy, military transit, and foreign corridor administration; Kazakhstan should distinguish Alash, socialist steppe, resource-town directorate, and federation routes.
- For fixed-purpose death or machine-like countries, create internal method choices rather than normal ideology choices: command hierarchy, recruitment logic, tribute economy, expansion doctrine, and endgame rule.

Industrial branches:
- Convert flat construction/equipment ladders into focus-gated decision loops. Rail states should unlock junction repair, rolling-stock seizure, rail-toll, and armored-train decisions. Factory states should unlock recurring client-city, arsenal contract, reconstruction protectorate, and production surcharge decisions.
- Geographically ground industry rewards in named state groups. Kazakhstan should separate oil towns, steppe rail, Semipalatinsk/Alma-Ata administration, and Caspian routes. Belarus should separate Minsk junctions, western corridor, eastern line, and forest depots.
- Reduce direct `add_building_construction` spam by shifting repeated effects into route-specific helper effects with custom tooltips and by making later focuses modify the same mechanic rather than adding another one-off building.

Expansion branches:
- Every full-size custom splinter needs a real expansion or postwar branch. At minimum: claims or war goals, target-state missions, integration decisions, resistance/legitimacy consequences, and AI target strategy.
- Naval actors need port-control missions, convoy raiding or escort decisions, dockyard/ship priorities, coastal war goals, and post-capture port integration. Apply this especially to `NRF`, `ARD`, `KRS`, and `NLC`.
- Dead-army or high-chaos actors should be intentionally overpowered through lore-specific mechanics, not just more equipment: controlled-state coring, grave-roll recruitment, automatic war pressure, conquered-state memorial integration, high-chaos penalties for neighbors, and aggressive AI strategies.
- Ancient restoration trees should stage legitimacy before conquest: rediscovery/recognition, charter proclamation, old-route military, claim wars, partial integration, then endgame identity. Do not create a new full formable chain unless the parent approves it.

## Icon Coverage Table

| File | Missing icon assignment | Missing `.gfx` definition | Repeated icon groups | Top repeated icons |
|---|---:|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 0 | 0 | 22 | `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` x4, `GFX_central_asia_soviet_collapse_steppe_federation` x4, `GFX_focus_soviet_collapse_guard_the_radio_stations` x4, `GFX_ukr_soviet_collapse_democratic` x4 |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 0 | 99 | `GFX_focus_FEV_diplomatic_plan` x4, `GFX_focus_IUL_supply` x4, `GFX_focus_IUL_war_plan` x4, `GFX_focus_MRC_civil_rule` x4 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 0 | 11 | `GFX_focus_CFR_civilian_hegemony_project` x3, `GFX_focus_CFR_concrete_republic` x3, `GFX_focus_CFR_municipal_board_elections` x3, `GFX_focus_CFR_the_builder_state` x3 |
| `005_soviet_collapse_ancient_restorations.txt` | 0 | 0 | 8 | Seven ancient icon families repeat x4 each across the four restoration trees. |

Icon conclusion: there are no load-breaking missing focus icons, but the unique-icon requirement is not met. The custom splinter file and ancient restoration file need icon-family expansion during a broad rework.

## Localisation And Reward Mismatch List

- Missing focus title keys: 0.
- Missing focus description keys: 0.
- Direct idea add/swap/timed reward spam: 0.
- Duplicate same direct idea call in a focus: 0.
- Reward mismatch risk remains high because 937 focuses have direct flat reward patterns and many route names still resolve into the same handful of helper effects.
- Hover spam risk is lower than before because staged idea updates are hidden in many places, but `soviet_collapse_update_consolidated_republic_ideas` still appears in 111 focus rewards through hidden effects and should stay hidden/custom-tooltipped during rework.
- Biggest mismatch surfaces:
  - `UWD_soviet_collapse_focus_tree`: 19 tiny equipment/factory focuses, but the worker/industrial route should unlock a production system.
  - `KRS`, `DHC`, `KHC`, `ARD`: many naval/host/port titles still lean on convoy, rail, dockyard, and helper loops without enough map outcome.
  - `soviet_collapse_kazakhstan_focus_tree`: 92 focuses and 57 flat reward focuses; route breadth is present but too many payoffs are generic.
  - Ancient restorations: repeated icons and 16-focus shape make all four restorations read as variants of one template.

## AI Behavior Gaps

- Missing `ai_will_do`: 0.
- Route-aware AI is still shallow. Many focuses have valid weights, but custom splinters with zero decision hooks do not yet drive route-specific behavior after the focus is complete.
- Naval actors need AI strategies for dockyards, convoy raiding/escort, port defense, naval invasion preparation, and coastal target selection.
- Aggressive chaos actors need stronger target strategies toward SOV and nearby rivals after hardline endpoints, plus limits so they do not choose diplomatic branches when high chaos or war state says conquest is the identity.
- Major republics need route AI that chooses between defensive consolidation, League leadership, foreign protectorate play, regional expansion, and internal faction payoff based on Soviet Collapse variables.

## Pathline And Layout Risks

Post-patch coordinate heuristic totals:
- Total pathline/layout risk signals: 115.
- `crowded_same_row_dx1`: 2, both still in Ukraine.
- `wide_shallow_prereq_line`: 55.
- `multi_parent_tangle`: 50.
- `mutual_exclusive_crowded_pair`: 6.
- `wide_mutual_exclusive_same_row`: 2.

Highest-risk trees:
- `soviet_collapse_kazakhstan_focus_tree`: 21 risk signals.
- `soviet_collapse_ukraine_focus_tree`: 15 risk signals.
- `soviet_collapse_central_asia_focus_tree`: 10 risk signals.
- `soviet_collapse_moldova_focus_tree`: 8 risk signals.
- `soviet_collapse_caucasus_focus_tree`: 7 risk signals.
- `UWD_soviet_collapse_focus_tree` and `BAC_soviet_collapse_focus_tree`: 6 each.

Remaining exact crowded same-row pairs:
- `ukr_soviet_collapse_socialist_republic_without_moscow` / `ukr_soviet_collapse_republic_of_laws`, both row `y = 6`, `dx = 1`.
- `ukr_soviet_collapse_army_supremacy` / `ukr_soviet_collapse_civilian_command_over_the_army`, both row `y = 7`, `dx = 1`.

## Small Patch Applied

Changed file:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

Changed focus ids:
- `FTH_commune_court_registers`
- `FTH_tachanka_column_oaths`
- `FTH_steppe_airstrips`

Before:
- The FTH local row cluster had four `dx = 1` same-row crowding risks:
  - `FTH_commune_supply_ledger` / `FTH_commune_court_registers`
  - `FTH_grain_and_rifle_stores` / `FTH_tachanka_column_oaths`
  - `FTH_extreme_gate` / `FTH_commune_court_registers`
  - `FTH_steppe_airstrips` / `FTH_extreme_path`

After:
- `FTH_commune_court_registers` moved from `x = 5, y = 10` to `x = 2, y = 10`.
- `FTH_tachanka_column_oaths` moved from `x = 5, y = 11` to `x = 3, y = 11`.
- `FTH_steppe_airstrips` moved to `x = 0, y = 12`; the committed base had `x = 4, y = 12`, while the dirty pre-patch working tree had already moved it to `x = 3, y = 12`.
- FTH same-row `dx = 1` crowding is now gone. The remaining FTH risks are only two pre-existing multi-parent convergence points: `FTH_enemy_front` and `FTH_settlement`.

Route behavior before and after:
- Gameplay behavior is unchanged. This was coordinate-only.
- Prerequisites, route locks, rewards, AI weights, focus ids, icons, localisation keys, and effects are unchanged.

Localisation keys changed:
- None.

Icon ids changed:
- None.

Safety note:
- The working tree already had unrelated edits in `005_soviet_collapse_custom_splinters.txt` before this pass, including PRA and DSC reward changes. I did not revert or normalize those edits. The patch above is limited to the three FTH coordinate changes.

## Validation Run

Commands run:
- Bracket, unsupported operator, duplicate focus id, missing `ai_will_do`, missing icon assignment, missing focus localisation, missing focus description localisation, missing `.gfx` icon definition, and same-row spacing audit over all four Soviet Collapse focus files.
  - Result: brace balance clean for all four files; no `<=` or `>=`; 1698 focuses in 41 trees; duplicate focus ids 0; missing `ai_will_do` 0; missing icon assignment 0; missing localisation 0; missing `.gfx` icon definitions 0; same-row `dx <= 1` pairs reduced to 2, both in Ukraine.
- Direct idea/operator grep:
  - `rg -n "add_ideas\\s*=|swap_ideas\\s*=|add_timed_idea\\s*=|<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Result: no matches.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - Result: clean.
- Post-patch pathline heuristic:
  - Result: total risk signals 115; FTH reduced to 2 multi-parent convergence signals; no FTH same-row `dx = 1` crowding remains.

Skipped validation:
- No in-game load or visual screenshot validation was run in this subagent pass.
- No decision/scripted-effect validation was run because the only gameplay file patch was focus coordinate-only.
- No localisation encoding write was needed because localisation was not edited.

## Remaining Route Risks

- Broad rework is still required. This pass did not and should not attempt to make 33 weak trees complete.
- The custom splinter file remains the largest content-quality risk: 1005 focuses, 550 flat reward focuses, 266 tiny equipment/factory focuses, and 99 repeated icon groups.
- Ukraine and Kazakhstan are the highest layout-risk republic trees. Ukraine still has the only two exact `dx = 1` same-row focus crowding pairs left in the four-file audit.
- Ancient restorations remain shallow stubs. They are readable, but not deep enough for the requested lore-specific overpowered chaos-country standard.
- The parent should treat this handoff as an audit plus a tiny layout cleanup, not as completion of the Soviet Collapse focus-tree rework.

## Plan Handoff Path

This handoff is the plan/audit artifact:

`docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_soviet_collapse_focus_all_trees_current_audit_handoff.md`

No separate broad improvement plan was written because `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` already exists and remains valid. This current handoff updates the counts and priorities from the actual current repo state.
