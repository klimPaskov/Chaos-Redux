# Event 056: Chaos, Balance, and Performance

## Balance objective

Event 56 should create a visible naval redistribution without deciding the campaign by itself.

The first firing must be large enough that every eligible country notices the result. It must also remain bounded enough that naval combat, repair queues, map readability, and late-game performance remain usable.

The event should produce winners and awkward recipients. It should not produce invalid recipients, unusable fleets, or unlimited repeat growth.

## Chaos impact map

Event-owned Chaos changes apply only to concrete first milestones. The event does not add Chaos for every ship or every country.

| Milestone | Chaos change | Repeat guard | Reason |
| --- | ---: | --- | --- |
| First global manifestation of Event 56 | +5 | Once per campaign | Complete fleets appearing worldwide are a direct anomalous event outcome. |
| First Event 56 firing that successfully commissions fleets in at least 25 countries | +5 | Once per campaign | The event has crossed from scattered naval gifts into a world-scale military redistribution. |
| First experimental naval asset actually delivered through Evolution II | +10 | Once per campaign | A registered special or experimental capability has entered ordinary national service. |
| First impossible fleet package actually delivered through Evolution III | +15 | Once per campaign | The evolved event has produced a formation outside ordinary naval procurement logic. |
| First country that was previously skipped as landlocked later receives a package after gaining direct usable coast | +3 | Once globally | The anomaly has followed a changed coastline into a new navy. |

The first two milestones can occur during the same firing. That is intentional when the first manifestation reaches at least 25 countries.

## What does not add event-owned Chaos

Event 56 must not add separate Chaos for:

- each recipient
- each ship
- each convoy
- each aircraft
- each emergency port
- each repeat receipt
- each commissioning choice
- each naval battle
- each blockade
- each sunk ship
- evolution activation by itself
- ordinary war, annexation, death, nuclear use, or world tension caused later

Those outcomes either do not justify a separate event milestone or already belong to shared Chaos sources.

## Reversal policy

Event 56 has no direct negative Chaos reversal.

The fleets become ordinary national assets after commissioning. Losing, dismantling, or scuttling them does not undo the fact that the global manifestation occurred. Peace, reduced tension, and other stabilizing outcomes continue to affect Chaos through their own shared systems.

A forced event-owned reversal would encourage strange farming behavior and would imply that the anomaly can be solved by destroying ships. The design does not support that conclusion.

## Global delivery budget

The event needs a world-level budget because it processes every eligible naval country in one firing.

The budget should consider:

- eligible recipient count
- current Chaos and enabled evolution stage
- recipient receipt counts
- package identity mix
- global performance setting where the mod exposes one
- actual ship entity count
- hull-equivalent value
- aircraft and convoy support
- delayed tranches already reserved

No single factor is enough. A carrier package can be expensive in value while adding few entities. A destroyer swarm can add many entities at lower value.

## Initial world-budget targets

The following values are planning anchors for hull-equivalent allocation. They require calibration against the implemented ship registry and performance tests.

Let `N` represent the number of eligible recipients for the firing.

| Active package stage | Working world budget | Working ceiling |
| --- | --- | ---: |
| Baseline | 350 plus 4 per eligible recipient | 700 |
| Evolution I | 450 plus 5 per eligible recipient | 900 |
| Evolution II | 550 plus 6 per eligible recipient | 1,100 |
| Evolution III | 650 plus 7 per eligible recipient | 1,350 |

These values are internal design targets, not player-facing numbers.

The implementation must test whether the chosen hull-equivalent scale can preserve a compact coherent package for every eligible country in the benchmark world. If it cannot, the value mapping or budget targets must be adjusted. Valid recipients should not be skipped merely because the planning anchor was too low.

## Ship-entity safety target

Hull-equivalent value must be paired with a direct entity-count limit.

The implementation should establish separate safe targets for:

- total combat ships created in one firing
- maximum combat ships for one recipient
- maximum ships in one initial task force
- maximum simultaneous delayed tranches

The final values require source and performance inspection. The design requirement is firm:

- the world cannot receive an uncapped destroyer or submarine explosion
- one country cannot receive a single task force with dozens of light ships beyond useful command size
- package identity must remain visible under the cap
- every eligible recipient should still receive a meaningful result

When entity limits are tighter than value limits, shift part of the reward into convoys, aircraft, fuel, repair support, or fewer heavier ships where the rolled identity permits it. Do not change a submarine package into a capital fleet merely to save entities.

## Fair allocation order

The global budget must not reward countries processed early and starve countries processed late.

A suitable design sequence is:

1. Build the full eligible recipient set.
2. Assign each recipient a protected minimum package share.
3. Roll package identities and receipt scales.
4. Estimate each package's defining minimum and desired expansion.
5. Reserve every defining minimum before distributing extra value.
6. Allocate remaining world budget through bounded randomized expansion.
7. Normalize entity-heavy packages if the direct ship count target is exceeded.
8. Commission recipients only after the whole allocation is stable.

This keeps the result global and random while protecting every recipient from processing-order bias.

## Protected minimum package

Every delivered package must contain a minimum expression of its identity.

Examples:

- carrier package: at least one carrier, a legal screen, and an aircraft support route
- capital package: at least one defining capital ship with screens
- cruiser package: enough cruisers to dominate combat value
- destroyer package: enough destroyers to feel like a swarm relative to its size band
- convoy package: a meaningful convoy reserve with escort groups
- invasion package: transport capacity plus escort and bombardment support

If the protected minimum cannot be delivered legally, remove that identity from the recipient's legal pool before the final roll. If no identity remains, skip the recipient with an internal reason.

## Local package limits

Country strength does not determine package identity, but local safety can influence package band.

Relevant factors include:

- number and level of controlled naval bases
- safe repair capacity
- ability to place carrier aircraft
- number of valid commissioning ports
- repeat receipt count
- world budget share

Factors that must not influence package identity include:

- ideology
- doctrine preference
- current production plan
- enemy fleet composition
- faction role
- whether the package would be strategically optimal

A minor country can receive a carrier or capital package. Local safety may keep it Compact or Standard when a Heavy package would not fit.

## Support-value balance

Support should make the rolled fleet usable for an initial period. It must not make sustainment free.

### Fuel

- grant enough for organization, redeployment, and a short operational window
- scale by package identity and active hulls
- do not fill an enormous strategic reserve unrelated to the package
- do not waste value above practical storage behavior

### Convoys

- invasion and convoy packages receive the most
- balanced, carrier, and capital packages receive moderate support
- submarine and coastal packages receive little unless their subvariant requires it
- breakup conversion cannot return more convoy value than the removed hull value justifies

### Aircraft

- carrier packages receive enough compatible aircraft to establish their role
- overflow aircraft can enter nearby bases or stockpile
- other packages receive aircraft only when their identity supports it
- no air technology is granted

### Port support

- emergency facilities provide only the minimum commissioning foothold
- repair support is temporary or bounded
- Event 55 remains the route for large infrastructure transformation

## Military power balance

The event intentionally disrupts military balance. A strict equal-power distribution would undermine the premise.

The following outcomes are acceptable:

- a minor coastal country becomes locally dangerous
- a major power receives a package that is less useful than a neighbor's
- an existing naval power becomes stronger
- an island country receives strong convoy security
- a land-focused country gains a navy it did not plan to use

The following outcomes are not acceptable:

- one random minor receives enough ships to exceed the total world budget by itself
- a package has no safe screen or aircraft support
- countries receive ships in enemy ports
- a repeat recipient gains full first-firing scale forever
- an AI country destroys every gift by immediate invalid use
- a country can turn every package into superior conversion profit

## Existing navy interaction

The event should supplement or complicate the existing navy. It does not replace national designs, production, or command.

A recipient with a large navy can integrate the package or keep it separate. A recipient with no navy gains an immediate foundation.

The event should avoid deleting, converting, refitting, or reorganizing pre-existing ships. Its commissioning task forces contain only the new cohort at creation.

## Ship naming and readability

Large global grants can produce naming collisions or unreadable fleets.

The final design should use a supported naming route that:

- avoids duplicate visible names where practical
- preserves country-appropriate naming where available
- uses clear numbered or class-based fallback names
- does not create a separate localisation burden for every ship
- identifies the package or task-force role clearly enough for the recipient

Names must remain ordinary naval names. The event mystery belongs in the report, not in dozens of joke ship names.

## Repair and organization balance

Granted ships should not enter combat at perfect readiness with no commissioning period.

A short readiness effect can represent complete crews and basic records while still requiring normal organization, positioning, and repair behavior.

Full commissioning receives the strongest immediate readiness support. Phased commissioning reduces port strain by delaying part of the force. Breakup reduces the number of active hulls.

The event should not spawn most ships heavily damaged. That would turn a gift into repair-queue clutter. Limited wear or temporary organization pressure is enough.

## Performance rules

### Bounded global pass

Event 56 can traverse the relevant country set once during its firing. It must not add a daily, weekly, or monthly whole-world scan.

### Sparse delayed work

Only countries with phased delivery or emergency commissioning receive delayed follow-up work. Each recipient gets one bounded resolution path.

### Bounded arrays and ledgers

- build the eligible list once
- process each recipient once
- clear allocation arrays after the firing
- keep only compact cohort and achievement memory
- do not retain a permanent per-ship event history table

### Bounded task forces

- use at most three commissioning ports per recipient
- use a small number of task forces per package
- split swarms into practical groups
- avoid one task force with every ship

### Bounded characters and assets

- do not generate admirals for each recipient
- do not create country-specific art for every package
- do not create custom ship models for ordinary package content

## DLC and content compatibility

### Ship designer content

Where a naval designer is active, the event can use safe existing designs or controlled event designs. Without that content, it uses legal predefined ship types that preserve the package identity.

The result should remain recognizable in both cases.

### Mine warfare

The sea-denial identity appears only when the active content supports it. Removing this identity should not reduce the rest of the pool below a useful range.

### Carrier aircraft

Where aircraft design systems are active, the event uses compatible legal aircraft. Without them, it uses supported predefined carrier aircraft or another legal aircraft route.

A carrier package is removed from the legal pool only when no credible aircraft support can be created.

### Special projects and experimental content

Experimental and impossible assets require their owner registration and any relevant content. A missing DLC or disabled owner system removes the asset cleanly.

The evolution still works with other legal entries. It does not substitute an unrelated hidden asset.

### Base-game experience

A player without optional naval content should still receive the full baseline event structure:

- all generally legal package identities except content-specific specialists
- commissioning choices
- repeat scaling
- evolutions using the safe content available
- event history
- achievements where their conditions remain possible

## Exploit risks and prevention

| Risk | Prevention direction |
| --- | --- |
| Repeated breakup produces superior resources | Use a lossy conversion tied to removed cohort value and declining receipt scale. |
| Save and reload repeats delayed delivery | Store one delivery proof and one cancellation proof per reserved tranche. |
| Tag or ideology change resets receipt count | Tie history to stable country identity rules rather than cosmetic state. |
| Port loss creates repeated rerolls | Permit one bounded port re-selection without changing identity or package value. |
| Player destroys granted ships and still meets achievements | Achievement checks require surviving tagged cohort value or actual use by granted defining ships. |
| Cluster firing applies Event 56 twice | One selected event can produce one Event 56 member transaction. |
| Event 42 duplicates carrier aircraft in the same cluster | Cross-event adapter checks support already granted by Event 56. |
| AI runs the whole fleet without fuel | Bounded AI reserve behavior and phased commissioning. |
| Huge light-ship packages damage performance | Direct entity cap, task-force cap, and world allocation before commissioning. |
| Country deliberately stays landlocked to preserve first scale | This is acceptable strategic timing because the country receives nothing until a later natural repeat. |

## Balance telemetry for testing

The implementation should be able to inspect these firing results during development without exposing them as normal player UI:

- eligible country count
- successful recipient count
- skipped recipient count by reason
- total combat ships created
- total hull-equivalent value
- package identity distribution
- size-band distribution
- receipt-scale distribution
- total convoys and aircraft granted
- emergency ports created
- full, phased, and breakup choices
- delayed tranches reserved, delivered, and cancelled
- experimental and impossible assets delivered
- time required to resolve the firing

Temporary diagnostic output must be removed or disabled after the feature is validated.

## Balance acceptance

The event is balanced when all of these statements are true:

- every valid recipient receives a coherent package or a clear internal skip reason
- the first firing changes naval capability across the world
- minors can receive surprising power without receiving unlimited fleets
- later repeats remain interesting and smaller
- package identity stays random
- AI countries can use or reduce awkward packages sensibly
- conversion is useful but inefficient
- carrier and capital packages include their functional support
- world ship creation stays inside tested performance limits
- no event-owned Chaos source can be farmed repeatedly
