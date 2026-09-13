# Event 41 AI probability scenario plan

## Audit purpose

The implementation must prove that AI action weights respond to the military situation. The audit should compare action ranking and threshold reversals. It should not claim exact selection probabilities when the complete candidate pool or external AI state is unavailable.

The probability auditor should begin with `hoi4.probability_inspect` for every weighted decision, event option, evolution MTTH surface, target selector, and random profile selection surface.

Use:

- `hoi4.probability_evaluate` for the named scenario matrix
- `hoi4.probability_sweep` for pressure, supply, front threat, and medical-capacity thresholds
- `hoi4.probability_compare` after implementation or any weight patch
- `hoi4.probability_render` for ranking and sensitivity evidence
- `hoi4.probability_simulate` only when an input is intentionally uncertain and declared as a range
- `hoi4.probability_sequence` only if the complete episode cadence and every state transition in the tested custom pool are declared

## Candidate action families

The audit should include every action visible in the tested state:

- rotate the sickest formations
- establish quarantine camps
- expand field hospitals
- sanitize camps and supply
- assign medical evacuation priority
- repair the medical corridor
- emergency medical mobilization
- isolate the military district
- abandon the contaminated sector
- restrict offensive operations
- preserve ordinary operations
- fight through the outbreak
- Evolution I coalition actions
- Evolution II port, demobilization, access, and civilian-hub actions

An unavailable action should be absent or score zero for a proven reason.

## Scenario A: Supplied major, localized outbreak

### State

- pressure: 32
- supply: strong
- field hospitals: strong
- transport: ample
- front threat: moderate
- active infected nodes: one
- profile indicators: camp-borne
- capital threat: none

### Expected ordering

1. sanitation or quarantine
2. rotation
3. field-hospital expansion
4. evacuation
5. offensive restriction
6. fight through near the bottom

### Expected behavior

The AI should use an early low-disruption response and avoid emergency measures.

## Scenario B: Undersupplied minor, spreading enteric outbreak

### State

- pressure: 55
- supply: poor
- infrastructure: damaged
- field hospitals: weak
- transport: scarce
- front threat: moderate
- profile indicators: enteric
- one valid damaged medical corridor

### Expected ordering

1. repair medical corridor or sanitize supply, depending current blocking proof
2. field-hospital expansion if affordable
3. quarantine
4. rotation only when a valid safe area exists
5. evacuation below corridor repair while the route is broken
6. fight through very low

### Expected behavior

The AI should recognize that evacuation is ineffective before the route is repaired. It should not spend unavailable trains or trucks.

## Scenario C: Capital threatened during a moderate outbreak

### State

- pressure: 48
- front includes capital approach
- enemy breakthrough risk: severe
- reserves: limited
- medical capacity: average
- transport: valid
- operational opportunity window: short

### Expected ordering

1. field hospitals or sanitation that can operate without pulling the line apart
2. preserve ordinary operations
3. controlled evacuation of the sick when it does not remove critical formations
4. fight through can rise above full rotation for a bounded period
5. abandon sector scores zero

### Expected behavior

The AI should defend the capital without treating disease as irrelevant. Fight through becomes plausible but not dominant unless the strategic danger is immediate.

## Scenario D: Army crisis with stable defensive line

### State

- pressure: 88
- front threat: manageable
- supply: average
- medical overload: severe
- active nodes: two
- civilian spillover: unavailable at baseline

### Expected ordering

1. emergency medical mobilization
2. restrict offensive operations
3. rotation or district isolation
4. evacuation
5. field hospitals
6. fight through at or near zero

### Expected behavior

The AI accepts large temporary costs to avoid a shattered infected front.

## Scenario E: No safe rear area

### State

- pressure: 62
- infected sector: isolated or nearly encircled
- rear destination: invalid
- transport route: blocked
- field hospitals: weak
- enemy pressure: high

### Expected ordering

1. in-place quarantine
2. local field hospitals
3. sanitation if supplies can reach the node
4. corridor repair when feasible
5. rotation and evacuation unavailable
6. abandon sector only when a valid fallback route appears

### Expected behavior

The AI should never start an impossible rotation mission.

## Scenario F: Evolution I allied coalition front

### State

- pressure: 57 in source country
- shared hub: active
- allied expeditionary formations: present
- ally medical capacity: average
- relations: strong
- foreign full outbreak: not yet present

### Expected ordering for source country

1. exchange field medical reports
2. separate coalition camps
3. quarantine or sanitation in shared node
4. restrict allied access only when lighter measures fail

### Expected ordering for exposed ally

1. inspect allied formations
2. early quarantine
3. avoid redeployment to another theater
4. ordinary operations only after exposure clears

### Expected behavior

Cooperative measures should dominate punitive access closure under normal allied relations.

## Scenario G: Evolution II port spillover risk

### State

- pressure: 73
- infected military port: active
- civilian population: high
- transport hub: crowded
- distant troop movement: scheduled
- alternate port: available
- civilian spillover receipt: none yet

### Expected ordering

1. protect civilian transport hubs
2. close or screen the infected military port
3. divert troop movement to the alternate port
4. field hospitals or evacuation
5. preserve ordinary port traffic low

### Expected behavior

The AI should accept the port cost because a viable alternative exists and civilian risk is high.

## Scenario H: War ends during War Plague

### State

- pressure: 61
- war state: ended
- returning formations: many
- civilian hubs: exposed
- transport: adequate
- civilian spillover receipt: none

### Expected ordering

1. controlled demobilization
2. protect civilian transport hubs
3. field hospitals and sanitation
4. unrestricted demobilization at or near zero

### Expected behavior

The end of combat lowers pressure but raises the importance of safe return routes.

## Evolution pacing scenarios

### Evolution I active-event MTTH

Compare:

- contained pressure 25, one node, no foreign contact
- pressure 60, several crowded nodes, allied front contact
- pressure 82, prolonged outbreak, failed quarantine, shared hub

Expected result:

- the contained scenario has the longest timing band
- the severe shared-front scenario has the shortest timing band
- none activates instantly through a routine threshold crossing

### Evolution II active-event MTTH

Compare:

- pressure 45, no civilian hub, one country
- pressure 68, large military hospital in a populated damaged state
- pressure 85, three countries, famine and refugee pressure, infected port

Expected result:

- the international damaged-hub scenario strongly outranks the isolated military scenario
- disabled Evolution II produces no valid candidate

## Profile-selection audit

The hidden profile selector should use a complete declared candidate pool.

Expected rank changes:

- cold crowded static front favors camp-borne
- hot damaged urban supply favors enteric
- warm wet jungle or marsh with long exposure favors tropical and vector-borne
- no profile should be impossible in all ordinary theaters unless its environmental gates fail
- the selector should preserve enough variation that one condition does not force the same profile in every episode

## Target-country audit

The target selector should compare valid at-war ordinary countries only.

Expected ordering:

- prolonged undersupplied crowded front above a rested dispersed front
- recent survivor below an otherwise similar country
- special Chaos country excluded
- country without a valid active front excluded
- active Event 41 country excluded from a new root firing

## Required comparison evidence

After any source change to weights, the probability auditor should compare the same scenario IDs before and after the patch. The handoff should state:

- surface inspected
- scenario inputs
- candidate pool completeness
- result type, such as exact, bounded, sampled, score-only, or unresolved
- expected and observed ranking
- threshold reversals
- dominance or starvation concerns
- comparison revision or artifact reference
