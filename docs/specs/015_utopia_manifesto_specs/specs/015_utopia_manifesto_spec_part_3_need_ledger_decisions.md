# Event 015 Utopia Manifesto, part 3 Need Ledger, decisions, missions, and integration

## Need Ledger presentation

The Need Ledger is the main mechanic. It can be shown through a decision category header at minimum. A scripted GUI board is strongly recommended because the player needs to read several values, state targets, and route warnings. The GUI should be readable and useful, not decorative.

The board should show:

| Panel | Content | Player use |
| --- | --- | --- |
| Stores | Common Stores value and shortage causes | decide whether to build storehouses, trade, or reduce expansion |
| Work | Vocational Freedom and public occasion pressure | decide whether to retrain, persuade, or override labor |
| Land | Land Need, valid target count, and claim decay warning | decide whether to seek leases, charters, or claims |
| Wards | occupied or chartered state list, integration progress, resistance | manage unusual occupation rules |
| Fracture | Outopia Fracture status without early spoilers | see when promises are breaking |
| League | common table members, cohesion, shared reserves | manage diplomatic route if unlocked |

Important values should use consistent colors in final localisation. Suggested identities are green for Eutopia, amber for Need, blue for Stores, purple for Vocational Freedom, red for Fracture, and yellow for League Cohesion.

## Dynamic value model

The spec does not lock exact numbers. The implementation should centralize thresholds and scaling values in script constants. Values should be dynamic and should read from country size, industry, stability, war support, manpower, stockpiles, wars, supply, rail access, ports, controlled states, occupied states, previous choices, and chaos tier.

### Common Stores

Common Stores represent the country's ability to meet practical needs. They should rise through public works, equipment commitments, civilian factory burdens, state repair, trade access, and stores-focused focuses. They should fall through war, bombing, overexpansion, occupation strain, convoy loss, emergency mobilization, and failed missions.

Common Stores should change:

- consumer goods burden or an equivalent country spirit
- decision availability for integration and relief
- Land Need pressure
- stability and public trust
- league or ward support
- AI willingness to expand

### Vocational Freedom

Vocational Freedom represents whether people can choose work according to inclination. It should rise through trade schools, adoption into trade families, public lectures, stable wages, and low forced assignment use. It should fall through emergency labor overrides, high mobilization, forced ward labor, and repeated command assignments.

Vocational Freedom should change:

- production efficiency and factory output
- strike or unrest risk
- manpower and training speed
- legitimacy in integrated wards
- route access between consent and coercion

### Land Need

Land Need is the gate that prevents arbitrary claims. It should rise when the country is crowded, lacks building slots, lacks ports, lacks agriculture proxies, has refugee pressure, loses access to key resources, has many integrated wards needing settlement, or has high Common Stores demand without land capacity. It should fall when stores are full, trade access is stable, states are developed, wards become autonomous, claims are renounced, or the country joins a league with shared stores.

Land Need should change:

- visibility of need dossiers
- temporary claims and demands
- diplomatic lease requests
- war goal preparation
- claim decay and renunciation rewards
- Eutopia and Fracture movement

### Outopia Fracture

Outopia Fracture measures contradiction. It should rise when the country uses coercive land claims, forces labor too often, occupies harshly, keeps claims after need disappears, hires auxiliaries excessively, suppresses audits, or chooses high-chaos paradox focuses. It should fall through public audits, claim renunciation, autonomous wards, voluntary integration, successful stores, and peaceful league admission.

Fracture should change:

- hidden route reveal
- domestic unrest
- foreign reactions
- occupation resistance
- super-event eligibility
- AI route safety

## Decision category families

The decision layer should not be a political power store. Decisions should ask the country to commit factories, equipment, trains, convoys, fuel, stability, war support, manpower, local support, state control, supply, units, or time.

### Reading and survey decisions

| Decision family | Availability | Costs and requirements | Effects direction | AI behavior |
| --- | --- | --- | --- | --- |
| Open public readings | after acceptance | stability threshold or small public order risk | raises legitimacy and early Eutopia, can increase factional debate | AI uses if stable |
| Send surveyors to state | Need Ledger unlocked | civilian factory burden, trains if distant, state controlled | identifies housing, stores, or land issues | AI prioritizes capital and high-value states |
| Publish the plain law sheet | legal branch | political stability and bureaucracy cost | reduces resistance and improves local support | AI uses when integrating wards |
| Audit the ledger | balanced or consent routes | time, stability, low war pressure | reduces Fracture and can remove unnecessary claims | AI uses if Fracture is high and not at war |

### Common Stores decisions

| Decision family | Availability | Costs and requirements | Effects direction | Failure or risk |
| --- | --- | --- | --- | --- |
| Build common storehouse | controlled state with infrastructure need | civilian factory burden, support equipment, local stability | raises Common Stores and local support | delays construction elsewhere |
| Convert tools to public stores | stockpile available | infantry or support equipment, maybe trucks | emergency Stores boost | weakens army readiness |
| Repair public halls | damaged or low stability states | construction capacity and manpower | stability and compliance | can fail under bombing or occupation |
| Open store convoy | port or ally access | convoys, fuel, route access | sends stores to ward or ally | convoy loss lowers Stores |
| Emergency ration register | low Stores, evolution or crisis | stability and war support cost | prevents panic and lowers Land Need temporarily | repeated use raises Fracture |

### Vocational Rolls decisions

| Decision family | Availability | Costs and requirements | Effects direction | Failure or risk |
| --- | --- | --- | --- | --- |
| Adopt a trade family | after trade focus | time, stability, local support | raises Vocational Freedom and production | slow in wartime |
| Public lecture cycle | education branch | command attention or civilian burden | research and legitimacy | small gain if repeated too often |
| Recruit workshop mentors | industry branch | support equipment, factories | improves production and stores | may reduce short-term output |
| Public occasion override | shortage, war, or Surveyor State route | stability, war support, legitimacy | moves labor to urgent category | raises Fracture if frequent |
| Refuse forced assignments | consent route | accepts production delay | raises Eutopia and freedom | can worsen shortages |

### Land Need and diplomacy decisions

| Decision family | Availability | Costs and requirements | Effects direction | Failure or risk |
| --- | --- | --- | --- | --- |
| Draft need dossier | Land Need above threshold | survey completed, neighbor valid, intelligence or relations | identifies target and possible request | bad dossier raises foreign suspicion |
| Request cultivation lease | dossier and target willing | relations, trade access, civilian support | temporary access, production or resource benefit | refusal can raise Land Need or Fracture |
| Invite local households | target state with local support | stores, convoys or rail access | peaceful charter settlement | failure causes backlash |
| Offer shared stores | Common Stores high | stores expenditure and convoys | improves target willingness, league path | can empty stores if overused |
| Demand boundary adjustment | high Land Need, route allows | dossier, target weaker or isolated | peaceful transfer, claim, or ultimatum | refusal can open crisis |
| Prepare needful war | coercive route or failed diplomacy | Land Need proof, military readiness, supply | limited war goal or border incident | high Fracture and foreign reaction |
| Renounce unneeded claim | claim exists, Land Need solved | no war with target | lowers Fracture, improves diplomacy | loses expansion option |

### Wardship and integration decisions

Wards are occupied, leased, chartered, or recently transferred states under Utopian administration. They should not all become instant cores.

| Decision family | Availability | Costs and requirements | Effects direction | Route variation |
| --- | --- | --- | --- | --- |
| Open ward survey | state occupied or chartered | control, supplied divisions or security, support equipment | starts integration track | all routes |
| Build ward storehouse | survey complete | civilian factory burden, support equipment, local support | compliance and Stores | stronger in consent route |
| Protect chosen trades | local compliance or local support | stability, time, no harsh occupation | compliance, lowers resistance | consent route |
| Assign public occasion labor | low stores or high need | manpower, command, Fracture | faster construction | Surveyor or Mandate route |
| Hold ward plebiscite | high compliance, low resistance | stability, no active war in state | core, autonomy, or league member | consent route |
| Confirm household adoption | high compliance and stores | stores, local support, infrastructure | gradual core progress | balanced route |
| Proclaim ward necessity | coercive route | state control, garrison, Fracture threshold | faster core or claim consolidation | Mandate route |
| Create autonomous charter | state stable but foreign identity strong | stores, diplomacy, low resistance | subject or autonomous member | consent and league route |

Integration should have partial success. A state might accept stores but reject direct coring, join the league but remain autonomous, or become a productive ward while raising Fracture because the process was forced.

## Timed missions

Timed missions should be active objectives, not passive checklists. Use varied durations. Easy missions should last roughly three months or more. Larger integration and war-preparation missions can last half a year or more.

| Mission family | Owner | Requirement direction | Success | Failure |
| --- | --- | --- | --- | --- |
| Guard the store belt | Utopian actor | keep supplied divisions in key storehouse states | Common Stores protected, local support rises | Stores fall, unrest and Fracture rise |
| Hold the public halls | Utopian actor | keep capital and key cities supplied and stable | legitimacy and Eutopia rise | pamphlet factionalism or empty shelf panic |
| Secure the ward rail | ward target | control rail path or build infrastructure | integration progress | resistance and delays |
| Protect the lease convoy | coastal or overseas target | maintain convoy and port access | charter support and stores | lease collapses or target suspicion |
| Prove need before war | coercive or failed diplomacy route | complete dossier, hold border, stockpile equipment | war goal becomes available | claim decays and Fracture rises |
| Recall the colonists | low need or failed ward | evacuate or release charter before deadline | Fracture falls and stores recover | population pressure and diplomacy worsen |
| Teach the second trade | vocational route | train workers through decisions or focuses | Vocational Freedom rises | output penalty and unrest |

## Scripted GUI and animated presentation direction

A scripted GUI board is recommended for the Need Ledger. It should have static fallbacks for all animated elements.

Suggested animated assets:

| Asset working label | Use | State logic | Frame direction | Static fallback |
| --- | --- | --- | --- | --- |
| need ledger seal animated | category header or GUI top | calm, shortage, crisis, mandate | book seal with changing page light and ledger marks | static closed book seal |
| common stores shelf animated | stores panel | full, strained, empty | shelf weight and lamp state drawn in separate frames | static shelf icon |
| land need compass animated | land panel | no need, need found, claim decaying | compass and shoreline marks drawn in separate frames | static compass icon |
| outopia fracture seal animated | hidden warning | low, rising, revealed | cracked geometric seal drawn in separate frames | static cracked seal |
| selected ward card glow | ward list | selected state, active mission, failure risk | subtle frame-by-frame border state | static selected border |

The animation package must follow the frame animation skill. It needs real source frames, sheets, previews, and static fallbacks. It must not be a filter pulse made from one still image.

## Occupation and integration rules

The manifesto should change how occupation feels. The country should have unusual integration tools, but those tools must be paid for.

### Consent-based wardship

Consent-based wardship uses stores, local trade choice, simple law, public halls, and plebiscites. It is slower. It gives better long-term cores, lower resistance, better diplomacy, and stronger Eutopia.

### Surveyor wardship

Surveyor wardship uses registries, work assignments, standardized houses, and managed integration. It is faster than consent if the state has stores and security. It can remain humane with audits. Without audits it drifts toward Fracture.

### Mandate wardship

Mandate wardship uses the Wasted Soil Thesis and the claim that subsistence need overrides local refusal. It is fast and powerful. It causes resistance, foreign hostility, Fracture, and possible coalition response. It should not be a free coring engine.

### Autonomous charters

Autonomous charters are a third option. The host does not core the land. It creates a subject, league member, demilitarized charter, or local partner. This lowers Fracture and can support the Eutopian League. It sacrifices direct factories and manpower.

## Claim decay and renunciation

Claims created by Need Dossiers should not behave like ordinary permanent claims. They are need mandates.

A need mandate should be removed, hidden, or politically punished when all of these are true:

- the country is not at war for the target
- Land Need has fallen below the claim threshold
- the claim has not been renewed by a valid dossier
- the target is not a core, charter, ward, or active settlement route

Renouncing an unneeded claim should be a positive action for consent and council routes. Keeping it after the ledger says need is solved should raise Fracture.

## Exploit controls

The decision system should prevent free construction, free units, free cores, and war goal spam.

Controls:

- only a limited number of active need dossiers at once
- target cooldowns after refusal or settlement
- active ward mission cap
- stores and equipment costs that scale with country size and target population
- claims that decay when need is solved
- cores only through integration projects or route-specific coercive cost
- AI target strength checks
- no repeated unit rewards without manpower, equipment, or mission requirements
- no demand against a major unless late route, high need, and strategic safety checks are met
- no claim against special chaos country using ordinary need logic unless the event explicitly treats it as a threat response

## Decision clutter control

The category should show only current actions. It should not list every possible target at once for the human player.

Use phases:

| Phase | Visible decisions |
| --- | --- |
| Reading | public readings, first surveys, common shelf |
| Counting | surveys, stores, trade adoption, public occasion |
| First Works | state projects, storehouses, education, guard missions |
| Need Doctrine | need dossiers, lease requests, charters, claim renunciation |
| Settlement | ward surveys, integration, plebiscites, autonomous charters |
| Commonwealth | faction, formable, shared reserves, late ambition |
| Outopia | hidden paradox actions, coercive ledger actions, crisis warnings |

For target-heavy decisions, use a selected-target pattern where the human chooses a target to inspect. AI can evaluate all valid targets through separate visibility or weighted logic.
