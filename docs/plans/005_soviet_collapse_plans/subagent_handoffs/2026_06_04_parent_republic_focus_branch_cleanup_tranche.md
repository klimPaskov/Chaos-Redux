# Event 005 Soviet Collapse Republic Focus Branch Cleanup Tranche

## Scope

Parent implementation pass for the current focus-tree cleanup request.

Touched file:

- `common/national_focus/005_soviet_collapse_republics.txt`

Untouched by design:

- `gfx/flags/`

## Changes

- Ukraine:
  - Moved the military-directory route out of the center/industry lane.
  - Moved `ukr_soviet_collapse_officer_patronage_lists` away from the mutual-exclusion row between `ukr_soviet_collapse_army_supremacy` and `ukr_soviet_collapse_mixed_emergency_cabinet`.
  - Removed the cross-branch `ukr_soviet_collapse_foreign_advisers_in_plain_coats` prerequisite from `ukr_soviet_collapse_purge_moscow_loyalists`; the purge now follows the socialist worker route instead of drawing a long line through the foreign-adviser lane.
  - Removed the economy cross-prerequisite from `ukr_soviet_collapse_officer_patronage_lists`; officer patronage now follows the military-directory route instead of drawing from the grain-loan branch.
  - Repositioned democratic autonomy/governor focuses into the political lane.
  - Repositioned army/Black Sea military focuses into the military and expansion lane.
  - Added a real branch payoff to `ukr_soviet_collapse_the_western_question_cannot_wait`: it now opens the external-border arbitration surface and shows the matching decision unlock.

- Belarus:
  - Moved `blr_soviet_collapse_last_train_east` out of the row of core route choices.
  - Moved `blr_soviet_collapse_orders_printed_like_timetables` to reduce crowding in the rail/military transition.
  - Reworked `blr_soviet_collapse_council_bargains_with_forests` from a generic legality/stability reward into a republican compact bridge that integrates forest committees and points players toward regional defense and recognition goal decisions.

- Reward identity:
  - `ukr_soviet_collapse_elections_under_shellfire` now opens the Ukrainian League Council and League Arbitration Board decision path.
  - `ukr_soviet_collapse_republic_of_laws` now unlocks League arbitration and anti-client charter decisions.
  - `ukr_soviet_collapse_civilian_command_over_the_army` now unlocks shared League unit deployment decisions.
  - `OGB_scholars_guard_the_charter` and `OGB_clerics_guard_the_charter` are no longer near-identical route choices: scholars now emphasize registers, recognition, and institutional legitimacy; clerics now emphasize manpower, social order, and early Kazan ferry guard access.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`
- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt common/decisions/005_soviet_collapse_decisions.txt`
- Brace-balance scan: `common/national_focus/005_soviet_collapse_republics.txt brace_balance 0`
- Unsupported-operator scan: no `<=` or `>=` in the touched focus file.
- Coordinate scan: no exact focus-coordinate duplicates in the Ukraine or Belarus focus trees.
- Flag safety check: `git status --short -- gfx/flags` returned no changes.

## Remaining Risks

- This is a focused tranche, not a full all-tree rewrite.
- The broad request still needs a full pass over all Soviet Collapse republic, custom splinter, factory successor, and ancient restoration trees for branch depth, route clarity, reward identity, and pathline crossings.
- The focus audit subagent for the wider pass was still running when this handoff was written.
