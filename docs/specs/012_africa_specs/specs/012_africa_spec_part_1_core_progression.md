# Event 12 Africa specification, part 1

## Core promise, host selection, progression, and event flow

All route, focus, decision, event-family, and mechanic names in this file are working labels, not final localisation. Final player-facing text must be written during implementation under the localisation direction in part 6.

## The playable promise

Event 12 turns one country whose current capital is in Africa into the first credible center of a continent-wide political project. The fantasy is public and simple. Africa can become one. The campaign that follows is deliberately complicated. The unifier must protect states that still fear colonial attack, prove that membership has value, build transport and military capacity across several regions, negotiate with governments that do not want to disappear, and decide whether continental unity means a federation, a union of crowns, a revolutionary state, a military order, a confederation, or a high-chaos transformation.

The event must not begin as a map-painting command. The opening power of the unifier comes from intervention, protection, recognition, logistics, and persuasion. Direct conquest remains possible later, especially under coercive routes, but it creates an integration burden, resistance, rival leagues, foreign sanctions, and member defections. A player who treats every African state as an immediate target should reach unity faster only when military superiority is overwhelming, and should inherit a brittle state that can break during the Scramble response crisis.

The package has four linked fantasies:

1. **Continental rescue.** The unifier can protect African countries that are threatened by colonial powers or already fighting them.
2. **Continental bargaining.** Independent African governments can join a Charter League without immediately surrendering sovereignty.
3. **Continental integration.** Membership can mature through negotiated federalisation, subject relationships, public accession, or coercion.
4. **Continental transformation.** A near-unified Africa can become a world-order actor and, at extreme chaos, a sponsor or rival of other continent-scale powers.

The design must preserve two truths at once. The unifier is the campaign protagonist of this package, but African states retain political agency. They can accept protection and still reject annexation. They can demand guarantees, form regional coalitions, bargain for autonomy, leave the League, or fight.

## Event identity

- Event ID: `12`
- Event type: Minor Fire-Once
- Automatic eligibility: chaos tier 4 or higher
- Cluster: Formables
- Member severity: Severe
- Canonical entry event: `chaosx.nr12.1`
- Public fantasy: continental unity
- Primary actor: one existing country whose current capital is in Africa
- Normal terminal milestone: control and political settlement of all African regions
- Optional terminal campaign state: The World

The event is classified as minor because it begins with one country and does not instantly rewrite the world. Its implementation is still a major content package. The severe member rating reflects the scale of the possible outcome, the number of countries affected, and the amount of persistent world reaction.

## Valid host selection

Event 12 host eligibility has one geographic contract: the candidate exists and its current capital state is in Africa. This admits Liberia, Ethiopia, South Africa, subjects, governments in civil war, relocated governments, dynamically created countries, and every other live country whose capital is on the continent.

### Required host conditions

A candidate must:

- exist
- have its current capital in an African state

No dossier mapping, focus-tree type, capital control, core-state count, contact count, subject status, capitulation state, civil-war state, exile state, or country classifier may narrow that pool. Event lifecycle guards still prevent a second Event 12 campaign or a launch after the shared world-end state.

### Capital authority

There is no separate African-rooted legitimacy test. The current capital is authoritative. Identity, political status, regional relationships, and country history can alter weighting and package content, but cannot make an African-capital country ineligible.

If at least one live country has its capital in Africa, Event 12 can select a host. It is unavailable only when no such country exists, or when the separate event lifecycle guards have already closed the event.

### Selection weights

The random selection should remain unpredictable while avoiding constant preference for the largest country. Use a weighted model with visible design factors:

- independent country: strong increase
- African subject with high autonomy and controlled capital: modest increase
- country already at war with a colonial holder: increase
- country guaranteeing or supporting another African state: increase
- medium regional power: increase
- very large existing major: mild decrease
- tiny island with almost no industry or manpower: mild decrease, not exclusion
- unstable country near capitulation: decrease
- country with several African neighbors: increase
- country with only overseas contact to the mainland: decrease
- human player: no automatic priority unless settings explicitly favor player countries

The host must remain playable even when it is weak. A weak host receives stronger emergency support, a narrower early target region, and greater diplomatic leverage. A strong host receives less free material support and faces more immediate suspicion from neighboring powers.

### Regional host overlays

The shared tree and mechanic are modified by one regional overlay. The overlay changes the opening member pool, first infrastructure projects, local military traditions, restoration candidates, portrait and name pools, economic priorities, and AI target order.

| Overlay | Geographic center | Opening emphasis | Early risk |
| --- | --- | --- | --- |
| Maghreb and Sahara | North Africa and Saharan routes | ports, desert supply, anti-colonial diplomacy, trans-Saharan corridors | European naval intervention and rival claims |
| West Atlantic | Senegal to the Gulf of Guinea | ports, gold and agricultural networks, diaspora arrival, coastal defence | competing restored states and foreign concessions |
| Sahel and Lake Chad | inland West Africa and central Sahel | cavalry, caravan routes, food security, cross-desert mobility | drought, dispersed fronts, rival religious claims |
| Nile and Horn | Nile valley, Red Sea, Ethiopian highlands, Somali coast | highland defence, Red Sea access, old imperial and sultanate claims | overlapping restoration claims and foreign bases |
| Congo Basin | central river systems | river transport, mineral sovereignty, forest logistics | weak infrastructure and concessionary intervention |
| Great Lakes | Uganda, Rwanda, Burundi, eastern Congo, inland Tanzania | dense regional diplomacy, lake transport, royal restoration politics | powerful local states resist central control |
| Swahili and Indian Ocean | East African coast and islands | ports, merchant networks, naval development, island federations | overseas blockade and coastal rivalry |
| Southern Africa | Cape, Zambezi, Kalahari, and southern plateau | industry, mining, rail, liberation armies, RSA branch | Allied intervention and entrenched settler governments |
| Madagascar and Islands | Madagascar, Comoros, Mauritius, Seychelles, island routes | maritime federation, convoy defence, dispersed development | isolation, low manpower, dependence on sea control |

The overlay is not a separate small tree. It is a set of branches, decisions, scripted localisation, state targets, and package pools inside the shared architecture.

## Initial transformation

The entry event gives the chosen country a visible but incomplete continental identity. It should not instantly rename the country as a finished African superstate. The first cosmetic identity signals leadership of a continental project while preserving the host name.

Examples of early identity structure:

- direct host name with a continental adjective through cosmetic localisation
- ideology-specific public state form where appropriate
- a Charter League faction name that does not replace the country name
- a new leader frame or state emblem that shows the continental project has begun

The implementation should avoid an early map name such as “African Authority” or “Continental Bureau.” Internal institutions may use those forms. The public country name must remain a direct name.

### Immediate package

The host receives:

- the shared Africa focus tree when the host still uses the generic tree, or an additive event package when it already has a meaningful tree
- the Continental Charter decision category
- an initial national spirit representing ambition without completed capacity
- a small pool of emergency diplomatic actions
- the regional overlay
- a first set of reconnaissance and contact missions
- access to the host stabilisation branch
- a provisional continental claim map for presentation and route logic
- no blanket continental cores
- no automatic war goals against independent African states
- a member and target registry
- initial AI strategy for protection, recruitment, and regional consolidation

### Public claims and real integration

The public fantasy may show broad claims or a special continental claim state. These claims communicate ambition and support late diplomatic or war paths. They do not create free supply, compliance, manpower, or instant cores.

Real integration follows a staged process:

1. establish contact or control
2. settle the local political status
3. build security and administrative access
4. reduce resistance or gain consent
5. complete regional infrastructure and representation requirements
6. grant a core only when the route and local conditions justify it

The unifier can reach a continental map faster than it can create a stable continental state. That gap is intentional and becomes the main post-conquest gameplay pressure.

## Opening event flow

### Entry event

The root event selects the host, applies the first package, records the actor, and opens the public project. The option direction should communicate acceptance, hesitation, or route-specific ambition without presenting a final route choice in a single popup.

### First contact sequence

Within a short dynamic delay, the host receives up to five regionally relevant contacts. Fewer than three contacts, or no surviving contact at all, never invalidates the selected host. Contacts can include:

- a threatened independent African state
- an African subject seeking support
- a colony with a visible liberation movement
- a regional power that demands proof before joining
- a restored polity candidate whose supporters offer local access
- a diaspora organisation asking what return would mean in practice

The player chooses which contact becomes the first priority. The choice should change early missions and relationships rather than give a small modifier. If no valid contact exists, the direct no-contact opening records that isolation and keeps the event moving.

### First proof mission

The host must complete one visible act before it can invite ordinary members broadly. Possible proofs include:

- defend an African country at war with a coloniser
- open a supply corridor to a threatened government
- win recognition from several African states
- defeat a colonial punitive expedition
- complete a regional rail or port link
- guarantee and preserve a weak African state for a set period
- mediate an African war without annexing either side

Failure does not end the event. It lowers confidence, raises colonial pressure, and opens a harder recovery branch.

## Baseline progression

Baseline stages describe ordinary campaign development. They are not event log evolutions.

### Baseline stage 1: Proclamation and survival

The host stabilises its government, defines the first constitutional direction, and establishes a continental secretariat as an internal institution. The player learns the core values and selects an early regional objective.

The main pressures are:

- host stability
- military readiness
- transport capacity
- member confidence
- foreign scrutiny

### Baseline stage 2: Protection before accession

The host gains actions that defend African countries without demanding immediate membership. Protection can take the form of guarantees, volunteers, equipment, evacuation, intelligence, convoy support, border missions, or intervention in a war against a colonial power.

Protected states remember whether the unifier kept its promises. Successful protection raises confidence and makes future accession cheaper. Failed protection creates long-term distrust and may empower a rival bloc.

### Baseline stage 3: The first Charter members

The League forms after the host proves capacity and obtains at least two willing members or one member plus one protected state. The host can invite countries, negotiate clauses, and create shared objectives.

Membership must grant real benefits:

- defensive coordination
- access to aid decisions
- infrastructure investment
- intelligence sharing
- emergency manpower or equipment support
- arbitration between members
- protection from forced integration for an initial term

### Baseline stage 4: Regional consolidation

The first regional congress opens after the League has enough reach. The player must choose a settlement model for one region. This becomes the template for later integration and reveals the cost of centralisation.

Regional consolidation can produce:

- an autonomous member bloc
- a federated subject
- a set of integrated states
- a restored regional polity under League protection
- a rival bloc if talks fail
- a coercive occupation if the player chooses force

### Baseline stage 5: Continental programme

Once several regions are connected, the host opens the large economic, military, diaspora, and restoration branches. The campaign stops being a sequence of nearby interventions and becomes a continental logistics and political project.

## Evolution structure

The user concept contains four post-baseline escalation layers. Project guidance normally allows one logged evolution stage per chaos tier. Event 12 begins at tier 4, so only three ordinary chaos tiers remain for normal logged evolutions. This package preserves the full content through the following classification:

- Evolution I is a logged tier 4 evolution.
- Evolution II is a logged tier 5 evolution.
- Evolution III is a logged tier 6 evolution.
- Evolution IV is a post-unification escalation phase. It uses evolution presentation and content depth, but it is not recorded as a second tier 6 evolution row.

This keeps the player-facing escalation intact and avoids violating the event log rule.

### Evolution I: Regional consolidation

Evolution I becomes available after the host has one functioning Charter region, has protected or integrated several states, and has shown that the project can survive a first crisis. Its delay should use a base around 90 days with factors for war, confidence, regional control, and colonial pressure.

Active-event effects:

- opens stronger intervention and regional settlement branches
- allows wars of liberation under defined conditions
- adds regional congress missions
- unlocks first integration projects
- expands the restoration candidate pool
- permits rival regional blocs
- adds early news and foreign reaction events
- raises the importance of transport and supply

Pre-fire evolved opening:

Event 12 normally cannot fire before tier 4. If a manual or future system deliberately forces an evolved opening, Evolution I starts with one regional partner, one hostile foreign reaction, and a partially active League structure instead of the ordinary first proof sequence.

### Evolution II: Continental machinery

Evolution II requires tier 5 and meaningful control or influence in several regions. It represents a shift from a charismatic project into a functioning continental state-building machine.

Active-event effects:

- stronger but temporary military preparation tools
- regional core and claim cleanup decisions
- deeper federalisation, subject conversion, and accession missions
- a visible integration burden system
- expanded resource and industry branches
- advanced leader frames and identity states
- route-specific elite, council, and regnal flavour
- strange but still mostly human military formations
- access to elephant logistics and rare experimental units
- harder foreign sanctions and coalition pressure

Pre-fire evolved opening:

If a valid forced opening occurs at tier 5, the host begins with a provisional League, two regional pressure points, an immediate foreign ultimatum, and a more advanced but less trusted unifier identity.

### Evolution III: Africa as a world pole

Evolution III requires tier 6, near-unification or overwhelming continental influence, and completion of a major constitutional route. It changes the external scale of play.

Active-event effects:

- broader anti-colonial war goals outside the continent where African interests remain held
- continental economy and manpower mobilisation
- pressure on overseas bases and adjacent islands
- sponsorship of other continent unifiers
- diplomatic choices to support, constrain, or oppose those unifiers
- access to the Scramble response crisis when Africa is unified
- hidden high-chaos branches for supernatural and nonhuman actors
- eligibility for continent-scale unions and rivalries

Pre-fire evolved opening:

A tier 6 forced opening begins as a crisis. The host receives a strong initial identity, several potential members, at least one rival regional coalition, and immediate great-power containment. It does not receive free continental control.

### Evolution IV content phase: World-order sponsorship

This phase begins only after Africa is unified or functionally near-unified, Evolution III has fired, and at least one other continent unifier exists or can be sponsored. It is not a normal Event Log evolution stage.

It unlocks:

- continent-to-continent treaties
- union negotiations
- rivalry and containment plans
- coordinated or competing world-order projects
- readable dynamic union names
- preparation for The World is One
- continent-scale war planning
- high-chaos state transformations

## Africa is one milestone

The continental milestone requires more than direct ownership. The unifier must settle all African regions through one or more accepted statuses.

A region counts as settled when every required state is in one of these conditions:

- directly owned and integrated
- owned by a federated subject that cannot leave during the current settlement term
- held by a loyal League member under a route that recognises confederal unity
- controlled by an allied restored polity that has accepted the continental constitution
- temporarily exempt under a peace settlement with a clear completion mission

Occupied enemy territory, an unresolved civil war, or a member that is actively leaving does not count.

The milestone should:

- change the host to the final Africa identity appropriate to route and ideology
- update flag, map name, adjective, leader frame, and national spirits
- close obsolete early decisions
- open post-unification branches
- trigger a global reaction sequence
- record the continental milestone
- make the Scramble response crisis available
- preserve autonomy statuses chosen by confederal routes

## RSA in the Allies branch

RSA requires a dedicated opening because an Allied South Africa becoming a continental conqueror without internal rupture would ignore the political and military context that makes the branch interesting.

Historical inspiration includes the 1939 split between neutrality and Allied participation, the Smuts and Hertzog divide, anti-war Afrikaner mobilisation, Black political demands linked to the war, and the existence of the Ossewabrandwag. The event is alternate history. It should use these tensions as pressure points without presenting any one movement as the sole source of continental politics.

### Civil war sides

The normal branch creates two principal sides and may create a third only when campaign conditions support it.

1. **Continental Coalition.** This is the Event 12 actor. It combines African nationalist organisations, labour networks, defecting soldiers, regional leaders, and anti-colonial political groups. It receives the shared Africa package with a Southern Africa overlay.
2. **Allied Union Government.** This side retains the existing Allied government, faction membership, selected ports, part of the professional army, and foreign support.
3. **Republican Nationalist breakaway, optional.** This appears only when anti-war nationalist pressure is high. It is hostile to the Allied government and distrustful of the Continental Coalition. It must not automatically become a continental ally.

### Territory and forces

Territory should be determined by political and military factors, not a crude racial partition. The Continental Coalition gains areas where anti-colonial organisation, local legitimacy, and defecting forces are strongest. The Allied government keeps major loyal bases, naval facilities, and regions where its command remains intact. The optional third side gains a limited nationalist heartland if its prerequisites are met.

Starting forces scale from:

- RSA army size
- local population
- controlled depots
- war participation
- Allied expeditionary presence
- organisation pressure
- chaos tier

No side should receive the entire stockpile through a vanilla split that creates exploit loops.

### War aims and foreign behaviour

The Allied government seeks to restore the pre-war state and keep the Cape route. The Continental Coalition seeks control of the country and recognition of its continental project. The optional third side seeks a separate republic and may later negotiate or fight.

Allied powers can:

- send limited aid
- defend strategic ports
- impose a blockade
- demand that the Continental Coalition abandon the continental programme
- withdraw support when the war becomes too expensive
- recognise a negotiated settlement under severe world pressure

### Continental victory

When the Continental Coalition wins:

- the Allied Union Government is defeated or exiled
- the Allies receive a special peace and recognition sequence
- a forced white peace occurs if the Continental Coalition is still fighting the Allies only because of the civil war
- the Cape route and foreign bases are settled through decisions rather than automatic permanent occupation
- Allied countries receive a temporary block on immediate reclamation war goals
- the new state inherits war damage and an integration burden
- Southern African neighbours react individually

The peace is not unconditional friendship. Sanctions, naval pressure, intelligence action, and later Scramble participation remain possible.

### Continental defeat

If the Continental Coalition loses, Event 12 does not silently vanish. A suppressed route survives through exile contacts, regional League diplomacy, and a delayed second chance if an independent African state takes leadership. This recovery is difficult and should not allow endless host switching.

### Non-Allied RSA

If RSA is not in the Allies, it can be selected normally. Its opening still contains internal political conflict and legitimacy missions, but no mandatory civil war.

## Event family map

The implementation should use event families rather than one long popup chain.

| Family | Function | Typical trigger | Consequence |
| --- | --- | --- | --- |
| Host transformation | establish actor and package | Event 12 entry | tree, identity, mechanic, regional overlay |
| First contacts | choose opening priorities | shortly after entry | target pool and first proof mission |
| Protection reports | show intervention outcomes | aid, guarantees, war entry | confidence and foreign pressure |
| Charter accession | negotiate member clauses | invitation accepted | member state and benefits |
| Charter refusal | preserve agency and rivalry | invitation rejected | cooldown, demands, rival influence |
| Regional congress | settle one region | reach and membership threshold | autonomy, federation, integration, or split |
| Member crisis | defection, coup, debt, or border dispute | low confidence or high pressure | emergency missions and possible exit |
| Restoration | revive a polity or claim | route and local support | country package and territorial dispute |
| Integration | move a member toward union | consent or coercion threshold | subject, annexation, or resistance |
| Rival bloc | create regional opposition | several resistant states | counter-League diplomacy and possible war |
| Colonial reaction | sanctions, ultimatums, expeditions | intervention or integration | external pressure and war risk |
| Diaspora return | movement, settlement, and representation | route unlock and capacity | manpower, advisors, industry, social pressure |
| Evolution | record major content expansion | tier and campaign conditions | new branches and systems |
| High-chaos revelation | introduce impossible actors | Evolution III and hidden conditions | supernatural mechanics and units |
| Continental milestone | record Africa is one | all regions settled | final identity and post-unification play |
| Scramble response | global containment attempt | unified Africa | sanctions, coalition, or settlement |
| World order | other continent unifiers | post-unification phase | alliance, union, rivalry, or war |
| World-end | last continent power | extreme chaos and prerequisites | The World terminal identity |

## Failure, recovery, and partial success

Event 12 should support campaigns that do not end in total unification.

### Stable confederation

A player may deliberately stop at a large League with autonomous members. This can be a successful end state for the confederal route. It grants strong diplomacy and shared defence but does not qualify for every world-order branch.

### Regional federation

The unifier may consolidate only two to four regions. The result remains playable and can survive as a major African power. Rival blocs become persistent diplomatic actors.

### Overextended union

A coercive unifier may own most of Africa while carrying extreme integration burden and resistance. The state can fracture after military defeat, leadership crisis, or the Scramble response.

### Failed protector

Repeated inability to defend members causes exits and a legitimacy crisis. The player must complete recovery missions, accept a looser constitution, or replace the leader.

### Foreign client

Heavy dependence on one sponsor can turn the unifier into a client state. The continental project survives in name but loses independent diplomacy until the dependency is broken.

### Rival victory

A regional bloc can defeat or outlast the original host. Under strict conditions it can inherit the continental project once. The successor receives a reduced package and the original host cannot be selected again.

## Connections to other Chaos Redux events

Connections should appear only when the related event is active or its actor exists.

### Event 6 Independence Wave

New African releases become priority contacts. The unifier can guarantee them, invite them, help them survive, or compete with foreign sponsors. Independence Wave origins should affect confidence and starting forces.

### Event 7 World in Fury

Fury actors are not ordinary League members. They can sign temporary anti-colonial arrangements, but their expansion logic and special-country identity make permanent integration dangerous. The League needs containment, border, and expulsion tools.

### Event 13 Natural Disasters

Grounded routes gain relief and reconstruction missions. High-chaos nature routes can increase disaster-family pressure against enemies through abstract shared hooks. Player-facing text should describe impossible weather and recurring calamity without naming another event system.

### Event 20 Black Plague and biological warfare systems

The League gains quarantine, medical corridor, and mutual aid responses. High-chaos routes can weaponise fictional or supernatural disease effects through the existing biological warfare framework. No event text or design note should provide real-world disease creation instructions.

### Event 46 Gods of Africa or equivalent future event

The event matrix lists Gods of Africa as a separate reserved event. Event 12 should not absorb its full fantasy. It can receive rare blessings, rival cults, or shared high-chaos actors once that event has a source spec. Until then, the connection remains a gated interface, not invented implementation.

### Event 98 New Ore

Resource discoveries can accelerate continental development, create concession conflicts, or intensify foreign intervention. The unifier should have a sovereignty decision rather than receive free resources without political consequences.

### Zombie Outbreak and Death

The League can coordinate quarantines, evacuation, coastal watches, and common defence. Nonhuman existential threats can temporarily raise member confidence and reduce integration resistance, while military failure can shatter the League.

## Pacing principles

- The player should receive an actionable first contact quickly after the entry event.
- The first League member should be achievable without war.
- Regional consolidation should take sustained play and require at least one visible proof.
- Continental integration should accelerate after the second region, but integration burden should prevent a simple snowball.
- Evolutions should use dynamic MTTH with a base near 90 days, modified by campaign state.
- No evolution should fire instantly unless a forced evolved opening is used.
- High-chaos content should remain hidden until its public symptoms appear.
- The Scramble response should occur after unity, not during the final ordinary integration step.
- The World path should require several other continent-scale actors and should be rare enough to remain campaign-ending.

## Event log and detail direction

The event log should show the selected host as actor from the moment Event 12 fires. Event Details should describe the continental project, protection-first opening, League bargaining, and possible escalation. It must not list modifiers, claims, cores, or rewards.

Logged evolution rows should represent:

1. regional consolidation
2. continental machinery
3. Africa as a world pole

The post-unification escalation phase should appear through the event detail, milestone history, and world-order systems rather than a fourth tier 6 evolution row.

## Completion conditions for this part

Implementation of the core is incomplete unless:

- host selection admits every existing country whose current capital is in Africa
- every regional overlay changes actual gameplay
- the first League member can be gained without conquest
- independent African states can refuse and remain meaningful
- public claims are separated from real cores
- the RSA Allied branch creates and resolves a civil war
- the three logged evolutions and the post-unification phase are distinct
- Africa is one accepts valid federal and confederal settlements as well as direct annexation
- failure and successor outcomes exist
- event log actor and milestone direction are wired
