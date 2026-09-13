# Event 40: Lawrence of Arabia

## Catalog identity

- Event ID: `40`
- Event name: Lawrence of Arabia
- Event type: Minor Fire-Once
- Minimum Chaos level: `1`, Calm World
- Cluster: none
- Planning status: complete design specification, pending implementation
- Catalog status until implementation and validation: To Be Reworked

Event 40 enters the normal event pool once. Its entry event is removed permanently after firing. The intervention campaign that follows is an internal event chain. Later Arabian targets do not count as new random event firings and do not add extra event-timer pressure.

The current exported catalog describes Event 40 as Minor Repeatable. That row is stale. The accepted design in this specification uses Minor Fire-Once. The authoritative workbook must be corrected during implementation, then the three catalog CSV snapshots must be regenerated through the repository exporter.

## Playable promise

Britain recalls T. E. Lawrence from a concealed life and sends him into an Arabian government that is vulnerable, strategically useful, or willing to bargain. Lawrence arrives with access to British funds, arms, officers, transport, intelligence, and political promises. The target government can cooperate, bargain, contain the mission, dismantle it, redirect it toward an independent Arab project, or lose control of its own officers and local allies.

The event is a regional contest over sovereignty. Britain tries to turn one intervention into a network of clients, allies, bases, routes, and political contacts. Arabian governments try to secure aid without surrendering policy, defeat the network, or use its resources to build a regional order that Britain cannot fully control.

Lawrence is a catalyst and a character with unusual reach. He is not treated as the sole creator of Arab politics or military action. Local rulers, officers, tribal leaders, urban nationalists, civil servants, smugglers, railway workers, and rival foreign sponsors determine what his campaign can accomplish.

## Historical correction for the 1936 setting

T. E. Lawrence died in May 1935 after a motorcycle crash. Event 40 begins after the standard 1936 start date, so the event cannot quietly present him as an ordinary living British officer.

The baseline premise is a concealed survival. Britain publicly accepted Lawrence's death while a small circle moved him into recovery and isolation. The entry event reveals that a man believed dead has been recalled for one more mission. The event does not claim a supernatural resurrection at Calm World. Nearby governments may suspect an impostor, a double, or a British deception, but the internal character is the real Lawrence unless a future accepted design explicitly creates a separate impostor branch.

This premise carries four rules.

1. The opening text must acknowledge that Lawrence was believed dead.
2. His survival remains a British secret until the first target detects or publicizes the mission.
3. If Lawrence dies during Event 40, he cannot return.
4. If installed vanilla or Chaos Redux already owns Lawrence as a live character, implementation must reuse or transfer that one character through a guarded ownership contract. It must not clone him.

## Event scope

### Britain

Britain is the normal sponsor and must exist when the event is selected. Britain must also be capable of supporting a foreign mission.

A valid sponsoring Britain normally meets all of these conditions:

- it is not capitulated
- it is not an actual nonhuman country
- it has a functioning government and can use normal diplomatic and civilian systems
- it can reach at least one valid Arabian target through land, port, air, subject, ally, or established client access
- it can commit a minimum intervention package without creating a negative stockpile transaction
- no terminal state has permanently removed Lawrence

A temporary British inability pauses the next regional stage. Examples include severe convoy loss, occupation of all useful regional bases, a temporary government crisis, or a war state that makes the mission impossible. A permanent inability ends the campaign. Examples include British annexation, permanent loss of Lawrence and all local networks, or a settlement that dissolves the British Arabian project.

A non-British successor does not automatically inherit the campaign. A successor can continue only when it inherits the British state, the event's sponsorship ledger, the relevant contacts, and a valid political claim to continue the mission.

### Arabian target registry

Target identity must use an explicit Event 40 registry. It must not infer Arabian identity from desert terrain, religion, language, ideology, continent, or a broad Middle East region.

The ordinary registry covers sovereign or potentially sovereign governments centered in:

- the Arabian Peninsula
- the Levant
- Mesopotamia

Egypt can join the target registry only when it is independent, outside a British subject relationship, and politically able to negotiate as its own government. North Africa west of Egypt is outside the ordinary campaign. This limit keeps the event focused and avoids turning one fire-once event into a general imperial influence system.

A released country created by Independence Wave or another valid liberation route can become eligible when its capital and core territory belong to the Event 40 registry. A temporary revolt tag is eligible only after it has a stable government, controlled territory, a valid capital, and enough lifecycle proof to survive the intervention.

A country is not a valid ordinary target when any of these conditions apply:

- it is classified as a special Chaos country
- it is actually nonhuman
- it is already a settled Event 40 client, ally, counter-bloc member, or federation member
- it has no controlled core state in the registry
- it is a British subject whose relationship already provides the same access that an intervention would seek
- it is in a terminal civil war state with no stable government to negotiate with
- it is already the active target
- its event package is being removed or rolled back

British subjects and earlier clients can still act as regional nodes. They can provide bases, ports, rail access, officers, intelligence, airfields, equipment, political pressure, and safe routes. They are not selected again merely to repeat the same settlement.

### Target weighting

Target selection is dynamic. The implementation should calculate a score from current conditions, then use weighted selection among all valid candidates.

Factors that raise target weight include:

- low stability or a divided officer corps
- a recent coup, civil war, independence, defeat, or colonial withdrawal
- strategic ports, oil, railways, air routes, or adjacency to existing British clients
- a government already requesting arms or protection
- an existing British military, diplomatic, commercial, or intelligence presence
- a nearby hostile power that makes British support attractive
- a player-controlled Arabian country, which must remain eligible without receiving an automatic preference that overwhelms all other logic
- Evolution II regional pressure from existing clients

Factors that lower target weight include:

- a strong intelligence service
- high stability and a consolidated officer corps
- an earlier neighboring success against Lawrence's methods
- membership in a functioning anti-British regional coalition
- British inability to reach the country safely
- recent settlement of another foreign intervention
- severe British overextension

The selection model must not use an undocumented exact probability claim. Probability evidence must be produced through named scenarios after implementation.

## One public mechanic value

### Lawrence's Influence

The target country tracks one persistent public value during its intervention, `Lawrence's Influence`, on a range from `0` to `100`.

This value summarizes the practical strength of the British-backed network inside the target. It includes access to officers, political leaders, tribal allies, intelligence contacts, routes, arms distribution, public promises, local intermediaries, and the government's willingness to follow British policy.

The category header shows:

- the exact current value
- a short qualitative band
- the recent direction of movement
- the next important threshold
- one concise explanation of the largest actionable cause of the current trend

Working band labels:

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| `0-19` | Broken Access | The mission has little reach and can be removed safely if Britain cannot rebuild it. |
| `20-39` | Restricted Mission | Lawrence has contacts and access, but the government controls the terms. |
| `40-59` | Contested Network | Britain and the target can both shape the settlement. Most bargaining routes are open. |
| `60-79` | Embedded Mission | British-backed institutions influence military and diplomatic policy. |
| `80-94` | Ascendant Network | The government risks losing effective control over officers, routes, and foreign policy. |
| `95-100` | Dominant Influence | A client, protectorate, government replacement, or exceptional counter-move can resolve the crisis. |

These are design bands, not final localisation. Implementation may adjust exact thresholds during evidence-based balance work, but it must preserve six readable states and the same broad outcome structure.

### What raises Influence

Influence can rise through:

- British arms and support-equipment deliveries that arrive successfully
- British gold, industrial aid, fuel, convoys, trains, aircraft, officers, or intelligence support
- target cooperation that grants direct access to officers, press, ports, railways, airfields, or government ministries
- British military or diplomatic victories that increase the value of British protection
- instability, government failure, local mutiny, or a foreign threat that makes British help more credible
- successful missions that secure routes, officers, communications, or local allies
- Evolution I sabotage and revolt incidents that the target fails to contain
- Evolution II pressure from neighboring clients and shared regional institutions

### What lowers Influence

Influence can fall through:

- exposed British agents or financial records
- arrests or defections among collaborators
- effective target counterintelligence
- route closures and interception of arms or gold
- secure foreign support that reduces dependence on Britain
- a target victory that improves confidence in its own government
- public proof of contradictory British promises
- Lawrence accepting limits or siding with a sovereign Arab charter
- British overextension, convoy failure, loss of regional bases, or political disavowal
- successful missions that guard institutions, turn contacts, or dismantle revolt cells

### What remains hidden

The simulation can track additional internal facts without asking the player to remember them as meters. Hidden or qualitative values include:

- British regional reach
- target preparedness
- local cell strength
- officer sympathy
- local political cooperation
- personal trust in Lawrence
- British promise credibility
- counter-bloc support
- federation readiness
- intervention generation and transaction proofs
- neighboring resistance memory
- current route safety

These facts feed Influence, AI decisions, incident selection, outcome gates, and tooltips. They do not become separate persistent public counters.

## Event lifecycle

Only one Arabian country is the active intervention target at a time. Earlier settlements remain active as regional memory and can affect later stages.

### Stage 1: Recall and arrival

Britain resolves the concealed-survival premise, verifies that Lawrence is available, and selects the first target. The target receives the opening event and the intervention category.

The first target should begin near the center of the scale only when Britain has strong pre-existing access or an evolution changes the opening. An ordinary baseline intervention begins with enough Influence to create a problem without deciding the outcome immediately.

The opening package sets:

- the active target
- the campaign generation ID
- starting Influence
- the first British support commitment
- visible intervention category state
- target and British strategy profiles
- Lawrence's current character role
- regional reaction eligibility

### Stage 2: Terms of access

The target decides the initial legal and practical status of the mission. It may grant broad access, accept narrow military aid, require government custody of arms, restrict Lawrence's travel, create a liaison office, or begin a counterintelligence file.

Britain decides how much it is prepared to commit. Heavy commitment produces faster gains and higher exposure. A limited mission preserves resources and reduces scandal risk, but gives the target more control.

This stage should normally last long enough for both human and AI governments to act. It is not a single popup outcome.

### Stage 3: Network contest

The active phase combines decisions, missions, incidents, military and diplomatic events, intelligence strength, route access, and changes in the wider war.

The player sees three to five relevant actions at a time. Obsolete actions disappear. No more than two active Event 40 missions should normally be visible at once.

The contest can move in either direction. It can pause around a negotiated middle band, accelerate toward dominance, or collapse after exposure.

### Stage 4: Institutional decision

An outcome becomes available when the target has remained in a decisive band long enough and the necessary political facts exist.

High Influence can create a client, protectorate, or British-backed government. Middle Influence can create an independent ally or armed partner. Low Influence can produce expulsion, arrest, dismantlement, or a negotiated British withdrawal. The rare defection route depends on Lawrence's personal state and cannot be selected through a simple public button.

A threshold alone does not force the settlement on the same day. The implementation should use confirmation periods and a short final mission or event so temporary spikes do not decide the country.

### Stage 5: Settlement and regional transfer

The event records the target outcome, closes its active intervention actions, applies persistent consequences, and updates regional memory.

After a dynamic delay, the campaign can select another valid target when Britain and Lawrence remain able to continue. The delay normally ranges from roughly three to eight months and changes with:

- British resources
- number and quality of established regional nodes
- previous exposure or failure
- war state
- distance and route access
- current evolution
- Lawrence's health, captivity, or political status

A typical campaign should resolve three to six interventions. A short campaign can end after one decisive failure or one settlement that removes Lawrence. A successful Evolution II campaign can last longer when enough valid governments remain.

## Baseline outcomes

### British protectorate or client government

This is the normal dominant-Influence settlement.

The target receives meaningful British assistance, which can include equipment, training, research cooperation, infrastructure projects, intelligence support, supply access, air routes, and protection. Britain receives durable access and strong control over the target's external policy.

The result must use an appropriate HOI4 autonomy or diplomatic structure. It cannot be represented only by a national spirit that claims the country is a client while it remains fully independent in every system.

The target retains internal agency. It can later seek autonomy, exploit competition among British clients, or join an independent federation route if the event state supports that transition.

### Independent British ally

The target accepts a durable British partnership without losing sovereignty.

Britain can receive military access, docking rights, supply cooperation, intelligence liaison, arms contracts, and improved relations. The target keeps independent diplomacy and can refuse later regional obligations.

This outcome should be attractive to a government that needs protection but has enough authority to resist a client settlement.

### Sovereign armed partner

The target accepts weapons and training under its own custody while rejecting broad British political access.

This settlement gives narrower benefits than a full alliance. It can create a strong anti-rival relationship without placing the target inside a British regional system. It is a common result for nationalist or cautious governments that successfully keep Influence in the lower middle bands.

### Restricted mission or unresolved balance

A campaign can end without a permanent alignment when neither side can force a settlement and the cost of continuing becomes too high.

The target retains a small British contact network and a limited suspicion modifier. Britain receives no client node. Later governments know that a British mission operated there, but the country is not permanently locked out of all diplomacy with Britain.

### Expulsion or arrest

A successful target government can expel Lawrence or detain him.

Expulsion removes the active mission, gives the target a national-confidence or anti-intervention benefit, and increases preparedness in nearby countries. Lawrence returns to Britain only if he escapes or Britain negotiates his release.

Arrest creates a separate recovery, exchange, trial, or defection chain. Britain can attempt a rescue, offer concessions, disavow Lawrence, or accept a public defeat. A prisoner cannot simultaneously act as a British operative elsewhere.

### Network dismantled

The target removes the mission and proves that the financial, officer, and route networks have been broken.

This is a stronger result than expelling one individual. It weakens British regional reach, creates durable methods that neighboring governments can copy, and can help form an anti-intervention coalition.

### Double-game victory

A skilled target can accept aid, expose selected British contacts, keep the useful parts of the network, and deny Britain the expected settlement.

This route requires strong intelligence or political capacity. It gives more material benefit than simple expulsion, but it carries a high risk of British retaliation and internal scandal if the operation fails.

### Lawrence defects to an independent Arab cause

This is a rare hidden settlement. It requires sustained personal trust, visible British overreach, a credible sovereign Arab program, local success, and a political route that can use Lawrence without placing him above every local leader.

Defection changes the regional campaign immediately. Britain loses its strongest intervention figure. British local agents may continue in reduced form. Lawrence becomes an adviser, commander, federation architect, or political figure for the independent project according to the accepted route.

Defection cannot occur because the target clicked one cheap decision. It must be assembled through several earlier choices and campaign facts.

## Regional completion conditions

The baseline campaign ends when any of these conditions becomes true:

- most valid Arabian governments have reached a durable settlement
- no valid target remains
- Lawrence is dead
- Lawrence is permanently removed and Britain chooses not to continue through local agents
- Britain loses the ability or political will to support the campaign
- a strong anti-British regional coalition defeats the network
- the event stabilizes into a durable British Arabian System
- Evolution III forms a regional federation and absorbs or supersedes the intervention campaign

The event must have a bounded cleanup path for every ending. It must clear active target pointers, missions, temporary access, queued incidents, category visibility, and generation-scoped data while preserving durable outcome memory.

## Lawrence as a character

Event 40 uses one canonical T. E. Lawrence character.

Possible roles include:

- concealed British liaison
- field adviser
- intelligence operative
- military adviser
- political adviser
- detained prisoner
- expelled former mission head
- independent Arab adviser
- federation architect
- rare federation leader
- retired or disavowed figure
- dead character

Lawrence should not begin as a super-general with extreme combat statistics. His strongest effects belong to liaison work, irregular strategy, intelligence, logistics, political access, and coordination. A military command role can become available through the campaign, but it remains grounded in the force and government that appoint him.

Character state changes must have immediate mechanical effects.

- Capture blocks normal British actions and opens recovery or negotiation.
- Expulsion removes access to the current target and raises neighboring preparedness.
- Defection closes British personal actions and opens independent Arab routes.
- Injury slows travel and can pause the campaign.
- Death permanently closes every Lawrence-dependent route.
- Leadership of a federation removes him from simultaneous British or target advisory roles.

Local British agents may continue after Lawrence is removed, but their actions are weaker and the hidden personal routes close.

## Player-facing writing direction

The text should center concrete actions and local actors. It should mention officers, rulers, tribal leaders, ministries, ports, railways, supply routes, gold, arms, public promises, and intelligence contacts.

The opening should communicate three facts without turning into an implementation explanation:

- Lawrence was believed dead
- Britain has concealed his survival
- an Arabian government has become the first destination of the renewed mission

Arabian governments must read as active political actors. They bargain, refuse, deceive, organize, cooperate, revolt, and build institutions. The event should avoid a passive population waiting for one British adventurer to create history.

The tone is serious, suspicious, opportunistic, and political. Small moments can use dry official irony. Violence, betrayal, colonial domination, and civil conflict should not become cheap comedy.

Do not use film stills, film dialogue, or actor likenesses as historical evidence. Do not copy the heroic lone-man framing associated with later popular culture.

All labels in this specification are working labels. Implementation owns final localisation after source review and localisation audit.
