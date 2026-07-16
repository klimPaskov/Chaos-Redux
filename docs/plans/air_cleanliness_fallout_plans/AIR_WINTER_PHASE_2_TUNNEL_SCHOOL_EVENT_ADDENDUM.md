# Air Winter Phase 2 Tunnel School Event Addendum

## Source and scope

This addendum implements the accepted Mountain Capital and Tunnel Schools row in `docs/specs/air_cleanliness_fallout_specs/specs/baseline/02_winter_mapmode_and_state_effects.md`.

The tranche is limited to one Phase 2 opening event, one delayed result, the established monthly Deaths calculation, and the scheduler records needed to route and clean the chain. It adds no periodic callback, world scan, Fallout survival coefficient, successor package, blackout GUI change, or manual scenario behavior.

## Selection identity

`chaosx.fallout.16` is selected only when the candidate state is both:

- classified as highland by `air_winter_presentation_is_highland`
- the current capital according to the state scoped `is_capital` trigger

The mountain-capital branch runs before the generic city branch. Non-capital highland and polar states continue to use `chaosx.fallout.14`. Capitals in other presentation classes retain their existing Phase 2 routes.

The typed event id freezes the selection identity. A first-frost marker can dispatch later even if the country moves its capital. The opening and delayed result continue to require the original state, original owner, valid Air Winter state, and highland presentation class. They do not reclassify the stored state as a current capital after selection.

## Classes Beneath the Capital

`chaosx.fallout.16` presents three choices.

### Civic tunnel schools

The administration converts service tunnels and protected galleries into full-time classrooms, kitchens, and dormitories.

- Cost: 500 manpower and 30 support equipment
- Immediate ledger: Shelter Capacity plus 6, Exposure minus 1, Building Damage Pressure plus 15
- Industry: local factory availability falls by 20 percent during the 30-day conversion
- Branch: `air_winter_tunnel_chain_civic`
- Opening memory: `air_winter_memory_tunnel_civic_schools`
- Delayed success: Building Damage Pressure is at most 65 and Disease Pressure is at most 65

### Alternating school and workshop shifts

Workshops operate at night while classrooms, kitchens, and infirmaries use the same protected space by day.

- Cost: 200 manpower and 15 support equipment
- Immediate ledger: Shelter Capacity plus 4, Adaptation plus 4, Building Damage Pressure plus 8
- Industry: local factory availability falls by 10 percent during the 30-day shared schedule
- Branch: `air_winter_tunnel_chain_shifts`
- Opening memory: `air_winter_memory_tunnel_shift_schools`
- Delayed result: the shared schedule settles without a success roll

### Dispersed cellar schools

The administration keeps the main tunnels available for repair shops and disperses classes through neighborhood cellars and protected rooms.

- Cost: 1 percent Stability
- Immediate ledger: Shelter Capacity plus 2, Adaptation plus 6, Exposure plus 1, Building Damage Pressure minus 8
- Branch: `air_winter_tunnel_chain_cellars`
- Opening memory: `air_winter_memory_tunnel_cellar_schools`
- Delayed success: Adaptation is at least 25 and Exposure is at most 55

The third route is always available. Every choice rechecks the original country and state transaction before payment, writes its branch before binding the pending owner, and calls the result after thirty days.

## The Tunnel Bell

`chaosx.fallout.17` has five mutually exclusive deterministic outcomes.

| Outcome | Ledger result | Durable result memory |
| --- | --- | --- |
| Civic conversion holds | Shelter plus 4, Adaptation plus 2, Disease minus 2, Building Pressure minus 8 | `air_winter_memory_tunnel_civic_success` |
| Civic conversion strains the galleries | Shelter minus 2, Exposure plus 1, Disease plus 2, Building Pressure plus 8 | `air_winter_memory_tunnel_civic_failure` |
| Shared shifts settle | Shelter plus 2, Reclamation plus 2, Building Pressure minus 8 | `air_winter_memory_tunnel_shifts_settled` |
| Cellar network holds | Shelter plus 2, Exposure minus 1, Disease minus 1 | `air_winter_memory_tunnel_cellars_success` |
| Cellar network fragments | Shelter minus 2, Exposure plus 2, Disease plus 2 | `air_winter_memory_tunnel_cellars_failure` |

The civic success, shared-shift result, and cellar success also write `air_winter_memory_tunnel_school_protection`. This shared memory multiplies the established monthly Air Winter civilian death percentage by 0.90 after the normal exposure, food, shelter, infrastructure, occupation, and adaptation calculation. It guarantees a real population-loss reduction without changing the Fallout survival formula.

## AI contract

The opening uses the existing primary, secondary, and risky base weights.

- Civic schools gain weight under democratic or communist government, when shelter is low, and when the delayed result is plausible. Pre-choice plausibility requires Building Damage Pressure at most 50 and Disease Pressure at most 65.
- Shared shifts gain weight under neutrality or peace and when neither specialized result is plausible.
- Cellar schools gain weight during war, under fascism, when Building Damage Pressure is high, and when the delayed result is plausible. Pre-choice plausibility requires Adaptation at least 19 and Exposure at most 54.

The pre-choice thresholds translate each opening route through its exact ledger changes. Unaffordable options are hidden and repeat the same affordability checks inside their click effects.

## Industry and cleanup

The civic and shared-shift routes use dedicated temporary state dynamic modifiers with `local_factories`. The duration is 31 days so the penalty remains active until the 30-day result resolves. The result removes both modifiers before applying its branch outcome.

Branch cancellation removes both modifiers and all three branch flags. State memory reset clears every opening memory, result memory, and the shared death-protection memory. The existing pending-owner reconciliation cancels the chain on ownership loss, invalid ownership, state invalidation, or Fallout transition. The Fallout snapshot therefore cannot be mutated by a late tunnel-school result.

## Assets

Both events use `GFX_report_event_air_winter_phase_2`, the dedicated Phase 2 Air Winter report image. The existing modifier icon `GFX_air_winter_phase_2` is used for both temporary industry modifiers. No new DDS, sprite definition, sound, or generated art is required.

## Review acceptance

This addendum does not approve or imply a post-Fallout seed-vault consumer, Fallout survival numbers, NZL successor work, blackout GUI correction, manual SCN-014, a province strike sweep, treaty pooled costs, active combat pressure, or strategic-bombing winter multipliers.
