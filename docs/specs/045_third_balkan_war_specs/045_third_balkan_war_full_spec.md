# Event 045: Third Balkan War complete specification


---

## Included file: `README.md`

# Event 045: Third Balkan War specification pack

This package is the accepted planning handoff for Chaos Redux Event 045, **Third Balkan War**.

Extract the top-level folder to:

```text
docs/specs/045_third_balkan_war_specs/
```

The package defines the complete event design, the dynamic opening war builder, the single public escalation mechanic, regional claims, foreign intervention, settlements, three true evolutions, AI strategy, achievements, assets, super-events, testing scenarios, and implementation acceptance criteria.

## Package map

| Folder | Purpose |
| --- | --- |
| `specs/` | Accepted source design split by gameplay surface |
| `diagrams/` | Lifecycle, decision, claim, and escalation maps |
| `research/` | Historical design research, bibliography, and source manifest |
| `prompts/` | Bounded implementation handoffs for assets, super-events, achievements, decisions, coding, and the final goal |
| `quality/` | Probability scenarios, acceptance criteria, design review, closure handoff, and tooling blocker report |
| `handoffs/` | Cross-system implementation map and documentation alignment requirements |

## Core non-negotiables

- Event ID `45` remains a Minor Fire-Once event with Chaos level `1`.
- The entry event remains `chaosx.nr45.1`.
- The opening always creates a multi-country regional war when the event is valid.
- The event exposes exactly one persistent custom value, **Balkan War Escalation**.
- Baseline escalation stages remain separate from Evolutions.
- Evolutions alter the structure of the war and do not act as ordinary escalation stages.
- Generic wars, deaths, annexations, puppeting, faction changes, and peace continue through shared Chaos Redux systems without duplicate Event 045 Chaos awards.
- **Another World War** is a handoff to normal war and faction systems, not a terminal world-end scenario.
- The event belongs to the Wars cluster with High member severity.
- The implementation must remain dynamic across changed borders, successor states, player countries, and alternate-history faction maps.

## Source status

Every supplied project source file and every archived subagent definition was read in full before this package was written. The stored specialist contracts were applied during the design review. Actual specialist invocation through the outer Codex tunnel was attempted and failed with transport errors. The exact blocker is recorded in `quality/045_third_balkan_war_subagent_blocker.md`.

---

## Included file: `specs/045_third_balkan_war_spec_part_1_core.md`

# Event 045: Third Balkan War

## Catalog identity

- Event ID: `45`
- Event name: Third Balkan War
- Event type: Minor Fire-Once
- Chaos level: `1`, Calm World
- Cluster: Wars
- Member severity: High
- Entry event: `chaosx.nr45.1`
- Accepted status after planning: Ready for implementation

## Event promise

The event turns the Balkans into the origin of a war that begins as a genuine regional struggle and can expand through decisions made by regional governments, outside patrons, guarantors, and factions. The opening conflict must already involve several countries. The player should never wait through a diplomatic prelude to discover whether the event will produce a war.

The central play question is whether governments treat the conflict as a bounded Balkan settlement or as an opportunity to settle every nearby rivalry. A regional belligerent chooses which claim is worth extending the war for. A neutral Balkan state decides whether its own frontier is now at stake. An outside power decides whether containment is worth more than weakening a rival. Each of those choices changes the same public measure, **Balkan War Escalation**.

The event can end with a contained regional victory, a negotiated settlement, an imposed armistice, a wider European war, or a global war that ordinary systems continue. It must never force the world-war outcome merely because the event has remained active for a long time.

## Player experience

A regional player receives an immediate wartime situation with clear objectives, a visible escalation stage, and a small set of actions that fit its current role. The player can press a registered claim, secure a military corridor, request foreign support, seek an armistice, or contest an ally's occupation. The player is not asked to manage a separate claim score, foreign influence score, camp cohesion score, and settlement score. Those calculations remain internal.

An outside player receives a role-aware intervention category only when it has a real route into the crisis. It can coordinate containment, arm one side, recognize a claim, issue a guarantee, invite a country into a faction, or prepare direct intervention. These are consequential commitments. They consume equipment, fuel, convoys, political capacity, diplomatic access, or military readiness according to the action.

The event should become easier to read as it grows. More countries and more hidden relationships may exist, but the decision category still presents only the current stage, the latest material cause of escalation, the next threshold, and the actions relevant to the current country.

## Public mechanic

The event has one persistent public value:

### Balkan War Escalation

- Range: `0` to `100`
- Public presentation: a labelled meter with five named stages
- Main cause: concrete expansion of the linked conflict
- Main response: containment actions, withdrawal of commitments, armistice compliance, or settlement
- No passive upward drift
- Hidden inputs are summarized in a concise tooltip instead of exposed as separate values

The five public stages are:

| Range | Stage | Campaign meaning |
| --- | --- | --- |
| `0-24` | Balkan Conflict | The opening regional camps are fighting and outside powers remain observers or limited suppliers. |
| `25-44` | The Balkans Are on Fire | More regional countries have joined, active claims have multiplied, or the original conflict has opened additional Balkan fronts. |
| `45-64` | European Crisis | Opposing camps have meaningful outside backing through arms, volunteers, guarantees, sanctions, deployments, or faction pressure. |
| `65-84` | The Powder Keg Explodes | Major powers or major-led factions are directly fighting on opposing sides. |
| `85-100` | Another World War | The linked conflict now qualifies as a wider global war and Event 045 hands control to normal war, faction, and peace systems. |

A numerical threshold is necessary but never sufficient for the final two stages. Each stage also requires the matching world-state proof. The meter caps below the next threshold until that proof exists. This prevents a large pile of aid shipments from being displayed as direct major-power war.

## Hidden simulation

The event may track many internal facts without making them player counters:

- event generation and active lifecycle
- opening cause and dispute family
- initiator and opening camp leaders
- opening participants and later entrants
- linked war identifiers
- country role and camp membership
- registered regional interests
- activated claims
- sponsor, recipient, support type, and support tier
- guarantees and faction commitments
- maximum escalation reached
- stage proof flags
- armistice offers and compliance
- settlement participation
- allied occupation disputes
- fragmentation candidates
- former allies with incompatible claims
- postwar memories

These facts should use bounded registered arrays, event targets, flags, and owner-scoped ledgers. The event must not add a broad daily whole-world scan.

## Lifecycle overview

1. Validate that the event can honestly create a multi-country Balkan war.
2. Build the current regional country pool from geography, country type, survival, and diplomatic state.
3. Select a valid dispute and an initiator.
4. Build two hostile camps, or a justified three-sided conflict graph.
5. Start the linked wars immediately.
6. Record opening participants, claims, sponsors, and escalation.
7. Show the outbreak super-event and role-aware decisions.
8. React to new entrants, support, guarantees, faction calls, direct intervention, armistices, occupation, and settlement.
9. Activate Evolutions through their own requirements and pacing.
10. Resolve through regional settlement, imposed ceasefire, wider-war continuation, or world-war handoff.
11. Clear temporary state and retain only defined postwar memories.

## Global-war honesty gate

The event should normally be unavailable for automatic selection when the world is already in a multi-faction global war whose active participants cover most valid Balkan candidates. In that state the event cannot honestly claim to have started another world war.

A large existing war does not automatically block Event 045 when the Balkan countries remain outside it and the event can create a distinct regional conflict. The `third_balkan_war_origin_crisis` memory is set only when Event 045 creates the first qualifying wider-war linkage. Force Trigger Mode may bypass normal selection for testing, but the causal origin flag still requires proof.

## Presentation direction

The opening uses restrained dark humour about the recurrence of Balkan crises and Europe's repeated belief that this time the fire will remain local. The fighting, civilian harm, and military losses are treated seriously. Each later stage removes more humour. The world-war handoff should be direct and grave.

The emotional focus should remain on mobilizing troops, crowded railways, frontier posts, contested ports, broken armistice lines, and foreign columns arriving in the region. Maps can appear as secondary objects but should not be the main visual subject.

Final player-facing wording belongs to implementation and super-event research. The spec supplies tone and factual direction, not pasteable localisation.

---

## Included file: `specs/045_third_balkan_war_spec_part_2_opening_and_participants.md`

# Event 045 opening and participant system

## Validity gate

Event 045 is valid only when the current map can support a real regional conflict.

The minimum opening is three valid regional countries distributed across at least two hostile camps. There must be at least one legal hostile pair and enough viable countries to avoid a disguised one-on-one war. When only two valid countries remain, the event is unavailable. Its Events-tab weight displays `N/A` rather than zero.

A valid opening country must:

- exist and control a capital
- control enough territory to function as a wartime country
- have a viable military or a valid emergency mobilization route
- not be capitulated
- use normal civilian and diplomatic systems
- not be classified as a special Chaos country or actual nonhuman country
- have a relevant Balkan position, border, territory, or registered regional claim
- be legally capable of belonging to one of the linked wars

Player-controlled regional countries remain eligible under the same validity rules. They receive no immunity from participation and no forced inclusion when their map position is irrelevant.

## Regional pool

The normal core pool includes:

- Yugoslavia
- valid Yugoslav successor states
- Bulgaria
- Greece
- Albania
- Romania
- Hungary
- Turkey when it controls European territory, the Straits approaches, or a registered Thracian interest

A Balkan-adjacent country may enter the opening pool only when current geography makes it part of the dispute. Valid evidence includes control of a state inside the maintained Balkan claim registry, a direct land border with the registered dispute zone, or an active regional claim on a state in that zone. Mere proximity is insufficient.

Outside powers that control regional territory can qualify as regional actors for the relevant territory. An outside major with no regional land, border, or claim remains an intervention actor rather than an opening belligerent.

## Existing wars and factions

A country already fighting a limited unrelated war can still qualify, but its war load reduces its opening score. A country close to capitulation, fighting an existential multi-front war, or unable to support another front should normally become a neutral observer or be excluded.

Countries inside the same faction cannot be placed in opposing opening camps. Same-faction regional actors may:

- join the same opening camp
- remain neutral
- appear as guarantors or later faction entrants
- become eligible for Event 045 alliance fracture only after Evolution III activates

If every valid regional country belongs to one faction and no legal hostile camp can be built, the event is unavailable.

## Opening size

The preferred opening contains four to six regional participants when that many valid countries exist. The system may use three when the map is fragmented or most candidates are invalid.

Participant count should respond to:

- number of valid regional countries
- current Chaos tier
- military viability
- active disputes
- faction and guarantee entanglement
- current war load
- whether a player country is in the candidate pool

The system should not fill a camp with an implausible ally solely to reach a target number. A smaller coherent opening is better than a larger nonsensical one.

## Dispute selection

The opening dispute is selected from maintained regional dispute families. A dispute becomes eligible only when the current map contains at least two valid interested countries and a meaningful target area.

### Baseline dispute families

1. **Macedonian claims** involving the Vardar, Pirin, and Aegean Macedonian state groups where current borders make the dispute live.
2. **Access to the Aegean** involving Western Thrace, the lower Maritsa corridor, or another maintained route from an inland claimant to an Aegean port.
3. **Serbian-Bulgarian frontier** involving the Timok, Niš, Caribrod, Strumica, or current equivalent border groups.
4. **Greek-Bulgarian rivalry** involving Western Thrace, the Struma corridor, Rhodope approaches, and related frontier groups.
5. **Albanian territorial claims** involving Kosovo, western Macedonia, northern borderlands, or southern borderlands when current state ownership supports the dispute.
6. **Romanian-Bulgarian frontier** centered on Southern Dobruja or its current equivalent.
7. **Hungarian-Romanian frontier** centered on Transylvania, the Partium edge, and current adjacent contested groups.
8. **Hungarian-Yugoslav frontier** involving Banat, Bačka, Vojvodina, or current successor-state equivalents.
9. **Yugoslav successor settlement** involving unresolved internal borders, capital claims, shared ports, railways, and former federal territory.
10. **Straits and European Thrace security** involving Turkey and countries whose current borders or claims directly affect the approaches.
11. **Unresolved prior settlement** drawn from existing claims, recent peace outcomes, occupation memories, or unfulfilled regional transfers.
12. **Absurd frontier incident** inspired by documented interwar border crises. The incident can be trivial, accidental, or administratively ridiculous, but the underlying camps still require real existing tensions.

The popular stray-dog version of the 1925 Petrich incident has competing origin accounts. It may inspire the absurd-incident family, but implementation should not present it as settled historical fact without stronger source proof.

## Dispute weighting

A dispute receives weight from:

- active claims and cores
- current ownership of the target state group
- negative relations and strategic rivalry
- prior wars and peace settlements
- access to a sea, port, rail hub, or supply corridor
- existing guarantees or defensive arrangements
- military readiness
- current ideology and national strategy
- event connections such as an active Old Great Bulgaria route
- Chaos tier and enabled Evolution I state

The dispute identity influences camp assignment and opening objectives. It never starts a long countdown. The linked wars begin in the opening transaction.

## Initiator selection

The initiator is the eligible country with the strongest combined dispute interest and viable offensive position. Selection should consider:

- direct claim or core relevance
- ability to reach the target area
- army readiness and supply
- war support
- current strategic aggression
- hostile relations
- support from likely camp partners
- whether the country is already overextended

The initiator becomes the default event-log actor. A player country may be selected when it is the strongest valid initiator. The event must not always force the player to be the initiator merely because a player exists in the region.

## Camp construction

Two camps are normal. Each candidate receives a score for every camp based on:

- shared claim or shared enemy
- ideological affinity
- faction and guarantee ties
- border adjacency
- military access
- strategic need for the same port, rail route, or Straits position
- relations with the initiator and opposing leader
- expected survival
- existing foreign support

Conflicting claims on the same state reduce the score for sharing a camp. A country with a stronger claim conflict against a proposed ally than against the nominal enemy should remain neutral or form a separate side.

Camp construction should seek military viability without manufacturing symmetry. One side may be stronger, but the opening should avoid a hopeless camp when another coherent assignment exists. Effective strength includes divisions, manpower, equipment, supply, terrain, fronts, and existing war load.

## Three-sided opening

A three-sided opening is valid only when the claim graph cannot be represented honestly by two camps. It requires:

- at least three viable countries or country groups
- three distinct objectives or two objectives with a genuine overlapping claimant
- at least one hostility edge for every side
- no side created solely to increase spectacle

Implementation should create a linked war graph. It need not make every camp fight every other camp. For example, one camp may fight both rivals while the two rival camps remain temporarily non-belligerent. A complete all-against-all opening belongs only to a valid high-Chaos situation or later Evolution III fracture.

## Opening escalation

The opening value is derived from the number of participants and inherited commitments. A recommended central formula is:

- base opening pressure for a three-country war
- an additional step for each participant beyond three
- a smaller step for each relevant outside guarantee or faction commitment already attached to the opening countries
- a cap below the European Crisis stage unless outside support has already become material

This normally places a three-country opening near the lower middle of Balkan Conflict and a six-country opening close to The Balkans Are on Fire. The exact constants belong in one Event 045 script-constant group.

## Opening transaction order

1. Build and freeze the valid regional pool for this generation.
2. Select the dispute and target state group.
3. Select the initiator and counter-camp leader.
4. Build camps and the hostility graph.
5. Validate every country and war edge again.
6. Save opening participants, camps, claims, and actor context.
7. Start all linked opening wars in one bounded transaction.
8. Apply only event-owned temporary wartime setup that is necessary for clarity or viability.
9. Calculate opening escalation.
10. Record Event 045 history once.
11. Show the outbreak super-event once.
12. Open role-aware decisions and missions.

If final validation fails, the event should reject the opening cleanly, restore no partial state, and return to an unavailable or retryable selection state according to the event-system contract. It must not leave one war from a failed multi-war transaction.

## Opening edge cases

### Fragmented Yugoslavia

Successor states are evaluated independently through geography and claim relevance. They do not automatically form one camp. A successor with no relevant border or claim remains outside the opening.

### Turkey without European territory

Turkey remains an outside power unless it has a registered Straits or Thracian claim that gives it direct regional standing. Naval proximity alone does not make it an opening belligerent.

### Region dominated by one country

When only one strong country and several nonviable remnants exist, the event should be unavailable instead of creating a ceremonial coalition with no military future.

### Existing Old Great Bulgaria content

Active Bulgarian claims and route memories may increase dispute weight and claim relevance. Event 045 must reuse those facts rather than grant duplicate claims or duplicate rewards.

### Player outside the Balkans

The player's country becomes eligible for intervention only if it can reach the region diplomatically or militarily. It is not inserted into the opening merely to guarantee player involvement.

---

## Included file: `specs/045_third_balkan_war_spec_part_3_escalation_intervention_decisions.md`

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

---

## Included file: `specs/045_third_balkan_war_spec_part_4_claims_settlement_connections.md`

# Event 045 claims, settlement, aftermath, and system connections

## Regional claim philosophy

The event uses a maintained regional claim registry. It does not generate generic expansion opportunities from country size, ideology, or random adjacency.

A registered claim must identify:

- claimant country or eligible successor family
- target state group
- historical or campaign-state basis
- current ownership test
- border or access requirement
- compatible dispute families
- conflicting claimants
- baseline or Evolution I availability
- settlement outcomes that may use it
- whether the result can become a claim, transfer, corridor, demilitarized zone, subject arrangement, or later integration path

A registered interest is weaker than an activated claim. It can influence entry, arbitration, and occupation disputes without promising ownership.

## Baseline claim groups

The implementation must map exact current state IDs through installed map data and the maintained Chaos Redux state registry. The working geographic groups below are design labels, not permission to guess state IDs.

| Claim family | Typical interested actors | Design use |
| --- | --- | --- |
| Vardar, Pirin, and Aegean Macedonia | Bulgaria, Greece, Yugoslavia or relevant successors, Albania where borders support it | Opening cause, competing claims, multi-sided conflict, settlement pressure |
| Western Thrace and lower Maritsa access | Bulgaria, Greece, Turkey where directly relevant | Aegean corridor, port access, demilitarized route, Evolution I expansion |
| Timok, Niš, Caribrod, and adjacent Serbian-Bulgarian frontier | Bulgaria, Serbia or Yugoslav successor | Limited border revision, defensive frontier, ally conflict |
| Struma and Rhodope approaches | Bulgaria and Greece | Corridor security, mountain-front mission, armistice line |
| Kosovo and western Macedonian borderlands | Albania, Serbia or Yugoslav successors, North Macedonian successor when present | Entry interest, competing settlement, fragmentation connection |
| Southern Albanian and Northern Epirus borderlands | Albania and Greece when current borders support the claim | Baseline or Evolution I claim, outside sponsor pressure |
| Southern Dobruja | Bulgaria and Romania | Direct dispute, negotiated exchange, demilitarized settlement |
| Transylvania and Partium edge | Hungary and Romania | Major Evolution I claim set, outside-power interest |
| Banat, Bačka, and Vojvodina | Hungary, Romania, Yugoslavia or relevant successors | Three-way claim graph, postwar ally dispute |
| Dalmatian, Bosnian, Croatian, Serbian, and Montenegrin successor borders | Yugoslav successor states with actual borders and claims | Fragmented map opening, Evolution II and III interaction |
| European Thrace and Straits approaches | Turkey, Greece, Bulgaria, and a current controller with direct standing | Access control, outside deployment, regional security |

Claims already granted or managed by another event remain owned by that system. Event 045 may read and recognize them, but it must not duplicate the grant, core, or completion reward.

## Activating a claim

A belligerent may activate one principal settlement claim and a bounded number of secondary claims according to stage, war size, and Evolution I state. The principal claim defines its public objective. Secondary claims remain less valuable in settlement.

Activation requires:

- a current registry match
- a valid claimant
- a reachable target or defensible diplomatic basis
- no prior completed settlement that permanently waived the claim unless Evolution I explicitly revives it
- a cost or political consequence appropriate to the claim

An ally's active claim on the same state creates an incompatibility memory. It does not immediately break the alliance at baseline.

## Occupation and war contribution

Occupation influences settlement but does not automatically settle ownership. The event should distinguish:

- military occupation
- registered claim
- principal objective
- war contribution
- legal controller before the war
- armistice-line control
- allied occupation of another member's claim

A country that occupies an unrelated state with no registered claim can use it as bargaining leverage or return it. It should not receive a new permanent claim merely because its army reached the state first.

## Settlement entry points

A regional settlement can begin through:

- decisive defeat of one opening camp
- accepted bilateral or multilateral armistice
- successful outside containment conference
- collapse or fragmentation of a participant
- negotiated settlement after military exhaustion
- a limited peace before opposing major powers enter direct war

Once the conflict reaches Another World War, Event 045 no longer tries to impose a complete regional peace. Active claims and memories remain available to the ordinary peace process and later flavour.

## Settlement evaluation

The settlement engine weighs:

- surviving governments
- active linked wars
- military occupation
- principal and secondary registered claims
- war contribution
- capital survival
- current escalation and maximum stage
- armistice compliance
- outside sponsor pressure
- neutral-country interests
- Evolution II breakaways
- Evolution III former allies
- existing subjects and factions
- whether a proposed transfer would make a country nonviable

The system should prefer a coherent settlement over assigning every occupied state to the current controller.

## Settlement families

### Status quo ante

Most territorial control returns to the pre-war state. The settlement may still include reparations, access, demilitarization, opinion changes, or a recognized unresolved claim.

### Limited border revision

One or more registered claims are settled through bounded transfers. The losing country must remain viable unless it has already collapsed through ordinary war or Evolution II.

### Corridor settlement

A port, railway, river route, or Straits approach is handled through military access, guaranteed transit, demilitarization, leased access, or a narrow transfer. This is preferable to handing over a large unrelated region merely to create sea access.

### Protectorate or subject arrangement

Available only when military defeat, sponsor control, government survival, and ordinary subject rules support it. It is not a default reward for a successful claim.

### Partition of a collapsed participant

Available after a genuine collapse with several viable successor actors. Evolution II packages, active claims, population, capital access, and supply determine the result. The event must not produce empty map fragments.

### Frozen armistice

Wars pause or end without a final settlement. Armistice lines, denied claims, and sponsor memories remain. The outcome can feed later conflicts.

### Wider-war continuation

The event closes most regional management while the linked war remains part of a larger European conflict. A later peace can still read the claim registry and origin memory.

## Peace acceptance

Regional AI should not reject every unfavorable settlement while waiting for a miracle. Acceptance rises when:

- the capital is lost
- surrender progress is high
- supply is broken
- manpower and equipment are exhausted
- no credible outside rescue exists
- allied cohesion is low
- the proposed terms preserve government viability

Acceptance falls when:

- the country holds its principal objective
- a credible sponsor is about to intervene
- the enemy is exhausted
- the settlement transfers an unregistered strategic region
- the country remains militarily capable of reversing the front

A human player sees the visible terms, signatories, state groups, access arrangements, and major diplomatic consequences before acceptance.

## Postwar memories

The event retains only memories that can change later behavior:

- principal claim fulfilled
- principal claim denied
- claim formally waived
- armistice violator
- outside sponsor
- settlement guarantor
- imposed settlement
- allied occupation dispute
- former ally betrayal
- Third Balkan War origin crisis
- Third Balkan War origin of wider war

Temporary participant arrays, selected targets, missions, offer state, support counters, and wartime modifiers are cleared.

## Event ending states

### Decisive regional victory

One camp wins before the conflict becomes a direct major-power war. A regional settlement applies.

### Negotiated settlement

Belligerents and mediators agree to terms. The result can include limited revisions, corridors, guarantees, and unresolved claims.

### Imposed ceasefire

Outside containment powers establish an armistice and the line-holding mission succeeds. A final settlement may remain partial.

### Wider European war

Major powers fight directly, but the conflict has not yet met the global proof. Event 045 remains active in a reduced role and keeps regional claims and armistice opportunities available.

### Another World War

The world-war proof is met. Event 045 records the origin crisis, locks the maximum stage, hides routine regional intervention actions, preserves claims and postwar memory, and hands the conflict to ordinary war, faction, and peace systems.

## Chaos impact map

The event should not award Chaos merely for firing, starting a war, annexing territory, changing factions, causing deaths, or signing peace. Those outcomes already belong to shared Chaos Redux systems.

Evolution activation adds zero Chaos.

The only candidate Event 045 specific Chaos source is a deliberate violation of a formally accepted event-owned armistice after the line and signatories have been recorded. Implementation must audit whether generic war, tension, and peace sources already represent that outcome. If overlap exists, the event-owned Chaos award is omitted and the violation affects only Balkan War Escalation and diplomatic memory.

A successful containment settlement may receive a bounded negative Chaos source only when it removes a distinct Event 045 escalation condition that generic peace does not already reverse. It must never refund deaths, destruction, annexations, or other lasting consequences.

## Shared-system connections

### Wars cluster

Event 045 joins the Wars cluster as a High severity member. The cluster member list becomes `4, 7, 45` after implementation. Event 045 retains its own valid-target gate. If it cannot build a valid opening, cluster firing skips it with a clear reason.

Cluster firing counts once for global pacing. Event 045 still records its own fire-once state and history when it participates.

### The Offensive

The Offensive may increase regional and outside AI willingness to choose aggressive options. It must not bypass validity, military viability, access, or settlement survival logic.

### Allies Backstab

Allies Backstab can destabilize factions involved in the war through its own event. Evolution III must not duplicate the same betrayal transaction. When Allies Backstab fires first, Event 045 reads the changed alliance graph and may use it as an incompatibility fact.

### Independence Wave and Random Civil War

Evolution II reuses their country release, civil-war, starting-force, and cleanup packages where suitable. Event 045 owns the request and regional placement. The provider system owns the country transaction.

### Old Great Bulgaria

Active Bulgarian route claims and identities can affect dispute weighting, claim availability, and AI. Event 045 does not grant a second copy of those claims or route rewards.

### Famine and Migration

Sieges, blockades, destroyed routes, and civilian flight continue through shared famine and migration systems. Event 045 does not apply flat refugee population changes or duplicate famine deaths.

### Deaths, Condemnation, and Air Cleanliness

Military and civilian losses use the shared Deaths system. Chemical, biological, nuclear, atrocity, and contamination consequences use their owning systems. Event 045 only records that they occurred inside the linked war when later flavour needs that context.

## Cleanup and persistence

Cleanup occurs when all linked regional wars have ended, the event has handed off to a wider war, or no valid regional participant remains.

Cleanup must:

- remove role-aware decision categories and active missions
- clear selected-target country flags and stored target IDs
- clear temporary event targets
- remove event-owned temporary modifiers
- close unaccepted offers
- stop further escalation transactions for the completed generation
- preserve only the approved postwar memories
- leave ordinary wars and faction state untouched after a wider-war handoff

---

## Included file: `specs/045_third_balkan_war_spec_part_5_evolutions.md`

# Event 045 Evolutions

## Evolution principles

The three Evolutions change what the war can become. They are not labels for ordinary escalation.

Each Evolution:

- respects its enable state
- requires the stated Chaos threshold
- uses dynamic pacing unless a valid pre-fire evolved opening applies
- records one evolution log entry when its changed behavior first becomes real
- adds zero Chaos merely for activating
- has a safe baseline route when disabled
- does not retroactively undo wars or countries that already exist

The shared evolution context uses Event ID `45`, a distinct type for each track, stage `1`, and the relevant actor when one country owns the milestone.

## Evolution I: The Old Borders Return

- Chaos requirement: `200+`
- Main change: broader historical claim families become available
- Base pacing target: about `100` days after eligibility when not seeded into the opening
- Public proof: the first broader Evolution I claim is formally activated

### Design purpose

Baseline claims stay close to the opening dispute and immediate neighboring interests. Evolution I allows governments to treat the war as a chance to reopen a larger regional settlement. The war can then involve Transylvania, Banat, Bačka, a broader Macedonian division, wider Thracian access, or other maintained historical groups that were not necessary to start the conflict.

### Eligibility pressure

The Evolution becomes more likely when:

- the war has lasted long enough for the opening objective to lose control of diplomacy
- a belligerent occupies a registered broader claim
- several governments have active but incompatible interests
- a settlement conference fails
- a neutral Balkan country sees its registered interest occupied
- an Event 048 Bulgarian route or another owner system has already revived a broader claim

It becomes less likely when:

- an armistice line is holding
- the opening dispute has been settled
- few valid broader claims remain
- major powers are cooperating on containment

### Pre-fire evolved opening

At `200+` Chaos, the opening dispute pool may include one valid Evolution I claim family. If selected, the Evolution logs during the opening and broader claims are available from the first day.

The evolved opening does not grant every claim in the registry. It selects one broader dispute with current geographic proof.

### Gameplay changes

- A bounded set of broader claim decisions becomes available.
- Neutral regional countries gain stronger intervention interest when an active belligerent occupies or claims one of their registered zones.
- Settlement conferences can redraw a larger part of the region.
- Allied occupation disputes become more common.
- Outside powers can recognize or oppose broader claims.
- The claim cap remains bounded by country role, war size, and settlement viability.

### Disabled behavior

When Evolution I is disabled, Event 045 uses only the opening dispute, immediate adjacent claims, and claims already owned by another active system. Baseline settlement remains complete.

## Evolution II: Balkanization

- Chaos requirement: `400+`
- Main change: genuinely weakened participants can fragment into viable breakaways, mutinies, or civil wars
- Base pacing target: about `120` days after at least one viable fragmentation candidate exists
- Public proof: the first validated breakaway, mutiny government, or civil-war front appears

### Design purpose

The Evolution represents internal collapse caused by the war. It never creates a country because a random timer expired while the participant remained stable.

### Fragmentation pressure

Each active participant may accumulate hidden pressure from:

- military casualties relative to fielded manpower
- loss of the capital
- share of core or owned territory occupied
- prolonged low stability
- broken supply and lost strategic corridors
- prolonged fighting
- mutiny or ideological conflict
- denied regional autonomy or suppressed independence memory
- a failed armistice or settlement that delegitimizes the government

Pressure falls when the country retakes its capital, restores supply, wins a major front, raises stability, or reaches a credible settlement.

### Candidate proof

A fragmentation incident requires:

- a valid state group with population and connected territory
- a valid capital candidate
- a release, civil-war, or claimant identity from an existing provider package
- enough manpower and equipment for a viable force
- supply access or a defined emergency support route
- a legal diplomatic relationship to the host and current camps
- a cleanup and rollback route

When no provider package can create a viable actor, that candidate is skipped. Implementation must not substitute an empty generic tag.

### Outcome families

#### Separatist uprising

A regional movement seizes a viable group of states and chooses a camp, independence, or a local defensive war according to claims and sponsors.

#### Regional breakaway government

An administrative region, former constituent state, or occupied frontier forms a government with a defined capital, army, and political origin.

#### Military mutiny

Units and a connected territorial base defect. The resulting actor may align with a camp or fight for a separate settlement.

#### Ideological revolt

A political movement creates a civil-war front when ideology and internal legitimacy support it. Ideology alone is not enough without territory and military proof.

#### Independence movement

The event requests a suitable Independence Wave package. Existing independence memory affects identity, support, and foreign recognition.

### Alignment

A new actor can:

- join the camp whose sponsor or claim supports it
- remain independent and defend its own territory
- attack the weakened host while avoiding the other camp
- open an additional front against a rival claimant

The alignment decision uses survival, sponsor, ideology, claims, and current occupation. It should not always choose the strongest camp.

### Pre-fire high-Chaos behavior

At `400+` Chaos, fragmentation pressure is active from the opening. The Evolution does not log and no breakaway appears until real weakening evidence and pacing requirements are met.

### Disabled behavior

When Evolution II is disabled, Event 045 makes no fragmentation requests. Ordinary civil wars, Independence Wave outcomes, and existing country mechanics remain free to operate through their own systems.

## Evolution III: War of All Against All

- Chaos requirement: `600+`
- Main change: opening camp structures can fracture over incompatible claims, occupation, ideology, sponsors, and regional dominance
- Base pacing target: about `90` days after a valid fracture condition exists
- Public proof: the first former allies enter a new linked war against each other

### Design purpose

Evolution III makes alliance membership conditional. It does not turn every ally into an enemy. A fracture requires a real conflict that the camp can no longer contain.

### Incompatibility sources

A camp gains hidden incompatibility from:

- two members claiming the same state group
- one member occupying another member's principal objective
- refusal to adjust an allied occupation
- incompatible settlement terms
- severe ideology conflict
- one member seeking regional dominance over another
- different outside sponsors backing competing partners
- a broken promise to transfer a corridor or capital region
- a separate Allies Backstab or faction rupture that changes the camp structure

Cohesion improves when claims are waived, occupation disputes are settled, sponsors coordinate, or a common enemy remains an immediate existential threat.

### Eligibility proof

A fracture requires:

- a camp with at least two surviving members
- one unresolved incompatibility source
- a legal war edge between the former allies
- viable forces and territory on both sides
- no active settlement that has already resolved the dispute

A camp cannot fracture merely because the Evolution timer completed.

### Fracture outcomes

#### Limited former-ally war

Two members fight over a named claim or occupation while remaining at war with the original enemy.

#### Camp split

Several countries divide into successor camps. Existing outside sponsors choose which relationships to preserve.

#### Three-sided regional war

The original two-camp structure becomes a three-sided linked war graph.

#### Full war of all against all

Every remaining camp has a valid hostility edge against every other camp. This outcome is reserved for severe overlapping claims and high Chaos. It is not the default Evolution result.

### Foreign sponsor behavior

Outside sponsors may:

- maintain support for one former ally
- divide support among successors
- suspend aid and pursue containment
- use the split to invite one successor into a faction
- intervene directly when a sponsored occupation is threatened

Sponsor choices can raise or lower Balkan War Escalation through the ordinary commitment rules.

### Pre-fire high-Chaos behavior

At `600+` Chaos, the opening builder may favor a justified three-sided conflict and begins camps with lower hidden cohesion. The Evolution still logs only when former allies actually fracture. A three-sided opening caused by pre-existing rival claims does not count as a former-ally fracture unless countries first belonged to the same camp.

### Disabled behavior

When Evolution III is disabled, Event 045 does not create new former-ally wars. Allied occupation disputes can still damage relations and settlements. Allies Backstab remains independent.

## Evolution ordering

The Evolutions can overlap but do not require strict linear activation.

- Evolution I can create the conflicting claims that later make Evolution III possible.
- Evolution II can create new actors that join camps or become independent sides.
- Evolution III can occur without Evolution II when ordinary countries have incompatible claims.
- Evolution II can occur without Evolution I when a country collapses under the baseline war.

Each Evolution logs separately and keeps its own enable state.

## Evolution aftermath

Evolution state persists only as long as its consequences need it.

- Activated broader claims remain available to settlement and postwar memory.
- Breakaway countries remain ordinary countries after creation and use provider-owned cleanup.
- Former-ally wars remain ordinary wars after the event hands off.
- Temporary pressure and eligibility variables clear when the event generation closes.

---

## Included file: `specs/045_third_balkan_war_spec_part_6_ai_achievements_assets.md`

# Event 045 AI, balance, achievements, assets, and writing direction

## AI goals

AI should make the event dangerous without behaving as if escalation is always the correct choice.

Regional AI tries to secure its principal objective, preserve the capital and supply network, obtain useful support, and avoid a settlement that destroys its viability. Outside AI chooses between containment and exploitation according to strategic interest and current capability.

Every weighted surface requires a dedicated probability audit before and after implementation changes.

## Regional AI factors

Regional countries consider:

- principal and secondary claim value
- relative army strength
- manpower and equipment reserves
- supply access and rail control
- capital safety
- current war support and stability
- number of fronts
- surrender progress
- available sponsors
- faction and guarantee ties
- ideology and strategic posture
- prior peace and claim memories
- escalation stage
- enabled Evolutions
- The Offensive and other aggression modifiers

Balkan AI is more willing than normal to call allies, activate a valid claim, accept material support, and intervene when its own registered interest is threatened. It is not more willing to commit suicide.

A country near defeat should accept a settlement that preserves government viability when no credible rescue exists. A country with a supplied army, a secure capital, and an imminent sponsor may continue fighting.

## Outside AI factors

Outside powers consider:

- ideology and relations with each camp
- faction and guarantee commitments
- rival powers already supporting the opposite camp
- strategic access to ports, railways, the Straits, or the Mediterranean
- distance and theater reach
- navy, air, convoy, fuel, and equipment capacity
- current war load
- stability and war support
- escalation stage and irreversible floor
- likelihood that containment partners will cooperate
- whether direct intervention creates a new major-power war

Containment becomes more likely when the outside power has limited regional interests, is overextended, faces high escalation, or has credible partners for a conference. Exploitation becomes more likely when a rival has committed first, a guarantee is meaningful, access is available, and the preferred camp can survive.

## AI hard blocks

AI must not:

- select a dead or invalid target
- support a camp that no longer exists
- send aid without a viable route
- guarantee a country it cannot plausibly defend
- invite a country into a faction when ordinary faction rules reject it
- create an opening war between same-faction allies
- activate a disabled Evolution path
- demand an unregistered territorial claim
- reject peace indefinitely after complete military defeat
- trigger direct intervention without forces, access, or war support
- treat special Chaos or nonhuman actors as ordinary Balkan governments

## Balance principles

### Opening viability

The opening should be coherent and survivable, not equal. The camp builder may apply a short event-owned mobilization package only when a valid small country would otherwise enter with no usable force. Such support must scale from its territory, manpower, industry, and opponents. It must not be a free army reward detached from the war.

### Escalation anti-farming

- Aid uses cumulative support tiers.
- Entry, guarantee, faction, and intervention sources record one-shot proofs.
- Repeated opening and closing of transit cannot farm gains or losses.
- A broken armistice records one violation per country and armistice generation.
- Stage reports fire once per upward threshold.
- Maximum stage is stored separately from current stage.

### Decision impact

Every major action changes a campaign choice, map objective, support relationship, settlement term, or escalation state. Tiny isolated modifiers do not count as complete actions.

### Event duration

The event can resolve quickly when one camp collapses or a credible conference succeeds. It can remain active for years when it becomes a wider war. There is no fixed total timer.

### Performance

Processing should be event driven through registered participants, sponsors, claims, and active missions. Do not scan every country every day. Use bounded pulses and owner-local hooks for facts that cannot be captured directly.

## Achievement set

All names below are working labels. Final wording must follow the achievement localisation style and source rules.

### `chaosx_achievement_045_keep_it_regional`

- Working label: Keep It Regional
- Eligible player: original Balkan participant
- Unlock: reach a settlement with the player's government independent and not defeated, maximum escalation below European Crisis, no direct outside-major entry, and at least three opening participants
- Disqualifiers: Force Trigger Mode where achievements are disabled, player changes away from the tracked country, subject status at settlement, or invalid event generation
- Difficulty: Medium
- Why it is not trivial: the player must win or compromise before foreign commitments cross the first outside-power threshold
- Icon direction: a contained flame inside a Balkan frontier outline, designed as a 64x64 achievement image

### `chaosx_achievement_045_the_conference_holds`

- Working label: The Conference Holds
- Eligible player: outside power that was not an opening participant
- Unlock: the conflict reaches European Crisis, the player leads or materially supports a containment conference with at least two cooperating outside powers, an armistice-line mission succeeds, and no hostile major-power pair enters direct war
- Disqualifiers: player directly joins a linked war, player sends an exploitative military commitment after the conference begins, or armistice failure
- Difficulty: Hard
- Icon direction: a conference table holding down a burning border map without generated text

### `chaosx_achievement_045_every_map_is_temporary`

- Working label: Every Map Is Temporary
- Eligible player: original Balkan participant
- Unlock: Evolution I activates, the player settles at least two registered claims through a negotiated or imposed regional settlement, no acquired state lies outside the maintained claim registry, and the event does not reach Another World War
- Disqualifiers: unregistered annexation by the player, event handoff before regional settlement, or player government destruction
- Difficulty: Hard
- Icon direction: layered treaty maps with two clearly different border lines and a wax seal

### `chaosx_achievement_045_no_friends_left`

- Working label: No Friends Left
- Eligible player: original participant that began with at least one camp ally
- Unlock: Evolution III creates a war against a former ally, the player survives independent with its capital, and the event reaches a settlement or wider-war handoff while the player remains active
- Disqualifiers: player becomes a subject, loses its capital permanently before resolution, or never enters the former-ally war
- Difficulty: Hard
- Icon direction: two broken alliance clasps around one surviving flagpole with no actual national flag

### `chaosx_achievement_045_a_very_small_incident`

- Working label: A Very Small Incident
- Eligible player: original participant in an absurd-frontier-incident opening
- Unlock: Event 045 becomes the verified origin of Another World War and the player survives for a defined post-handoff period
- Disqualifiers: pre-existing global war blocks origin proof, player country is annexed, or the opening cause was not the absurd incident family
- Difficulty: Very Hard
- Icon direction: a tiny broken border marker casting an oversized world shadow

### `chaosx_achievement_045_the_entente_reversed`

- Working label: The Entente Reversed
- Eligible player: Balkan participant or regional mediator
- Unlock: a settlement is signed by at least four surviving Balkan governments, at least two signatories began on opposing camps, every signatory remains independent, and none is annexed through the settlement
- Disqualifiers: fewer than four valid signatories, annexation of a signatory, or world-war handoff before agreement
- Difficulty: Hard
- Icon direction: four distinct hands around a Balkan pact document, no readable generated text

Each achievement requires tracking, localisation, three achievement-state assets where the engine pattern requires them, docs, and completion audit.

## Asset inventory

### Super-event images

1. Opening outbreak image
2. Another World War handoff image

The second image is used only when the final stage proof is met.

### Report and news images

- additional Balkan entrant
- foreign arms and volunteers
- guarantee or faction enforcement
- direct major intervention
- armistice or settlement

A smaller reusable report family may be used when the images remain distinct enough to communicate the stage cause.

### Decision category picture

One static picture showing a Balkan frontier rail junction, crowded mobilization, border barriers, and a visible route toward a port or mountain pass. It must contain no fake controls, meters, or generated text.

### Decision and mission icons

- regional claim
- arms shipment
- volunteers or military mission
- strategic corridor
- mediation
- armistice
- allied occupation dispute
- regional mobilization
- transit access
- guarantee
- faction invitation
- sanctions
- direct intervention
- rail-line mission
- port-corridor mission
- armistice-line mission
- Straits mission

Each icon family is designed for its own consumer. Decision and mission icons are not resized achievement art.

### Achievement icons

Six independent 64x64 completed icons plus the required grey and not-eligible variants according to the current achievement consumer.

## Asset source direction

The opening and report art may use sourced period photographs when the subject is real historical mobilization, diplomacy, or frontier activity. A fictional alternate-history composition may use generated 1936-1945 documentary-style art. The source mode must be recorded for each image.

Icons use native transparent ImageGen output and preserve alpha. The category picture and super-event scenes use the full-canvas treatment required by their inspected consumers.

No visual should joke about casualties. The restrained humour belongs in the recurrence and diplomatic framing.

## Super-event writing direction

### Opening

- Viewpoint: Europe learns that several Balkan armies are already moving
- Visible facts: regional camps, mobilization, frontier claims, and foreign governments watching
- Tone: restrained dark humour followed by immediate seriousness
- Uncertainty: whether outside powers will contain or exploit the war
- Avoid: generic map-change language, jokes about victims, and unsourced famous quotations

### Another World War

- Viewpoint: the regional origin has become a multi-major or multi-faction conflict
- Visible facts: direct major-power war and fronts outside the original theater
- Tone: grave and concise
- Uncertainty: none about the scale, but the eventual settlement remains open
- Avoid: treating the result as a terminal world end

The often-attributed Bismarck remark about a foolish event in the Balkans is not approved as a final quote because its provenance is uncertain. A text researcher may reconsider it only after finding a reliable original source. The final quote, cultural remark, and button wording require separate research.

---

## Included file: `diagrams/045_third_balkan_war_lifecycle.md`

# Event 045 lifecycle diagram

```text
Automatic selection or manual event test
                |
                v
      Valid multi-country map?
          |             |
         no            yes
          |             |
      Show N/A          v
                   Build regional pool
                         |
                         v
                 Select dispute family
                         |
                         v
                 Select initiator and camps
                         |
                         v
               Validate linked war graph
                    |            |
                   fail         pass
                    |            |
                 rollback        v
                         Start linked wars now
                                 |
                                 v
                     Record opening and show
                         outbreak super-event
                                 |
                                 v
                 Role-aware decisions and missions
                                 |
       +-------------------------+--------------------------+
       |                         |                          |
       v                         v                          v
 Regional claims          Foreign commitments       Armistice work
       |                         |                          |
       +-------------------------+--------------------------+
                                 |
                                 v
                    Balkan War Escalation changes
                                 |
          +-----------+----------+-----------+-----------+
          |           |                      |           |
          v           v                      v           v
       regional   European Crisis       Powder Keg   World War proof
       victory          |                      |           |
          |             |                      |           v
          |             |                      |      Handoff to normal
          |             |                      |      war and faction logic
          |             |                      |
          +-------------+----------------------+
                                 |
                                 v
                 Settlement, ceasefire, or continuation
                                 |
                                 v
                    Cleanup temporary event state
                                 |
                                 v
                      Preserve approved memories
```

## Evolution overlays

```text
Chaos 200+ and broader valid claim
                -> Evolution I: The Old Borders Return

Chaos 400+ and a genuinely weakened participant
                -> Evolution II: Balkanization

Chaos 600+ and unresolved allied incompatibility
                -> Evolution III: War of All Against All
```

The Evolutions can overlap. None replaces the escalation stages.

---

## Included file: `diagrams/045_third_balkan_war_escalation_map.md`

# Balkan War Escalation map

| Stage | Numeric range | Required proof | Main new actions | Exit route |
| --- | --- | --- | --- | --- |
| Balkan Conflict | `0-24` | Opening linked wars | principal claim, corridor mission, arms request, local arbitration | decisive victory or early armistice |
| The Balkans Are on Fire | `25-44` | wider regional participation or several real fronts | neutral intervention, secondary claim, regional mobilization | regional conference or military settlement |
| European Crisis | `45-64` | material outside commitments | containment coalition, sanctions, volunteers, guarantees, faction pressure | coordinated withdrawal or imposed armistice |
| The Powder Keg Explodes | `65-84` | opposing majors or major-led factions in direct war | direct-intervention management, reduced regional settlement controls | wider European peace or further spread |
| Another World War | `85-100` | global-war proof | regional actions close except essential claim and survival state | normal world-war systems own continuation |

## Irreversible floors

```text
Outside major enters directly
    -> escalation cannot fall below European Crisis

Opposing majors or major-led factions fight directly
    -> escalation cannot fall below The Powder Keg Explodes

Another World War proof met
    -> stage locks and Event 045 hands off
```

## Anti-farming structure

```text
Aid clicks -> hidden cumulative sponsor-to-camp support -> bounded support tiers -> escalation only on tier crossing

Guarantee -> one proof record -> escalation once when enforced

Faction entry -> one entrant record -> escalation once

Armistice -> one generation -> one violation record per country
```

---

## Included file: `diagrams/045_third_balkan_war_decision_map.md`

# Event 045 decision map

## Regional belligerent phase

```text
Current role and stage
        |
        +-> Formalize one valid claim
        +-> Request foreign arms
        +-> Secure one strategic corridor mission
        +-> Offer or answer armistice terms
        +-> Resolve allied occupation when relevant
```

## Neutral Balkan phase

```text
Registered regional interest
        |
        +-> Mobilize named frontier
        +-> Offer arbitration
        +-> Open or close named transit route
        +-> Demand neutrality guarantees
        +-> Join a compatible camp when proof exists
```

## Outside containment phase

```text
Reach and diplomatic access
        |
        +-> Convene conference
        +-> Coordinate arms suspension
        +-> Pressure guarantee withdrawal
        +-> Establish armistice line
        +-> Apply coordinated sanctions
```

## Outside exploitation phase

```text
Preferred camp and viable route
        |
        +-> Send weapons shipment
        +-> Dispatch volunteers
        +-> Recognize one registered claim
        +-> Issue guarantee
        +-> Invite to faction
        +-> Prepare direct intervention
```

Only relevant actions appear. The category does not show every row in all four phases at once.

---

## Included file: `diagrams/045_third_balkan_war_claim_registry_map.md`

# Event 045 claim registry design map

| Registry layer | Purpose | Public effect |
| --- | --- | --- |
| Geographic state group | Exact current map states and adjacency | names the claim and settlement area |
| Interested actor family | identifies valid claimant and successor families | controls who may register an interest |
| Baseline dispute flag | makes the group eligible for opening or immediate adjacent claims | enables early objectives |
| Evolution I flag | marks broader historical ambitions | enables wider claims after Evolution I |
| Conflict set | records overlapping claimants | affects camps and Evolution III |
| Settlement modes | transfer, corridor, access, demilitarization, subject, unresolved memory | bounds postwar results |
| External owner link | points to another event that already owns the claim | prevents duplicate grants and rewards |

## Implementation map rule

The state groups must be built from installed map data and inspected with the HOI4 map tools. Working historical names in the spec are not state IDs. Every claim helper, tooltip, decision, settlement check, and AI target must use the same maintained state-group definition.

---

## Included file: `research/045_third_balkan_war_research_notes.md`

# Event 045 historical and regional research notes

## Research purpose

The research identifies concrete regional patterns that can sharpen the event. It does not require the alternate-history war to reproduce one historical conflict exactly.

## The Second Balkan War as the main structural precedent

The strongest precedent is the collapse of a recent coalition into war among former allies. The First Balkan War drove the Ottoman Empire from most of its European territory. The Second Balkan War followed when former allies fought over the settlement, especially Macedonia. Romania and the Ottoman Empire entered while Bulgaria was already fighting Serbia and Greece.

Design use:

- the opening can begin with a coherent coalition history but incompatible territorial aims
- the event needs a real former-ally fracture path
- Romania or another regional country can enter opportunistically after the front has weakened a belligerent
- occupation and settlement claims should matter as much as the opening cause

## Macedonia as a multi-claim region

Macedonia was divided among competing state projects and remained central to Bulgarian, Serbian or Yugoslav, Greek, and Albanian political questions. The dispute was never a simple two-country border problem.

Design use:

- Macedonian claims are the strongest normal three-sided opening family
- one side may seek territory, another strategic access, and a third protection of a current settlement
- Evolution I can reopen a wider division without granting every claimant the same objective

## Albania, Adriatic access, and Great Power limits

Serbia's movement toward the Adriatic during the First Balkan War was blocked by Great Power support for an Albanian state. Recent research also emphasizes that Albanian statehood was recognized while borders excluded many Albanian-populated areas and severed social and economic ties.

Design use:

- access to the Adriatic or a protected Albanian border can become an opening cause
- outside powers may support a state for reasons that differ from the local claimant's goals
- settlement can use corridor access or guarantees instead of simple annexation

The event should avoid converting ethnic history into automatic claims. Current country borders, active political claims, and campaign context remain required.

## Southern Dobruja

Southern Dobruja changed hands after the Second Balkan War and returned to Bulgaria under the 1940 Treaty of Craiova. The settlement also involved forced population exchange.

Design use:

- Bulgarian-Romanian rivalry has a concrete registered claim family
- a negotiated territorial settlement can be plausible
- population consequences belong to the shared migration system, not a flat Event 045 transfer effect

## Trianon revisionism

The Treaty of Trianon removed Transylvania, Banat, Bačka, and other territories from Hungary and sharply restricted the Hungarian military.

Design use:

- Hungarian-Romanian and Hungarian-Yugoslav claims fit Evolution I
- Banat can produce a three-way interest graph involving Hungary, Romania, and a Yugoslav actor
- outside powers may treat Hungarian intervention as part of a wider revisionist crisis

The spec does not assume every Hungarian government pursues every claim. Ideology, strategy, current borders, and prior settlements shape activation.

## Balkan Entente as containment precedent

Greece, Romania, Turkey, and Yugoslavia signed the Balkan Entente in 1934 to protect territorial integrity and the regional status quo. Bulgaria and other revisionist states remained outside the arrangement.

Design use:

- regional countries can cooperate on containment even when they have other rivalries
- an outside or regional conference should become stronger when several governments coordinate
- containment can involve guarantees, arms suspension, observation, and joint pressure rather than one instant peace decision
- the achievement set can reward a multi-state settlement that preserves independent governments

## Incident at Petrich

A Greek-Bulgarian border crisis in 1925 led to a brief Greek incursion and League of Nations intervention. Popular accounts include a stray dog, while other accounts describe a direct border-post clash. The origin story is disputed.

Design use:

- an absurd or trivial frontier incident can trigger the opening without making the underlying claims absurd
- the line-holding and outside-observer missions have a historical analogue
- the event can use irony about the small incident and the large consequence

Source caution:

- do not present the dog story as certain fact
- do not treat the incident as bloodless
- use a researched final cultural remark rather than a copied meme

## Balkan crises and wider alliance escalation

The 1912-1913 crisis altered Great Power alignments and contributed to the strategic context of 1914. Regional territorial ambitions and failed mediation could force outside patrons to choose between credibility and restraint.

Design use:

- the event should model guarantees, sponsors, and faction commitments as actions that can convert regional war into direct major conflict
- failed mediation should change later willingness and claims
- the world-war handoff requires actual major-power linkage, not only a high number

## Historical restraint

The event should not suggest that Balkan peoples are naturally inclined toward war. It models governments, claims, security arrangements, alliances, military opportunities, and failed settlements.

Atrocities, forced migration, famine, chemical warfare, and other severe consequences remain with their shared systems and are not used as cheap regional flavour.

## Research questions for implementation

1. Which exact installed HOI4 state groups best represent each claim family?
2. Which Yugoslav successor providers already exist in the repository and can be reused safely?
3. Which claims are already owned by Event 048 or another implemented route?
4. Which vanilla and Chaos Redux peace effects can deliver corridor access, demilitarization, and bounded transfer cleanly?
5. Which sourced period images have clear rights for the super-event and category picture?
6. Which verified quote and public-domain or clearly licensed recording fit each super-event role?

---

## Included file: `research/045_third_balkan_war_bibliography.md`

# Event 045 research bibliography

Access date for web sources: 2026-08-31.

## Strong design sources

### Richard C. Hall, Balkan Wars 1912-1913

- Publisher: 1914-1918 Online, International Encyclopedia of the First World War
- URL: https://encyclopedia.1914-1918-online.net/article/balkan-wars-1912-1913/
- Use: structure of the First and Second Balkan Wars, Macedonia, Southern Dobruja, former allies, Romanian and Ottoman entry, wider Great Power consequences
- Confidence: High

### Yugoslavia: A Country Study

- Publisher: Library of Congress Federal Research Division
- URL: https://tile.loc.gov/storage-services/master/frd/frdcstdy/yu/yugoslaviacountr00curt_0/yugoslaviacountr00curt_0_djvu.txt
- Use: Balkan League, Serbian movement toward the Adriatic, Albanian state formation, Macedonia, Yugoslav regional background
- Confidence: High

### Historical Documents, Office of the Historian

- Publisher: United States Department of State
- URL: https://history.state.gov/historicaldocuments/frus1969-76v39/d142
- Use: concise identification of the 1934 Balkan Entente members and its territorial-integrity purpose
- Confidence: High for the cited note

### The Balkan Entente in Turkish-Yugoslav Relations, 1934-41

- Publisher: JSTOR record for a peer-reviewed article
- URL: https://www.jstor.org/stable/44157737
- Use: regional containment and status-quo diplomacy
- Confidence: High for bibliographic identity, article access may require a subscription

### Treaty of Trianon

- Publisher: European Network Remembrance and Solidarity
- URL: https://enrs.eu/article/anniversary-of-the-treaty-of-trianon
- Use: territorial and military consequences affecting Transylvania, Banat, Bačka, and Hungarian revisionism
- Confidence: Medium to High

### The Albanians, the First Balkan War, and the Decisions of the London Conference of 1912-1913

- Authors: Ethem Çeku and Sedat Baraliu
- Publisher: SAGE Journals
- DOI page: https://journals.sagepub.com/doi/10.1177/02656914251401388
- Use: Albanian statehood, excluded populations, severed regional ties, and Great Power diplomacy
- Confidence: High

### Report of the International Commission to Inquire into the Causes and Conduct of the Balkan War

- Publisher: Carnegie Endowment for International Peace, 1914
- Archive: https://archive.org/details/reportofinternat00inteuoft
- Use: contemporary inquiry and caution against turning wartime harm into humour
- Confidence: High as a contemporary commission report, interpretation still requires care

### The Balkan Wars, 1912-1913

- Author: Jacob Gould Schurman
- Project Gutenberg: https://www.gutenberg.org/files/36192/36192-h/36192-h.htm
- Use: contemporary diplomatic settlement details and territorial questions
- Confidence: High as a period work, perspective and terminology require contextual reading

### The 1912/13 Balkan Crisis, Prelude to World War

- Publisher: Habsburg history portal
- URL: https://ww1.habsburger.net/en/chapters/191213-balkan-crisis-prelude-world-war
- Use: persistent regional expansion pressure and Great Power misreading
- Confidence: Medium to High

## Focused supporting sources

### Treaty of Craiova and Southern Dobruja

- Bulgarian National Radio archive: https://old-news.bnr.bg/en/post/100437047/bnr-80-years-in-80-yeeks-treaty-of-craiova-and-return-of-south-dobruja
- Supporting academic article: https://journals.bsu.by/index.php/history/en/article/view/5825
- Use: return of Southern Dobruja and forced population exchange
- Confidence: Medium to High

### Incident at Petrich

- Cambridge archival record: https://archivesearch.lib.cam.ac.uk/repositories/9/archival_objects/478646
- Bulgarian News Agency retrospective: https://www.bta.bg/en/news/archives/990234-october-19-1925-border-incident-near-petrich-leads-to-greek-incursion-into-bul
- Recent scholarly summary: https://journals.rcsi.science/0869-544X/article/view/430858
- Use: border incident, League intervention, ceasefire, withdrawal, and compensation
- Confidence: Medium to High for the crisis and settlement
- Caution: the stray-dog origin story has competing accounts and is not treated as settled fact

### Balkan Entente treaty background

- Center for Eurasian Studies analysis and treaty discussion: https://avim.org.tr/en/Analiz/1934-PACT-OF-BALKAN-ENTENTE-THE-PRECursor-OF-BALKAN-SOUTHEAST-EUROPE-COOPERATION
- Use: treaty text context and regional cooperation
- Confidence: Medium

## Rejected or restricted quote direction

The line commonly attributed to Otto von Bismarck about a foolish event in the Balkans was not verified to a reliable original source during this planning pass. It is not approved as final super-event text. A later text researcher may use it only after finding defensible primary or scholarly provenance.

---

## Included file: `research/045_third_balkan_war_source_manifest.md`

# Event 045 source-reading manifest

This manifest records every supplied project source and every archived subagent definition processed before the Event 045 specification was written.

## Reading result

- Total records: `42`
- Supplied project files outside the archive: `22`, including the subagent archive itself
- Archived subagent definitions: `20`
- Project Markdown, TOML, and CSV source files read in full: `21`
- Archive definitions read in full: `20`
- Unread supplied files: `0`

The ZIP container is listed as a supplied record. Its 20 TOML members are also listed individually because their full contents were extracted and read.

## Files

| # | Source path | Bytes | Lines | SHA-256 |
| --- | --- | ---: | ---: | --- |
| 1 | `chaosx_dynamic_triggers.md` | 3,935 | 61 | `7f6733ef08b816c38aba6d5c675f98c054e9167accd5be3bdf536b65bb60291e` |
| 2 | `chaosx_dynamic_effects.md` | 14,618 | 280 | `2ed4e8f3d220d7d09fd32eabe5e2d35226816d417dbbc11a9635758080bccdf7` |
| 3 | `CHAOS_REDUX_MECHANICS(9).md` | 71,678 | 1164 | `f3a4276d534056b5349c17e029df8f0821dd2b7728237af07d377375a3c38291` |
| 4 | `chaos_redux_clusters_catalog(4).csv` | 2,836 | 14 | `ae37b095ccf1e264397284b1c9e2e9184433e75c5bb6957ef50ea14cef1c63f7` |
| 5 | `chaos_redux_scenarios_catalog(4).csv` | 12,239 | 56 | `0704f9c5a77b6c1bb06f5eead93eb9e130986718763ed7cc212225fc84e22ce2` |
| 6 | `chaos_redux_events_catalog(4).csv` | 52,722 | 252 | `a2d1edcd12a2891eb4b9040139447993f0657af93b166fa0ddd4a1b1186a6fbf` |
| 7 | `chaos-redux-improvement-loop.md` | 27,478 | 287 | `dd1cea075f7d76a5a0c1c8a55ce65bc69d677afd3010cf51d42baa39054cfa53` |
| 8 | `AGENTS(10).md` | 43,195 | 417 | `5fd1111fc9acb189987b5d11b371a1d4202f63c91f5d9487f6408515321d7567` |
| 9 | `chaos-redux-subagents(1).md` | 36,164 | 357 | `ff5e08f96238d5cc3a353fd71253252e7f06d638f4261a6715bbb16d7d6ede9d` |
| 10 | `config(2).toml` | 11,385 | 189 | `df72462c8abcafffeb8250bcd5934680928604a4c64181bd401340c57f508adb` |
| 11 | `chaos-redux-decisions-missions(1).md` | 74,499 | 1166 | `8503d548c92d96ffa4419e760045d726201a69fa78a4a55a87087d855b1af5a5` |
| 12 | `chaos-redux-event-assets.md` | 124,623 | 1519 | `7c15faa859cd40540cd1d64a00ff2112d68327aa37ae8dbe762763e5ba405cc8` |
| 13 | `chaos-redux-3d-model-pipeline.md` | 87,136 | 413 | `ced1ca88126e46f860d55abb66d5507c48aa40b9687715855497e8b0cf71a377` |
| 14 | `chaos-redux-events(1).md` | 72,941 | 804 | `91463e91407af1fe88358050729cb247793f004ac96e890e3ff659c455b85714` |
| 15 | `chaos-redux-comfyui.md` | 2,123 | 16 | `128acd133fedc56b14612eed163de11d7261dac887f11eacf4c8b695dae97fa0` |
| 16 | `chaos-redux-debug-playtest.md` | 30,145 | 666 | `ec9d66e433e9d964a2561844aa45281342842b973e059a09fab18f2107283a43` |
| 17 | `chaos-redux-focus-trees.md` | 98,154 | 1503 | `51f741f8abde30c7772be46072fa4530361dcf4fc348da97b69c86206761789b` |
| 18 | `chaos-redux-frame-animation.md` | 27,086 | 495 | `a8dd6bdcec2b849c6f5c85abffb863510a5585418f2e608c713c8ba83154aa48` |
| 19 | `chaos-redux-super-events.md` | 33,028 | 793 | `d7afffcf25b70333fd50aaef1f72378c1c270b8057269597f085c96204e01607` |
| 20 | `README(20260830-071218).md` | 2,351 | 37 | `bb4b9587eddce00479b5792a7897dbe6f41cc48c5a46fe67b2e129dafbaf8978` |
| 21 | `chaos-redux-event-planning(1).md` | 195,156 | 2277 | `09a18e704984a9d08cb20851f6599acc494ff1939016e384fd049c3b3c412464` |
| 22 | `subagents(4).zip` | 59,612 | n/a | `799dfd4e95715d0840b90009558e4d719e2f42eba16db4a258644bc990bd796d` |
| 23 | `subagents_extracted/chaosx_3d_model_pipeline.toml` | 24,375 | 187 | `235cb326978966a6b284c64dd0dfe8acf9d2be668393b8122c5e37b88875cb92` |
| 24 | `subagents_extracted/chaosx_ai_probability_auditor.toml` | 6,348 | 66 | `20336a1ec04210d7f468e364fa48ca59427a5fa1292e8765af9eb746a73e6856` |
| 25 | `subagents_extracted/chaosx_asset_source_researcher.toml` | 3,017 | 58 | `4db7e102822821201eb80055d45ad89272de7cdc4c6c695953d45854bd0e8df6` |
| 26 | `subagents_extracted/chaosx_country_package_auditor.toml` | 7,965 | 87 | `b140694067beb96d77ab31f6bf1eaa595eff02cf6ae83ce33e50e7ef2bedece4` |
| 27 | `subagents_extracted/chaosx_decision_mission_auditor.toml` | 8,443 | 99 | `b8d579a9aec9fae7f9a6c5a291976660460ee8a3f1b69e8ef77af70535315433` |
| 28 | `subagents_extracted/chaosx_documentation_curator.toml` | 10,140 | 131 | `8aea5aad0f4c5350013377041e57029d3cd296774a6713977f2e34cccf533885` |
| 29 | `subagents_extracted/chaosx_event_completion_auditor.toml` | 4,117 | 66 | `59cbca30c23cd810ac31618eb0ece7a1280455b641096dd2c701e680b261aaee` |
| 30 | `subagents_extracted/chaosx_event_ui_worker.toml` | 10,720 | 84 | `4afc059508881379bc272bbfac519ddbbe0c448c1fa5f46626cd78fd459f736d` |
| 31 | `subagents_extracted/chaosx_focus_tree_auditor.toml` | 4,499 | 80 | `83149977d6749cfe743d8ec4c2afa769a019dbfbbc8fd62390460b3629f444e3` |
| 32 | `subagents_extracted/chaosx_generated_event_art.toml` | 3,909 | 72 | `f7c85c45acf334f76b93ed95409b0165affdc801fea6dd1094651533d89ae3ea` |
| 33 | `subagents_extracted/chaosx_icon_artist.toml` | 7,611 | 104 | `1afbd89167f2dab6bba6271d2da7523c923a5faba495dbeedde43950af70c0f7` |
| 34 | `subagents_extracted/chaosx_improvement_loop_planner.toml` | 7,069 | 61 | `a90323b1cbbd664fa61e245186fe7dd912498018e07f3e2393e2641555fbd2bf` |
| 35 | `subagents_extracted/chaosx_localisation_auditor.toml` | 9,109 | 108 | `f754134bb8df4ec8c99a50c3de69eda2c2b6a211a026aae396af600f224bf30e` |
| 36 | `subagents_extracted/chaosx_portrait_creator.toml` | 2,029 | 20 | `87b001c6fb5afc33267eb77a3187ff654dbf6b03ae5d669cb2d5182bf7ac2174` |
| 37 | `subagents_extracted/chaosx_repo_explorer.toml` | 12,690 | 234 | `3b7380b83e0dd6bba741b5c5cd5419e3e5bf22c284459d28d60706b246d964a1` |
| 38 | `subagents_extracted/chaosx_scripted_system_architect.toml` | 5,387 | 74 | `b2e012aaec78bc875ae27275eb03f86d425aa19ece182716d2570117ff56cacf` |
| 39 | `subagents_extracted/chaosx_skill_maintainer.toml` | 3,819 | 47 | `1c5efb578a007fc1e3e7f0561d7353876d73918be830f754870041f9d2f66ac2` |
| 40 | `subagents_extracted/chaosx_spreadsheet_doc_worker.toml` | 4,605 | 59 | `896cb63222484317280d31c340edfc282847774f8edab31a68d7fc2b8b0be33b` |
| 41 | `subagents_extracted/chaosx_super_event_audio_researcher.toml` | 3,339 | 65 | `248c26c573151ac503886da9bc8cf1942d2af41608528fb2e92161a7808f7d9b` |
| 42 | `subagents_extracted/chaosx_super_event_text_researcher.toml` | 3,921 | 62 | `c918dae02f2b1127f71134065558f313faec82fba49f3e43022bfeaf3bfb66cb` |

## Tooling note

Full source reading and parent review were completed. Specialist invocation was attempted separately and failed at the outer MCP transport. That failure did not prevent reading the supplied subagent definitions and did not remove any specification section. See `quality/045_third_balkan_war_subagent_blocker.md`.

---

## Included file: `quality/045_third_balkan_war_probability_scenarios.md`

# Event 045 probability and AI scenario contract

This document defines the mandatory named scenarios for every weighted Event 045 surface. It does not choose final numeric weights. The implementation owner chooses the intended balance, and `chaosx_ai_probability_auditor` verifies whether the source produces the required ordering.

Every audit begins with `hoi4.probability_inspect`. The auditor must state whether the candidate pool and external factors are complete. Use exact evaluation where the pool is complete, bounded or score-only evidence where it is not, sweeps for changing escalation or strength, and `hoi4.probability_compare` after every patch.

## P45-S01: Coherent calm-world opening

- World state: Chaos below 200, six valid regional governments, no common faction, no large existing regional war
- Candidate disputes: Macedonia, Aegean access, Southern Dobruja, absurd frontier incident
- Required ordering: disputes supported by current borders and at least two interested governments outrank flavour-only causes
- Opening expectation: two camps, four to six participants preferred, no unsupported adjacent power
- Failure condition: one-on-one opening when four or more coherent participants exist

## P45-S02: Fragmented Yugoslav space

- World state: Yugoslavia absent, several valid successor governments exist, neighboring states have mixed claims and relations
- Required ordering: successor-border and Macedonian disputes gain relevance, but participants without geographic or political connection remain excluded
- Opening expectation: camp construction recognizes successor states individually and avoids rebuilding a fictional unified Yugoslav actor
- Failure condition: dead-tag targeting, duplicate successor participation, or indiscriminate regional enrollment

## P45-S03: Same-faction regional map

- World state: all otherwise valid regional governments belong to one faction and are not in a valid internal rupture state
- Required result: automatic Event 045 weight is unavailable and displayed as `N/A`
- Failure condition: camp logic forces same-faction allies into opening war

## P45-S04: Contained regional belligerent

- Actor: Balkan belligerent with weak equipment reserves, exposed capital rail line, one valid claim, and no outside sponsor
- Required ordering: defensive mission and armistice tools outrank a new offensive claim or wider intervention request
- Sweep: improve equipment, supply, capital security, and allied strength
- Expected movement: claim pressure and support requests rise only as survival becomes credible

## P45-S05: Opportunistic regional belligerent

- Actor: Balkan belligerent with favorable strength, secure supply, an occupied registered claim, and rival sponsor involvement
- Required ordering: press claim and secure corridor outrank immediate armistice
- Hard limit: unregistered claims remain zero or unavailable
- Failure condition: AI pursues unrelated land or rejects all settlements after total military defeat

## P45-S06: Outside containment coalition

- Actor: outside major with no direct claim, high current war load, two credible mediation partners, and escalation in European Crisis
- Required ordering: conference, support suspension, and armistice pressure outrank arms, volunteers, guarantee, and direct intervention
- Sweep: reduce war load and remove mediation partners
- Expected movement: containment weakens gradually, not instantly

## P45-S07: Rival-driven exploitation

- Actor: outside major with theater access, reserves, war support, and a strategic rival supporting the opposite camp
- Required ordering: bounded arms or volunteers may outrank containment
- Direct intervention rule: remains below indirect support until a guarantee, faction commitment, strategic access threat, or hostile major proof exists
- Failure condition: direct war becomes the default response to the first rival shipment

## P45-S08: Evolution II fragmentation

- Target: participant with capital loss, severe instability, heavy casualties, occupation, and at least one valid provider-backed breakaway candidate
- Comparison target: otherwise similar participant with stable capital, low casualties, and no valid candidate
- Required ordering: the first target has materially higher fragmentation eligibility
- Hard limit: missing provider proof makes the result unavailable, not merely low weight
- Failure condition: empty tag creation, duplicate civil war, or fragmentation from time alone

## P45-S09: Evolution III former-ally rupture

- Candidate pair A: former allies with incompatible active claims and disputed occupation
- Candidate pair B: former allies with no claim, occupation, ideological, leadership, or settlement dispute
- Required ordering: pair A can rupture after pacing, pair B remains unavailable
- Sweep: remove occupation, settle the claim, or reconcile the settlement term
- Expected movement: rupture chance falls or disappears as the concrete dispute is removed

## P45-S10: World-war origin honesty

- Scenario A: Event 045 linked wars bring opposing major-led factions into direct conflict and spread beyond the original theater
- Scenario B: the same global war already existed before Event 045 fired
- Required result: Scenario A can set verified origin and reach Another World War, Scenario B cannot
- Failure condition: escalation score alone grants origin credit or the final stage without current proof

## Required comparison report

For every weighted patch, report:

- source surface and identifiers
- baseline scenario hashes
- candidate-pool completeness
- exact, bounded, sampled, or score-only status
- ordering before the patch
- intended ordering supplied by the owner
- ordering after the patch
- starvation, dominance, and invalid-target findings
- unresolved external factors

A passing comparison proves the accepted ordering. It does not prove that one precise percentage will hold in every campaign state unless the complete normalized pool and all external factors were supplied.

---

## Included file: `quality/045_third_balkan_war_acceptance_criteria.md`

# Event 045 implementation acceptance criteria

## Identity and registration

- Event ID `45`, entry `chaosx.nr45.1`, Minor Fire-Once, and Chaos level `1` remain aligned across registration, localisation, Event Details, docs, and catalog.
- Event 045 is registered in the Wars cluster with High member severity.
- The event stays disabled in the default reworked-event allowlist until every required surface is ready.
- Invalid automatic selection shows `N/A`, not a misleading zero weight.

## Opening validity and transaction

- At least three valid ordinary regional governments are required.
- Every participant has a current geographic, claim, guarantee, faction, ideology, or strategic connection to the selected dispute.
- Two camps are the normal opening.
- A three-sided opening requires a proven conflict graph and no missing hostile edge.
- Same-faction governments are not placed in opposing opening camps.
- Special Chaos and actual nonhuman countries are excluded from ordinary camp construction.
- Dead, capitulated, territoryless, and nonviable actors fail closed.
- The opening transaction either creates the complete valid war graph or rolls back all temporary setup.
- The outbreak begins immediately after successful setup.

## Balkan War Escalation

- Exactly one persistent public custom value exists.
- The meter uses the accepted 0 to 100 range and five named stages.
- Time alone never raises escalation.
- Every increase and decrease has a material cause and repeat guard.
- Support uses cumulative tiers rather than one reward per click.
- The Powder Keg Explodes requires direct opposing major or major-faction war proof.
- Another World War requires wider-war proof and cannot be reached by score alone.
- Irreversible floors apply after direct major commitments where the spec requires them.
- Latest cause, next threshold, and missing proof display correctly.

## Claims and settlements

- One maintained registry supplies regional interests and claim groups.
- Exact state groups are verified with installed map data and HOI4 map tools.
- No generic occupation-to-claim shortcut exists.
- Other event-owned claims are read without duplicate ownership.
- Settlement terms depend on active claims, occupation, surviving governments, and event state.
- Status quo, limited revision, corridor, justified subject, verified partition, frozen armistice, and wider-war continuation routes have distinct validity rules.
- Peace cleanup removes temporary war goals, decisions, missions, and settlement targets.
- Only defined postwar memories remain.

## Decisions and missions

- One ordinary decision category and one static category picture are used.
- The category exposes three to five primary actions in normal phases, never more than six.
- Active missions stay between one and three.
- Country lists use selected-target presentation.
- Every action has at most four spendable cost types and correct texticons.
- Costs and requirements match the action and are not hidden in effects.
- Missions require concrete state, unit, supply, rail, port, corridor, occupation, or diplomatic work.
- Success, partial success, and failure use distinct logic.
- AI has an equivalent route for every meaningful human action.
- Obsolete and invalid actions clean up after role, target, war, or lifecycle changes.

## Evolutions

- Evolution I requires 200 or more Chaos, separate pacing, and broader registered ambitions.
- Evolution II requires 400 or more Chaos, severe proven weakening, and a valid provider-backed actor.
- Evolution III requires 600 or more Chaos and a concrete former-ally dispute.
- Evolution state itself changes no Chaos.
- Disabled Evolutions do not set recorded flags, create actors, open decisions, or unlock later stages.
- Each Evolution appears correctly in the main Evolutions tab, related-history view, and Event Details catalog.
- Evolution actor, tier, stage, event identity, date, and enabled state remain aligned.

## AI and probability

- Every weighted surface has a baseline P45 scenario audit.
- Owner-selected balance changes receive a same-scenario `hoi4.probability_compare` pass.
- Invalid actions and targets evaluate to unavailable or zero.
- Regional AI weighs survival, supply, claims, sponsors, capital security, and settlement feasibility.
- Outside AI weighs ideology, rivalry, access, reserves, current war load, guarantees, factions, and containment partners.
- Complete defeat prevents endless AI settlement refusal.

## Shared systems and Chaos

- Generic wars, peace, deaths, annexations, puppeting, and faction changes use their existing shared sources.
- Event 045 does not duplicate those Chaos changes.
- Any event-owned Chaos source is separately defined, one-shot or bounded, and logged through Chaos History.
- Shared Deaths, migration, famine, and civilian routing use their own owner contracts when consequences reach them.
- The event does not add a broad recurring whole-world scan.

## Presentation and assets

- Opening outbreak and verified world-war handoff each have a distinct complete super-event package.
- The final stage is presented as a wider-war handoff, not a terminal world end.
- Quotes and cultural references are verified and not invented.
- Audio is licensed, musical, unique unless reuse is explicitly approved, settings-aware, and documented.
- Required report art, category art, decision icons, mission icons, and six achievement triplets are final and wired.
- No placeholder, unrelated reuse, primitive local drawing, or opaque-square alpha failure remains.
- No unrequested portrait, flag, 3D model, custom tag, or dedicated scripted GUI is added.

## Achievements

- All six achievement definitions, trackers, disqualifiers, localisation, icon triplets, and persistence rules exist.
- Achievements read the event's gameplay ledgers rather than duplicate registries.
- Invalid generations and false origin states cannot unlock achievements.
- Delayed and post-handoff achievements survive save and reload.

## Logs, docs, and catalog

- History records the event once with a meaningful actor context.
- Event Details explains the premise, public escalation stages, and three Evolutions without implementation notes or hidden spoilers.
- Stage reports and Evolution logs do not duplicate ordinary history entries.
- Event docs, super-event research, audio catalog, asset provenance, completion report, and source package are aligned.
- The authoritative workbook is updated after final player-facing wording exists.
- The three catalog CSV snapshots are regenerated and not edited directly.

## Required final scenarios

- normal two-camp opening
- justified three-sided opening
- insufficient candidates
- all candidates in one faction
- fragmented Yugoslav region
- opening rollback after one late validation failure
- contained regional settlement
- Evolution I claim settlement
- Evolution II provider-backed fragmentation
- Evolution III former-ally rupture
- direct major intervention and escalation floor
- score threshold without proof
- verified Another World War origin
- rejection of false origin during a pre-existing global war
- each Evolution disabled
- every achievement positive and main negative case
- save and reload during opening, Evolution, armistice, settlement, and post-handoff tracking

The implementation is incomplete while any criterion above is missing, simplified, unwired, unaudited, or supported only by a placeholder.

---

## Included file: `quality/045_third_balkan_war_design_audit.md`

# Event 045 parent design audit

## Audit scope

This audit applies the stored role contracts for event planning, improvement, decisions and missions, scripted systems, AI probability, assets, localisation, super-events, completion review, documentation, and catalog alignment. It reviews the specification package, not an implementation.

Actual specialist invocation was attempted and blocked by the outer tool transport. The parent therefore performed the design review directly. The blocker is recorded separately.

## Event promise test

The event promise is immediate regional war with a credible path toward containment, European escalation, or world war. The package delivers that promise at the opening. It does not delay conflict behind a prewar countdown, and it does not assume the historical 1936 map.

The opening remains readable because the participant graph is built from one selected dispute and bounded actor roles. The camp system prevents the event from becoming a random declaration generator. The same-faction gate, existing-world-war gate, and rollback transaction protect causal and diplomatic coherence.

Verdict: Pass.

## Evolution test

The three Evolutions change different structural layers:

- Evolution I expands the claim and settlement space.
- Evolution II expands the actor and front space through validated internal fragmentation.
- Evolution III changes the alliance graph through concrete former-ally disputes.

None of them is a renamed baseline escalation stage. Each has its own Chaos requirement, trigger proof, pacing, enable behavior, and cleanup.

Verdict: Pass.

## Cognitive-load test

The public layer contains one persistent custom value, Balkan War Escalation. Claims, sponsors, support types, camp relations, stage proofs, armistice records, and settlement facts remain internal unless they are needed in one concise tooltip or selected-target view.

The decision category budget stays within three to five primary actions in normal states and one to three active missions. No dedicated scripted GUI is required. A static category picture gives identity without adding fake controls.

Verdict: Pass.

## Decision quality test

The action families represent military, logistical, diplomatic, and territorial commitments. They do not form a political-power store. The missions ask the player to hold railways, capitals, ports, corridors, armistice lines, and disputed occupation zones. Foreign support requires routes and material capacity. Containment works better through cooperation.

Every major action affects escalation, a claim, a mission, a support relationship, a settlement term, or a war role. Tiny modifier dust is not used as the primary effect.

Verdict: Pass.

## AI test

The design provides separate regional and outside-power reasoning, hard invalidity blocks, surrender realism, and named probability scenarios. Direct intervention is not the default response to minor aid. Fragmentation and ally rupture require proof rather than elapsed time.

The final numeric weights remain implementation-owned and require MCP evidence. This is the correct boundary for a planning pack.

Verdict: Pass with implementation evidence required.

## Historical and regional specificity test

The claim registry covers the main recurring territorial families relevant to the interwar Balkans while refusing unrestricted expansion. Research is used as design grounding, not as a claim that one historical settlement mechanically determines every alternate-history map.

The disputed Petrich stray-dog account and the often-attributed Bismarck quotation are treated as uncertain. Neither is approved as an asserted fact or final quote.

Verdict: Pass.

## Asset and presentation test

The asset inventory is proportional to the event. Two super-events are justified by two distinct thresholds, the outbreak and verified world-war handoff. Report art, a static category picture, decision and mission icons, and achievement art support gameplay clarity.

The package avoids portraits, flags, custom tags, animation, and 3D work because the accepted design does not require them. This is restraint, not missing depth.

Verdict: Pass.

## Shared-system test

The event relies on normal war, peace, Deaths, annexation, puppeting, faction, migration, famine, and civilian-routing owners. It does not duplicate their Chaos sources. The event keeps its lifecycle, claim registry, opening graph, escalation ledger, and settlement logic in its own owner package.

Verdict: Pass.

## Edge-case test

The package explicitly covers:

- insufficient valid participants
- all candidates in one faction
- dead or nonviable actors
- special Chaos and nonhuman actors
- fragmented Yugoslav space
- Turkey only when strategically relevant
- justified three-sided war
- partial setup failure and rollback
- aid and commitment farming
- stage score without proof
- pre-existing global war
- invalid fragmentation provider
- former allies without a concrete dispute
- disabled Evolutions
- save and reload persistence

Verdict: Pass.

## Remaining implementation risks

The main risks belong to implementation and evidence:

1. Mapping exact state groups against the installed map and modded state registry.
2. Building a linked three-sided conflict without duplicate or contradictory war declarations.
3. Persisting generation-scoped arrays and event targets safely across save and reload.
4. Detecting support and direct intervention without broad recurring scans.
5. Creating settlement terms that respect active wars and ordinary peace-conference behavior.
6. Validating weighted AI through complete candidate pools.
7. Sourcing final licensed musical audio and verified super-event quotations.

These risks are covered by the implementation prompts and acceptance criteria. They do not require another broad design expansion.

## Final design verdict

The package is deep enough for implementation and remains within the event's scope. It has a clear playable loop, concrete choices, distinct Evolutions, AI direction, historical grounding, restrained assets, cleanup rules, and measurable acceptance scenarios.

No design simplification, fallback, or omitted accepted surface was found in the parent review.

---

## Included file: `quality/045_third_balkan_war_improvement_closure.md`

# Event 045 improvement-loop closure handoff

Broad expansion is no longer recommended before implementation.

The event has reached a stable design boundary:

- the opening delivers the event promise immediately
- one public value explains growth and containment
- baseline stages and Evolutions are separated
- regional claims are bounded by a maintained registry
- regional and outside players have distinct action loops
- settlements support victory, compromise, armistice, and wider-war continuation
- AI has role-specific goals and named probability scenarios
- assets support the mechanic without introducing unused visual systems
- achievements reward containment, revision, fragmentation, betrayal, origin, and regional agreement
- cross-event connections use existing provider and shared-system contracts
- edge cases and cleanup are explicit

Another large expansion would likely add duplicate claim actions, more visible counters, unnecessary country packages, an unjustified custom GUI, or extra super-events without improving the main play loop.

## Final implementation tasks

The remaining work is implementation, evidence, and polish:

1. Verify exact map state groups and claim ownership.
2. Implement the event-owned camp, war, escalation, claim, support, Evolution, and settlement ledgers.
3. Implement the decision and mission category with AI equivalents.
4. Run the required event-chain and probability MCP workflows.
5. Produce and wire the accepted visual and audio assets.
6. Write final player-facing localisation from the supplied direction.
7. Implement and test all six achievements.
8. Align Event Logs, Event Details, documentation, audio records, and the authoritative workbook.
9. Run the completion auditor and resolve every finding.

The improvement loop can stop after these tasks are implemented and validated. A later loop pass is justified only if implementation exposes a new design gap that this package does not cover.

---

## Included file: `quality/045_third_balkan_war_subagent_blocker.md`

# Event 045 specialist invocation blocker

## Requested specialist use

The planning task required the full project source set and the provided subagent definitions. All 21 supplied project files and all 20 archived subagent TOML definitions were read in full.

The parent attempted to discover and invoke the configured specialists through the outer Codex tool route. The attempts included direct inventory queries for agent and spawn capabilities, a specific query for `chaosx_improvement_loop_planner`, and a command-route probe.

## Tool result

The specialist inventory calls failed with HTTP 429 responses from the MCP tunnel. The command-route probe failed with HTTP 404. No local Codex or Qoder executable was available as a safe substitute.

No specialist process ran and no subagent output is presented as if it had run.

## Parent response

The parent applied the stored role contracts directly while preparing this specification. The package therefore includes separate parent reviews for:

- improvement-loop depth and closure
- decision and mission design
- probability scenario requirements
- asset scope
- super-event research boundaries
- achievement implementation
- scripted-system ownership
- localisation direction
- completion acceptance
- documentation and catalog alignment

This manual role application does not replace the required implementation-time specialist passes. The coding prompt still requires the appropriate bounded specialists when the runtime route is available.

## Effect on the specification

The transport failure did not cause any planned design section to be removed, shortened, or replaced with a fallback. It does limit the evidence claim. The package is parent-reviewed and source-complete, but it is not subagent-verified.

---

## Included file: `handoffs/045_third_balkan_war_implementation_surface_map.md`

# Event 045 implementation surface map

This is a planning map. Final file names should follow existing repository ownership and current precedents after inspection.

## Event owner package

| Surface | Expected owner | Required content |
| --- | --- | --- |
| Entry and follow-up events | `events/045_third_balkan_war.txt` | entry, reports, role notifications, stage reports, settlement and aftermath events |
| Script constants | `common/script_constants/045_third_balkan_war_constants.txt` | stage bands, proof floors, support tiers, pacing, mission durations, AI anchors, registry ids |
| Scripted triggers | `common/scripted_triggers/045_third_balkan_war_triggers.txt` | event validity, regional eligibility, dispute validity, camp compatibility, stage proof, claim proof, Evolution gates, settlement gates |
| Scripted effects | `common/scripted_effects/045_third_balkan_war_effects.txt` | opening transaction, camp construction, war linkage, escalation registration, claim activation, support ledger, settlement, cleanup |
| On actions | `common/on_actions/045_third_balkan_war_on_actions.txt` | narrow event-owned reactions where direct hooks exist and bounded pulses where necessary |
| Decisions | `common/decisions/045_third_balkan_war_decisions.txt` | role-aware actions, selected-target decisions, missions, cleanup |
| Category | `common/decisions/categories/045_third_balkan_war_categories.txt` | one ordinary category with static picture and dynamic description |
| Ideas or dynamic modifiers | event-owned files only when needed | temporary mobilization, corridor, armistice, or settlement effects with complete lifecycles |
| Opinion modifiers | event-owned file | support, betrayal, occupation dispute, mediation, and settlement memories |
| AI strategy | event-owned AI files or owner helpers | camp commitment, containment, exploitation, surrender realism, wider-war posture |

## Shared event-system surfaces

| Shared surface | Required change |
| --- | --- |
| Event registration | classify Event 045 as Minor Fire-Once, level 1, and ready only after completion |
| Event name selectors | add final name and debug mapping |
| Event log actor mapping | choose a meaningful opening actor or camp leader |
| Event Details | premise, public stages, three Evolution previews, Chaos level, cluster status |
| Evolution logger | type, stage, tier, actor, enabled state, list and detail localisation |
| Cluster registry | Wars member, High severity, correct minimum tier and role |
| Settings manual event path | normal and Force Trigger behavior with validity and test bypass separation |

## Claim and map data

The implementation must inspect the installed map before freezing state groups. Use `hoi4.map_inspect` for the maintained regional groups and record the exact state and adjacency evidence. Put stable group identifiers in the Event 045 owner registry or the shared universal state registry only when another owner genuinely needs the same group.

Required families:

- Macedonia
- Aegean access and Western Thrace
- Serbian-Bulgarian frontier
- Kosovo, western Macedonia, and Albanian interests
- Southern Dobruja
- Transylvania and Partium
- Banat, Bačka, and Vojvodina
- Yugoslav successor disputes
- European Thrace and the Straits

## Decision presentation and assets

| Asset family | Final owner path direction |
| --- | --- |
| Category picture | `gfx/interface/decisions/045_third_balkan_war/` |
| Decision icons | `gfx/interface/decisions/045_third_balkan_war/` |
| Mission icons | event-scoped decision or mission icon folder following inspected precedent |
| Report and news images | `gfx/event_pictures/045_third_balkan_war/` |
| Super-event images | event-scoped super-event folder following current slot wiring |
| Achievement icons | root achievement folder with full achievement ids and three state files |
| Audio | `sound/045_third_balkan_war/` with one unique file for each super-event |

Every non-portrait asset uses the proper narrow asset worker. No runtime path may point into `docs/assets/` after completion.

## Localisation surfaces

- event titles, descriptions, options, and report text
- event name and Event Details selectors
- escalation stage names and concise cause or proof tooltips
- decisions, missions, costs, requirements, success, partial success, and failure
- claims, named regions, settlements, armistice, and postwar memories
- three Evolution names and descriptions across every log surface
- six achievement entries
- two super-event packages
- scripted localisation for role, stage, selected target, latest cause, missing proof, and settlement summary

All final player-facing text must follow the Chaos Redux writing rules and remain free of process notes, hidden variables, uncertain historical claims, and unsourced quotations.

## Achievements

Add all six definitions to the single Chaos Redux achievement registry. Reuse Event 045 ledgers for proof. Add tracking and cleanup in Event 045 owner effects, not in a detached parallel subsystem.

## Super-events and audio

Two complete packages are required:

1. the successful opening transaction
2. the verified Another World War handoff

Each needs a deliberate slot, title, description, button, verified quote, image, unique licensed musical audio, settings-aware playback, sound definitions, source documentation, audio catalog row, and event trigger.

## Documentation and spreadsheet

Expected permanent documentation:

- `docs/events/045_third_balkan_war/overview.md`
- system notes for opening, escalation, claims, intervention, settlement, Evolutions, AI, achievements, and validation as needed
- `docs/super_events/045_third_balkan_war_super_event_research.md`
- completion report under the event plan folder
- updated authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- regenerated CSV snapshots through the repository exporter

## Required specialist routing

- `chaosx_scripted_system_architect` for repeated owner helpers
- `chaosx_decision_mission_auditor` for the decision package
- `chaosx_ai_probability_auditor` for weighted surfaces before and after patches
- `chaosx_asset_source_researcher` and `chaosx_generated_event_art` for scene art according to source mode
- `chaosx_icon_artist` for decisions, missions, and achievements
- `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher`
- `chaosx_localisation_auditor`
- `chaosx_event_completion_auditor`
- `chaosx_spreadsheet_doc_worker` after final implementation wording exists

The event UI worker is out of scope because no dedicated scripted GUI is accepted.

---

## Included file: `prompts/045_third_balkan_war_asset_prompt.md`

# Asset production prompt for Event 045: Third Balkan War

Use `chaos-redux-event-assets`, `chaos-redux-super-events`, and `chaos-redux-frame-animation` only if later review adds a genuine animation requirement. Route work through the correct narrow asset subagents with context-complete prompts. Character portraits and 3D work are outside this accepted asset set.

Read the full Event 045 spec pack first, especially:

- `specs/045_third_balkan_war_spec_part_1_core.md`
- `specs/045_third_balkan_war_spec_part_3_escalation_intervention_decisions.md`
- `specs/045_third_balkan_war_spec_part_6_ai_achievements_assets.md`
- `research/045_third_balkan_war_research_notes.md`
- `prompts/045_third_balkan_war_super_event_prompt.md`

Use the temporary workspace `docs/assets/045_third_balkan_war/` during active production. Final runtime files must move to event-scoped engine folders. Promote durable provenance and crosswalk facts into permanent Event 045 documentation, verify that no runtime reference points into `docs/assets/`, then remove the temporary workspace only after the complete event is accepted.

## Required reference inspection

Before producing each asset family, inspect the matching skill-local vanilla reference folder, its `contact_sheet.png`, and its `CATALOG.md` entry. Follow the active vanilla or Chaos Redux consumer to confirm exact dimensions, frame count, alpha behavior, and target sprite definition.

For the decision category picture, inspect:

```text
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/
```

Create and document the contact sheet first if it is missing.

## Required scene art

### Opening outbreak super-event image

- Stable working basename: `045_third_balkan_war_outbreak`
- Subject: several Balkan armies already mobilizing through one frontier rail junction, crowded troop transport, mountain or border infrastructure, mixed equipment, and evidence of multiple national columns
- Tone: period documentary realism, restrained irony in the situation rather than comedy in the people
- Source mode: sourced period image when a defensible archival scene fits, otherwise generated alternate-history documentary art
- Avoid: a map as the central subject, modern equipment, readable generated text, gore, triumphant single-national propaganda, and jokes about casualties

### Another World War handoff super-event image

- Stable working basename: `045_third_balkan_war_world_war`
- Subject: the regional junction overwhelmed by major-power columns, aircraft, foreign staff vehicles, or several military routes leaving the original theater
- Tone: grave, wider scale, visually distinct from the opening
- Use only when the final stage proof exists

### Report or news image family

Create distinct or clearly staged images for:

- another Balkan country entering
- foreign arms or volunteers arriving
- guarantee or faction enforcement
- direct major intervention
- armistice or regional settlement

Use sourced archival material only when attribution, rights, date, and period fit are defensible. Generated scenes must look like 1936-1945 documentary photographs, not modern cinematic concept art.

## Decision category picture

- Stable working basename: `045_third_balkan_war_category`
- Subject: a frontier rail and road junction, border barriers, mobilizing columns, a visible port or mountain route in the distance, and signs of several competing directions
- Presentation: static category picture
- No fake buttons, fake meter, fake map controls, or generated text
- Confirm the runtime canvas from the actual consumer rather than assuming the reference family's nominal size

## Decision icons

Create independent 32x32 source compositions for:

- `decision_045_register_claim`
- `decision_045_request_arms`
- `decision_045_invite_volunteers`
- `decision_045_secure_corridor`
- `decision_045_offer_armistice`
- `decision_045_allied_occupation`
- `decision_045_frontier_mobilization`
- `decision_045_transit_access`
- `decision_045_mediation`
- `decision_045_guarantee`
- `decision_045_faction_invitation`
- `decision_045_sanctions`
- `decision_045_direct_intervention`

Use native ImageGen transparency, preserve alpha, keep one strong silhouette, and validate at final size. Do not derive these by resizing achievement or super-event art.

## Mission icons

Create independent mission-specific 32x32 art for:

- `mission_045_capital_rail_line`
- `mission_045_port_corridor`
- `mission_045_armistice_line`
- `mission_045_restrain_ally`
- `mission_045_straits_approaches`

## Achievement icons

Create separate 64x64 completed art for the six achievement IDs in `prompts/045_third_balkan_war_achievement_prompt.md`, plus the exact grey and not-eligible variants required by the current achievement consumer.

Achievement files must remain directly under the engine-required achievement root and use full achievement IDs as basenames. Each concept needs its own source art and manifest row.

## Packaging and evidence

For every asset record:

- stable asset ID and consumer
- source mode
- source URL, creator, archive, license, date, and rights confidence when sourced
- ImageGen prompt and native transparency mode when generated
- original source file
- processed PNG preview
- final DDS path
- proposed sprite name
- actual dimensions and alpha behavior
- contact-sheet review
- final-size readability review
- runtime handoff and pending wiring

Do not ship placeholders, primitive local drawings, reused unrelated icons, opaque square backgrounds, fake checkerboards, or unapproved fallbacks. Mark an asset blocked when the required source, rights, reference, or generation route cannot be verified.

---

## Included file: `prompts/045_third_balkan_war_super_event_prompt.md`

# Super-event research and production prompt for Event 045

Use `chaos-redux-super-events`, `chaos-redux-event-assets`, and the narrow super-event text, audio, and image subagents. Read the full Event 045 specification and research notes before selecting any final wording, quote, image, or music.

Event 045 has two justified super-event roles.

## Super-event A: outbreak

### Trigger meaning

The event has successfully created a valid multi-country Balkan war and recorded its opening camps. The war is already active when the presentation appears.

### Text direction

- Title direction: short identification of the Third Balkan War or the return of the Balkan powder-keg problem
- Description direction: several regional armies are already moving, the dispute is known, and outside powers are deciding whether to contain or exploit it
- Button direction: restrained dark humour about historical recurrence, diplomatic optimism, borders, or the belief that a regional war can stay regional
- Quote direction: verified public-domain or historical wording about Balkan rivalry, alliance failure, mediation, territorial ambition, or the danger of a regional crisis
- Tone: ironic at the recurrence, serious about the fighting
- Avoid: jokes about deaths, ethnic stereotypes, generic world-in-flames language, invented quotes, and final text copied from the planning spec

The frequently attributed Bismarck remark about a foolish event in the Balkans is not approved. Use it only if the text researcher finds reliable original or scholarly provenance. Otherwise reject it and document the rejection.

The 1925 Petrich incident may support a brief researched allusion, but the stray-dog origin story has competing accounts and must not be stated as certain fact.

### Image direction

Use the outbreak image brief in `prompts/045_third_balkan_war_asset_prompt.md`. The image should show mobilization and frontier movement rather than a map.

### Audio direction

Find a unique, intentional musical recording with a verified license. Search first for period-appropriate public-domain or clearly licensed Balkan, southeastern European, military, orchestral, or folk material whose recording rights are also usable. Avoid choosing one belligerent's triumphal national recording as the neutral event cue unless the context and rights clearly justify it.

The final cue should normally be one to two minutes after editing. Preserve the source, verify composition and recording rights separately, convert to game-ready WAV, register a unique audio ID, create the settings-volume wrappers, use `play_current_super_event_sound = yes`, and update the canonical music catalogue.

## Super-event B: Another World War

### Trigger meaning

Balkan War Escalation has reached at least `85`, opposing major powers or major-led factions are directly fighting, and one wider-war proof in the specification is met. Event 045 records the Balkan conflict as the origin crisis and hands control to normal war and faction systems.

### Text direction

- Title direction: the regional war has become a wider world war
- Description direction: direct major-power conflict and fronts outside the original theater are now visible facts
- Button direction: grave, brief, and free of triumphant humour
- Quote direction: verified historical or public-domain wording about alliance escalation, war spreading beyond control, or the cost of failed restraint
- Tone: serious and final about scale, while not describing a terminal world end
- Avoid: apocalyptic extinction language, invented prophecy, and lines that imply the campaign has ended

### Image and audio direction

Use a visually distinct world-war handoff image. Select a unique licensed musical cue with wider scale and no reuse from another super-event unless the user explicitly approves the exact reuse.

## Required research output

For each super-event provide:

- stable role and proposed slot
- at least three title directions before final selection
- at least three quote candidates with exact source, author, work, year, link, public-domain or copyright status, and confidence
- at least three short cultural remark directions where the role permits one
- rejected candidates and reasons
- selected final title, description, button, and quote only after source checks
- image source mode and asset handoff
- at least three audio candidates with title, creator or composer, performer or recording source, source URL, license, duration, usage terms, attribution, and suitability
- selected source download and processed WAV
- base sound definition and settings-wrapper IDs
- final audio ID and helper wiring plan
- permanent research note under `docs/super_events/`
- update to `music/chaosx_music_track_list.html`

Any unverified quote, cultural reference, or recording remains blocked. Do not fill a missing slot with default art, default audio, or provisional text and call it complete.

---

## Included file: `prompts/045_third_balkan_war_achievement_prompt.md`

# Achievement implementation handoff for Event 045

Implement the complete Event 045 achievement set from `specs/045_third_balkan_war_spec_part_6_ai_achievements_assets.md`.

## Required achievements

1. `chaosx_achievement_045_keep_it_regional`
2. `chaosx_achievement_045_the_conference_holds`
3. `chaosx_achievement_045_every_map_is_temporary`
4. `chaosx_achievement_045_no_friends_left`
5. `chaosx_achievement_045_a_very_small_incident`
6. `chaosx_achievement_045_the_entente_reversed`

## Implementation contract

For every achievement, implement the complete runtime surface:

- a stable achievement definition in the single Chaos Redux achievement registry
- event-owned tracking flags or variables
- precise unlock triggers
- explicit disqualifiers
- save and reload persistence
- cleanup after an invalid event generation
- player-country continuity rules
- final localisation written from the working direction in the spec
- three independent achievement-state assets when required by the current consumer
- documentation and catalog-facing alignment where achievement summaries are shown

Do not convert the working labels into final text without a localisation pass. Do not weaken a difficult achievement into an automatic unlock. Do not count Force Trigger Mode, invalid opening generations, or unrelated pre-existing world wars unless the achievement contract explicitly allows them.

## Shared proof rules

Use the same Event 045 ledgers that control gameplay. Do not maintain a second contradictory achievement-only claim registry, participant list, stage proof, or settlement record.

The following facts must be available to achievement triggers:

- original participant status
- opening participant count
- opening cause family
- maximum escalation reached
- direct outside-major entry
- conference leadership and cooperating powers
- successful armistice-line mission
- active registered claims settled by the player
- Evolution I and Evolution III activation
- former-ally war participation
- verified Third Balkan War origin of Another World War
- settlement signatories and their opening camps
- final independence, subject status, annexation, capital survival, and player-country continuity

When the event hands off to a wider war, preserve only the achievement facts needed for post-handoff checks and clear them after success, permanent failure, or campaign invalidation.

## Asset handoff

Route six complete achievement triplets to `chaosx_icon_artist` through the event asset workflow. Each completed icon must be independently composed for the achievement surface. Grey and not-eligible variants must follow the exact current achievement precedent. Do not resize decision art, reuse another achievement, or make local primitive substitutes.

## Validation

Test every unlock and every main disqualifier in separate scenarios. Include a negative test where the numerical escalation threshold is reached without the required world-state proof. Include a negative test where a pre-existing world war prevents Event 045 origin credit. Include a save and reload checkpoint before each delayed or post-handoff unlock.

The completion handoff must list definitions, tracking identifiers, localisation keys, asset paths, scenario evidence, and any unresolved blocker. No simplification or fallback is authorized.

---

## Included file: `prompts/045_third_balkan_war_decision_mission_prompt.md`

# Decision and mission implementation handoff for Event 045

Implement the Event 045 decision system from the accepted specifications and diagrams. Read `chaos-redux-decisions-missions` before editing and use `chaosx_decision_mission_auditor` after the parent implementation pass.

## Presentation choice

Use one ordinary Event 045 decision category with a static category picture and a compact dynamic header. Do not build a dedicated scripted GUI. The header shows:

- Balkan War Escalation as the only persistent custom value
- current named stage
- latest material cause of movement
- next threshold and any missing proof
- the current country's role

Keep the category phase-aware. A country should normally see three to five primary actions, never more than six, and one to three active missions. Use the selected-target pattern for country lists so the category does not display one action row for every Balkan participant or sponsor.

## Required action families

### Regional belligerents

- activate one valid regional claim or settlement goal
- secure a named military corridor
- request or reject foreign support
- press for an armistice when military conditions justify it
- contest an allied occupation that conflicts with the country's registered interests

### Neutral Balkan governments

- declare guarded neutrality
- mobilize around a newly relevant registered interest
- mediate a bilateral frontier issue
- join a camp only through a real claim, threat, guarantee, ideological, or strategic connection
- prepare defenses around a named frontier, port, railway, or capital route

### Outside containment powers

- coordinate mediation
- suspend arms or volunteers
- pressure a guarantor or faction leader to limit commitments
- sponsor an armistice conference
- enforce sanctions or diplomatic pressure against the party widening the war

### Outside exploitative powers

- send equipment through a viable route
- send volunteers or a military mission
- recognize one registered claim
- issue a guarantee
- invite a participant into a faction through normal validity rules
- prepare direct intervention only when access, forces, readiness, and escalation justify it

## Required mission families

- hold the capital rail line
- secure an Aegean or Adriatic corridor
- observe and hold an armistice line
- restrain an ally from occupying a disputed registered region
- secure or deny the Straits approaches when Turkey and the theater make that objective relevant

Missions must name their states or named regions and require real action. They should use varied durations, normally 90 to 180 days, based on travel, construction, and combat difficulty. Success, partial success, and failure need distinct effects.

## Costs and effects

Use no more than four spendable cost types for one action. Match costs to the act through equipment, fuel, convoys, trains, command power, XP, stability, war support, civilian factory burden, or tied military capacity. Political power may support diplomatic actions but must not become the default payment.

Every action must change a relationship, mission, claim, settlement term, map objective, support tier, or escalation state. Do not add a tray of small modifier purchases. All costs need matching texticons and clear blocked tooltips.

## AI and probability evidence

Every AI-usable action needs equivalent scripted logic. Before changing weights, route the surface through `chaosx_ai_probability_auditor` and the named scenarios in `quality/045_third_balkan_war_probability_scenarios.md`. After the owner applies the chosen balance, run `hoi4.probability_compare` on the same scenarios.

## Cleanup

Remove obsolete actions after camp destruction, target invalidation, settlement, role change, wider-war handoff, or event cleanup. Clear selected targets, temporary flags, active missions, costs, and stale decision activations. Do not use a whole-world daily scan.

The handoff must list every category, decision, mission, helper, localisation key, cost type, AI surface, cleanup hook, audit result, and unresolved risk. No unapproved fallback is permitted.

---

## Included file: `prompts/045_third_balkan_war_coding_prompt.md`

# Coding-agent implementation prompt for Event 045

Implement Event 045, Third Balkan War, from the complete accepted package under `docs/specs/045_third_balkan_war_specs/`. Treat every mapped requirement as acceptance criteria. Do not replace dynamic camp construction, linked wars, claims, intervention, Evolutions, AI, achievements, assets, or settlement logic with smaller substitutes.

## Mandatory preparation

Read `AGENTS.md`, all event-package files, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, the relevant offline wiki pages, current vanilla documentation, and at least one current vanilla precedent for each engine surface touched. Use the HOI4 MCP event and probability tools for the supported event-chain and weighted surfaces. Record exact blockers when a mandatory route is unavailable.

## Required gameplay implementation

- Keep Event ID `45`, type Minor Fire-Once, Chaos level `1`, and entry `chaosx.nr45.1`.
- Register Event 045 in the Wars cluster with High member severity.
- Keep it disabled by default until the complete rework is ready.
- Add a reusable validity trigger that requires enough ordinary, viable regional governments to form a real multi-country war.
- Dynamically assemble two opening camps, or a justified three-sided linked war graph, from current borders, claims, factions, guarantees, ideology, geography, and campaign state.
- Never place same-faction countries in opposing opening camps.
- Make opening setup transactional and rollback-safe.
- Expose exactly one persistent custom value, Balkan War Escalation, with the five accepted stages and proof gates.
- React to regional entry, support tiers, volunteers, guarantees, faction calls, direct major intervention, hostile major pairs, theater spread, armistice compliance, and settlements without passive upward drift.
- Implement the maintained regional-interest and claim registry through map-inspected state groups.
- Implement role-aware decisions and missions with selected targets, varied real costs, clear tooltips, AI equivalents, and complete cleanup.
- Implement regional victory, negotiated settlement, imposed ceasefire, frozen armistice, wider-war continuation, and Another World War handoff.
- Implement all three Evolutions through separate enable state, dynamic pacing, log entries, content gates, and cleanup. Evolution activation itself adds zero Chaos.
- Reuse Independence Wave and Random Civil War provider packages for valid Evolution II actors instead of creating empty tags.
- Implement the six achievements and complete asset, super-event, event-log, Event Details, documentation, and catalog alignment.

## Chaos and origin rules

Do not duplicate generic Chaos from wars, peace, deaths, annexations, puppeting, or faction changes. Add event-owned Chaos only for a separately defined Event 045 consequence that shared systems do not already represent. The final Another World War stage is not a world-end scenario. Set the origin memory only when Event 045 proves that its linked conflict created the first qualifying wider war. A pre-existing global war must not receive false Event 045 origin credit.

## Technical architecture

Centralize thresholds, stage bands, support tiers, durations, cooldowns, AI factors, and settlement tuning in script constants. Use event targets for short-lived scope pointers and stable generation identifiers for persistent ledgers. Use registered participants, claims, sponsors, missions, and bounded pulses. Do not add a broad daily, weekly, or monthly all-country loop without explicit user authorization.

Reuse shared classifiers for special and nonhuman countries and shared stockpile or population helpers when applicable. Event-specific lifecycle and validation remain in Event 045 owner files. Document any genuinely cross-system helper added to the dynamic registry in the same change.

## Required specialist passes

Use the correct bounded subagents with explicit context and no inherited thread state:

- scripted-system architect for reusable helpers
- decision and mission auditor for the category and missions
- AI probability auditor before and after weighted changes
- generated art, source research, and icon workers for accepted assets
- super-event text and audio researchers for the two accepted super-event moments
- localisation auditor for visible text
- event completion auditor before the final claim
- spreadsheet worker only after final in-game wording and implementation facts exist

Do not invoke the event UI worker because the accepted design has no dedicated scripted GUI.

## Validation and completion

Use `hoi4.event_inspect`, event render or compare routes, and the probability scenarios in the quality folder. Test opening validity, two-camp and three-sided setup, rollback, same-faction rejection, fragmented Yugoslavia, support tier anti-farming, stage proof caps, settlement families, each Evolution enabled and disabled, wider-war origin, pre-existing world-war rejection, achievements, save and reload, invalid-target cleanup, cluster integration, and Event Log displays.

Produce a concrete completion report with changed files, identifiers, scenario evidence, assets, audio and source records, docs, workbook export, unresolved plans, and simplifications. If any accepted surface is missing, fallback, unwired, unaudited, or unverified, mark the implementation incomplete. No simplification or fallback is authorized by this prompt.

---

## Included file: `prompts/045_third_balkan_war_goal_prompt.md`

# Goal prompt for Event 045 implementation

Implement Chaos Redux Event 045, Third Balkan War, from `docs/specs/045_third_balkan_war_specs/`. No unapproved simplification is allowed.

Keep Event 045 as Minor Fire-Once, Chaos level 1, entry `chaosx.nr45.1`, and a High-severity Wars cluster member. Require at least three valid ordinary regional governments and a coherent opposing structure. Reject openings where every candidate belongs to one faction or an existing global war makes Event 045 origin false. When valid, immediately create a multi-country war. Build two camps normally. Permit three sides only when claims and diplomacy justify the linked graph. Never oppose same-faction allies. Make setup transactional and rollback-safe.

Expose exactly one persistent custom value, Balkan War Escalation. Implement all five stages and proof gates. Time never raises it. Regional entry, support tiers, volunteers, guarantees, faction commitments, direct major intervention, hostile major pairs, theater spread, armistice violation, containment, withdrawal, and settlement use repeat-guarded changes. A threshold cannot display direct major war or Another World War without matching proof. The final stage hands control to ordinary systems. It is not a world-end scenario.

Build the accepted regional-interest and claim registry from HOI4 map evidence. Claims cannot become generic expansion rights. Use the same registry for participation, decisions, occupations, settlements, AI, achievements, and postwar memory.

Implement one phase-aware decision category with a static picture. Show escalation, stage, latest cause, next missing proof, and country role. Present three to five primary actions, never more than six, and one to three active missions. Use selected targets for country lists. Actions need real costs, clear tooltips, AI equivalents, and no more than four spendable cost types. Missions must require concrete map, military, logistics, or diplomatic work.

Implement Evolution I at 200 or more Chaos through broader registered ambitions. Implement Evolution II at 400 or more after real military and political weakening, reusing Independence Wave and Random Civil War providers where suitable. Implement Evolution III at 600 or more only when former allies have a concrete incompatible claim, occupation, settlement, ideology, or leadership dispute. Use separate dynamic pacing. Evolution activation gives zero Chaos. Disabled Evolutions cannot set flags or unlock content.

Do not duplicate shared Chaos from wars, peace, deaths, annexations, puppeting, or faction changes. Preserve Event 045 origin memory only when its linked conflict creates the first qualifying wider war. Implement all six achievements and both super-event packages with complete tracking, art, verified text, licensed audio, localisation, playback, and persistence. Complete all accepted assets. No portraits, flags, custom countries, dedicated scripted GUI, manual scenario, or 3D assets are authorized.

Before editing, read AGENTS, this package, relevant skills, offline wiki pages, vanilla documentation,. Use mandatory HOI4 MCP event and probability routes. Run the named P45 scenarios before and after weighted changes. Use bounded project subagents with explicit context. Centralize tuning, use event-owned ledgers and bounded processing, and do not add a whole-world recurring scan without explicit permission.

Completion requires evidence for validity and rollback, camp structures, fragmented maps, same-faction rejection, support anti-farming, proof-gated stages, settlements, each Evolution enabled and disabled, wider-war origin, pre-existing world-war rejection, achievements, cluster behavior, event-log surfaces, persistence, and cleanup. Update final docs and the authoritative workbook, then export its CSV snapshots. Report every fallback, blocker, and skipped meaningful validation. Mark the goal incomplete while any accepted requirement is missing.
