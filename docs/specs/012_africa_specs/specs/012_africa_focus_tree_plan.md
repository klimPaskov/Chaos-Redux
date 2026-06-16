# Event 012 — Africa Focus Tree and Route Architecture

## Focus tree purpose

The Africa event package needs a large shared focus tree or a country-specific overlay tree that works for any valid African-capital unifier. The tree must not be a vertical ladder of claims. It is the playable identity of the new African unifier and should interact with every major mechanic: legitimacy, congress authority, charter cohesion, colonial alarm, liberation momentum, paper cores, regional authorities, faction membership, diaspora return, the Second Scramble, and post-unification world ambitions.

The implementation agent owns exact focus count, coordinates, and final focus names. The spec defines route families, anchor focus groups, locks, payoffs, focus filters, and branch interactions. A complete implementation should likely contain at least 120–180 focuses if built as a full shared tree, plus an RSA civil-war subtree and high-chaos/post-unification extension branches. A smaller tree would be a simplification unless the implementation proves that fewer focuses still preserve all route families and gameplay loops.

## Focus filter taxonomy

The tree should use focus filters or internal search categories so the player can read it:

| Filter | Route family |
| --- | --- |
| `africa_statebuilding` | Opening congress, paper-core burden, administration, early legitimacy. |
| `africa_political` | Federalist, revolutionary, military, crown/traditional, high-chaos covenant routes. |
| `africa_liberation` | Anti-colonial war, interventions, claims, liberation committee. |
| `africa_charter_league` | Faction, diplomacy, recognition, member votes, cohesion. |
| `africa_integration` | Regional authorities, protectorates, federation, annexation, resistance management. |
| `africa_industry` | Ports, railways, resources, factories, construction, continental economy. |
| `africa_military` | Liberation armies, irregulars, veterans, special units, elephant corps, doctrine. |
| `africa_diaspora` | Afro-American and diaspora return, volunteers, expertise, culture, tension. |
| `africa_high_chaos` | Supernatural/nature routes, nonhuman pacts, disaster prophecy, mythical units. |
| `africa_post_unification` | Africa Is One, Second Scramble, continental sponsor route, world-end path. |

## High-level architecture map

```text
                              [The Continental Claim]
                                      |
                 [Emergency Congress in the Capital] -- [Paper Cores, Real Burdens]
                                      |
          +---------------------------+---------------------------+
          |                           |                           |
 [Statebuilding Trunk]       [First Charter Diplomacy]      [First Liberation Staff]
          |                           |                           |
          |                  +--------+--------+                  |
          |                  |                 |                  |
 [Administration]     [Invite African Wars]  [Observer States]  [War Preparation]
          |                  |                 |                  |
          +------------------+--------+--------+------------------+
                                      |
                            [Choose the Congress Soul]
                                      |
        +-------------+--------------+-------------+--------------+
        |             |              |             |              |
 [Federal Congress] [People's Front] [General Staff] [Crown Congress] [High-Chaos Covenant]
        |             |              |             |              |
        +------+------+--------------+------+------+
               |                            |
       [Regional Authority System]   [Liberation and Colonial Wars]
               |                            |
     +---------+----------+        +--------+--------+
     |                    |        |                 |
 [Integration Branch] [League Branch] [Industry] [Military]
     |                    |        |                 |
     +----------+---------+--------+--------+--------+
                |                           |
        [Africa Is One]             [Second Scramble]
                |                           |
                +-----------+---------------+
                            |
                    [Continental Pole]
                            |
           +----------------+----------------+
           |                                 |
 [Sponsor Other Continent Unifiers]   [World Is One Path]
```

The tree should be visually wide and layered. Political routes sit in the middle; industry and military support routes flank them; integration and liberation should run below and interact with politics; high-chaos routes should be hidden or locked to one side until visible. Post-unification routes should sit below the African unification payoff, not clutter early play.

## Opening trunk

### The Continental Claim

Route opener. Announces the unifier’s claim and begins the paper-core burden. Unlocks the Continental Congress decision category and the first news event. Gives a small but meaningful burst of Legitimacy and Colonial Alarm. This focus should not declare all wars.

### Emergency Congress in the Capital

Creates the first Congress offices. Sets the initial values for Legitimacy, Authority, Charter Cohesion, Liberation Momentum, and Colonial Alarm. Unlocks first decisions:

- Call Regional Delegates.
- Survey Paper Cores.
- Send Protection Offer.
- Assemble Liberation Staff.
- Publish Charter Draft.

### Paper Cores, Real Burdens

Explains that the unifier has claimed the continent but cannot administer it yet. Reduces the worst paper-core burden for controlled home-region states and unlocks regional integration missions. The focus should use dynamic tooltip text to show that cores exist but integration matters.

### The First Charter Diplomacy

Opens faction diplomacy. Unlocks observer invitations for African countries, protected-member offers for countries at war with non-African colonizers, and low-cost recognition missions for recently released African states.

### The First Liberation Staff

Creates an anti-colonial military office. Unlocks war-preparation missions against colonial holders in Africa and volunteer/support decisions for African countries already at war with colonial powers.

### Choose the Congress Soul

Main route fork. It should not be available instantly; require at least some Legitimacy or a first regional congress. The five route families are mutually exclusive for the central identity, but their support branches can still remain available.

## Political route family A — Federal Congress

Narrative: the unifier argues that Africa can only become one if regions remain visible and protected inside a federal structure. This is the safest route for cohesion and integration, slower for war, best at retaining African members without revolt.

Mechanical identity:

- Higher Charter Cohesion and Regional Trust.
- Slower annexation, more subject/federation paths.
- Easier peaceful integration and recognition.
- Lower Colonial Alarm from diplomatic actions, but lower war momentum.
- Strongest path for “Not a New Empire” achievement.

Anchor focus groups:

| Focus group | Purpose | Unlocks |
| --- | --- | --- |
| Charter Assembly | Formalizes member votes and regional rights. | League vote decisions, veto handling, member confidence. |
| Regional Autonomy Statutes | Makes regional authorities useful instead of temporary puppets. | Authority-specific modifiers, slower but safer integration. |
| Federal High Court | Arbitration over borders and integration. | Border dispute missions, peaceful settlement options. |
| Continental Citizenship | Enables diaspora return without destabilizing members. | Skilled diaspora advisor pool and manpower decisions with low unrest. |
| Congress of Capitals | Late federal payoff. | Can form United African Federation without annexing every subject directly. |

Failure state:

If Authority is too low, federalism can become paralysis. Member states block wars, integration slows, and foreign patrons can exploit regional vetoes.

AI behavior:

AI prefers this route when the unifier is democratic, neutral, weak, already has several faction members, or faces strong colonial powers. AI avoids it if it is already strong and high chaos pushes aggressive options.

## Political route family B — People’s Liberation Front

Narrative: anti-colonial revolution becomes the continent’s organizing language. The unifier frames Africa as a world-historical liberation front connected to workers, soldiers, ports, plantations, mines, and diaspora radicals.

Mechanical identity:

- Strongest Liberation Momentum.
- Cheaper support for anti-colonial wars.
- More equipment and militia recruitment from unions, ports, and colonial armies.
- Higher Colonial Alarm and ideological backlash.
- Can sponsor revolts in colonial holdings faster.
- Better at creating African republic subjects, weaker at retaining monarchist or conservative members.

Anchor focus groups:

| Focus group | Purpose | Unlocks |
| --- | --- | --- |
| Liberation Committee | Directly references OAU-style liberation support as design inspiration. | Training camps, equipment convoys, volunteer cadres. |
| Port Unions and Mine Cells | Uses industrial labour and logistics. | Sabotage against colonial holders, construction speed in ports/mines. |
| The Red Charter | Route lock and ideology shift. | Socialist party names, revolutionary leader/council options. |
| Exile Radios | Pan-African propaganda and diaspora ties. | Influence growth in occupied African states, foreign pressure events. |
| People’s Continental Army | Late payoff. | Large but equipment-hungry liberation army; risk of command fragmentation. |

Failure state:

If Legitimacy falls or equipment is low, revolutionary recruitment creates uncontrolled militias and member fear. Strong African countries can accuse the unifier of exporting revolution and leave.

AI behavior:

AI prefers this route when communist/socialist, when many African states are colonized, when the unifier is at war with a colonial holder, or when high chaos increases radical choices. It avoids this route if it depends heavily on democratic Western aid.

## Political route family C — Continental General Staff

Narrative: Africa can only be united by command. The unifier centralizes the war effort around generals, railway officers, garrison defectors, and emergency committees. This route is aggressive, militarized, and efficient, but dangerous for cohesion.

Mechanical identity:

- Highest Authority and military readiness.
- Fastest forced integration and war preparation.
- Lower Charter Cohesion and Regional Trust.
- Stronger ability to suppress member resistance.
- High risk of coups, regional mutinies, and Second Scramble escalation.

Anchor focus groups:

| Focus group | Purpose | Unlocks |
| --- | --- | --- |
| General Staff Above Parliament | Route lock. | Military leader/council, army law changes, command-power decisions. |
| Railway War Offices | Links logistics and conquest. | Rail repair objectives, supply hub construction, depot missions. |
| Askari and Veteran Bureaus | Integrates colonial-era African soldiers. | Veteran cadre units, officer decisions, doctrine bonuses. |
| The Protectorate System | Military occupation and puppet route. | Fast protectorate decisions, resistance risk, local garrisons. |
| Continental War Plan | Late payoff. | Coordinated ultimatums against colonial holders and resistant members. |

Failure state:

If Cohesion collapses, the military route produces revolts and breakaway generals. If Authority is high but Legitimacy low, integration can become occupation, creating long-term unrest.

AI behavior:

AI chooses this route when fascist/authoritarian/military, when war is already broad, when the unifier has strong industry, or when colonial holders are weak enough for fast campaigns. It should not choose it when surrounded by stronger enemies and low stability.

## Political route family D — Crown Congress and Old Thrones

Narrative: old crowns, councils, emperors, oba courts, mansas, negus claims, asantehene-like authority, and symbolic kingship are pulled into a modern continental frame. This is not a restoration of one real empire over all Africa; it is an alternate-history route where ceremonial and traditional legitimacy becomes a weapon.

Mechanical identity:

- Strong Legitimacy and high regional flavour.
- Unlocks councils, regencies, ceremonial leaders, traditional advisors, and symbolic title changes.
- Works well with regional authorities and slower integration.
- Can create powerful unity spirits if old thrones cooperate.
- Risks regional rivalry and accusations of invented monarchy.

Anchor focus groups:

| Focus group | Purpose | Unlocks |
| --- | --- | --- |
| The Council of Old Seats | Invites regional traditional authorities. | Regional title events, advisor pools, legitimacy boosts. |
| The Crown Without One Crown | Avoids overclaiming one ethnicity or dynasty. | Cosmetic title variants based on selected country and route. |
| Aksum, Mali, Kongo, Zimbabwe | Historical-memory route nodes. | Regional integration bonuses tied to history-inspired authority, no false source claims. |
| The Royal Road and Drum | Ceremony plus logistics. | Stability, infrastructure, legitimacy missions. |
| The Lion Throne of Africa | Late payoff. | Dramatic cosmetic identity, possible animated portrait/frame, high cohesion if regions accepted. |

Name/title rules:

- Use researched and respectful title pools.
- Let the Crown Congress and absurd court routes use the source-language ruler/court display-name pool without translating it or putting raw phrases in ids.
- Do not create a single fake “African king” title that pretends all African traditions are the same.
- Use dynamic localisation: selected-country route names should draw from its region, while pan-continental titles remain invented and generic enough to avoid claiming real sacred authority.

AI behavior:

AI prefers this route when monarchist/neutral/traditional, when Ethiopia or another monarchy-like tag is selected, when the player chooses a ceremonial path, or when high Legitimacy makes it attractive. It avoids it if revolutionary or anti-traditional route flags dominate.

## Political route family E — Green Covenant and High-Chaos Myth

Narrative: once chaos rises, the public begins reporting impossible natural signs. Rivers flood colonial depots; spiders appear on radio wires; elephants follow orders they were never given; storms arrive when an ultimatum is ignored; rainforest actors claim to speak for no human state. The unifier can either suppress these stories, use them as propaganda, or bargain with them.

This route should not unlock at baseline. It appears from Evolution II or later, or through high chaos and specific regional incidents.

Mechanical identity:

- Strong weird units and disaster/prediction powers.
- High Colonial Alarm and global fear.
- Can ally with supernatural or nonhuman actors.
- Risks losing normal diplomatic recognition.
- Can cause natural disasters if colonialists refuse ultimatums, but this must be costly and increase chaos/condemnation-like pressure where applicable.

Anchor focus groups:

| Focus group | Purpose | Unlocks |
| --- | --- | --- |
| The Web Behind the Congress | Ananse-inspired intelligence/sabotage route. | Spy webs, misinformation, resistance operations. |
| The Tide Has a Witness | Mami Wata-inspired coast/river route. | Port storms, convoy disruption, flood warnings, healing rituals. |
| Courts of Thunder and Ironwood | Orisha/vodun/nature-inspired high-chaos route. | Disaster prediction, storm ultimatums, high-risk rituals. |
| The Great Herds Remember | Elephant logistics and weird units. | Elephant corps, heavy supply movement, intimidation, terrain bonuses. |
| Forests That Refuse the Border | Congo Basin high-chaos nonhuman pact. | Gorilla/chimpanzee guardian polities only as explicit nonhuman actors. |

Failure state:

If Covenant Pressure rises too high, normal allies leave, disasters backfire, nonhuman actors become uncontrollable, and the unifier can become a world-threat-like actor.

AI behavior:

AI only chooses this route at high chaos, with specific route flags, or under a rare AI personality. Ordinary AI should not stumble into it because it can destabilize the world.

## Industry branch — Continental economy

The industry branch must be geographically grounded and must interact with liberation and integration. It should not be a generic factory chain.

Major focus groups:

| Focus group | Region | Gameplay |
| --- | --- | --- |
| Port Congresses | West African Coast, Swahili Coast, South African ports, islands | Ports, dockyards, convoy capacity, trade protection, diaspora entry. |
| Rail Spine Survey | Nile-Horn, East Africa, Zambezi, South African belt | Railways, supply hubs, strategic movement, integration missions. |
| Sahara and Sahel Roads | Maghreb/Sahara/Sahel | Infrastructure, desert supply, motorized/cavalry movement, famine-risk mitigation. |
| River Authorities | Congo/Nile/Niger/Zambezi | Infrastructure, supply, resource extraction, flood/disaster hooks. |
| Copper, Gold, Oil, Rubber, Grain | Resource regions | Resource decisions and industry growth; avoid flat resource dumps without state work. |
| Continental Arsenal | Integrated industrial states | Military factories, production lines, equipment conversion, unit support. |
| The Development Bank | Federal/reform path | Civilian factories, construction decisions, foreign investment risks. |
| Revolutionary Planning Boards | People’s Front path | Military factories and worker mobilisation, but consumer goods and stability tradeoff. |
| Military Works Directorate | General Staff path | Forts, rail, depots, supply hubs, industry tied to war plans. |
| Royal Works and Roads | Crown path | Infrastructure and legitimacy, lower unrest. |
| Living River Oaths | High-chaos path | Flood prediction, construction speed in rivers/coasts, disaster risk. |

Industry rewards should include buildings, resources, production lines, repair speed, regional construction decisions, supply improvements, and integration bonuses. Small modifiers can support the branch but must not be the main reward.

## Military branch — Liberation armies and special forces

The military branch should give the unifier a fighting identity. It must include starting forces, reinforcement pathways, route-specific units, and AI force-growth logic.

Major focus groups:

| Focus group | Gameplay |
| --- | --- |
| Improvised Continental Command | Reduces starting army disorganization and unlocks first templates. |
| Colonial Veteran Bureaus | Recruits and trains former colonial soldiers; adds officer quality and veteran cadres. |
| Capital Defence Committees | Defensive militia and garrison units; tied to Legitimacy and home-region states. |
| Railway Guard Formations | Units and missions around rail/supply states. |
| Desert Columns | Cavalry/motorized/light infantry for Sahara/Sahel. |
| Mountain and Highland Schools | Ethiopian/Horn/Rift mountain units. |
| River and Lake Flotillas | Naval/river support, convoy and port decisions where supported by game mechanics. |
| Liberation Army Standardization | Converts irregulars into regular templates; consumes army XP and equipment. |
| Elephant Logistics Corps | Evolution II/high-chaos unit support; supply, breakthrough, intimidation, terrain costs. |
| The Continental Army | Late payoff; powerful but supply-heavy army reforms. |

### Elephant units

Evolution II asks for stronger and weirder units like elephant units. They should be designed as high-chaos support or special battalion content, not as ordinary infantry spam.

Possible implementation forms:

- Support company or special battalion unlocked by focus and tech/idea.
- High supply use and terrain limits.
- Strong breakthrough, suppression/intimidation, jungle/forest/savanna flavor, but vulnerable to modern armor/air.
- Requires a route flag, animal-handling equipment/abstract support equipment, and high Legitimacy or Green Covenant pressure.
- AI uses conservatively unless high chaos route is active.

## Diplomacy and League branch

This branch manages African countries before conquest. It should produce the faction mechanics the user asked for.

Major focus groups:

| Focus group | Gameplay |
| --- | --- |
| Charter Invitations | Opens observer/protected/member invitation decisions. |
| Defend the Colonised State | If an African country is at war with a colonizer, the unifier can intervene, send aid, and form a faction to save it. |
| The Congress Vote System | Adds member votes, confidence, and cohesion. |
| Recognition Offices | Improves foreign recognition and lowers immediate intervention risk. |
| Anti-Puppet Clauses | Prevents foreign powers from quietly puppeting members. |
| Shared War Council | Enables shared reserves, war goals, and coordinated liberation targets. |
| Member Confidence Missions | Timed missions to keep members from leaving. |
| Pressure for Integration | Opens influence and integration pressure; risky against strong members. |
| Protectorate Compacts | Safer puppet path for smaller members. |
| Federation Accession Acts | High-Legitimacy peaceful integration path. |

This branch must create real faction rules: minimum membership for certain actions, refusal logic, expulsion or departure logic, shared war goals, AI choices, and failure states.

## Expansion and integration branch

Expansion is not “declare war on every African country.” It is a region-by-region continental project.

Major focus groups:

| Focus group | Gameplay |
| --- | --- |
| Regional Congress Survey | Reveals region integration requirements and paper-core burden. |
| Claims Office | Converts paper cores into visible claims/war goals/requirements in specific regions. |
| Colonial Ultimatums | Demands African states from non-African holders; refusal raises Colonial Alarm and may create war goals. |
| Liberation War Plans | War goals against colonial holders and collaborators. |
| Regional Authority Release | Creates local African subject authorities to help govern and fight. |
| Integration Missions | Hold capitals, secure rail, build administration, lower resistance, spend equipment/support. |
| Member Pressure | Influence-puppet-annex path for African faction members. |
| Resistance and Exit Crisis | Strong members can resist; focus path can mitigate or provoke. |
| Continental Accession | Integrate enough regions to reduce paper-core burden significantly. |
| Africa Is One | Requires all African states controlled by unifier or loyal integrated/federal authorities. Fires super-event role label and unlocks Second Scramble. |

### Postwar handling

Every expansion focus that creates a war goal must also define postwar treatment:

- Direct integration.
- Regional authority release.
- Protectorate status.
- Federation membership.
- Occupation settlement.
- Resistance and compliance work.
- Border settlement events.
- Member confidence effects.
- Colonial alarm effects.

## Diaspora return branch

The prompt explicitly asks to “invite afro-americans back.” The branch should be broader: African diaspora return from the Americas, Caribbean, Europe, and colonial metropoles, with a special Afro-American route because that was named.

Design goals:

- Create skilled manpower and advisors, not only recruitable population.
- Tie return to ports, stability, housing/industry, legitimacy, and political route.
- Avoid implying diaspora people are a resource to consume. It is a political and social route with tradeoffs.

Major focus groups:

| Focus group | Gameplay |
| --- | --- |
| The Return Offices | Unlock diaspora return decisions and port requirements. |
| Afro-American Delegations | Special route for African-American volunteers, engineers, doctors, pilots, and political organizers. |
| Caribbean and Atlantic Networks | Naval/convoy, cultural, and intelligence support. |
| Exile Professors and Engineers | Research, construction, and advisor unlocks. |
| Returnee Settlement Councils | Housing/consumer goods/local support missions. |
| Citizenship Without Erasure | Legitimacy and integration bonuses; reduces internal tension. |
| Diaspora Guard Cadres | Volunteer divisions; must cost equipment, training time, and convoy access. |
| Pan-Atlantic Congress | Late payoff, stronger recognition and post-unification Afro-Atlantic options. |

Failure state:

If the unifier has low stability, high authoritarian pressure, or no ports, diaspora return creates political backlash, disappointed volunteers, and foreign propaganda.

## Regional authority side branches

Each major region should have a side branch or dynamic focus group unlocked when the unifier controls or sponsors enough of that region.

| Regional branch | Anchor ideas |
| --- | --- |
| West African Congress | Congress politics, ports, Ghana-Mali-Songhai memory, trade unions, gold/cocoa/resources, diaspora entry. |
| Sahel Caravan Authority | Desert logistics, caravan roads, cavalry/motorized columns, drought and supply missions. |
| Nile-Horn League | Aksum/Kush/Ethiopian highland legitimacy, Red Sea ports, mountain troops. |
| Maghreb Congress | Ports, Sahara, anti-colonial diplomacy, North African identity balance. |
| East African Railway Congress | Askari veterans, railways, ports, Indian Ocean supply. |
| Great Lakes Council | Lakes, manpower, local political settlements, monarchy/republic tensions. |
| Congo Basin Charter | River transport, minerals, rainforest, high-chaos nonhuman/nature routes. |
| Zambezi-Stone Cities Authority | Great Zimbabwe/Mutapa-inspired legitimacy, copper/coal/rail, southern front. |
| South African Liberation Congress | RSA branch aftermath, mines, ports, anti-apartheid labour politics. |
| Indian Ocean Congress | Madagascar/islands, convoy lanes, naval support, coastal diplomacy. |

## Post-unification branch

### Africa Is One

Requires all African states under direct control, loyal subject control, or integrated federation control. This focus is not a simple coring button. It should:

- Clear or greatly reduce paper-core burden.
- Trigger the `Africa is one` super-event role label.
- Change cosmetic identity to a more explicit continental form.
- Unlock final leader/title/portrait/frame changes.
- Unlock the Second Scramble crisis.
- Unlock continent-sponsor paths only after the Second Scramble is handled or the unifier is strong enough to risk it.

### The Second Scramble

The user requested “Scramble for Africa” after Africa secures the continent. This should be an outside reaction, not a reward-only focus.

The crisis should include:

- Colonial holders and former holders react.
- Major powers with African-adjacent interests can form a crisis conference or intervention coalition.
- Diplomatic ultimatums, sanctions, naval blockades, border incidents, or direct war pressure.
- If colonial powers are already weak, the crisis can fail diplomatically and give Africa recognition.
- If they are strong, Africa must prepare for a major showdown.

### Continental Pole

After surviving or resolving the Second Scramble, Africa can become a world-chaos pole. This branch unlocks:

- Anti-colonial war goals outside Africa.
- Pressure against countries holding African-adjacent interests.
- Sponsorship of other continental unifiers.
- Dynamic naming for cross-continent unions.
- World-end path prerequisites.

## Sponsor other continent unifiers branch

Evolution III asks that Africa can trigger or sponsor Middle East, Europe, Asia, South America, and other continent unifiers. This should be a post-unification or near-post-unification route, not an early exploit.

Focus groups:

| Focus group | Gameplay |
| --- | --- |
| The Continental Export Office | Unlocks sponsor decisions for other continent unifier movements. |
| Middle East Charter | Sponsor Middle East/Arab/West Asian unifier. Africa can fund, arm, or pressure it. |
| Asia Charter | Sponsor Asian unifier, with higher cost and larger diplomatic risk. |
| Europe Charter | Sponsor European unifier, high danger, may provoke major powers. |
| South America Charter | Sponsor South American unifier across Atlantic/diaspora networks. |
| Continental Congress of Congresses | Creates a world congress of continent unifiers. |
| Pressure the Successful | If another unifier succeeds, Africa can negotiate union, federation, or annexation depending on route. |

## Dynamic union names

When Africa annexes, integrates, or federates with successful continent unifiers, the cosmetic identity should update dynamically.

| Controlled/Integrated continents | Working cosmetic name direction |
| --- | --- |
| Africa only | United Africa / African Union / African Congress state based on route. |
| Africa + Middle East | African-Middle Eastern Union, Afro-Arab Union, or Nile-to-Euphrates Congress depending on route. |
| Africa + Asia | Afroasian Union. If Middle East is also included, keep Afroasian rather than double-counting West Asia. |
| Africa + Europe | Afroeurasian Union. |
| Africa + Europe + Asia | Afroeurasian Union, with route-specific subtitle. |
| Africa + South America | Afro-Atlantic Union or Afro-South Atlantic Congress. |
| Africa + multiple non-Eurasian continents | World Congress/Continental Union wording until world-end path. |
| All continental unifiers integrated | The World Is One terminal path. |

Dynamic names must be backed by localisation, flags/cosmetic tags, and asset states. Do not hardcode one final name for every combination.

## World-end path focus branch

This branch remains locked until:

- Africa fully unifies and `Africa is one` has fired.
- World chaos is already in World Collapse / extreme chaos.
- Other continental unifiers exist.
- The other unifiers have pursued their post-unification path.
- The other unifiers have unlocked or accepted their own world-end branch.

Then Africa can pursue the World Is One ambition. The branch must be terminal and should coordinate with world-end scenario rules.

Focus groups:

| Focus group | Gameplay |
| --- | --- |
| A Congress of Continents | Summons or threatens all continent unifiers. |
| The Last Borders Are Administrative | Begins world integration meter. |
| One Charter Above Nations | Forces route choice: federation, empire, revolutionary union, military command, covenant. |
| Those Who Refuse the World | War/ultimatum branch against remaining independent powers. |
| The World Is One | Terminal world-end focus; fires world-end super-event role label and stops normal event firing. |

## RSA civil-war subtree

If RSA branch triggers, the normal tree is temporarily replaced or gated by a civil-war trunk.

Subtree lanes:

| Lane | Purpose |
| --- | --- |
| Congress Underground | Build African Congress legitimacy, labour support, rural networks, anti-apartheid agitation. |
| Mine and Port Strikes | Disrupt loyalist industry and gain local support at cost of supply and stability. |
| Defecting Units | Win over African soldiers, police, railway guards, and sympathetic officers. |
| Allied Pressure | Manage or resist Allied intervention and propaganda. |
| The Pretoria Test | Timed objective to control key South African cities. |
| Victory Settlement | Forces Allied peace and opens full Africa tree. |
| Loyalist Crackdown | If player is loyalist or AI loyalist wins, suppresses the attempt and creates aftermath. |

The civil-war subtree should be intense but not enormous; it is an entry branch, not a separate event as large as the entire Africa tree.

## Idea lifecycle plan

| Idea | Start/unlock | Role | Mitigation | Upgrade | Failure/corruption | Final form |
| --- | --- | --- | --- | --- | --- | --- |
| Paper Cores, Real Burdens | Starts with event. | Offsets all-African core grant. | Regional integration missions, statebuilding focuses. | Continental Administration. | Administrative Overreach. | Removed or converted after Africa Is One. |
| Continental Claim | Starts with event. | Legitimacy and war goal basis, raises alarm. | Diplomacy or war successes. | Africa Is One / Continental Pole. | Suppressed Claim if defeated. | Post-unification identity. |
| Improvised Congress | Starts with event. | Low authority, unstable decisions. | Opening trunk. | Federal Assembly / Liberation Committee / General Staff / Crown Council / Green Covenant. | Congress Fracture. | Route-specific government idea. |
| Colonial Alarm | Hidden/visible pressure. | Drives external reaction. | Diplomacy, recognition, slow integration. | Second Scramble. | Great Power Intervention. | Resolved after victory/recognition. |
| Charter League | Unlocks with faction. | Faction cohesion and shared war. | League branch. | Continental League / Federation / War Command. | Fractured Charter. | Continental order idea. |
| Diaspora Return Offices | Diaspora branch. | Skilled manpower/advisors. | Settlement/citizenship focuses. | Pan-Atlantic Congress. | Disappointed Returnees. | Stable return network. |
| Green Covenant Pressure | High-chaos route. | Supernatural power and risk. | Ritual controls, legitimacy. | Courts of Thunder / Forest Pact. | Unbound Covenant. | World-end route identity or removed if suppressed. |

## Reward diversity standards

The implementation must avoid filling this tree with political power, stability, war support, and flat ideas. Each branch should include concrete rewards:

- Buildings: factories, dockyards, ports, railways, supply hubs, forts, anti-air, infrastructure, airbases.
- Resources: oil, rubber, chromium, steel, aluminium, tungsten, food/grain abstraction where supported.
- Decisions: integration, aid, war planning, regional authorities, diaspora return, disaster prediction, sponsor unifiers.
- Missions: hold capitals, secure rail corridors, control ports, build regional administrations, defend members.
- Units: local militias, veterans, railway guards, desert columns, mountain troops, diaspora cadres, elephant corps.
- Politics: leader/council changes, party names, advisor pools, laws, cosmetic tags, flags, portraits.
- Diplomacy: faction invitations, recognition, guarantees, anti-puppet clauses, peace events, ultimatums.
- Mechanics: legitimacy, authority, cohesion, momentum, regional trust, colonial alarm, covenant pressure.

## Exploit checks for implementation

- No repeatable free core spam: cores are granted baseline but integration benefits must require work.
- No free unit loops: unit decisions require equipment, manpower, region control, cooldowns, or missions.
- No war-goal spam: colonial ultimatums and war goals use regional cooldowns and alarm costs.
- No puppet abuse: integration of subjects uses trust, authority, and time; not instant annex all.
- No influence farming: member influence has caps and decay, and excessive pressure can cause resistance.
- No bypass exploit: route switches should not allow collecting incompatible federal, revolutionary, military, crown, and covenant payoffs.
- No sponsor snowball: continent-unifier sponsorship requires post-unification progress and large costs.



## Revision 2 focus-tree expansion: Legacy Authority Lane and Impossible Congress

The focus tree must add a visible **Legacy Authority Lane** after the Charter League trunk. This lane reveals historical observer offices and Charter subjects by region: Western Roads, Nile and Stelae, Forest and River Crowns, Mint Cities and Islands, Southern Memory Courts. It should not become a linear list of claims. Each focus group unlocks decisions, missions, subject packages, local rivalries, integration-temperature changes, and route-specific AI behavior.

New anchor focus groups:

- **Inventory the Old Thrones:** reveal observer authorities in controlled or liberated regions.
- **Charter the First Legacy Office:** choose the first authority to become an observer, subject, or merged bureau.
- **Councils of the Western Roads:** unlock Jolof-Wolof, Mossi, Songhai, Hausa/Bornu/Futa/Segu packages.
- **Forest Crowns and River Titles:** unlock Kongo, Ndongo-Matamba, Luba, Lunda, Loango, Kuba, and central forest integration.
- **Nile and Stelae Compacts:** unlock Kush-Meroe, Makuria-Alodia, Sennar, Aksum, Adal-Harar, Ajuran.
- **Mint Cities and Lake Courts:** unlock Swahili Coast, Buganda, Bunyoro, Great Lakes Highlands, Nyamwezi/Hehe.
- **Stone, Flood, and Island Registers:** unlock Stone Cities, Mutapa/Rozvi, Barotse, Merina, Sakalava/Betsimisaraka, Comorian Passage, desert/frontier councils.
- **The League Must Not Become a Museum:** federal/modernizing safeguard that keeps historical offices from dominating the state.
- **The Museum Must Not Become a Prison:** anti-centralization safeguard that keeps the unifier from crushing local authority too cheaply.
- **The Continental Register:** late focus that turns the authority web into a continent-wide integration and defense interface.

At Evolution III/IV, add the hidden or route-locked **Impossible Congress** branch under Green Covenant:

- **The Trees File a Petition**
- **The First Nonhuman Envoys**
- **No Seats for Caricature**
- **The Forest Parliament**
- **Treaty of Teeth and Roots**
- **The Court of Thunder and Tides**
- **The Spider at the Signature Table**
- **The World Root Mandate**

These focuses unlock nonhuman/supernatural actors and disaster-warning mechanics, but must create major tradeoffs: Human Legitimacy loss, Colonial Alarm, Wild Mandate growth, Omen Reliability risk, and possible revolt by human authorities.

## Archive of Old Seats branch expansion

The main Africa focus architecture should include a dedicated **Archive of Old Seats** side branch. It should unlock after the Charter League exists and at least one regional authority is protected or controlled. It connects to political legitimacy, regional integration, and high-chaos absurd routes.

### Branch architecture

```text
Charter League established
  -> Open the Archive of Old Seats
      -> The First Regional Files
          -> Rivers and Crowns      -> West/Central dossiers
          -> Stone and Stelae       -> Meroe/Aksum/Kilwa/Great Zimbabwe monument routes
          -> Desert Books           -> Sahara/Sahel/Red Sea dossiers
          -> Lake Courts            -> Great Lakes/Madagascar dossiers
          -> Coastal Ledgers        -> Swahili/Atlantic/Indian Ocean port leagues
      -> Fork: Respect the Old Seats / Documents Before Consent / Seal Them Under One Archive
          -> Respect path: autonomy, legitimacy, old-court advisors, slower integration
          -> Counterfeit path: fast claims, forged regalia, exposure missions
          -> Central archive path: fewer subjects, stronger bureaucracy, higher local tension
      -> High-chaos fork: Sign the Bestiary Clause / Break the Bestiary Clause
          -> Bestiary Clause: nonhuman observers, Green Covenant, absurd units
          -> Break clause: rationalist/industrial extraction, anti-mythic stability, possible revolt
      -> Evolution IV finale: Charter Signs Itself / Parliament of Root and Fang route label
```

### Focus groups and roles

| Focus group | Narrative role | Mechanical role | Reward style |
| --- | --- | --- | --- |
| Open the Archive of Old Seats | The unifier admits that older political memories still matter. | Unlock dossier decisions, `archive_mandate`, dossier UI tab. | Decision category, scripted localisation, first archive idea upgrade. |
| The First Regional Files | The archive starts with places the unifier can actually reach. | Reveals nearby dossier pools only. | Targeted decisions and region lists, not global reveal. |
| Rivers and Crowns | West/Central court and river systems. | Songhai, Manden, Asante, Oyo/Benin/Ife, Kongo/Luba/Lunda/Kuba packages. | River guards, court advisors, trade-road missions. |
| Stone and Stelae | Monument legitimacy from Meroe, Aksum, Kilwa, Great Zimbabwe. | Site-protection missions and monument-based legitimacy. | Construction, rail, anti-air/forts, local guards, legitimacy. |
| Desert Books | Sahel, Sahara, Red Sea, and scholar/caravan routes. | Well networks, cavalry scouts, scholar courts. | Cavalry/motorized scouts, supply, train/convoy costs. |
| Lake Courts | Great Lakes and Madagascar. | Court roads, lake patrols, island autonomy. | Lake flotillas, hill detachments, port/road missions. |
| Coastal Ledgers | Swahili, Comorian, Atlantic, and Indian Ocean port authorities. | Customs houses, convoys, maritime autonomy. | Dockyards, convoys, naval XP, port defenses. |
| Respect the Old Seats | Federal/legalist settlement. | Better local trust, slower annexation, peaceful cores. | Advisors, autonomy decisions, long missions. |
| Documents Before Consent | Forgery/coercion settlement. | Faster paper cores and claims, exposure risk. | Claims, temporary compliance, scandal missions. |
| Seal Them Under One Archive | Centralized archive state. | Fewer autonomous subjects, stronger authority, higher resistance. | Bureaucratic idea upgrades, integration speed with unrest. |
| The Bestiary Clause | High-chaos legal absurdity. | Nonhuman observer seats and animal/supernatural packages. | New decisions, special units, nonhuman sovereignty. |
| The Charter Signs Itself | Evolution IV route label, not final localisation. | Nature/nonhuman parliament, world-union interaction. | Super-event direction, terminal path hook, huge risks. |

### Route tradeoffs

- The **Respect** path is slower and less explosive, but it creates the safest long-term integration and unlocks old-seat achievements.
- The **Counterfeit** path is powerful and aggressive, but every forged seal becomes a possible event, mission, or supernatural accusation.
- The **Central Archive** path is stable for large empires but angers local sovereignty movements.
- The **Bestiary** path is strong in forests, rivers, and high-chaos defensive wars, but it scares foreign powers and limits extraction.
- The **Anti-Bestiary** path keeps normal diplomacy, but can provoke the Great Forest or Great Herds into open resistance if nonhuman sovereignty was already high.

The implementation should not represent this as a single vertical chain. It needs at least one branch fork, several regional side lanes, and high-chaos late unlocks that stay hidden until eligible.


## Ruler/court display names in focus-route payoffs

Focus rewards that create or publicly recast a ruler/council identity can call the country-package localisation pool for source-language court-name flavour. The route should still be mechanically deep: old polities, Charter League politics, nonhuman/supernatural branches, Authority Atlas dossiers, and post-unification systems are not reduced to a naming gag.

The implementation may expose this through focuses such as a court proclamation, translation bureau, counterfeit crown, or foreign-legation embarrassment, but the exact focus names and layout remain implementation-owned.

## Archive of Old Seats focus-lane addendum

## Required Archive of Old Seats focus lane

The final implementation must include an **Archive of Old Seats** lane using the detailed design in `012_africa_niche_country_expansion.md`. This lane is a real branch family, not a flavour focus.

Minimum implementation requirements:

- One opener focus that unlocks the dossier decision layer.
- At least five regional dossier focus groups: West/Central, Stone/Stelae, Desert/Sahel/Red Sea, Lake/Madagascar, and Coastal/Indian Ocean.
- A three-way policy fork: respectful restoration, counterfeit/coercive restoration, and centralized archive integration.
- A late high-chaos Bestiary Clause fork.
- At least one Evolution IV focus group that links nonhuman/supernatural delegations to post-unification or world-union ambition.
- Focus rewards must include decisions, missions, advisors, state-building projects, local guards, claims/cores through integration, and mechanic value changes. They must not be mostly political power, stability, or new idea spam.
- Every focus group must have route-specific AI weights and focus filters/search tags.
