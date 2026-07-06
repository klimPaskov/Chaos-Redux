# 006 Independence Wave Spec Part 3: Decisions, Missions, and Scripted GUI

## Context bridge

Independence Wave is Event 6, a Minor Repeatable event in the Liberations cluster. The event instantly releases multiple countries in wave counts of 3, 4, 5, 7, and 10, while preserving the former host with at least one state and preferably the capital. Each released country receives Event 6 origin content even when the same tag can also appear through another event such as Soviet Collapse. The overview defines the release system and the mechanics file defines the living values. This file turns those values into decision categories, timed objectives, target rules, visible management surfaces, and cleanup rules.

All category, decision, mission, and GUI names in this file are working labels. They are not final localisation. Implementation should write final player-facing text from the direction given here.

## Architecture goals

The decision and mission layer should make every Event 6 country feel newly independent, exposed, and active. The player should not only watch values drift. They should decide where the provisional government spends legitimacy, how much foreign help it accepts, whether it risks border pressure, how it handles the former host, and whether it joins a cooperative league or a coercive bloc.

The architecture has five goals.

1. Turn the mechanics layer values into visible levers that the player and AI can use.
2. Keep categories curated so a wave with many countries does not create a debug-like decision wall.
3. Make missions map-based wherever possible, using capitals, ports, rail hubs, supply links, border states, disputed states, and regional groups.
4. Give former hosts, sponsors, leagues, and aggressive blocs their own active responses.
5. Make the triggerable scenario playable even when every possible country is released.

The system should use dynamic costs, durations, caps, and target lists. Political power is allowed when the action is political, but most important actions should also consume equipment, manpower, XP, convoys, trains, factories, stability, war support, local control, legitimacy, foreign support, coalition trust, or time.

## Decision surface map

| Surface | Who sees it | Purpose | Clutter rule |
| --- | --- | --- | --- |
| Working label: provisional statecraft | Event 6 released countries | Core survival, legitimacy, instability, government building | Always visible for Event 6 origin countries until the country is fully stabilized or absorbed. Shows only current phase actions. |
| Working label: local control | Event 6 released countries | State integration, rail hubs, ports, district guard, border administration | Shows only eligible state groups and active missions, with a hard cap. |
| Working label: recognition and patrons | Event 6 released countries and eligible sponsors | Recognition, aid, patron influence, anti-puppet clauses, sponsor rivalry | Separate sponsor targets into a short scored list. Hide dead, hostile, unreachable, and saturated sponsors. |
| Working label: host dispute | Event 6 released countries and former hosts | Border heat, settlement, reclamation, former host anger | Shows only countries with live Event 6 origin links to the host. |
| Working label: Independence League | League members and eligible releases | League cohesion, membership, common defense, charter goals, arbitration | Shows once a league project exists. Separate member actions from leader actions. |
| Working label: coercive compact | Aggressive bloc members | Aggressive Bloc Pressure, demands, ultimatums, synchronized border activity | Hidden unless the route exists. Uses strict target caps and cooldowns. |
| Working label: regional formation | Event 6 countries with formable potential | Preparation, state integration, votes, claims, post-formation cleanup | Hidden until a country has the right origin, region, and reveal condition. |
| Working label: host recovery | Former hosts | Remaining administration, loyal railways, capital preservation, settlement or response | Shows only to hosts that lost states through Event 6. |
| Working label: global release scenario | Scenario controller, released countries, former hosts | Release-all setup and variant objectives | Only exists in manual scenario variants. It must not appear in normal random waves. |

## Lifecycle phases

Decision visibility should be driven by a phase variable or equivalent scripted state. The phase is not a public story stage. It is a clutter-control and AI-routing tool.

| Phase | Typical time | Core problem | Decisions visible |
| --- | --- | --- | --- |
| Shock | First 90 to 180 days after release | Survive the first administrative collapse | Emergency government, capital security, first militia, first recognition probe, first host contact. |
| Consolidation | After first survival missions or after 90 days | Turn sudden independence into a working state | Registry, courts, district control, aid corridor, basic army, rail and port control, first settlement. |
| Bargaining | After recognition, host anger, or border heat becomes meaningful | Choose sponsor, league, neutrality, settlement, or confrontation | Treaty missions, patron balancing, league charter, border commission, host negotiations. |
| Ambition | After strong legitimacy or high chaos pressure | Build a larger project | Formable preparation, league leadership, aggressive bloc pressure, expansion claims, protectorate logic. |
| Aftermath | After war, settlement, league victory, bloc failure, or formation | Clean the system and prevent stale content | Integration, disarm militias, treaty enforcement, league reform, sponsor exit, host final settlement. |

Phase movement should be reversible only when the country suffers a major shock, such as capital loss, puppet collapse, severe host war, league expulsion, or patron takeover. Most normal progress should move forward.

## Active mission capacity

The system can create many potential missions. It must cap active missions at several levels.

| Owner | Default active mission cap | High chaos adjustment | Notes |
| --- | --- | --- | --- |
| Event 6 released country | 3 | 4 at the highest chaos evolutions | One survival mission, one local control mission, and one diplomatic or border mission should usually be the visible mix. |
| Former host | 3 | 4 if the host lost 5 or more states | Host recovery should not flood the host with one mission per release. |
| Sponsor | 2 per target, 5 total | No automatic increase | Sponsor actions should be strategic, not spam. |
| League | 3 league-wide, 1 per member | 4 league-wide if under war pressure | League missions should rotate by common goal. |
| Aggressive bloc | 2 pressure missions, 1 war-preparation mission | 3 pressure missions at high chaos | Pressure should be dangerous, not a wall of buttons. |
| Release-all scenario controller | 5 global objectives | 7 for total war variants | Scenario mode can be broader because it is deliberately extreme. |

If a cap is full, new lower-priority missions should queue silently or wait for the next scoring pulse. Do not show blocked duplicates. The player should see a clear category header that tells them why no more missions can start.

## Target selection model

### Country target validity

Any country selected by an Event 6 decision must pass a target validity rule.

| Target type | Required validity |
| --- | --- |
| Released country | Exists, has Event 6 origin memory, owns or controls at least one state, is not only a government in exile, is not fully annexed, and is not using Soviet Collapse origin for the current content. |
| Former host | Exists or has a valid successor host record, still owns at least one state, is linked to the released country by Event 6 host memory, and has not already closed the dispute through final settlement. |
| Sponsor | Exists, has enough industry or regional relevance to sponsor, is not the current target's enemy unless the decision is covert or hostile, has a valid route to send support when logistics matter, and is not blocked by ideology or route. |
| League member | Exists, has Event 6 origin or an approved associate status, is not at war with the league leader unless the war itself is the league crisis, and is not under puppet pressure above the route limit. |
| Aggressive bloc member | Exists, has Event 6 origin or high-chaos invitation status, accepts the coercive route, has no final settlement that forbids coercive claims, and has pressure above the minimum. |
| Formable rival | Exists, has a live overlapping claim or state requirement, and has not accepted a final arbitration or integration settlement. |

### State target validity

State decisions should prefer named state groups, but implementation can build those groups through state flags, scripted triggers, or arrays.

| State target | Required validity |
| --- | --- |
| Capital state | Controlled by the actor, connected to supply or capable of reconnection, not already under a duplicate capital security mission. |
| Claimed state | Claimed or regionally eligible by Event 6 origin, not locked by another event origin, not already integrated by a different Event 6 country, not the former host's last state. |
| Disputed border state | Adjacent to actor or linked by release package, connected to a host dispute record, not already under final treaty. |
| Port state | Has a port or is the selected aid corridor coast, can be convoy linked, not blockaded beyond action limit. |
| Rail hub or supply state | Contains rail, supply hub, major VP, or state flag marking it as a logistics anchor. |
| League common defense state | Belongs to a member, borders a hostile former host or bloc target, or contains the shared defense anchor. |
| Scenario state | Any release-eligible state after release-all generation, subject to host survival and final cleanup rules. |

### Priority scoring

When several targets are valid, the category should score and show the top few. Use a dynamic score rather than fixed lists.

| Factor | Raises priority for released country actions | Raises priority for host actions |
| --- | --- | --- |
| Capital threatened | Emergency government, capital guard, evacuation preparation | Host capital defense, loyal corridor, central command. |
| Low legitimacy | Constituent assembly, recognition probe, anti-puppet clauses | Propaganda response, settlement pressure, negotiation. |
| High instability | Security mission, district registry, militia integration | Reclamation preparation, border pacification, loyalist rescue. |
| High border heat | Commission, de-escalation, defensive line | Ultimatum preparation, border guard, counter-claim. |
| Low local control | Registry, courts, rail police, local guard | Influence local elites, sabotage provisional offices. |
| High patron influence | Anti-puppet reform, diversify sponsors | Expose foreign hand, counter-sponsor diplomacy. |
| High league cohesion | League charter, shared defense, arbitration | Split the league, negotiate member by member. |
| High aggressive pressure | Ultimatum, synchronized claims, war preparation | Preemptive defense, call allies, settlement under pressure. |

## Dynamic cost model

Decision costs should be generated from base bands and adjusted by country size, package tier, phase, chaos, and current values. Exact numbers belong in script constants or a tuning file.

| Cost family | Used for | Scaling factors | Notes |
| --- | --- | --- | --- |
| Legitimacy cost | Emergency decrees, anti-puppet reforms, centralization, risky border moves | Lower cost at high legitimacy, higher cost when unstable | Spending legitimacy should be visible as political risk. |
| Local Control cost | Integration, requisitions, district guard, rail policing | Costs more when local control is low or state is contested | Avoid letting a player integrate states they do not actually control. |
| Foreign Support cost | Aid spending, foreign advisor missions, emergency equipment | Costs support stock and raises patron influence | Foreign Support is useful, but never free. |
| Patron Influence cost | Sponsor demands, patron-led actions, puppet pressure | Cost can be negative in the sense that sponsor pressure rises | Use as tradeoff, not as a resource the player wants to spend. |
| Coalition Trust cost | League votes, shared reserves, arbitration enforcement | Higher cost for aggressive or selfish actions | Prevent one member from draining the league. |
| Equipment cost | Militias, guards, border missions, volunteer transfers | Scale by divisions, state population, and package tier | Use infantry equipment, support equipment, trucks, artillery, trains, and convoys. |
| Manpower cost | Militia, administration, garrison, league reserve | Scale by state count and local control | Use sparingly for tiny released countries. |
| XP cost | Army reform, officer missions, doctrine transfer | Scale by route and support channel | XP costs should not block survival basics. |
| Stability and war support cost | Crackdowns, concessions, aggressive moves, unpopular settlements | Scale by legitimacy and ideology route | Costs should matter, but not trap AI into collapse. |
| Factory burden | Aid corridors, reconstruction, rail, ports, fort lines | Scale by industry and target state | Use timed idea or consumer goods burden where appropriate. |
| Time cost | Missions, conferences, integration, charter votes | Scale by chaos, contested status, local control, war | Use varied durations, not one timer. |

## Duration bands

| Band | Typical duration | Used for |
| --- | --- | --- |
| Emergency | 45 to 75 days | Only immediate survival actions under direct threat. Rare for normal missions. |
| Short | 90 to 120 days | First registry, district guard, first recognition probe, basic rail security. |
| Medium | 135 to 180 days | Border commissions, treaty work, aid corridors, integration steps. |
| Long | 210 to 300 days | Formable preparation, league charter goals, major reconstruction, host recovery. |
| Strategic | 365 days or more | Full regional integration, treaty enforcement, scenario-wide objectives. |

Durations should shorten with high local control, high legitimacy, strong foreign support, and relevant focus unlocks. Durations should lengthen with high instability, war, low supply, heavy host anger, rival sponsors, and state contest.

## Outcome structure

Every important decision or mission should have success, partial success, failure, and cleanup handling.

| Outcome | Meaning | Typical result |
| --- | --- | --- |
| Success | The action reaches its intended state | Value gain, state progress, new action unlock, route progress, or idea lifecycle upgrade. |
| Partial success | The action works but creates a tradeoff | Main value gain plus another value loss, sponsor influence rise, host anger rise, or local control damage. |
| Failure | The action misses its objective or is interrupted | Value loss, instability rise, border heat rise, mission cooldown, hostile event, or harder follow-up. |
| Cancellation | Target dies, route closes, war ends, state changes owner, or category closes | Refund only safe partial costs, clear flags, remove active mission, update target lists. |
| Obsolescence | Later phase or final settlement makes the action irrelevant | Hide decision, complete or fail mission according to final state, clear stale target flags. |

Partial success should be common in Event 6. A small state might secure recognition while accepting too much patron influence. A host might calm a border while hardening local anger. A league might win arbitration while losing cohesion.

## Released country category: provisional statecraft

This is the first category every Event 6 country receives. It handles legitimacy, instability, basic institutions, and survival.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show legitimacy band, instability band, current phase, and strongest current crisis. |
| Primary value tooltip | Show current legitimacy, recognition, instability, and local control average. |
| Warnings | Capital threatened, no army, high patron influence, low local control, host ultimatum risk. |
| Available actions | 3 to 6 actions based on phase and route. Hide actions solved by focus progress. |
| Active missions | At most one emergency mission and one institution mission from this category. |

### Decision family: emergency government

| Field | Direction |
| --- | --- |
| Who sees it | Event 6 released country in Shock or any country whose legitimacy has collapsed. |
| Target | Own capital or provisional capital state. |
| Requirements | Control capital, not under final occupation settlement, not already centralized through focus. |
| Costs | Political capacity, stability risk, legitimacy risk if repeated, small support equipment or infantry equipment if martial administration is chosen. |
| Duration | Clickable decision with a short cooldown, or a 90 day mission if capital security must be proven. |
| Success | Lower instability, raise legitimacy slightly, unlock registry actions. |
| Partial success | Lower instability but raise patron influence or former host anger if foreign advisers or loyalist officers are used. |
| Failure | If capital is lost or supply is cut, instability rises and a fallback capital mission opens. |
| AI | Use early unless stability is critically low and there is no capital threat. |
| Cleanup | Remove when a focus or later phase creates stable government institutions. |

Variants should include civilian committee, military emergency staff, coalition cabinet, and foreign-backed provisional office. These are route directions, not final text. The variant changes value tradeoffs and later focus availability.

### Decision family: provisional assembly

| Field | Direction |
| --- | --- |
| Who sees it | Released countries with legitimacy below the settled band or a democratic, coalition, or neutral route. |
| Target | Country scope. |
| Requirements | No active emergency coup, not a puppet, instability below the breakdown band or enough local control to risk assembly. |
| Costs | Political power, stability, time, local control in capital, and possible sponsor influence if foreign observers are invited. |
| Duration | 120 to 180 days mission. |
| Success | Strong legitimacy gain, recognition gain if observers are present, unlock constitutional focus or equivalent branch. |
| Partial success | Legitimacy gain with coalition trust loss or sponsor rivalry increase. |
| Failure | Instability rises, route may open military caretaker or patron-backed order actions. |
| AI | Democratic and league-minded AI prioritizes it. Aggressive AI uses it only if legitimacy is weak. |
| Cleanup | Clear assembly flags after route lock or government formation. |

### Decision family: emergency decree

| Field | Direction |
| --- | --- |
| Who sees it | Released countries with high instability, low local control, hostile host, or aggressive route. |
| Target | Country scope or selected state group. |
| Requirements | Legitimacy above a minimum unless the route accepts authoritarian risk. |
| Costs | Legitimacy, stability, war support, command power, support equipment. |
| Duration | Instant decision with cooldown, or 60 to 90 day local mission for harsh state actions. |
| Success | Reduces instability or improves local control in one target. |
| Partial success | Gains control while raising border heat, host anger, or patron influence. |
| Failure | Local control falls and militia fragmentation risk rises. |
| AI | Military and survival AI uses when breakdown is near. Coalition AI avoids unless capital is threatened. |
| Cleanup | Route locks should remove incompatible decree variants. |

### Mission family: hold the provisional capital

| Field | Direction |
| --- | --- |
| Trigger | Capital threatened, low legitimacy, host anger above grievance, or first 180 days after release. |
| Objective | Control capital, keep it connected to supply, and maintain a minimum number of supplied divisions there or adjacent. |
| Duration | 120 days at baseline, shorter if under direct war threat, longer for large partition packages. |
| Success | Legitimacy gain, instability loss, local control gain in capital state, unlock capital institution decisions. |
| Partial success | Capital held without enough supply or troops, lower reward and add a logistics follow-up mission. |
| Failure | Instability rises, recognition progress pauses, host confidence or border heat rises. |
| AI | Always prioritize if capital is threatened. Spawn or move units if possible. |
| Cleanup | Ends if capital is moved by valid focus, country annexed, or final settlement changes capital. |

### Mission family: first census and registry

| Field | Direction |
| --- | --- |
| Trigger | Shock phase completed or local control below secure band. |
| Objective | Hold selected core states and keep instability below threshold while spending administrative capacity. |
| Duration | 90 to 150 days based on state count. |
| Success | Local control gain, legitimacy gain, enables integration or taxation decisions. |
| Partial success | Gain local control in capital only, instability rises elsewhere. |
| Failure | Local control falls in target state group and militia actions become more expensive. |
| AI | Prefer high VP and capital states first. |
| Cleanup | State flags clear when integrated, lost, or ceded. |

## Released country category: local control and administration

This category handles per-state control, logistics, district guards, ports, railways, and public administration.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show local control average, worst state group, and active integration count. |
| Target list | Top 3 vulnerable owned states or state groups. |
| Mission cap | One integration mission, one logistics mission, one security mission. |
| Cleanup status | Hide completed state groups and show only new problems. |

### Decision family: appoint district administration

| Field | Direction |
| --- | --- |
| Who sees it | Released country controlling states with low local control. |
| Target | Owned or controlled state group. |
| Requirements | State is not under final cession, has no active duplicate administration mission, and country has minimum legitimacy. |
| Costs | Political power, support equipment, small manpower, possible stability cost if imposed. |
| Duration | 90 to 135 day mission. |
| Success | Local control increase, instability decrease in target, unlock tax or recruitment action for that state. |
| Partial success | Local control increase with legitimacy loss if local elites are bypassed. |
| Failure | Local control decrease, hostile local council event, or patron-backed local faction growth. |
| AI | Select capital first, then high VP, rail, port, and resource states. |
| Cleanup | Remove target flag if state ownership changes or control reaches secured band. |

### Decision family: district guard battalions

| Field | Direction |
| --- | --- |
| Who sees it | Released countries with low local control or border heat. |
| Target | Owned state group, border state, rail hub, or port. |
| Requirements | Equipment stockpile, manpower, local control above minimum, no repeated free unit flag in same state. |
| Costs | Infantry equipment, support equipment, manpower, army XP or command power for training. |
| Duration | 75 to 120 days if mission-based, instant unit spawn only for emergency packages with strict one-time flags. |
| Success | Raise local control, add limited defensive unit or state modifier, lower instability. |
| Partial success | Add weaker unit and raise instability or patron influence if foreign trainers are used. |
| Failure | Equipment consumed, militia fragmentation risk, possible rogue battalion event. |
| AI | Use for vulnerable border and capital states. Avoid if equipment is critically low. |
| Cleanup | State one-time guard flag prevents repeated unit farming. Remove unit growth path when integrated army focus replaces it. |

### Decision family: secure rail and depot network

| Field | Direction |
| --- | --- |
| Who sees it | Released countries with rail, supply, or logistics targets. |
| Target | Rail hub, supply hub, or corridor state group. |
| Requirements | Control target, not cut off from capital unless the mission is a reconnection mission. |
| Costs | Trains, trucks, support equipment, civilian factory burden, time. |
| Duration | 120 to 180 days. |
| Success | Supply improvement direction, local control gain, border defense readiness, lower mission costs nearby. |
| Partial success | Supply improves but instability rises due to requisitions. |
| Failure | Supply disruption, local control loss, and possible host infiltration target. |
| AI | High priority if supply is poor or a war is active. |
| Cleanup | Stop if state is lost, railway destroyed beyond event scope, or focus upgrades the network. |

### Decision family: open local courts

| Field | Direction |
| --- | --- |
| Who sees it | Released countries in consolidation or bargaining phase. |
| Target | Stable state group or capital. |
| Requirements | Legitimacy above weak band, instability below breakdown, local control at minimum. |
| Costs | Political power, stability, time. |
| Duration | 135 to 180 days. |
| Success | Legitimacy and local control gain, unlock settlement and recognition confidence. |
| Partial success | Local control gain with coalition trust loss if courts are factional. |
| Failure | Legitimacy loss and local control decrease in target. |
| AI | Moderate priority for democratic and neutral AI, lower for high-chaos aggressive AI. |
| Cleanup | Hide when legal-institution focus or formable government replaces it. |

### Mission family: guard the aid corridor

| Field | Direction |
| --- | --- |
| Trigger | Active foreign aid through port, border crossing, or rail line. |
| Objective | Control corridor states and maintain supplied divisions along the corridor. |
| Duration | 120 to 180 days, refreshed only after cooldown. |
| Success | Foreign Support gain, local control gain, sponsor influence depending on sponsor terms. |
| Partial success | Aid arrives but with equipment loss or sponsor influence rise. |
| Failure | Foreign Support loss, sponsor rivalry rise, possible convoy or border incident. |
| AI | Use when aid is important and corridor is practical. |
| Cleanup | Clear when aid route closes, sponsor dies, target state lost, or war blocks route. |

## Released country category: recognition and diplomacy

Recognition should not be a passive meter. This category lets a new country seek external acknowledgement, avoid puppet status, or trade independence for security.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show recognition band, strongest sponsor, patron influence band, and treaty status. |
| Sponsor list | Top 3 eligible sponsors by score, plus league recognition if relevant. |
| Diplomatic warning | Show if patron influence is near dependence or if sponsor rivalry is dangerous. |
| Treaty memory | Show if a final settlement, partial recognition, or anti-puppet clause exists. |

### Decision family: send recognition delegation

| Field | Direction |
| --- | --- |
| Who sees it | Released country that is not fully recognized. |
| Target | Eligible sponsor, neighbor, major, regional power, or league council. |
| Requirements | Legitimacy minimum, no active delegation to same target, target not hostile, reachable diplomacy route. |
| Costs | Political power, civilian factory burden or convoy if distant, legitimacy risk, possible foreign support cost. |
| Duration | 120 to 180 days mission. |
| Success | Recognition gain from target, possible Foreign Support unlock. |
| Partial success | Recognition gain with patron influence or sponsor rivalry increase. |
| Failure | Recognition stagnates, sponsor rivalry rises, host anger may rise if the target publicly sides with the release. |
| AI | Seek nearby and ideology-compatible targets first. Avoid dominance by one sponsor unless survival AI is desperate. |
| Cleanup | Clear delegation target if target dies, relations become hostile, or full recognition reached. |

### Decision family: accept observer mission

| Field | Direction |
| --- | --- |
| Who sees it | Released country with low recognition and medium legitimacy. Sponsors may also trigger an offer. |
| Target | Sponsor or league observer body. |
| Requirements | Not in secret route, not under total patron lock, capital secure enough to host observers. |
| Costs | Local control in capital, political power, possible intelligence exposure, sponsor influence. |
| Duration | 90 to 135 days. |
| Success | Recognition gain, legitimacy gain, future treaty action cheaper. |
| Partial success | Recognition gain but sponsor influence rises and host anger rises. |
| Failure | Legitimacy loss and sponsor rivalry if observers withdraw. |
| AI | League-minded AI accepts balanced observers. Aggressive AI accepts only if recognition is low. |
| Cleanup | Observer flags clear after final report, war with sponsor, or patron crisis. |

### Decision family: negotiate anti-puppet clauses

| Field | Direction |
| --- | --- |
| Who sees it | Released country with patron influence in foothold or higher, or sponsor aid active. |
| Target | Dominant sponsor or treaty partner. |
| Requirements | Recognition or Foreign Support from target, legitimacy above weak band, not already a subject. |
| Costs | Legitimacy, foreign support, sponsor approval, time, possible aid reduction. |
| Duration | 135 to 210 days. |
| Success | Patron influence reduction, unlock balanced sponsorship or independent route. |
| Partial success | Patron influence reduced but Foreign Support drops or sponsor rivalry rises. |
| Failure | Patron influence rises, puppet pressure event, or sponsor demands concessions. |
| AI | Independent and league AI use early. Desperate AI delays if aid is vital. |
| Cleanup | Hide after puppet status, final independence treaty, or sponsor collapse. |

### Decision family: request guarantee or protector clause

| Field | Direction |
| --- | --- |
| Who sees it | Released country facing high former host anger or border heat. |
| Target | Major sponsor, regional power, or league. |
| Requirements | Recognition above observed band, sponsor willing, target not at war with actor, not blocked by neutrality route. |
| Costs | Patron influence, coalition trust if league, foreign support, diplomacy cost, possible host anger. |
| Duration | 120 to 180 days. |
| Success | Defensive guarantee, host reclamation readiness reduced, recognition gain. |
| Partial success | Guarantee-like deterrent without formal guarantee, with higher patron influence. |
| Failure | Host anger rises and sponsor rivalry rises. |
| AI | Use if host threat is high and sponsor dependence risk is acceptable. |
| Cleanup | Clear if sponsor dies, guarantee replaced by faction membership, or settlement closes dispute. |

### Mission family: international conference bid

| Field | Direction |
| --- | --- |
| Trigger | Recognition in observed or de facto band, host dispute unresolved, or league charter active. |
| Objective | Maintain legitimacy, keep capital secure, secure support from at least two external actors or enough league members. |
| Duration | 180 to 300 days. |
| Success | Large recognition gain, settlement willingness increase, league cohesion gain if league-backed. |
| Partial success | Recognition gain with unresolved border heat or patron influence increase. |
| Failure | Recognition loss, sponsor rivalry rise, host anger rise. |
| AI | Use for diplomatic routes and league leaders. Avoid if active war makes success impossible. |
| Cleanup | Cancel if actor capitulates, host dispute ends, or conference target dies. |

## Released country category: army and militia organization

Event 6 countries should not be empty tags. This category builds survival forces while preventing free unit loops.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show current army readiness direction, militia fragmentation warning, and equipment shortage. |
| Main actions | Raise guards, integrate militias, request officers, standardize templates, defensive line. |
| Mission cap | One unit-generation mission and one army reform mission. |
| Exploit guard | Show that state-based formations are one-time or require real resources. |

### Decision family: raise provisional guards

| Field | Direction |
| --- | --- |
| Who sees it | Released country with low army size or capital threat. |
| Target | Capital or selected state group. |
| Requirements | Not already used the emergency package for that state, equipment and manpower available, local control minimum. |
| Costs | Infantry equipment, support equipment, manpower, stability or local control. |
| Duration | Instant only for opening package. Repeatable version is 90 to 120 day mission. |
| Success | Spawn limited defensive units or strengthen existing template, lower instability. |
| Partial success | Units spawn understrength, instability or militia fragmentation rises. |
| Failure | Equipment lost and rogue militia risk. |
| AI | Use when division count is below survival need and supply exists. |
| Cleanup | One-time state and country flags prevent repeated free units. |

### Decision family: integrate irregular militias

| Field | Direction |
| --- | --- |
| Who sees it | Released country with militia fragmentation, high instability, or early units. |
| Target | Country or state group. |
| Requirements | Enough legitimacy or command power, local control minimum. |
| Costs | Army XP, command power, infantry equipment, stability risk. |
| Duration | 120 to 180 day mission. |
| Success | Improve templates, lower instability, raise legitimacy if done consensually. |
| Partial success | Improve army but lower legitimacy or coalition trust. |
| Failure | Rogue units, local control loss, possible host exploitation. |
| AI | Military AI prioritizes. Democratic AI uses after assembly or local control. |
| Cleanup | Hide once army professionalization focus resolves militia issue. |

### Decision family: request officer cadres

| Field | Direction |
| --- | --- |
| Who sees it | Released countries with Foreign Support or sponsor route. |
| Target | Sponsor or league. |
| Requirements | Recognition or support channel open, no hostile sponsor relation, army not fully professionalized. |
| Costs | Patron influence, Foreign Support, command power, possible sponsor rivalry. |
| Duration | 90 to 150 days. |
| Success | Army XP, doctrine bonus direction, commander or advisor unlock direction, readiness increase. |
| Partial success | Smaller military benefit with patron influence or ideology drift. |
| Failure | Sponsor influence wasted, rivalry increase, host anger if officers are provocative. |
| AI | Use when army weakness is severe and patron influence is manageable. |
| Cleanup | Clear if sponsor dies, war blocks transfer, or route rejects foreign officers. |

### Decision family: defensive line project

| Field | Direction |
| --- | --- |
| Who sees it | Released country bordering former host or aggressive neighbor. |
| Target | Border state group. |
| Requirements | Control target states, local control minimum, enough construction capacity. |
| Costs | Civilian factory burden, infantry equipment, support equipment, possibly manpower. |
| Duration | 150 to 240 days. |
| Success | Forts or defense modifiers direction, border heat may lower if defensive or rise if provocative. |
| Partial success | Defense improves, but host anger rises due to fortification. |
| Failure | Construction wasted, local control loss, border heat rise. |
| AI | Use if host threat is high. Avoid if settlement route is close and border heat low. |
| Cleanup | Hide after final border settlement if no longer needed. |

### Mission family: prove command obedience

| Field | Direction |
| --- | --- |
| Trigger | Instability high, militia integration underway, or aggressive bloc pressure rising. |
| Objective | Maintain minimum stability, keep capital supplied, avoid rogue militia events, and hold assigned state. |
| Duration | 120 to 180 days. |
| Success | Instability down, legitimacy up, army decisions cheaper. |
| Partial success | Army improves while legitimacy falls. |
| Failure | Rogue command event, local control loss, route pressure toward military rule. |
| AI | Use if militia fragmentation risk is active. |
| Cleanup | Remove if country is annexed, army route resolved, or militia idea replaced. |

## Released country category: border dispute and host settlement

This category sits on both released-country and host-side logic. It should make border heat a playable choice, not only a path to war.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show border heat, former host anger, current dispute state, and settlement window. |
| Target list | Top disputed state groups, host capital protected from invalid demands. |
| Action split | De-escalation, commission, defensive preparation, claims, ultimatum, and treaty enforcement. |
| Warning | Show host last-state protection and treaty lock status where relevant. |

### Decision family: propose border commission

| Field | Direction |
| --- | --- |
| Who sees it | Released country and former host while dispute is active. |
| Target | Disputed state group. |
| Requirements | Not at total war with the other side, border heat not beyond war crisis unless league mediation exists, valid disputed states. |
| Costs | Legitimacy or host political capacity, time, coalition trust if league-backed, sponsor influence if sponsor-backed. |
| Duration | 150 to 240 days. |
| Success | Border heat down, recognition or settlement willingness up, may assign claims or demilitarized status direction. |
| Partial success | Border heat down in one state, host anger or local control worsens elsewhere. |
| Failure | Border heat up, host anger up, aggressive bloc pressure may rise. |
| AI | Diplomatic AI and exhausted hosts prefer. Aggressive AI avoids unless losing. |
| Cleanup | Clear target flags after final settlement, war, or state ownership change. |

### Decision family: demand local plebiscite

| Field | Direction |
| --- | --- |
| Who sees it | Released countries with legitimacy and local control in disputed state, or league-mediated route. |
| Target | Disputed state. |
| Requirements | Control or strong local control in target, not host last state, no duplicate vote mission, no final treaty. |
| Costs | Legitimacy, local control, stability, time, possible sponsor or league support. |
| Duration | 180 to 300 days mission. |
| Success | Claim upgrade or core preparation direction, recognition gain, border heat may fall if accepted. |
| Partial success | Claim strengthens but host anger rises. |
| Failure | Legitimacy loss, local unrest, border heat rises. |
| AI | Use if local control high and host not overwhelming. |
| Cleanup | Vote flags clear on state transfer or final rejection. |

### Decision family: fortify the disputed line

| Field | Direction |
| --- | --- |
| Who sees it | Released country or host with active border heat. |
| Target | Border state group. |
| Requirements | Control target, not under demilitarized treaty, construction capacity. |
| Costs | Civilian factory burden, support equipment, infantry equipment, war support. |
| Duration | 120 to 210 days. |
| Success | Defensive readiness, possible deterrence. Border heat changes based on route and visible posture. |
| Partial success | Defense improves but settlement willingness drops. |
| Failure | Border heat rises and local control drops. |
| AI | Defensive AI uses if threat is high. Settlement AI avoids if talks are active. |
| Cleanup | Demilitarized settlement removes or blocks future fortification. |

### Decision family: issue limited border demand

| Field | Direction |
| --- | --- |
| Who sees it | Ambition route, aggressive bloc route, or high-chaos release. |
| Target | Disputed state group that is not host last state and not protected by final settlement. |
| Requirements | Border heat above minimum, aggressive pressure or legitimacy support, valid army readiness. |
| Costs | Legitimacy, war support, coalition trust or aggressive pressure, equipment, diplomatic backlash. |
| Duration | Clickable with cooldown, may create timed ultimatum. |
| Success | Target accepts transfer, demilitarized compromise, or claim settlement based on relative pressure. |
| Partial success | Claim gained but no transfer, host anger rises. |
| Failure | Host reclamation readiness rises, war risk or border incident mission. |
| AI | Aggressive AI uses against weak hosts. Avoid if host has overwhelming allies. |
| Cleanup | Demand cooldown per target. Clear if war starts or treaty resolves. |

### Mission family: prevent border incident cascade

| Field | Direction |
| --- | --- |
| Trigger | Border heat reaches crisis band and neither side has declared war. |
| Objective | Keep divisions in assigned border states, avoid offensive actions, keep talks or observation open. |
| Duration | 90 to 150 days. |
| Success | Border heat falls, settlement window opens. |
| Partial success | Border heat stabilizes but host anger remains high. |
| Failure | Border heat spikes, border skirmish event or war preparation opens. |
| AI | Use for defensive and settlement routes. Aggressive route may intentionally fail or ignore. |
| Cleanup | Clear on war, final settlement, or state control change. |

## Former host category: host recovery and response

Former hosts need active gameplay because Event 6 must not fully delete them and host response is a core conflict. Host decisions should not erase released countries by default. They should choose between stabilization, negotiation, pressure, and reclamation.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show former host anger, host exhaustion, reclamation capacity, settlement willingness, number of live Event 6 releases. |
| Release list | Top 3 disputes by anger, state value, border heat, and host readiness. |
| Capital protection | Show if host capital is safe, threatened, or retained by fallback rule. |
| Action split | Stabilize remaining host, negotiate, pressure, reclaim, counter-sponsor. |

### Decision family: secure the remaining capital

| Field | Direction |
| --- | --- |
| Who sees it | Former host after losing states through Event 6. |
| Target | Host capital or fallback capital. |
| Requirements | Host exists, owns at least one state, not already under capital security mission. |
| Costs | Political power, command power, infantry equipment, support equipment, stability. |
| Duration | 90 to 150 days mission. |
| Success | Host exhaustion down, reclamation capacity up, capital retention flag strengthened. |
| Partial success | Capital secured but host anger rises due to emergency measures. |
| Failure | Host exhaustion rises, release confidence rises, host response costs increase. |
| AI | Always use if capital threat is high. |
| Cleanup | Clear if host capital changes through valid event logic or host annexed. |

### Decision family: loyal administration drive

| Field | Direction |
| --- | --- |
| Who sees it | Former host with high exhaustion or several released states. |
| Target | Remaining core state group, rail corridor, or region near releases. |
| Requirements | Control target, not actively collapsing, no duplicate mission. |
| Costs | Political power, manpower, support equipment, civilian factory burden. |
| Duration | 120 to 180 days. |
| Success | Host exhaustion down, reclamation capacity up, settlement willingness can rise if moderate. |
| Partial success | Host exhaustion down but anger up. |
| Failure | Host exhaustion up, local unrest, release local control may rise nearby. |
| AI | Stabilization hosts use before aggression. Revanchist hosts use only if exhausted. |
| Cleanup | Remove after recovery phase or if host loses target. |

### Decision family: issue autonomy settlement offer

| Field | Direction |
| --- | --- |
| Who sees it | Former host with settlement willingness and a live release. Released country sees counterpart offer. |
| Target | Event 6 released country. |
| Requirements | Not in total war, host not demanding last state, release not in coercive bloc lock, recognition not final against host. |
| Costs | Host legitimacy or stability, release legitimacy, possible local control concessions, time. |
| Duration | 120 to 210 days mission. |
| Success | Border heat down, host anger down, release recognition up, claims adjusted. |
| Partial success | Border heat falls but one side loses legitimacy or local control. |
| Failure | Host anger rises, release distrust rises, aggressive routes gain pressure. |
| AI | Diplomatic and exhausted hosts use. Revanchist hosts use only when weak or externally pressured. |
| Cleanup | Clear after final treaty, war declaration, or release annexation. |

### Decision family: prepare reclamation plan

| Field | Direction |
| --- | --- |
| Who sees it | Former host with high anger and enough reclamation capacity. |
| Target | Event 6 release or disputed state group. |
| Requirements | Host owns more than last state, target not under protected final treaty, border heat high or release aggressive, host army readiness minimum. |
| Costs | Army XP, command power, equipment, war support, stability risk, host exhaustion. |
| Duration | 150 to 240 days mission. |
| Success | Unlock ultimatum, limited war goal, or pressure decision according to route and world tension. |
| Partial success | Reclamation capacity rises but host exhaustion and foreign backlash rise. |
| Failure | Host exhaustion rises, release recognition or league cohesion rises. |
| AI | Revanchist host uses against weak isolated release. Avoid if target is league-backed and host is weak. |
| Cleanup | Clear if host settles, target dies, or war starts. |

### Decision family: expose foreign patronage

| Field | Direction |
| --- | --- |
| Who sees it | Former host facing sponsor-backed release. |
| Target | Sponsor-target pair. |
| Requirements | Sponsor exists, release has patron influence or foreign support, host has intelligence or diplomacy capacity. |
| Costs | Political power, intelligence exposure direction, stability, possibly command power. |
| Duration | 120 to 180 days. |
| Success | Release patron influence rises in a harmful way or recognition from that sponsor becomes costlier, sponsor rivalry rises. |
| Partial success | Sponsor rivalry rises but release gains anti-puppet legitimacy. |
| Failure | Host credibility loss, release recognition gain. |
| AI | Use when diplomatic route and sponsor pressure is high. Avoid if it would strengthen release coalition. |
| Cleanup | Clear if sponsor dies, target becomes puppet, or relationship becomes irrelevant. |

### Mission family: loyal corridor

| Field | Direction |
| --- | --- |
| Trigger | Host is split by releases or capital supply is threatened. |
| Objective | Hold rail states connecting host capital to remaining industry or ports. |
| Duration | 150 to 240 days. |
| Success | Host exhaustion down, reclamation capacity up, release border heat may fall if corridor is defensive. |
| Partial success | Corridor held but host anger rises through emergency requisitions. |
| Failure | Host exhaustion rises, release local control nearby rises, reclamation delayed. |
| AI | High priority for any host with supply problems. |
| Cleanup | Clear if border settlement, host annexation, or rail corridor lost permanently. |

### Mission family: reclaim without deletion guard

| Field | Direction |
| --- | --- |
| Trigger | Host wins a reclamation war or limited border conflict. |
| Objective | Enforce settlement while preserving Event 6 country rules if full annexation would violate design. |
| Duration | 90 to 180 days after peace or occupation. |
| Success | Transfer limited states, puppet, autonomy, or settlement according to route, remove invalid claims, update origin memory. |
| Partial success | Host regains key state but release retains independence under harsher terms. |
| Failure | Occupation backlash, release resistance, league intervention. |
| AI | Use postwar based on host route and external pressure. |
| Cleanup | Must clear duplicate war goals, active disputes, and stale target flags. |

## Sponsor category: recognition and patronage

Sponsors can be player countries, AI majors, regional powers, or league institutions. Sponsor actions should create useful aid and visible risks.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show target release, support channel, patron influence, sponsor rivalry, and logistics status. |
| Target list | Top Event 6 countries by strategic value, ideology fit, weakness, route compatibility, and distance. |
| Channel display | Recognition, arms, volunteers, industry, intelligence, ideology, logistics, guarantee. |
| Warning | Dominance risk, rival sponsor reaction, host anger, convoy route risk. |

### Decision family: recognize provisional authority

| Field | Direction |
| --- | --- |
| Who sees it | Eligible sponsor and sometimes release as a request. |
| Target | Event 6 release. |
| Requirements | Target exists, legitimacy minimum or sponsor accepts risk, not enemy, sponsor not blocked by ideology or route. |
| Costs | Political power, diplomatic backlash, possible relations loss with host. |
| Duration | Clickable with cooldown or 90 day internal approval mission for cautious sponsors. |
| Success | Target recognition gain, sponsor influence gain, host anger may rise. |
| Partial success | Limited recognition with smaller gains and rivalry increase. |
| Failure | Sponsor loses credibility, target legitimacy can fall. |
| AI | Ideology-compatible sponsors and rivals of host more likely. Distant or exhausted sponsors less likely. |
| Cleanup | Hide if target fully recognized, annexed, or sponsor at war with target. |

### Decision family: send arms convoy

| Field | Direction |
| --- | --- |
| Who sees it | Sponsor with equipment and route. Release may request. |
| Target | Event 6 release with aid corridor. |
| Requirements | Convoy or border route, target not hostile, equipment available, no active duplicate convoy. |
| Costs | Infantry equipment, support equipment, trucks, convoys, fuel if air route, sponsor political cost. |
| Duration | 90 to 150 day mission with corridor objective when needed. |
| Success | Target Foreign Support gain, military readiness gain, sponsor influence gain. |
| Partial success | Some support arrives, convoy losses, patron influence or rivalry rises. |
| Failure | Equipment loss, sponsor rivalry rise, host anger or border heat rise. |
| AI | Use when target can survive and sponsor has surplus. Avoid if convoy route unsafe and sponsor is weak. |
| Cleanup | Clear convoy target flags on delivery, route closure, war, or target death. |

### Decision family: send advisers and officers

| Field | Direction |
| --- | --- |
| Who sees it | Sponsor with military channel open. |
| Target | Event 6 release. |
| Requirements | Recognition or intelligence access, target accepts, not blocked by anti-puppet route. |
| Costs | Command power, army XP, political backlash, patron influence gain. |
| Duration | 120 to 180 days. |
| Success | Target army reform, XP, advisor unlock direction, patron influence rise. |
| Partial success | Military benefit with sponsor rivalry or local backlash. |
| Failure | Adviser scandal, host anger, target legitimacy loss. |
| AI | Use for strategic clients and allied league members. |
| Cleanup | Clear after route rejects foreign officers or target integrates army. |

### Decision family: fund reconstruction mission

| Field | Direction |
| --- | --- |
| Who sees it | Industrial sponsor or league institution. |
| Target | Event 6 release with low local control or damaged economy. |
| Requirements | Target stable enough, route access, sponsor civilian industry. |
| Costs | Civilian factory burden, convoys, political power, patron influence gain. |
| Duration | 180 to 300 days. |
| Success | Target local control, industry, and recognition improve. |
| Partial success | Industry improves while patron influence rises. |
| Failure | Corruption, sponsor rivalry, target instability. |
| AI | Use if target is likely to survive and sponsor wants influence without war. |
| Cleanup | Clear if target annexed, infrastructure route replaced, or war blocks project. |

### Decision family: demand patron concession

| Field | Direction |
| --- | --- |
| Who sees it | Sponsor with high influence over target. |
| Target | Event 6 release. |
| Requirements | Patron Influence above foothold, target not protected by anti-puppet clause, sponsor not overextended. |
| Costs | Sponsor political power, target legitimacy or autonomy, sponsor rivalry. |
| Duration | Clickable with cooldown, may trigger target response mission. |
| Success | Patron influence rises, target receives aid or protection but loses independence resilience. |
| Partial success | Target accepts limited concession and gains anti-puppet backlash. |
| Failure | Target rejects, patron influence falls, rivalry or host diplomacy changes. |
| AI | Dominating sponsors use when target is desperate. Friendly sponsors avoid unless ideology route pushes it. |
| Cleanup | Hide after target becomes puppet, fully rejects patron, or sponsor relationship breaks. |

## League category: Independence League

The league is not just a faction. It is a collective survival mechanism for Event 6 countries. The category appears when enough countries begin league formation or when a focus or high-chaos condition unlocks it.

### League creation requirements

| Requirement | Direction |
| --- | --- |
| Minimum members | At least three Event 6 origin countries, or two if both are large regional releases under severe host threat. |
| Legitimacy | Founding members should have minimum legitimacy or a crisis route that accepts unstable league founding. |
| Recognition | At least one member needs observed recognition or the league forms as an unrecognized compact with lower starting cohesion. |
| Common pressure | Former host anger, border heat, sponsor domination, or shared survival threat. |
| Route compatibility | Members must not be locked into hostile aggressive bloc routes unless the league is transforming into a coercive body. |

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show League Cohesion, League Authority, member count, common threat, and current charter goal. |
| Member list | Show active members, endangered members, dominant member, and puppet-risk members. |
| Shared reserves | Show pooled aid, volunteers, equipment direction, and current transfer cap. |
| Votes | Show active league votes and blocked reasons through concise tooltips. |
| Warnings | Low cohesion, sponsor rivalry, leadership contest, member default, aggressive pressure. |

### Decision family: convene founding charter

| Field | Direction |
| --- | --- |
| Who sees it | Eligible Event 6 country with enough coalition trust or focus unlock. |
| Target | Candidate member group. |
| Requirements | Minimum candidates, no active duplicate founding mission, not locked by aggressive bloc. |
| Costs | Legitimacy, coalition trust, political power, recognition effort, time. |
| Duration | 180 to 300 day mission. |
| Success | League forms, cohesion initialized, members get shared category, super-event threshold may become eligible later. |
| Partial success | League forms weakly with low cohesion or sponsor pressure. |
| Failure | Coalition trust loss, rival blocs or host split actions become easier. |
| AI | Coalition AI attempts if several releases face the same host or threat. |
| Cleanup | Clear candidate flags after formation, failure, or member invalidation. |

### Decision family: admit endangered member

| Field | Direction |
| --- | --- |
| Who sees it | League leader or member with authority. Target release may request. |
| Target | Event 6 release outside league. |
| Requirements | Target exists, not in hostile bloc, not puppet-locked, threat or legitimacy reason. |
| Costs | League cohesion, shared reserves, possible host anger, recognition burden. |
| Duration | 90 to 150 days. |
| Success | Target joins, cohesion changes based on compatibility, threat deterrence improves. |
| Partial success | Target joins with sponsor strings or low trust. |
| Failure | Cohesion loss, target distrust, sponsor rivalry. |
| AI | Admit threatened compatible releases. Avoid members that would trigger unwinnable war. |
| Cleanup | Clear invitation flags when target joins, refuses, dies, or becomes puppet. |

### Decision family: league arbitration panel

| Field | Direction |
| --- | --- |
| Who sees it | League members with internal disputes or host border conflict. |
| Target | Disputed state or member pair. |
| Requirements | League cohesion above weak band, no active arbitration duplicate, parties not at war with each other unless ceasefire exists. |
| Costs | League cohesion, legitimacy from parties, time, possible local control concessions. |
| Duration | 150 to 240 days. |
| Success | Border heat down, claims clarified, league authority up. |
| Partial success | One dispute cools while another member loses trust. |
| Failure | League cohesion loss, member exit risk, aggressive bloc pressure gain. |
| AI | League-minded AI uses for high border heat. Aggressive members may reject. |
| Cleanup | Clear on state transfer, war, or final settlement. |

### Decision family: pooled defense reserves

| Field | Direction |
| --- | --- |
| Who sees it | League members with shared reserve system. |
| Target | Endangered member or common front state group. |
| Requirements | Shared reserve available, target endangered, no duplicate transfer, route allows common defense. |
| Costs | Real equipment or manpower from contributing members, league cohesion, convoy or rail route. |
| Duration | 90 to 180 days mission. |
| Success | Target gains support, league cohesion rises if fair, host deterrence improves. |
| Partial success | Aid arrives but contributing member loses trust or sponsor rivalry rises. |
| Failure | Equipment lost, cohesion falls, target instability rises. |
| AI | Contribute if own threat is manageable and target is strategically important. |
| Cleanup | Strict transfer flags and pool accounting prevent reserve farming. |

### Decision family: common recognition tour

| Field | Direction |
| --- | --- |
| Who sees it | League leader or diplomatic member. |
| Target | External sponsor or region. |
| Requirements | League cohesion minimum, at least two members stable, sponsor valid. |
| Costs | League cohesion, political power, convoys if distant, sponsor rivalry risk. |
| Duration | 180 to 300 days. |
| Success | Recognition gain for multiple members, league authority up. |
| Partial success | Recognition for leader only, cohesion loss. |
| Failure | Sponsor rivalry, host anger, league credibility loss. |
| AI | Use when several members have low recognition and no war crisis. |
| Cleanup | Clear when full recognition reached or target sponsor no longer valid. |

### Mission family: hold the common front

| Field | Direction |
| --- | --- |
| Trigger | League member is threatened by host war, aggressive neighbor, or bloc pressure. |
| Objective | Members hold key border states, keep target capital supplied, and maintain minimum league cohesion. |
| Duration | 180 to 365 days. |
| Success | League cohesion and authority up, defensive bonuses or shared decisions unlock. |
| Partial success | Front held but cohesion drops from unequal burden. |
| Failure | Member exit risk, host confidence, aggressive bloc pressure. |
| AI | League AI should coordinate defense and avoid suicidal expansion during the mission. |
| Cleanup | Clear if war ends, member exits, target capitulates, or common threat disappears. |

### Mission family: charter goal

| Field | Direction |
| --- | --- |
| Trigger | League forms or reforms. |
| Objective | Complete one major goal, such as mutual recognition, common defense, host settlement, anti-puppet charter, or shared reconstruction. |
| Duration | 300 to 540 days. |
| Success | League authority rises, shared category upgrades, super-event threshold can be met if scale is high. |
| Partial success | One member benefits more than others, cohesion drops. |
| Failure | League stagnation, exits, leadership contest. |
| AI | Choose goal based on member threats and route. |
| Cleanup | Only one charter goal active at once. Completed goals get one-time flags. |

## Aggressive bloc category: coercive compact

The aggressive bloc is the high-chaos alternative to the cooperative league. It should feel dangerous and tempting, with strong expansion tools and high backlash.

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show Aggressive Bloc Pressure, member count, current enemy, and backlash risk. |
| Target list | Former hosts, rival releases, disputed regions, weak neighbors, and formable blockers. |
| Pressure meter | Show whether the bloc is posturing, threatening, mobilizing, or committed. |
| Warning | Show war risk, league opposition, sponsor isolation, host preemption. |

### Decision family: found coercive compact

| Field | Direction |
| --- | --- |
| Who sees it | High-chaos release, ambition route, or failed league route. |
| Target | Candidate releases with aggressive pressure. |
| Requirements | Minimum candidates, high border heat or ambition, no league lock unless league transforms, route unlock. |
| Costs | Legitimacy, coalition trust, stability, war support, diplomatic backlash. |
| Duration | 150 to 240 days. |
| Success | Aggressive bloc forms, pressure initialized, members unlock coercive actions. |
| Partial success | Bloc forms with unstable cohesion and sponsor hostility. |
| Failure | Legitimacy loss, host anger, league opposition. |
| AI | Rare. Use only for high-chaos or aggressive archetypes with weak hosts nearby. |
| Cleanup | Clear if bloc collapses or transforms into league settlement. |

### Decision family: synchronized claim drive

| Field | Direction |
| --- | --- |
| Who sees it | Aggressive bloc members. |
| Target | Disputed state group or former host region. |
| Requirements | Pressure minimum, target not protected by final treaty, member claims overlap, valid army readiness. |
| Costs | Aggressive pressure, war support, equipment, legitimacy, sponsor relations. |
| Duration | 120 to 210 days. |
| Success | Claims strengthened, host anger rises, ultimatum unlocks. |
| Partial success | Claims strengthened for one member, bloc pressure unstable. |
| Failure | Border heat spikes, host preemption, league opposition. |
| AI | Use against weak isolated targets and when bloc has military advantage. |
| Cleanup | Per-target cooldown and claim flags prevent spam. |

### Decision family: coordinated ultimatum

| Field | Direction |
| --- | --- |
| Who sees it | Bloc leader or member with authority. |
| Target | Former host, rival release, or neighbor holding target states. |
| Requirements | Pressure high, war prep mission complete or target weak, no final treaty, valid war goal constraints. |
| Costs | Aggressive pressure, equipment, command power, war support, legitimacy, massive diplomatic backlash. |
| Duration | Clickable leading to timed response, or 90 day ultimatum mission. |
| Success | Target concedes limited states, puppet status, demilitarized zone, or claim recognition. |
| Partial success | Target accepts talks, bloc pressure falls, host anger remains. |
| Failure | War, preemptive defense, league counter-pact, or sponsor sanctions. |
| AI | Use only with favorable strength ratio or route compulsion. |
| Cleanup | Clear ultimatum target flags on response, war, or treaty. |

### Decision family: punish defector

| Field | Direction |
| --- | --- |
| Who sees it | Aggressive bloc leader when member exits or refuses major pressure vote. |
| Target | Former bloc member. |
| Requirements | Bloc pressure high, target is valid and not protected by league treaty, no duplicate punishment. |
| Costs | Bloc pressure, legitimacy, war support, internal cohesion risk. |
| Duration | 90 to 180 days. |
| Success | Defector intimidated or expelled, bloc pressure stabilizes. |
| Partial success | Defector remains neutral, bloc pressure falls. |
| Failure | Bloc fracture, league gains legitimacy, host gains settlement opportunity. |
| AI | Use rarely unless bloc is radical and strong. |
| Cleanup | Remove if bloc collapses, target dies, or peace treaty closes issue. |

### Mission family: prepare shock campaign

| Field | Direction |
| --- | --- |
| Trigger | Coordinated ultimatum planned or pressure at mobilizing band. |
| Objective | Place supplied divisions in selected border states, maintain equipment stockpile, keep pressure high. |
| Duration | 120 to 210 days. |
| Success | War goal or ultimatum strength, aggressive pressure up, host deterrence or fear effect. |
| Partial success | War prep completes with high instability or sponsor isolation. |
| Failure | Pressure loss, border incident, host preemption. |
| AI | Use before war. Avoid if target strength ratio bad. |
| Cleanup | Clear if war starts, target concedes, or pressure collapses. |

### Mission family: contain bloc backlash

| Field | Direction |
| --- | --- |
| Trigger | Aggressive pressure too high, multiple ultimatums, or civilian instability. |
| Objective | Keep stability above threshold, prevent member exits, manage host anger or sponsor backlash. |
| Duration | 180 to 300 days. |
| Success | Pressure stabilizes, bloc avoids collapse. |
| Partial success | Bloc survives with sponsor isolation or legitimacy loss. |
| Failure | Member exits, civil conflict risk, league opposition. |
| AI | Aggressive AI attempts if collapse risk is high. |
| Cleanup | Remove when bloc dissolves or transforms. |

## Formable preparation category

Formables should be region-based and origin-aware. Event 6 should not hardcode one fictional country while ignoring every other release. This category provides a generic preparation architecture that special country or regional packages can enrich.

### Category reveal conditions

A formable preparation category should appear when at least one of these is true.

| Reveal condition | Direction |
| --- | --- |
| Regional state control | Country controls a minimum share of states in a defined Event 6 region or historical identity group. |
| Focus unlock | Country completes a route that publicly turns survival into ambition. |
| League vote | League endorses regional settlement or federation project. |
| Aggressive pressure | Coercive bloc opens conquest-oriented formable claims. |
| High chaos evolution | Rare or local polity formables become valid under later chaos evolutions. |
| Hidden identity | A special researched identity unlocks through region, ideology, leader, or prior decision. |

### Category state

| Visible element | Direction |
| --- | --- |
| Header summary | Show formable readiness, required state groups, integration state, recognition need, and rival claimants. |
| State list | Show named region groups, not a raw state dump. |
| Preparation tracks | Integration, legitimacy, recognition, military security, league or sponsor clearance. |
| Warning | Rival claimant, host last-state protection, route incompatibility, patron dependence, missing local control. |

### Decision family: assemble regional dossier

| Field | Direction |
| --- | --- |
| Who sees it | Event 6 country with region eligibility. |
| Target | Region or formable project. |
| Requirements | Event 6 origin, initial state control or claim, not blocked by other event origin. |
| Costs | Political power, legitimacy, research or administrative time, local control in key states. |
| Duration | 150 to 240 days. |
| Success | Reveals required state groups, unlocks integration missions, recognition path. |
| Partial success | Reveals limited claims but raises host anger or rival claimant attention. |
| Failure | Legitimacy loss, border heat, dossier cooldown. |
| AI | Use if country has enough strength and route ambition. |
| Cleanup | Clear if project abandoned, formable completed, or country loses required core region. |

### Decision family: integrate claimant state

| Field | Direction |
| --- | --- |
| Who sees it | Country with revealed formable state group. |
| Target | Required state group. |
| Requirements | Control target, local control minimum, no active integration duplicate, not protected by final treaty against actor. |
| Costs | Local control, legitimacy, equipment for garrison, civilian factory burden, time. |
| Duration | 180 to 365 days depending on size and resistance. |
| Success | State group counts as integrated, core preparation or claim upgrade direction. |
| Partial success | Integration counts for readiness but instability rises or recognition suffers. |
| Failure | Local control drops, border heat or rival claim rises. |
| AI | Prioritize capital, contiguous, and high value required states. |
| Cleanup | Clear if state lost, ceded, or integrated into final formable. |

### Decision family: neutralize rival claim

| Field | Direction |
| --- | --- |
| Who sees it | Country with rival Event 6 claimant or host counterclaim. |
| Target | Rival country or disputed state group. |
| Requirements | Rival exists, overlapping valid claim, no final arbitration, not allied beyond allowed settlement route. |
| Costs | Legitimacy, coalition trust or pressure, sponsor influence, time, possible equipment. |
| Duration | 120 to 240 days. |
| Success | Rival claim weakened, arbitration opens, or rival accepts settlement. |
| Partial success | Rival claim weakens but border heat rises. |
| Failure | Rival gains legitimacy, league cohesion falls or war risk rises. |
| AI | Diplomatic routes choose arbitration. Aggressive routes choose pressure. |
| Cleanup | Clear after formable completion, settlement, rival annexation, or claim expiry. |

### Decision family: convene formation assembly

| Field | Direction |
| --- | --- |
| Who sees it | Country meeting readiness thresholds. |
| Target | Formable project. |
| Requirements | Required state groups controlled or settled, local control and legitimacy high enough, recognition or route substitute, not puppet-locked unless formable is client project. |
| Costs | Legitimacy, recognition effort, stability, political power, league cohesion or sponsor approval if used. |
| Duration | 210 to 365 days mission. |
| Success | Unlock formable decision or execute formation if all hard requirements met. |
| Partial success | Cosmetic or partial federation form, more integration needed, patron or league strings. |
| Failure | Legitimacy loss, rival claims rise, project cooldown. |
| AI | Attempt only when secure and not facing immediate death. |
| Cleanup | On formation, clean old claims, ideas, country flags, route locks, and Event 6 origin overlays as appropriate while preserving origin memory. |

### Mission family: formation security period

| Field | Direction |
| --- | --- |
| Trigger | Formation assembly starts or a formable is declared under pressure. |
| Objective | Hold required capital and integrated states for duration, prevent puppet takeover, keep legitimacy and instability within limits. |
| Duration | 180 to 365 days. |
| Success | Final formable consolidation, core handling, recognition, achievement hook. |
| Partial success | Formable exists but starts with instability or contested regions. |
| Failure | Formation delayed, breakaway risk, rival claimant returns. |
| AI | Use if formation near and war threat manageable. |
| Cleanup | Clear security flags after success, failure, or state loss. |

## Scenario-specific category: release-all variants

The triggerable scenario releases all possible countries. Intensity scales starting territory and units, not whether all possible countries are released. Scenario type controls whether they start in a faction, at war with everyone, at war with hosts, or in a settlement race.

### Scenario setup values

| Value | Direction |
| --- | --- |
| Scenario intensity | Sets starting state share, unit packages, equipment stockpiles, local control, host exhaustion, and starting border heat. |
| Scenario type | Determines faction membership, war state, diplomacy locks, and objective families. |
| Global release pressure | Counts how many countries are live, how many hosts survived, how many wars started, and how many leagues or blocs formed. |
| Scenario objective score | Tracks whether the player is stabilizing, conquering, preserving hosts, or leading a league. |

### Scenario type: all released countries independent

| Field | Direction |
| --- | --- |
| Opening | Every possible country releases with no automatic league and no automatic global war. |
| Main category | Stabilize the new map. |
| Main objectives | Secure capitals, prevent host deletion, establish recognition, resolve a number of disputes. |
| Mission mix | Lower war pressure, many local control missions, settlement and recognition emphasis. |
| AI | Regional AI clusters form leagues or sponsor ties based on pressure, not all at once. |
| Cleanup | Remove scenario-only objectives after global pressure falls or victory condition met. |

### Scenario type: all released countries in a common league

| Field | Direction |
| --- | --- |
| Opening | Every possible release joins a large league or regional sub-leagues if one world league is too unwieldy. |
| Main category | League emergency congress. |
| Main objectives | Keep cohesion, prevent member exits, protect capitals, win recognition, avoid sponsor capture. |
| Mission mix | Charter goals, common defense, pooled reserves, arbitration overload. |
| AI | League AI prioritizes survival and avoids early wars unless attacked. |
| Cleanup | Split oversized league into regional leagues if member count creates UI or AI overload. |

### Scenario type: all releases at war with former hosts

| Field | Direction |
| --- | --- |
| Opening | Every release starts in war against its former host or local host successor. |
| Main category | War of the new states. |
| Main objectives | Hold capitals, keep host from deleting releases, force settlements, avoid league collapse. |
| Mission mix | Defense, aid corridors, host recovery, war settlement, common front. |
| AI | Releases prioritize survival and local fronts. Hosts prioritize capital and limited reclamation. |
| Cleanup | On peace, move to settlement and integration categories. |

### Scenario type: all releases at war with everyone

| Field | Direction |
| --- | --- |
| Opening | Every possible release is hostile to neighbors or to all non-league actors, depending on engine-safe implementation. |
| Main category | Open season. |
| Main objectives | Survive, form bloc or league, hold capitals, reach regional dominance. |
| Mission mix | Aggressive bloc pressure, emergency defense, sponsor collapse, war exhaustion. |
| AI | AI should avoid impossible naval or distant fronts and focus on local threats. |
| Cleanup | Strong cleanup needed to remove invalid war goals, dead target flags, and impossible missions. |

### Scenario type: partition congress

| Field | Direction |
| --- | --- |
| Opening | Every country releases, but starting wars are delayed while a global or regional congress timer begins. |
| Main category | Partition congress. |
| Main objectives | Resolve disputes before the congress timer fails, or exploit it to prepare. |
| Mission mix | Recognition, border commission, host settlement, rival claim neutralization. |
| AI | Diplomatic AI uses congress. Aggressive AI prepares ultimatums. |
| Cleanup | When congress ends, unresolved disputes generate border heat and route-specific consequences. |

### Scenario global mission: preserve every capital

| Field | Direction |
| --- | --- |
| Trigger | Scenario start. |
| Objective | Every live release and surviving host keeps a valid capital for a set period. |
| Duration | 365 days baseline. |
| Success | Global stabilization reward, achievement hook, lower global chaos pressure. |
| Partial success | Most capitals survive, but failed regions get instability or host anger. |
| Failure | Global border heat and aggressive pressure rise. |
| AI | All AI should prioritize capitals during this mission. |
| Cleanup | Clear after success, failure, or scenario victory. |

### Scenario global mission: first world recognition round

| Field | Direction |
| --- | --- |
| Trigger | Scenario start or after first stabilization period. |
| Objective | Reach recognition thresholds for a minimum share of released countries. |
| Duration | 540 days baseline. |
| Success | Unlock league reform, settlement path, and achievement hook. |
| Partial success | Recognized countries stabilize, unrecognized regions become aggressive or patron dominated. |
| Failure | Patron rivalry and border heat surge globally. |
| AI | Sponsors and releases should pursue regional recognition, not every target at once. |
| Cleanup | Clear sponsor target flags and conference flags after end. |

## Scripted GUI architecture

The decision categories can carry the system alone at low scope, but Event 6 benefits from a compact scripted GUI because it can create many countries and values. The GUI should clarify, not replace, decisions and missions.

### GUI working label: Independence Wave ledger

This is a compact management panel available to an Event 6 country, former host, league leader, or scenario controller when relevant. The panel changes mode based on actor type.

| Mode | Actor | Purpose |
| --- | --- | --- |
| Released country mode | Event 6 released country | Show survival values, selected target state, sponsor status, host dispute, and active missions. |
| Former host mode | Former host | Show lost releases, anger, exhaustion, reclamation capacity, settlement willingness, and selected dispute. |
| Sponsor mode | Eligible sponsor | Show sponsored releases, influence channels, rivalry, and aid route risk. |
| League mode | League leader or member | Show members, cohesion, authority, common front, reserves, and charter goal. |
| Aggressive bloc mode | Bloc leader or member | Show pressure, backlash, target claims, ultimatum status, and member loyalty. |
| Scenario mode | Scenario controller or selected observer country | Show global release count, surviving hosts, wars, league or bloc count, and scenario objectives. |

### Released country GUI layout

| Panel area | Content | Interaction |
| --- | --- | --- |
| Header card | Country name, Event 6 origin badge direction, package tier, chaos evolution, current phase | Hover explains origin and why content is Event 6-specific. |
| Value strip | Legitimacy, Recognition, Foreign Support, Patron Influence, Coalition Trust, Border Heat, Instability, Local Control average | Hover shows band, recent changes, and main unlocks. |
| Warning slots | Capital danger, host ultimatum, patron dependence, local control collapse, league vote pending | Click can jump to relevant decision category or selected mission. |
| Target selector | Current state group, host, sponsor, league member, or formable project | Uses top-scored targets and manual cycling buttons. |
| Action row | Up to four important buttons that mirror decision actions | Buttons must have decision equivalents or call shared helper logic. |
| Mission list | Active missions with days remaining and target | Click moves map to target if possible. |
| Route hint | Current focus route hooks and locked family hints without spoilers | Shows public direction only. |

### Former host GUI layout

| Panel area | Content | Interaction |
| --- | --- | --- |
| Header card | Host name, number of releases, capital status, host phase | Hover explains host survival protection and capital retention status. |
| Value strip | Former Host Anger, Host Exhaustion, Reclamation Capacity, Settlement Willingness | Hover shows value bands and current consequences. |
| Release list | Top disputes by score | Select target release for host response decisions. |
| State dispute card | Disputed states, host last-state guard, treaty status | Click highlights states or cycles dispute groups. |
| Action row | Stabilize, negotiate, prepare reclamation, expose patronage | Mirrors decision families. |
| Mission list | Active host recovery and dispute missions | Click target navigation. |

### Sponsor GUI layout

| Panel area | Content | Interaction |
| --- | --- | --- |
| Header card | Sponsor role, active sponsored releases, rivalry warning | Filter targets by region, ideology, or threat. |
| Target list | Top valid releases with recognition need and patron influence level | Select target. |
| Channel strip | Recognition, arms, volunteers, industry, intelligence, ideology, logistics, guarantee | Buttons open or highlight decisions by channel. |
| Rivalry card | Rival sponsors and strongest contested target | Shows risk of pushing too much influence. |
| Aid route card | Port, rail, land, or air route status | Shows blocked route reasons. |

### League GUI layout

| Panel area | Content | Interaction |
| --- | --- | --- |
| Header card | League name direction, members, charter goal, leader | Hover explains league type and current goal. |
| Value strip | League Cohesion, League Authority, shared reserves, common threat | Hover shows changes and unlocks. |
| Member list | Member status, puppet risk, capital danger, contribution | Select member for aid or arbitration. |
| Vote card | Active vote, eligible voters, current likely result direction | Buttons to support, oppose, delay, or enforce where route allows. |
| Common front map | Current league defense target and endangered states | Click target navigation. |
| Mission list | Charter and common front missions | Shows deadlines and burden split. |

### Aggressive bloc GUI layout

| Panel area | Content | Interaction |
| --- | --- | --- |
| Header card | Bloc identity direction, leader, target, pressure band | Hover explains backlash risk. |
| Pressure strip | Aggressive Bloc Pressure, member loyalty direction, war readiness, isolation risk | Shows thresholds and consequences. |
| Target card | Selected host, rival release, or region | Shows treaty blocks and host last-state guard. |
| Ultimatum card | Active demand, timer, likely response direction | Shows warning if war likely. |
| Member row | Contribution, loyalty, defection risk | Select member for pressure or discipline decisions. |

### Scenario GUI layout

| Panel area | Content | Interaction |
| --- | --- | --- |
| Header card | Scenario type, intensity, live releases, surviving hosts | Hover explains that intensity changes territory and units, not release count. |
| Global values | Global release pressure, live wars, league count, bloc count, recognized releases | Shows progress toward scenario objectives. |
| Regional cards | Europe, Africa, Asia, Americas, Middle East, Oceania or project regions | Select region for filtered objectives. |
| Objective list | Current global missions | Click shows targets or affected countries. |
| Cleanup warning | Dead targets, invalid wars, host last-state protection, orphaned missions | Only visible when cleanup actions or errors exist. |

## GUI button rules

Scripted GUI buttons must not become a separate untracked system.

| Rule | Direction |
| --- | --- |
| Decision mirror | Every button that changes gameplay must either trigger a matching decision, call the same scripted effect helper, or be represented by an AI decision. |
| Cost clarity | Button tooltips need the same dynamic cost and requirement summaries as the decision. |
| Cooldown clarity | Buttons show cooldown state and active mission conflicts. |
| AI equivalent | AI must be able to perform the same strategic action through decisions or scripted pulses. |
| Cleanup | Buttons hide when route closes, target dies, actor loses Event 6 origin, or final settlement completes. |
| No hidden exploit | Buttons cannot bypass active mission caps, target caps, or one-time flags. |
| No final wording in spec | The spec gives direction only. Implementation writes final GUI labels and tooltips. |

## Scripted GUI value presentation

| Value | Display direction | Tooltip direction |
| --- | --- | --- |
| Legitimacy | Main statehood meter | Show current band, recent gains, recent losses, major unlocks. |
| Recognition | Diplomatic meter | Show recognized actors, pending delegation, next threshold. |
| Foreign Support | Support pool or channel cards | Show support by channel and whether it is usable or tied to a sponsor. |
| Patron Influence | Warning meter | Show dominant sponsor, dependence threshold, anti-puppet actions. |
| Sponsor Rivalry | Risk meter | Show rival sponsors and what may trigger crisis. |
| Coalition Trust | Cooperation meter | Show league entry readiness and member trust risks. |
| Border Heat | Dispute meter | Show selected host or state group, crisis threshold, settlement options. |
| Instability | Internal danger meter | Show capital, militias, local control, and government weakness. |
| Local Control | Average and selected-state card | Show best and worst state groups, active integration missions. |
| Former Host Anger | Host dispute meter | Show why the host is angry and whether it can act. |
| Host Exhaustion | Host strain meter | Show recovery actions and why host cannot act. |
| League Cohesion | Shared league meter | Show member exits, shared reserves, charter goal. |
| Aggressive Bloc Pressure | Coercive route meter | Show ultimatum thresholds, war risk, and backlash. |

Important values should use consistent colour identities across scripted localisation, decision categories, and GUI. The spec does not assign final colours, but implementation should reserve a stable colour per value family and avoid reusing the same colour for opposite meanings.

## Scripted helper architecture direction

Implementation should avoid duplicating logic across events, decisions, missions, focuses, and GUI buttons. The following helper families should be planned or created by the scripted system architect during implementation.

| Helper family | Purpose | Inputs | Outputs or side effects |
| --- | --- | --- | --- |
| Event 6 actor validation | Confirms actor uses Event 6 origin content | Country scope, optional origin tag | yes or no trigger. |
| Release to host link | Finds former host and dispute records | Release country, host memory | Saved event target or target list. |
| State target scorer | Scores eligible states for local control, border, logistics, formable missions | Actor, target family, route | Ordered target flags or selected target. |
| Sponsor scorer | Scores sponsors by ideology, distance, industry, route, rivalry | Release country, sponsor pool | Top sponsor targets. |
| Mission cap checker | Blocks duplicate mission starts | Actor, category, mission family | yes or no trigger and tooltip reason. |
| Dynamic cost builder | Sets working variables for cost summaries and effects | Action type, actor size, values | Cost variables for decisions and GUI. |
| Value change logger | Applies value changes and records recent-change tooltip data | Actor, value, amount, cause | Value update and recent change memory. |
| League member validator | Checks membership, puppet risk, war status, route compatibility | League scope, member scope | yes or no trigger. |
| Aggressive target validator | Checks treaty blocks, host last-state guard, pressure thresholds | Bloc actor, target | yes or no trigger. |
| Formable readiness checker | Checks region, origin, state groups, local control, recognition, route | Actor, formable project | readiness variables and trigger result. |
| Cleanup sweeper | Clears stale flags for dead targets, lost states, route closures | Actor or global scenario | Cleanup side effects. |

These helpers should use script constants for thresholds, caps, duration bands, AI weights, and value gains where the engine supports them. If a field rejects script constants, implementation can copy the constant into a variable before use.

## Focus hooks that alter categories

The focus tree file defines focus trees in detail. The decisions and GUI file defines how focuses should change decision and GUI architecture.

| Focus type | Decision and GUI effect |
| --- | --- |
| Early statehood focus | Moves Shock to Consolidation, unlocks registry and courts, lowers emergency government cooldown. |
| Assembly focus | Improves provisional assembly mission success and opens recognition delegation. |
| Army centralization focus | Replaces emergency guard actions with professional army missions and hides rogue militia decisions. |
| Local autonomy focus | Makes district administration cheaper, improves local control, reduces legitimacy cost, may slow centralization. |
| Foreign aid focus | Opens more sponsor channels and aid corridor missions, raises patron influence risk. |
| Anti-puppet focus | Unlocks anti-puppet clause decisions and patron influence reduction. |
| League diplomacy focus | Opens founding charter, admission, common recognition, and league GUI mode. |
| Aggressive ambition focus | Opens coercive compact, synchronized claims, and pressure GUI mode. |
| Border settlement focus | Improves commission and treaty missions, lowers host anger from defensive actions. |
| Formable ambition focus | Reveals formation category and regional dossier. |
| High-chaos hidden focus | Raises release power and unlocks stranger decisions, but increases instability, sponsor fear, or border heat. |

Focuses should not simply grant flat value changes. They should unlock categories, replace weak decisions with stronger decisions, alter costs, change AI target preference, and update GUI warnings.

## AI decision architecture

AI must understand Event 6 decisions through archetypes and value priorities. AI should not randomly click every available button.

### Released country AI archetype behavior

| Archetype | Priority actions | Avoids |
| --- | --- | --- |
| Survival republic | Capital mission, assembly, recognition delegation, district administration, defensive line | Aggressive claims unless host threat is existential. |
| Military caretaker | Emergency decree, militia integration, officer cadres, defensive line, reclamation deterrence | Long assembly if instability is high. |
| Patron client | Sponsor recognition, arms convoy, officer mission, guarantee request | Anti-puppet clauses until patron influence becomes dangerous. |
| Balanced neutral | Diversify sponsors, anti-puppet clauses, border commission, local courts | Dominant patron demands, aggressive bloc. |
| League builder | Coalition trust, league charter, common recognition, arbitration | Unilateral border demands that damage cohesion. |
| Aggressive claimant | Claim drive, fortify line, ultimatum preparation, coercive compact | De-escalation unless weak or exhausted. |
| Regional formable | Dossier, integrate claimant states, neutralize rivals, assembly | Early wars before enough control unless high chaos. |

### Former host AI archetype behavior

| Archetype | Priority actions | Avoids |
| --- | --- | --- |
| Stabilizer | Capital security, loyal administration, autonomy settlement, border commission | Reclamation while exhausted. |
| Revanchist | Reclamation plan, expose patronage, fortify line, limited demands | Recognition of releases unless losing or blocked. |
| Exhausted survivor | Capital survival, loyal corridor, settlement, international mediation | Multi-front reclamation. |
| Diplomatic host | Border commission, autonomy settlement, sponsor diplomacy | Aggressive action against league-backed releases. |
| Collapse host | Emergency capital, loyal corridor, limited response | Complex diplomacy and far targets. |

### Sponsor AI behavior

| Sponsor goal | Action pattern |
| --- | --- |
| Ideological expansion | Recognize compatible release, send advisers, push party support, accept patron influence. |
| Regional balance | Recognize releases that weaken rival host, avoid full puppet pressure, support settlement. |
| Client building | Arms, reconstruction, guarantees, patron concessions, dominance risk. |
| Humanitarian or stabilizer | Observer mission, reconstruction, anti-puppet clauses, league recognition. |
| Rivalry containment | Avoid stacking too many actions on one target if sponsor rivalry is near crisis. |

### League AI behavior

League AI should treat cohesion as its health. It should avoid actions that win one member a claim while causing several exits unless the league route is intentionally transforming.

| Condition | AI response |
| --- | --- |
| Low cohesion | Arbitration, shared burden, no new aggressive votes. |
| Endangered member | Pooled reserves, common front, recognition tour if not at war. |
| Strong league authority | Admit members, charter goal, settlement enforcement. |
| Sponsor rivalry | Diversify support, anti-puppet charter, avoid single-sponsor dominance. |
| Member aggression | Arbitration first, discipline or expulsion if repeated. |

### Aggressive bloc AI behavior

Aggressive bloc AI can be bold, but it should not self-destruct without a route reason.

| Condition | AI response |
| --- | --- |
| Pressure low | Claim drive and propaganda actions. |
| Pressure high and target weak | Ultimatum and shock campaign. |
| Target strong or league-backed | Fortify, build pressure, seek sponsor, delay war. |
| Bloc backlash high | Contain backlash mission. |
| Member defection | Punish only if leader has advantage and pressure route demands it. |

## Cooldown model

Cooldowns prevent spam and make decisions feel weighty.

| Action family | Cooldown direction |
| --- | --- |
| Emergency government | Short early cooldown, longer after repeated use. |
| Recognition delegation | Per sponsor cooldown, global diplomacy cap. |
| Arms convoy | Per sponsor and per route cooldown, convoy mission blocks duplicate. |
| District administration | Per state group cooldown. |
| Militia raising | Per state one-time flag plus country cooldown. |
| Border commission | Per dispute cooldown after failure. |
| Limited demand | Per target cooldown and pressure cost. |
| Reclamation plan | Per release cooldown, clears on war or treaty. |
| League admission | Per target invitation cooldown. |
| League arbitration | Per dispute cooldown. |
| Aggressive ultimatum | Per target long cooldown, clears on war or capitulation. |
| Formable dossier | Per formable project cooldown after failure. |
| Integration mission | Per state group active lock and post-failure cooldown. |

Cooldown reductions should come from focus unlocks, high legitimacy, high local control, league authority, or high chaos route pressure. Cooldown bypasses should be rare and should consume real resources.

## Cleanup architecture

Cleanup is central because Event 6 repeats and can create many tags.

### Country cleanup

| Trigger | Cleanup behavior |
| --- | --- |
| Event 6 country annexed | Clear active missions, preserve origin memory for possible re-release, remove decision categories unless government in exile content exists. |
| Event 6 country puppeted | Close independent-only actions, switch patron influence to subject pressure, leave survival actions if subject route exists. |
| Event 6 country changes origin through another event | Do not overwrite Event 6 origin. Origin-specific content should be selected by release source. |
| Event 6 country forms larger country | Move relevant values to formable or convert to inherited values, clean obsolete state flags, keep Event 6 memory for achievements and overlays. |
| Event 6 country joins league | Enable league category, clear incompatible bloc actions. |
| Event 6 country joins bloc | Enable aggressive bloc category, clear incompatible league actions unless transformation route exists. |

### State cleanup

| Trigger | Cleanup behavior |
| --- | --- |
| State lost | Cancel local control, integration, fortification, and corridor missions for that state. |
| State ceded by treaty | Clear dispute flags, local control working penalties, duplicate claims. |
| State becomes core through formable | Clear working integration flags and old claim preparation missions. |
| State is host last state | Block release, demand, transfer, and formable actions that would delete the host. |
| State under another event origin lock | Hide Event 6 integration and claim actions unless that origin explicitly allows overlap. |

### Target cleanup

| Trigger | Cleanup behavior |
| --- | --- |
| Sponsor dies | Cancel sponsor missions, remove target from sponsor list, convert support to orphaned aid or collapse. |
| Host dies | Resolve host dispute through successor logic or close host response categories. |
| League dissolves | Clear league missions, member flags, shared reserve accounting, and GUI mode. |
| Bloc dissolves | Clear pressure missions, ultimatum flags, punishment flags, and war-prep claims. |
| Scenario ends | Clear scenario-only objectives, global counters, and observer categories. |

## Exploit prevention matrix

| Exploit | Prevention |
| --- | --- |
| Free units from repeated militia decisions | State one-time flags, equipment and manpower costs, mission caps, no instant repeat after re-release. |
| Infinite recognition from one sponsor | Per sponsor cooldowns, diminishing returns, full recognition cap, patron influence risk. |
| Patron aid with no downside | Aid raises patron influence, sponsor rivalry, host anger, or dependency unless balanced. |
| Border claim spam | Per target cooldown, legitimacy and pressure cost, final treaty locks, host last-state guard. |
| League reserve farming | Shared reserves draw from real member pools or limited league pool, transfer caps, cooldowns. |
| Aggressive ultimatum spam | High pressure requirement, long cooldown, war risk, diplomatic backlash, target validity. |
| Formable core spam | Integration missions, local control thresholds, region groups, final core cleanup, origin checks. |
| Scenario war-goal overload | Regional target caps, cleanup sweeps, local war focus, no impossible distant war goals. |
| Route switching to collect rewards | Route locks, cleanup of incompatible actions, idea replacements, claim cleanup. |
| Host deletion through demands | Host last-state and capital retention checks on every transfer and ultimatum family. |
| Dead target missions | Validation and cleanup sweeps on owner death, target death, state loss, war end, and treaty. |
| GUI bypass of decision costs | GUI buttons call the same helpers and respect caps, cooldowns, and costs. |

## Localisation and presentation direction

Implementation should write final text from this direction.

| Surface | Direction |
| --- | --- |
| Decision category headers | Concise public status, current values, active mission cap, strongest warning. |
| Decision names | Name the action the government is taking, not the mechanical value. |
| Decision descriptions | Explain public purpose, costs, risks, and visible consequences. Do not reveal hidden route variables. |
| Mission text | State the actual objective, named state group, deadline, and failure risk. |
| GUI labels | Short labels and tooltips that use dynamic actor, state, value, and target names. |
| Blocked requirements | Use custom tooltips and icon-first costs. Avoid raw trigger dumps. |
| Super-event hooks | Do not write final super-event titles or quote text in this file. The super-event and asset file defines research prompts. |
| Scenario text | Explain current scenario mode and objectives. Do not expose implementation setup notes. |

The emotional center should be new governments trying to survive, former hosts trying to hold together, sponsors turning recognition into leverage, and coalitions struggling to keep members alive. Do not make the main presentation a map-change summary or a generic diplomatic notification.

## Documentation outputs from this layer

Implementation should create or update canonical documentation from these requirements. The decision layer needs these docs.

| Document need | Direction |
| --- | --- |
| Decision category map | List all categories, owners, reveal conditions, and cleanup conditions. |
| Mission audit table | Owner, category, target, duration, success, partial, failure, duplicate risk. |
| GUI field ledger | Every displayed value, source variable, tooltip source, and update trigger. |
| Target group ledger | Named state groups, region groups, host links, formable groups. |
| AI action map | AI archetype, action priorities, blocked routes, invalid target gates. |
| Exploit checklist | Confirm each exploit prevention from this file exists or is explicitly replaced. |

## Acceptance criteria for decisions, missions, and scripted GUI

The decision, mission, and GUI design is complete when the implementation agent can answer these questions without inventing the decision, mission, or GUI architecture.

1. Which decision categories exist for Event 6 released countries.
2. Which decision categories exist for former hosts.
3. Which decision categories exist for sponsors.
4. Which decision categories exist for the Independence League.
5. Which decision categories exist for aggressive blocs.
6. Which decision categories exist for formable preparation.
7. Which scenario categories exist for release-all variants.
8. How active mission caps prevent clutter.
9. How target selection works for countries and states.
10. What costs and duration bands apply.
11. How success, partial success, failure, cancellation, and obsolescence work.
12. How provisional statecraft decisions change legitimacy and instability.
13. How local control decisions change state integration and logistics.
14. How recognition and patron decisions change recognition, support, influence, and rivalry.
15. How army and militia decisions create forces without free unit loops.
16. How border and host settlement decisions manage border heat and host anger.
17. How former host decisions manage exhaustion, anger, reclamation, and settlement.
18. How sponsor decisions support or dominate released countries.
19. How league decisions create membership, cohesion, authority, reserves, and charter goals.
20. How aggressive bloc decisions create pressure, ultimatums, and backlash.
21. How formable preparation works generically across regions.
22. How release-all scenario variants use decisions and missions.
23. What scripted GUI modes exist and what each mode displays.
24. How GUI buttons avoid bypassing decision costs and AI equivalents.
25. What helper families should centralize target selection, costs, values, and cleanup.
26. How focus unlocks alter categories.
27. How AI archetypes use the categories.
28. What cooldowns and cleanup rules prevent stale or exploitable content.
29. What localisation direction applies without writing final player-facing text.
30. What documentation tables the implementation needs to keep the system auditable.
