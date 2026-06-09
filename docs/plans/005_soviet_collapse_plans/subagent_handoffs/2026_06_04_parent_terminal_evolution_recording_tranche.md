# Event 005 parent terminal evolution recording tranche

Date: 2026-06-04

Scope: parent implementation pass for Soviet Collapse terminal release and triggerable scenario evolution recording. Flag assets were explicitly out of scope and were not opened or edited.

## Changed files

- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Gameplay change

Terminal release now records the Republic Secession Progression milestones after the forced release and war setup, before terminal/scenario cleanup clears the force flags.

Affected helpers:

- `soviet_collapse_apply_terminal_collapse`
- `soviet_collapse_force_triggerable_scenario_terminal_release`

Both helpers now call:

- `soviet_collapse_record_secession_evolution_milestones`

This keeps Union Unmade and the standalone triggerable Soviet Collapse scenario aligned with the event-log evolution layer after the map has actually been ruptured into breakaways.

## Validation

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt`
- `rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt`
- brace-depth check for `common/scripted_effects/005_soviet_collapse_effects.txt`: `brace_level 0`
- `git status --short -- gfx/flags interface/flags`: no output

## Remaining work

This is a narrow wiring fix, not completion of the full Soviet Collapse goal. Remaining priorities include the focus-audit blockers, focus reward depth, decision/mechanic links for low-link trees, and live verification of every ordinary and high-chaos release candidate.
