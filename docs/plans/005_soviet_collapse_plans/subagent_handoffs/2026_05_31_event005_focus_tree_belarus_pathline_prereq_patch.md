# Event 005 Focus Tree Audit/Patch Handoff - Belarus Pathline Prerequisites

Date: 2026-05-31
Agent: Chaos Redux focus-tree subagent
Scope: bounded active audit and small patch for Event 005 Soviet Collapse focus depth/layout/reward spam.

## Files Inspected

| File | Trees | Focuses | Icon assignments | Notes |
| --- | ---: | ---: | ---: | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 | 501 | Ukraine, Belarus, Kazakhstan, and shared republic trees are present. Patch applied only to Belarus focus pathline prerequisites. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 1005 | Large chaos-splinter surface remains too broad for this tranche. No file edits. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 | 128 | CFR/MFR/OGB inspected. OGB remains a shallow high-chaos successor needing broader route depth. No file edits. |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | 64 | Ancient restorations remain 16-focus stubs with repeated small stockpile/building rewards. No file edits. |

## Route Coverage Table

| Required route/problem | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine should not feel ugly/linear | `soviet_collapse_ukraine_focus_tree` | Partial, not patched here | The tree is large and has route families, but still needs a full layout pass around route selectors, Black Sea/Bread State/League lanes, and reward identity. Avoided broad movement to prevent conflict with parent work. |
| Belarus spacing/pathlines | `soviet_collapse_belarus_focus_tree` | Patched locally | Several focuses used hidden `available` gates for real prerequisites or one OR prerequisite block where the gate required statehood plus a route. Patched visible prerequisites and cleaned two malformed focus indent blocks. |
| Chaos countries need OP identity-driven trees | Custom splinter trees in `005_soviet_collapse_custom_splinters.txt`; OGB in `005_soviet_collapse_factory_successors.txt` | Needs broader work | Existing trees are numerous and icon-covered, but many still use similar reward rhythm. OP identity specialization should be planned/implemented by route family rather than one-off reward swaps. |
| Ancient restorations should have real depth | KZR/SOG/KHW/ALN ancient focus trees | Needs broader work | 16-focus trees have claims and decision hooks, but remain shallow compared with the spec. Broader branch additions should be parent-owned. |
| Reward spam / idea spam | All four named files | Partial | This tranche did not add ideas. It reduced hover/pathline noise in Belarus by turning hidden completed-focus gates into real visible prerequisites. Repeated small stockpile/building rewards remain, especially ancient/restoration and selected custom splinter routes. |

## High-Priority Fixes Applied

Changed file:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus ids:

- `blr_soviet_collapse_which_road_is_belarus`
- `blr_soviet_collapse_council_bargains_with_forests`
- `blr_soviet_collapse_red_without_the_center`
- `blr_soviet_collapse_orders_printed_like_timetables`
- `blr_soviet_collapse_guide_companies`
- `blr_soviet_collapse_swamp_roads_closed`
- `blr_soviet_collapse_the_forest_general_staff`
- `blr_soviet_collapse_a_forest_that_can_govern`
- `blr_soviet_collapse_prepare_league_freight_tables`
- `blr_soviet_collapse_join_the_league_when_war_comes`
- `blr_soviet_collapse_minsk_supplies_the_front`
- `blr_soviet_collapse_railway_neutrality`
- `blr_soviet_collapse_rail_war_state`
- `blr_soviet_collapse_the_forest_state_rumor`
- `blr_soviet_collapse_armored_train_workshops`
- `blr_soviet_collapse_the_league_depot_at_minsk`

Before:

- Several Belarus focuses had only one visible prerequisite while `available` required another completed focus.
- `blr_soviet_collapse_join_the_league_when_war_comes` used one prerequisite block containing `state_between_armies` and all four route selectors, which is OR semantics. The `available` block required `state_between_armies` plus one route selector, so the pathline/unlock display was misleading.
- `blr_soviet_collapse_the_forest_general_staff` used one prerequisite block for two focuses, giving OR path semantics while `available` required both.
- Two Belarus focus blocks had extra indentation around `focus = {` / `id =`.

After:

- Existing hidden completed-focus requirements are now visible prerequisites where they are true structural dependencies.
- OR route choices remain as a single prerequisite block only where the route choice is genuinely OR.
- AND dependencies are split into separate prerequisite blocks.
- Redundant completed-focus `available` gates were removed where prerequisites now encode the same condition.
- Non-completed dynamic gates remain in `available`, such as chaos-tier/pressure/faction-state checks.

## Icon Coverage Table

| Surface | Coverage | Notes |
| --- | ---: | --- |
| Republics | 501 icons / 501 focuses | No icon ids changed. Existing repeated/generic icon quality still needs a visual audit. |
| Custom splinters | 1005 icons / 1005 focuses | No icon ids changed. Coverage exists; identity quality not fully verified in this tranche. |
| Factory successors | 128 icons / 128 focuses | No icon ids changed. |
| Ancient restorations | 64 icons / 64 focuses | No icon ids changed. |

## Localisation And Reward Mismatch List

- No localisation keys changed.
- No focus ids were renamed.
- Patched focuses already had existing localisation surfaces; this patch changed prerequisites/pathlines only.
- Remaining mismatch risk: Belarus route text may still promise corridor/forest/League systems more strongly than the currently visible reward tooltips show. Ukraine and ancient restoration reward text still need a full focus-by-focus reward-tone audit.

## AI Behavior Gaps

- Belarus route selector AI has basic route/context modifiers, but downstream late-branch AI remains mostly `base` plus simple flags.
- Ancient restoration trees have many flat `ai_will_do = { base = ... }` blocks and need route-aware peaceful-symbolic versus expansionist weighting.
- OGB has stronger AI than the 16-focus ancient trees, but still needs a broader OP identity pass if it is meant to be a dangerous chaos successor rather than a compact restoration tag.
- Custom splinter AI was not fully audited in this tranche due file size and parent-conflict risk.

## Missing Or Simplified Content

- Ukraine layout/branch readability remains unresolved.
- Custom splinter OP identity remains unresolved.
- Ancient restoration depth remains unresolved.
- Repeated small stockpile/building rewards remain outside the Belarus pathline patch.
- No new route family, formable chain, decision category, idea, icon, localisation, Event006 file, or flag asset was touched.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_event005_focus_tree_belarus_pathline_prereq_patch.md` passed with no output.
- `git diff --name-only -- gfx/flags` returned no files.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt` returned no unsupported operators.
- Brace balance check on `common/national_focus/005_soviet_collapse_republics.txt` returned `brace_balance=0 min_balance=0`.
- `git diff --name-only -- '*006*'` is not empty because the shared workspace already contains Event006 changes outside this task. This subagent did not edit Event006 files.

## Remaining Route Risks

- The Belarus patch improves visible route/path semantics, but it is not a full layout screenshot validation pass.
- The four inspected files are already dirty from parent work; this handoff lists only the focus ids touched in this subagent tranche.
- Broader route-depth work should continue from `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` or a parent-owned replacement plan.
