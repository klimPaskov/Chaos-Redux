# Shared-System and Event Connections

## Integration rule

Event 51 should connect to existing systems through stable public facts, validated gateways, and owner APIs. It should not read or mutate another system's private ledger.

Connections in this file are divided into required integration and conditional integration. Conditional integration should be implemented only when the live owner exposes a safe public fact or gateway.

# Required integrations

## Event 013 Natural Disasters

Event 51 owns persistent heat. Event 013 owns actual wildfire and other supported natural-disaster incidents.

Event 51 can submit a wildfire call when:

- the state has a suitable terrain or vegetation profile
- heat exposure is prolonged
- drought or dry-condition proof exists
- no incompatible disaster already owns the state
- the request carries current episode generation

The stable gateway is `call_natural_disaster` from country scope with Event 013's documented temporary inputs and target proofs.

Event 51 should inspect the exact supported disaster family constants. It must not invent a new drought family inside Event 013 unless the owner package already supports it or is expanded through a separately accepted design.

## Air Cleanliness

Heat alone does not directly add Air Contamination.

Wildfire smoke and ash are counted through Event 013 and the shared Air Cleanliness source reservoir. A wildfire caused by Event 51 must not also add a heat-owned contamination source.

If Air Winter or another atmosphere state materially alters heat, Event 51 may read an owner-published climate fact. It must not infer behavior from private contamination arrays.

## Deaths

Evolution I civilian mortality uses the shared exact population transaction. The implementation should register a heat-specific Deaths reason through the established constant and localisation pattern.

Military losses use the shared military casualty path.

Event 51 must not:

- store a second heat-death total
- add Chaos separately for deaths already counted by Deaths
- apply a second population loss after Migration moves people
- count isolated report deaths twice

## Famine

Event 51 submits proof-carrying heat and harvest incidents through the Famine adapter.

Famine owns:

- Food Security
- Food Reserves
- Relief Access
- famine mortality
- relief decisions and missions
- recovery

Event 51 can read only the published owner facts needed for heat scoring and destination safety.

## Migration

Event 51 submits survivor-flight, evacuation, or unsafe-habitation requests through Migration.

Migration owns:

- cohorts
- routes
- reception
- settlement
- return
- movement mortality

Event 51 publishes versioned heat safety and projected duration facts. It can consume a versioned trapped-population or reception-demand receipt.

## Event system

Event 51 registers as Minor Repeatable with Chaos level 1.

The entry event applies one normal event history and pacing transaction. Follow-up reports, missions, mortality pulses, and recovery events do not act as new random event firings.

## Event logs and Event Details

Event 51 needs:

- event name mapping
- repeatable classification
- enabled-state default appropriate to reworked events
- Event Details premise
- evolution preview rows
- history actor behavior for a global event
- evolution log entries
- public super-event linkage where the framework displays it

The premise should describe the persistent global heat system without listing hidden formulas.

## Natural Disasters cluster

Event 51 becomes a High-severity member of the Natural Disasters cluster.

Cluster behavior must ensure:

- one global pacing event
- normal Event 51 history and repeatable cap behavior
- no duplicate active Heat Wave when the cluster contains another heat-like member
- Event 51 is skipped with a recorded reason when an episode or recovery is active
- the cluster can still fire other valid members

The current CSV snapshot does not yet list Event 51 as a member. The authoritative workbook and live registry need alignment during implementation.

## Universal cost framework

When Event 026 Black Friday or another shared universal cost modifier applies to decision costs, Heat Wave decisions should use the existing framework if their cost types are supported.

The event should not create separate discount logic. Costs that cannot safely use the shared framework should be documented and remain unaffected.

# Conditional event connections

## Event 050 The Great Embargo

A Heat Wave target under a major embargo should face weaker:

- emergency food imports
- spare-part and machinery access
- fuel and transport access
- foreign relief
- lend-lease support

Event 51 should read public embargo status and enforcement facts. It should not duplicate sanctions or create a second embargo modifier.

The connection should make Event 50 materially worsen a later Heat Wave without making survival impossible.

## Event 034 Industrial Boom

An active extreme industrial boom can raise:

- water demand
- power and cooling pressure
- worker exposure
- risk of infrastructure failure

Heat protection that shuts down output can reduce boom benefits or raise Overheating management pressure through an owner adapter.

Event 51 should not directly force the Boom to collapse unless Event 34 publishes a compatible pressure input.

## Event 035 Great Depression 2.0

A depression can reduce:

- civilian capacity available for mitigation
- imports
- infrastructure repair
- hospital and water investment

It can also reduce industrial heat load. The net effect should depend on country conditions rather than being a simple universal penalty.

## Event 033 Acid Rain Superstorm

Acid Rain and Heat Wave can overlap. The overlap should use owner facts only.

Possible accepted interaction if the Event 33 implementation supports it:

- rain temporarily lowers raw heat pressure in affected states
- contaminated rainfall worsens water safety, crop damage, and recovery
- shelter use can increase indoor heat pressure

Do not create this interaction until Event 33's actual state and Air Cleanliness behavior is inspected.

## Diseases and outbreaks

Heat, water shortage, sanitation failure, and crowding can raise disease vulnerability. Event 51 may send a bounded risk fact to an owning outbreak system when a documented gateway exists.

It must not start arbitrary diseases through direct tag or flag manipulation.

## Camps and repression

Confinement sites in severe heat can create exceptional humanitarian risk. If the camp system exposes site and authority facts, Event 51 can:

- raise site water and mortality pressure
- create discovery or Condemnation consequences for denied relief
- use the shared exact population transaction through the camp owner

Event 51 should not inspect or mutate the private camp ledger directly.

## Occupation and resistance

Occupied states may have damaged governance, unequal allocation, restricted movement, and poor infrastructure. Heat Stress can use published occupation and devastation facts.

Resistance or compliance should not change through arbitrary heat pulses. Changes require a condition-linked report, failed distribution, or owner-system action.

## Nuclear fallout and Air Winter

Fallout, contamination, and Air Winter can alter sunlight, agriculture, infrastructure, and health. Any direct climate interaction requires a stable owner fact.

Event 51 must not assume nuclear winter always cancels heat. A damaged, contaminated state can still experience severe local heat and water failure.

## Asteroid aftermath

Dust, wasteland, destroyed states, and altered resources can change vulnerability in a later Heat Wave. Event 51 should read the world left behind through terrain, infrastructure, population, and owner facts. It does not need a special Event 28 adapter unless the owner exposes one.

## Riches Found and mining systems

A high-output mine in severe heat can increase water and industrial pressure. Use actual extraction and state importance rather than the event history alone.

# Shared country classifiers

The following shared predicates remain centralized:

- `is_desert_state`
- `is_special_chaos_country`
- `is_actual_nonhuman_country`
- `uses_normal_civilian_systems`

Event-owned validation belongs in Event 51 files. Do not add event lifecycle or Heat Stress logic to the shared classifier registry.

# Dynamic helper policy

Before adding helpers, inspect the existing dynamic effects.

Likely reused helpers:

- `call_natural_disaster`
- `apply_exact_state_civilian_population_loss`
- `apply_state_population_loss_without_recruitable_manpower_gain`
- stockpile debit helpers for support equipment, motorized equipment, convoys, trains, infantry equipment, and fuel

Potential new cross-system helper should enter `chaosx_dynamic_effects` only when its contract is neutral and has callers beyond Event 51. Event-owned orchestration stays in Event 51's own scripted-effects files.

# Adapter failure policy

Every cross-system request should return or expose an acceptance result where the owner API supports it.

If rejected:

- Event 51 records a compact debug reason
- no partial owner-ledger write occurs
- the request proof is cleared
- the player-facing event uses a safe local consequence or no consequence
- it does not retry every day without a cooldown

# Integration acceptance matrix

| Integration | Required proof |
| --- | --- |
| Natural Disasters | Valid request, supported family, no duplicate incident, Event 013 owns impact |
| Air Cleanliness | Heat adds zero direct contamination, wildfire source appears once |
| Deaths | Exact heat loss recorded once with real state population change |
| Famine | Owner accepts or rejects proof cleanly, no direct private-ledger write |
| Migration | Owner controls movement and population transfer, no double debit |
| Event logs | One event history entry, correct evolutions, no follow-up pacing duplication |
| Cluster | One pacing transaction and a clear skip reason during active episode |
| Cost framework | Supported cost modifications apply once and display correctly |
