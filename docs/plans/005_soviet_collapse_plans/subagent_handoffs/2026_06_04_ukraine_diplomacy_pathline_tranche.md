# Parent Tranche Handoff: Ukraine Diplomacy Pathline Cleanup

## Scope

Bounded Event005 Soviet Collapse focus-tree layout cleanup for the Ukraine tree.

No flag, sprite, gfx, or interface files were touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`

## Identifiers Changed

- `ukr_soviet_collapse_german_liaison_question`
- `ukr_soviet_collapse_protectorate_debate`

## Before

Both focuses pulled direct prerequisite lines from `ukr_soviet_collapse_question_of_statehood`, creating long edges from the statehood fork through or near the route-lock row.

`ukr_soviet_collapse_protectorate_debate` also required `ukr_soviet_collapse_open_the_liaison_offices` only through an `available` check, so its focus pathline did not match the actual route requirement.

## After

- `ukr_soviet_collapse_german_liaison_question` now depends on `ukr_soviet_collapse_foreign_courts_notice_kyiv`.
- `ukr_soviet_collapse_protectorate_debate` now depends on `ukr_soviet_collapse_open_the_liaison_offices`.
- `ukr_soviet_collapse_protectorate_debate` moved to `x = 25, y = 6`, directly below the liaison-office node.
- The redundant `has_completed_focus = ukr_soviet_collapse_open_the_liaison_offices` availability requirement was removed because it is now represented by the prerequisite.

This keeps the foreign/protectorate path inside the diplomacy lane instead of drawing long dependency lines through the opening political route row.

## Validation

- `git diff --check` passed on touched files.
- Brace balance passed on touched script/focus files.
- No unsupported `<=` or `>=` operators found in touched gameplay/localisation files.
- Coordinate/prerequisite inspection confirmed:
  - `foreign_courts_notice_kyiv` remains at `x = 20, y = 4` under `question_of_statehood`.
  - `german_liaison_question` is now at `x = 21, y = 6` under `foreign_courts_notice_kyiv`.
  - `open_the_liaison_offices` remains at `x = 25, y = 5` under `foreign_courts_notice_kyiv`.
  - `protectorate_debate` is now at `x = 25, y = 6` under `open_the_liaison_offices`.
- `git status --short -- gfx/flags interface/flags` returned no scoped flag changes.

## Remaining Gaps

This does not fully solve the Ukraine tree. The focus audit still identifies deeper route-lock and crossing issues in the socialist/democratic lanes, the officer route, and late branch convergence. The next Ukraine layout pass should rebuild the early political route row more comprehensively.
