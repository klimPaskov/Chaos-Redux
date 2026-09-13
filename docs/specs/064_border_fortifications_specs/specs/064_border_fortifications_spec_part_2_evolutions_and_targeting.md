# Event 064 Border Fortifications

## Part 2: Evolutions and strategic targeting

## Evolution model

Event 064 has three global evolution stages:

| Evolution | Chaos requirement | Accepted role |
| --- | ---: | --- |
| Defense in Depth | `200+` | Strengthen selected frontier anchors and create bounded secondary positions behind the border. |
| Fortress States | `400+` | Turn selected border states into integrated defensive sectors with stronger forts, anti-air, radar, logistics work, and selective coastal defenses. |
| Fortress World | `600+` | Extend the phenomenon to capitals, major victory points, supply hubs, and other critical internal approaches. |

Evolution state changes what a future Event 064 wave can do. It does not trigger a free retrofit at the moment an evolution becomes available.

This matters for pacing. The player first experiences the clear global border rule. Later waves become deeper and more selective as Chaos rises. A country can remember the earlier line and see it grow into a layered defensive system over repeated incidents.

## Eligibility, maturation, and first materialization

Each evolution follows the shared Chaos Redux evolution contract.

1. Its Chaos threshold makes it eligible.
2. The shared evolution pacing resolves maturation after eligibility. The threshold tick itself grants no effects.
3. The evolution must also be enabled in the event settings.
4. A later Event 064 wave reads the enabled and matured stages before building its candidate sets.
5. The evolution is logged as a concrete Event 064 development only when its package changes at least one valid building or position.
6. Evolution eligibility and maturation add zero direct Chaos.

The planning anchor for normal maturation is around 90 days, adjusted through the shared dynamic evolution system. A higher current Chaos value, repeated Event 064 history, widespread wars, and prior military-abundance incidents can shorten the wait. A calm map just above the threshold can mature more slowly.

### First firing at high Chaos

A campaign can reach a high Chaos value before Event 064 fires naturally. The first wave can use every enabled evolution that has legitimately matured by then. This is a pre-fire evolved opening, not a reason to bypass evolution enablement or fabricate earlier history.

If the shared system permits a first-firing maturation roll, it should use the normal evolution framework. The event should not hardcode that all three stages are automatically active merely because current Chaos is above 600.

A high-tier first wave applies cumulative concrete packages in one transaction, subject to per-wave and role caps. It does not set every frontier to the final cap.

## Disabled evolution independence

Every package must work without hidden dependence on an earlier disabled stage.

- If Defense in Depth is disabled, Fortress States can still select border states, strengthen their direct frontier sectors, and add its state support package. It does not create second-line positions through the disabled stage.
- If Fortress States is disabled, Fortress World can still create internal redoubts. It does not add the state anti-air, radar, logistics, or coastal package.
- If Fortress World is disabled, lower packages continue normally.
- Re-enabling a stage affects later waves. It does not backfill omitted positions at once.

The evolution log records the material result. A stored highest stage with no concrete package effect does not count.

## Strategic role model

The evolved wave classifies candidates into five roles.

| Role | Purpose | Main source |
| --- | --- | --- |
| Direct frontier | Every qualifying current foreign land-border province | Baseline |
| Frontier anchor | A direct frontier province with unusually high military value | Defense in Depth and later |
| Depth position | A bounded position one operational step behind a direct frontier | Defense in Depth and later |
| Fortress State | A selected border state receiving an integrated state package | Fortress States and later |
| Internal redoubt | A capital, major victory-point, supply, industrial, port, or critical internal approach position | Fortress World |

A province can satisfy several role tests. It receives one resolved land-fort role for the wave. State support buildings are resolved separately.

### Role priority

Use the following priority when one province qualifies for several land-fort roles:

1. capital or designated national redoubt
2. strategic frontier anchor
3. Fortress State direct frontier sector
4. ordinary direct frontier
5. depth position
6. other internal redoubt

The priority identifies the cap and report role. It does not allow a third fort increase in one wave. A direct frontier province can receive its ordinary one level and one resolved anchor or state-sector bonus. A depth or internal position receives one level.

## Strategic scoring

Selection should combine deterministic value with bounded variation. The same capital, mountain pass, or supply junction should often matter, but a repeatable event should not always choose an identical list when several candidates have similar value.

### Positive factors

Increase priority for a province or state when it has one or more of these features:

- current war frontier
- hostile neighboring country
- stronger or similarly strong neighboring army
- recent loss of adjacent territory
- capital approach
- major victory point
- supply hub
- important railway junction or route to the frontier
- high infrastructure connection between the capital and the border
- mountain or hill terrain
- a river crossing on an otherwise direct land approach
- narrow land corridor
- enclave or exposed salient
- state containing large military or civilian industry
- state containing an important airbase
- state containing a port and a foreign land frontier
- missile, nuclear, radar, air-defense, or other strategic site created by a connected Chaos Redux event
- repeated Event 064 history that left the surrounding sector weaker than comparable sectors
- current Military Preparation cluster context

### Negative factors

Reduce priority when a candidate is:

- already at or above the role cap
- isolated from any meaningful route or objective
- in an impassable or invalid building position
- a duplicate of a stronger role in the same province
- a second or third target in a state before other valid regions receive one
- in a state the country is about to lose according to clear current control conditions
- a state with no normal supply connection and no strategic objective
- a coastal province with no port or landing role when selecting coastal defenses
- part of a tiny border segment already receiving its full quota

A negative factor should not remove an ordinary direct frontier from the baseline. It only changes evolved selection.

### Threat and diplomacy

Relations do not remove a frontier from the event, but threat helps choose evolved priorities.

- Active enemies receive the highest military-threat score.
- Countries with a war goal, claim pressure, hostile strategy, or severe relation collapse receive a lower but meaningful score.
- Neutral and allied frontiers remain eligible for anchors and state packages through terrain, capital, supply, or geographic value.
- The event should still produce strange allied border fortifications. Threat scoring must not quietly convert the global rule into an enemy-only event.

## Diversity and quota rules

Evolved packages use country quotas to prevent carpet fortification.

### General quota principles

- Scale sublinearly with frontier size.
- Give a small country at least one valid evolved target when geometry permits.
- Use hard country caps so a continental empire cannot consume an unbounded number of expensive selections.
- Prefer distinct border states and strategic regions before adding another target to an already selected area.
- Allow a disconnected enclave or overseas land frontier to receive representation when it has meaningful size or strategic value.
- Do not spend a quota slot on a candidate that cannot change a building because it is already at cap, unless the state still receives another valid package component.
- Recompute candidates every wave. Do not keep a permanent target list after the frontier changes.

### Starting quota anchors

These are preliminary tuning anchors, not final hard constants.

| Candidate family | Starting quota |
| --- | --- |
| Frontier anchors | About one per six direct frontier provinces, minimum one, hard cap twelve |
| Depth positions | About one per eight direct frontier provinces, minimum one, hard cap ten |
| Fortress States | About thirty percent of current border states, minimum one, hard cap six |
| Internal redoubts | One for 1 to 5 controlled states, two for 6 to 15, three for 16 to 30, four for 31 or more, plus one for a major, hard cap six |
| Coastal defense states | Up to half of selected coastal Fortress States, minimum one when a suitable threatened coast exists, hard cap three |

The implementation can refine these values after large-map testing. The final result must preserve bounded growth and geographic spread.

## Evolution I: Defense in Depth

### Chaos requirement

`200+`

### Purpose

Defense in Depth turns the flat frontier belt into a layered system. It identifies a limited number of decisive border points and a limited number of approaches behind them. It should make selected sectors harder to bypass while leaving enough unfortified interior space for maneuver.

### Frontier anchors

A frontier anchor is an ordinary direct frontier province with high strategic value.

Preferred anchor roles include:

- a direct approach to a capital or major victory point
- a mountain or hill pass
- a river crossing on a likely route
- a narrow corridor
- the border end of an important railway or supply route
- a border province in a high-industry state
- the frontier around a major port or naval base
- a currently contested war-front province

Each selected anchor can receive one additional land-fort level in the same wave after the ordinary baseline level, subject to the two-level per-wave ceiling.

Starting role caps:

- ordinary direct frontier cap: level `4`
- frontier anchor cap: level `5`

A province already above the anchor cap is preserved and does not receive another level from this event package.

### Depth positions

A depth position is a valid defensive point behind the direct frontier. It should be near enough to form a second operational line, but it should not be another complete border belt.

Preferred depth positions include:

- a major-city approach in a border or immediately adjacent interior state
- a railway junction behind a border sector
- a supply-hub approach
- a mountain pass behind the first line
- a river-crossing defense behind the border
- a narrow corridor that connects a frontier to the national interior
- an approach to a high-value industrial or port state
- a capital approach when the capital lies close to the frontier

Starting depth cap: level `2` total.

Each selected depth position receives one land-fort level per evolved wave until the active cap is reached.

### One operational step behind

The engine may not expose a perfect province-graph definition of one operational step behind every frontier. The implementation must still preserve the design.

Preferred resolution order:

1. Use current supported province adjacency, building, terrain, victory-point, supply, and state conditions when they can identify a real position safely.
2. Use border-state and immediately adjacent controlled-state logic to find a bounded depth candidate.
3. Use a maintained province-role registry only for map features the engine cannot identify reliably, such as specific narrow passes or crossings.
4. If no defensible candidate exists, leave the depth slot unused. Do not fortify a random interior province.

Any maintained registry must be documented, validated against the current map, and kept separate from general random selection.

### Country experience

The local report should distinguish:

- ordinary frontier positions improved
- strategic anchors reinforced
- depth positions created

The report does not need to name every province. It can name the highest-value state or region and summarize the remainder.

### Balance intent

Defense in Depth should produce a visible strongpoint pattern. It should not create an unbroken second line across every state behind every border. The event remains Medium severity inside its clusters.

## Evolution II: Fortress States

### Chaos requirement

`400+`

### Purpose

Fortress States selects a bounded set of border states and turns them into integrated defensive sectors. The package combines stronger frontier works with state support systems. Different states receive different combinations according to their role.

### Fortress State selection

A Fortress State must contain at least one direct frontier province. Score each candidate using:

- current hostile border length
- number and value of strategic frontier anchors
- capital, major victory point, industry, supply, railway, airbase, port, or strategic-site role
- mountain, hill, river, or corridor geography
- current war pressure
- coastal exposure
- missing anti-air or radar coverage
- Military Preparation cluster context
- spread across the country's distinct frontiers

Select roughly thirty percent of valid border states, with a minimum of one and a hard cap of six. If fewer states can receive a meaningful package, use the smaller number.

### Stronger direct sector

In each selected Fortress State, qualifying direct frontier provinces can receive one extra land-fort level beyond the ordinary wave. This is the resolved anchor or state-sector bonus and remains subject to the two-level per-wave ceiling.

A province selected as both a strategic anchor and part of the stronger state sector does not receive two separate bonuses. It receives one evolved bonus under the higher applicable cap.

Starting role caps:

- ordinary direct frontier cap: level `6`
- selected strategic or Fortress State frontier cap: level `7`
- depth-position cap: level `3`

These caps define long-term repeated-wave ceilings. One wave still adds at most two land-fort levels to a direct frontier province and one level to a depth position.

### State anti-air

Selected states with important industry, airbases, ports, capitals, supply hubs, missile sites, nuclear sites, radar gaps, or current enemy air pressure can receive one state anti-air level.

Starting cap: level `3` total.

Do not add anti-air to every selected state by default. A state that has no air-defense role can receive another valid package component instead.

### Radar

Selected states with air-warning, naval-warning, port, strategic-site, or major-front value can receive one radar level.

Starting cap: level `2` during this evolution, rising to `3` under Fortress World when the state remains strategically important.

Radar should be rarer than land forts. Prefer geographic coverage and major sectors over filling every border state.

### Supply-related construction

Supply work should help a country use the forts it received. It must not create free supply hubs along every frontier.

Automatic package priority:

1. Restore or strengthen existing damaged infrastructure or rail support when the current engine effect can do so safely.
2. Add one infrastructure improvement in a selected state below the active infrastructure cap.
3. Strengthen an existing railway or connection when a verified route can be identified.
4. Create a new supply hub only when a genuine strategic gap is proven, the country quota permits it, the state has a valid site, and balance testing supports the cost of a free hub.

A new hub should be exceptional. Most Fortress States receive an infrastructure or railway improvement instead.

Starting automatic limits:

- one supply-related automatic change per selected state per wave
- no more than two exceptional new supply hubs worldwide in one wave unless a later implementation audit proves a higher bound safe
- no supply change in a state already at its relevant cap and without damage

The player response decision can invest more deeply in one selected sector.

### Coastal defenses

A coastal border state must contain both a valid foreign land frontier and a valid coast or port role. An island state with no land frontier is not a Fortress State under Evolution II.

Preferred coastal targets:

- port province
- naval-base province
- direct coastal approach beside a fortified land frontier
- major landing approach protecting a border port or supply route

Each selected target can receive one coastal-fort level, subject to a starting cap of level `3`.

Do not fortify every coastal province. Limit the automatic package to ports and one or two high-value landing approaches in the selected state.

### Package composition

A selected Fortress State should receive a role-based package, not every building type by default.

| State role | Preferred package |
| --- | --- |
| Active hostile front | stronger direct sector, depth position where valid, infrastructure or railway support |
| Industrial border state | stronger direct sector, anti-air, infrastructure support |
| Air-defense sector | stronger direct sector, anti-air, radar |
| Coastal border state | stronger direct sector, port coastal fort, radar or anti-air according to threat |
| Mountain or corridor sector | stronger anchors, bounded depth position, infrastructure support |
| Strategic-site state | stronger direct sector, anti-air, radar, supply support |

A normal state receives two or three meaningful package components. A tiny state with few valid slots can receive one.

### Country experience

The local report should name or highlight the most important Fortress State and summarize how many states received integrated packages. The response category should make those selected states valid targets for further local investment.

## Evolution III: Fortress World

### Chaos requirement

`600+`

### Purpose

Fortress World extends the pattern beyond national frontiers. Countries receive a bounded network of internal redoubts around places whose loss could decide a war. The world begins to resemble fortified state systems, with defenses extending beyond national borders.

### Internal redoubt candidates

Preferred candidates include:

- national capital
- fallback capital candidate when the current capital is invalid or already a frontier anchor
- major victory point
- supply hub
- railway junction connecting several regions
- narrow internal corridor
- major industrial center
- major port or naval base
- strategic airbase
- missile, nuclear, radar, or other critical Chaos Redux site
- approach between an exposed frontier and the capital
- last secure supply route during an active defensive war

The redoubt should protect a meaningful position or approach. It should not place a fort in a random rural province because the quota exists.

### Capital redoubt

Every valid country should receive one capital redoubt when the capital has a legal land-fort position and the active cap allows a change.

If the capital province is already a direct frontier province, resolve it as a capital frontier anchor. It can receive the ordinary level and one evolved bonus, but no third level from the internal package.

If the capital province itself cannot receive a fort, select the strongest valid approach in the capital state or a directly connected controlled state.

### Additional redoubts

Use the country-size quota from the strategic model, with a hard cap of six. Prefer geographic spread and distinct roles.

Suggested order:

1. capital or capital approach
2. highest-value supply hub or junction
3. highest-value major victory point
4. industrial or port hub exposed to a likely advance
5. second regional supply or victory position in a distant region
6. special strategic site

A country with one small state can receive only one redoubt. A continental major can receive several. A large colonial empire should distribute later slots across distinct important regions and avoid concentrating all of them around the capital.

### Island and isolated countries

Fortress World gives land-borderless countries their first local construction package.

An island country can receive:

- capital redoubt
- port or naval-base redoubt
- major victory-point redoubt
- supply-hub defense
- coastal-facing approach defenses only when they are part of the redoubt role and use valid land-fort positions

This package does not convert every island coast into a Fortress State. Coastal forts remain tied to Evolution II's valid coastal border-state rule or to the player's evolved local project when a specific island defense role is allowed.

### Starting caps

| Role | Fortress World cap |
| --- | ---: |
| Ordinary direct frontier | level `7` |
| Strategic frontier anchor or selected Fortress State sector | level `8` |
| Depth position | level `4` |
| Internal redoubt | level `3` |
| State anti-air in selected strategic states | level `3` |
| Radar in selected strategic states | level `3` |
| Coastal fort at selected evolved targets | level `3` |

These are long-term caps. Fortress World still uses gradual repeated waves.

### Internal gaps remain important

The event must leave maneuver space between redoubts. Most internal provinces receive nothing. The country should have defensive centers and fallback routes, not a complete inland carpet.

Redoubts become stronger through repeated waves only when they remain valid strategic positions. A moved capital or changed supply network can shift later selections. Old physical forts remain where they were built.

### Country experience

The local report should identify the capital or highest-value redoubt and summarize any additional redoubts. The response category can unlock a single National Redoubt project for further investment during that wave's response window.

## Evolution package overlap

A single high-tier wave resolves all enabled stages in order.

Example for one direct frontier province:

1. Baseline gives one level if below the ordinary cap.
2. Defense in Depth can classify it as an anchor.
3. Fortress States can classify its state as selected.
4. The province resolves to the highest strategic direct-frontier role.
5. It receives at most one evolved bonus after the baseline level.
6. Fortress World does not add an internal-redoubt level if the same province is already the capital frontier anchor.

Example for one interior supply hub:

1. Baseline does nothing because it is not on a direct frontier.
2. Defense in Depth can select it only if it is a valid near-front depth position.
3. Fortress States can improve the surrounding state's supply support only when that state is a selected border state.
4. Fortress World can classify the hub or its approach as an internal redoubt.
5. It receives one land-fort level under the highest resolved interior role.

## Repeat-wave targeting

Repeated waves should not always reinforce the same already strong positions.

Candidate scoring should include diminishing priority for:

- positions already at the active cap
- states selected in the immediately previous wave when comparable untouched states exist
- regions already holding a large share of the country's evolved positions

Candidate scoring should increase for:

- new borders created since the last wave
- states that lost forts through combat damage or state transfer when the current engine exposes the condition safely
- newly important capitals, supply hubs, ports, strategic sites, and war fronts
- newly threatened fronts

The event does not need a permanent detailed province ledger for every old wave. It can use current building levels, limited last-wave state markers, and current strategic conditions.

## Changed borders after construction

Physical forts remain after the map changes.

- A peace settlement can leave a former border belt deep inside one country.
- An advancing army can capture and use the line against its builder.
- A released country can inherit old forts.
- An annexed frontier can become an internal defensive belt.
- A new front receives no Event 064 fort until another wave.

This persistence is part of the event. It creates map history and prevents the implementation from running a recurring border-maintenance process.

The Event 064 response category must update or cancel stale targets when control changes, but it must not move completed buildings.

## Evolution history

Each evolution has two distinct documentation surfaces.

### Event Details evolution catalog

The catalog describes what the stage can add:

- Defense in Depth: selected strategic anchors and secondary positions
- Fortress States: integrated border-state packages
- Fortress World: internal national redoubts

This is premise-level information. It does not expose exact caps, quotas, hidden scores, or Chaos gains.

### Evolution history

Log the first concrete materialization of each stage when the package changes at least one valid position.

The history row should record:

- date
- evolution name
- number of countries affected by that package
- number of positions or states changed by that package
- no misleading single-country actor

If a stage is enabled but every candidate is already capped or invalid, do not create a false materialization row. A later wave can create it when the package first changes the world.

## Evolution text direction

The implementation writes final localisation from these directions.

### Defense in Depth

Describe the new line as layered and deliberate in form, while keeping its origin uncertain. Emphasize secondary belts, covered approaches, and strongpoints appearing behind the obvious frontier. Avoid technical scoring language and avoid stating that governments successfully completed a normal building program.

### Fortress States

Describe whole border regions taking on the structure of military districts. Show anti-air positions, observation systems, reinforced transport links, and coastal works as parts of one defensive landscape. Avoid a simple list of building bonuses.

### Fortress World

Describe capitals and internal hubs gaining redoubts even far from foreign borders. The public meaning should be that permanent fallback warfare has become normal. Avoid end-of-world language because this remains an evolved minor event.

## Evolution completion standard

The evolution system is complete only when:

- every stage respects its threshold, enablement, and shared maturation contract
- stage activation alone adds no Chaos
- future waves use matured stages without retroactively rebuilding the world at activation time
- disabled stages skip cleanly
- higher stages remain valid when lower stages are disabled
- strategic scoring produces bounded, geographically spread targets
- candidate pools exclude invalid or capped positions
- every land-fort province is deduplicated before construction
- no direct frontier province gains more than two levels in one wave
- depth and internal positions gain no more than one level in one wave
- Fortress State support buildings follow role-based packages and caps
- supply construction prefers existing networks and does not flood the map with free hubs
- coastal defenses stay selective
- island countries gain meaningful redoubts at Fortress World when valid
- evolution history records concrete first materialization, while eligibility has no history entry
- repeated waves can shift targets after wars and border changes
- large-map tests confirm quotas, caps, spread, and transaction performance
