# Event 012 — Country Packages, Regional Authorities, and High-Chaos Actors

## Country-package philosophy

Event 012 can select many different African-capital countries. It cannot assume one historical leader, one ideology, one flag, or one national story. The implementation must therefore build a flexible **Africa Unifier package** with route-specific identity layers and country-specific localisation hooks.

A selected country should keep enough of its starting identity to feel like the host matters. Ethiopia-led Africa, Liberia-led Africa, South Africa-led Africa, Egypt-led Africa, a newly released Congo-led Africa, and a small West African republic-led Africa should not read identically. The shared tree can be common, but the first events, starting issues, leader options, regional legitimacy, and route text should adapt.

## Selected unifier package

## Country and cosmetic naming style

Country names should be direct. Use the polity or region name first, with a route-appropriate state form when needed: `Asante`, `Kongo`, `Aksum`, `Nubia`, `Buganda Kingdom`, `Kilwa Sultanate`, `Funj Sultanate of Sennar`, `Rif Republic`, `Mossi Kingdoms`, or `Swahili Coast`.

Do not name countries after generic institutions such as compacts, offices, bureaus, commissions, boards, registries, military missions, colleges, guards, custodians, or authorities. Those terms are allowed for mechanics, decisions, focus groups, advisors, internal institutions, or subject-status notes, but the public country/cosmetic name should remain simple.

Ideology-specific variants should be used where they add flavour. Examples: a royal route can use `Kingdom` or `Sultanate`, a republican route can use `Republic`, a socialist route can use `Union`, `Commune`, or `People's Republic`, a military route can use a direct martial state name, and a high-chaos route can use a direct supernatural/nonhuman place-name without pretending the actor is a normal human state.

## Leader and court display-name flavour

Event 012-created or Event 012-recast ruler/council displays can use this untranslated source-language joke pool:

- `qaama saalaa koo xuuxaa`
- `haadha kee waliin wal qunnamtii saalaa raawwadhe`

Use the strings only in player-facing localisation or scripted localisation. Internal ids, file paths, tags, variables, sprite names, achievement ids, and asset filenames stay neutral. Historical country names, old-seat polity names, office names, symbols, flags, and source notes remain researched. Nonhuman/supernatural packages use institutional speaker/body wrappers instead of ordinary human personal-name framing.

### Required surfaces

| Surface | Requirement |
| --- | --- |
| Country identity | Every transformed country needs cosmetic name, adjective, flag path, and ideology-specific variants where relevant. |
| Leader/council display | Event-created or Event-recast public ruler/council displays can draw from the source-language joke pool above; serious institutional and historical names remain intact. |
| Portrait | Real leaders use sourced portraits; fictional/council/high-chaos leaders use generated portraits with route-appropriate personal, institutional, or court-mask display names. |
| Starting problems | Every meaningful country begins with at least one problem to solve: legitimacy, command, supply, industry, faction trust, or foreign pressure. |
| Unit path | Every fighting actor gets dynamic starting units and at least one reinforcement path through focuses, decisions, objectives, volunteers, depots, or special mechanics. |
| AI path | Every country package receives AI route behaviour, refusal logic, and invalid-route blockers. |

### Selected-country archetypes

| Archetype | Examples | Starting identity hooks | Mechanical tilt |
| --- | --- | --- | --- |
| Ancient/imperial legitimacy | Ethiopia or similar monarchy/highland state | Aksum, Solomonic/imperial rhetoric where applicable, mountain defence, anti-Italian memory if relevant. | Easier Crown Congress; stronger Legitimacy; strong mountain troops; slower modern industry. |
| Diaspora republic | Liberia or similar | Returnee politics, Atlantic ties, constitutionalism, foreign dependence risk. | Strong diaspora branch; weaker starting army; better recognition; stronger port/diplomacy path. |
| Industrial southern state | RSA branch or other industrialized south | Mines, ports, labour, racial politics, Allied entanglement. | Strong industry but severe legitimacy/civil-war risks; RSA special branch. |
| Nile or North African state | Egypt/modded North African capitals | Nile logistics, Arab-African balance, Mediterranean diplomacy, old state bureaucracy. | Strong diplomacy/logistics; tension with Maghreb/Sahara and Middle East identity paths. |
| Recently released state | Independence Wave or collapse-created African tag | Fragile legitimacy, new flag, local liberation story. | High Legitimacy potential but weak industry; regional authority interactions. |
| Small unifier | Minor one-state African country | Absurdity and underdog fantasy. | High paper-core burden, strong focus/decision help, dynamic unit package must scale enough to survive. |
| Subject or protectorate | African subject with capital in Africa | Anti-patron crisis, hidden independence networks. | Starts with patron pressure and liberation route; may need breakaway event before full tree. |

### Implemented selected-unifier origin layer

The live implementation classifies the selected host into Highland Legacy, Atlantic Return Route, Union Rupture, Nile Sea Gate, Western Congress Ports, Congo River-Forest Mandate, Indian Ocean Gate, or General Congress Mandate. Each profile receives a distinct opening spirit, mapped value movement, a small logistics grant, AI posture coverage, and visible Continental Congress localisation.

The same profile then drives an active origin mandate case after the Charter Mandate focus. The Continental Congress decision spends political power, support equipment, and profile-specific logistics before starting a 120-day mission. The mission checks capital control and profile-specific value gates: highland profiles use Authority and Old-Seat Legitimacy; Atlantic Return profiles use Legitimacy, Regional Trust, and Restoration Debt discipline; RSA uses Liberation Momentum, Authority, and Colonial Alarm discipline; Nile/Red Sea uses Archive Mandate, Old-Seat Legitimacy, and Authority; West Atlantic uses League Cohesion, Liberation Momentum, and Legitimacy; Congo/forest uses Regional Trust, Habitat Trust, and a Mythic Pressure cap; Indian Ocean uses Legitimacy, League Cohesion, and Colonial Alarm discipline; the general profile uses Legitimacy and Authority. Success gives another profile-specific value shift and files the case, while failure damages Legitimacy and Authority and raises Colonial Alarm and Restoration Debt before the case can be retried.

## Dynamic starting forces

The selected unifier is expected to fight. It must not receive a flat generic army.

Starting force should scale from:

- Number of owned/core states.
- Controlled population and industry.
- Current manpower and equipment stockpile.
- Chaos tier and event evolution state.
- Whether it is at war.
- Whether it is a subject or independent.
- Whether RSA civil war branch is active.
- Whether the host already has a meaningful army.

### Force package bands

| Band | Situation | Starting military design |
| --- | --- | --- |
| Weak opening | Tiny unifier, low industry, few states. | Capital Defence Committees, irregular infantry, small equipment grant, emergency training decisions, first regional authority support. |
| Normal opening | Medium country with some industry. | Regular infantry core, militia support, staff office, limited artillery/support, logistics penalties until reforms. |
| Severe opening | Already at war or high colonial threat. | Additional militia, emergency garrisons, defensive buffs, early aid corridor decisions. |
| High-chaos opening | Chaos tier high or evolved pre-fire. | Stronger irregulars, weird volunteer cadres, possible elephant logistics unlock later, higher alarm. |
| RSA civil war | RSA in Allies selected. | Split forces between loyalist and Congress sides; loyalists better equipped, Congress higher manpower/support growth. |

### Template families

| Template | Story | Unlock/source |
| --- | --- | --- |
| Capital Defence Committees | Improvised local defenders. | Event start for weak/normal unifier; cheap but low training. |
| Congress Guard | Political/security troops guarding offices and rail hubs. | Statebuilding focuses and decisions. |
| Liberation Columns | Mobile anti-colonial infantry. | Liberation Staff branch. |
| Railway Guards | Supply and rail-protection units. | Railway War Offices / regional missions. |
| Desert Columns | Camel/cavalry/motorized/light infantry abstraction. | Sahel/Sahara branch. |
| Highland Schools | Mountain infantry. | Nile-Horn/Ethiopian/Rift branch. |
| Port Defence Brigades | Coastal and port garrison units. | Port Congresses / island branch. |
| Diaspora Cadres | Volunteer formations with better support/research but limited number. | Diaspora return branch. |
| Elephant Logistics Corps | High-chaos/special support or battalion. | Evolution II and military/covenant path. |
| Forest Guardian Allies | Nonhuman/supernatural assistance, not ordinary recruited humans. | High-chaos pact; classified separately. |

## Regional authorities

Regional authorities are the core method for avoiding immediate annexation. They should be real subjects/faction members with specific identities, not a single generic puppet repeated ten times.

### Shared authority rules

All regional authorities should:

- Spawn only when the unifier controls enough of their region or chooses release/federation settlement.
- Receive a local flag, name, ruling council/leader, starting ideas, small but useful forces, and regional decisions.
- Begin as subjects or charter members, not full annexed land.
- Provide integration progress and local military support.
- Have a trust/resistance value.
- Be eligible for peaceful integration, protectorate status, or federation.
- Be able to resist if abused, especially under military/forced integration routes.
- Use regional localisation and asset direction.

### West Africa (`WAC`, placeholder)

**Identity:** port unions, Pan-African congress politics, Gold Coast/Lagos/Dakar/Bamako networks, Ghana-Mali-Songhai historical memory.

**Starting problem:** coastal cities and inland authorities disagree over whether the Congress is a federation, revolution, or empire.

**Military style:** port guards, riverine supply, light infantry, veteran cadres, logistics.

**Economy:** gold/cocoa/trade/ports; early diaspora return gateway.

**Route hooks:** federal and revolutionary routes both strong; crown route can invoke Mali/Songhai ceremonial memory; high-chaos Ananse web can appear here.

**Assets:** flag based on fictional congress seal, not a fake historical flag; sourced symbols only if using real attested motifs; generated council portrait.

### Sahel (`SAH`, placeholder)

**Identity:** desert roads, caravan networks, oasis towns, Sahelian cavalry/motor columns, trans-Saharan logistics.

**Starting problem:** supply, drought, and thin control over vast spaces.

**Military style:** desert columns, cavalry/motorized units, raiders, scouts.

**Economy:** roads, infrastructure, trans-Saharan trade, desert supply depots.

**Route hooks:** military route excels; federal route lowers revolt risk; crown route uses old caravan authority; high chaos can unlock storm/drought prophecy.

**Assets:** fictional desert road seal, decision icons for oasis/convoy/rail.

### Maghreb Coast (`MAG`, placeholder)

**Identity:** Mediterranean ports, Sahara gateway, anti-colonial diplomacy, Arab-African identity balance.

**Starting problem:** foreign navies, metropolitan ties, identity tension with Middle East and African routes.

**Military style:** port defence, mountain/desert units, anti-naval convoy missions.

**Economy:** ports, rail, oil/minerals where applicable.

**Route hooks:** important for Africa + Middle East dynamic union and Afroeurasian later.

**Assets:** fictional congress flag; historical symbols must be sourced if used.

### Nile-Horn (`NHR`, placeholder)

**Identity:** Nile corridor, Horn of Africa, Aksum/Kush/Ethiopian highland legitimacy, Red Sea.

**Starting problem:** competing old states, mountain supply, Red Sea external pressure.

**Military style:** highland/mountain troops, Red Sea port guards, defensive cadres.

**Economy:** Nile agriculture, Red Sea ports, mountain roads.

**Route hooks:** Ethiopia-led unifier gets extra legitimacy; crown route strong; military route gets mountain schools.

**Assets:** if using real Ethiopian or Coptic/Islamic symbols, source carefully; fictional league seal otherwise.

### East African Railways (`EAC`, placeholder)

**Identity:** railways, ports, askari/veteran memories, Indian Ocean trade, anti-colonial campaigns.

**Starting problem:** colonial rail infrastructure and coastal-inland tension.

**Military style:** railway guards, askari veteran cadres, light infantry.

**Economy:** rail, ports, infrastructure, supply hubs.

**Route hooks:** revolutionary liberation camps; federal regional autonomy; high-chaos Mami Wata coastal route.

**Assets:** rail/port focus icons and faction emblem.

### Great Lakes (`GLK`, placeholder)

**Identity:** lake networks, inland kingdoms/republics, manpower and food, regional diplomacy.

**Starting problem:** local rivalries and external borders can make integration fragile.

**Military style:** infantry manpower, lake supply abstraction, defensive units.

**Economy:** agriculture, infrastructure, lakeside supply.

**Route hooks:** federal route safest; military pressure can trigger resistance; crown route can be strong if titles are respectful and non-specific.

**Assets:** lake-and-sun council seal, generated council portrait.

### Congo Basin (`CBC`, placeholder)

**Identity:** Congo river system, rainforest logistics, minerals, rubber, resource sovereignty, high-chaos nature entry.

**Starting problem:** enormous terrain, resource extraction, colonial legacy, weak roads.

**Military style:** river guards, jungle infantry, supply-light units.

**Economy:** minerals/rubber/river transport; high potential, high burden.

**Route hooks:** high-chaos “Forests That Refuse the Border” can appear here; nonhuman forest guardian pact must be handled sensitively.

**Assets:** river/forest seal, possible high-chaos animated forest pact emblem.

### Zambezi-Stone Cities (`ZSC`, placeholder)

**Identity:** Great Zimbabwe/Mutapa/Maravi echoes, copper/coal/rail, southern interior.

**Starting problem:** rail, mines, southern colonial pressure, links to RSA branch.

**Military style:** rail guards, infantry, mine-protection units.

**Economy:** copper/coal/steel/mining, infrastructure.

**Route hooks:** industry branch strong; crown route can invoke stone-city legitimacy carefully; military route creates southern war plan.

**Assets:** stone-wall emblem, mining/resource icons.

### South African Liberation (`SLC`, placeholder)

**Identity:** anti-apartheid and labour politics, mines, ports, RSA civil-war aftermath.

**Starting problem:** racial state collapse, loyalist remnants, Allied settlement, mine economy.

**Military style:** strike guards, mine/rail brigades, urban militias, veteran cadres.

**Economy:** mines, factories, ports; strong but politically volatile.

**Route hooks:** only spawns through RSA branch or southern integration; revolutionary/military/federal routes all interact differently.

**Assets:** generated liberation congress flag; real movement symbols require sourcing and permissions if used.

### Indian Ocean (`IOC`, placeholder)

**Identity:** Madagascar, Comoros, Mauritius, Seychelles, Indian Ocean routes.

**Starting problem:** islands are hard to supply and easy for navies to isolate.

**Military style:** port defence, naval/convoy support, marines if available.

**Economy:** ports, convoys, dockyards, trade.

**Route hooks:** diaspora and maritime routes; Africa + Asia route; Mami Wata coast route.

**Assets:** ocean/ship/star seal, naval decision icons.

## High-chaos supernatural and nonhuman actors

These are optional high-chaos content. They should not appear in grounded baseline play. They should be rare, dramatic, and clearly classified.

### Orisha/Vodun/Nature Courts

Inspired by West African religious concepts, but implementation must avoid claiming a single universal African religion. Use broad fictional “courts,” “covenants,” or “shrines” and leave specific deity references to researched/sensitive localisation. The route can draw design inspiration from the idea that divine power converges with natural force and witnessed objects, but it should not flatten living religions into combat spells.

Gameplay:

- Weather prediction.
- Storm/flood/drought warning missions.
- High-risk disaster ultimatums against colonial holders.
- Legitimacy and Covenant Pressure tradeoffs.
- Special report events where governments disagree whether events are natural, sabotage, or supernatural.

### Ananse Web

Ananse is a trickster/wisdom figure in Akan tradition and broader West African cultural memory. The game route should use this as an intelligence, deception, puzzle, and sabotage theme rather than a monster-spawn route.

Gameplay:

- Infiltration of colonial administrations.
- False orders and telegraph confusion.
- Member-infiltration detection.
- Rare “least expected turn” events where a stronger power’s plan backfires.

### Mami Wata Tidemarks

Mami Wata traditions are associated with water, prosperity/healing, danger/destruction, snakes/divination, and Atlantic survival. Use as coastal/river high-chaos route with respect.

Gameplay:

- Port protection.
- Flood/storm prediction.
- Convoy disruption.
- Healing/recovery events after coastal disasters.
- High-risk retaliation when colonial fleets ignore warnings.

### The Great Herds

Elephant units and logistics should be strange but not cartoonish. Use them as high-chaos military-symbolic support.

Gameplay:

- Supply movement in rough terrain.
- Breakthrough and intimidation at high cost.
- Terrain-specific strengths and vulnerabilities.
- Special focus/idea/animation asset.

### Congo Basin Primate Confederacy / Forest Guardian Pact

This is the only place where gorilla/chimpanzee “nation” ideas can be safely used, and only under strict rules:

- Explicitly nonhuman high-chaos actor.
- Spawns only in rainforest/Congo Basin high-chaos route.
- No human names, human ethnic caricature, human parties, or human politics.
- Classified as `is_actual_nonhuman_country` and `is_special_chaos_country` if implemented.
- Uses institutional/symbolic leader name such as “The Forest Council,” not a personal human name.
- Does not replace or parody human regional authorities.
- Can ally, refuse borders, sabotage extractive colonial states, or demand forest protections.

Gameplay:

- Forest zones become difficult for colonial occupiers.
- Resource extraction decisions can anger the pact.
- Federal/Green Covenant path can negotiate.
- Military/extractive path can provoke war.
- If integrated respectfully, it gives jungle defense and disaster prediction; if abused, it becomes a hostile nonhuman actor.

## Party and ideology naming directions

The selected unifier and authorities need route-specific party names.

| Route | Party/council direction |
| --- | --- |
| Federal Congress | African Federal Congress, Charter Assembly, Congress of Regions. |
| People’s Liberation Front | Pan-African People’s Front, Liberation Committee, Workers’ and Peasants’ Congress. |
| Continental General Staff | Continental Defence Directorate, General Staff Council, Emergency War Office. |
| Crown Congress | Council of Old Seats, Crown Congress, High Council of Thrones. |
| Green Covenant | Green Covenant, Courts of River and Storm, Forest/Tide/Web councils. |
| RSA loyalist | Union Emergency Cabinet, Allied Union Directorate, HNP/SAP/UP variants if historically routed. |

Names should be localised by selected country and route where feasible. Do not reuse one generic name everywhere.

## Leader and portrait rules

- Existing real leaders use their existing or sourced portraits.
- New fictional one-person leaders use actual-ish regional/gender name pools in grounded routes; event-recast public display names can instead draw from the source-language court-name pool above.
- Female-presenting generated portraits require female name pools and female leader metadata where supported.
- Male-presenting generated portraits require male name pools and must not use female metadata.
- Councils, congresses, courts, directorates, forest pacts, and symbolic bodies use institutional names in grounded routes; absurd human joke-route councils may use `Court of [GetAfricaAbsurdObsceneName]` style aliases, while nonhuman actors keep institutional names.
- Animated portraits are reserved for major route transformations: Africa Is One, high-chaos covenant, Crown Congress final, RSA victory aftermath, world-end path.


## Country-specific opening flavour examples

These are directions, not final localisation:

| Host | Opening angle |
| --- | --- |
| Ethiopia | “The highlands have seen empires come and go; now the claim descends from the mountains into ports, deserts, and rivers.” |
| Liberia | “The Atlantic return route becomes the first road of the Congress; diaspora politics are central from day one.” |
| South Africa | “The proclamation breaks the Union before it can claim the continent; civil war if in Allies.” |
| Egypt/Nile state | “The Nile offices claim that Africa cannot be divided from its river roads and sea gates.” |
| West African republic | “Ports, unions, and congress halls move first; old Sahelian and Atlantic networks wake behind them.” |
| Congo Basin state | “Rivers and forests make the proclamation hard to map; high-chaos routes have early hooks.” |
| Small island/Indian Ocean host | “The unifier begins from a sea gate and must build continental legitimacy through convoys and diplomacy.” |

## Acceptance criteria for country packages

Implementation is incomplete if:

- The selected unifier uses the same text and route identity regardless of host archetype.
- Regional authorities are generic tags with copied flags/leaders/ideas.
- RSA branch lacks civil-war forces, Allied peace, and post-victory transition.
- High-chaos nonhuman actors are not registered or are treated as human countries.
- Historical symbols or real leader portraits are generated instead of sourced.
- New fighting authorities spawn with no starting units or no reinforcement pathway.
- Flags, ideology names, party names, leader portraits, focus tree loading, AI, and localisation are not aligned.



## Revision 2 expansion hook: niche authorities and absurd higher-tier actors

The subject layer is expanded by `012_africa_niche_polities_and_subjects.md` and `012_africa_high_chaos_absurd_paths.md`. Those files are now source design, not optional flavour. The implementation should add a large set of historical/legacy observer authorities and Charter subjects before relying on the supernatural layer.

New human legacy authorities include, at minimum, Jolof-Wolof, Mossi, Songhai, Oyo, Benin, Dahomey, Asante, Kongo, Luba, Lunda, Kush-Meroe, Aksum, Ajuran, Swahili Coast, Buganda, Stone Cities/Great Zimbabwe, Barotse Floodplain, and Merina Rova. Additional second-priority authorities include Hausa, Bornu, Baguirmi-Wadai, Futa, Segu-Bambara, Ndongo-Matamba, Loango, Kuba, Makuria-Alodia, Sennar, Adal-Harar, Bunyoro, Great Lakes Highlands, Nyamwezi, Maravi, Sakalava/Betsimisaraka, Comorian Passage, Nama-Herero-Damara, Khoe-San Tracks, and Zulu-Nguni military colleges.

High-chaos nonhuman and supernatural actors are added only through the Green Covenant/Impossible Congress lane and require explicit nonhuman/supernatural treatment. Gorilla Nation, Chimpanzee Assembly, Bonobo Kinship Congress, Great Herds, Crocodile Rivers, Hyena Radio Dominion, Termite Citadel Engineers, Baobab Senate, Locust Customhouse, Giraffe Signal Towers, Okapi Court, Orisha/Vodun Nature Courts, Ananse Web, Mami Wata Tidemark, and Bird of the Walls must not be presented as human African countries. They are Covenant actors with separate mechanics, assets, AI, and classification.

## Niche polity restoration layer

The country-package surface now includes a full **Archive of Old Seats** layer. The detailed design lives in `specs/012_africa_niche_country_expansion.md` and the research basis lives in `research/012_africa_niche_polities_research_addendum.md`.

This layer adds many niche African polity inspirations without turning the opening event into instant map spam. Historical polities appear first as **restoration dossiers**. A dossier can become a local office, observer seat, subject authority, protectorate, integration project, or rebel claimant depending on the unifier's route, local trust, and chaos tier.

### Minimum regional coverage

| Macro-region | Required dossier examples | Gameplay promise |
| --- | --- | --- |
| North/Nile | Kush/Meroe, Aksum/Zagwe, Punic Ledger, Numidia, Garamantes wells. | River monuments, ironworks, Red Sea and desert logistics. |
| West/Senegambia | Manden, Songhai, Jolof/Waalo/Cayor/Sine/Saloum, Futa Toro/Jallon, Asante/Fante, Oyo/Ife/Benin/Dahomey/Aro. | River charters, gold roads, palace courts, cavalry roads, anti-fort tribunals. |
| Sahel/Lake Chad | Kanem-Bornu, Hausa/Sokoto/Gwandu, Wadai, Darfur, Funj/Sennar, Massina. | Desert cavalry, scholars, wells, old emirate integration and refusal. |
| Horn/Red Sea | Ifat, Adal/Harar, Ajuran, Mogadishu/Merca/Barawa, Aussa/Afar, Beja/Dahlak. | Port cities, well systems, highland-border routes, Red Sea diplomacy. |
| East/Indian Ocean | Kilwa, Mombasa, Malindi, Pate-Lamu, Zanzibar, Comoros. | Dhow routes, coral offices, convoy and customs decisions. |
| Central/Kongo | Kongo/Loango, Ndongo/Matamba, Luba, Lunda, Kuba, Chokwe, Yeke, Lozi. | Court offices, river customs, copper/ivory routes, queen-court and floodplain paths. |
| Great Lakes | Buganda, Bunyoro, Toro, Ankole, Rwanda, Burundi, Busoga, Karagwe. | Lake fleets, hill courts, cattle/road logistics, careful integration. |
| Southern/Zambezi | Great Zimbabwe, Mutapa, Rozwi, Maravi, Zulu/Swazi/Sotho/Tswana, Khoekhoe/San offices. | Stone-city legitimacy, gold roads, lake corridors, restitution offices, RSA-civil-war tie-ins. |
| Madagascar/islands | Merina, Sakalava, Betsimisaraka, Antemoro, Comorian Congress. | Highland bureaucracy, coastal coalitions, island fleets, scribal networks. |

### Historical package handling

- Historical dossiers are not automatically full country tags. The implementation can represent them as scripted dossier records, local subjects, regional authority modifiers, or country packages when the map state justifies a separate tag.
- Final historical flags and symbols require sourced asset work. If no attested flag is usable, create a historically grounded neutral seal and document the uncertainty.
- Real leaders require sourced portraits. Most old-seat packages should use councils, offices, courts, boards, or congresses to avoid invented historical leaders.
- Dossier integration should grant paper claims first, then local trust and integration missions, and only then cores.

## Expanded absurd high-chaos actors

High-chaos nonhuman and supernatural actors are now broader than the initial forest and nature packages. These unlock through the Bestiary Clause and Parliament of Root and Fang paths described in `012_africa_niche_country_expansion.md`.

| Actor | Tier gate | Identity | Country-package rule |
| --- | --- | --- | --- |
| Gorilla Highlands Council | Evolution III | Explicit nonhuman forest council. | Institutional leader, actual-nonhuman classification, forest autonomy mechanics. |
| Chimpanzee Marshes | Evolution III | Nonhuman marsh/forest caucus. | Sabotage/intelligence route; no human names or caricature tone. |
| Bonobo Glasshouse Court | Evolution III | Nonhuman collective court. | De-escalation and panic-diplomacy mechanics; no sexualized writing. |
| Okapi Court | Evolution III | Elusive courier and forest law office. | Observer subject by default; rare full country only if forest route dominates. |
| Crocodile Rivers | Evolution III | River toll and ferry-law board. | River crossing/port mechanics with accident risk. |
| Baobab Senate | Evolution III/IV | Impossible tree parliament. | War-veto and legitimacy mechanics; cannot be annexed normally. |
| Termite Surveyor Republic | Evolution III/IV | Nonhuman construction/sabotage engineers. | Rail/supply construction and fort sabotage; eats output if neglected. |
| Honeyguide Commons | Evolution III | Scout and guide network. | Recon and depot discovery; fragile habitat dependency. |
| Lion Arbitration Circuit | Evolution III/IV | Predator court as coercive tribunal. | Fear arbitration and surrender pressure; raises Bestiary Alarm. |
| Great Forest Federation | Evolution IV | Federation of forest nonhuman delegations. | Major high-chaos subject/faction or breakaway. |
| Great Herds | Evolution IV | Elephant/savanna political force. | Heavy auxiliaries, supply routes, anti-ivory clauses. |
| Dust Senate | Evolution IV | Desert/mirage legal body. | Well law, sandstorm disasters, mirage-road missions. |
| Tidemark | Evolution IV | River/sea supernatural compact. | Convoy miracles, port flooding, naval pressure. |
| Masks That Vote | Evolution IV | Supernatural court masks as legal witnesses. | Forgery exposure and legitimacy trials. |

These actors must stay mechanically and textually separated from historical human polities. They are absurd Chaos Redux entities, not alternate labels for living peoples.

Current implementation note: Event 012 registers 11 explicit Bestiary actor tags with direct public display identities. The original actor tags are `GHP` Gorilla Highlands, `BBS` Baobab Senate, `TDM` Tidemark Dominion, `ANW` Ananse Web, `OVN` Orisha/Vodun Nature Courts, and `CRR` Crocodile Rivers; the expanded actor tags are `CTL` Chimpanzee Telegraph League, `OKP` Okapi Court, `TRM` Termite Citadel Engineers, `HGD` Honeyguide Commons, and `GHC` Great Herds. They have country/history files, ideology and party localisation, nonhuman/special classification, seat-state transfer hooks, setup-package effects, focus-tree access, AI posture coverage, generated flag/portrait assets, actor-target decisions from the unifier decision layer, and local consequence events for the expanded actor decisions.

Current implementation note: `africa_generate_created_country_role_staff` gives every created regional authority and Bestiary actor one generated role advisor when its setup package applies. The advisor names are functional staff/court/body labels, not invented historical human personnel; nonhuman and supernatural actors receive explicit fictional/nonhuman staff wrappers. The roles use vanilla slots and traits: political advisors for organisers/builders/omen keepers, high command for route and forest logistics, army chiefs for muster/river/herd command, navy chiefs for maritime actors, and theorists for survey/signal roles. This covers the first advisor surface, while broader bespoke advisor pools remain future country-package depth.

Current implementation note: the selected unifier now receives one opening origin profile through `africa_apply_unifier_origin_package`. Registered hosts map to Highland Legacy (`ETH`), Atlantic Return Route (`LIB`), Union Rupture (`SAF`), Nile Sea Gate (`EGY`, `SUD`, `ERI`, `DJI`, `SOM`), Western Congress Ports (`WAC`, `GHA`, `MLI`, `SEN`, `NGA`, `GNA`, `VOL`, `DAH`, `IVO`, `SIE`, `GAM`, `TOG`, `NGR`), Congo River-Forest Mandate (`CBC`, `COG`, `ANG`, `CMR`, `EQG`, `GAB`), Indian Ocean Gate (`IOC`, `MAD`, `MZB`, `KEN`, `TZN`), or General Congress Mandate for other valid hosts. Each profile has a visible spirit, live Congress header label, value movement, logistics grant, cleanup path, and AI posture. This closes the first opening identity pass for selected hosts, while deeper route-specific events and bespoke long-form host branches remain future country-package depth.

## Archive of Old Seats package and formable addendum

## Archive of Old Seats package integration

`specs/012_africa_niche_country_expansion.md` is now part of the country-package source design. It expands the subject/formable layer with historical **restoration dossiers** and high-chaos **nonhuman/supernatural packages**.

### Formable implications

- The unified Africa path should not simply erase restored old seats. Once Africa is politically unified, the player chooses whether the old seats become provincial archives, autonomous charter houses, or a second chamber inside the continental state.
- Respectful settlements reduce resistance and speed long-term coring. Coercive settlements give faster short-term control but increase `restoration_debt` and make later world-union paths harder.
- If the unifier forms Afro-Asian, Afro-Eurasian, or other continent unions, the Archive of Old Seats can become a global institution that recognizes old seats on other continents. This is a late-game hook for other continental unifier events.
- If the Bestiary Clause is active, nonhuman observer seats can persist into cross-continent unions. This should change dynamic country names and super-event tone, but final super-event text remains research-gated.

### Additional hidden formables / identity states

| Identity state | Unlock | Result |
| --- | --- | --- |
| Federation of Old Seats | High `old_seat_legitimacy`, high local sovereignty, low restoration debt, many dossiers peacefully settled. | Africa keeps a federal/charter name variant, lower revolt risk, slower direct annexations, old-seat advisors. |
| The Counterfeit Empire | Counterfeit Crown route, many forged seals, high control, low exposure. | Fast integration and aggressive claims; huge scandal risk and high mythic backlash. |
| The Green Covenant of Africa | Green Covenant route, high nonhuman sovereignty, nature-court pact. | Strong defensive/environmental powers; resource extraction and total-war options become dangerous. |
| Parliament of Root and Fang | Evolution IV, Bestiary Clause, at least three nonhuman delegations and one supernatural court. | Absurd continental identity; can interact with world-end path if other continent unifiers accept similar impossible actors. |
| The Museum State | Predatory Museum route and heavy exploitation of old seats. | Strong extraction, harsh stability/resistance penalties, high chance of old-seat and supernatural counter-coalition. |

These identities can be cosmetic tags or scripted dynamic names rather than full tag switches. The implementation should use dynamic naming where the set of accepted old seats and nonhuman delegations changes the final title.
