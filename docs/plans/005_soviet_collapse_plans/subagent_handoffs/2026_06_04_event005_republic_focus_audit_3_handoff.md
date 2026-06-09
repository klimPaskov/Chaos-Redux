# Event005 Republic Focus Audit 3 Handoff

Scope: bounded audit and patch of Event005 Soviet Collapse republic focus trees, focused on Ukraine and Belarus in `common/national_focus/005_soviet_collapse_republics.txt`.

Context note: the worktree and `common/national_focus/005_soviet_collapse_republics.txt` already had broad uncommitted changes before this pass. This handoff lists only this audit's scoped edits. No flag assets, `gfx/flags`, `interface/flags`, `.tga/.dds` flag files, flag-related interface definitions, or Event006 files were touched by this pass.

## Changed Files

| File | Change type |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Bounded Ukraine/Belarus route-lock cleanup, local formatting cleanup, and Belarus reward-depth patch. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_republic_focus_audit_3_handoff.md` | Required subagent handoff. |

## Focus IDs Patched

| Focus id | Change |
| --- | --- |
| `ukr_soviet_collapse_socialist_republic_without_moscow` | Removed redundant visible `mutually_exclusive` links. Existing hidden availability lock still blocks other Ukraine route choices after any route is completed. |
| `ukr_soviet_collapse_black_banner_compact` | Removed redundant visible `mutually_exclusive` links. Chaos-tier branch gate and hidden route lock remain. |
| `ukr_soviet_collapse_elections_under_shellfire` | Removed redundant visible `mutually_exclusive` links. Hidden route lock remains. |
| `ukr_soviet_collapse_officers_above_parties` | Removed redundant visible `mutually_exclusive` link. Hidden route lock remains. |
| `ukr_soviet_collapse_protectorate_debate` | Removed redundant visible `mutually_exclusive` link. Hidden route lock and liaison-office gate remain. |
| `ukr_soviet_collapse_grain_loan` | Normalized local `completion_reward` indentation only. |
| `ukr_soviet_collapse_british_caution` | Normalized over-indented focus header fields only. |
| `ukr_soviet_collapse_ports_need_soldiers` | Normalized over-indented `x` coordinate line only. |
| `blr_soviet_collapse_national_council_of_minsk` | Removed redundant visible `mutually_exclusive` links and normalized route-lock block indentation. Hidden route lock remains. |
| `blr_soviet_collapse_socialist_autonomy_without_moscow` | Removed redundant visible `mutually_exclusive` links and normalized route-lock block indentation. Hidden route lock remains. |
| `blr_soviet_collapse_military_transit_directorate` | Removed redundant visible `mutually_exclusive` links and normalized route-lock block indentation. Hidden route lock remains. |
| `blr_soviet_collapse_foreign_corridor_administration` | Removed redundant visible `mutually_exclusive` links and normalized route-lock block indentation. Hidden route lock and foreign-appetite gate remain. |
| `blr_soviet_collapse_orders_printed_like_timetables` | Replaced a shallow repeated military-helper reward with direct command XP, depot control, a spawned mobile column, and a rail construction payoff. |
| `blr_soviet_collapse_forest_defense_staff` | Added the existing Republican Mobile Column template unlock and a resilience variable gain. |

## Behavior Before And After

| Area | Before | After |
| --- | --- | --- |
| Ukraine route-choice row | The route focuses were already locked by hidden `NOT has_completed_focus` checks, but also drew redundant mutual-exclusion lines between route choices. | Route lock behavior remains through hidden availability checks, while the visible mutual-exclusion pathline web is removed from the main route row. |
| Belarus route-choice row | Four route focuses formed a complete visible mutual-exclusion graph while also using hidden route-completion locks, producing dense crossing lines near the fork. | Route lock behavior remains through hidden availability checks, while the visible complete-graph exclusion lines are removed. |
| Belarus military transit follow-up | `orders_printed_like_timetables` gave command power and another military consolidation helper call. | It now gives a concrete rail-security package: command power, army XP, depot control, one mobile column, and a rail construction level. |
| Belarus forest branch | `forest_defense_staff` gave war support and army XP only. | It now also unlocks the Republican Mobile Column template and improves independence resilience. |

## Validation

| Check | Result |
| --- | --- |
| Required reference pass | Read the requested repo skills, offline core wiki pages, offline National Focus wiki page, vanilla effects/triggers/script concept docs, and relevant existing Event005 helpers/decisions before editing. |
| `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt` | Passed with no output. |
| `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt` | No matches. |
| Brace-balance check | `common/national_focus/005_soviet_collapse_republics.txt: brace_depth=0 min_depth=0 bad=[]`. |
| Targeted route-lock exclusion scan | No visible `mutually_exclusive` links remain among the targeted Ukraine and Belarus route-choice rows. |
| Ukraine/Belarus coordinate and prerequisite audit | Ukraine: 83 parsed focuses, no duplicate coordinates, no parent-at-or-below-child prerequisites, no missing same-prefix prerequisites. Belarus: 53 parsed focuses, same results. |

## Remaining Risks

1. No in-game screenshot or live focus-tree rendering check was available in this subagent pass.
2. Removing visible mutual-exclusion links keeps functional route locking but changes UI communication from red exclusion lines to unavailable route focuses once another route is completed.
3. The broader file still contains pre-existing uncommitted edits outside this tranche; parent review should isolate this handoff from earlier dirty-worktree state.
