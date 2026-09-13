# Player Experience and Design Pillars

## The first thirty seconds

The entry event should establish three facts immediately.

First, the heat is worldwide. The player should see that this is not one state suffering a local modifier.

Second, the crisis is uneven. A desert front, crowded capital, damaged grain belt, and northern mountain state should not receive the same pressure.

Third, the event will last long enough to require a plan. The player should understand that emergency decisions can reduce harm but cannot protect every system at once.

The opening presentation should therefore show:

- the current Global Heat Wave Intensity and its initial trend
- a concise national exposure summary
- the three most exposed owned or controlled states
- one immediate choice of national protection priority
- one practical first action based on the country's actual weakness

The first screen should not show the full internal formula or a list of ten future disasters.

## The two-value rule

The player actively tracks only two event-specific values.

### Global Heat Wave Intensity

This is a worldwide value from 0 to 100. It tells the player how hard the global heat system is pushing every state. It has a named band, a trend arrow or word, and a short explanation of the next threshold.

### Local Heat Stress

This is a state condition. It tells the player where the heat is actually dangerous after local vulnerability and mitigation are considered. The ordinary presentation should use a qualitative band and trend. Exact internal points can appear in debug tools but should not be required for normal play.

Every other calculation should answer one of four player questions:

1. Why is this place suffering?
2. What will happen if nothing changes?
3. Which action would help?
4. What must be sacrificed to take that action?

If a value does not answer one of those questions, it stays hidden.

## Design pillars

### Uneven pressure

The event should produce a world map of different risks. Heat should follow climate and terrain, but current war damage, urban density, supply failure, water access, and preparation must be strong enough to change the result. A well-prepared desert state can outperform a badly damaged temperate city.

### Competing protection

The player cannot fully protect the army, cities, farms, industry, and transport at once. The system should offer strong measures whose opportunity costs are visible. Protection priorities should shift resources and alter which states or sectors receive mitigation.

### Gradual failure

Major consequences should have warning states. Rail throughput falls before tracks fail. Reservoir pressure rises before service collapses. Crop stress appears before famine. Unit exhaustion appears before recurring manpower loss. Environmental exposure accumulates before terrain degradation.

### Action before punishment

The event should create problems the player can influence. Severe harm should follow exposure, weak systems, bad priorities, missed missions, or a very high evolution. Random incidents can still occur, but they should use the current state to determine where and how serious they are.

### Persistent memory

Every episode ends. Temporary penalties, active reports, episode arrays, and current Heat Stress disappear through cleanup. Permanent losses do not disappear. Population loss, damaged buildings, desertification, wasteland, Famine outcomes, and Migration outcomes remain until their owning systems reverse them.

### Strategic military consequences

The event should change front management. A player who keeps attacking through an extreme desert heat surge should pay more than a player who rotates formations, protects water routes, fights at night, and uses cooler terrain.

### Ordinary life as evidence

The event should be visible through cities, farms, railways, hospitals, water queues, soldiers, ports, and work schedules. Report events should make the crisis feel global without flooding the player with disconnected flavour.

## Player loop by phase

| Phase | Main player question | Expected actions | Main risk |
| --- | --- | --- | --- |
| Onset | What is exposed first? | Choose national priority, open water measures, inspect hotspots | Spending too late because the opening appears mild |
| Expansion | Which systems get protected? | Start missions, shift army posture, protect farms or cities | Spreading resources across too many sectors |
| Surge | What can still be kept running? | Emergency rationing, rotation, closures, imports, repair | Continuing normal operations through extreme stress |
| Plateau or lull | Is this the end or a pause? | Rebuild reserves, prepare for resurgence, finish missions | Cancelling protection too early |
| Decline | Which temporary measures can be relaxed? | Phase down burdens, repair damaged networks | Removing protection before local states cool |
| Recovery | What permanent damage must be addressed? | Restore water systems, rail, farms, industry, displaced people | Treating recovery as automatic cleanup |

## Failure profiles

The event should support distinct failure profiles rather than one generic bad outcome.

### Urban failure

Water pressure and hospital overload make dense cities the main crisis. Mortality, unrest, sanitation, and internal displacement rise.

### Agricultural failure

Crop and livestock losses outlast the hottest days. Famine can become the main secondary crisis even after temperatures begin to fall.

### Military failure

Large armies remain concentrated in extreme states. Supply consumption rises, organization recovery collapses, attrition grows, and Evolution I can cause real manpower loss.

### Infrastructure failure

Rail restrictions, power shortages, damaged roads, pump failures, and industrial cooling problems create a network cascade.

### Environmental failure

Extreme exposure remains high long enough to create persistent dryland, desertification, or rare wasteland.

A country can suffer more than one profile, but the player-facing category should identify the current dominant risk and the next most urgent hotspot.

## Success profiles

Success does not mean eliminating heat. A strong response should produce visible comparative success:

- lower local Heat Stress than similarly exposed neighbors
- protected capital water service
- no prolonged lethal state
- completed harvest protection
- maintained rail corridors
- rotated armies without losing a front
- fewer deaths
- no Famine request or a contained Famine request
- safe Migration reception or no forced movement
- no permanent terrain degradation
- faster recovery with less repair burden

## Replay value

Repeatability should come from changing world conditions, not random text alone. A later episode may target a different strategic weakness because wars, borders, cities, damaged infrastructure, deserts, migration, and prior mitigation have changed.

The same country should not receive the same optimal plan every time. A peaceful industrial state may protect cities during one episode, then prioritize the front during a later war. A country that lost a grain belt to desertification may become import-dependent and vulnerable to embargo during the next episode.

## Design rejection tests

Reject an implementation when any of these are true:

- every state receives the same modifier
- intensity rises in a straight line and then ends
- a country can buy every response with political power
- the best strategy is to click every decision
- state reports fire without matching local conditions
- Evolution I kills population without a visible lethal state
- famine or migration is duplicated inside Event 51
- a wildfire creates both Event 013 contamination and a second heat-owned contamination amount
- temporary Heat Stress remains after cleanup
- permanent terrain change can occur without sustained prior exposure
- the player must monitor more than the two accepted public values
