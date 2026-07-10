# Event 018 AI Strategy Matrix

All route names are working labels. Final implementation should convert these intentions into route-aware focus weights, decision weights, target scores, strategy plans, and invalid-route blockers.

## Field owner behavior

| Situation | Preferred posture | Development behavior | Safety behavior | Diplomacy behavior | Closure behavior | Avoid |
| --- | --- | --- | --- | --- | --- | --- |
| Small peaceful resource-poor state | Foreign concession or balanced buyers | Develop core works with outside machinery | Moderate to high safety because losses are costly | Seek guarantee, several buyers, or commission | Close if public crisis exceeds national capacity | Nationalization without replacement capacity |
| Small state beside stronger claimant | Commission, guarantee, or cautious national authority | Improve transport and administration before maximum yield | High safety and strong field guards | Invite mediator and avoid exclusive hostile patron | Suspend or seal if defense collapses | Unilateral militarization that invites seizure |
| Industrial major with severe deficit | National authority or strategic reserve | Rapid development, domestic allocation, heavy machinery | Moderate safety unless war desperation is extreme | Use contracts selectively and resist exclusivity | Delay closure while field remains essential | Giving majority control to a rival |
| Industrial major with no deficit | Commercial charter or diversified exports | Develop if profitable and defensible | High safety because urgency is low | Invite bids and balance buyers | Close or suspend earlier in evolved crisis | Maximum extraction for no strategic reason |
| Fascist or militarized government at war | National authority, wartime requisition | Maximum shifts, guards, military transport | Low to moderate safety, concealment more likely | Reserve output, pressure neighbors, accept aligned investor | Close only when breach threatens state survival | Neutral commission unless militarily necessary |
| Communist or strongly statist government | National authority or state-to-state concession | Public works, rail, national processing | Moderate safety, mass labor possible under pressure | Nationalize foreign holdings when prepared | Full closure if leadership accepts loss of strategic asset | Permanent foreign control without leverage |
| Democratic market government | Domestic charter, regulated concession, balanced buyers | Commercial development with inspection | High safety and compensation | Normal contracts, arbitration, commission | Close when public deaths and breach are severe | Concealment and coercive labor except in extreme crisis |
| Neutral authoritarian government | National authority or one protected concession | Controlled development and strong guards | Moderate safety, concealment possible | Play rivals, seek guarantees, avoid faction dependence | Suspend if field risks regime survival | Border war against much stronger claimant |
| Owner losing a major war | Wartime requisition or emergency suspension | Extract if resource is immediately useful, otherwise deny | Lower safety under desperation | Seek aid in exchange for access | Controlled demolition, suspension, or hurried closure | Long peacetime projects that cannot finish |
| Owner with several active fields | Specialize postures by field | Prioritize highest net strategic value | Invest safety where depth and population are high | Avoid duplicate exclusive contracts | Close low-value dangerous fields first | Maximum investment in every field |

## Value-based owner rules

| Condition | AI response |
| --- | --- |
| Developed Yield low, resource deficit high, safety manageable | Prioritize appraisal, primary works, and transport |
| Developed Yield high, Foreign Pressure low | Stabilize institution and maintain regulated output |
| Developed Yield high, Foreign Pressure high | Improve guards, renegotiate access, or seek commission |
| Excavation Depth high, safety high, no evolved incidents | Continue only if resource need or contract value is strong |
| Excavation Depth high, safety low | Rotate crews, reinforce shafts, suspend deep work |
| Foreign Pressure critical with valid claimant | Prefer arbitration, guarantee, commission, or frontier mission based on strength |
| Smuggling high and material loss significant | Secure named routes and break network |
| Disturbance newly revealed | Test, inspect, evacuate lower works, and avoid immediate maximum shifts unless desperate |
| Disturbance high, public knowledge low | Careful AI reveals and restricts, authoritarian AI may conceal |
| Breach Pressure rising | Reinforce perimeter, hunt only with hard attack, prepare evacuation |
| Breach Pressure critical and full seal feasible | Begin full sealing |
| Breach Pressure critical and seal infeasible | Evacuate, request aid, prepare military defense |
| Final breach countdown active | Attempt last seal if success chance meaningful, otherwise preserve army and civilians |

## Foreign buyer behavior

| Buyer condition | Desired action | Offer composition | Escalation ceiling | Avoid |
| --- | --- | --- | --- | --- |
| Severe resource deficit at war | Seek priority or exclusive access | Equipment, machinery, guarantee, transport | Coercive pressure if owner weak and route vital | Investing in inaccessible field |
| Moderate deficit at peace | Normal contract or minority concession | Civilian construction, rail, commercial terms | Diplomatic dispute only | Border escalation without claim |
| Resource-abundant major | Observe or invest for denial of rival | Limited machinery, market access | Covert rivalry if strategic | Overpaying when supply is abundant |
| Faction leader and owner is member | Request bloc allocation | Equipment, research, protection | Faction pressure | Treating member as enemy concession target |
| Rival of existing concession holder | Competing bid, diversified access, covert survey | Better terms, guarantee, political support | Espionage and smuggling | Direct seizure without claim or military path |
| Embargoed or isolated country | Smuggling, covert purchase, alternative corridor | Intelligence, clandestine equipment | High covert activity | Public exclusive bid that cannot be honored |
| Neighbor with claim | Access demand, survey dispute, border leverage | Settlement, compensation, shared administration | Border crisis if strong and valid | Commercial-only behavior when revisionist route is active |
| Distant country with no route | Observer only | None or diplomatic statement | None | Active contract decisions |

## Investor acceptance model

The investor should estimate:

- expected resource access
- duration and stability of contract
- route security
- owner survival chance
- field stage and reserve size
- rival bids
- compensation protection
- war risk
- evolution danger after public reveal

Investor AI should withdraw or demand revision when the field is suspended, occupied, publicly overrun, or under final closure.

## Border claimant behavior

| Relative strength and context | AI behavior |
| --- | --- |
| Much weaker than owner, no guarantor support | Seek access, compensation, or arbitration, do not escalate to war |
| Similar strength, valid claim, high field value | Use surveys, patrols, frontier mission, and limited border war if negotiation fails |
| Stronger claimant, owner isolated | Demand shared access or transfer, escalate when refusal and supply permit |
| Claimant at war elsewhere | Delay, use covert action, avoid opening second front |
| Commission provides acceptable quota | Comply unless ideology or expansion route strongly rejects it |
| Owner violates commission and claimant is prepared | Demand restoration, mobilize, then reopen dispute |
| Field is closing or resources are removed | Reduce escalation, pursue compensation or abandon claim |
| Evolution III public crisis | Shift from territorial seizure to containment, quarantine, or opportunistic occupation based on ideology and threat |

## Foreign aid during Evolution III

| Donor type | Aid preference | Conditions | Expected return |
| --- | --- | --- | --- |
| Ally or faction leader | Equipment, volunteers, transport, access | Owner is strategically important | Military access, bloc security, relations |
| Concession partner | Engineers, hard-attack equipment, evacuation support | Contract and field assets at risk | Preserve concession or compensation |
| Neighbor under threat | Border troops, intelligence, tunnel mapping | Breach can spread or cave country can emerge nearby | Joint defense and field containment |
| Distant major | Research aid, equipment, observers | Public evidence and global concern | Intelligence, influence, future access |
| Rival seeking advantage | Conditional aid or deliberate delay | Owner weak and field valuable | Concession, base access, political leverage |
| Isolationist or overextended state | Little or no aid | No direct threat or resources unavailable | None |

## Anti-cave ordinary-country AI

| Strategic problem | Priority response | Required checks | Failure response |
| --- | --- | --- | --- |
| Cave armor exceeds piercing | Anti-tank research, production, lend lease request, armor concentration | Current piercing, stockpile, factory capacity | Delay and fortify instead of attacking |
| New resource state occupied less than activation period | Immediate recapture mission | Distance, supply, available divisions | Prepare denial or containment if recapture impossible |
| Mature anchor near front | Concentrated hard-attack offensive and engineering cleanup | Piercing, air support, supply | Isolate anchor and cut routes |
| Defender must retreat from rich state | Resource denial and evacuation | Time, engineers, civilian routes | Leave intact only if denial impossible or political route forbids |
| Origin state exposed | Strategic offensive toward origin | Front feasibility and coalition support | Keep pressure while securing own anchors |
| Tunnel infiltration route suspected | Guard hubs, forts, anti-tunnel mission | Intelligence evidence and valid states | Fall back to layered defense |
| Cave country controls several fronts | Coalition, access, shared intelligence | World-threat level and diplomacy | National defense if cooperation impossible |
| Human rival still at war during cave crisis | Consider ceasefire or reduced offensive | Threat proximity and national survival | Continue rivalry only if cave threat distant or exploitable |

## Cave-country route choice

| Campaign geography | Hierarchy preference | Doctrine preference | Resource strategy |
| --- | --- | --- | --- |
| Compact continent, defensible origin, few fronts | One Maw | Stone Phalanx | Concentrated rich-anchor corridor |
| Wide continent, dispersed fronts, threatened origin | Many Chambers | Burrow War or Scree Tide | Distributed anchors and secondary deep capital |
| Rich resource belt with poor surrounding land | Hoard the Veins | Stone Phalanx | Fortify high-value nodes and avoid barren detours |
| Mountainous or urban terrain | Many Chambers or One Maw | Burrow War | Tunnel links and supply disruption |
| Open plains and many weak enemies | One Maw or Many Chambers | Scree Tide | Rapid capacity activation and pursuit |
| Strong fortified industrial enemies | One Maw | Stone Phalanx | Break one industrial belt and convert factories |
| Enemy has very high hard attack | Many Chambers or Hoard the Veins | Burrow War | Disperse, infiltrate, protect anchors, study weapons |
| Origin nearly lost | Many Chambers if available | Burrow War | Designate secondary deep capital and recapture |

## Cave-country target scoring

Cave AI should score enemy states through a weighted model.

Strong positive factors:

- total strategic resources
- capacity value after floor and cap
- several resource types
- adjacent to an active anchor
- supply hub or rail junction
- enemy capital or industrial center that blocks access
- low defender piercing
- state required for continent completion

Negative factors:

- no resources and no strategic route value
- impassable or invalid terrain
- strong concentrated hard attack
- poor supply with no future anchor
- isolated pocket that would split the army
- naval-only access before world end
- state already targeted by a stronger active offensive

The AI should not ignore a low-resource corridor when it is the only route to a rich region. Path value and destination value both matter.

## Cave-country front behavior

| State | AI behavior |
| --- | --- |
| Under capacity and secure | Hold anchors, wait for queue, attack one rich route |
| At capacity and organized | Concentrated offensive toward next anchor |
| Over capacity after state loss | Recapture anchor, withdraw to supply, consolidate weak broods |
| Enemy piercing low | Use phalanx or broad pressure depending on doctrine |
| Enemy piercing high | Avoid frontal waste, use burrow or multi-front pressure, defend anchors |
| Origin attacked | Highest strategic priority unless world-end distributed route reduced dependence |
| Near continent completion | Concentrate against remaining eligible states, guard completed regions |
| World-end active | Maintain origin continent, coordinate several footholds, prioritize local anchors on each continent |

## Focus AI validity gates

Every focus or decision must weight to zero or hide when required context is invalid.

Required blockers include:

- dead or missing target country
- lost or invalid origin state
- no active resource anchors for anchor upgrades
- no enemy using the studied weapon profile
- doctrine already locked by another route
- hierarchy already locked by another route
- disabled Evolution IV or world-end route
- chaos below terminal requirement for final capstone
- continent condition impossible due to stale state group
- no valid cross-continent rupture candidate
- cave country already defeated
- world end already active from another scenario

## AI balance goals

The owner AI should sometimes create Evolution IV through greed or desperation, but it should not do so in every campaign. The cave AI should be frightening and coherent, but capable opponents with hard attack, resource denial, and coordinated fronts must be able to contain it. Foreign AI should care most when it actually needs the resource or faces the threat. These distributions should be validated across several world states, not tuned from one country only.
