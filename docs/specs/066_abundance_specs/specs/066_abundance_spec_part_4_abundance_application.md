# Abundance Application

## Owner-controlled application

Event 66 never writes directly into another system's internal ledger.
The selected candidate returns to its provider with the country, wave identity, card identity, candidate identity, strength profile, and stored target data.
The provider performs the operation and returns a receipt.

This rule preserves stage transitions, source ledgers, caps, cleanup, modifiers, death accounting, contamination accounting, event ownership, and DLC behavior.
It also lets future systems define abundance without changing the Event 66 core.

## Abundance shapes

### Accumulative quantity

An accumulative quantity receives a grant large enough to change planning immediately.
The grant uses an absolute floor and a country-relative scale based on the normal size or throughput of that value.
The provider also applies an engine-safe ceiling so the result cannot overflow script arithmetic or corrupt UI formatting.

The target should feel absurd for a minor country and still matter for a major country.
A single universal number cannot meet both goals.

### Bounded gauge

A bounded gauge moves toward its upper practical limit.
The provider uses the public meaning of the gauge, not the sign or storage convention of its internal variable.
Stability abundance means high Stability.
Panic abundance means high panic even if the owner stores calmness internally.

If the gauge is already near the top, the provider may add retention, resistance to decay, or an owner-defined overflow state so the choice still matters.

### Stockpile

A stockpile receives an amount scaled by country size, current armed forces, production capacity, normal consumption, and the value's own storage model.
A family provider selects only concrete tokens that exist and can be granted safely.

Equipment abundance does not invent missing archetypes, bypass mutually exclusive technology rules, or grant event-owned equipment whose owner has not registered it.

### Capacity or charge pool

A capacity fills to its upper practical range.
If the owner supports temporary over-capacity, the provider can add it through a documented overflow state.
If not, the result stops at the legitimate cap.

### Stage or threshold mechanic

A staged value enters a high valid stage.
The owner decides whether intermediate transitions must execute in order or whether one safe transition can establish the final stage.
Event 66 cannot skip mandatory initialization, reports, modifiers, cleanup, or source ledgers.

### State-distributed value

A state-distributed provider chooses a bounded set of valid owned or controlled states.
The number and importance of states can scale with the strength profile and country size.
The provider owns target selection and state mutation.

The event should avoid giving one large country hundreds of effects merely because it controls many states.
Breadth needs a cap and a country-relative rule.

### Owner-custom value

A system can define a custom abundance operation when its value does not fit the common shapes.
The operation must still be deterministic for the stored candidate, idempotent for the wave item, visible enough to explain, and auditable.

## Strength profiles

Every provider receives one of four conceptual profiles:

- Low cluster profile
- Standard direct profile
- Medium cluster profile
- High cluster profile

All profiles must create a clear abundance result.
The difference comes from magnitude, overflow persistence, distribution breadth, or stage depth.
The owner chooses the axis that makes sense for its value.

Low normally establishes immediate saturation with little or no overflow persistence.
Standard establishes saturation with normal persistence.
Medium can add stronger persistence or broader distribution.
High can apply the strongest safe persistence, breadth, or upper-stage pressure.

The profile does not alter whether high values are good or bad.
A High profile applied to a harmful pressure makes the harmful abundance stronger or more persistent.

## Country-relative scaling

Providers should use the value's own meaningful scale.
Useful inputs include:

- country population
- deployed and reserve manpower
- division count
- factory count and industrial throughput
- normal monthly gain or spending
- fuel capacity and consumption
- equipment demand
- number of controlled states
- number of valid targets
- mechanic stage and headroom
- crisis intensity
- current law, route, or DLC state
- cluster profile
- current evolution only when that evolution explicitly changes strength

The result must contain floors, caps, and clear rounding.
Small countries must not receive zero through truncation.
Large countries must not exceed engine-safe arithmetic or create unbounded loops.

## Persistence

Some values matter only if abundance lasts long enough to influence play.
A provider can attach a bounded abundance state that slows decay, increases generation, expands storage, or holds the value near saturation.

Persistence is part of the selected value's owner operation.
It is not a generic national spirit shared by every candidate.
A stockpile, pressure, balance of power, and crisis stage can require different treatments.

Repeat firing can refresh or intensify persistence only through provider rules.
It must not stack without a cap.

## Harmful abundance

Harmful candidates use the same magnitude and receipt standards as beneficial candidates.
The provider must identify the public consequence clearly enough for a choice tooltip, but it does not need to reveal hidden follow-up events.

A harmful result can:

- raise an active crisis pressure
- push a low-is-desirable gauge toward its danger threshold
- increase resistance or public condemnation
- add an unsafe stockpile or burden
- intensify a country-specific struggle
- create overflow costs
- activate an owner-defined critical stage when the owner explicitly permits it

The event does not add a compensating reward merely because the choice is harmful.
Mixed values can carry both a gain and a burden through their owner operation.

## Atomicity and receipts

Every atomic candidate in a selected card has a unique wave-item identity.
The provider records application before any delayed follow-up that could call it again.
A save load, event refresh, duplicate callback, or cluster duplicate cannot apply the same item twice.

A receipt contains:

- wave identity
- country identity
- card index
- candidate index
- provider and candidate identity
- result status
- applied magnitude, stage, or target summary
- harm class
- persistence status when relevant
- owner transaction identity when one exists
- rejection or partial reason

A pair or triple is a set of independent atomic transactions.
The card succeeds completely only when every item succeeds.
A partial result keeps successful items and reports the failures.
Universal rollback is not required because many owner systems cannot safely reverse a completed effect.
Preflight and idempotence are the protection against half-applied corruption.

## Follow-up presentation

After selection, the player receives a compact result summary through the option tooltip, a short follow-up report, or the event's immediate effect display.
The summary names the values that applied and flags any item that became invalid before selection.

It should not expose exact safety caps, internal variables, provider names, receipt IDs, or hidden future consequences.
Detailed technical receipts belong in debug and audit surfaces.

## Interaction with shared systems

### Deaths

A provider that causes population loss uses the exact population and Deaths APIs owned by the relevant system.
Event 66 does not subtract population and then log the same deaths again.

### Air Cleanliness

A provider that increases contamination uses a registered source or country contribution.
It does not set the global contamination total directly.
The normal Air Cleanliness to Chaos synchronization remains authoritative.

### Condemnation

A provider that creates condemnation uses the owner source categories, evidence state, public disclosure rules, and sanctions path.
It does not bypass hidden evidence or write only the displayed total.

### Famine and migration

A provider touching food security, reserves, relief access, displacement, reception, or border pressure uses the famine or migration owner interfaces.
It must not duplicate population transfers, deaths, trapped populations, or relief ledgers.

### Event-owned mechanics

A provider attached to another event changes the exposed value without marking the owner event as fired.
It does not advance unrelated stages unless the owner callback defines that progression as the abundance operation.

## Chaos impact map

The first campaign manifestation of Abundance adds a one-time `+5` Chaos because the same impossible phenomenon appears across the world.
Later ordinary repeat firings add no automatic Event 66 Chaos.

Evolution activation adds no Chaos.
Pair and triple construction adds no Chaos by itself.
Cluster participation adds no separate cluster premium.

Concrete consequences continue to use their existing sources.
Deaths, contamination, wars, annexations, ideology changes, military buildup, and other shared effects must not be counted again by Event 66.
An owner-specific harmful abundance can add an event-specific Chaos source only when it creates an abnormal consequence not already measured, and the owner must guard that source against repetition.

Recovery, containment, or decay belongs to the owner system.
Event 66 does not issue a generic Chaos refund when an abundant harmful value later falls.

## Exploit and safety rules

- A selected item applies once per wave.
- Provider persistence and repeat stacking have owner-defined caps.
- A zero-effect provider cannot remain broadly eligible as a substitute for missing logic.
- Equipment families cannot grant invalid or mutually exclusive tokens.
- Population and state transactions cannot bypass their shared accounting helpers.
- Global ledgers cannot be overwritten directly.
- Another event's fired state cannot be granted through enumeration.
- A manual test or force trigger cannot unlock achievements.
- Country switching cannot combine achievement ledgers from several tags.
- Provider failures are reported and isolated.
