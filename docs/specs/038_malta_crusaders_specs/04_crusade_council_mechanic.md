# Crusade Council mechanic

## Purpose

The Crusade Council is the event's single management loop.
It turns the abstract idea of a new crusade into three questions the player can answer: whether the expedition holds together, whether the military orders cooperate, and whether the cause is believed.
Everything else the campaign tracks stays internal and surfaces only as an event, a tooltip sentence, or an unlocked or locked action.

## What the player sees

| Readout | Form | Answers |
| --- | --- | --- |
| Command Standing | five named steps, no number | Does the expedition hold its four anchors? |
| Order Cohesion | whole number 0 to 100 | Will the orders obey, bargain, or break? |
| Sacred Legitimacy | whole number 0 to 100 | Do the Church, donors, volunteers, and pilgrims believe? |

Two numeric meters and one standing line are the whole public budget.
No other persistent Event 38 value is shown.
Supply uses the normal supply interface.
Resistance, relic standing, principality loyalty, Papal relations, and order grievance are internal and reach the player only through events, the demand card, and one-line tooltip causes.

Each readout shows its current band and the one thing that would move it to the next band.
A meter never shows a list of contributing numbers.

## Command Standing

Command Standing replaces a 0 to 100 authority meter.
Authority would only restate things the player can already see on the map, so the standing is computed from them.

### The four anchors

- Malta, held with a usable Grand Harbour.
- Jerusalem, held for at least 30 days.
- The sea road, meaning at least one bridge port connects Malta by sea to a Holy Land port without a proven blockade.
- The primary supply port, meaning the best port of the Holy Land command, reselected by the owner trigger if it is lost.

### Steps

| Step | Condition | Consequence |
| --- | --- | --- |
| Fractured | fewer than two anchors held, or an unresolved order rupture | only emergency and survival actions are offered, no new charters, the Eleventh Crusade check starts |
| Disputed | two anchors held | regional campaigns and principality charters are blocked |
| Functional | three anchors held, or all four held for less than 120 days | normal campaign actions and settlement choices |
| Recognized | all four anchors held for 120 uninterrupted days | direct integration, order arbitration, wider diplomacy |
| Supreme | Recognized, a completed government settlement, and no unanswered demand | Holy See, Kingdom of God, and Holy World preparation gates |

The opening release starts at Functional, because Malta, Jerusalem, the sea road, and the port are all held on day one but have not yet proven stable.
The step is stored as one integer and recomputed by an owner-local refresh effect.
The refresh runs when a registered anchor state changes control, when a demand resolves, when a government settlement completes, and when the council window opens.
It does not poll.

## Order Cohesion

**Meaning:** whether the orders cooperate or turn the crusade into a rivalry over land, money, command, and relics.

**Gains:** a demand honoured fairly, a joint command that succeeds, a shared victory, Papal arbitration accepted, a charter honoured.

**Losses:** a demand refused, favouritism toward one order, a casualty blamed on another order, a relic scandal, an order dealing with a foreign sponsor on its own.

| Band | Name | Effect |
| --- | --- | --- |
| below 30 | Open Rivalry | one order incident is always open, joint actions are blocked |
| 30 to 49 | Strained | demands cost more and mixed-order formations are weaker |
| 50 to 74 | Working | Convene Joint Command is available and mixed-order operations work |
| 75 and above | United | confederation capstones and the elite mixed formation unlock |

A formal dominant-order settlement changes what Cohesion measures.
The value then reads as obedience to the dominant order, with the same thresholds and a different tooltip.
It does not create another value.

## Sacred Legitimacy

**Meaning:** religious recognition, public belief, Papal support, and the prestige of sacred sites and relics.
It measures political belief and never proves divine truth.

**Gains:** Jerusalem held under humane administration, pilgrim routes kept open, relief of a stricken Christian community, Papal recognition, a relic accepted by the Church.

**Losses:** a sacred site looted or lost, a relic exposed as false, open conflict with the Pope, public Condemnation for an atrocity, a sacrilege scandal.

| Band | Name | Effect |
| --- | --- | --- |
| below 20 | Discredited | foreign donations stop and Blessed access is lost |
| 20 to 39 | Contested | limited volunteers, relic effects uncertain |
| 40 to 64 | Recognized | normal religious diplomacy and volunteer access |
| 65 to 79 | Sacred Mandate | Blessed formations and Papal routes open |
| 80 and above | Universal Claim | Kingdom of God and Holy World preparation gates |

Condemnation is the one shared-system input with a fixed rule: a new public Condemnation event against an Event 38 actor lowers Legitimacy by a script-constant step once per source event.
This is the player-visible link to camps, chemical or biological use, and exposed atrocities (see `16_chaos_deaths_condemnation_migration.md`).

## Movement scale

A minor event moves Cohesion or Legitimacy by 2 to 5, a decision or mission by 5 to 10, and a defining victory, scandal, or settlement by 10 to 20.
No single action crosses more than one band without a route-defining event.
Values clamp at 0 and 100 and report only the applied change.

## Orders

### Seats

The council has up to six order seats, and a demand can only come from a seated order.
At the opening the Hospitallers, the Templar Revival, and the Naval Orders hold seats.
The Teutonic Chapter, the Order of Saint Lazarus, and the Siege Brotherhoods receive a seat when Evolution I activates, or earlier when the player completes the first focus of that order's path.
This keeps the baseline council to three voices and lets Evolution I add three more.

### Order record

Each seated order keeps only three internal facts: influence (low, normal, high), grievance (0 to 3), and headquarters state.
Influence is shown as seat prominence.
Grievance is shown only as a warning mark on the seat when it reaches 3.
Everything else about an order (unit variants, commanders, route compatibility) derives from the focus path and is not stored on the order.

| Order | Identity | What a seat gives | What it costs |
| --- | --- | --- | --- |
| Hospitallers | care, fortification, endurance | field hospitals, recovery, attrition reduction | refuse to serve camps or harsh requisition, which strains Cohesion if the player uses them |
| Templar Revival | finance, offence, conquest | procurement, breakthrough, war finance | debt and sponsor dependence, treasury demands |
| Teutonic Chapter | discipline, heavy armour | Armored Knight quality, organization | command-post and ideology demands, hidden-route exposure |
| Order of Saint Lazarus | disease, contaminated regions | outbreak and fallout resilience, relief missions | public fear, conflict with biological warfare |
| Naval Orders | islands, ports, convoys | marines, convoy defence, island invasion | dockyard and transport command demands |
| Siege Brotherhoods | engineers, fortress assault | Siege Hosts, engineer support, fort attack | heavy transport, workshop, and civilian-damage demands |

## Demands

One major demand is open at a time.
The first demand arrives no earlier than 90 days after the opening and after the council window has first opened, so the player learns the opening war before council pressure peaks.
After that the interval follows the cadence table in `28_balance_tuning_tables.md`: 150 to 240 days when stable, 210 to 330 days while United, and 75 to 150 days below Cohesion 30, never shorter than 60 days.

A demand states the requesting order, one concrete request, a 45-day deadline, and what each answer costs.
Typical requests are a headquarters in a named state, a share of captured equipment, funding for hospitals or workshops, an order commander, operational autonomy for a front, a principality charter, custody of a relic, or a role in Jerusalem.

The answers are:

| Answer | Cost | Result |
| --- | --- | --- |
| Accept | the full request | Cohesion gain, grievance of that order falls by 1 |
| Compromise | half the request, once per order and demand | half the Cohesion gain, grievance unchanged |
| Refuse | none | Cohesion loss, grievance of that order rises by 1 |

An unanswered demand at its deadline counts as a refusal.
There is no deferral.
A deferral would be a free cooldown reset, and the 45-day deadline already gives the player time to prepare.

## Incidents

An incident opens when an order's grievance reaches 3 or Cohesion falls below 30.
Only one incident is open at a time, and it offers three bounded responses: concede the grievance, send it to Papal or council arbitration, or suppress it.
Suppression lowers Command Standing by one step for 90 days and Cohesion by a script-constant amount.
An order that causes three incidents within 365 days loses its seat for 180 days and its headquarters state gains local resistance.
No incident creates a country split or a civil war.

## Dominant order

One order can become the formal dominant order through a route focus.
It requires at least Functional standing, the order's own path progress, no open incident, and a settlement event.
Dominance strengthens that order's tools, weakens rivals, and changes the Cohesion reading to obedience.
Dominant-order capstones are mutually exclusive.
The confederation route instead rewards high Cohesion and balanced seats with broader unit access and less specialization.

## Relics

Relics exist only from Evolution III.
The campaign has at most three relic claims, each drawn from a researched tradition such as a True Cross fragment, a Holy Lance tradition, or a Maltese or Rhodian order relic.

Each claim has a custodian (Malta, Jerusalem, an order, or the Pope) and a standing: unexamined, accepted, disputed, or exposed.
Whether a claim holds up is decided once, at examination, by a fixed weighted roll whose weights depend on the custodian and the claim's tradition.
The result is stored only as the standing and is never printed as a true or false value.

Four actions drive the system: sponsor an expedition, examine a claim, display a relic in Jerusalem, and transfer custody.
Outcomes move Legitimacy, Cohesion (custody disputes), and foreign interest.
A relic never gives a permanent flat combat bonus.
Accepted relics are the sponsorship basis for Blessed formations.

## Blessed formations

Blessed formations are elite variants for the player who has built Sacred Mandate.
They require Evolution III or an approved terminal setup, Legitimacy of 65 or more, a relic or Papal sponsor, full equipment and manpower, and a strict country cap.
Losses are permanent, and losing Sacred Mandate stops new formations without deleting existing ones.
Battlefield miracle reports are event flavour and add no hidden power.

## Council window

The Crusade Council is a dedicated event-owned window because the player seats orders, answers demands, and reads three linked readouts together.
A decision category alone cannot show those relationships.
The decision category keeps ownership of timed missions, map-targeted actions, and ordinary costs, and the window calls the same accepted helpers.

The window contains:

- the Command Standing line with four anchor icons showing held or lost
- the Cohesion and Legitimacy meters with the next material threshold
- the order seats, three at the opening and up to six, with a dominant-order frame and a warning mark when a grievance is at 3
- one demand or incident card with its deadline
- three answer buttons (Accept, Compromise, Refuse) and one Convene Joint Command button

It carries no relic card, no ledger, and no list of hidden numbers.

States to design and review: normal, hover, selected seat, demand open, incident open, order dominant, seat suspended, Jerusalem lost, Papal route active, terminal ready, and closed after defeat or annexation.
Every state has a static fallback, and animation is allowed only to mark a live danger or the current selection.

### Sample tooltip text

- Command Standing: Functional. Hold all four anchors for 98 more days to be recognized.
- Order Cohesion: Strained. The Templar request for the Cyprus treasury is unanswered.
- Sacred Legitimacy: Recognized. A relic accepted by Rome would carry the cause toward a sacred mandate.
- Demand: The Hospitallers ask for a field hospital in Haifa within 45 days.
- Incident: The Naval Orders have refused to escort the Teutonic convoy.

## AI behavior

The AI answers the same demands and incidents as the player and uses the same availability rules.
It prefers to accept a demand it can afford while Cohesion is below 50, to compromise when the cost is above its reserve, and to refuse only when the order is low influence and the cost is a hardship.
It resolves an open incident before opening a new offensive and avoids relic examination when a scandal is recent.
Demand timing, answer choice, and relic examination odds are weighted surfaces and need named probability scenarios (see `15_ai_probability_and_balance.md`).

## Cleanup

The mechanic closes or transforms when Malta is annexed with no successor, when the country becomes the Holy See or Kingdom of God, when the Teutonic Order changes the council structure, when Atlantis destroys the actor, when the Holy World replaces ordinary management, or when the event is cleanly defeated.
Transformation keeps the durable order, relic, principality, and Legitimacy facts that later routes need and removes stale buttons, invalid targets, expired demands, and selected-card state.
