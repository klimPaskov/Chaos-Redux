# Event005 terminal release tranche

## Scope

Parent-side patch for the Soviet Collapse terminal release path.

## Changed files

- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Implementation

- `soviet_collapse_apply_terminal_collapse` now runs `soviet_collapse_force_terminal_all_possible_core_countries_exhaustive` after the ordinary terminal republic release, Soviet subject freeing, and current-tier internal release pass.
- The normal active/progressive release scheduler remains unchanged. Internal, niche, and pressure-successor releases during the crisis still depend on dynamic release pressure, chaos tier gates, and capped release loops.
- The standalone triggerable scenario already used the exhaustive all-possible release sweep; this patch aligns the organic Union Unmade path with that terminal behavior.

## Validation

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt`
- Brace balance check on `common/scripted_effects/005_soviet_collapse_effects.txt`: zero net braces, no negative nesting.

## Remaining risks

- This does not rebalance the progressive release cadence, focus-tree layout, or evolution-detail localisation. Those remain separate active Event005 work items.
- High-chaos successor forcing is still controlled by chaos/scenario flags. This patch only guarantees all possible former-union core countries are swept at Union Unmade.
