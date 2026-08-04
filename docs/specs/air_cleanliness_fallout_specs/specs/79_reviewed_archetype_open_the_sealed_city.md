# Reviewed archetype chain 79: Open the Sealed City

## Status

This is a reviewed, dormant implementation row for the Quarantine state archetype. It is not a normal super-event and it does not create a country tag. The chain is eligible only after a completed Border Inspection Crisis memory, a current urban state receipt, recovery-year timing, and a live Quarantine government.

## State contract

The candidate producer selects the lowest valid owned state id. The state must be controlled by the country, have current identity, survival, and supply rows, retain a city or large-city category, and carry `fallout_event_726_memory_closed`. The state must have current Air Winter Shelter, Supply Access, Reclamation, Exposure, and optional Disease ledgers, one repairable infrastructure level, and population above the minimum. Registry, delayed result, callback, and cleanup gates recheck the same state id and owner.

The opening freezes Food, Medicine, Power, Recognition, Cohesion, population, Shelter, Supply Access, Reclamation, infrastructure, Exposure, and Disease. It also initializes country-owned sealed-city ledgers for civic legitimacy, scientific access, military salvage, memorial readiness, district trust, salvage access, and faction pressure. The ledgers are clamped to the shared numeric range.

## Branches

The human and hidden AI lanes share the same four branches.

1. Civic rooms reopen under named ward stewards. Food, Scrap, and Recognition fund the register and key custody.
2. Scientific access sends a clinic and archive team through the service tunnel. Food, Power, Scrap, and Recognition fund sampling and chain of custody.
3. Military salvage sends a controlled column to the depot. Food, Fuel, Support Equipment, and Command Power fund filters, pumps, and the inspected salvage route.
4. A permanent memorial district opens around the safest rooms. Food, Medicine, Fuel, and Recognition fund the family register, clinic support, and memorial keys.

Each branch schedules a deterministic 35-day result. The result grades the frozen state and country values, applies branch-specific city ledgers, changes Supply Access, Shelter, Reclamation, Exposure, Disease, Food, Cohesion, Recognition, Stability, War Support, and bounded Deaths, and adds a short dedicated modifier. A 270-day callback regrades current district trust, branch ledger strength, legitimacy, scientific access, memorial readiness, and faction pressure. It applies further state and country changes, records the delayed memory, and authenticates cleanup.

Failure casualties use `apply_exact_state_civilian_population_loss` with the Fallout aftermath reason. The chain never removes the host country, creates a replacement tag, or uses a generic political-power store. A stale owner, state, generation, target, or candidate receipt cancels before a result or callback can mutate the world.

## Scheduler and Event Log wiring

The row uses candidate `740`, transaction `710077`, route `7186`, and Event Log history `9183`. Event ids are `chaosx.fallout.740` through `chaosx.fallout.746` under the existing `chaosx.fallout` namespace. The ordinary producer owns candidate construction, the state target is explicit, and the chain remains dormant until the shared Fallout coordinator issues a receipt.

Human events `.740`, `.742`, and `.744` are visible. Hidden AI events `.741`, `.743`, and `.745` resolve the same branch and delayed contracts without player-facing text. Cleanup `.746` removes the state reservation, timed modifiers, temporary variables, and country flags after generation-bound reauthentication.

History `9183` routes through the shared Event Log name and detail selectors. Choice, result, callback, and cancellation payloads have dedicated scripted localisation and concrete Ash Ward, North Gate, East Gate, clinic, and depot wording.

## Asset and review surface

The dedicated report image is `GFX_report_event_fallout_open_the_sealed_city`, registered in `interface/fallout_consolidated.gfx`. Source, processed PNG, runtime DDS, manifest, and GFX handoff live under `docs/assets/740_open_the_sealed_city/`.

Candidate `FALLOUT-740` is an internal identity with no workbook or catalog row. The chain is intentionally dormant and does not increase release-floor credit until the wider reviewed tranche is promoted.
