# Air Winter Event Pilot Depth Review

## Review boundary

This review compared the pre-expansion 35-block Air Winter event pilot with the accepted biome and chain-depth obligations. It also records the implemented Phase 1 regional return, heavy-industry, island-refugee, Desert City, and dead-city salvage tranches. It is a source review only. Hearts of Iron IV was not launched.

The pilot already proves the bounded dispatch model, one visible event per eligible country cooldown, regular state and country event targets, delayed deterministic results, state memory, AI choice weights, Deaths integration, and cleanup through the existing monthly state pass. It does not count toward the 660-block Fallout living-world floor.

## Accepted biome coverage

| Accepted state identity | Pre-expansion coverage | Review result |
| --- | --- | --- |
| Breadbasket | `chaosx.fallout.10` preserves or consumes seed stock and writes state memory. | Partial. Event 18 carries the delayed result and guarded storage diverts local factories. Post-Fallout food recovery remains approval-gated. The active user contract forbids a political-power store. |
| Coal or heavy industry | `chaosx.fallout.23` and `.24` allocate scarce heat and return a delayed coal-ledger result. | Covered by the dedicated `chaosx.fallout.36` and `.37` furnace chain. Positive coal or an exact four-operational-factory ladder establishes state identity. The broad clinic and heat route remains available after exact Phase 3 identities are exhausted. |
| Hydroelectric region | No event checked a dam building before the first expansion. | Covered by `chaosx.fallout.22` and `.25`. |
| Oil region | No event checked oil resources, refineries, or fuel storage before the first expansion. | Covered by `chaosx.fallout.26` and `.27`. |
| Tropical coast | `chaosx.fallout.12` and `.15` cover nearshore food loss, deep-water patrols, and a delayed return or loss. | Covered. |
| Desert city | `chaosx.fallout.13` covers frozen mains and water convoys. | Covered by the exact-receipt `chaosx.fallout.13` route and `chaosx.fallout.49`. Three authorities commit municipal works, railway tankers, or motor columns and return through nine deterministic results. |
| Mountain capital | `chaosx.fallout.5` and `.14` covered marked passes, herds, and lower-valley movement. | Covered by `chaosx.fallout.16` and `.17`, including shelter, industry, delayed outcomes, and population protection. |
| Island state | `chaosx.fallout.12` and `.15` cover small craft, rescue patrols, food, exposure, disease, and state memory. | Covered for maritime survival and refugee admission by `chaosx.fallout.38` and `.39`. The dedicated route uses exact engine island topology, a real foreign coastal source, balanced population movement, three policies, and six delayed results. |
| Dead city candidate | No event performed an early salvage transaction before the Phase 5 expansion. | Covered by `chaosx.fallout.47` and `.48`. The route identifies a ruined major city through original urban category, a persistent building-loss receipt, current damaged-building evidence, and continued owner control. It is not described or treated as a committed Fallout dead-city grade. |
| Reactor state | No event checked reactor buildings or created a cooling failure before the first expansion. | Covered by `chaosx.fallout.28` and `.29`. |

## Chain-depth review

The pilot has strong delayed-result depth in its transport, heating, shelter, harvest, city, archive, continuity, thaw, and second-winter families. Those chains carry a state target, record a branch flag before dispatch, resolve through state conditions, write durable memory, and clear the pending branch.

The five Phase 1 regional entries now carry a complete shared delayed return. Several Phase 2 regional entries remain intentionally shorter. The mountain-capital and exact Desert City routes carry full delayed results, while other regional entries establish voice and early choices without all returning later.

The most important gap identified by the baseline review was infrastructure identity. The accepted hydroelectric, oil, reactor, and exact coal or heavy-industry rows lacked dedicated live identity routes, even though the engine exposes the required state buildings and resources.

## Phase 1 regional return depth

The Phase 1 regional return contract contains six manually authored blocks:

- `chaosx.fallout.1` through `.5`, the five regional openings
- `chaosx.fallout.6`, the shared 21-day result

The ten opening policies write exclusive owner-bound branches and preserve their matching state and country memories. The shared result requires regular country and state targets, the generic pending row, the stored original owner, current ownership, and exactly one branch. It reads live ledgers and operational buildings after the delay even if ordinary Air Winter progression has moved the state beyond Phase 1.

Each branch exposes one success and one direct inverse failure. Exact pre-choice AI projections reverse the opening ledger changes, then government and crisis weights express policy preference. Casualty failures route through Deaths. Phase 1 raises Building Damage Pressure where appropriate but never damages a building. Three mutually exclusive timed state modifiers represent factory-access disruption, supply disruption, or marked-corridor relief for 21 days. Opening-only stale rejection cannot clear a newer transaction. Full proof is recorded in `AIR_WINTER_PHASE_1_REGIONAL_RETURN_EVENT_PROOF.md`.

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

## Island-refugee depth

The island-refugee contract contains two manually authored blocks:

- `chaosx.fallout.38`, Boats Beneath the Shore Lights
- `chaosx.fallout.39`, Thirty Days at the Island Shore

The route accepts the exact engine `is_island_state` or `is_one_state_island` topology after mountain-capital identity and before generic city routing. The existing monthly state pass records one highest-scoring live coastal source per owner. The bounded dispatcher excludes the receiver and selects the highest remaining source score, with lower state id resolving an exact tie.

Dispatch defers the Phase 2 seen flag and first-frost receipt. No live source means no event, cooldown, receipt, or marker consumption. Rescue, quarantine, and exclusion calculate 2 percent, 1 percent, or 0.25 percent of current destination population, apply ceilings of 40,000, 20,000, or 5,000 people, and protect 1,000 people at the source. The exact source loss is added to the destination, so migration does not create population or enter the Deaths ledger.

The opening spends real Manpower, Convoys, or Support Equipment where required and writes one exclusive branch only after a positive transfer. Event `.39` partitions each branch into direct success and inverse failure after 30 days. All six outcomes write distinct state and country memories. The three failures record local casualties through Deaths. Stale and zero-transfer openings roll back without consuming the route. The complete engine-sensitive proof is in `AIR_WINTER_PHASE_2_ISLAND_REFUGEE_SOURCE_AND_POPULATION_PROOF.md`.

## Desert City depth

The Desert City contract contains one shared opening and one dedicated result:

- the exact-receipt interface inside `chaosx.fallout.13`, The Frozen Main and the Ward Cisterns
- `chaosx.fallout.49`, nine policy-specific water-route results after 30 days

The Phase 2 selector checks exact arid urban identity after mountain capitals and engine islands but before the generic city route. A typed `desert_city` subtype survives temporary selection, first-frost storage, country candidate comparison, and the final owner-bound opening receipt. Generic arid and Mediterranean event 13 rows carry subtype `none`. First-frost coalescing compares both event id and subtype, so the two event 13 identities cannot consume each other's seasonal marker.

Municipal works are always executable and exchange Stability and temporary local factory access for water, shelter, and adaptation. Railway tankers require an operational railway and pay Manpower, Trains, and Fuel. Motor columns require operational infrastructure and pay Manpower, Motorized Equipment, Fuel, and Command Power. Paid choices repeat exact affordability at display and click time.

Each branch resolves through success, partial, or failure. The nine result partitions are exhaustive and mutually exclusive. Failures use the Deaths system, apply route-specific water, exposure, disease, refugee, Stability, or War Support consequences, and damage at most one operational repairable target. Success applies a timed local supply benefit, while failure applies a timed local supply penalty. The result validator independently proves the pending flag, bound original owner, event country, state owner, and exact branch. A malformed branch without its pending receipt is cancelled during the existing state reconciliation pass. The full proof is in `AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_PROOF.md`.

## Phase 5 dead-city salvage depth

The dead-city salvage contract contains two manually authored blocks:

- `chaosx.fallout.47`, Lamps Beneath the Empty Blocks
- `chaosx.fallout.48`, What Came Up from the Service Streets

The selector requires Phase 5, an original `large_city`, `metropolis`, or `megalopolis` category, a persistent Air Winter building-loss receipt, current damage in one of seven building families, and ownership and control by the same country. This proves a ruined major-city salvage candidate without claiming the later Fallout `dead_city` grade.

The opening gives survey engineers, military quartermasters, and licensed district crews competing control of the same site. Survey and military routes repeat exact affordability checks before display and at click time. Licensed salvage has no payable resource gate, so every valid opening retains one executable option. Each route writes one exclusive branch, applies distinct Adaptation, Reclamation, Exposure, pressure, and national consequences, refreshes the 46-day cooldown, and schedules event `.48` after 30 days.

The result uses success, partial, and disaster predicates for each branch. Their complements are explicit, so exactly one ordinary result is available for every valid branch. One narrow fictional altered return replaces a disaster only when the final Chaos tier, active nuclear fallout with positive intensity, and active chemical or biological contamination all coexist. All casualties enter Deaths. Equipment gains use concrete equipment types. Disaster paths damage at most one operational repairable building when a target remains. Every result marks the site exhausted, while ownership or control loss cancels the pending branch through reconciliation. The complete proof is in `AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_PROOF.md`.

## Implementation disposition

The pilot contains 52 blocks, 191 options, 190 effect-bearing options, and 67 delayed-result schedules. Phase 1 regional policy, island refugee admission, seed and livestock policy, mountain capitals, Desert City water logistics, hydroelectric states, oil or refinery states, reactor states, coal or heavy-industry states, and ruined major-city salvage have opening and delayed-result chains. The shared Phase 3 country memory still permits one ordinary Phase 3 identity chain per country in a campaign, so the four exact infrastructure routes provide deterministic cross-playthrough breadth rather than four guaranteed incidents for every country. The shared Phase 5 memory likewise permits one ordinary Phase 5 identity chain per country, with the dead-city route winning over the generic Phase 5 city route when both qualify.

## Deferred depth

The following accepted rows remain unresolved after this tranche:

- an approved post-Fallout food-recovery consumer for the seed-ledger outcomes
- post-Fallout focus, successor-identity, and migration consumers for island-refugee policy memory

They require separate reviewed contracts and are not claimed by the completed expansions.
