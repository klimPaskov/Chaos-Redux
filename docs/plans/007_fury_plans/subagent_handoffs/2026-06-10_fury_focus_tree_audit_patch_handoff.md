# Event 007 Fury focus-tree audit patch handoff

## Scope

Audited and patched narrow focus-tree issues in `common/national_focus/007_fury_focus_tree.txt` only.

## Changed files

- `common/national_focus/007_fury_focus_tree.txt`
- `docs/plans/007_fury_plans/subagent_handoffs/2026-06-10_fury_focus_tree_audit_patch_handoff.md`

## Changed focus ids

- `fury_cut_the_rail_before_the_war`
- `fury_rail_and_registry`
- `fury_occupation_as_recruitment`
- `fury_all_roads_are_front_roads`
- `fury_second_war_table`
- `fury_rival_column`
- `fury_hardened_doctrine`
- `fury_all_borders`
- `fury_the_last_neighbor_has_fallen`

## Behavior before and after

- Before: `fury_cut_the_rail_before_the_war`, `fury_rail_and_registry`, and `fury_all_roads_are_front_roads` referenced unregistered `GFX_goal_generic_railway`.
- After: those focuses use registered vanilla `GFX_goal_generic_construct_infrastructure`.
- Before: `fury_occupation_as_recruitment` referenced unregistered `GFX_goal_generic_manpower`.
- After: it uses registered vanilla `GFX_focus_generic_manpower`.
- Before: cooperation and rivalry gateway focuses only checked global Evolution II unlock state, so triggerable-scenario pact/hostile actors could receive scenario route state without the route gateway becoming available.
- After: `fury_second_war_table` and `fury_rival_column` accept global Evolution II, country-applied Evolution II, or the matching triggerable scenario type flag when another Fury actor actually exists.
- Before: Evolution I and Evolution III gateway focuses only checked global unlock state, so scenario-created evolved actors could be blocked from their evolved branches or could re-run a gateway reward.
- After: `fury_hardened_doctrine` and `fury_all_borders` also accept country-applied evolution state and bypass when that evolution is already applied.
- Before: `fury_the_last_neighbor_has_fallen` required `fury_core_by_administration`, which locked the world-end/no-neighbor route after the mutually exclusive `fury_core_by_march`.
- After: it accepts either `fury_core_by_administration` or `fury_core_by_march` while still requiring `fury_the_next_neighbor`.

## Localisation keys and icon ids changed

- Localisation keys changed: none.
- Icon ids changed:
  - `GFX_goal_generic_railway` to `GFX_goal_generic_construct_infrastructure`
  - `GFX_goal_generic_manpower` to `GFX_focus_generic_manpower`

## Meaningful validation

- Recounted focus blocks: 52 focus blocks.
- Checked focus references: no missing referenced focus ids.
- Checked focus localisation in `localisation/english/007_random_expansion_l_english.yml`: every focus id has title and `_desc`.
- Checked focus icons against mod and vanilla `.gfx`: no unresolved icon ids after patch.
- Checked duplicate focus coordinates: none found.
- Checked `ai_will_do` presence: every focus has an `ai_will_do` block.
- Checked braces in the focus file: balanced.
- Checked Fury focus, localisation, icon, helper, trigger, and constants files for unsupported `<=` or `>=`: none found.

## Skipped validation

- Did not run the game or a full HOI4 parser. This was a static focus-tree audit and the repository has broad unrelated Fury/event changes in progress.

## Remaining route risks

- The Internal Fury branch from the focus spec is represented mostly through opening, army, and occupation route mechanics rather than as a named War Directorate / Civil Mobilization / Compliance Administration fork.
- The tree has no broad bypass coverage beyond the evolved gateway fixes made here.
- Many rewards are variable/flag/helper driven and need live scenario validation to confirm AI pacing, especially world-end eligibility and no-neighbor timing.
