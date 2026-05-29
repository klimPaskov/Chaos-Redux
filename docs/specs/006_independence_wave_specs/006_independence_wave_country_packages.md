# Event 6: Independence Wave Country Packages

The event creates dynamic countries, so this file defines country packages instead of pretending every possible released state receives a bespoke tree. A country package is a complete identity rule set: tag selection, territory, ideology, names, leaders, assets, focus access, decisions, AI behavior, and release-origin handling.


## Absolute host survival rule

No country package may delete its host. Every package must be carved from a host in a way that leaves the existing country with at least one state after the wave resolves. The protected state should be the current capital when the host still owns it. If the capital is not owned at resolution, the protected state is the best remaining owned state.

Package territory rules:

- full historical claims are inspiration, not mandatory starting borders
- starting territory may be reduced to one valid state if needed
- packages that need several states must be skipped when those states would remove the host from the map
- a package may receive claims on protected territory later, but not through the initial wave release
- the batch resolver must check the combined effect of all packages before release
- if two packages together would consume a host, the lower-score package is removed or reduced first

This applies to ordinary releasables, dormant tags, protectorates, city packages, historical-return packages, local-polity packages, and strange packages.

## Non-connection rule

Event 006 is not Event 005. Any country released by this event must be marked with `chaosx_release_origin = independence_wave`. The same tag can be used by another event, but it must receive Event 006 mechanics only when this origin is set.

This is absolute for Soviet republic style tags and for historical-return packages in Soviet or post-Soviet geography. If Event 006 releases a republic that Event 005 could also release, it still receives Event 006 country package logic. It must not receive Soviet Collapse republic missions, collapse focus trees, collapse startup ideas, collapse event logs, or Event 005 formable logic.

Example:

- Volga Bulgaria or Old Great Bulgaria released by Event 005 gets Event 005 content.
- Volga Bulgaria or Old Great Bulgaria released by Event 006 gets the Independence Wave tree and Volga historical-return overlay.
- A Soviet republic style tag released by Event 006 gets the Liberation Provisional Tree, a compact Event 006 subset, or an Event 006 package overlay.
- Event 006 should not require Event 005 variables, Event 005 missions, or republic-specific 005 content.

Shared utility helpers can be reused only when they are genuinely event-neutral. Any helper that reads collapse progress, Event 005 republic routes, Soviet Collapse event logs, or Event 005 package flags is not event-neutral and must be blocked for Event 006 releases.

## Package ladder

| Ladder | Chaos gate | Main source | Typical batch role |
| --- | --- | --- | --- |
| Ordinary releasable | Baseline | existing HOI4 or mod tags with valid cores | main pool for first waves |
| Dormant or game-rule tag | Evo I to Evo II | tags that exist but require decisions, focuses, or game rules in normal play | occasional surprise inside plausible regions |
| Protectorate or city package | Evo II to Evo III | strategic port, city, rail hub, canal, oil zone, or patron-backed borderland | support pool and patron gameplay |
| Historical-return package | Evo IV | researched old-state, kingdom, sultanate, confederacy, indigenous authority, or local polity | high-chaos identity shock |
| Strange package | Evo V | impossible state, necromantic authority, archive-state, anti-mankind directorate | rare major escalation |

## Country package matrix

| Package | Spawn conditions | Political identity | Assets | Focus and mechanics |
| --- | --- | --- | --- | --- |
| Standard Releasable Breakaway | Existing or modded tag has valid cores, scripted cores, or safe release states | Mostly democratic at low chaos, broader ideology rolls later | Use existing flags and portraits when available | Liberation Provisional Tree with generic route selection |
| Game-Rule or Formable-Compatible Breakaway | Tag exists in HOI4 through game rule, formable, focus, or decision and region checks pass | Depends on the historical identity and host crisis | Use existing assets if present, otherwise require asset work | Same tree with special eligibility checks and package flag |
| Border Protectorate | Major backs the committee before host suppresses it | Nominally independent with patron leverage | Patron-backed flag variant and adviser assets if needed | Patron Cabinet branch weighted strongly |
| Free Port or Free City | Industrial city, port, canal, rail junction, or trade hub breaks away | Civic, neutral, syndicalist, criminalized, or foreign-controlled | City seal, merchant council, dock militia | Civic, industry, diplomacy, intelligence, and patron branches |
| Railway Sovereignty | Rail hub or supply corridor becomes the basis of authority | Neutral, military, syndicalist, patron-backed, or strange | Rail flag, timetable seal, junction council portrait | Rail repair decisions and optional railway league route |
| Historical-Return State | Evo IV or higher and regional old-state memory is plausible | Democratic restoration, council, monarchy, emirate, directorate, revolutionary, or mythic route | Historical symbols require research. Fictional high-chaos variants can be generated | Common tree plus historical-return overlay |
| Local-Polity or Indigenous Authority | Evo IV or higher and local community authority is plausible | Land congress, chiefs, councils, protectorate renegotiation, or civic charter | Real symbols and leaders require sourced research | Local-polity overlay plus civic, patron, or land recovery routes |
| Necromantic Custodianship | Evo V and grave, battlefield, plague, camp, or mass-death pressure | Not normal ideology. State as grave administration | Generated symbolic assets | Necromancy module and containment decisions |
| Anti-Mankind Directorate | Evo V and anti-human doctrine or strange-state contact | Hostile impossible state | Generated symbolic assets | Anti-mankind module and world-threat hooks |

## Ordinary pool rules

The ordinary pool should dominate the first firing.

Selection rules:

- Prefer inactive countries with existing cores or clearly scripted cores.
- Prefer tags already known to the mod or base game.
- Prefer countries whose release does not require a custom asset package.
- Prefer plausible host relationships.
- Avoid overloading one small region with too many tiny states.
- Avoid releasing a country that already exists unless the package is a civil split or cosmetic variant with a clear reason.

Typical ordinary categories:

- European regional releasables such as Catalonia, Galicia, Basque Country, Scotland, Wales, Brittany, Occitania if present, and similar tags.
- Colonial or mandate releasables such as Algeria, Morocco, Tunisia, Egypt if not independent, Syria, Lebanon, Iraq if not independent, Indonesia, Vietnam, Burma, and African colonial tags if valid.
- Borderland or minority states such as Kurdistan, Armenia, Azerbaijan, Georgia, Ukraine, Belarus, and other dormant tags if inactive and valid.
- Existing Americas deimperialized tags if the mod or game rule supports them, such as Charrua, Guarani, Itza, Maya, Miskito, Nahua, Inuit, Inca, and Isthmo-American identities.

The implementation agent must verify actual tag names from the repository. This spec gives design identities, not guaranteed tag IDs.

## Batch size by evolution

| Evolution state | Release count target | Pool behavior |
| --- | ---: | --- |
| Baseline | 3 to 5 | ordinary tags only, mostly democratic |
| Evo I | 4 to 6 | ordinary tags plus rare dormant tags |
| Evo II | 5 to 7 | ordinary tags, regional clusters, city and protectorate packages |
| Evo III | 6 to 9 | claims, patron-backed releases, stronger countries |
| Evo IV | 8 to 12 | historical-return and local-polity packages unlock |
| Evo V | 10 to 16 | strange packages and impossible-state releases unlock if performance allows |

If valid candidates are insufficient, release fewer countries. Do not spawn nonsense.

## Researched high-chaos candidate matrix

This matrix is an expansion pool. Do not implement every package blindly. Each row needs a valid tag, state mapping, assets, localisation, leader plan, and balance review.

| Candidate | Package family | Region logic | Suggested chaos gate | Focus overlay |
| --- | --- | --- | --- | --- |
| Assyria | Mesopotamian historical-return | Northern Mesopotamia, Nineveh, Mosul, Khabur, or nearby state cluster if valid | Evo IV | Assyria overlay |
| Mesopotamia | River-state or mandate-era revival | Tigris and Euphrates valley, Baghdad, Basra, Mosul if valid | Evo IV | Mesopotamia overlay |
| Marsh Arab river authority | Local-polity river package | Southern Iraq marshes and river districts | Evo IV | River and marsh local-polity overlay |
| Kurdistan | Existing or dormant tag | Kurdish-majority mountain regions if tag and states exist | Baseline to Evo II depending on setup | ordinary tree or mountain overlay |
| Volga Bulgaria | Steppe historical-return | Volga and Kama region if valid | Evo IV | Volga overlay, not Event 005 tree |
| Idel-Ural | Steppe federation | Volga-Ural region if valid | Evo IV | federation overlay |
| Circassia | Caucasus historical-return | Northwest Caucasus if valid | Evo IV | mountain confederacy overlay |
| Mountain Republic | Caucasus confederation | North Caucasus mountain regions if valid | Evo IV | confederal council overlay |
| Don Host | Cossack or dormant tag | Don region if valid and not claimed by another event | Evo II to Evo IV | military frontier overlay |
| Kuban Host | Cossack or dormant tag | Kuban region if valid and not claimed by another event | Evo II to Evo IV | military frontier overlay |
| Bukhara | Central Asian emirate | Bukhara and surrounding Central Asian states | Evo IV | emirate restoration overlay |
| Khiva | Central Asian khanate | Khwarazm region if valid | Evo IV | khanate restoration overlay |
| Kokand | Central Asian khanate | Fergana region if valid | Evo IV | khanate restoration overlay |
| Asante | West African old-state | Gold Coast interior and Kumasi region if valid | Evo IV | palace and trade-route overlay |
| Dahomey | Existing or old-state package | Bight of Benin if not already ordinary tag | Evo II to Evo IV | palace or ordinary overlay |
| Sokoto | Sahel emirate federation | Northern Nigeria and nearby Sahel states | Evo IV | emirate federation overlay |
| Kanem-Bornu | Lake Chad historical-return | Lake Chad basin across Chad, Nigeria, Niger, Cameroon if valid | Evo IV | trade-route and dynasty overlay |
| Darfur | Sultanate restoration | Darfur region if valid | Evo IV | sultanate and frontier overlay |
| Buganda | Great Lakes kingdom | Central Uganda and Lake Victoria region if valid | Evo IV | kabaka and protectorate treaty overlay |
| Bunyoro | Great Lakes kingdom | Western Uganda if valid | Evo IV | royal council overlay |
| Barotseland | Lozi local-polity | Upper Zambezi and Lozi area if valid | Evo IV | treaty autonomy overlay |
| Zulu | Southern African old-state | Natal and Zulu kingdom memory if valid | Evo IV | regimental and royal prestige overlay |
| Xhosa council | Local-polity | Eastern Cape if valid | Evo IV | land congress overlay |
| Basotho mountain state | Existing or local-polity | Lesotho or mountain region if valid | Baseline to Evo IV | mountain defense overlay |
| Herero authority | Local-polity | Central Namibia if valid | Evo IV | land recovery and mounted defense overlay |
| Nama authority | Local-polity | Southern Namibia if valid | Evo IV | land recovery and treaty memory overlay |
| Mapuche Araucania | Indigenous local-polity | Southern Chile and Argentina if valid | Evo IV | land congress and mountain defense overlay |
| Aymara congress | Indigenous local-polity | Altiplano in Bolivia, Peru, Chile, Argentina if valid | Evo IV | Altiplano community overlay |
| Guarani republic | Indigenous or game-rule tag | Paraguay, southern Brazil, northern Argentina, Uruguay if valid | Evo II to Evo IV | forest and language overlay |
| Charrua revival | Indigenous or game-rule tag | Uruguay and nearby regions if valid | Evo II to Evo IV | fragile survival overlay |
| Palmares | Quilombo historical-return | Brazilian interior or northeast if state mapping supports it | Evo IV | forest defense and hidden settlement overlay |
| Muisca cultural state | Indigenous local-polity | Colombian highlands if valid | Evo IV | council and mountain overlay |
| Maya | Game-rule or indigenous package | Yucatan and adjacent Maya regions if valid | Evo II to Evo IV | land congress overlay |
| Itza | Game-rule or indigenous package | Peten and Yucatan region if valid | Evo II to Evo IV | land congress overlay |
| Nahua | Game-rule or indigenous package | Central Mexico if valid | Evo II to Evo IV | old name and modern charter overlay |
| Miskito | Game-rule or local-polity | Mosquito Coast if valid | Evo II to Evo IV | protectorate coast overlay |
| Inuit union | Game-rule or local-polity | Arctic regions if valid | Evo II to Evo IV | survival and recognition overlay |
| Free City | City package | high-value port, treaty city, canal city, industrial hub | Evo II | free city overlay |
| Railway Republic | Infrastructure package | rail junction, supply hub, bridge region | Evo II | railway overlay |
| Archive-State | Strange package | collapsed capital or dead bureaucracy | Evo V | archive-state module |
| Necromantic Custodianship | Strange package | grave, battlefield, camp, mass-death, plague zone | Evo V | necromancy module |
| Anti-Mankind Directorate | Strange package | explicit anti-human doctrine pressure | Evo V | anti-mankind module |

## Package implementation fields

Every implemented package needs these fields in data or documentation:

- package id
- package display name
- candidate tag or custom tag plan
- origin event id
- allowed host regions
- blocked host regions
- required states or state clusters
- protected host state interaction
- reduced starting territory version
- fallback states
- ideology weights by chaos tier
- leader plan
- flag plan
- focus overlay
- startup ideas
- army template direction
- starting equipment rules
- diplomacy rules
- claim rules
- AI behavior
- asset requirements
- localisation requirements
- validation notes

## Ideology naming patterns

Ordinary releases can use standard ideology names. High-chaos packages need specific naming.

| Route | Naming style |
| --- | --- |
| Democratic | Republic, Council Republic, Free State, Charter State, Protected State |
| Non-aligned | Kingdom, Emirate, Sultanate, Protectorate, State Council, Regency, Confederacy |
| Fascist | Directorate, National State, Revival Authority, Border Guard State |
| Communist | Commune, Workers Council, Revolutionary Committee, Peasant Congress |
| Patron | Protectorate, Client Republic, Allied State, Mandated Authority |
| Anti-patron | Free Charter State, Independent Council, Sovereign League Member |
| Strange | Custodianship, Directorate, Archive-State, Census Authority, Sealed Administration |

## Ordinary to high-chaos transition

The event should show the world learning the pattern.

- Baseline: ordinary petitions become small countries.
- Evo I: committees copy each other and become more professional.
- Evo II: countries cooperate and ask each other for guarantees.
- Evo III: independence becomes a border weapon and a patron game.
- Evo IV: old names and local authorities return because chaos makes them politically usable.
- Evo V: the idea of statehood breaks into impossible forms.

## Asset policy for packages

- Real flags, symbols, and real historical leaders need sourced research.
- Fictional flags for impossible states, archive-states, and speculative variants can use generated art.
- Event photo assets should use period-compatible images when possible.
- For indigenous and local-polity packages, avoid modern activist imagery unless the spec explicitly asks for modern reference only. The setting should still feel compatible with HOI4.
- If the agent cannot verify a real symbol or leader, it should use a generic council, seal, or generated fictional variant and mark the source gap.

## Compatibility notes

- Do not release countries into states already locked by a more important ongoing event unless the target system allows it.
- If a tag already exists, use recognition, support, claims, or faction mechanics instead of creating a duplicate.
- If a historical package lacks assets, state mapping, or leaders, keep it as a candidate data entry and block it from live spawn until ready.
- If a normal tag and historical package overlap, use the more ordinary tag at low chaos and the historical package at high chaos only.
- If performance is strained, cap high-chaos batch size before creating extra custom states.


## Expanded package schema

Every country package should be written as data first and flavor second. A package that lacks any required field should remain disabled until it is completed.

| Field | Required value |
| --- | --- |
| package_key | stable internal key such as `iw_pkg_assyria` |
| package_type | ordinary, dormant, protectorate, city, railway, historical_return, local_polity, strange |
| chaos_gate | baseline, Evo I, Evo II, Evo III, Evo IV, Evo V |
| region_gate | state, strategic region, continent, or host-type requirement |
| host_gate | weak, colonial, occupied, low stability, wartime, overextended, low legitimacy, prior suppressor |
| origin_flag | always `chaosx_release_origin_independence_wave` after release |
| minimum_states | usually one, sometimes two or more when geography requires it |
| protected_state_policy | must never take protected host state at release |
| shrink_policy | how the package falls back to a smaller start |
| starting_government | ideology weights and special leaders |
| starting_army_band | petition, emergency, patron, old-name, land congress, strange |
| starting_ideas | temporary spirits and crisis flags |
| tree_access | shared provisional tree plus optional overlay |
| decision_access | which decision families are visible |
| asset_needs | flags, leaders, advisors, icons, event art |
| AI_profile | route and decision bias |
| failure_text | what the dossier says if skipped or reduced |

## Package enablement checklist

A package is enabled only when these checks pass.

1. The package has at least one valid start state after host survival protection.
2. The host remains alive with at least one state after the entire batch resolves.
3. The tag either already exists or a custom tag has been created and localized.
4. The release origin is set before any focus tree, decision, or startup event checks run.
5. The package has a valid focus access path.
6. The package has at least one flag and one fallback leader or council.
7. The package has country names for its supported ideological outcomes.
8. The package has AI behavior for ordinary survival and at least one route preference.
9. The package has cleanup rules for failed releases and civil splits.
10. The package does not require Event 005 content.

## Ordinary releasable package depth

Ordinary packages use existing releasables, but they should still vary by crisis context.

| Variant | Trigger direction | Startup spirit | Tree bias | Decision bias |
| --- | --- | --- | --- | --- |
| Civic petition state | host negotiated or invited observers | Petition Government | civic councils and recognition | recognition, observers, elections |
| Emergency depot state | host suppressed or war is nearby | Seized Depots | military survival and depot defense | brigades, depot inventory, radio station |
| Colonial assembly state | host is colonial or overseas | Assembly Against Distant Rule | civic, anti-patron, land congress if eligible | observers, autonomy settlement, diaspora committees |
| Occupation shadow state | host is occupied or losing cores | Provisional Administration | military and diplomacy | guarantee, volunteers, evacuation of archives |
| Patron-made state | major supplied or recognized early | Sponsored Cabinet | patron cabinet and anti-patron struggle | advisers, cabinet seats, broker exposure |
| Loyalist-split state | loyalists were armed | Divided Barracks | crisis branch and officer mandate | street defense, loyalist negotiations |

Ordinary packages should not all begin with the same government description. The crisis origin should be visible through events, spirits, and starting decisions.

## Dormant and game-rule package depth

Dormant or game-rule tags are more surprising than ordinary releasables, so their dossiers need stronger justification.

| Gate | Required explanation | Gameplay hook |
| --- | --- | --- |
| Tag exists through a game rule | local actors use a legal or exile precedent | recognition starts higher but legitimacy can be contested |
| Tag exists through a focus in another path | committee copies the symbol without the original sponsor | foreign attention rises and asset reuse must be checked |
| Tag exists as a generated Americas tag | local congress uses identity documentation or revival politics | land congress decisions and cultural recognition matter |
| Tag exists as a formable route | the committee claims a future state, not a full starting state | start small with claims and border commission |
| Tag exists as a dead tag | old government archives or surviving institutions return | historical-return pressure rises |

Do not enable dormant tags at baseline unless there are too few ordinary candidates and the result is still plausible.

## Historical-return package rules

Historical-return packages are not ordinary nostalgia. They should use old names to create modern political problems.

| Rule | Design effect |
| --- | --- |
| The old name is an argument, not an automatic core grant | package can start small and claim more later |
| Modern compromise must exist | player can build a state without becoming a mythic revanchist |
| Asset research matters | real symbols and leaders need sourced handling |
| Host survival still wins | old capitals can remain under the host at release |
| High chaos enables the package | lower tiers should not flood the map with old polities |
| The overlay changes focus flavor | same shared tree, but route text and decisions feel different |

## Historical-return package matrix, core set

| Package key | Name direction | Region gate | Minimum start | Main claim logic | Modern route | Escalation route | Asset notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iw_pkg_assyria` | Assyrian Provisional Authority, Assyria, Nineveh Assembly | northern Mesopotamia | one valid northern Mesopotamian state | Assyrian communities, ancient name, minority defense | civic assembly and protected rights | militant Nineveh directorate or archive-state | real symbols need source review |
| `iw_pkg_mesopotamia` | Mesopotamian Provisional State, River Republic, Kingdom of the Two Rivers | Iraq core or river basin states | one river state | Tigris and Euphrates administration, mandate memory | modern river administration | old empire symbolism or royal restoration | avoid generic ancient flag if not sourced |
| `iw_pkg_volga_bulgaria` | Volga Bulgar Provisional Council, Volga Bulgaria | Volga-Kama region | one valid Volga state | Bulgar memory, trade river, Islam, old city sites | modern federal republic | historical restoration or guarded mythic path | Event 006 overlay only |
| `iw_pkg_circassia` | Circassian Council, Cherkessia, Mountain Assembly | northwest Caucasus | one mountain or piedmont state | Circassian memory and diaspora | mountain autonomy state | exile return and Black Sea claims | symbol research required |
| `iw_pkg_mountain_republic` | Mountain Republic, North Caucasus Congress | North Caucasus multi-region | two states if possible, one if needed | mountain federalism and anti-imperial congress | federation compromise | armed mountain league | use only when state support allows |
| `iw_pkg_bukhara` | Bukhara Council, Emirate of Bukhara, Bukhara Republic | Bukhara or oasis region | one oasis state | city, emirate, Silk Road memory | reformist oasis republic | emirate restoration | real emir portraits must be sourced |
| `iw_pkg_khiva` | Khiva Council, Khwarezm Authority | Khiva or lower Amu Darya | one state | oasis and khanate memory | canal and oasis governance | khanate restoration | careful flag sourcing |
| `iw_pkg_kokand` | Kokand Valley Authority, Fergana Congress | Fergana region | one valley state | valley trade and khanate memory | valley republic | khanate or mountain border push | may need custom assets |

## African historical-return package matrix

| Package key | Name direction | Region gate | Minimum start | Main claim logic | Modern route | Escalation route | Asset notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iw_pkg_asante` | Asante Council, Asante Union, Kumasi Authority | southern Ghana or Ashanti region | one Kumasi-adjacent state if supported | Asante state memory and Kumasi center | constitutional council | royal restoration and regional claims | real symbols need source checks |
| `iw_pkg_sokoto` | Sokoto Council, Northern Emirates League | northern Nigeria or nearby Sahel | one state | emirate network and caliphate memory | emirate federation under modern law | militant emirate directorate | avoid flattening Fulani and Hausa identities |
| `iw_pkg_kanem_bornu` | Kanem-Bornu Authority, Lake Chad State | Lake Chad region | one lake-adjacent state | lake trade empire and mai memory | lake customs union | old empire border push | source symbols and leaders carefully |
| `iw_pkg_darfur` | Darfur Council, Sultanate of Darfur | western Sudan if state support exists | one Darfur state | sultanate memory and peripheral autonomy | protected regional state | armed sultanate | avoid modern conflict simplification |
| `iw_pkg_buganda` | Buganda Kingdom, Buganda Provisional Council | Uganda, Lake Victoria north shore | one Buganda state | kabaka and kingdom institutions | constitutional kingdom or civic council | protectorate renegotiation | real royal references need care |
| `iw_pkg_barotseland` | Barotseland Council, Lozi Floodplain Authority | western Zambia | one floodplain or western state | Lozi institutions and Barotseland memory | autonomy settlement | river kingdom restoration | floodplain and treaty imagery |
| `iw_pkg_zulu` | Zulu Council, Zululand Authority | Zululand or Natal region | one Zululand state | Zulu kingdom memory | constitutional royal council | regiment memory and border pressure | avoid turning route into only militarism |
| `iw_pkg_herero` | Herero Land Council, Ovaherero Authority | central Namibia | one state | land, cattle, colonial violence memory | land restitution state | grave memory and anti-colonial militancy | real traumatic history needs sober tone |
| `iw_pkg_nama` | Nama Council, Namaqua Authority | southern Namibia or Namaqualand | one state | Nama pastoral and land memory | land congress | grave memory and desert defense | source visual symbols carefully |
| `iw_pkg_palmares` | Palmares Republic, Quilombo Council | northeastern Brazil | one state | maroon settlement memory and anti-slavery resistance | defended republic | fortified maroon expansion | use sourced or symbolic assets carefully |

## South American local-polity package matrix

| Package key | Name direction | Region gate | Minimum start | Main claim logic | Modern route | Escalation route | Asset notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iw_pkg_mapuche` | Mapuche Congress, Araucania Council | south-central Chile, nearby Andes if valid | one state | land congress and Araucania memory | negotiated land congress | armed border defense | avoid monarchist joke route by default |
| `iw_pkg_aymara` | Aymara Highland Congress, Altiplano Authority | Bolivia, Peru, northern Chile | one highland state | Altiplano and Lake Titicaca communities | highland civic state | mining and border confrontation | textiles and lake motifs |
| `iw_pkg_guarani` | Guarani Assembly, River Forest Council | Paraguay and nearby states | one state | language and river communities | language republic | river defense and cross-border claims | real cultural symbols require review |
| `iw_pkg_charrua` | Charrua Memory Council, Rio de la Plata Assembly | Uruguay or nearby grasslands | one state | grasslands memory and identity recovery | civic recognition route | mobile militia and memory route | do not invent sacred symbols casually |
| `iw_pkg_tupi_coastal` | Coastal Tupi Assembly | Brazilian coast if supported | one state | coastal identity and colonial memory | local assembly | port and forest defense | optional later expansion |
| `iw_pkg_andes_communes` | Andean Community League | Andes if state support exists | one state | mountain community governance | communal autonomy | mining seizure crisis | may share Aymara mechanics |

## City, port, and railway packages

City and infrastructure packages exist because an independence wave can be about control of a node, not a full nation.

| Package | Spawn condition | Starting territory | Main gameplay | Host survival interaction |
| --- | --- | --- | --- | --- |
| Free port | major port in weak host | one port state | customs revenue, convoys, recognition, naval access | cannot take last port if it is protected state |
| Canal authority | canal or chokepoint state | one strategic state | guarantees, naval transit, patron pressure | skipped if host has one state |
| Industrial city | high factory state and low host legitimacy | one city state | strikes, factories, foreign investors | protected capital blocks release |
| Railway sovereignty | rail hub or supply node crisis | one rail state | supply, trains, military access, rail league | can start as enclave only if supported |
| Oil protectorate | oil state with foreign attention | one resource state | fuel, foreign guarantees, puppet pressure | high patron leverage by default |
| Border buffer | disputed border and major sponsor | one border state | guarantee, demilitarized zone, claims | cannot chain with another candidate that deletes host |

## Strange package rules

Strange packages should be rare and mechanically distinct.

| Package | Spawn gate | Statehood claim | Early effect | Containment path | Escalation path |
| --- | --- | --- | --- | --- | --- |
| Necromantic custodianship | Evo V, grave region, high deaths | the dead are counted as a constituency | manpower distortion and fear | civic purge, clerical containment, foreign quarantine | grave census, undead bureaucracy, strange pact |
| Anti-Mankind Directorate | Evo V, high radicalization, anti-human doctrine flag | political independence from humanity | diplomatic isolation and terror pressure | military overthrow, league embargo | anti-mankind league and world-threat hook |
| Archive-State | Evo V, destroyed administration, high archive evacuation | paperwork proves a state that reality denies | claims and recognition paradox | archive audit, legal settlement | infinite claims and sealed borders |
| Railway Cult | Evo V, rail hub collapse, supply disasters | rail routes become the body of the state | trains, supply, military access | civic rail authority | rail sovereignty and logistics cult |

Strange packages can use generated leaders and flags unless a real historical symbol is involved. They should not borrow real traumatic identity symbols for supernatural content.

## Package-specific AI profiles

| AI profile | Used by | Decision bias | Focus route bias | War behavior |
| --- | --- | --- | --- | --- |
| cautious_provisional | ordinary civic releases | recognition, elections, observers | civic councils and diplomacy | avoids offensive wars |
| survival_militia | emergency releases | depot, brigades, defensive belt | military survival | defends capital and cores |
| patron_client | protectorates and supported releases | accept advisers, request guarantee | patron cabinet | joins patron wars if dependent |
| anti_patron | high leverage states with civic legitimacy | expose brokers, league protection | anti-patron recovery | avoids patron wars |
| old_name_moderate | historical-return with low radicalization | archive review, modern compromise | historical-return modern route | uses claims cautiously |
| old_name_revisionist | historical-return with claim ambition | border surveys, ultimata | national directorate and old-state overlay | may start border wars |
| land_congress | local-polity states | land congress, community defense | local-polity overlay | defensive unless land war branch active |
| strange_actor | strange packages | hidden doctrine actions | strange module | unpredictable but gated by containment |

## Package failure and reduction text

Every package family needs short failure text so a reduced wave feels intentional.

| Situation | Text direction |
| --- | --- |
| skipped by host survival | The committee could not claim its capital without leaving the host government with no surviving territory |
| reduced to one state | The assembly accepts a foothold and records wider claims for later arbitration |
| overlapped by stronger package | Rival petitions force the conference to split the map before independence |
| no asset support | The dossier is deferred until usable symbols, names, and leaders exist |
| missing tag | The committee remains a movement until a custom tag is implemented |
| too many active wars | Foreign observers freeze recognition until the local war front stabilizes |

## Shared tag collision examples

| Shared tag | Event 005 use | Event 006 use |
| --- | --- | --- |
| Volga Bulgaria | Soviet Collapse old-state or regional collapse content | Independence Wave historical-return package with provisional tree and Volga overlay |
| Caucasus mountain tag | collapse route if tied to Event 005 successor logic | Independence Wave mountain congress or local-polity package |
| Central Asian emirate tag | collapse or scripted regional event if present | Independence Wave old-name return from weak host, no Event 005 variables |
| Generated Americas tag | ordinary or decision-created tag in base game | local-polity package with Event 006 land congress mechanics |

The implementation should never check the tag alone to assign content. It must check the origin flag first.

## Minimum package set for a satisfying first implementation

A first complete implementation should support enough packages to show the ladder without trying to build every possible tag.

| Tier | Minimum recommended support |
| --- | --- |
| Baseline | ordinary releasable package, civic and emergency variants |
| Evo I | dormant or game-rule package support, non-democratic ideology roll |
| Evo II | congress package behavior and mutual guarantee support |
| Evo III | protectorate, free port, border commission, patron struggle |
| Evo IV | at least six historical-return or local-polity packages from at least three continents |
| Evo V | at least two strange packages and one containment path |

Recommended high-chaos first set:

- Assyria or Mesopotamia for the Middle East
- Mapuche or Aymara for South America
- Asante or Buganda for Africa
- Volga Bulgaria for shared-tag origin separation testing
- Palmares for a distinct non-state memory package
- Circassia or Mountain Republic for mountain federation logic

## Asset dependency tiers for packages

| Asset tier | Packages allowed | Asset requirement |
| --- | --- | --- |
| Reuse tier | ordinary tags with existing content | existing flag and fallback leader |
| Light package tier | dormant tags and city states | one flag, council portrait, two icons |
| Historical package tier | old-name packages | flag, leader or council, overlay icons, event image direction |
| Full package tier | playable old-state or local polity | multiple flags, leaders, advisors, ideas, focus icons, decision icons |
| Strange tier | supernatural or impossible packages | generated flags, generated portraits, custom icons, super-event candidate art |

A package should not be enabled above its asset tier.

## Formation and package evolution rules

Country packages should define both release identity and possible later formation identity. A package does not need a formable route if it is a minor temporary actor, but any long-lived package should be checked for formation potential.

Formation data per package should include:

- formation family
- state group or target region
- route unlock
- hidden reveal condition if any
- formation decision
- post-formation missions
- identity changes
- flag and portrait needs
- AI willingness
- disqualifiers
- integration risks

## Package formation matrix

| Package type | Formation potential | Example routes | Default decision behavior |
| --- | --- | --- | --- |
| Standard releasable | low to medium | regional federation, local compact, League charter | visible after coalition or expansion branch |
| Game-rule or formable-compatible tag | medium | restore blocked vanilla-style identity through Event 006 origin | visible only when tag support and origin checks pass |
| Border protectorate | medium | protected mandate, border security union, sponsor-backed compact | visible when patron leverage is high |
| Free city or port | medium | free city league, merchant compact, port authority union | visible when trade and recognition routes mature |
| Railway sovereignty | medium to high | Railway League of Corridors, Corridor Directorate | visible when rail hubs and supply routes are controlled |
| Historical return | high | Assyria, Mesopotamia, Volga Bulgaria, Mapuche Araucania, Sokoto, Asante, Buganda, Kanem-Bornu, Palmares | hidden until route, old-state memory, and state control align |
| Local polity | high | Aymara, Guarani, Charrua, Barotse, Darfur, Herero, Nama, Zulu variants | hidden or route-locked, with local support and land congress requirements |
| Strange package | rare high | archive-state, necromantic registry, anti-mankind directorate, impossible railway authority | hidden behind high chaos and route reveal |

## Shared-tag and formation-origin logic

A country can have both release origin and formation origin.

Recommended tracking:

| Flag or variable | Scope | Meaning |
| --- | --- | --- |
| `chaosx_release_origin_independence_wave` | country | tag was created by Event 006 |
| `chaosx_formation_origin_independence_wave` | country | larger identity was formed through Event 006 |
| `chaosx_independence_wave_formable_family` | country | regional, historical_return, local_polity, protectorate, railway, strange |
| `chaosx_independence_wave_formed_tag_or_cosmetic` | country | final identity after formation |
| `chaosx_independence_wave_integration_stage` | country | post-formation integration progress |

The same base tag can appear in Event 005 and Event 006, but Event 006 formation decisions must only appear when the Event 006 release origin or formation origin is valid.

## Animated package identity

Some packages deserve animated portraits or animated symbols after route transformation:

- strange packages
- hidden historical-return routes
- final local-polity congresses
- anti-patron liberation leaders
- host-rump survivor leaders after The Rump That Endures
- railway sovereignty or archive-state symbolic councils

Ordinary provisional councils do not need animated portraits. Use static portraits unless animation communicates a major identity change.
