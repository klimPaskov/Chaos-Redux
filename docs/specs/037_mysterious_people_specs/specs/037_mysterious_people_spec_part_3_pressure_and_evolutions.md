# Event 037: Mysterious People

## Part 3: Overpopulation Pressure and evolutions

## Public mechanic

Event 037 exposes one persistent country value to the player:

## Overpopulation Pressure

Overpopulation Pressure measures whether the country can house, feed, move, serve, and integrate the population created by Event 037. The public scale runs from `0` to `100`.

| Range | Public stage | Meaning |
| --- | --- | --- |
| `0` to below `20` | Absorbing | Spare capacity is handling the increase. The country can exploit a demographic dividend. |
| `20` to below `40` | Strained | Housing and services are under pressure, but ordinary investment can recover the situation. |
| `40` to below `60` | Overcrowded | Several states are failing to keep pace. Food, transport, and settlement action is required. |
| `60` to below `80` | Emergency | The country faces active humanitarian and political consequences. Famine and displacement risks are high. |
| `80` to `100` | Breakdown | Support systems are failing across important states. Sustained mortality, mass movement, repression, or collapse can follow. |

The player should see the current stage, trend, next threshold, strongest positive factor, strongest negative factor, and a short explanation of the most useful available response.

## Internal pressure model

The public value is calculated from state-level pressure. State calculations can use several internal inputs because the player manages the result, not the formula.

Main state factors are:

- mysterious population as a share of real state population
- population density and settlement concentration
- housing and temporary accommodation capacity
- infrastructure and transport access
- supply connection and local logistics
- food-security projection from Famine
- refugee and displacement load from Migration
- local integration state
- war damage, occupation, blockade, bombing, and fallout
- state development, industry, and administrative investment
- active Event 037 support programs
- repeated arrivals before earlier cohorts were absorbed

The country value should combine a population-weighted national average with a smaller worst-state component. One tiny catastrophic state can raise concern but cannot place a huge country at Breakdown alone. A catastrophic capital or industrial state must remain visible.

## Pressure behavior

Pressure rises when another firing adds a large cohort, support capacity falls, Famine projections worsen, refugees concentrate, borders trap people, registration is blocked, forced movement transfers pressure to a weak destination, or support programs expire before permanent capacity exists.

Pressure falls when housing and service programs complete, agricultural and relief work improves Famine projections, planned settlement moves people to proven destinations, integration rises, war damage is repaired, and migration safely distributes concentration.

Deaths can reduce demand because fewer people remain. The event interface must identify whether a decline came from successful capacity work, ordinary mortality, forced displacement, or atrocity. It cannot present mass death as a normal project success.

## Demographic dividend

Countries at Absorbing or low Strained pressure can gain a dynamic demographic-dividend effect. It scales with integrated mysterious population and spare capacity.

Useful directions include:

- stronger long-term recruitable population
- higher factory and construction labor availability
- improved recovery from prior population loss
- better use of underpopulated states
- stronger civilian output where support remains healthy

The dividend grows as integration succeeds and weakens as pressure rises. At Overcrowded pressure, congestion and service strain largely neutralize it. At Emergency and Breakdown, the country receives active penalties tied to food, construction, production, stability, recruitment administration, and transport.

Use one staged dynamic effect or one effect family that changes with pressure. Do not create a stack of permanent spirits for each firing and each pressure band.

## Evolution structure

Event 037 has three evolutions. Each changes the scale and consequences of future manifestations.

Evolution activation follows the shared system:

- eligibility comes from Chaos and event history
- activation uses paced evolution timing
- evolution state gives no direct Chaos
- shared evolution logging records the milestone
- disabled evolutions do not set recorded flags or unlock gated behavior
- a higher enabled evolution includes lower-stage mechanics required for function even when a lower evolution is disabled

## Evolution I: Population Surge

### Eligibility and pacing

- global Chaos is at least `200`
- Event 037 has fired at least once, unless a valid pre-fire evolved opening applies
- Evolution I is enabled

Recommended base evolution timing is about `90` days after eligibility.

Faster factors can include high world mysterious share, a recent firing, several countries at Strained or worse pressure, and high global humanitarian stress. Slower factors can include long stability, strong integration, low world share, and no country above Strained.

### Changed manifestation

Future firings use the Evolution I grant scale. Existing settlements expand. New districts, farms, workshops, and villages appear. The workforce benefit becomes large enough to alter national development plans.

The first broad capacity problems appear:

- housing shortages
- schools, clinics, water, and transport falling behind
- employment mismatch
- longer registration
- rural opportunities where food and transport exist
- meaningful decisions for housing, utilities, services, agriculture, and planned settlement

A strong country can emerge much more powerful. A weak country can recover through selective investment, foreign relief, or controlled settlement.

Neglect produces improvised housing, local unrest, hidden communities, service failure, and higher vulnerability to later food shocks.

## Evolution II: Overpopulation Crisis

### Eligibility and pacing

- global Chaos is at least `400`
- Event 037 has fired at least once, unless a valid pre-fire evolved opening applies
- Evolution II is enabled

Recommended base timing is about `120` days after eligibility.

Faster factors can include world mysterious share above `5%`, several countries at Overcrowded pressure, widespread food vulnerability, major wars or blockades, and recent refugee movement. Slower factors can include successful support investment, strong food projections, and long periods without manifestation.

Evolution II can activate when Evolution I is disabled. It enables the support mechanics required for its crisis loop without recording Evolution I.

### Changed manifestation

Future firings use the Evolution II scale. Many states receive enough people to overwhelm ordinary service growth. Event 037 becomes a direct pressure source for existing Famine and Migration systems.

Event 037 does not create a separate food meter. It publishes burden and support facts. Famine determines Food Security, Food Reserves, Relief Access, stages, mortality, and relief.

Event 037 does not create a separate refugee system. It submits proven movement requests and receives results. Migration owns routes, cohorts, borders, trapped people, reception, settlement, deaths, and return.

### Crisis loop

A country at Overcrowded or worse must manage linked risks:

- food demand exceeds production or relief access
- damaged transport prevents distribution
- crowded cities send people toward safer states
- rural settlement fails without water, roads, or work
- closed borders trap people in deteriorating states
- foreign relief creates dependency or leverage
- military logistics protects distribution while consuming war resources

Successful management preserves the demographic advantage. Failure creates food insecurity, famine, starvation deaths, migration, trapped populations, riots, resistance, foreign pressure, and possible government collapse when existing political conditions support it.

Deaths reduce real population and Event 037 provenance through the shared transaction. They enter Deaths and generate Chaos through the normal deaths rule.

## Evolution III: Humanity Multiplies

### Eligibility and pacing

- global Chaos is at least `600`
- Event 037 has fired at least once, unless a valid pre-fire evolved opening applies
- Evolution III is enabled

Recommended base timing is about `150` days after eligibility.

Faster factors can include world mysterious share above `10%`, at least one Breakdown country, catastrophic Event 037-linked Famine, repeated manifestations, world war, or broad transport collapse. Slower factors can include no country above Overcrowded, strong global food access, and long calm periods.

Evolution III can activate when lower stages are disabled. It enables all lower mechanics required to function while recording only legitimate enabled milestones.

### Changed manifestation

Future firings use the Evolution III scale. A single manifestation can add a substantial fraction of a state's population. Dense urban regions can gain millions. Repeated manifestations can make mysterious people a majority.

Global consequences become severe:

- food demand rises faster than normal production
- construction is pulled toward housing
- rail, road, port, and supply systems overload
- safe destinations fill
- countries compete for grain, fuel, trains, trucks, and convoys
- military mobilization becomes easier after integration while civilian support becomes harder
- border and settlement disputes intensify
- governments face pressure to classify people by origin

A food-secure industrial country can still exploit the population increase and sustain a huge workforce and army. The event must reward preparation and expose structural weakness. It must not force every country into collapse.

A country at sustained Breakdown can face catastrophic famine, repeated flight, closed borders, abandoned districts, military requisition, authority failure, repression, secession, or civil conflict. Political collapse should emerge from actual war, stability, ideology, and authority conditions. Event 037 should not create a generic civil war from one number.

## Extreme measures

At Evolution III, severe pressure and compatible politics can reveal harsher routes.

### Closed settlement zones

The government restricts movement, registration, and access to designated areas.

Possible consequences:

- lower movement into protected districts
- concentrated pressure inside zones
- slower integration
- hidden population
- resistance and discovery risk
- higher Famine vulnerability when supply is weak

### Forced relocation

The government orders mysterious people into selected domestic or foreign destinations.

The action uses Migration and requires a valid origin, destination, route, transport, and reception result. Unsafe movement can create deaths and Condemnation. A refused destination creates trapped people or failure, not disappearance.

### Forced labor

The government places mysterious people into camp or forced-labor structures.

The action uses Camp and Repression. It can increase extraction or construction in the short term while creating mortality, resistance, evidence, Condemnation, and political consequences.

### Systematic killing

The government deliberately kills the Event 037 population.

This route uses existing genocide and atrocity systems. The target is living mysterious population recorded in each affected state.

It must create:

- exact real population loss
- exact Event 037 ledger loss from applied deaths
- shared Deaths entries
- evidence, discovery, and cover-up behavior
- Condemnation when exposed
- resistance and survivor flight
- foreign reactions and sanctions
- durable perpetrator history

A sanitized population-control button is forbidden. Pressure may fall because fewer people remain, but the cause remains visible through the atrocity owner.

## Pre-fire evolved opening

Event 037 can first appear after evolution thresholds have been reached.

The first firing uses the highest enabled eligible stage:

- under `200` Chaos, baseline
- at `200` or more, Evolution I scale when enabled
- at `400` or more, Evolution II scale when enabled
- at `600` or more, Evolution III scale when enabled

The opening report reflects scale without exposing developer tier language.

Evolution logging must remain clean:

- an enabled pre-fire evolution can record immediately before manifestation when the shared system supports it
- disabled stages remain unrecorded
- higher stages receive lower mechanics required to function
- evolution activation adds no Chaos
- population created by the manifestation can trigger concrete one-shot Chaos milestones

## Recovery

Evolution stages do not reverse. The world has learned that larger manifestations are possible.

Pressure can recover fully. A country can move from Breakdown to Absorbing through investment, relief, settlement, integration, reconstruction, and time.

A recovered country retains living population, integrated workforce benefits, historical policy and atrocity memory, provenance, and future vulnerability.

Temporary emergency decisions close when no longer valid. Long-term housing, transport, agriculture, and integration benefits remain when projects created real capacity.

## Evolution acceptance statement

Each evolution must change future manifestations and player choices. Evolution I introduces capacity investment. Evolution II connects population burden to Famine and Migration. Evolution III permits enormous growth, severe collapse, and atrocity routes through existing systems. Flags, logs, and thresholds alone do not satisfy the design.
