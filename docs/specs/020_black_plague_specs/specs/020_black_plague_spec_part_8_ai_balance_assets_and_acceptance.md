# Event 20 Black Plague Specification, Part 8

## AI behavior, balance targets, achievements, assets, localisation direction, and completion standard

All names and labels in this file are working labels, not final localisation.

## AI design principle

Every AI country should understand three questions.

1. How close is the disease to my population and military routes?
2. What level of response can I sustain without losing a war or collapsing my economy?
3. Is my strategic goal prevention, containment, aid, exploitation, cure development, or weaponization?

The AI should select coherent response packages. It should not click every visible action, spend all equipment on one state, close every border permanently, or weaponize the plague simply because a project is available.

## Human-country AI response archetypes

Archetypes are dynamic strategic profiles, not permanent personality labels. A country can move between them as war, ideology, capacity, and infection change.

### Prepared administrator

**Typical conditions**:

- high stability
- strong civilian industry
- good medical capacity
- no immediate existential war
- democratic or cautious government

**Behavior**:

- invests early in surveillance and reserves
- uses targeted port and border controls
- shares countermeasure knowledge
- prioritizes hospitals and relief corridors
- avoids weaponization

### Militarized containment state

**Typical conditions**:

- high army strength
- active land threat
- authoritarian or military government
- strong command capacity

**Behavior**:

- uses cordons and troop-route restrictions
- protects fronts and supply hubs first
- accepts stability and resistance costs
- can neglect civilian relief if capacity is limited
- may weaponize when losing a war

### Denialist or underreacting state

**Typical conditions**:

- low preparedness
- severe political crisis
- economic weakness
- ideology or route that resists restrictions
- high emergency burden

**Behavior**:

- delays quarantine
- keeps borders and production open
- underfunds hospitals
- becomes a spread source
- changes behavior only after deaths or neighboring infection cross a high threshold

Denial should emerge from incentives and political condition, not a random suicide weight.

### Cooperative medical state

**Typical conditions**:

- strong research
- allies or faction network
- high global threat
- low offensive biowarfare interest

**Behavior**:

- develops and publishes countermeasures
- sends aid and scientists
- protects leading research centers
- supports global eradication

### Opportunist biowarfare state

**Typical conditions**:

- biological warfare capability
- aggressive route
- high chaos
- strategic enemy suffering from infection
- sufficient safety and intelligence capacity

**Behavior**:

- seeks samples
- starts a weaponization project
- hoards countermeasure knowledge
- uses covert delivery when attribution risk is acceptable
- still protects its own territory

### Desperate collapse state

**Typical conditions**:

- near capitulation
- severe domestic infection
- low stability and supply
- stockpile or project access

**Behavior**:

- accepts dangerous acceleration
- may use biological doomsday release when route and ideology allow
- prioritizes capital and army survival over long-term population

## State response scoring

AI state priorities use a weighted urgency score.

### Urgency increases from

- Severe Crisis or Collapsed status
- large population
- capital, major victory point, port, rail hub, supply hub, or major industry
- high outgoing spread pressure
- border with a clean core region
- frontline or strategic redeployment route
- rat emergence pressure
- current rat attack

### Urgency decreases from

- state already lost beyond realistic reach
- no supply access
- very low remaining population and low strategic value
- another state presenting a greater immediate threat
- emergency burden above safe capacity

The AI should sometimes abandon a nearly lost state to protect a larger clean region. That choice should be visible through event or decision consequences.

## Response package selection

### Low threat

- surveillance
- reserve production
- transport inspection
- prevention law when affordable

### Border threat

- targeted border corridor closure
- port inspections
- pre-position hospitals
- troop-route restriction only on exposed routes

### One infected state

- quarantine plus relief
- hospital construction
- treatment reserve
- cordon when spread pressure is high

### Several infected states

- prioritize population centers and transport hubs
- cap active cordons by capacity
- seek foreign aid
- develop countermeasure
- accept controlled economic damage

### Rat Nation threat

- protect capitals, ports, and supply corridors
- use armor, air, engineers, and fortified cordons
- liberate and quarantine retaken states
- coordinate through world-threat actions

### Rat King threat

- share countermeasure knowledge aggressively
- defend continental capitals and relief ports
- target royal burrow nodes and the Rat King capital
- delay rival wars when survival is at stake
- use emergency evacuation only when defeat is plausible

## AI cure policy

AI countries with active infection or high exposure should begin countermeasure work when they have sample access and capacity.

### Priority factors

- own infected population
- ally or faction infection
- neighboring infection
- research and medical capacity
- global countermeasure deficit
- Rat Nation existence
- enemy weaponization evidence

### Sharing behavior

- cooperative states publish or exchange
- authoritarian and opportunist states restrict sharing
- desperate states trade knowledge for aid
- a country facing the Rat King should usually share unless a route explicitly forbids it

## AI weaponization policy

The AI starts the project only when:

- valid sample access exists
- biological warfare capability exists
- facility and resources are available
- route permits offensive biowarfare
- accident risk is not already catastrophic or desperation overrides it
- a meaningful enemy target exists

### AI avoids weaponization when

- domestic infection is uncontrolled
- the country lacks containment safety
- allies would break relations or faction cohesion
- the target already has strong countermeasures and no strategic value
- world threat requires cooperation
- the country is likely to lose the facility

### Deployment scoring

High-priority targets:

- enemy capitals and industrial population centers
- major ports and supply hubs
- regions with weak preparedness
- enemy concentration zones

Blocking conditions:

- friendly or allied control
- high risk of immediate domestic return route
- target already Rat-Controlled
- insufficient stockpile or delivery capacity
- route or law prohibition

## Triggerable scenario AI opening

After a manual scenario launch, human AI immediately treats seeded domestic infections and bordering rat actors as active emergencies. It prioritizes capitals, ports, supply hubs, and population centers, then selects a limited response package that includes Black Plague-specific rat-clearing decisions when Rat Infestation is high.

Scenario-created Rat Nations begin in survival and expansion mode but do not run dominance annexation during the initial royal-consolidation grace period. The Rat King begins in coronation and consolidation mode, protects the Royal Basin, selects a government route from the live map state, and cannot enter the world-end lane before normal Evolution V eligibility.

## Rat Nation AI

Base Rat Nation AI behavior is defined in Part 5 and the AI matrix. It should behave aggressively without becoming random.

### Core rules

- expand toward infected and populous states
- preserve the emergence capital until growth stabilizes
- establish burrow nodes
- keep a connected plague corridor
- avoid long clean-territory thrusts without infection support
- challenge weaker adjacent broods through dominance
- choose focus routes matching origin and campaign state
- pursue proto-sentience only when secure

## Rat King AI

### Strategic phases

#### Consolidation

- integrate transferred territory
- restore Brood Cohesion
- choose government route
- secure capital and major corridors

#### Regional domination

- capture ports, capitals, and supply hubs
- develop military caste and plague mastery
- solve Hunger through planned conquest

#### Continental campaign

- select a viable continent
- hold land corridors and relief ports
- prevent human coalition stabilization
- pursue Evolution V conditions

#### World-end campaign

- complete required focus groups
- defend the sovereign and royal burrow network
- capture designated capitals
- maintain continent threshold
- trigger terminal scenario when all conditions are true

The AI should strongly pursue world end after completing the Evolution V route. It should not abandon a nearly complete continent to start a remote war without strategic reason.

## Balance goals

## Mortality

The event must produce very large losses under neglect while preserving meaningful counterplay.

- exceptional response can keep a state below 15 percent annual loss
- strong response can hold loss near 10 to 25 percent in a full year
- weak response can lose 25 to 50 percent
- collapsed or evolved states can lose 40 to 70 percent
- prolonged rat control can lose 60 to 85 percent or more

Mortality should be tuned through cumulative scenario tests, not one isolated tick value.

## Spread

- early outbreak should threaten nearby states without engulfing a continent in weeks
- an uncontained regional outbreak should create several new states per month by the middle phase
- Evolution I should be visibly faster without making decisions irrelevant
- Evolution II should create rare but consequential overseas jumps
- Rat occupation should be the most reliable spread source

## Containment cost

- one state quarantine should be affordable for most functional countries
- several severe quarantines should strain a minor country heavily
- a large major can manage several states but should feel the consumer goods, supply, and unit burden
- full border and port closure should be strategically painful during war and trade dependence

## Cure pace

- best-case full countermeasure: about six months
- normal strong country: six to twelve months
- weak or wartime country: one to two years
- no samples or cooperation: very slow
- Evolution I adaptation: a meaningful extra stage rather than total reset

## Weaponization pace

- safety-first project: eighteen to thirty months
- reckless compressed project: twelve to eighteen months with major risk
- repeated failure: more than thirty months or abort

## Rat emergence

- first Rat Nation should appear only after the player has experienced uncontrolled connected spread
- minimum starting force must survive a normal local response
- catastrophic basins can create a regional front immediately
- global tag and division caps protect performance

## Rat growth

- normal pulse around thirty days
- early pulse gives a small but meaningful batch
- strong late Rat King pulses can create large armies
- human players should have time to predict and disrupt a pulse
- no infinite unit explosion in depopulated states

## Rat King progression

- Evolution IV should require actual rat success
- Rat King consolidation should take time
- Evolution V should be a late campaign state
- world end should be difficult but reachable for a successful rat player or AI

## Anti-snowball counterplay

Rat Nations and the Rat King are intentionally stronger than ordinary infantry states. Counterplay should rely on preparation and combined tools.

Effective tools include:

- armor against soft swarms
- air power against concentrated broods
- engineers and fortified cordons
- clean supply corridors
- port control
- burrow clearance
- rapid quarantine after liberation
- countermeasure progress
- attacking royal nodes and the sovereign

Counterplay should not become one universal rat debuff button.

## Achievement design

Achievements are difficult route and mastery goals. All titles are working labels. A permanent Black Plague triggerable-scenario launch flag disqualifies these ordinary achievements unless the live achievement framework explicitly marks one as scenario-eligible. Launching an instant Evolution III and IV setup must not award natural-campaign mastery achievements.

### Achievement 1: The First Cordon

**Eligible**: any human country that owns the origin state.

**Goal**:

- contain and cure the origin state
- allow no second state to become Infected
- keep event-attributed deaths below a strict share of origin population

**Disqualifiers**:

- weaponization
- foreign state infection
- Rat Nation emergence

**Difficulty**: hard early response.

### Achievement 2: Forty Days

**Eligible**: any country bordering an infected foreign state.

**Goal**:

- maintain a targeted border quarantine for at least forty days
- remain at war during part of the period
- prevent infection from crossing that corridor
- keep supply to the active front above a minimum

**Difficulty**: medium to hard strategic tradeoff.

### Achievement 3: Open Roads, Closed Graves

**Eligible**: origin owner or first infected country.

**Goal**:

- eradicate the domestic outbreak without using full border closure or total civilian travel suspension
- use hospitals, surveillance, and targeted containment instead
- keep losses below a demanding threshold

**Difficulty**: hard medical route.

### Achievement 4: Physician Against the Night

**Eligible**: any human country with active infection.

**Goal**:

- reach full countermeasure progress before Evolution I records
- cure every domestic state
- publish the protocol

**Disqualifiers**:

- weaponization project begun

**Difficulty**: very hard research and containment.

### Achievement 5: The Common Remedy

**Eligible**: any human country.

**Goal**:

- provide countermeasure knowledge or medical aid to at least ten countries
- contribute to global eradication
- never deploy a biological weapon

**Difficulty**: hard cooperative campaign.

### Achievement 6: The Cabinet of Black Glass

**Eligible**: biowarfare-capable human country.

**Goal**:

- complete the weaponization project through the safety-first route
- hold a stockpile for a full year
- suffer no domestic accident
- never deploy it
- finish the global outbreak with full domestic countermeasure progress

**Difficulty**: hard dual-use restraint.

### Achievement 7: The Physician's Folly

**Eligible**: human country that deploys weaponized Black Plague.

**Goal**:

- suffer a traced domestic return outbreak from the same program
- contain and cure it
- remain the original government

**Difficulty**: very hard consequence recovery.

### Achievement 8: Burn the Warrens

**Eligible**: any human country.

**Goal**:

- personally destroy or lead the destruction of every Rat Nation before the Rat King appears
- clear every burrow node in liberated territory
- complete global plague eradication

**Difficulty**: very hard military and medical campaign.

### Achievement 9: No Census Required

**Eligible**: base Rat Nation.

**Goal**:

- field one hundred rat divisions through brood pulses
- control at least thirty plague states
- never use ordinary manpower or equipment

**Difficulty**: hard rat growth campaign.

### Achievement 10: One Crown, Many Tails

**Eligible**: base Rat Nation.

**Goal**:

- absorb at least five rival Rat Nations
- win Evolution IV candidacy
- become the Rat King

**Difficulty**: very hard dominance campaign.

### Achievement 11: The Rat That Read

**Eligible**: Rat King.

**Goal**:

- complete the Council government route
- reach maximum Sentience
- capture a defined set of research capitals
- preserve a minimum human population in controlled states

**Difficulty**: hard alternative rat government.

### Achievement 12: Crown of One Continent

**Eligible**: Rat King.

**Goal**:

- control a full continent under the world-end definition
- record Evolution V
- do not trigger world end yet

**Difficulty**: very hard conquest and restraint.

### Achievement 13: The Pale Sovereign

**Eligible**: Rat King.

**Goal**:

- complete the world-end path
- trigger the Rat King terminal scenario

**Difficulty**: terminal challenge.

### Achievement 14: Doctor Wu's Last House Call

**Eligible**: human country that receives the Event 163 connection.

**Goal**:

- use Doctor Wu's accelerated protocol after Evolution II
- cure infections on at least two continents
- prevent any Rat King from appearing

**Difficulty**: rare cross-event mastery.

The achievement matrix gives exact tracking directions and icon concepts.

## Asset package overview

The full asset inventory is in the asset matrix and prompt. The core package includes:

### Disease presentation

- Black Plague disease icon
- decision category icon or selected disease icon
- state status icons for Threatened, Infected, Severe Crisis, Collapsed, Contained, Recovery, Cured, weaponized, and Rat-Controlled
- mapmode legend assets
- disease board panel elements
- countermeasure progress states
- animated crisis seal with static fallback
- black fog prototype package

### Event images

- first outbreak report image
- first Severe Crisis report image
- first overseas jump news image
- first Rat Nation emergence report image
- Rat King coronation super-event image
- world-end super-event image
- optional global defeat aftermath image when eligible

### Rat Nations

- collective leader portraits for four origin archetypes
- optional proto-sentience variants
- unique flag sets for every tag in the final pool
- base focus icon families
- unit, brood pulse, dominance, burrow, and anti-rat decision icons

### Rat King

- static and animated leader portrait
- government route portrait variants if needed
- base and route flag sets
- Dominion, Sentience, Brood Cohesion, and Hunger UI icons
- Rat King seal animation
- deep focus icon families
- royal unit and world-end decision icons

### Achievements

- fourteen completed 64 by 64 icons
- grey variants
- not-eligible variants using the approved overlay workflow

## Animation decisions

### Animation is recommended for

- disease crisis seal at Severe Crisis and Collapsed state
- black fog state effect if engine feasible
- Rat King leader portrait
- Rat King world-end readiness seal

### Static presentation is better for

- ordinary decision icons
- most focus icons
- state status icons
- report and news images
- base collective Rat Nation portraits

This keeps motion meaningful and avoids an unreadable interface.

## Localisation direction

Planning files do not provide final pasteable localisation. Implementation should write finished text from these directions.

### Event title direction

Use a direct disease identity with period gravity. Avoid update-history wording and avoid implying that the disease is the ordinary existing plague entry.

### Opening description direction

- viewpoint from local population and overwhelmed authorities
- dynamic origin state and owner
- clustered illness, household deaths, crowded wards, stopped work, and fearful movement
- incomplete cause during early recognition
- no numeric effect list

### Event option direction

- early option can be grim administrative resolve or frightened understatement
- severe crisis option should avoid cheap humor
- weaponization choices can use cold military euphemism that condemns the speaker through context
- Rat Nation reveal should show fear and disbelief without calling itself a warning
- Rat King reaction can use a short researched cultural remark

### Decision text direction

- name the actual public action
- describe visible cost and consequence
- use icon-first costs
- explain targeted states and corridors
- show dynamic requirements through scripted localisation
- do not reveal hidden relapse rolls or evolution thresholds

### Focus text direction

Rat focus text should describe instinct, burrows, movement, hierarchy, and captured behavior. Rat King focus text should become more organized and political as Sentience grows. Government routes need distinct tone.

### Event Details direction

Describe premise, progression, and visible systems. Do not list modifiers, death formulas, exact thresholds, secret achievements, or hidden world-end conditions.

### Super-event text boundary

Final titles, button remarks, quotes, and cultural references remain blocked until the super-event text research output verifies them. Two public-domain quote candidates are documented, but implementation still chooses and wires final text.

## Documentation alignment

The final implementation must keep the following synchronized.

- event script and state lifecycle
- disease registry
- crisis board and mapmode
- containment decisions and AI
- countermeasure progress
- special project and delivery systems
- Rat Nation and Rat King packages
- focus trees and country identities
- super-events and audio
- event log and evolution entries
- event and system documentation
- asset manifests and GFX handoffs
- catalog workbook

## Completion standard

Event 20 is complete only when every requested surface is implemented or explicitly blocked with evidence.

### Core disease

- one weighted mainland origin state
- no continent-wide temporary idea
- nonlinear real population deaths
- state-by-state spread
- preparation, threat, infection, containment, recovery, and cure states
- dynamic mapmode refresh
- established Black Plague states use a black base colour in the existing disease mapmode
- black fog feasibility result

### Shared response

- no duplicate disease category
- Black Plague-specific decisions appear as separate entries inside the general disease category
- city rat clearing, granary and warehouse sealing, sewer and burrow clearance, shelter treatment, transport-hub vermin control, and harsh district demolition are implemented
- dynamic crisis board
- state-targeted actions with real costs
- underreaction and overreaction both viable
- AI equivalents
- cleanup and relapse

### Cure and biowarfare

- separate Black Plague identity
- visible country countermeasure progress
- no instant cure
- long iterative weaponization special project
- stockpile accidents
- existing delivery system integration
- condemnation and retaliation

### Evolutions

- five logged evolutions
- active and pre-fire entry behavior
- dynamic pacing
- Evolution I stronger strain
- Evolution II overseas spread
- Evolution III Rat Nations
- Evolution IV separate Rat King country
- Evolution V world-end path

### Rat Nations

- complete tag pool
- strong dynamic starting armies
- no manpower or equipment
- no manual deployment
- timed growth pulses
- plague immunity
- occupation infection
- mutual non-hostility and dominance absorption
- shared but varied focus tree
- leader portraits, flags, AI, and cleanup

### Rat King

- separate country and deep tree
- sentient leader and government
- government routes
- advanced army pulse
- world-end readiness and continental campaign
- complete identity assets

### Triggerable scenario

- registered in the existing Triggerable Scenarios window
- Low, Medium, High, and Maximum intensity support
- many established plague states across several continents
- immediate Evolutions I through IV
- several independent Rat Nations and one separate Rat King
- Rat Nations and the Rat King coexist after bootstrap
- event, evolution, death, tag, and mapmode data remain idempotent
- Chaos floor creates instant crisis without setting world end
- ordinary achievements are protected from scenario shortcuts

### World end

- chaos greater than 1000
- enough states and deaths
- completed world-end path
- continent control
- terminal super-event
- complete world takeover sequence
- incompatible systems stopped

### Quality and proof

- focus, decision, country, localisation, and completion audits
- meaningful balance scenarios
- no undisclosed simplifications or fallback content
- final docs and spreadsheet alignment
- all assets final or honestly blocked
- all accepted plans promoted into the source spec or dispositioned
