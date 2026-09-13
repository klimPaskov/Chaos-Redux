# Gods of Africa AI and probability scenario contract

## Purpose

This document defines the named scenarios required for weighted-logic inspection and comparison.

No probabilities were evaluated in the planning environment because the live source pools and HOI4 MCP route were unavailable. The implementation agent must build the complete candidate pools from source before claiming exact or normalized results.

## Required workflow

For every weighted surface:

1. run `hoi4.probability_inspect`
2. identify complete candidates, modifiers, external state, exclusions, and normalization behavior
3. run the appropriate evaluate, sweep, simulation, sequence, comparison, or render operation
4. classify the result as exact, bounded, sampled, score-only, or unresolved
5. let the owning agent patch source
6. run `hoi4.probability_compare` against the same named scenarios

Do not use sequence analysis unless cadence, cooldown, removal, reset, and terminal rules are fully declared.

## Surface A: participant response

Candidate pool:

- fulfill
- propose substitute
- request extension
- refuse
- permanent defiance

### `RESP-COOPERATIVE-AFFORDABLE`

State:

- Strength `70`
- Wrath `15`
- demand burden `7 percent` of usable reserve
- target at peace
- positive hidden history
- no African territory held
- Africa is a useful ally

Expected ordering:

1. fulfill
2. substitute
3. extension
4. refuse
5. defiance

Acceptance:

- fulfill has clear dominance
- defiance is possible only at a very low score

### `RESP-COOPERATIVE-HARDSHIP`

State:

- Strength `70`
- Wrath `10`
- demand burden `25 percent` of usable reserve
- target losing a major war
- positive hidden history
- extension and substitutes valid

Expected ordering:

1. substitute or extension
2. fulfill
3. refuse
4. defiance

Acceptance:

- AI should seek a workable alternative before refusing
- direct fulfillment should remain possible for an allied emergency

### `RESP-GAMBLER-WEAK-AFRICA`

State:

- Strength `15`
- Wrath `35`
- burden `15 percent`
- target is stronger than Africa
- no alliance
- no African territory held

Expected ordering:

1. substitute or refuse
2. extension
3. fulfill
4. defiance

Acceptance:

- refusal should score materially above compliance
- permanent defiance should not automatically dominate because ordinary gambling remains available

### `RESP-OCCUPIER`

State:

- Strength `55`
- Wrath floor `60`
- target controls African core territory
- demand is territory return
- target seeks continued occupation

Expected ordering:

1. refuse or defy
2. comply depending military balance
3. extension
4. substitute only if territory demand permits a settlement

Acceptance:

- military balance and war plans drive the top choice
- substitute cannot bypass the exact land issue with trivial material

### `RESP-LOYAL-ALLY-EMERGENCY`

State:

- Strength `65`
- Wrath `0`
- Africa losing a major war
- target has a strong alliance and aid history
- emergency equipment demand burden `18 percent`

Expected ordering:

1. fulfill
2. substitute with another urgently needed family
3. extension
4. refuse
5. defiance

Acceptance:

- alliance obligation and hidden history materially change the result

### `RESP-ABUSIVE-AFRICA`

State:

- Strength `80`
- Wrath `20`
- target complied with five recent demands
- new punitive burden `35 percent` without a valid offense
- reciprocal doctrine

Expected ordering:

1. refuse or substitute
2. extension
3. fulfill
4. defiance rises compared with cooperative baseline

Acceptance:

- the AI should react to demand abuse
- reciprocal doctrine should make this state rare through demand selection before response weighting

## Surface B: permanent defiance

### `DEFY-LOW-CREDIBILITY`

State:

- Strength `10`
- target much stronger
- no alliance or positive history
- repeated demands are expensive

Expected:

- defiance receives a strong score

### `DEFY-HIGH-CREDIBILITY`

State:

- Strength `90`
- high Chaos
- target has weak defenses
- no powerful coalition

Expected:

- defiance remains possible but scores below negotiation or selective compliance

### `DEFY-IDEOLOGICAL-RIVAL`

State:

- target leads hostile bloc
- occupies African territory
- already at high Wrath
- expects war

Expected:

- defiance dominates normal compliance choices

### `DEFY-LOYAL-PARTNER`

State:

- strong positive history
- African protection active
- no major burden shock

Expected:

- defiance is effectively starved without a major route change

## Surface C: demand family selection

Candidate families must be complete for the inspected evolution and DLC state.

### `DEMAND-AFRICA-FUEL-CRISIS`

State:

- Africa fuel reserve critically low
- active mechanized and air war
- target has large fuel surplus
- target also has rifle surplus

Expected ordering:

1. fuel
2. trucks or transport
3. aircraft or armor where valid
4. rifles

### `DEMAND-RAIL-COLLAPSE`

State:

- Event 012 rail corridors damaged
- Africa has few trains and convoys
- target has valid transport surplus

Expected ordering:

1. trains
2. convoys
3. industrial repair
4. fuel

### `DEMAND-AIR-DEFICIT`

State:

- Africa faces strategic bombing
- aircraft stock and production are low
- target produces aircraft
- Evolution II active

Expected ordering:

1. aircraft
2. fuel
3. anti-air or industrial support if represented

### `DEMAND-TERRITORIAL-OCCUPIER`

State:

- target holds African core territory
- no active peace settlement

Expected:

- territory-return demand dominates material families

### `DEMAND-SURPLUS-SUPPRESSION`

State:

- Africa has large rifle surplus
- no rifle deficit
- target has rifles and several other valid capacities

Expected:

- rifle family is heavily suppressed unless doctrine or current plan gives a real reason

### `DEMAND-RECENT-FAMILY`

State:

- last two demands used fuel
- fuel need remains moderate
- trains and industrial support are also needed

Expected:

- recent-family penalty moves trains or industry above fuel
- severe fuel emergency can override the diversity penalty

### `DEMAND-DLC-PARITY`

Compare:

- full DLC setup
- base-game setup

Acceptance:

- core strategic role remains available in both
- DLC-only candidate receives zero validity without removing all valid options

## Surface D: demand burden band

Candidate bands:

- ceremonial
- standard
- severe
- emergency
- punitive

### `BAND-LOW-WRATH-WEAK-TARGET`

State:

- low Wrath
- weak major
- no emergency
- limited Strength

Expected:

- ceremonial or standard dominates

### `BAND-HIGH-NEED-STRONG-TARGET`

State:

- Africa in major emergency
- strong target with surplus
- medium Wrath
- global Strength

Expected:

- emergency band dominates

### `BAND-PUNITIVE-OFFENDER`

State:

- repeated failures
- high Wrath
- proven occupation
- high Strength
- target has capacity

Expected:

- punitive band becomes possible and may lead

### `BAND-PUNITIVE-NO-OFFENSE`

State:

- high Strength
- low Wrath
- compliant history
- no current emergency

Expected:

- punitive band has zero validity

## Surface E: punishment tier

This surface should use deterministic gates before weighted family choice.

### `TIER-WEAK-MAX-WRATH`

State:

- Strength `10`
- Wrath `100`
- repeated failures
- high Chaos

Expected:

- capability tier equals I
- every Tier II to V candidate is excluded before normalization

### `TIER-REGIONAL-MAX-WRATH`

State:

- Strength `30`
- Wrath `100`

Expected:

- capability tier equals II

### `TIER-CONTINENTAL-MAX-WRATH`

State:

- Strength `50`
- Wrath `100`

Expected:

- capability tier equals III

### `TIER-GLOBAL-FIRST-REFUSAL`

State:

- Strength `75`
- Wrath rises from `20` to `35`
- first ordinary refusal
- no major offense

Expected:

- first-failure cap restricts result to Tier I or II

### `TIER-GLOBAL-REPEATED-OFFENSE`

State:

- Strength `75`
- Wrath `80`
- three serious failures
- territory occupation

Expected:

- Tier IV can become valid

### `TIER-EXTREME-INCOMPLETE-GATE`

State:

- Strength `90`
- Wrath `95`
- Chaos `500`
- serious offense

Expected:

- Tier V excluded due Chaos gate

### `TIER-EXTREME-FULL-GATE`

State:

- Strength `90`
- Wrath `95`
- Chaos `850`
- repeated serious offense
- Evolution III
- Africa stable
- no recent extreme cooldown

Expected:

- Tier V becomes valid
- lower tiers remain possible unless design explicitly commits an ultimatum

## Surface F: punishment family

Candidate families depend on selected tier.

### `PUNISH-OCCUPATION`

State:

- target holds African cores
- Tier III

Expected ordering:

1. supply or military disruption
2. unrest in occupied African states
3. diplomatic isolation
4. unrelated stockpile event

### `PUNISH-BROKEN-EQUIPMENT-PACT`

State:

- target promised equipment then cancelled
- Tier II

Expected ordering:

1. production or stockpile disruption
2. military readiness pressure
3. general diplomatic pressure

### `PUNISH-HIGH-CHAOS-AMBIGUOUS`

State:

- high Chaos
- Tier IV
- target has vulnerable disaster states
- no recent disaster family

Expected:

- natural disaster weight rises
- direct atrocity route does not become automatic

### `PUNISH-RECENT-DISASTER`

State:

- target recently received same disaster family
- several non-disaster families valid

Expected:

- repetition penalty moves another family above it

### `PUNISH-ATTRIBUTION-RISK`

State:

- Africa uses reciprocal doctrine
- target is a useful trade partner
- direct action would create high condemnation

Expected:

- covert, diplomatic, or limited family scores above openly attributable mass violence

## Surface G: substitute acceptance

### `SUB-NEEDED-EQUIVALENT`

State:

- requested aircraft
- target offers fuel of equivalent burden
- Africa also has severe fuel deficit
- low Wrath

Expected:

- high acceptance

### `SUB-UNNEEDED-OBSOLETE`

State:

- target offers obsolete rifles
- Africa has rifle surplus
- high Wrath

Expected:

- rejection dominates

### `SUB-RELIABLE-PARTNER`

State:

- moderate value gap
- strong history
- reciprocal doctrine

Expected:

- acceptance score rises compared with neutral baseline

### `SUB-REPEAT-BAD-FAITH`

State:

- prior broken substitute agreements
- low-value offer

Expected:

- rejection strongly dominates

## Surface H: extension acceptance

### `EXT-GOOD-HISTORY-LOGISTICS`

State:

- good history
- target route disrupted by war
- partial upfront payment offered

Expected:

- acceptance dominates

### `EXT-REPEAT-DELAY`

State:

- two prior delays
- high Wrath
- no upfront value

Expected:

- rejection dominates

### `EXT-AFRICAN-EMERGENCY`

State:

- urgent wartime need
- short original deadline

Expected:

- extension score falls unless alternative support arrives immediately

## Surface I: Africa target selection

### `TARGET-OCCUPIER`

State:

- one participant occupies African cores
- several neutral participants are due

Expected:

- occupier gains strong priority

### `TARGET-AVOID-HARASSMENT`

State:

- one compliant participant received the previous demand
- several equally capable participants are eligible

Expected:

- recent-target penalty moves others above it

### `TARGET-EMERGENCY-CAPACITY`

State:

- Africa needs aircraft
- only two participants can provide them

Expected:

- valid providers dominate target pool

### `TARGET-HARDSHIP-DEFER`

State:

- due participant is near capitulation and cannot provide any meaningful family

Expected:

- target receives a defer or ceremonial result and does not block the queue

### `TARGET-HUMAN-STAGGER`

State:

- several human participants become due together

Expected:

- deterministic dispatch budget separates demand dates

## Surface J: protection target

### `PROTECT-FAVORED-CRISIS`

State:

- participant has strong positive history
- low Wrath
- major disaster
- Africa has capacity

Expected:

- protection receives high score

### `PROTECT-NEUTRAL-CRISIS`

State:

- participant has neutral history
- same crisis

Expected:

- score below favored case

### `PROTECT-DEFYING`

State:

- permanent defiance

Expected:

- normal protection excluded

### `PROTECT-AFRICA-WEAK`

State:

- partner qualifies
- Africa lacks stockpile and units

Expected:

- large military package excluded
- modest diplomatic or relief action may remain

## Surface K: doctrine and focus route

### `FOCUS-STABLE-COALITION`

State:

- Africa secure
- several friendly powers
- low foreign occupation

Expected:

- Reciprocal Covenant scores above Sovereign Exaction

### `FOCUS-OCCUPIED-CONTINENT`

State:

- foreign powers hold major African regions
- several demands refused
- Africa at war

Expected:

- Sovereign Exaction and Judgment routes rise

### `FOCUS-EMERGENCY-SUPPLY`

State:

- Africa losing war due fuel and transport shortage

Expected:

- Provision emergency nodes dominate unrelated diplomatic content

### `FOCUS-NO-TIER-V-GATE`

State:

- Evolution III absent or Strength permanently low

Expected:

- late extreme policy receives zero validity

## Sensitivity sweeps

Run sweeps over:

- Strength from `0` to `100` in steps of `10`
- Wrath from `0` to `100` in steps of `10`
- burden from `0` to `40 percent` of usable reserve
- Chaos tiers from Calm World through World Collapse
- failure count from `0` to at least `5`
- positive history from none to exceptional
- African need score from surplus to critical deficit

Required rendered views:

- participant response heatmap by Strength and burden
- punishment tier matrix by Strength and Wrath with gate overlays
- demand family comparison under African need scenarios
- doctrine route comparison
- before and after probability comparison for every patched surface

## Starvation and dominance checks

Flag a failure when:

- defiance has meaningful weight for loyal partners without a major shock
- compliance dominates even when the target faces ruin and Africa is weak
- punitive demand band appears without offense or emergency
- one demand family dominates across unrelated need states
- natural disasters dominate every high-Chaos punishment pool
- Tier V becomes automatic whenever its gate opens
- priority offender logic starves every other participant indefinitely
- recent-family penalty prevents an urgent repeated request
- a DLC candidate leaves the base-game pool empty

## Sequence analysis contract

Use `hoi4.probability_sequence` only after declaring:

- participant cooldown formula
- active-demand budget
- demand completion and failure timing
- recent-target penalties
- recent-family penalties
- Wrath transactions
- Strength update cadence
- system ending rules
- defiance removal from ordinary queue
- target invalidation

Named long-run sequences:

- `SEQ-COOPERATIVE-5Y`
- `SEQ-GAMBLER-5Y`
- `SEQ-DEFIANT-5Y`
- `SEQ-AFRICA-WAR-3Y`
- `SEQ-MULTIPLAYER-4P-3Y`

Expected long-run behavior:

- cooperative participant receives varied demands and trends toward low Wrath
- gambler experiences occasional punishment without automatic extreme escalation
- defiant participant receives no ordinary demand leakage
- Africa at war shifts toward emergency need families
- four human players receive staggered demand cadence

## Reporting template

For each scenario, record:

- scenario ID
- source revision
- inspected surface
- complete candidate pool status
- external factor completeness
- tool used
- exact or other evidence classification
- baseline result
- intended ordering
- patch owner
- comparison result
- remaining uncertainty
