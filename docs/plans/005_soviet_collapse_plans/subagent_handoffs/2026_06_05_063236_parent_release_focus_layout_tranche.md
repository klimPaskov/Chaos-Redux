# Event005 Parent Release And Focus Layout Tranche

Timestamp: 2026-06-05 06:32 UTC

## Scope

Parent implementation tranche after the focus audit handoff `2026_06_05_061350_event005_focus_tree_audit_handoff.md`.

Touched gameplay files:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

No flags or visual assets were touched.

## Release Pacing

Tightened dynamic follow-on release helpers so higher chaos still increases wave size, but does not by itself permit extra non-base/internal/pressure-successor waves.

The follow-on helper now explicitly zeros pressure successor, generic follow-on, and internal follow-on counts when neither `has_soviet_collapse_nonbase_republic_release_pressure` nor `has_soviet_collapse_severe_component_release_pressure` is true. This keeps base first-year republic backlog behavior separate from later non-base/internal progression.

## Focus Layout

Ukraine:

- Fixed the duplicate coordinate created between `ukr_soviet_collapse_foreign_advisers_in_plain_coats` and `ukr_soviet_collapse_protectorate_debate`.
- Cleaned Ukraine coordinates until the parser audit reported:
  - 83 focuses
  - 99 prerequisite edges
  - 0 pathlines running through another focus
  - 0 same-row adjacent pairs
  - 0 duplicate coordinates

Belarus:

- Moved four rail/diplomacy nodes to clear one blocking rail focus and three same-row adjacent pairs.
- Cleaned Belarus coordinates until the parser audit reported:
  - 53 focuses
  - 0 pathlines running through another focus
  - 0 same-row adjacent pairs
  - 0 duplicate coordinates

## Remaining Layout Debt

The broad focus-tree goal is not complete. Current audit still reports remaining pathline or adjacency issues in:

- `soviet_collapse_kazakhstan_focus_tree`: 38 through-lines, 5 same-row adjacent pairs.
- `soviet_collapse_moldova_focus_tree`: 8 through-lines, 2 same-row adjacent pairs.
- `soviet_collapse_baltic_focus_tree`: 8 through-lines.
- `soviet_collapse_caucasus_focus_tree`: 8 through-lines.
- `soviet_collapse_central_asia_focus_tree`: 5 through-lines, 3 same-row adjacent pairs.
- `soviet_collapse_internal_republic_focus_tree`: 4 through-lines, 1 same-row adjacent pair.
- `soviet_collapse_breakaway_focus_tree`: 3 through-lines.
- Several custom/factory successor trees still have 1-6 through-lines each, especially `UWD`, `NLC`, and `BAC`.

Kazakhstan needs a manual branch re-layout rather than accepting the generated coordinate candidate, because the generated candidate reduced collisions but moved several route anchors into odd lanes.

## Validation

- Brace balance passed with depth 0 and no early closes for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `rg -n "<=|>="` returned no hits in the same six files.
- `git diff --check` passed for the two touched gameplay files.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `hoi4-decisions-missions`
