# Event 012 Africa — Niche Country Expansion and Absurd High-Tier Packages

This file expands the Africa event with a dedicated **Archive of Old Seats** system. It turns the user request for “more niche African countries” into playable, controlled content: historical polities appear as restoration dossiers, regional subjects, protectorates, compact members, or rare breakaway claimants, while absurd nonhuman and supernatural entities unlock only through high-chaos evolutions.

The goal is not to flood the map with dozens of microstates immediately. The goal is to make the continent feel politically alive: the unifier must decide whether old courts, port leagues, river states, mountain councils, forest guardians, and impossible high-chaos delegations become partners, puppets, rivals, masks, or ghosts in the archive.

## Design rules for the niche layer

1. **Historical polities begin as dossiers, not instant countries.** A dossier is a visible record, a local committee, a treaty archive, or a claimant network. It can mature into a subject, autonomous authority, integrated province, or rebellious rival.
2. **Every dossier needs a local reason to exist.** A coastal city-state uses ports and convoys. A Sahel emirate uses wells, cavalry, scholars, and desert roads. A forest kingdom uses court ritual, masks, roads, and trade. A stone-city route uses monuments and gold roads.
3. **Old seats can refuse.** Strong or prestigious dossiers should sometimes resist integration, demand autonomy, expose forged claims, appeal to foreign patrons, or join rival continental factions.
4. **The unifier can choose respect or fabrication.** Respectful restoration raises local trust and slows annexation. Counterfeit restoration gives faster compliance and claims, but creates scandal, revolt, and supernatural backlash at high chaos.
5. **High-chaos absurd actors are explicit nonhuman/supernatural countries or institutions.** They are not human ethnic caricatures. If implemented as countries, they need shared chaos-country and actual-nonhuman classification.
6. **Spawn caps protect usability.** The player should manage a curated set of active dossiers, not a wall of every possible tag.
7. **Final assets are source-gated.** Historical flags, symbols, and real leaders require sourced asset work. Fictional and nonhuman identities use generated assets.

## Unlock structure

| Layer | Unlock gate | What appears | Core value pressure |
| --- | --- | --- | --- |
| Archive I: Survey of Old Seats | Baseline after the unifier establishes the Charter League and controls/protects at least one region. | Dossier viewer, regional archive decisions, first local committees. | `archive_mandate`, `old_seat_legitimacy`. |
| Archive II: Restored Offices | Evolution I or strong regional authority. | Regional subject paths, guard units, local courts, treaty missions. | `local_sovereignty`, `regional_trust`. |
| Archive III: Contested Crowns | Evolution II / Rising Chaos. | Rival claimants, forged regalia, old-seat rebellions, elephant/logistics absurdity. | `restoration_debt`, `colonial_alarm`, `paper_core_burden`. |
| Archive IV: The Bestiary Clause | Evolution III / Chaos Tier. | Nonhuman observer seats, forest and river pacts, limited animal/supernatural auxiliaries. | `mythic_pressure`, `nonhuman_sovereignty`. |
| Archive V: Parliament of Root and Fang | Evolution IV / Totalen Chaos. | Nonhuman countries, supernatural courts, impossible ecological blocs, cross-continent covenant pressure. | `bestiary_alarm`, `covenant_pressure`, `world_threat` when abused. |

## New mechanic values

| Value | Meaning | What raises it | What lowers it | What it unlocks or blocks |
| --- | --- | --- | --- | --- |
| `archive_mandate` | Ability to open and administer old-polity dossiers. | Focuses, scholar missions, regional capitals held, monument protection. | Forgery scandals, looting, rejected dossiers, occupation abuse. | More active dossiers, better research speed, lower restoration cost. |
| `old_seat_legitimacy` | How believable local restoration work appears to the region. | Respecting autonomy, holding congresses, sourcing regalia, defending local states. | Instant integration pressure, fabricated lineages, puppet coercion, failed missions. | Peaceful integration, subject loyalty, old-court advisors. |
| `local_sovereignty` | How much autonomy restored offices expect. | Granting protectorate status, local assemblies, regional flags, historical charters. | Direct annexation, resource extraction, forged claims. | High value improves stability but slows coring; low value speeds integration but causes revolt. |
| `restoration_debt` | Accumulated promises owed to restored authorities. | Granting privileges, borrowing local troops, using old regalia for legitimacy. | Paying reconstruction costs, accepting autonomy, fulfilling missions. | Too high triggers refusal, rival congresses, or foreign appeals. |
| `mythic_pressure` | How much the archive has become supernatural rather than administrative. | High chaos, divine/nature court decisions, forged sacred claims, disaster prediction use. | Rationalist/archivist route, public courts, normal treaty law. | Unlocks supernatural powers and risks; can corrupt subjects into nonhuman/supernatural routes. |
| `nonhuman_sovereignty` | Recognition claimed by explicit nonhuman or ecological actors. | Bestiary Clause, forest autonomy, animal delegation victories, nature-court treaties. | Resource extraction, hunting crackdowns, refusing observer seats, mechanized clearing. | Unlocks nonhuman auxiliaries, observer seats, and eventual nonhuman countries; high value blocks normal annexation. |
| `bestiary_alarm` | Human panic and foreign propaganda about animal/supernatural governance. | Nonhuman tags, animal units in war, disaster miracles, supernatural ultimatums. | Careful concealment, diplomacy, limiting nonhuman seats, ecological treaties. | High value gives foreign powers intervention justifications and can trigger a Scramble variant. |

## Dossier lifecycle

Every niche polity should use the same lifecycle, tuned by region.

| Stage | Player-facing state | Actions | Outcomes |
| --- | --- | --- | --- |
| Rumour | The archive reports a name, seat, or claimant network. | Send researchers, inspect local support, choose whether to reveal the dossier. | Adds small legitimacy or exposes a fraud. |
| Charter Office | A local office appears under the Charter League. | Fund scribes, secure monuments, guard rail/port/well states, invite elders/courts/municipal councils. | Unlocks local decisions, adviser candidates, and subject path. |
| Local Guard | The office raises guards, scouts, cavalry, river patrols, or port militias. | Spend equipment, army XP, manpower, trains/convoys/fuel, or require unit presence. | Dynamic units appear; failure can arm rebels. |
| Council Seat | The dossier receives a League vote. | Grant observer/member seat, demand anti-puppet clauses, ask for tribute or manpower. | Raises cohesion if respected; raises debt if exploited. |
| Settlement | The dossier becomes autonomy, protectorate, integration project, puppet, or annexed authority. | Run integration missions or recognize local sovereignty. | Gives claims/cores gradually. Bad settlement causes revolt or foreign appeal. |
| Refusal / Revolt | The old seat rejects the unifier. | Negotiate, concede autonomy, suppress, or let stronger states leave and fight. | Creates war, split, or rival continental legitimacy. |

## Regional dossier matrix

### North, Sahara, and Nile

| Dossier / package | Core region | Unlock tier | Gameplay identity | Units and decisions | Refusal or absurd branch | Asset/source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Kushite-Meroitic Court | Sudan/Nile cataracts | Archive I | Monument/ironwork legitimacy. | `Protect the Royal Cemeteries`, `Reopen Cataract Foundries`, Nile guard infantry. | High mythic pressure creates a pyramid-court oracle that predicts floods and foreign offensives. | Historical symbols sourced; supernatural court generated. |
| Napatan River Guard | Upper Nile | Archive II | Defensive river authority. | River forts, supply-hub missions, rail-bridge guard templates. | Refuses if the unifier strips river autonomy. | Sourced historic motifs where possible. |
| Aksumite Stelae Office | Eritrea/Tigray/Red Sea route | Archive I/II | Red Sea inscription legitimacy and trade. | Stelae protection, port convoy missions, mountain detachments. | Can become a rival Red Sea claimant if ignored. | Historical assets sourced. |
| Zagwe Mountain Register | Ethiopian highlands | Archive II | Monastic/mountain administration. | Mountain fort, pilgrimage road, highland supply decisions. | With high mythic pressure, rock churches become disaster shelters and prophecy nodes. | Sourced/generative mix. |
| Punic Harbor Ledger | Tunisia/coastal Maghreb | Archive II | Naval finance and old harbor administration. | Convoy ledgers, naval XP, dockyard projects, elephant-corps memory focus. | Counterfeit route creates “Carthaginian Accountants” who demand impossible tribute. | Historical symbols sourced; absurd accountants generated icon only. |
| Numidia | Algeria/Tunisia/Morocco interior | Archive II | Mobile desert cavalry and anti-imperial memory. | Cavalry scouts, desert supply, motorized light cavalry conversion. | Can join or oppose Punic Ledger depending on autonomy. | Sourced motifs / generated unit icons. |
| Garamantian Well Network | Fezzan/Sahara | Archive III | Desert well and hidden-road control. | Well restoration, supply decisions, desert attrition mitigation. | High chaos opens mirage roads that move divisions unpredictably. | Source review required; mirage assets generated. |
| Aïr Caravan Subject | Niger/Sahara | Archive II | Tuareg/caravan law inspiration; living-community-sensitive. | Salt road convoys, camel scouts, desert diplomacy. | Leaves if exploited as a puppet cavalry farm. | Source review; no caricature icons. |
| Senussi Zawiya Network | Libya/Sahara | Archive II/III | Religious-desert resistance and diplomacy. | Safehouses, desert militias, foreign-recognition dilemmas. | Can denounce forged sacred claims. | Source review required. |

### West African rivers, courts, and savannas

| Dossier / package | Core region | Unlock tier | Gameplay identity | Units and decisions | Refusal or absurd branch | Asset/source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Wagadu Gold Road Survey | Mali/Mauritania/Senegal interior | Archive I | Old gold-road legitimacy. | Caravan guard, gold route survey, old capital mission. | Forged gold regalia scandal. | Historical motifs sourced. |
| Manden Charter Office | Mali/Guinea | Archive I | Griot/scholar and river legitimacy. | Congress decisions, river flotilla guards, book caravans. | Can expose counterfeit lineages and lower unifier legitimacy. | Source review for symbols. |
| Songhai River Authority | Gao/Timbuktu/Jenne | Archive I/II | Niger river state and scholar cities. | River patrols, mud-brick repairs, scholar guard. | Strong enough to resist integration if the unifier lacks trust. | Sourced historical images/symbols. |
| Takrur-Futa Toro Office | Senegal River | Archive II | Riverine Islamic reform and local legitimacy. | River levies, border missions, scholar courts. | Can demand religious autonomy. | Source review. |
| Jolof-Waalo-Cayor-Sine-Saloum Bloc | Senegambia | Archive II | Nested small-polity diplomacy. | Rotating claimant mediation, cavalry scouts, river tolls. | If mishandled, five minor refusals become one anti-unifier front. | Mostly source review; generated neutral council icon. |
| Futa Jallon Mountain Office | Guinea highlands | Archive II | Highlands, refugees, pastoral roads. | Mountain detachments, pass control missions. | Demands asylum/autonomy clauses. | Source review. |
| Massina Delta Council | Inland Niger Delta | Archive II | Marsh/rice/cattle logistics and jurist councils. | Delta crossings, food stores, cattle convoy. | High-chaos wetlands produce crocodile customs pact. | Historical sourced; crocodile pact generated. |
| Mossi Cavalry Houses | Burkina Faso/Ghana interior | Archive II | Inland cavalry and anti-raid defense. | Cavalry/motorized scout templates, fortified town missions. | Strong resistance; may leave the League rather than be annexed. | Source review. |
| Asante-Fante Gold Stool Subject | Ghana | Archive I/II | Gold, stools, forest roads, coast tension. | Forest-road missions, coastal fort tribunals, gold reserve decisions. | Refuses if sacred regalia is treated as generic compliance. | Historical symbols sourced with care. |
| Oyo Cavalry Road | Yoruba savanna/forest edge | Archive II | Cavalry roads and palace politics. | Cavalry conversion, road garrison missions, palace envoys. | Rival with Ife/Benin legitimacy if the unifier plays one against the other. | Source review. |
| Ife-Owo-Benin Court Register | Nigeria southwest/Edo | Archive I/II | Court craft, bronze/ivory legitimacy, forest diplomacy. | Court artisan offices, anti-looting missions, palace guard. | High mythic pressure can turn court masks into living witness events, not a monster route by default. | Historical art motifs sourced; supernatural variants generated. |
| Dahomey-Allada-Porto-Novo Ledger | Benin coast | Archive II | Palace guard, coastal diplomacy, reckoning with slave-fort legacies. | Anti-slave-fort tribunal, palace guard, coastal negotiations. | Predatory Museum route can weaponize history and cause moral/political collapse. | Historical symbols sourced; no glamorization. |
| Aro-Delta River Network | Niger Delta | Archive II/III | River commerce and oracle/diplomacy. | Canoe patrols, river intelligence, oil/port sabotage prevention. | High chaos creates Ananse-style contract loopholes across the whole charter. | Source review; Ananse assets generated and researched separately. |
| Nupe-Igala-Kwararafa Crossings | Niger-Benue | Archive II | River-crossing authority and cavalry mix. | Bridge missions, mixed cavalry/river guards. | Can become a swing bloc between Sahel and forest routes. | Source review. |
| Bamum-Grassfields Archive | Cameroon highlands | Archive II/III | Palace art, scripts, highland federation. | Archive scribe missions, hill militia, court-modernization adviser. | Forgery route can create fake scripts and “proof storms.” | Source review; absurd script-storm generated. |

### Central Africa and Kongo basin

| Dossier / package | Core region | Unlock tier | Gameplay identity | Units and decisions | Refusal or absurd branch | Asset/source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Kongo-Loango-Kakongo Customs Board | Congo/Angola coast | Archive I/II | River mouth customs, coastal diplomacy, anti-colonial church/court memory. | River forts, coastal customs, foreign mission bargaining. | Can appeal to Portugal/Belgium if abused. | Historical symbols sourced. |
| Ndongo-Matamba Queen’s Road | Angola interior | Archive I/II | Guerrilla corridors and queen-court legitimacy. | Ambush corridors, queen-court guards, fort-line missions. | If ignored, a Matamba claimant can lead a resistance war. | Real Queen Nzinga assets must be sourced if used; fictional successors generated. |
| Kasanje Mercenary Market | Angola/Congo trade routes | Archive III | Dangerous auxiliary and trade-soldier package. | Hire irregulars at high legitimacy cost, spend infantry equipment/army XP. | Can mutiny or sell claims to foreign powers. | Generated/sourced mixed. |
| Luba | Katanga/Congo | Archive I/II | Court offices, memory boards, copper and ivory routes. | Copper road, court council, memory-board legitimacy. | Forgery exposure hurts all Central African dossiers. | Historical source motifs. |
| Lunda Ring of Courts | Angola/DRC/Zambia | Archive II | Dynastic ring and long-distance diplomacy. | Court envoys, road guards, autonomy compacts. | Can resist annexation by forming its own ring of subjects. | Historical source motifs. |
| Kuba Raffia Court | Congo | Archive II | Court art, raffia administration, ritual office. | Administrative textiles, forest roads, militia guards. | At high mythic pressure masks can demand a vote; must stay supernatural, not horror caricature. | Historical motifs sourced; living masks generated. |
| Chokwe Caravan Office | Angola/Zambia/DRC | Archive II | Art, caravan, hunting-road and trade diplomacy. | Scout detachments, ivory route, border missions. | Refuses predatory extraction. | Source review. |
| Yeke-Garanganze Copper Authority | Copperbelt | Archive III | Copper resource state and strongman diplomacy. | Copper mines, rail hubs, security guards, foreign contract decisions. | Can become resource oligarchy breakaway. | Source review. |
| Lozi-Barotse Floodplain Authority | Zambezi floodplain | Archive II | Seasonal capitals, canoe logistics, floodplain administration. | Canoe transport, flood missions, supply bonuses in wetland states. | High chaos opens `The River Moves the Capital` event. | Source review/generated flood UI. |
| Azande-Mangbetu Forest Court | NE Congo/South Sudan | Archive III | Forest diplomacy, elite guard, borderland buffer. | Forest scouts, ambush lines, autonomy demands. | Forest Guardian Pact may subsume it if nonhuman sovereignty is too high. | Source review. |

### Horn, Red Sea, and Somali coast

| Dossier / package | Core region | Unlock tier | Gameplay identity | Units and decisions | Refusal or absurd branch | Asset/source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Ifat-Walashma Register | Eastern Shewa/Zeila links | Archive II | Muslim sultanate memory and highland buffer. | Border envoys, highland passes, legal courts. | Can contest Adal/Harar inheritance. | Source review. |
| Adal-Harar War Ledger | Harar/Zeila/Somali-Horn routes | Archive II/III | Highland-border war memory, musketeer route, Red Sea patrons. | Musketeer/irregular template, Red Sea port missions. | If foreign-backed, can refuse continental unifier integration. | Historical source review. |
| Ajuran Hydraulic Office | Somalia/Shabelle-Juba | Archive II | Wells, canals, fortified water points. | Well repair, supply water missions, camel guards. | Drought prophecy route under high mythic pressure. | Source review required. |
| Mogadishu-Merca-Barawa Port League | Somali coast | Archive I/II | City-state merchants and coinage. | Customs, convoy escorts, port AA/coastal forts. | Can become a rival Indian Ocean commercial league. | Source review. |
| Aussa-Afar Salt Gate | Afar/Red Sea approaches | Archive II | Salt routes and desert gatekeeping. | Salt-road convoys, desert scouts, port access. | Refuses if Red Sea route is sold to outsiders. | Source review. |
| Beja-Dahlak-Medri Bahri Chain | Red Sea/Sudan/Eritrea | Archive II | Island/coast/highland tolls. | Island convoy, coast forts, camel scouts. | Can sponsor a Red Sea neutral corridor. | Source review. |

### Swahili coast, Great Lakes, Madagascar, Indian Ocean

| Dossier / package | Core region | Unlock tier | Gameplay identity | Units and decisions | Refusal or absurd branch | Asset/source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Kilwa-Songo Mnara Coral Office | Tanzania coast | Archive I | Swahili trade, coral architecture, coinage. | Coral city restoration, convoy windows, customs houses. | Can demand maritime autonomy and resist inland command. | UNESCO/archival source mode. |
| Mombasa-Malindi Subject | Kenya coast | Archive II | Rival coastal city diplomacy. | Port rivalry arbitration, convoy/toll missions. | Can play foreign powers against the unifier if alarm is high. | Source review. |
| Pate-Lamu Book and Dhow Office | Kenyan coast | Archive II | Dhow routes and manuscript diplomacy. | Convoys, coastal scouts, archive protection. | High chaos creates a tidal archive that predicts invasions. | Source review/generated supernatural. |
| Zanzibar-Shirazi Maritime Register | Zanzibar/Tanzania coast | Archive II/III | Island port and plantation/anti-slavery reckoning. | Convoy, coastal forts, tribunal missions. | Foreign puppet risk if the unifier mishandles island autonomy. | Source review. |
| Comorian Island Congress | Comoros | Archive II | Small island diplomacy and naval bases. | Naval access, dockyard projects, convoy protection. | May demand equal League vote despite small size. | Source review. |
| Buganda-Bunyoro-Toro-Ankole Lake Board | Uganda/western lakes | Archive I/II | Court roads, lake fleets, cattle and hill administration. | Lake flotilla, hill levies, road missions. | Strong courts can leave and declare a defensive war. | Source review. |
| Rwanda-Burundi Hill Court | Rwanda/Burundi | Archive II | Centralized hill administration; high care. | Hill forts, administrative reform, local-trust missions. | No joke/absurd branch; only serious crisis routes. | Source review; no caricature. |
| Busoga-Karagwe-Buhaya Lake Corridor | Victoria/Kagera | Archive II | Lake trade and buffer states. | Lake patrols, rail/port missions. | Can swing between Buganda and Great Lakes Congress. | Source review. |
| Merina Imerina Register | Madagascar highlands | Archive I/II | Highland bureaucracy, island army, rice works. | Highland guard, rice field logistics, island road focus. | Can demand island autonomy before continental integration. | Historical source review. |
| Sakalava Boina-Menabe Subject | Madagascar west | Archive II | Coastal confederacy and naval access. | Coastal fleet, port missions, west-coast subjects. | Rival to Merina if coerced. | Source review. |
| Betsimisaraka-Antemoro Scribal Coast | Madagascar east/southeast | Archive II | Coastal coalition and writing/scribes. | Scribe office, coast guards, cyclone/disaster prediction path. | High mythic pressure creates storm-warning cult mechanics. | Source review/generated supernatural. |

### Southern Africa and Zambezi stone route

| Dossier / package | Core region | Unlock tier | Gameplay identity | Units and decisions | Refusal or absurd branch | Asset/source mode |
| --- | --- | --- | --- | --- | --- | --- |
| Great Zimbabwe Enclosure Office | Zimbabwe | Archive I | Stone city, gold routes, royal enclosure legitimacy. | Protect enclosure, gold-road rail mission, fortress restoration. | High mythic pressure creates stone-wall omen events. | UNESCO/archival source mode. |
| Mutapa-Rozwi-Butua Court Line | Zimbabwe/Mozambique/Zambia | Archive II | Successor courts and gold-road politics. | Court envoys, gold roads, mountain guards. | Can accuse the unifier of stealing stone-city legitimacy. | Source review. |
| Maravi-Chewa Lake Corridor | Malawi/Mozambique/Zambia | Archive II | Lake, iron, central-southern diplomacy. | Lake escorts, ironworks, local spirit offices. | High mythic pressure links to rain and famine predictions. | Source review/generated supernatural. |
| Zulu-Swazi-Sotho-Tswana Frontier Councils | South Africa/Lesotho/Eswatini/Botswana | Archive II/III | Military and frontier polities with living-community care. | Hill forts, cattle roads, commandos, peace missions. | If RSA civil-war branch active, these can become kingmaker or anti-unifier fronts. | Source review; no generic “warrior tribe” route. |
| Ndebele-Mthwakazi Guard | Zimbabwe/South Africa | Archive II | Mounted frontier guard and settlement politics. | Cavalry/motorized scouts, fort missions. | Can resist both RSA and northern unifier. | Source review. |
| Khoekhoe-San Restitution Offices | South Africa/Namibia/Botswana | Archive III | Land restitution, frontier memory, scouts. | Restitution missions, scout units, local trust recovery. | Refuses exploitation; no absurd branch. | Careful source review, generated neutral icons only if respectful. |

## High-tier absurd and nonhuman packages

These unlock only after the unifier has already built the Charter League, and only under the specified evolution/tier gates. They should not appear in ordinary baseline play.

### Evolution II: Bestiary liaison offices

These are not full countries by default. They are special unit, logistics, and decision packages that foreshadow the nonhuman routes.

| Office | Unlock | Gameplay role | Costs and risks | Follow-up |
| --- | --- | --- | --- | --- |
| Elephant Logistics Bureau | Rising Chaos and Central/East/Southern authority. | Heavy supply porterage, jungle/savanna breakthrough, slow armored support analogue. | Food/supply strain, high training time, colonial propaganda. | Can become Great Herds faction if abused or exalted. |
| Crocodile Ferry Inspectors | Delta, Nile, Zambezi, Niger, or Congo river control. | River-crossing bonuses and port sabotage detection. | Raises local fear and river accident events. | Can mature into Crocodile Rivers. |
| Ostrich Courier Service | Sahel/savanna route. | Fast desert message network; lowers mission durations. | High failure chance in bad terrain or heavy war. | Can be folded into mirage-road route. |
| Honeyguide Scout Subject | Forest and savanna edge. | Recon and hidden-depot discovery. | If ignored, leaks to Ananse Web. | Can become Honeyguide Commons observer seat. |
| Marabou Signal Towers | Nile/Sahel/Great Lakes. | Warning events and air-raid/supply notices. | Public unease and ominous event text. | Can feed divine-court prophecy path. |
| Termite Survey Office | Forest/savanna. | Construction speed for rail/supply/forts; detects weak buildings. | Can quietly eat stockpiles and paperwork. | Unlocks Termite Surveyor Republic at Evolution III/IV. |


### Court-name joke interaction

Counterfeit crowns, unprintable coronations, and fake claimants can use the source-language court/ruler name pool from `012_africa_country_packages_and_subjects.md`. Serious historical offices and living-community-adjacent dossiers remain respectful unless the route creates a separate fake claimant, propaganda alias, or absurd court mask. Nonhuman delegations use institutional speaker titles, not human personal-name pools.

### Evolution III: Nonhuman delegations

These can become observer seats, limited subjects, or rare country tags. If represented as countries, their leaders should be institutional or collective.

| Delegation / possible tag | Core region | Identity | Mechanics | Hard limits |
| --- | --- | --- | --- | --- |
| Gorilla Highlands Council (`GOR`) | Great Lakes/Congo highlands | Explicit nonhuman forest council. | Defensive forest infantry, intimidation, forest autonomy. | Cannot use normal ideology spread; no human leader names. |
| Chimpanzee Marshes (`CHP`) | Congo basin/forest wetlands | Nonhuman territorial caucus. | Ambush, sabotage, forest intelligence. | Must be written as nonhuman, not human-coded. |
| Bonobo Glasshouse Court (`BON`) | Congo basin | Nonhuman peace/panic court. | Lower internal violence, strange diplomatic penalties to militarists. | Avoid sexualized writing; collective leader only. |
| Okapi Court (`OKP`) | Ituri/Congo forests | Elusive courier and forest law office. | Hidden movement, scouting, escaped-column missions. | Minimal map presence; better as observer subject. |
| Crocodile Rivers (`CRK`) | Nile/Niger/Congo/Zambezi deltas | River tolls and terrifying ferry law. | River crossing, port/convoy controls, accident risk. | High `bestiary_alarm` if used offensively. |
| Baobab Senate (`BAO`) | Sahel/savanna | Impossible tree parliament. | Slow but huge legitimacy/restraint bonuses; can filibuster wars. | Cannot be annexed normally; can only be compacted or ignored. |
| Termite Surveyor Republic (`TRM`) | Forest/savanna construction zones | Nonhuman engineer state. | Rail/supply construction, sabotage against fortifications. | Eats civilian factory output if neglected. |
| Honeyguide Commons (`HGD`) | Forest/savanna | Scout commons and guide network. | Recon, hidden depot reveal, resistance detection. | Fragile; collapses if fighting devastates habitat. |
| Lion Arbitration Circuit (`LIO`) | Savanna | Predator court as symbolic coercive tribunal. | Fear-based arbitration, enemy surrender chance on weak targets. | Raises alarm and local sovereignty loss. |

### Evolution IV: Supernatural and ecological blocs

| Bloc / possible tag | Role | Unlock gate | Gameplay loop | Failure state |
| --- | --- | --- | --- | --- |
| Great Forest Federation (`OGF`) | Federation of Gorilla/Chimp/Okapi/Honeyguide/forest guardian seats. | At least three forest delegations recognized and high `nonhuman_sovereignty`. | Forest defence, ecological vetoes, anti-extraction ultimatums, supernatural ambushes. | If coerced, declares a forest war and invites nature courts. |
| Great Herds Compact (`HIC`) | Elephants and savanna animal logistics become a political force. | Elephant Bureau used repeatedly or consecrated by nature route. | Heavy auxiliaries, supply lines, stampede offensives, ivory-prohibition decisions. | Abused ivory/resource extraction triggers Great Herds revolt. |
| Tidemark Dominion (`TID`) | Mami Wata / river-sea supernatural compact. | Coastal/delta dossiers, high mythic pressure, storms or naval wars. | Convoy miracles, port flooding, enemy supply disruption. | Can flood friendly ports if promises are broken. |
| Dust Senate (`DUS`) | Sahara/desert spirits and mirage-road law. | Garamantes/Aïr/Senussi dossiers and high mythic pressure. | Desert teleport-adjacent missions, sandstorm disasters, well law. | Lost routes can strand armies and isolate capitals. |
| Masks That Vote (`MSK`) | Court masks become legal actors. | Benin/Kuba/Luba/Dahomey/Ife style court dossiers plus high mythic pressure. | Votes in League, exposes lies, protects court autonomy. | If forged, masks accuse the unifier and remove legitimacy. |
| Ananse Ledger (`WEB`) | Trickster contract intelligence network. | Aro/Akan/West African dossiers and high chaos. | Contract loopholes, spy networks, diplomacy traps. | Can trap the unifier in its own guarantees. |
| Orisha-Vodun Nature Courts (`OVN`) | Supernatural divine-court route. | Yoruba/Ewe/Fon/Akan-derived source routes plus Evolution IV. | Disaster prediction, divine sanctions, war miracles, ideological split. | Can overtake the Charter League if covenant pressure is ignored. |

## Absurd route families for the selected unifier

These are route overlays that any selected Africa unifier can unlock if it meets the gate. They should sit inside the focus tree and decision system, not replace normal African unification.

### Archivist Route — “The Record Must Survive”

The unifier treats historical polities as local partners and uses congresses, courts, and protected archives to build legitimacy. It gains slower integration but lower revolts.

- Focuses unlock archive surveys, monument protection, regional scholars, old court advisers, and local-law settlements.
- Decisions cost civilian factory time, trains, convoys, support equipment, and protection missions rather than only political power.
- Best for democratic/legalist, socialist-federal, and cautious monarchist/military routes.
- High payoff: old seats willingly convert paper cores into legitimate cores faster after long missions.
- Failure: too much restoration debt creates a League of Old Seats that can block continental wars.

### Counterfeit Crown Route — “The Seals Are Convenient”

The unifier fabricates lineages, seals, treaties, and documents to force the archive to support continental rule.

- Faster claims, faster integration, stronger war justification.
- Raises `restoration_debt`, lowers `old_seat_legitimacy`, and creates `forgery_exposure` missions.
- Strong for fascist, absolutist, and desperate military routes.
- High payoff: quick puppet conversions and temporary compliance spikes.
- Failure: old seats expose the fraud; high-chaos masks, Ananse contracts, or divine courts punish the unifier.

### Green Covenant Route — “The Land Is a Signatory”

The unifier lets forests, rivers, herds, and spiritual courts become political actors.

- Unlocks nonhuman observer seats, disaster prediction, forest defence, and ecological vetoes.
- Raises `nonhuman_sovereignty` and `mythic_pressure`.
- Strong defensive and logistics tools, but resource extraction and total-war choices become harder.
- Failure: nature courts can overrule the unifier, fracture the League, or trigger an ecological civil war.

### Bestiary Protectorate Route — “The Animals Have Papers”

The unifier gives legal personhood or protectorate status to nonhuman delegations.

- Unlocks Gorilla Highlands, Crocodile Customs, Baobab Senate, Elephant Bureau, and Honeyguide Commons.
- Great for absurd high-chaos play and defensive wars.
- Blocks some normal diplomacy and scares colonial powers.
- Failure: if the unifier treats them as disposable unit factories, the nonhuman delegates form a hostile Great Forest/Great Herds bloc.

### Predatory Museum Route — “Everything Old Must Obey”

The unifier plunders old seats, sacred regalia, monuments, and animal pacts to fuel conquest.

- Strongest short-term extraction: resources, manpower, compliance, war support.
- Causes immediate legitimacy collapse in multiple regions.
- Unlocks cursed units and disaster threats at high chaos.
- Failure: the Archive turns into a continent-wide accusation; old seats, supernatural courts, and nonhuman countries can coordinate against the unifier.

### World Zoological Parliament Route — “The Charter Has Too Many Signatures”

Evolution IV absurd route where human regional authorities and nonhuman/supernatural delegations create a continent-wide parliament that is powerful but barely controllable.

- Requires multiple recognized nonhuman delegations, at least one supernatural court, high League cohesion, and high `mythic_pressure`.
- Unlocks impossible diplomatic tools: wars can be vetoed by trees, rivers can demand tolls, animals can block railways, and court masks can expose secret treaties.
- Can become a bridge to “The World Is One” if other continental unifiers also accept nonhuman or supernatural legal actors.
- Failure: the parliament declares the unifier a temporary clerk and attempts to absorb the state apparatus.

## New decision families

| Family | Visible use | Example decisions / missions | Costs beyond PP/CP | AI logic |
| --- | --- | --- | --- | --- |
| Restoration Dossiers | Open and mature historical-polity dossiers. | `Open the [Region] Archive`, `Survey the Old Seat`, `Publish the Charter Record`, `Invite the Court to the League`. | Civilian factory burden, support equipment, trains, convoys, held capital/port/monument states, stability risk. | AI opens nearby dossiers first and avoids remote dossiers during major war. |
| Regalia and Monuments | Protect sites and symbols that create legitimacy. | `Guard the Royal Cemeteries`, `Repair Coral Stone Offices`, `Secure the Great Enclosure`, `Protect the Stelae Road`. | Divisions in named states, infantry equipment, support equipment, construction capacity, rail access. | AI prioritizes if it needs legitimacy or controls the required states. |
| Old Guard Mobilisation | Raise regional guard units without free-unit spam. | `Raise River Patrols`, `Call the Hill Levies`, `Convert Caravan Guards`, `Train Court Escorts`. | Manpower, rifles, support equipment, army XP, local support, mission success. | AI uses only when threatened or preparing a regional campaign. |
| Charter Autonomy | Negotiate autonomy, protectorates, or integration. | `Grant Observer Seat`, `Offer Protectorate Charter`, `Begin Integration Settlement`, `Demand Direct Rule`. | League Cohesion, Regional Trust, stability, war support, local sovereignty, restoration debt. | AI respects autonomy if weak; coerces only when strong and radical. |
| Forgery Crisis | Manage counterfeit claims. | `Silence a Counterfeit Claimant`, `Burn the False Seal`, `Double Down on the Lineage`, timed `Forgery Exposed` mission. | Legitimacy, spies/intel exposure, stability, court trust. | High-risk AI only for authoritarian routes. |
| Bestiary Clause | Unlock nonhuman observer seats. | `Grant Nonhuman Observer Seat`, `Negotiate Forest Autonomy`, `Ask the Crocodiles for Ferry Law`, `Hear the Baobab Senate`. | Mythic pressure, nonhuman sovereignty, habitat state control, local trust. | AI only at high chaos or Green Covenant route. |
| Supernatural Sanctions | Use nature/divine courts carefully. | `Request a Rain Omen`, `Ask the Masks to Test the Treaty`, `Let the River Judge the Port`. | Covenant Pressure, stability, cooldown, disaster risk, regional autonomy. | AI avoids unless desperate/high chaos. |

## Mission examples

| Mission | Duration band | Objective | Success | Failure |
| --- | --- | --- | --- | --- |
| Guard the Royal Cemeteries | 120–180 days | Keep supplied divisions in Nile/Meroe target states and keep rail access open. | +old-seat legitimacy, unlocks Kushite guard. | Looting scandal, local revolt risk, colonial propaganda. |
| Repair the Coral Office | 120 days | Control Kilwa/Zanzibar/Mombasa-style port group, spend convoys and civilian construction. | Swahili customs decisions and convoy bonus. | Coastal autonomy pressure and smuggler events. |
| Hold the Old Lake Roads | 150 days | Hold named Great Lakes capitals/ports and keep local trust above threshold. | Lake flotilla guard and court-road integration. | Great Lakes courts resist integration. |
| Prove the Seal | 90–150 days | Avoid forgery exposure while maintaining legitimacy and court support. | Counterfeit route claim bonus. | Public scandal and old-seat coalition. |
| Hear the Baobab Senate | 180 days | Do not start new wars while a savanna compact votes; keep supply and habitat damage low. | Massive legitimacy and nonhuman observer unlock. | Senate filibusters continental war goals. |
| River Judgment | 90 days | Maintain port order and avoid resource extraction decisions. | Crocodile Rivers grants river crossing powers. | Friendly port flooding and convoy loss. |

## Focus tree hooks

The Africa focus tree should gain an **Archive of Old Seats** side branch that can connect to political, regional, and high-chaos branches.

### Branch opener

- **Open the Archive of Old Seats**: unlocks dossier UI/decision tab and `archive_mandate`.
- **The First Regional Files**: reveals only dossiers inside controlled/protected regions.
- **Scholars Before Soldiers**: lowers restoration debt and improves legitimacy but slows coercive integration.
- **Documents Before Consent**: opens the Counterfeit Crown fork.

### Regional lanes

- **Rivers and Crowns**: West African and Central African court/river dossiers.
- **Stone and Stelae**: Great Zimbabwe, Meroe, Aksum, Zagwe, Kilwa, and stone/coral monument protection.
- **Desert Books**: Sahel, Sahara, Red Sea, and caravan dossiers.
- **Lake Courts**: Great Lakes and Madagascar routes.
- **Coastal Ledgers**: Swahili, Comorian, Atlantic, and Indian Ocean port compacts.

### Route locks

| Route | Locks out | Payoff |
| --- | --- | --- |
| Respect the Old Seats | Predatory Museum; strongest counterfeit choices. | Peaceful integration, more advisors, lower revolts. |
| Counterfeit the Lineages | Pure Archivist finale; some local-trust achievements. | Fast claims/cores, higher war tempo, scandal risk. |
| Seal Them Under One Archive | Full autonomy; extreme Green Covenant. | Centralized integration, stable bureaucracy, fewer special subjects. |
| Sign the Bestiary Clause | Anti-nonhuman rationalist route. | Nonhuman observer seats, absurd units, high-chaos paths. |
| Break the Bestiary Clause | Green Covenant / World Zoological Parliament. | Resource extraction, normal diplomacy, anti-mythic stability. |

### High-chaos focus groups

- **The Bestiary Clause**: opens nonhuman observer seats.
- **The Ape Delegates**: reveals Gorilla/Chimp/Bonobo/Okapi packages if Congo/Great Lakes forest regions qualify.
- **The Baobab Senate**: savanna parliament path; powerful legitimacy and war veto risks.
- **The Crocodile Customs Houses**: river tolls and port/river warfare.
- **The Masks Take Minutes**: court masks become legal witnesses and expose forgeries.
- **The Charter Signs Itself**: Evolution IV path toward World Zoological Parliament and nature-court domination.

## AI behavior

| Actor | Ordinary behavior | High-chaos behavior | Hard blockers |
| --- | --- | --- | --- |
| Selected Africa unifier | Opens nearby dossiers in controlled/protected regions; respects strong old seats if weak; uses autonomy to stabilize. | Can pick Counterfeit, Green Covenant, or Bestiary routes if ideology/chaos supports it. | Must not open remote dossiers without access; must not spawn nonhuman countries before gate. |
| Regional authority subjects | Support dossiers inside their region; resist direct annexation if local sovereignty is high. | Some convert into supernatural/nonhuman-aligned authorities. | Should not join foreign factions while protected unless trust collapses. |
| Historical dossier subjects | Seek autonomy, guards, and monument protection. | Strong dossiers can expose forgeries or lead old-seat coalition. | Must not receive generic full Africa tree unless promoted to a real subject. |
| Nonhuman delegations | Do not appear. | Seek observer seats, habitat protections, autonomy, and anti-extraction clauses. | No ordinary ideology spread, advisors, or human leader name pools. |
| Colonial powers | Use dossier disputes as propaganda and intervention pretexts. | Use `bestiary_alarm` to frame Africa as a world threat or justify new scramble. | Should not intervene if already defeated/peace-locked by continental outcome. |

## Asset requirements

Historical dossiers require a source-first asset approach. The asset prompt must not generate historical flags, well-attested symbols, or real leader portraits by default.

| Asset family | Source mode | Notes |
| --- | --- | --- |
| Historical dossier flags/seals | Sourced or historically grounded synthesis after source review. | Use neutral archive emblems if no attested flag exists; document uncertainty. |
| Historical leaders | Sourced portraits only. | Most dossiers should use councils/offices instead of real leaders unless sourced. |
| Dossier decision icons | Generated icons, but based on region-specific motifs after source review. | 32x32 readability. |
| Dossier focus icons | Generated/sourced motif icons. | Separate from decision/idea icons. |
| Nonhuman leaders | Generated collective or creature portraits. | Institutional names; no human random-name pools. |
| Supernatural court images | Generated. | Must be explicitly fictional/supernatural. |
| UI dossier tab | Generated/static UI panels plus possible animated warning seals. | Use frame-animation skill if animated. |
| Achievement icons | Generated. | Completed, grey, and ineligible variants when implemented. |

## Acceptance criteria for this expansion

- The implementation includes an Archive of Old Seats gameplay layer with at least regional dossier pools, not just flavour text.
- At least one dossier package exists for each macro-region: North/Nile, West, Sahel, Horn, Swahili/Indian Ocean, Central, Great Lakes, Southern, and Madagascar or island route.
- At least 24 historical dossier entries are implemented as either subjects, decisions, missions, advisors, route modifiers, or scripted dossier records. Full tags are optional, but visible gameplay is not.
- At least 6 high-chaos absurd/nonhuman packages are implemented, with at least 3 capable of becoming countries or observer subjects at Evolution III/IV.
- Historical dossier integration grants claims/cores only through staged settlement, not instant full cores.
- Nonhuman/supernatural tags are classified as special chaos countries and actual nonhuman where applicable.
- No human African polity is described with animalizing language.
- Dossier decisions use varied costs and map objectives.
- AI uses nearby, valid, route-compatible dossiers and avoids impossible remote targets.
- Asset manifests distinguish sourced historical symbols from generated fictional/nonhuman art.
- Achievements and prompts include the niche/absurd expansion so it cannot be skipped by implementation.


## Archive ruler-mask flavour

The Archive of Old Seats keeps serious polity names and researched office structures. Event-created office holders, fake restoration kings, regents, council heads, ritual clerks, bestiary observers, and archive commissioners can receive a source-language court/ruler display mask where the route is theatrical or high-chaos. Keep those display names untranslated and out of raw ids.

