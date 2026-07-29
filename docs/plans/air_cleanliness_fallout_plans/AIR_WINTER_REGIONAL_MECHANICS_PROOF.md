# Air Winter regional mechanics proof

## Scope

This proof records the deterministic mechanical differences attached to the reviewed nine-class Air Winter presentation ledger. The same class that selects ordinary-map snow, frost, cold rain, ash, dead vegetation, frozen water, dim light, and thaw now also changes state pressure and survival-ledger movement.

The implementation does not infer climate or geography at runtime. Each valid state already has one reviewed presentation-class receipt. The regional mechanics read that receipt through the existing `air_winter_presentation_is_*` triggers.

## Source ownership

Shared tuning lives in `air_winter_regional_mechanics` inside `common/script_constants/air_cleanliness_winter_constants.txt`.

The state consumers live in `common/scripted_effects/air_cleanliness_winter_effects.txt`:

- `air_winter_calculate_state_pressure` applies one regional pressure adjustment before adaptation, food, shelter, and reclamation resistance.
- `air_winter_update_survival_ledgers` applies one regional food-loss adjustment during an active winter phase.
- The same survival helper applies severe-phase shelter strain for boreal, highland, and polar states.
- The same survival helper applies regional water loss during an active winter phase.
- The same survival helper applies severe-phase disease pressure for maritime, Mediterranean, arid, tropical, equatorial, and oceanic states.

No new daily, weekly, monthly, country, or state iterator was added. These consumers run inside the existing host-owned monthly state pass.

## Regional balance table

| Presentation class | Pressure | Food loss | Severe shelter loss | Water loss | Severe disease |
| --- | ---: | ---: | ---: | ---: | ---: |
| Boreal continental | +6 | +0.50 | +0.20 | 0 | 0 |
| Temperate maritime | +1 | +0.10 | 0 | +0.10 | +0.50 |
| Mediterranean | -2 | +0.25 | 0 | +0.50 | +0.25 |
| Desert and arid plateau | -3 | +0.35 | 0 | +1.00 | +0.25 |
| Tropical coast and monsoon | -4 | +0.30 | 0 | +0.35 | +2.00 |
| Equatorial rainforest | -5 | +0.25 | 0 | +0.40 | +2.50 |
| Mountain and highland | +3 | +0.40 | +0.15 | +0.20 | 0 |
| Island and oceanic | -4 | +0.10 | 0 | +0.15 | +0.75 |
| Polar and subpolar | +8 | +0.60 | +0.30 | +0.25 | 0 |

Positive pressure makes a higher Air Winter phase more likely. Negative pressure is stored as a positive reduction constant and is subtracted by the state-pressure helper.

The additions are deliberately smaller than the global contamination and survival-ledger terms. Regional identity changes the path through winter without replacing infrastructure, occupation, adaptation, food, shelter, reclamation, strategic bombing, and neighboring-state pressure.

## Determinism proof

Each regional consumer uses one ordered `if` and `else_if` chain. A state can therefore receive at most one regional value from each mechanical family.

The presentation ledger is prepared before the Air Winter cycle opens. State pressure and survival updates read the same durable class throughout that cycle. No `random`, weighted list, unordered candidate choice, or changing country scope selects the class.

The state update retains its existing cycle receipt. Calling the state helper twice in one cycle cannot apply the regional food, shelter, water, or disease additions twice.

## Consequence integration

Regional pressure feeds the existing deterministic phase target and one-step phase transition. The resulting phase continues to drive:

- exact state population loss through the Deaths system
- building damage and repair pressure
- state-category degradation
- local supply and construction effects
- controller and enemy military movement and attrition
- country air-operation burden from working controlled airfields
- exposure and disease pressure
- food, shelter, water, adaptation, recovery, and reclamation
- event candidate selection
- winter mapmode data
- ordinary-map regional visual entities

The regional constants do not call Deaths directly. Population loss remains owned by `air_winter_apply_state_population_loss`, which preserves the shared exact-loss and Deaths receipt contract.

## Permanent Fallout atmosphere

`fallout_air_contamination_permanent_99` keeps Air Winter enabled after the transition pause. The next ordinary monthly cycle applies the same regional mechanics against the fixed 9,900-basis-point atmosphere. The permanent lock freezes Air Contamination inputs but does not freeze state winter consequences.

## Evidence boundary

The implementation is source-proven against the reviewed presentation ledger, the existing host monthly route, the Air Winter phase and survival helpers, the exact Deaths route, the official installed modifier catalogue, and vanilla state-modifier precedents. HOI4 was not launched. Live playtesting is a later user validation handoff and is not a completion requirement for this static implementation tranche.
