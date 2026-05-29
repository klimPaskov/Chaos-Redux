# Soviet Collapse Focus Tree Audit and Patch Handoff

Subagent: chaos-redux focus tree auditor  
Date: 2026-05-29  
Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- Directly related scripted helpers were inspected but not edited.

## References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- Offline Paradox wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`.
- Vanilla focus precedents: `generic.txt`, `soviet.txt`, `baltic_shared.txt`.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Subagent-owned hunk: moved one Moldova focus down one row to clear a mutual-exclusion/pathline collision. This file already has broader modified Ukraine hunks in the current worktree; those are treated as parent/user state and are not claimed here. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Moved two custom splinter focuses one row up to remove same-row prerequisite lines; removed two duplicate equipment reward lines. |

Other modified files in the worktree were outside this subagent scope and were not touched.

## Changed Focus IDs

| Focus id | File/line after patch | Before | After |
| --- | --- | --- | --- |
| `moldova_soviet_collapse_river_guard_brigades` | `common/national_focus/005_soviet_collapse_republics.txt:7770` | `x = 12`, `y = 4`; sat on a mutual-exclusion midpoint between `moldova_soviet_collapse_dniester_defense_directorate` and `moldova_soviet_collapse_ukrainian_border_compact`. | `x = 12`, `y = 5`; clears the marker/line collision without changing route logic. |
| `BBH_settlement` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:8191` | `x = 8`, `y = 8`; same row as an OR prerequisite path into `BBH_industry_plan`. | `x = 8`, `y = 7`; prerequisite line now runs downward. |
| `BBH_red_and_black_depots` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:8353` | Granted the same `support_equipment_1` stockpile reward twice. | Grants the stockpile reward once and keeps the factory/helper payoff. |
| `KHC_laba_rear_area` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:15298` | Granted the same small `support_equipment_1` stockpile reward twice. | Grants the support equipment once and keeps artillery, building, variable, recovery, and idea-update rewards. |
| `UWD_workers_canteen_compact` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:19014` | `x = 7`, `y = 8`; same row as prerequisite path into `UWD_kama_foundry_contracts`. | `x = 7`, `y = 7`; prerequisite line now runs downward. |

No localisation keys or icon ids were changed.

## Route Coverage Table

| Required route/content area | Implemented route or branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine political identity and statehood routes | `soviet_collapse_ukraine_focus_tree`, 83 focuses, starts at `common/national_focus/005_soviet_collapse_republics.txt:18` | Present but still needs layout and route clean-up | The current worktree already contains broad Ukraine layout edits outside this subagent hunk. A fresh straight-line detector still finds 8 prerequisite paths passing through other focus coordinates, including `question_of_statehood` to `black_banner_compact` through `socialist_republic_without_moscow` and multiple later foreign/League/Black Banner overlaps. |
| Generic breakaway republic | `soviet_collapse_breakaway_focus_tree`, 36 focuses, line 2250 | Simplified | Has state-building and survival content but limited expansion, decision, and route-specific AI payoff. |
| Internal republic | `soviet_collapse_internal_republic_focus_tree`, 62 focuses, line 3038 | Present but generic | Enough width, but branch payoffs lean on shared helpers and flat construction/equipment. |
| Baltic republics | `soviet_collapse_baltic_focus_tree`, 42 focuses, line 4542 | Present but compact | Political and defensive identity exists; limited direct mechanic and expansion payoff. |
| Caucasus republics | `soviet_collapse_caucasus_focus_tree`, 40 focuses, line 5506 | Present but compact | Needs stronger mountain/league/neighbor conflict hooks. |
| Central Asia | `soviet_collapse_central_asia_focus_tree`, 45 focuses, line 6430 | Present with some expansion | Has direct state claims at lines 7408-7423; still needs deeper decision/postwar handling. |
| Moldova | `soviet_collapse_moldova_focus_tree`, 48 focuses, line 7562 | Present; one layout patch applied | Route structure exists; remaining rewards still lean on standard helpers and flat support. |
| Belarus | `soviet_collapse_belarus_focus_tree`, 53 focuses, line 8731 | Present but needs payoff variety | Needs more distinct military/security/foreign route outcomes. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses, line 10052 | Broad but reward-heavy | Largest republic tree; still has many flat construction/equipment/stat payoffs and repeated helper use. |
| Full custom splinter trees | FTH, BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC each have 47 focuses | Partially present | These trees are playable shells but should become much more dangerous: factories, neighbor aggression, cores/claims, war goals, route-specific decision hooks, and AI strategy. |
| Shallow crisis splinters | PRA has 22 focuses; TSC, RMC, DSC, NRF, ICD each have 18 focuses | Missing depth | These are the weakest route families. They need full political or fixed-purpose hierarchy, industry, military, expansion, and endgame branches instead of short ladders. |
| Chaos/death/zombie-like splinters | RMC, DSC, NRF, ICD, TSC, ARD, NLC, BBH, FTH, BSC, PRA, BAC, GAC, DHC, KHC | Missing dangerous behavior | `common/national_focus/005_soviet_collapse_custom_splinters.txt` contains no direct `create_wargoal`, `declare_war_on`, `add_state_core`, `add_state_claim`, `transfer_state_to`, or `annex_country` effects. |

## Missing or Simplified Content

1. Direct focus idea spam is currently avoided in the focus files: no focus directly adds multiple ideas, no focus directly repeats an idea reward, and no direct external-support self-grants were found.
2. The idea lifecycle is still noisy by design pressure: `soviet_collapse_update_consolidated_republic_ideas` is called 109 times from the two focus files and is defined at `common/scripted_effects/005_soviet_collapse_effects.txt:5060`.
3. Shared focus reward helpers are overused as the main payoff layer: `soviet_collapse_apply_focus_legal_recognition` appears 297 times, `soviet_collapse_apply_focus_military_consolidation` 248 times, `soviet_collapse_apply_focus_depot_and_supply_control` 254 times, `soviet_collapse_apply_focus_league_preparation` 220 times, `soviet_collapse_apply_focus_foreign_channel` 175 times, and `soviet_collapse_apply_focus_high_chaos_identity` 94 times.
4. 812 focuses include at least one flat reward term from `add_equipment_to_stockpile`, `add_building_construction`, `add_manpower`, `army_experience`, `add_stability`, `add_war_support`, or `add_political_power`. Some are appropriate support rewards, but the current density explains the repeated small-reward feel.
5. Custom splinter focus trees do not directly deliver the requested overpowered chaos-country behavior. Neighbor aggression should be implemented through focus-unlocked decisions, claims, war goals, cores, special units, AI strategy, and postwar settlement logic.
6. The 18- and 22-focus custom splinters are shallow enough that they should be redesigned by the parent rather than patched piecemeal by this subagent.
7. Ukraine remains visually risky even after current worktree edits. The current straight-line detector finds 8 paths through other focus coordinates: `question_of_statehood` to `black_banner_compact` through `socialist_republic_without_moscow`; `workers_congress_in_kharkiv` to `purge_moscow_loyalists` through `free_soil_compromise`; `equipment_corridor_authority` to `the_ukrainian_commune_debate` through `dead_fields_living_columns`; `advisers_without_flags` to `equipment_corridor_authority` through `black_sea_hegemony`; `romanian_grain_and_river_bargain` to `carpathian_security_belt` through `republican_deep_battle`; `open_the_liaison_offices` to `ports_need_soldiers` through `direct_national_claims`; `carpathian_security_belt` to `dead_fields_living_columns` through `equipment_corridor_authority`; and `black_soil_oath` to `grain_census_of_everyone` through `black_banner_takes_the_villages`.

## Icon Coverage Table

| Metric | Result |
| --- | --- |
| Focus ids audited | 1506 |
| Focus icons assigned | 1506 |
| Missing focus icon references | 0 |
| Missing sprite definitions in mod/vanilla interface scan | 0 |
| Unique focus icons | 1346 |
| Icons repeated more than twice | 29 |

Repeated icons are not load-breaking, but the 29 repeated icon groups are a visual-quality problem. Prioritize Ukraine and high-chaos custom splinters for a distinct icon pass once route redesigns settle.

## Localisation and Reward Mismatch List

| Area | Finding |
| --- | --- |
| Focus names | 0 missing keys found in the audited focus ids. |
| Focus descriptions | 0 missing description keys found in the audited focus ids. |
| Patched reward text | No localisation changed. `BBH_red_and_black_depots` and `KHC_laba_rear_area` now show one fewer duplicate stockpile line through game effects; their titles/descriptions do not depend on exact duplicate quantities. |
| Reward semantics | Many descriptions imply route-defining consolidation, danger, or state-building while the reward is still mostly factory/equipment/stat helper output. This is a design mismatch rather than missing localisation. |

## AI Behavior Gaps

1. Every audited focus has an `ai_will_do` block, but many weights are local flat weights rather than route strategy.
2. The custom splinter trees do not have enough AI behavior for the requested dangerous chaos-country role: no focus-driven neighbor aggression, no visible high-chaos war plan cadence, and no strong route-aware pressure toward claims, war goals, cores, or postwar behavior.
3. The shallow PRA/TSC/RMC/DSC/NRF/ICD trees need route-aware AI only after they receive real branch families. Adding detailed weights to the current ladders would preserve the shallow structure.
4. Republic trees need AI strategy around League, foreign support, high-chaos escalation, and regional expansion. Focus weights alone are not enough.

## High-Priority Parent Fixes

1. Reflow Ukraine's opening and political/military junctions first. Remove the long diagonal lines out of `ukr_soviet_collapse_question_of_statehood` and keep mutually exclusive markers out of active branch paths.
2. Redesign PRA, TSC, RMC, DSC, NRF, and ICD into full fixed-purpose crisis trees with hierarchy, industry, military, expansion, and endgame branches.
3. Add overpowered chaos-country expansion packages for RMC, DSC, NRF, ICD, TSC, ARD, NLC, BBH, FTH, BSC, PRA, BAC, GAC, DHC, and KHC. Use claims, cores, war goals, neighbor-specific decisions, special units, factories, AI strategy, and postwar settlement hooks.
4. Replace repeated flat reward ladders with mechanic and decision payoffs. Keep small factories/equipment as support rewards, not the identity of a branch.
5. Reduce helper-tooltip noise around consolidated republic ideas. Consider hidden helper refreshes plus custom effect tooltips for the player-facing payoff.
6. Add route-specific AI strategy plans after route content is real. High-chaos tags should actively choose aggression and not sit on generic development ladders.
7. Run an icon differentiation pass after route redesigns, especially for Ukraine and the high-chaos custom splinters.

## Validation Run

- Focus parser/topology audit, grouped by `focus_tree`: 34 trees, 1506 focuses, 0 duplicate focus ids, 0 missing prerequisites, 0 upward prerequisites, 0 same-row prerequisites, 0 duplicate coordinates per tree, 0 mutual-exclusion midpoint collisions per tree.
- Ukraine straight-line visual detector: 8 prerequisite paths still pass through other focus coordinates. This is a layout-quality finding, not a syntax failure.
- Reward duplicate audit: 0 duplicate identical `add_equipment_to_stockpile` entries remaining inside individual focus blocks.
- Direct idea audit: 0 focus blocks directly adding multiple ideas, 0 duplicate direct idea grants.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed.
- Brace check on both edited focus files: final depth 0, early closes 0.
- Unsupported operator check on both focus files for `<=` and `>=`: no matches.

## Skipped Validation

- No in-game load test was run from this subagent.
- No full mod-wide validator was run because the worktree contains many modified files outside this subagent scope.
- No localisation encoding rewrite was performed because no localisation files were edited.

## Remaining Route Risks

- This audit did not complete the full Soviet Collapse focus tree rework. It only applied narrow, safe cleanup and documented the larger route/design work.
- Broad route depth, dangerous chaos expansion, Ukraine layout quality, and mechanic-driven payoff conversion remain parent-owned.
- `common/national_focus/005_soviet_collapse_republics.txt` includes broader current-worktree Ukraine changes outside this subagent-owned patch; parent should review them with the handoff findings before finalizing.
- The custom splinter file still has no direct focus-level war goals, cores, or claims; adding them should be done with decision/postwar hooks rather than raw isolated effects.

## Plan Handoff Path

This handoff is the implementation-ready parent plan:

`docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_audit_patch_handoff.md`
