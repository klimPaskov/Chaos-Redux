# Shared individual-crisis targeting effects

`adjust_individual_crisis_candidate_ticket_weight` is a country-scope helper for weighted bounded-country pools.

Input: the caller sets the temporary `individual_crisis_candidate_base_weight` immediately before the call.

Output: `individual_crisis_candidate_adjusted_weight` is always initialized and receives the caller base multiplied by the shared load curve.

The curve is base multiplied by four at derived load zero, base multiplied by two at load one, base multiplied by one at load two, and zero at load three or above.

The helper derives load through `individual_crisis_load_is_below_cap` and owns no persistent state.

`adjust_individual_crisis_existing_provider_candidate_ticket_weight` is the Random Terror-specific entry point.

It temporarily excludes exactly the current Random Terror provider from the derived load, then restores the exclusion marker to zero.

`individual_crisis_apply_candidate_ticket_curve` is the private shared arithmetic worker used by both public entry points.

Example:

```text
set_temp_variable = { individual_crisis_candidate_base_weight = 1 }
adjust_individual_crisis_candidate_ticket_weight = yes
# Read individual_crisis_candidate_adjusted_weight here.
```

The load trigger rebuilds a temporary load from the fourteen provider lifecycle markers and is documented in `docs/systems/event_system/individual_crisis_targeting.md`.

## Fixed-target companion status

`apply_individual_crisis_fixed_target_event_pressure` has no declaration or consumed caller.
Its normalized pressure factors are already declared as `individual_crisis_targeting.load_zero_factor`, `load_one_factor`, and `load_two_factor`, with the existing cap providing the zero-result band.
These factors are separate from the whole-ticket multipliers used by the candidate helpers above.

A future companion can evaluate an explicit owner-selected country scope and return temporary pressure without changing persistent state.
The first consumer must declare target resolution, pressure units, output consumption, missing-target behavior, and consistency across the weighted picker's two evaluation passes before implementation.
Callers must initialize temporary inputs and outputs outside the helper to preserve their lifetime across helper boundaries and retain a zero result if entering the target scope is skipped.

The current design and exact blockers are recorded in [the fixed-target companion handoff](../../docs/plans/021_random_civil_war_plans/subagent_handoffs/individual_crisis_fixed_target_contract_2026-09-13.md).
This section documents unresolved architecture and does not declare an executable API.
