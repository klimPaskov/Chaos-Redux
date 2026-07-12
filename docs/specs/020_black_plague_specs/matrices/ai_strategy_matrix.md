# AI Strategy Matrix

## Human country response

| Actor state | Primary goals | Preferred actions | Avoids | Escalation trigger |
| --- | --- | --- | --- | --- |
| no nearby infection | raise preparedness efficiently | surveillance, reserve, prevention law | full border closure, expensive cordons | infection enters neighboring country or port route |
| borders infected state | block likely route, protect high-value states | targeted corridor closure, hospital staging, inspections | closing unrelated borders | source reaches Severe Crisis or military route opens |
| one domestic infected state | contain locally and protect transport network | quarantine plus relief, hospitals, treatment, cordon if needed | unsupplied quarantine, spreading reserves too thin | state becomes Severe Crisis or second state infected |
| several domestic states | prioritize population and hubs, seek help | emergency burden allocation, cure program, foreign aid | every harsh action in every state | capital or major hub threatened, burden cap exceeded |
| widespread collapse | preserve core country and research | triage, evacuation perimeter, army cordons, international mission | defending low-value unreachable states | Rat emergence pressure or government survival risk |
| Rat Nation neighbor | stop territorial and disease spread | armor, air, fortify line, clean liberated states | infantry-only attritional attacks | rat pulse or capital threatened |
| Rat King continental threat | survive and interrupt terminal path | share cure, defend capitals and ports, strike crown and nodes | rival wars, research hoarding | Evolution V or continent objective active |
| triggerable scenario opening | stabilize several simultaneous fronts | prioritize capitals, ports, supply hubs, city rat clearing, hospitals, and one response package per priority state | clicking every emergency action, ignoring rat fronts | launch bootstrap ends and live threat is visible |

## Political and strategic modifiers

| Condition | AI effect |
| --- | --- |
| democratic and stable | favors transparent reports, medical aid, knowledge sharing, lower coercive response |
| authoritarian and stable | favors cordons, movement restrictions, controlled information, mixed sharing |
| fascist or aggressive biowarfare route | higher weaponization and doomsday willingness, lower public sharing |
| communist with strong state capacity | favors centralized quarantine, mass hospital and production programs |
| low stability | delays expensive actions, higher coverup chance, higher failure risk |
| losing major war | prioritizes front supply, may underreact or use desperate weapon route |
| high industry | supports more simultaneous hospitals, reserves, and aid |
| low industry | selects one priority state, seeks foreign aid, avoids broad closures |
| island country after Evolution II | high port inspection and closure priority |
| large overseas empire | balances convoy supply against port infection, protects core ports first |
| full countermeasure | shifts from emergency suppression to cleanup, still monitors weapon threat |

## Countermeasure AI

| Situation | Action weight |
| --- | --- |
| owns infected state | very high begin program |
| ally infected and shares border or faction | high begin or aid |
| Rat Nation exists | very high global knowledge and adaptation |
| no sample access | seek ally sample, intelligence, or relief mission |
| active weapon project | cure program competes for facility and scientist capacity |
| high research and low threat | publish or alliance share |
| aggressive route and strategic advantage | hoard and possibly steal |
| Evolution I adaptation needed | prioritize adaptation before broad reopening |

## Weaponization AI

| Requirement or condition | Effect on project start |
| --- | --- |
| sample access | mandatory |
| biological warfare capability | mandatory |
| secure facility | mandatory unless desperate route allows reckless facility |
| domestic uncontrolled outbreak | strong negative |
| containment safety high | positive |
| enemy weak preparedness | positive |
| enemy already Rat-Controlled | block |
| high condemnation and fragile diplomacy | negative |
| near capitulation | strong positive for desperate routes |
| world_in_threat from Rat King | strong negative for most human AI |
| fascist or high-chaos offensive doctrine | positive |

## Project choice AI

| AI profile | Preferred branch | Iteration behavior |
| --- | --- | --- |
| cautious major | Safety-First | accepts delays, rotates staff, shares some cure data |
| aggressive prepared major | Dual-Use | pays high industry, protects secrecy |
| desperate authoritarian | Military Acceleration | skips safeguards, accepts leaks |
| cooperative medical state | Defensive Conversion | redirects project when cure need rises |
| collapsing state | acceleration or doomsday | prioritizes immediate deployability |

## Triggerable scenario actor initialization

- human AI starts with its country phase already calculated from seeded states and routes
- Rat Nation AI begins in survival and expansion mode and pauses dominance annexation during the royal-consolidation grace period
- Rat King AI begins in coronation and consolidation mode and cannot select Evolution V content without live eligibility
- existing actors are preserved and only missing scenario targets are created

## Rat Nation AI

| Archetype | Early priority | Mid priority | Late priority | Avoids |
| --- | --- | --- | --- | --- |
| Urban Warren | hold city and first node | nearby cities and rail hubs | proto-sentience through captured records | open plains against armor |
| Field Brood | spread through rural connection | encircle cities and food regions | wide territory and stable Brood Mass | costly city assault without support |
| Dock Brood | secure port | infest linked ports and islands | sea network and Rat King port score | inland overextension without corridor |
| War Brood | exploit frontline collapse | seize depots and pursue retreats | military dominance and rival absorption | static defense when breakthrough exists |

### Base rat focus choice

| Campaign condition | Preferred route |
| --- | --- |
| one strong capital and small territory | Dominant Beast and Nest Defense |
| wide fragmented territory | Distributed Instinct and Field movement |
| several research cities controlled | Emergent Cunning and Proto-Sentience |
| many weak human states | Mass Swarm and Flood the Front |
| fortified human front | Giant Mutation or Burrow Warfare |
| low long-term population | Preserve the Herd |
| immediate existential threat | Consume the State and rapid pulse |
| stronger adjacent rat rival | resist absorption, defensive node, avoid challenge |
| weaker adjacent rival | challenge and integrate |

## Rat King AI

| Phase | Goals | Focus and decision behavior | Failure response |
| --- | --- | --- | --- |
| consolidation | secure transfer, capital, cohesion | coronation lane, royal pulse, government selection | pause expansion, suppress disputed crown |
| government formation | choose route fitting empire | Crown for concentrated dominance, Council for dispersed empire, Hierophancy for high death route | switch support lanes, cannot change core government freely |
| regional domination | capture ports, capitals, nodes | administration, military caste, plague mastery | preserve corridor and rebuild Brood Cohesion |
| continental campaign | select best continent, meet control rule | target capitals and relief ports, maintain 90 percent threshold | retake lost strategic states before remote wars |
| world-end | complete focus path and protect sovereign | maximum priority on target continent and final objectives | strike human research leaders, restore Dominion, delay final focus if threshold lost |

## Rat King government selection

| World condition | Crown | Council | Hierophancy |
| --- | ---: | ---: | ---: |
| one brood overwhelmingly dominated | high | low | medium |
| territory on several disconnected regions | low | high | medium |
| high Sentience and preserved population | medium | high | low |
| enormous deaths and weak global cure | medium | low | high |
| capital exposed | low | high | medium |
| rapid continent conquest available | high | medium | high |
| controlled territory depopulated | medium | high | very low |

## AI validity and safety

- no action targets a dead country or invalid state
- no Rat Nation selects overseas behavior before Evolution II and a valid port
- no AI starts a mission it cannot materially attempt
- no Rat King selects a continent with no eligible states
- no world-end focus completes while live continent conditions fail
- no human AI spends the last essential front divisions on a cordon without comparing military threat
- no AI publishes or steals countermeasure progress repeatedly for reward farming
- no rat AI creates normal diplomatic relations with humans
- no normal human AI uses nonhuman recruitment or focus routes
- no scenario-created AI actor duplicates an existing tag, history row, evolution row, or army package
