# Parent Handoff: Dynamic Release Pressure And Focus Cleanup Visibility

## Scope

This tranche keeps active Soviet Collapse releases gradual while giving high-chaos pressure successors enough burst budget to appear when the existing dynamic pressure gates are satisfied. It also hides focus helper calls that can expose internal idea-removal cleanup in focus reward previews.

## Files Changed

- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

## Gameplay Behavior

- High-chaos pressure-successor follow-on releases now have larger tiered budgets:
  - tier 3: 2
  - tier 4: 6
  - tier 5: 12
  - pressure successor cap: 12
- These values still run through the existing dynamic pressure gates in `has_soviet_collapse_pressure_successor_follow_on_release_pressure` and the active follow-on backlog helper. Calm-world first-year releases remain the first-wave/base republic lane.
- Focus completion rewards that settle starting tensions now keep the player-facing custom tooltip while hiding the internal `soviet_collapse_clear_focus_starting_tension_ideas` cleanup.
- PRA authority recalculation helper calls that only update internal variables are now hidden in the relevant focus rewards.

## Validation

- `git diff --check -- common/script_constants/005_soviet_collapse_constants.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`
- Brace balance check for the three touched files.
- `rg -n "<=|>="` on the three touched files.
- Parser check found zero visible calls to:
  - `soviet_collapse_clear_focus_starting_tension_ideas`
  - `soviet_collapse_update_pra_authority_idea`
  - `soviet_collapse_update_dsc_dead_army_idea`

## Remaining Gaps

- This does not complete the broader focus-tree quality goal. A focus audit subagent is still responsible for current layout, branch-depth, reward-depth, and Ukraine/Belarus readability findings.
- This does not touch flags.
- This does not claim live-game validation.
