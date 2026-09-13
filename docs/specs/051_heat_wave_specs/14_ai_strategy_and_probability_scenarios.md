# AI Strategy and Probability Scenarios

## AI objective

AI should treat Heat Wave as a resource-allocation and force-posture crisis. It should identify the dominant national risk, choose a protection priority, fund a small number of meaningful actions, and stop taking actions that no longer fit the state of the episode.

AI must use the same gameplay rules as the player. A human-only category header or target selector can have an AI-equivalent path, but the AI must pay the real costs and satisfy the same outcome gates.

## National risk assessment

Each AI country should build one hidden national response profile from:

- exposed population
- number and importance of Dangerous, Extreme, and Scorched states
- active war and front importance
- military unit exposure
- food vulnerability and Famine facts
- urban water pressure
- industrial and rail importance
- available transport, fuel, equipment, manpower, and civilian capacity
- expected episode duration
- embargo or import access
- national stability and governance capacity
- current evolution stage

The profile selects one national priority and ranks local targets.

## Priority selection

### Protect Population Centres

Increase weight when:

- several high-population states are Extreme
- capital water system is failing
- Evolution I is active
- cooling centers can materially reduce mortality
- country is at peace or has no severe hot front

Reduce weight when:

- exposed population is low
- agriculture is near catastrophic failure
- active front collapse would be immediate

### Sustain the Front

Increase weight when:

- country is in a major war
- several divisions are Heat-Exhausted or Critical
- hot states contain important fronts, ports, or supply hubs
- no cooler defensible line exists

Reduce weight when:

- no exposed military force exists
- food or capital water collapse is more severe
- fuel and motorized stockpiles cannot support the policy

### Defend the Harvest

Increase weight when:

- country depends on a small number of agricultural states
- Famine risk is high
- imports are blocked or unavailable
- a harvest mission can still succeed

Reduce weight when:

- target harvest is already irrecoverable
- agriculture is minor and imports are secure
- the country cannot supply the required transport

### Preserve Industrial Output

Increase weight when:

- country has major industrial hotspots
- war production is critical
- rail and power systems remain protectable
- temporary output loss would have large strategic cost

Reduce weight when:

- severe mortality or water failure dominates
- controlled shutdown is clearly safer
- industry is small

### Balanced Emergency Plan

Increase weight when:

- no sector dominates
- administrative capacity is weak
- resources are insufficient for a specialized policy
- the country has several moderate problems and no immediate catastrophic one

It should not become the default merely because its conditions are broad.

## Target scoring

State target score should include:

- Heat Stress band and upward trend
- population
- capital and victory-point role
- agricultural role
- industrial role
- front and supply role
- water stage
- active mission
- mitigation gap
- projected consequence without action
- action effectiveness
- action cost relative to stockpiles

Invalid targets receive zero score.

Target lists should be complete when the game normalizes weights across them. If the MCP tool cannot see the full candidate pool, results must be reported as bounded or unresolved, not exact.

## Budget control

AI should reserve resources. It should not spend all trains, trucks, fuel, support equipment, or civilian capacity on Heat Wave actions.

Suggested reserve logic:

- maintain a wartime logistics reserve
- protect a minimum convoy reserve for import-dependent countries
- avoid spending equipment needed for current reinforcement
- cap simultaneous high-cost mitigation projects
- prefer one strong project over several weak projects

The exact reserve thresholds require scenario testing.

## Decision behavior

### Emergency Water Rationing

Very high weight when a populated state approaches System Failure. Lower weight after the state cools or when rationing is already active.

### Cooling Centres

High weight under Evolution I when mortality reduction is large. Low weight in sparsely populated states or where water and power failure make the action ineffective.

### Army Heat Protocols

High weight before or during a hot war. Low weight without exposed divisions.

### Harvest Protection

High weight before catastrophic crop failure. Zero after no valid recoverable target remains.

### Rail Maintenance

High weight for capital, front, port, food, or industrial corridors. Low for isolated low-value track.

### Night Shifts

High weight for industrial states with cooler nights and functioning transport. Low during Evolution III hot-night conditions.

### Controlled Shutdown

High weight when permanent damage risk exceeds short-term output value. AI should accept shutdown more readily in peacetime.

### Food Imports

High weight when Famine owner facts indicate need and a route exists. Zero under complete embargo or route failure unless a smuggling or special owner path exists.

### Evacuation

High weight only when the origin cannot be kept safe and Migration accepts the route. Avoid premature evacuation of manageable states.

## Military AI

Military AI should:

- lower offensive priority in Scorched states
- avoid training in severe states
- rotate Critical divisions where replacements exist
- preserve key defensive fronts
- avoid overstacking a hot low-supply state
- favor cooler routes when strategic cost is acceptable
- acclimatize reserves before a planned hot offensive where time exists
- increase logistics and support priority for exposed fronts

It should not use blanket strategic withdrawal from every hot state.

## Recovery AI

AI should compare recovery projects by permanent value:

1. capital water and critical supply
2. major rail corridor
3. high-value industrial reopening
4. agricultural recovery before the next harvest cycle
5. military rest and readiness
6. low-value cosmetic or minor repairs

AI should stop funding temporary heat mitigation after all owned states leave relevant bands.

## Probability audit contract

Every weighted surface requires the project probability workflow.

The auditor must begin with `hoi4.probability_inspect` and then choose tools based on evidence:

- `hoi4.probability_evaluate` for one named situation
- `hoi4.probability_sweep` for intensity, stockpile, war, or stress ranges
- `hoi4.probability_compare` after any patch
- `hoi4.probability_simulate` for repeated target selection when the pool is complete
- `hoi4.probability_sequence` only when cadence, cooldowns, resource changes, and terminal states are fully declared
- `hoi4.probability_render` when a matrix or sensitivity view improves review

The auditor remains read-only. The parent or owning patch agent chooses balance targets and edits source.

## Named probability scenarios

### HW-AI-01 Peaceful Urban Major

**State:** Peace, large capital and two industrial cities at Extreme, strong stockpiles, no Famine.

**Expected ordering:** Protect Population Centres first, cooling and water actions above industrial preservation, no army protocol action.

### HW-AI-02 Agrarian Low-Infrastructure Minor

**State:** Two key agricultural states at Dangerous and rising, weak roads, limited trucks, no large city.

**Expected ordering:** Defend the Harvest, one focused harvest mission, water protection above expensive rail project.

### HW-AI-03 Desert Warfront Major

**State:** Major war, 30 divisions in Extreme desert front, low supply, adequate civilian sector.

**Expected ordering:** Sustain the Front, army protocols, rail corridor, rotation. Population actions remain secondary unless a city reaches lethal conditions.

### HW-AI-04 Northern Industrial Country

**State:** Most states Manageable, one dense industrial capital at Dangerous, cooler nights.

**Expected ordering:** Night shifts and water protection. No evacuation and low harvest spending.

### HW-AI-05 Existing Famine and Devastation

**State:** Active Famine, damaged infrastructure, Extreme heat, poor import route.

**Expected ordering:** Food route, water, population protection. Industrial preservation should fall sharply.

### HW-AI-06 Evolution I Lethal Capital

**State:** Capital Scorched, water System Failure, mortality active.

**Expected ordering:** Cooling centers, water delivery, rationing, organized evacuation preparation. Other projects delayed.

### HW-AI-07 Evolution II Drying Grain Belt

**State:** Key farm states near permanent degradation threshold.

**Expected ordering:** Harvest protection and water restoration dominate unless the front is existential.

### HW-AI-08 Evolution III Scorched Front

**State:** Near-uninhabitable frontline, Critical units, cooler fallback available.

**Expected ordering:** Rotation or organized withdrawal above continued offensive. Holding remains possible for capital or encirclement prevention.

### HW-AI-09 Import-Dependent Island

**State:** Weak domestic agriculture, valid ports, high convoy need, port at Dangerous.

**Expected ordering:** Port and rail protection, emergency imports, convoy reserve. No impossible land-route action.

### HW-AI-10 Embargoed Country

**State:** Severe food pressure and broad embargo.

**Expected ordering:** Domestic harvest and rationing above blocked imports. Import action weight must be zero when the owner system rejects access.

### HW-AI-11 Special Nonhuman Country

**State:** Actual nonhuman actor controls hot states.

**Expected ordering:** No ordinary civilian, food, cooling-center, or Migration decisions. Military and terrain behavior only where valid.

### HW-AI-12 Recovery State

**State:** Global intensity zero, water and rail damage remain.

**Expected ordering:** Repair projects only. All onset and surge decisions weight zero.

### HW-AI-13 Competing Catastrophes

**State:** Lethal capital, failing grain belt, major hot front, limited resources.

**Expected ordering:** National profile should select the consequence with highest near-term expected loss. The sweep should show clear changes as mortality, front importance, and food risk vary.

### HW-AI-14 No Valid Action

**State:** All states Manageable, no exposed units, no damage.

**Expected ordering:** AI takes no paid action. It should not spend resources because the category is visible.

## Scenario evidence requirements

For each scenario, record:

- source revision
- scenario ID
- complete or incomplete candidate pool
- exact external state assumptions
- evaluated scores or probabilities
- expected ordering
- actual ordering
- dominance or starvation findings
- unresolved factors

After a source patch, compare the same scenario IDs. Do not replace them with easier cases.

## AI rejection conditions

Reject AI behavior when:

- Balanced Emergency Plan dominates every scenario
- AI always protects industry because factory count outweighs mortality
- AI evacuates manageable states
- AI buys actions without valid targets
- AI empties critical logistics stockpiles
- AI ignores lethal urban exposure during peace
- AI abandons an existential front without a replacement line
- AI keeps training units in Scorched states
- AI continues emergency actions after recovery
- special nonhuman actors use ordinary civilian decisions
