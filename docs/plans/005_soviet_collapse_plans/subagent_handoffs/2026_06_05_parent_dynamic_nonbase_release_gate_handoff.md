# Event005 Parent Handoff: Dynamic Non-Base Release Gate

## Scope

Parent-side release pacing fix for the active Soviet Collapse crisis. This tranche does not touch flag sprites, terminal Union Unmade force-release behavior, or triggerable scenario force-release behavior.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`

## Behavior Changed

- `has_soviet_collapse_dynamic_follow_on_release_pressure` now requires the non-base release tier and the existing non-base pressure model, plus at least one runtime pressure signal:
  - terminal collapse
  - triggerable scenario chaos include
  - real regional cascade pressure
  - war release pressure
  - failure release pressure
  - elapsed crisis months meeting `constant:soviet_collapse_release_mtth.low_threat_follow_on_month_gate`
  - accumulated `soviet_collapse_progressive_release_pressure` meeting `constant:soviet_collapse_release_mtth.sustained_pressure_roll_gate`
  - release urgency meeting `constant:soviet_collapse_threat_guard.real_release_pressure_urgency_gate`
- `has_soviet_collapse_pressure_successor_follow_on_release_pressure` now has the same active-crisis runtime guard, but uses `constant:soviet_collapse_release_mtth.sustained_pressure_mature_gate` for the pressure variable before special pressure successors can enter normal progressive release.
- Terminal collapse, forced chaos-successor spawning, and triggerable scenario chaos mode remain exempt from the active-crisis delay guard.

## Why

The active crisis path was already split into base republics, internal republics, and pressure successors, but the non-base gates could still open as soon as the chaos tier and a broad pressure condition existed. The new guard makes the active campaign path depend on actual crisis progression variables instead of chaos tier alone.

## Validation

- `git diff --check -- common/scripted_triggers/005_soviet_collapse_triggers.txt` passed.
- Brace-balance check for `common/scripted_triggers/005_soviet_collapse_triggers.txt` returned `0`.
- Search for unsupported `<=` / `>=` in the touched trigger/effect/constant files returned no matches.
- Confirmed `chaosx.nr5.130` through `chaosx.nr5.137` progressive-release report events already have `minor_flavor = yes`.

## Remaining Work

- Review the focus audit subagent handoff when it completes.
- Continue focus-tree cleanup: branch structure, pathline layout, reward depth, and removal of helper-mediated idea spam.
- Audit active release pacing in-game once the next focus/release tranche is ready; static checks cannot prove live pacing across all chaos tiers.
