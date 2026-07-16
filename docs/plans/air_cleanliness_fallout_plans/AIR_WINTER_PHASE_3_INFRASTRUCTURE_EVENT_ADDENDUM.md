# Air Winter Phase 3 Infrastructure Event Addendum

## Source and scope

This addendum implements three accepted rows from `docs/specs/air_cleanliness_fallout_specs/specs/baseline/02_winter_mapmode_and_state_effects.md`: Dam Ice Crisis, Black Refinery Snow, and Cooling Pond Emergency.

The batch is limited to Phase 3 event routing and six manually authored blocks. It does not add a new scheduler family, a periodic callback, treaty policy, population movement, or a Fallout survival formula.

## Deterministic route order

After an unseen Phase 3 state becomes the country's ordinary event candidate, route selection inside that state uses this order:

1. reactor state
2. hydroelectric state
3. oil or refinery state
4. existing transport state
5. existing clinic and heat route

The exact identities are:

- reactor: `nuclear_reactor`, `nuclear_reactor_heavy_water`, or `commercial_nuclear_reactor`
- hydroelectric: `dam`, `dam_mountain`, or `cataract_dam_mountain`
- oil or refinery: an oil resource or an operational `synthetic_refinery`

Only the selected opening ids enter the ordinary candidate allowlist. Result ids are called from their opening chain and are not scheduler candidates.

The order is state-local. Country candidate selection still compares family priority, origin cycle, frozen phase and pressure score, then state id. A higher-scoring transport state can defeat a reactor state elsewhere in the country. The shared `air_winter_event_seen_phase_3` memory permits one ordinary Phase 3 chain per country.

## Dam Ice Crisis

`chaosx.fallout.22` presents three choices:

- put protected crews on the gates and intakes
- lower the reservoir before the next freeze
- keep every turbine feeding the emergency grid

All three choices return after thirty days. Protected crews resolve from disclosed Water Security and Reclamation thresholds. Full-head operation resolves from disclosed Adaptation and Building Damage Pressure thresholds. The controlled drawdown is deterministic and spends water for lower building pressure. Failure damages one installed dam family in a fixed order and local infrastructure. Every route writes distinct state memory.

## Black Refinery Snow

`chaosx.fallout.26` presents three choices:

- shut exposed lines and ration fuel
- keep military fuel moving
- redirect process heat into district shelters

The result returns after twenty-one days. Military output succeeds only when Adaptation remains high and Building Damage Pressure remains below its ceiling. Natural oil output receives a temporary state resource penalty. An operational synthetic refinery receives repairable opening damage. Fire failure can damage an installed synthetic refinery, fuel silo, and local infrastructure. The district-heating route improves Shelter Capacity and Disease Pressure while consuming fuel. Every route writes distinct state memory.

Holding military output can leave `air_winter_memory_oil_fortress_candidate` on the state. No Fallout successor or fortress consumer exists yet, so this tranche does not claim that later route as implemented.

## Cooling Pond Emergency

`chaosx.fallout.28` presents three choices:

- scram the reactor and flood the cooling circuit
- hold reduced output through the cold
- give the plant council emergency authority

The result returns after thirty days. Water Security, Adaptation, Building Damage Pressure, and national Energy Fulfilment determine the routes. Emergency pumping spends manpower, Command Power, and support equipment. It applies a temporary state `local_factory_energy_consumption` modifier, while the country-scoped `energy_ratio` trigger checks whether the grid still meets the disclosed threshold. A failed cooling route damages one installed reactor family in a fixed order and calls the existing nuclear-fallout state helper. The helper adds a low reactor-accident intensity up to its cap and ensures state fallout remains for at least six months. This adds an ordinary state fallout input without changing the Fallout grade formula or global Air Contamination coefficients.

## AI and government variation

Every opening choice has an AI weight. Democratic administrations prefer public safety and shutdown. Fascist administrations and countries at war place more weight on continued output. Communist administrations place more weight on protected work crews, district heat, and plant councils. Neutral administrations prefer controlled drawdown and technical custody. Derived pre-choice state-ledger thresholds include each route's exact opening changes. The reactor scram uses a separate 60 percent pre-choice energy floor above its 50 percent result threshold, accounting for its own local demand increase and later live grid movement. Ambitious routes therefore gain weight only when the delayed success remains plausible.

The delayed result has one valid option for the committed branch and state conditions. Hidden AI therefore resolves the same deterministic branch as a human player.

## Cleanup

Each opening writes one branch flag, one pending-result flag, and the originating country on the state before the delayed event is issued. State reset, ownership loss, an invalid owner, active Fallout, or an active Fallout transition invalidates the branch. The existing Fallout snapshot state pass freezes all Air Winter fields and then calls `air_winter_event_cancel_pending_chain`, so a later result cannot mutate the frozen row. A resolved result clears its exact branch flag before the state is refreshed.

The state memory reset clears every new opening and result memory. No state or country is scanned outside the existing monthly Air Winter pass.

## Assets

All six blocks use `GFX_report_event_air_winter_phase_3`, the dedicated Air Winter Phase 3 report image registered in `interface/air_cleanliness_winter.gfx`. The existing manifest row maps all ten Phase 3 blocks to that sprite. No new art, sprite, or audio is required for this tranche.

## Review acceptance

This addendum does not approve or imply Shared Sampling Grid precision beyond basic treaty reports, relief-vote, pooled-cost, evacuation-corridor, major-burner, Fallout numerical-survival, successor, or blackout-GUI policies.
