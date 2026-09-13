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
