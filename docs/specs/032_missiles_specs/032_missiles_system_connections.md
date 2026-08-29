# Event 32 system connections

## Connection rule

Event 32 owns missile-program progression, operational missile reserve, launch-state records, conventional missile operations, missile guidance failures, missile command crises, and missile retaliation incidents.

Other systems retain ownership of their own payloads, countries, terminal routes, events, and shared ledgers.

A connection should use a narrow helper or adapter. Event 32 must not copy another system's logic into its own files.

## Event 5: Soviet Collapse

### Required bridge

Soviet Collapse can divide a country that owns missile sites, reserves, nuclear payloads, and prepared operations.

The Event 5 release transaction should call an Event 32 succession helper after state allocation is frozen and before final military cleanup.

The helper must:

- identify Event 32 launch states in each successor package
- transfer physical site control
- mark inherited sites compromised
- split ordinary missile reserve by site capacity and central-command share
- preserve exact total reserve
- assign reduced Command Control to successor programs
- cancel or reassign prepared operations
- create site-resolution decisions
- keep Event 23 nuclear payload ownership separate
- raise Rogue Launch Commands pressure when that evolution is active
- avoid creating an Event 32 random-event history row

### Soviet central-government choices

When the Soviet government still controls the codes or central reserve, Event 5 or Event 23 may allow it to:

- remove payloads before release
- scuttle a site
- threaten a breakaway
- negotiate custody
- retain remote control where a route explicitly supports it

Event 32 provides the physical and command records. Event 5 and Event 23 decide the political route.

## Event 6: Independence Wave

A released country may inherit a launch state.

Required behavior:

- use the Event 32 inherited-site helper
- do not give every released country a missile program automatically
- initialize a program only when it inherits a site or a separate Event 32 firing reaches it
- preserve reservation and package rules from Event 6
- avoid transferring a site to two countries
- create no duplicate reserve
- block site use until the new country resolves technology and command access

The Event 6 allocator should treat an active launch state as strategic infrastructure during transfer validation.

## Event 13: Natural Disasters

Natural disasters can damage:

- launch sites
- roads and rail access
- command centers
- warning systems
- reserve storage

Event 13 remains the owner of disaster targeting, delayed impacts, deaths, and aftermath.

Event 32 should expose a narrow state-damage adapter that Event 13 may call after a valid disaster hits a launch state.

Possible results:

- readiness loss
- capacity loss
- site damage
- reserve destruction
- guidance backlog
- false-warning pressure
- repair mission

A disaster does not activate an Event 32 evolution by itself.

## Event 16: Brilliant Scientist

The current repository already calls `brilliant_scientist_record_missile_crisis` from the Event 32 country report.

The rework must preserve this bridge.

Recommended call point:

- after the active Kruger host receives its first successful Event 32 program transaction
- before the first report option finishes
- only when the existing Event 16 helper gates permit it

Event 32 must not duplicate:

- mandate changes
- dependence changes
- exposure changes
- personal character history
- project history

Advanced Event 16 technologies may affect Event 32 guidance, command, or range only through explicit compatible adapters.

The Event 32 baseline does not grant Kruger technology.

## Event 21: Random Civil War

Event 21 should call the Event 32 civil-war split helper when the selected country has a missile program.

The helper must:

- follow site control
- split reserve without duplication
- lower both sides' Command Control
- mark frontier sites compromised
- clear prepared operations
- create emergency site actions
- raise Rogue Launch Commands pressure
- preserve payload custody through owning systems

A civil war involving a country with no Event 32 program receives no missile content.

## Event 23: Soviet Nuclear Bombs

Event 23 owns:

- Soviet nuclear technology grant
- initial 100-bomb arsenal
- Soviet threat and development decisions
- Soviet political use during collapse

Event 32 owns:

- missile delivery integration after Special Warheads
- launch-state and reserve requirements
- guidance and command risk
- exact missile operation

A Soviet nuclear missile launch must consume:

- Event 32 operational missiles
- Event 23 or shared nuclear stockpile
- Event 32 launch capacity
- Event 32 readiness and command cost

Then it calls the shared nuclear consequence route.

Event 32 must not grant nuclear bombs to countries merely because they have missiles.

## Event 27: Doctrine Research

No automatic bridge is required.

A future missile-doctrine family can use Event 32 profile and readiness hooks only after a separate accepted design. Event 32 should not grant land, air, or naval doctrine progress.

## Event 28: Asteroid Incoming

No direct mechanic bridge is required.

Both systems may use strategic impact visuals, but Event 32 must not use asteroid impact logic or record a missile strike as an asteroid.

## Event 29: Riches Found

No required direct bridge.

A Riches Found state may become a strategic industrial target if it contains valuable factories, infrastructure, or resources. Event 32 uses ordinary target scoring. It should not know the hidden Riches Found evolution state unless a separate cross-event design is accepted.

## Event 52: Fuel Shortage and related fuel crises

Fuel shortage should reduce:

- replenishment output
- readiness restoration
- launch preparation
- extended-range viability

The bridge should read real fuel stockpile and existing fuel-crisis modifiers.

Event 32 should not create a separate global fuel-crisis system.

## Event 76: USA Tests Weapons

Event 76 remains a separate testing event.

Possible Event 32 bridge after Event 76 is reworked:

- validated test data gives a temporary guidance benefit
- test accident creates readiness or command pressure
- successful test reduces the next maintenance cost
- public testing improves attribution or deterrence
- failed testing can provide an Unreliable Guidance incident seed

The bridge should call Event 32 helpers. Event 32 should not absorb Event 76's event identity, target incident, or news.

## Other war and conflict events

Event 4 Random War, Event 11 Secret Alliance, faction events, and ordinary wars provide targets and strategic conditions.

Event 32 responds through ordinary war-state and enemy validation. It does not need event-specific target code for every war creator.

## Special chaos countries

The shared `is_special_chaos_country` and `is_actual_nonhuman_country` triggers inform recipient profiling.

Potential organized recipients may include:

- Kruger sovereignties with functioning industry
- Death or Fury actors with an accepted command structure
- advanced nonhuman derivative countries with full public packages

Potential invalid recipients may include:

- temporary outbreak carriers
- transient script tags
- pure horde actors
- map-only entities
- actors with no industry, technology, or command system

Each special system remains responsible for proving that its actor can use missiles. Event 32 should not infer capability from the classification alone.

## Chemical warfare system

Chemical missile delivery must use the shared exact-state chemical contract.

Event 32 provides:

- missile reserve
- launch site
- target state
- preparation
- delivery method
- incident record

Chemical warfare provides:

- agent eligibility
- physical chemical payload
- protection and policy gates
- release
- contamination
- disruption
- evidence
- attribution
- condemnation
- deaths
- Air Cleanliness pressure

A failed missile that does not release its agent does not create confirmed chemical use.

## Biological warfare system

Biological missile delivery uses the shared biological strike and outbreak contracts.

Event 32 must not:

- create a new disease definition
- replace outbreak spread
- bypass containment
- duplicate deaths
- duplicate condemnation
- grant a stockpile

## Nuclear and thermonuclear systems

Event 32 calls the shared strike consequence routes.

The shared system owns:

- nuke type
- blast
- population loss
- building damage
- fallout
- Air Cleanliness
- condemnation
- chaos
- Deaths
- visuals
- confirmed-use history

Event 32 owns delivery-specific reserve, site, guidance, command, and retaliation effects.

## Air Cleanliness

Conventional missile strikes do not add CBRN Air Cleanliness pressure unless they hit a source that the shared system explicitly models.

Chemical, biological, nuclear, thermonuclear, and special launch-site accidents call the existing Air Cleanliness sources once.

Event 32 must not duplicate the current values:

- chemical state contamination
- outbreak pressure
- nuclear strike pressure
- thermonuclear strike pressure

## Condemnation

Conventional attacks use ordinary diplomatic and war consequences.

Special payloads use the existing Condemnation categories:

- chemical
- biological
- nuclear
- repeat use
- cover-up where relevant

Event 32 may add evidence and attribution inputs. It does not create a missile-specific sanctions ladder.

## Deaths

Every civilian and military death from Event 32 uses the shared Deaths system.

Required sources include:

- conventional missile impact
- launch-site accident
- neutral accidental strike
- site assault
- special payload through shared routes
- delayed contamination or outbreak through owning systems

Event 32 should register a stable death-reason family if the shared enum requires one.

## Chaos Meter

Direct Event 32 firing and evolution changes use event-owned chaos deltas.

Strike consequences use:

- direct conventional escalation where designed
- shared death contribution
- shared contamination contribution
- shared nuclear-use ladder
- shared war or peace systems

Avoid double counting one strike under several event-owned paths.

## Fallout consequence route

A severe nuclear or thermonuclear exchange may raise Air Contamination to the Fallout threshold.

Event 32 must not:

- set `world_end`
- set Fallout flags directly
- show a competing terminal super event
- bypass the 100 percent contamination condition
- create an ordinary Event 32 world-end row

Event 32 provides real strikes and shared consequence calls. Fallout decides whether the campaign transition is ready.

## Event Logs

Connections must preserve log ownership.

- Event 32 firing records one Event 32 history row.
- Event 32 global evolution unlock records one Event 32 evolution row.
- Event 23 records its own nuclear milestone.
- Event 5 records its own collapse.
- Event 13 records its own disaster.
- CBRN confirmed use records through the shared systems.
- Fallout records through its dedicated consequence presentation.

A bridge must not create duplicate history rows.

## Triggerable scenarios

SCN-015 is owned by Event 32.

It may call:

- Event 32 program setup
- Event 32 evolution unlock helpers
- Event 32 incident setup
- existing war and payload validity helpers

It must not launch another event's scenario without that scenario's contract.

## Documentation and workbook

Implementation must align:

- `docs/events/032_missiles.md`
- Event 32 spec package
- relevant shared-system docs when an API changes
- `docs/systems/event_system/triggerable_scenarios.md`
- authoritative event catalog workbook
- generated event, cluster, and scenario CSV exports
- any Event 23, Event 5, Event 6, Event 13, Event 16, Event 21, Event 76 documentation whose bridge changes

## API ownership rule

When a connection is reusable across event families:

- put it in the owning shared system
- document inputs, outputs, defaults, side effects, and example
- keep it idempotent
- avoid a periodic global caller
- use exact receipts
- fail closed

When a connection is unique to Event 32:

- keep it in `032_missiles_*` files
- document the caller and lifecycle
- avoid adding it to the global dynamic registry without demonstrated cross-system reuse
