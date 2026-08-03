# Event 006 generic focus isolated-command repair

Date: 2026-08-03.

## Scope

This bounded repair uses the current repository and current `hoi4.focus_inspect` output. The obsolete pasted flag-log was not used.

## Changed files

- `common/national_focus/006_independence_wave_focus.txt`

## Changed focus and behavior

`independence_wave_preserve_independent_command` now has the same visible prerequisite as its mutually exclusive `independence_wave_standardize_with_league` alternative: `independence_wave_adopt_military_archetype_program`.

Before the repair, the focus was available at the military branch row without a visible parent and the focus inspector reported it as isolated. After the repair, it is part of the military-archetype branch and still preserves the existing mutual exclusion, completion reward, AI weighting, and downstream defense capstone contract.

The focus remains at its existing coordinate `x = 49`, `y = 8` so it does not collide with adjacent military choices. The resulting parent connector spans eight columns and does not cross another focus. The inspector no longer reports `FOCUS_ISOLATED` for Event 006.

## Validation

Ran `hoi4.focus_inspect` for `independence_wave_focus_tree` after the patch. The tree resolves 184 focuses and 193 connectors with zero crossing or node-intersection diagnostics. The only Event 006 layout note is the intentional long connector from the shared military-archetype parent to this far-right mutually exclusive choice. The remaining reported icon errors and one localisation warning belong to vanilla `common/continuous_focus/generic.txt`, not the Event 006 tree.

No gameplay runtime, live focus rendering, or save/load validation was performed.

## Remaining risk

The vanilla continuous-focus source still has the pre-existing missing icon/localisation diagnostics reported by the MCP inventory. They were not changed because they are outside Event 006 ownership.
