# Parent Tranche: Custom Splinter Tooltip Cleanup And Death-State Aggression

Date: 2026-06-01

## Scope

This parent tranche targeted two current Event005 focus-tree blockers:

- custom-splinter focus reward spam caused by visible tag-conditional helper payloads
- weak high-chaos aggression payoff for Red Martyrs and Iron Commissariat compared with the Dead Soldiers' Congress

Hard constraint followed: no flag files, flag sprites, flag interface entries, or flag orientation logic were edited.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Gameplay Changes

The following shared custom-splinter focus helpers now show one concise route tooltip and run their existing payload in `hidden_effect`:

- `soviet_collapse_apply_custom_splinter_first_guard_identity`
- `soviet_collapse_apply_custom_splinter_stores_identity`
- `soviet_collapse_apply_custom_splinter_legitimacy_identity`
- `soviet_collapse_apply_custom_splinter_rival_identity`
- `soviet_collapse_apply_custom_splinter_doctrine_identity`
- `soviet_collapse_apply_custom_splinter_economy_identity`
- `soviet_collapse_apply_custom_splinter_league_identity`
- `soviet_collapse_apply_custom_splinter_foreign_identity`
- `soviet_collapse_apply_custom_splinter_inner_faction_identity`
- `soviet_collapse_apply_custom_splinter_special_arm_identity`
- `soviet_collapse_apply_custom_splinter_supply_identity`
- `soviet_collapse_apply_custom_splinter_enemy_front_identity`
- `soviet_collapse_apply_custom_splinter_civil_rule_identity`
- `soviet_collapse_apply_custom_splinter_propaganda_identity`
- `soviet_collapse_apply_custom_splinter_settlement_identity`
- `soviet_collapse_apply_custom_splinter_industry_plan_identity`
- `soviet_collapse_apply_custom_splinter_hidden_doctrine_identity`
- `soviet_collapse_apply_custom_splinter_extreme_gate_identity`

The original bodies were preserved as matching `_payload` helpers. Existing focus call sites keep calling the public helper names, so route behavior remains wired while focus reward UI stops listing every irrelevant tag-conditional branch.

`soviet_collapse_apply_high_chaos_focus_identity_payload` now gives one-time high-chaos war packages to:

- `soviet_collapse_red_martyrs_successor`
- `soviet_collapse_iron_commissariat_successor`

Each package grants route variables, emergency manpower, assault columns, expansion claims, and neighbor-conflict escalation. The payload also calls `soviet_collapse_apply_breakaway_neighbor_conflict_plan` for high-chaos successors so identity route focuses are more likely to create actual inter-breakaway fighting.

## Localisation

Added concise focus-effect tooltip keys for all custom-splinter identity wrappers. Updated `soviet_collapse_apply_focus_high_chaos_identity_tt` to mention neighboring breakaway war plans.

## Validation

Parent validation run after the patch:

- brace balance on `common/scripted_effects/005_soviet_collapse_effects.txt`: passed with balance 0
- unsupported `<=` / `>=` scan on touched gameplay and localisation files: no hits
- `git diff --check` on touched gameplay and localisation files: passed
- localisation BOM check for `005_soviet_collapse_l_english.yml`: `efbbbf`
- first-order visible duplicate idea scan for Event005 focus rewards after wrappers: 0
- payload helper scan confirmed no focus file calls `_identity_payload` directly

## Remaining Gaps

This does not complete the full focus-tree rework. Remaining parent work includes:

- route-depth implementation for Ukraine, Belarus, Kazakhstan, OGB, ancient restorations, and factory states
- direct CFR/MFR project mechanics and route AI
- broader layout/pathline fixes after route payoff edits
- full release/scenario verification for all ordinary and chaos splinters
- final decision and mission audit for inter-breakaway war tools
