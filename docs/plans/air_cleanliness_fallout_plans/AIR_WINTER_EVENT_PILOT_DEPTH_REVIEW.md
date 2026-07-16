# Air Winter Event Pilot Depth Review

## Review boundary

This review compared the pre-expansion 35-block Air Winter event pilot with the accepted biome and chain-depth obligations. It also records the implemented heavy-industry tranche. It is a source review only. Hearts of Iron IV was not launched.

The pilot already proves the bounded dispatch model, one visible event per eligible country cooldown, regular state and country event targets, delayed deterministic results, state memory, AI choice weights, Deaths integration, and cleanup through the existing monthly state pass. It does not count toward the 660-block Fallout living-world floor.

## Accepted biome coverage

| Accepted state identity | Pre-expansion coverage | Review result |
| --- | --- | --- |
| Breadbasket | `chaosx.fallout.10` preserves or consumes seed stock and writes state memory. | Partial. Event 18 carries the delayed result and guarded storage diverts local factories. Post-Fallout food recovery remains approval-gated. The active user contract forbids a political-power store. |
| Coal or heavy industry | `chaosx.fallout.23` and `.24` allocate scarce heat and return a delayed coal-ledger result. | Covered by the dedicated `chaosx.fallout.36` and `.37` furnace chain. Positive coal or an exact four-operational-factory ladder establishes state identity. The broad clinic and heat route remains available after exact Phase 3 identities are exhausted. |
| Hydroelectric region | No event checked a dam building before the first expansion. | Covered by `chaosx.fallout.22` and `.25`. |
| Oil region | No event checked oil resources, refineries, or fuel storage before the first expansion. | Covered by `chaosx.fallout.26` and `.27`. |
| Tropical coast | `chaosx.fallout.12` and `.15` cover nearshore food loss, deep-water patrols, and a delayed return or loss. | Covered. |
| Desert city | `chaosx.fallout.13` covers frozen mains and water convoys. | Partial. It is a single-block regional choice. |
| Mountain capital | `chaosx.fallout.5` and `.14` covered marked passes, herds, and lower-valley movement. | Covered by `chaosx.fallout.16` and `.17`, including shelter, industry, delayed outcomes, and population protection. |
| Island state | `chaosx.fallout.12` and `.15` cover small craft, rescue patrols, food, exposure, disease, and state memory. | Covered for maritime survival. Refugee admission policy remains outside this pilot. |
| Dead city candidate | No event performs an early salvage transaction. | Missing. It should remain separate from the Phase 3 infrastructure batch because it needs its own casualty and equipment-risk contract. |
| Reactor state | No event checked reactor buildings or created a cooling failure before the first expansion. | Covered by `chaosx.fallout.28` and `.29`. |

## Chain-depth review

The pilot has strong delayed-result depth in its transport, heating, shelter, harvest, city, archive, continuity, thaw, and second-winter families. Those chains carry a state target, record a branch flag before dispatch, resolve through state conditions, write durable memory, and clear the pending branch.

The Phase 1 and several Phase 2 regional entries remain intentionally shorter. The mountain-capital route now carries a full delayed result, while other regional entries establish voice and early choices without all returning later.

The most important gap identified by the baseline review was infrastructure identity. The accepted hydroelectric, oil, reactor, and exact coal or heavy-industry rows lacked dedicated live identity routes, even though the engine exposes the required state buildings and resources.

## Selected expansion

The selected reviewed tranche adds six manually authored blocks:

- `chaosx.fallout.22` and `.25`, Dam Ice Crisis and its delayed result
- `chaosx.fallout.26` and `.27`, Black Refinery Snow and its delayed result
- `chaosx.fallout.28` and `.29`, Cooling Pond Emergency and its delayed result

The exact Phase 3 routes are selected before the existing broad transport and clinic routes when the same state has the relevant identity. The state-local order is reactor, dam, oil or refinery, coal or heavy industry, transport, then clinic and heat. Country candidate selection still compares family priority, origin cycle, phase and pressure score, then state id. A higher-pressure transport state can therefore defeat a reactor state in another part of the same country.

This batch changes no monthly phase coefficient, population formula, Fallout grade coefficient, treaty policy, or world iteration. It uses the existing Air Winter ledgers, event cooldown, candidate ordering, state refresh, Deaths and fallout helpers, and pending-chain cleanup.

## Heavy-industry depth

The heavy-industry contract contains two manually authored blocks:

- `chaosx.fallout.36`, The Furnace Shift
- `chaosx.fallout.37`, The Works Inspector's Ledger

The route accepts positive coal or a combined total of at least four operational factories. Its exact five-case ladder is at least four military, at least three military and one civilian, at least two military and two civilian, at least one military and three civilian, or at least four civilian. Fully damaged factories do not qualify.

Full shifts add Adaptation, Exposure, Building Damage Pressure, Stability loss, and a Deaths request. The delayed success gate requires Adaptation at least 40 and Building Damage Pressure no more than 55. Failure issues 0.50 repairable damage to one operational military factory, otherwise one operational civilian factory, otherwise infrastructure. If no target remains, the failure still applies Exposure, pressure, Deaths, and Stability consequences without inventing a damage target.

Controlled shutdown conditionally applies a 31-day local-factory modifier and a 31-day coal-output modifier. Event `.37` arrives on day 30 and removes both in its immediate block before the restart result. Full shifts and shutdown are exact exclusive branches. Every opening clears old furnace memory, refreshes the state, refreshes the 46-day cooldown immediately before scheduling, and every result or cancellation clears its branch and shutdown state. AI full-shift plausibility uses the exact pre-choice inverse of the 40 and 55 result gate.

## Mountain-capital depth

The mountain-capital contract contains two manually authored blocks:

- `chaosx.fallout.16`, Classes Beneath the Capital
- `chaosx.fallout.17`, The Tunnel Bell

The route checks highland and capital identity before generic city routing. Civic conversion and shared shifts apply temporary local factory penalties while increasing shelter. Civic conversion and cellar dispersal resolve through disclosed ledger thresholds. Shared shifts resolve to a fixed middle outcome. Successful routes write a durable protection memory that multiplies the existing monthly Air Winter civilian death percentage by 0.90.

The route leaves the phase coefficients, Fallout survival coefficients, treaty policy, and world iteration unchanged. Only states with a successful tunnel-school result modify the established Air Winter Deaths calculation.

## Seed-ledger depth

The seed-ledger contract contains:

- `chaosx.fallout.18`, The Spring Ledger
- two conditional seed-plot outcomes
- one fixed herd-depletion outcome
- two conditional breeding-stock outcomes

The delayed result arrives after 45 days. Seed plots test Reclamation and Exposure. Breeding stock tests Food Reserve and Shelter Capacity. AI plausibility gates translate those thresholds back through each opening route's exact ledger changes. All three routes use the shared owner-bound pending transaction and state reset cleanup.

The guarded seed route also applies a 10 percent local factory penalty for 46 days. The modifier is removed when either seed result resolves or any pending-chain cancellation runs.

This batch changes no phase coefficient, Fallout survival coefficient, treaty policy, route selector, or world iteration.

## Implementation disposition

The pilot contains 46 blocks, 137 options, 136 effect-bearing options, and 48 delayed-result schedules. Seed and livestock policy, mountain capitals, hydroelectric states, oil or refinery states, reactor states, and coal or heavy-industry states have opening and delayed-result chains. The shared Phase 3 country memory still permits one ordinary Phase 3 identity chain per country in a campaign, so the four exact infrastructure routes provide deterministic cross-playthrough breadth rather than four guaranteed incidents for every country.

## Deferred depth

The following accepted rows remain unresolved after this tranche:

- an approved post-Fallout food-recovery consumer for the seed-ledger outcomes
- an early dead-city salvage chain
- refugee admission and identity consequences for island states

They require separate reviewed contracts and are not claimed by the completed expansions.
