# Event 53 Adapter Contract Matrix

## Owner-level matrix

| Owner or system | Event 53 packages | Existing supplied evidence | Required adapter work | Source bookkeeping isolation | Receipt and cleanup owner |
| --- | --- | --- | --- | --- | --- |
| Event 53 lifecycle | Targeting, pacing, demands, direct packages, selection | Event-owned orchestration is required by dynamic-effect registry rules | Implement complete Event 53 owner files | Native Event 53 lifecycle | Event 53 |
| Shared stockpile debit helpers | Equipment, fuel, trains, convoys, payment demands | Public debit helpers are documented | Add amount calculation, affordability, origin, idempotence, and receipts | No source event involved | Event 53 |
| Shared building-damage helper | Factory and some infrastructure damage | Public helper is documented | Add target profiles, state receipts, death ownership, and package scale | No source event involved | Event 53 or industrial owner |
| Exact population-loss helpers | Nuclear and other real death transactions | Public exact population helpers are documented | Use only through the system that owns the actual loss | No duplicate Deaths entry | Calling death owner |
| Event 013 Natural Disasters | Single and several disasters | `call_natural_disaster` is a documented public gateway | Add Event 53 origin profile and a multi-job wrapper for several disasters | Event 013 normal firing and opening remain untouched | Event 013 |
| Event 006 Independence Wave | One release, several releases, total fracture, armed release compound | Owner API is indexed and the event is marked Needs Testing | Add Event 53 request profiles, frozen candidate sets, origin bypass, target retention, and receipts | Event 006 fired count, cluster, evolution, super-event, and terminal routes remain untouched | Event 006 |
| Famine runtime | Famine pressure, catastrophic famine, disease-food compounds | Owner API is indexed and mechanics are documented | Add proof-carrying Event 53 severity requests and receipts | No separate source event firing | Famine |
| Migration runtime | Displacement, mass displacement, humanitarian compounds | Owner API is indexed and mechanics are documented | Add Event 53 origin requests, exact cohort proofs, and receipts | No retired immigration event recreation | Migration |
| Disease runtime | Ordinary outbreak, smallpox, plague, multiple epidemics, compounds | Disease mechanics are referenced across supplied guides | Add bounded origin-safe seeding adapters and source-event suppression | No automatic event evolution, special country, super-event, or terminal route | Disease or plague owner |
| Event 52 Intel Leaked | Normal and severe intelligence exposure, compounds | Catalog status is To Be Reworked | Rework source system and expose a bounded Event 53 adapter | All Event 52 firing, history, weight, evolution, opening, and terminal state suppressed | Event 52 |
| Event 50 Great Embargo | Normal and severe embargo, compounds | Catalog status is To Be Reworked | Rework source system and expose a DLC-aware bounded adapter | All Event 50 firing, history, weight, evolution, opening, and terminal state suppressed | Event 50 |
| Event 021 Random Civil War | Ordinary, multi-front, maximum fracture, compounds | Catalog status is To Be Reworked | Rework source framework and expose continuing-government proof | All Event 021 firing, history, weight, evolution, opening, and terminal state suppressed | Event 021 or shared civil-war owner |
| War crisis | Border conflict, external war, multi-actor crisis, several wars, compounds | No complete adapter contract appears in supplied registries | Create reusable bounded actor, access, and conflict resolver | No source event firing unless a named owner later exists | War crisis owner |
| Military fracture | Mutiny, command fracture, mass mutiny, compounds | No complete adapter contract appears in supplied registries | Create reusable unit, command, depot, and target-retention owner | No source event firing unless a named owner later exists | Military fracture owner |
| Political crisis | Stability, War Support, strike, coup, hostile movement | Direct and reusable ownership can be split during implementation | Implement direct packages or bounded shared adapters | No false source event records | Event 53 or political owner |
| Character crisis | Assassination | No safe adapter appears in supplied registries | Create eligible-character and protected-role adapter | No source event firing | Character owner |
| Occupation and resistance crisis | Occupation revolt, separatist uprising | No complete Event 53 adapter appears in supplied registries | Create state, actor, force, war, and cleanup adapters | No source event firing | Occupation or uprising owner |
| Nuclear, Deaths, fallout, Air Cleanliness | Nationwide annihilation | Shared population and Air Cleanliness mechanics are documented | Create no-attacker national strike adapter with exact state ledger | No source nuclear event firing or false Condemnation | Event 53 plus each shared subsystem |

## Mandatory adapter inputs

Every adapter receives:

- Event 53 transaction ID
- selected target country
- package ID
- behavior tier
- requested severity profile
- Event 53 origin token
- source-firing suppression proof
- reserved targets where required

## Mandatory adapter outputs

Every adapter returns:

- accepted or rejected result
- package ID
- transaction ID
- resolved targets
- skipped targets and reasons
- delayed-job count
- attribution mode
- cleanup owner
- completion or queued state

## Adapter activation gate

A package adapter remains inactive until all of these pass:

- validity and apply contracts agree
- one complete transaction succeeds
- target change and invalidation cases are tested
- duplicate call is idempotent
- save and reload preserves state
- source event bookkeeping remains unchanged
- owner cleanup runs
- probability inspection shows one Event 53 ballot
