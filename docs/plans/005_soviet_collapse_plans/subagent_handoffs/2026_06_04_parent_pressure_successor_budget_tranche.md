# Event005 Parent Tranche - Pressure Successor Release Budget

## Scope

Parent-side bounded implementation toward the Soviet Collapse release goals.

Latest user constraint respected: no `gfx/flags` or `interface/flags` files were read or edited.

## Files Changed

- `common/script_constants/005_soviet_collapse_constants.txt`

## Gameplay Surface

Dynamic follow-on release pressure for high-chaos special successor countries.

## Before

The live follow-on budget for special pressure successors was too low for the current special-successor pool:

- chaos tier 3: 2 releases
- chaos tier 4: 6 releases
- chaos tier 5: 12 releases
- cap: 18 releases

That could leave many eligible special actors outside the live progressive release flow even after the crisis reached high chaos.

## After

The budget now lets the existing dynamic `every_possible_country` pressure-successor scan exhaust far more of the eligible pool:

- chaos tier 3: 8 releases
- chaos tier 4: 24 releases
- chaos tier 5: 48 releases
- cap: 64 releases

The implementation remains dynamic. It still uses `is_soviet_collapse_pressure_successor_progressive_candidate = yes` and the existing release helper instead of hardcoding a separate tag sequence.

## Evidence

The current special pressure-successor trigger contains 32 spawn tags, including `FEV`, `NRF`, `OGB`, `PRA`, `TSC`, `ICD`, `ARD`, and `NLC`. A tier-5 budget of 48 gives the live follow-on pulse enough attempts to release the full eligible set when their existing candidate triggers pass.

Terminal collapse and the chaos triggerable scenario already set `soviet_collapse_force_all_chaos_successors` before calling `soviet_collapse_spawn_terminal_high_chaos_successors`, so this tranche targets the non-terminal live high-chaos release pacing rather than replacing terminal release logic.

## Remaining Gaps

- This does not complete the full focus-tree rework.
- The selected foreign patron republic menu still needs runtime confirmation or a narrower fix for reports where selecting a target opens an empty panel.
- Evolution detail text still needs a separate spreadsheet/spec alignment pass.
