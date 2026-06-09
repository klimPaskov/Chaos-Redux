# Event 005 parent republic pathline blocker tranche

Date: 2026-06-04

Scope: parent coordinate-only pass for the same-row prerequisite/pathline blockers identified by the fresh focus-tree audit. Flag assets were explicitly out of scope and were not opened or edited.

## Changed files

- `common/national_focus/005_soviet_collapse_republics.txt`

## Layout changes

The following audited same-row parent-child links were moved so the parent and child no longer share the same focus row:

- `ukr_soviet_collapse_appointed_governors`
- `ukr_soviet_collapse_breadbasket_empire`
- `internal_soviet_collapse_crimean_tatar_councils`
- `central_asia_soviet_collapse_local_republic_council`
- `central_asia_soviet_collapse_military_border_authority`
- `central_asia_soviet_collapse_khwarazm_and_older_names`
- `central_asia_soviet_collapse_khwarazm_restoration_debate`
- `blr_soviet_collapse_guide_companies`
- `blr_soviet_collapse_the_league_depot_at_minsk`

Two immediate child links created by the compact move were also corrected:

- `ukr_soviet_collapse_grain_census_of_everyone`
- `ukr_soviet_collapse_no_one_leaves_the_bread_line`
- `blr_soviet_collapse_the_forest_state_rumor`

This keeps the Ukraine high-chaos bread-state chain and the Belarus League depot/forest-rumor chain vertically ordered instead of creating a new same-row pathline.

## Validation

- Audited same-row link check: `same_row_failures 0`
- Per-tree duplicate coordinate check:
	- `soviet_collapse_ukraine_focus_tree`: 83 focuses, `duplicate_coords 0`
	- `soviet_collapse_internal_republic_focus_tree`: 62 focuses, `duplicate_coords 0`
	- `soviet_collapse_central_asia_focus_tree`: 45 focuses, `duplicate_coords 0`
	- `soviet_collapse_belarus_focus_tree`: 53 focuses, `duplicate_coords 0`
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt`
- brace-depth check for `common/national_focus/005_soviet_collapse_republics.txt`: `brace_level 0`
- `git status --short -- gfx/flags interface/flags`: no output

## Remaining work

This fixes the concrete same-row blocker set from the fresh audit. It does not complete the full Soviet Collapse focus-tree rework. Remaining work still includes reward-depth cleanup, route-specific decision/mechanic links for low-link trees, deeper political/industry/expansion branches for compact trees, and stronger high-chaos conquest/coring behavior across weak chaos actors.
