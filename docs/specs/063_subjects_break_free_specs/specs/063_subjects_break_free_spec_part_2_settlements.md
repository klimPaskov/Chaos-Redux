# Event 063: Subjects Break Free

## Part 2: Independence settlements and war outcomes

## Settlement purpose

Independence occurs before the final relationship with the former overlord is settled. The separation cannot be cancelled by a player or AI choice. Reactions decide recognition, continuing agreements, claims, mobilization, and the risk of war.

Each released country receives one settlement result:

1. negotiated separation
2. unilateral separation with recognition
3. contested separation without immediate war
4. armed refusal

The result is based on the subject posture, the former overlord response, the frozen relation snapshot, current war topology, and the active evolution state.

## Human choice structure

### Newly independent player

A human-controlled released country chooses a posture after independence:

| Working posture label | Meaning | Main consequences |
| --- | --- | --- |
| Conciliatory settlement | Seek recognition while preserving useful ties | Better chance of continued trade, access, guarantees, or faction cooperation. Lower immediate military readiness. |
| Guarded sovereignty | Accept practical cooperation without accepting political conditions | Balanced recognition and defense position. Keeps more options open. |
| Defiant independence | Reject former control and prepare for coercion | Stronger readiness and network support. Higher chance of claims, sanctions, border incidents, or war. |

These are working role labels. Final option text should use the voice of the affected country and the situation.

The player cannot choose to remain a subject. The event premise is the break itself. The posture determines the terms under which the new government tries to secure it.

### Human former overlord

A human-controlled former overlord chooses one policy for the release batch under its authority:

| Working policy label | Meaning | Main consequences |
| --- | --- | --- |
| Recognize independence | Accept the new status and seek ordinary relations | Removes reconquest pressure and improves peaceful outcomes. Can preserve faction ties or convert dependent agreements. |
| Negotiate association | Accept independence while seeking access, trade, bases, or guarantees | Creates bilateral terms where the released state agrees. Failure leads to unilateral recognition or a contested settlement. |
| Contest the separation | Refuse full recognition without opening immediate war | Creates claims, diplomatic pressure, mobilization, and a possible ultimatum or border incident. |
| Restore authority | Prepare force to reverse the breakaway | Available only when a safe armed route exists. At Evolution II it can open one combined independence war against a cohort. |

The batch policy applies to all subjects released from that overlord in the firing. Each pair can still resolve differently because subject postures, claims, faction ties, geography, and military balance differ.

The former overlord cannot force the countries back into subject status through the event choice. Restoration requires a war outcome or a later ordinary game action.

## Multiplayer reaction window

Independence is immediate even when a player controls the subject and another player controls the former overlord. The event does not wait for all human players before changing status.

A human-human pair enters a short pending settlement window:

- both players receive their reaction event
- each choice is stored independently
- the pair resolves as soon as both choices exist
- if one side does not answer, a pragmatic default resolves the pair after a small number of game days
- the timeout must not pause other releases or other players
- a direct independence war cannot start until the pair resolves
- saving and reloading preserves the pending choices and deadline

The default for an unanswered subject is Guarded Sovereignty. The default for an unanswered former overlord is Negotiate Association when practical, otherwise Recognize Independence. The timeout should never select Restore Authority automatically for a human player.

A player overlord receives one batch event covering every former subject in the firing. A player subject receives one direct event because its country has one settlement to resolve. Other human players receive the global report only.

## AI settlement evaluation

AI countries evaluate the same postures and policies. Their weights should reflect the actual relation. Ideology alone is insufficient.

### Newly independent AI

Conciliatory behavior is favored by:

- high opinion of the former overlord
- shared ideology or a stable political relationship
- continued faction membership
- dependence on former-overlord trade, access, or protection
- a common external war
- weak armed forces and no nearby liberation support

Guarded behavior is favored by:

- mixed relations
- moderate relative strength
- a need to preserve trade or military access
- uncertain foreign recognition
- a dangerous neighborhood
- a former overlord that appears willing to negotiate

Defiant behavior is favored by:

- strong hostility or ideological conflict
- a credible independent army
- major claims or cores in dispute
- support from other liberated states
- Liberation Pact guarantees or high Pact cohesion
- recent repression or forced reduction of autonomy
- a former overlord already weakened by war

### Former-overlord AI

Recognition is favored by:

- high war load, low stability, high surrender progress, or severe casualties
- friendly relations and ideological compatibility
- a subject that already had high autonomy
- a desire to preserve the faction or military access
- strong foreign guarantees for the released state
- a large release batch that the overlord cannot realistically reverse

Negotiated association is favored by:

- important bases, trade routes, resources, or access
- moderate relations
- a former overlord that expects influence to survive independence
- a released country that remains open to cooperation
- shared enemies or an ongoing common war

Contestation is favored by:

- disputed cores or strategic territory
- low subject autonomy
- a nationalist or authoritarian government
- domestic weakness that makes concession politically costly
- a strong army combined with uncertainty about a full war
- a belief that diplomatic pressure can recover privileges

Armed refusal is favored by:

- a safe war topology
- a strong former overlord
- a strategically important subject
- severe hostility and unresolved claims
- a credible restoration objective
- low external support for the breakaway
- Evolution II when several subjects can be fought in one coherent theater

Armed refusal should become unattractive when the former overlord is already losing a major war, when the released state has overwhelming guarantees, when the sides remain co-belligerents against a common enemy, or when opening the war would cause uncontrolled faction escalation.

## Settlement matrix

The following matrix gives the intended result ordering. It does not prescribe fixed probabilities.

| Subject posture | Overlord recognizes | Overlord negotiates | Overlord contests | Overlord seeks restoration |
| --- | --- | --- | --- | --- |
| Conciliatory | Negotiated separation | Negotiated separation if terms are accepted, otherwise unilateral recognition | Contested separation with strong mediation chance | Contested separation at baseline, armed refusal only when safe |
| Guarded | Unilateral separation with recognition | Negotiated or unilateral recognition | Contested separation | Armed refusal when safe and credible |
| Defiant | Unilateral separation with recognition | Unilateral recognition after failed talks, or contested separation over specific terms | Contested separation with high mobilization | Armed refusal when safe, especially under Evolution II |

Negotiation is not a second independence gate. It concerns ordinary interstate terms after independence.

## Outcome 1: Negotiated separation

The former overlord recognizes independence and both governments agree on at least one practical relationship.

Possible retained or converted arrangements include:

- faction membership
- guarantees
- military access
- docking rights
- resource rights or trade preference
- equipment licenses
- limited basing or transit rights
- non-aggression pact
- continued lend-lease for a bounded period

No arrangement is automatic. It must fit the previous relation and the two postures. A conciliatory released state can retain several links. A guarded state may accept trade and access but reject bases. A defiant state rarely accepts a negotiated package even after recognition.

The settlement should remove subject-only arrangements that no longer make sense. The countries now interact as independent states.

### Diplomatic aftermath

- mutual opinion normally improves or remains stable
- the former overlord receives no restoration war goal
- temporary historical claims created only by the separation are cleared
- the released country can receive a guarantee from the former overlord if relations are strong
- faction membership can continue when both sides agree and the faction leader accepts it
- the released country joins the liberation network as an active independent state
- Pact membership remains a separate decision

A peaceful outcome should be strategically useful. It preserves influence, access, and alliance options for the former overlord while giving the released country legal security.

## Outcome 2: Unilateral separation with recognition

The released country declares its terms and the former overlord accepts the new status without a detailed association agreement.

### Diplomatic aftermath

- no restoration war goal is created
- subject-derived military control and access are removed unless an ordinary agreement already exists
- the former overlord can keep trade or non-aggression arrangements when both sides remain friendly
- faction membership is reviewed and is not automatically removed
- mutual opinion changes according to whether recognition was willing or reluctant
- the released country can seek guarantees and wider recognition through the liberation network

This is the normal fallback when negotiation fails over bases, access, or economic terms but the former overlord still accepts independence.

## Outcome 3: Contested separation without immediate war

The released state is independent, but the former overlord refuses to treat the settlement as final.

### Contested sovereignty state

Both countries receive a visible temporary diplomatic condition that explains the unresolved dispute. The condition should affect recognition, relations, border readiness, and AI behavior. It must not become a large generic combat modifier.

The dispute can contain one or more specific issues:

- restoration of subject status
- military bases or access
- strategic ports or islands
- outstanding debts or equipment
- disputed cores or claims
- faction membership
- treatment of former-overlord forces
- control of a border crossing, railway, or supply route

The event should choose issues that exist in the snapshot. It should not invent a strategic-port dispute for a landlocked country or a territorial dispute where neither side has a relevant core or claim.

### Pressure sequence

A contested settlement can produce:

- recognition missions
- mediation offers
- sanctions or suspended trade
- a bounded ultimatum
- frontier mobilization
- a border incident where a real border exists
- foreign guarantees
- liberation-network aid
- a later negotiated settlement
- escalation into an independence war under Evolution II

A border incident is valid only when the two countries share a land border and are not already at war with each other. Either country may be fighting unrelated wars. If they do not share a border, use diplomatic pressure, naval access disputes, or an ultimatum instead.

### Claim discipline

The event does not grant broad claims on the former empire.

- existing cores and claims remain
- the former overlord may receive a time-limited restoration claim or restore-subject war goal against the released country's current territory
- any new claim must be limited to land that the former overlord previously administered through the subject relation or already claims
- the released state receives no free claims against the former overlord merely because it became independent
- border disputes use existing territorial facts or a narrow event-specific strategic issue

Time-limited claims and restoration goals expire after recognition, mediation, a settled peace, or a long period without use.

## Outcome 4: Armed refusal

The former overlord attempts to reverse the separation by force. The released country fights to preserve its independence.

At baseline, armed refusal is a rare safe outcome and one firing can open at most one new independence-war theater. If several selected pairs qualify, the highest-priority safe pair can enter war and the others remain contested. Evolution II expands the event into coordinated wars and raises the total firing cap to two theaters across compound and individual wars.

### Safe war gate

A direct war can start only when:

- both countries still exist and remain independent of each other
- neither country is already at war with the other
- the war does not violate a protected owner-system transaction
- the released state controls territory from which it can fight
- the former overlord can reach the theater or has a valid strategic route
- the sides are not locked on the same side of an external war in a way that the engine cannot safely separate
- faction and guarantee chains have been evaluated
- expeditionary forces, military control, and subject-derived access have been returned or ended
- the event can assign coherent war leadership and goals

When a common external war makes immediate conflict unsafe, the result becomes a contested wartime separation. Recognition or armed settlement resumes after the common war or after the topology becomes safe.

### War aims

The former overlord fights to restore a subject relationship. Annexation is not the default objective.

The breakaway side fights for:

- recognition of independence
- survival of its current owned territory
- removal of temporary restoration claims
- ordinary postwar relations or a bounded truce

The war should not produce free cores, continent-wide claims, or a generic conquest mandate for either side.

### Forces and starting condition

Because the released state keeps its existing armed forces, Event 063 does not grant a replacement army. It can receive a temporary mobilization condition, emergency equipment from allies, or network support when the military balance is poor. Such support comes from decisions and existing stockpiles, not from unlimited scripted equipment.

A former overlord should not retain control of the released state's expeditionary units, garrisons, or subject-derived military access when war begins. Units that cannot be returned cleanly must be removed from foreign control before hostilities.

### Third-party escalation

The event distinguishes support from direct intervention.

1. diplomatic recognition
2. equipment, convoys, fuel, or financial burden
3. advisers or volunteers
4. guarantee
5. direct entry into the independence war

Most outside support should stop at levels two or three. Direct intervention is reserved for countries with enough strength, access, political compatibility, and manageable war load. Evolution II can increase willingness, but it should not call every faction or guarantee into every local conflict.

## Compound independence wars under Evolution II

When several subjects of the same overlord break free in one firing and the former overlord refuses recognition, the event can create one compound war.

### Theater construction

- all safe breakaway members of the cohort join the same defensive side
- the strongest viable breakaway becomes war leader
- the former overlord leads the restoration side unless an existing faction structure requires another valid leader
- one compound war is created for the coordinated former-overlord cohort
- selected armed refusals involving other former overlords can open individual independence-war theaters
- one firing can open at most two new independence-war theaters across compound and individual wars
- unsafe members remain in contested separation and can join later only when topology permits

A compound war should not create separate duplicate wars between the same overlord and each subject.

### External liberated-state intervention

Compatible countries freed through Event 063, Independence Wave, or Soviet Collapse may answer a request from the breakaway war leader.

A theater can have at most three direct liberated-state interveners. Additional supporters provide material aid, volunteers, recognition, or mediation. This cap prevents a local independence war from pulling the entire liberation network into direct combat.

The Liberation Pact can coordinate support. Its members still evaluate access, strength, current wars, cohesion, and the risk of exposing their own territory.

## Peace and war termination

### Breakaway victory

A breakaway victory produces:

- recognition by the former overlord
- removal of the restoration objective
- cleanup of event-created temporary claims
- a truce
- increased liberation-network standing
- increased Pact cohesion when Pact members honored commitments
- no automatic annexation of former-overlord territory

### Negotiated or mediated peace

A white peace or negotiated settlement can count as successful independence when the breakaway remains independent. It should remove restoration goals and settle or defer narrow territorial disputes.

### Former-overlord victory

The normal former-overlord victory restores a subject relationship. The autonomy type should reflect the campaign and war result. It must not default to the harshest possible status.

- negotiated surrender can restore a high-autonomy relation
- decisive military defeat can restore a lower-autonomy relation
- a government that accepted foreign intervention may receive stricter terms
- annexation requires an ordinary justified path or a separate accepted event outcome

The shared liberation-origin record remains as history but active network and Pact membership are suspended.

### Former overlord ceases to exist

The breakaway side receives recognition. Event-created restoration goals and claims are cleared. The war closes or is inherited only if another legitimate owner system explicitly provides a successor claimant.

### Long stalemate

A prolonged war opens mediation. Factors include casualties, unchanged fronts, shared enemies, supply failure, and outside pressure. Mediation should become more likely before a small independence war consumes many years without movement.

### Breakaway ceases to exist

Its active network membership is removed. Its origin record remains historical. If the country later returns through a valid owner system, the record can be revalidated.

## Faction handling

### Peaceful separation

A released country may remain in its existing faction when:

- the faction relation is not solely a hidden consequence of subject status
- the released country and faction leader are not hostile
- the settlement is recognized or negotiated
- the faction is not fighting a war that makes the new independent membership impossible

### Contested separation

The released country usually leaves a faction led by the former overlord. It can remain in a third-party faction when that faction independently accepts it. The event should not remove a country from an unrelated faction to make the settlement simpler.

### Armed refusal

A country cannot remain in the former overlord's faction while fighting the former overlord. It leaves or is expelled before war. Existing membership in a third-party faction is preserved only when war topology remains safe.

### Liberation Pact interaction

A country already in another faction becomes a Pact partner and remains in its current faction. Full Pact membership is for compatible unfactioned countries or countries that independently leave their prior faction through ordinary rules.

## Agreement cleanup matrix

| Agreement or relation | Negotiated | Recognized unilateral | Contested | Armed refusal |
| --- | --- | --- | --- | --- |
| Subject status | Removed | Removed | Removed | Removed before war |
| Faction membership | May remain | Reviewed | Usually removed if led by overlord | Removed if same faction |
| Military access | May convert | Retained only if ordinary agreement | Usually removed | Removed |
| Docking rights | May convert | Retained only if ordinary agreement | Usually removed | Removed |
| Equipment licenses | May continue | Can continue | Suspended or reviewed | Ended unless protected third party |
| Lend-lease | May continue for bounded period | Reviewed | Usually suspended | Ended between belligerents |
| Expeditionary forces | Returned or renegotiated | Returned unless ordinary arrangement | Returned | Returned before war |
| Guarantees | Can be created or retained | Can be created | Third-party guarantees matter | Can trigger only through safe normal rules |
| Non-aggression pact | Common | Possible | Unlikely | Removed |
| Event-created restoration goal | None | None | Possible and time-limited | Active war aim |

## Settlement resolution and cleanup

A settlement is complete when:

- the countries have a stable independent relationship or an active independence war
- all subject-derived military control has been resolved
- faction membership is coherent
- claims and war goals match the outcome
- direct human choices are consumed
- temporary settlement flags have a clear expiry or owner
- recognition and network status are updated
- pending missions and decisions reflect the current phase

A later ordinary war, alliance, puppet action, annexation, or diplomatic change remains possible. Event 063 should not permanently lock the countries into the initial settlement.
