# Event005 Parent Handoff: FTH Explicit Reward Cleanup Tranche

Date: 2026-06-05

## Scope

Parent-side implementation tranche for the Free Territory of Huliaipole focus tree. The goal was to reduce the focus-reward spam feel by replacing repeated broad helper packages in the FTH opening and mid-tree with explicit black-banner mechanics.

## Changed Files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

## Focuses Updated

- `FTH_first_guard`
- `FTH_stores`
- `FTH_legitimacy`
- `FTH_rival`
- `FTH_doctrine`
- `FTH_economy`
- `FTH_league`
- `FTH_foreign`
- `FTH_inner_faction`
- `FTH_special_arm`
- `FTH_supply`
- `FTH_civil_rule`
- `FTH_propaganda`
- `FTH_settlement`

## Behavior Change

These focuses no longer rely on the same broad custom-splinter identity helper packets for their main rewards. They now grant direct, focus-specific effects:

- military-depth, depot-depth, legal-depth, and League-depth progression
- militia manpower, infantry/support/artillery equipment, command power, army XP, and mobile columns
- explicit depot control, recognition, institution strength, resilience, local authority, liaison, and League support variable changes
- map effects such as infrastructure, factories, rail linkage, and supply-node construction
- neighbor conflict pressure, expansion claims, and Soviet crisis pressure where the focus text promises active escalation
- League deployment decision unlocks only on relevant League/civil settlement nodes

This keeps the FTH tree powerful and aggressive without making the opening route feel like every focus grants the same repeated idea/helper bundle.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt` passed.
- Confirmed no direct `add_ideas` or `remove_ideas` remain in the four Event005 focus files.
- Confirmed the removed nonexistent helper name `soviet_collapse_advance_foreign_focus_depth` is not present.
- Confirmed the FTH tree slice is brace-balanced.
- Confirmed no `gfx/flags` files were touched.

## Remaining Work

This is not a full focus-tree completion claim. Remaining focus-tree work includes:

- later FTH focuses still contain several generic helper packets
- other chaos trees still need explicit concept-driven rewards instead of generic helper stacks
- all Event005 trees still need a final branch-depth/pathline audit after more parent-side patches
- the fresh `chaosx_focus_tree_auditor` run launched on 2026-06-05 is still pending at the time of this handoff

No flags, flag sprites, Event006 files, or binary assets were touched.
