# Event 6: Independence Wave Country Packages

The event creates dynamic countries, so this file defines country packages instead of pretending every possible released state receives a bespoke tree. A country package is a complete identity rule set: tag selection, territory, ideology, names, leaders, assets, focus access, decisions, AI behavior, and release-origin handling.

## Current source-of-truth correction

Current source-of-truth map: `docs/plans/006_independence_wave_plans/source_of_truth_map.md`.

As of the 2026-06-08 correction, the active Event 006 base release pass uses a generic `every_possible_country` scan. Kuban (`KUB`) and Altai (`ALT`) are not package-expansion targets, but they may appear as ordinary vanilla releases if they pass the same inactive possible-country and host-safety checks as every other vanilla tag.

Niche generic, custom, and chaos-only countries are deferred to a later explicit pool. They should not be added by hardcoding every releasable tag into the base pass.

Playable wrap-up does not require every candidate in this package matrix to become a bespoke package. A country is acceptable for the current niche lane when it has a valid tag/country setup, unique flag support, safe release anchors, Event 006 origin, and access to the shared Liberation Provisional Tree. Package identity should be expressed through decisions, missions, ideas, route state, event details, localisation, claims, and leader/asset hooks while the shared tree stays generic. Package-specific focus stacks, full formables, animated route art, and package-specific report variants are future polish unless the user explicitly promotes a country into a bespoke route.

## Absolute host survival rule

No country package may delete its host. Every package must be carved from a host in a way that leaves the existing country with at least one state after the wave resolves. The protected state should be the current capital when the host still owns it. If the capital is not owned at resolution, the protected state is the best remaining owned state.

Package territory rules:

- full historical claims are inspiration, not mandatory starting borders
- starting territory may be reduced to one valid state if needed
- packages that need several states must be skipped when those states would remove the host from the map
- a package may receive claims on protected territory later, but not through the initial wave release
- the batch resolver must check the combined effect of all packages during hidden release validation
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
- Niche generic releasables using existing vanilla tags, cores, and flags, such as Katanga, Biafra, Cabo Verde, Rif, Rapa Nui, Rio Grande, Welsh Argentina, and inactive Horn of Africa tags. High-chaos generic releases can also use custom tags with verified anchor states and unique flag assets, including Asante, Kanem-Bornu, Palmares, and the Aymara Highland Congress. Asante and Kanem-Bornu have African story decisions and spirits while still sharing the Liberation Provisional Tree. Palmares and Aymara remain shared-tree niche tags until a later package pass promotes them.
- Borderland or minority states such as Kurdistan, Armenia, Azerbaijan, Georgia, Ukraine, Belarus, and other dormant tags if inactive and valid.
- Existing Americas deimperialized tags if the mod or game rule supports them, such as Charrua, Guarani, Itza, Maya, Miskito, Nahua, Inuit, Inca, and Isthmo-American identities.

The implementation agent must verify actual tag names from the repository. This spec gives design identities, not guaranteed tag IDs.

## Batch size by evolution

These are release-scale tiers. They should not create per-country evolution rows, package-specific evolution rows, or per-route progression entries. Baseline waves are ordinary release-scale behavior; the first actual evolution log milestone begins at Gathering Storm or the equivalent non-calm chaos condition.

| Evolution state | Release count target | Pool behavior |
| --- | ---: | --- |
| Baseline | 3 to 5 | ordinary tags only, mostly democratic |
| Dossier Surge | 4 to 6 | ordinary tags plus rare dormant tags |
| Rising Chaos Release Pattern | 5 to 7 | ordinary tags, regional clusters, city and protectorate packages |
| Chaos Tier Release Pattern | 6 to 9 | claims, patron-backed releases, stronger countries |
| Great Partition Week | 8 to 12 | historical-return, local-polity, strange, and impossible-state packages unlock if performance allows |
| Open Season | 10 to 16 | world-collapse release pressure lets the league-backed border crisis and hardest package claims spread at maximum scale |

If valid candidates are insufficient, release fewer countries. Do not spawn nonsense.

## Researched high-chaos candidate matrix

This matrix is an expansion pool. Do not implement every package blindly. Each row needs a valid tag, state mapping, assets, localisation, leader plan, and balance review.

| Candidate | Package family | Region logic | Suggested chaos gate | Focus overlay |
| --- | --- | --- | --- | --- |
| Assyria | Mesopotamian historical-return | Northern Mesopotamia, Nineveh, Mosul, Khabur, or nearby state cluster if valid | Evo IV | Assyria overlay |
| Mesopotamia | River-state or mandate-era revival | Tigris and Euphrates valley, Baghdad, Basra, Mosul if valid | Evo IV | Mesopotamia overlay |
| Marsh Arab river authority | Local-polity river package | Southern Iraq marshes and river districts | Evo IV | River and marsh local-polity overlay |
| Kurdistan | Existing or dormant tag | Kurdish-majority mountain regions if tag and states exist | Baseline to Evo II depending on setup | implemented mountain-registry overlay |
| Volga Bulgaria | Steppe historical-return | Volga and Kama region if valid | Evo IV | Volga overlay, not Event 005 tree |
| Idel-Ural | Steppe federation | Volga-Ural region if valid | Evo IV | federation overlay |
| Circassia | Caucasus historical-return | Northwest Caucasus if valid | Evo IV | mountain confederacy overlay |
| Mountain Republic | Caucasus confederation | North Caucasus mountain regions if valid | Evo IV | confederal council overlay |
| Don Host | Cossack or dormant tag | Don region if valid and not claimed by another event | Evo IV | implemented Don river records overlay |
| Kuban Host | Cossack or dormant tag | Kuban region if valid and not claimed by another event | Evo II to Evo IV | historical candidate only; superseded as current requested package scope |
| Altai-Oyrot Kurultai | Steppe/mountain historical-return | Altai Krai and Oyrot Region if valid | Evo IV | historical candidate only; superseded as current requested package scope |
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
| Namibia Land Council | Existing local-polity carrier | Khomas if Namibia is inactive and the host is weakened | Evo IV | implemented land-records overlay |
| Bechuanaland Kgotla Council | Existing local-polity carrier | Bechuanaland if Botswana is inactive and the host is weakened | Evo IV | implemented kgotla-records overlay |
| Gold Coast Legislative Council | Existing local-polity carrier | Ghana if GHA is inactive and the host is weakened | Evo IV | implemented Gold Coast records overlay |
| Mapuche Araucania | Indigenous local-polity | Southern Chile and Argentina if valid | Evo IV | land congress and mountain defense overlay |
| Aymara congress | Indigenous local-polity | Altiplano in Bolivia, Peru, Chile, Argentina if valid | Evo IV | Altiplano community overlay |
| Guarani republic | Indigenous or game-rule tag | Paraguay, southern Brazil, northern Argentina, Uruguay if valid | Evo II to Evo IV | forest and language overlay |
| Charrua revival | Indigenous or game-rule tag | Uruguay and nearby regions if valid | Evo II to Evo IV | fragile survival overlay |
| Palmares | Quilombo historical-return | Brazilian interior or northeast if state mapping supports it | Evo IV | forest defense and hidden settlement overlay |
| Muisca cultural state | Indigenous local-polity | Colombian highlands if valid | Evo IV | council and mountain overlay |
| Maya | Game-rule or indigenous package | Yucatan and adjacent Maya regions if valid | Evo II to Evo IV | land congress overlay |
| Itza | Game-rule or indigenous package | Peten and Yucatan region if valid | Evo II to Evo IV | implemented lake-council overlay |
| Nahua | Game-rule or indigenous package | Central Mexico if valid | Evo II to Evo IV | old name and modern charter overlay |
| Miskito | Game-rule or local-polity | Mosquito Coast if valid | Evo II to Evo IV | protectorate coast overlay |
| Inuit union | Game-rule or local-polity | Arctic regions if valid | Evo II to Evo IV | survival and recognition overlay |
| Free City | City package | high-value port, treaty city, canal city, industrial hub | Evo II | free city overlay |
| Railway Republic | Infrastructure package | rail junction, supply hub, bridge region | Evo II | railway overlay |
| Archive-State | Strange package | collapsed capital or dead bureaucracy | Evo V | archive-state module |
| Necromantic Custodianship | Strange package | grave, battlefield, camp, mass-death, plague zone | Evo V | necromancy module |
| Anti-Mankind Directorate | Strange package | explicit anti-human doctrine pressure | Evo V | anti-mankind module |

## Current African Story Mechanics

The first African story pass keeps the shared Liberation Provisional Tree generic and places distinct country flavor in decisions, ideas, claims, leaders, and route flags:

- `ASN` can convene the Asante Stool Court, gaining legitimacy, local-polity strength, a stool-court spirit, and public claims on nearby West African proof territory.
- `KBN` can open the Kanem-Bornu Caravan Court, gaining legitimacy, claim ambition, a caravan-authority spirit, and claims around the Lake Chad/Sahel route.
- `DFR` can sign the Acacia Frontier Pact, gaining militia strength, a frontier pact spirit, and Darfur proof claims.
- `ZUL` can raise the Lion Crown, gaining militia strength, claims, and a lion-crown spirit, and can seat the Gorilla Chair as a strange high-chaos leader route using a generated portrait.
- African story releases can call an African Dossier Congress to turn local stories into shared Congress proof and foreign attention.

Further African continent passes should extend this same pattern to additional African releases without adding country-specific stacked focuses to the shared tree.

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
| `iw_pkg_dahomey` | Dahomey Palace Council, Bight Customs Authority | Bight of Benin | one coastal state | Dahomey old-state memory and coastal customs | palace council under public law | customs-backed old-name pressure | vanilla DAH has flags and advisors, but no bespoke country leader role |
| `iw_pkg_sokoto` | Sokoto Council, Northern Emirates League | northern Nigeria or nearby Sahel | one state | emirate network and caliphate memory | emirate federation under modern law | militant emirate directorate | avoid flattening Fulani and Hausa identities |
| `iw_pkg_kanem_bornu` | Kanem-Bornu Authority, Lake Chad State | Lake Chad region | one lake-adjacent state | lake trade empire and mai memory | lake customs union | old empire border push | source symbols and leaders carefully |
| `iw_pkg_darfur` | Darfur Council, Sultanate of Darfur | western Sudan if state support exists | South Darfur `887` | South Darfur records and North Darfur petitions | protected regional council | armed sultanate or regional council | implemented as custom `DFR`; avoid modern conflict simplification |
| `iw_pkg_buganda` | Buganda Kingdom, Buganda Provisional Council | Uganda, Lake Victoria north shore | one Buganda state | kabaka and kingdom institutions | constitutional kingdom or civic council | protectorate renegotiation | real royal references need care |
| `iw_pkg_barotseland` | Barotseland Council, Lozi Floodplain Authority | western Zambia | one floodplain or western state | Lozi institutions and Barotseland memory | autonomy settlement | river kingdom restoration | floodplain and treaty imagery |
| `iw_pkg_zulu` | Zulu Council, Zululand Authority | Zululand or Natal region | one Zululand state | Zulu kingdom memory | constitutional royal council | regiment memory and border pressure | avoid turning route into only militarism |
| `iw_pkg_herero` | Herero Land Council, Ovaherero Authority | central Namibia | one state | land, cattle, colonial violence memory | land restitution state | grave memory and anti-colonial militancy | real traumatic history needs sober tone |
| `iw_pkg_nama` | Nama Council, Namaqua Authority | southern Namibia or Namaqualand | one state | Nama pastoral and land memory | land congress | grave memory and desert defense | source visual symbols carefully |
| `iw_pkg_palmares` | Palmares Republic, Quilombo Council | northeastern Brazil | one state | maroon settlement memory and anti-slavery resistance | defended republic | fortified maroon expansion | use sourced or symbolic assets carefully |

## Implemented starter packages

The current implementation enables verified high-chaos starter packages without adding new tags or unsourced leader content.

| Package key | Carrier tag | Initial release | Proof route | Release constraint |
| --- | --- | --- | --- | --- |
| `iw_pkg_buganda` | vanilla `UGA` | state `548` Uganda | Lukiko records, protectorate treaty review, Buganda Lukiko Charter | enabled at chaos tier IV/V when UGA is inactive and state `548` has a weakened host |
| `iw_pkg_sokoto` | vanilla `SOK` | state `902` Sokoto | scholar council, northern emirate registers, Sokoto Emirate Federation | enabled at chaos tier IV/V; Event 006 masks SOK cores on `901` and `781` during release, then restores them as later claim/proof targets |
| `iw_pkg_bukhara` | vanilla `BUK` | state `830` Bukhara | oasis council, oasis charter, Bukhara Oasis Assembly | enabled at chaos tier IV/V when BUK is inactive and state `830` has a weakened host; state `742` remains later proof/claim territory |
| `iw_pkg_khiva` | vanilla `KHI` | state `831` Khiva | canal council, water charter, Khiva Khanate Assembly | enabled at chaos tier IV/V when KHI is inactive and state `831` has a weakened host; state `832` remains later proof/claim territory |
| `iw_pkg_mesopotamia` | vanilla `IRQ` | state `291` Iraq/Baghdad | river records, river-petition map, Mesopotamian River Compact | enabled at chaos tier IV/V when IRQ is inactive and state `291` has a weakened host; Mosul `676`, Basrah `1011`, Anbar `1010`, and Al Hajara `675` remain later proof/claim territory |
| `iw_pkg_don_cossack_krug` | vanilla `DON` | state `218` Rostov | Don river records, Don petition map, Don Cossack Krug | enabled at chaos tier IV/V when DON is inactive and state `218` has a weakened host; Millerovo `245` and Volgodonsk `238` remain later proof/claim territory |
| `iw_pkg_barotseland` | vanilla `BAR` | state `981` Barotseland | Litunga records, floodplain treaty map, Barotse Floodplain Council | enabled at chaos tier IV/V when BAR is inactive and state `981` has a weakened host; vanilla BAR history, leader, localisation, portraits, and flags are reused |
| `iw_pkg_dahomey` | vanilla `DAH` | state `776` Dahomey | palace council, Bight customs charter, Dahomey Palace Council | enabled at chaos tier IV/V when DAH is inactive and state `776` has a weakened host; vanilla DAH history, localisation, advisors, and flags are reused |
| `iw_pkg_miskito` | vanilla `MIS` | state `317` Nicaragua | shore records, coastal petition map, Miskito Shore Council | enabled at chaos tier IV/V when MIS is inactive and state `317` has a weakened host; Event 006 dynamically adds cores on states `312` and `317`, starts from `317`, keeps `312` as later proof/claim territory, and reuses vanilla MIS history, council leader, localisation, portraits, and flags |
| `iw_pkg_itza` | vanilla `ITZ` | state `311` Belize | Peten records, Yucatan petition map, Itza Lake Council | enabled at chaos tier IV/V when ITZ is inactive and state `311` has a weakened host; Event 006 dynamically adds the vanilla-commented core on state `311`, starts from `311`, keeps state `313` as later proof/claim territory, and reuses vanilla ITZ history, council leader, localisation, portraits, and flags |
| `iw_pkg_maya` | vanilla `MAY` | state `475` Chiapas | Maya council records, peninsula petition map, Maya Yucatan Assembly | enabled at chaos tier IV/V when MAY is inactive and state `475` has a weakened host; Event 006 dynamically adds the vanilla-commented core set on `313`, `474`, `475`, and `476`, starts from `475`, keeps `313`, `474`, and `476` as later proof/claim territory, and reuses vanilla MAY history, council leader, localisation, portraits, and flags |
| `iw_pkg_circassia` | vanilla `KBK` | state `827` Kabardino-Balkaria/Nalchik | mountain records, Caucasus pass petitions, Circassian Mountain Council | enabled at chaos tier IV/V when KBK is inactive and state `827` has a weakened host; vanilla KBK history, localisation, portraits, and flags are reused, while states `821` and `826` remain later petition/claim targets |
| `iw_pkg_andes_communes` | vanilla `INC` | state `947` Tacna-Moquegua, state `494` Ucayali, or state `951` Arica y Tarapaca | highland records, Andean petition map, Andean Community League | enabled at chaos tier IV/V when INC is inactive and one of the release seats has a weakened host; Event 006 dynamically adds release cores only on `947`, `494`, and `951`, keeps Lima `303`, Piura `492`, and Antofagasta `506` as later proof/claim territory, and reuses vanilla INC history, council, localisation, portraits, and flags |
| `iw_pkg_nahua` | vanilla `NAH` | state `314` San Salvador | San Salvador records, charter petition map, Nahua Charter Assembly | enabled at chaos tier IV/V when NAH is inactive and state `314` has a weakened host; Event 006 dynamically adds the vanilla-precedent core on `314`, starts from `314`, keeps wider claims out of the first tranche, and reuses vanilla NAH history, council, localisation, portraits, and flags |
| `iw_pkg_inuit` | vanilla `INU` | state `463` Alaska | Arctic register, Arctic petition map, Inuit Arctic Council | enabled at chaos tier IV/V when INU is inactive and state `463` has a weakened host; Event 006 dynamically adds the vanilla Inuit core set on `463`, `864`, `472`, `683`, `466`, `332`, `101`, and `861`, starts from `463`, keeps the wider Arctic map as later proof/claim territory, and reuses vanilla INU history, council, localisation, portraits, and flags |
| `iw_pkg_namibia` | vanilla `NMB` | state `541` Khomas | Khomas land records, land petition map, Namibia Land Council | enabled at chaos tier IV/V when NMB is inactive and state `541` has a weakened host; Event 006 starts from vanilla NMB's Khomas core, records land petitions as proof territory, and reuses vanilla NMB history, characters, localisation, portraits, and flags |
| `iw_pkg_bechuanaland` | vanilla `BOT` | state `542` Bechuanaland | kgotla records, district petition map, Bechuanaland Kgotla Council | enabled at chaos tier IV/V when BOT is inactive and state `542` has a weakened host; Event 006 starts from vanilla BOT's Bechuanaland core, records district petitions as proof territory, and reuses vanilla BOT history, characters, localisation, portraits, and flags |
| `iw_pkg_palestine_mandate` | vanilla `PAL` | state `454` Palestine | treaty audit, guarantee review, Palestine Mandate Council | enabled at chaos tier III or higher when PAL is inactive and state `454` has a weakened non-capital host; Event 006 starts from vanilla PAL's Palestine core, uses the shared Protected Mandate route under a Palestine-specific package label, and reuses vanilla PAL history, mandate cosmetic tag, characters, localisation, portraits, and flags |
| `iw_pkg_ghana` | vanilla `GHA` | state `274` Ghana | Gold Coast records, council petition map, Gold Coast Legislative Council | enabled at chaos tier IV/V when GHA is inactive and state `274` has a weakened host; Event 006 starts from vanilla GHA's Ghana core, records Gold Coast petitions as proof territory, and reuses vanilla GHA history, characters, localisation, portraits, and flags |
| `iw_pkg_eritrea_red_sea` | vanilla `ERI` | state `550` Eritrea | Red Sea records, coastal petition map, Eritrea Red Sea Council | enabled at chaos tier IV/V when ERI is inactive and state `550` has a weakened host; Event 006 starts from vanilla ERI's Eritrea core, records coastal petitions as proof territory, and reuses vanilla ERI history, characters, localisation, portraits, and flags |
| `iw_pkg_darfur` | custom `DFR` | state `887` South Darfur, with North Darfur `767` as petition proof | Darfur records, North Darfur petition map, Darfur Council, Acacia Frontier Pact | enabled at chaos tier IV/V when DFR is inactive and South Darfur has a weakened host; Event 006 seeds DFR cores at runtime, starts from South Darfur because North Darfur is impassable and force-linked in vanilla, uses a vanilla generic African leader portrait, and uses imagegen-regenerated DFR flag assets |
| `iw_pkg_zulu` | custom `ZUL` | state `719` Natal | Natal records, royal-house petitions, regimental rolls, Zulu Council, Lion Crown, Gorilla Chair | enabled at chaos tier IV/V when ZUL is inactive and Natal has a weakened host; Event 006 seeds a ZUL core at runtime, starts from Natal only, uses custom country/history/localisation files, imagegen-regenerated ZUL flag assets, and the generated Gorilla Chair portrait for the strange-story decision route |
| `iw_pkg_mapuche` | custom `MAP` | state `950` Araucania, with Aysen `949` and Rio Negro `512` as later survey/recovery territory | Araucania land records, Mapuche land-petition map, Mapuche Land Congress | enabled at chaos tier IV/V when MAP is inactive and Araucania has a weakened host; Event 006 seeds MAP cores at runtime, starts from Araucania, uses custom country/history/localisation files, a vanilla generic South American leader portrait, and uses imagegen-regenerated MAP flag assets |

Implementation notes:

- `UGA` is accepted as the Buganda carrier because vanilla country localisation already supports `UGA_neutrality = "Kingdom of Buganda"` and state `548` is a clean one-state start.
- `SOK` uses vanilla tag, history, localisation, and flags, but the initial Event 006 release is constrained to `902` so Borno `901` and Niger `781` remain later proof targets rather than free cross-colonial territory.
- `BUK` uses vanilla tag, history, localisation, and flags. Vanilla BUK has capital `830`, state `830` core, and Stalinabad `742` core; Event 006 starts the package from Bukhara and records Stalinabad as a later proof target instead of granting it for free.
- `KHI` uses vanilla tag, history, localisation, and flags. Vanilla KHI has capital `831`, cores on Khiva `831` and Dashhowuz `832`, and existing flag assets; Event 006 starts the package from Khiva and records Dashhowuz as a later proof target instead of granting it for free.
- `IRQ` is accepted as the Mesopotamian River Compact carrier because vanilla country history sets capital `291`, vanilla Iraq states already carry IRQ cores, and vanilla provides country history, characters, localisation, portraits, and ideology flag assets. Event 006 starts from Baghdad, treats Mosul, Basrah, Anbar, and Al Hajara as later river-petition proof territory, and does not create or replace flags.
- `DON` is accepted as the Don Cossack Krug carrier because vanilla country history sets capital `218`, vanilla provides country history, character data, localisation, parties, and complete ideology flag assets. Event 006 starts from Rostov, temporarily masks any broader Don cores on Millerovo and Volgodonsk during release selection, treats those states as later Don-petition proof territory, and does not create or replace flags.
- Superseded KUB/ALT note: earlier Kuban Cossack Rada and Altai-Oyrot Kurultai package handoffs framed `KUB` and `ALT` as implemented Event 006 package carriers. The 2026-06-05 user correction supersedes that framing for current scope. Do not treat KUB/ALT as accepted Event 006 package additions, package-overlay targets, or asset requests unless a later user request explicitly reopens them.
- `BAR` uses vanilla tag, history, localisation, leader data, portrait registration, and all ideology flag assets. Vanilla BAR has capital/core state `981`; Event 006 starts and proves the package from that single floodplain state.
- `DAH` uses vanilla tag, history, localisation, advisors, and all ideology flag assets. Vanilla DAH has capital/core state `776`; Event 006 starts and proves the package from that single coastal state. Vanilla DAH does not provide a clear country-leader role, so this tranche avoids bespoke leader or portrait creation and keeps authority represented through the Event 006 palace council spirit, decisions, focuses, and log entries.
- `MIS` uses vanilla tag, history, council character, localisation, portraits, and all ideology flag assets. Vanilla history comments list cores on `312` and `317`, and vanilla Chile liberation precedent dynamically adds those cores before transfer; Event 006 owns the same dynamic core seeding without editing state history.
- `ITZ` uses vanilla tag, history, council character, localisation, portraits, and all ideology flag assets. Vanilla history comments list core `311`, and vanilla Chile liberation precedent dynamically adds that core before transfer; Event 006 owns the same dynamic core seeding without editing state history and records `313` as later Yucatan petition proof instead of direct expansion.
- `MAY` uses vanilla tag, history, council character, localisation, portraits, and all ideology flag assets. Vanilla history comments list cores on `313`, `474`, `475`, and `476`, and vanilla Chile liberation precedent dynamically adds those cores before transfer; Event 006 owns the same dynamic core seeding without editing state history, starts from Chiapas `475`, and records `313`, `474`, and `476` as later peninsula petition proof instead of direct expansion.
- `KBK` is accepted as the Circassian package carrier because vanilla country localisation includes Circassian and Kabardino-Balkarian identity variants, state `827` is a clean mountain start, and vanilla flag/history/portrait support exists. Event 006 starts the package from Nalchik and records nearby Caucasus pass petitions as proof targets instead of granting them during release.
- `INC` is accepted as an Andean Community League carrier because vanilla provides a real Neo-Inca/Inca tag, country history, council character, localisation, portraits, and flags. Event 006 does not treat this as a Mapuche or Aymara fallback. It starts only from supported non-capital seats and records Lima, Piura, and Antofagasta as petition targets rather than free expansion.
- `NAH` is accepted as a Nahua Charter Assembly carrier only through vanilla's San Salvador support: vanilla NAH history sets capital `314`, vanilla Trial of Allegiance scripting dynamically adds a `NAH` core to state `314`, and vanilla provides the council character, localisation, portraits, and flags. Event 006 does not treat this as a central-Mexico, Mapuche, Aymara, or generic Yucatan fallback.
- `INU` is accepted as an Inuit Arctic Council carrier only through vanilla Arctic support: vanilla INU history sets capital `463`, vanilla history comments list cores on `463`, `864`, `472`, `683`, `466`, `332`, `101`, and `861`, and vanilla Chile liberation scripting dynamically adds those cores before transfer. Event 006 starts from Alaska `463`, records the other Arctic states as proof and petition targets, does not include optional vanilla `875` or `650` in this first package, and does not use Event 005 content.
- `NMB` is accepted as a Namibia Land Council carrier through vanilla South West Africa support: vanilla NMB history sets capital `541`, vanilla state `541` Khomas has an NMB core, and vanilla provides country history, characters, localisation, portraits, and ideology flag assets. Event 006 starts from Khomas, treats broader Namibian land petitions as proof rather than free expansion, and does not require new flags.
- `BOT` is accepted as a Bechuanaland Kgotla Council carrier through vanilla Botswana support: vanilla BOT history sets capital `542`, vanilla state `542` Bechuanaland has a BOT core, and vanilla provides country history, characters, localisation, portraits, and ideology flag assets. Event 006 starts from Bechuanaland, treats district petitions as proof rather than free expansion, and does not require new flags.
- `PAL` is accepted as a Palestine Mandate Council carrier through vanilla Palestine support: vanilla PAL history sets capital `454`, vanilla state `454` Palestine has a PAL core, vanilla history applies the `PAL_mandate` cosmetic tag, and vanilla provides country history, characters, localisation, portraits, and ideology plus mandate flag assets. Event 006 starts from Palestine, uses the shared Protected Mandate treaty route under a distinct package label, and does not require new flags.
- `GHA` is accepted as a Gold Coast Legislative Council carrier through vanilla Ghana support: vanilla GHA history sets capital `274`, vanilla state `274` Ghana has a GHA core, and vanilla provides country history, characters, localisation, portraits, and ideology flag assets. Event 006 starts from Ghana, treats Gold Coast petitions as proof rather than free expansion, and does not require new flags.
- `DFR` is accepted as a custom Darfur Council carrier through Event 006 runtime core seeding. Vanilla South Darfur `887` is a controlled, releasable starting anchor; vanilla North Darfur `767` is impassable and force-linked, so Event 006 treats it as a petition/proof target instead of a starting state. DFR uses custom country/history/localisation files, a vanilla generic African portrait, Acacia Frontier Pact story mechanics, and imagegen-regenerated flag assets documented under `docs/assets/006_independence_wave/flags/manifest.md`.
- `ZUL` is accepted as a custom Zulu Council carrier through Event 006 runtime core seeding. Natal `719` is the controlled starting anchor and proof state; broader royal-house and regimental petitions remain represented through route variables, decisions, and focus rewards rather than free starting expansion. ZUL uses custom country/history/localisation files, Lion Crown story mechanics, the Gorilla Chair strange-story leader hook, imagegen-regenerated flag assets, and the generated Gorilla Chair portrait documented under `docs/assets/006_independence_wave/leader_portraits/manifest.md`.
- `MAP` is accepted as a custom Mapuche Land Congress carrier through Event 006 runtime core seeding. Araucania `950` is the controlled starting anchor and proof state; Aysen `949` and Rio Negro `512` become surveyed cores through Mapuche land-petition work so the generic Border Commission recovery path can transfer more territory without erasing a host. MAP uses custom country/history/localisation files, a vanilla generic South American portrait, and imagegen-regenerated flag assets documented under `docs/assets/006_independence_wave/flags/manifest.md`.
- Event 005 references `KHI` in progressive-release candidate logic only. Event 006 keeps Khiva separated through high-chaos package gating, Event 006 origin flags, and `independence_wave_package_khiva`; no Event 005 focus tree, decision, event-log, or helper file is touched for the Khiva package.
- These packages use Event 006 origin flags, the shared provisional focus tree, package-specific startup spirits, Formation Ledger decisions, and Event 006 route state. Evolution logging remains tier-scoped rather than package-scoped.
- No Event 005 focus tree, decision, event-log, or helper state is used by these packages.
- Generic non-Danzig city/port releases now receive the `free_port_authority` package label, `independence_wave_package_free_port_authority`, Free Port Manifest and Harbor Courts focuses, manifest/customs/proclamation decisions, and a post-proclamation integration mission. This package uses the existing Event 006 free-city board idea/icon family, does not create or replace flags, and does not write per-route evolution rows.
- Canal-state city/port releases now receive the `canal_authority` package label, `independence_wave_package_canal_authority`, Canal Register and Pilot Offices focuses, register/transit-charter/proclamation decisions, a post-proclamation integration mission, and a canal authority spirit. This package uses the existing Event 006 free-city board idea/icon family, does not create or replace flags, and does not write per-route evolution rows.
- Inland city-state releases without harbor or canal control now receive the `municipal_authority` package label, `independence_wave_package_municipal_authority`, Municipal Charter File and Service Patrols focuses, charter/service-board/proclamation decisions, a post-proclamation integration mission, and a municipal authority spirit. This package uses existing Event 006 municipal/free-city board icon families, does not create or replace flags, and does not write per-route evolution rows.
- Generic non-oil protectorate releases now receive the `protectorate_mandate` package label, `independence_wave_package_protectorate_mandate`, Protectorate Treaty Audit and Observer Ministry focuses, treaty audit/guarantee review/proclamation decisions, a post-proclamation integration mission, and a protectorate mandate spirit. This package uses the existing Event 006 sponsored-cabinet idea/icon family, does not create or replace flags, and does not write per-route evolution rows.
- Palestine Mandate releases now receive the `palestine_mandate` package label, `independence_wave_package_palestine_mandate`, and the shared Protected Mandate focus, treaty audit, guarantee review, proclamation, post-proclamation integration mission, and protectorate mandate spirit. This package uses vanilla PAL assets and existing Event 006 sponsored-cabinet idea/icon families, does not create or replace flags, and does not write per-route evolution rows.
- Ghana releases now receive the `ghana` package label, `independence_wave_package_ghana`, Gold Coast records and petition focuses, record/petition/proclamation decisions, a post-proclamation integration mission, and a Gold Coast Legislative Council spirit. This package uses vanilla GHA assets and existing Event 006 local-polity idea/icon families, does not create or replace flags, and does not write per-route evolution rows.
- Eritrea releases now receive the `eritrea` package label, `independence_wave_package_eritrea`, Red Sea records and coastal-petition focuses, record/petition/proclamation decisions, a post-proclamation integration mission, and an Eritrea Red Sea Council spirit. This package uses vanilla ERI assets and existing Event 006 local-polity idea/icon families, does not create or replace flags, and does not write per-route evolution rows.
- Darfur releases now receive the `darfur` package label, `independence_wave_package_darfur`, Darfur records and petition focuses, record/petition/proclamation decisions, a post-proclamation integration mission, and a Darfur Council spirit. This package uses custom DFR tag/history/country/localisation files, a vanilla generic African portrait, subagent-created reconstructed DFR flags, and existing Event 006 local-polity idea/icon families, and does not write per-route evolution rows.
- Mapuche releases now receive the `mapuche` package label, `independence_wave_package_mapuche`, Araucania land records and petition decisions, a proclamation decision, a post-proclamation integration mission, and a Mapuche Land Congress spirit. This package uses custom MAP tag/history/country/localisation files, a vanilla generic South American portrait, subagent-created upright MAP flags, existing Event 006 local-polity idea/icon families, the shared provisional focus tree, and does not write per-route evolution rows.
- Mesopotamian releases now receive the `mesopotamia` package label, `independence_wave_package_mesopotamia`, Mesopotamian river records and petition focuses, record/petition/proclamation decisions, a post-proclamation integration mission, and a Mesopotamian River Compact spirit. This package uses vanilla IRQ assets and existing Event 006 old-name idea/icon families, does not create or replace flags, and does not write per-route evolution rows.
- Don releases now receive the `don_cossack_host` package label, `independence_wave_package_don`, Don river records and petition focuses, record/petition/proclamation decisions, a post-proclamation integration mission, and a Don Cossack Krug spirit. This package uses vanilla DON assets and existing Event 006 old-name idea/icon families, does not create or replace flags, and does not write per-route evolution rows.
- KUB/ALT package implementation claims in older handoffs are superseded for source-of-truth purposes. They are not current Event 006 package scope, they should not drive package-specific evolution rows, and they should not displace the generic niche release lane.
- Oil-state protectorate releases now receive the `oil_protectorate` package label, `independence_wave_package_oil_protectorate`, Oil Concession Audit and Oil-Field Guard Offices focuses, concession audit/fuel board/proclamation decisions, a post-proclamation integration mission, and an oil protectorate spirit. This package uses the existing Event 006 sponsored-cabinet idea/icon family, does not create or replace flags, and does not write per-route evolution rows.
- Package-specific portraits, seals, animated route art, and any future flag work remain asset work. Current gameplay wiring uses Event 006 category, decision, idea, and focus icon families while vanilla tag assets remain untouched.

## Central American local-polity package matrix

| Package key | Name direction | Region gate | Minimum start | Main claim logic | Modern route | Escalation route | Asset notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iw_pkg_miskito` | Miskito Shore Council, Mosquito Coast Authority | Caribbean coast of Central America | state `317` | shore records and coastal petitions | shore council under public law | coastal petition pressure | implemented with vanilla MIS flags and council portrait |
| `iw_pkg_maya` | Maya Council, Yucatan Assembly | Yucatan and nearby Maya states | state `475` | council records and Maya municipal petitions | council federation | peninsula proof claims | implemented with vanilla MAY flags and council portrait |
| `iw_pkg_itza` | Itza Lake Council, Peten Authority | Peten and Yucatan support | state `311` | Peten records and Yucatan petitions | lake council under public law | Yucatan petition pressure | implemented with vanilla ITZ flags and council portrait |

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
| Municipal authority | inland city state without harbor or canal control | one city state | service boards, workshops, courts, public order | protected capital blocks release |
| Railway sovereignty | rail hub or supply node crisis | one rail state | supply, trains, military access, rail league | can start as enclave only if supported |
| Oil protectorate | oil state with foreign attention | one resource state | fuel, foreign guarantees, puppet pressure | high patron leverage by default |
| Border buffer | disputed border and major sponsor | one border state | guarantee, demilitarized zone, claims | cannot chain with another candidate that deletes host |

Implemented support:

- Free port authority gameplay is implemented for non-Danzig Event 006 city/port releases that control a coastal owned state with a naval base. The route opens a manifest, negotiates a customs charter, proclaims a Free Port Authority, and runs an integration mission that fails if the authority becomes a subject or loses harbor control.
- Canal authority gameplay is implemented for non-Danzig Event 006 city/port releases that control a canal state. The route opens a canal register, negotiates a transit charter, proclaims a Canal Authority, and runs an integration mission that fails if the authority becomes a subject, loses canal control, or patron leverage reaches the dangerous threshold.
- Municipal authority gameplay is implemented for non-Danzig Event 006 city-package releases that control an inland city state but no harbor or canal state. The route opens a municipal charter file, organizes a service board, proclaims a Municipal Authority, and runs an integration mission that fails if the authority becomes a subject or loses inland city control.
- Protected mandate gameplay is implemented for generic non-oil Event 006 protectorate-package releases. The route audits treaty files, reviews guarantees to reduce leverage, proclaims a Protected Mandate, and runs an integration mission that fails if the mandate becomes a subject or patron leverage reaches the dangerous threshold.
- Oil protectorate gameplay is implemented for Event 006 protectorate-package releases that control an oil-producing state. The route audits oil concessions, seats a fuel board, proclaims an Oil Protectorate, and runs an integration mission that fails if the protectorate becomes a subject, loses oil-field control, or lets patron leverage reach the dangerous threshold.
- Danzig keeps its bespoke Free City Board and Danzig Free City charter path instead of using the generic free-port authority label.
- The generic routes currently reuse Event 006 free-city board, municipal workshop, and sponsored-cabinet art, decision icons, and existing idea icon families. Bespoke free-port seals, canal seals, municipal seals, protectorate mandate seals, oil-concession seals, merchant-council or treaty-broker portraits, animated route art, and unique future flag work remain asset follow-up items.

## Strange package rules

Strange packages should be rare and mechanically distinct.

| Package | Spawn gate | Statehood claim | Early effect | Containment path | Escalation path |
| --- | --- | --- | --- | --- | --- |
| Necromantic custodianship | Evo V, grave region, high deaths | the dead are counted as a constituency | manpower distortion and fear | civic purge, clerical containment, foreign quarantine | grave census, undead bureaucracy, strange pact |
| Anti-Mankind Directorate | Evo V, high radicalization, anti-human doctrine flag | political independence from humanity | diplomatic isolation and terror pressure | military overthrow, league embargo | anti-mankind league and world-threat hook |
| Archive-State | Evo V, destroyed administration, high archive evacuation | paperwork proves a state that reality denies | claims and recognition paradox | archive audit, legal settlement | infinite claims and sealed borders |
| Railway Cult | Evo V, rail hub collapse, supply disasters | rail routes become the body of the state | trains, supply, military access | civic rail authority | rail sovereignty and logistics cult |

Strange packages can use generated leaders and flags unless a real historical symbol is involved. They should not borrow real traumatic identity symbols for supernatural content.

## Implemented strange package identities

The current implementation enables two first-pass Evo V strange package identities without adding new tags, country files, history files, or flag assets.

| Package key | Carrier | Package proof | Release constraint |
| --- | --- | --- | --- |
| `iw_pkg_archive_state` | any valid Event 006 strange release | Sealed Archive Audit, archive-state route state, containment or unmarked congress follow-through | enabled at chaos tier V when the release receives the strange package marker; city, port, railway, and administrative packages default to archive-state behavior |
| `iw_pkg_necromantic_custodianship` | any valid Event 006 strange release with rural, pastoral, or wasteland authority and no city/railway override | Quiet Dead Census, necromantic route state, containment or unmarked congress follow-through | enabled at chaos tier V when the release receives the strange package marker and its initial state profile fits the grave-register heuristic |

Implementation notes:

- These identities use Event 006 origin flags, `independence_wave_package_archive_state` or `independence_wave_package_necromantic_custodianship`, package IDs, Formation Ledger labels, Sealed Dossier decisions, and AI strategy overlays.
- The shared containment path remains the first implemented resolution path for both identities. Archive-State actors are nudged toward audits and registry containment; Necromantic Custodianships are nudged toward the quiet census and stronger militia posture.
- These package identities do not load Event 005 content and do not create new tag files or flag assets.
- Final strange package portraits, route seals, animated dossier states, and bespoke strange flags remain asset work before strange packages can be treated as fully finished visual packages.

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

## Formation and package history rules

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
