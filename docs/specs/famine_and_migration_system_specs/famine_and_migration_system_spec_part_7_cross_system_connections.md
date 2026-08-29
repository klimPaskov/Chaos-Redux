# Famine and Migration Mechanics

## Part 7: Cross-system and event connections

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any wording in this historical specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Integration rule

Famine and migration are shared consequence systems. Existing events and mechanics should call them through bounded adapters with explicit actor, target, cause, severity, and proof fields.

An event keeps ownership of its own premise, stages, choices, evolutions, super-events, countries, and terminal routes. Famine owns food-security pressure and famine mortality. Migration owns civilian movement, migration-route mortality, reception burden, and return. The neutral transfer primitive owns only exact physical debit, route-death separation, and survivor credit.

The adapter model prevents parallel famine or migration logic from being reimplemented inside each event.

## Chaos Meter

### Deaths

Every famine, occupation-repression, forced-labor, and forced-displacement death enters the existing Deaths ledger.

The shared total continues to affect Chaos through the existing deaths threshold.

Migration itself does not add deaths or Chaos. Deaths caused by dangerous routes, border violence, or trapped exposure do.

### Air Cleanliness

Air Cleanliness changes the likelihood, severity, and recovery of active food-security states.

The famine system reads contamination bands and current winter or environmental states. It does not create a second global pollution value.

Migration can redistribute population away from contaminated states. Overcrowded safe states can face food and medical pressure, but the movement does not clean the air.

### Condemnation

The condemnation system receives deliberate-starvation, relief-obstruction, lethal forced-labor, deportation, violent-pushback, forced-return, camp-deprivation, and cover-up sources.

Public and hidden evidence follow the existing condemnation contract.

## Camps and genocide

The camp and genocide system connects through:

- food-deprivation requests
- labor-removal requests
- forced-labor death registration
- deportation and transfer requests
- nearby flight-pressure requests
- escapee and survivor reception
- liberation return and family reunification
- hidden and public evidence

The camp system remains responsible for site state, discovery, concealment, and tribunals.

## Chemical warfare

Chemical contamination can:

- reduce local food production
- contaminate water and storage
- increase medical and flight pressure
- block return
- create evacuation from affected states

Chemical deaths remain chemical deaths. Later hunger uses famine. Route exposure to chemical contamination uses the chemical system when it is the direct physical cause.

Civilian protective equipment, shelters, decontamination, medical support, and warning coverage can reduce both flight pressure and secondary food-system damage.

## Biological warfare and outbreaks

Biological attacks and outbreaks can:

- remove labor
- close routes
- overload medical capacity
- create voluntary flight
- create quarantine and border disputes
- increase famine vulnerability
- spread through overcrowded conditions when exposure is proven

Outbreak deaths remain outbreak deaths. Hunger deaths remain famine.

The system should give countries a controlled-reception alternative to indiscriminate border closure.

## Nuclear and thermonuclear systems

Nuclear adapters should create:

- immediate survivor exodus from the target state
- secondary exodus from fallout states
- reception pressure in safe states
- return restrictions
- local food-production and route damage
- Air Cleanliness and nuclear-winter pressure through the existing system

The nuclear system remains responsible for blast, fallout, condemnation, and direct chaos effects.

## Strategic bombing

The bombing system should request displacement when persistent damage crosses a meaningful civilian threshold.

It should also pass proven transport, housing, port, rail, and storage damage into food security.

Bombing does not create a generic refugee flow from every air mission. The adapter uses actual state impact and recent damage.

## Natural disasters

The existing natural-disaster entry point should add optional famine and displacement outputs to its resolved aftermath.

Suggested family behavior:

- drought increases food-production pressure and delayed rural migration
- flood and tsunami create immediate displacement, crop loss, and transport failure
- earthquake creates housing displacement and route damage
- locusts create direct crop pressure
- wildfire creates evacuation, crop loss, and Air Cleanliness pressure
- volcano creates evacuation, ash pressure, crop loss, and long return delays
- severe cold creates transport and need pressure
- heat wave creates water, labor, and crop pressure

Event 13 keeps ownership of its damage jobs and reports. It calls the appropriate famine or migration adapter only after exact target states and causal facts are known.

## War, peace, and occupation

### War

War creates scoped triggers through:

- front movement
- control changes
- siege and encirclement
- bombing
- naval blockade
- military requisition
- evacuation orders
- refugee arrival

A declaration of war alone should not create movement in every state.

### Peace

Peace can:

- reopen routes
- permit voluntary return
- end military requisition
- expose occupation evidence
- create border and citizenship disputes
- trigger demobilization and housing pressure
- leave unresolved camps, famine, or contamination

The peace system should not automatically return every displaced cohort on the day of peace.

### Occupation

Occupation-law changes call the shared policy profiles described in Part 4.

Liberation lowers fear and can open return, but only after food, housing, route, and persecution checks pass.

## Event 5 Soviet Collapse

This is the deepest existing event connection.

Event 5 already contains grain extraction, forced-labor quotas, gulag expansion, NKVD pressure, deportation, republic fear, and evidence themes.

Adapters should connect:

- grain extraction to food pressure
- forced-labor quotas to labor removal and forced-labor deaths
- gulag expansion to camp population, famine, outbreak, and forced labor
- deportation to exact forced movement
- movement restrictions to trapped pressure
- concealment to hidden evidence and delayed relief
- republic hunger and deportation memory to independence pressure
- collapse and civil war to internal displacement and refugee flows
- coalition intervention to relief corridors and return

The event's political and military stages remain owned by Event 5.

## Event 6 Independence Wave

Newly released countries can inherit:

- refugee inflows
- returning co-nationals
- damaged food routes
- disputed property
- sponsor relief
- border closure by former rulers
- reception burden beyond their small state capacity

Recognition and foreign-aid decisions can support relief and resettlement.

The release process should not duplicate population. A state keeps its current population, including arrivals and losses.

## Event 9 White Peace

White peace can reopen civilian routes and start voluntary return.

It should not erase occupation, camp, famine, or displacement memory.

## Event 10 Death Island and isolated-state events

An isolated island crisis can use the island-blockade and maritime-evacuation contracts when the event's world state creates human civilian populations at risk.

Special nonhuman actors remain excluded from ordinary civilian cohorts.

## Event 11 Secret Alliance

Covert coalitions can:

- sponsor refugee routes
- use camps or refugee flows as intelligence sources
- close borders to protect secrecy
- exploit displacement politically

Only concrete event content should call these adapters.

## Event 12 and Event 13 natural-disaster family

Every disaster that damages food, water, housing, or transport should use the shared aftermath adapters.

Disaster clusters should not count each famine or migration consequence as another random pacing event.

## Event 14 Cannibalism and Hunger Lines

The Hunger Lines scenario and cannibalism system can connect through:

- famine pressure as a recruitment and escalation input
- displacement and abandoned districts as territorial opportunity
- disrupted relief routes
- trapped populations
- host-country fear and border policy
- relief success reducing hunger-driven support

Cannibalism deaths remain owned by Event 14. Ordinary hunger deaths use famine.

## Event 15 Utopia Manifesto

Direct connections include:

- common stores and rationing
- blockade and shortage
- refugee districts
- open or closed sanctuary
- redistribution and local resistance
- foreign relief and inspection
- return or integration after the movement changes territory

Separate famine and migration adapters can make the Utopia premise materially affect food and movement without duplicating an event-only refugee tracker.

## Event 16 Brilliant Scientist and Kruger technology

Advanced technologies can provide bounded relief tools when their existing capabilities support it.

Possible effects include:

- improved logistics
- synthetic food or material substitution if an accepted technology supports it
- decontamination
- medical support
- advanced airlift or transport
- protected habitats

The system should not invent a new Kruger technology solely to remove famine. Any connection must use an existing or separately accepted technology.

## Event 18 cave and underground actors

Cave emergence, underground hazards, and abandoned mining regions can create:

- evacuation
- depopulated mining states
- food-route collapse
- host reception
- blocked return

Nonhuman country exclusions still apply.

## Event 19 Infantry Spawn and custom forces

Spawned armies can create displacement through battles, occupation, and state control.

The system should not classify every custom force as a civilian threat. It should use actual war, damage, occupation, and nonhuman classification.

No new combat unit is created by this system.

## Event 20 Black Plague

The plague system should connect through:

- flight from outbreak states
- quarantine reception
- closed borders
- overcrowding and sanitation pressure
- route-based spread only with proven exposure
- famine from labor and route failure
- return after containment

Rat Nations and other nonhuman actors remain excluded from ordinary civilian reception logic.

## Event 21 Random Civil War

Civil wars can create:

- rapid internal displacement
- ideological destination choice
- border flight
- return after settlement
- partitioned family and property claims
- famine through front and route damage

The event should pass the actual rebel, original country, state, and war context.

## Event 23 Soviet Nuclear Bombs

Soviet nuclear use connects through the general nuclear adapters, plus Event 5 republic and border consequences when applicable.

## Event 25 Alien Technology in Antarctica

Expedition logistics should not normally use civilian famine or migration. A failed expedition can use its own personnel consequences.

No shared civilian adapter is needed unless the event later creates a populated Antarctic settlement.

## Event 28 Asteroid Incoming

The asteroid event can create:

- immediate displacement from surviving rings
- blocked return to wasteland states
- famine from dust, transport, and crop loss
- Air Cleanliness pressure
- international resettlement

The asteroid system owns immediate impact deaths and destruction.

## Event 32 Missiles

Missile attacks can call the same bombing, chemical, biological, nuclear, and displacement adapters according to warhead type and actual target effects.

## Event 33 Acid Rain Superstorm

Acid rain can create:

- contaminated food and water
- crop pressure
- evacuation
- shelter and clean-state reception
- Air Cleanliness interaction
- delayed return

The event owns the storm route and direct effects. Famine owns later food-security consequences; migration separately owns any proven movement.

## Event 43 global flood and related flood concepts

Flooding can create large internal and international movement, damaged food routes, and permanent resettlement from uninhabitable states.

If the event creates water-covered or invalid states, the migration system must move only surviving population that can legally leave before state conversion.

## Event 50 Great Embargo

The embargo event can add food pressure only when:

- the target depends on imports
- relevant routes are actually restricted
- domestic substitution is insufficient
- relief exemptions are absent

The event should create diplomatic relief, smuggling, and third-country aid choices.

## Event 51 Heat Wave

Heat can create crop, water, labor, and migration pressure, especially in states already affected by drought, wildfire, outbreak, or high Air Contamination.

## Event 95 Occupation Revolt

Famine, deportation, forced labor, and unequal relief can increase revolt pressure.

Successful protected administration and relief can reduce it.

## Event 118 Locust Plague

This backlog event should call the shared famine system. It must not implement a separate flat famine effect.

The locust event owns swarm movement and crop damage. Famine owns food stages, relief, and famine deaths; migration separately owns any proven displacement.

## Event 120 Volcano

Volcano aftermath should call ash, Air Cleanliness, crop loss, evacuation, reception, and return adapters.

## Event 131 Mutiny

Famine, civilian starvation, unequal military rations, and failed evacuation can increase mutiny pressure.

Mutiny remains owned by its event.

## Event 141 mass-suicide concept

This system should not use famine or migration to hide or reclassify suicide deaths. It can create flight pressure and reception from threatened areas, but the death reason remains owned by the event.

## Event 149 Immigrations

Event 149 should be retired, disabled, or converted into a compatibility adapter.

Its random population drain should not remain active beside this system.

## Great Shortage and other backlog concepts

Any future shortage event should become a pressure source or narrative wrapper around the shared food system. It should not create a parallel global shortage meter.

## Disease cluster

Disease cluster members can call outbreak-flight and quarantine adapters after their own target states are resolved.

The migration consequence does not add extra cluster pacing events.

## Natural Disasters cluster

Disaster members can call food and displacement aftermath adapters.

Cluster severity can scale the initial request, but the later state progression remains dynamic.

## Liberations cluster

Liberation can open return, expose camps, and create emergency relief.

It can also trigger reverse displacement or retaliation if the new authority threatens part of the population.

## Wars cluster

War events can create movement through their actual conflicts, control changes, and damage. The cluster itself should not create a generic refugee total.

## Peace cluster

Peace events can open return and corridor settlement. They do not automatically resolve famine or reception capacity.

## Manual scenarios

Existing manual scenarios can call the famine or migration adapters when their launched world state provides the exact facts required by that mechanic.

Relevant examples include:

- Soviet Collapse
- Disaster Barrage
- Hunger Lines
- Black Plague Unbound
- Fallout or nuclear scenarios

The scenario wrapper can supply initial severity or coverage. Ongoing deaths and movement remain dynamic.

## Shared country classifiers

Ordinary civilian flows should exclude countries that pass the special Chaos country or actual nonhuman classifiers when they do not represent a normal human civilian society.

A special actor can still be:

- the cause of flight
- the military threat controlling a route
- the source of contamination
- the target of foreign containment

Human civilians living under a transformed or captured government require a documented population-transition rule before exclusion.

## World-threat aggregate

Mass famine and displacement can be consequences of world threats. They should not automatically register a new existential threat source.

A specific owning event can decide whether its famine or displacement escalation changes the shared threat aggregate.

## Event-log relationship

This system should have its own concise system history or use the Chaos Meter history where appropriate.

It should not create fake random-event history entries for every state pulse.

Suggested records include:

- state entered famine
- state entered catastrophic famine
- major relief operation
- mass evacuation
- border closure with trapped population
- mass return or integration
- deliberate-starvation evidence exposed

The Deaths tab remains the detailed death ledger.

## Documentation ownership

The final implementation should create a permanent system document under `docs/systems/` and update related event docs only where they call an adapter.

The event catalog workbook should update affected rows, especially Event 5, Event 13, Event 14, Event 15, Event 20, Event 28, Event 33, Event 50, Event 118, and Event 149, after implementation facts are known.

The three catalog CSV files remain export-only.

## Integration acceptance

Integration is complete only when:

- every listed active connection uses a shared adapter
- no event duplicates the food, movement, or death transaction
- event ownership and shared-system ownership are clear
- clusters do not create extra pacing events for consequences
- special and nonhuman country exclusions are correct
- manual scenarios can seed the system without fixed long-term casualties
- Event 149 no longer applies a competing flat migration effect
- docs and catalog wording reflect the final implemented behavior
