# Famine and Migration Mechanics

## Part 2: Famine and food security

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

> **Superseded incident-layer and probability note (2026-08-25):** Any wording in this historical specification about incident events, event-option probability, `famine_incident.1`, `migration_incident.1`, `fm_*`, or combined `famine_migration_*` planning IDs is superseded. The register helpers are accounting/presentation seams only; the incident event files and constants were deliberately deleted.

## Food security model

Food security is evaluated at state level. The system does not attempt to simulate every farm, calorie, or market transaction. It combines the pressures that matter for gameplay into a dynamic state condition with clear causes and a meaningful mortality result.

Each active state has four conceptual components:

- food availability
- access and distribution
- population vulnerability
- relief and recovery capacity

The state becomes dangerous when availability and access remain below need while vulnerability rises faster than relief can compensate.

## Pressure composition

The hidden famine pressure score should be built from named components. The player sees the major contributors in the state modifier tooltip or a concise report.

### Local production pressure

Local production pressure rises through:

- drought
- flood
- locusts
- wildfire
- volcanic ash
- severe cold or heat
- crop disease
- chemical contamination of land or water
- radioactive fallout
- labor loss from death, conscription, displacement, camps, deportation, or outbreaks
- destruction of infrastructure required to gather and distribute food
- abandoned rural districts

Production pressure should be state-specific. A disaster in one state should not create the same local production loss in every state of the country.

### Import and transport pressure

Import and transport pressure rises through:

- loss of a normal land corridor
- isolated island or enclave status
- damaged ports
- convoy shortage
- naval blockade
- hostile control of nearby sea zones when the route actually depends on them
- rail damage
- destroyed supply hubs
- damaged infrastructure
- fuel shortage
- shortage of trains or trucks
- strategic bombing of transport and storage
- embargo or sanctions where the country depends on imported food or inputs
- occupation boundaries that block internal movement
- quarantine that closes a route without replacing it with relief access

A country that is self-sufficient and has functioning internal routes should not receive a large famine penalty from a diplomatic embargo alone. The system should prove import dependence or an actual transport deficit before applying that pressure.

### Extraction and policy pressure

Extraction and policy pressure rises through:

- occupation requisition
- forced grain procurement
- confiscation of private reserves
- collective punishment
- military priority rationing that excludes civilians
- camp and gulag ration deprivation
- forced labor quotas that reduce local food production
- deportation of agricultural workers
- scorched-earth policy
- destruction of stored food
- deliberate obstruction of relief
- falsified production reports
- corruption or black-market diversion
- politically unequal rationing

Policy pressure is attributed to the responsible authority. It can create hidden atrocity evidence before it becomes public.

### Population need pressure

Population need pressure rises through:

- large incoming displaced populations
- returning populations before housing and food recover
- urban crowding
- camp expansion
- demobilization into damaged states
- loss of nearby productive states
- concentration of civilians in a besieged city
- evacuation into a receiving state with low capacity

Population need pressure should use the current state population after migration and deaths. A receiving state can move from safe to strained if arrivals exceed its capacity.

### Environmental system pressure

Air Cleanliness is a global environmental pressure that modifies the food system.

The design uses four bands:

- Below 25 percent contamination, local sources dominate and normal recovery remains available.
- At 25 percent and above, crop shocks spread more easily and recovery becomes slower in already affected states.
- At 50 percent and above, mild nuclear-winter and sunlight-loss conditions can add broad production and transport pressure during active winter periods.
- At 75 percent and above, severe food-production pressure can affect many active states, especially states already damaged by war, ash, fallout, or transport collapse.
- At 100 percent, ordinary recovery is no longer sufficient. Protected enclaves, sealed facilities, exceptional technology, external food stocks, or evacuation are required to prevent severe decline.

Air contamination should not create famine deaths in every state through a global flat tick. It should increase the pressure of states already in the active registry and make new food-security requests more likely when a state also has local vulnerability.

Famine does not directly reduce Air Cleanliness. Burning crops, wildfires, ash, chemical releases, radioactive fallout, and other physical sources can do so through their owning systems.

## Food security stages

### Supply strain

Supply strain is the first visible stage.

Typical effects:

- mild local construction and production disruption
- reduced local recruitment recovery
- higher consumer and administrative burden
- increased risk of protests or flight when another shock occurs
- no automatic famine mortality

The state can recover through routine transport repair, imports, rationing, or local substitution.

### Acute shortage

Acute shortage means normal distribution has failed for a material share of the population.

Typical effects:

- noticeable state output loss
- lower local construction and repair speed
- reduced organization of civilian administration
- higher disease and flight pressure
- limited civilian deaths may occur from malnutrition-related vulnerability only when exposure persists and protection is weak
- relief decisions and state missions become urgent

The system should distinguish limited acute-shortage mortality from full famine mortality. The Deaths breakdown still uses `From famine` when hunger is the proximate cause.

### Famine

Famine is a mortality stage.

Typical effects:

- significant recurring civilian population loss
- sharp local production and construction penalties
- worsening disease vulnerability
- strong civilian flight pressure
- serious political opposition or resistance pressure
- possible garrison and unit supply problems when the same route supports the army
- international relief or condemnation events

Ignoring a state at this stage should create deaths large enough to matter at country and world scale.

### Catastrophic famine

Catastrophic famine represents a state where food access has collapsed and relief is absent, blocked, overwhelmed, or deliberately denied.

Typical effects:

- very high recurring civilian population loss
- severe depopulation
- rapid labor and production collapse
- mass displacement attempts
- trapped-population deaths when borders and routes are closed
- high opposition, mutiny, separatist, or revolutionary pressure
- public or hidden atrocity evidence when policy contributed
- possible collapse of local administration

Catastrophic famine must remain recoverable while the state retains enough population and a valid relief route. Recovery should require several actions or a major change in the military and political situation.

## Mortality model

Famine deaths are dynamic and population-scaled.

The design formula is:

```text
actual famine deaths =
state population
× stage mortality pressure
× exposure time
× vulnerability
× access failure
× policy harm
× environmental pressure
× governance failure
× protection and relief reduction
```

This is a design formula. The implementation agent should translate it into centralized script constants and reusable effects after inspecting the engine limits.

### Stage mortality pressure

The stage provides the base mortality band. Supply strain has no direct mortality. Acute shortage has a low band. Famine has a high band. Catastrophic famine has a very high band.

### Exposure time

Mortality increases when the same state remains in a dangerous stage. A newly entered famine state should not immediately receive the same loss as a state left without relief for months.

Exposure should use bounded age bands or accumulated pressure, not a simple unlimited multiplier.

### Vulnerability

Vulnerability rises through:

- prior famine or acute shortage
- outbreak activity
- chemical or radioactive contamination
- harsh weather
- camp or forced-labor population
- overcrowding
- damaged medical capacity
- high share of vulnerable cohorts
- repeated displacement
- prior bombing or disaster damage

### Access failure

Access failure reflects whether food exists but cannot reach civilians. It rises with blockade, destroyed transport, occupation boundaries, closed corridors, and administrative collapse.

### Policy harm

Policy harm reflects requisition, deliberate deprivation, forced procurement, unequal rationing, concealment, relief obstruction, and other government action.

### Environmental pressure

Environmental pressure reflects local disaster and Air Cleanliness conditions.

### Governance failure

Governance failure reflects corruption, falsified reports, poor stability, loss of control, weak administration, and unresolved local opposition.

### Protection and relief reduction

Protection and relief reduce the final loss through:

- food reserves
- functioning rail, port, convoy, train, and truck routes
- fair rationing
- emergency imports
- international relief
- local food substitution
- medical support
- shelters and sanitation
- organized evacuation
- protected humanitarian corridors
- advanced Kruger or other relevant technology where an existing system provides a credible food, transport, or environmental solution

The reduction can prevent a mortality pulse or reduce it sharply. It cannot erase deaths that have already been recorded.

### Exact population transaction

The final loss must use the existing exact state civilian population loss contract. The state returns the amount actually removed after its protected population floor is applied. The Deaths ledger records exactly that result once.

The visible Deaths reason is `From famine`.

A famine pulse cannot also call a generic population reduction path. The exact transaction owns the physical loss.

## Protected population floor

The system should protect a small residual population unless another terminal system is explicitly allowed to create a wasteland or empty state.

The floor should scale with the state and context. It should prevent a normal famine from reducing every state to zero while allowing catastrophic loss in dense states.

A protected enclave, evacuation, sealed facility, or special technology can raise the practical floor. A terminal wasteland path can use its own stronger contract.

## Island blockade model

Island and isolated coastal states require a specific famine route because their risk is often determined by shipping.

### Eligibility proof

An island blockade famine request should require evidence from several independent conditions:

- the state is a true island, archipelago state, or isolated enclave with no valid safe land corridor
- the owner or controller is at war
- the normal civilian supply route depends on a port or maritime access
- the port is damaged, blocked, occupied, or under effective hostile pressure
- the responsible country lacks sufficient convoys, fuel, escort capacity, or access
- no functioning humanitarian corridor is active
- local reserves and local production cannot cover the current population need

A single hostile ship or generic war state is not enough.

### Pressure scaling

Island pressure rises with:

- duration of isolation
- port damage
- convoy deficit
- loss of nearby friendly ports
- air and naval interdiction
- local population density
- low local production
- incoming evacuees
- winter or severe weather
- high Air Contamination
- deliberate refusal of relief

It falls with:

- convoy escort
- emergency airlift where technology and aircraft allow it
- restored port access
- seizure or opening of a nearby corridor
- relief agreement
- evacuation of part of the population
- local fishing or agricultural substitution where the state can plausibly support it

### Player responses

The state can offer a limited set of relevant actions:

- organize escorted relief convoys
- repair and defend the port
- create an emergency airlift
- negotiate a neutral relief corridor
- ration and release reserves
- evacuate vulnerable civilians
- prioritize the garrison and accept civilian harm
- conceal the crisis
- refuse relief for military or ideological reasons

Each option should use concrete resources and consequences.

## Siege and encirclement model

A besieged city or state can enter famine pressure when it loses both ordinary supply and civilian escape.

The model should consider:

- state control and surrounding control
- supply hub and rail access
- port access
- duration
- winter and weather
- population density
- military stockpile priority
- evacuation possibilities
- bombardment and bombing
- relief attempts

A siege can create a trapped population modifier. If the defender blocks evacuation or the attacker refuses passage, deaths can gain an attributed policy component.

## Occupation and requisition model

Occupation can create food pressure without an explicit famine event.

The system should provide occupation-law adapters that respond to the actual law or special policy applied in the state.

Possible policy profiles include:

- protected administration with low extraction and better relief access
- normal occupation with moderate requisition
- harsh extraction with high requisition and labor pressure
- collective punishment with food denial and restricted movement
- camp and forced-labor administration
- scorched-earth withdrawal

The exact occupation laws depend on the implemented repository. The coding agent must map the profiles to real law identifiers and existing Chaos Redux laws after local inspection.

Occupation food pressure should rise when the occupier extracts from a state whose production and routes are already damaged. A well-supplied state under moderate occupation should not automatically enter famine.

## Camps, gulags, and forced labor

The camp and genocide system should call the famine system when deprivation is caused by food denial, overcrowding, transport failure, or labor exhaustion.

The owner of each death is determined by proximate cause:

- starvation and malnutrition use `From famine`
- execution, gassing, extermination processing, and direct killing remain atrocity deaths
- fatal forced labor uses `From forced labor`
- deaths during deportation or transfer use `From forced displacement`
- disease deaths use the outbreak or disease reason when disease is the proximate cause

This split prevents double counting and allows the player to see how the same camp network kills through several mechanisms.

A gulag expansion can also remove agricultural labor from origin states, increase local food pressure, and create migration or deportation flows.

## Outbreak interaction

Outbreaks can worsen famine through:

- loss of labor
- quarantine of transport routes
- medical system overload
- mortality among transport and agricultural workers
- closure of markets and ports
- panic buying and local distribution failure

Famine can worsen outbreaks through:

- malnutrition
- crowding at relief centers
- unsafe water and sanitation
- weakened medical capacity
- long displacement routes

The system should not treat refugees as an inherent disease source. An outbreak can travel with a cohort only when the origin has active exposure and the route or destination lacks containment.

## Nuclear and thermonuclear interaction

A nuclear strike can create three distinct food-security effects:

- immediate loss of local production and storage
- fallout contamination and evacuation
- global or regional climate pressure through Air Cleanliness and nuclear winter

The immediate blast deaths remain nuclear deaths. Later starvation caused by destroyed food access uses `From famine`. Fallout deaths remain fallout deaths.

This distinction lets the Deaths tab show the full aftermath without recording one person twice.

## Strategic bombing interaction

Strategic bombing can raise food pressure when it damages:

- infrastructure
- railways
- ports
- supply hubs
- factories involved in transport or food processing
- housing and storage

Bombing can also create immediate exodus. The famine system should receive the resulting labor loss and transport damage. It must not apply a generic famine modifier to every bombed state.

## Natural disaster interaction

The natural-disaster system should pass a famine pressure request when the disaster affects food production, water, transport, shelter, or labor.

Examples:

- drought creates production and water pressure
- flood destroys crops, storage, routes, and housing
- locusts create direct crop loss
- volcanic ash reduces crops and transport while also affecting Air Cleanliness
- wildfire destroys crops and creates smoke pressure
- tsunami destroys coastal storage, ports, and routes
- severe cold increases need and blocks transport
- heat wave reduces water, labor, and crop output

The disaster remains the owner of its immediate deaths and physical damage. The famine system owns later hunger deaths.

## Relief system

Relief should be a real logistical effort.

### Domestic relief

Domestic relief can use:

- food reserve release
- rationing
- train allocation
- truck allocation
- convoy allocation
- fuel
- support equipment
- civilian factory burden
- temporary military supply reduction
- local administration and security capacity

The player should often choose between military priority and civilian relief. This tradeoff should be visible.

### Foreign relief

Foreign relief can use:

- diplomatic access
- neutral corridor agreement
- convoys and escorts
- airlift capacity
- donor stockpiles
- receiving port and rail capacity
- inspection or observer access
- sanctions relief or temporary trade exception

Foreign aid can increase trust and reduce condemnation. A regime that accepts food while blocking observers may receive less effective relief and retain hidden evidence.

### Requisition from safer states

A government can move food pressure from one state to another through requisition.

This is a valid emergency tool, but it is not free. The donor state loses reserves and may enter supply strain. Repeated use creates regional grievance and political opposition. Requisition from occupied or persecuted states can become an atrocity source.

### Evacuation as relief

Evacuating part of the population lowers need pressure in the famine state. It creates transport cost and reception pressure elsewhere. A dangerous or blocked route can create displacement deaths.

The system should never treat evacuation as a direct reduction with no destination.

## Concealment and false reporting

A government can conceal the severity of a famine or falsify production reports.

Concealment can:

- delay public events
- reduce foreign relief offers
- suppress immediate political pressure
- preserve military or diplomatic reputation for a short period
- increase actual deaths because relief is delayed
- create hidden cover-up evidence
- increase the severity of eventual exposure

False reporting can also cause central requisition to continue after local production has collapsed.

The player should see that concealment hides information. The exact hidden evidence and future exposure route should remain unrevealed.

## Political escalation from famine

Famine political pressure should grow from lived conditions and visible responsibility.

Potential outcomes include:

- bread riots
- food committees
- rural resistance
- urban strikes
- garrison mutiny
- separatist organizing
- anti-colonial mobilization
- religious relief networks challenging the state
- opposition parties gaining support
- local authorities refusing requisition
- mass desertion from forced-labor sites
- revolutionary cells recruiting among displaced people

The strongest movement is selected from credible local and national actors. A state with no communist presence should not spontaneously become communist only because people are hungry.

The system can create new opposition support when the existing political structure leaves no credible channel, but the result should still follow the country's ideology, region, prior movements, foreign influence, and state identity.

## Recovery progression

Famine recovery uses several steps:

1. Stop the worsening source.
2. Restore access or reduce population need.
3. Maintain relief long enough to leave the mortality stage.
4. Repair production and transport.
5. Resolve displacement and labor loss.
6. Settle political and evidentiary consequences.

A state can move from catastrophic famine to famine, then acute shortage, then supply strain, then normal. It should not jump directly to normal because one convoy arrived.

Recovery can fail if the route closes again, the state receives a large return flow too early, the government resumes requisition, or Air Cleanliness worsens.

## Historical-profile rule

Historical profiles can alter the pressure composition, valid reports, regional memory, and AI behavior. They do not set a casualty target.

Examples include:

- Soviet grain extraction and movement restriction
- wartime Chinese drought, requisition, locust, and weak relief
- Bengal import loss, transport priority, crop shock, and administrative failure
- Greek occupation, blockade, requisition, and island flight
- Leningrad siege and winter isolation
- Dutch transport stoppage and occupied-city shortage
- Brazilian drought migration and confinement
- Ethiopian concealment, relief manipulation, and forced resettlement
- Congo conflict, forced labor, displacement, and hunger interaction

Part 5 defines these profiles and their historical cautions.

## Acceptance outcomes for famine

The famine design is complete only when:

- every active state shows a clear severity and cause breakdown
- unmanaged famine and catastrophic famine create significant dynamic deaths
- relief can materially reduce deaths
- island blockade pressure requires actual isolation evidence
- Air Cleanliness modifies food pressure and recovery
- occupation, camps, gulags, forced labor, deportation, disasters, outbreaks, bombing, nuclear aftermath, and events can call the appropriate famine or migration adapter with exact owner evidence
- exact Deaths registration uses `From famine`
- no fixed historical casualty total is used
- political opposition follows credible actors and responsibility
- recovery is gradual and can reverse
- movement caused by famine resolves through the migration system with a real destination
