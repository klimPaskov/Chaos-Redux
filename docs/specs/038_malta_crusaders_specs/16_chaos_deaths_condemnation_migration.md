# Shared system integration

## Core rule

Event 38 must use the existing Chaos Redux systems as owners of global state. It can publish Event 38 facts, call stable APIs, and register exact consequences. It must not create parallel Chaos, Deaths, Condemnation, famine, migration, camp, contamination, or world-threat ledgers.

## Chaos Meter

### Generic sources

Do not duplicate these existing sources:

- war
- peace
- annexation
- puppeting
- liberation
- faction joining or leaving
- ideology change
- nuclear or thermonuclear use
- world tension
- military buildup
- division buildup
- deaths
- air contamination

### Event 38 one-shot sources

Suggested event-owned consequences are:

| Outcome | Direction | Initial tuning | Rule |
| --- | --- | ---: | --- |
| Jerusalem secured as a stable crusader center for the first time | Increase | `+5` | one campaign milestone |
| first durable Crusader Principality created | Increase | `+3` | one campaign milestone |
| Pope installed as supreme ruler in Rome | Increase | `+5` | one campaign milestone |
| Teutonic Order faction proclaimed | Increase | `+10` | hidden one-shot |
| Operation The Final Crusade begins | Increase | `+15` | hidden one-shot |
| Atlantis betrayal begins | Increase | `+20` | hidden one-shot |
| negotiated withdrawal and regional settlement | Decrease | `-3` | one settlement generation |
| durable peace with a major regional opponent | Decrease | `-5` | one campaign milestone |
| Holy World preparation formally dissolved | Decrease | `-10` | only if terminal state never activated |
| Atlantis defeated and extermination policy dismantled | Decrease | `-10` | one aftermath milestone |

These values are starting tuning, not final code. They need balance review and central script constants.

Evolution activation, formable cosmetic changes, relic discovery, ordinary unit spawning, and ordinary focus completion give zero Chaos unless a separate concrete consequence in the table occurs.

### Chaos history

Every Event 38-owned change uses the shared history pipeline with:

- event ID 38
- actor where relevant
- localized cause
- exact amount
- one-shot proof

No hidden route name appears before public reveal.

## Air Cleanliness and contamination

Event 38 does not add ambient contamination by default.

Possible sources:

- chemical or biological siege ammunition
- unconventional warfare by Atlantis, Holy World, or ordinary Malta
- nuclear use
- disaster or wildfire effects owned by another system

Every source registers through its owner system. Event 38 decisions can read current contamination and treaty membership.

Hospitaller and Saint Lazarus routes can:

- improve local protection
- support evacuation and relief
- build filters or hospitals
- contribute to treaty projects
- respond to contaminated states

They cannot reduce global contamination directly without using the Air Cleanliness APIs and documented source clearing.

## Deaths

### Population-loss contract

Any Event 38 direct civilian loss uses `apply_exact_state_civilian_population_loss` with:

- requested loss
- protected minimum remaining population
- Event 38 or shared reason constant
- Deaths logging flag
- target country proof where applicable
- one-shot contract proof

The effect returns the exact applied amount and reconciles recruitable-manpower credit.

### Likely Event 38 death sources

- explicit siege or sack outcomes
- occupation atrocities
- camp and extermination sites
- famine
- forced displacement harm
- chemical, biological, or nuclear use
- terminal war consequences

Ordinary battle casualties remain military-casualty owned. Bombing, nuclear, outbreak, camp, famine, and migration deaths remain owned by their source systems.

### Double-counting prevention

- a famine death is logged by famine only
- a migration route death is part of the migration transaction only
- a camp death is logged by the camp system only
- a chemical or biological death is logged by the weapon or outbreak system only
- Event 38 does not register an extra generic “crusade death” for the same people

## Condemnation

Event 38 actors can receive Condemnation for:

- chemical, biological, nuclear, or thermonuclear use
- exposed camps
- systematic killing
- destroyed records
- blocked inspection
- cover-up
- repeated public atrocities
- hostile weaponized zombie deployment if another route enables it

Ordinary conquest and religious government do not automatically create Condemnation. Public actions and discovered evidence do.

### Malta route effects

High Condemnation can:

- reduce Sacred Legitimacy
- expel supporters
- block Papal recognition
- increase embargo pressure
- weaken principality loyalty
- strengthen resistance
- trigger compliance or reform decisions

### Holy World

The Holy World does not clear existing Condemnation. Believer governments can still react to atrocities, especially before terminal submission. Terminal politics can suppress some diplomacy, but the source ledger remains intact.

### Atlantis

Atlantis is expected to accumulate severe atrocity and repeat-use condemnation after evidence becomes public. Hidden evidence remains hidden until discovery.

## Famine

Event 38 interacts with famine through the existing state-owned food-security system.

Likely pressures:

- blockade of Malta or island principalities
- damaged ports and convoys
- siege of Jerusalem
- forced requisition
- migration load
- scorched territory
- terminal war disruption

Malta and principalities can use accepted famine decisions and adapters:

- reserve release
- emergency imports
- route repair
- escorted relief convoys
- airlift
- invited relief
- evacuation
- safer-state requisition
- concealment or extraction under harsh routes

Blockade famine requires war, isolation or maritime dependence, route disruption, convoy or escort shortage, inadequate local supply, and no relief corridor. Island status alone is insufficient.

Hospitaller routes improve relief access and response. They do not make famine impossible.

## Migration

Migration can arise from:

- opening territorial seizures
- war defeat
- siege
- atrocities
- famine
- terminal side assignment
- forced religious policy
- Atlantis extermination
- withdrawal or restoration settlements

Movement uses the shared migration cohort transaction. Closed borders create trapped populations. Forced return and violent pushback can produce Deaths through the migration owner.

### Event 38 decisions

Event 38 can request:

- organized evacuation
- corridor negotiation
- reception in Malta or a principality
- third-country resettlement
- safe return after settlement
- forced removal only on harsh routes with full consequences

It must not reduce origin population and then independently add destination population outside the shared transaction.

### Holy World side assignment

The terminal setup should not instantly move whole populations merely because governments choose sides. Population movement occurs only through war, policy, fear, evacuation, or route decisions.

## Camps and repression

### Ordinary Malta

Direct rule, harsh order government, or Papal coercion can activate detention or repression sites through the shared system. The event should not assume the player must use them.

Humane and constitutional routes can:

- inspect sites
- close sites
- reform authority
- expose records
- protect detainees
- negotiate local administration

### Atlantis

Atlantis uses the full camp and repression network. Active sites register in bounded arrays and process through host-local logic.

The route can create:

- detention sites
- concentration sites
- forced-labour sites
- extermination sites
- experiment sites only when source technology and policy allow them
- restricted chemical or biological sites

Every site needs lifecycle, evidence, discovery, population loss, Deaths, Condemnation, resistance, reform, liberation, and cleanup.

## Religious policy and population

The event can model:

- conversion pressure
- church jurisdiction
- local Christian collaboration
- Muslim resistance
- Orthodox resistance
- interchurch disputes
- protected sacred access
- local autonomy

It must not implement a protected-class selector or reduce whole populations to one religious policy variable. State and country outcomes should use existing resistance, compliance, local support, migration, and event systems.

## Shared country classifiers

### Malta and ordinary derivatives

These actors normally satisfy `uses_normal_civilian_systems` and are not actual nonhuman countries.

### Event-special routing

When another system should exclude Malta from ordinary targeting, use an event-owned trigger based on stable Event 38 origin or actor facts. Do not place Malta in the shared special-country classifier merely to avoid one Event 40 target.

### Hidden and terminal actors

Atlantis and Holy World remain human political states. They also use normal civilian systems. They can receive event-owned terminal markers without being marked nonhuman.

If a truly nonhuman derivative is ever added later, that requires a separate accepted design and classifier update.

## World threat aggregate

The Teutonic Order, Atlantis, and Holy World can count as existential threats only if the project accepts Event 38 as a registered threat source.

Recommended source flags:

```text
world_threat_source_malta_crusaders_teutonic
world_threat_source_malta_crusaders_atlantis
world_threat_source_malta_crusaders_holy_world
```

Before adding them, inspect the current `refresh_world_threat_state` registry and update its documentation and every count assumption. Use one source per concurrently meaningful threat. Clear each source on defeat or dissolution, then call the refresh effect.

Baseline Malta does not need a world-threat source merely because it is at war.

## Natural disaster gateway

Event 38 may call `call_natural_disaster` only through documented inputs and owner validation. Example uses might include a route-specific disaster during a relic expedition or terminal war only when accepted in final design.

The event should normally react to disasters rather than generate them.

## Stockpile debits

Use the shared stockpile removal helpers for supported equipment and fuel. New Event 38 equipment families need documented owner helpers when dynamic removal is required.

No cost should be described in localisation without a matching actual debit.

## Cleanup and reconciliation

On annexation, route transformation, defeat, or terminal transition:

- clear active Event 38 requests
- preserve shared Deaths, Condemnation, contamination, famine, migration, and evidence history
- clear only Event 38-owned active markers
- close or transfer camps through the camp system
- remove stale world-threat sources
- refresh world threat
- cancel invalid relief, migration, and project receipts
- preserve population exactly

## Integration acceptance tests

1. siege loss with exact population debit
2. famine and migration in the same state
3. camp site discovered after Atlantis defeat
4. hidden evidence remains absent from public Condemnation
5. chemical use under Event 36 treaty membership
6. Malta excluded from Lawrence targeting without shared nonhuman classification
7. Holy World terminal with existing contamination and deaths disabled by settings
8. world-threat source activates and clears
9. no duplicate Chaos from war or deaths
10. save and reload with active migration, famine, camps, and terminal routes
