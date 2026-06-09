# Parent Handoff: Focus Reward Idea Helper Cleanup

Date: 2026-06-05

Scope:

- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Changes

- Removed focus-driven `add_ideas` behavior from `soviet_collapse_update_pra_authority_idea`.
  - PRA setup still grants the single starting `pra_timetable_sovereignty_board` identity spirit.
  - PRA focus calls now deepen rail authority, rolling stock, depot control, liaison reach, command power, war support, and related rail mechanics without adding or replacing national spirits as focus rewards.
- Reworked `soviet_collapse_update_dsc_dead_army_idea`.
  - The helper no longer removes old DSC ideas and adds `dsc_dead_army_politics` from focus completion.
  - The focus path now hardens the dead-army mechanic through roll-call legitimacy, revenant mobilization, local authority pressure, independence resilience, manpower, war support, front-road claims, and controlled-state cores.
- Preserved starting identity spirits from release setup where they represent the initial country package rather than focus rewards.

## Audit Result

Before this tranche, 23 focus reward helper call sites reached scripted effects with idea operations.

After this tranche, 18 focus reward helper call sites still reach idea operations, and the remaining call sites are cleanup/removal paths:

- `soviet_collapse_add_republic_focus_recovery_progress`
- `soviet_collapse_clear_focus_starting_tension_ideas`

No focus reward helper call sites now add PRA or DSC national spirits.

## Validation

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_parent_dynamic_nonbase_release_gate_handoff.md`
- Brace balance check:
  - `common/scripted_effects/005_soviet_collapse_effects.txt brace_balance 0`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt brace_balance 0`
- `rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt`
  - no matches

## Remaining Work

- The broader focus-tree goal remains incomplete.
- `PRA_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, and other compact chaos trees still need deeper branch structure and more country-specific route mechanics.
- Layout/pathline risks from the focus-auditor report still need a parent patch pass.
- Generic reward-helper hotspots remain and should be replaced or wrapped with route-specific payloads in future tranches.
