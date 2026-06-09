# Event005 Parent PRA Railway Identity Tranche

Date: 2026-06-01

## Scope

Parent patch for the Pale Railway Authority focus/decision surface after the full focus-tree audit identified `PRA_soviet_collapse_focus_tree` as a shallow special-chaos tree with too many stockpile/building rewards and too little rail-state gameplay.

No flag sprites, flag configuration, `gfx/flags`, `interface/flags`, `gfx`, or `interface` files were edited.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Implementation

- Added `soviet_collapse_update_pra_authority_idea`.
  - Keeps PRA on one visible authority spirit at a time instead of stacking multiple PRA authority ideas.
  - Updates between timetable board, railway guard, corridor toll authority, and moving-state authority based on route flags.
- Added `soviet_collapse_build_pra_corridor_network`.
  - Repairs infrastructure and railways across controlled core station territory.
  - Adds a supply hub and raises rolling-stock/depot control.
- Added `soviet_collapse_create_pra_rail_guard_column_template` and `soviet_collapse_spawn_pra_rail_guard_columns`.
  - Creates a recruitable `Railway Guard Column` template.
  - Spawns 1-4 columns dynamically from PRA rail authority, rolling stock, armored-train route, and chaos tier.
  - Grants matching manpower and equipment through variables instead of flat one-off stockpiles.
- Rewired PRA focuses away from several flat stockpile rewards into the new helpers.
- Made `pra_declare_the_moving_state` hidden until a focus actually unlocks it.
- Made PRA decisions reinforce the same rail guard/corridor systems instead of only adding separate rewards.

## Validation

- Brace balance checked for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
- No unsupported `<=` or `>=` operators found in touched gameplay/localisation files.
- `git diff --check` passed for touched files.
- `git diff --name-only -- gfx/flags interface/flags` returned no touched flag paths.
- Scoped focus file still has no direct `add_ideas` or `add_timed_idea`.
- New tooltip keys are present:
  - `soviet_collapse_build_pra_corridor_network_tt`
  - `pra_mobilize_station_guard_tt`
  - `pra_drive_the_junction_columns_tt`
  - `pra_declare_the_moving_state_tt`

## Remaining Risks

- This is one special-chaos tranche only. The full focus-tree audit still lists ancient restorations, `TSC/RMC/DSC/NRF/ICD`, `OGB`, Ukraine, Belarus, Kazakhstan, shared regional trees, and many 47-focus splinter templates as incomplete.
- The broader Soviet Collapse goal remains incomplete until release logic, evolution details, selected-target decision visibility, terminal collapse coverage, and the remaining focus tranches are audited and patched.
