# Air Winter Event Pilot Depth Review

## Review boundary

This review compared the pre-expansion 35-block Air Winter event pilot with the accepted biome and chain-depth obligations. It is a source review only. Hearts of Iron IV was not launched.

The pilot already proves the bounded dispatch model, one visible event per eligible country cooldown, regular state and country event targets, delayed deterministic results, state memory, AI choice weights, Deaths integration, and cleanup through the existing monthly state pass. It does not count toward the 660-block Fallout living-world floor.

## Accepted biome coverage

| Accepted state identity | Pre-expansion coverage | Review result |
| --- | --- | --- |
| Breadbasket | `chaosx.fallout.10` preserves or consumes seed stock and writes state memory. | Partial. The opening is specific, but it has no delayed seed outcome. |
| Coal or heavy industry | `chaosx.fallout.23` and `.24` allocate scarce heat and return a delayed coal-ledger result. | Substantial. The chain is not restricted to an industrial state, so it remains a broad Phase 3 route. |
| Hydroelectric region | No event checks a dam building. | Missing. |
| Oil region | No event checks oil resources, refineries, or fuel storage. | Missing. |
| Tropical coast | `chaosx.fallout.12` and `.15` cover nearshore food loss, deep-water patrols, and a delayed return or loss. | Covered. |
| Desert city | `chaosx.fallout.13` covers frozen mains and water convoys. | Partial. It is a single-block regional choice. |
| Mountain capital | `chaosx.fallout.5` and `.14` cover marked passes, herds, and lower-valley movement. | Partial. Tunnel schooling and protected civic shelter remain absent. |
| Island state | `chaosx.fallout.12` and `.15` cover small craft, rescue patrols, food, exposure, disease, and state memory. | Covered for maritime survival. Refugee admission policy remains outside this pilot. |
| Dead city candidate | No event performs an early salvage transaction. | Missing. It should remain separate from the Phase 3 infrastructure batch because it needs its own casualty and equipment-risk contract. |
| Reactor state | No event checks reactor buildings or creates a cooling failure. | Missing. |

## Chain-depth review

The pilot has strong delayed-result depth in its transport, heating, shelter, harvest, city, archive, continuity, thaw, and second-winter families. Those chains carry a state target, record a branch flag before dispatch, resolve through state conditions, write durable memory, and clear the pending branch.

The Phase 1 and several Phase 2 regional entries are intentionally shorter. They establish regional voice and early choices, but they do not all return later. This is acceptable for the pilot and remains a future depth target.

The most important gap identified by the baseline review was infrastructure identity. The accepted hydroelectric, oil, and reactor rows had no live route, even though the engine exposes exact state buildings and resources for all three.

## Selected expansion

The selected reviewed tranche adds six manually authored blocks:

- `chaosx.fallout.22` and `.25`, Dam Ice Crisis and its delayed result
- `chaosx.fallout.26` and `.27`, Black Refinery Snow and its delayed result
- `chaosx.fallout.28` and `.29`, Cooling Pond Emergency and its delayed result

These routes are selected before the existing broad transport and clinic routes when the same Phase 3 state has the relevant infrastructure. Reactor takes precedence over dam, dam takes precedence over oil or refinery, and the existing transport and clinic order remains unchanged after those exact identities are exhausted. Country candidate selection still compares family priority, origin cycle, phase and pressure score, then state id. A higher-pressure transport state can therefore defeat a reactor state in another part of the same country.

This batch changes no monthly phase coefficient, population formula, Fallout grade coefficient, treaty policy, or world iteration. It uses the existing Air Winter ledgers, event cooldown, candidate ordering, state refresh, Deaths and fallout helpers, and pending-chain cleanup.

## Implementation disposition

The selected six blocks are live. The pilot contains 41 blocks, 119 options, and 118 effect-bearing options. Hydroelectric, oil or refinery, and reactor identities now have opening and delayed-result chains. The shared Phase 3 country memory still permits one ordinary Phase 3 identity chain per country in a campaign, so the three routes provide deterministic cross-playthrough breadth rather than three guaranteed incidents for every country.

## Deferred depth

The following accepted rows remain unresolved after this tranche:

- delayed seed-vault consequences
- tunnel schools for mountain capitals
- an early dead-city salvage chain
- refugee admission and identity consequences for island states
- state-specific heavy-industry routing beyond the broad heat chain

They require separate reviewed contracts and are not claimed by the Phase 3 infrastructure batch.
