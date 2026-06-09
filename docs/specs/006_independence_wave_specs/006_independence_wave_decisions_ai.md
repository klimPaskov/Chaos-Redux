# Event 6: Independence Wave Decisions, AI, and Dynamic Variables

This file defines decisions and AI for Event 006. It must treat Event 006 as independent from Event 005.

## Release-origin variables

| Variable or flag | Scope | Meaning |
| --- | --- | --- |
| `chaosx_release_origin_independence_wave` | country | country was released by Event 006 |
| `chaosx_independence_wave_package_type` | country | ordinary, game_rule, protectorate, city, railway, historical_return, local_polity, strange |
| `chaosx_independence_wave_candidate_tier` | candidate | baseline, learned, congress, claims, old_local, impossible |
| `chaosx_independence_wave_batch_index` | country | which wave created this country |
| `chaosx_independence_wave_host` | country or event target | host that lost the candidate |
| `chaosx_independence_wave_release_count_target` | global or event | count target for this wave after scoring |
| `chaosx_independence_wave_actual_release_count` | global or event | successful releases after validation |
| `chaosx_independence_wave_protected_host_state` | host or event target | state reserved so the host cannot be deleted |
| `chaosx_independence_wave_host_survival_floor` | host | confirms the host must keep at least one state after this wave |

The release-origin flag prevents tag confusion. A shared tag such as Volga Bulgaria uses Event 006 content only when this flag is set. Soviet republic style tags released by Event 006 also use Event 006 content only. They must not join Event 005 collapse progress, Event 005 republic missions, Soviet Collapse focus loading, Event 005 formable routes, or Event 005 event-log states.

Origin must be checked before any tree, package, formable, GUI, achievement, or startup idea is assigned. If a tag already exists with Event 005 origin, Event 006 should not overwrite it. If a tag exists with Event 006 origin, Event 005 should not claim it through tag name alone.

## Dynamic variables

| Variable | Scope | Meaning | Increases from | Decreases from |
| --- | --- | --- | --- | --- |
| independence_wave_pressure | candidate or host | How close the candidate is to open independence | host weakness, war, foreign attention, earlier waves | negotiation, autonomy, propaganda |
| independence_wave_legitimacy | candidate | How credible the new state looks | petitions, observers, repression by host, elections, historical archive proof | loyalist opposition, failed governance, radical violence |
| independence_wave_radicalization | candidate | How likely non-democratic or extreme routes become | suppression, deaths, high chaos, foreign betrayal | reforms, democratic guarantees, observer-protected elections |
| independence_wave_militia_strength | candidate | Starting military power | factories, depots, manpower, foreign aid, war | host raids, lack of industry, failed recruitment |
| independence_wave_foreign_attention | host or candidate | Whether majors care | reporters, ideology, resources, strategic ports | remote location, low value, major wars elsewhere |
| independence_wave_patron_leverage | candidate | Risk of puppeting or client status | foreign loans, advisers, guarantees, rescue | expose brokers, league charter, domestic legitimacy |
| independence_wave_coalition_cohesion | global or coalition | Cooperation among released states | mutual aid, arbitration, shared enemies | rival claims, ideology conflict, patron competition |
| independence_wave_claim_ambition | candidate | Desire to demand more land | high chaos, nationalist route, border offices, host weakness | arbitration, democratic route, foreign restraint |
| independence_wave_occult_pressure | candidate | Strange route pressure | high chaos, deaths, grave sites, anomalies | strong civic route, low deaths, containment decisions |
| independence_wave_old_state_memory | candidate | Historical-return pressure | old-state region, archive event, high chaos, cultural focus | modern compromise, failed archive proof |
| independence_wave_local_authority_strength | candidate | Strength of chiefs, councils, land congresses, municipal boards, or local institutions | local-polity package, protectorate treaty, land support | internal splits, patron coercion |

## Batch release calculation

The wave should calculate a target count before candidate resolution.

| State | Base target | Modifiers |
| --- | ---: | --- |
| Baseline | 3 to 5 | +1 if host is losing war, +1 if many valid ordinary candidates exist |
| Evo I | 4 to 6 | +1 if previous wave suppression was harsh |
| Evo II | 5 to 7 | +1 if coalition cohesion is high |
| Evo III | 6 to 9 | +1 if major patron conflict exists |
| Evo IV | 8 to 12 | +1 if multiple historical-return or local-polity packages are valid |
| Evo V | 10 to 16 | cap by performance and valid candidate count |

The event should never create invalid countries just to meet the target.


## Host survival validation pass

Before any release effect runs, the event must reserve one host state and verify the whole batch against it.

Validation order:

1. Reserve the capital state if the host owns it.
2. If the host does not own its capital, reserve the strongest remaining owned state.
3. Score every candidate against the reserved state and the host's remaining state count.
4. Reduce candidate territory where possible.
5. Remove candidates that would take the reserved state or consume the host's final state.
6. Recalculate the actual release count after removals.
7. Write the final count to `chaosx_independence_wave_actual_release_count`.

The target count is only a target. Host survival is mandatory. A failed validation should lower the number of releases, not delete the host.

## Candidate decision map

### Compile Ordinary Candidate List

- Available internally during the immediate release resolver.
- Adds existing releasable, dead, or modded tags that pass state checks.
- Baseline and Evo I draw primarily from this list.
- AI has no visible choice here.

### Compile Dormant and Game-Rule Candidate List

- Available from Evo I or Evo II.
- Adds tags that exist in the game through game rules, focuses, decisions, or formables if activation is safe.
- The implementation must verify actual tag IDs from the repository.

### Compile Historical-Return Candidate List

- Available from Evo IV.
- Adds researched candidates such as Assyria, Mesopotamia, Sokoto, Asante, Buganda, Kanem-Bornu, Barotseland, Mapuche Araucania, Aymara, Palmares, and Volga Bulgaria.
- Requires package data and assets before live spawn.

### Compile Strange Candidate List

- Available from Evo V.
- Adds necromantic, anti-mankind, archive-state, and other impossible packages.
- Requires high occult pressure or explicit strange-state conditions.

## Host decision map

### Open Negotiations

- Available to hosts after an instant release wave creates active release dossiers.
- Best when host stability is medium or high and pressure is not near the break point.
- Lowers pressure and radicalization.
- Raises committee legitimacy if talks drag on.
- AI: democratic and stable hosts prefer it. Fascist and collapsing hosts avoid it unless overextended.

### Offer Local Autonomy

- Available after negotiations or as immediate concession.
- Can prevent full independence by creating an autonomy settlement.
- Adds precedent pressure to later waves.
- AI: stable empires use it for low-industry regions. Weak hosts use it when fighting a larger war.

### Arrest Committee Leaders

- Available if host has police capacity or army nearby.
- Can stop low-legitimacy candidates.
- Raises radicalization, foreign attention, and death risk.
- AI: authoritarian hosts use it often. Democratic hosts use it only under high war pressure or low foreign attention.

### Send the Army to the Capital

- Requires available divisions or command power.
- Raises immediate suppression chance.
- Raises foreign attention and future militia strength if it fails.
- AI: used by hosts at war only if the candidate has high industry, ports, or resources.

### Flood the Airwaves

- Uses propaganda to lower pressure.
- Works best against low-legitimacy candidates.
- Fails badly if foreign reporters are present or the host recently committed atrocities.

### Arm Loyalist Councils

- Creates loyalist counter-pressure.
- Can prevent release or create post-release internal conflict.
- High risk in high chaos.

### Invite Foreign Observers

- Lowers violence risk and makes elections credible.
- Makes suppression more expensive.
- Raises foreign attention.

### Ask for Territorial Guarantee

- Host asks a major to guarantee borders.
- Can deter breakaways.
- Increases foreign leverage and may create future patron conflict.

### Trade a Border District

- Transfers a small district, resource state, port, or local autonomy arrangement to avoid full independence.
- Cannot transfer the protected host state or the host's final remaining state.
- Reduces one crisis but raises global precedent.

### Evacuate Archives and Depots

- Reduces the new state's starting legitimacy or equipment if release happens.
- Raises bitterness and claim ambition.

## Breakaway decision map

### Request Recognition

- Core decision for all packages.
- Higher success with legitimacy, observers, civic route, and low radicalization.

### Seize the Depot Inventory

- Grants equipment based on local depots, factories, and host preparation.
- Raises host anger.

### Form Local Defense Brigades

- Creates weak defensive units.
- Scales by militia strength and chaos tier.

### Call the Diaspora Committees

- Adds manpower, advisors, or political power.
- More effective for Assyria, Armenia, Poland-like exiles, and other diaspora-compatible packages.

### Convene the Small States Congress

- Requires earlier breakaways or coalition cohesion.
- Opens aid, guarantees, volunteers, and league preparation.

### Demand the Border Parish

- Opens a limited border claim against an unowned core. Adjacent non-core border claims require high chaos and league backing.
- Civic route prefers arbitration. Patron and anti-puppet routes prefer negotiated transfer. Nationalist and officer routes prefer ultimatum.
- Claimed border states remain contested targets so the next Border Commission action can transfer, freeze, or escalate them instead of trapping the claim as dead state. Non-core overreach opens host warning, negotiation, and reclamation-war responses.

### Accept Foreign Advisers

- Gives equipment, planning, advisors, or recognition.
- Raises patron leverage.

### Expose Foreign Brokers

- Reduces patron leverage.
- Can remove adviser bonuses or anger a major.

### Emergency Elections

- Raises legitimacy for civic routes.
- Can fail under civil conflict or high radicalization.

### Directorate Security Rule

- Stabilizes violent countries.
- Locks or biases toward military, nationalist, or authoritarian route.

### Open the Old Archive

- Historical-return package decision.
- Raises old-state memory and unlocks package overlay if evidence or chaos threshold is enough.

### Convene the Land Congress

- Local-polity package decision.
- Raises local authority strength and legitimacy.
- Can reduce patron leverage if the congress is strong.

### The Unmarked Congress

- Strange high-chaos decision.
- Opens impossible-state route.
- Should trigger warning events.

### Census of the Quiet Dead

- Necromancy package decision.
- Raises occult pressure and unlocks grave-state mechanics.

## Major power decisions

### Recognize the Committee

- Grants legitimacy and foreign attention.
- May anger the host.

### Supply Rifles Through the Port

- Grants equipment and patron leverage.
- Requires port, border access, or smuggling route.

### Offer a Military Mission

- Adds army XP, advisor, doctrine, or planning speed.
- Raises patron leverage sharply.

### Demand Cabinet Seats

- Turns support into dependency.
- Opens patron cabinet route.

### Guarantee the Existing Border

- Supports host against committee claims.
- Can deter weak breakaways.

### Broker an Autonomy Settlement

- Prevents release if pressure is moderate.
- Gives major diplomatic credit and leverage.

### Sabotage Rival Patron

- Intelligence action against another major's influence.
- Raises conflict risk.

## AI weighting by condition

| Condition | Host AI | Breakaway AI | Major AI |
| --- | --- | --- | --- |
| low chaos | negotiate or limited suppression | civic and recognition | observe or ignore |
| host losing war | autonomy, evacuation, guarantee request | armed survival | support if strategic |
| high foreign attention | observers and negotiation | recognition | recognition or pressure |
| high radicalization | suppression if authoritarian, autonomy if democratic | revolutionary or military | sponsor by ideology |
| high claim ambition | border guarantee or army | nationalist and claims | back or block claims |
| high patron leverage | host exploits rival patron fear | anti-patron or dependent route | push cabinet seats |
| Evo IV old-state unlock | host resists old claims | historical-return overlay | sponsor if useful |
| Evo V strange unlock | emergency containment | strange module if package | containment unless also strange |

## Abuse prevention

- Do not let a player farm infinite equipment by triggering repeated releases in the same states.
- Do not allow one host to be shredded every month without cooldowns.
- Do not spawn high-chaos historical packages at low chaos.
- Do not spawn custom tags without assets and localisation.
- Do not let patron support create free puppets without diplomatic cost.
- Do not let small-state league guarantees create impossible defensive webs at low chaos.
- Cap batch size if performance or candidate count is weak.
- Block Event 006 package mechanics for tags released by Event 005.


## Decision category architecture

The event needs several living categories, not one store-like menu.

| Category | Owner | Opens when | Closes when | Main work |
| --- | --- | --- | --- | --- |
| Petitions Against the State | host | release dossiers exist after the instant wave | all aftermath crises settle or host loses crisis control | recognition, suppression, observers, loyalists, foreign guarantee, archive evacuation |
| Committee Survival | new breakaway | country released by the instant wave | recognized, annexed, civil conflict resolved, or package fails | legitimacy, depot control, brigades, elections, diaspora, recognition |
| Patronage and Recognition | majors and regional powers | foreign attention crosses threshold | crisis resolves or relations collapse | recognition, supplies, advisers, cabinet demands, rival sabotage |
| Small States Congress | released Event 006 countries | at least two Event 006 countries survive | league formed, congress collapses, or members become puppets | guarantees, volunteers, arbitration, faction formation |
| Border Commission | host, breakaway, patron | claim ambition or settlement path exists | claim settled, war starts, or commission expires | surveys, plebiscites, arbitration, ultimatums, protected transfers |
| Old Archive and Land Congress | historical-return or local-polity states | package type supports it | modern compromise, escalation, or suppression | old documents, local authority, treaty memory, land defense |
| Sealed Dossier | strange packages and observers | Evo V strange trigger | containment, reveal, or escalation | archive audit, grave census, anti-mankind pressure, quarantine |

Each category must have a clear lifecycle and cleanup. Decisions should not remain visible after the crisis they describe is over.

## Mission and decision split

Use clickable decisions for choices and timed missions for proof of control.

| Content | Use clickable decision | Use timed mission |
| --- | --- | --- |
| Negotiation | start talks, choose settlement terms | maintain talks while stability stays above threshold |
| Suppression | order crackdown or arrest leaders | hold the capital, rail hub, or depot for a duration |
| Observers | invite, deny, or expel observers | keep observer corridor open and unsupplied by hostile troops |
| Loyalists | arm or disarm local loyalists | prevent loyalists from losing the district or mutinying |
| Recognition | request or grant recognition | survive a recognition probation period without becoming puppet |
| Depot seizure | seize or surrender depot stockpiles | hold depot state and keep supply route open |
| Congress | call delegates or refuse attendance | keep enough members independent until charter vote |
| Border revision | file claim, request arbitration, negotiate transfer, freeze observers, or issue ultimatum | hold claimed district or complete arbitration timer |
| Strange containment | open audit or seal bureau | keep occult pressure below threshold until review ends |

Goal-style missions should auto-complete when the player has already done the work. Do not require a second paid click for holding a state or placing divisions.

## Dynamic cost model

Costs should scale with country size, crisis intensity, and action type.

| Cost input | Where used | Direction |
| --- | --- | --- |
| host_state_count | host decisions | larger host pays more to police or negotiate across distance |
| host_stability | suppression, delay, loyalists | low stability makes actions riskier and less reliable |
| host_war_support | military crackdown | high war support makes army use cheaper but raises radicalization |
| host_equipment_stockpile | loyalists, depot raids | weak stockpile limits crackdown and armed supporters |
| candidate_legitimacy | recognition, observers, elections | high legitimacy lowers recognition cost and raises host suppression cost |
| candidate_radicalization | arrests, security rule, strange pressure | high radicalization makes compromise harder |
| foreign_attention | recognition, advisers, observers | high attention lowers diplomatic cost but raises patron leverage |
| patron_leverage | aid and cabinet demands | high leverage makes aid stronger but puppet risk worse |
| coalition_cohesion | congress decisions | high cohesion lowers guarantee and volunteer costs |
| chaos_tier | all crisis actions | higher chaos shortens timers, raises stakes, increases release count |
| active_breakaway_wars | major aid and congress | too many wars raise cost and reduce AI appetite |

Fixed values can be tuning anchors, but every visible action should clearly belong to one of these scaling bands.

## Host decision expansion

| Decision | Type | Cost family | Short-term effect | Long-term effect | AI preference | Failure or risk |
| --- | --- | --- | --- | --- | --- | --- |
| Open Negotiations | clickable | political power, civilian factory burden, legitimacy exposure | lowers pressure and radicalization | may create autonomy settlement or peaceful release | democratic, stable, overstretched hosts | talks raise committee legitimacy if prolonged |
| Offer Local Autonomy | clickable | stability, political power, autonomy spirit | lowers pressure strongly | creates future autonomy precedent | democratic or low-war hosts | later waves demand same deal |
| Delay and Investigate | clickable plus timer | political power, intelligence exposure | buys time | can reveal patron brokers or old archives | cautious AI and low-threat hosts | delay can backfire if pressure rises |
| Arrest Committee Leaders | clickable | command power, equipment, stability | lowers pressure if legitimacy is low | raises radicalization and martyr memory | authoritarian stable hosts | high foreign attention punishes it |
| Send the Army to the Capital | timed mission | command power, equipment, tied divisions, supply strain | blocks capital loss and depot seizure | can suppress or trigger violent release | wartime or high-war-support hosts | failure gives candidate stronger army |
| Guard the Final State | auto mission | tied divisions and supply | protects host survival state | ensures host remains alive | all AI hosts when near one-state rump | not optional for validation |
| Flood the Airwaves | clickable | political power, consumer goods, stability risk | lowers legitimacy | creates propaganda memory | fascist or authoritarian hosts | can expose lies and raise foreign attention |
| Arm Loyalist Councils | clickable plus mission | infantry equipment, command power, local support | creates loyalist obstacle | can cause civil split | low-stability or nationalist hosts | loyalists may become independent actors |
| Invite Foreign Observers | clickable plus mission | political power, diplomacy, rail or port access | lowers suppression cost later and raises legitimacy | peaceful outcomes and recognition improve | democracies and weak hosts | observers make violent suppression costly |
| Ask for Territorial Guarantee | clickable | political power, relations, concessions | major warns candidates | patron can demand future access | weak hosts near major allies | grants leverage to guarantor |
| Trade a Border District | clickable | one state or claim concession, stability | resolves one candidate or shrinks release | host survival improves, future claims possible | pragmatic weak hosts | nationalists lose support |
| Evacuate Archives and Depots | clickable and timed | trains, trucks, infantry equipment, fuel | denies candidate old-state and militia strength | raises host survival but hurts economy | hosts facing high-chaos packages | failure boosts old-state memory |
| Release Under Conditions | clickable | legitimacy, autonomy loss, war support | peaceful release with constraints | lower radicalization, possible future guarantee | democratic or exhausted hosts | new state may later reject conditions |
| Declare Emergency Unity | clickable | stability, war support, political power | blocks several decisions and raises crackdown strength | possible military government route for host | authoritarian and war hosts | high radicalization and future unrest |

## Breakaway decision expansion

| Decision | Type | Cost family | Short-term effect | Long-term effect | AI preference | Failure or risk |
| --- | --- | --- | --- | --- | --- | --- |
| Request Recognition | clickable | political power, legitimacy, foreign attention | asks majors and neighbors for recognition | unlocks civic route and guarantees | civic and moderate AI | patron leverage if one sponsor dominates |
| Guard the Provisional Capital | timed mission | tied divisions, supply, command | protects capital and legitimacy | unlocks recognized government or emergency rule | all new states | failure unlocks crisis branch |
| Seize the Depot Inventory | clickable plus mission | local support, risk of host raid | grants equipment and militia strength | raises host anger and radicalization | military and revolutionary AI | failed seizure weakens army |
| Form Local Defense Brigades | clickable | manpower, infantry equipment, support equipment | spawns defensive units | unlocks doctrine and defensive belt | all AI under threat | overuse hurts economy |
| Call the Diaspora Committees | clickable | political power, convoys if overseas, foreign attention | raises legitimacy and manpower | unlocks diaspora advisors or volunteers | historical-return and local-polity AI | may raise patron attention |
| Emergency Elections | timed mission | stability, political power | lowers radicalization | civic route lock and recognition | democratic AI | failure may open officer mandate |
| Directorate Security Rule | clickable | command power, stability, legitimacy | suppresses loyalists and radical opposition | military or nationalist route lock | authoritarian AI | lowers recognition and triggers crisis |
| Convene the Small States Congress | clickable | political power, relations, coalition cohesion | invites Event 006 countries | league path and guarantees | independent small states | patron conflict can split congress |
| Send Volunteers to the Next Wave | clickable | manpower, equipment, command power | helps active candidates | raises coalition cohesion | league and revolutionary AI | host and majors may retaliate |
| Demand the Border Parish | clickable | claim ambition, political power, legitimacy risk | opens commission | later claim or protected transfer | national directorate AI | failed demand lowers recognition |
| File for Arbitration | timed mission | political power, foreign attention | lowers war risk | possible peaceful state transfer | civic and league AI | slow and uncertain |
| Accept Foreign Advisers | clickable | autonomy risk, patron leverage | stronger army and industry | patron route or puppet risk | weak military AI | locks out some achievements |
| Expose Foreign Brokers | clickable | intelligence exposure, political power | lowers patron leverage | anti-patron recovery | high-legitimacy AI | failure worsens leverage |
| Open the Old Archive | clickable | stability, political power, archive risk | raises old-state memory and claims | historical-return overlay | old-name AI | may trigger extremist branch |
| Modernize the Old Name | timed mission | legitimacy, stability, old-state memory | channels old name into civic state | modern compromise achievement path | moderate historical AI | revanchists may revolt |
| Convene the Land Congress | clickable and timed | local support, stability, manpower | raises local-polity legitimacy | land autonomy and community defense | local-polity AI | host loyalists can disrupt it |
| The Unmarked Congress | hidden clickable | occult pressure, stability | opens strange module | strange-state route | strange AI only | alarms neighbors |
| Census of the Quiet Dead | hidden timed mission | occult pressure, manpower anomaly | strange manpower and legitimacy changes | necromancy path | necromantic AI | containment intervention |

## Major power decision expansion

| Decision | Type | Cost family | Effect | Leverage consequence | AI logic |
| --- | --- | --- | --- | --- | --- |
| Recognize the Committee | clickable | political power, relations with host | raises legitimacy and foreign attention | small leverage increase | democracies if candidate civic, rivals if host enemy |
| Supply Rifles Through the Port | clickable | infantry equipment, convoys, intelligence exposure | raises militia strength | medium leverage | majors at war with host or seeking influence |
| Offer a Military Mission | clickable | command power, officers, equipment | army XP, templates, defense bonuses | high leverage | fascist, communist, or imperial majors |
| Demand Cabinet Seats | clickable | diplomatic pressure | turns aid into patron cabinet route | very high leverage | aggressive patrons and opportunists |
| Guarantee the Existing Border | clickable | political power, relations | protects host or new state from claims | leverage over protected side | status quo powers |
| Broker an Autonomy Settlement | clickable | political power, relations, foreign attention | prevents release or shrinks it | small leverage and prestige | democracies and regional mediators |
| Sabotage Rival Patron | clickable | intelligence exposure, spies if system exists | reduces rival leverage | risk of scandal | rivals of active patron |
| Recognize the League | clickable | political power and relations | raises coalition cohesion | moderate leverage with league | democracies, isolated small powers |
| Arm the Loyalists | clickable | equipment and exposure | helps host loyalists | leverage with host | authoritarian patrons or host allies |
| Threaten Non-Recognition | clickable | diplomatic cost | pressures new state to accept terms | raises leverage and radicalization | imperial or patron AI |

## Timed mission examples

| Mission | Owner | Duration direction | Auto-complete condition | Failure effect |
| --- | --- | --- | --- | --- |
| Keep the Observer Road Open | host or breakaway | shorter at high chaos | controlled route from border or port to candidate capital | observer scandal, radicalization rises |
| Hold the Provisional Capital | breakaway | 30 to 90 days by strength | capital state held and supplied | crisis branch or government exile |
| Secure the Depot Belt | breakaway | 45 to 120 days | depot state held and enemy not adjacent if possible | equipment lost, host raid succeeds |
| Guard the Host Capital | host | 45 to 120 days | protected state held and not selected by release | suppression credibility rises |
| Prevent the Loyalist Mutiny | host or breakaway | 30 to 80 days | loyalist variable below threshold | civil split or street fighting |
| Recognition Probation | breakaway | 60 to 180 days | not puppet, not capitulated, legitimacy above threshold | recognition stalls |
| Congress Charter Window | Event 006 members | 90 to 180 days | enough independent members and cohesion | congress collapse or patron takeover |
| Border Arbitration Clock | both sides | 60 to 150 days | pressure and claim ambition within range | ultimatum or border war |
| Archive Audit | historical-return | 60 to 180 days | old-state memory balanced with civic legitimacy | mythic escalation or archive scandal |
| Containment Review | strange package | 45 to 120 days | occult pressure reduced | strange reveal escalates |

## AI strategy matrix

| Actor state | AI priority | Avoids | Notes |
| --- | --- | --- | --- |
| Stable democratic host | negotiation and observers | arrests unless pressure extreme | wants legitimacy and low war risk |
| Unstable democratic host | autonomy and peaceful release | long delays | fears collapse more than territory loss |
| Fascist host | arrests, loyalists, propaganda | observers | may trade territory if fighting a larger war |
| Communist host | propaganda and revolutionary co-option | patron-backed releases | may support foreign committees elsewhere |
| Non-aligned empire | delay, foreign guarantee, army | full acceptance | fears precedent and protectorate loss |
| Colonial host | suppress if strong, autonomy if weak | observers if atrocities likely | high risk of repeated waves |
| Host at war | army, archives, trade district if overstretched | long negotiations | tries to protect capital and supply |
| Ordinary civic breakaway | recognition and elections | offensive claims | wants survival and legitimacy |
| Emergency breakaway | depot, brigades, capital defense | early elections if unsafe | stabilizes before diplomacy |
| Historical-return breakaway | old archive, modern compromise, claims if strong | patron cabinet if legitimacy high | chooses revanchism only with high claim ambition |
| Local-polity breakaway | land congress and community defense | foreign cabinet seats | focuses on autonomy and local claims |
| Protectorate | advisers and guarantee | anti-patron unless leverage too high | may become puppet if pressured |
| League member | congress, guarantees, volunteers | major-led faction | protects other Event 006 countries |
| Strange state | hidden doctrine and survival | normal recognition unless containment path | restricted to high chaos |

## AI numerical guidance

Implementation can tune exact values, but the direction should match these weights.

| Condition | Weight effect |
| --- | --- |
| host stability below 35 percent | host suppression risk rises, negotiation success falls |
| host at war with major | candidate pressure rises, host army decisions cost more |
| candidate legitimacy above radicalization | civic route and recognition decisions favored |
| radicalization above legitimacy | military, revolutionary, nationalist, or strange route favored |
| patron leverage above safe threshold | anti-patron decisions become attractive if legitimacy is high |
| foreign attention above threshold | majors consider recognition and aid |
| coalition cohesion above threshold | congress decisions and league focuses favored |
| active wars too high | release count throttles and majors avoid new commitments |
| candidate would delete host | candidate invalid until shrunk |
| package type historical_return | old archive and modern compromise decisions become visible |
| package type strange | sealed dossier decisions visible only after reveal conditions |

## Cleanup and exploit prevention

| Problem | Required cleanup |
| --- | --- |
| Candidate skipped by hidden resolver | remove pending score flags, pressure targets, temporary decisions, and event targets |
| Host no longer exists for reasons outside Event 006 | cancel active host decisions and mark crisis unresolved by external collapse |
| New country is annexed | close its categories, keep global memory, preserve achievement disqualifiers |
| Patron target becomes puppet of someone else | close rival patron decisions and update leverage |
| League member joins major faction | remove league founding eligibility and adjust cohesion |
| Border war starts | close arbitration decisions and open war cleanup |
| Strange package contained | hide strange decisions and convert to civic or military recovery route |
| Debug or test firing used | set achievement disqualifier |
| Event 005 origin detected | block Event 006 decisions and focus overlay |

## Decision localisation style

Decision text should explain the action in plain terms.

Good pattern:

- title names the action, such as `Invite Foreign Observers`
- description states who is being moved, armed, recognized, or pressured
- tooltip shows dynamic pressure changes, cost family, and long-term risk
- hidden variables are summarized as player-facing ideas like legitimacy, leverage, or radicalization

Avoid vague tooltips such as `Gain political power` or `This may have consequences`. Consequences should be concrete whenever possible.

## Scripted GUI and mechanic window plan

Event 006 should use decision categories as the entry point for its mechanic windows. A normal decision category can remain the base layer, but important values should be visible through scripted GUI when the system becomes too dense for tooltips.

Core windows:

| Window | Opens from | Main values | Main actions | AI equivalent |
| --- | --- | --- | --- | --- |
| Independence Dossier Board | host crisis category | pressure, legitimacy, radicalization, foreign attention, protected state | negotiate, suppress, delay, observer, loyalists, guarantees | weighted host decisions and event options |
| New States Congress | released-state coalition category | cohesion, member confidence, patron pressure, shared reserves | charter vote, mutual guarantees, shared arms, arbitration | shared decisions and scripted AI pulses |
| Patron Ledger | breakaway foreign influence category | sponsor influence by type, dependency, broker exposure | accept aid, balance patrons, expose broker, reject clauses | AI sponsor and target decisions |
| Formation Ledger | package formation category | state control, integration, recognition, reveal state | reveal requirements, form state, integrate districts | formation decisions with AI guards |

Each GUI button must have:

- visible cost
- missing-requirement tooltip
- scripted trigger
- scripted effect
- dynamic localisation
- AI equivalent
- cleanup path
- event log hook when the action is important
- achievement hook when relevant

Do not use a scripted GUI button to bypass normal decision balance. The GUI button should call the same helper family that decisions, focuses, and AI actions can call.

## Formation decisions

Formation decisions should be handled inside Event 006 decision categories. A formable can be public, route-locked, hidden, high-chaos, patron-backed, or package-specific.

Every formation decision needs:

- visible or hidden reveal condition
- named required state group
- owned and controlled checks
- subject or ally rules if the formation can include members
- release origin or formation origin checks
- route disqualifiers
- costs beyond political power where appropriate
- post-formation integration missions
- identity change logic
- event log entry
- AI safety checks
- cleanup of obsolete pre-formation decisions

Formation should usually grant claims and staged integration rather than instant full cores on every contested state. Large formables should require follow-up projects such as holding capitals, securing rail links, negotiating autonomy, spending equipment, reducing resistance, or keeping legitimacy above a threshold.

## Suggested Event 006 formable decision families

| Decision family | Eligible packages | Proof required | Risk |
| --- | --- | --- | --- |
| Proclaim a Regional Congress | coalition and ordinary breakaways | members, cohesion, recognition, non-puppet status | patron backlash and member refusal |
| Convene the Old Name Assembly | historical-return packages | core region, archive proof, old-state memory, legitimacy | rival claimants and host anger |
| Ratify Local Land Authority | local-polity packages | local support, named land group, anti-patron or civic route | foreign refusal and border crisis |
| Accept the Protected Mandate | protectorate packages | sponsor guarantee, border control, dependency acceptance | puppet pressure and anti-patron resistance |
| Seal the Impossible Registry | strange packages | hidden route, high chaos, occult or anti-mankind pressure | world threat and diplomatic rupture |

## Dynamic cost and tooltip requirements

Formation and GUI actions should use varied costs:

- political power only for paperwork, congress votes, recognition, or lawmaking
- command power for military orders and crisis command
- army XP for officer integration and militia regularization
- equipment for mobilization, guard forces, and post-formation administration
- trains and fuel for rail and corridor projects
- convoys for overseas aid or port-backed protectorates
- stability, war support, legitimacy, or local support for risky political action
- faction cohesion for League votes
- patron leverage or foreign influence debt for sponsor actions

Dynamic localisation should show named state groups and current requirements. The player should see a clear summary, not raw trigger logic.

## Active subagent patch surfaces

During implementation, `chaosx_decision_mission_auditor` may directly patch local decision issues such as costs, tooltips, GUI button text, cleanup, cooldowns, visibility, AI checks, and existing formation requirements. It must write a handoff under:

```text
docs/plans/006_independence_wave_plans/subagent_handoffs/
```

If it finds a need for a new decision system, formable suite, or GUI window, it should write a plan handoff and stop.
