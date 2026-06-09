# Parent Handoff: Ukraine And Belarus Route Lock Tranche

## Scope

This tranche fixes the audit finding that Ukraine and Belarus route-choice focuses looked like route locks but could still be sequenced through hidden or incomplete logic.

The patch avoids a full pairwise mutual-exclusion mesh because that would draw long red lines across the route rows and recreate the pathline clutter the user called out. Instead, it uses:

- adjacent visible `mutually_exclusive` links for readable route-row signaling
- centralized hidden route-completed triggers that enforce one completed route across the whole route family

No flag files were touched.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

## Gameplay Behavior

Added route-completed triggers:

- `has_soviet_collapse_ukraine_state_route_completed`
- `has_soviet_collapse_belarus_state_route_completed`

Ukraine route behavior:

- `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_officers_above_parties` now have adjacent visible route-lock links.
- All four early route focuses now use the Ukraine route-completed trigger, so completing any route blocks the others.
- `ukr_soviet_collapse_protectorate_debate` also uses the Ukraine route-completed trigger, but does not draw a long mutual-exclusion line from the far foreign branch back to the early political row.

Belarus route behavior:

- `blr_soviet_collapse_national_council_of_minsk`, `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, and `blr_soviet_collapse_foreign_corridor_administration` now have adjacent visible route-lock links.
- All four Belarus route focuses use the Belarus route-completed trigger, so completing any route blocks the others.

## Validation

- `git diff --check -- common/scripted_triggers/005_soviet_collapse_triggers.txt common/national_focus/005_soviet_collapse_republics.txt`
- Brace balance check on both touched files.
- `rg -n "<=|>="` on both touched files.
- Mutual-exclusion reciprocity parser:
  - `0` missing targets
  - `0` non-reciprocal links
- Republic focus-tree coordinate parser:
  - `0` in-tree coordinate overlaps

## Remaining Gaps

- This improves route behavior and visual route signaling, but it is not the full Ukraine/Belarus tree rework. Their political, industrial, military, diplomacy, and expansion branches still need broader depth passes.
- The larger Event005 goal remains incomplete: many focus trees still need bespoke branch identities, stronger chaos-country expansion mechanics, and less helper-heavy reward design.
