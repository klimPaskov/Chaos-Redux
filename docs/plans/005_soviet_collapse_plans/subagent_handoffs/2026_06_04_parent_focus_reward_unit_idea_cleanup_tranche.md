# Event005 Parent Focus Reward Unit And Idea Cleanup Tranche

## Scope

Parent-side tranche for the active Soviet Collapse focus-tree rework goal.

Touched files:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

No flag files, `.tga` files, or `gfx/flags` files were touched.

## Evidence

Parent audit parsed the four Event005 focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`: 501 focuses, 170 tiny reward-like focuses.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 1005 focuses, 495 tiny reward-like focuses.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: 128 focuses, 25 tiny reward-like focuses.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: 64 focuses, 14 tiny reward-like focuses.

The focus files had no literal `add_ideas` focus rewards, but helper-level audit found one repeated idea handling offender:

- `soviet_collapse_update_pra_authority_idea` repeated the same four PRA authority idea add/remove checks through each route branch.

The same focus audit also showed that direct unit/template rewards are rare in focus files, while the shared chaos signature-force helper was used by many chaos-splinter focuses and decisions.

## Changes

### Shared Chaos Signature Forces

`soviet_collapse_apply_custom_splinter_mobilize_signature_forces` now deploys an actual mobile republican column by calling the existing `soviet_collapse_spawn_focus_mobile_column` helper inside a hidden effect.

Player-facing text is handled through the new tooltip key:

- `soviet_collapse_custom_splinter_signature_mobile_column_tt`

This turns a repeated manpower/equipment reward pattern into a visible map effect without adding a new template system or new idea.

### PRA Authority Idea Cleanup

Added:

- `soviet_collapse_clear_pra_authority_ideas`

`soviet_collapse_update_pra_authority_idea` now clears the old PRA authority idea set once, then applies the single current authority idea for the active route:

- `pra_timetable_sovereignty_board`
- `pra_railway_guard`
- `pra_corridor_toll_authority`
- `pra_moving_state_authority`

This removes repeated helper-level idea churn while preserving the one-active-authority-idea design.

### BSC/TNC/ALA Decision And War-Plan Wiring

The focus-tree audit identified BSC, TNC, and ALA as three template-shaped custom splinter trees with weak focus-to-decision signalling.

Patched:

- `BSC_special_arm` now shows `unlock_decision_tooltip = bsc_mobilize_signature_forces`.
- `BSC_extreme_gate` now shows `unlock_decision_tooltip = bsc_push_extreme_route`.
- `TNC_special_arm` now shows `unlock_decision_tooltip = tnc_mobilize_signature_forces`.
- `TNC_extreme_gate` now shows `unlock_decision_tooltip = tnc_push_extreme_route`.
- `ALA_special_arm` now shows `unlock_decision_tooltip = ala_mobilize_signature_forces`.
- `ALA_extreme_gate` now shows `unlock_decision_tooltip = ala_push_extreme_route`.
- `ALA_war_plan` now calls `soviet_collapse_apply_custom_splinter_war_plan_bonus`, matching the existing BSC/TNC war-plan payoff path and converting the focus into a real war-plan/assault/claim reward instead of only a generic assault helper.

This does not fully redesign those three trees, but it connects their military and high-chaos routes to actual decisions and a stronger expansion payoff.

## Validation

Ran:

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_l_english.yml docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_parent_focus_reward_unit_idea_cleanup_tranche.md`
- brace balance check on both touched files
- localisation BOM check for `localisation/english/005_soviet_collapse_l_english.yml`
- helper-level duplicate idea add/remove audit for `common/scripted_effects/005_soviet_collapse_effects.txt`
- duplicate ID scan for `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- flag diff guard: `git diff --name-only | rg '(^|/)gfx/flags/|\\.tga$|(^|/)flags/'`

Results:

- `git diff --check` passed.
- `common/scripted_effects/005_soviet_collapse_effects.txt` brace balance: 0.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` brace balance: 0 and UTF-8 BOM present.
- `localisation/english/005_soviet_collapse_l_english.yml` brace balance: 0 and UTF-8 BOM present.
- Duplicate idea add/remove top-level effects: 0 after the cleanup.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` duplicate ID scan: 0 duplicates.
- Flag diff guard returned no paths.

## Remaining Issues

This tranche does not complete the focus-tree rework. The parent audit still shows hundreds of tiny reward-like focuses and insufficient route-level payoff across the four focus files. The spawned focus-tree auditor should provide the ranked layout/depth blocker list for the next implementation tranche.
