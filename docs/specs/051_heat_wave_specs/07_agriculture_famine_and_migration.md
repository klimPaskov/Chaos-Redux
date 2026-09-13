# Agriculture, Famine, and Migration

## Agriculture design role

Agriculture turns the Heat Wave from a short tactical emergency into a crisis that can outlast the peak. Crop damage, livestock stress, irrigation competition, post-harvest spoilage, and transport disruption should create delayed food pressure.

Event 51 does not own a universal food system. It produces validated heat pressure and sends it to the shared Famine system.

## Hidden agricultural pressure

Each relevant state can calculate an internal Agricultural Heat Pressure from:

- Local Heat Stress
- consecutive severe days
- terrain and land-use proxy
- existing aridity and degradation
- water condition
- infrastructure and supply
- war damage and occupation
- current harvest-protection measures
- regional amplification
- active wildfire or drought effects
- labor disruption
- transport and cold-storage proxy

The value remains hidden. The player sees a state status and any active harvest mission.

## Agricultural state roles

The event should classify states by practical role rather than assuming every non-urban state is farmland.

Suggested roles:

- major grain or staple belt
- irrigated agricultural state
- livestock-heavy rural state
- mixed rural state
- low-agricultural relevance
- already degraded or desert state

Use existing state resources, buildings, terrain, population, maintained registries, or event-owned curated groups only when the live repository supports them. Do not invent a global agricultural state map without a documented source and maintenance plan.

## Crop stress progression

### Early stress

- higher water demand
- lower labor efficiency
- planting or harvest delays
- reduced expected yield

### Severe stress

- flowering or reproduction failure represented through stronger expected harvest loss
- irrigation restrictions
- crop abandonment
- increased food import demand

### Prolonged extreme stress

- major harvest failure proof
- soil and vegetation damage
- Famine incident request
- Migration pressure from rural livelihoods
- Evolution II environmental exposure gain

The event should avoid immediate famine on the first hot week. Food consequences need exposure, vulnerability, and failed protection.

## Livestock

Livestock reports and pressure can include:

- higher drinking-water demand
- reduced feeding and movement
- emergency slaughter
- transport toward cooler states
- disease vulnerability from crowded watering points
- mortality during prolonged extreme conditions

Livestock loss should feed agricultural pressure and Famine demand. It should not create a separate animal stockpile or mortality ledger.

## Irrigation conflict

Water allocation should connect cities, farms, industry, and the army.

The national priority system determines which sector receives the strongest protection. A country that protects population centers may reduce immediate urban deaths but allow agricultural pressure to rise. A country that defends the harvest may accept stricter city rationing or lower industrial output.

The player should see these consequences in decision tooltips and hotspot summaries.

## Harvest protection action

A state-targeted harvest protection project can include:

- emergency irrigation allocation
- night harvesting
- temporary labor movement
- livestock relocation
- protected seed and fodder reserves
- repair of canals and pumps
- rail priority for food movement

Possible costs:

- civilian factory burden
- motorized equipment
- trains
- fuel
- manpower
- temporary urban water pressure

The action must use no more than four spendable cost types.

## Harvest mission

Working mission role: **Protect the [Named Agricultural Region] Harvest**.

Suggested duration: 120 to 180 days.

Success requires a combination of:

- target states remaining below a catastrophic agricultural pressure threshold
- functioning supply or rail access
- completed water allocation
- no prolonged Scorched exposure
- enough transport capacity

Partial success is valid when some states are protected and others fail.

Success can:

- reduce or prevent a Famine incident request
- preserve environmental resilience
- reduce recovery time
- improve food-safety projections for Migration

Failure can:

- submit a Famine request with proof
- increase Migration pressure
- create a harvest-failure report
- increase environmental exposure

## Famine adapter contract

Event 51 publishes a proof-carrying incident package. The live implementation should match the owner API exactly.

The package should contain or prove:

- source event identity `051`
- current episode generation
- target state
- current controller and owner validity
- Agricultural Heat Pressure stage
- water condition
- duration of severe exposure
- transport and relief condition
- current mitigation
- whether a prior request for the same incident generation exists

Famine decides:

- whether the request is accepted
- Food Security stage movement
- Food Reserves and Relief Access behavior
- famine mortality
- relief decisions
- famine recovery

Event 51 must never write Famine's primary ledger directly.

## Famine timing

A heat-triggered Famine request should normally require:

- a major agricultural state or an already vulnerable food system
- prolonged Dangerous, Extreme, or Scorched stress
- severe water pressure or crop damage
- weak transport or imports
- failed or absent harvest protection
- no adequate relief path

A country already experiencing Famine can receive an intensification fact rather than a duplicate new incident.

Food pressure can continue after global intensity falls. Famine owns that continuation.

## Migration adapter contract

Heat displacement should use the shared Migration system.

Event 51 can submit requests for:

- internal movement from a Scorched or water-failed state
- cross-border survivor flight when no safe internal destination exists
- organized evacuation before a severe surge
- return or resettlement after the state becomes safe

The request should prove:

- origin state
- hazard stage and trend
- projected hazard duration
- water and food condition
- current population and protected floor
- valid destination-safety facts when available
- no duplicate cohort request
- whether movement is voluntary, organized, trapped, or emergency flight

Migration owns cohort size, route, reception, settlement, return, and movement mortality.

## Destination safety publication

Event 51 should publish a versioned heat-safety fact for destination selection:

- current Local Heat Stress band
- trend
- projected episode duration band
- water condition summary
- environmental degradation stage
- active wildfire or disaster conflict

This allows Migration to avoid moving people from one lethal state into another.

A mountain or northern state can be safer, but reception capacity still matters. The event should not treat cooler land as unlimited empty space.

## Trapped population feedback

Migration can return a versioned trapped-population or reception-demand receipt. Event 51 can use it to:

- increase local water pressure
- increase cooling-center load
- increase food pressure
- raise hotspot priority
- unlock a corridor or reception mission

It must not read Migration's private cohort ledger directly.

## Movement and population accounting

Movement is not a second death source. Event 51 should not debit population when Migration already transfers it.

Heat mortality at origin and forced-displacement mortality on route require separate proven transactions and separate Deaths reasons through their owning systems.

## Recovery and return

As states cool, Event 51 publishes improved hazard facts. Migration decides whether voluntary return, local integration, or continued settlement is valid.

Permanent desertification or wasteland can keep the origin unsuitable after the Heat Wave ends. In that case, return should not become automatic merely because global intensity reached zero.

## Cross-event food pressure

### The Great Embargo

A country under Event 50 embargo should have weaker emergency food imports, fuel access, spare parts, and foreign relief. Heat Wave should read public embargo facts rather than recreating sanctions.

### Industrial Boom and Great Depression 2.0

An overheated boom can raise industrial and water competition. A depression can reduce mitigation capacity and imports. Event 51 should use owner-published state or country facts where available.

### Natural Disasters

Wildfire, drought consequences, and damaged infrastructure can raise Famine proof. Event 51 should avoid duplicating the disaster's direct damage.

## AI behavior

Agricultural AI should prioritize harvest protection when:

- the country depends on a small number of key agricultural states
- food security is already weak
- imports are blocked
- major cities depend on the same region
- the Heat Wave is expected to last

AI should not spend its last trains or trucks on a low-value harvest mission while a capital water system or active front is collapsing.

## Acceptance cases

1. A short moderate Heat Wave lowers output pressure but does not automatically create Famine.
2. A long Evolution II episode can submit a strong Famine request after harvest protection fails.
3. Famine records the stage and any mortality, not Event 51.
4. A Scorched rural population can create a Migration request without Event 51 directly moving population.
5. A safe mountain destination can be rejected when reception capacity or food safety is inadequate.
6. An embargoed country finds emergency imports less effective through the embargo system's public facts.
7. Permanent desertification can keep a return route unsafe after heat recovery.
