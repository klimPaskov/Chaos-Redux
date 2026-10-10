# Shared system integration

## Core rule

Event 38 must use the existing Chaos Redux systems as owners of global state. It can publish Event 38 facts, call stable APIs, and register exact consequences. It must not create parallel Chaos, Deaths, Condemnation, famine, migration, camp, contamination, or world-threat ledgers.

## Connections the player feels

Every integration below earns its place by changing a player decision.
Anything that would only add a number, flag, or tooltip line is left to the owner system.

| Shared system | What the player sees in Event 38 | Where it is defined |
| --- | --- | --- |
| Condemnation | a new public Condemnation against an Event 38 actor lowers Sacred Legitimacy once per source event, so exposed camps, chemical use, and cover-ups cost foreign support, Blessed access, and Papal routes | Condemnation below |
| Camps and repression | harsh direct rule or Papal coercion can open sites, and a seated Hospitaller or Saint Lazarus order objects, which strains Order Cohesion and can trigger an incident; humane routes can inspect and close sites | Camps below |
| Famine | a blockade of Malta or an island principality threatens the sea-road anchor and so Command Standing; relief delivered through the famine owner's actions raises Legitimacy once per contract generation; Conceal Hunger and Continue Requisitions on an Event 38 state cost Legitimacy | Famine below |
| Migration | seizures and sieges create refugees; the owner's Evacuate Civilians action is the only evacuation action, and a state packed with trapped people hurts the occupation choice between a commandery and a principality | Migration below |
| Fallout and contamination | a seated Saint Lazarus or Hospitaller order reduces attrition and recovery penalties in contaminated owned states, and nothing else about contamination changes | Air Cleanliness below |
| Chaos Meter | a short list of one-shot milestones moves Chaos, and every other source stays with its owner | Chaos Meter below |
| Deaths | sack and siege outcomes use the exact population-loss contract and one Deaths record | Deaths below |
| CBRN | siege ammunition upgrades need the Event 36 treaty stance and technology, and use creates shared Condemnation | Event 36 in `14_event_chain_reactions_cross_events.md` |

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

Each new public Condemnation against an Event 38 actor lowers Sacred Legitimacy by a script-constant step, once per source event.
High Condemnation can also:

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

Famine is owned by `docs/systems/famine_system.md`.
Event 38 adds no famine decisions and no famine values.
The owner's category offers Release Food Stores, Import Food, Restore Relief, Escort Relief, Airlift Relief, Requisition Food, Evacuate, Conceal Hunger, and Continue Requisitions, and Malta and its principalities use those actions as they stand.

Event 38 supplies pressure through the owner's adapter contract: blockade of Malta or an island principality, damaged ports and convoys, the siege of Jerusalem, forced requisition, scorched territory, and terminal war disruption.
Blockade famine follows the owner's proof, which needs war, geographic isolation, maritime dependence, port or route disruption, convoy or escort shortage, inadequate local supply, and no proven relief corridor.
Island status alone is insufficient.

Event 38 reads two outcomes.
Relief delivered to an Event 38 state raises Legitimacy once per relief contract generation.
Concealing hunger or continuing requisitions on an Event 38 state lowers Legitimacy, because the owner already condemns the cover-up.
A seated Hospitaller order improves nothing hidden here; its value is the recovery and attrition effects described in `04_crusade_council_mechanic.md`.

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

### Event 38 and migration actions

Migration is owned by `docs/systems/migration_system.md`, which offers Evacuate Civilians, Open Emergency Reception, Screen Incoming Civilians, Distribute Arrivals, Close the Border, Local Integration, Resettle Abroad, Help Families Return, and Force Repatriation among others.
Event 38 adds no migration decisions.
Its settlement choices (commandery, principality, restoration, Papal administration, treaty return) read the owner's trapped-people and reception facts, and forced removal under a harsh route goes through the owner's repatriation action with full consequences.
Event 38 must not reduce origin population and then independently add destination population outside the shared transaction.

### Holy World side assignment

The terminal setup should not instantly move whole populations merely because governments choose sides. Population movement occurs only through war, policy, fear, evacuation, or route decisions.

## Camps and repression

### Ordinary Malta

Direct rule, harsh order government, or Papal coercion can activate detention or repression sites through the shared system. The event should not assume the player must use them.

A seated Hospitaller or Saint Lazarus order objects to active sites, which strains Order Cohesion and can open an incident.
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

## Natural disasters

Event 38 reacts to disasters through the shared state and population contracts and does not generate them.
No Event 38 action calls `call_natural_disaster`.

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
