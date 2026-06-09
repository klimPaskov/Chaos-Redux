# Event 005 parent terminal release and focus layout sweep

## Scope

Parent follow-up after the focus-tree auditor tranche. This sweep did not touch any flag assets.

## Files changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` via subagent handoff `2026_06_04_event005_focus_tree_auditor_layout_depth_handoff.md`

## Implemented

- Added a terminal breakaway finalization helper that sweeps all existing Soviet Collapse breakaway countries after terminal collapse and triggerable terminal release.
- The helper sets missing breakaway setup flags, loads the event-created focus tree, initializes republic component variables, joins the anti-Soviet terminal war, and applies neighbor conflict planning.
- Added a guard so triggerable scenario initial forces are applied once per breakaway country.
- Cleared the remaining audited one-column same-row focus spacing risks in the generic breakaway and Kazakhstan focus trees.

## Validation

- `one_unit_same_row_risks`: `0` across the checked Event005 focus files:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Brace scan:
  - `common/national_focus/005_soviet_collapse_republics.txt`: `final_depth=0`, `min_depth=0`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `final_depth=0`, `min_depth=0`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: `final_depth=0`, `min_depth=0`
- Unsupported operators: no `<=` or `>=` matches in touched focus/effect files.
- Direct focus idea operations: no `add_ideas`, `remove_ideas`, or `swap_ideas` matches in `common/national_focus/005_soviet_collapse*.txt`.
- `git diff --check` passed for the touched Event005 files and focus auditor handoff.
- Flag asset diff scan returned no changed flag or `.tga` paths.

## Remaining blockers

- The broader focus-tree design goal is not complete. The latest auditor still identifies shallow route families, especially several custom splinter and restoration trees that need more bespoke mechanics and route endpoints.
- Direct focus files no longer contain idea operations, but `common/scripted_effects/005_soviet_collapse_effects.txt` still contains many idea operations through shared reward and lifecycle helpers. Those must be reviewed helper-by-helper before claiming that idea spam is fixed.
- Terminal release and triggerable scenario behavior has been made more exhaustive in script, but it still needs a live game verification pass before completion can be claimed.
- Evolution details and spreadsheet wording alignment still need a dedicated comparison pass.
- No flag work remains in this tranche by user instruction.
