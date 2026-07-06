# 006 Independence Wave Spec Part 2: Mechanics

The core release logic established Event 6 as a Minor Repeatable Liberations event that instantly releases several countries in waves, keeps the former host alive, separates Event 6 origin from Soviet Collapse origin, and gives each released country Independence Wave content. the mechanics layer defines the living mechanics that make those countries and their former hosts play like sudden states trying to survive, not empty tags.

This file uses working labels for mechanics, routes, decisions, missions, and UI surfaces. These labels are not final player-facing localisation.

## Mechanic design promise

Independence Wave should create a triangle of pressure.

The new country wants to become real. It needs domestic authority, outside recognition, armed control of its territory, and enough help to survive.

The former host wants to decide whether the loss is tolerable. It can protest, negotiate, undermine, blockade, prepare reclamation, or attack if it has the strength and anger to do so.

Foreign sponsors and other released countries can keep the new state alive, but their help creates dependency, rivalry, faction pressure, and border disputes.

The system should make every route a tradeoff. A player can rush foreign aid, but this raises patron influence. A player can crack down on instability, but this can lower legitimacy and raise border heat. A player can push maximal claims, but this can damage recognition and push the country toward an aggressive bloc. A player can join the Independence League, but league arbitration can limit expansion and make member disputes matter.

The values should change through visible actions. Focuses, decisions, missions, state control, war, settlements, patron actions, league actions, and former host responses should all move the mechanics. No important value should exist only as a hidden number.

## Origin scope

Every value in this file belongs to Event 6 origin unless the canonical implementation explicitly promotes it into a shared Chaos Redux system.

A tag that exists because of Soviet Collapse uses Soviet Collapse content. The same tag that appears through Independence Wave uses the Event 6 origin values, focus overlay, decisions, missions, and route logic. If a tag later forms a larger country through Event 6, the formable should remember the Event 6 origin unless the formation decision explicitly ends the Independence Wave package and replaces it with a completed formable package.

Origin scope matters for four reasons.

1. A vanilla or pre-existing country should not have its focus tree replaced only because Event 6 can theoretically release that tag.
2. A country released by a different Chaos Redux event should not receive Event 6 league, border heat, patron influence, or formable logic unless that event intentionally opts in.
3. A tag that reappears in a later wave should not duplicate aid, recognition, units, or formable rewards from its previous Event 6 life.
4. A formable or cosmetic identity created through Event 6 should still know which original country, host, wave, sponsor, and league path created it.

Every Event 6 released country needs an origin ledger. The ledger should remember the wave, former host, release package tier, release class, chaos evolution, primary region, initial anchor states, current league or bloc state, and current content package.

## Core values

Each Independence Wave country tracks these values.

| Value | Range | High means | Low means | Core pressure |
| --- | --- | --- | --- | --- |
| Legitimacy | 0 to 100 | The public and institutions accept the government | The country looks like a working occupation, committee, or militia camp | State-building |
| Recognition | 0 to 100 | Foreign governments treat the country as a real state | The country is isolated or treated as a local disturbance | Diplomacy |
| Foreign Support | 0 to 100 | Outside aid is flowing and useful | The country is on its own | Survival |
| Patron Influence | 0 to 100 | Sponsors can bend or capture the country | The country can act independently | Dependency |
| Coalition Trust | 0 to 100 | Other released countries trust this country | Other released countries suspect it or avoid it | League cooperation |
| Border Heat | 0 to 100 | Host retaliation or border conflict is likely | The border dispute is quiet or settled | Host conflict |
| Post-Release Instability | 0 to 100 | Administration, militias, economy, and public order are breaking down | The state is functioning | Internal crisis |
| Local Control | 0 to 100 | The government actually controls its released territory | The map says it owns land, but state power is thin | Integration |

Former hosts track these values.

| Value | Range | High means | Low means | Core pressure |
| --- | --- | --- | --- | --- |
| Former Host Anger | 0 to 100 | The host wants restitution, pressure, or war | The host is willing to tolerate or settle the loss | Response intensity |
| Reclamation Capacity | 0 to 100 | The host has the army, logistics, stability, and border access to act | The host is too weak or distracted | Feasibility |
| Negotiation Willingness | 0 to 100 | The host sees settlement as useful | The host refuses settlement or cannot offer it | Peace path |
| Host Exhaustion | 0 to 100 | The host cannot keep contesting releases | The host can sustain pressure | Forced settlement |

League and bloc systems track these values once the relevant network exists.

| Value | Range | High means | Low means | Core pressure |
| --- | --- | --- | --- | --- |
| League Cohesion | 0 to 100 | The Independence League can coordinate members | The league is a paper pact or close to fracture | Defensive bloc strength |
| League Authority | 0 to 100 | League decisions, arbitration, and shared coordination matter | Members ignore league votes | Shared government |
| Aggressive Bloc Pressure | 0 to 100 | Maximalist countries are coordinating against old borders | Aggressive routes are isolated | High-chaos escalation |
| Sponsor Rivalry | 0 to 100 | Foreign sponsors are competing around released countries | Sponsor activity is quiet or balanced | Proxy conflict |

## Value bands

Use the same broad band language across all values so players learn the pattern. The final localisation should use readable in-world wording and dynamic numbers, not raw debug labels.

| Band | Value range | Positive values mean | Negative pressure values mean |
| --- | --- | --- | --- |
| Broken | 0 to 9 | The institution barely exists | The crisis is almost absent |
| Fragile | 10 to 24 | The institution exists but fails under pressure | The crisis is manageable |
| Disputed | 25 to 44 | The institution works only in some places | The crisis is spreading |
| Functional | 45 to 64 | The institution can shape play | The crisis is dangerous |
| Entrenched | 65 to 84 | The institution can carry a route | The crisis dominates policy |
| Commanding | 85 to 100 | The institution can define the country | The crisis can trigger route failure or escalation |

For Legitimacy, Recognition, Foreign Support, Coalition Trust, Local Control, League Cohesion, and League Authority, high is usually good.

For Patron Influence, Border Heat, Post-Release Instability, Former Host Anger, Aggressive Bloc Pressure, Sponsor Rivalry, and Host Exhaustion, high is usually dangerous, although some routes can exploit the danger.

The design should avoid invisible fractional precision. Player-facing numbers should normally show whole values or simple threshold terms. Fractions matter only if a UI progress bar needs small steps.

## Initial value model

Initial values should use anchors plus dynamic adjustments. The exact constants belong in implementation tuning, but the anchors below define the intended balance.

| Release package | Legitimacy | Recognition | Foreign Support | Patron Influence | Coalition Trust | Border Heat | Instability | Local Control | Former Host Anger added |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Seed | 25 to 35 | 0 to 8 | 0 to 5 | 0 to 5 | 5 to 15 | 15 to 30 | 75 to 90 | 20 to 35 | 6 to 12 |
| Compact | 30 to 42 | 5 to 15 | 3 to 10 | 3 to 10 | 10 to 22 | 20 to 38 | 60 to 78 | 30 to 45 | 10 to 18 |
| Regional | 35 to 50 | 8 to 22 | 8 to 18 | 8 to 18 | 15 to 28 | 30 to 50 | 48 to 66 | 40 to 58 | 18 to 30 |
| Partition | 40 to 58 | 12 to 28 | 12 to 25 | 12 to 28 | 15 to 30 | 45 to 68 | 40 to 60 | 45 to 65 | 28 to 45 |
| Ambition | 45 to 65 | 10 to 30 | 15 to 35 | 18 to 40 | 10 to 26 | 60 to 82 | 45 to 70 | 42 to 64 | 40 to 60 |

Dynamic adjustments should push those anchors.

| Factor | Legitimacy | Recognition | Foreign Support | Patron Influence | Coalition Trust | Border Heat | Instability | Local Control | Host Anger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Existing vanilla or established Chaos Redux tag | Higher | Higher | Slightly higher | No direct change | Higher | Lower | Lower | Higher | Lower |
| Niche historical or local polity | Mixed | Lower at first | Lower unless sponsor-backed | Higher if sponsor-backed | Lower at first | Higher | Higher | Lower | Higher |
| Host is already losing a war | Higher | Slightly higher | Higher | Higher | Higher with nearby releases | Higher if host sees betrayal | Lower if host authority failed | Higher in occupied areas | Higher but capacity lower |
| Host has very high stability and intact army | Lower | Lower | Lower | No direct change | Lower | Higher | Higher | Lower | Higher and capacity higher |
| Release includes capital-like urban anchor | Higher | Higher | Higher | Higher | No direct change | Higher | Lower | Higher | Higher |
| Release lacks contiguous states | Lower | Lower | Lower | Higher | Lower | Higher | Higher | Lower | Higher |
| Same wave has nearby Event 6 countries | Slightly higher | Slightly higher | No direct change | No direct change | Higher | Mixed | Lower if cooperative | Higher if rail and border links exist | Higher |
| High chaos evolution | Higher for armed releases | Lower for strange releases | Higher | Higher | Lower unless league path exists | Higher | Higher or converted into radical strength | Mixed | Higher |

The implementation should keep the host survival rule above all package calculations. If the package must shrink to keep the host alive, initial values should update after the shrink. A country that expected a Regional package but only receives one anchor state should start with more instability, lower local control, and higher border heat because its public claims no longer match its actual territory.

## Legitimacy

Legitimacy measures whether the new government can claim the right to rule.

It is not the same as stability. Stability represents broad national order. Legitimacy is specific to the Independence Wave government. A released country can have decent stability because the war is quiet, but low legitimacy because its ministries, army, local elites, and public institutions do not believe the provisional cabinet has earned obedience.

### Legitimacy bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Broken mandate | The state risks emergency replacement, host-backed restoration, patron capture, or collapse events. |
| 10 to 24 | Hollow authority | The government can act, but decisions cost more and failure events are common. |
| 25 to 44 | Disputed authority | Basic state-building is possible, but formables, strong armies, and league leadership are blocked. |
| 45 to 64 | Provisional mandate | The country can pursue normal survival paths and negotiate with hosts. |
| 65 to 84 | Accepted mandate | The country can lead league work, integrate states, and claim a wider future. |
| 85 to 100 | Founding mandate | The country can attempt major formables, federal projects, and high-risk constitutional or revolutionary routes. |

### What legitimacy changes

Legitimacy should affect the country in visible ways.

| Surface | Effect direction |
| --- | --- |
| Focus routes | Early state-building focuses require enough legitimacy or offer emergency alternatives when legitimacy is low. |
| Decisions | Administrative, recruitment, integration, and recognition decisions become cheaper or more effective with higher legitimacy. |
| Missions | Legitimacy changes the difficulty of capital defense, public administration, and militia integration missions. |
| Army | Low legitimacy creates militia disobedience, worse organization, slower training, or risk of splinter units. |
| Diplomacy | Recognition missions are easier when legitimacy is functional or better. |
| Formables | Major formables require accepted or founding legitimacy unless the route is high-chaos and accepts a dangerous substitute. |
| League | League leadership requires high legitimacy, but league membership should only require disputed or provisional legitimacy. |
| Host response | Low legitimacy makes the former host more willing to claim that the state is working. |

### Legitimacy gains

Legitimacy should rise from actions that prove the country can govern.

| Source | Gain direction | Design note |
| --- | --- | --- |
| Holding the capital or anchor state for a deadline | Moderate to high | This should be one of the clearest early missions. |
| Creating a provisional government through focuses | Moderate | Each political route should solve legitimacy differently. |
| Integrating militias into a national command | Moderate | This can also lower instability. |
| Securing rail, port, or supply anchors | Small to moderate | This ties legitimacy to actual map control. |
| Recognition by one or more credible powers | Moderate | Recognition should help, but should not replace domestic work. |
| League certification or arbitration success | Small to moderate | Cooperative states can validate one another. |
| Winning a host border conflict defensively | High | Victory proves the government can defend itself. |
| Negotiating a host settlement | Moderate to high | The gain is stronger when the host formally accepts borders. |
| Completing a region-specific state-building branch | Moderate to high | This is where shared trees become regionally distinct. |
| Successful local control missions in most owned states | Moderate | This links legitimacy and local control. |

### Legitimacy losses

Legitimacy should fall when the government looks working, captured, or unable to defend its people.

| Source | Loss direction | Design note |
| --- | --- | --- |
| Losing the capital or anchor state | High | This should start a crisis mission or emergency branch. |
| Patron Influence crossing the client threshold | Moderate | Aid becomes evidence of dependency. |
| Post-Release Instability above the commanding band | Moderate to high over time | Disorder corrodes authority. |
| Former host occupation of released states | Moderate to high | Scales with state importance. |
| Failed government formation missions | Moderate | Failure should not be harmless. |
| Aggressive war without recognition | Moderate | The country looks like a raiding state. |
| League arbitration refusal | Small to moderate | Only applies when the country uses league legitimacy but ignores league rulings. |
| Accepting puppet status | High | A puppet route can still survive, but it loses independent legitimacy. |
| Repeated emergency crackdowns | Small repeated losses | Crackdowns can solve disorder while hurting the mandate. |

### Legitimacy route variations

Each route should treat legitimacy differently.

| Route type | Legitimacy logic |
| --- | --- |
| Democratic or legalist route | Gains legitimacy from elections, councils, observers, legal continuity, host settlement, and league arbitration. |
| Military route | Gains legitimacy from security, victory, supply control, and integration of units, but struggles with recognition and civilian trust. |
| Socialist or revolutionary route | Gains legitimacy from local committees, worker or peasant mobilisation, and anti-host success, but may lose recognition with hostile sponsors. |
| Monarchist or restoration route | Gains legitimacy from dynastic symbols, old institutions, religious or noble backing, and control of historic centers. It can lose legitimacy if the claimant lacks territory. |
| Patron-backed route | Gains short-term legitimacy through aid and recognition, but loses long-term independent legitimacy if Patron Influence dominates. |
| League route | Gains legitimacy through shared certification, member defense, and joint recognition work. It loses legitimacy if the league fractures. |
| Aggressive bloc route | Can replace normal legitimacy with fear, mobilization, and victory pressure. It should be powerful, but unstable and diplomatically costly. |
| High-chaos strange route | Can use unusual forms of legitimacy such as prophecy, antiquity, local myth, sacred memory, industrial command, or war cult authority. The final text must handle these as direction, not unsourced claims. |

### Legitimacy hooks

Working decision families tied to legitimacy:

| Working family | Purpose | Costs and risks |
| --- | --- | --- |
| Provisional government assembly | Establishes the first governing structure | Political power, stability risk, local support, possible patron interference. |
| Administrative inventory | Turns claimed institutions into usable state capacity | Civilian factory burden, command power, trains, local control requirement. |
| Militia oath program | Converts local guards into state forces | Infantry equipment, support equipment, army XP, legitimacy gain, possible instability if rushed. |
| Public mandate drive | Builds legitimacy through public institutions | Stability, time, local control, ideology-specific risks. |
| Emergency crackdown | Lowers instability quickly | Command power, infantry equipment, possible legitimacy loss, higher border heat if brutal. |

Working mission families tied to legitimacy:

| Working mission | Success | Failure |
| --- | --- | --- |
| Hold the founding capital | Legitimacy and local control gain, instability loss | Legitimacy collapse risk, host confidence gain, emergency route opens. |
| Guard the first ministries | Legitimacy gain, militia obedience gain | Instability gain, political route delay. |
| Secure the declaration corridor | Recognition and legitimacy gain when rail or port route remains open | Foreign support delay, sponsor influence can rise because the country needs emergency aid. |
| Complete the public mandate period | Higher legitimacy and route unlock | Radical or military fallback pressure. |

Focus hooks:

| Focus branch | Legitimacy use |
| --- | --- |
| Opening survival branch | Gives first legitimacy tools and emergency alternatives. |
| Political route branch | Defines how the state claims authority. |
| Army integration branch | Links legitimacy to unit obedience and recruitment. |
| Host settlement branch | Turns legitimacy into treaty strength. |
| League branch | Lets legitimacy become league leadership prestige. |
| Formable branch | Requires accepted or founding legitimacy unless the route is high-chaos and intentionally rejects normal legality. |

## Recognition

Recognition measures how much the outside world treats the new country as a state. It is not only a count of countries that recognize it. It is a combined state of public diplomatic acceptance, trade access, foreign observers, treaty commitments, and whether other powers believe the government can survive.

### Recognition bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Isolated claim | The country can barely trade or seek aid except through covert channels. |
| 10 to 24 | Observed authority | Foreign observers, journalists, exiles, or liaison offices can appear, but formal deals are weak. |
| 25 to 44 | De facto contacts | Minor aid, limited trade, and informal guarantees become possible. |
| 45 to 64 | Partial recognition | Major diplomatic decisions, open aid corridors, and negotiated host settlements become realistic. |
| 65 to 84 | Treaty recognition | Strong guarantees, league leadership, and wider trade support become possible. |
| 85 to 100 | Settled status | The country is treated as hard to reverse without major war. |

### Recognition uses

| Surface | Effect direction |
| --- | --- |
| Trade and economy | Higher recognition unlocks foreign investment, trade access, and reconstruction decisions. |
| Foreign support | Higher recognition makes aid safer and lowers the patron influence gained from normal aid. |
| Host settlement | The host finds it harder to dismiss a recognized state. |
| League | The league needs members with enough recognition to claim international weight. |
| Aggressive routes | Aggressive actions become more costly when recognition is low. |
| Formables | Diplomatic or federal formables often need recognition. Conquest or high-chaos formables can bypass it with costs. |
| Super-event thresholds | Major league or formable super-events are stronger when recognition is high. |

### Recognition gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Sending observer missions | Small to moderate | Should cost time, convoys or diplomatic effort, and local control. |
| Sponsor recognition | Moderate | Gives faster recognition but also raises Patron Influence. |
| League mutual recognition | Small per member, stronger with league authority | Useful for small states. |
| Host treaty or armistice | High | The strongest non-war recognition source. |
| Defensive victory over former host | Moderate to high | Recognition rises when the country proves survival. |
| Control of capital and claimed anchor states | Small repeated gains | Recognition should follow visible control. |
| Avoiding aggressive wars during the recognition period | Small over time | Rewards restrained routes. |
| Completing region-specific diplomatic focus groups | Moderate | Allows local flavour without final text. |

### Recognition losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Losing capital or anchor state | High | Foreign observers lose confidence. |
| Aggressive bloc membership | Moderate or high | Depends on bloc pressure and ideology. |
| Starting unjustified wars against other released countries | Moderate | Especially damaging inside the league network. |
| Patron Influence above client levels | Moderate | Outsiders treat the country as a proxy. |
| Sponsor Rivalry above dangerous levels | Small repeated losses | Foreign support becomes suspicious. |
| Former host diplomatic campaign success | Small to moderate | Host decisions can erode recognition. |
| Post-Release Instability above high bands | Small repeated losses | Disorder makes formal recognition harder. |

### Recognition decision hooks

Working decision families:

| Working family | Purpose | Costs and risks |
| --- | --- | --- |
| Invite foreign observers | Opens initial recognition paths | Requires capital control and local control, costs convoys or diplomatic effort. |
| Recognition tour | Builds relations with a selected sponsor or nearby state | Political power, civilian burden, possible patron influence. |
| Publish state continuity evidence | Uses historical, legal, or administrative claims to improve recognition | Requires stability and low enough instability, can fail for strange high-chaos tags. |
| League recognition pact | Members recognize each other and pool diplomatic credibility | Requires Coalition Trust and enough member legitimacy. |
| Treaty conference with former host | Attempts a host settlement | Requires low enough Border Heat or high enough host exhaustion. |
| Anti-puppet assurance | Reduces fear of sponsor capture | Costs foreign support tempo and reduces Patron Influence if successful. |

Working mission hooks:

| Working mission | Success | Failure |
| --- | --- | --- |
| Keep the observer route open | Recognition and support gain | Patron Influence rises because emergency channels replace formal access. |
| Hold the treaty capital | Recognition gain and host anger loss | Border Heat and Former Host Anger rise. |
| Complete a neutral conference window | Host settlement chance and recognition gain | Sponsor Rivalry rises if patrons sabotage the process. |

## Foreign Support

Foreign Support is the useful side of outside involvement. It covers arms, advisors, volunteers, intelligence help, industrial investment, observer missions, logistics access, medical aid, and diplomatic help.

Foreign Support should never be free. Every strong support action should create at least one pressure, such as Patron Influence, Sponsor Rivalry, Host Anger, convoy risk, intelligence exposure, ideological drift, or league suspicion.

### Support channels

Foreign Support should be split into channels in design, even if implementation compresses some channels into shared values.

| Channel | Helps with | Main risk |
| --- | --- | --- |
| Recognition | Diplomatic acceptance and host settlement | Patron leverage over foreign policy. |
| Arms | Equipment, unit readiness, border defense | Dependency on sponsor supply and possible host anger. |
| Volunteers | Early survival and defensive wars | Sponsor influence, foreign escalation, ideological pressure. |
| Industry | Factories, construction, rail, ports, supply | Economic dependency and consumer burden. |
| Intelligence | Counter-host operations and sponsor competition | Sponsor Rivalry and coup risk. |
| Logistics | Aid corridors, convoys, trains, fuel | Route vulnerability and blockade risk. |
| Ideology | Party growth, advisors, route unlocks | Domestic legitimacy loss if seen as foreign capture. |

### Foreign Support bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | On its own | Only local tools are available. |
| 10 to 24 | Contact channels | Small aid, observers, and low-risk support are possible. |
| 25 to 44 | Aid stream | Equipment and advisors can change survival odds. |
| 45 to 64 | Foreign lifeline | The country can build a serious army or economy through aid. |
| 65 to 84 | Sponsor-backed state | Support is powerful, but Patron Influence must be watched. |
| 85 to 100 | Proxy pillar | The country can become strong quickly, but capture pressure is severe. |

### Foreign Support gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Recognition decisions | Small to moderate | Formal recognition makes support easier. |
| Accepting arms shipments | Moderate | Costs convoys, relations, or ideological concessions. |
| Volunteer agreements | Moderate | Strong in war, costly in independence. |
| Sponsor investment projects | Moderate to high | Builds economy but raises influence. |
| League shared reserves | Small to moderate | Support without one patron dominating. |
| Holding aid corridors | Small repeated gains | Requires map control and missions. |
| High-chaos sponsor scramble | High | More aid, more rivalry, more manipulation. |

### Foreign Support losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Sponsor defeated, capitulated, or cut off | Moderate to high | Support should not survive impossible routes. |
| Aid corridor lost | Moderate | Good mission failure consequence. |
| Patron Influence crisis rejected | Moderate | Independence route sacrifices aid to stay free. |
| League sanctions against aggressive member | Small to moderate | Defensive league can punish maximalist behavior. |
| Former host blockade success | Moderate | Host response can attack support indirectly. |
| Sponsor Rivalry crisis | Mixed | Rivalry can add aid but disrupt usable support. |

### Support decisions

Foreign support decisions should use non-political costs wherever possible.

| Working decision family | Main benefit | Main cost or risk |
| --- | --- | --- |
| Request rifle shipments | Infantry equipment or militia conversion | Convoys, patron influence, sponsor relation requirement. |
| Request support equipment mission | Support equipment and template unlocks | Patron influence, intelligence exposure. |
| Invite officer cadres | Army XP, commander traits, training decisions | Patron influence, legitimacy loss if high. |
| Industrial loan mission | Factories, infrastructure, construction speed | Civilian factory burden, patron influence. |
| Volunteer corridor | Volunteer units or working combat support | Sponsor rivalry, host anger, route access. |
| Intelligence liaison | Counter-host actions and border information | Sponsor rivalry, ideological drift, coup risk. |
| Balanced aid conference | Foreign support without one dominant patron | Sponsor rivalry, time, recognition requirement. |

## Patron Influence

Patron Influence measures the cost of foreign support. It is the pressure that outside powers gain over the new country.

A country can accept high patron influence intentionally. A client route should be playable and powerful, not only a failure state. It should trade independent legitimacy, league trust, and formable access for equipment, advisors, protection, and sponsor-backed ideology.

### Patron Influence bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Independent | Sponsors have no meaningful hold. |
| 10 to 24 | Friendly advisers | Aid has strings, but the state can refuse demands. |
| 25 to 44 | Influence foothold | Sponsor demands, party pressure, and adviser privileges begin. |
| 45 to 64 | Binding dependency | Some decisions require sponsor approval or create refusal crises. |
| 65 to 84 | Client danger | Puppet pressure, route locking, coups, and league suspicion become serious. |
| 85 to 100 | Captured state | The country risks puppet status, sponsor coup, forced faction entry, or leader replacement. |

### Patron Influence gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Any strong foreign aid | Small to high | Scales by aid type and recognition. Low recognition makes aid more binding. |
| Single sponsor dominance | Repeated gain | If one sponsor gives most support, influence rises faster. |
| Foreign advisors and officer cadres | Moderate | Useful military path with political cost. |
| Sponsor-funded industry | Moderate | Creates economic dependency. |
| Sponsor guarantee | Moderate to high | Guarantees are powerful and should not be free. |
| Ideological support | Moderate | Ties domestic politics to foreign policy. |
| Emergency bailout during low legitimacy | High | Rescue at the worst moment should create heavy dependency. |

### Patron Influence losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Rising Recognition | Small over time | A recognized state can bargain better. |
| Balanced aid from multiple sponsors | Small to moderate | Can reduce dominance but increase Sponsor Rivalry. |
| League support replacing sponsor support | Moderate | Defensive league can help members escape dependency. |
| Anti-puppet reforms | Moderate | Costs support tempo, stability, or sponsor anger. |
| Refusing sponsor demands | Moderate | Often reduces support or raises coup risk. |
| Victory without sponsor troops | Moderate | Proves independent capability. |

### Patron Influence crisis states

| Trigger concept | Outcome direction |
| --- | --- |
| High Patron Influence with low Legitimacy | Sponsor can demand leader change, base rights, faction entry, or puppet status. |
| High Patron Influence with high Recognition | Sponsor influence becomes a diplomatic struggle instead of immediate capture. |
| High Patron Influence inside a strong league | League can vote to limit the sponsor, defend the member, or expel the member if it becomes a proxy. |
| High Patron Influence in aggressive bloc | Sponsor can turn the bloc into a proxy war tool, but rival sponsors raise Sponsor Rivalry. |
| Patron Influence reaches captured band | The country must choose independence crisis, client route, coup risk, or open puppet path. |

### Patron route hooks

Patron routes should not feel like generic ideology paths. They should change the country package.

| Surface | Patron route effect direction |
| --- | --- |
| Leader | Can add sponsor-aligned leader, minister, council, or military mission. |
| Party | Sponsor ideology gains party names and movement labels. |
| Advisors | Sponsor advisers become available and cheaper. |
| Decisions | Aid becomes cheaper, but refusal decisions become harder. |
| League | Coalition Trust falls with independent members. Client states may create a sponsor caucus inside the league. |
| Formables | Some formables become blocked, client-branded, or require sponsor approval. |
| Flags and cosmetics | Client route may need route-specific flag or cosmetic name if it becomes stable. |

## Sponsor Rivalry

Sponsor Rivalry measures competition among foreign powers around Event 6 countries. It can exist around one country, a region, or a league.

Sponsor Rivalry is not automatically bad. Balanced rivalry can help a new state avoid capture by one patron. Dangerous rivalry can turn recognition, aid, and border disputes into proxy pressure.

### Sponsor Rivalry bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Quiet channels | Sponsors are not a major pressure. |
| 10 to 24 | Competing envoys | Small bonuses to aid choice, minor risks. |
| 25 to 44 | Rival missions | Sponsors undercut each other, but the country can exploit competition. |
| 45 to 64 | Proxy contest | Aid improves, Patron Influence and instability risks rise. |
| 65 to 84 | Foreign struggle | Coup, sabotage, league fracture, and host escalation events become likely. |
| 85 to 100 | Proxy crisis | A local release can become a great-power confrontation or trigger aggressive bloc support. |

### Sponsor Rivalry gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Multiple major sponsors active in same region | Moderate repeated gain | Strongest when ideologies oppose each other. |
| One sponsor backs a release while another backs the former host | High | Creates proxy border risk. |
| Several releases accept different patrons | Moderate to high | Can damage league cohesion. |
| Aggressive bloc seeks foreign arms | High | Sponsor rivalry should be one path to global fear. |
| Host diplomatic counter-recognition | Small to moderate | Competing diplomatic campaigns raise rivalry. |
| Intelligence liaison decisions | Moderate | Useful but risky. |

### Sponsor Rivalry losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| League recognition framework | Moderate | Strong league can channel sponsors through common rules. |
| Host settlement | Moderate | Removes one proxy flashpoint. |
| Balanced neutral doctrine | Small repeated loss | A route can try to keep foreign competition limited. |
| One sponsor leaves or loses access | Moderate | May also raise Patron Influence if another sponsor dominates. |
| Recognition above treaty band | Small repeated loss | Settled status reduces opportunistic contest. |

### Sponsor Rivalry decisions

| Working decision family | Purpose | Risk |
| --- | --- | --- |
| Balance sponsor missions | Reduce Patron Influence from one sponsor | Raises Sponsor Rivalry and can lower aid efficiency. |
| Expose rival patronage | Reduce a rival sponsor foothold | Raises intelligence exposure and instability. |
| Accept competing guarantees | Gain protection from several powers | Raises Sponsor Rivalry and league suspicion. |
| Neutral conference channel | Lower rivalry and improve recognition | Requires high legitimacy and recognition. |
| Sponsor caucus inside the league | Turns patron alignment into league politics | Can split the league or create client blocs. |

## Coalition Trust

Coalition Trust is each country's relationship with other Independence Wave countries. It measures whether other released governments believe this country will respect their borders, join common defense, share aid, and avoid turning the wave into a private empire.

Coalition Trust is not identical to League Cohesion. Coalition Trust belongs to countries. League Cohesion belongs to the league once it forms.

### Coalition Trust bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Distrusted | Other releases refuse shared plans unless forced by fear. |
| 10 to 24 | Contact only | Observer contact and minor aid are possible. |
| 25 to 44 | Working contact | Basic league preparation and recognition pacts can begin. |
| 45 to 64 | Reliable partner | League membership, arbitration, and shared defense are realistic. |
| 65 to 84 | Trusted founder | The country can lead committees or mediate disputes. |
| 85 to 100 | Coalition pillar | The country can drive league formation or federal projects. |

### Coalition Trust gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Same wave survival | Small | Shared origin creates a first connection. |
| Mutual recognition | Small to moderate | Cooperative diplomacy. |
| League observer contact | Small | First step toward league. |
| Defending another released country | High | Strongest trust source. |
| Settling border dispute through arbitration | Moderate | Shows restraint. |
| Sharing foreign aid | Moderate | Uses Foreign Support to build coalition. |
| Refusing exclusive patron demands | Moderate | Independent countries trust the member more. |
| Host threat against several releases | Small repeated gain | Common danger can unite rivals. |

### Coalition Trust losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Pressing claims on another released country | Moderate to high | Directly opposes league logic. |
| Aggressive bloc alignment | High | Defensive league members distrust maximalists. |
| Patron Influence above client band | Moderate | Members fear proxy capture. |
| Sponsor Rivalry inside league | Small repeated loss | Rival sponsors split members. |
| Refusing league arbitration | Moderate | Only applies if league path is active. |
| Abandoning a member under attack | High | Should have a clear consequence. |
| Host settlement that sacrifices another release | High | Creates lasting distrust. |

### Coalition Trust uses

| Surface | Use |
| --- | --- |
| League formation | Requires several countries with reliable or better trust. |
| League leadership | Higher trust increases leadership chance and influence over votes. |
| Shared reserves | Members with high trust receive better aid. |
| Recognition pacts | Trust reduces diplomatic cost. |
| Arbitration | Trust unlocks peaceful border settlement. |
| Aggressive bloc refusal | High trust blocks or strongly discourages joining the aggressive bloc. |
| Formables | Federal or league-backed formables require trust from members that join or accept the new identity. |

## Border Heat

Border Heat measures how close the release and former host are to escalation. It also covers disputes with other released countries when their claims overlap, but the former host relationship is the main use.

Border Heat should make the host a living actor. The host is not a passive state donor. It keeps at least one state, preferably the capital when possible, and then decides how hard to challenge the release.

### Border Heat bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Quiet border | Normal defenses and diplomatic contact. |
| 10 to 24 | Watchful border | Host protest and small incidents possible. |
| 25 to 44 | Disputed border | Border missions, claims, and limited pressure appear. |
| 45 to 64 | Militarized border | Host mobilization and release defensive missions become important. |
| 65 to 84 | Reclamation crisis | Ultimatums, proxy moves, war preparation, and league intervention can occur. |
| 85 to 100 | Open flashpoint | War, forced settlement, or major league intervention becomes likely. |

### Border Heat gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Larger release package | Higher initial heat | Partition and Ambition packages should be dangerous. |
| Former host anger | Repeated gain | Host anger feeds border pressure. |
| Release claims outside immediate package | Moderate | Claims should not be free. |
| Military buildup near host border | Small to moderate | Useful for defense, risky for diplomacy. |
| Host refuses recognition | Small repeated gain | Diplomatic hostility matters. |
| Patron sends volunteers or arms | Moderate | Host sees escalation. |
| Aggressive bloc pressure | High | Maximalist routes intensify border heat. |
| Failed arbitration | Moderate | Peaceful path failure matters. |
| Former host is ideological enemy | Small to moderate | Ideology shapes escalation. |

### Border Heat losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Host settlement | High | Treaty lowers heat strongly. |
| League arbitration success | Moderate | Especially when league authority is high. |
| Demilitarized border mission | Moderate | Costs defensive readiness. |
| Recognition above partial band | Small repeated loss | Formal diplomacy stabilizes. |
| Host exhaustion above high band | Moderate | Host cannot sustain pressure. |
| Release abandons maximal claims | Moderate | Sacrifices ambition for safety. |
| Shared threat from another event | Small | A world threat can make old disputes less urgent. |

### Border Heat outcomes

| Threshold or pattern | Outcome direction |
| --- | --- |
| Disputed border with low host capacity | Host uses diplomatic protest, sanctions, or covert pressure. |
| Disputed border with high host capacity | Host gains reclamation preparation and border missions. |
| Militarized border with strong release | Release can deter war or force settlement. |
| Reclamation crisis with strong league | League can intervene, arbitrate, or threaten collective defense. |
| Open flashpoint with aggressive bloc | Bloc can trigger regional war or super-event threshold if large enough. |
| Open flashpoint with low legitimacy release | Host can demand return, autonomy, or puppet settlement. |

### Border Heat decision hooks

| Working decision family | Purpose | Costs and risks |
| --- | --- | --- |
| Border commission | Clarifies disputed states and claims | Political effort, local control, risk of failed talks. |
| Fortify the release line | Defensive bonuses and border control | Infantry equipment, support equipment, civilian factory burden, raises heat. |
| Demilitarized settlement | Lowers heat | Requires recognition and host willingness, can lower aggressive route support. |
| League arbitration request | Lowers heat through league | Requires trust and league authority. |
| Host ultimatum response | Choose settlement, delay, mobilization, or refusal | Costs legitimacy, equipment, stability, or border heat. |
| Maximal claim campaign | Raises claims and bloc pressure | Damages recognition and coalition trust. |

## Post-Release Instability

Post-Release Instability is the internal disorder created by sudden independence. It includes broken administration, rival militias, legal confusion, supply disruption, contested police authority, tax failure, food panic, refugee movement, split rail command, and uncertainty over who can issue orders.

It should be the main early crisis for most released countries. A country that ignores it should feel weaker even if it is not immediately at war.

### Instability bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Settled administration | Instability is no longer a central problem. |
| 10 to 24 | Manageable disorder | Some decisions remain useful, but the state can focus on other goals. |
| 25 to 44 | Strained administration | Early penalties and missions matter. |
| 45 to 64 | Severe disorder | Army, economy, local control, and legitimacy suffer. |
| 65 to 84 | Fracturing state | Failure events, rival councils, militia splits, and patron capture become likely. |
| 85 to 100 | Near breakdown | The country faces emergency replacement, collapse, civil conflict, or forced dependency. |

### Instability effects

| Surface | Effect direction |
| --- | --- |
| Economy | High instability reduces construction efficiency, output, or consumer capacity. |
| Army | High instability reduces organization, training speed, and militia obedience. |
| Diplomacy | High instability makes recognition harder. |
| Legitimacy | High instability repeatedly lowers legitimacy. |
| Local control | High instability slows control gains and can reduce state control. |
| Focus routes | Some routes need to stabilize first, while high-chaos routes can exploit instability. |
| Decisions | Stabilization decisions cost equipment, manpower, XP, or local control, not only political power. |

### Instability gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Sudden release package | Initial | Seed and Ambition packages can both be unstable for different reasons. |
| Low legitimacy | Repeated | Public distrust feeds disorder. |
| Low local control | Repeated | Weak state presence makes disorder worse. |
| Losing important states | Moderate to high | Especially capital, ports, rail hubs, and depots. |
| Patron rivalry | Small to moderate | Sponsors split institutions. |
| Failed missions | Moderate | Failure should have teeth. |
| Host covert pressure | Small to moderate | Former host can destabilize without war. |
| Aggressive mobilization | Small to moderate | Rapid militarization disrupts government. |

### Instability losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Provisional administration focuses | Moderate | Core early branch. |
| Integrating militias | Moderate | Also improves army. |
| Securing rail and supply hubs | Moderate | Links map action to stability. |
| Local control missions | Small to high | Depends on state value. |
| Recognition and aid | Small to moderate | Aid helps if not captured by patrons. |
| League stabilization support | Small to moderate | Useful for small countries. |
| Host settlement | Moderate | Uncertainty falls when borders settle. |
| Emergency crackdown | High immediate loss | Should hurt legitimacy or raise border heat. |

### Instability route variations

| Route | Instability treatment |
| --- | --- |
| Civilian route | Lowers instability through institutions, elections, local councils, and public administration. |
| Military route | Lowers instability quickly through command and guard networks, but can hurt legitimacy and recognition. |
| Revolutionary route | Converts some instability into mobilization, but risks factional splits. |
| Patron route | Lowers instability with external resources, but raises Patron Influence. |
| League route | Lowers instability with shared advisers and common reserves. |
| Aggressive route | Can ignore some instability while at war, but risks collapse after setbacks. |
| High-chaos route | May transform instability into a strange power source, but this should be dangerous and route-locked. |

## Local Control

Local Control measures whether the released country controls its own territory in practice. Ownership and control on the HOI4 map are not enough. A new country can own a state, but still have low local control if ministries, police, depots, rail lines, food distribution, and local leaders are not integrated.

Local Control should be partly country-wide and partly state-aware. The country-wide value is the average sense of control used for most UI and route gates. State-aware control matters for integration, coring, recruitment, resistance, and formable decisions.

### Local Control bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Paper control | The government has almost no usable presence outside a few buildings. |
| 10 to 24 | Thin control | Emergency decisions work, but recruitment and integration are poor. |
| 25 to 44 | Contested control | Basic administration exists in anchor states. |
| 45 to 64 | Working control | State integration and military recruitment are reliable. |
| 65 to 84 | Deep control | Cores, formables, and strong recruitment become realistic. |
| 85 to 100 | Rooted control | The country can absorb larger territories or lead federal integration. |

### State layers

Each released state can be treated as one of four layers.

| State layer | Meaning | Local Control expectation |
| --- | --- | --- |
| Anchor state | The state that makes the country exist | Should start highest and matter most. |
| Support state | A contiguous state that gives ports, industry, rail, or depth | Starts lower than anchor, but can be integrated early. |
| Disputed state | A state the country controls but whose claim is contested | Starts low and raises Border Heat. |
| Claimed state | A state not yet controlled but claimed by route or formable logic | No local control until acquired. |

### Local Control gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Holding anchor state | Small repeated gain | Baseline proof of state presence. |
| Local administration decisions | Moderate | Costs equipment, manpower, or civilian burden. |
| Rail and supply missions | Moderate | Makes logistics meaningful. |
| Militia integration | Small to moderate | Local guards become state forces. |
| Recognition and host settlement | Small to moderate | Public uncertainty falls. |
| League technical missions | Small | Useful for weak members. |
| Defeating local host-backed unrest | Moderate | Ties host pressure to local control. |

### Local Control losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Losing state control | High for affected state | Country-wide loss depends on state importance. |
| Instability above severe band | Repeated | Disorder erodes control. |
| Host covert pressure | Small to moderate | Host can attack control without war. |
| Sponsor rivalry | Small | Rival patrons split local institutions. |
| Rapid expansion | Moderate | New territory lowers average control until integrated. |
| Aggressive bloc overreach | Moderate | Conquest without integration weakens control. |

### Local Control uses

| Surface | Use |
| --- | --- |
| Cores | Cores should require deep local control unless the state is a clear anchor. |
| Recruitment | Higher control improves manpower and militia conversion. |
| Industry | Construction decisions work better in high-control states. |
| Formables | Required regions should need ownership, control, and enough local control or integration work. |
| Host settlement | Host is less able to reclaim high-control states diplomatically. |
| League | High-control members contribute more to shared reserves. |
| Instability | High local control lowers instability over time. |

## Former Host Anger

Former Host Anger measures the political pressure inside the old host to reverse or punish the release. It is an aggregate value per host that reflects lost states, lost industry, ideology, army confidence, claims, border heat, humiliation, and domestic politics.

Former Host Anger should make hosts active without allowing them to erase every release automatically. High anger needs Reclamation Capacity to become dangerous. A furious host with no army should create diplomatic pressure, sabotage, or future missions. A strong angry host can become a real military threat.

### Former Host Anger bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Shock absorbed | Host can tolerate the release or has bigger problems. |
| 10 to 24 | Protest current | Host complains, claims, and creates diplomatic friction. |
| 25 to 44 | Organized pressure | Host can undermine recognition, fund loyalists, or demand talks. |
| 45 to 64 | Reclamation preparation | Host can prepare border forces, sanctions, ultimatums, or covert action. |
| 65 to 84 | National crisis | Host leadership faces pressure to reverse the loss. |
| 85 to 100 | Revenge mandate | Host can seek war or forced settlement if capacity allows. |

### Former Host Anger gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Losing states | Initial | Scales with state value, industry, resources, population, ports, and rail. |
| Losing a core or capital-adjacent state | High | Especially important. |
| Multiple releases from one host | Repeated | Prevent one host from being shredded without pressure. |
| Ambition package or maximal claims | High | Strong driver of host response. |
| Host ideology favors central control | Moderate | Fascist, communist, military, and imperial routes can be angrier. |
| Release accepts hostile patron | Moderate | Creates proxy framing. |
| Border Heat above militarized band | Repeated | Border pressure feeds domestic anger. |
| Aggressive bloc rhetoric or wars | High | Host anger should spike. |

### Former Host Anger losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Host settlement | High | Most direct reduction. |
| Recognition above treaty band | Moderate | Host loses diplomatic room. |
| Host exhaustion | Small repeated loss | Host cannot keep pressure alive. |
| Other wars or crises | Small to moderate | Host priorities shift. |
| Release gives economic concession | Small to moderate | A treaty can buy down anger. |
| League arbitration accepted | Moderate | Gives host a way to save face. |
| Host loses a reclamation conflict | High | Defeat can force acceptance. |

### Reclamation Capacity

Reclamation Capacity is the host's ability to act on anger.

| Capacity factor | Capacity direction |
| --- | --- |
| Strong army near border | Higher |
| Good stability and war support | Higher |
| Sufficient equipment and supply | Higher |
| Direct land border or port access | Higher |
| Major power status | Higher |
| Already in major war | Lower unless the release is a strategic rear crisis |
| Low stability or civil war | Lower |
| Host exhaustion | Lower |
| High foreign guarantees for release | Lower or riskier |
| Strong Independence League | Lower or riskier |

Host AI should only escalate to war when both anger and capacity are high enough, unless high chaos explicitly allows reckless behavior. A weak host can still choose covert or diplomatic pressure.

### Negotiation Willingness

Negotiation Willingness is the host's willingness to settle. It is not the opposite of anger. A host can be angry and still negotiate if it lacks capacity, fears the league, or wants economic concessions.

| Factor | Willingness direction |
| --- | --- |
| High release recognition | Higher |
| High release legitimacy | Higher |
| Host exhaustion | Higher |
| Strong league backing the release | Higher or lower depending on ideology |
| Release offers concessions | Higher |
| Release joined aggressive bloc | Lower |
| Host has high reclamation capacity | Lower unless it wants a favorable treaty |
| Host ideology favors compromise | Higher |
| Release holds host cores with low local control | Lower |

Negotiation should have real outcomes. A settlement can reduce Border Heat and Former Host Anger, raise Recognition, add claims or remove claims, create economic concessions, set demilitarized border missions, block immediate war, or open future settlement events.

### Host decision hooks

| Working host decision family | Purpose | Costs and risks |
| --- | --- | --- |
| Diplomatic protest campaign | Lower release Recognition, raise Border Heat | Political power, relations cost, can fail against recognized states. |
| Loyalist contact network | Raise release instability or lower local control | Intelligence exposure, condemnation risk if discovered by league. |
| Border guard mobilization | Raise Reclamation Capacity and deter release claims | Equipment, manpower, supply, Border Heat gain. |
| Economic pressure | Reduce release Foreign Support or industry | Trade cost, sponsor rivalry, league backlash. |
| Offer autonomy settlement | Reduce anger and heat, possibly regain influence | Domestic legitimacy or political cost for host. |
| Recognize independence | Ends or lowers dispute | Anger loss, host political cost, possible stability hit for hardline hosts. |
| Reclamation ultimatum | Force release choice | Requires high anger and capacity, risks war and league intervention. |
| Prepare reclamation war | Moves toward conflict | Equipment, command power, world tension or threat, league reaction. |

## Host Exhaustion

Host Exhaustion prevents endless host pressure. It rises when the host fails to reverse releases, loses border conflicts, faces other wars, loses stability, or sees many Event 6 releases survive with recognition.

High exhaustion should make settlements more likely and war less sustainable. It should not make the host harmless by itself. A hostile exhausted host can still sponsor loyalists, refuse recognition, or wait for another chance.

### Host Exhaustion gains

| Source | Gain direction |
| --- | --- |
| Failed reclamation ultimatum | Moderate |
| Lost border conflict | High |
| Multiple releases survive beyond a deadline | Moderate |
| Host is in a losing war | Moderate repeated gain |
| Host has low stability | Small repeated gain |
| League defense succeeds | High |
| Recognition of releases reaches treaty band | Moderate |

### Host Exhaustion losses

| Source | Loss direction |
| --- | --- |
| Host recovers stability and army strength | Small repeated loss |
| Host peacefully settles and stabilizes politics | Moderate |
| Host reconquers a release | Moderate |
| Host gains a strong sponsor against releases | Small to moderate |

Host Exhaustion should be visible to host players when they have Event 6 disputes. Released countries can see a simplified read of host pressure and exhaustion through decision category text or diplomacy decisions.

## League Cohesion

League Cohesion exists after enough Event 6 countries create an Independence League. Before formation, individual Coalition Trust and league contact flags prepare the path.

The league should not form from one country and a friend. It should need several surviving Event 6 releases, enough trust, enough recognition or shared danger, and a reason to cooperate. Host threats, patron competition, and border disputes all shape the path.

### League formation readiness

A league can form when most of these are true.

| Requirement type | Direction |
| --- | --- |
| Member count | Several Event 6 countries exist and are not puppets of the same patron. |
| Coalition Trust | A core group has reliable or better trust. |
| Recognition or common danger | Either enough recognition exists to claim diplomatic weight, or enough Host Anger and Border Heat exists to justify common defense. |
| Local survival | Members have at least thin local control and hollow or better legitimacy. |
| Patron condition | Patron Influence is not so high that every member is a proxy. |
| Border condition | Member border disputes are not all in open flashpoint. |

A defensive league can form at lower recognition if common danger is high. A diplomatic league needs more recognition and legitimacy. A federal or common-front league needs higher trust and cohesion.

### League Cohesion bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Broken league | The league is collapsing or exists only as a memory. |
| 10 to 24 | Paper league | Members share a name but little else. |
| 25 to 44 | Working forum | Arbitration, observer pacts, and small shared aid work. |
| 45 to 64 | Common front | Defensive plans, shared reserves, and coordinated recognition work. |
| 65 to 84 | League authority | The league can discipline members, coordinate wars, and lead settlements. |
| 85 to 100 | Federal horizon | Strong enough for rare federation, common command, or major super-event milestones. |

### League Cohesion gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Mutual recognition pact | Small to moderate | First diplomatic foundation. |
| Shared host threat | Small repeated gain | Common danger unites members. |
| League arbitration success | Moderate | Shows the league can solve disputes. |
| Shared reserve contributions | Moderate | Members invest resources. |
| Defensive victory for a member | High | Common defense proves value. |
| Balanced patron rules | Moderate | Keeps members from becoming proxies. |
| League focus branch completion | Moderate to high | Political route can build institutions. |

### League Cohesion losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Member joins aggressive bloc | High | Direct split. |
| Member accepts puppet status | Moderate to high | League trust in independence falls. |
| Failed arbitration | Moderate | Disputes damage authority. |
| Sponsor Rivalry above foreign struggle band | Small repeated loss | Sponsors divide members. |
| Member starts war against another member | High | Can cause immediate fracture. |
| League fails to defend a member | High | Common defense promise loses credibility. |
| Leadership dispute | Small to moderate | Can happen after successes or patron pressure. |

### League Authority

League Authority is the league's ability to make members follow decisions. Cohesion is emotional and political unity. Authority is institutional power.

| Authority source | Design direction |
| --- | --- |
| Formal charter focus | Raises authority and unlocks votes. |
| Shared command decision | Raises authority and military coordination, but some members lose autonomy. |
| Arbitration success | Raises authority. |
| Strong leader member | Raises authority if trusted, lowers trust if seen as domination. |
| Federal branch | Converts authority into possible formable or common government path. |
| Patron caucus | Can raise authority inside a patron bloc, but lowers independent cohesion. |

League Authority should unlock stronger shared decisions, such as shared reserves, common border commissions, joint defense missions, member sanctions, collective recognition campaigns, and rare federal formation routes.

### League shared decisions

| Working decision family | Purpose | Costs and risks |
| --- | --- | --- |
| Shared reserves | Move equipment, manpower, or working units to threatened members | Costs member stockpiles, trust, or league authority. |
| Common recognition mission | Improves recognition for several members | Requires cohesion and foreign access. |
| League arbitration panel | Lowers member border heat | Can fail and lower cohesion. |
| Joint border defense | Deters former host war | Equipment, command power, supply, risk of host anger. |
| Patron rules charter | Lowers patron capture and sponsor rivalry | Angers sponsors and client members. |
| Member sanction | Punishes aggressive or puppet member | Lowers trust with target, can cause exit. |
| Emergency membership vote | Adds threatened release quickly | Can lower cohesion if member is unstable. |

## Aggressive Bloc Pressure

Aggressive Bloc Pressure represents the high-chaos alternative to defensive cooperation. It is the force that pushes some Event 6 countries to treat the old map as a target rather than a problem to settle.

The aggressive bloc should not be a simple faction button. It should grow from high Border Heat, low Recognition, military confidence, radical routes, former host hostility, patron competition, and ambition packages. It can share some league mechanics, but its values point toward expansion, threat, and coercion instead of defensive legitimacy.

### Aggressive Bloc Pressure bands

| Range | Working band | Gameplay meaning |
| --- | --- | --- |
| 0 to 9 | Isolated hardliners | No coordinated bloc. |
| 10 to 24 | Maximalist circles | Some countries unlock hardline rhetoric and claim decisions. |
| 25 to 44 | Claim network | Countries can share claim support and border incidents. |
| 45 to 64 | War caucus | Members coordinate military preparation and reject settlements. |
| 65 to 84 | Aggressive bloc | A faction or faction-like bloc can form. |
| 85 to 100 | Partition engine | Super-event thresholds, major wars, and hidden formable routes become likely. |

### Pressure gains

| Source | Gain direction | Design note |
| --- | --- | --- |
| Border Heat above militarized band | Moderate repeated gain | Border danger feeds maximalism. |
| Former host uses threats or attacks | Moderate to high | Host hostility can radicalize releases. |
| Ambition package | High initial | Ambition releases are natural candidates. |
| Low Recognition with strong army | Moderate | Isolation plus strength favors force. |
| Patron arms without patron restraint | Moderate | Sponsors can empower hardliners. |
| Failed league arbitration | Moderate | Peaceful system looks weak. |
| High chaos evolution | Moderate to high | Evolutions IV and V should accelerate pressure. |
| Victory over host | High for some routes | Success encourages further claims. |

### Pressure losses

| Source | Loss direction | Design note |
| --- | --- | --- |
| Treaty recognition | Moderate | Settled status weakens maximalism. |
| League cohesion above common front | Moderate | Strong league can absorb hardliners. |
| Military defeat | High | Failed aggression discredits bloc. |
| Patron restraint or aid withdrawal | Moderate | Sponsors can cool pressure. |
| Border settlement | Moderate | Removes flashpoints. |
| High legitimacy civilian route | Small repeated loss | Institutions can resist war caucuses. |

### Aggressive bloc decisions

| Working decision family | Purpose | Costs and risks |
| --- | --- | --- |
| Claim coordination | Members support each other's claims | Raises Border Heat, lowers Recognition. |
| Border incident chain | Creates pressure on host or rival | Equipment, command power, instability risk. |
| War caucus preparation | Improves readiness and shared attack timing | Raises host anger and sponsor rivalry. |
| Punish settlement member | Pressures a member that accepted peace | Can cause fracture or war. |
| Maximalist formation route | Reveals hidden formable claims | Requires high pressure, territory, and route commitment. |
| Bloc arms pool | Shares foreign aid among hardliners | Raises Patron Influence and Sponsor Rivalry. |

### Aggressive bloc failure states

The aggressive bloc should be frightening when it works, but unstable when it overreaches.

| Failure pattern | Result direction |
| --- | --- |
| Pressure high and army weak | War caucus creates instability, coup risk, or failed mobilization. |
| Pressure high and recognition low | Foreign states refuse treaties, making aid more patron-heavy. |
| Pressure high inside league | League fracture, member sanctions, or bloc split. |
| Pressure high after defeat | Collapse of hardline route, host settlement, or radical revenge branch. |
| Pressure high with sponsor rivalry | Proxy crisis and super-event threshold if several members and sponsors are involved. |

## Interlocking values

The mechanics should interact constantly. A player should rarely be able to improve every value at once.

| Action pattern | Good result | Pressure created |
| --- | --- | --- |
| Accept a major arms shipment | Foreign Support rises, army improves | Patron Influence rises, Sponsor Rivalry can rise, Host Anger can rise. |
| Invite foreign observers | Recognition rises | Requires local control and time, can create patron foothold. |
| Crack down on disorder | Instability falls quickly | Legitimacy can fall, Border Heat can rise, local unrest events can appear. |
| Hold a public mandate process | Legitimacy rises | Takes time and can fail if instability is high. |
| Build border forts | Local defense improves | Border Heat and Host Anger rise. |
| Accept host settlement | Recognition rises, Border Heat falls | Maximalist support and Aggressive Bloc Pressure fall, some claims may be abandoned. |
| Join the league | Coalition Trust and support rise | League arbitration can limit expansion and patron autonomy. |
| Join aggressive bloc | Claims, readiness, and pressure rise | Recognition and Coalition Trust fall, Host Anger rises. |
| Balance several sponsors | Patron Influence from one sponsor falls | Sponsor Rivalry rises. |
| Form a larger country | Legitimacy and ambition rise | Local Control requirements, host anger, and integration pressure rise. |

## Dynamic drift and pulses

Values should move from actions first, then from periodic pulses. The event should not rely on passive drift alone.

A regular Event 6 pulse should only affect active Event 6 countries and their former hosts. The pulse should not iterate the world unnecessarily without a bounded implementation pattern. The design intent is a small active-country ledger, not a daily global scan.

### Released country pulse direction

| Condition | Drift direction |
| --- | --- |
| Local Control is much higher than Legitimacy | Legitimacy slowly rises. |
| Legitimacy is much higher than Local Control | Legitimacy slowly falls or Local Control missions become urgent. |
| Recognition is high and Patron Influence is low | Patron Influence slowly decays. |
| Foreign Support is high and Recognition is low | Patron Influence slowly rises. |
| Post-Release Instability is high | Legitimacy and Local Control slowly fall. |
| Border Heat is high and army is weak | Instability rises and host pressure events become more likely. |
| Coalition Trust is high with several nearby releases | League formation readiness rises. |
| Aggressive Bloc Pressure is high | Coalition Trust falls unless the country is already hardline. |
| Sponsor Rivalry is high | Patron Influence and instability risk rise, but Foreign Support opportunities can also rise. |

### Former host pulse direction

| Condition | Drift direction |
| --- | --- |
| Multiple releases survive with recognition | Host Exhaustion rises, Anger may fall slowly. |
| Border Heat remains high | Anger rises. |
| Reclamation Capacity is high and anger is high | Host escalation decisions become more likely. |
| Host is losing another war | Reclamation Capacity falls, Host Exhaustion rises. |
| Release accepts settlement | Anger and Border Heat fall, Negotiation Willingness can rise for other releases. |
| Aggressive bloc forms near host | Anger rises sharply and capacity can be redirected toward war. |

### League pulse direction

| Condition | Drift direction |
| --- | --- |
| Members have high Coalition Trust | League Cohesion rises. |
| Members have high Patron Influence from rival sponsors | Sponsor Rivalry rises and League Cohesion falls. |
| Members settle disputes through arbitration | League Authority rises. |
| Member wars or claim disputes exist | Cohesion falls, Aggressive Bloc Pressure can rise. |
| Former hosts threaten several members | Cohesion rises if members are not divided by patrons. |
| League fails to aid a member | Cohesion and Authority fall. |

## Focus hook map

The shared Independence Wave focus overlay should interact directly with the mechanics. Region and country inserts can change names, assets, and state targets, but the mechanical architecture should stay consistent.

| Focus family | Main values affected | Role |
| --- | --- | --- |
| Opening survival | Legitimacy, Instability, Local Control | Gives the country first tools to function. |
| Government formation | Legitimacy, Recognition, Patron Influence | Defines how the country claims authority. |
| Emergency army | Instability, Local Control, Border Heat | Creates early defense and militia integration. |
| Recognition diplomacy | Recognition, Foreign Support, Patron Influence | Opens foreign relations and settlement paths. |
| Economic footing | Local Control, Instability, Foreign Support | Repairs factories, rail, ports, and supply. |
| Host settlement | Border Heat, Recognition, Former Host Anger | Offers peace, concessions, or preparation. |
| League contact | Coalition Trust, League Cohesion | Moves from shared origin to cooperation. |
| League leadership | Coalition Trust, League Authority, Recognition | Lets strong members lead shared systems. |
| Patron alignment | Foreign Support, Patron Influence, Sponsor Rivalry | Makes aid powerful but dangerous. |
| Independent path | Legitimacy, Recognition, Patron Influence | Escapes sponsor capture and strengthens autonomy. |
| Regional ambition | Local Control, Border Heat, Legitimacy | Adds claims, integration, and formation preparation. |
| Aggressive maximalism | Aggressive Bloc Pressure, Border Heat, Recognition | Opens high-chaos claim and war routes. |
| Hidden formable preparation | Legitimacy, Local Control, Recognition or Aggressive Pressure | Reveals larger country decisions when earned. |

### Focus route tradeoffs

| Route | Gains | Loses or risks |
| --- | --- | --- |
| Civilian founding route | Legitimacy, Recognition, Instability reduction | Slower army growth, weaker immediate host deterrence. |
| Military emergency route | Local Control, army readiness, fast instability reduction | Recognition and legitimacy risk, higher Border Heat. |
| League route | Coalition Trust, League Cohesion, shared support | Less freedom for maximal claims, league obligations. |
| Patron route | Foreign Support, units, advisors, industry | Patron Influence, sponsor rivalry, possible puppet pressure. |
| Independent diplomacy route | Recognition, anti-puppet resilience | Slower aid, higher early vulnerability. |
| Regional formable route | Legitimacy and late-game ambition | Integration burden, host anger, local control requirements. |
| Aggressive bloc route | Claims, war readiness, high-chaos power | Recognition loss, league distrust, host war risk, overreach. |

### Focus gate examples

Working gates should be expressed through values, not only one-time flags.

| Focus type | Gate direction |
| --- | --- |
| Early government focus | Available at low legitimacy, stronger effect if legitimacy already disputed or better. |
| First recognition focus | Needs capital or anchor state control and instability below near breakdown. |
| League contact focus | Needs another Event 6 country and some Coalition Trust. |
| League formation focus | Needs multiple candidate members, trust, recognition or common danger, and no open member war. |
| Patron alignment focus | Needs a valid sponsor and low enough recognition or an ideological reason. |
| Anti-puppet focus | Needs Patron Influence above foothold or a sponsor demand event. |
| Border settlement focus | Needs Border Heat in disputed or higher bands and host negotiation willingness. |
| Maximal claim focus | Needs high chaos evolution, high Border Heat or Aggressive Pressure, and route lock. |
| Major formable focus | Needs local control, legitimacy, required territory path, and route unlock. |

## Decision hook map

The decision layer should be where the player actively manages the mechanics. It should stay readable by phases, selected targets, and route locks.

### Released country decision categories

| Working category | Values | When visible | Role |
| --- | --- | --- | --- |
| Independence administration | Legitimacy, Instability, Local Control | Every Event 6 country at release | Core survival decisions. |
| Recognition and sponsors | Recognition, Foreign Support, Patron Influence, Sponsor Rivalry | Once first government step completes or recognition path opens | Diplomacy, aid, anti-puppet work. |
| Border commission | Border Heat, Former Host Anger, Local Control | When border heat or claims exist | Host talks, border defense, disputed states. |
| League contact | Coalition Trust, League Cohesion | When at least two Event 6 countries exist and contact is possible | Cooperation, league formation, shared decisions. |
| Aggressive claims | Aggressive Bloc Pressure, Border Heat, Recognition | High chaos, hardline route, or high pressure | Maximalist claims and bloc action. |
| Formation projects | Legitimacy, Recognition, Local Control, Border Heat | Revealed by focus, region, route, or chaos | Formable decisions and integration work. |

### Decision families and value effects

| Working family | Primary value gain | Primary value cost or risk | Cost palette |
| --- | --- | --- | --- |
| Build provisional ministries | Legitimacy and Local Control | Civilian burden, time, possible instability if rushed | Civilian factories, political power, trains. |
| Secure rail administration | Local Control and instability loss | Equipment and construction burden | Infantry equipment, trains, civilian factories. |
| Integrate militias | Legitimacy and army readiness | Support equipment, army XP, failure can raise instability | Infantry equipment, support equipment, army XP. |
| Emergency guard deployment | Instability loss, border defense | Legitimacy loss if repeated, Border Heat gain | Command power, infantry equipment, manpower. |
| Recognition mission | Recognition | Patron foothold or diplomatic cost | Political power, convoys, local control, relations. |
| Arms request | Foreign Support and equipment | Patron Influence, Host Anger | Convoys, relations, recognition, patron debt. |
| Balanced sponsor conference | Patron Influence control | Sponsor Rivalry and time | Recognition, political power, stability. |
| Anti-puppet reforms | Patron Influence loss | Foreign Support loss, sponsor anger | Stability, political power, advisor removal. |
| Border arbitration | Border Heat loss | Coalition Trust risk if failed | Legitimacy, recognition, league authority. |
| Fortify border belt | Defense and local control | Border Heat and Host Anger | Infantry equipment, support equipment, factories. |
| Host settlement offer | Recognition and heat loss | Claims lost, legitimacy risk for hardliners | Political power, economic concessions, local control. |
| League shared reserves | Foreign Support and defense | League cohesion strain, member stockpile cost | Equipment, manpower, league authority. |
| Maximal claim push | Aggressive pressure and claims | Recognition loss, trust loss, host anger | Army XP, command power, equipment, local control. |
| Formation integration project | Local Control, cores, legitimacy | Resistance, instability, host anger | Equipment, manpower, stability, time, state control. |

### Decision phase control

The decision category should not show every possible action at once.

| Phase | Visible decision style |
| --- | --- |
| Opening survival | A small set of government, local control, militia, and recognition contact decisions. |
| Recognition phase | Sponsor and observer decisions appear, but high-tier aid is hidden until recognition or patron route opens. |
| Border phase | Border commission and host response decisions appear only when heat or host anger justify them. |
| League phase | League contact and shared decisions appear when enough Event 6 countries exist. |
| High-chaos ambition phase | Aggressive claims, hidden formables, and dangerous bloc decisions appear after route and evolution gates. |
| Settlement or aftermath phase | Obsolete emergency decisions close, integration and treaty maintenance decisions replace them. |

### Host decision categories

Former hosts need their own Event 6 response tools when they lose states.

| Working category | Values | Role |
| --- | --- | --- |
| Lost provinces response | Former Host Anger, Reclamation Capacity, Negotiation Willingness | Main host reaction category. |
| Reclamation preparation | Anger, Capacity, Border Heat | Military and coercive path. |
| Settlement channel | Negotiation Willingness, Host Exhaustion | Treaty, autonomy, recognition, concessions. |
| Counter-recognition | Release Recognition, Sponsor Rivalry | Diplomatic pressure and sponsor competition. |
| Loyalist networks | Release Instability and Local Control | Covert or political pressure. |

Host decisions should use the host's resources. A strong host spends equipment, command power, political power, supply, and stability. A weak host spends political capital and creates covert pressure, but should not create free armies or instant wars.

## Mission hook map

Missions should ask the player to prove statehood through action. Avoid passive stockpile checks unless the stockpile must be delivered, held in a state, or committed to a named project.

### Released country mission families

| Working mission family | Value focus | Objective style | Success | Failure |
| --- | --- | --- | --- | --- |
| Founding capital defense | Legitimacy, Local Control | Hold capital or anchor state for a deadline | Legitimacy gain, instability loss | Legitimacy loss, host confidence, emergency branch. |
| Rail and supply control | Local Control, Instability | Hold or repair named rail, port, or supply states | Control gain, economy unlock | Instability gain, aid delays. |
| Militia integration period | Legitimacy, Instability | Spend equipment and keep units supplied | Better templates, instability loss | Militia splinter, equipment loss, legitimacy hit. |
| Recognition observer window | Recognition | Keep route open and avoid high border heat | Recognition gain, aid options | Patron influence gain, recognition delay. |
| Host settlement deadline | Border Heat, Host Anger | Keep talks open while avoiding escalation | Heat loss, recognition gain | Heat and anger gain, ultimatum risk. |
| Border defense posture | Border Heat, Local Control | Place supplied divisions in border state group | Deterrence and control gain | Host capacity gain, local control loss. |
| League arbitration term | Coalition Trust, League Cohesion | Keep member dispute below heat threshold | Trust and cohesion gain | Trust loss, bloc pressure gain. |
| Aid corridor protection | Foreign Support, Patron Influence | Keep port, rail, or border corridor open | Support gain with lower influence | Support loss or higher patron debt. |
| Integration project | Local Control, Formable access | Hold and administer claimed states over time | Claims become cores or lower resistance | Instability and resistance rise. |

### Former host mission families

| Working mission family | Value focus | Objective style | Success | Failure |
| --- | --- | --- | --- | --- |
| Rally reclamation support | Anger and Capacity | Prepare army and border logistics | Capacity gain, ultimatum unlock | Host exhaustion or anger loss. |
| Diplomatic counter-recognition | Release Recognition | Build relations with powers or neighbors | Release recognition loss, sponsor rivalry | Host exhaustion gain, release recognition gain. |
| Border mobilization term | Capacity, Border Heat | Place supplied divisions near release | Reclamation threat | Border heat gain, cost burden, failure lowers capacity. |
| Settlement mandate | Negotiation Willingness | Keep domestic politics stable during talks | Settlement option | Anger gain, hardliner pressure. |
| Loyalist network operation | Release Instability | Covert support or political pressure | Release instability gain | Exposure, league backlash, sponsor rivalry. |

### Mission duration direction

Mission durations should vary by difficulty.

| Mission type | Duration direction |
| --- | --- |
| Opening capital defense | Medium, long enough for reaction. |
| Emergency crackdown | Shorter, but with clear cost and risk. |
| Recognition observer window | Medium to long, because diplomacy takes time. |
| Host settlement | Medium to long, with danger of interruption. |
| Border defense | Medium, tied to host escalation pace. |
| Integration project | Long, especially for non-anchor states. |
| League arbitration | Medium, enough time for member actions. |
| Aggressive bloc war preparation | Medium, but shorter at high chaos. |

## Visible presentation

The mechanics need a readable presentation layer from the first implementation pass. A richer scripted GUI can supplement normal surfaces, but this system requires values to be visible from the start.

### Required early presentation surfaces

| Surface | What it shows |
| --- | --- |
| Decision category header | Current Legitimacy, Recognition, Instability, Border Heat, and Local Control for the released country. |
| Recognition and sponsor category | Foreign Support, Patron Influence, and Sponsor Rivalry. |
| League category | Coalition Trust, League Cohesion, League Authority, and member state. |
| Host response category | Former Host Anger, Reclamation Capacity, Negotiation Willingness, and Host Exhaustion. |
| National spirit tooltips | Short explanation of how current values affect the country. |
| Focus tooltips | Which values the focus changes or requires, with hidden outcomes kept hidden. |
| Event detail view | Premise and state of the Independence Wave system, without listing mechanical effects. |
| Super-event direction files | Major thresholds only, not ordinary value movement. |

### Value colour direction

Final localisation can choose exact project colours, but the direction should stay consistent.

| Value | Colour identity direction |
| --- | --- |
| Legitimacy | Government authority and public mandate colour. |
| Recognition | Diplomatic or blue identity. |
| Foreign Support | Aid and supply identity. |
| Patron Influence | Foreign pressure or purple identity. |
| Coalition Trust | Cooperative or yellow identity. |
| Border Heat | Threat or red identity. |
| Post-Release Instability | Disorder or orange identity. |
| Local Control | Grounded control or green identity. |
| League Cohesion | Shared front identity, distinct from Coalition Trust. |
| Aggressive Bloc Pressure | Dark red or hardline pressure identity. |
| Former Host Anger | Host response identity, distinct from Border Heat. |
| Sponsor Rivalry | Proxy conflict identity. |

Tooltips should show cause and effect. A player should understand why a value rose or fell through public actions, not through hidden variable names.

### Compact UI panel direction

The decision and GUI file defines a compact Independence Wave panel for cases where normal decision headers become too dense.

The panel would show cards for:

1. Statehood: Legitimacy, Instability, Local Control.
2. Diplomacy: Recognition, Foreign Support, Patron Influence.
3. Borders: Border Heat, former host pressure, settlement state.
4. Cooperation: Coalition Trust, league state, sponsor rivalry.
5. Ambition: claims, formable readiness, aggressive bloc pressure when relevant.

Animated presentation is useful for warning states, league formation readiness, patron capture danger, and aggressive bloc pressure. Any final animation must use real frame-sheet assets and static fallbacks. Do not plan a final GIF or filter pulse as the implementation.

## Differences by release package tier

Release package tier should change how the same mechanics feel.

### Seed package

Seed countries are tiny and fragile.

| Mechanic | Tier behavior |
| --- | --- |
| Legitimacy | Starts low. Must prove basic government before ambitious routes. |
| Recognition | Starts near zero unless the tag is already well known. |
| Foreign Support | Small, often humanitarian or covert. |
| Patron Influence | Low at first, but emergency aid can quickly dominate. |
| Coalition Trust | Can rise quickly because seed countries need friends. |
| Border Heat | Moderate unless the anchor state is valuable or symbolic. |
| Instability | Very high. Early play focuses on survival. |
| Local Control | Low outside the anchor. |
| Host Anger | Usually low to moderate, unless the state is strategic. |
| Route access | Defensive, recognition, and league contact. Aggressive routes should be rare before high chaos. |

### Compact package

Compact countries are weak but playable.

| Mechanic | Tier behavior |
| --- | --- |
| Legitimacy | Disputed or near provisional. |
| Recognition | Some observer paths can open early. |
| Foreign Support | Aid can meaningfully change survival. |
| Patron Influence | Manageable unless aid is rushed. |
| Coalition Trust | Good early league candidates. |
| Border Heat | Important but not always dangerous. |
| Instability | High but solvable. |
| Local Control | Enough to begin state integration. |
| Host Anger | Moderate. |
| Route access | Normal shared tree, recognition path, first league work, limited border settlement. |

### Regional package

Regional countries can matter militarily and diplomatically.

| Mechanic | Tier behavior |
| --- | --- |
| Legitimacy | Can reach provisional quickly if local control is maintained. |
| Recognition | De facto contact should be possible with effort. |
| Foreign Support | Sponsors care more because the country has strategic depth. |
| Patron Influence | Significant risk due to larger aid packages. |
| Coalition Trust | Mixed. Regional countries can lead or intimidate smaller releases. |
| Border Heat | Usually disputed or militarized. |
| Instability | Moderate to high, linked to multiple states. |
| Local Control | State-aware integration matters. |
| Host Anger | Significant. |
| Route access | League leadership, border commission, regional ambition, first formable preparation. |

### Partition package

Partition countries reshape a section of a host.

| Mechanic | Tier behavior |
| --- | --- |
| Legitimacy | Can be decent if based on strong institutions, but fragile if borders are contested. |
| Recognition | Outside powers notice immediately. |
| Foreign Support | Strong sponsor offers appear. |
| Patron Influence | High risk. |
| Coalition Trust | Smaller releases may fear domination. |
| Border Heat | High by default. |
| Instability | Strong starting administration can lower instability, but multi-state disputes keep pressure. |
| Local Control | Starts mixed and needs integration. |
| Host Anger | High. |
| Route access | Host settlement, league leadership, aggressive route seeds, regional formables, sponsor rivalry. |

### Ambition package

Ambition countries are rare, dangerous, and often high-chaos.

| Mechanic | Tier behavior |
| --- | --- |
| Legitimacy | Can start high from myth, history, ideology, or force, but often contested. |
| Recognition | Starts mixed. Some powers fear it. Others want to exploit it. |
| Foreign Support | Large offers possible. |
| Patron Influence | High or rapidly rising. |
| Coalition Trust | Low unless the country uses a restrained league path. |
| Border Heat | Very high. |
| Instability | High, but some high-chaos routes can weaponize it. |
| Local Control | Enough to fight, not enough to integrate without work. |
| Host Anger | Very high. |
| Route access | Hidden formables, maximal claims, aggressive bloc, strong super-event thresholds. |

## Differences by chaos evolution

The same values should exist from the baseline, but later evolutions change intensity, available decisions, and routes.

### Baseline: First petitions

Baseline waves release three countries and keep mechanics simpler.

| Mechanic | Baseline behavior |
| --- | --- |
| Legitimacy | Central early value. |
| Recognition | Slow and limited. |
| Foreign Support | Small and mostly basic. |
| Patron Influence | Exists, but major capture crises are rare. |
| Coalition Trust | Contact value only, usually no full league. |
| Border Heat | Host protest and limited reclamation preparation. |
| Instability | Major early problem. |
| Local Control | Anchor-state integration. |
| Host Anger | Present but often diplomatic. |
| Aggressive Pressure | Normally dormant. |

### Evolution I: Dossier surge

| Mechanic | Evolution I behavior |
| --- | --- |
| Legitimacy | Dossier and legal continuity decisions improve early gains. |
| Recognition | Observer and petition evidence paths open. |
| Foreign Support | Small support missions become common. |
| Patron Influence | First sponsor footholds. |
| Coalition Trust | Observer contacts between releases. |
| Border Heat | Host negotiation and border claim missions appear. |
| Instability | Slightly easier to reduce for prepared releases. |
| Local Control | Compact packages make control more achievable. |
| Host Anger | More structured response choices. |
| Aggressive Pressure | Rare, mostly from high heat cases. |

### Evolution II: Cascading petitions

| Mechanic | Evolution II behavior |
| --- | --- |
| Legitimacy | Shared examples raise legitimacy for some new releases. |
| Recognition | Multi-country recognition efforts appear. |
| Foreign Support | Patron outreach becomes a real system. |
| Patron Influence | Client risk becomes important. |
| Coalition Trust | League preparation begins. |
| Border Heat | Multi-host and multi-release disputes appear. |
| Instability | Region decisions can reduce disorder differently. |
| Local Control | State groups and logistics matter more. |
| Host Anger | Host response scales across several releases. |
| Sponsor Rivalry | Starts to matter in active regions. |

### Evolution III: Border commission crisis

| Mechanic | Evolution III behavior |
| --- | --- |
| Legitimacy | Border outcomes affect legitimacy strongly. |
| Recognition | Recognition depends on restraint or defensive success. |
| Foreign Support | Arms and volunteer channels grow. |
| Patron Influence | Sponsor-backed border claims become risky. |
| Coalition Trust | Arbitration can raise or break trust. |
| Border Heat | Becomes central. |
| Instability | Defeat or failed arbitration can destabilize governments. |
| Local Control | Disputed states need integration missions. |
| Former Host Anger | Can move into reclamation preparation. |
| Aggressive Pressure | First real hardline route seeds. |

### Evolution IV: Great partition week

| Mechanic | Evolution IV behavior |
| --- | --- |
| Legitimacy | Major countries can reach accepted mandate through route success. |
| Recognition | League and formable recognition become major goals. |
| Foreign Support | Large aid packages and sponsor rivalry become common. |
| Patron Influence | Client state crises become common. |
| Coalition Trust | Full league formation path opens. |
| Border Heat | Host crises can span regions. |
| Instability | Some packages are strong but politically volatile. |
| Local Control | Integration and formable projects become central. |
| League Cohesion | Full league mechanic is active. |
| Aggressive Pressure | High-chaos and ambition releases can organize. |
| Sponsor Rivalry | Can threaten league fracture. |

### Evolution V: Open season

| Mechanic | Evolution V behavior |
| --- | --- |
| Legitimacy | Normal legitimacy can be bypassed by hardline power, but the bypass is dangerous. |
| Recognition | Settled diplomacy is harder for maximalist states. |
| Foreign Support | Powerful aid can flood in. |
| Patron Influence | Proxy capture and sponsor demands are severe. |
| Coalition Trust | Defensive trust is harder unless the league is already strong. |
| Border Heat | Very high across many releases. |
| Instability | Some routes weaponize instability, others risk collapse. |
| Local Control | Rapid expansion without integration becomes a central risk. |
| League Cohesion | League can become a major actor or fracture. |
| Aggressive Pressure | Full aggressive bloc formation path. |
| Sponsor Rivalry | Proxy crisis and super-event thresholds. |

## AI behavior

AI must understand the mechanics well enough that Event 6 countries do not all behave the same.

### Released country AI archetypes

Each Event 6 country should receive an AI leaning at release. The leaning can change when values change.

| AI archetype | When it fits | Preferred values | Avoids |
| --- | --- | --- | --- |
| Survivor | Seed or weak compact release, low army, high instability | Legitimacy, Local Control, Instability reduction | Aggressive claims, expensive patron conflicts. |
| Recognition seeker | Moderate legitimacy, accessible diplomacy, not at war | Recognition, host settlement, anti-puppet safeguards | High Border Heat and aggressive bloc. |
| League builder | Nearby Event 6 countries, high trust, shared host threat | Coalition Trust, League Cohesion, shared reserves | Patron capture and member disputes. |
| Patron client | Low recognition, high threat, valid strong sponsor | Foreign Support, Patron route | Anti-puppet reforms and neutral balancing. |
| Balanced sponsor player | Several sponsors available, moderate recognition | Support without capture | Single sponsor dominance. |
| Border defender | High host anger, moderate army, defensive route | Local Control, forts, deterrence | Offensive maximalism unless high chaos. |
| Border revanchist | High Border Heat, ambition package, strong army | Claims, border incidents, aggressive pressure | Host settlement and league limits. |
| Hidden formable seeker | Required territory possible, high legitimacy or high pressure | Local Control, route claims, formation projects | Random wars that block integration. |
| High-chaos maximalist | Evolution IV or V, strong army, low recognition, high heat | Aggressive Bloc Pressure, claims, war preparation | Defensive league arbitration. |

### Released country AI value priorities

| Situation | AI priority |
| --- | --- |
| Instability above severe band | Stabilize unless high-chaos route can exploit it. |
| Legitimacy below hollow band | Government and capital missions first. |
| Local Control below contested band | Local administration and rail missions first. |
| Recognition below observed band and host heat low | Recognition missions. |
| Patron Influence above client danger | Anti-puppet reforms if independence route, or client route if patron AI. |
| Border Heat above reclamation crisis | Defense, settlement, league call, or aggressive mobilization based on archetype. |
| Coalition Trust high with enough countries | League contact and formation. |
| Aggressive Pressure high and army strong | Bloc decisions and maximal claims. |
| Aggressive Pressure high and army weak | Stabilize or seek patron arms before escalation. |

### Former host AI archetypes

| Host archetype | When it fits | Behavior |
| --- | --- | --- |
| Absorbed host | Low anger, low capacity, other crises | Protest lightly or ignore. |
| Legal protest host | Democratic or weak military, moderate anger | Counter-recognition, settlement, economic claims. |
| Reclamation planner | High anger and capacity | Border mobilization, ultimatums, war preparation. |
| Covert pressure host | Moderate anger, weak direct capacity | Loyalist networks, sponsor competition, instability actions. |
| Settlement host | High exhaustion, high release recognition | Treaty, concessions, recognition, border guarantees. |
| Revenge host | High chaos, very high anger, strong army | War risk, aggressive response, pressure on league. |

### Sponsor AI

Sponsors should not throw aid at every release.

| Sponsor condition | Behavior |
| --- | --- |
| Ideological match with release | More likely to offer aid and advisors. |
| Rival sponsor active nearby | More likely to compete, raising Sponsor Rivalry. |
| Former host is rival | More likely to recognize and arm release. |
| Former host is ally | More likely to pressure release toward settlement or refuse recognition. |
| Release has high legitimacy and recognition | More likely to formalize aid, lower influence gain. |
| Release has low legitimacy and high instability | More likely to demand influence in exchange for aid. |
| Release joins aggressive bloc | Sponsors divide between exploiting it, restraining it, or opposing it. |
| League has high authority | Sponsors may work through league rules or try to split the league. |

### League AI

League AI should prefer survival and cooperation unless dominated by hardliners.

| League state | AI behavior |
| --- | --- |
| Low cohesion | Avoid major wars, prioritize arbitration and recognition. |
| Common front cohesion | Share reserves with threatened members. |
| High authority | Enforce arbitration and patron rules. |
| Sponsor rivalry high | Attempt neutral conference or risk caucus split. |
| Aggressive pressure rising | Sanction, expel, appease, or split depending on leadership. |
| Member under host attack | Aid if cohesion and capacity allow. Failure should matter. |

## Failure states

Failure states should create play, not only punishment. A failed released country can become a client, emergency military state, host protectorate, league ward, aggressive radical state, or collapsed government that another actor exploits.

### Released country failure states

| Failure state | Trigger direction | Result direction |
| --- | --- | --- |
| Government breakdown | Legitimacy very low and Instability very high | Emergency route, leader replacement, militia split, or host-backed settlement. |
| Patron capture | Patron Influence very high with low legitimacy or high aid dependency | Client route, puppet pressure, sponsor leader, faction entry. |
| Host reclamation crisis | Border Heat and Host Anger high with host capacity | Ultimatum, border war, league call, or settlement. |
| Local control failure | Local Control very low in key states | Resistance, lost recruitment, integration rollback, host loyalist events. |
| Recognition collapse | Recognition low after aggressive action or defeat | Aid becomes covert, patron influence rises, league trust falls. |
| League expulsion | Coalition Trust very low after member betrayal | Loss of shared reserves and possible aggressive bloc path. |
| Aggressive overreach | Aggressive Pressure high with defeat or low local control | Instability spike, hardline coup, host counteroffensive, sponsor withdrawal. |
| Formable failure | Formation attempted with weak local control or legitimacy | Integration crisis, claims delayed, border heat increase. |

### Former host failure states

| Failure state | Trigger direction | Result direction |
| --- | --- | --- |
| Exhausted host | Host Exhaustion high and capacity low | Settlement path, reduced anger, recognition of some releases. |
| Humiliated host | Failed reclamation war | Domestic crisis, anger spike then exhaustion, possible regime route if later implemented. |
| Overextended host | Too many release disputes at once | Must prioritize targets, some disputes freeze or settle. |
| Diplomatic isolation | Counter-recognition fails against high recognition releases | Host loses pressure tools and gains exhaustion. |
| League deterrence failure | Host challenges strong league and loses | League cohesion rises, host exhaustion rises, super-event threshold possible. |

### League and bloc failure states

| Failure state | Trigger direction | Result direction |
| --- | --- | --- |
| League fracture | Cohesion very low, member wars, sponsor rivalry | League dissolves, members choose independence, patron caucus, or aggressive bloc. |
| Paper league | Cohesion low but not broken | Only weak decisions remain. No super-event. |
| Patron split | Sponsor Rivalry high inside league | Member caucuses, expulsion risk, client bloc route. |
| Aggressive bloc collapse | Military defeat or pressure crash | Members return to league, become isolated, or fall into host settlements. |
| Aggressive bloc victory spiral | Pressure high and victories repeated | Major super-event threshold and stronger claims. |

## Cleanup rules

Cleanup needs to be designed from the start because Event 6 is repeatable and tags can overlap with other event systems.

### Country cleanup

| Situation | Cleanup direction |
| --- | --- |
| Event 6 country is annexed | Clear active decision categories, missions, league membership, sponsor target data, and active border disputes. Keep history flags needed for event log and achievements. |
| Event 6 country becomes a puppet by route | Keep Event 6 values, but switch to client rules. Some independent decisions close. |
| Event 6 country forms a larger country | Transfer or transform Event 6 values into the formable package. Clear obsolete release package flags. |
| Event 6 country loses all Event 6 states but survives elsewhere | Trigger emergency relocation or collapse logic if valid. Do not silently leave broken mechanics. |
| Tag exists without Event 6 origin | Do not load Event 6 focus overlay or decisions. |
| Same tag is released again by Event 6 | Use prior Event 6 memory to prevent duplicate one-time rewards, then reinitialize active values carefully. |
| Same tag later appears through Soviet Collapse | Soviet Collapse origin content must win for that release path. Event 6 origin data must not leak into it. |

### Host cleanup

| Situation | Cleanup direction |
| --- | --- |
| All releases from a host are gone | Close host response category after any aftermath or reclamation settlement resolves. |
| Host recognizes all active releases | Clear or freeze reclamation tools, keep treaty maintenance if designed. |
| Host is annexed | Clear host response missions and retarget disputes only if a successor route explicitly exists. |
| Host capital would be lost by release package | Shrink release package before release. Never rely on cleanup to fix host deletion. |
| Host enters a different major event crisis | Event 6 pressure can pause, reduce, or transform if that crisis is more important. Do not leave impossible missions active. |

### League cleanup

| Situation | Cleanup direction |
| --- | --- |
| League drops below minimum members | Downgrade to contact network or dissolve after grace period. |
| League leader annexed | Leadership vote or emergency successor. |
| Member becomes invalid | Remove from member lists, shared reserves, votes, and target arrays. |
| Member joins aggressive bloc | Remove or mark as hostile depending on league rules. |
| League becomes formable or federation | Convert league values into new formable or faction package. |
| Sponsor caucus splits the league | Separate member lists and close incompatible decisions. |

### Sponsor cleanup

| Situation | Cleanup direction |
| --- | --- |
| Sponsor capitulates or no longer exists | Aid channel decays, Patron Influence can remain as institutional memory, active missions close. |
| Sponsor becomes ally of former host | Aid decisions close or transform into settlement pressure. |
| Sponsor becomes enemy of release | Patron Influence becomes subversion pressure. |
| Release rejects sponsor | Clear active sponsor missions after costs and consequences resolve. |
| Multiple sponsors become one side of a war | Sponsor Rivalry recalculates and may collapse into patron dominance. |

### State cleanup

| Situation | Cleanup direction |
| --- | --- |
| State leaves release control | Local control for that state drops or freezes, integration missions cancel. |
| State becomes core through integration | Remove working local control penalties and claims if appropriate. |
| State is ceded in settlement | Remove release integration missions and adjust legitimacy or recognition according to treaty. |
| State is claimed by multiple Event 6 countries | Keep one dispute record and route it through arbitration or border heat, not duplicated missions. |

## Exploit prevention

Event 6 can create many tags, claims, units, and decisions. It needs clear guardrails.

| Exploit risk | Prevention direction |
| --- | --- |
| Releasing the same tag repeatedly for free units | Event 6 origin memory, one-time unit packages, scaled reopening packages, and cleanup of old rewards. |
| Farming recognition through repeated sponsors | Recognition gains should have diminishing returns by sponsor and route. |
| Accepting aid then instantly removing influence | Anti-puppet reforms should cost time, support, stability, or sponsor anger. |
| Free unit loops from militia integration | Unit decisions need equipment, manpower, cooldowns, local control, and one-time state flags. |
| Core spam through formables | Cores require local control, integration missions, route gates, and state group checks. |
| War goal spam through aggressive bloc | Claim and war decisions need pressure, cooldowns, target validity, and escalating costs. |
| Host deletion by release packages | Host survival shrink happens before release. Capital retention is preferred. |
| League shared reserve farming | Reserve transfers consume real member stockpiles or limited league pool. |
| Sponsor rivalry infinite aid | Rivalry can open aid choices, but usable Foreign Support should cap and patron risks should rise. |
| Puppet abuse | Puppet status should close independent route decisions and alter league membership. |
| Switching route to collect all rewards | Route locks and cleanup remove incompatible decisions, ideas, claims, and AI plans. |
| Dead sponsor or dead host decisions | Target validity gates and cleanup remove actions. |
| Existing country tree replacement | Load Event 6 overlay only when Event 6 created or reactivated the tag with origin flag. |
| Aggressive bloc joining and leaving for claims | Claims should be tied to route commitment, cooldowns, and diplomatic costs. |

## Achievement and super-event hooks from mechanics

Achievements and super-events use the mechanic thresholds defined here.

| Hook | Mechanic threshold direction |
| --- | --- |
| Defensive league formation super-event | League Cohesion and Authority high, enough members, enough territory or threat. |
| Aggressive bloc super-event | Aggressive Bloc Pressure high, several members, serious host or regional threat. |
| Great partition shock super-event | Many releases in one wave, multiple hosts, high host anger, high chaos. |
| League survival achievement | League survives host war with cohesion above common front and no member puppet collapse. |
| Anti-puppet achievement | Country reaches treaty recognition with Patron Influence below foothold. |
| Host settlement achievement | Country resolves border heat through treaty without war and keeps local control. |
| Maximalist route achievement | Country forms a high-chaos formable through aggressive bloc pressure and survives the backlash. |
| Restoration or regional formable achievement | Country reaches required local control, legitimacy, and territory through Event 6 origin. |
| Former host recovery achievement | Host survives multiple releases without losing capital and settles or reverses disputes under rules. |

## Acceptance criteria for mechanics

The mechanic design is complete when the implementation agent can answer these questions without inventing the mechanic design.

1. What values does an Event 6 country track.
2. What values does a former host track.
3. What values does the Independence League or aggressive bloc track.
4. What range and threshold bands apply to each value.
5. How release package tier changes initial values.
6. How chaos evolution changes mechanic intensity and route availability.
7. What actions raise and lower Legitimacy.
8. What actions raise and lower Recognition.
9. What actions raise and lower Foreign Support and Patron Influence.
10. What actions raise and lower Coalition Trust and League Cohesion.
11. What actions raise and lower Border Heat and Former Host Anger.
12. What actions raise and lower Post-Release Instability and Local Control.
13. How Sponsor Rivalry changes patron behavior and league risk.
14. How focus branches should hook into mechanics.
15. How decisions and missions should manage mechanics.
16. How AI countries should choose routes and actions.
17. What failure states exist.
18. What cleanup rules prevent stale mechanics.
19. What exploit risks need guardrails.
20. Which thresholds feed super-event and achievement preparation.
