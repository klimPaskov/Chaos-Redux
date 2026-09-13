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
