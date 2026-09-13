# Gods of Africa

## Catalog ownership

- Parent event: `012`, **Africa Is One**
- System type: persistent Event 012 diplomatic, tribute, protection, and punishment layer
- Availability: after Africa Is One Evolution I and the consolidation delay
- Event `070`: reserved for another idea
- Normal event pool identity: none
- Cluster identity: inherited only through Event 012, with no separate cluster member

Gods of Africa is part of the African unifier's campaign. It does not receive a separate normal-event weight, separate event type, separate fire-once registration, or `chaosx.nr70.*` entry event.

## Playable promise

Africa has become capable of speaking to the great powers as one political force. Its rulers announce that the Gods of Africa have awakened through continental unity and that the world is moving toward complete Chaos. Foreign powers are told that respect, tribute, and restraint can earn protection. Refusal creates a growing risk that Africa, Chaos, or the Gods will answer.

The system gives every major and every player-controlled country a long relationship with the African unifier. A participant receives changing demands, decides how far to comply, watches its own Wrath rise or fall, and judges whether current Gods of Africa Strength makes the threat credible. Africa gains real equipment, fuel, transport, industry, political concessions, and strategic space from compliance. The relationship can mature into friendship, remain a managed bargain, collapse into hostility, or end in open defiance.

The core tension comes from uncertainty about the source of punishment. A disrupted railway may be sabotage. A storm may be an ordinary disaster that arrived at an impossible moment. A military collapse may come from African intelligence, local unrest, or something no government can explain. The player can see the current Strength and personal Wrath, but cannot see a precise formula that predicts every consequence.

## Design judgment

The source concept works when Africa's threats remain tied to African capability. Without that limit, the system would give a weak unifier arbitrary power over stronger countries and would make both public values meaningless. Gods of Africa Strength therefore sets the maximum practical punishment tier. Wrath controls how strongly the system tries to punish a participant inside that ceiling.

The system also needs reciprocity. A long compliance route cannot consist only of repeated losses. Loyal countries eventually receive protection, aid, access, and a large final settlement. Those rewards arrive gradually enough that the player still pays a real price for obedience.

The public interface uses two values only. Extra history, capacity, need, reliability, offense, recent punishment, and relationship facts remain hidden. The player receives clear causal feedback through demand text, reports, tooltips, diplomatic behavior, and visible outcomes without gaining a third meter.

## Identity and cultural boundary

### Fictional state doctrine

The Gods of Africa are a fictional Chaos Redux doctrine formed after continental unification. They are not presented as a historically real shared African pantheon. Africa contains many religious traditions, including indigenous traditions, Christianity, Islam, Judaism, Hindu traditions, and many forms of mixed practice. The system must avoid treating these traditions as one old religion or using a collage of unrelated sacred symbols as proof of authenticity.

The African unifier claims that continental unity has given a common voice to powers that were previously understood through many local languages, practices, faiths, and political traditions. That claim is part of the new state's ideology. It can be accepted literally, treated as a political myth, interpreted through existing local faiths, or rejected by people inside Africa. The game does not need to settle which interpretation is correct.

### Public claim

The Gods describe themselves as the true gods and claim that complete Chaos will consume the world. Their public doctrine states that a united Africa has been chosen to organize resistance, demand restitution, and judge foreign interference. Tribute is framed as support for continental survival, repayment for exploitation, proof of respect, or obedience to a divine order depending on the demand and the current relationship.

### Internal African interpretations

The African unifier should have a doctrine choice that changes how it uses the system without adding another public value.

#### Reciprocal covenant

The state presents tribute as a mutual compact. Demands favor concrete African needs, loyal countries receive more protection, negotiation remains useful, and the best final friendship rewards become stronger. Punishments still exist, but the AI avoids destroying countries that have a long cooperative record.

#### Sovereign exaction

The state presents tribute as an owed payment. Demands become larger, refusal raises Wrath faster, Africa receives more immediate material gain, and punitive routes become easier to justify. Foreign defiance becomes more common and the hidden friendship route becomes harder to reach.

#### Strategic ambiguity

This may be retained as a secondary policy inside either doctrine. The leadership refuses to define whether the Gods act through divine force, African institutions, or Chaos. This policy improves bluffing and diplomatic uncertainty. It does not permit punishment above the Strength ceiling.

These are working design labels. Final player-facing names require localisation research and should not borrow names from real deities or sacred offices without a specific source and cultural reason.

### Persistent personalities

The Gods should feel like recurring speakers. The system can achieve this through a small set of fictional voice roles that determine tone and demand family. The roles are not public meters and do not form a collectible roster.

| Working voice role | Main subject | Low-Wrath manner | High-Wrath manner |
| --- | --- | --- | --- |
| The Keeper of Oaths | recognition, agreements, access, diplomacy | formal and patient | accusatory and humiliating |
| The Provider | equipment, fuel, convoys, industry | practical and reciprocal | exacting and suspicious |
| The Shield | protection, mutual defense, African wars | protective and urgent | condemns abandonment |
| The Witness | occupation, colonial territory, broken promises | grave and evidentiary | names offenses and demands restitution |
| The Hand of Judgment | punishments and final defiance | restrained and distant | direct and punitive |

Final names should be newly written fictional titles. Their visual symbols should use one coherent state-designed system. They should not combine unrelated religious objects from several regions.

## Availability and activation

### Required conditions

Gods of Africa can activate only when all of the following are true:

- Africa Is One has fired.
- The African unifier exists as a valid country.
- Africa Is One Evolution I is active and enabled.
- The unifier has survived the consolidation delay.
- The unifier is not in a terminal defeat or dissolution state.
- The Event 012 continental campaign has not already reached its final secured-Africa settlement.

### Consolidation delay

The normal delay is approximately 180 days from the establishment of the African unifier. The delay begins from the authoritative Event 012 establishment proof, not from a guessed date or a second duplicate flag.

The delay represents institutional consolidation. The unifier needs time to establish a continental capital, communication network, diplomatic service, military chain of command, and common doctrine before it can issue credible demands to the world.

The activation should use one owner-managed delayed event or a bounded mission attached to the African unifier. It should not poll every country each day.

### Delayed activation under weak conditions

The system may activate while Africa remains weak. Weakness does not cancel the public doctrine. It limits Gods of Africa Strength and therefore limits punishment.

A unifier facing immediate capitulation, severe internal collapse, or loss of its capital may postpone the proclamation until it regains a minimum operating condition. This postponement prevents a broken country from opening a global interface that will end a few days later. The delay must have a maximum review interval so the system does not become permanently lost after recovery.

### Participant enrollment

At activation, every valid country in either of these groups becomes a participant:

- current major countries
- current player-controlled countries

The African unifier is excluded from its own participant list.

A country that qualifies through both groups receives one participant record.

A country that becomes a major or becomes player-controlled later should be enrolled through a bounded onboarding check. The preferred route is an Event 012 registry refresh from one owner scope at a low cadence, combined with direct registration when a player takes control where the project already exposes such a hook. The system must not add an unrestricted all-country daily action.

Once enrolled, a surviving country remains a participant even if it later loses major status. This prevents a country from escaping the system through temporary loss of major rank. Annexed or invalid participants are archived and removed from the active queue.

### Initial introduction

Each participant receives one introduction that explains:

- the African unifier now speaks on behalf of the Gods
- Gods of Africa Strength is global
- Wrath of the Gods belongs to that participant
- demands can recur indefinitely
- compliance transfers real resources to Africa
- refusal may cause punishment inside the current Strength ceiling
- permanent defiance stops ordinary demand calls and abandons the normal friendship route

The introduction should not reveal exact hidden relationship weights, punishment formulas, rare outcomes, or the final settlement threshold.

## System lifetime

The system remains active while the African unifier exists and the Event 012 campaign remains unresolved.

It can end in four ways:

1. Africa secures the continent according to the authoritative Africa Is One victory definition.
2. The African unifier is destroyed or dissolved.
3. A participant defeats and capitulates the African unifier, ending the system for that victor even if a successor African state survives elsewhere.
4. Event 012 enters a terminal route whose own settlement replaces the tribute cycle.

Ordinary demand generation stops as soon as an ending is committed. Active demands are cancelled before final settlement events are issued.

## The two public values

### Gods of Africa Strength

Gods of Africa Strength is one global value shared by all participants. It measures the combined credibility, reach, and destructive capability behind the Gods' threats.

It is displayed on a 0 to 100 scale. The exact component weights remain hidden, but the player should receive a concise explanation of the main current causes.

Suggested design bands:

| Range | Working band | Practical meaning |
| --- | --- | --- |
| `0 to 19` | Limited | Africa can pressure, bluff, disrupt locally, and cause small incidents |
| `20 to 39` | Regional | Africa can sustain covert action, limited disasters, and focused economic or military disruption |
| `40 to 59` | Continental | Africa can damage several states, sustain larger intervention, and back demands with serious power |
| `60 to 79` | Global | Africa can reach major powers, coordinate repeated punishment, and cause national crises |
| `80 to 100` | Extreme | Catastrophic punishment becomes possible when Wrath, Chaos, offense history, and escalation also qualify |

The band names are working labels. Final text should describe credibility and reach without presenting a technical damage table.

#### Strength sources

Strength should be derived from these factor families:

- African military power relative to the world
- deployed army, reserve manpower, equipment condition, and supply sustainability
- military industry, civilian industry, dockyards, transport, fuel, and construction capacity
- air and naval reach
- technology and strategic capabilities
- control of African core territory
- control of continental capitals, ports, rail corridors, and strategic resources defined by Event 012
- stability, war support, surrender condition, and internal cohesion
- current wars and whether Africa is winning or losing
- active foreign bases and occupied African territory
- current global Chaos tier
- Africa Is One evolution state
- Event 012 routes that improve diplomacy, intelligence, disaster response, covert reach, or military projection
- accepted owner systems that can genuinely support the threat

Strength must not be a copy of division count. A large but unsupplied army should contribute less than a smaller force with industry, fuel, transport, air cover, and continental control.

#### Strength losses

Strength should fall when:

- Africa loses large areas of the continent
- its industrial base or transport network collapses
- its army suffers severe equipment or manpower shortages
- its capital or key continental institutions are lost
- its surrender progress becomes critical
- its stability or internal condition deteriorates
- foreign powers destroy the capabilities used to carry out threats
- Event 012 reversals disable relevant systems

Strength should respond gradually to ordinary fluctuations and quickly to major defeats. This prevents daily oscillation while preserving the meaning of a destroyed fleet, lost capital, or collapsed front.

#### Chaos contribution

Chaos increases the credibility of unexplained or supernatural consequences. It cannot make a powerless Africa fully omnipotent. The Chaos contribution is therefore an amplifier with a fixed share of the Strength calculation, not a replacement for African capability.

At high Chaos, a strong Africa can access stranger punishment channels and wider effects. At low Chaos, the same Africa relies more heavily on diplomacy, intelligence, sabotage, military pressure, and ordinary disasters.

### Wrath of the Gods

Wrath of the Gods is tracked separately for each participant on a 0 to 100 scale.

Suggested design bands:

| Range | Working band | Relationship behavior |
| --- | --- | --- |
| `0 to 14` | Calm | modest requests, long patience, higher chance of protective or friendly treatment |
| `15 to 29` | Watchful | normal demands and clear reminders of past conduct |
| `30 to 49` | Angered | larger demands, shorter patience, more punitive wording |
| `50 to 69` | Hostile | severe demands, frequent verification, credible punishment risk |
| `70 to 84` | Vengeful | major punishment becomes likely when Strength permits it |
| `85 to 100` | Condemning | extreme consequences become eligible only under the full capability and escalation gates |

#### Wrath gains

Wrath rises from:

- direct refusal of a valid demand
- failure to complete a timed demand
- deliberate underpayment or cancellation of a promised transfer
- repeated requests for delay without later compliance
- war against the African unifier
- occupation of African territory
- ownership or control of African core territory after a return demand
- support for a current enemy of Africa
- attacking an African ally under a recognized protection agreement
- breaking a signed agreement with Africa
- hostile diplomatic action
- sabotage or intelligence action that the African unifier can prove
- public mockery or repudiation of the Gods when a route deliberately chooses provocation
- returning to hostility after a prior reconciliation

Routine world politics should not raise Wrath. The system should respond to conduct that affects Africa or directly rejects the Gods' authority.

#### Wrath reductions

Wrath falls from:

- completing demands in full
- completing a negotiated substitute
- voluntary aid outside an active demand
- returning African territory
- ending a hostile war
- helping Africa in a major conflict
- defending African territory or allies
- honoring a difficult agreement over time
- accepting a costly reconciliation settlement
- providing emergency relief when Africa faces disaster, famine, or transport collapse

A single large payment should not erase a long record of war, occupation, and broken agreements. Reductions affect current Wrath, while permanent hidden grievances can remain relevant to final friendship.

#### Wrath floors and safeguards

Certain conditions impose a temporary floor:

- active war with Africa
- current occupation of African core territory
- permanent defiance
- an unresolved broken treaty
- a recent extreme offense

The floor prevents a country from paying one demand while continuing the behavior that caused the conflict.

### Clear public feedback without a third meter

The player should receive qualitative relationship cues through:

- the manner of demand text
- whether Africa offers negotiation or insists on exact payment
- whether a request is framed as ceremony, aid, debt, restitution, or punishment
- diplomatic opinion and AI behavior
- periodic reports that mention remembered cooperation or unresolved offenses
- availability of protective aid
- the final outcome event

No separate public loyalty, favor, covenant, standing, trust, or friendship number is added.

## Hidden relationship memory

The final relationship uses a hidden record that cannot be solved through one exact visible threshold.

The record should include:

- total demands completed
- proportion of demands completed
- consecutive compliance streaks
- negotiated substitutes honored
- voluntary aid episodes
- emergency aid provided when Africa was losing or suffering disaster
- African territory returned
- time spent at low Wrath
- time spent at high Wrath
- wars against Africa
- African territory occupied
- allies of Africa attacked
- agreements broken
- permanent defiance
- reconciliation attempts and whether they were completed
- severe punishments already suffered
- current diplomatic alignment
- final campaign conduct during continental consolidation

The system should preserve permanent negative marks for major war, occupation, betrayal, and defiance. It should also preserve permanent positive marks for exceptional voluntary aid and defense of Africa.

The hidden record may use several internal values because the two-value limit applies to player-facing state. These internal values should feed final outcomes, AI behavior, demand tone, and rare protective events.

## Core tribute loop

### One active demand per participant

A participant can have only one ordinary active demand. This is a hard clarity and exploit rule.

When a demand is active, its mission shows:

- what Africa requires
- the amount or diplomatic condition
- the deadline
- the immediate consequence of compliance
- the broad consequence of refusal or failure
- whether substitution or extension is allowed
- the current Strength and personal Wrath

A second ordinary demand cannot be issued until the first is resolved or cancelled.

### Demand cadence

The normal participant cooldown should vary between roughly 90 and 210 days.

The cooldown becomes shorter when:

- Wrath is high
- Africa faces a genuine emergency
- Event 012 has reached later evolutions
- the participant repeatedly obstructs small demands
- the participant occupies African territory

The cooldown becomes longer when:

- the participant has complied repeatedly
- Africa has no urgent need
- the participant recently provided major voluntary aid
- a serious punishment recently occurred
- the participant is temporarily incapable of meaningful payment
- the world already has too many active Gods demands for readable multiplayer play

A global dispatch budget should stagger demands across participants. The system should avoid sending many human players popups on the same day.

### Africa's current needs

Before selecting a demand, the system builds a hidden need profile for the African unifier. It should consider:

- infantry and support equipment deficits
- artillery, truck, train, convoy, tank, and aircraft deficits
- fuel reserve and expected consumption
- current war and front condition
- transport and supply pressure
- construction and repair needs
- resource shortages
- naval and air vulnerability
- available manpower and reinforcement pressure
- continent-control priorities
- active disaster, famine, migration, or reconstruction pressure
- diplomatic isolation
- foreign bases and occupied African territory

The need profile should discourage repeated requests for a stockpile Africa already has in excess.

### Target capacity

The system builds a hidden capacity profile for the participant. It should consider:

- current and expected equipment stockpiles
- equipment production and monthly output
- manpower reserve and fielded army needs
- fuel reserve and consumption
- convoys and trains above protected operating floors
- civilian and military industry
- current war, surrender progress, and active fronts
- trade and resource position
- ability to use lend-lease or direct transfer mechanics
- autonomy, subject, faction, and access restrictions
- recent demands already paid
- severe disasters or economic collapse
- DLC availability and valid engine mechanics

A demand should draw from usable capacity above a protected floor. The system may still make a painful request, especially at high Wrath, but it should not routinely ask for an impossible amount or select a family the participant cannot use.

### Demand severity

The design relationship is:

**Demand Severity = Target Capacity + Wrath + Gods of Africa Strength + Chaos + Current African Need + Conduct History**

The terms are weighted and bounded. Target capacity and current need establish what can be asked. Wrath and Strength determine how aggressive Africa can be. Chaos and conduct history alter patience, tone, and the upper demand band.

Suggested burden bands use a share of usable capacity above the protected floor:

| Demand band | Typical share of usable reserve | Typical role |
| --- | --- | --- |
| Ceremonial | `2 to 5 percent` | low Wrath, symbolic test, early relationship |
| Standard | `5 to 10 percent` | ordinary material support |
| Severe | `10 to 20 percent` | high need, high Wrath, major power target |
| Emergency | `15 to 30 percent` | Africa is losing a major war or facing a severe crisis |
| Punitive | `20 to 40 percent` | repeated refusal with high Strength and a valid offense history |

The final amount should be rounded to readable multiples appropriate to the resource. A percentage should never appear as a demand for fractional equipment.

### Demand deadlines

Deadlines should fit the action:

- ceremonial and simple political demands: about 45 to 90 days
- normal equipment and fuel transfers: about 60 to 120 days
- heavy equipment, aircraft, trains, or industrial commitments: about 90 to 180 days
- emergency wartime support: about 30 to 60 days
- territorial withdrawal and diplomatic realignment: about 60 to 180 days depending on war state

Distance, route access, war, convoy availability, and transfer method may alter the deadline. The same duration should not be used for every demand.

## Demand families

### Infantry and support equipment

Africa requests rifles, support equipment, artillery, trucks, or other compatible land equipment.

Selection rules:

- the target must own a transferable compatible token
- a protected reserve remains available for the target's fielded army and reinforcement need
- Africa should have a current deficit or a route reason for the request
- obsolete and current equipment can be accepted through a weighted compatibility rule
- high-Wrath Africa may reject a shipment composed entirely of obsolete material

Possible negotiated substitutes include another land-equipment family, fuel, trucks, trains, convoys, or an industrial commitment.

### Tanks and armored equipment

This family becomes common after Africa Is One Evolution II or when Africa has a proven armored-equipment need.

The request should scale from the target's actual production and stockpile. A weak major without armored production should not receive a tank demand merely because the family exists.

### Aircraft

Aircraft demands respond to African air deficits, enemy bombing pressure, active wars, and later Event 012 evolutions.

The selector should distinguish broad role families where the implementation can transfer valid equipment safely. The player should not be asked for a plane archetype that its current version or DLC cannot identify.

### Fuel

Fuel demands can be large because fuel is a strategic bulk resource and the decision skill does not require conservative fuel values.

The target must retain a protected operating floor based on army, air, naval, and convoy activity unless the demand is explicitly punitive. Africa should prioritize fuel during active mechanized, naval, or air wars.

### Convoys and trains

Transport demands respond to African supply deficits, overseas commitments, damaged rail networks, and reconstruction.

A target keeps a minimum convoy or train reserve needed for active supply and trade. Punitive demands may approach that floor but should clearly warn the player about the cost.

### Industrial support

Industrial tribute should create a timed civilian-factory burden, construction contribution, repair program, or direct economic support that the engine can prove.

The player-facing action should state the duration and burden. It should not hide an indefinite consumer-goods penalty behind a vague promise.

Possible uses include:

- rebuilding African railways
- repairing ports and supply hubs
- constructing factories or airfields in Event 012 priority states
- supporting continental resource extraction
- funding disaster recovery
- sustaining a major African war effort

### Strategic resources

Resource demands should use valid trade, rights, extraction, or industrial mechanisms. A demand should not claim that a resource was transferred if the engine cannot represent the transfer.

Possible forms include:

- temporary preferential trade
- resource rights in a controlled state
- industrial allocation that simulates a purchase
- a production burden tied to the resource type
- ending an embargo against Africa

DLC mechanics may provide a more exact route, but the family needs a base-game path.

### Manpower and military assistance

This family is available only when a valid implementation can prove a real transfer or commitment.

Possible forms include:

- expeditionary forces
- volunteers
- a timed manpower grant through an accepted owner helper
- training cadres
- garrison support
- defense of a named African front or state group

A vague manpower payment should not remove population without creating a valid receiving effect.

### Lend-lease and continuing support

A demand can require a continuing aid agreement for a fixed period when the game can verify delivery. The system should not depend on a native lend-lease agreement that script cannot reliably inspect or cancel.

Where exact inspection is unavailable, use an Event 012 owned periodic transfer contract with declared amounts and a clear deadline.

### Diplomatic recognition

Recognition demands are useful when Africa is consolidating, isolated, or contesting a rival claimant.

Possible outcomes include:

- a recognition flag and opinion change
- removal of a hostile recognition status
- a public guarantee
- support for Africa in an Event 012 conference or settlement
- formal acceptance of the African unifier's territorial claim

Recognition should influence other countries and Event 012 diplomacy. It should not exist as an empty popup choice.

### Military access and basing

Africa may request access, port use, air transit, docking rights, or removal of foreign access from an African enemy.

The demand must check whether the requested diplomatic action is valid. It should avoid asking a participant to grant access that the engine already grants through faction or subject status.

### Withdrawal from African territory

This is one of the most important demand families.

A participant that controls African core territory can be ordered to:

- return specific states
- release an Event 012 claimant
- transfer occupation to the African unifier
- accept a withdrawal timetable
- stop building or expanding a foreign base

The demand must name the exact states or a clearly defined state group. It cannot say only that Africa wants its land back.

Compliance produces a major Wrath reduction and a strong hidden positive mark. Refusal creates a high Wrath gain and unlocks stronger retaliation within the Strength ceiling.

### End support for an enemy of Africa

The target may be ordered to stop:

- equipment aid
- volunteers
- guarantees
- basing
- recognition
- intelligence support
- faction sponsorship

The implementation must check which forms of support can be detected and ended. Unsupported forms should not appear in the demand pool.

### Alliance and faction concessions

Later Event 012 evolutions may allow demands to:

- leave a hostile faction
- join an African-led bloc
- sign a non-aggression pact
- guarantee Africa or an African ally
- recognize an African security arrangement
- end a guarantee of an African enemy

These are high-impact demands. They should require high Strength, a relevant diplomatic situation, and route support from the African unifier.

### Ceremonial tribute

Ceremonial demands are smaller and provide variety at low Wrath or after long compliance.

They can use a modest material shipment, a short industrial commitment, a diplomatic ceremony, or a public recognition action. They should still produce a real effect and should not become filler that repeatedly consumes attention.

### Emergency appeals

When Africa is losing a major war, facing a catastrophic disaster, or nearing supply collapse, the system may issue an emergency demand.

Emergency appeals have:

- a short deadline
- a strong need-based family weight
- high hidden relationship value for compliance
- a limited Wrath penalty for refusal when the target is also in crisis
- a larger penalty when a favored or allied country abandons a clear obligation

This family supports a genuine friendship route because loyalty matters most when Africa is under pressure.

## Participant response model

During an active demand, the normal player-facing phase exposes no more than five primary actions.

### Fulfill the demand

The participant transfers or commits the requested amount.

Effects:

- the demand resolves successfully
- Wrath falls
- hidden long-term standing improves
- Africa receives the material or concession
- the next demand cooldown increases
- the chance of protective treatment rises
- a compliance report is sent to Africa

The decision must verify the cost at click time and debit it once.

### Propose a substitute

The participant offers another demand family of similar burden.

The system should present up to three valid substitutes chosen from current capacity and African need. The player should not navigate a long store of every possible resource.

Africa's acceptance depends on:

- current need
- value of the substitute
- Wrath
- doctrine route
- prior negotiation reliability
- whether the participant is trying to dump obsolete or useless material

A rejected substitute does not immediately count as refusal. It consumes time and may raise Wrath slightly if the offer was poor.

### Request an extension

The participant asks for more time.

An extension may require one or two costs that fit the action, such as political effort, an upfront partial shipment, a temporary diplomatic concession, or a small increase in the final amount. It should not use more than four cost types.

Acceptance is more likely at low Wrath, after a long compliance record, or when the transfer route is genuinely disrupted. Repeated extensions become harder.

### Refuse

The participant rejects the current demand but remains inside the recurring system.

Effects:

- Wrath rises
- the hidden refusal count rises
- punishment is evaluated
- the participant can receive future demands
- the final friendship route remains possible in principle, but repeated refusal damages it

The player should see the broad current risk based on Strength and Wrath. The exact punishment roll remains hidden.

### Defy the Gods

Defiance is a permanent strategic commitment under normal conditions.

Effects:

- ordinary recurring demands stop
- Wrath rises to a high floor
- a permanent defiance mark is set
- the normal favored friendship route closes
- Africa treats the country as openly hostile
- punishments can continue
- later Event 012 evolutions may unlock sanctions, covert action, alliances against the target, war goals, or intervention

The action requires a confirmation window because it changes the long-term campaign.

### Voluntary offering

Outside an active demand, a participant may receive one optional aid action when it has a meaningful reason to help Africa. This action should not remain permanently visible.

Valid moments include:

- African emergency war
- major disaster
- famine or migration crisis
- severe transport collapse
- final continental campaign

Voluntary aid reduces Wrath, creates a hidden positive mark, and can unlock future protection. It should have a cooldown and a meaningful cost to prevent relationship farming.

## Negotiation and partial outcomes

Demands should support partial success when the action can be measured.

Possible outcomes:

- full compliance
- accepted substitute
- accepted extension followed by compliance
- partial shipment with a remaining balance
- negotiated reduction in exchange for a diplomatic concession
- failed negotiation followed by refusal
- missed deadline
- fraudulent or cancelled payment

Partial payment should not silently count as full compliance. It can reduce the Wrath gain from failure and preserve some hidden goodwill.

Africa's AI should compare the offered value with current need. A country cannot satisfy an aircraft emergency by offering a trivial political concession unless the system rates that concession as genuinely valuable.

## Africa-side gameplay

The African unifier receives its own decision layer. It should not become a target-by-target spreadsheet.

### Continental priority

Africa can select one current need priority from a small valid set, such as:

- land equipment
- fuel and transport
- air defense
- industrial repair
- continental liberation
- emergency relief

The priority changes demand-family weights and protective spending. It does not let the player set arbitrary amounts.

Only one priority is active at a time. Changing it has a cooldown or a modest institutional cost.

### Grant leniency

Africa can reduce or postpone one selected participant's demand when that country has a cooperative history, faces a genuine crisis, or offers a strong substitute.

Leniency lowers immediate tribute but improves hidden relationship value and can prevent unnecessary defiance. The extractive doctrine makes leniency more costly or less available.

### Mark a priority offender

Africa can select one participant with a proven offense, such as occupation of African territory, war, betrayal, or repeated refusal.

The action increases that target's demand and punishment priority. It does not increase the maximum punishment tier above current Strength.

Only one or a small number of priority offenders may be active. This prevents manual harassment of every country.

### Protect a reliable country

Africa can spend equipment, fuel, convoys, political capital, or military commitment to aid a participant with a strong hidden cooperation record.

Possible aid includes:

- equipment transfer
- expeditionary force
- guarantee
- disaster relief
- reconstruction help
- convoy support
- famine or migration assistance through accepted owner APIs

Protection should be a real cost to Africa. It proves that the friendship route has value before final settlement.

### Issue a public pardon

Africa may clear a temporary Wrath floor after a war ends, territory is returned, or a reconciliation settlement is completed.

A pardon does not erase permanent hidden grievance marks. It allows the normal demand cycle to resume under a distrusted relationship.

### Escalate a proven offense

Africa may accelerate punishment review when a participant is at war with Africa, occupies African territory, attacks a protected ally, or breaks a formal agreement.

The action cannot create a punishment family that current Strength, Chaos, and escalation history do not support.

## Punishment architecture

### Governing rule

Punishment intent and punishment capability are calculated separately.

**Desired Punishment = Wrath + Failure History + Offense Severity + Failed Demand Severity + Chaos + Current Hostility**

**Maximum Punishment = Gods of Africa Strength Band + Valid African Capability + Event 012 Evolution Access**

**Applied Punishment = the lower valid result after target-condition, repetition, and cooldown checks**

This is the central balance invariant.

### Punishment tiers

#### Tier I: pressure and limited disruption

Maximum at low Strength.

Possible effects:

- temporary diplomatic pressure
- public unrest
- small stability or war-support loss inside a larger event package
- limited production disruption
- minor sabotage
- a small accident
- a local supply interruption
- a failed ritual or embarrassing omen
- a propaganda scare
- a modest stockpile loss
- one small natural-disaster call when Event 013 accepts it

The presentation may sound grand while the effect remains limited. This contrast should come from concrete outcome text, not from a joke that mocks African belief.

#### Tier II: focused operational damage

Available from regional Strength.

Possible effects:

- damage to buildings in one or a few valid states
- temporary rail or supply disruption
- loss of equipment from one force category
- port or convoy disruption
- a moderate local disaster
- covert support for unrest
- a limited military-readiness penalty
- temporary industrial burden

#### Tier III: multi-state crisis

Available from continental Strength.

Possible effects:

- infrastructure and factory damage across several states
- severe supply disruption
- significant equipment losses
- disruption of airfields, ports, or rail hubs
- a medium natural-disaster sequence
- loss of organization or planning across a large part of the military
- regional population displacement through the migration system when valid
- a major diplomatic isolation campaign

#### Tier IV: national catastrophe

Available from global Strength and high Wrath.

Possible effects:

- several coordinated disasters
- large state-building destruction
- substantial military losses
- prolonged economic damage
- collapse of transport in a major region
- severe population loss through exact population accounting
- repeated sabotage and local uprisings
- African-led sanctions or war preparation

Tier IV requires repeated failure or a major direct offense. It should not follow one ordinary refusal.

#### Tier V: existential punishment

Available only from extreme Strength under the full gate.

Required conditions should include all of the following:

- very high Wrath
- extreme Gods of Africa Strength
- high global Chaos
- repeated serious failures or a major offense such as war and occupation
- Event 012 evolution access
- no recent Tier V punishment against the same target
- Africa is not near collapse
- the target still exists and has enough population or infrastructure for a meaningful sequence

Possible effects include:

- destruction across most major population and industrial centers
- collapse of national infrastructure
- enormous military losses
- several regional catastrophes
- loss of a large majority of civilian population in the rare maximum route

The maximum population route should be staged through an emergency sequence. The participant receives a final opportunity to return territory, end war, accept surrender terms, or pay an extraordinary settlement. Failure then applies exact state population losses in waves with a protected minimum population floor. The Deaths system records each applied loss once.

The route must never delete the whole country through one unexplained command. The player should understand that the system has reached its highest public risk band.

### Punishment family selection

The selector should prefer consequences connected to the offense and African capability.

Examples:

- occupation of African territory favors military, supply, uprising, and diplomatic retaliation
- refusal of equipment tribute favors stockpile, production, or military disruption
- broken protection agreements favor diplomatic isolation and alliance consequences
- high-Chaos hostility may favor natural disaster or unexplained catastrophe
- war against Africa favors direct strategic retaliation

The system should track recent punishment families and avoid repeating the same catastrophe without a reason.

### Target condition

Punishment should account for the target's size and current condition.

A country already near capitulation should receive a strategically meaningful effect without needless duplicate destruction, unless it entered the extreme route through deliberate escalation. A large major can absorb wider effects than a small player country.

Target-condition scaling must not lower the Strength ceiling. It adjusts which valid consequence fits the target.

### Bluff outcomes

At low Strength, some threats should fail or produce smaller results.

Possible outcomes include:

- the promised storm weakens before landfall
- local saboteurs cause limited damage
- a predicted military collapse becomes a short supply failure
- a ritual receives attention but no proven effect
- frightened markets cause a temporary disruption

A bluff outcome can still raise tension and influence AI. It must not secretly apply a high-tier effect under another name.

### Attribution

Punishments may have different public attribution states:

- openly ordered African action
- suspected African covert action
- unexplained event claimed by the Gods
- ordinary disaster interpreted through the system
- confirmed Chaos manifestation

Direct African military, sabotage, CBRN, or atrocity action should use existing Condemnation rules when applicable. An ambiguous natural disaster does not automatically create condemnation against Africa without evidence.

### Natural Disasters integration

Gods of Africa should call the Event 013 `call_natural_disaster` gateway with documented inputs.

The owner system remains responsible for:

- selecting a valid participant and broad punishment tier
- setting origin and attribution context
- checking recent-family repetition
- interpreting the returned result
- applying Wrath and history consequences
- issuing the Gods-specific report

Event 013 remains responsible for disaster validation, target resolution, impact, aftermath, and cleanup.

A rejected disaster call fails closed. The system should select another valid punishment family or record a failed manifestation. It should not apply an unvalidated disaster directly.

### Deaths and population accounting

Any punishment that removes civilian population must use the shared exact civilian-population transaction.

Requirements:

- one exact debit per state and wave
- a protected minimum remaining population
- one Deaths reason assigned to the punishment family
- no recruitable-manpower credit retained from the state-population reduction
- no duplicate Chaos award for deaths already counted by the shared system
- no second debit by migration for the same cohort

### Chaos handling

Routine demands, compliance, refusal, and Wrath movement should not directly change Chaos.

Concrete disasters, wars, annexations, deaths, contamination, and other shared causes continue through their owner systems.

Event 012 may record one-shot Chaos milestones for a first proven global punishment, a first Tier V sequence, or another distinct event-owned consequence. Those milestones must not duplicate the generic effects caused by the punishment.

## Protection and favor

### Protection eligibility

Protection can occur when a participant has:

- low current Wrath
- a strong hidden compliance record
- voluntary aid history
- no active war against Africa
- no unresolved occupation of African territory
- no permanent defiance

The exact eligibility remains hidden. The player learns through offers and Africa's conduct.

### Protection families

Possible benefits include:

- African equipment or fuel transfer
- expeditionary forces
- guarantee or alliance support
- reconstruction after a disaster
- convoy or transport support
- intelligence sharing
- favorable trade
- relief access
- famine assistance
- migration reception or evacuation support
- diplomatic support in a crisis
- reduced demand severity
- longer deadlines
- accepted substitution

Protection should draw from Africa's real capacity. A weak Africa may offer symbolic support, diplomacy, or a modest shipment. A dominant Africa can send a large expeditionary army or major reconstruction aid.

### Protective intervention against disaster

The Gods may claim to have reduced a disaster's severity for a reliable participant. Mechanically, this should use Event 013 mitigation or aftermath hooks where available. It should not cancel unrelated owner systems through ad hoc flags.

### No protection farming

A participant cannot repeatedly send tiny aid shipments to farm protection.

Voluntary aid requires:

- a valid African need
- a meaningful capacity-scaled contribution
- a cooldown
- one hidden credit per incident or threshold
- diminishing relationship gain from repeated identical transfers

## Defiance and reconciliation

### Permanent defiance route

Defiance stops ordinary demands and changes the relationship into an open contest.

The participant receives:

- a high Wrath floor
- hostile African diplomacy
- continued punishment review
- possible sanctions and war routes at later Event 012 evolution stages
- access to defensive decisions that help survive sabotage, disaster, isolation, and African pressure

Defiance should create active play. The participant may prepare infrastructure, counterintelligence, relief reserves, alliances, air defense, continental diplomacy, or a war against Africa.

### Defensive preparation

Defiant countries can receive a small decision family based on the current threat:

- reinforce critical transport nodes
- harden disaster response
- investigate African networks
- secure stockpiles
- build diplomatic support against retaliation

These actions cost real resources and reduce the chance or impact of compatible punishment families. They cannot reduce the Strength ceiling itself unless they destroy or contain the underlying African capability.

### Rare reconciliation

A defiant country may regain entry only through a costly route after a major political or strategic change.

Suggested conditions:

- no active war with Africa
- all occupied African core territory returned
- current government differs from the one that declared defiance, or a major reconciliation focus has completed
- a large reparations or aid package is paid
- Africa accepts the request
- no unpardonable terminal offense remains

Reconciliation removes permanent demand opt-out, reduces Wrath to a high but manageable band, and sets a permanent prior-defiance mark. It does not restore the favored route immediately.

## War with Africa

Ordinary tribute calls should pause during active war between a participant and the African unifier. The relationship is handled through wartime demands, punishment, surrender, territory, and diplomacy.

Possible wartime content includes:

- demands to withdraw from African states
- surrender terms
- release of African claimants
- end of support for African enemies
- prisoner or equipment exchanges
- ceasefire offers
- retaliation missions

Wrath remains at a war floor and continues to respond to occupation, attacks on protected allies, and broken truces.

A participant that capitulates Africa ends the Gods system for itself. Existing demands and punishments against that victor stop. The victor receives a defeat report and a permanent hidden historical result.

If the African unifier survives through a successor, government-in-exile, or Event 012 restoration route, the Gods do not automatically regain authority over the victor. Restoration requires a separate Event 012 re-legitimation milestone.

## Africa secures the continent

### End of tribute cycle

When the authoritative Event 012 victory condition says that Africa has secured the continent, ordinary demands stop.

The doctrine states that foreign tribute was required to survive unification, remove outside control, rebuild continental power, and prepare for Chaos. Once those aims are secured, the relationship becomes a permanent settlement.

### Final evaluation

Every surviving participant is evaluated from:

- current Wrath
- full compliance ratio
- compliance streaks
- voluntary aid
- emergency aid
- war and occupation history
- broken agreements
- territory returned
- permanent defiance
- reconciliation
- support during the final continental campaign
- Africa's doctrine route
- Africa's final Strength

No single final payment guarantees the highest result.

### Favored by the Gods

Requirements are based on sustained cooperation, low Wrath, no unresolved major hostility, and a strong positive hidden record.

Possible settlement rewards:

- alliance or invitation into an African-led security structure
- a large expeditionary army
- major equipment transfer
- manpower or military assistance through a valid route
- favorable trade and resource agreements
- guarantee
- strategic cooperation
- shared disaster response
- privileged entry into a later World Is One constitutional route

The reward scales with Africa's final capability and the participant's contribution. A country that funded Africa for years should receive a material result large enough to affect the late campaign.

### Respected

This outcome fits mixed but generally cooperative histories.

Possible rewards:

- improved relations
- limited trade
- guarantee or non-aggression pact
- modest equipment support
- limited disaster or relief cooperation
- observer status in an African-led institution

### Distrusted

This outcome fits inconsistent participants that avoided becoming a major enemy.

Results:

- no large reward
- ordinary diplomacy remains possible
- negative memories persist
- future Event 012 diplomacy weighs the record

### Enemy of the Gods

This outcome fits war, occupation, permanent defiance, repeated refusal, betrayal, or extreme Wrath.

Possible consequences:

- long-term hostility
- diplomatic isolation
- sanctions
- African guarantees for the target's enemies
- later confrontation
- exclusion from World Is One negotiations
- continued retaliation through Event 012 content where valid

The end of ordinary tribute does not require Africa to forgive an enemy.

## Africa Is One evolution integration

### Evolution I

Evolution I unlocks the system after the consolidation delay.

Available content:

- equipment, fuel, convoy, train, industrial, recognition, territory, and basic diplomatic demands
- one active demand per participant
- low and medium punishment tiers according to Strength
- basic protection and leniency
- hidden final-relationship memory

Evolution I does not guarantee high Strength.

### Evolution II

Evolution II expands material and logistical reach.

New or stronger content:

- tanks and aircraft demands
- larger industrial programs
- reconstruction and continental infrastructure support
- continuing transfer contracts
- stronger protection packages
- improved demand matching to African deficits
- higher punishment ceiling when Strength also qualifies
- stronger foreign trade and resource concessions

### Evolution III

Evolution III expands foreign-policy leverage and high-Chaos intervention.

New or stronger content:

- faction and alignment demands
- foreign-base removal
- sanctions
- priority-offender routes
- intervention against occupiers
- coordinated punishment
- Tier IV and Tier V access when all gates qualify
- wider World Is One integration
- costly reconciliation after defiance

Disabled later evolutions must remove only their added families. Baseline progression and existing demands need clean alternatives.

## Event 012 route integration

Gods of Africa should connect to the existing Charter, aid, guarantee, liberation, congress, settlement, rail, force, resource, sanctions, and foreign-base systems owned by Africa Is One.

Examples:

- a cooperative Charter route lowers demand aggression and improves final friendship
- a militarized liberation route gives more weight to equipment, access, and withdrawal demands
- continental railway projects create specific industrial and train demands
- foreign bases create Wrath and withdrawal demands
- sanctions routes support punishment through diplomacy and trade
- a rival African claimant reduces Strength and can challenge the doctrine's legitimacy
- successful regional congresses improve Strength through continental control and institutional coherence

Gods of Africa should read authoritative Event 012 state. It should not create duplicate continent-control, claimant, base, or victory ledgers.

## World Is One integration

If Event 012 enters its World Is One constitutional campaign, the Gods relationship history should shape participation.

Possible effects:

- favored countries receive founding invitations or privileged negotiation status
- respected countries receive ordinary invitations
- distrusted countries face conditions
- enemies become likely opponents, holdouts, or excluded powers
- prior voluntary aid improves bargaining position
- permanent defiance creates a strong resistance weight

The World Is One route owns its own terminal logic. Gods of Africa supplies relationship evidence and participant disposition.

## Triggerable Scenario `SCN-011`

The Africa Is One scenario type should create the African unifier and then start the normal consolidation delay. It should not fire Gods of Africa immediately unless the selected scenario setup explicitly begins after consolidation.

The World Is One scenario type should initialize enough Gods relationship history to support its chosen setup. It should avoid launching a redundant tribute cycle after continental security is already established.

Scenario intensity can influence:

- initial African capability
- continent control
- initial Strength
- participant Wrath distribution
- number of active hostile foreign positions

The scenario remains owned by `SCN-011`. Gods of Africa does not receive a separate triggerable scenario ID.

## Event and report structure

### One-time activation surfaces

- hidden owner event that validates and activates the system
- African-unifier proclamation event
- global news or report event
- participant introduction event
- optional one-time super-event when Strength reaches the accepted global-credibility threshold

### Recurring participant surfaces

- demand issue event or mission creation
- compliance report
- substitute offer result
- extension result
- refusal result
- failed demand result
- punishment report
- protection report
- voluntary aid result
- defiance confirmation and aftermath
- rare reconciliation chain

### Africa-side reports

Africa receives compact summaries for:

- major powers that complied
- refusals
- broken agreements
- voluntary aid
- current priority offenders
- severe punishments
- new favored candidates

Routine small transfers should be grouped into periodic reports when possible. Africa should not receive a popup for every rifle shipment from every AI country.

### Event Logs

The global Events log should record only major system milestones, such as:

- activation of Gods of Africa under Event 012
- first globally credible punishment if it changes world understanding
- permanent defiance by a major player or major power when log policy accepts it
- Tier V punishment
- Africa's defeat ending the system
- final secured-continent settlement

Routine demands and payments belong to the event-owned internal ledger and participant UI. They should not count as random pacing events or flood the global event history.

## AI design

### Participant AI archetypes

AI behavior should emerge from campaign state. It should not assign one permanent personality to each tag.

#### Cooperative pragmatist

More likely when:

- Africa is strong
- demand burden is manageable
- relations are good
- the target has no African territorial interest
- the target needs African support
- the target is losing a war
- current Wrath is low or medium

Behavior:

- complies with useful and affordable demands
- negotiates painful demands
- provides emergency aid when strategically valuable
- avoids permanent defiance unless Africa becomes abusive

#### Selective gambler

More likely when:

- Africa has medium Strength
- the target is strong enough to absorb limited punishment
- the demand is expensive
- the target has mixed relations with Africa
- the target believes future Strength may fall

Behavior:

- fulfills cheap demands
- substitutes frequently
- refuses high-cost demands
- invests in mitigation
- avoids reaching the highest Wrath bands when possible

#### Defiant rival

More likely when:

- the target is stronger than Africa
- it occupies African territory
- it leads a hostile faction
- relations are already poor
- it expects to defeat Africa
- the demand attacks a core strategic interest

Behavior:

- refuses or permanently defies
- strengthens defenses
- builds an anti-African coalition
- targets African capability to lower Strength

#### Loyal ally

More likely when:

- allied to Africa
- protected by Africa
- helped during unification
- threatened by a common enemy

Behavior:

- treats demands as alliance support
- gives emergency aid
- expects reciprocal protection
- reacts strongly if Africa abuses the relationship

### Participant AI decision factors

AI should evaluate:

- exact demand burden relative to usable capacity
- current and projected war needs
- Strength band
- current Wrath band
- punishment recently suffered
- Africa's current military trend
- distance and access
- diplomatic alignment
- territorial conflict
- hidden relationship history
- value of final friendship
- validity of substitute options
- expected mitigation capability
- current Chaos tier

### Africa AI

Africa's AI should:

- select demand families from real need
- avoid requesting resources already in excess
- scale amount to target capacity
- avoid repeatedly targeting the same compliant country
- prioritize occupiers and active enemies
- use leniency when preserving a useful partner is better than provoking defiance
- protect countries with strong cooperation records
- avoid Tier IV and Tier V punishment when a lower action serves the objective
- stop destroying a target that can no longer provide tribute unless the route is punitive and the offense remains severe
- consider attribution and condemnation when using direct methods
- pause broad demands during immediate African collapse

### Probability evidence requirement

Every weighted participant choice, demand-family selector, Africa target selector, punishment-family selector, and AI route choice requires a named scenario audit through the project probability tools during implementation.

The implementation must provide complete candidate pools and declared external factors before claiming exact probabilities.

## Multiplayer

### Independent relationships

Wrath, active demand, deadline, defiance, and hidden history are participant-specific.

One player's refusal must not raise another player's Wrath.

### Shared Strength

All players see the same Gods of Africa Strength because it belongs to the African unifier and world state.

### Staggered dispatch

Human participants should receive demands on deterministic staggered dates based on participant registration order or a stable seed. This avoids simultaneous pauses and popup storms.

### African player

When the African unifier is player-controlled, it receives the Africa-side category and can set priorities, grant leniency, protect partners, mark priority offenders, and use route actions.

The player cannot manually write arbitrary demand amounts or select invalid demand families. The owner system calculates valid offers.

### Participant control changes

When a human takes control of an already enrolled AI participant, its existing Wrath and history remain. Any active demand should be shown immediately through the normal UI.

When a human takes control of a newly valid country, the country is enrolled once and receives the introduction.

## Presentation

### Default surface

The default surface is an ordinary decision category with a compact attached display.

The participant sees:

- Gods of Africa Strength meter
- Wrath of the Gods meter
- one active demand mission when present
- up to five response actions
- one concise current relationship note
- one concise current African priority note when relevant

The player should understand the current risk and next action without opening another window.

### Value display

Each meter should show:

- current value
- qualitative band
- trend direction
- next threshold
- short tooltip with the main actionable causes

The tooltip should not expose a full component ledger.

### Category picture

The category picture should show the fictional continental institution that issues demands. It should focus on one coherent chamber, monument, signal, or ceremonial apparatus. It should avoid a map-only composition and avoid a collage of masks, pyramids, animals, and unrelated religious objects.

### Full scripted GUI gate

A dedicated event-owned GUI should be considered only if implementation proves that the normal category cannot handle selected-target Africa-side actions and two clear meters.

A full GUI would require:

- a named Event 012 owner window
- exact entry point
- functional target selection
- AI-equivalent actions
- scripted-GUI ownership and cleanup
- MCP inspect, render, rewrite, and comparison evidence
- asset handoffs

The full GUI is not a default requirement in this specification.

## Focus integration summary

Gods of Africa should use an Event 012 overlay branch that becomes visible after Evolution I and the consolidation milestone.

The branch should include:

- proclamation and institutional setup
- doctrine fork between reciprocal covenant and sovereign exaction
- provision and logistics route
- oaths and diplomatic leverage route
- protection route
- judgment and retaliation route
- later Evolution II and III expansion
- a convergence capstone tied to continental security

The branch must change demands, protection, punishment, and diplomacy. It should not become a chain of flat Strength bonuses.

Detailed route architecture is in `012_gods_of_africa_focus_integration.md`.

## Assets and visual direction summary

Required visual families should remain small and purpose-driven:

- activation report or news image
- decision category picture
- separate Strength and Wrath icons
- response decision icons
- Africa-side action icons
- doctrine idea icons
- achievement triplets when achievements are accepted
- one super-event image only if the credibility threshold is accepted

Final art should be generated because the system is fictional and high-Chaos. Historical symbols and real sacred objects should be used only after specific research and should not be merged into an invented universal religion.

Broad animation is not required. One warning-state loop may be considered later if a dedicated GUI is accepted. It would require genuine source frames and a static fallback.

## Super-event role

One super-event candidate is justified when the system first becomes globally credible.

Trigger direction:

- Gods of Africa is active
- the super-event has not fired
- Strength reaches a global-reach threshold
- Africa still exists and the Event 012 campaign remains active

If Africa already meets the threshold at activation, the proclamation can trigger it. If Africa is weak, activation uses normal news and the super-event waits until Strength rises.

The final title, quote, cultural remark, image, and audio require separate research. No wording or track is selected in this specification.

## Achievement directions

### Long obedience

Reward a participant that reaches Favored without war against Africa, occupation of African territory, permanent defiance, or a broken formal agreement.

### Survive defiance

Reward a participant that permanently defies at high Strength and survives until Africa's continental settlement or defeat without capitulating to Africa.

### Continental provision

Reward the African unifier for receiving meaningful tribute across several different demand families from a broad set of major powers.

### The careful gambler

Reward a participant that refuses several major demands, never chooses permanent defiance, never reaches the maximum Wrath band, and receives at least a Respected final outcome.

Achievement implementation needs full tracking, disqualifiers, localisation, icon triplets, docs, and catalog alignment.

## Balance invariants

The implementation must preserve these rules:

1. Wrath alone never unlocks a punishment above the current Strength ceiling.
2. One normal refusal never causes Tier IV or Tier V punishment.
3. A weak Africa can bluff and disrupt, but cannot erase a major power.
4. A strong Africa still needs high Wrath, high Chaos, escalation history, and a valid offense for Tier V.
5. Every material demand checks target capacity and a protected reserve.
6. Every material payment strengthens Africa through a real transfer or commitment.
7. Africa cannot request a family that the target cannot meaningfully provide.
8. Only one ordinary demand is active per participant.
9. Routine demand events do not count as normal random pacing events.
10. Routine transactions do not flood the global Event Log.
11. Shared disaster, Deaths, migration, famine, condemnation, and Chaos systems retain ownership of their own effects.
12. Every population loss is applied and logged once.
13. Defiance stops ordinary demands but does not erase hostility.
14. Final friendship depends on full history, not one last payment.
15. Africa's victory settlement ends the tribute loop cleanly.
16. Event `070` remains unassigned by this system.

## Anti-exploit rules

- no tiny repeated voluntary-aid farming
- no cancelling a promised transfer after receiving Wrath reduction
- no duplicate debit from event option and decision completion
- no active-demand duplication after save and reload
- no escaping the participant registry by losing major status
- no escaping permanent defiance through tag switching
- no repeated extension loop
- no substitute offer below the accepted burden band
- no demand for an unavailable DLC mechanic
- no Africa-side arbitrary amount entry
- no punishment reroll by reopening an event
- no duplicate disaster call after a saved result
- no repeated Tier V sequence inside its global and target cooldowns
- no final Favored result after an unresolved permanent disqualifier

## Failure and cleanup

The system must fail closed when:

- the African unifier event target is missing
- the selected participant is invalid
- a demand family cannot resolve a transferable token
- capacity proof is missing
- the target cannot pay the calculated amount
- a disaster call rejects its inputs
- a population transaction lacks its contract proof
- a selected state group is empty
- a DLC adapter is unavailable

Cleanup must remove:

- active demand missions
- target flags
- selected-target state
- pending debit proof
- delayed punishment jobs
- temporary event targets
- temporary substitute offers
- participant queue entries for invalid countries
- Africa-side target selection for invalid participants

Permanent history should remain only where later Event 012 content needs it.

## Implementation acceptance

The system is ready for completion review only after:

- Event 012 owner state is reused instead of duplicated
- all public values and thresholds are wired
- demand families have capacity and need checks
- material transfers are real
- AI has complete response and target logic
- probability scenarios pass their intended orderings
- participant and Africa-side categories are localized and readable
- defiance, reconciliation, war, defeat, and final settlement are complete
- disaster and population routes use shared APIs
- event logs record only major milestones
- Event 012 docs and authoritative XLSX are aligned
- Event 070 is freed in the authoritative workbook
- required assets are final and wired
- completion and localisation audits are complete
- no fallback, placeholder, missing AI path, or missing cleanup is concealed

## Your Task

Implement Gods of Africa as an Event 012 owner subsystem using this package as the accepted design source. Preserve the two-value limit, capacity-based tribute, real transfers, per-participant Wrath, hidden relationship memory, Strength-based punishment ceiling, persistent player routes, Africa-side agency, Event 013 disaster gateway, exact Deaths accounting, Event 012 evolution integration, final settlements, AI, multiplayer behavior, presentation, assets, documentation, and catalog alignment. Keep Event 070 available for another idea. Report every blocker or deviation and do not substitute a smaller system without explicit approval.
