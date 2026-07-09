# 012 Africa spec part 11, country package implementation tiers

This file expands the country package matrix into implementation tiers and full notes for priority countries. Tags are placeholders unless the implementation already has a safe unused tag. Country names are direct map names. All labels are working labels, not final localisation.

## Tier structure

| Tier | Package class | Required for first implementation | Notes |
| --- | --- | --- | --- |
| Tier 0 | Event owner and RSA branch | Yes | Needed for the event to function |
| Tier 1 | Major restored polities | Yes for at least ten | These give the continent system depth and regional identity |
| Tier 2 | Secondary restored polities and city states | Strongly preferred | Can share focused overlay mechanics if country-specific variation remains |
| Tier 3 | High-chaos nonhuman and supernatural actors | Needed for high-chaos implementation | Must be clearly nonhuman or supernatural |
| Tier 4 | Future expansion and rare variants | Optional | Should not block the core package |

## Tier 0, Africa unifier package

### Africa unifier

| Field | Design |
| --- | --- |
| Public identity | Direct Africa identity through cosmetic tag and ideology-specific names |
| Spawn or transformation | A valid African-capital country is selected by the event |
| Starting territory | Its existing territory only |
| Claims and cores | Starts with visible continental ambition, but full cores require staged integration |
| Main mechanics | Charter League, regional integration, route focus tree, member confidence, unifier legitimacy, diaspora routes |
| Starting ideas | One major mixed idea for unfinished continental mandate, plus route-specific transformations |
| Military | Existing army plus League guard pathway, not free continent-scale force |
| Economy | Starts weak or strong based on selected country, then grows through regional projects |
| Focus tree | Full shared Africa tree with route packages from part 9 |
| AI | Chooses route by ideology, strength, war state, stability, and chaos tier |
| Assets | Cosmetic flag family, leader portrait frame, focus icon families, decision category icon, route emblems |
| Failure states | Rival blocs, member exit, colonial countercoalition, integration revolts |
| Special notes | The unifier must not instantly annex native African countries |

The unifier package should not erase the original country's identity. Its old leader, ideology, and geography should influence the route. A coastal unifier should lean toward diaspora and naval routes. A Sahel unifier should lean toward caravan and inland integration. A southern unifier should encounter RSA and Allied logic sooner.

## Tier 0, RSA civil-war branch

### South Africa, Allied loyalist side

| Field | Design |
| --- | --- |
| Public name | South Africa or Union of South Africa based on ideology |
| Spawn condition | RSA is selected while in the Allies |
| Role | Holds the Allied loyalist government and existing international ties |
| Territory | Receives part of RSA based on civil-war split, with capital and ports balanced for play |
| Starting politics | Allied alignment, anti-continental legitimacy, emergency cabinet |
| Military | Receives part of existing army, stronger foreign support, better officers |
| Decisions | Allied aid, port defense, anti-League propaganda, peace if continental side wins |
| Focus access | Emergency loyalist branch or temporary survival package |
| AI | Defend ports, seek Allied support, avoid suicidally attacking deep interior |
| Assets | Existing South Africa assets can be reused where appropriate, plus emergency variant if needed |
| Failure | If capitulated by continental side, Allied peace should trigger and the continental package continues |

### Azania, continental side

| Field | Design |
| --- | --- |
| Public name | Azania as direct map name for the continental breakaway |
| Spawn condition | RSA selected while in the Allies |
| Role | Continental unifier branch that fights for the Africa package |
| Territory | Receives interior, mobilized cities, or contested split based on balance |
| Starting politics | Anti-colonial continental movement with route choice after victory |
| Military | Receives militia, defectors, railway guards, and League guard embryos |
| Decisions | Seize depots, rally miners and rail workers, call African support, seek neutral mediation |
| Focus access | Emergency civil-war opener, then shared Africa tree after victory |
| AI | Survive first, take key ports, avoid overextension until Allied peace |
| Assets | New flag, emergency portrait or council portrait, civil-war report image direction |
| Failure | If defeated, Africa event should record failed unifier state and stop ordinary package safely |

The RSA branch should not let the player skip the League system. Winning the civil war grants legitimacy and a route opening, not instant continental cores.

## Tier 1, major restored polities

The first implementation should include at least ten major restored polities. Each can begin as a League member, regional subject, autonomous partner, or rival depending on route and local conditions.

### Aksum

| Field | Design |
| --- | --- |
| Region | Horn highlands and Red Sea |
| Public names | Aksum, Kingdom of Aksum, Aksum Republic, Aksum Commune |
| Core territory direction | Northern Ethiopia and Eritrean highland claims where state layout permits |
| Claimed territory direction | Red Sea routes and old highland influence zones |
| Spawn or restoration | Sacred Soil, Crown, or regional restoration decision after Horn confidence work |
| Starting politics | Monarchist or non-aligned by default, with republican and socialist alternatives |
| Starting forces | Highland guards, Red Sea patrol detachments, mountain infantry if supply permits |
| Unique mechanic | Stelae legitimacy and Red Sea tolls as local support values |
| Integration route | Federal member if respected, crown partner if restored by royal route, rival if coerced |
| Focus overlay | Highland courts, Red Sea trade, church and court mediation, mountain defense |
| Assets | Historical motifs should be sourced for symbols, generated portraits allowed only for fictional leaders |
| AI | Defend highlands, prefer autonomy, accept federation at high confidence |

### Kush

| Field | Design |
| --- | --- |
| Region | Nile valley and Sudan |
| Public names | Kush, Kingdom of Kush, Kush Republic, Kush Commune |
| Core territory direction | Sudanese Nile corridor around Meroe where feasible |
| Claimed territory direction | Nubian and Nile-linked state groups |
| Spawn or restoration | Nile restoration project, Sacred Soil heritage route, Crown route |
| Starting politics | Non-aligned heritage monarchy or republican restoration |
| Starting forces | Nile guards, desert scouts, river crossing detachments |
| Unique mechanic | Pyramid and river legitimacy, heritage protection missions |
| Integration route | Strong federal candidate if heritage sites protected |
| Focus overlay | Nile roads, river forts, old capital restoration, desert supply |
| Assets | Meroe and Kush symbols require source review, fictional route variants can be generated |
| AI | Prioritize river defense and autonomy guarantee |

### Makuria

| Field | Design |
| --- | --- |
| Region | Nubia and middle Nile |
| Public names | Makuria, Kingdom of Makuria, Makuria Republic |
| Core territory direction | Nubian corridor between Egypt and Sudan where state layout permits |
| Claimed territory direction | Christian Nubian historical anchor areas |
| Spawn or restoration | High legitimacy Nile restoration or Crown route |
| Starting politics | Non-aligned or democratic local restoration |
| Starting forces | River militia, fortress guards, light infantry |
| Unique mechanic | Border monastery and fortress mediation as local support missions |
| Integration route | Federal member or crown partner |
| Focus overlay | Nile fortresses, manuscript protection, desert river supply |
| Assets | Historical symbols should be sourced if used, otherwise abstract generated motifs |
| AI | Avoid aggressive wars, accept protection if surrounded |

### Kanem-Bornu

| Field | Design |
| --- | --- |
| Region | Lake Chad and Sahel |
| Public names | Kanem-Bornu, Bornu, Kanem-Bornu Sultanate, Kanem-Bornu Republic |
| Core territory direction | Lake Chad basin around Chad, Nigeria, Niger, and Cameroon state groups where feasible |
| Claimed territory direction | Sahel caravan and lake influence zones |
| Spawn or restoration | Sahel caravan project or Crown route |
| Starting politics | Sultanate leaning non-aligned, with republican and socialist alternatives |
| Starting forces | Camel scouts, lake guards, desert infantry, cavalry where appropriate |
| Unique mechanic | Caravan tolls, lake supply, desert legitimacy |
| Integration route | Strong autonomy demand, good associated-state candidate |
| Focus overlay | Lake patrols, caravan routes, desert supply, sultanate courts |
| Assets | Source historical symbols where attested, generate fictional variants for route flags |
| AI | Protect Lake Chad, resist coercive annexation, accept aid during colonial wars |

### Songhai

| Field | Design |
| --- | --- |
| Region | Niger bend and western Sahel |
| Public names | Songhai, Songhai Empire, Songhai Republic, Songhai Commune |
| Core territory direction | Niger bend and Mali or Niger-linked state groups |
| Claimed territory direction | Trans-Saharan trade and river routes |
| Spawn or restoration | Sahel or Timbuktu project after regional control |
| Starting politics | Non-aligned restoration, republican administration, or revolutionary river state |
| Starting forces | River guards, desert scouts, militia from old trade towns |
| Unique mechanic | River scholarship and trade-route legitimacy |
| Integration route | Federal member if Timbuktu and river routes are protected |
| Focus overlay | Niger fleets, manuscript houses, caravan markets, desert diplomacy |
| Assets | Manuscript and river motifs, avoid fake readable text in generated images |
| AI | Seeks river security and autonomy |

### Oyo

| Field | Design |
| --- | --- |
| Region | Yoruba country and western Nigeria |
| Public names | Oyo, Oyo Empire, Oyo Republic, Oyo Commune |
| Core territory direction | Western Nigeria state groups where feasible |
| Claimed territory direction | Yoruba and regional cavalry influence areas |
| Spawn or restoration | Gulf of Guinea restoration, Crown route, or local congress |
| Starting politics | Monarchist or republican, with revolutionary alternative |
| Starting forces | Cavalry-inspired mobile militia, city guards, depot troops |
| Unique mechanic | Cavalry prestige and city legitimacy |
| Integration route | Strong federal or crown partner, resists military governors |
| Focus overlay | City councils, cavalry schools, trade roads, court mediation |
| Assets | Source historical regalia motifs where possible |
| AI | Prefers autonomy and local order |

### Benin or Edo

| Field | Design |
| --- | --- |
| Region | Southern Nigeria and Niger delta approach |
| Public names | Benin, Edo, Kingdom of Benin, Edo Republic |
| Core territory direction | Edo and nearby southern Nigeria state groups where feasible |
| Claimed territory direction | Court and trade influence zones |
| Spawn or restoration | Gulf of Guinea restoration with art and court legitimacy |
| Starting politics | Court restoration, republican, or socialist civic route |
| Starting forces | City guards, river delta patrols, militia |
| Unique mechanic | Bronze court legitimacy and port trade pressure |
| Integration route | Federal or crown partner, high resistance to pillage or coercion |
| Focus overlay | Court craft, port access, delta security, heritage return |
| Assets | Historical symbols and court art motifs need source care |
| AI | Protect capital and trade routes |

### Asante

| Field | Design |
| --- | --- |
| Region | Gold Coast and forest belt |
| Public names | Asante, Kingdom of Asante, Asante Republic, Asante Commune |
| Core territory direction | Ghana forest and Gold Coast state groups |
| Claimed territory direction | Akan and trade influence zones |
| Spawn or restoration | Gulf of Guinea route, Crown route, or Federal local congress |
| Starting politics | Monarchical restoration or republican forest state |
| Starting forces | Forest guards, gold-route militia, local defense units |
| Unique mechanic | Golden Stool legitimacy as source-gated symbol direction |
| Integration route | Strong crown partner or federal member if symbols are respected |
| Focus overlay | Forest roads, gold routes, court diplomacy, local levies |
| Assets | Source historical symbol references before flag or icon work |
| AI | High autonomy demand, values respect and aid |

### Kongo

| Field | Design |
| --- | --- |
| Region | Congo basin and Atlantic central Africa |
| Public names | Kongo, Kingdom of Kongo, Kongo Republic, Kongo Commune |
| Core territory direction | Western Congo and northern Angola state groups around old capital direction |
| Claimed territory direction | Congo River and Atlantic trade zones |
| Spawn or restoration | Congo basin project, Crown route, Sacred Soil route |
| Starting politics | Court restoration, republican river state, or socialist river commune |
| Starting forces | River guards, forest militia, port detachments |
| Unique mechanic | River legitimacy and old capital reconstruction |
| Integration route | Federal member or crown partner, rival if exploited for resources |
| Focus overlay | River ports, old capital, church and court memories, forest routes |
| Assets | Source historical emblems where attested, generated for fictional variants |
| AI | Defend river access and avoid being resource puppet |

### Luba

| Field | Design |
| --- | --- |
| Region | Central Africa and Katanga-adjacent interior |
| Public names | Luba, Kingdom of Luba, Luba Republic |
| Core territory direction | Central Congo interior state groups where feasible |
| Claimed territory direction | Luba cultural and trade influence zones |
| Spawn or restoration | Congo basin integration or restored polity branch |
| Starting politics | Local kingdom, republican administration, or communal route |
| Starting forces | Interior militia, mining-belt guards if controlled |
| Unique mechanic | Memory boards and court legitimacy as source-gated motif direction |
| Integration route | Associated state or federal member |
| Focus overlay | Interior roads, copper routes, court memory, local guards |
| Assets | Use symbolic source review before precise iconography |
| AI | Defensive, prefers autonomy and regional protection |

### Lunda

| Field | Design |
| --- | --- |
| Region | Central Africa, Angola, Congo, Zambia link |
| Public names | Lunda, Kingdom of Lunda, Lunda Republic |
| Core territory direction | Cross-border central-southern interior where state layout permits |
| Claimed territory direction | Kazembe and interior trade branches if included |
| Spawn or restoration | Regional restoration after Congo basin and Zambezi projects |
| Starting politics | Court restoration or regional republic |
| Starting forces | Interior scouts, river and forest guards |
| Unique mechanic | Tributary network restoration and border mediation |
| Integration route | Strong associated-state candidate |
| Focus overlay | Cross-border caravans, interior roads, tribute mediation, guard paths |
| Assets | Generated fictional variants likely needed unless sourced symbols are verified |
| AI | Avoid aggressive expansion unless backed by Crown route |

### Great Zimbabwe

| Field | Design |
| --- | --- |
| Region | Zimbabwe plateau |
| Public names | Great Zimbabwe, Zimbabwe, Zimbabwe Republic, Zimbabwe Commune |
| Core territory direction | Zimbabwe plateau state groups around Great Zimbabwe direction |
| Claimed territory direction | Plateau and trade-route heritage zones |
| Spawn or restoration | Zambezi and Zimbabwe plateau project |
| Starting politics | Heritage republic or royal restoration |
| Starting forces | Stone-city guards, plateau militia, rail detachments |
| Unique mechanic | Stone city legitimacy and gold-route restoration |
| Integration route | Federal member with high heritage protection needs |
| Focus overlay | Stone roads, trade routes, plateau defense, heritage restoration |
| Assets | Great Zimbabwe imagery should use UNESCO or source-informed motifs |
| AI | Defend plateau, accept investment, resist extraction-only policy |

### Mutapa

| Field | Design |
| --- | --- |
| Region | Zimbabwe, Mozambique, and Zambezi trade routes |
| Public names | Mutapa, Kingdom of Mutapa, Mutapa Republic |
| Core territory direction | Zambezi and eastern plateau state groups where feasible |
| Claimed territory direction | Gold and Indian Ocean trade routes |
| Spawn or restoration | Zambezi project, Swahili or Crown route |
| Starting politics | Monarchy or regional republic |
| Starting forces | Plateau militia, river guards, trade-route detachments |
| Unique mechanic | Gold-route diplomacy and coastal trade access |
| Integration route | Federal or crown partner, may rival Great Zimbabwe if both restored poorly |
| Focus overlay | Zambezi crossings, trade roads, coastal access, court envoys |
| Assets | Fictional route flags likely generated, historical motifs need review |
| AI | Seeks coast access and autonomy |

### Kilwa

| Field | Design |
| --- | --- |
| Region | Swahili coast |
| Public names | Kilwa, Sultanate of Kilwa, Kilwa Republic, Kilwa Commune |
| Core territory direction | Tanzanian coast and islands around Kilwa direction |
| Claimed territory direction | Swahili coast city-state network and Indian Ocean trade |
| Spawn or restoration | Swahili coast project, port control, or diaspora route |
| Starting politics | Sultanate, merchant republic, or socialist port commune |
| Starting forces | Port guards, dhow patrol abstraction, coastal militia |
| Unique mechanic | Indian Ocean trade and port confidence |
| Integration route | Federal member or associated maritime state |
| Focus overlay | Mosques, coral-stone cities, port customs, sea lanes |
| Assets | UNESCO Kilwa source direction for event art, generated fictional flags for alternate variants |
| AI | Protect ports, join if convoys and autonomy are guaranteed |

### Buganda

| Field | Design |
| --- | --- |
| Region | Great Lakes |
| Public names | Buganda, Kingdom of Buganda, Buganda Republic |
| Core territory direction | Uganda and Lake Victoria state groups where feasible |
| Claimed territory direction | Great Lakes influence zones |
| Spawn or restoration | Great Lakes project or Crown route |
| Starting politics | Kingdom with republican option |
| Starting forces | Lake guards, capital militia, highland infantry |
| Unique mechanic | Lake Victoria legitimacy and local parliament tension |
| Integration route | Federal member with strong autonomy demand |
| Focus overlay | Lake ports, royal council, local assembly, highland defense |
| Assets | Source historical flag or symbols if used |
| AI | Strong defensive local route, resists coercion |

### Merina

| Field | Design |
| --- | --- |
| Region | Madagascar |
| Public names | Merina, Kingdom of Merina, Madagascar, Madagascar Republic |
| Core territory direction | Madagascar highlands if route uses Merina, whole island if Madagascar identity |
| Claimed territory direction | Island ports and highlands |
| Spawn or restoration | Indian Ocean island project or Crown route |
| Starting politics | Monarchy, republic, or socialist island route |
| Starting forces | Highland militia, port guards, island defense units |
| Unique mechanic | Island autonomy and convoy dependence |
| Integration route | Associated island state, federal member after port and convoy missions |
| Focus overlay | Highland roads, port defense, island councils, convoy work |
| Assets | Source historical flag if restored Merina uses attested symbols |
| AI | High autonomy, needs convoy protection |

### Sokoto

| Field | Design |
| --- | --- |
| Region | Northern Nigeria and Sahel edge |
| Public names | Sokoto, Sokoto Sultanate, Sokoto Republic |
| Core territory direction | Northern Nigeria state groups where feasible |
| Claimed territory direction | Sahel and Hausa-Fulani historical influence zones |
| Spawn or restoration | Sahel or Gulf of Guinea project, Crown or Sacred Soil route |
| Starting politics | Sultanate or conservative republic |
| Starting forces | Cavalry and desert militia abstraction, city guards |
| Unique mechanic | Religious authority and caravan legitimacy |
| Integration route | Associated state or federal member after autonomy guarantee |
| Focus overlay | Schools, caravan roads, emirate councils, border defense |
| Assets | Source historical symbols with care |
| AI | Resists revolutionary centralization, accepts protection if threatened |

### Futa Jallon

| Field | Design |
| --- | --- |
| Region | Upper Guinea highlands |
| Public names | Futa Jallon, Futa Jallon Imamate, Futa Jallon Republic |
| Core territory direction | Guinea highlands where state layout permits |
| Claimed territory direction | Western Sahel and highland influence zones |
| Spawn or restoration | Sahel or Gulf of Guinea project |
| Starting politics | Imamate or republican highland route |
| Starting forces | Highland militia, caravan guards |
| Unique mechanic | Highland mediation and caravan legitimacy |
| Integration route | Federal member with religious autonomy |
| Focus overlay | Highland paths, schools, mediation, local defense |
| Assets | Historical symbols require source review |
| AI | Defensive, values autonomy and local authority |

### Zulu

| Field | Design |
| --- | --- |
| Region | Southern Africa |
| Public names | Zulu, Kingdom of Zulu, Zulu Republic |
| Core territory direction | KwaZulu-Natal and nearby state groups where feasible |
| Claimed territory direction | Southern regional influence zones |
| Spawn or restoration | Southern integration, Crown route, or RSA aftermath |
| Starting politics | Monarchy, republic, or military local route |
| Starting forces | Infantry regiments, local defense units, former RSA defectors if branch supports it |
| Unique mechanic | Regimental tradition and local autonomy |
| Integration route | Federal or crown member, rival if RSA branch mishandles it |
| Focus overlay | Regional defense, regimental reform, local governance, southern settlement |
| Assets | Source historical symbols if used |
| AI | Defend home region and negotiate autonomy |

## Tier 2, secondary restored polities

Tier 2 packages may use smaller focus overlays, but each still needs identity and non-generic local mechanics.

| Polity | Region | Role | Package notes |
| --- | --- | --- | --- |
| Sao | Lake Chad | Archaeological and old city-state restoration | Small protectorate or heritage member tied to Kanem-Bornu and Lake Chad |
| Mossi | Burkina Faso and Sahel edge | Cavalry and plateau polity | Strong autonomy, useful for Sahel rival or federal member |
| Dahomey | Bight of Benin | Coastal military and royal restoration | Can rival Oyo or Benin if handled poorly |
| Kuba | Congo basin | Court and forest polity | Strong cultural asset needs, good federal member |
| Kazembe | Lunda and Luapula link | Trade and tributary branch | Works as Lunda-related subject or federal member |
| Lozi or Barotse | Zambezi | Floodplain and river polity | Strong water mission and autonomy content |
| Rozwi | Zimbabwe plateau | Plateau restoration | Can be partner or rival of Mutapa and Great Zimbabwe |
| Futa Toro | Senegal river | Sahel river polity | River mediation and caravan missions |
| Swahili city states | East African coast | Network of maritime subjects | Shared maritime overlay for Mombasa, Zanzibar, Lamu, Kilwa-style partners |
| Bamum | Cameroon grassfields | Art, court, and highland polity | Small but distinctive country package |
| Garamantes | Sahara | Ancient oasis and desert route | Good rare restoration or high-chaos ancient-host link |
| Alodia | Sudan | Nubian successor | Smaller Nile restoration linked to Makuria and Kush |

## Tier 3, high-chaos nonhuman and supernatural actors

These actors must be explicitly nonhuman, animal, supernatural, or impossible. They should not speak or behave as disguised human ethnic caricatures.

### Virunga Gorillas

| Field | Design |
| --- | --- |
| Public name | Virunga Gorillas |
| Nature | Nonhuman animal actor with high-chaos intelligence or supernatural representation |
| Region | Great Lakes and Congo forest zones |
| Spawn condition | Deep Green route, severe forest pressure, high chaos |
| Military | Very limited but absurd defensive units, forest-only bonuses, no normal industry path |
| Diplomacy | Can be protected, negotiated with, or angered through habitat decisions |
| Mechanics | Habitat pressure, forest wrath, member shock |
| AI | Ordinary AI almost never controls or creates them |
| Assets | Generated nonhuman portraits or emblem, no human ethnic dress |

### Congo Chimpanzees

| Field | Design |
| --- | --- |
| Public name | Congo Chimpanzees |
| Nature | Nonhuman high-chaos animal actor |
| Region | Congo basin |
| Spawn condition | Deep Green route or failed forest exploitation |
| Military | Ambush and sabotage abstractions, not normal divisions unless route explicitly supports absurd units |
| Diplomacy | Can disrupt colonial extraction and punish coercive annexation |
| Mechanics | Forest sabotage, panic, and containment |
| AI | Rare, defensive, high-chaos only |
| Assets | Generated animal actor imagery, no human caricature |

### Living Statues of Kush

| Field | Design |
| --- | --- |
| Public name | Living Statues of Kush |
| Nature | Supernatural animated monuments or ancient host |
| Region | Nile and Meroe-linked zones |
| Spawn condition | High-chaos Sacred Soil or Deep Green interaction with Kush restoration |
| Military | Small elite living-stone formations with extreme durability and severe limitations |
| Diplomacy | Cannot be treated as ordinary human member |
| Mechanics | Relic awakening, containment, blowback if overused |
| AI | Very rare, mostly player-driven |
| Assets | Generated supernatural stone host, clear nonhuman visual style |

### Stone Host of Great Zimbabwe

| Field | Design |
| --- | --- |
| Public name | Stone Host of Great Zimbabwe |
| Nature | Supernatural ancient host linked to stone city myth direction |
| Region | Zimbabwe plateau |
| Spawn condition | High-chaos heritage route, failed coercive extraction, or Deep Green covenant |
| Military | Slow defensive formations, fortification and attrition mechanics |
| Diplomacy | Protects sites and attacks desecration or coercion |
| Mechanics | Heritage pressure, stone defense, local fear |
| AI | Rare and defensive |
| Assets | Generated living-stone army and ruins, no human caricature |

### Red Sea Oracle

| Field | Design |
| --- | --- |
| Public name | Red Sea Oracle |
| Nature | Supernatural coastal or maritime power |
| Region | Red Sea and Horn ports |
| Spawn condition | High-chaos Aksum or Red Sea route |
| Military | Naval weather and port disruption abstractions |
| Diplomacy | Issues demands through omens and coastal events |
| Mechanics | Storm pressure, convoy disruption, port blessing or curse |
| AI | Rare, should not pursue normal conquest |
| Assets | Generated sea storm and oracle symbol, no human office title as country name |

### Rain Prophet State

| Field | Design |
| --- | --- |
| Public name | Rain Prophet State |
| Nature | Supernatural disaster-predicting actor |
| Region | Can appear in drought or flood pressure regions |
| Spawn condition | High chaos, repeated disaster pressure, Deep Green route |
| Military | Minimal conventional force, strong disaster pressure effects |
| Diplomacy | Demands appeasement, warns or punishes |
| Mechanics | Rain debt, flood risk, drought risk, blowback |
| AI | Very rare, not available to ordinary low-chaos AI |
| Assets | Generated weather prophet body or symbolic council, not ethnic caricature |

### Fever Without Name

| Field | Design |
| --- | --- |
| Public name | Fever Without Name |
| Nature | Fictional disease pressure actor or hidden route, not a real pathogen |
| Region | Any high-chaos region with outbreak pressure |
| Spawn condition | High chaos and biowarfare or disaster chain crossing safe thresholds |
| Military | No normal army by default, uses outbreak and panic mechanics |
| Diplomacy | Treated as hazard or supernatural pressure |
| Mechanics | Abstract infection pressure, containment, blowback, condemnation |
| AI | AI should not deliberately weaponize unless explicit rare route is enabled |
| Assets | Symbolic disease icon, no real-world pathogen imagery |

## Tier 4, future expansion candidates

Future packages can include island microstates, city-state networks, regional movement variants, and ideology-specific restoration variants. They should be queued only after Tier 0 and Tier 1 function with real decisions, AI, assets, and integration.

## Package common requirements

Every country package that fights must have:
- starting division concept
- equipment and manpower source
- route-based reinforcement
- leader or council identity
- country name and adjective direction
- party name direction
- flag source mode
- AI behavior
- decisions or focus overlay
- integration route
- cleanup rules

Every restored polity must have a reason not to be instantly annexed. The player should want to work with them, pressure them, or fight them based on route choices.
