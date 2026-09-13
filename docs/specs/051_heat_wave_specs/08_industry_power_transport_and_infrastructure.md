# Industry, Power, Transport, and Infrastructure

## Design goal

Heat should create a network problem. Factories need workers, water, power, rail, and maintenance. Railways and roads need restrictions and repair. Pumps and hospitals need electricity. Ports and dockyards need labor and water. A country should be able to preserve selected networks, but keeping everything at full output should increase the risk of permanent damage.

## Industrial cooling pressure

Each industrial state can calculate hidden Cooling and Power Pressure from:

- Local Heat Stress
- factory and dockyard count
- resource extraction
- active construction
- population and worker load
- power-system proxy
- water condition
- infrastructure
- recent damage
- night-shift conversion
- national protection priority
- regional amplification

This pressure remains internal. The player sees one of several sector statuses and any active maintenance decision.

## Factory effects

### Strained heat

- modest factory and construction reduction
- increased maintenance reports
- lower worker efficiency

### Dangerous heat

- material factory, dockyard, and construction reduction
- higher risk of local shutdown report
- stronger water competition
- power and transport pressure

### Extreme heat

- severe output loss without protection
- risk of actual building damage after confirmed exposure
- higher accident and machinery-failure incidents
- larger night-shift benefit and cost

### Scorched heat

- sustained ordinary production becomes unsafe
- temporary shutdown may be the least damaging option
- unprotected states can lose building levels or infrastructure
- Evolution III can create abandonment pressure in the worst states

The event should avoid directly deleting large numbers of factories through an ordinary pulse. Actual building damage must follow prolonged exposure, failed protection, and a bounded incident or degradation transaction.

## Night-shift conversion

A country or state can shift heat-sensitive work toward cooler hours.

Benefits:

- lower worker exposure
- lower daytime industrial pressure
- reduced risk of machinery and rail failure
- lower Local Heat Stress contribution from industrial load

Costs and drawbacks:

- temporary conversion disruption
- command or administrative burden
- lower efficiency where lighting, transport, or security is weak
- possible air-operation or rail-schedule conflict
- less effect when nights remain extremely hot

Night-shift conversion should weaken during high nighttime retention and Evolution III.

## Controlled shutdown

A player can close selected high-risk factories, mines, or construction sites before failure.

This is a real sacrifice:

- immediate production loss
- lower water and power demand
- reduced building-damage risk
- faster recovery

A controlled shutdown should be stronger than a small passive modifier. It should protect named industrial hotspots and remain for a defined period or until the state cools.

## Power-system pressure

HOI4 may not expose a universal electricity system. Event 51 should represent power stress through state and country effects tied to industry, pumps, transport, and hospital service.

Power pressure rises with:

- high industrial and urban load
- high Heat Stress
- damaged infrastructure
- low fuel or resource access
- drought or low cooling-water fact where available
- simultaneous regional heat

Power failure can worsen:

- water pumping
- hospital capacity
- factory output
- railway and port throughput
- cooling centers

The event should not create a public power meter.

## Railways

Railways should receive a staged heat response.

### Monitoring stage

- hotspot identification
- minor throughput pressure
- maintenance action becomes available

### Restriction stage

- lower railway and supply throughput
- slower movement or strategic redeployment through the affected corridor
- higher train demand
- speed-restriction report

### Damage stage

- actual railway or infrastructure damage after prolonged severe exposure or a failed mission
- local repair mission
- possible supply cascade at fronts and cities

Railway maintenance should include period-appropriate actions such as inspections, reduced speed, adjusted schedules, ballast and track work, protected work crews, and priority repair materials.

## Critical corridor mission

Working mission role: **Keep the [Named Corridor] Operational**.

Suggested duration: 120 to 180 days.

Target selection should identify a corridor that matters to at least one of:

- capital supply
- active front
- major port
- major agricultural region
- major industrial cluster
- evacuation or relief route

Success requires the relevant rail and infrastructure links to remain above a supported condition threshold and the country to commit trains, equipment, or civilian capacity.

Failure should cause real corridor degradation or a serious throughput penalty. It should not merely remove a tiny amount of political power.

## Roads and infrastructure

Severe heat can degrade roads, bridges, and general infrastructure through expansion, surface damage, heavy emergency traffic, and maintenance overload.

Effects should be gradual:

- reduced state infrastructure efficiency
- increased repair burden
- local infrastructure damage after confirmed extreme exposure
- slower relief and migration routes

Infrastructure damage should use an existing shared helper when it fits. A random-state building-damage helper should not be used blindly because Heat Wave targets condition-linked states, not arbitrary ones.

## Ports and waterways

Heat and low water can affect ports and inland waterways through:

- reduced loading productivity
- worker exposure
- lower river or reservoir access where represented by local pressure
- increased water competition
- repair and dredging burden
- convoy and import delays

The event should avoid claiming exact river-depth simulation when the map system does not expose it. Use state-based port and supply effects.

## Resource extraction

Mines, oil fields, and other extraction sites can suffer through:

- worker heat exposure
- machinery overheating
- water demand
- transport bottlenecks
- controlled shutdowns

Resource extraction penalties should scale with the state's extraction importance. A state with no resources should not receive a mining report.

## Building damage thresholds

Actual damage should require:

- Extreme or Scorched Heat Stress
- minimum uninterrupted exposure
- high sector pressure
- failed or absent protection
- valid building target
- per-state and per-building cooldown
- episode damage cap

Possible targets:

- infrastructure
- railways
- civilian factories
- military factories
- dockyards
- airbases
- supply hubs only if the engine and repository support safe damage and repair behavior

Building damage must not target a building type absent from the state.

## Recovery

A damaged state enters one of three recovery profiles:

### Automatic reopening

For states that only received temporary output reductions.

### Assisted restoration

For states with severe water, power, rail, or industry pressure but little direct damage. Decisions can shorten recovery.

### Reconstruction

For states with actual building or infrastructure loss. Recovery uses normal repair plus event missions and owner-system support.

The Heat Wave can remove temporary penalties. It must not restore destroyed buildings for free during cleanup.

## AI behavior

Industrial AI should choose protection based on strategic value.

- War economy prioritizes military factories, supply corridors, and ports.
- Import-dependent countries prioritize ports, rail, and power.
- Agricultural countries prioritize rail from food regions.
- Urban industrial majors protect capital utilities and the largest industrial cluster.
- Low-industry minors should not spend more on complex industrial mitigation than the exposed sector is worth.

AI should prefer controlled shutdown when expected damage exceeds the value of short-term output.

## Acceptance cases

1. Rail throughput falls before actual rail damage.
2. A maintenance mission can prevent damage at a meaningful resource cost.
3. A controlled factory shutdown protects buildings but visibly sacrifices output.
4. Hot nights reduce the benefit of night-shift conversion.
5. An industrial state with failed power worsens its water and hospital pressure.
6. A resource report never targets a state with no relevant extraction.
7. Cleanup removes temporary output penalties but does not rebuild damaged factories.
