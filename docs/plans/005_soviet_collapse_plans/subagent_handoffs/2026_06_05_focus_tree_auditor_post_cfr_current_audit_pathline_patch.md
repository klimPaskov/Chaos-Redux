# Event005 Focus Tree Auditor Handoff: Post-CFR Current-State Audit

## Scope

Fresh focus-tree audit after the parent CFR/Construction Directorate tranche recorded in `2026_06_05_parent_cfr_construction_focus_depth_tranche.md`.

This is not a completion claim for Event005. The parent goal remains broad and incomplete.

Flags and visual assets were out of scope. I did not inspect, edit, or touch `gfx/flags`, flag sprites, images, or assets.

## Files Audited

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` only for focus reward helper interpretation

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md`

## Bounded Patch

Changed current worktree position for:

- `CFR_the_concrete_committee`: from current `x = 27 y = 6` to `x = 27 y = 5`

Reason:

- Before the patch, the heuristic path from `CFR_the_unfinished_city_speaks` at `(17, 4)` to `CFR_the_concrete_committee` at `(27, 6)` ran horizontally through `CFR_invite_the_foreign_contract_board` at `(19, 6)`.
- After the patch, the same parent-to-child line no longer crosses that sibling route focus.

Safety:

- One coordinate only.
- Same parent, same reward, same AI, same branch identity.
- No flags, assets, localisation, scripted effects, decisions, or icons touched.

Note:

- `005_soviet_collapse_factory_successors.txt` was already heavily modified in the parent worktree. This patch is relative to the current dirty worktree state, not a clean HEAD-only diff.

## Audit Summary

Counts from the four audited focus files:

- Total focus blocks parsed: 1,698
- Duplicate focus IDs inside audited Event005 files: 0
- Duplicate focus IDs against `common/national_focus/*.txt` for audited Event005 IDs: 0
- Coordinate duplicates: 0
- Missing or recursive `relative_position_id`: 0
- Parent focus at or below child focus: 0
- Mutually-exclusive line-through-focus heuristic hits: 0
- Continuous focus panel proximity risks: 0
- Unsupported `<=` or `>=` operators in audited focus files: 0
- Direct `add_ideas`, `remove_ideas`, `swap_ideas`, or `add_timed_idea` inside focus rewards: 0

## Idea Spam Findings

No audited focus block directly adds, removes, swaps, or times ideas.

Focus-called scripted helpers that still touch ideas:

- `soviet_collapse_add_republic_focus_recovery_progress`: called by focuses 11 times. It can remove `soviet_collapse_republican_startup_disorder` and `soviet_collapse_republican_startup_disorder_mitigated` when recovery completes.
- `soviet_collapse_clear_focus_starting_tension_ideas`: called by focuses 7 times. It removes tag-specific opening tension ideas for `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, and `OGB`.

Assessment:

- The direct focus idea spam problem is currently reduced to helper-mediated idea lifecycle work.
- These two helpers are cleanup-oriented rather than additive spam, but their repeated focus usage should still be reviewed so they do not fire redundant cleanup every route step.

## Shallow Reward Findings

The shallow reward scan remains the largest active problem. The broad signature found 1,127 focus rewards that are helper-only or nearly helper-only without visible unlocks such as decisions, units, claims, cores, war goals, missions, tech, advisors, events, or route mechanics.

By file:

- `005_soviet_collapse_republics.txt`: 387
- `005_soviet_collapse_custom_splinters.txt`: 616
- `005_soviet_collapse_factory_successors.txt`: 90
- `005_soviet_collapse_ancient_restorations.txt`: 34

Highest repeated helper calls in focus rewards:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 142
- `soviet_collapse_apply_focus_military_consolidation`: 131
- `soviet_collapse_apply_focus_legal_recognition`: 108
- `soviet_collapse_apply_focus_republican_compact_plan`: 95
- `soviet_collapse_apply_focus_foreign_channel`: 66
- `soviet_collapse_apply_focus_security_supply_plan`: 65
- `soviet_collapse_apply_focus_high_chaos_identity`: 54
- `soviet_collapse_apply_focus_chaos_assault_plan`: 50

Recommended parent patch order for reward depth:

1. `005_soviet_collapse_custom_splinters.txt`: highest shallow count and many repeated generic identity helpers. Prioritize high-chaos and aggression branches first.
2. `005_soviet_collapse_republics.txt`: Ukraine, Belarus, Kazakhstan, Baltic, and fallback breakaway trees still have many helper-only political/military/foreign route nodes.
3. `005_soviet_collapse_factory_successors.txt`: CFR is improved by the parent tranche, but MFR still has 22 pathline risks and many helper-only arsenal route rewards.
4. `005_soviet_collapse_ancient_restorations.txt`: lowest shallow count; keep as follow-up after major countries and chaos splinters.

## Layout Findings

After the bounded patch, the pathline-through-focus heuristic still reports 520 total risks.

Top affected trees:

- Kazakhstan republic tree: 84
- Ukraine republic tree: 40
- Belarus republic tree: 40
- Baltic republic tree: 30
- Moldova republic tree: 22
- UWD custom splinter tree: 22
- MFR factory successor tree: 22
- BAC custom splinter tree: 18
- Internal republic tree: 17
- Caucasus republic tree: 17
- KHC custom splinter tree: 17
- NLC custom splinter tree: 16

Remaining CFR pathline risks:

- `CFR_the_unfinished_city_speaks` to `CFR_elect_the_site_committees` crosses `CFR_publish_the_planners_charter`.
- `CFR_the_board_becomes_the_cabinet` to `CFR_cities_first` crosses `CFR_rails_first`.
- `CFR_the_board_becomes_the_cabinet` to `CFR_contracts_first` crosses `CFR_factories_first`.
- `CFR_the_state_that_builds` to `CFR_buy_peace_with_concrete` crosses `CFR_the_builder_state_marches_east`.

I did not patch these because each needs a small branch layout decision rather than a single safe coordinate nudge.

## Validation Run

- Parsed all four audited focus files for focus counts, duplicate IDs, coordinates, prerequisites, mutual exclusions, relative positions, continuous panel proximity, pathline heuristics, direct idea effects, and helper call frequency.
- Ran unsupported operator scan for `<=` and `>=`: no matches.
- Ran brace balance on all four audited focus files: final depth 0 and minimum depth 0 for each.
- Ran `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt`: no output.
- Ran `git diff --name-only -- gfx/flags`: no output.
- Ran `git status --short -- gfx/flags common/national_focus/005_soviet_collapse_factory_successors.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md`: only the focus file and this handoff file were shown.

## Remaining Risks

- The pathline heuristic is conservative and can overcount, but the highest clusters match the user's visible complaint about bad pathlines and line crossings.
- The shallow reward heuristic intentionally flags helper-only rewards even when the helper may do useful hidden work. The parent should inspect helper payloads before rewriting a focus, but the repeated helper counts show where branch identity is weakest.
- No final Event005 completion claim is supported by this audit.
