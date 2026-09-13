# Environmental Degradation and Terrain

## Design purpose

Evolution II and III should leave physical evidence in the world. Environmental degradation must be gradual, conditional, and rare enough that each permanent change matters.

The system should distinguish three things:

1. Temporary Local Heat Stress.
2. Persistent environmental degradation facts owned by Event 51.
3. Actual map terrain changes, which require safe engine and map-tool support.

A modifier alone cannot silently replace an accepted actual terrain change. If the map path is unavailable or unsafe, the implementation must report that terrain conversion remains blocked.

## Permanent environmental ledger

Each state can hold a persistent degradation stage independent of the active episode.

Working stages:

| Stage | Meaning |
| --- | --- |
| 0 | No permanent heat degradation |
| 1 | Reduced environmental resilience |
| 2 | Permanently dried or ecologically damaged |
| 3 | Desertified where the terrain family permits it |
| 4 | Wasteland, Evolution III only |

The exact stored representation should follow live repository patterns. It must be stable across owner and controller changes.

## Eligibility inputs

Permanent degradation evaluation should use:

- current evolution stage
- cumulative episode exposure
- prior-episode degradation
- current terrain family
- current aridity classification
- water-system failure duration
- agricultural and vegetation pressure
- wildfire history
- infrastructure and population collapse
- mitigation and recovery
- current Global Heat Wave Intensity
- regional amplification
- episode generation and prior transaction proof

## Warning and confirmation

A state should not change permanently on the first qualifying pulse.

Suggested process:

1. State reaches an environmental-risk threshold.
2. A warning stage appears and the state enters the environmental hotspot list.
3. A final mitigation or recovery action becomes available where plausible.
4. Exposure remains above the threshold for a confirmation period.
5. The event records the permanent stage change once.
6. Actual map terrain update occurs only after map validation and synchronized cleanup.
7. A report explains the physical change.

## Exposure anchors

Suggested minimum starting anchors for implementation review:

| Change | Exposure direction |
| --- | --- |
| Stage 0 to 1 | 60 to 120 days of high mitigation-adjusted Extreme exposure |
| Stage 1 to 2 | Additional 90 to 180 days, or repeat severe episode exposure |
| Stage 2 to 3 | Already dry family, failed water system, and long Scorched or repeated Extreme exposure |
| Stage 3 to 4 | Evolution III, very long Scorched exposure, severe collapse, and global cap |

These ranges should be centralized and tested. A state can accumulate risk across episodes where permanent degradation already exists, but ordinary temporary exposure should not remain as a hidden permanent counter forever after full recovery.

## Terrain-family progression

### Plains and agricultural land

Preferred progression:

- healthy plains or farmland
- reduced resilience
- persistent dryland or degraded plains
- desert only after repeated or extreme exposure
- wasteland only after later Evolution III collapse

Agricultural loss should normally precede terrain conversion.

### Forest

Preferred progression:

- forest under drought stress
- dry or sparse forest condition
- damaged open land or dry plains after severe vegetation loss
- desert only in suitable climate after repeated degradation
- wasteland only after prior desertification and collapse

Wildfire can accelerate the path through Event 013 but should not guarantee conversion.

### Jungle

Preferred progression:

- humid heat stress and vegetation pressure
- dry forest or savanna-like degraded condition where a supported terrain mapping exists
- dry plains or desert only after extraordinary repeated exposure
- wasteland extremely rare

Jungle must not use desert logic merely because human heat stress is high.

### Hills

Preferred progression:

- stressed hills
- dry or bare hills condition
- dryland or desert only where climate and prior degradation support it

Hills can remain strategically cooler than plains while still losing vegetation and water.

### Mountains

Preferred progression:

- reduced water resilience and vegetation stress
- barren mountain or degraded mountain condition where supported
- wasteland only during final extreme collapse

Mountains should resist conversion. Their main long-term risk can be water-source loss and receiving-population pressure.

### Marsh

Preferred progression:

- water and sanitation stress
- dried marsh or damaged wetland condition
- plains or dryland after long hydrological collapse
- desert only after additional degradation

### Urban

Preferred progression:

- persistent urban heat vulnerability
- damaged water and power systems
- partial abandonment or ruined urban condition where supported
- wasteland only after severe depopulation, infrastructure collapse, and prior degradation

An urban state should not become desert merely because it is hot.

### Desert

Preferred progression:

- severe desert stress
- persistent water and habitability collapse
- wasteland under Evolution III conditions

Existing desert terrain receives no redundant desertification stage.

### Wasteland

No further terrain degradation stage. It can retain temporary Heat Stress and recovery logic where population or units remain.

## Actual terrain mapping

The live implementation must inspect:

- current terrain definitions
- state and province terrain ownership
- any existing Chaos Redux terrain-change precedent
- province and state map consistency
- supply, railway, building, and strategic-region implications
- map rewrite and comparison tools

Required tool path:

- `hoi4.map_inspect`
- supported declarative `hoi4.map_rewrite`
- deterministic comparison
- rollback evidence
- targeted lint and map validation

The implementation must define whether the change affects a state-level terrain abstraction, province terrain, or a maintained event-owned state classification. It must not assume one state has one simple terrain token when the engine uses province terrain.

## Safe fallback policy

There is no silent fallback.

If actual terrain conversion cannot be proven safe:

- retain the permanent degradation ledger
- retain visible state condition and gameplay effects only if the user accepts that temporary implementation explicitly
- mark map terrain conversion blocked
- do not call the environmental feature complete

This package does not pre-approve a modifier-only replacement.

## Permanent water damage

A degradation stage can include persistent water vulnerability even when the map terrain cannot express it directly.

Persistent water damage should:

- increase future Heat Stress
- lengthen water recovery
- raise drought and Famine risk
- affect Migration destination safety
- be visible in the state tooltip
- have a separate owner-approved restoration path if reversibility is desired later

## Restoration

Event 51 cleanup does not restore permanent degradation.

Possible future restoration belongs to a shared environmental recovery system or an event-owned long-term project accepted later. It should require time, water, construction, population, and stable control.

Wasteland should be extremely difficult or impossible to reverse unless a separate major system explicitly owns that capability.

## Degradation caps

Suggested safeguards:

- per-episode cap on new Stage 3 desertifications
- much lower per-episode cap on new wasteland states
- global cap on same-day terrain transactions
- no two permanent stage changes for one state in one episode unless a rare Evolution III branch explicitly proves the path
- no degradation while the state is already in confirmed strong recovery
- no random selection outside the qualifying set

Caps prevent a high-intensity pulse from rewriting the whole map at once.

## Border and controller changes

Permanent degradation follows the state. It does not disappear when occupied, annexed, liberated, or transferred.

A new controller should inherit:

- current environmental stage
- current Heat Stress
- recovery burden
- valid mitigation options

It should not inherit the previous controller's completed national priority or invalid missions.

## Achievement and event-log hooks

Permanent changes can support:

- first global desertification milestone
- first wasteland milestone
- country achievement for preserving a key fertile region
- event details showing total permanent changes from the latest episode
- recovery reports

The event log should record major world milestones, not every state score adjustment.

## Acceptance cases

1. A fertile state cannot become desert during a short first episode.
2. A previously degraded dry state can desertify after a long Evolution II episode.
3. A forest can lose resilience and vegetation before any desert path.
4. A mountain state resists terrain conversion and mainly suffers water-source pressure.
5. Wasteland requires Evolution III, prior degradation, severe collapse, and caps.
6. Terrain changes survive owner and controller changes.
7. Cleanup removes temporary Heat Stress but preserves the permanent ledger.
8. Map conversion remains blocked when map tooling cannot prove a safe result.
