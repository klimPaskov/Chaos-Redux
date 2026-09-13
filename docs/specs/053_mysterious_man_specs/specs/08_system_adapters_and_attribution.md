# 8. System Adapters and Attribution

## Integration model

Event 53 connects to other systems through bounded consequence adapters. It does not call another event's normal entry event and does not reproduce another owner's full logic inside the Event 53 file.

Each owner exposes two public surfaces for Event 53:

- a read-only validity trigger
- an apply adapter that accepts a locked Event 53 transaction and returns a receipt

The validity trigger and apply adapter remain in the owning system's files unless the owner delegates through an existing neutral public gateway.

## Event 53 request context

Every owner adapter receives a complete request context:

| Input | Purpose |
| --- | --- |
| Event 53 transaction ID | Prevent duplicate application and match receipts |
| Target country | The selected player country |
| Consequence package ID | Stable package identity |
| Active behavior tier | Baseline through Evolution III |
| Requested severity profile | Owner-safe scale request |
| Refusal count | Optional dynamic scaling input |
| Visit count | Optional dynamic scaling input |
| Origin mode | Event 53 refusal consequence |
| Suppress source firing | Mandatory source-event bookkeeping bypass |
| Suppress source opening presentation | Prevent normal source event or super-event opening |
| Preserve owner aftermath | Allow real owner processing and cleanup |
| Reserved targets | State, country, character, or compound targets when needed |

The owner may clamp requested severity to its own safe range. It cannot replace the selected package with another consequence.

## Existing neutral helpers

Event 53 should reuse the following public neutral helpers when their contracts fit:

- `call_natural_disaster`
- `remove_support_equipment_from_stockpile`
- `remove_motorized_equipment_from_stockpile`
- `remove_convoys_from_stockpile`
- `remove_trains_from_stockpile`
- `remove_infantry_equipment_from_stockpile`
- `remove_fuel_from_stockpile`
- `damage_buildings_in_random_states`
- `apply_state_population_loss_without_recruitable_manpower_gain`
- `apply_exact_state_civilian_population_loss`

The natural-disaster gateway remains neutral even though Event 013 owns the disaster runtime. Event 53 prepares the documented call inputs and receives the gateway outputs.

The stockpile helpers perform debits only. Event 53 remains responsible for amount calculation, affordability, package selection, receipts, and presentation.

The population-loss helpers must be used only by the system that owns the actual death transaction. Event 53 cannot remove population separately after an owner has already recorded the same deaths.

## Shared dynamic registry boundary

The following remain Event 53-owned and must not be added to `chaosx_dynamic_effects`:

- consequence pool construction
- package validity orchestration
- equal selection
- demand selection
- visit scheduling
- refusal attribution
- source-event bookkeeping suppression
- Event 53 transaction receipts
- legal-successor transfer
- Event 53 cleanup

A new neutral helper can enter the shared registry only when unrelated systems need the same behavior and the helper has no Event 53 lifecycle or selection semantics.

## Independence Wave adapter

The Independence Wave owner already has an indexed owner API and release ledger. Event 53 requires a dedicated bounded adapter that can:

- enumerate viable movements from the selected target
- reserve all state packages before release
- select one, several, or a maximum fracture set according to the requested package
- create viable country packages
- create forces, equipment, manpower, leaders, flags, focus content, claims, diplomacy, and wars where appropriate
- retain Event 53 origin
- leave Event 006 firing, weight, history, evolution, super-event, and terminal state untouched
- return released-country and state receipts

Different movement candidates are target variants inside the selected Event 53 package.

## Natural Disasters adapter

Event 53 uses `call_natural_disaster` as the stable country-scope gateway.

For a single-disaster package, Event 53 sets the origin mode, requested severity, target mode, and any required targets, then calls the gateway once.

For a several-disasters package, the Natural Disasters owner must expose a compound request mode or a bounded wrapper that:

- reserves distinct primary targets
- chooses compatible disaster families
- queues all jobs under one Event 53 transaction
- returns job counts and skipped-target receipts

Event 53 must not loop over disasters and call several unrelated normal openings.

## Famine adapter

The famine owner validates real food-security conditions. Event 53 can request pressure, incident registration, target count, and severity, but famine decides whether the request is valid.

The adapter must:

- use the famine namespace and active-state registry
- preserve Food Security, Food Reserves, and Relief Access behavior
- own gradual mortality
- use exact population loss and Deaths registration
- exchange survivor movement requests with Migration through versioned proof
- preserve famine decisions, missions, relief, concealment, and recovery where they apply
- return selected states and incident IDs

Event 53 does not create a separate flat famine modifier or direct famine deaths.

## Migration adapter

The migration owner validates displacement cause, origin, route, destination, reception, and settlement.

The adapter must:

- create real cohorts
- debit origin population once
- credit survivors once
- keep route deaths inside the transfer transaction
- create trapped people when borders block movement
- own internal displacement, cross-border flight, evacuation, transit, reception, return, and settlement
- return cohort, origin, destination, and movement receipts

Event 53 cannot create a generic national population loss and call it displacement.

## Disease adapter

The disease owner must expose an origin-safe request surface that can seed one or several outbreaks without firing a source event.

The adapter must own:

- agent selection inside the selected package
- state seeding
- intensity
- spread
- mortality
- containment
- cure or treatment interaction
- Air Cleanliness contribution
- state and country cleanup
- special-country or terminal-route suppression unless the selected Event 53 package explicitly and safely includes it

The ordinary disease-outbreak package can choose among valid ordinary agents after selection. Smallpox, plague, and multiple-epidemic packages have their own top-level ballots because their campaign identities are materially different.

## Intel Leaked adapter

Event 52 requires a bounded exposure adapter. The adapter must separate the intelligence crisis package from Event 52's normal firing lifecycle.

It should accept:

- target country
- normal or severe exposure profile
- duration profile
- foreign recipient eligibility
- Event 53 origin

It should return:

- recipient count
- exposure categories
- duration
- skipped recipients
- cleanup job proof

The adapter cannot record Event 52 as fired or trigger its normal opening presentation.

Until this adapter exists and passes source-bookkeeping tests, both Intel Leaked registry entries remain inactive.

## Great Embargo adapter

Event 50 requires a bounded embargo adapter. It owns:

- coalition selection
- participant validity
- diplomatic and economic pressure
- native embargo use when available
- non-DLC enforcement behavior
- duration
- participant cleanup
- target removal cleanup

The adapter receives Event 53 origin and suppresses Event 50 firing, history, pacing, and evolution.

Until this adapter exists, both embargo registry entries remain inactive.

## Random Civil War adapter

Event 021 or its shared civil-war framework must expose request profiles for:

- ordinary civil war
- multi-front civil war
- maximum civil fracture
- civil-war components inside compound packages

The adapter owns ideology, region, legal government, command split, states, forces, equipment, leaders, diplomacy, wars, and cleanup.

It must return the continuing legal-government proof so Event 53 preserves one target marker.

Until the framework exposes a safe origin-bypass adapter, Event 53 civil-war packages remain inactive.

## War-crisis adapter

The reusable war owner should support:

- one external war
- one border conflict
- multi-actor border crisis
- several neighboring wars
- compound war components

Validity must account for reachability, faction and subject relations, existing wars, truces, guarantees, access, capitulation, special Chaos exclusions, and minimum viable strength.

The adapter cannot create a fake attacker solely to satisfy the package.

## Military-fracture adapter

The military-fracture owner should support:

- baseline mutiny
- command fracture
- mass mutiny
- compound mutiny components

It owns unit selection, command actors, equipment transfer or destruction, depot seizure, rebel setup, and cleanup.

It must never duplicate units, equipment, characters, or Event 53 target markers.

## Character-assassination adapter

The character owner must enumerate safe eligible targets and remove exactly one selected character.

The adapter must protect:

- characters already removed or unavailable
- characters whose removal would break required engine roles
- duplicated character ownership
- active transfer or country transformation transactions
- protected scripted identities where no replacement path exists

Character selection happens after the assassination package receives its ballot.

## Occupation-revolt adapter

The occupation or resistance owner validates meaningful non-core or occupied territory. It owns target states, local actors, force packages, claims, resistance state, war form, and cleanup.

The adapter must distinguish a local uprising from an Independence Wave release and from a national civil war.

## Direct Event 53 packages

Event 53 can directly own packages that need no larger subsystem, including:

- government paralysis
- direct Stability and War Support collapse
- supported stockpile losses
- direct factory and infrastructure damage
- temporary industrial blackout
- multi-region sabotage when no shared owner exists
- a bounded diplomatic crisis when it does not duplicate Great Embargo
- nationwide no-attacker nuclear annihilation through approved shared destruction primitives

Direct packages still need idempotent transaction proof, dynamic scaling, receipts, Deaths integration where applicable, and cleanup.

## Origin and history separation

Every owner adapter must distinguish these records:

| Record | Allowed behavior |
| --- | --- |
| Event 53 History | One row for the original parent firing |
| Event 53 evolution history | One row for each actual enabled milestone |
| Event 53 visit ledger | Internal lifecycle data, not ordinary History rows |
| Owner operational ledger | Allowed when required for gameplay and cleanup |
| Source event History | Forbidden for borrowed packages |
| Source event fired count | Forbidden |
| Source event pacing | Forbidden |
| Source cluster record | Forbidden |
| Source super-event opening | Forbidden |
| Source world-end progression | Forbidden |

## Chaos and global-system attribution

Event 53 does not duplicate generic Chaos sources.

Wars, annexations, deaths, contamination, nuclear use, and other ordinary global consequences change Chaos through their established systems.

Evolution activation gives zero Chaos.

The first appearance and payment give zero Chaos.

Refusal consequences use established Chaos sources for wars, annexations, deaths, contamination, nuclear use, and other tracked outcomes. A direct Event 53 package can add an event-specific Chaos change only when its accepted package design names a concrete consequence that no existing source records. The implementation must not add Chaos twice for the same political collapse, deaths, nuclear destruction, contamination, war, or fracture.
