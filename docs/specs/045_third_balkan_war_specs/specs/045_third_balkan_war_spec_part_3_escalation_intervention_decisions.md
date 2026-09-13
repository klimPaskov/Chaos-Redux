# Event 045 escalation, intervention, decisions, and missions

## Escalation contract

Balkan War Escalation changes only when a country makes the linked conflict materially larger or materially smaller. Time can confirm a stable de-escalation after a concrete containment action, but time alone never increases the value.

All gains and losses must use one event-owned transaction helper with source identity, actor, target camp, amount, repeat guard, stage floor, and history reason. This avoids double application from the same guarantee, sponsor, or war entry.

## Escalation source families

The ranges below are tuning bands. Final values should scale within the band from actor importance, commitment size, current stage, and whether the source crosses a new proof threshold.

| Source | Suggested band | Repeat rule |
| --- | --- | --- |
| Additional Balkan country enters a linked war | `+8` to `+12` | Once per country per generation |
| New registered claim opens a real additional front | `+3` to `+6` | Once per claim family |
| Foreign material support crosses a support tier | `+3` to `+6` | Once per sponsor, camp, and tier |
| Volunteers, expeditionary force, or military mission arrives | `+4` to `+7` | Once per sponsor and camp for each distinct commitment class |
| Guarantee is enforced | `+8` to `+12` | Once per guarantor and protected country |
| Faction member enters through the crisis | `+8` to `+12` | Once per entrant |
| Coordinated sanctions or blockade creates opposing bloc pressure | `+3` to `+6` | Once per coalition and stage |
| Outside major enters directly | `+12` to `+18` | Once per major |
| Opposing major powers or major-led factions enter direct war | `+15` to `+25` | Once per verified opposing pair or faction linkage |
| Linked war opens a non-Balkan strategic theater | `+10` to `+15` | Once per macro-region |
| Accepted armistice is deliberately violated | `+6` to `+10` | Once per violating country and armistice generation |

Material support should use cumulative support tiers rather than awarding escalation for every click. Sending a small second shipment after a major first shipment should not farm the meter. The internal ledger should aggregate equipment value, fuel, aircraft, volunteers, and other support into a sponsor-to-camp commitment class.

## Containment source families

| Reversal | Suggested band | Conditions |
| --- | --- | --- |
| Coordinated arms suspension | `-3` to `-6` | Opposing sponsors both reduce or halt material aid |
| Guarantee withdrawal before direct entry | `-4` to `-8` | The guarantee was relevant and no replacement commitment is made |
| Verified troop or volunteer withdrawal | `-4` to `-7` | A real military commitment leaves the linked conflict |
| Armistice accepted and line established | `-8` to `-14` | All required belligerents accept and active offensives stop |
| Armistice line held to mission completion | `-6` to `-10` | No prohibited occupation or offensive breach |
| Settlement conference reaches agreement | `-10` to `-18` | A durable regional settlement ends at least one linked war |
| Foreign containment coalition dissolves opposing commitments | `-5` to `-10` | At least two outside powers act together and remove a live escalation source |

Escalation cannot be reduced below an irreversible floor created by direct conflict:

- Direct outside-major entry sets a floor at the European Crisis threshold.
- Opposing majors or major-led factions in direct war set a floor at the Powder Keg threshold.
- Verified Another World War locks the final stage and ends regional meter management.

A stage can move downward before these floors when concrete commitments are withdrawn and the lower state remains stable through a short confirmation window. The maximum reached stage remains in the hidden record.

## Stage proof

### Balkan Conflict

The opening linked wars exist and the conflict has not met a higher proof.

### The Balkans Are on Fire

The value crosses `25` and at least one of these is true:

- four or more regional countries are directly involved
- at least one later regional entrant has joined
- more than one registered claim family has opened a real front

### European Crisis

The value crosses `45` and outside involvement is material. Valid proof includes opposing camps with outside sponsors, an enforced foreign guarantee, a foreign volunteer commitment plus a second opposing commitment, or a major power deploying military support with direct access to the theater.

### The Powder Keg Explodes

The value crosses `65` and at least two hostile major powers or two major-led faction structures are directly involved in the linked war graph. Proxy aid alone cannot satisfy this stage.

### Another World War

The value crosses `85`, the Powder Keg proof remains true, and at least one wider-war proof exists:

- three or more major countries are directly committed across the linked wars
- two major-led factions have several non-Balkan members committed
- the linked war graph has active fronts in the Balkans and at least one separate strategic macro-region
- the crisis joins two previously separate major wars into one effective global conflict

Until a valid wider-war proof exists, the public value caps at `84`.

## Stage reports

Each upward stage transition receives one report or news event. It should identify the concrete development that crossed the threshold, not repeat the meter definition. The report family covers:

- another Balkan country entering
- opposing foreign support becoming public
- a guarantee or faction call being enforced
- direct major-power entry
- the global-war handoff

Downward movement should normally use a concise decision-category status update and settlement event, not another dramatic report chain.

## Decision category structure

The event uses normal decisions with a static category picture. It does not need a separate mechanic window.

The category header shows:

- the escalation meter
- current stage
- latest material source or reversal
- next threshold and its proof requirement
- the country's current role

The category uses conditional replacement so one phase shows three to five primary actions. Six is the hard maximum. One to three missions may be active. Target-heavy families use the selected-target pattern rather than displaying every country at once.

## Regional belligerent actions

### Formalize a Valid Regional Claim

Working label. The country selects one currently valid claim from the maintained registry. The action records a settlement objective and may affect neutral-country intervention interest. It does not grant an automatic core.

Possible costs and requirements:

- political capacity
- army experience or command power for military planning
- current control, border access, or a viable route to the target
- a stability or diplomatic consequence when the claim conflicts with an ally

### Request Foreign Arms

The country selects an outside sponsor with access and compatible interests. The request can be accepted, reduced, conditioned, or refused. A large accepted package crosses a support tier and raises escalation.

Possible costs and risks:

- political capacity
- sponsor influence memory
- convoy or rail route requirement
- later diplomatic obligation

### Invite Volunteers or a Military Mission

The country invites a sponsor to commit personnel. This is stronger than arms support and creates a visible foreign commitment. It should require diplomatic access, available sponsor forces, and a valid theater route.

### Secure a Strategic Corridor

The country begins a goal mission around a selected port, railway, supply hub, or Straits approach. Success improves the campaign position and can strengthen the related settlement claim. Failure can expose the camp to foreign pressure or a lost capital route.

### Offer Armistice Terms

Available when the current military and diplomatic state supports a real offer. Terms depend on occupation, active claims, war contribution, escalation stage, and sponsor pressure. A country that is completely defeated should not demand maximal terms.

### Accept or Reject Outside Mediation

The country responds to a specific conference or guarantor proposal. Acceptance can begin an armistice mission. Rejection preserves military freedom but may worsen sponsor relations and increase the chance of outside intervention.

### Demand an Allied Occupation Adjustment

Available when an ally occupies a state covered by the country's active claim. The action opens negotiation or a timed withdrawal demand. It is a key baseline source of postwar tension and a major Evolution III precursor.

## Neutral Balkan actions

### Register an Interest

The country identifies a valid disputed state group that affects its own security or claim. This does not force entry. It enables later mobilization, arbitration, or intervention choices.

### Mobilize the Disputed Frontier

The country commits equipment, fuel, command capacity, and divisions to a named border group. This is preparation, not a free national modifier.

### Join a Camp

The country selects a camp whose objectives and diplomatic position are compatible. Entry requires a claim, guarantee, faction tie, security threat, or major strategic interest. It raises escalation once.

### Offer Regional Arbitration

A neutral regional government attempts a bounded settlement. Its chance improves when it has relations with both sides, no active claim on the target, and support from outside containment powers.

### Demand Neutrality Guarantees

The country asks outside powers or neighboring camps to recognize a neutral corridor or frontier. Failure can move it toward intervention.

### Open or Close Transit

The country changes access through a relevant port, Straits passage, railway, or border corridor. The action affects supply and sponsor access. It should not become a generic whole-country trade toggle.

## Outside-power containment actions

### Convene a Containment Conference

Requires a relationship with at least two belligerents or cooperation from another outside power. The conference creates a timed diplomatic objective rather than an instant peace button.

### Coordinate an Arms Suspension

Targets an opposing sponsor or coalition. It becomes effective only when material commitments are genuinely reduced.

### Pressure a Guarantee Withdrawal

Attempts to remove a guarantee before enforcement. The action can fail when the guarantor has strong ideology, faction, or rivalry reasons to remain.

### Enforce a Ceasefire Line

Available after armistice acceptance. It creates the armistice-line mission and requires observers, diplomatic access, and enough leverage.

### Apply Coordinated Sanctions

Requires at least one cooperating outside power or a strong international position. Sanctions create economic and diplomatic pressure. They do not directly end a war.

## Outside-power exploitation actions

### Send a Weapons Shipment

Consumes a meaningful stockpile and transport route. Support scales from sponsor industry, recipient need, distance, and escalation stage. Repeated shipments cross bounded tiers.

### Dispatch Volunteers

Requires available forces, political willingness, and theater access. The commitment is public and raises escalation.

### Recognize a Claim

Strengthens one settlement objective and damages relations with competing claimants. It can also make a neutral Balkan country more likely to intervene.

### Issue a Guarantee

Creates a real future commitment. It should be unavailable when the sponsor cannot reach or defend the recipient.

### Invite to Faction

Available only when ordinary faction rules and event-specific safety checks permit it. Invitation can pull existing faction members toward the crisis and therefore carries a large escalation risk.

### Prepare Direct Intervention

This is a timed military commitment. It requires access, forces, supply, war support, and a defined camp. Completion can lead to direct entry and the largest single escalation source.

## Mission families

### Secure the Capital Rail Line

- Role: regional belligerent
- Objective: hold the capital and a dynamically selected chain of rail or supply states while keeping them connected
- Duration: normally `90-150` days
- Difficulty factors: terrain, damaged rail, enemy pressure, number of fronts, and current escalation
- Success: strengthens supply, camp viability, and settlement standing
- Failure: weakens defensive confidence and can increase foreign intervention interest

### Keep the Aegean or Adriatic Corridor Open

- Role: country whose war objective or survival depends on a port corridor
- Objective: hold the named port and inland connection, maintain transport, and prevent encirclement
- Duration: normally `90-150` days
- Costs: convoys or trains, fuel, equipment, and tied-down divisions according to the route
- Success: improves aid delivery and validates the corridor claim
- Failure: cuts support and can make armistice terms harsher

### Enforce the Armistice Line

- Role: all required signatories and the outside mediator
- Objective: withdraw from prohibited states, avoid new offensive entry, and hold the line for `60-90` days
- Success: lowers escalation and opens settlement
- Failure: records the violator, ends the armistice, and applies a one-shot event-owned escalation source

### Restrain Allied Occupation

- Role: camp member with an ally occupying its active claim
- Objective: resolve the occupation through transfer, joint administration, withdrawal, or a negotiated waiver within `60-90` days
- Success: prevents a fracture memory
- Failure: increases hidden incompatibility and Evolution III eligibility

### Guard the Straits Approaches

- Role: Turkey or another directly relevant controller
- Objective: hold named European Thrace, Straits, port, and supply positions while controlling military access
- Success: limits foreign deployment and strengthens mediation leverage
- Failure: opens a wider access route and raises sponsor interest

## Cost rules

No action may consume more than four spendable cost types. State control, relations, unit placement, border access, and route access are requirements, not hidden costs.

Costs should be dynamic from country size, distance, stockpile, commitment class, current war load, and stage. Major actions must not become political-power-only purchases. Every displayed cost needs the matching texticon.

## AI equivalents

Every player decision and mission requires an AI path using the same validity helpers and outcome effects. AI does not need to interact with the human selected-target interface. It may evaluate all valid targets through bounded decision weights and owner effects.
