# Event 050 acceptance scenarios

These scenarios are implementation and audit targets. They are not claims of completed runtime testing.

## Scenario A: Import-dependent player opening

Setup:

- one eligible player country
- high oil and rubber dependence
- shallow fuel stockpile
- several valid majors

Expected:

- player can be selected through the intended class roll
- opening Pressure reflects coalition quality
- fuel or imported materials appear as the urgent exposure
- replacement-supply mission starts
- category shows no more than five primary actions
- at least one intermediary, smuggling, and self-sufficiency path is valid

## Scenario B: Self-sufficient continental major

Setup:

- AI major with domestic resources and land access
- strong stability and army
- normal coalition

Expected:

- economic damage is lower than Scenario A at the same Pressure
- AI favors defiance, diplomacy, or selective adaptation
- the embargo still matters through foreign support and efficiency loss
- AI does not offer an excessive concession immediately

## Scenario C: Coalition collapse

Setup:

- weak justification
- two conditional core enforcers
- useful neutral route

Expected:

- target opens replacement supply
- core members defect according to contribution
- Pressure enters the collapsing band
- crisis ends only after confirmation or decisive collapse
- outcome records coalition failure and clears the ledger

## Scenario D: Negotiated settlement

Setup:

- strong convenor
- target has critical dependence
- one valid limited concession

Expected:

- player sees the exact public commitment
- convenor and core participants evaluate the same settlement package
- acceptance lowers Pressure or ends the crisis
- obligation persists for its intended term
- cleanup does not remove the concession

## Scenario E: Smuggling exposure under baseline

Setup:

- valid neutral route
- no Evolution I
- medium enforcement

Expected:

- success, partial exposure, and public exposure are possible
- clean success gives material relief
- exposure raises Pressure and affects the host
- no secondary-sanction action appears without Evolution I

## Scenario F: Evolution I secondary sanctions

Setup:

- Chaos at least 400
- Evolution I enabled
- active intermediary route
- strong coalition

Expected:

- evolution uses pacing unless active before firing
- evolution log records once
- neutral receives a real compliance choice
- continuing trade has economic value and real risk
- coalition pays a bounded enforcement cost
- evasion remains viable

## Scenario G: Resource Seizure

Setup:

- Pressure at least 70
- critical oil shortage
- reachable vulnerable oil region
- target has sufficient army and fuel

Expected:

- preparation mission names the region and staging requirements
- stockpile and map conditions matter
- coercive access, war, intervention, and abandonment are possible
- no free cores appear
- generic war and Deaths systems own later consequences

## Scenario H: Unsafe Resource Seizure blocked

Setup:

- severe Pressure
- only resource target belongs to a much stronger faction
- target army is weak

Expected:

- AI refuses the route
- human sees a clear blocked reason
- no invalid war goal or target is created

## Scenario I: Evolution II two targets

Setup:

- Chaos at least 800
- Evolution II active before firing
- two or more free ledger slots

Expected:

- two or three distinct targets are selected within the cap
- each receives its own coalition, Pressure, duration, and decisions
- one global event firing is recorded
- additional targets appear in event-specific detail or reports

## Scenario J: Overlapping coalition roles

Setup:

- country X is core against target A
- country X is neutral toward target B
- country X is intermediary for target C

Expected:

- roles stay separate by sequence
- grouped presentation avoids popup spam
- one crisis choice does not overwrite the others
- cleanup of target A preserves roles for B and C

## Scenario K: Sanction-breaker cooperation

Setup:

- three active targets
- complementary resources and valid routes
- targets are not at war with one another

Expected:

- network opens real barter or transport actions
- benefits depend on complementary supply
- exposure or betrayal can affect several ledgers
- network dissolves after fewer than two targets remain
- no permanent faction is created by default

## Scenario L: Condemnation overlap

Setup:

- target has public Condemnation sanctions and Event 50

Expected:

- coalition justification can use public Condemnation
- shared native embargo behavior is not applied twice
- Event 50 resolution leaves Condemnation state intact
- public text does not reveal hidden evidence

## Scenario M: Famine risk without automatic famine

Setup:

- embargoed island target with food imports
- sufficient reserves and open relief corridor

Expected:

- Event 50 adds route pressure
- famine does not begin without its own validated conditions
- no direct Event 50 death tick occurs

Then remove reserves and close relief access through valid owner systems.

Expected:

- famine owner can register the crisis
- famine values and deaths remain famine-owned

## Scenario N: Repeat firing against former target

Setup:

- one completed Event 50 crisis
- later repeat selects the same country

Expected:

- fresh coalition, Pressure, duration, targets, and response state
- prior durable projects and obligations remain correctly
- no old route or review marker leaks

## Scenario O: Multiplayer human intermediary

Setup:

- player A is target
- player B is selected neutral intermediary

Expected:

- player B receives a timed meaningful choice
- ignoring the event uses the stated default
- authoritative effects apply once
- player A sees the result without duplicated global outcomes

## Scenario P: Cluster firing

Setup:

- Negative Economy cluster triggers Event 50 with other members

Expected:

- cluster counts once for global pacing
- Event 50 history and repeatable handling still apply
- target collision rules work
- Great Depression 2.0 and Event 50 do not stack on one target unless an accepted high-chaos cluster rule allows it
- skip reasons are visible

## Scenario Q: Full cleanup

Setup:

- Evolution II active
- three crises with shared participants
- resolve the middle crisis first

Expected:

- middle target loses all crisis-owned state
- other two crises continue unchanged
- active registry count falls immediately
- later Event 50 firing can use the free slot
- no stale decisions, missions, targets, or modifiers remain
