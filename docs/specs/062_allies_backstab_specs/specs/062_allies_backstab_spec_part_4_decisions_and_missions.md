# Event 062 crisis decisions and missions

## Presentation choice

The event uses the ordinary decisions interface with one event-owned category and one static category picture. It does not need a full scripted GUI.

The category changes its description and visible actions according to the country's current role:

- original faction leader
- retained loyalist member
- expelled government
- expelled-group leader
- neutral withdrawal member
- selected outside sponsor or mediator

The category header shows:

- the current role
- the current side leader
- working value `Crisis Cohesion`
- the current cohesion stage
- the next threshold and its main consequence
- the principal active mission
- the linked opponent or settlement partner

The header should fit in a short block. Hidden formulas stay in tooltips or remain internal.

## Visibility budget

Each role and phase shows three to five primary decisions. Six is the hard maximum. Obsolete actions disappear when the war, role, target, or settlement state changes.

Each country has one to three active Event 62 missions. A hidden queue can wait for a slot. The category should never display every possible target row at once.

Targeted actions use a selected-target flow when more than one victim, loyalist member, or sponsor is valid. The human player sees one target's actions at a time. AI evaluates all valid targets through its own visibility path.

## Cost rules

Each action may use no more than four spendable cost types. Costs scale from country capacity and the size of the linked crisis.

Suitable costs include:

- command power
- army experience
- political power for actual diplomacy or political commitments
- infantry equipment
- support equipment
- trucks
- trains
- convoys
- fuel
- manpower
- stability
- war support
- temporary civilian factory burden
- temporary military production burden
- committed divisions as a requirement or temporary lock

Costs should be large enough to change planning. A major action cannot be a small political power purchase followed by a minor modifier.

## Phase structure

### Shock phase

The first `30` days focus on role commitment, emergency mobilization, unit withdrawal, and side formation.

### Active war phase

The category prioritizes capital defense, punitive operations, co-victim coordination, outside support, and defection control.

### Settlement phase

Settlement actions appear after military proof, exhaustion, mediation, or a cohesion threshold. They replace the most aggressive preparation actions.

### Aftermath phase

Only final recognition, readmission, successor-faction formation, and cleanup actions remain. The category closes after the last relevant action or mission resolves.

## Original faction leader decisions

### Secure the War Council

**Availability:** shock phase, once per generation.

**Purpose:** obtain clear commitments from retained members and establish one command plan.

**Costs:** command power, army experience, and support equipment scaled by loyalist size.

**Effect direction:** raise loyalist cohesion by a meaningful amount, improve the chance that retained members answer calls, and reduce early defection risk for a short period.

**Risk:** a low-trust member can refuse the demand. Refusal lowers cohesion and can open an Evolution II stance choice.

**AI:** high priority when cohesion is below coordinated and the leader has enough resources to sustain the coming war.

### Demand Renewed Commitments

**Availability:** retained members have not yet declared a stance.

**Purpose:** force every remaining member to state whether it supports the purge.

**Costs:** political power and a stability consequence if several members refuse.

**Effect direction:** committed members strengthen cohesion. Refusal becomes public and can accelerate a split.

**Risk:** using the action while the leader is weak or unpopular can create more defections than silence would have caused.

**AI:** used by confident leaders and by desperate leaders with few other options. Cautious AI avoids it when projected refusals are severe.

### Coordinate Punitive Operations

**Availability:** active legal war, no duplicate offensive mission.

**Purpose:** commit the faction to a concentrated campaign against one selected victim or victim group.

**Costs:** fuel, infantry equipment, command power, and an optional temporary production burden. Four cost types are the maximum.

**Effect direction:** start the mission `Break the Expelled Resistance`, improve planning against the selected target, and make a limited settlement easier after success.

**Risk:** failure reduces cohesion and increases the chance that members demand an end to the war.

**AI:** high when the target capital is reachable, supply is viable, and the loyalist side has a real advantage.

### Offer Conditional Readmission

**Availability:** forced-compliance intent, settlement proof, and the victim government still exists.

**Purpose:** end the war by returning the victim to the faction under public safeguards or restrictions.

**Costs:** political power and a leader-cohesion concession.

**Effect direction:** send visible terms to the victim. Acceptance ends the linked war, restores membership where legal, grants victim protection, and records a fragile reconciliation.

**Risk:** rejection lowers leader prestige and can strengthen victim recognition.

**AI:** likely when the war is expensive, the victim remains viable, and the leader still values the victim's strategic position.

### Recognize the Separation

**Availability:** settlement phase, especially after a failed offensive or successful victim defense.

**Purpose:** accept that the expelled governments remain independent.

**Costs:** stability and war support scaled by how publicly the leader promised victory.

**Effect direction:** end the linked conflict, create a truce, remove active crisis state, and preserve betrayal memory.

**AI:** likely when no credible victory remains and continued war threatens the faction itself.

## Retained loyalist member decisions

### Reaffirm the Faction

**Availability:** shock phase, once.

**Purpose:** commit forces and political support to the original leader.

**Costs:** command power and equipment or a required force commitment.

**Effect direction:** raise loyalist cohesion and improve joint operations.

**Risk:** the member becomes more exposed to victim retaliation and loses access to neutral withdrawal during the current generation.

**AI:** favored by close ideological partners, beneficiaries of the leader, and members threatened by the victims.

### Demand a Mutual Security Charter

**Availability:** member stays loyal but fears a later purge.

**Purpose:** require safeguards against another arbitrary expulsion.

**Costs:** political power.

**Effect direction:** create a demand that the leader can accept or refuse. Acceptance costs leader freedom but raises cohesion and grants the member future Event 62 protection. Refusal lowers cohesion.

**AI:** favored by medium and weak members that are loyal but vulnerable.

### Withhold Forces

**Availability:** active crisis, the member is not the leader, and no hard treaty requires immediate participation.

**Purpose:** remain in the faction while limiting direct involvement.

**Costs:** war support and relations with the leader.

**Effect direction:** preserve the member's equipment and manpower, lower loyalist cohesion, and prevent full offensive bonuses.

**Risk:** the leader can later isolate or threaten the member. At Evolution II, this action raises defection interest.

**AI:** favored by overextended, undersupplied, or politically divided members.

### Join the Expelled Governments

**Availability:** Evolution II or III, valid victim side, no contradictory war, subject bundle safe.

**Purpose:** leave the original faction and enter the victim coalition.

**Costs:** stability, war support, and any required military withdrawal burden.

**Effect direction:** move the political unit to the victim side, update cohesion on both sides, and attach it to the linked war when legal.

**Risk:** the new side may be much weaker, and the country loses original faction support.

**AI:** uses the full side-choice score and never selects an illegal side.

### Withdraw from the Crisis

**Availability:** Evolution II or III, a neutral exit is legal.

**Purpose:** leave the faction without joining the victims.

**Costs:** political power and temporary diplomatic isolation.

**Effect direction:** remove the member from faction obligations, deny its forces to both sides, and create a short truce with the crisis participants.

**Risk:** both camps may distrust the neutral government, and a later event can exploit the isolation.

**AI:** favored by distant, overextended, politically incompatible, or militarily exhausted members with no strong side preference.

## Expelled government decisions

### Emergency Mobilization

**Availability:** shock phase, once, government controls viable territory.

**Purpose:** convert available manpower and equipment into a defensive force and shorten mobilization delays.

**Costs:** infantry equipment, support equipment, command power, and a temporary factory burden.

**Effect direction:** unlock emergency raising of ordinary formations, improve mobilization on controlled core territory, and reduce the opening shock penalty.

**Risk:** the burden weakens long-term production. No free divisions appear without manpower and equipment.

**AI:** highest priority for a victim with low field strength and enough resources to benefit.

### Secure the Capital and Supply Spine

**Availability:** victim controls its capital and at least one relevant supply route.

**Purpose:** turn the capital, nearby rail route, or principal port into the center of resistance.

**Costs:** trains, infantry equipment, and command power.

**Effect direction:** start `Hold the Government Together`, identify the exact capital and route states, and provide a meaningful defense package while the objective remains active.

**Risk:** failure causes a large cohesion loss and strengthens loyalist settlement demands.

**AI:** high unless the capital is already indefensible and an evacuation or settlement route is stronger.

### Open the Expelled Governments Liaison

**Availability:** at least two victims from the same purge, no liaison active.

**Purpose:** coordinate military access, equipment requests, and common terms.

**Costs:** political power, command power, and a small equipment contribution scaled to capacity.

**Effect direction:** establish temporary coalition rules, raise victim cohesion, and unlock joint missions.

**Risk:** countries with poor relations may refuse, which weakens the initial coalition.

**AI:** favored when co-victims share borders, ideology, or a strong common threat.

### Request a Foreign Lifeline

**Availability:** one or more outside sponsors pass interest and access checks.

**Purpose:** ask for equipment, guarantees, intelligence support, or mediation.

**Costs:** political power, convoys when overseas transport is needed, and a dependency or exposure consequence.

**Effect direction:** invite no more than two selected sponsors into the crisis. The sponsor chooses its own commitment.

**Risk:** rival sponsors can compete, and heavy support can shape later faction alignment.

**AI:** favored when the loyalist side is much stronger or the victim lacks equipment.

### Pool the Emergency Reserves

**Availability:** multiple victims, liaison active, one country has a meaningful surplus and another has a proven shortage.

**Purpose:** transfer paid equipment among co-victims.

**Costs:** donor equipment and transport capacity.

**Effect direction:** execute one bounded transfer with a receipt, raise cohesion, and improve the recipient's mission viability.

**Risk:** repeated use is limited by cooldown and donor reserve floors.

**AI:** donors act only when their own front remains sustainable.

### Seek Recognized Separation

**Availability:** survival or battlefield proof, victim cohesion at least coordinated, or a mediator is active.

**Purpose:** force the loyalists to accept independence and end the war.

**Costs:** political power and concessions defined by the visible offer.

**Effect direction:** send terms based on capital control, casualties, relative strength, outside support, and the original conflict intent.

**Risk:** a failed offer can strengthen loyalist resolve for a limited period.

**AI:** favored after a successful hold mission or when the loyalists are exhausted.

### Form a Successor Compact

**Availability:** at least two independent surviving victims, cohesion at unified, common war or settlement, and no faction conflict.

**Purpose:** convert the temporary coalition into a durable faction or owner-approved pact.

**Costs:** political power, command power, and a stability commitment.

**Effect direction:** form the new bloc, select its leader, apply fresh-faction protection, and replace temporary liaison state.

**Risk:** incompatible members can refuse. The action cannot dissolve an existing valid faction without explicit consent and legal proof.

**AI:** favored after victory or recognized separation, not during imminent capitulation.

## Outside sponsor decisions

### Guarantee the Expelled Governments

**Availability:** sponsor has relations, access, capability, and no contradictory war.

**Purpose:** deter complete liquidation and support a negotiated or defensive outcome.

**Costs:** political power, convoys, equipment, and an optional civilian factory burden.

**Effect direction:** provide a bounded aid package, raise victim cohesion, and increase loyalist settlement pressure.

**Risk:** the sponsor may become involved if the crisis widens through existing guarantee rules or Evolution III.

### Back the Original Faction

**Availability:** sponsor supports the leader and can reach the theater.

**Purpose:** provide equipment, fuel, or diplomatic recognition to the loyalists.

**Costs:** equipment, fuel, convoys, and political power.

**Effect direction:** improve the selected loyalist mission and reduce the chance of immediate settlement.

**Risk:** support damages relations with victims and rival sponsors.

### Convene an Armistice Conference

**Availability:** both sides remain viable, sponsor has diplomatic standing, no conference active.

**Purpose:** open a timed settlement mission.

**Costs:** political power and a temporary civilian factory or diplomatic burden.

**Effect direction:** freeze the most aggressive event decisions for a short negotiation window, collect terms, and start `Secure an Armistice`.

**Risk:** bad faith or a renewed offensive ends the conference and records a settlement violation.

### Threaten Direct Intervention

**Availability:** Evolution III or an existing guarantee obligation, sufficient military access and strength.

**Purpose:** force one side to accept terms under threat of entry.

**Costs:** command power, war support, and military readiness requirements.

**Effect direction:** sharply shift settlement willingness. Direct entry occurs only through a legal and visible follow-up.

**Risk:** a failed threat damages sponsor credibility and can widen the war.

## Missions

### Hold the Government Together

- Role: expelled government
- Duration: `120-180` days, scaled by geography and strength
- Objective: retain the capital, remain uncapitulated, and keep the named supply route or fallback port functional
- Success: major cohesion gain, recognition leverage, improved defensive state, and achievement progress
- Partial success: capital held but route lost, smaller cohesion gain and a harder follow-up
- Failure: major cohesion loss, loyalist leverage, possible evacuation or separate-peace pressure

### Break the Expelled Resistance

- Role: original faction leader
- Duration: `150-240` days
- Objective: occupy the selected victim capital or reach a defined surrender threshold while keeping the attacking route supplied
- Success: settlement leverage and a limited war-intent payoff
- Partial success: route secured without decisive occupation, moderate leverage
- Failure: loyalist cohesion loss, higher member refusal, and victim recognition opportunity

### Keep the Expelled Governments Connected

- Role: victim-group leader
- Duration: `120-180` days
- Objective: preserve all surviving victim capitals and maintain a legal land, port, or convoy connection among members
- Success: cohesion reaches at least coordinated, joint reserve action improves, and successor-compact progress opens
- Partial success: one member isolated but not capitulated, no full reward and no coalition collapse
- Failure: separate-peace interest rises and the liaison weakens

### Prevent a Second Defection

- Role: original faction leader
- Evolution: II or III
- Duration: `120` days
- Objective: keep loyalist cohesion above shaken and prevent another political unit from leaving
- Success: loyalist cohesion gain, member protection charter option, achievement progress
- Failure: a new stance round opens for the most dissatisfied valid member

### Decide the Bloc

- Role: pending member during Evolution II
- Duration: `7-14` days
- Objective: choose loyalist, victim, or neutral stance before the deadline
- Success: selected legal stance applies
- Failure: AI or deterministic safety logic chooses the highest valid stance, with neutrality preferred when all side choices are contradictory

### Secure an Armistice

- Role: selected mediator
- Duration: `90-150` days
- Objective: keep both sides inside the conference, prevent new event-linked offensives, and obtain minimum term support
- Success: visible settlement offer and temporary truce
- Partial success: one victim or loyalist member accepts a separate limited term
- Failure: conference ends, cohesion hardens on the side that did not break talks, and a violation memory is recorded when responsibility is proven

## Mission completion rules

Goal-style missions complete automatically when their conditions are satisfied. The player does not pay a second click after doing the work.

Mission tooltips name the capital, state group, route, opponent, required divisions, and deadline. They do not expose raw state IDs or vague phrases such as sufficient forces.

Success and failure use separate effects. No mission gives the same small stability or war support change under both outcomes.

## Idea lifecycle

| Working idea | Initial role | Improvement path | Failure path | Removal |
| --- | --- | --- | --- | --- |
| Betrayed by the Bloc | victim shock, core defense, weak planning and supply coordination | Coordinated Defense or Internationally Supported Defense | Isolated Government | settlement, annexation, or crisis handoff |
| War Council Purge | loyalist offensive coordination with faction trust cost | Disciplined War Council | Fractured Command | settlement, faction collapse, or crisis handoff |
| Expelled Governments Liaison | temporary co-victim coordination | Successor Compact institutions | Broken Liaison | compact formation, separate peace, or coalition collapse |

The implementation may use staged ideas or dynamic modifiers according to local precedent. Each visible state needs an appropriate idea icon if it appears in the national spirit interface.
