# Event 062: Allies Backstab complete specification

---

# Event 062 core design

## Catalog entry

- Event ID: `62`
- Event name: Allies Backstab
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: `1`
- Cluster: Wars
- Cluster role: High member

## Premise

Alliances across the world identify members that appear expendable, remove them from the bloc, and attack them. Several factions are affected by one event firing. A faction can lose one member, several weak members, or at higher Evolutions split into opposing camps.

The event is forced once a faction is selected. The faction leader does not receive a harmless refusal option that cancels the incident. Player agency begins with the way the purge is prosecuted, resisted, widened, negotiated, or settled.

## Player experience

An uninvolved player receives one aggregated international report built around the largest fracture in the generation. The report states how many factions were affected and names only the most important examples that can fit cleanly. It does not produce one world popup for every faction.

A player inside an affected faction receives one role-specific event:

- the faction leader learns which governments have been removed and chooses the public war intent
- an expelled government sees the expulsion, the immediate military danger, and any co-victims
- a member retained by the faction decides how strongly to support the purge
- at Evolution II or III, a dissatisfied member can join the expelled bloc or withdraw from the crisis when legal
- a selected outside sponsor receives a bounded intervention or mediation opportunity

The expulsion is already real when the role event appears. The war declaration follows after a short hidden transaction step that rechecks all legal and war-side conditions. This gap exists to prevent broken diplomacy, not to turn the purge into an avoidable ultimatum.

## Global firing rule

One Event 62 firing must affect at least two distinct valid factions. When fewer than two valid factions exist, the event has no valid target and is unavailable to normal selection. A manual force route may expose the same failure reason, but it must not invent invalid factions or apply a partial transaction.

Each selected faction receives a separate transaction receipt under the same global generation. A failure in one faction does not roll back completed safe transactions in another faction. A faction that becomes invalid before mutation is skipped and replaced from the unused valid-faction pool when possible.

## Affected faction count

The ordinary baseline uses a bounded faction budget.

| Valid factions at draw time | Baseline factions affected | Evolution I factions affected | Evolution III maximum |
| --- | --- | --- | --- |
| `0-1` | Event unavailable | Event unavailable | Event unavailable |
| `2` | `2` | `2` | `2` |
| `3-5` | `2` | `3` when possible | `3-4` |
| `6-9` | `2-3` | `3-4` | `4-5` |
| `10+` | `3` | `4` | `4-6` |

The exact roll inside a range is weighted by faction pressure and the global mutation budget. Evolution III may select six factions, but no more than three may undergo a full internal bloc war in one generation. Other selected factions use a baseline or Evolution I purge.

## Faction identity

The event treats the current faction leader as the stable transaction anchor. It takes a membership snapshot before any country leaves. The snapshot remains the source for generation history even when the faction later dissolves or changes leader.

A political unit is the selection unit used for faction size and side assignment:

- an independent faction member forms one political unit
- subjects inside the same faction travel with their overlord as one bundle unless a safe independence route is explicitly invoked
- a subject whose overlord is outside the faction is excluded until implementation proves a legal owner-specific route
- a country cannot appear in two political units

This prevents an overlord and its subjects from being selected separately and placed on contradictory sides.

## Faction eligibility

A faction is valid when all of these are true:

- it has a living faction leader
- it contains at least two valid political units
- at least one nonleader unit can be expelled and opposed legally
- it has no unresolved Event 62 transaction
- its Event 62 faction cooldown has ended
- it is outside the fresh-faction protection period
- its members can be snapshotted without duplicate or invalid country entries
- the event can identify a legal immediate war, a legal delayed war, or a proven shared-war separation path

A two-member faction is valid. Its sole nonleader member becomes the only baseline target. The event records the bilateral betrayal even if the original faction later becomes a one-country shell or dissolves through normal engine behavior.

A faction created recently by Secret Alliance, A Faction Comes Calling, an Event 62 victim compact, or another faction-forming system receives a default protection period before it can be selected. The baseline planning value is `180` days. An Event 62 successor faction receives `365` days because immediate repeated betrayal would create a deterministic loop.

## Ordinary-country boundary

The event is designed for ordinary faction politics. An actual nonhuman country and a system actor that cannot use normal diplomacy are excluded. A special but human country may participate only when its owner marks normal faction behavior as safe.

The event should use the shared country classifiers as inputs, then keep its detailed participant trigger in the Event 62 owner files. It must not expand the shared classifier with Event 62 lifecycle rules.

## Generation lifecycle

Every firing creates one global generation number and one faction transaction number per selected faction.

A generation moves through these states:

1. valid factions collected
2. factions selected without replacement
3. membership and war state snapshotted
4. victims selected
5. initial side roles assigned
6. expulsion applied
7. military and diplomatic relationships reconciled
8. delayed war launch revalidated
9. crisis decisions and missions opened
10. settlement, victory, collapse, or ordinary-war handoff recorded
11. temporary state cleaned
12. durable memory and achievement facts preserved

Every state transition is idempotent. Reloading or receiving the same delayed event twice cannot expel a country twice, create duplicate wars, repeat equipment grants, or add a second crisis category.

## Public mechanic value

The event exposes one custom value, working label `Crisis Cohesion`.

Each active side has its own value, but a country sees only the value for the side it currently serves. The concept and thresholds remain identical for loyalists, expelled governments, and a successor bloc.

| Value | Stage | Meaning |
| --- | --- | --- |
| `0-24` | Disintegrating | members seek exits, separate peace becomes likely, and joint actions weaken |
| `25-49` | Shaken | the side can act, but failures can trigger defections or isolation |
| `50-74` | Coordinated | joint missions, settlement leverage, and reliable support become available |
| `75-100` | Unified | the side can sustain major joint action and claim a durable political outcome |

The category header shows the exact value, the stage name, the next threshold, and the most important recent cause. It does not expose the hidden target, defection, or settlement formulas.

Initial cohesion is dynamic. Suggested central tuning anchors are:

- loyalist side base: `55`
- expelled side base: `40`
- at least two mutually friendly victims: `+10`
- credible common external threat: loyalist `+10`
- severe leader-member hostility: loyalist `-10`
- outside guarantee or active mediator: expelled side `+10`, once per source class
- no viable route between co-victims: expelled side `-10`

Important events move cohesion in visible steps. A capital loss, member defection, separate peace, failed mission, successful war council, outside guarantee, or accepted settlement should matter. Routine combat does not create constant small ticks.

## Hidden simulation values

The event may track as many internal values as needed, including:

- faction selection pressure
- member vulnerability
- core-member protection
- strategic utility
- war contribution
- defection interest
- neutral-withdrawal interest
- side viability
- war launch legality
- military balance
- settlement willingness
- outside sponsor interest
- escalation proof

These values remain hidden unless one becomes a direct player choice. They feed the single public cohesion value, event availability, role events, AI behavior, and settlement outcomes.

## Baseline invariants

The baseline must preserve these rules:

- at least two factions are affected per normal firing
- every selected faction has a pre-mutation snapshot
- the faction leader is never the initial baseline victim
- one or more weak members are expelled
- former allies attack when a legal conflict edge can be created
- several victims from one faction cooperate by default and do not automatically fight each other
- the event never places one country on both sides of the same war
- no subject fights its overlord unless an owner-approved independence transaction resolved the relationship first
- no event effect directly creates civilian deaths, migration, famine, or contamination
- the event does not grant Chaos for the draw or for Evolution activation
- active decisions disappear after the linked crisis ends
- durable betrayal and settlement memories remain available to later events

---

# Event 062 faction and victim selection

## Selection goals

The event should usually strike members that the faction can describe as weak, exhausted, isolated, or expendable. The outcome must remain uncertain enough that repeated firings do not always select the smallest tag.

Raw size is one input. Strategic value, war contribution, geography, supply, and political trust can protect a small country. Severe losses can make a previously important member vulnerable. A large member can become a target when it is militarily broken and politically isolated, but this should be uncommon.

## Faction selection pressure

Eligible factions receive a hidden pressure score. The score determines which factions enter the generation, not which members become victims.

Suggested factor families are:

| Factor family | Pressure direction |
| --- | --- |
| size and number of political units | larger factions receive more pressure, especially at high Evolution |
| capability disparity | a large gap between strongest and weakest members raises pressure |
| political divergence | ideology distance, poor relations, and hostile memories raise pressure |
| war strain | multiple fronts, high losses, capitulations, and broken supply raise pressure |
| faction instability | recent exits, leadership disputes, and failed calls raise pressure |
| shared external threat | a credible common enemy lowers pressure unless internal hostility is already severe |
| institutional depth | long membership, strong relations, and high mutual contribution lower pressure |
| recent Event 62 exposure | active and cooling factions are invalid, not merely reduced in weight |

Faction size must not dominate every draw. A medium faction under severe strain can outrank a larger stable alliance. Evolution III adds a strong large-faction preference only after the faction passes the full-fracture validity gate.

## Member vulnerability model

Every nonleader political unit receives a normalized score relative to the other members of its faction. Higher values mean greater vulnerability.

The implementation should centralize the weights. The planning allocation below is the intended starting model.

| Component | Share of baseline score | Interpretation |
| --- | --- | --- |
| military weakness | `25` | division count, average strength, organization readiness, and deployed military capacity |
| equipment and manpower weakness | `15` | usable stockpile, reinforcement condition, available manpower, and mobilization depth |
| industrial weakness | `15` | military factories, civilian support capacity, dockyards where relevant, and current usable output |
| territorial and supply weakness | `10` | controlled states, capital security, rail and port access, and supply continuity |
| current war strain | `15` | number of fronts, enemy proximity, surrender progress, and threatened capital or supply hubs |
| military losses | `8` | recent casualties and equipment losses relative to national capacity |
| low faction contribution | `7` | low war contribution, weak expeditionary support, and failure to cover useful fronts |
| political isolation | `5` | poor relations with the leader and core members, ideology distance, and betrayal memories |

The values are ranks or normalized ratios inside the current faction. A twenty-division country in a faction of small states can be strong. The same country inside a major-power alliance can be weak.

## Core-member protection

A member receives core status when one or more of these facts are proven:

- it belongs to the strongest capability tier of the faction
- it supplies a large share of faction divisions, industry, air power, naval access, or war contribution
- it controls a capital, port, strait, rail corridor, or front that the faction currently depends on
- it has long membership, strong relations, and repeated support history
- the faction would lose a critical theater connection if it were expelled

Core status applies a major protection deduction to vulnerability. It does not create absolute immunity. A core member can still become a victim when military collapse, surrender progress, leader hostility, or strategic rivalry overwhelms the protection.

The faction leader is a separate case. It is excluded from baseline victim selection. Evolution II can leave the leader isolated in a rump faction when most members defect, which creates a leader-betrayed outcome without attempting to expel the legal faction leader through an unsafe effect.

## Strategic utility

A small country may be useful enough to avoid selection. Strategic utility includes:

- control of a front against the faction's current enemy
- a port or naval base needed for supply
- a rail or land bridge between other members
- an airfield network serving an active theater
- access to resources that the faction lacks
- a credible army positioned where no other member can replace it

Strategic utility is recalculated at the selection snapshot. Historical importance without current gameplay value does not provide permanent immunity.

## Protection and grace rules

A political unit is invalid as a victim when any of these apply:

- it contains the faction leader
- it was created, released, or transferred too recently to produce a safe package
- it has active Event 62 victim protection
- its removal would produce an unresolved subject-overlord conflict
- it is already in an Event 62 crisis
- it lacks any controlled state and has no viable government-in-exile route approved for this event
- it is an actual nonhuman or excluded system actor
- it cannot be separated from a shared war without placing countries on both sides

Planning defaults:

- ordinary faction-join grace: `180` days
- newly created Event 62 successor-faction grace: `365` days
- country victim protection after resolution: `1,095` days
- faction reuse cooldown after resolution: `720` days
- active-generation protection: permanent until cleanup

A human-controlled country receives the same hard protection after a prior Event 62 victimization. It has no permanent immunity. The event can target a weak player country after the protection expires.

## Candidate pool construction

Victim selection follows this order:

1. build the nonleader political-unit list
2. remove hard-invalid units
3. calculate normalized vulnerability and protection
4. sort by adjusted vulnerability
5. begin with units above the faction median vulnerability
6. expand downward only when the required victim count cannot be filled
7. draw without replacement from the eligible high-vulnerability group
8. revalidate each selected unit against the final bundle and loyalist-side viability rules

The draw remains weighted. The weakest unit should dominate when the gap is clear, but two similarly weak units should both be plausible.

## Victim count by faction size

The baseline uses the number of political units before expulsion.

| Political units | Baseline victims | Evolution I victims |
| --- | --- | --- |
| `2-5` | `1` | `1` |
| `6-9` | `1` | `1-2` |
| `10-14` | `1-2` | `2-3` |
| `15+` | `2-3` | `3-4` |

The count cannot exceed the valid candidate pool. A faction with three or more political units must retain the leader and at least one additional viable loyalist unit after a baseline or Evolution I purge. A two-member faction is the explicit exception.

At Evolution II, a full split follows side-viability rules instead of the victim-count table. At Evolution III, the world mutation budget can reduce a faction's planned victim count so one generation does not create an uncontrolled number of country mutations.

## Multi-victim grouping

Victims selected from the same faction belong to one expelled group for the generation. The group receives:

- mutual non-aggression for the active crisis
- temporary military access where legal
- permission to coordinate supply and war planning through event decisions
- a shared settlement position unless a member deliberately seeks separate peace
- a candidate group leader selected from capability, legitimacy, relations, and player status

The group is not forced into a permanent faction at once. It can operate as a temporary coalition. A durable successor faction becomes available only after survival, sufficient cohesion, and legal membership checks.

## Group leader selection

The expelled group leader is selected from independent victim political units. The score reads:

- military and industrial capacity
- capital security
- relations with other victims
- ideology compatibility
- diplomatic recognition and outside support
- player control
- absence of subject status
- ability to create or lead a faction under current engine rules

The strongest country does not win automatically. A somewhat weaker country with much better relations and legitimacy can lead. When a human player is a credible candidate, the player may accept or decline leadership. Declining does not remove the player from the group.

## High-contribution casualty protection

A country that suffered severe losses while making a high faction contribution should not be treated as weak solely because it was used heavily by the alliance. Losses increase vulnerability, while high contribution and strategic utility provide counterweight.

The probability audit must include a damaged high-contribution ally and a low-contribution isolated ally. The isolated ally should remain the preferred target unless the damaged ally is also collapsing politically and strategically.

## Player faction leader behavior

A human faction leader cannot choose no purge. The player receives a choice over conflict intent and the treatment of retained members. The target list is already selected by the global resolver.

The player can choose among valid directions such as:

- compel readmission or political compliance
- seize only registered cores and claims
- remove the victim government when severe ideological hostility supports it
- pursue complete destruction only under a narrow high-chaos and tiny-target gate

The final event options must show the visible war aim and likely diplomatic cost. Hidden follow-up branches remain hidden.

## Selection failure

A selected faction is skipped when its final snapshot no longer supports the transaction. Common reasons include:

- the only target was annexed or changed faction
- a subject relationship changed and cannot be reconciled
- a shared war makes legal hostility impossible
- the faction fell below two political units
- another event already dissolved the faction
- the selected countries entered a terminal or special state

The resolver attempts one replacement faction from the unused snapshot pool. It does not rescan the world repeatedly. When the final generation contains fewer than two completed faction transactions, the event records a failed firing only if the shared event system already committed the draw. Normal selection should prevent that state through the valid-target gate.

---

# Event 062 betrayal transaction and war graph

## Transaction purpose

Faction removal and war creation cannot be treated as one unguarded script block. Members may share wars, guarantees, expeditionary forces, subjects, military access, research arrangements, and supply routes. The event uses a staged transaction with proof at every mutation.

## Snapshot

Before any country leaves, the event stores:

- original faction leader
- original faction membership by political unit
- subject bundles and overlords
- current faction name or stable faction identity when available
- all active wars involving future loyalists or victims
- which countries share a war side
- bilateral wars already active between selected countries
- guarantees, military access, docking rights, and non-aggression relations relevant to the conflict
- current capitals and controlled territory
- victim and loyalist side leaders
- intended victim count and conflict intent
- current player roles

The snapshot is immutable evidence for the generation. Live conditions are read again before every delayed mutation.

## Transaction phases

### Phase 1: lock roles

The faction leader and retained members receive the loyalist role. Selected victims receive the expelled role. At Evolution II, uncommitted members receive a pending stance role until side selection finishes.

Every country receives one generation receipt. A country with a receipt from another active Event 62 transaction cannot be selected again.

### Phase 2: reconcile political units

The resolver confirms that each subject remains with its overlord. A subject is never moved independently during the baseline purge.

When a high-Evolution fracture creates a strong independence case, Event 62 may submit a request to the owner of the subject-release mechanic. That owner resolves independence. Event 62 waits for a success receipt before assigning the former subject to another side.

### Phase 3: return controlled military relationships

Where supported safely, the event should:

- return expeditionary forces before hostility begins
- end event-created military access between future enemies
- retain a short withdrawal-access window so units are not trapped without a route home
- stop new event-owned aid and coordination between future enemies
- remove only the guarantees or non-aggression relations that directly block the event conflict

Unrelated outside guarantees remain. They can influence intervention or war entry.

Existing lend-lease, research-sharing, and other relationships that the engine cannot revoke generically are not fabricated as cancelled. The event stops its own future support and records the unresolved relationship for implementation review.

### Phase 4: expel victims

Victims leave the original faction as one transaction group. Each removal writes a receipt before the next removal occurs.

The event then applies the initial victim and loyalist crisis states. It opens role events for human players and records the temporary coalition links among co-victims.

### Phase 5: delayed revalidation

A hidden follow-up runs after a short delay, planned as one day. It rechecks:

- every side leader still exists
- victims remain outside the original faction
- no country is already at war on both prospective sides
- subject bundles remain coherent
- the intended war goal remains legal
- at least one valid hostility edge remains
- a delayed shared-war separation has completed when required

The follow-up is idempotent. A second call sees the phase receipt and exits.

### Phase 6: launch conflict

The loyalist war leader declares the event-linked war against the expelled group leader or each independent victim, according to the verified engine pattern. Other loyalists and co-victims enter the same conflict side only when the implementation can prove the war graph is legal.

The event must use the smallest number of war objects that represents the conflict correctly. It must not create one redundant war for every pair of countries.

### Phase 7: open active crisis

The event registers the side leaders in a sparse active array. Only active generations receive periodic cohesion, mission, and cleanup processing.

## War launch modes

### Immediate legal war

Use this mode when the future sides do not share an incompatible war and the declaration can be made safely after expulsion.

### Delayed separation war

Use this mode when victims and loyalists currently share a war side, but the engine and repository have a verified way to remove or reassign the victim without corrupting the existing war. War begins only after the separation receipt exists.

### Armed expulsion pending war

Use this mode when a shared war cannot be separated safely. The victim is expelled and all hostile crisis state begins, but the event declaration waits until the shared war ends or another legal opening appears.

This is a designed legal-safety state. It is not a harmless resolution. The former allies retain hostile memories, the victim can prepare, and a bounded mission checks for the first legal war opening. The state closes only through reconciliation, faction dissolution, victim destruction by another actor, or the eventual event-linked declaration.

### Existing hostility

When loyalists and victims are already at war, the event does not create a duplicate war. Expulsion and crisis roles attach to the existing conflict when its sides match the intended transaction.

## Conflict intent

The faction leader chooses one visible intent after the targets are known. AI chooses from the same valid set.

### Forced compliance

This is the baseline default. Loyalists seek readmission, political submission, or a controlled postwar settlement. It should map to a limited or puppet-style legal war goal after repository verification.

### Territorial settlement

This intent is available only when loyalists hold registered cores or claims on victim territory. The settlement cannot take unrelated states through an event shortcut.

### Regime replacement

This intent requires severe ideological hostility, a supported replacement path, and a viable target government. It should not create a generic ideology flip without political proof.

### Liquidation

This is a narrow high-chaos option for a tiny target or an already terminal rivalry. It carries the strongest diplomatic and cohesion cost. It never becomes the default AI choice and never bypasses ordinary peace, occupation, Deaths, or Condemnation systems.

## Victim war aim

Victims fight for recognized separation and survival. Their public objectives are:

- retain the capital and a viable core territory
- prevent forced readmission or subjugation
- keep co-victims from making separate peace
- obtain outside recognition or mediation
- force an armistice or defeat the loyalist war leader

A victim that invades loyalist territory can gain bargaining leverage. The event does not grant automatic cores or arbitrary annexation rights.

## Initial crisis effects

### Expelled government

The initial mixed state should represent shock and emergency resolve. It may provide meaningful defensive mobilization on controlled core territory while reducing planning, supply coordination, or diplomatic access for the first stage.

After the shock period, it transforms into one of these directions:

- coordinated defense when cohesion and co-victim links are strong
- isolated government when cohesion is low
- internationally supported defense when a sponsor commits
- settlement administration after an accepted agreement

### Loyalist war council

The loyalist state improves coordinated action against the selected victims while imposing a real faction-cohesion and diplomatic cost. It strengthens or weakens according to retained-member commitments and the result of the first mission.

### Expelled governments coordination

This state exists only for two or more cooperating victims. It improves joint planning, military access, and supply cooperation. It is removed when the coalition dissolves, members make separate peace, or a permanent successor faction replaces it.

## Dynamic balance support

The event should help a very weak victim survive long enough to make choices without giving free victory.

When the loyalist-to-victim effective strength ratio exceeds a central threshold, planned around `4:1`, the victim receives stronger emergency decision access, lower mobilization costs, and higher outside-sponsor interest. It does not receive free high-quality divisions.

When the ratio is close, the event offers fewer catch-up tools. When the victims are stronger, loyalist AI becomes more willing to negotiate or limit the war aim.

Emergency formations require manpower and equipment. They use an existing legal template or a verified event-owned emergency template. No custom subunit, equipment type, model, counter, or sound package is created for this event.

## Co-victim military rules

Co-victims should cooperate unless a later choice breaks the coalition.

The event should provide:

- military access or the closest safe equivalent
- non-aggression between victims
- a shared war side when legal
- optional equipment pooling through explicit donor decisions
- a joint capital-defense or corridor mission
- a common settlement offer

It should not:

- force victims into permanent faction membership immediately
- transfer equipment without donor payment and consent
- grant cores, annexations, or subjects
- keep cooperation after a member signs separate peace

## Member stance at Evolution II

A pending member receives a short stance window. The member can:

- remain loyal to the original leader
- join the expelled bloc
- leave the faction and remain neutral

The choice is constrained by existing wars, subjects, guarantees, and side viability. A country cannot choose a side that places it against itself through another active war.

AI uses the side-choice model. A player sees the principal relationships and immediate consequences, not the hidden score.

## Outside intervention limit

Each faction transaction may invite no more than two outside powers into the active decision layer. Candidates are selected from guarantees, ideology, relations, rivalry with the leader, geographic access, and military capacity.

Baseline outside action focuses on equipment, guarantees, and mediation. Direct war entry requires existing treaty obligations or high-Evolution proof. The event must not turn every baseline purge into a global war.

## Transaction interruption

The transaction can be interrupted by annexation, civil war, faction dissolution, peace, tag change, or another event. Every phase rechecks its targets.

When a required actor disappears:

- select a successor side leader from the original snapshot when possible
- attach the crisis to an existing matching war when safe
- close a failed side cleanly when no viable member remains
- preserve completed expulsion and betrayal memory
- remove stale decisions, missions, access, and pending declarations

The event never resurrects a country merely to finish its transaction.

---

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

---

# Event 062 Evolutions

## Evolution principles

The Evolutions change the scale and political structure of the betrayal. They do not rename normal stages of the same war.

Each Evolution:

- respects its individual enable state
- requires the stated Chaos threshold
- records only when its changed behavior becomes real
- adds zero Chaos merely for eligibility, activation, or logging
- can affect a generation already in progress only after valid conditions and pacing
- can shape the initial firing immediately when the world already meets its threshold
- leaves a safe baseline route when disabled

The suggested base pacing after a threshold becomes available during an active generation is about `90` days. Dynamic factors can shorten or lengthen the wait. A completed timer never substitutes for faction, side, or legal-war proof.

## Evolution I: Alliance Purges

- Chaos requirement: `200+`
- Main change: more factions can be affected, large factions remove more members, and co-victims gain structured coordination

### Faction scale

Evolution I uses the expanded faction budget in the core specification. It favors factions with a clear vulnerable tail and enough retained members to remain viable.

Large factions follow the expanded victim-count table. A multi-victim purge must preserve one expelled group and cannot select political units that immediately create subject or war contradictions.

### Victim coordination

When two or more victims come from the same faction, the first valid Evolution I incident can create:

- the temporary expelled-governments liaison
- mutual military access and non-aggression where legal
- the joint capital-connection mission
- bounded equipment-pooling decisions
- a common settlement position
- a later successor-compact route

The victims can still disagree. Separate peace, ideology hostility, territorial disputes, or outside sponsor rivalry can break the liaison.

### Evolution proof

Evolution I records when one of these first occurs:

- a firing affects more factions than the baseline cap would permit
- one faction removes more victims than its baseline size band permits
- two or more victims establish the expelled-governments liaison

The threshold alone does not record the Evolution.

### Pre-fire behavior

At `200+` Chaos, an Event 62 firing may use the expanded faction and victim budgets immediately. The first actual expanded purge records Evolution I.

### Disabled behavior

When Evolution I is disabled:

- faction count remains at baseline
- victim count remains at baseline
- victims can receive basic non-aggression and shared defensive war alignment
- the structured liaison, joint reserve decisions, and successor-compact progress do not open through this Evolution

Baseline cooperation still prevents co-victims from automatically attacking each other.

## Evolution II: Internal Bloc Wars

- Chaos requirement: `400+`
- Main change: retained members can join the expelled governments or leave the faction, producing two opposing groups

### Eligibility proof

A full internal bloc war requires:

- at least four valid political units in the original faction
- at least two viable units on each prospective side, unless one side is a single major with strong territorial viability
- one or more unresolved tension sources
- a legal side assignment for every participating political unit
- a valid war leader for both sides
- no settlement that already resolved the purge

A faction with fewer units can still use the baseline or Evolution I purge.

### Tension sources

Valid tension includes:

- severe ideology distance from the faction leader
- poor relations with the leader and strong relations with a victim
- a prior broken guarantee, aid promise, or security charter
- large differences in war aims
- one member bearing disproportionate losses
- a leader that contributes little while demanding major sacrifices
- rival outside sponsors
- a territorial dispute between retained members
- previous Secret Alliance or faction-instability memory
- an Event 45 faction-rupture fact that is not already owned by an active Event 45 transaction

The event should not generate tension from nothing when every member is cohesive, safe, and committed to one existential war.

### Side assignment

The original leader begins on the loyalist side. Primary victims begin on the expelled side. Every other political unit receives scores for:

- loyalist side
- expelled side
- neutral withdrawal

The score reads relations, ideology, strength, shared wars, war contribution, existing tensions, geography, supply, subjects, sponsor ties, and projected survival.

Assignment follows hard legality before preference. A country that cannot join either side safely receives neutral withdrawal when legal. If neutrality is also impossible, it remains with the side that preserves the current legal war graph.

### Member choice

A human pending member sees the principal facts for each legal choice:

- side leader
- current cohesion stage
- shared enemies and contradictory wars
- expected military balance
- immediate faction and diplomacy changes

The event does not show the hidden numerical side score.

### Internal war outcomes

#### Loyalist purge with defections

One or more retained members join the victims. The original faction remains with the leader and its supporters.

#### Balanced faction split

Both sides contain several viable members. The victim side can use a temporary coalition and later form a successor faction.

#### Neutral withdrawals

Some members leave without joining either war side. Their exit lowers original faction cohesion and can accelerate a wider collapse.

#### Leader isolated

Most core members defect, leaving the legal faction leader with a small rump. This is the main route by which the leader can become the object of betrayal without unsafe direct leader expulsion.

#### Failed split

Not enough members defect or the war graph cannot be legalized. The generation continues as a normal purge. Evolution II does not record.

### Evolution proof

Evolution II records when a retained political unit actually leaves the original faction and joins the expelled side, or when the first legal two-sided bloc war begins.

A member merely considering defection does not count.

### Pacing factors

Faster pacing:

- loyalist cohesion is disintegrating
- victims survive the opening attack
- several members refused renewed commitments
- the leader is weak relative to core members
- outside sponsors back opposing camps
- The Offensive is active and the military balance is viable

Slower pacing:

- a common existential enemy remains immediate
- the original leader is very strong and trusted
- every prospective defector lacks legal access
- the victims are already near capitulation
- an armistice conference is active

### Pre-fire behavior

At `400+` Chaos, a valid faction can begin the event with pending member stances. The full split applies only after side proof. If the opening produces an actual defection and internal war, Evolution II records immediately.

### Disabled behavior

When Evolution II is disabled, retained members cannot switch to the expelled side through Event 62. They can support, withhold forces, demand safeguards, or follow other event systems that independently change faction membership.

## Evolution III: The Alliances Collapse

- Chaos requirement: `600+`
- Main change: several large factions can fracture in the same generation, with members choosing sides or withdrawing according to the live world state

### Large-faction priority

A large-faction fracture candidate normally has at least six political units. The super-event threshold uses a stricter large-faction definition of at least eight political units before mutation.

Evolution III increases selection pressure for:

- major-led factions
- alliances spanning several regions
- factions with many weak members and several rival core members
- factions already divided by war aims or sponsors
- alliances whose leader has lost military credibility

A stable large faction can still avoid a full split. Size creates exposure, not automatic collapse.

### Generation budgets

One Evolution III generation may:

- select up to six factions
- produce no more than three full internal bloc wars
- move or withdraw no more than eighteen political units across all selected factions
- invite no more than two outside sponsors per faction transaction

When a planned result exceeds the budget, the resolver preserves the highest-pressure full fractures and converts the remainder to smaller purges.

### Side logic

Members choose sides from the same Evolution II model with stronger weight on:

- existing wars
- relations with prospective side leaders
- ideology compatibility
- military balance and survival
- prior faction tension
- territorial continuity
- outside sponsor commitments
- fear of becoming the next purge target

Neutral withdrawal is more common for distant members and governments that cannot join either side without entering contradictory wars.

### Cross-faction timing

Each faction transaction remains independent. A member of one faction cannot join the split inside another faction unless it has first left its own transaction cleanly and passes ordinary faction rules.

The Evolution creates simultaneous political shock, but it does not merge every crisis into one global war.

### Global fracture super-event

A one-time super-event is justified only when the generation proves a world-order fracture. It fires when Evolution III is enabled and one of these conditions is met:

- at least three factions with eight or more political units each suffer a full internal bloc war, and at least twelve political units change side or withdraw
- at least two major-led factions split, and at least eight countries enter new Event 62 linked wars
- one faction with at least twenty political units breaks into three viable political camps, and at least ten units leave the original leader

The super-event does not fire for a single purge, a near miss, or several two-member betrayals. It is fire-once per campaign.

### Evolution proof

Evolution III records when the first generation completes the minimum simultaneous-collapse proof:

- at least two large factions suffer actual internal splits in the same generation
- at least six political units change side or withdraw across those factions

The super-event threshold is stricter than the Evolution log threshold.

### Pre-fire behavior

At `600+` Chaos, the event can build an Evolution III generation from the opening draw. Full-fracture and mutation budgets apply before any country is moved.

### Disabled behavior

When Evolution III is disabled:

- Event 62 can still use enabled Evolution I and II behavior
- no special large-faction selection bonus applies
- no simultaneous-collapse proof or super-event is recorded
- ordinary independent faction collapses can still occur through their own systems

## Evolution ordering

The Evolutions are cumulative in capability but record separately.

- Evolution I can create co-victim institutions without an internal split
- Evolution II can split one faction even when Evolution I never produced a multi-victim purge
- Evolution III can trigger only from multiple realized fractures and therefore uses the Evolution II side model
- a high-Chaos initial firing can realize several Evolutions on the same day, with one log record for each actual behavior

Disabling one Evolution removes only its owned behavior. Baseline event progression and independently enabled Evolutions remain functional.

## Evolution cleanup

Evolution state is global event capability. Generation-specific arrays, pending stances, side scores, and active missions clear when each crisis ends.

Durable facts remain:

- Event 62 victim history
- faction betrayal history
- prior defection or neutral withdrawal
- successor-faction origin
- settlement guarantees and violations
- Evolution achievement progress

---

# Event 062 outcomes, aftermath, and system connections

## Settlement framework

The event creates war and political pressure. It should also define how a crisis can end before an ordinary total peace conference erases its identity.

Every scripted settlement shows the visible terms to human participants. It identifies membership, independence, territory, subject status, truce, guarantees, and faction consequences. Hidden AI scores are never presented as terms.

The event does not seize arbitrary territory through a hidden effect. Territorial terms use registered cores, claims, occupied frontier groups, or an accepted negotiated transfer.

## Outcome families

### Loyalist punitive victory

The loyalist side achieves the active offensive mission, occupies the victim capital, forces capitulation, or obtains a decisive battlefield advantage.

Possible settlements depend on the original intent:

- conditional readmission
- political compliance or subject status when legally supported
- transfer of registered cores or claims
- regime settlement when a valid political route exists
- ordinary peace-conference handoff when no safe scripted settlement fits

The result should cost the original faction cohesion. A purge that destroys a former ally demonstrates danger to every retained member.

### Victim defensive survival

The victim holds its capital and supply spine through the mission window, remains politically viable, and prevents decisive loyalist victory.

This outcome unlocks recognized separation, stronger outside recognition, and successor-compact progress. It does not require the victim to conquer the entire former faction.

### Victim battlefield victory

The expelled side defeats or incapacitates the loyalist war leader, occupies its capital, or causes the original faction to collapse.

The victims can demand recognition, reparative equipment transfers when available, release from imposed relations, and a durable successor bloc. They do not gain automatic cores on loyalist territory.

### Conditional readmission

The victim rejoins the original faction under visible guarantees.

Required terms can include:

- a mutual security charter
- a long Event 62 victim-protection period
- restored military access
- limits on punitive territorial demands
- removal of active hostile crisis states
- retained betrayal memory and reduced trust

Readmission is fragile. A second Event 62 betrayal after a formal guarantee can create a settlement-violation fact.

### Recognized separation

Both sides accept the victim's independence from the faction.

The outcome creates a truce, removes active war missions, preserves the country's independence, and records whether an outside power guaranteed the settlement.

### Successor compact

Two or more surviving victims convert their temporary liaison into a durable faction or pact after reaching unified cohesion.

The compact receives fresh-faction protection and retains its origin memory. It becomes a valid future Event 62 target only after that protection expires.

### Neutral member exit

A retained member withdraws from the faction without entering the war. It receives a short truce and diplomatic isolation. The original faction loses cohesion and size.

A neutral exit is a completed political outcome, not a victim victory.

### Faction disintegration

The original leader loses enough members that the faction no longer exists or has no viable common purpose. Event 62 records the collapse and hands remaining wars to ordinary systems.

The event does not force all former members into one replacement faction.

### Ordinary-war handoff

A linked crisis can become part of a larger war that the event should no longer micromanage. The event then:

- freezes Event 62 settlement escalation
- removes temporary preparation decisions that no longer fit
- preserves betrayal roles and achievement facts
- leaves ordinary wars and factions untouched
- continues only bounded recognition or aftermath events when still meaningful

## AI settlement willingness

AI acceptance rises when:

- its capital is lost or threatened
- surrender progress is high
- equipment, manpower, fuel, or supply is exhausted
- the active mission failed
- side cohesion is disintegrating
- no credible outside rescue exists
- the terms preserve government viability
- continuing war threatens the rest of the faction

AI acceptance falls when:

- the capital and supply route are secure
- the active mission succeeded
- the enemy is overextended
- a credible sponsor is about to act
- cohesion is unified
- the terms demand unrelated territory or impossible political changes
- the country can realistically reverse the front

The Offensive reduces settlement willingness only when a viable military path remains. It cannot make an exhausted country reject every survivable agreement.

## Durable memories

The event preserves only facts that can change later play:

- original faction leader of the purge
- expelled victim
- co-victim partner
- retained loyalist member
- member that demanded safeguards
- member that defected
- member that withdrew neutrally
- outside sponsor
- settlement mediator
- settlement guarantor
- conditional readmission
- recognized separation
- successor-compact origin
- settlement violator
- Event 62 faction collapse
- most recent victim and faction cooldown dates

Temporary target arrays, side scores, selected decision targets, event targets, mission flags, and preparation modifiers are removed.

## Cleanup conditions

A faction transaction closes when one of these is true:

- all linked wars ended and settlement state is known
- all victims ceased to exist
- the original loyalist side ceased to exist
- the original faction dissolved and no Event 62 settlement remains possible
- the crisis was handed to a wider war
- an accepted readmission or recognized separation completed
- every surviving participant left the linked conflict through a valid outcome

Cleanup must:

- remove the crisis decision category and active missions
- clear selected-target flags and stored target IDs
- clear pending stance choices
- remove temporary access and non-aggression arrangements when their role ends
- remove or transform temporary ideas
- remove countries from the sparse active registry
- clear delayed declaration requests
- preserve durable memories and achievement receipts

## Wars cluster

Event 62 is a High member of the Wars cluster.

The authoritative workbook must add the membership without replacing other cluster memberships. The cluster runtime supports many-to-many membership and aligned member arrays.

Cluster behavior:

- Event 62 retains its own requirement for at least two valid factions
- an invalid Event 62 member is skipped with a clear reason
- a cluster firing counts once for global pacing
- Event 62 still applies its repeatable cap reduction and history when it fires as a member
- other war-cluster members and Event 62 must not act on the same country or war graph without revalidation

## Random Civil War

An expelled country can already be internally unstable. Event 62 may submit a bounded instability request when the country has real instability proof.

Random Civil War owns civil-war creation, territory division, army transfer, and cleanup. Event 62 does not duplicate those effects.

When a civil war begins:

- the recognized government keeps the Event 62 victim role unless the owner returns another result
- the rebel side does not automatically become a loyalist ally
- Event 62 revalidates capital, war leader, and settlement targets
- a destroyed or divided victim can trigger ordinary-war handoff

## The Offensive

The Offensive can change AI posture in an Event 62 crisis.

It may increase:

- willingness to choose a stronger legal war intent
- priority for punitive operations
- readiness to join a viable internal bloc war
- willingness to exploit a weakened victim

It must not bypass:

- target validity
- war-side legality
- subject safety
- supply and access
- minimum force viability
- settlement acceptance when no credible military route remains

## Secret Alliance and faction-forming events

A faction created by Secret Alliance or another event receives fresh-faction protection before Event 62 can target it.

After protection expires, its origin affects pressure and side choice:

- secret coalition memories can create lower institutional trust
- a shared hidden sponsor can strengthen one side
- recently revealed members can prefer neutral withdrawal
- betrayal history lowers future willingness to join the same leader

Event 62 never edits the owner rules of the source faction-forming event.

## A Faction Comes Calling

A recently invited country receives ordinary join grace. A country that was invited through a promise of protection gains additional weight against accepting a leader's punitive demands when that promise is broken.

Later invitations can read Event 62 victim history and reduce accession willingness or demand a mutual security charter.

## Subjects Break Free

Evolution II or III can create a political case for subject independence when an overlord and subject would otherwise need different sides.

Event 62 submits a request to the subject-release owner. It does not directly grant independence through duplicate logic. Until a success receipt exists, the subject remains with its overlord bundle.

## White Peace and peace systems

A valid White Peace outcome can close an Event 62 war. Event 62 reads the peace and records whether the result was recognized separation, readmission, or an unresolved truce.

Event 62 does not duplicate generic peace Chaos changes.

## Third Balkan War

Event 45 can read an Event 62 faction rupture as an incompatibility source inside an active Balkan conflict.

Ownership boundary:

- Event 62 owns its purge and faction transaction
- Event 45 owns its regional camps, claims, and war escalation
- neither event creates a second former-ally war between the same countries
- when Event 45 already owns a faction split, Event 62 treats those countries as an existing rupture and selects another faction when possible

## Return to Peacetime

A recent demobilization can make a country appear weak. The target model should read current military and industrial capacity, while also recognizing temporary demobilization state so the same event chain does not deterministically punish every demobilized minor.

An expelled country under Return to Peacetime can use its own rearmament decisions. Event 62 does not bypass their costs.

## Famine and Migration

Event-linked sieges, blockades, destroyed routes, and population flight are handled by the shared Famine and Migration systems.

Event 62 can provide incident context and exact participant facts. It does not apply flat population loss, refugee transfer, or duplicated famine mortality.

## Deaths, Condemnation, and Air Cleanliness

Military and civilian deaths use the shared Deaths pipeline. Nuclear, chemical, biological, atrocity, and contamination consequences use their owner systems.

Event 62 can record that a use occurred inside a betrayal war for later relations or settlement logic. It does not create a second consequence transaction.

## Event log and details

One global Event 62 history entry is recorded per firing. Per-faction role events do not each count as a pacing event.

The history entry should show:

- date
- Event 62 identity
- number of factions affected
- number of countries expelled
- number of internal splits
- number of linked wars created or attached
- largest affected faction or representative crisis when useful

A single actor flag is normally omitted because the event has several faction leaders. Evolution II may record the first split's faction leader as actor. Evolution I and III can remain global.

Event Details should present the premise and current public state. After firing, it may show the latest generation summary and the number of unresolved faction transactions. It must not expose target scores or hidden future side choices.

---

# Event 062 AI, balance, achievements, and presentation

## AI purpose

AI should make betrayal dangerous while preserving basic strategic competence. The event changes alliance behavior, but it does not instruct countries to enter impossible wars, abandon every useful partner, or refuse every viable settlement.

Every weighted selection and AI choice requires a dedicated probability audit before and after implementation.

## Faction-selection AI

The faction selector favors high internal pressure while preserving diversity among valid candidates.

It should respond to:

- faction size
- capability disparity
- political divergence
- recent military strain
- weak institutional ties
- prior betrayal or defection memories
- loss of a common threat
- fresh-faction and Event 62 cooldowns

A large stable faction should not always outrank a smaller alliance already near collapse. Evolution III adds a stronger large-faction preference only after full-fracture conditions are proven.

## Victim-selection AI

The target model should normally prefer weak, exhausted, isolated, low-contribution members.

It should protect:

- the faction leader during baseline selection
- core military and industrial contributors
- strategically essential ports, fronts, and corridors
- recent joiners during grace
- recent Event 62 victims during protection
- subject bundles that cannot be separated safely

A high-casualty country with major war contribution should usually rank below a low-contribution isolated country. The probability scenarios define this ordering as a required audit case.

## Faction leader AI

The leader chooses conflict intent from visible strategic facts.

Forced compliance becomes more likely when:

- the victim remains strategically useful
- the leader expects a quick victory
- the leader wants the country back inside the bloc
- no major territorial claim exists

Territorial settlement becomes more likely when:

- loyalists hold registered cores or claims
- the target territory is reachable
- the claim does not conflict with another loyal member

Regime replacement becomes more likely when:

- ideology hostility is severe
- a viable political replacement exists
- outside sponsors will tolerate the outcome

Liquidation remains rare. AI considers it only when the target is very small, relations are irreparable, Chaos is high, and the diplomatic and military cost is affordable.

Leader AI should secure cohesion before launching a difficult offensive. It accepts settlement when victory is no longer credible.

## Retained-member AI

A retained member evaluates:

- relations with the original leader and victims
- ideology compatibility
- fear of becoming the next target
- military and industrial strength of each side
- shared wars and contradictory enemies
- territorial connection and supply
- war contribution and perceived fairness
- outside sponsors
- prior security promises
- current cohesion

Close partners remain loyal. Politically isolated members with strong victim ties can defect. Distant or exhausted members can withdraw neutrally.

A member does not join a side merely because it is stronger. Survival matters, but relations, war legality, and political identity must remain material.

## Victim AI

Victims prioritize:

1. preventing immediate capitulation
2. protecting the capital and supply route
3. coordinating with co-victims
4. obtaining equipment or guarantees when outmatched
5. seeking recognized separation after survival proof
6. accepting readmission only when the terms preserve government viability

Victim AI does not spend its last equipment on a minor cohesion action while the capital lacks a defense. It does not donate reserves when its own divisions cannot reinforce.

## Outside sponsor AI

An outside power considers:

- relations and ideology
- guarantees and existing treaty obligations
- rivalry with the original faction leader
- strategic interest in the region
- distance, access, convoys, fuel, and equipment
- current war load
- stability and war support
- expected escalation
- whether another sponsor backs the opposite side

Mediation is favored by overextended powers and governments with balanced relations. Material support is favored when one side is strategically valuable and reachable. Direct intervention remains high-Evolution or treaty-bound.

## The Offensive integration

When The Offensive is active, AI receives stronger preference for viable aggressive actions. It should:

- favor punitive operations when supply and force ratio support them
- lower the threshold for a legal defection war
- resist settlement while a plausible offensive path remains

It should not:

- target invalid countries
- ignore shared-war conflicts
- enter a side without access
- choose liquidation by default
- continue a hopeless war after capital, supply, and reserves are lost

## Military balance anchors

The event compares effective side strength rather than raw division count. The calculation should include:

- fielded divisions adjusted by strength and organization
- available manpower
- equipment readiness
- military factories and current output
- air and naval support where the theater requires them
- fuel and supply
- number of active fronts
- capital and route security

Suggested response bands:

| Loyalist to victim strength | Design response |
| --- | --- |
| below `1.25:1` | leader AI prefers limited aims or settlement, victims receive no catch-up package |
| `1.25:1` to `2.5:1` | ordinary crisis balance |
| `2.5:1` to `4:1` | victim support interest rises and emergency costs reduce moderately |
| above `4:1` | strongest emergency tools and outside-sponsor interest, no free victory |

These are starting anchors. Final values require MCP probability and implementation balance evidence.

## Repeatability balance

The event already uses the shared Minor Repeatable weight system. The event also needs local anti-repetition:

- active faction transactions are invalid
- faction cooldown after resolution
- victim country protection after resolution
- fresh faction protection
- successor-faction protection
- no country selected twice in one generation
- no faction selected twice in one generation
- no direct repeat reward from a failed transaction

A later firing can affect former victims after protection expires. Their betrayal memory changes trust and side-choice behavior.

## Achievements

Achievement names below are working labels. Final localisation requires a separate writing pass.

### The Weak Link Holds

**Role:** expelled player country.

**Requirement:** the player was in the highest-vulnerability candidate tier at selection, remained uncapitulated, kept the original capital, and obtained recognized separation or a defensive victory.

**Disqualifiers:** console or debug disqualification under normal achievement policy, loss of original capital for the full failure period, voluntary readmission before survival proof.

**Difficulty:** hard.

**Tracking:** store the selection-tier receipt, starting capital, generation ID, capitulation state, and final outcome.

**Icon direction:** a cracked alliance chain held together around a small national shield. Completed icon shows the shield intact. Grey and not-eligible variants follow the normal achievement triplet.

### Council of the Cast Out

**Role:** expelled player country in a multi-victim purge.

**Requirement:** at least three original victims survive, establish the liaison, reach unified cohesion, form a successor compact, and secure peace with every surviving compact member independent.

**Disqualifiers:** player leaves the victim coalition before settlement, compact forms with fewer than three original victims, any counted member remains a subject of the original leader.

**Difficulty:** very hard.

**Tracking:** original victim array, liaison receipt, cohesion threshold, successor-faction origin, member independence, final peace.

**Icon direction:** several broken table placards arranged into a new circular council.

### No Second Betrayal

**Role:** player faction leader during Evolution II.

**Requirement:** after the first internal split, complete `Prevent a Second Defection`, keep at least five original political units loyal, and resolve the war without another loyal unit leaving.

**Disqualifiers:** a second defection, faction dissolution, player changes country, or the conflict ends through the leader's capitulation.

**Difficulty:** hard.

**Tracking:** original membership snapshot, first split proof, mission receipt, post-split exit counter, final loyal membership.

**Icon direction:** a war council seal with one broken segment and the remaining ring locked together.

### A Seat of Our Own

**Role:** player participant in the Evolution III world-order fracture.

**Requirement:** survive an Evolution III generation, become leader of a valid faction containing members from at least two different shattered original factions, and keep the new faction intact for one year.

**Disqualifiers:** faction created only from one original faction, fewer than three independent political units, loss of faction leadership during the holding period.

**Difficulty:** extreme.

**Tracking:** original faction identities, Evolution III generation receipt, new faction leader, membership origins, one-year timer.

**Icon direction:** two shattered alliance emblems joined beneath a new central chair.

## Achievement implementation rules

Achievements belong in the single Chaos Redux achievement registry. Each needs:

- a stable ID
- trigger and disqualifier logic
- persistent progress receipts
- English localisation
- completed, grey, and not-eligible icons
- event documentation
- catalog or achievement documentation alignment

The event cannot award an achievement from a hidden approximate score without storing the proof used at selection.

## Event and report art

### Main report image

Use a generated World War II era documentary scene. The subject should be the moment of betrayal in physical form, such as allied liaison officers removing a former partner's insignia at a guarded checkpoint, military representatives leaving a joint headquarters under armed watch, or a former ally's flag and documents being taken down while troops seal the gate.

The image should show period uniforms, architecture, vehicles, equipment, and photographic technology. It should avoid readable generated text, modern tactical gear, cinematic color grading, abstract maps, and generic conference-table compositions.

Planned event-picture canvas: `210x176`, subject to exact local consumer inspection.

### Decision category picture

Use a static full-canvas picture that establishes the broken-alliance theme. It can show severed liaison lines, empty chairs in a war council, removed insignia, or a guarded alliance headquarters. It must not contain fake buttons, fake meters, or painted interface controls.

The canonical decision-category picture references should be inspected before production. The current skill reference family uses `114x101`, but implementation must inspect the active consumer before locking size.

### Conditional super-event image

Evolution III's global fracture super-event needs a distinct generated image. It should show several alliance symbols and military delegations separating under armed pressure across one coherent period scene. It should communicate a world order breaking into rival camps without turning into a map graphic.

Planned super-event canvas: `457x328`, subject to exact local consumer inspection.

## Icon package

Each icon family needs its own generated source art and target-specific composition.

### Decision icons

- broken alliance emblem
- war council commitment
- emergency mobilization
- expelled-governments liaison
- foreign guarantee
- conditional readmission
- recognized separation
- faction defection
- neutral withdrawal
- successor compact

### Mission icons

- capital and supply-spine defense
- punitive offensive
- co-victim connection
- prevent a second defection
- armistice conference

### Idea icons

- betrayed by the bloc
- war council purge
- expelled-governments liaison
- coordinated defense
- isolated government

### Achievement icons

Four completed icons and their normal grey and not-eligible variants.

All alpha-backed icons request native transparency and preserve it through PNG and DDS processing. Each icon type uses its own source output. Focus icons, decision icons, idea icons, and achievement icons are never satisfied by resizing one another.

## Asset exclusions

The accepted event design does not introduce new countries, leaders, flags, portraits, units, equipment, technologies, buildings, 3D models, counters, unit audio, focus trees, or animated sprites.

The implementation and asset workers must not add these surfaces as decoration. A later accepted expansion can change the boundary through a new spec addendum.

## Super-event direction

The Evolution III super-event role is global alliance-order fracture.

It needs:

- one intentionally selected slot
- final title, description, reaction text, and verified quote
- unique licensed or public-domain musical audio
- generated image
- settings-aware sound playback
- one-time trigger proof
- documentation and catalog alignment

No quote, cultural reference, or audio selection is fixed by this planning pack. Those require the super-event text and audio research workflows.

## Writing direction

### Main global report

The report should describe concrete signs of alliance rupture. Suitable details include sealed headquarters, removed insignia, border posts closing, liaison officers escorted out, depot access revoked, and former partners receiving conflicting orders.

The text names the largest affected faction and states that other alliances suffered similar purges. It should not list formulas or every affected country.

### Faction leader event

The viewpoint is the government ordering the purge. The tone can use official security language, fear of weakness, and political self-justification. It should reveal the targets and visible war intent without treating the leader's claims as objective truth.

### Victim event

The viewpoint is the expelled government. It should focus on blocked communications, units stranded outside home territory, revoked access, urgent capital defense, and the identity of co-victims.

### Retained-member event

The viewpoint is uncertainty inside the alliance. The member sees which government was removed, which commitments are demanded, and why remaining neutral or defecting carries risk.

### Evolution III report

The public evidence is simultaneous alliance fracture. The text should use several concrete collapses and changing military alignments. It should avoid generic claims that history changed forever.

### Option tone

- faction leader options use security doctrine, ambition, or calculated restraint
- victim options use emergency resolve, bitter restraint, or practical coordination
- retained-member options use loyalty, fear, self-preservation, or open dissent
- mediator options use controlled diplomatic language
- a cutting or ironic option is acceptable for minor role events, but mass casualty outcomes should remain serious

Final wording must mention dynamic faction names, countries, capitals, co-victims, or settlement terms where useful. It must not expose hidden future defections or achievement conditions.
