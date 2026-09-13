# Event 58: Provincial and exceptional construction

## Evolution II: Provincial Construction

### Threshold

- Chaos requirement: `400+`

After the two state-building layers, each state attempts one province-level construction package.

The state is the unit of selection. The selected package determines the actual provinces affected. A package can place one structure, improve one route, or add one level across every relevant province in a coherent state feature.

The package must use real province geography. It cannot choose a random province without checking the reason that province belongs to the result.

## Provincial package registry

Province packages use the same owner-provider principle as state buildings.

A package entry defines:

- its stable identity and display family
- the states where the package can be considered
- the province set that qualifies inside a selected state
- whether it places one result or a connected group
- a current capacity check for every affected province
- its relative weight after validity filtering
- the placement operation
- owner callbacks and responsibility when needed
- any uniqueness, distance, graph, DLC, or map restriction
- how partial capacity is handled

A package is invalid when it cannot place any meaningful part of its intended result.

When some eligible provinces are already capped, a multi-province package applies to the remaining eligible provinces. The package still succeeds when at least one province changes. It records the number of changed provinces for reporting and testing.

## Provincial weighting direction

The layer should favor transport and ordinary defense over rare strategic nodes.

A representative valid-state balance should make rail construction or upgrades the most common package, followed by land-border and coastal defenses. Naval bases and supply hubs remain less common because they can change logistics and invasion geography sharply.

Context determines the actual candidate pool. An inland interior state may have only rail and supply candidates. A coastal border state may have every major package available.

The intended relative order in a state where every standard package is valid is:

1. railway construction or upgrade
2. land-border fortification
3. coastal fortification
4. naval-base construction or upgrade
5. supply-hub construction
6. owner-registered special province package, according to its own risk band

This is an ordering target. Exact weights require the probability audit and complete candidate list.

## Land-border fortification package

A land-border fort result adds one land-fort level to every relevant border province inside the selected state that has room.

A relevant border province is a land province that touches a land province outside the current controller's territory. Borders entirely inside the same controlled country are not fortified.

The provider can distinguish these cases when the live engine and project precedent support them:

- active enemy border
- border with a non-allied foreign country
- border with an ally or subject
- border across an occupied state boundary

The default package should prefer active enemy and non-allied foreign borders. It can remain valid on an allied border when no diplomacy-sensitive distinction is safe to implement, but this must be visible in the probability and map acceptance evidence.

Every affected province gains only one level from this package in one firing. Existing forts remain and can be improved on later Event 58 firings until the normal maximum is reached.

A state with no relevant uncapped border province cannot roll this package.

## Coastal fortification package

A coastal-fort result adds one coastal-fort level to every relevant sea-facing land province inside the state that has room.

A relevant coast must connect to a usable naval sea area. Inland lakes and province edges that do not support ordinary naval access do not qualify.

The package can affect several coastal provinces, including islands inside one state. It adds one level per qualifying province in one firing.

A state with no usable sea coast or no uncapped coastal-fort location cannot roll this package.

## Naval-base package

A naval-base result selects one usable coastal province inside the state.

Selection preference is:

1. upgrade an existing naval base below its cap
2. place a new naval base in a coastal province connected to the state's main transport or population center
3. prefer a province with a victory point, urban importance, railway access, or another verified sign of practical port use
4. resolve equal candidates randomly

A new port must not be placed on an unusable lake coast, an impassable province, or a province whose map definition cannot host the building.

The package adds one naval-base level. It does not add dockyards, convoys, ships, coastal forts, or a supply hub unless a future owner registers a different compound package for a higher-risk layer.

A state with no valid coastal province cannot roll this package.

## Railway package

The railway package improves transport through the selected state.

Its preferred forms are:

1. upgrade one existing railway path through the state by one level
2. extend a short valid connection from the state's main developed province to the nearest compatible railway network controlled by the same country
3. connect two existing railway endpoints inside the state when a short missing segment breaks an otherwise coherent route

The main developed province should be selected from the state capital, highest victory point, strongest existing transport node, or another verified map precedent.

The route must be contiguous, legal, and bounded. It cannot jump across provinces, cross sea without a valid engine route, enter an unrelated controller's territory, or create a path through impassable terrain.

Rail creation is an implementation evidence gate. The coding agent must inspect the installed map, supply, and railway graph tools and a vanilla or Chaos Redux precedent. If runtime path construction cannot be implemented safely through a verified engine operation, the new-connection form remains blocked. The package may still use verified upgrades to existing railways.

An unverified railway result must not be replaced with infrastructure, trains, supply grace, or a state modifier. Those are different outcomes.

A state with no valid upgrade and no verified connection path cannot roll this package.

## Supply-hub package

A supply-hub result places one hub in a strategically sensible province inside the selected state.

The package is uncommon and uses strict validity:

- the state has no existing supply hub that already serves the same area
- a valid land province can host the hub
- the province can connect to an existing railway or receive a verified short railway connector as part of the same package
- the location does not violate owner-defined minimum separation or facility rules
- the state has enough strategic, population, industrial, front, or transport importance to justify a hub

Preferred locations include the state capital, a major victory point, an existing railway junction, a major port, or a central province that resolves a clear supply gap.

When the package includes a short rail connector, the hub and connector form one atomic package. If either part cannot be created safely, nothing is placed and the state rerolls.

A supply hub does not grant trains, trucks, fuel, or temporary supply bonuses.

## Future province packages

Future systems can register province packages such as:

- defensive stronghold belts
- canal, tunnel, bridge, or corridor anchors when the engine representation exists
- event-owned coastal batteries
- special railway nodes
- local power-grid anchors
- project-specific province facilities

The owner must define exact province validity and placement. Event 58 does not infer province geometry from a building name.

## Province package rerolls

The state first builds the valid package set, then selects one package by weight.

The selected package resolves its province targets and revalidates them. If every intended province became invalid, the package is removed and the state rerolls among the remaining valid packages.

A package that changes at least one valid province succeeds. It does not reroll merely because some other provinces were capped.

The event must never apply two different Evolution II packages to one state in the same firing.

## Province reporting

Player summaries group province results by package family. They do not list every fortified province or rail segment.

A concise detail tooltip can show:

- states receiving rail work
- states receiving border forts
- states receiving coastal forts
- states receiving naval bases
- states receiving supply hubs
- total provinces changed where a multi-province package applied

Exact province names should appear only for rare or strategically important results where the information is useful and readable.

## Evolution III: Exceptional Construction

### Threshold

- Chaos requirement: `600+`

Evolution III adds a limited number of exceptional structures across the world after all state and province layers have completed.

This is a global allocation, not one roll per state. The result should feel rare even though the earlier layers affect every state.

## Exceptional allocation budget

The budget scales with the number of states that have at least one valid exceptional entry after earlier layers.

The target rule is:

- one exceptional placement for roughly every `100` valid world states
- minimum target of `5` placements when at least `5` valid locations exist
- normal cap of `10` placements at `600-799` Chaos
- cap of `15` placements at `800+` Chaos
- never place more structures than the number of valid unique locations

These values are tuning targets. They must be centralized and audited against the actual map and provider pool.

A small map or heavily altered campaign can receive fewer than the minimum because validity always wins.

## Exceptional provider contract

Exceptional entries need more information than ordinary buildings.

Each owner defines:

- the exceptional structure family
- whether the structure is a building, facility, landmark, state modifier with a physical construct, or another supported instance
- exact candidate states or geographic rules
- any province anchor used by the visual or gameplay system
- one-per-state, one-per-country, or one-per-world limits
- whether repeat Event 58 firings can create another instance
- the owner callback that initializes its normal mechanics
- capture, destruction, shutdown, discovery, repair, and cleanup behavior
- any required 2D or 3D assets already owned by the source system
- a player-facing display family for reports and achievements

An exceptional provider without a complete lifecycle cannot enter the pool.

## Exceptional selection process

Evolution III uses a global candidate set built after the earlier layers.

For each budget slot:

1. select an exceptional risk family from the valid provider pool
2. select one valid location from that provider's current candidates
3. revalidate capacity, uniqueness, DLC, owner system, and geography
4. place the real structure and complete its owner callback
5. remove every candidate invalidated by that placement
6. prevent another exceptional result in the same state during the same firing

If a selected provider has no valid location after revalidation, it is removed for that allocation pass. The resolver continues with the remaining providers and locations.

Evolution III never fills an unused budget slot with an ordinary state building or province package.

## Exceptional structure families

### Dams

A dam can appear only at a provider-defined valid river or reservoir site. The owner must define the state, province anchor, normal economic or supply effects, damage behavior, and any map entity.

Event 58 cannot decide that every river province can host a dam.

### Special-project facilities

A special-project facility requires its DLC, facility database, placement rules, uniqueness, and project-system initialization.

The facility can appear without ordinary construction time when its owner allows Event 58 grants. It does not automatically complete a project, grant scientists, unlock research, or count the source event as fired.

### Rare landmarks and state constructs

A landmark or state-modifier structure needs a real owner-defined location and persistent instance. It cannot be a generic bonus renamed as a landmark.

A visual landmark must use its owner's normal map-entity and asset pipeline. Event 58 does not create a new 3D model merely because it can place the structure.

### Event-owned exceptional buildings

A future event can register one of its buildings when it supplies the full adapter and declares Event 58 compatibility.

The original event remains unfired unless its owner explicitly defines another history relationship. The new structure can still awaken part of the owner system through its callback.

## Repeated exceptional waves

Later Event 58 firings rebuild the exceptional candidate set from the current world.

A structure with world uniqueness cannot appear again. A one-per-country structure can appear in another country. A repeatable dam or facility can appear again only at another owner-approved location.

The event does not remember every rejected candidate. It relies on current owner validity and persistent uniqueness markers.

## Map and graph safety

Every province and exceptional placement must be proven against the actual installed map.

Implementation must inspect:

- state and province membership
- land and sea adjacency
- usable coastline
- existing naval-base anchors
- railway paths and levels
- supply hubs and railway connectivity
- impassable terrain
- facility and landmark locations
- map changes introduced by Chaos Redux

Static assumptions copied from a vanilla state list are insufficient because other Chaos Redux events can transfer, destroy, transform, or register locations.

The resolver may use owner-maintained candidate registries for rare fixed sites. It must still revalidate the live state and province before placement.

## Performance boundary

Evolution II and Evolution III run only during the Event 58 transaction.

The design does not authorize a whole-world daily, weekly, or monthly scan. It does not authorize continuous railway pathfinding or exceptional-site polling.

The transaction should reuse the frozen state list, bounded provider arrays, and local candidate sets. Temporary arrays, event targets, and counters are cleared after reports and achievement checks.
