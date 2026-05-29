# Event 6: Independence Wave Focus Trees

This file defines focus-tree architecture for countries released by Event 6. It must not become a focus-by-focus blueprint, a coordinate map, or a numbered list of final focuses. The implementation agent should create the exact in-game focus count, names, layout, prerequisites, rewards, and AI weights from the route architecture below.

## Core rule

Event 006 and Event 005 are separate standalone systems. The same tag can appear through more than one event, but its mechanics must follow its release origin. Event 006 must never turn a release into part of the Soviet Collapse system.

- `independence_wave` gives the country the Independence Wave tree or a package-specific Independence Wave overlay.
- `soviet_collapse` gives the country the Soviet Collapse tree or package content from Event 005.
- A shared tag such as Volga Bulgaria can exist in both systems, but the tree, decisions, startup ideas, route locks, event logs, and formable routes are different.
- Event 006 focus content must not require Event 005 missions, Event 005 variables, republic focus trees, Event 005 route states, Event 005 collapse progress, or Event 005 country package flags.
- If Event 006 releases a Soviet republic style tag, a Volga package, a Caucasus package, a Central Asian package, or any other tag that Event 005 can also touch, the country remains an Independence Wave release. It receives Event 006 provisional state-building content, not Event 005 republic content.

## Standalone Soviet-region release rule

Soviet-region geography does not imply Soviet Collapse mechanics. Event 006 may target the Soviet Union, Russia, a Soviet successor, a post-Soviet host, or a region that Event 005 can also affect only because that host satisfies normal Independence Wave targeting. The result is still Event 006 content.

If Event 006 releases Ukraine, Belarus, Kazakhstan, Armenia, Georgia, Azerbaijan, any other Soviet republic style tag, Volga Bulgaria, Old Great Bulgaria, or another shared tag, the implementation must:

- set and check `chaosx_release_origin_independence_wave`
- load only the Liberation Provisional Tree, a compact Event 006 subset, or an Event 006 package overlay
- block Event 005 tree loaders, republic branches, collapse missions, collapse decisions, collapse startup ideas, collapse event-log states, and collapse package variables
- use Event 006 legitimacy, recognition, patron, coalition, border, formable, GUI, and package variables
- treat the old owner as the Independence Wave host, not as a Soviet Collapse parent

If Event 005 released the same tag earlier, Event 006 must not overwrite it with Independence Wave focus content unless a separate additive integration is explicitly designed. If Event 006 released the tag earlier, Event 005 must not convert it into a Soviet Collapse participant by tag name alone. Origin flags decide all event-specific content.

Old Great Bulgaria and Volga Bulgaria therefore need origin-separated packages:

| Origin | Tree family | Meaning |
| --- | --- | --- |
| Event 005 Soviet Collapse | Event 005 collapse package | republic-collapse or successor-state content from that event |
| Event 006 Independence Wave | Event 006 historical-return overlay | old-state memory revived through petitions, archives, recognition, patron pressure, league politics, and Volga-Kama state-building |

The Event 006 version must have different route names, different starting problems, different decision families, different formable checks, and different AI behavior from the Event 005 version. Generic utility helpers may be shared only when they are truly event-neutral and do not pull a country into the wrong event system.

## Design contract

The tree must do six jobs.

| Job | Design meaning | Player-facing result |
| --- | --- | --- |
| Make a new state playable | The country needs immediate problems and tools | Recognition, army, budget, legitimacy, loyalists, host anger |
| Support many tags | The same architecture must work for ordinary releasables and custom packages | Generic trunk plus package overlays |
| Let routes diverge | Government identity changes how the country survives | Civic, officer, revolutionary, nationalist, patron, anti-patron, historical-return, local-polity, and strange routes |
| Let repeated waves matter | Earlier breakaways can help later ones | Congress, guarantees, volunteers, league, arbitration |
| Scale with chaos | Higher chaos releases more states and unlocks more unusual trees | Historical-return and local-polity overlays arrive late |
| Keep high chaos special | Strange branches should be hidden and earned | Necromantic, anti-mankind, archive-state, and rail-state modules appear only after conditions justify them |

Do not replace this with a small linear tree. Do not force every release through the same political reward chain.


## Host survival boundary

Focus content may add claims, demands, border commissions, pressure events, or later war goals, but it must not retroactively make the original Event 006 wave take every state from a host. The release origin creates a surviving host and a new breakaway. The tree can let the breakaway pursue more land afterward through normal gameplay, but the first wave must leave the host with at least one state.

Package overlays should therefore support reduced starting borders. A historical-return country can begin with a small core foothold, then use its overlay to seek recognition, archives, claims, federations, or border revisions later.

## Tree shape

The intended tree is a modular lane map.

| Lane | Opens from | Main route role | Can converge into | Hidden or restricted variants |
| --- | --- | --- | --- | --- |
| Provisional opening | release setup | Create legitimacy, budget, militia ledger, first diplomacy | First Sovereignty Congress | tiny-state emergency subset |
| Civic legitimacy | Local Charter path | elections, councils, rights, observers, recognition | Recognized Nation, League Charter | protected observer variant after repression |
| Military survival | Militia Congress path | depots, brigades, officer staff, defensive belt, emergency rule | Armed Independence, crisis recovery | loyalist conflict variant |
| Revolutionary committee | radicalization and left sponsor logic | workshop militias, commune supply, volunteers, police purge | Armed Independence, radical league | communist sponsor variant |
| National directorate | claim ambition and border grievance | emergency broadcast, youth battalions, border memory, claims | Armed Independence, border revision | high-chaos irredentist variant |
| Patron cabinet | foreign attention and sponsor leverage | loans, advisers, embassies, staff missions, puppet pressure | Dependent State Charter or anti-patron recovery | rival patron variant |
| Anti-patron struggle | high patron leverage or exposed brokers | counter agents, broker exposure, debt escape, league protection | Recognized Nation or League Charter | failed anti-patron crisis |
| Historical-return overlay | high chaos and package type | old institutions, archives, treaty claims, symbols, old capitals | modern restoration or mythic escalation | package-specific hidden branch |
| Local-polity overlay | high chaos and package type | land congress, traditional authority, protectorate dispute, community defense | recognized local state or protected autonomy | land war branch |
| Coalition congress | previous breakaways alive | congress, supply board, volunteers, guarantees, arbitration | League of New States | patron-dominated congress variant |
| Border commission | claim ambition or host settlement | surveys, petitions, arbitration, protected transfers, ultimatums | integrated districts, border war route | nationalist escalation variant |
| Crisis branch | failed stability, loyalists, capital loss, patron betrayal | broken charter, emergency session, cabinet rebuild, street defense | recovery, military rule, patron dependency | capital exile variant |
| Strange modules | very high chaos | necromancy, anti-mankind, archive state, impossible diplomacy | strange coalition or world-threat hooks | hidden until conditions are met |

The visible tree should start with a compact shared trunk. It then splits into political identity, survival, economy, diplomacy, coalition, border, and package lanes. High-chaos modules should remain hidden during ordinary low-chaos campaigns.

## Focus filter taxonomy

| Filter tag | Meaning | Main branches |
| --- | --- | --- |
| political | government form, legitimacy, elections, route locks | provisional charter, democratic mandate, radical seizure, patron cabinet |
| internal_faction | militias, officers, loyalists, secret cells, councils | militia congress, officer bloc, civil committee, loyalist crisis |
| industry | factories, repair, taxation, resources | emergency budget, war workshops, civic reconstruction |
| army | templates, defense, command, equipment | militia drills, depot seizure, defensive belt |
| diplomacy | recognition, guarantees, volunteers, faction rules | recognition mission, small-state congress, patron negotiations |
| intelligence | infiltration, counterintelligence, puppet pressure | liaison screens, counter agents, expose brokers |
| expansion | claims, demands, border commissions, wars | border survey, greater claim, ultimatum draft |
| package | historical-return or local-polity identity | old archive, land congress, treaty memory, royal or council legitimacy |
| special_mechanic | event variables | sovereignty ledger, coalition board, patron ledger, pressure register |
| high_chaos | strange doctrine and impossible-state routes | unmarked congress, grave census, human renunciation |
| crisis | civil war, capital loss, betrayal | emergency session, broken charter, last recognition bid |
| late_game | faction leadership and regional order | league presidency, charter of small nations, final doctrine vote |

## Shared opening lane

### Narrative role

The new country does not begin as a finished state. It begins as a committee, council, emergency cabinet, military staff, old archive society, local authority, or municipal board trying to become a state before the host reverses the result.

### Mechanical role

The opening lane should:

- create the legitimacy ledger
- create the budget spirit
- unlock basic army decisions
- reveal host anger and loyalist risk
- set the release-origin flag
- set package type
- route the country into generic or package overlay content
- open first recognition options

### Rough focus groups

Use focus groups rather than fixed focus lists.

| Group | Story purpose | Gameplay purpose |
| --- | --- | --- |
| Provisional council | who claims authority | legitimacy, route hints, early political power |
| Petition archive | why the state exists | legitimacy from host mistakes or old identity |
| Barracks count | what soldiers are available | templates, equipment, manpower scaling |
| Emergency budget | how the state pays for survival | temporary construction, consumer goods, repair |
| Border communications | how the outside world hears about it | foreign attention, recognition decisions |
| Host anger ledger | what the old state might do | suppression memory, loyalist risk, war warning |

### Anchor names the implementation may use

These are optional names, not a fixed list:

- Summon the Provisional Council
- Read the Separation Petition
- Count the Barracks
- Emergency Budget Session
- Foreign Reporters at the Border
- Guard the Radio Station
- Open the First Depot
- Repair the Rail Yard
- Publish the Host Reply
- First Sovereignty Congress

### Reward style

Rewards should be small but meaningful. The opening should not instantly solve the country.

Good rewards:

- temporary legitimacy
- political power
- small infantry equipment grant
- temporary repair speed
- one or two weak militia divisions when justified
- unlocks for decisions
- recognition progress
- reduced host retaliation chance

Bad rewards:

- huge free armies at low chaos
- instant industry from nothing
- full recognition without route investment
- claims before the border route opens

## Government route family

Government routes should split early and shape the country for the rest of the tree.

### Civic councils path

A democratic or civic route built around elections, town councils, observers, civil rights, recognition, and league diplomacy.

Major groups:

- provisional charter
- local elections
- protected observers
- civil service rebuild
- rights of minorities and municipalities
- recognized nation
- league charter support

Rewards:

- stability
- legitimacy
- recognition
- lower patron leverage
- better coalition cohesion
- weaker emergency army bonuses

AI:

- preferred by democratic candidates, low radicalization candidates, observer-protected releases, and candidates with high foreign attention.

### Officer mandate path

A military emergency route built around survival, staff offices, depots, defensive belts, and martial law.

Major groups:

- officer emergency committee
- command register
- depot discipline
- fortify the capital road
- national guard statute
- emergency rule review

Rewards:

- division organization
- defense on core territory
- equipment capture
- war support
- militia templates
- stability cost if prolonged

AI:

- preferred when at war, near hostile host divisions, low manpower, or high loyalist risk.

### Revolutionary committee path

A radical route built around workshop militias, old police purges, communes, ideological volunteers, and sponsor links.

Major groups:

- committee seizure
- workers arms board
- purge host police files
- revolutionary schools
- foreign volunteers
- radical league debate

Rewards:

- militia strength
- recruitable population factor
- cheaper infantry equipment production
- radicalization increase
- diplomatic penalties with hostile ideologies

AI:

- preferred by communist or high-radicalization candidates, especially after violent suppression.

### National directorate path

A nationalist route built around border memory, claims, youth battalions, emergency broadcasts, and old grievance politics.

Major groups:

- directorate proclamation
- border memory office
- youth battalions
- heroic dead propaganda
- claim register
- ultimatum debate

Rewards:

- war support
- claim ambition
- attack or planning bonuses
- faster border dispute escalation
- lower coalition cohesion if uncontrolled

AI:

- preferred by fascist or non-aligned candidates, high claim ambition, and candidates with lost cores or border claims.

### Patron cabinet path

A survival route built around foreign loans, advisers, recognition, military missions, and puppet pressure.

Major groups:

- emergency loan office
- foreign adviser mission
- embassy corridor
- patron cabinet seats
- base-rights controversy
- dependent state charter

Rewards:

- equipment
- recognition
- guarantees
- industrial aid
- patron leverage
- autonomy danger

AI:

- preferred by weak candidates with high foreign attention, low army strength, and nearby rival patrons.

### Anti-patron recovery path

This path opens if patron leverage becomes dangerous.

Major groups:

- expose foreign brokers
- debt audit
- counterintelligence screens
- league protection appeal
- buy back the rail depots
- cabinet without masters

Rewards:

- lower patron leverage
- autonomy recovery
- intelligence bonuses
- possible loss of foreign equipment flow

AI:

- preferred by civic, league, and nationalist routes when patron leverage crosses a danger threshold.

## Historical-return overlay framework

Historical-return overlays appear only at higher chaos. They should not replace the tree. They add a package lane that changes legitimacy, claims, symbols, and route flavor.

### Shared historical-return groups

| Group | Purpose | Reward style |
| --- | --- | --- |
| Open the old archive | prove that the name has memory | legitimacy, package flag, localisation variant |
| Convene the restoration council | decide modern or old-state framing | route lock toward civic restoration, monarchic council, directorate, or mythic branch |
| Recover old symbols | flags, seals, rituals, documents | national spirit, assets, advisor unlocks |
| Name the border memory | decide claims or restraint | claim ambition or recognition |
| Modern state compromise | keep the old name but govern as a modern state | stability and recognition |
| Mythic escalation | high-chaos route where old memory becomes dangerous | buffs with instability, world reaction, hidden branch |

### Assyria overlay

Use when a high-chaos wave creates an Assyrian package.

Themes:

- northern Mesopotamian homeland logic
- minority protection and exile petitions
- Nineveh, Khabur, Mosul, or nearby regional anchors if state mapping supports it
- tension between civic protection, church-linked representation, armed defense, and old imperial symbolism

Route groups:

- Nineveh Petition Archive
- Khabur Villages Appeal
- Guards of the Plain
- Congress of Exiles
- The Ancient Name Debate
- Modern Assyrian State
- Imperial Shadow Rejected or Imperial Shadow Embraced

The civic route should avoid turning ancient imperial memory into instant conquest. The high-chaos nationalist route can do that, but it should create foreign fear and regional hostility.

### Mesopotamia overlay

Use when a high-chaos wave creates a river-state, mandate-era revival, or federated valley state.

Themes:

- Tigris and Euphrates logistics
- Baghdad, Basra, Mosul, oil, rail, river police
- British mandate memory if appropriate
- Arab, Kurdish, Assyrian, Marsh, and urban tensions depending on state mapping

Route groups:

- River Administration Restored
- Baghdad Ledger
- Basra Customs Board
- Mosul Compromise
- Oil and River Revenue
- Federal Valley Congress
- Mandate Ghosts or Independent River State

### Volga Bulgaria overlay

Use only when Event 006 creates the package through Independence Wave logic.

Themes:

- Volga-Kama old-state memory
- trade route legitimacy
- Tatar, Bulgar, Islamic, steppe, and river politics depending on the mod's country setup
- recognition as a modern state with old symbols

Route groups:

- Volga Archive Opened
- Merchants of the River Road
- Kama Defensive Line
- Council of the Old Name
- Modern Volga Republic
- Steppe Memory Unbound

Do not import Event 005 focus routes, branch names, startup ideas, decisions, republic missions, collapse variables, event log states, or Soviet Collapse formable logic. The Event 006 version is not a clone of the Soviet Collapse version under a different trigger. It must use the Independence Wave historical-return overlay, with separate route names, separate starting problems, separate package variables, and separate formation or restoration decisions.

### Steppe and Caucasus overlays

Candidates include Idel-Ural, Circassia, Mountain Republic, Don, Kuban, Bukhara, Khiva, and Kokand if valid.

Themes:

- mountain defense
- confederated councils
- cavalry or local militia memory
- exile government and treaty language
- old emirate or khanate institutions where appropriate

### African old-state and local-polity overlays

Candidates include Buganda, Bunyoro, Asante, Sokoto, Kanem-Bornu, Darfur, Barotseland, Zulu, Herero, Nama, and similar researched packages.

Shared route groups:

- Palace or Council of Recognition
- Treaty Memory Office
- Royal Guard or Local Defense Board
- Mission School and Archive Files
- Land Settlement Congress
- Colonial Border Rejection
- Protectorate Renegotiation
- Modern Charter Compromise

Package flavor:

- Buganda should use kabaka, chiefs, protectorate treaty memory, and Lake Victoria regional politics.
- Asante should use Kumasi, Golden Stool symbolism with care, trade routes, and British pressure.
- Sokoto should use emirate federation, scholarly legitimacy, Sahel trade, and northern Nigerian geography.
- Kanem-Bornu should use Lake Chad trade routes, old dynasty memory, and frontier defense.
- Barotseland should use Lozi institutions, Zambezi floodplain logic, and treaty autonomy.
- Zulu should use regimental memory, Natal pressure, and military prestige.
- Herero and Nama packages should use land recovery, colonial violence memory, and mounted or community defense.

### South American local-polity overlays

Candidates include Mapuche Araucania, Aymara congress, Guarani republic, Charrua revival, Palmares, Muisca, Maya, Itza, Nahua, Miskito, Inca, and similar tags if valid.

Shared route groups:

- Land Congress
- Treaty Line Remembered
- Forest or Mountain Defense
- Community Guard
- Mission Archive Disputed
- Border Across the Mountains
- Recognition Without a Patron
- Old Name, Modern Charter

Package flavor:

- Mapuche Araucania should use land congresses, cross-border pressure, and treaty memory.
- Aymara should use Altiplano politics, community councils, and Andes defense.
- Guarani should use Paraguay and adjacent forest region logic, language identity, and mission memory.
- Charrua should be rare and fragile, tied to Uruguay and regional survival.
- Palmares should be a quilombo-inspired restoration, focused on hidden communities, forest defense, and anti-plantation memory.

## Local-polity overlay framework

Local-polity routes should not pretend that every release starts as a modern parliamentary state. They can become one, but the first political question is who speaks for the community.

Major groups:

- assemble the land congress
- recognize chiefs, councils, elders, municipal boards, or protective committees
- settle internal authority disputes
- define land recovery or protectorate terms
- choose armed guard, civic guard, or patron protection
- seek recognition from ordinary states without losing autonomy

Compatibility:

- civic councils route can merge with local charter
- patron cabinet can become protectorate route
- national directorate can become land recovery route
- revolutionary route can become anti-colonial committee route
- strange routes require high chaos and special triggers

## Free port and free city overlay

Free ports and free cities are not ethnic restorations. They are emergency city-states.

Path groups:

- merchant council
- dock police
- customs ledger
- port neutrality
- foreign consular quarter
- harbor militia
- syndicalist dock strike route
- smuggling scandal
- city charter recognized

Rewards:

- trade influence
- naval base repair
- convoy or dockyard bonuses
- intelligence
- high patron risk

## Railway Sovereignty overlay

Railway states are born from logistics collapse.

Path groups:

- junction committee
- timetable authority
- armored train depot
- bridge guard
- ration corridor
- customs at the sidings
- railway league
- high-chaos iron schedule route

Rewards:

- supply bonuses
- rail repair speed
- logistics companies
- armored train or rail gun flavor if balanced
- strange high-chaos route if unlocked

## Strange module framework

Strange modules are not ordinary ideological branches. They should become visible only after the campaign has earned them.

### Anti-Mankind Doctrine Module

Unlocks from very high chaos, anti-human route flags, mass death, impossible-state package type, or explicit strange-state contact.

Path groups:

- Human Category Rejected
- Office of Species Security
- Census of the Unfit
- Border Without Refuge
- Pact with the Inhuman
- Directorate of Final Separation

Rewards:

- powerful internal control
- severe diplomatic penalties
- containment pressure
- strange-state cooperation
- possible world-threat hooks

### Necromancy Cult Module

Unlocks from very high chaos, grave regions, mass death, battlefield contamination, plague, or occult pressure.

Path groups:

- Grave Census
- Custodians of the Quiet Dead
- Requisition the Cemeteries
- Silent Labor Register
- Dead Border Guards
- The State That Inherits the Bodies

Rewards:

- manpower or compliance mechanics with moral and diplomatic cost
- instability
- fear modifiers
- super-event candidate
- containment decisions for neighbors

### Archive-State Module

A high-chaos bureaucracy route where archives, seals, and dead offices keep governing.

Path groups:

- Seal Still Valid
- Ministry Without Ministers
- Census Before Citizenship
- Law of the Absent Cabinet
- Recognition by Paper Alone
- The Country That Files Back

Rewards:

- compliance, stability, and intelligence oddities
- weak manpower
- strong resistance to annexation
- surreal diplomatic reactions

## Coalition congress and league lane

Unlocks when previous Independence Wave countries exist and coalition cohesion is high.

Path groups:

- invitation circular
- first congress hall
- shared ammunition board
- arbitration committee
- volunteer registry
- mutual guarantee statute
- charter vote
- league presidency

The league should not be free. It can fail through rival claims, patron leverage, ideology conflict, or one member's border war.

## Border commission and expansion lane

Unlocks from claim ambition, host settlement failure, old-state overlays, nationalist route, or high chaos.

Path groups:

- local surveys
- parish petitions
- rail and river boundaries
- protected transfer request
- ultimatum draft
- border arbitration
- limited war plan
- claim freeze under observers

Democratic and civic routes should prefer arbitration. Nationalist and high-chaos routes should prefer ultimatums.

## Crisis branch

Crisis content opens when the country is unstable.

Triggers:

- loyalist sabotage
- capital threatened
- patron betrayal
- civil conflict
- recognition collapse
- budget failure
- host invasion
- radical route backlash

Path groups:

- emergency session
- broken charter
- street defense committees
- loyalist file purge
- cabinet exile plan
- capital defense board
- recovery congress
- military rule vote

A crisis branch should allow recovery, not only punishment.

## Convergence and late-game settlement

The tree should have several settlement outcomes.

| Settlement | Requirements | Result |
| --- | --- | --- |
| Recognized Nation | high legitimacy, low patron leverage, recognition progress | stable civic state |
| Armed Independence | strong army, hostile host, survival route | militarized but durable state |
| Dependent State Charter | high patron leverage and foreign support | survival as client or puppet drift |
| League Member | coalition cohesion and congress success | mutual guarantees and faction content |
| Regional Revisionist | high claim ambition and expansion route | border demands and war risk |
| Historical Restoration | historical-return overlay completed | old-name legitimacy and package-specific claims |
| Local Protected State | local-polity overlay completed | land congress or authority recognition |
| Impossible State | strange module completed | containment and world-threat hooks |

## Small-country subsets

Tiny countries should not receive the whole tree if it creates absurd power. They should receive a compact subset:

- provisional opening
- recognition
- small army and police
- budget survival
- patron or league choice
- crisis response
- limited package flavor

They should not receive full regional conquest routes unless high chaos or package design specifically permits it.

## Route lock and compatibility rules

### Mutually exclusive route families

- civic councils vs officer mandate as primary government form
- revolutionary committee vs national directorate as primary ideology route
- patron cabinet vs anti-patron recovery as final patron state
- ordinary civic restoration vs impossible-state doctrine

### Compatible side lanes

- industry can support all routes
- military survival can support all routes, with different rewards
- diplomacy can support civic, patron, and league routes
- border commission can support nationalist, historical-return, and some local-polity routes
- coalition congress can support civic, anti-patron, and small-state routes

### Conditional compatibility

- a historical-return package can be democratic, military, nationalist, patron-backed, or strange depending on route locks
- a local-polity package can become civic, protectorate, revolutionary, or land-recovery route
- free ports can become civic, patron, syndicalist, or criminalized crisis routes
- railway sovereignty can become civic logistics state, military corridor, patron route, or strange iron schedule route

## Focus reward diversity standard

Rewards should mix:

- national spirits
- timed spirits
- scripted variables
- decision unlocks
- small equipment grants
- template unlocks
- advisor unlocks
- recognition progress
- patron leverage changes
- coalition cohesion changes
- border claim setup
- crisis recovery
- cosmetic tag changes
- event log entries

Avoid flat repeated political power rewards.

## AI behavior standards

AI should read:

- ideology
- war state
- host relation
- stability
- legitimacy
- radicalization
- militia strength
- patron leverage
- coalition cohesion
- claim ambition
- package type
- chaos tier
- neighboring threat

Ordinary AI should avoid hidden high-chaos branches unless the relevant route is already active. AI should not choose a package overlay that does not match its package type.

## Localisation and naming style

Focus names should feel like emergency state-building, not generic national focus filler.

Good patterns:

- action plus institution: Convene the Land Congress
- document plus consequence: Publish the Host Reply
- place plus pressure: Guard the Northern Rail Yard
- old name plus modern compromise: The Ancient Name in a Modern Charter

Avoid:

- bland names like Improve Industry
- repeated names across every package
- claims that imply a historical fact the package has not earned

## Icon and asset direction

Use shared icon families when possible:

- petitions and papers
- border posts
- assembly halls
- militia rifles
- radio towers
- train junctions
- old seals
- land congresses
- river maps
- foreign embassies
- broken chains
- grave ledgers

Package overlays need at least a small icon set for old archive, land congress, package guard, recognition, and crisis.

## Implementation handoff

The implementation agent should:

- build the final focus tree from these route families
- use focus filters from the taxonomy
- keep high-chaos routes hidden until unlocked
- add package overlays as modular branch groups
- validate that Event 006 never uses Event 005 focus content, even for Soviet republic style tags, Volga Bulgaria, Old Great Bulgaria, or any other shared tag
- validate that Event 005 cannot claim an Event 006 release by tag name alone
- document actual focus count after implementation
- update asset and icon ledgers after actual focus count is known


## Expanded branch interaction model

The common tree should behave like a state-building network. Political choices alter military, industry, diplomacy, border, and crisis lanes.

| Route choice | Military effect | Industry effect | Diplomacy effect | Border effect | Crisis risk |
| --- | --- | --- | --- | --- | --- |
| Civic councils | slower mobilization, better discipline | civilian repair and tax legitimacy | recognition and observers improve | claims filtered through arbitration | vulnerable to officer impatience |
| Officer mandate | fast defense and emergency laws | military factories and requisition | recognition harder but guarantees possible | defensive claims favored | coup risk if war goes badly |
| Revolutionary committee | militias and volunteer networks | workshops and collectivized supply | communist sponsors and radical league | claims tied to oppressed districts | repression and purge risk |
| National directorate | stronger attack and border troops | youth labor and mobilization | recognition weaker, intimidation stronger | claims, ultimatums, border wars | radicalization and war risk |
| Patron cabinet | better equipment and advisors | loans and foreign construction | sponsor access and puppet risk | patron-backed transfers | anti-patron revolt |
| Anti-patron recovery | counterintelligence and loyal army | debt audits and domestic repair | league protection and balanced recognition | restrained claims | failed broker exposure |
| Historical-return modern | symbolic units and guards | archive grants and cultural institutions | recognition through moderated identity | claims mostly through commission | revanchist backlash |
| Historical-return mythic | old guards and shock units | old capital projects | fear, curiosity, and isolation | aggressive claims | strange or nationalist drift |
| Local-polity congress | community defense | local resource control | observer and autonomy diplomacy | land claims and treaty review | loyalist and settler conflict |
| Strange module | abnormal forces or rules | unstable special economy | isolation or strange diplomacy | rule-breaking claims | containment or global panic |

## Shared opening lane expansion

The opening should give the player several early problems at once.

| Focus group | Story meaning | Mechanical unlock | Should connect to |
| --- | --- | --- | --- |
| Provisional Council | the country exists but is not settled | legitimacy ledger, starting decisions, route preview | all political routes |
| Petition Ledger | the new state presents why it exists | legitimacy or radicalization from host history | civic, national, historical-return |
| Barracks Count | the council counts weapons and defectors | starting army recalculation, depot decisions | military, officer, revolutionary |
| Emergency Budget | the state tries to pay officials | temporary economy spirit and tax decisions | industry, civic, patron |
| Recognition Desk | letters and envoys begin | diplomacy decisions, observer access | civic, patron, league |
| Host Anger Register | the old state records losses | host pressure and border claims | crisis, border commission |
| Survivor Rump Note | host survival state is recorded | prevents invalid release effects | border and settlement logic |

The opening should not force a player to complete every lane before making choices. The first split should happen early, then side lanes should remain available when compatible.

## Political route locks

| Route lock | Opens from | Locks out | Remains compatible with | Failure state |
| --- | --- | --- | --- | --- |
| Civic Mandate | local charter, elections, observers, high legitimacy | dictatorship routes, anti-mankind, most mythic escalation | league, arbitration, modern old-name route | officer emergency if capital falls |
| Officer Mandate | militia congress, capital danger, low stability | full civic mandate, revolutionary committee | defensive league, patron aid if limited | junta crisis or military dependency |
| Revolutionary Committee | radicalization, workers, left sponsor | patron cabinet, civic mandate | radical league, anti-patron, volunteers | internal purge or isolation |
| National Directorate | claim ambition, border grievance, radicalization | civic mandate, anti-patron moderate | military survival and some old-name routes | border war failure and legitimacy collapse |
| Patron Cabinet | foreign aid and leverage | anti-patron at first, full independence achievements | military, industry, border transfer | puppet dependency |
| Anti-Patron Recovery | broker exposure or high leverage | patron cabinet finishers | civic, league, intelligence | failed exposure and dependency |
| Modern Restoration | historical-return package and civic legitimacy | mythic restoration | civic, league, arbitration | revanchist revolt |
| Mythic Restoration | old-state memory and high chaos | civic mandate | national directorate and strange modules | containment, coalition fear |
| Land Congress | local-polity package | patron cabinet if anti-colonial route chosen | civic, community defense, arbitration | land war or loyalist split |
| Strange Doctrine | Evo V and hidden pressure | ordinary recognition route | strange coalition only | containment or global hostility |

## Industry and logistics route

Industry is not a generic factory column. It should show how a small state becomes capable of acting.

| Focus group | Unlocks | Route interactions |
| --- | --- | --- |
| Emergency Tax Offices | temporary consumer goods and political power recovery | civic route improves legitimacy, military route risks resistance |
| Repair the Rail Yard | supply, trains, repair speed, railway decisions | railway sovereignty gets extra nodes |
| Convert Municipal Workshops | infantry equipment or support equipment | revolutionary route gets militia bonuses |
| Reopen the Port Ledger | convoys, trade opinion, foreign aid route | free port and patron routes gain more value |
| Protect the Food Districts | stability, war support, attrition reduction | local-polity and rural packages gain legitimacy |
| Archive Grants and Museums | stability and old-state memory balance | historical-return modern route uses it to avoid mythic drift |
| Foreign Loan Board | construction and debt | patron leverage rises unless anti-patron safeguards exist |
| League Supply Pool | shared equipment and volunteers | coalition congress and league route payoffs |

Avoid plain factory rewards when a decision, spirit, or supply mechanic would express the same idea better.

## Military route expansion

| Focus group | Unlocks | Compatible routes | Risk |
| --- | --- | --- | --- |
| Depot Audit | equipment scaling and depot decisions | all routes | host raids if exposed |
| Militia Standards | templates and training | civic, officer, revolutionary | slow if low legitimacy |
| Officer Staff | command power and generals | officer, patron, national | coup pressure |
| Community Defense Belt | forts, terrain defense, local manpower | local-polity, civic, military | low offensive value |
| Volunteer Liaison Office | volunteer sending and receiving | league, revolutionary, patron | foreign escalation |
| Emergency Mobilization Law | manpower and output | military, national, strange | stability loss |
| Patron Training Mission | doctrine bonus and advisors | patron cabinet | puppet leverage |
| League Defense Board | mutual guarantees and shared defense | coalition congress | drags members into wars |
| Strange Force Office | package-specific abnormal units or modifiers | strange modules only | containment and diplomatic isolation |

## Diplomacy and recognition route expansion

| Focus group | Story role | Mechanics |
| --- | --- | --- |
| First Recognition Mission | envoys ask neighbors to treat the state as real | recognition progress and opinion |
| Observer-Protected Elections | foreign observers protect civic legitimacy | civic route, lower radicalization, host suppression cost |
| Neutrality Declaration | state promises not to become a proxy | lowers patron leverage and claim ambition |
| Patron Embassy Row | foreign missions compete | aid, advisers, leverage, cabinet demands |
| Balanced Sponsors | multiple patrons prevent one puppet route | stronger aid with lower single-patron leverage but higher intrigue |
| Small States Congress | released countries coordinate | coalition cohesion, guarantee decisions |
| League Charter | formal faction if conditions pass | super-event candidate, faction creation |
| Recognition by the Old Host | settlement after reduced release | lower border war risk and possible trade bonuses |
| Recognition Refused | failure branch | national, revolutionary, or strange route pressure rises |

Diplomacy should not guarantee safety. It trades vulnerability to the host for vulnerability to patrons.

## Border and expansion route expansion

Expansion should start as a commission, not instant conquest.

| Focus group | Unlocks | Restraint path | Escalation path |
| --- | --- | --- | --- |
| Border Survey Office | claim ledger and state scoring | arbitration | propaganda claims |
| Petition the Villages | local support in target districts | plebiscite | militia pressure |
| Protected Transfer Talks | peaceful state transfer if host agrees | autonomy bargain | patron-backed ultimatum |
| Old Capital Question | historical-return target check | symbolic recognition without transfer | war goal or crisis |
| League Arbitration Board | coalition mediates disputes | cohesion gain | league split if ignored |
| Ultimatum Draft | final diplomatic warning | withdraw for stability | limited war goal |
| War of the Dossier | border war route | restricted goals | full claim conflict at high chaos |

A breakaway can claim the host capital later, but the initial wave cannot take every host state. The tree should treat such claims as later gameplay.

## Historical-return overlay details

Historical-return overlays should have three competing paths.

| Path | Narrative role | Mechanical role | Failure |
| --- | --- | --- | --- |
| Archive Legitimacy | documents, witnesses, clergy, scholars, old symbols | legitimacy, claims, culture, museums, advisors | archive scandal or contested evidence |
| Modern Compromise | old name under modern institutions | stability, recognition, restrained claims, civic route | revanchist backlash |
| Restoration Pressure | old rulers, old borders, capital memory | claim ambition, special guards, border ultimatums | isolation, war, strange drift |

Package-specific notes:

| Package | Required overlay flavor | Avoid |
| --- | --- | --- |
| Assyria | minority protection, language, churches, diaspora, Nineveh plain defense | treating ancient empire claim as simple conquest |
| Mesopotamia | river administration, Iraqi mandate memory, royal or republican compromise | giving all river land at release |
| Volga Bulgaria | Volga trade, Bulgar memory, Islam, archive legitimacy, Event 006 origin | copying Soviet Collapse republic tree |
| Circassia | mountain and diaspora memory, Black Sea diplomacy | generic Cossack or Russian route framing |
| Bukhara | oasis administration, reformist court, religious schools, trade | making it only a monarchist restoration |
| Asante | Kumasi center, council authority, royal symbolism, federation option | flattening Asante into generic Ghana split |
| Sokoto | emirate network, scholars, Hausa and Fulani complexity | portraying the route as only conquest |
| Kanem-Bornu | Lake Chad trade, mai memory, caravan guard | ignoring cross-border lake geography |
| Buganda | kabaka question, local parliament, protectorate memory | using modern monarchy politics without care |
| Barotseland | Zambezi floodplain, Lozi institutions, treaty memory | treating it as random separatism |
| Palmares | maroon republic, anti-slavery memory, fortified communities | using supernatural content on real trauma by default |
| Zulu | royal council and regiment memory, constitutional route | making all content Shaka nostalgia |
| Herero and Nama | land return, cattle, grave memory, anti-colonial survival | using trauma as spectacle |
| Mapuche | land congress, community law, Araucania memory, defensive war | defaulting to a foreign king meme |
| Aymara | Altiplano, Lake Titicaca, mining, highland defense | merging all Andean identities |
| Guarani | language, river and forest communities, cross-border recognition | treating it as only Paraguay nationalism |
| Charrua | memory recovery, grassland mobility, civic recognition | inventing false institutions without source caution |

## Local-polity overlay details

Local-polity routes should focus on land and community authority.

| Focus group | Effect direction |
| --- | --- |
| Convene the Land Congress | legitimacy, local support, route lock |
| Map Communal Lands | state modifiers, claims, lower industrial extraction |
| Community Defense Companies | defensive militia and terrain bonuses |
| Treaty Memory Office | recognition and arbitration bonuses |
| Reject the Broker Chiefs | lowers patron leverage and corruption |
| Protect the Schools and Language | stability, manpower, advisor unlocks |
| Land War Emergency | if negotiations fail, defensive war path |
| Protected Autonomy Formula | option to settle short of full expansion |

The payoff should not always be full conquest. A stable recognized local state, a protected autonomy network, or a league-backed settlement can be stronger and more interesting.

## Strange module details

Strange modules should be hidden until the event earns them.

| Module | Opening signal | Focus group direction | Payoff |
| --- | --- | --- | --- |
| Anti-Mankind Doctrine | legal language stops referring to citizens as people | renunciation office, sealed courts, external enemies, inhuman diplomacy | hostile doctrine state that can join strange coalitions |
| Necromancy Cult | casualty ledgers and grave registries become political documents | grave census, mortuary ministries, dead regiments, containment crisis | manpower and fear mechanics with high diplomatic cost |
| Archive-State | documents name officials who do not exist | paper ministries, map room, recognition paradox, infinite claims risk | claims and legitimacy distorted by archives |
| Railway Sovereignty | rail dispatchers and garrisons declare the network sovereign | timetable law, rail militia, hub defense, supply priority | supply power and rail league route |

The tree should offer containment or recovery where possible. Strange route visibility should never clutter a normal low-chaos playthrough.

## Crisis branch details

| Crisis | Opens when | Focus groups | Recovery path | Collapse path |
| --- | --- | --- | --- | --- |
| Broken Charter | stability very low or elections fail | emergency session, cabinet rebuild, legitimacy drive | civic recovery or officer mandate | civil split |
| Capital Exile | capital lost but country survives | exile cabinet, foreign recognition, return plan | retake capital and restore government | puppet dependency |
| Patron Betrayal | leverage too high or cabinet seats demanded | expose brokers, purge mission, league plea | anti-patron recovery | patron puppet |
| Loyalist Civil Conflict | loyalists armed and pressure high | street defense, amnesty, loyalist purge | reconciliation or military rule | civil war |
| Border War Shock | expansion war goes badly | emergency defense, arbitration plea | restrained settlement | nationalist dictatorship |
| Strange Containment | occult pressure revealed | audit board, quarantine, moral tribunal | civic or military containment | strange doctrine lock |

Crisis branches should be useful, not only punishment. A country that recovers from crisis should gain a distinct route memory and possibly a stronger late-game identity.

## Late-game ambitions

| Ambition | Eligible routes | Payoff |
| --- | --- | --- |
| Recognized Nation | civic, anti-patron, modern old-name, land congress | removes provisional penalties and strengthens diplomacy |
| Armed Independence | officer, revolutionary, national, emergency civic | military doctrine and defensive security |
| Dependent State Charter | patron cabinet | stronger aid but autonomy cap |
| League Founder | civic, anti-patron, coalition route | faction formation and super-event candidate |
| Regional Arbiter | civic, league, modern old-name | border arbitration decisions and reduced war risk |
| Restoration State | historical-return mythic or national | claims, unique guards, higher foreign fear |
| Protected Local Order | local-polity | community defense, autonomy network, land settlement |
| Strange Coalition Member | strange modules only | links to other high-chaos systems |

## AI route selection standards

AI should choose routes based on conditions, not flat weights.

| Condition | Route bias |
| --- | --- |
| high legitimacy and low war | civic councils |
| low stability and enemy nearby | officer mandate |
| high radicalization and left sponsor | revolutionary committee |
| high claim ambition and border grievance | national directorate |
| high foreign aid and low autonomy concern | patron cabinet |
| high patron leverage and high legitimacy | anti-patron recovery |
| package historical-return and moderate radicalization | modern restoration |
| package historical-return and high claim ambition | mythic restoration or national directorate |
| package local-polity | land congress |
| coalition cohesion high | congress and league route |
| capital threatened | crisis and military survival |
| Evo V strange conditions | strange module only if route is already revealed |

AI should not choose hidden or extreme focuses because they exist. The route must be active or conditions must be clearly true.

## Focus count guidance without a blueprint

Do not produce a fixed focus-by-focus map from this document. The implementation should choose a final count that meets route depth.

Recommended depth bands:

| Country support level | Tree depth direction |
| --- | --- |
| tiny ordinary release | opening subset, civic or military choice, recognition or survival payoff |
| ordinary playable release | full shared trunk, two or three political paths, industry, army, diplomacy, crisis |
| protectorate or city state | shared trunk, patron or anti-patron, economy, diplomacy, limited border route |
| historical-return package | shared tree plus overlay, modern and restoration branches |
| local-polity package | shared tree plus land congress overlay and community defense |
| strange package | shared emergency subset plus strange module and containment branch |
| league leader | full tree with coalition congress and late-game ambition |

The final tree should be deep enough to be playable, but it should not become a giant identical tree for every tiny one-state release.

## Icon reuse and new icon expectations

| Branch | Icon style |
| --- | --- |
| Provisional opening | documents, councils, maps, seals, border desks |
| Civic | ballots, assemblies, observer armbands, charters |
| Military | depots, rail guards, barracks, field phones |
| Revolutionary | workshops, red committees, worker militia, communal stores |
| National | broadcast towers, border stones, youth formations, claim maps |
| Patron | embassies, loan papers, foreign missions, cabinet silhouettes |
| Anti-patron | broken strings, exposed files, counterintelligence desks |
| Coalition | small flags, congress tables, shared supply crates |
| Historical-return | archives, old seals, restored city gates, museum cases |
| Local-polity | land maps, councils, community guards, river or mountain symbols |
| Strange | sealed files, blank stamps, grave ledgers, inhuman courts |

Prefer reused vanilla icons when the concept is generic. Create new icons for package overlays and route-defining mechanics.

## Formation route overlays

The Liberation Provisional Tree should support formable paths without turning every release into a formable chase. Formation overlays are route modules that become visible only when the package type, route, state control, and chaos tier justify them.

Formation overlays follow this rhythm:

1. identity clue or archive focus group
2. claim office or border memory focus group
3. legitimacy, recognition, or congress preparation focus group
4. decision unlock focus
5. map-control formation decision
6. formation event or news event
7. post-formation stabilization branch

Focuses prepare the claim. The final formation decision verifies the map. A focus may never form a large state by itself if state control is the real proof.

Formation overlay types:

| Overlay | Unlock source | Focus role | Decision role | Post-formation branch |
| --- | --- | --- | --- | --- |
| League federation | coalition congress and high cohesion | draft shared charter and member rules | form a federation or compact if members qualify | common command, arbitration, shared reserves |
| Old-state restoration | historical-return package | collect archives, revive institutions, choose modern compromise or mythic restoration | form old-name state if core region is controlled | integration, capital question, rival claimants |
| Local polity congress | local-polity package | convene land council, defend customary authority, build administration | form recognized local state or confederation | land settlement, subject autonomy, regional recognition |
| Patron mandate | protectorate package | accept or resist sponsor legal framework | form client mandate or protected union | dependency crisis or anti-patron recovery |
| Strange proclamation | strange package | reveal hidden doctrine or non-human authority | form impossible state if route and chaos conditions hold | world-threat hooks, diplomatic breakdown, containment |

## Formation lane design requirements

For each implemented formable lane, the final tree must define:

- route family that reveals the formable
- package types that can use it
- state groups or named regions it references
- decision category or Formation Ledger entry it unlocks
- mutually exclusive routes that block it
- support branches that reduce integration costs or reveal requirements
- AI personality and campaign state that can choose it
- post-formation focuses that solve the new state's problems
- assets such as formation focus icons, formation decision icon, flag, portrait, faction emblem, and animated seal when dramatic enough

The focus tree should not show every hidden formable at game start. It can show sealed route anchors, rumors, or state-group clue focuses only after the relevant reveal.

## Animated route payoff notes

Animated leader portraits and route emblems should be reserved for major route endings:

- first historical-return formable completed
- strange package reveals its real authority
- anti-patron route defeats sponsor control
- League of New States becomes a real bloc
- necromantic or anti-mankind authority becomes public
- a host survives as a one-state rump and turns survival into a new political identity

The tree should note which focus or decision flips the portrait or emblem. Each animated portrait needs a static fallback and a cleanup condition when the leader, cosmetic tag, or route changes.

## Focus and scripted GUI links

Focuses that unlock or modify the Independence Dossier Board, New States Congress, Patron Ledger, or Formation Ledger must describe what the player sees after completion.

Examples:

- a civic legitimacy focus can reveal observer status and legitimacy breakdown
- a military survival focus can unlock depot and supplied-division mission cards
- a patron cabinet focus can open sponsor influence tracks
- a coalition congress focus can unlock vote cards and mutual guarantee buttons
- a formation route focus can reveal named state-group requirements

A focus that unlocks a GUI button must also define the decision or scripted effect family that AI can use. Human-only GUI actions are incomplete.
