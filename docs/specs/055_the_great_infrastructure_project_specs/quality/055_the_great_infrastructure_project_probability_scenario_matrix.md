# Event 55 Probability Scenario Matrix

## Evidence status

This is the planning contract for a later read-only `chaosx_ai_probability_auditor` pass.

The current package does not claim exact event, target, candidate, partner, or AI selection probabilities because no final implementation pool exists.

Each scenario begins as score-ordering and hard-zero evidence. Exact normalized results require the complete candidate pool and external state.

## Surface A: Event target selection

### Scenario T1, broad unserved world

State:

- thirty valid ordinary countries
- twenty-five have never received Event 55
- five have active programs
- no recent-target cooldowns among the unserved countries

Expected ordering:

- every valid unserved country scores above a served country with no emergency
- recent recipient would score zero
- special and capitulated actors score zero
- no single major should dominate only because it owns more states

### Scenario T2, damaged existing recipient

State:

- several unserved countries remain
- one served country has a Severed strategic route
- one served country has an idle program

Expected ordering:

- unserved countries remain the main group
- the damaged recipient scores above the idle served recipient
- damaged assistance does not become more common than first-time program establishment while many unserved countries remain

### Scenario T3, almost universal distribution

State:

- nearly every valid country has received Event 55
- several served countries have different project states

Expected ordering:

- damaged or suspended project assistance scores highest
- stale proposal renewal scores above an ordinary active-project breakthrough
- recent recipients remain zero

## Surface B: Project family selection

### Scenario P1, peaceful industrial continental major

State:

- wide country
- strong civilian industry
- several industrial regions
- distant coast and frontier
- no embargo
- adequate trains and trucks

Expected ordering:

- national railway and strategic highway are strong
- resource corridor depends on a real remote resource source
- grand port is competitive only at a strong coastal node
- fixed links remain zero without a registered crossing

### Scenario P2, wartime continental major with supply strain

State:

- active land war
- weak rail connection to front
- strong train reserve
- moderate National Works Capacity

Expected ordering:

- railway or military highway toward the supply problem leads
- accelerated schedule gains method preference
- prestige or unrelated port project falls
- a multi-year continental network falls unless it directly solves the war need and remains feasible

### Scenario P3, maritime trading state

State:

- compact territory
- strong convoy reserve
- major port
- friendly trade partners
- weak need for a long domestic trunk

Expected ordering:

- grand port and international trade corridor lead
- highway can remain useful for port hinterland
- long railway scores low
- fixed crossing appears only with a registry entry

### Scenario P4, poor wide country

State:

- large route distances
- weak civilian industry
- low train and truck reserves
- stable peace

Expected ordering:

- smaller resource or regional highway proposal leads
- continent-scale railway remains valid only if a strong strategic need exists, but AI start willingness stays low
- AI should wait or seek foreign finance rather than consume defense stockpiles

### Scenario P5, compact coastal minor

State:

- one or two states
- useful port
- moderate industry
- no domestic long route

Expected ordering:

- grand port or compact highway project can qualify
- false continental railway and coast-to-coast variants score zero
- international corridor depends on a real adjacent or maritime partner route

### Scenario P6, resource-rich interior

State:

- important remote resource state
- weak link to industry or port
- import dependence on the same resource family

Expected ordering:

- resource corridor leads
- railway or highway mode follows route geography
- unrelated port project remains lower unless it is the destination of the corridor

### Scenario P7, friendly regional bloc

State:

- three friendly neighboring countries
- complementary industry, resources, and ports
- no active war among them
- stable route control

Expected ordering:

- international corridor is strong
- partner willingness is positive
- contributions scale with route share
- no partner with no benefit should accept a large burden

### Scenario P8, hostile borders and active embargo

State:

- intended transit countries are hostile
- host is embargoed
- a domestic resource alternative exists

Expected ordering:

- hostile international route is zero
- domestic resource corridor rises
- alternative route through nonparticipating friendly states can qualify
- Event 55 cannot nullify the full embargo

### Scenario P9, Evolution II extreme engineering

State:

- valid registered crossing
- strong capacity
- peaceful bilateral relationship
- major strategic connection

Expected ordering:

- bridge or tunnel becomes competitive
- conservative method gains preference
- the family is zero when the crossing token is removed
- cost and duration remain much higher than ordinary national projects

### Scenario P10, Evolution III world network

State:

- experienced host
- at least three stable partners
- several completed national routes
- high capacity
- no war among core participants

Expected ordering:

- continental network can lead
- network remains low or zero if one critical partner refuses
- a third project slot is used only in the highest capacity stage

## Surface C: Construction method

### Scenario M1, peacetime fixed link

Expected order:

- conservative engineering
- standard public works
- accelerated schedule

### Scenario M2, urgent relief artery

Expected order:

- accelerated schedule when the route can finish in time and reserves are adequate
- standard public works
- conservative engineering

### Scenario M3, marginal capacity and prior overrun

Expected order:

- standard or conservative method
- accelerated schedule receives a strong penalty
- AI can refuse to start any method

## Surface D: Partner response

### Scenario R1, fair allied corridor

Expected order:

- accept
- counteroffer
- delay
- refuse

### Scenario R2, useful route with unfair burden

Expected order:

- counteroffer
- accept as transit partner
- refuse
- full acceptance remains lower

### Scenario R3, hostile claimant

Expected order:

- refusal is dominant
- acceptance is zero when war or invalid hostility gate applies

### Scenario R4, relief emergency

Expected order:

- acceptance rises for a safe relief route
- military access remains separate unless the agreement includes it

## Surface E: Trouble response

### Scenario F1, near-complete suspended railway

Expected order:

- resume or repair
- reduce scope
- reroute
- abandon
- new project start remains below recovery actions

### Scenario F2, permanently lost foreign terminal

Expected order:

- reroute or reduce scope
- transfer when valid
- abandon
- continued full funding scores zero

### Scenario F3, strained completed port

Expected order:

- maintenance or repair
- partner assistance when relevant
- no duplicate new grand port at the same node

## Dominance expectations

In a broad mixed-geography test pool, no one ordinary project family should exceed a design share of roughly `55%` unless the supplied geography makes other families invalid.

This is a balance expectation, not an exact probability claim.

## Required MCP workflow

1. Run `hoi4.probability_inspect` on each weighted surface.
2. Record the complete candidate pool and external factors.
3. Use `hoi4.probability_evaluate` for named scenarios.
4. Use sweeps for National Works Capacity, war state, partner count, and project scale.
5. Apply owner-selected weight changes outside the read-only auditor.
6. Run `hoi4.probability_compare` against the same scenario IDs.
7. Render matrix or sensitivity evidence when it improves review.
8. Mark incomplete pools as unresolved, not exact.
