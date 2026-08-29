# Famine and Migration Mechanics

## Part 3: Displacement, migration, exodus, and return

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any historical wording in this specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Population movement principle

Migration is a population transfer between real states. It is not a death effect and it is not a free population creation effect.

Every completed flow must have:

- an origin state
- a movement cause
- a cohort type when cohort choice matters
- a route state
- a destination state
- a destination country
- an amount requested
- an amount actually removed from the origin
- any route deaths
- an amount actually added to the destination
- a durable-outcome status

The destination receives only the population that left the origin and survived the route.

## Movement types

### Internal displacement

Civilians move to another state inside the same country or controlled territory.

Internal displacement is normally preferred because it avoids an international border and preserves political membership. It can still fail when every nearby state is unsafe, overcrowded, under occupation, contaminated, or cut off.

### Cross-border refugee flight

Civilians leave the country or occupied territory because the origin is unsafe and a foreign state offers a safer route.

Cross-border flight depends on border policy, diplomatic access, route safety, capacity, and persecution risk.

### Organized evacuation

A government or recognized authority organizes temporary movement from an unsafe state to a safer state.

Evacuation requires transport, scheduling, destination capacity, and protection. It can prioritize cohorts and can be reversed when conditions improve.

### Spontaneous exodus

Civilians leave with limited state coordination because fear or immediate danger exceeds the perceived risk of travel.

Spontaneous exodus uses less organized transport, is harder to direct, and creates higher congestion and route risk.

### Deportation and forced relocation

An authority compels civilians to leave their state.

Forced movement can be used for occupation policy, ethnic or political persecution, labor relocation, security zones, camp transfers, scorched-earth withdrawal, or ideological projects.

It creates attributed responsibility, resistance pressure, hidden or public atrocity evidence, and route deaths when conditions are dangerous.

### Camp and prison transfer

Camp, gulag, prison, and forced-labor populations are moved between sites or from civilian states into sites.

This movement uses the same exact population transfer rules. It remains linked to the camp and genocide system for detention, evidence, and site processing.

### Return and repatriation

Displaced people return to the origin or another accepted home state after the cause of flight has ended and minimum safety conditions are met.

Return should be voluntary by default. Forced return is a separate policy with separate risks and condemnation.

### Local integration

A receiving country settles a displaced population into normal local life. Integration requires time, food, housing, administration, local support, and political protection.

### Third-country resettlement

A second receiving country accepts part of a displaced population from a first host. This relieves the first host and creates a new destination obligation.

## Flight-pressure model

The state flight-pressure score is built from named drivers.

### War and front pressure

Flight pressure rises through:

- enemy advance toward the state
- loss of neighboring states
- recent control change
- encirclement risk
- battle damage
- collapsing friendly army presence
- destroyed supply and medical routes
- official evacuation orders
- fear of the incoming army or ideology

The system should consider whether the country is losing the local war, not only whether it is at war somewhere.

### Strategic bombing pressure

Repeated bombing creates movement when civilian damage, infrastructure loss, housing damage, fire, and fear become material.

Bombing-related exodus should scale with:

- bombing intensity and persistence
- state population density
- shelter and air-defense protection
- housing and infrastructure damage
- recent civilian bombing deaths
- safe nearby destinations
- official evacuation capacity

A single low-impact raid should normally create fear or preparation, not a mass exodus.

### Nuclear pressure

A nuclear or thermonuclear strike creates an immediate movement request for survivors in the affected state and nearby states when fallout, fire, infrastructure collapse, or fear makes remaining unsafe.

The blast death effect resolves first. The migration system then uses the surviving population and the current route network.

Fallout can block return for a long period and can force secondary movement from an initial receiving state.

### Camp, genocide, and repression pressure

Flight pressure rises sharply when civilians face:

- concentration or extermination camps
- gulag expansion
- deportation lists
- targeted executions
- forced labor seizure
- collective punishment
- ethnic, national, religious, ideological, or political persecution
- discovered mass killing
- disappearance of neighboring communities
- occupation raids

Direct persecution overrides ordinary ideology affinity. A civilian population should not remain because the persecuting authority nominally shares its ideology.

### Famine pressure

Acute shortage creates moderate flight pressure. Famine creates strong pressure. Catastrophic famine creates mass movement attempts unless movement is blocked or the population is too weak to travel.

The poorest and most vulnerable cohorts can be less able to leave even when their desire to leave is high. The route model should represent this through transport access and vulnerability, not through a lower danger score.

### Outbreak pressure

An outbreak creates movement when people fear infection, quarantine, coercive containment, or health-system collapse.

The system should distinguish:

- voluntary flight before quarantine
- organized medical evacuation
- illegal crossing of a quarantine boundary
- border closure by neighboring countries
- forced isolation
- return after containment

Refugees and migrants are not treated as inherently diseased. An outbreak can move with a cohort only when the origin has active exposure and containment fails.

### Natural-disaster pressure

Disasters can create immediate or delayed movement:

- flood and tsunami create immediate evacuation
- earthquake and wildfire create immediate displacement
- drought and crop failure create delayed migration
- volcanic ash can create both evacuation and long-term resettlement
- severe cold and heat can create temporary movement
- repeated disasters can turn temporary displacement into permanent migration

### Occupation and ideology pressure

The ideology relationship between the population's home authority, the incoming authority, and available destinations influences fear.

The comparison is bounded.

- Similar ideologies can reduce fear when there is no evidence of persecution or brutality.
- A democratic population facing a fascist or exterminatory occupier can receive high fear.
- A population under an authoritarian government may flee toward a more protective destination.
- A population can also fear a nominally democratic or communist authority when occupation behavior, bombing, camps, ethnic policy, or prior atrocities justify it.

The model should use actual policy and campaign evidence above abstract ideology whenever the evidence is strong.

## Desire, ability, and route separation

The system should separate three questions.

### Desire to leave

Desire reflects danger, fear, persecution, famine, bombing, outbreak, and expected treatment.

### Ability to leave

Ability reflects transport, health, wealth, organization, official permission, border access, military control, and route knowledge.

### Destination availability

Availability reflects safe states, border policy, receiving capacity, diplomacy, route access, and persecution risk at the destination.

A population can have very high desire and very low ability. This creates a trapped population, which can become a major crisis.

## Destination selection

### Internal destination priority

The system should first seek an internal destination when one is valid.

A valid internal state should normally have:

- no active front or immediate control risk
- no severe famine
- no active camp or extermination threat
- no severe outbreak without reception containment
- no dangerous fallout or chemical contamination
- functioning food and transport access
- available reception capacity
- reasonable route connection

The origin country may direct the flow to a less preferred internal state through an organized evacuation. This creates efficiency gains and political costs when the destination is culturally distant or already strained.

### Foreign destination priority

When internal movement cannot resolve the pressure, the system seeks foreign destinations.

Destination weight should consider:

- border openness
- route safety
- distance
- alliance, guarantee, faction, subject, or neighbor relationship
- ideology compatibility
- cultural, linguistic, national, religious, or family ties where the repository can support them
- existing diaspora or prior flow
- reception capacity
- food security
- absence of war, bombing, camps, outbreak, and contamination
- willingness to accept the specific cohort
- risk of forced return
- diplomatic pressure from the origin or other powers

No one factor should dominate every case.

### Maritime destination

Island and coastal evacuation can use maritime routes when:

- a functioning port exists or an emergency embarkation point is available
- convoys, fuel, and escort exist
- the destination has a receiving port
- naval danger is acceptable or an armistice corridor exists

Maritime routes can carry larger cohorts but risk heavy route deaths when attacked or overloaded.

### Third-country destination

A host can negotiate resettlement with another country when the first host is over capacity, the displaced cohort cannot safely return, and the third country accepts the transfer.

## Border policy

Border policy is a country posture that changes movement resolution.

### Open humanitarian entry

The country accepts valid endangered cohorts and distributes them through its reception network.

Benefits:

- lower trapped-population deaths
- diplomatic trust
- lower condemnation risk
- potential long-term labor and population gain

Costs and risks:

- food, shelter, transport, and medical burden
- local political pressure
- outbreak containment needs when exposure is proven
- security screening demands

### Controlled entry

The country uses quotas, screening, priorities, or limited crossing points.

It can prioritize vulnerable groups, ideological allies, skilled workers, co-nationals, or family reunification. Excluded cohorts can remain trapped.

### Transit only

The country allows movement through its territory toward another destination but does not offer long-term settlement.

Transit needs route access, transport, food, and a confirmed onward destination. A failed onward agreement creates a stranded population.

### Emergency quarantine entry

The country accepts an exposed cohort into controlled reception and medical isolation.

This is more expensive than closure but can reduce deaths and avoid uncontrolled spread.

### Closed border

The country refuses ordinary entry.

Closure can lower immediate reception load. It creates:

- trapped population pressure
- irregular crossings and smuggling
- diplomatic incidents
- possible route deaths
- domestic political conflict
- public or hidden condemnation when the danger is known and severe

A border closure should not make the people disappear.

### Violent pushback

The country uses force to stop or return crossings.

This can create deaths, evidence, condemnation, and hostile relations. It can also radicalize the displaced cohort and the origin population.

### Forced return

The host sends a displaced population back to the origin.

Forced return is high risk when the origin remains unsafe. Deaths during the return route use the forced-displacement reason. Later deaths from famine, camps, bombing, or outbreak return to their owning reason.

## Trapped populations

A trapped population exists when desire to leave is high but no safe and permitted route is available.

The modifier can appear:

- in the origin state
- at a border state
- in a port or transit state
- around a camp or ghetto
- in a besieged city

Trapped pressure increases through:

- closed borders
- destroyed transport
- hostile patrols
- quarantine without aid
- weather
- famine
- bombing
- camp raids
- lack of shelter

It falls through:

- a humanitarian corridor
- border opening
- organized transport
- third-country acceptance
- danger reduction in the origin
- local relief

Trapped populations can suffer deaths from famine, outbreak, exposure, bombing, occupation, or forced displacement. The proximate cause determines the Deaths reason.

## Population transfer and state effects

### Origin state

A substantial outward flow can create:

- labor shortage
- abandoned farms
- reduced factory workforce
- lower local construction and repair capacity
- depopulated housing districts
- lower immediate food need
- lower recruitable population
- political radicalization among those left behind
- property and return claims

The effect should scale with the share of state population moved, not only the absolute number.

### Destination state

A substantial inward flow can create:

- shelter pressure
- food and water pressure
- sanitation and medical pressure
- transport congestion
- local labor supply
- new political support or opposition
- demand for schools, administration, and policing
- relief institutions
- tension with existing population

A destination with adequate capacity and support can turn the flow into a long-term benefit.

### Transit state

A transit state can face short-term congestion without receiving permanent population. It needs food, rail, port, policing, and medical support.

### Exact transaction rule

The implementation needs a shared exact population transfer adapter.

The design contract is:

1. Validate origin, destination, amount, route, and responsible authority.
2. Calculate the maximum safe origin debit above the protected floor.
3. Apply the exact origin civilian population reduction.
4. Resolve route deaths separately.
5. Add only the surviving amount to the destination state.
6. Reconcile any recruitable-manpower side effects on both sides.
7. Record origin, destination, cause, cohort, amount, and date.
8. Refresh origin and destination modifiers.

The implementation agent must inspect current vanilla and repository behavior for positive state population changes before finalizing the helper.

## Route deaths

Movement should not kill civilians by default.

Route deaths can occur when the route has one or more proven hazards:

- active combat
- bombing
- naval attack
- minefields
- severe weather
- starvation or lack of water
- outbreak exposure
- forced march
- overcrowded transport
- violent border enforcement
- contaminated terrain
- destroyed bridge or rail route
- forced return to a dangerous origin

The loss scales with moved population, route duration, vulnerability, transport quality, escort, shelter, food, medical support, and coercion.

The visible Deaths reason is `From forced displacement` for coercive or route-exposure deaths that do not belong to another more direct cause.

## Government choices at the origin

### Organize evacuation

The country selects a valid destination, assigns transport, and moves a bounded cohort.

The action can prioritize vulnerable civilians, industrial workers, administrative staff, or the general population.

### Support spontaneous flight

The country opens routes, provides information, and offers limited transport without full control.

This is cheaper but creates more congestion and route risk.

### Hold the population in place

The country restricts movement to preserve labor, production, secrecy, or control.

This can reduce immediate outflow. It increases trapped pressure and responsibility if the state remains dangerous.

### Close internal exits

The country uses police or military control to prevent movement from a state.

This can protect other states from uncontrolled inflow or outbreak exposure. It can also create deaths and resistance.

### Seek a corridor

The country negotiates with an enemy, neutral state, faction partner, or international relief actor.

The corridor can support food relief, evacuation, or both.

### Forced relocation

The country removes a population for security, ideology, occupation, labor, or settlement policy.

This creates attributed repression and can integrate with camps, gulags, occupation, and genocide systems.

## Government choices at the destination

### Receive and shelter

The country accepts the flow and assigns temporary shelter.

### Distribute arrivals

The country moves arrivals from an overloaded border or port state into several safer states.

### Prioritize entry

The country accepts selected cohorts first.

### Establish controlled reception

The country creates screening, registration, quarantine, or security facilities.

This can improve order and outbreak containment. Harsh or discriminatory use can create internment, forced labor, or atrocity consequences.

### Integrate labor and families

The country begins local integration. This consumes capacity and time, then converts the displaced modifier into normal population and labor.

### Maintain transit status

The country supports onward movement without integration.

### Close the border

The country blocks new inflow and accepts the consequences at the frontier.

### Return or expel

The country sends people back or to another state. Safe voluntary return differs from coercive expulsion.

### Aid the origin

The country spends resources to make return possible by improving food, housing, medical support, transport, or safety in the origin.

## Reception capacity

Reception capacity should be derived from real country and state conditions.

Positive factors include:

- available food and supply
- infrastructure and rail
- ports and convoys
- housing and building capacity
- civilian factories available for relief
- medical capacity
- stability and administration
- safe states away from the front
- prior relief institutions
- international aid

Negative factors include:

- famine or acute shortage
- active war damage
- outbreak
- contamination
- high existing displaced population
- low infrastructure
- damaged housing
- domestic political crisis
- hostile local policy

A large country with safe interior states should usually have more capacity than a small damaged state. It should still need transport and distribution.

## Ideology and identity model

Ideology influences migration through three bounded channels.

### Expected treatment at the origin

People are more likely to flee an authority associated with direct persecution, camps, forced labor, political terror, ethnic targeting, or hostile occupation.

### Expected treatment at the destination

People are more likely to choose a country that protects their political, national, religious, or social identity.

### Host selection policy

Governments can favor ideological allies, co-nationals, skilled workers, vulnerable groups, or politically useful exiles.

The system should avoid simplistic mappings. Fascist states can accept co-national refugees while rejecting other groups. Communist states can welcome political exiles while restricting people seen as hostile. Democracies can close borders despite public sympathy. Neutral or non-aligned states can become major humanitarian hosts.

## Movement and military gameplay

The system should interact with war without becoming a free military exploit.

- Evacuation can preserve population and labor but consumes transport needed by the army.
- Depopulated states can be easier to supply but harder to repair and defend.
- Incoming populations can support labor and recruitment only after settlement and legal integration.
- Refugees do not immediately become free manpower.
- A government can recruit volunteers or exile formations through separate decisions and political conditions.
- Forced recruitment from displaced populations creates coercion, resistance, and condemnation risks.
- Refugee corridors can become military targets or diplomatic commitments.

## Return conditions

Voluntary return requires a minimum safety package:

- the original immediate danger has ended
- the origin is controlled by an authority the cohort can safely live under
- no active camp, genocide, or targeted persecution threat remains
- food security is above the mortality stages
- housing and basic infrastructure exist
- fallout and contamination are below the return limit
- an actual route exists
- the displaced population is not prevented from leaving by the host

A cohort can refuse return when persecution memory, changed borders, destroyed homes, or host integration makes return unattractive.

## Postwar durable outcomes

### Voluntary return

The origin regains population and labor. The host loses reception pressure. The return flow can receive reconstruction support.

### Local integration

The host gains normal population and eventual economic benefit. The origin retains a diaspora and can receive remittance, political, or claim-related events if the repository supports them.

### Third-country resettlement

The original host shares the burden with an accepting country.

### Prolonged displacement

The population remains in temporary status. Long duration increases political pressure, radicalization risk, lost education and labor, and the chance that temporary settlements become permanent.

## Category unlock and cleanup

The first proven flow records migration accounting and presentation context through `migration_register_initial_incident`; it does not create an event object, event ID, event-pool entry, event-log row, random event, or pacing pulse.

The decision category unlocks after a sustained issue threshold. It can close when:

- no meaningful active flows remain
- no trapped population remains
- return or integration is complete
- the recent incident window expires

The category can reopen later without losing historical memory.

## Event 149 absorption

The catalog entry `Immigrations` should not remain a separate random population-drain event.

Its useful premise should be absorbed into the separate mechanics through explicit adapters as:

- ordinary spontaneous migration incidents
- politically driven emigration
- skilled-worker or ideological exile flows
- receiving-country responses
- long-term integration or return

Event 149 is retired and must not be replaced by an incident event or flat population reduction. The deleted famine and migration incident event files and constants are deliberate, and all earlier incident-event or incident-option probability wording is superseded.

## Acceptance outcomes for migration

The migration design is complete only when:

- origin and destination population changes reconcile exactly
- movement is never counted as death
- dangerous route deaths are separate and attributed
- internal displacement, international flight, evacuation, deportation, return, and integration have distinct behavior
- bombing, nuclear, camps, genocide, famine, outbreaks, occupation, disasters, and war loss can generate flows
- borders can open, control, quarantine, transit, close, push back, or force return
- closed borders create trapped populations instead of deleting the flow
- ideology is one bounded factor and direct persecution can override it
- receiving states gain both burden and possible long-term benefit
- the decision category is hidden until displacement becomes a sustained issue
- only a few current actions are visible
- AI can choose destinations, reception policies, corridors, and durable outcomes
- Event 149 no longer competes with the shared model
