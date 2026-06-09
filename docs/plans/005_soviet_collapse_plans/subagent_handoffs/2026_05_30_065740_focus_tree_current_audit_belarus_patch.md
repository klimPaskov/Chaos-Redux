# Event 005 Soviet Collapse Focus Tree Current Audit and Belarus Pathline Patch

Date: 2026-05-30 06:57 UTC
Subagent: Chaos Redux focus tree auditor/patch-capable subagent

## Scope and References

Audited the requested focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Read before inspection/editing: `AGENTS.md`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, required offline wiki pages including National focus/Decision/Event/Idea/AI/Localisation/Effects/Triggers/Scopes/Data structures/Modifiers/On actions, vanilla documentation under `~/projects/Hearts of Iron IV/documentation/`, and vanilla focus precedents under `~/projects/Hearts of Iron IV/common/national_focus/`.

The worktree was already dirty in the scoped Event 005 files. This handoff claims only the one focus coordinate patch listed below plus the audit evidence.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_065740_focus_tree_current_audit_belarus_patch.md`

## Patch

| Focus id | File line | Before | After | Why safe |
|---|---:|---|---|---|
| `blr_soviet_collapse_minsk_central_dispatch` | `common/national_focus/005_soviet_collapse_republics.txt:10018` | `x = 8`, `y = 6`; the focus sat on the line from `blr_soviet_collapse_council_bargains_with_forests` to `blr_soviet_collapse_national_council_of_minsk`. | `x = 7`, `y = 6`; no prerequisite, reward, AI, icon, or localisation changed. The touched block indentation was also normalized. | Coordinate-only pathline cleanup. Simulated alternatives showed `x = 7, y = 6` removed the hit without adding same-row adjacency or a new line hit. |

No localisation keys, icon ids, scripted helpers, decisions, or rewards were changed.

## Route Coverage Table

Legend: `families` are detected route surfaces, not proof of quality. `idea ops` counts direct idea maintenance in focus blocks; all add/swap/timed idea spam is currently zero, while hidden `remove_ideas` cleanup remains in eight specific focuses. `mech/dec/exp` are focus counts with direct mechanic, decision, or expansion hooks by scan. `flat` counts focuses with direct flat reward patterns. `AI base-only` counts focuses whose `ai_will_do` appears to be only a base weight.

| Tree | Line | Focuses | Families detected | Helper calls / top repeats | Idea ops | Mech / dec / exp hooks | Flat reward focuses | AI base-only | Icon reuse groups | Layout risk |
|---|---:|---:|---|---|---:|---|---:|---:|---:|---|
| `soviet_collapse_ukraine_focus_tree` | 18 | 83 | political, industry/logistics, military, diplomacy, expansion, high-chaos | 131; military x21, foreign x18, depot x15 | 0 | 8 / 7 / 0 | 52 | 27 | 4 | 23 wide prereqs, 16 wide MEs, 45 line hits |
| `soviet_collapse_breakaway_focus_tree` | 2356 | 36 | political, industry/logistics, military, diplomacy, expansion | 47; military x12, legal x9, depot x9 | 0 | 0 / 0 / 0 | 21 | 18 | 2 | clean by heuristic |
| `soviet_collapse_internal_republic_focus_tree` | 3153 | 62 | political, industry/logistics, military, diplomacy, expansion | 110; depot x24, foreign x20, legal x19 | 0 | 0 / 0 / 0 | 42 | 25 | 3 | 8 wide prereqs, 1 line hit |
| `soviet_collapse_baltic_focus_tree` | 4657 | 42 | political, industry/logistics, military, diplomacy, expansion | 58; legal x14, depot x12, military x12 | 0 | 0 / 0 / 0 | 20 | 18 | 3 | 12 wide prereqs, 3 line hits |
| `soviet_collapse_caucasus_focus_tree` | 5621 | 40 | political, military, diplomacy, expansion | 64; legal x17, depot x16, military x13 | 0 | 2 / 2 / 0 | 21 | 23 | 2 | 8 wide prereqs, 4 line hits |
| `soviet_collapse_central_asia_focus_tree` | 6550 | 45 | political, industry/logistics, military, diplomacy, expansion | 77; legal x20, depot x13, league x12 | 0 | 4 / 3 / 1 | 28 | 15 | 2 | 11 wide prereqs, 4 wide MEs, 2 hits |
| `soviet_collapse_moldova_focus_tree` | 7699 | 48 | political, industry/logistics, military, diplomacy, expansion | 73; legal x19, foreign x14, league x12 | 0 | 1 / 0 / 0 | 31 | 20 | 2 | 18 wide prereqs, 5 hits |
| `soviet_collapse_belarus_focus_tree` | 8867 | 53 | political, industry/logistics, military, diplomacy, expansion | 73; depot x20, military x11, legal x9 | 0 | 4 / 3 / 0 | 33 | 12 | 2 | 19 wide prereqs, 0 hits after patch |
| `soviet_collapse_kazakhstan_focus_tree` | 10199 | 92 | political, industry/logistics, military, diplomacy, expansion | 128; league x24, depot x21, military x21 | 0 | 4 / 4 / 0 | 57 | 61 | 0 | 25 wide prereqs, 2 wide MEs, 19 hits |
| `FTH_soviet_collapse_focus_tree` | 15 | 47 | all major families plus high-chaos | 67; military x11, depot x9, league x8 | 0 | 0 / 0 / 0 | 26 | 0 | 3 | 1 wide prereq |
| `PRA_soviet_collapse_focus_tree` | 1219 | 22 | industry/logistics, military, diplomacy, expansion | 37; legal x7, military x6, depot x6 | 1 | 11 / 11 / 1 | 18 | 0 | 0 | 1 wide prereq |
| `TSC_soviet_collapse_focus_tree` | 1814 | 18 | political, military, diplomacy, expansion | 28; legal x4, high-chaos x4, league x3 | 1 | 1 / 0 / 1 | 13 | 0 | 0 | 1 wide prereq |
| `RMC_soviet_collapse_focus_tree` | 2291 | 18 | political, industry/logistics, military, diplomacy, expansion | 27; high-chaos x4, legal x4, military x3 | 1 | 1 / 0 / 1 | 12 | 0 | 0 | 1 wide prereq |
| `DSC_soviet_collapse_focus_tree` | 2775 | 18 | political, industry/logistics, military, diplomacy, expansion | 29; high-chaos x6, military x6, legal x4 | 1 | 8 / 5 / 2 | 14 | 0 | 0 | 1 wide prereq |
| `NRF_soviet_collapse_focus_tree` | 3351 | 18 | political, industry/logistics, military, diplomacy, expansion | 23; high-chaos x5, legal x4, league x3 | 1 | 5 / 4 / 1 | 15 | 0 | 0 | 1 wide prereq |
| `ICD_soviet_collapse_focus_tree` | 3854 | 18 | industry/logistics, military, diplomacy, expansion | 23; legal x4, high-chaos x4, league x3 | 1 | 1 / 0 / 1 | 13 | 0 | 0 | 1 wide prereq |
| `BSC_soviet_collapse_focus_tree` | 4328 | 47 | all major families plus high-chaos | 44; league x7, legal x4, idea update x3 | 0 | 0 / 0 / 0 | 28 | 0 | 3 | clean by heuristic |
| `TNC_soviet_collapse_focus_tree` | 5457 | 47 | all major families plus high-chaos | 44; league x6, legal x5, idea update x3 | 0 | 0 / 0 / 0 | 26 | 0 | 3 | clean by heuristic |
| `ALA_soviet_collapse_focus_tree` | 6594 | 47 | all major families plus high-chaos | 47; legal x6, league x5, military x4 | 0 | 0 / 0 / 0 | 24 | 0 | 3 | clean by heuristic |
| `BBH_soviet_collapse_focus_tree` | 7713 | 47 | all major families plus high-chaos | 60; military x8, legal x6, pressure x6 | 0 | 0 / 0 / 0 | 25 | 0 | 3 | 1 wide prereq |
| `KRS_soviet_collapse_focus_tree` | 8917 | 47 | all major families plus high-chaos | 64; military x12, depot x9, legal x7 | 0 | 0 / 0 / 0 | 27 | 0 | 3 | 1 wide prereq |
| `UDC_soviet_collapse_focus_tree` | 10159 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 62; legal x8, league x5, command x5 | 0 | 0 / 0 / 0 | 23 | 0 | 0 | 6 wide prereqs |
| `SDZ_soviet_collapse_focus_tree` | 11359 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 62; legal x8, league x5, archive x5 | 0 | 0 / 0 / 0 | 23 | 0 | 0 | 6 wide prereqs |
| `GAC_soviet_collapse_focus_tree` | 12603 | 47 | all major families plus high-chaos | 59; legal x8, league x6, military x5 | 0 | 0 / 0 / 0 | 25 | 0 | 0 | 2 wide prereqs |
| `DHC_soviet_collapse_focus_tree` | 13785 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 50; legal x5, idea update x4, league x4 | 0 | 0 / 0 / 0 | 23 | 0 | 2 | 4 wide prereqs, 1 hit |
| `KHC_soviet_collapse_focus_tree` | 14990 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 49; legal x5, idea update x4, league x4 | 0 | 0 / 0 / 0 | 25 | 0 | 3 | 4 wide prereqs, 1 hit |
| `FEV_soviet_collapse_focus_tree` | 16188 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 63; depot x10, legal x8, military x6 | 0 | 0 / 0 / 0 | 22 | 12 | 13 | 10 wide prereqs |
| `SZA_soviet_collapse_focus_tree` | 17363 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 66; depot x9, legal x8, military x5 | 0 | 0 / 0 / 0 | 21 | 13 | 12 | 10 wide prereqs |
| `UWD_soviet_collapse_focus_tree` | 18543 | 47 | all major families plus high-chaos | 54; legal x7, depot x7, military x5 | 0 | 0 / 0 / 0 | 25 | 11 | 15 | 12 wide prereqs, 3 hits |
| `MRC_soviet_collapse_focus_tree` | 19747 | 47 | all major families plus high-chaos | 54; military x7, legal x6, depot x5 | 1 | 0 / 0 / 0 | 23 | 9 | 12 | 5 wide prereqs |
| `IUL_soviet_collapse_focus_tree` | 20923 | 47 | all major families plus high-chaos | 62; legal x10, depot x9, league x6 | 0 | 0 / 0 / 0 | 22 | 11 | 15 | 6 wide prereqs |
| `BAC_soviet_collapse_focus_tree` | 22080 | 47 | all major families plus high-chaos | 59; legal x9, depot x7, military x7 | 0 | 0 / 0 / 0 | 23 | 12 | 3 | 6 wide prereqs, 1 hit |
| `ARD_soviet_collapse_focus_tree` | 23225 | 47 | industry/logistics, military, diplomacy, expansion, high-chaos | 61; military x9, legal x9, depot x7 | 0 | 3 / 3 / 0 | 28 | 11 | 3 | 2 wide prereqs |
| `NLC_soviet_collapse_focus_tree` | 24423 | 47 | all major families plus high-chaos | 62; idea update x7, legal x7, foreign x6 | 0 | 0 / 0 / 0 | 26 | 5 | 3 | 7 wide prereqs, 4 hits |
| `CFR_soviet_collapse_focus_tree` | 16 | 47 | political, industry/logistics, military, diplomacy, expansion | 50; mandate x6, public works x6, housing x4 | 0 | 5 / 4 / 2 | 18 | 0 | 11 | clean by heuristic |
| `OGB_soviet_collapse_focus_tree` | 1136 | 23 | political, industry/logistics, military, expansion | 11; idea update x4, legal x2, pressure x2 | 1 | 4 / 0 / 3 | 18 | 0 | 0 | clean by heuristic |
| `MFR_soviet_collapse_focus_tree` | 1713 | 58 | political, industry/logistics, military, diplomacy, expansion | 61; security x4, client arms x4, unsafe output x4 | 0 | 5 / 3 / 1 | 17 | 0 | 0 | clean by heuristic |

## Worst Offenders With Line References

- Ukraine: `soviet_collapse_ukraine_focus_tree` at `005_soviet_collapse_republics.txt:18` remains the worst layout offender. The route selectors `ukr_soviet_collapse_socialist_republic_without_moscow` (`:228`), `ukr_soviet_collapse_black_banner_compact` (`:267`), `ukr_soviet_collapse_elections_under_shellfire` (`:312`), `ukr_soviet_collapse_officers_above_parties` (`:541`), and `ukr_soviet_collapse_protectorate_debate` (`:1708`) produce very wide mutual-exclusion and prerequisite geometry. This needs a deliberate route layout pass, not another one-node move.
- Belarus: patched one exact hit around `blr_soviet_collapse_minsk_central_dispatch` (`005_soviet_collapse_republics.txt:10018`). Remaining Belarus risk is wide, dense routing around `blr_soviet_collapse_which_road_is_belarus` (`:8953`) and the four route selectors at `:9040`, `:9067`, `:9097`, and `:9127`.
- Kazakhstan: `soviet_collapse_kazakhstan_focus_tree` (`005_soviet_collapse_republics.txt:10199`) is the largest tree and still has 25 wide prerequisite lines, 19 heuristic line hits, 57 flat reward focuses, and 61 base-only AI blocks.
- `PRA_soviet_collapse_focus_tree` (`005_soviet_collapse_custom_splinters.txt:1219`) is short but has the best decision integration among compact chaos trees: 22 focuses, 11 decision hooks. It remains flat-reward heavy.
- `TSC_soviet_collapse_focus_tree` (`:1814`), `ICD_soviet_collapse_focus_tree` (`:3854`), `DSC_soviet_collapse_focus_tree` (`:2775`), and `NRF_soviet_collapse_focus_tree` (`:3351`) are 18-focus crisis trees. They cannot satisfy the requested overpowered, lore-mechanic-connected country standard without a real route expansion.
- `OGB_soviet_collapse_focus_tree` (`005_soviet_collapse_factory_successors.txt:1136`) has only 23 focuses, no decision unlocks by direct scan, and only 11 helper calls. It is the clearest factory-successor depth failure.
- `CFR_soviet_collapse_focus_tree` (`:16`) and `MFR_soviet_collapse_focus_tree` (`:1713`) are mechanically better than `OGB`, but still lean on repeated local helper families and need route specialization.
- Full custom splinters with 47 focuses but zero direct decision/expansion hooks by scan: `BSC` (`:4328`), `TNC` (`:5457`), `ALA` (`:6594`), `BBH` (`:7713`), `KRS` (`:8917`), `UDC` (`:10159`), `SDZ` (`:11359`), `GAC` (`:12603`), `DHC` (`:13785`), `KHC` (`:14990`), `FEV` (`:16188`), `SZA` (`:17363`), `UWD` (`:18543`), `MRC` (`:19747`), `IUL` (`:20923`), `BAC` (`:22080`), and `NLC` (`:24423`).
- Naval/port lore mismatch remains high in `NRF`, `ARD`, `KRS`, and `NLC`: they need port control, convoy/raid, naval war, coastal integration, and AI target loops rather than more convoy/XP rewards.

## Missing Or Simplified Content

1. The full rework remains incomplete. Many trees have route labels but not enough route mechanics, decisions, postwar handling, leader/advisor/law changes, unit templates, or map consequences.
2. Chaos countries are still not consistently overpowered through lore-specific mechanics. `DSC` and `NRF` have some hooks; `TSC`, `ICD`, and `OGB` are still too shallow; most 47-focus custom splinters have no direct decision or expansion hooks.
3. Decision integration is uneven. Ukraine, PRA, DSC, NRF, ARD, CFR, MFR, Belarus, Kazakhstan, Central Asia, and Caucasus have some direct hooks. Many other trees have zero direct decision unlocks.
4. Expansion and postwar handling are thin. Direct expansion hooks are absent from Ukraine, Belarus, Kazakhstan, Moldova, Baltic, internal republics, and most 47-focus custom splinters by scan.
5. Flat reward density remains high: 893 focuses across the three scoped files include direct flat reward patterns. The largest offenders are Kazakhstan 57, Ukraine 52, internal republics 42, Belarus 33, Moldova 31, ARD 28, BSC 28, Central Asia 28, and KRS 27.
6. Direct idea add/swap/timed spam is gone, but hidden idea refresh remains frequent and repeated helper rhythm remains high. This is better for hover readability, but not enough for route depth.

## Icon Coverage

| File | Missing icon assignments | Repeated icon groups | Notes |
|---|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 0 by scan | 20+ groups | Top repeats include `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`, `GFX_central_asia_soviet_collapse_steppe_federation`, and `GFX_moldova_soviet_collapse_ukrainian_corridor`. |
| `005_soviet_collapse_custom_splinters.txt` | 0 by scan | 90+ groups | Worst repeated families include `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, and `GFX_focus_IUL_war_plan`. |
| `005_soviet_collapse_factory_successors.txt` | 0 by scan | 11 groups | CFR repeats several construction-state icons three times each; OGB and MFR are cleaner. |

No icon ids were changed. Technically load-safe icon coverage is better than design-quality icon coverage.

## Localisation And Reward Mismatch

- No localisation files were edited.
- Previous audits found no missing focus title/description keys; I did not rerun the full localisation scan in this pass because no focus ids or localisation keys changed.
- Reward mismatch remains mostly design-level: focus titles imply rail states, dead armies, revenant fleets, factory polities, and restoration states, but many rewards still resolve to the same helper families plus flat stats/equipment.
- The eight direct hidden `remove_ideas` cleanups remain in `OGB_the_council_takes_the_seal`, `PRA_the_board_overrules_ministers`, `TSC_the_committee_of_instruments`, `RMC_communes_of_witnesses`, `DSC_witness_officers`, `NRF_living_harbor_committees`, `ICD_commissars_of_last_addresses`, and `mrc_protect_village_autonomy`. They are hidden where inspected and do not create visible remove-idea spam.

## AI Behavior Gaps

- No focus is missing an `ai_will_do` block by scan.
- Route-aware AI is still weak. Base-only or near-base AI is especially high in Kazakhstan, Ukraine, internal republics, Moldova, Caucasus, Baltic, FEV, SZA, UWD, IUL, BAC, and ARD.
- Chaos country endpoints need persistent `add_ai_strategy` and target logic tied to their lore. Some individual focuses do this, but it is not systematic.
- Decision-target AI cannot be fully assessed from focus files alone. Trees with zero decision hooks cannot yet express meaningful route-aware decision behavior through focus unlocks.

## High-Priority Fixes First

1. Full Ukraine route layout pass around the five route selectors listed above. Current line density is too high for a safe one-focus patch.
2. Kazakhstan route and AI pass. It has the most focuses, the most flat rewards, and the most base-only AI.
3. Deepen `OGB`, `TSC`, `ICD`, `DSC`, `NRF`, and `PRA` into actual chaos/special-state route trees, or explicitly classify them as compact crisis actors and document the limitation. Current depth does not satisfy the complaint.
4. Add direct decision/mission hooks to 47-focus custom splinters that currently have zero, starting with `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `NLC`, `KRS`, and the host trees.
5. Replace flat reward ladders with route-specific mechanics: port control, rail authority decisions, grave-roll recruitment, factory contract systems, state integration, postwar claims/cores, and aggressive AI strategies.
6. Icon pass after route depth changes. Do not spend asset effort before the route structure is stable.

## Validation Run

Passed:

```sh
git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt
```

Brace balance:

```text
common/national_focus/005_soviet_collapse_republics.txt: final_depth=0 min_depth=0
common/national_focus/005_soviet_collapse_custom_splinters.txt: final_depth=0 min_depth=0
common/national_focus/005_soviet_collapse_factory_successors.txt: final_depth=0 min_depth=0
```

Other checks:

- Unsupported `<=` / `>=` in the three scoped focus files: none.
- Belarus pathline hit recheck after patch: `0`.
- Continuous focus panel obstruction heuristic across the three scoped files: `0` risk hits.
- Duplicate focus ids by fresh parser: none.
- Direct duplicate same-helper calls within one focus: none found.
- Direct add/swap/timed idea focus operations: none found.

Skipped validation:

- No in-game launch, screenshot, or HOI4 external parser validation was run.
- No full localisation scan rerun after this patch because no localisation ids changed.
- No commit was made, per instruction.

## Remaining Route Risks

The user complaint is still valid overall. This pass fixed one narrow Belarus pathline issue and provides current evidence, but the large design problem remains: the trees are much larger than stubs in many places, yet too many branches still deliver generic helper calls, flat rewards, weak direct mechanics, weak expansion/postwar handling, repeated icons, and base-weight AI. A full rework remains incomplete.

No new improvement plan was written because `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` already covers the broad route redesign backlog and remains accurate.
