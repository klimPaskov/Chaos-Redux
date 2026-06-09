# Event 005 Parent Focus Helper And Layout Tranche 3

Date: 2026-06-04
Owner: parent Codex agent

## Scope

This tranche followed the current focus-audit handoff at:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_focus_tree_current_worktree_audit.md`

No flag files were edited. The latest user correction is to leave flags alone.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_parent_focus_helper_layout_tranche_3.md`

## Helper Cleanup

Removed the hidden high-chaos escalation call from ordinary republic focus helpers:

- `soviet_collapse_apply_focus_legal_recognition`
- `soviet_collapse_apply_focus_socialist_sovereignty`
- `soviet_collapse_apply_focus_military_consolidation`
- `soviet_collapse_apply_focus_depot_and_supply_control`
- `soviet_collapse_apply_focus_league_preparation`
- `soviet_collapse_apply_focus_foreign_channel`

Then removed the now-unused `soviet_collapse_apply_high_chaos_focus_escalation_payload` wrapper.

Dedicated chaos route helpers still call `soviet_collapse_apply_high_chaos_focus_payload` directly:

- `soviet_collapse_apply_focus_chaos_legitimacy_plan`
- `soviet_collapse_apply_focus_chaos_assault_plan`
- `soviet_collapse_apply_focus_chaos_supply_plan`
- `soviet_collapse_apply_focus_chaos_league_plan`
- `soviet_collapse_apply_focus_high_chaos_identity`

This keeps special chaos-country aggression and identity payloads explicit while stopping ordinary legal, military, depot, league, and foreign focuses from carrying high-chaos payloads through a generic wrapper.

## Layout Cleanup

Ukraine:

- Removed the `ukr_soviet_collapse_foreign_courts_notice_kyiv` prerequisite from `ukr_soviet_collapse_army_supremacy`, so the military route lock no longer draws a foreign-diplomacy line into the commander fork.
- Moved `ukr_soviet_collapse_army_supremacy` to `x = 8`, `y = 8` so it pairs cleanly with `ukr_soviet_collapse_mixed_emergency_cabinet`.
- Moved `ukr_soviet_collapse_free_soil_compromise` to `x = 17`, `y = 6`, near its democratic/black-banner route split rather than far across the tree.
- Moved `ukr_soviet_collapse_black_sea_port_ledgers` to `x = 24`, `y = 5`, reducing the long line from `ukr_soviet_collapse_black_sea_defense_staff`.

Belarus:

- Removed the `blr_soviet_collapse_forest_defense_staff` prerequisite from `blr_soviet_collapse_council_bargains_with_forests`.
- Removed the `blr_soviet_collapse_council_bargains_with_forests` prerequisite from `blr_soviet_collapse_guide_companies`.
- Removed the `blr_soviet_collapse_national_council_of_minsk` prerequisite from `blr_soviet_collapse_swamp_roads_closed`.
- Removed the distant `blr_soviet_collapse_swamp_roads_closed` prerequisite from `blr_soviet_collapse_armored_train_workshops`.
- Moved `blr_soviet_collapse_the_forest_state_rumor` to `x = 24`, `y = 14`.

The post-patch coordinate audit found no Ukraine long edges at Manhattan distance `>= 14`. Belarus is reduced to three borderline long edges at distance `14`; the severe `17-26` distance crossings from the audit were removed.

## Validation

- Brace balance:
  - `common/national_focus/005_soviet_collapse_republics.txt`: final depth `0`, min depth `0`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: final depth `0`, min depth `0`
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/scripted_effects/005_soviet_collapse_effects.txt` passed.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/scripted_effects/005_soviet_collapse_effects.txt` found no unsupported operators.
- `git status --short -- gfx/flags interface/flags` produced no output.
- `rg -n "soviet_collapse_apply_high_chaos_focus_escalation_payload" common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_*.txt` produced no output.

## Remaining Work

This is not a full focus-tree completion claim. Remaining broad work includes:

- deeper bespoke route rewrites across all republic and custom successor trees
- remaining Belarus borderline long edges and other non-audited rendered pathline risks
- custom successor idea/authority lifecycle cleanup, especially repeated PRA authority update calls
- further chaos-country per-tag expansion and decision integration
- final focus audit after a larger rewrite tranche

Skills used: `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`.
