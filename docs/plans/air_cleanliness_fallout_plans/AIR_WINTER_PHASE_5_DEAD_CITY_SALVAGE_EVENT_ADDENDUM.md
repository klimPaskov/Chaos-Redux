# Air Winter Phase 5 Dead-City Salvage Event Addendum

## Review status

Accepted for implementation after independent engine, route, identifier, and improvement-loop review. The final contract below resolves the review disagreement in favor of Phase 5 because Phase 5 is the first sustained Ash Winter phase, while Phase 4 only begins category decay. Implementation must preserve every invariant in this document.

## Source and scope

This addendum implements the Dead city candidate and Night salvage row from `docs/specs/air_cleanliness_fallout_specs/specs/baseline/02_winter_mapmode_and_state_effects.md`.

The tranche is limited to one manually authored opening block, one delayed result block, deterministic state identity, equipment costs and yields, Deaths integration, repairable building damage, one bounded high-Chaos altered-return result, state and country memory, AI, cleanup, localisation, a dedicated Fallout-owned report image, and engine-sensitive proof.

It does not create the post-Fallout Dead City Permit institution, numerical Scrap, a new scheduler family, a periodic callback, a country or state scan, a Fallout grade, a Fallout request gate, or a successor package.

## Event ids and route order

The opening block uses `chaosx.fallout.47`. The delayed result uses `chaosx.fallout.48`. Both suffixes are free in the dedicated Fallout file. Suffix `.49` remains unallocated. The reserved living-world suffixes `100` through `126` remain untouched.

Within the unseen Phase 5 selector, the state-local order is:

1. ruined major-urban salvage candidate
2. generic Phase 5 city
3. low-shelter abandonment
4. archive convoy

The route remains in the ordinary-phase family and consumes the shared `air_winter_event_seen_phase_5` receipt. It does not become a supplemental incident and adds no candidate family, marker, or second country receipt.

A dedicated same-phase score bonus of 131 makes a valid ruined major-urban state win over another Phase 5 state owned by the same country. The existing phase weight of 1,000 still lets a genuine Phase 6 state win. The bonus changes no cross-phase ordering.

## Exact pre-Fallout identity

The route is a ruined major-urban salvage candidate. It is not an exact Fallout dead city. `fallout_state_grade = dead_city` does not exist until Fallout grading, after Air Winter event dispatch is disabled.

The state qualifies only when every condition below is true:

- Air Winter is active and the current state phase is exactly Phase 5.
- The state is owned and controlled by the same country. Enemy occupation blocks the route.
- The recorded original category is exactly `large_city`, `metropolis`, or `megalopolis`.
- `air_winter_last_building_loss_date` exists, proving that the Air Winter damage transaction previously damaged a building in the state.
- At least one current damaged level exists among infrastructure, civilian factories, military factories, air bases, dockyards, supply nodes, or railways.
- The state does not have the durable exhausted-site memory.

The original category uses an exact three-case disjunction. A lower-bound comparison is invalid because `large_island` sorts above the urban values. Current state category is not required. A former metropolis that degraded to a town remains a truthful ruined urban candidate.

The persistent loss date is used instead of the short-lived recent-loss flag. The current damaged-level test prevents an already repaired site from qualifying. Raw Building Damage Pressure is not an identity gate because the monthly building transaction spends its threshold before event candidate capture.

## Opening conflict

`chaosx.fallout.47` presents three competing authorities in the same damaged city:

- municipal engineers want one surveyed and braced service route
- military quartermasters want the buried depots opened immediately
- fire, rail, and utility crews want district salvage licenses

The labels below describe mechanics and are not final localisation.

### Survey and brace the service route

Display-time and click-time requirements:

- at least 500 available Manpower
- at least 30 Support Equipment
- at least 10 Motorized Equipment

Payment and immediate state changes:

- spend 500 Manpower, 30 Support Equipment, and 10 Motorized Equipment
- Adaptation plus 4
- Reclamation plus 2
- Exposure plus 1
- Building Damage Pressure plus 8

The opening writes the survey branch and matching state and country policy memory.

### Seize the military depots

Display-time and click-time requirements:

- at least 1,000 available Manpower
- at least 120 Infantry Equipment
- at least 20 Motorized Equipment
- at least 1,000 Fuel

Payment and immediate state changes:

- spend 1,000 Manpower, 120 Infantry Equipment, 20 Motorized Equipment, and 1,000 Fuel
- Adaptation plus 2
- Exposure plus 3
- Building Damage Pressure plus 15

The opening writes the military branch and matching state and country policy memory.

### License the district crews

This route has no payable resource gate, so every valid popup retains one executable choice. Its opportunity cost is the loss of central control and the lower expected equipment yield.

Immediate state changes:

- Reclamation plus 4
- Exposure plus 2
- Building Damage Pressure plus 8
- national Stability minus 0.005

The opening writes the licensed-crews branch and matching state and country policy memory.

All three valid choices clear an older dead-city pending branch and policy record, apply their exact costs and ledger changes once, write exactly one branch, refresh the state to bind the original owner, refresh the 46-day country cooldown, and schedule `chaosx.fallout.48` after 30 days.

## Deterministic delayed results

The delayed event has ten mutually exclusive acknowledgement options. Survey, military, and licensed branches each have success, partial recovery, and disaster. A tenth altered-return option replaces an otherwise valid disaster only under the exact fictional high-Chaos cause gate.

No random list, MTTH, hidden roll, or dynamic equipment type is used.

### Survey success

Success requires all of these live result conditions:

- Phase 5 or lower
- Adaptation at least 35
- Reclamation at least 30
- Exposure no more than 60
- Building Damage Pressure no more than 65

Result:

- gain 60 `support_equipment_1`
- gain 20 `motorized_equipment_1`
- gain 3 `train_equipment_1`
- Reclamation plus 4
- Building Damage Pressure minus 15

### Survey partial recovery

Partial recovery requires that success is false and all of these conditions are true:

- Phase 5 or lower
- Exposure no more than 72
- Building Damage Pressure no more than 80
- Adaptation at least 25 or Reclamation at least 20

Result:

- gain 30 `support_equipment_1`
- gain 10 `motorized_equipment_1`
- civilian loss equal to 0.00005 of the remaining state population through the Deaths contract
- Exposure plus 1

### Survey disaster

This is the exact inverse of survey success and survey partial recovery after the altered-return gate is excluded.

Result:

- civilian loss equal to 0.00015 of the remaining state population through the Deaths contract
- Exposure plus 3
- Building Damage Pressure plus 15
- repairable damage of 0.50 to operational infrastructure when one level remains
- national Stability minus 0.01

### Military success

Success requires all of these live result conditions:

- Phase 5 or lower
- Adaptation at least 35
- Exposure no more than 65
- Building Damage Pressure no more than 65

Result:

- gain 300 `infantry_equipment_1`
- gain 30 `support_equipment_1`
- gain 25 `motorized_equipment_1`
- civilian loss equal to 0.00010 of the remaining state population through the Deaths contract
- Reclamation plus 2

### Military partial recovery

Partial recovery requires that success is false and all of these conditions are true:

- Phase 5 or lower
- Adaptation at least 20
- Exposure no more than 80
- Building Damage Pressure no more than 85

Result:

- gain 140 `infantry_equipment_1`
- gain 10 `support_equipment_1`
- gain 10 `motorized_equipment_1`
- civilian loss equal to 0.00020 of the remaining state population through the Deaths contract
- Exposure plus 2
- Building Damage Pressure plus 8

### Military disaster

This is the exact inverse of military success and military partial recovery after the altered-return gate is excluded.

Result:

- civilian loss equal to 0.00035 of the remaining state population through the Deaths contract
- Exposure plus 4
- Building Damage Pressure plus 25
- repairable damage of 0.50 to one operational military factory, otherwise operational infrastructure
- national Stability minus 0.02

### Licensed-crews success

Success requires all of these live result conditions:

- Phase 5 or lower
- Reclamation at least 35
- Exposure no more than 65
- Building Damage Pressure no more than 70

Result:

- gain 45 `support_equipment_1`
- gain 12 `motorized_equipment_1`
- gain 2 `train_equipment_1`
- civilian loss equal to 0.00005 of the remaining state population through the Deaths contract
- Reclamation plus 4

### Licensed-crews partial recovery

Partial recovery requires that success is false and all of these conditions are true:

- Phase 5 or lower
- Reclamation at least 25
- Exposure no more than 75
- Building Damage Pressure no more than 85

Result:

- gain 20 `support_equipment_1`
- gain 5 `motorized_equipment_1`
- civilian loss equal to 0.00015 of the remaining state population through the Deaths contract
- Exposure plus 2

### Licensed-crews disaster

This is the exact inverse of licensed-crews success and partial recovery after the altered-return gate is excluded.

Result:

- civilian loss equal to 0.00025 of the remaining state population through the Deaths contract
- Exposure plus 4
- Building Damage Pressure plus 15
- repairable damage of 0.50 to one operational civilian factory, otherwise one operational military factory, otherwise operational infrastructure
- national Stability minus 0.01

### Fictional altered return

The altered-return option is available only when all of these conditions are true:

- the selected branch would otherwise resolve as its disaster
- the frozen world is at the final Chaos tier of at least 1,000
- the state has the active `nuclear_fallout_state` modifier and positive live nuclear fallout intensity
- the state also has live chemical contamination or an active biological-contamination flag

This is fictional high-Chaos content. It is not an inference that ordinary radiation produces rapid mutation. The gate affects only this result and never the Fallout request, transition, or state grade.

Result:

- gain 20 `support_equipment_1`
- gain 5 `motorized_equipment_1`
- civilian loss equal to 0.00025 of the remaining state population through the Deaths contract
- Adaptation plus 8
- Exposure plus 3
- Disease Pressure plus 4
- national Stability minus 0.02
- write distinct altered-return state and country memory

Every result marks the site exhausted. A later owner cannot farm another equipment yield from the same state.

## AI contract

The opening base weights are 60 for the surveyed route, 10 for military seizure, and 30 for licensed crews. Every modifier below is multiplicative and all satisfied modifiers stack.

Survey success is plausible before the choice only when Adaptation is at least 31, Reclamation at least 28, Exposure no more than 59, and Building Damage Pressure no more than 57. Those values translate exactly through the opening changes to the delayed success thresholds.

Military success is plausible before the choice only when Adaptation is at least 33, Exposure no more than 62, and Building Damage Pressure no more than 50.

Licensed-crews success is plausible before the choice only when Reclamation is at least 31, Exposure no more than 63, and Building Damage Pressure no more than 62.

Each option doubles its weight when its exact plausibility trigger passes and halves its weight when it fails. Surveyed salvage receives one additional factor of 2 only when the country is at peace and has a democratic or neutral government. Military seizure receives separate factors of 2 for a fascist government, being at war, and War Support at or above 0.65. Licensed crews receives separate factors of 2 for a communist or democratic government and Stability at or below 0.45, while being at war applies a factor of 0.5.

The delayed event contains no AI chance roll. Its exact branch, live ledgers, and altered-return gate expose one option.

## Transaction, memory, and cleanup

The three branch flags are exclusive. Each branch trigger requires its own flag and rejects the other two. The result trigger accepts only the exact exclusive disjunction. Generic reconciliation cancels a row with more than one branch.

Every opening performs this sequence:

1. revalidate regular country and state targets, Phase 5 identity, exhausted-site absence, and payable resources
2. clear older dead-city pending, policy, and outcome memory
3. apply the exact payment and immediate consequences
4. write one branch and one state and country policy memory
5. refresh the state so the generic pending marker and original owner are bound
6. refresh the country cooldown
7. schedule the result after 30 days

The result does not recheck Phase 5, original category, the loss receipt, or current damaged levels. Repairs and phase movement during the delay must affect the deterministic outcome without stranding a committed transaction.

Each result rechecks the generic owner-bound target contract, continued control by the stored owner, the exclusive branch, and the exact outcome predicate. It grants equipment once, applies Deaths and repairable damage where required, clears all three branch flags, writes one result memory, marks the state exhausted, and refreshes the state. Generic reconciliation then removes the pending marker and stored owner.

`air_winter_event_cancel_pending_chain` clears all three branches. The dedicated `on_state_control_changed` hook sends any live dead-city branch through the shared reconciliation effect on the exact control-change edge. Monthly reconciliation remains the ownership and malformed-ledger backstop. Ownership loss, control loss, invalid owner, state reset, active Fallout, or active Fallout transition cannot leave a result able to mutate the frozen Fallout row. Durable policy and result memories remain until the normal Air Winter state or country reset. A later valid opening after an interrupted chain replaces the old policy record before writing the new branch.

The Fallout snapshot captures canonical Air Winter values and live building damage before it cancels pending event branches. It adds no new snapshot schema field for this chain.

## Engine-sensitive proof basis

Static implementation proof must record these surfaces:

- `damaged_building_level@type` in state scope for current damaged levels
- the persistent Air Winter building-loss receipt and original-category ledger
- `non_damaged_building_level` in state scope before repairable failure damage
- `damage_building` in state scope
- country-scope `add_equipment_to_stockpile` with fixed concrete equipment types and constant amounts
- exact negative equipment payments through existing helpers
- state-scope Deaths requests through `air_winter_event_apply_deaths`
- regular event-target propagation into a delayed country event
- exact branch cancellation before a Fallout transition can advance

Static source review cannot prove live popup behavior, delayed target retention, equipment stockpile display, building repair behavior, AI frequency, save recovery, or multiplayer behavior. Hearts of Iron IV must not be launched for this tranche.

## Assets and localisation

Both blocks use `GFX_report_event_air_winter_dead_city_salvage`.

The final DDS lives at `gfx/event_pictures/fallout/air_winter/report_event_air_winter_dead_city_salvage.dds`. The dedicated fictional documentary scene shows night crews crossing an ice and ash covered service street below collapsed urban facades, with lamps, braces, hand tools, and a guarded truck. It contains no creature, logo, lettering, zombie asset, audio, sprite, file, or path.

Localisation must name frozen service tunnels, damaged depots, unstable floors, utility crews, precise recovered equipment categories, and recorded casualties. Government-aware authority terms remain dynamic. The altered-return text describes an impossible social and bodily event without attributing it to ordinary radiation.

## Expected implementation totals

The existing pilot contains 48 Air Winter blocks, 146 options, 145 effect-bearing options, and 51 delayed schedules.

This tranche adds:

- 2 manually authored blocks
- 13 options
- 13 effect-bearing options
- 3 delayed schedules

The expected post-tranche totals are 50 blocks, 159 options, 158 effect-bearing options, and 54 delayed schedules.

## Review disposition

The engine review required a pre-Fallout candidate name, exact original-category cases, current damaged-level evidence, concrete equipment rather than unimplemented Scrap, state-scope Deaths, and owner-bound delayed cleanup.

The route and identifier review accepted `.47` and `.48`, the ordinary-phase family, shared Phase 5 receipt, and Phase 5 precedence. Its recommendation to use the persistent Air Winter building-loss receipt replaces the earlier raw-pressure proposal.

The improvement-loop proposal supplied the three-authority conflict, equipment transactions, three-tier results, state and country memories, and dedicated asset direction. Its Phase 4 placement is not adopted because the later route audit established Phase 5 as the first sustained heavy-damage fit. Its proposed altered-contact omission is replaced by the narrow high-Chaos gate above, which follows the user's explicit fictional-mutant boundary and existing mixed-contamination evidence.

No numerical Scrap substitute, generic Phase 5 art reuse, ordinary-radiation mutation claim, new iterator, or post-Fallout completion claim is approved.
