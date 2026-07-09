# 020 Black Plague spec Part 9 - Rat warfare, units, and counterplay

This part defines mutated rat unit families, automatic growth, military AI, human counterplay, border cordons, cleanup operations, and defeat logic. It expands the unit and combat direction from Part 5 to Part 8.

All unit family names, doctrine labels, operation labels, and icons are working labels only. They are not final localisation.

## Rat warfare purpose

Rat countries should fight in a way that feels unnatural without becoming impossible to counter. They should be stronger than normal infantry when the outbreak is neglected, especially in infected, urban, ruined, and high-death states. They should have clear weaknesses against prepared containment, air control, organized cordons, supply isolation, medical cleanup, and coordinated offensives.

The player should never train mutated rat units manually through a normal division training queue. Rat units grow from the rat tick, focus unlocks, absorbed warrens, and plague-state pressure.

## Nonhuman unit economy

Rat nations and the King should ignore human manpower and ordinary equipment for mutated rat units. They can still interact with captured industry through special growth values, warren modifiers, and scavenging abstractions.

Core rules:

- mutated rat units do not consume manpower
- mutated rat units do not require infantry equipment as a normal production input
- rat unit growth is automatic and scripted through ticks, focuses, and state pressure
- rat countries should be excluded from human manpower and equipment systems where needed through shared nonhuman triggers
- rat countries can receive special scripted stock values such as brood pressure, warren capacity, scavenged stores, or corpse pressure if the implementation needs internal values
- rat countries should not receive ordinary lend lease, normal volunteer recruitment, or normal subject templates unless a future accepted addendum deliberately changes that

## Mutated rat template families

The implementation can represent these as special units, hidden templates, or scripted-spawn division templates depending on what the engine supports. The gameplay identity should preserve the families below.

| Unit family | Battlefield role | Unlock source | Strengths | Weaknesses | Human counter |
| --- | --- | --- | --- | --- | --- |
| Warren swarm | baseline rat formation | base rat opening | stronger than basic infantry, high recovery, strong in infected states | weak anti-tank, weak air defense, supply-sensitive outside plague states | cordons, air support, prepared infantry, cleanup |
| Sewer rush | fast assault and urban breach | human war route | speed and breakthrough in urban, infrastructure, and port states | worse in mountains, deserts, and clean rural states | fortify clean lines, destroy infrastructure, guard ports |
| Plague gnawers | attrition and disease pressure | plague ecology route | worsens disease load, strong attack in severe states | lower organization outside infected zones | medical response, quarantine, anti-rat operations |
| Burrow guard | nest defense | warren defense route | strong defense, high attrition against attackers, hidden reserves | slow, poor offensive value | siege cleanup, engineers, supply isolation |
| Brood mass | late mass unit | swarm growth capstone or King route | large attack and staying power | heavy supply strain, vulnerable to air and isolation | air control, encirclement, deep cordons |
| King guard | elite sovereign unit | King Royal route or high King command | elite shock and defense near King core | limited number, route dependence | target King capital, elite anti-rat operations |
| Hunger tide | reckless late swarm | Hunger Mind route | huge growth and offensive pressure | overextension, supply damage, high world response | deny targets, cut roads, let overextension bite |
| Council wardens | stable defensive unit | Brood Council route | durable defense and relapse suppression | slow conquest | concentrated offensive and cleanup after breakthrough |

## Unit progression by evolution

| Event phase | Rat unit availability |
| --- | --- |
| Before Evolution III | no rat units |
| Evolution III first rat nation | warren swarm, limited burrow guard, possible sewer rush if urban state |
| Base rat focus progress | plague gnawers, stronger burrow guard, brood mass through late route |
| Rat absorption | inherited units and stronger tick bands |
| Evolution IV King | organized warren swarm, King guard if route supports it, stronger brood mass |
| King government route | route-specific elite or mass variants |
| Evolution V world-end path | Hunger tide or continental swarm variants if path reaches terminal stage |

The first rat nation should not start with every unit family. Unit families should arrive through route progress so humans can learn and respond.

## Template quality bands

Rat units should scale in quality through route progress and disease pressure. Avoid a single flat template for all campaign states.

| Quality band | Typical source | Use |
| --- | --- | --- |
| feral | small first warren, low focus progress | dangerous against militia, beatable by prepared armies |
| organized | base rat route progress | stronger and more reliable, able to threaten minors |
| black warren | high disease load or absorbed nest | major local threat, heavy attrition pressure |
| crowned | King of Rats established | national-scale nonhuman army |
| continental | King controls large region and late focus path | global threat army |
| terminal | world-end path near completion | deliberately absurd and campaign-ending if not stopped |

Quality should come from scripted modifiers, template selection, unit count, or hidden unit traits based on what is safest to implement.

## Terrain and state interaction

Rat armies should care about state status and terrain.

Preferred rat terrain:

- urban states
- forests and marshes where containment is hard
- ruined states with low infrastructure but high disease load
- port states after Evolution II if port warrens are unlocked
- high-population states with severe infection
- states with rail, supply depots, or abandoned industrial districts

Harder rat terrain:

- clean open plains with strong cordons
- mountains with prepared defenders
- deserts and low-population regions
- islands without port access before Evolution II
- strongly supplied fortified lines

State interactions:

| State condition | Rat benefit | Human answer |
| --- | --- | --- |
| infected | higher combat efficiency and growth | quarantine, medical response, cleanup |
| severe | stronger plague gnawers and death pressure | emergency hospitals, retreat or cordon |
| collapse | best growth fuel, rat emergence risk | urgent containment or evacuation |
| contained | lowers rat spread benefits | maintain cordon and treat |
| clean and fortified | weakens rat offensive edge | defend here and counterattack |
| warren-remnant | relapse and hidden reserve risk | burn out warren remnants |
| rat-held port | overseas risk after Evolution II | naval quarantine and port assault |

## Automatic rat reinforcement tick

The tick is the core rat recruitment system. It should happen through a regular event-owned pulse or a shared safe pulse if the implementation environment allows it. It should not require human player clicks.

Tick owner:

- base rat tags use base rat tick
- King tag uses King tick
- absorbed rat tags lose their tick after absorption
- defeated tags lose their tick after final cleanup

Tick inputs:

| Input | Effect direction |
| --- | --- |
| rat-held plague states | main growth source |
| disease load in those states | raises growth and quality |
| remaining population and cumulative deaths | raises growth, but heavy evacuation lowers potential |
| warren pressure | raises local spawn chance |
| focus progress | unlocks unit families and modifiers |
| government route | changes growth shape for King |
| containment pressure | reduces growth |
| supply isolation | reduces or delays growth |
| active human cleanup nearby | reduces relapse and reserve spawn |
| chaos tier | raises cap and severe outcomes |
| world-end path progress | raises terminal growth only after earned |

Tick outputs:

- add new mutated rat divisions in valid rat-held states
- reinforce existing divisions through strength or organization if direct reinforcement is safer
- add temporary local combat bonuses in overloaded cases instead of spawning too many units
- increase warren pressure if growth is blocked but states remain infected
- create reserve defenders in core nests under attack when defensive route allows it

## Tick pacing bands

Tick pacing should feel dangerous but not instantly unwinnable in first emergence.

| Band | Trigger direction | Pacing direction |
| --- | --- | --- |
| dormant | no rat country or no valid rat-held plague states | no tick |
| fresh warren | first emergence and few states | slow tick, enough to survive |
| growing warren | several infected states | steady tick and occasional unit family upgrade |
| black warren | high deaths and plague load | fast tick, strong local army pressure |
| crowned swarm | King exists | organized tick, better unit selection |
| continental swarm | King holds large region | high tick with global threat response |
| terminal hunger | world-end path late stage | extreme tick, intentionally overpowered if not stopped |

The implementation should use caps and consolidation effects to avoid uncontrolled division count performance problems. If unit count is too high, represent pressure through state modifiers, temporary combat buffs, and fewer stronger units.

## Rat AI strategic logic

Rat AI should be aggressive, but it should not throw the swarm into impossible attacks before the system has built pressure.

Base rat AI priorities:

1. secure core warren state
2. complete opening trunk
3. grow enough units to survive local counterattack
4. attack weak infected neighbors
5. target high-population states when path and supply allow
6. absorb weaker nearby rat nations
7. fortify if surrounded by stronger humans
8. prepare King eligibility if dominant

King AI priorities:

1. consolidate inherited states
2. choose a government route based on state base and threat
3. absorb remaining rat pockets
4. build swarm command and warren economy
5. target connected continent-control states
6. counter human cordons
7. pursue world-end path only after thresholds are plausible
8. protect capital nest or council core depending on government route

AI target scoring factors:

| Factor | Raises target value | Lowers target value |
| --- | --- | --- |
| infected or severe state | easier spread and combat | clean state with strong defenses |
| high population | growth fuel and death pressure | evacuated state |
| port after Evolution II | overseas route | no naval or port logic yet |
| weak owner | easier conquest | major power with strong army |
| low infrastructure but infected | rats can thrive if plague route | clean low-infra areas slow rat movement |
| adjacent rat border | easy access | isolated island without port access |
| capital or victory point | strategic pressure | too heavily defended |
| nearby human cordon | attack if weak | avoid if strong and supplied |

## Human counterplay principle

Humans should be able to beat rat countries through preparation, timing, and coordinated operations. Ordinary warfare should help, but the event should reward disease-specific and anti-rat actions.

Counterplay pillars:

- prevent the first rat emergence by containing collapse states
- starve rat growth through evacuation, cure progress, and cleanup
- hold cordons in clean or contained states
- retake warren states with prepared offensives
- run post-retake cleanup missions
- block ports after Evolution II
- coordinate internationally when rats become regional or global threats
- target the King before the world-end path finishes

## Anti-rat military operations

### Cordon line

Role:

- stop rat spread across a border or infected state ring

Requirements:

- divisions assigned to key states or state-control abstraction
- supply access
- support equipment and infantry equipment
- command power or army XP for coordination

Effects:

- lowers rat attack success and border spread
- lowers disease spread from rat-held states
- raises attrition cost for both sides if overused

Failure:

- threatened state becomes exposed or infected
- rat AI gains breach confidence
- local panic rises

### Clean corridor offensive

Role:

- create a clean path into rat-held territory by combining military advance and disease cleanup

Requirements:

- controlled staging states
- active medical support
- divisions with supply
- trucks or trains to maintain route

Effects:

- lowers post-advance relapse risk
- improves chance of keeping retaken state
- slows rat reinforcements in adjacent states

Failure:

- attacking army suffers attrition and supply damage
- warren remnants persist

### Nest assault

Role:

- attack a core warren state or King capital nest

Requirements:

- military control of adjacent states
- high containment strength or anti-rat preparation
- equipment and support equipment
- possibly air superiority or artillery abstraction if implementation supports it

Effects:

- major progress toward rat defeat
- can trigger Broken Warren or Broken Crown state
- high risk of casualties and disease exposure

Failure:

- rat defensive reserves spawn if route allows
- disease load rises in attacker staging states
- local morale or war support hit

### Port seal

Role:

- prevent rat sea spread after Evolution II

Requirements:

- control or contest of port state or sea route
- convoys, fuel, naval or air patrol abstraction
- port inspection decision active

Effects:

- lowers overseas rat spread and port vermin path
- weakens rat-held port as spread source

Failure:

- exposed port states appear overseas
- trade and convoy losses rise

### Burnout operation

Role:

- remove warren remnants after retaking a state

Requirements:

- state controlled by human country
- no active rat divisions in state
- support equipment, infantry equipment, trucks, medical capacity
- time and local security

Effects:

- removes warren-remnant status
- lowers relapse pressure
- allows recovery decisions to finish

Downside:

- heavy-handed operations damage state recovery and can raise resistance
- delaying operation keeps relapse risk active

## Medical and civilian counterplay

Military operations alone should not solve the crisis.

### Evacuation

Purpose:

- reduce deaths and lower rat growth fuel

Use cases:

- threatened high-population states
- rat border states likely to be attacked
- port states at overseas risk after Evolution II

Tradeoffs:

- economic output loss
- supply burden in receiving states
- disease risk if evacuation is badly managed
- possible stability cost

### Field hospitals

Purpose:

- reduce death ticks and keep armies functional in infected regions

Use cases:

- infected front states
- clean corridor offensives
- retaken warren states

Tradeoffs:

- support equipment and trucks
- limited medical capacity

### Recovery administration

Purpose:

- restore state after cure or warren cleanup

Use cases:

- recovering states
- retaken rat states
- post-King defeat regions

Tradeoffs:

- slow and costly
- can be interrupted by relapse or new fighting

## Research and doctrine counterplay

The event should let human countries improve anti-rat and anti-plague performance over time.

Research or project directions:

| Direction | Effect |
| --- | --- |
| plague countermeasures | lower death and spread, enable stronger cleanup |
| military containment doctrine | stronger cordons and anti-rat operations |
| field hospital expansion | lower army and civilian losses in infected fronts |
| port quarantine methods | lower overseas spread after Evolution II |
| warren cleanup methods | reduce relapse and warren-remnant duration |
| safe sample handling | lower accident risk when studying Black Death |

These should be abstract gameplay projects, not real-world lab instructions.

## Interaction with existing biowarfare systems

Rat-held states should become dangerous sample sources. Countries may study them through the biowarfare system, but this should be high-risk.

Rules:

- rat-held plague is a valid sample source only through safe abstract project hooks
- weaponization and cure research share some sample access logic but create different consequences
- accidents can seed outbreaks at home
- studying rat plague should raise safety burden and world attention
- successful defensive study helps anti-rat cleanup and cure progress

## Human AI counterplay

Human AI must not ignore rats. The rat crisis should change AI behavior.

AI response tiers:

| Tier | Trigger | AI behavior |
| --- | --- | --- |
| local alarm | rat country borders AI or near ally | cordon, local quarantine, border defense |
| regional threat | rats control several states | prioritize anti-rat fronts and aid neighbors |
| King threat | King exists | coalition logic, major military priority, cure sharing |
| continental threat | rats approach continent control | high priority war behavior and emergency measures |
| terminal threat | King world-end path near completion | maximum available response, risky cooperation with rivals |

Human AI should consider:

- distance to rat states
- strength ratio
- state population at risk
- ports at risk
- stability and war state
- faction obligations
- cure progress
- available equipment and support equipment
- recent failures against rats

Human AI should avoid:

- spending all resources on distant rat wars while homeland collapses
- attacking fortified warren cores without preparation if alternatives exist
- ignoring cleanup after retaking states
- using weaponized Black Death in a way that guarantees self-infection unless desperate or extreme

## Rat-to-rat absorption detail

Rat-to-rat absorption should reduce tag clutter and create King momentum.

Absorption conditions:

- rat countries are adjacent, connected through rat-held states, or linked by port route after Evolution II
- one rat country is clearly stronger by state count, unit strength, disease load, or focus progress
- weaker rat country is not protected by a temporary route state
- stronger country is not near collapse unless Hunger Mind or similar route supports reckless absorption

Absorption effects:

- transfer states to stronger rat country or King
- transfer units where possible
- add growth pressure or unit tick strength
- mark weaker tag closed and clear its decisions
- transfer relevant plague and warren state status
- record evolution or history entry if the absorption is significant

Human counterplay:

- attack while rats are merging
- isolate rat pockets to prevent adjacency
- retake connecting states
- clean warren remnants before absorption path finishes

## King-specific counterplay

The King is harder to defeat than base rat nations. Counterplay should depend on the chosen government route.

| King route | Human target | Counterplay direction |
| --- | --- | --- |
| Royal command | capital nest and leader command network | targeted nest assault, cut command tunnels, force Broken Crown |
| Brood council | multiple council warrens | isolate and clear several warren centers, prevent recovery |
| Hunger mind | overextension and supply collapse | deny new targets, evacuate population, cut roads, let hunger route strain itself |

Generic King counterplay:

- keep continent-control requirement broken
- interrupt world-end focus conditions
- retake ports after Evolution II
- burn out warren remnants in recovered states
- share cure and anti-rat research
- prevent rat unity from recovering after defeats

## Defeat aftermath design

A large rat war should leave scars. Aftermath depends on scale.

| Scale | Aftermath |
| --- | --- |
| small base warren defeated | local recovery decisions, disease monitoring, event-log entry |
| major warren defeated | regional cleanup missions, possible news report, achievement checks |
| King defeated early | Broken Crown cleanup, severe but recoverable regional aftermath |
| King defeated after major conquest | defeat super-event candidate, postwar reconstruction and vigilance decisions |
| terminal path interrupted | major relief and recovery package, possible high-tier achievement |

Aftermath should not pretend normality returns immediately. Retaken states can have population loss, damaged infrastructure, disease residue, and warren-remnant cleanup needs.

## Balance and performance considerations

Rat systems can become large. The design should stay deep without creating performance problems.

Guidelines:

- cap unit spawns or convert excess pressure into stronger units and state modifiers
- clear dead rat tags and duplicate ticks after absorption
- avoid daily all-country scans unless the implementation has explicit approval and a narrow method
- use event-owned state lists or status flags where possible
- prioritize state target pools instead of creating visible decisions for every state
- let AI use hidden broad checks while human UI stays curated
- keep route effects meaningful and strong, but not infinite unless terminal path has been earned

## Asset needs for rat warfare

| Asset | Type | Source mode | Use |
| --- | --- | --- | --- |
| mutated rat unit icon family | unit or interface icons | generated | warren swarm, sewer rush, plague gnawers, burrow guard, King guard |
| anti-rat operation decision icons | decision icons | generated | cordon, nest assault, cleanup, port seal |
| rat warfare focus icon pack | focus icons | generated | military lanes in base rat and King trees |
| warren-remnant state marker | UI or mapmode sprite | generated | retaken rat states that need cleanup |
| King government route emblems | focus or UI icons | generated | Royal, Council, Hunger routes |
| rat threat animated warning | scripted GUI sprite | generated frames | disease board rat threat state |

All generated icons should inspect the relevant reference folders and follow target sizes from the asset skill.

## Localisation direction for warfare and counterplay

Final player-facing text should show consequences through concrete in-world action. It should not use jokes for mass death. Human decision text should make costs and requirements clear without revealing hidden rat route logic. Rat-player focus and decision text can describe warren behavior after the player controls a rat country.

Direction by surface:

| Surface | Direction |
| --- | --- |
| rat unit text | nonhuman military identity, simple and readable |
| anti-rat decisions | practical military and medical operations with clear costs |
| cleanup missions | retaken states remain unsafe until work is finished |
| King counterplay | focus on disrupting the route's visible state, not hidden variables |
| defeat aftermath | recovery, missing population, ruined districts, and vigilance |

No final localisation is provided in this planning file.
