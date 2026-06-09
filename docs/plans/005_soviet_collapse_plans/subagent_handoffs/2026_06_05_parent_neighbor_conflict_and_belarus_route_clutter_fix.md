# Parent Tranche: Neighbor Conflict and Belarus Route Clutter Fix

## Scope

Continued the Event005 wrap-up toward two requested outcomes:

- Breakaway republics should fight each other, with chaos breakaways especially aggressive.
- Focus pathlines should stay clean and avoid unnecessary mutual-exclusion clutter.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

## Scripted Effects

Cleaned the two neighbor-conflict helper blocks:

- `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`
- `soviet_collapse_apply_breakaway_neighbor_conflict_plan`

The previous blocks were brace-balanced but the `declare_war_on` sections were visually malformed and easy to misread. They now use a clear pattern:

- add claims on neighboring breakaway-controlled states
- add conquer and antagonize AI strategies
- declare war immediately in max-chaos / high-chaos / terminal / scenario paths
- otherwise create an annex wargoal if one is missing

This preserves the existing design while making the war path safer and easier to maintain.

## Focus Layout

Removed redundant visible `mutually_exclusive` lines from the four Belarus route focuses:

- `blr_soviet_collapse_national_council_of_minsk`
- `blr_soviet_collapse_socialist_autonomy_without_moscow`
- `blr_soviet_collapse_military_transit_directorate`
- `blr_soviet_collapse_foreign_corridor_administration`

The actual route lock is still enforced by `available = { hidden_trigger = { NOT = { has_soviet_collapse_belarus_state_route_completed = yes } } }`, and the route-completed scripted trigger checks all four completed focuses. Route flags and downstream branch prerequisites were not changed.

## Validation

- Brace balance passed for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
- `git diff --check` passed for the touched files.
- A focused `rg` scan confirmed the four Belarus route focuses no longer contain visible `mutually_exclusive` blocks.

## Remaining Risks

- This does not solve every focus pathline issue in Ukraine, Kazakhstan, or other trees.
- This does not complete the full focus reward-depth rewrite.
- The broader Event005 goal remains active and incomplete.
