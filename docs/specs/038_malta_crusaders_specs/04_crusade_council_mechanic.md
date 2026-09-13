# Crusade Council mechanic

## Purpose

The Crusade Council is the event's central management loop. It converts the abstract idea of a new crusade into a system of command, rival orders, religious recognition, territorial obligations, and visible tradeoffs.

The system uses exactly three persistent public values. It can use many internal ledgers, but those ledgers do not become extra numbers that the player must memorize.

## Public values

### Crusade Authority

**Range:** 0 to 100

**Meaning:** the central government's recognized ability to command armies, collect obligations, appoint governors, and make settlement decisions.

**Main gains:**

- securing Jerusalem
- holding Malta and the primary maritime bridge
- completing supply and command missions
- winning major regional wars
- integrating command structures
- receiving Papal recognition
- resolving order demands successfully
- creating stable principalities

**Main losses:**

- losing sacred centers
- supply collapse
- contradictory orders
- failed offensives
- principality defiance
- foreign sponsor humiliation
- order mutiny
- civilian atrocities that discredit central rule

**Threshold roles:**

| Band | Public state | Main consequence |
| --- | --- | --- |
| 0 to 19 | Fractured Command | emergency actions, strong order autonomy, possible command breakdown |
| 20 to 39 | Disputed Command | limited integration, frequent demands, weak subject control |
| 40 to 59 | Functional Command | normal campaign actions and principality management |
| 60 to 79 | Recognized Command | stronger administration, order arbitration, wider diplomatic access |
| 80 to 100 | Supreme Command | advanced formables, Papal supremacy preparation, terminal readiness support |

Authority should move in meaningful increments. One major mission or outcome should normally move it by 5 to 15 points before scaling and caps.

### Order Cohesion

**Range:** 0 to 100

**Meaning:** the ability of the military orders to cooperate without turning the crusade into a rivalry over land, money, command, relics, and prestige.

**Main gains:**

- shared command missions
- balanced territory grants
- joint victories
- transparent spoils settlement
- Papal arbitration
- mixed-order formations
- protecting wounded members and civilian hospitals
- honouring negotiated order charters

**Main losses:**

- repeatedly favouring one order without formal dominance
- denying promised land or wealth
- competing claims to Jerusalem
- casualties blamed on another order
- false relic scandals
- separate diplomacy with foreign sponsors
- succession disputes
- command autonomy during a crisis

**Threshold roles:**

| Band | Public state | Main consequence |
| --- | --- | --- |
| 0 to 19 | Open Rivalry | order incidents, command refusal, possible breakaway headquarters |
| 20 to 39 | Bitter Competition | higher costs, weaker mixed formations, frequent demands |
| 40 to 59 | Uneasy Council | ordinary coexistence and limited joint actions |
| 60 to 79 | Common Cause | stronger joint formations and lower demand pressure |
| 80 to 100 | United Orders | confederation capstones, elite mixed formations, stable succession |

A dominant-order route changes the meaning of low cohesion. Once formal dominance is established, the system measures obedience to the dominant order. The UI keeps the same public value and changes its label or tooltip context. It does not create a fourth value.

### Sacred Legitimacy

**Range:** 0 to 100

**Meaning:** religious recognition, public belief, Papal support, sacred-site control, and the prestige attached to relics and victories.

**Main gains:**

- control of Jerusalem and Rome under valid routes
- Papal recognition
- authentic or widely accepted relic claims
- pilgrim protection
- humane administration of sacred sites
- defending Christian communities
- major victories framed as providential
- support from Catholic governments

**Main losses:**

- loss or looting of sacred sites
- exposure of false relics
- conflict with the Pope
- attacks on Christian communities
- order corruption
- sacrilege scandals
- atrocities tied to religious policy
- failed prophecies or public claims

**Threshold roles:**

| Band | Public state | Main consequence |
| --- | --- | --- |
| 0 to 19 | Discredited Cause | weak foreign support, no blessed units, possible clerical opposition |
| 20 to 39 | Contested Cause | limited donations and uncertain relic effects |
| 40 to 59 | Recognized Cause | normal religious diplomacy and volunteer access |
| 60 to 79 | Sacred Mandate | blessed formations, Papal routes, stronger foreign movements |
| 80 to 100 | Universal Claim | Kingdom of God and Holy World preparation support |

Sacred Legitimacy is not proof of divine truth. It measures political and public belief.

## Hidden supporting ledgers

The system can track these private facts:

- strength and influence of each order
- unresolved demand count
- order headquarters by state
- principality loyalty and obligations
- foreign sponsor receipts
- local Christian cooperation
- Muslim and Orthodox resistance pressure
- Papal support state
- relic custody and controversy
- supply network quality
- holy site control duration
- recent major victory or defeat
- atrocity evidence and public condemnation
- governance method by state group

These facts feed the three values, events, AI, and tooltips. They should not appear as an exposed wall of numbers.

## Council presentation

### Preferred surface

The normal campaign should use a dedicated event-owned **Crusade Council** window because the player manages order seats, active demands, territorial grants, relic custody, and three linked values. A normal decision category alone would make the target and status relationships difficult to read.

The window must remain compact and usable. It should not become a ledger.

### Layout

The recommended layout contains:

- a top band with three meters and their next material thresholds
- a central order council with six order emblems and one dominant-order frame
- one active demand card
- one selected territorial or relic matter card
- no more than five primary action buttons in the current phase
- a small status strip for Jerusalem, Malta, Rome, and the maritime bridge
- concise tooltips that explain the current cause, next threshold, and available response

The decision category remains the owner of timed missions, map-targeted actions, and ordinary decision costs. The GUI calls accepted decision helpers and does not create a second gameplay implementation.

### States

The UI needs:

- normal
- hover
- selected
- available
- blocked
- warning
- demand active
- order dominant
- order marginalized
- relic disputed
- Jerusalem lost
- Papal route active
- terminal ready
- closed after defeat or annexation

Every visual state needs a static fallback. Animation is allowed only when it clarifies a live danger or active selection.

## Order system

### Order registry

The public order families are:

1. Hospitallers
2. Templar Revival
3. Teutonic Chapter
4. Order of Saint Lazarus
5. Naval Orders
6. Siege Brotherhoods

Each order record contains:

- current influence
- current headquarters state
- land grants
- treasury or equipment obligations
- commander roster
- unlocked unit variants
- current demand
- demand cooldown
- grievance memory
- foreign sponsor ties
- route compatibility
- dominance status

Influence remains hidden and is represented through council seat prominence, order status labels, demands, and route availability.

### Hospitallers

**Identity:** hospitals, casualty recovery, fortification, local care, medical logistics, and defensive endurance.

**Gameplay:** field hospitals, HP, recovery, attrition reduction, forts, disease response, contaminated-region operations, relief access.

**Demands:** hospital sites, protected budgets, authority over wounded troops, neutral medical access, control of key fortresses.

**Failure risk:** medical neutrality disputes, underfunded hospitals, refusal to serve harsh regimes, conflict with extermination routes.

### Templar Revival

**Identity:** offensive warfare, finance, debt, conquest, and centralized elite command.

**Gameplay:** breakthrough, attack planning, war finance, procurement, rapid war preparation, captured wealth.

**Demands:** treasury control, land concessions, banking privileges, operational independence, priority equipment.

**Failure risk:** debt dependency, corruption, rival claims, sponsor capture, aggressive overreach.

### Teutonic Chapter

**Identity:** discipline, heavy armour, eastern military tradition, and doctrinal rigidity.

**Gameplay:** Armored Knight quality, organization, training, heavy equipment, harsh winter preparation, high command.

**Demands:** command posts, heavy workshops, exclusive training grounds, ideological authority.

**Failure risk:** factional radicalization and hidden German route exposure. The public branch must remain viable without entering the hidden Teutonic Order faction.

### Order of Saint Lazarus

**Identity:** care for the diseased, service in contaminated regions, attrition warfare, and social stigma.

**Gameplay:** field hospitals, outbreak protection, attrition resistance, contaminated state operations, relief missions, casualty recovery.

**Demands:** hospitals, quarantine authority, access to vulnerable populations, separate chapters.

**Failure risk:** public fear, false disease accusations, conflict with biological warfare, exploitation of the sick.

### Naval Orders

**Identity:** islands, ports, convoy protection, marines, boarding, and amphibious war.

**Gameplay:** naval invasion planning, convoy defence, marine units, coastal forts, captured ports, light escorts.

**Demands:** island headquarters, dockyard priority, command of transports, naval autonomy.

**Failure risk:** convoy losses, piracy allegations, competition with Malta's civilian port authority.

### Siege Brotherhoods

**Identity:** engineers, catapults, trebuchets, fort assault, demolition, and battlefield construction.

**Gameplay:** siege formations, fort attack, engineer support, rail and depot work, bridging, demolition.

**Demands:** workshops, heavy transport, state construction rights, captured engineer corps.

**Failure risk:** extreme supply burden, civilian damage, obsolete doctrine, unsafe explosive experiments.

## Demand loop

Only one major order demand should normally be active at a time. A second emergency demand is allowed during terminal or civil conflict states.

A demand contains:

- requesting order
- concrete request
- deadline
- cost or commitment
- immediate effect
- long-term consequence
- refusal consequence
- compromise route
- AI choice weights

Examples include:

- grant an order headquarters in a named city
- transfer captured equipment
- fund hospitals or workshops
- appoint an order commander
- recognize an order's operational autonomy
- grant a principality charter
- transfer relic custody
- reserve Jerusalem administration for a chosen body

The player can normally accept, refuse, negotiate, or defer once. Repeated deferral raises grievance pressure and cannot become a free cooldown reset.

## Dominant-order settlement

One order can become politically dominant through focus and council choices. Dominance requires:

- a route focus
- a minimum Authority threshold
- the order's relevant campaign proof
- no unresolved council rupture
- a formal settlement event

Dominance provides stronger order-specific tools and weakens some rivals. It also creates route-specific risks. The player cannot gain every dominant-order capstone in one campaign.

The confederation route instead rewards high cohesion, balanced chapters, and shared command. It gains broader unit access but less extreme specialization.

## Relic system

### Purpose

Relics provide legitimacy, foreign interest, custody disputes, and uncertainty. The system never confirms supernatural authenticity.

### Candidate families

- fragments associated with the True Cross
- Holy Lance traditions
- saint relics
- crusader banners
- icons and manuscripts
- objects associated with Jerusalem
- Maltese and Rhodian order relics

Final names and historical claims require research. The implementation must distinguish a real historical tradition from a fictional object invented for the event.

### Relic record

Each relic has:

- custody actor and state
- public claim quality
- controversy state
- discovery source
- recognition state
- theft or loss state
- associated order
- public effect family
- hidden authenticity state or unresolved marker

The hidden authenticity state must never print as a raw true or false value.

### Relic outcomes

A relic can be:

- accepted
- disputed
- exposed as false
- stolen
- hidden
- transferred to the Pope
- held by an order
- displayed in Jerusalem
- destroyed or lost during war

Effects should change legitimacy, diplomacy, recruitment, resistance, order relations, and events. A relic should not give a permanent flat combat bonus without custody and public context.

## Sacred sites

The system tracks a small fixed set of sites:

- Malta and Fort St Angelo
- Jerusalem
- Rome after the Papal route
- selected order headquarters
- route-specific relic sites

Control duration matters. A single-day occupation does not count as stable sacred control.

## Miracles and blessed formations

At high legitimacy and Chaos, battlefield reports can describe improbable survival, unexplained morale, or disputed miracles. The mechanics remain grounded in organization, recovery, morale, command, and recruitment.

Blessed formations require:

- Evolution III or an approved terminal setup
- high Sacred Legitimacy
- equipment and manpower
- an order or Papal sponsor
- a bounded formation cap

They are elite units, not free immortal troops. Losses remain real.

## AI behavior

AI evaluates council actions from:

- current value bands
- active war state
- order strength and route
- equipment and supply
- imminent demand deadline
- control of Jerusalem and Malta
- Papal relations
- principality stability
- human allies and enemies
- hidden-route eligibility

AI should prioritize preventing collapse when Authority or Cohesion is below 20. It should pursue specialization only when the relevant order can be supplied. It should avoid relic claims when recent scandals make another exposure likely.

All demand timing, order selection, relic selection, and route choices require probability inspection and named scenarios.

## Cleanup

The mechanic closes or transforms when:

- Malta is annexed with no successor
- the country becomes the Holy See or Kingdom of God
- the Teutonic faction changes the council structure
- Atlantis destroys or occupies the Malta actor
- the Holy World terminal replaces ordinary management
- the event is cleanly defeated or dissolved

Transformation preserves durable order, relic, principality, and legitimacy facts needed by later routes. It removes stale buttons, invalid targets, expired demands, and temporary selected-card state.
