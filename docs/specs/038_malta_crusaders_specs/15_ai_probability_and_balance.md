# AI, probability, and balance specification

## Purpose

Event 38 contains many weighted surfaces. Source inspection alone cannot prove their behavior. Every probability-bearing surface requires a baseline audit, an owner-approved tuning change, and a comparison under the same named scenarios.

The probability auditor remains read-only and never chooses the design target.

## Weighted surfaces

Required audit surfaces include:

- Event 38 automatic selection eligibility and cluster interaction
- opening conditional foothold selection
- pre-fire package alternatives
- evolution MTTH and factor models
- order demand selection
- active order incident selection
- relic expedition outcomes
- relic dispute and exposure timing
- principality candidate selection
- principality AI routes
- Malta focus AI
- Malta decision AI
- sponsor and volunteer selection
- regional campaign target selection
- Papal support and rejection choices
- Teutonic Order negotiation choices
- Atlantis 90 percent AI option
- Atlantis regional target priorities
- Holy World believer and nonbeliever assignment
- Holy World regional war order
- manual scenario side balance
- terminal settlement choices

## Evidence classes

The audit must label results as:

- exact
- bounded
- sampled
- score-only
- unresolved

Exact probability cannot be claimed when the candidate pool or external factors are incomplete.

## Core AI principles

### Survival before spectacle

Malta AI protects Malta, Jerusalem, the bridge, and supply before pursuing distant claims, relics, or hidden routes.

### Coherent fronts

AI prioritizes one connected campaign region. It avoids scattered one-state wars.

### Affordable formations

AI builds custom units only when it has the equipment, supply, fuel, and cap capacity. It uses ordinary infantry and militia for routine line holding.

### Political consistency

AI routes reflect government, order balance, Papal relations, local governance, and campaign outcomes. It should not switch from a humane constitutional route into extermination or hidden alliance logic without explicit route conditions.

### Terminal balance

Holy World side assignment must preserve a viable nonbeliever coalition at every manual scenario intensity.

## Named baseline scenarios

### AI-001 Standard regional opening

- 1936 owners
- Chaos below 200
- AI Malta
- no cross-event conflicts
- baseline package

Expected behavior:

- Dodecanese or another coherent island foothold is preferred
- no more than four displaced owners
- AI defends supply and Jerusalem

### AI-002 Human Malta opening

- human Malta
- baseline package

Expected behavior:

- AI does not make player choices
- target selection and event options remain player controlled

### AI-003 Evolution I pre-fire

- Chaos 250
- Evolution I enabled and active before firing

Expected behavior:

- stronger units and orders
- territory normally unchanged

### AI-004 Evolution II constrained map

- Chaos 450
- no valid Jerusalem principality carrier
- Cyprus valid

Expected behavior:

- Crusader Cyprus is selected over an invalid or disconnected actor

### AI-005 Evolution III no sponsor

- Chaos 650
- all likely Catholic sponsors invalid or hostile

Expected behavior:

- use equivalent legitimacy package
- do not force an invalid ally

### AI-006 Supply collapse

- low convoys
- hostile naval superiority
- Jerusalem threatened

Expected behavior:

- escort, air bridge, evacuation, and port defence dominate relic or expansion actions

### AI-007 High Authority, low Cohesion

Expected behavior:

- centralization or formal dominance becomes more attractive
- AI addresses open rivalry before new expansion

### AI-008 High Cohesion, moderate Authority

Expected behavior:

- confederation, mixed-order units, and principality federation become attractive

### AI-009 High Legitimacy, valid Pope

Expected behavior:

- Holy See route is competitive but not forced

### AI-010 Civilian constitutional Malta

Expected behavior:

- humane governance, local restoration, and negotiated settlement gain weight
- hidden Teutonic alliance acceptance falls sharply

### AI-011 Expedition defeated

- Jerusalem lost
- bridge lost
- Malta survives

Expected behavior:

- Eleventh Crusade survival and rebuild actions dominate
- no suicidal immediate reinvasion

### AI-012 Direct occupation burden

- several regions controlled
- resistance high
- Authority functional

Expected behavior:

- principality or local restoration becomes more attractive

### AI-013 Strong Germany hidden route

- all Teutonic conditions valid
- Germany strong
- Malta compatible
- Holy Realm positive

Expected behavior:

- alliance formation has a high but not automatic probability according to route

### AI-014 Incompatible Malta hidden route

- civilian route
- low legitimacy
- Germany strong

Expected behavior:

- Malta normally rejects Teutonic alliance

### AI-015 Atlantis eligible AI Germany

- complete option pool
- all eligibility conditions valid

Expected behavior:

- Atlantis option normalizes to 90 percent
- non-Atlantis option normalizes to 10 percent

### AI-016 Atlantis ineligible

- one founding member absent

Expected behavior:

- Atlantis option is unavailable, not weighted low

### AI-017 Holy World preparation at 900 Chaos

- Pope supreme
- one continent proven

Expected behavior:

- terminal readiness holds
- activation remains unavailable before 1000

### AI-018 Holy World side assignment, Low

Expected behavior:

- modest believer coalition
- most major industry remains nonbeliever

### AI-019 Holy World side assignment, Maximum

Expected behavior:

- extensive believer coalition
- at least two strong nonbeliever industrial centers remain when possible
- no automatic Papal victory

### AI-020 Existing world factions

Expected behavior:

- side assignment and coalition creation do not produce broken duplicate factions or impossible wars

### AI-021 Multiple human players

Expected behavior:

- human side choices are not overridden by AI

### AI-022 Atlantis versus Holy World readiness

Expected behavior:

- route ownership and terminal conflict rule are deterministic

## Tools and workflow

For each surface:

1. run `hoi4.probability_inspect`
2. record the complete candidate pool and external factors
3. define scenario IDs and exact inputs
4. use `hoi4.probability_evaluate` for specific scenarios
5. use `hoi4.probability_sweep` for threshold and factor sensitivity
6. use `hoi4.probability_simulate` only when exact normalization is not practical and sampling conditions are declared
7. use `hoi4.probability_sequence` only for a complete cadence and recovery contract
8. use `hoi4.probability_render` when a matrix, sensitivity plot, timeline, or comparison improves review
9. after tuning, run `hoi4.probability_compare` against the same scenarios

## Opening balance model

The opening force budget should respond to:

- selected state count
- displaced owner strength
- total enemy divisions near the opening theaters
- Malta's industrial base
- evolution package
- AI or human control only where needed for usability
- port and supply capacity

Recommended balance target:

- Malta can survive with competent play
- Malta cannot win every opening war through auto-battle
- enemy majors remain dangerous
- supply failures punish scattered expansion
- the initial special units feel powerful in their roles

## Force budget bands

The exact numbers require implementation evidence. Initial design bands are:

| Package | Special line battalions in fielded divisions | Ordinary guards and militia | Strategic reserve |
| --- | ---: | ---: | ---: |
| Baseline | 20 to 36 | 12 to 24 | 2 to 4 divisions |
| Evolution I | 32 to 52 | 16 to 30 | 3 to 6 divisions |
| Evolution II | 40 to 64 across Malta and subjects | 24 to 42 | 4 to 8 divisions |
| Evolution III | 52 to 80 across coalition | 30 to 54 | 6 to 10 divisions |

These are battalion and division budget bands, not fixed spawn counts. The final setup must compare local combat width, equipment, and enemy strength.

## Public value balance

### Initial bands

| Package | Authority | Cohesion | Legitimacy |
| --- | ---: | ---: | ---: |
| Baseline | 42 to 55 | 35 to 55 | 35 to 50 |
| Evolution I | 45 to 60 | 30 to 55 | 40 to 55 |
| Evolution II | 45 to 65 | 35 to 60 | 45 to 65 |
| Evolution III | 55 to 70 | 40 to 65 | 60 to 75 |

Ranges allow route and random setup variation. Values should be rounded and visible as whole numbers.

### Movement scale

- minor event: 2 to 5 points
- meaningful decision or mission: 5 to 10 points
- major victory, loss, scandal, or settlement: 10 to 20 points

One action should not move a value from collapse to maximum without a route-defining event.

## Decision costs

Costs should scale from country capability. Suggested cost families:

- equipment and manpower for formation raising
- fuel, convoys, and naval commitment for sea operations
- trains, support equipment, and civilian capacity for logistics
- army or navy experience for doctrine and command
- Authority, Cohesion, or Legitimacy as consequences, not generic currencies spent on every action
- stability or war support only when the action genuinely affects domestic politics

No action uses more than four spendable cost types.

## Unit balance

### Armored Knights

Target role: resist low-piercing infantry and attack prepared positions with support.

Hard counters: anti-tank, artillery, air attack, fuel and supply disruption, encirclement.

### Mounted Knights

Target role: exploit open fronts and rapidly reinforce.

Hard counters: forts, dense urban terrain, anti-tank, air attack, remount losses.

### Archers and Crossbows

Target role: low-fuel soft attack and defence.

Hard counters: armour, artillery range, air attack.

### Siege Hosts

Target role: fortress reduction.

Hard counters: mobility, counterbattery, air attack, low supply.

### Blessed formations

Target role: elite concentration.

Hard counters: cap, full equipment cost, legitimacy dependency, normal battlefield losses.

### Atlantean Supreme tanks

Target role: hidden-route spearhead.

Hard counters: logistics, fuel, strategic bombing, concentrated late anti-tank, encirclement, replacement scarcity.

## Economy balance

Malta should depend on a port network and external support. Balance review must prevent:

- free factory creation in every controlled port
- principality tribute exceeding the subject's economy
- Templar finance with no debt or influence cost
- conversion loops that create more equipment value than consumed
- repeated sponsor packages
- convoy grants that make naval warfare irrelevant
- terminal construction decisions usable before terminal activation

## Principality balance

Principalities should reduce occupation burden and provide local forces. They should also cost direct output and create obligations or succession risk.

A principality should not be strictly better than direct rule in every region. AI weights should consider resistance, supply, local cooperation, Authority, and route.

## Holy World balance

### Normal route

The full-continent requirement and 1000 Chaos gate already demand major success. Terminal bonuses can be extreme. The final war should still require logistics, regional campaigning, and coalition management.

### Manual scenario

Intensity packages must preserve nonbeliever viability. Balance metrics should compare:

- civilian factories
- military factories
- dockyards
- deployed divisions
- air power
- naval strength
- strategic resources
- controlled continents
- supply hubs and ports

Country count alone is not a valid balance measure.

## Exploit scenarios

Required tests:

- raise and disband special units for equipment profit
- create and annex principalities repeatedly
- transfer one state between subjects to satisfy continent proof
- farm order demands for values
- repeat relic expeditions
- accept and cancel sponsor aid
- rebuild Eleventh Crusade forces repeatedly
- duplicate initial Atlantis tanks
- use Holy World projects before activation
- launch manual scenario twice
- switch tags during release or settlement
- make a subject count without real Papal control
- trigger two terminal routes on one day

## Balance completion report

The final report should include:

- named probability scenarios and results
- opening force comparison
- value movement audit
- decision cost audit
- special-unit counter analysis
- principality direct-rule comparison
- economy and supply analysis
- terminal side balance at all four intensities
- exploit findings and fixes
- unresolved evidence classes
