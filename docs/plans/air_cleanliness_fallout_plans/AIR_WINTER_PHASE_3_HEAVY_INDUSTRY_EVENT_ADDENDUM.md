# Air Winter Phase 3 Heavy Industry Event Addendum

## Review status

Accepted after independent engine, numerical-balance, transaction, and context-free final review. No actionable design finding remains. Implementation must preserve every invariant in this document.

## Source and scope

This addendum implements the Coal or heavy industry and Furnace rationing row from `docs/specs/air_cleanliness_fallout_specs/specs/baseline/02_winter_mapmode_and_state_effects.md`.

The tranche is limited to one manually authored Phase 3 opening block, one delayed result block, state identity, deterministic AI, ledger effects, Deaths integration, repairable building damage, temporary state production loss, memory, cleanup, localisation, and proof. It adds no scheduler family, country or state scan, periodic callback, Fallout numerical formula, treaty policy, scenario row, or post-Fallout consumer.

## Event ids and route order

The opening block uses `chaosx.fallout.36`. The delayed result uses `chaosx.fallout.37`. Both suffixes are free in the dedicated Fallout file. The reserved living-world suffixes `100` through `126` remain untouched.

After an unseen Phase 3 state becomes the country's ordinary event candidate, state-local route selection uses this order:

1. reactor state
2. hydroelectric state
3. oil or refinery state
4. coal or heavy-industry state
5. transport state
6. clinic and heat state

Heavy industry precedes transport because industrial states commonly have infrastructure or railways and would otherwise never reach their identity route. Reactor, dam, and oil or refinery identities retain precedence because their accepted chains depend on rarer building and resource surfaces.

The country scheduler remains unchanged. It still compares family priority, origin cycle, frozen phase and pressure score, then state id. The shared `air_winter_event_seen_phase_3` memory still permits one ordinary Phase 3 chain per country.

## State identity

A state qualifies when either of these conditions is true:

- it has a positive amount of coal
- it has at least four operational civilian and military factories in total

Coal uses the direct state-scoped `coal` resource comparison. Operational factories use `non_damaged_building_level` for `arms_factory` and `industrial_complex`.

The combined minimum is expressed as a deterministic five-case ladder:

- at least four military factories
- at least four civilian factories
- at least three military factories and one civilian factory
- at least two military factories and two civilian factories
- at least one military factory and three civilian factories

All comparison thresholds are script constants. No installed but fully damaged factory contributes to the identity.

The disjunction is required by the accepted source row, which names coal or heavy industry. A coal-only state is therefore an intended identity rather than an expansion of scope. The opening uses a coal-workings description when coal is present and a factory-hall description otherwise. Final choice text must remain truthful for collieries, coke ovens, foundries, and machine halls instead of assuming that every eligible state has the same building mix.

## Opening contract

`chaosx.fallout.36` has two choices. The labels below describe mechanics and are not final localisation.

### Full furnace shifts

The state keeps its current factory and coal output. The opening applies:

- Adaptation plus 2
- Exposure plus 2
- Building Damage Pressure plus 15
- civilian loss equal to 0.00015 of the remaining state population through the existing Deaths contract
- national Stability minus 0.01

The Stability change is a consequence, not a payable cost. The option remains available at low Stability and the engine clamps the resulting national value normally.

The result arrives after 30 days. Full shifts succeed when Adaptation is at least 40 and Building Damage Pressure is no more than 55 at result time.

Success applies:

- Adaptation plus 4
- Reclamation plus 2
- Building Damage Pressure minus 8

Failure applies:

- repairable damage of 0.50 to one operational military factory, otherwise one operational civilian factory, otherwise local infrastructure
- Exposure plus 2
- Building Damage Pressure plus 25
- further civilian loss equal to 0.00010 of the remaining state population through the Deaths contract
- national Stability minus 0.005

The fixed damage order gives a coal-only state a valid physical failure surface when it has no operational factory. Building Damage Pressure and civilian loss still apply if no damageable infrastructure remains.

### Full shutdown

The opening applies:

- Adaptation plus 2
- Exposure minus 3
- Building Damage Pressure minus 15
- a temporary industry modifier with `local_factories = -0.50` when at least one operational civilian or military factory remains
- a separate temporary coal-workings modifier with `state_resources_coal_factor = -0.25` when the state has positive coal

Both modifiers last 31 days. A factory-only state receives only the factory penalty. A coal-only state receives only the coal penalty. A state with both identities receives both because the order closes both the furnace halls and the coal workings. The result arrives after 30 days. Its immediate effect removes both modifiers from a valid shutdown branch when the report is delivered, even if a human leaves the result popup unacknowledged. Each result option removes both modifiers again as an idempotent guard before refreshing the state. Automatic expiry prevents a lost or invalid result from leaving a permanent production penalty.

The fixed restart result applies:

- Reclamation plus 2
- Exposure minus 1
- Building Damage Pressure minus 8

This route avoids immediate civilian loss and national Stability loss. Its cost is the disclosed factory and coal-output interruption.

## AI contract

The full-shift route uses a base weight of 30. The shutdown route uses a base weight of 60.

The AI treats full shifts as mechanically plausible only when the pre-choice state has Adaptation at least 38 and Building Damage Pressure no more than 40. Those boundaries translate exactly through the opening's Adaptation gain of 2 and Building Damage Pressure gain of 15 to the result thresholds of 40 and 55.

Full shifts gain weight for a country at war, a fascist government, high War Support, and a state that passes the plausibility trigger. They lose weight when the state fails the plausibility trigger or national Stability is low.

Shutdown gains weight for a country at peace, a democratic or communist government, low national Stability, and a state that fails the full-shift plausibility trigger. Government and war weights remain separate from the state-ledger test, so ideology cannot make an implausible delayed result certain.

The delayed result exposes exactly one valid option for the stored branch and deterministic outcome. AI resolution therefore follows the same state test as human resolution.

## Transaction and cleanup

Each opening choice performs this sequence:

1. revalidate the regular country and state targets and the heavy-industry identity at click time
2. clear both furnace branch flags, both shutdown modifiers, and all five older durable furnace memories
3. apply the exact state and country consequences
4. write exactly one furnace branch flag and one opening memory flag
5. refresh the state so the generic pending-result flag and original country owner are bound
6. refresh the country cooldown
7. schedule `chaosx.fallout.37` after 30 days

The result trigger requires valid regular targets and exactly one furnace branch through an exclusive branch test. A row with both branch flags is invalid and generic reconciliation cancels it. Each result option rechecks the generic target contract and its exclusive branch. The full-shift success and failure click guards also repeat the exact Adaptation and Building Damage Pressure predicate or its negation. Every option removes both shutdown modifiers where present, clears both branch flags, writes one result memory, and refreshes the state. The generic reconciliation then clears the pending-result flag and stored owner because no branch remains.

`air_winter_event_cancel_pending_chain` removes both shutdown modifiers and both furnace branch flags. Ownership loss, invalid owner, state reset, active Fallout, or an active Fallout transition therefore cannot leave a pending production penalty or allow a delayed result to mutate a frozen Fallout row.

The state-memory reset clears every furnace opening and result memory. A later owner that has not seen its ordinary Phase 3 event can receive the route without inheriting contradictory outcome memory.

No temporary or global event target is added. The chain uses the regular targets already saved by the bounded Air Winter scheduler.

## Engine-sensitive proof basis

Static implementation proof must record these surfaces:

- direct state resource comparison for coal identity
- `non_damaged_building_level` in state scope for operational factory identity
- `damage_building` in state scope for repairable factory or infrastructure damage
- `add_dynamic_modifier` and `remove_dynamic_modifier` in state scope
- `local_factories` as a state modifier
- `state_resources_coal_factor` as a generated state resource modifier
- regular event-target propagation into a delayed event fired from the opening chain
- exact cancellation before the Fallout snapshot can advance

The opening event and click guard recheck Phase 3 and the original disjunctive identity. The delayed result does not recheck Phase 3, coal, or the four-factory threshold because legitimate state changes during the delay must not invalidate an owner-bound result.

The official installed documentation and a vanilla precedent must be cited for every surface in the implementation proof. Static source review cannot prove live popup behavior, delayed target retention, AI choice frequency, modifier arithmetic, save recovery, or multiplayer behavior. Hearts of Iron IV must not be launched for this tranche.

## Assets

Both blocks use `GFX_report_event_air_winter_phase_3`, the dedicated Air Winter Phase 3 report image registered in `interface/fallout_consolidated.gfx`. The asset manifest must map `.36` and `.37` to that sprite. No new art, sprite, audio, or path is required.

## Excluded surfaces

This tranche does not create a coal stockpile, alter Air Contamination, change Fallout grading or survival, consume the post-Fallout seed ledger, add a heavy-industry successor, create a treaty project, or change the manual Fallout scenario. It does not approve any fallback.

## Review disposition

The engine review accepted the direct coal comparison, exact four-factory partition ladder, route order, typed ids, two conditional state modifiers, long threshold comparisons, and owner-bound result. It identified the valid edge where no operational factory or infrastructure remains at failure time. The accepted behavior is to apply no physical building damage in that rare state while retaining the disclosed deaths, Exposure, Building Damage Pressure, and Stability consequences. No substitute damage surface is invented.

The balance review accepted the two-choice structure, all casualty and ledger values, the exact AI inverse, the 0.50 repairable damage amount, and the split modifier values. It recommended making coal secondary to factory identity. That recommendation is not adopted because the accepted source row explicitly requires coal or heavy industry. Coal-only presentation and the conditional coal-workings penalty keep the route mechanically and textually valid without creating a coal stockpile.

The transaction review accepted delivery-time immediate removal, 31-day automatic expiry, two conditional modifier ids, stability loss as a consequence, repeated click guards, and the owner-bound delayed result. It requires exclusive branch proof, pre-opening replacement cleanup, idempotent modifier removal, and the exact 46-day cooldown refresh immediately before each 30-day schedule. Those requirements are part of this addendum.

The final context-free review approved the complete contract without an actionable finding. Its acceptance remains static and does not claim live popup timing, multiplayer behavior, save recovery, or delayed-target retention.
