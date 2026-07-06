# 006 Independence Wave Spec Part 4: Focus Trees and Country Packages

## Focus tree architecture

## Design promise for the focus and country layer

Independence Wave countries should not appear as empty tags with generic map color and no gameplay. Every Event 6 origin country should receive a survival problem, a political direction problem, a military problem, a diplomacy problem, a former host problem, and a future ambition problem. The shared focus overlay exists so one system can cover hundreds of possible releases while still letting important releases feel distinct.

The design uses three content scales.

| Scale | Who uses it | What it gives | What it must not do |
| --- | --- | --- | --- |
| Shared overlay | Every Event 6 origin country | Survival trunk, basic politics, economy, militia, recognition, host dispute, league and patron hooks | It must not read like one generic tree for every country. |
| Regional insert | Any release in a broad regional family | Regional politics, terrain, military style, local claims, regional economy, and cultural asset direction | It must not force unique country content for every tag. |
| Ambition insert | Selected stronger releases or high-chaos releases | Larger route, special leader path, league leadership, aggressive bloc, formable preparation, or rare identity branch | It must not become free conquest without host response, recognition cost, or integration work. |

The shared overlay should be implemented so a small release feels complete with the trunk and regional insert, while a major release gains a stronger ambition insert. A country that exists only briefly should still have a useful opening tree and decisions. A country that survives should see the overlay mature into diplomacy, army, economy, and formation content.

## Origin-aware focus loading

The focus layer must obey the Event 6 origin rule. A tag that appears through Independence Wave receives Event 6 content. The same tag that appears through Soviet Collapse, vanilla release, a different Chaos Redux event, or normal game setup does not automatically receive the Event 6 overlay.

| Country state | Focus handling |
| --- | --- |
| New Event 6 tag with no existing tree | Full shared overlay with regional insert and any eligible ambition insert. |
| Existing vanilla or Chaos Redux tag with no meaningful unique tree | Full shared overlay, but preserve existing country names and assets unless the Event 6 package changes them. |
| Existing tag with a meaningful unique tree | Additive Event 6 overlay through decisions, national spirits, focus subtree, or unlocked branch if the engine pattern supports it. Do not blindly replace the tree. |
| Same tag released by Soviet Collapse | Soviet Collapse content only. Event 6 mechanics stay locked unless Event 6 origin memory is set. |
| Existing independent country invited into league or sponsor system | Receives associate decisions and GUI access, but not the released-country survival tree unless it was actually released by Event 6. |
| Annexed Event 6 country restored later by normal peace | Re-enable Event 6 country package only if the origin memory is preserved and the restoration is connected to the same Event 6 lifecycle. |

The implementation should attach the overlay through origin memory, not only through tags. Working implementation concepts include an Event 6 origin flag, a former-host target, a release package tier variable, a region family variable, a focus insert selector, and a cleanup marker. Exact variable names belong to implementation.

## Shared overlay architecture map

The shared overlay should be a real tree shape, not a vertical chain. It should have an opening survival trunk, then several lanes that unlock in phases. The implementation agent owns exact node count and coordinates, but the final tree should preserve this architecture.

```text
Opening survival trunk
    -> Emergency government lane
    -> Local administration and economy lane
    -> Army and militia lane
    -> Recognition and patrons lane
    -> Host dispute and borders lane
    -> League or neutrality lane
    -> Regional insert lane
    -> Ambition insert lane when eligible
    -> Hidden high-chaos lane when eligible
```

### Opening survival trunk

The opening trunk is shared by all Event 6 origin countries. It represents the first months after instant release.

| Focus group | Narrative role | Mechanical role | Decision and GUI connection | Reward style |
| --- | --- | --- | --- | --- |
| Working label: provisional authority | Create the first recognized internal command | Raises legitimacy floor, lowers instability floor, unlocks basic statecraft actions | Opens provisional statecraft category and GUI country mode | Idea mitigation, small stability support, first leader confirmation, decision unlocks |
| Working label: secure the capital | Keep the new country from collapsing instantly | Adds capital defense, local control, emergency supply, and first militia route | Starts or strengthens hold capital mission | Forts, rail repair, supply support, militia or guards if justified |
| Working label: first registry | Build a state record after sudden independence | Improves local control and recognition readiness | Improves census and registry mission outcomes | Administration idea upgrade, manpower unlock, compliance or resistance handling |
| Working label: emergency budget | Turn seized offices and depots into a budget | Opens early economy actions | Improves local control construction decisions | Small factory or construction project, not flat political power |
| Working label: first foreign note | Make the new state visible abroad | Opens recognition path | Unlocks recognition delegation decisions | Recognition value, foreign support channel, diplomatic decision access |

The opening trunk should be short enough that minor tags can reach useful decisions quickly. It should not solve every problem. It should open choices.

### Political route family

The political family chooses how the new state claims authority. Not every small release needs every route. The shared overlay should show a curated subset based on region family, package tier, ideology, starting legitimacy, and chaos evolution.

| Route family | Eligibility | Main values moved | Tradeoff | Typical end state |
| --- | --- | --- | --- | --- |
| Civil republic | Most ordinary republics, city states, local councils, non-monarchic historical identities | Legitimacy, recognition, coalition trust | Slower military centralization and lower coercive options | Recognized republic, league-friendly member, settlement-capable state |
| Emergency executive | Low legitimacy, high border heat, war pressure, threatened capitals | Legitimacy, local control, former host anger | Faster action, higher instability and sponsor suspicion | Presidential emergency state or strong provisional government |
| Assembly of peoples | Multiethnic, indigenous, regional federation, or league-oriented releases | Coalition trust, local control, recognition | Harder to centralize army, more internal bargaining | Federation-ready state or league anchor |
| Military council | Severe instability, defecting army districts, border states, host threat | local control, army readiness, border heat | Recognition penalty and higher former host anger | Defensive junta, coercive compact candidate, or disciplined frontier state |
| Restoration authority | Monarchy, sultanate, emirate, old kingdom, dynastic claimant, temple or sacred identity | Legitimacy, recognition, patron influence | Asset burden, succession risk, higher ideological polarization | Restored kingdom, principality, emirate, or sacred state |
| Foreign-backed cabinet | Low local control but high sponsor access | foreign support, recognition, patron influence | Client-state risk and coalition trust penalty | Protected republic, sponsor-aligned state, or puppet-risk route |
| High-chaos mandate | High chaos evolution, strange claimant, antiquarian restoration, radical border compact | aggressive bloc pressure, border heat, instability | Severe diplomatic cost and runaway failure risk | Ambition state, coercive bloc member, or dangerous hidden route |

Political routes should update visible country package surfaces when relevant. A route can change ruling party direction, leader role, advisor roster, flag variant, cosmetic name, AI focus weights, decision availability, and idea lifecycle. Final names remain an implementation localisation task.

### Administration, economy, and local control lane

This lane stabilizes the territory the country actually controls. It should use region-aware rewards rather than generic factories everywhere.

| Focus group | State or terrain emphasis | Rewards and unlocks | Link to mechanics |
| --- | --- | --- | --- |
| Working label: district offices | Any package with several states | Local control missions, courts, police or guard decisions | Raises local control, lowers instability |
| Working label: rail and depot authority | Landlocked, border, Soviet-region, Central European, Chinese, African inland, Andean | Rail repair, supply hubs, train or truck costs, depot security missions | Raises local control, affects aid corridor missions |
| Working label: port and customs service | Island, port city, coastline, river delta, Swahili coast, Caribbean, Mediterranean | Dockyard, convoy, port garrison, customs revenue idea upgrade | Raises foreign support, recognition, and sponsor access |
| Working label: frontier roads | Mountain, desert, jungle, steppe, savanna, highlands | Infrastructure, logistics, terrain-specific guard units | Raises local control and army readiness, lowers failure risk |
| Working label: harvest and ration offices | Rural, food-producing, low industry, indigenous, steppe, Sahel | Stability, manpower access, militia sustainment, lower instability | Mitigates post-release instability |
| Working label: arsenals and workshops | Industrial, urban, old factory districts, rail hubs | Military factory, conversion, repair, equipment stockpile missions | Supports army lane and border defense |
| Working label: river or lake authority | Mesopotamia, Nile, Congo, Danube, Volga, Great Lakes, Amazon, Paraná, Mekong | Infrastructure, ports where valid, supply, regional commerce | Raises local control, improves formable preparation |

Small countries should receive rewards scaled to state count and industry. The tree should not give a one-state release the same industrial package as a partition-tier state. Strong countries should get more construction projects but also bigger administration missions.

### Army and militia lane

Every fighting Event 6 country needs a path to create and improve forces. The army lane should connect to decisions and missions instead of handing out repeated free divisions.

| Focus group | Uses | Unit direction | Costs or pressure |
| --- | --- | --- | --- |
| Working label: call local guards | Early survival | Militia, police, factory guards, district guards, mountain bands, port guards | Manpower, infantry equipment, local control, instability risk |
| Working label: officer cadre | Professionalization | Converts some militia templates toward regular infantry or mountaineers where region supports it | Army XP, command power, recognition or sponsor support |
| Working label: depot seizure or depot audit | Released states with rail hubs or former army stockpiles | Equipment stockpiles and guarded depot missions | Border heat or former host anger if aggressive |
| Working label: border defense plan | Host dispute or high border heat | Forts, anti-air, defensive missions, planning speed | Slower diplomacy, higher host suspicion |
| Working label: volunteer channel | Sponsor or league route | Volunteer units, advisors, training, better templates | Patron influence, sponsor rivalry, coalition trust cost |
| Working label: integrated command | Late consolidation | Removes militia fragmentation or upgrades army idea | Requires command obedience mission success |
| Working label: offensive staff | Ambition or aggressive bloc route | War preparation missions, claims, limited ultimatums | Raises border heat and aggressive bloc pressure |

The army lane should avoid a free unit loop. Spawning should be tied to focus one-time flags, mission success, decision costs, local control, sponsor aid, league reserves, or depot control. High-chaos releases can start with stronger or stranger troops, but they should also begin with more instability, higher host anger, or lower recognition.

### Recognition, patron, and diplomacy lane

This lane turns the country from a sudden map actor into a state other powers acknowledge. It should be useful to peaceful, league, sponsor, and ambitious routes.

| Focus group | Purpose | Decisions opened | Failure risk |
| --- | --- | --- | --- |
| Working label: delegations abroad | First recognition | recognition delegation, observer mission | Sponsor rivalry if several patrons compete |
| Working label: treaty language | Anti-puppet protection | anti-puppet clauses, guarantee talks | Patron influence if one sponsor dominates |
| Working label: neutral conference | Settlement and neutrality path | host settlement, conference bid | Slow progress, low army readiness |
| Working label: patron office | Foreign-backed route | arms convoy, adviser mission, reconstruction funding | Client-state pressure |
| Working label: balanced sponsors | Multi-sponsor strategy | expose rival patronage, buy out contracts | Rivalry and sabotage |
| Working label: public recognition tour | League or regional insert | league recognition tour, regional observer mission | Requires coalition trust |

Diplomacy focuses should affect recognition, foreign support, patron influence, sponsor rivalry, coalition trust, and former host negotiation willingness. They should not only grant relations modifiers.

### Host dispute and border lane

The host dispute lane is shared by released countries and mirrored by host response decisions from the decision and GUI system. It should let countries choose settlement, defense, arbitration, or escalation.

| Route | Unlocks | Mechanic impact | AI tendency |
| --- | --- | --- | --- |
| Settlement route | border commission, autonomy settlement, treaty enforcement | lowers border heat and former host anger, improves recognition | Preferred by weak republics and league-oriented AI |
| Defensive route | fortify disputed line, hold capital, loyal corridor counterplay | lowers conquest risk, can raise host anger | Preferred by small threatened releases |
| Plebiscite route | local control tests, claims tied to population or state control | raises legitimacy if successful, raises border heat if abused | Preferred by civic and federal routes |
| Limited demand route | limited border demand and ultimatum preparation | raises border heat and ambition | Preferred by military or aggressive AI only when ready |
| Host reconciliation route | return, confederation, protectorate, or mutual recognition options | lowers instability and patron influence, may reduce independence ambition | Rare player or AI option for doomed states |

The host must always retain at least one state. Focuses that prepare claims should not bypass the host survival rule. Any focus that creates a direct claim on a host capital should route through a settlement, formable, or war logic that checks host survival first.

### League, neutrality, and aggressive bloc lane

The shared overlay should allow three broad external strategies.

| Strategy | Who uses it | Focus role | Decisions and GUI |
| --- | --- | --- | --- |
| Neutral survival | Countries avoiding patrons and blocs | Recognition through restraint, host settlement, defensive army | recognition, settlement, local control, neutral conference |
| Independence League | Countries choosing released-country cooperation | League membership, common defense, arbitration, pooled reserves, common recognition | league charter, league missions, shared GUI mode |
| Coercive compact | High-chaos or militarized states rejecting compromise | Pressure, synchronized demands, shared ultimatums, punishment of defectors | aggressive bloc category and pressure missions |

The league route should not be automatic. It should require at least two or three eligible released countries, minimum coalition trust, and enough recognition or common threat. The coercive compact should require high chaos, aggressive route choice, high border heat, or a militarized leader path.

### Regional insert lane

The regional insert is the main tool that prevents the shared tree from feeling empty. It should be selected from the country package region family. One country can have multiple small regional traits, but only one main regional insert should drive the tree to avoid clutter.

Regional inserts should add focus groups, decision unlock variants, idea upgrades, unit variations, advisor archetypes, flag and portrait directions, and AI weights. They should not replace the survival trunk.

### Ambition insert lane

Ambition inserts are for selected strong countries, high-chaos releases, or countries with formation potential. They give a larger project such as league leadership, regional federation, old kingdom restoration, port league, frontier march, indigenous confederation, Mesopotamian river state, or aggressive compact leadership.

Ambition inserts should usually be hidden until the country survives the shock phase, reaches enough legitimacy, controls the required state groups, or selects a matching political route. Some high-chaos ambition inserts can appear earlier, but they must carry instability, recognition, or host anger costs.

## Shared idea lifecycle

Event 6 countries should use a small number of deep ideas, not a stack of shallow modifiers. The exact modifiers belong to implementation. The lifecycle below defines what each idea is for and how it changes.

| Idea working label | Start or unlock | Starting role | Mitigation path | Upgrade path | Failure path | Final forms |
| --- | --- | --- | --- | --- | --- | --- |
| improvised administration | Most Event 6 releases | Mixed or negative state capacity problem | Opening trunk, registry mission, district offices | Regional administration, federal registry, restored chancery, port customs office | bureaucracy collapse, local boss rule | Removed or transformed into a government institution idea |
| disputed independence | Most releases with host anger | Recognition and host problem | recognition delegation, settlement, league arbitration | treaty-backed independence, league-protected republic, restored recognized state | puppet pressure, reclamation crisis | recognized country, protected country, or client state |
| militia fragmentation | Releases with starting irregular forces | Army weakness and command obedience problem | officer cadre, command mission, army lane | integrated command, local guard system, professional army | rogue militia, warlord drift, compact radicalization | removed, upgraded, or converted to route army idea |
| broken logistics | Landlocked, mountain, rural, border, African inland, Andean, Soviet-region | Supply and rail weakness | rail and depot authority, aid corridor, frontier roads | rebuilt corridor, state railway, river supply authority | aid corridor failure, depot vulnerability | logistics institution or infrastructure program |
| foreign ledger | Sponsor-backed or low-recognition releases | Foreign help with dependency risk | balanced sponsors, anti-puppet clauses, neutral conference | balanced aid, treaty-backed aid, league aid office | patron capture, sponsor rivalry crisis | removed, balanced, or client-state route idea |
| border fever | Releases with claims or host dispute | Border heat and public pressure | arbitration, border commission, defensive route | recognized borders, negotiated frontier, guarded frontier | border incident cascade, coercive compact pressure | settled border, frontier state, or aggressive doctrine |
| league confidence | League members | Cooperation value | common recognition tour, pooled defense, arbitration | charter member, league command, common front | league suspicion, expulsion risk | league institution idea or removed after settlement |
| antiquarian mandate | High-chaos historical restorations | Strange legitimacy with poor recognition | research dossier, local symbols, survival proof | restored court, sacred mandate, historical mission | fanatic court, invented lineage scandal | ambition or hidden route identity |

The implementation should use idea upgrades and replacements rather than adding a new idea after every focus. A country can start with two to four ideas based on package tier. It should not start with the full table.

## Focus reward rules

Focus rewards should vary by branch and region.

| Branch | Good reward types | Rewards to avoid as the main payoff |
| --- | --- | --- |
| Opening trunk | unlock decisions, mitigate starting ideas, small capital defense, first militia, local control | flat political power as the main reward |
| Political routes | leader role, party direction, law changes, advisor unlocks, idea transformations, route decisions | repeated stability or popularity only |
| Economy lane | factories, infrastructure, railways, ports, dockyards, resources, construction decisions, consumer goods relief | country-wide small modifiers that ignore geography |
| Army lane | templates, training decisions, commander pool, depot missions, reserve decisions, fortification | repeated free divisions with no cost |
| Recognition lane | recognition value, sponsor access, guarantee route, anti-puppet clauses, diplomatic missions | flat opinion bonuses only |
| Host dispute lane | border commission, settlement missions, defensive works, claims tied to state control | unconditional cores or war goals |
| League lane | league authority, pooled defense, charter missions, arbitration | faction creation with no membership rules |
| Ambition lane | formable preparation, special advisors, high-risk claims, postwar integration | direct empire creation without state proof |

## Regional insert: European republics and old border claimants

This family covers European republics, old regions, border claimants, city states, historical crowns, and treaty-era arguments. It should appear often in early waves because many of these tags already exist or have obvious state anchors.

### Eligibility and tone direction

Eligible packages include existing releasables, old republics, border regions, disputed linguistic regions, restored duchies or kingdoms, free cities, and small national committees. The tone should be legalistic, anxious, organized, and border-conscious. It should not become a generic romantic nationalist tree for every country.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: municipal legitimacy | City halls, councils, parliament fragments, local ballots | legitimacy and recognition | provisional assembly, recognition delegation |
| Working label: treaty border files | Old maps, plebiscite claims, border commission work | border heat and host anger | border commission, plebiscite, arbitration |
| Working label: customs and railways | Central European and port economies | local control, foreign support | rail and depot, port customs, aid corridor |
| Working label: republican guard | Defensive militias, gendarmerie, local officers | army readiness and instability | raise guards, integrate militias |
| Working label: league of small states | Cooperation among threatened releases | coalition trust and league cohesion | founding charter, common front |

### Political inserts

European republics should usually get civil republic, emergency executive, military council, and league routes. Restoration route appears for old kingdoms, duchies, princely states, or monarchic claimants. High-chaos mandate appears for strange restorations such as old orders, revived free cities with exaggerated claims, or impossible treaty interpretations.

### Military and economy direction

Small European countries often have some industry, railways, and educated officer cadres. Their starting forces should lean toward gendarmerie, defecting infantry, urban guard, railway troops, and border guards. Mountain or alpine releases can use mountain detachments. Port releases can use naval guards and convoys.

### Asset direction

Historical flags, real coats of arms, and real leaders require sourced assets. Fictional high-chaos variants, invented emergency cabinets, and alternate route flags can use generated art. Existing vanilla flags should be reused when the tag is already registered and the flag is suitable.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Scotland | existing if safe | compact or regional | European republic, league | Usually early-pool if releasable. |
| Wales | existing if safe | seed or compact | European republic | Shared tree plus Celtic regional tone. |
| Brittany | existing if safe | seed or compact | European republic, old claimant | Stronger if France is weak. |
| Catalonia | existing if safe | compact or regional | European republic, port economy | Can become league-friendly or sponsor-backed. |
| Bavaria | existing if safe | compact or regional | old border claimant, restoration possible | Could use restoration or federal route. |
| Silesia | existing or new X if missing | seed or compact | border claimant, industrial | Border heat must be carefully controlled. |
| Danzig or Free City | existing or new X if missing | seed | port polity | Strong sponsor and host dispute hooks. |
| Trieste | new Event 6 tag if missing, X ending | seed or compact | port polity, border claimant | Must avoid deleting host capital. |
| Occitania | new Event 6 tag if missing, X ending | regional | European republic | Stronger high-chaos cultural claimant. |
| Etruria | new Event 6 tag if missing, X ending | regional or ambition | restoration or antiquarian | High-chaos or researched restoration path. |

## Regional insert: Soviet-region overlap with Event 6 origin separation

This family covers Soviet republics, Central Asian republics, Caucasus states, Baltic states, Volga and Ural identities, Cossack regions, Siberian identities, and other countries that can overlap with a separate Soviet Collapse system.

### Origin separation rule

If a Soviet-region tag appears through Event 6, it must receive Event 6 mechanics, Event 6 decisions, Event 6 focus overlay, and Event 6 origin flags. It must not receive Soviet Collapse route logic unless the separate Soviet Collapse system explicitly creates it. A shared tag must use origin-aware focus availability.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: commissariat remnants | Use old ministries, local soviets, party offices, or republic committees | legitimacy and instability | emergency government, local courts |
| Working label: army district inheritance | Defecting districts and depots | militia fragmentation, army readiness | depot audit, officer cadres |
| Working label: rail corridor republic | Rail hubs, steppe lines, supply routes | local control and foreign support | rail and depot network, aid corridor |
| Working label: border of republics | Administrative borders become state borders | border heat and host anger | border commission, settlement |
| Working label: non-collapse path | Confirms Event 6 identity | origin lock and content separation | GUI and decision filters |

### Political inserts

Soviet-region Event 6 countries can use civil republic, assembly of peoples, military council, foreign-backed cabinet, and high-chaos mandate. Socialist successor flavor can exist, but it should remain Event 6-specific and should not copy Soviet Collapse content. A restoration route appears for Volga Bulgaria, old khanates, Caucasian kingdoms, or Cossack hosts when researched and chaos conditions support it.

### Military and economy direction

These releases can plausibly start with defecting infantry, security units, border guards, rail troops, cavalry in steppe areas, mountain troops in the Caucasus, and small air assets if they inherit airfields. Starting equipment should scale with depots, rail hubs, local industry, host army weakness, and chaos tier.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Ukraine | existing if safe | regional or partition | Soviet-region Event 6 | Must not become Soviet Collapse Ukraine unless released by Event 5. |
| Belarus | existing if safe | compact or regional | Soviet-region Event 6 | Rail and border mission heavy. |
| Georgia | existing if safe | compact or regional | Caucasus mountain | Can get mountain defense insert. |
| Armenia | existing if safe | compact | Caucasus, recognition | High former-host and neighbor sensitivity. |
| Azerbaijan | existing if safe | compact or regional | Caucasus, resource | Oil and sponsor hooks if state control supports it. |
| Kazakhstan | existing if safe | regional or partition | steppe, rail corridor | Cavalry and rail route. |
| Turkestan | existing or new X if missing | regional or ambition | Central Asian federation | Formable preparation through the formable web. |
| Volga Bulgaria | new Event 6 tag if missing, X ending | regional or ambition | restoration, river | Event 6 route only when released by Independence Wave. |
| Idel-Ural | new Event 6 tag if missing, X ending | regional or ambition | federal, river, rail | Strong league or federation insert. |
| Don Host | new Event 6 tag if missing, X ending | compact or regional | Cossack, military council | Cavalry and border heat route. |
| Siberian Republic | existing or new X if missing | regional | rail corridor, frontier | Focus on railways, isolation, foreign support. |

## Regional insert: Middle Eastern and Mesopotamian identities

This family covers Assyria, Mesopotamia, Kurdish or regional mountain states if available, marsh and river identities, old mandates, emirates, sultanates, Levantine city or coast polities, and high-chaos ancient restorations.

### Research anchors

Mesopotamia should be framed around the Tigris and Euphrates river world, not only a generic Iraq release. Cambridge describes ancient Mesopotamia as the land of those rivers, mostly in modern Iraq and northeastern Syria, with areas of southeastern Turkey and western Iran, and as a region where early literate urban society arose. Assyria can draw from northern Mesopotamian historical memory, but real ancient symbols require source review and modern Assyrian identity should be handled carefully. The spec should treat those anchors as design references, not as claims that a 1936 state would simply revive antiquity.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: river administration | Irrigation, river towns, grain, bridges | local control and economy | river authority, rail and depot |
| Working label: mosaic assembly | Religious and ethnic plurality, local councils | legitimacy and coalition trust | provisional assembly, anti-puppet clauses |
| Working label: mandate files | Former mandate borders, consular memories, foreign guarantees | recognition and patron influence | recognition delegation, guarantee talks |
| Working label: mountain or desert defense | Kurds, Assyrians, desert emirates, tribal defense | army readiness and instability | local guards, officer cadres |
| Working label: antiquarian restoration | High-chaos ancient or local restoration | legitimacy, recognition penalty, border heat | formation dossier, ambition route |

### Political inserts

Civil republic, assembly of peoples, restoration authority, foreign-backed cabinet, and high-chaos mandate are all valid depending on identity. Military council is valid for border or war-pressure releases. Restoration authority should not always mean monarchy. It can represent a patriarchal council, emirate, sultanate, tribal confederation, restored city authority, or scholarly restoration circle when appropriate.

### Military and economy direction

Starting forces can include tribal levies, mountain guards, river police, urban militias, defecting army battalions, desert cavalry, and foreign-trained cadres. Economy should emphasize river infrastructure, oil only where state control supports it, ports for coastal states, and roads or supply hubs for inland routes.

### Asset direction

Modern communities, real religious symbols, historic flags, real leaders, and well-attested ancient symbols need sourced asset research. Fictional high-chaos antiquarian symbols can use generated art only when they are not presented as real historical symbols. Public names should be readable country names, not ministries or offices.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Assyria | new Event 6 tag if missing, X ending | compact or regional | Mesopotamian, mosaic, high-chaos ambition | Needs sensitive modern and historical source review. |
| Mesopotamia | new Event 6 tag if missing, X ending | regional or ambition | river state, federation | Can be formable or country based on state control. |
| Kurdistan | existing if safe or new X if missing | regional | mountain, recognition | Mountain defense and patron risk. |
| Marsh Arab Republic | new Event 6 tag if missing, X ending | seed or compact | river and marsh | Local control and river routes. |
| Lebanon or Levant coast identity | existing if safe | seed or compact | port, mosaic | Recognition and sponsor competition. |
| Hejaz | existing if safe | compact | restoration or religious polity | Sourced symbols and leader review. |
| Luristan | new Event 6 tag if missing, X ending | seed or compact | mountain, tribal | Defensive and host settlement routes. |
| Neo-Babylonian restoration | new Event 6 tag or cosmetic if used, X ending | ambition or high-chaos | antiquarian mandate | Hidden and costly, not a normal early release. |

## Regional insert: African historical and local polity releases

This family covers restored kingdoms, emirates, coastal city states, protectorate fragments, federations, local polities, indigenous or regional authorities, and high-chaos historical claimants across Africa.

### Research anchors

The design should use concrete anchors. UNESCO identifies Kilwa Kisiwani and Songo Mnara as Swahili trading cities whose prosperity rested on Indian Ocean trade with Arabia, India, and China, especially between the thirteenth and sixteenth centuries. The Met records courtly art exchange among Benin, Owo, and Ijebu kingdoms, which supports a Benin-region insert focused on court culture and regional diplomacy. World History Encyclopedia places Kongo on the western coast of central Africa in the region of modern DR Congo and Angola from the fourteenth to nineteenth century. These anchors support focus inserts about ports, courts, river states, trade, and restored authority without turning every African release into the same generic colonial revolt.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: restored court | Kingdoms, emirates, palace states, sacred courts | legitimacy and recognition | restoration authority, local courts |
| Working label: river and caravan offices | Congo, Nile, Niger, Senegal, Zambezi, caravan routes | local control, economy | frontier roads, river authority |
| Working label: coastal customs | Swahili, Gulf of Guinea, Red Sea, island ports | foreign support and economy | port customs, aid corridor |
| Working label: local chiefs council | Decentralized or multi-polity releases | coalition trust and instability | assembly of peoples, district offices |
| Working label: anti-client clause | Releases threatened by colonial or patron domination | patron influence and recognition | anti-puppet clauses, balanced sponsors |
| Working label: memory of old borders | Historical restoration or local polity | border heat and ambition | border commission, formation dossier |

### Political inserts

African releases should not all default to imported ideology labels. Civil republic, assembly of peoples, restoration authority, military council, and foreign-backed cabinet should be filtered by package identity. Restoration authority can represent a monarchy, court, emirate, oba authority, manikongo-style court direction, sultanate, or sacred kingship. Assembly of peoples can represent councils, local chiefs, towns, clan federations, or anti-client congresses.

### Military and economy direction

Starting forces vary strongly. Use local guards, rifle associations, defecting colonial troops, askari-style units when suitable, port guards, river patrols, cavalry in Sahel or savanna, mountain or forest detachments, and high-chaos royal guard or sacred guard variants. Reinforcement should come through local control, sponsor aid, league training, border defense, and depot seizure rather than repeated free spawns.

Economy should emphasize local resources, ports, roads, railways, river corridors, trade centers, and limited industry. Industrial rewards should be modest unless the released states actually include industrial centers.

### Asset direction

Historical flags, real court symbols, real leaders, real regalia, and historical emblems require sourced asset work. Fictional alternate route flags, invented league emblems, and high-chaos symbolic courts can use generated art. Avoid flattening culturally distinct polities into generic masks, spears, or animal emblems. Asset prompts should describe the specific court, river, port, or regional identity.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Kongo | new Event 6 tag if missing, X ending unless registered | regional or ambition | restored court, river | Strong formable and legitimacy insert. |
| Benin | new Event 6 tag if missing, X ending unless registered | compact or regional | restored court, regional diplomacy | Needs sourced symbol review. |
| Kilwa | new Event 6 tag if missing, X ending | seed or compact | Swahili port | Port customs and Indian Ocean trade direction. |
| Buganda | new Event 6 tag if missing, X ending unless registered | compact | restored court, lake region | Lake and court routes. |
| Sokoto | new Event 6 tag if missing, X ending unless registered | regional or ambition | emirate, Sahel | Cavalry, religious, and federation routes with source review. |
| Darfur | new Event 6 tag if missing, X ending | compact or regional | sultanate, caravan | Frontier and caravan economy. |
| Nubia | new Event 6 tag if missing, X ending | compact or regional | Nile, restoration | River defense and settlement. |
| Ashanti | existing if safe or new X if missing | regional | restored court, forest | Military and court identity. |
| Zanzibar | new Event 6 tag if missing, X ending unless registered | seed or compact | island port, sultanate | Port, sponsor, and customs focus. |
| Aksumite restoration | new Event 6 tag or cosmetic if missing, X ending | high-chaos ambition | antiquarian, sacred | Hidden or high-chaos, sourced symbol caution. |

## Regional insert: South American indigenous and historical groups

This family covers indigenous polities, old confederations, Andean restorations, frontier autonomies, river and highland states, and historical republics or provincial claimants.

### Research anchors

The Inca Empire should be treated as an Andean imperial and administrative memory rather than a generic South American empire. Britannica Education describes the Inca as a powerful Indian people of western South America whose empire stretched along the Pacific coast and the Andes before Spanish conquest in the 1530s. Mapuche-related releases should emphasize long resistance, decentralized leadership, land, frontier defense, and local authority. Encyclopedia.com notes Huilliche resistance in the War of Arauco, use of the Bio-Bio River as a boundary, and wartime leadership chosen for resistance purposes. These anchors support region-specific focus content around highland roads, local assemblies, frontier defense, and legitimacy through land control.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: land assembly | Indigenous or local land authority | legitimacy, coalition trust, local control | assembly of peoples, local courts |
| Working label: highland road state | Andes, plateau, mountain states | logistics, army readiness | frontier roads, mountain guards |
| Working label: river and forest corridors | Amazon, Paraná, Orinoco, forest or river polities | local control, aid corridor | river authority, district offices |
| Working label: frontier resistance | Mapuche and similar frontier identities | army readiness, border heat | defensive line, prevent border cascade |
| Working label: old imperial road | Inca or Andean restoration | legitimacy, ambition, local control | formation dossier, state integration |
| Working label: coastal customs | Pacific or Atlantic ports | foreign support and recognition | port customs, recognition delegation |

### Political inserts

Assembly of peoples should be common. Civil republic, emergency executive, military council, and restoration authority appear depending on identity. High-chaos mandate can appear for Andean imperial restoration, prophetic restoration, or exaggerated old boundary claims, but it should be expensive and instability-heavy.

### Military and economy direction

Starting forces should reflect terrain and local organization. Use mountain bands, local guards, cavalry or horse militia where appropriate, river patrols, forest detachments, and defecting border units. Reinforcement paths should use local control, highland roads, supply missions, sponsor arms, and league support. Industry should not be over-granted to rural or indigenous states. Roads, supply, agriculture, and manpower access matter more.

### Asset direction

Historical and indigenous symbols require sensitive source review. Avoid generic pan-indigenous imagery. Fictional high-chaos symbols can be generated only when clearly alternate and not presented as real sacred symbols. Generated leaders should use plausible regional name pools and correct gender metadata.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Mapuche | new Event 6 tag if missing, X ending | compact or regional | frontier resistance, land assembly | Strong defensive and anti-client route. |
| Aymara | new Event 6 tag if missing, X ending unless registered | seed or compact | highland, assembly | Highland roads and local control. |
| Quechua Republic | new Event 6 tag if missing, X ending | regional | highland, assembly | Can prepare Andean federation. |
| Inca restoration | new Event 6 tag or formable tag if missing, X ending | ambition or high-chaos | old imperial road | Hidden or formation-linked, not ordinary early release. |
| Guarani | new Event 6 tag if missing, X ending | compact | river and forest | River corridor and land assembly. |
| Charrua | new Event 6 tag if missing, X ending | seed | local polity, frontier | Smaller defensive package. |
| Patagonia | existing or new X if missing | regional | frontier, port | Can be republic or indigenous route depending package. |
| Riograndense Republic | existing or new X if missing | compact | historical republic | European-style republic insert with South American economy. |
| Amazonian Confederation | new Event 6 tag or cosmetic if missing, X ending | high-chaos ambition | river and forest | Should rely on local control and logistics, not free factories. |

## Regional insert: Asian regional polities

This family covers old kingdoms, regional republics, steppe identities, mountain states, port cities, minority regions, colonial border states, and high-chaos restorations across Asia outside the Soviet-region rule.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: mountain government | Himalaya, Caucasus-adjacent, Yunnan, Shan, uplands, Tibet-related | legitimacy, logistics, army readiness | mountain guards, frontier roads |
| Working label: steppe council | Mongolia-adjacent, Inner Asian, nomad or cavalry identities | army readiness, local control | cavalry guards, district offices |
| Working label: port concession state | treaty ports, colonial ports, island ports | recognition, patron influence | port customs, observer mission, anti-puppet clauses |
| Working label: old court or sultanate | historic kingdoms, sultanates, princely states | legitimacy and restoration authority | local courts, restoration route |
| Working label: frontier federation | multiethnic border regions | coalition trust and local control | assembly of peoples, border commission |
| Working label: industrial corridor | Manchurian, Chinese, Indian, Korean, Japanese-adjacent industrial regions | economy and army readiness | rail and depot, arsenals |

### Political inserts

Civil republic, restoration authority, assembly of peoples, foreign-backed cabinet, and military council should be available based on identity. High-chaos mandate can create ancient restoration or strange claimant routes, such as Hittite-style antiquarian claims in Anatolia, but such routes need source review and should not replace normal regional identities.

### Military and economy direction

Asian regional packages can draw from mountain detachments, cavalry, port guards, railway troops, defecting army districts, factory guards, and foreign-trained cadres. Strong industrial regions should get arsenals and factory routes. Mountain and rural regions should get logistics, manpower, and defense routes instead.

### Asset direction

Real flags, real monarchs, real princely symbols, religious symbols, and real leaders require sourced assets. Fictional route variants can use generated art. For generated one-person leaders, use region-appropriate name pools and gender alignment.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Tibet | existing if safe | compact or regional | mountain, restoration | Event 6 origin if released by wave, not other systems. |
| Shan | new Event 6 tag if missing, X ending unless registered | seed or compact | mountain, border federation | Local militia and sponsor routes. |
| Uyghurstan or East Turkestan | existing if safe or new X if missing | regional | frontier, assembly, patron risk | Sensitive naming handled by implementation direction. |
| Bengal | existing if safe | regional or partition | river, industrial corridor | Strong economy and recognition route. |
| Punjab | existing if safe | regional | frontier, agriculture, army | Military and river route. |
| Dravidian Republic | new Event 6 tag if missing, X ending | regional or ambition | federal, coastal | Requires careful state selection. |
| Manchuria | existing if safe | regional or partition | industrial corridor, sponsor risk | Patron pressure should be prominent. |
| Korea regional split | existing or new X if missing | compact or regional | industrial, nationalism | Must preserve existing country content if meaningful. |
| Hittite restoration | new Event 6 tag or cosmetic if missing, X ending | high-chaos ambition | antiquarian, Anatolian | Hidden route with sourced symbol caution. |
| Goryeo restoration | new Event 6 tag or cosmetic if missing, X ending | high-chaos ambition | old court | Could be cosmetic or formable, not a routine release. |

## Regional insert: island and port polities

This family covers islands, city ports, treaty ports, canal zones, naval bases, free cities, coastal sultanates, and trade polities. Some are geographically tiny but strategically important.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: customs house state | Port revenue and recognition | foreign support, recognition | port customs, observer mission |
| Working label: harbor guard | Defense and naval security | army readiness, local control | port guard, defensive line |
| Working label: convoy lifeline | Aid and supply | foreign support, patron influence | arms convoy, aid corridor |
| Working label: free port charter | Neutral or league role | coalition trust, recognition | league arbitration, neutral conference |
| Working label: smuggler crisis | High instability or patron rivalry | instability, sponsor rivalry | expose patronage, secure port |
| Working label: maritime league | Ambition insert for several port states | league cohesion and authority | common recognition tour, pooled defense |

### Political inserts

Port polities commonly use civil republic, emergency executive, foreign-backed cabinet, and league routes. Restoration authority is valid for sultanates, islands with monarchic histories, or orders. High-chaos mandate can create maritime orders, pirate republics, or impossible charter states, but these should carry sponsor rivalry and host anger.

### Military and economy direction

Starting forces are small but can have port guards, marines or naval militia when appropriate, convoy assets, coastal forts, anti-air, and a small navy if the state includes a naval base or inherited ships. Reinforcement should use convoys, foreign support, league defense, dockyard projects, and port security missions.

### Asset direction

Historical port flags, coats of arms, orders, and real naval emblems need sourced assets. Fictional free-port and high-chaos maritime emblems can use generated art. Do not use generic anchor icons for every port state.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Malta | existing if safe or new X if missing | seed or compact | island, port, order route | Existing flags if registered. |
| Cyprus | existing if safe | compact | island, mosaic, port | Sponsor rivalry and guarantees. |
| Zanzibar | new X if missing | seed or compact | island port, sultanate | African and port family overlap. |
| Singapore | existing if safe or new X if missing | seed or compact | port concession, industrial | High sponsor interest. |
| Hong Kong | new Event 6 tag if missing, X ending | seed | port concession | Strong anti-puppet and patron risk. |
| Tangier | new Event 6 tag if missing, X ending | seed | international port | Recognition and sponsor rivalry. |
| Danzig | existing or new X if missing | seed | free city, border | European and port overlap. |
| Trieste | new X if missing | seed or compact | free port, border | Host survival and border heat critical. |
| Aden | existing or new X if missing | seed | port and strait | Convoy and sponsor routes. |
| Maritime League | formable or faction identity, X ending if tag or cosmetic | ambition | port coalition | Should usually be a league or cosmetic route, not a normal release. |

## Regional insert: high-chaos niche and strange claimants

This family covers unusual historical restorations, local polities, religious or scholarly claimants, old dynastic files, city charters, antiquarian states, exile-led projects, and stranger high-chaos governments. They should appear at higher chaos tiers and not dominate early waves.

### Design boundaries

High-chaos does not mean random nonsense. A strange claimant should have a region, a public country name, a reason the map accepts it, a government role, a starting problem, and an asset direction. It can be absurd or ominous, but it still needs country package logic.

### Focus insert groups

| Focus group | Purpose | Mechanics | Decisions |
| --- | --- | --- | --- |
| Working label: archive miracle | A dossier, charter, relic, court record, or mythic legal claim becomes politically real | legitimacy and recognition split | formation dossier, recognition delegation |
| Working label: impossible cabinet | A strange government structure tries to rule | instability and legitimacy | emergency decree, local courts |
| Working label: cult of borders | Boundary obsession and old maps | border heat and aggressive pressure | synchronized claim drive, border demand |
| Working label: patron of curiosities | Foreign powers exploit or study the strange state | foreign support and patron influence | observer mission, adviser mission |
| Working label: old banners raised | Public identity and military recruitment | army readiness and instability | raise guards, integrated command |
| Working label: refusal of ordinary statehood | Hidden route | high-chaos mandate, recognition penalty | coercive compact or unique ambition decisions |

### Political inserts

High-chaos packages can use restoration authority, military council, foreign-backed cabinet, emergency executive, or high-chaos mandate. Civil republic remains possible for strange states trying to become normal. Assembly of peoples is possible for federated revivals or confederations.

### Military and economy direction

Their troops can be better or stranger than normal, but not free. They should pay with instability, low recognition, high host anger, patron dependence, or poor logistics. Unit themes can include ceremonial guards turned field troops, antiquarian militias, exile cadres, foreign adventurers, local zealots, archive-office guards, or defectors attracted by the new banner.

### Asset direction

Real ancient symbols, religious symbols, and historical flags require source review. Fictional strange states can use generated portraits, flags, and emblems. The asset prompt must state that generated art is alternate or fictional when that is true.

### Example packages

| Public country or identity | Candidate tag handling | Package scale | Insert type | Notes |
| --- | --- | --- | --- | --- |
| Neo-Babylonia | new X if used | high-chaos ambition | antiquarian, river | Hidden, Mesopotamian, high recognition penalty. |
| Hittite Anatolia | new X if used | high-chaos ambition | antiquarian, Anatolian | Needs source caution for symbols. |
| Etruria | new X if used | high-chaos ambition | antiquarian, European | Could be cosmetic route rather than tag. |
| Aksumite restoration | new X if used | high-chaos ambition | sacred, African | Requires sourced symbol caution. |
| Carthage | new X if used | high-chaos ambition | port, antiquarian | Likely formable or ambition route, not normal release. |
| Teutonic or knightly state | existing or new X if used | high-chaos ambition | order, border | Real symbols sourced, generated variants for alternate route. |
| Maritime Order | new X if used | high-chaos port | island, order | High sponsor and league tension. |
| Archive Republic | new X if used | special local claimant | legal absurdity | Public name should be a country or region, not office name. |

## Ambition inserts for selected stronger releases

Only selected countries should receive ambition inserts. The rule is not that every tag gets unique content. The rule is that every tag gets shared and regional content, while stronger or rarer releases get a larger ambition route.

### Ambition eligibility

A country can receive an ambition insert if one or more of the following is true.

| Eligibility | Meaning |
| --- | --- |
| Controls a meaningful regional core group | The country has enough territory to plausibly lead a larger project. |
| Has an old kingdom, empire, federation, or confederation identity | The release has a researched larger horizon. |
| Has high legitimacy and recognition | It can claim leadership without looking like a doomed militia. |
| Has high local control and army readiness | It can act beyond survival. |
| Is a port or city network anchor | It can lead a maritime or trade league. |
| Is a high-chaos claimant | It can unlock stranger ambitions with higher cost. |
| Is elected or accepted by other Event 6 releases | It can lead a league without conquest. |
| Has an aggressive political route | It can form or join a coercive compact. |

### Ambition insert families

| Ambition family | Region examples | Unlock pattern | Payoff | Failure risk |
| --- | --- | --- | --- | --- |
| League founder | Any region with several Event 6 releases | coalition trust, recognition, at least two candidates | lead Independence League, arbitration, pooled reserves | leadership dispute, expulsion, league collapse |
| Regional federation | Europe, South America, Central Asia, Africa, India, Southeast Asia | assembly route, state integration, local control | federation or confederation decision route | internal faction failure |
| Restored kingdom or court | Africa, Middle East, Asia, Europe | restoration route, legitimacy, sourced asset readiness | restored monarchy or court identity | succession crisis, recognition penalty |
| River civilization | Mesopotamia, Nile, Congo, Danube, Volga, Amazon, Mekong | river states, infrastructure, local control | river authority, formable preparation | supply collapse or rival river claims |
| Maritime league | islands, ports, straits, Swahili coast, Mediterranean, Caribbean, treaty ports | port control, convoys, recognition | port faction or trade league | sponsor rivalry and blockade risk |
| Frontier march | Caucasus, Andes, Central Asia, Sahel, Patagonia, Siberia | military council, border heat, local control | defensive frontier or expansion route | host war and border incident cascade |
| Antiquarian restoration | high-chaos historical claims | chaos evolution, dossier, legitimacy route | hidden restoration or formable | low recognition, high instability |
| Coercive compact leader | aggressive high-chaos releases | military route, high border heat, aggressive pressure | synchronized claims and ultimatums | global backlash and member defections |

### Strong-country insert structure

A strong-country insert should add a late early-game route and a mid-game route. It should not wait until the country is already a major power.

1. A reveal focus or focus group that shows the ambition after survival is plausible.
2. A preparation group that moves local control, legitimacy, recognition, or army readiness.
3. A choice between negotiated, league, patron, or coercive pursuit where relevant.
4. A decision family that proves control over required states or members.
5. A payoff that changes country identity, unlocks formable preparation, leads a league, or opens a postwar integration route.
6. A failure route if the country loses legitimacy, becomes a client, fails formation security, loses its capital, or loses league confidence.

## Ordinary small releases without empty gameplay

Most releases will not have a bespoke ambition insert. They still need to feel playable.

### Required small-release content

Every Event 6 origin country should receive the following minimum content.

| Surface | Minimum content |
| --- | --- |
| Focus tree | Opening survival trunk, two to three shared lanes, one regional insert, route-aware AI weights. |
| Ideas | Two to three starting ideas with clear mitigation paths. |
| Decisions | Provisional statecraft, local control, recognition, and host dispute decisions appropriate to phase. |
| Missions | At least one survival mission and one local control or recognition mission. |
| Leader | Provisional leader, council, monarch, committee, or military command with correct portrait direction. |
| Parties | Region and route direction for ruling party and opposition party labels, not final names. |
| Forces | Dynamic starting units and reinforcement route if expected to fight. |
| Assets | Flag direction, leader portrait direction, idea and focus icon direction. |
| AI | Survival route, recognition route, and local defense behavior. |

### How ordinary releases differ from each other

Ordinary releases should differ through region insert, starting state profile, starting values, leader role, party direction, unit families, decision target lists, host relationship, sponsor access, and one or two local focuses. They do not need a full unique tree.

| Difference source | Example result |
| --- | --- |
| Port versus inland | Port gets customs, convoy, port guards, sponsor access. Inland gets roads, rail, and supply. |
| Mountain versus plains | Mountain gets mountain guards and defensive logistics. Plains get cavalry, rail, or regular infantry. |
| High legitimacy versus low legitimacy | High legitimacy can seek recognition early. Low legitimacy must build registry and local control first. |
| Former host anger | High anger opens defensive and settlement content earlier. Low anger permits negotiation. |
| Sponsor access | Nearby major powers open patron route. Isolated countries rely on league or local consolidation. |
| Regional family | Local focus descriptions, icons, advisors, and unit families change. |
| Package tier | Larger packages get more lanes and later ambitions. Small packages get tighter survival content. |

## Focus integration with mechanics

Every major focus group should move at least one mechanic value.

| Focus group | Legitimacy | Recognition | Foreign support | Patron influence | Coalition trust | Border heat | Instability | Local control | Host anger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provisional authority | up | small up | no direct | no direct | no direct | no direct | down | small up | no direct |
| secure the capital | up if successful | no direct | no direct | no direct | no direct | can rise if militarized | down | up | can rise |
| first registry | up | up if transparent | no direct | no direct | up for assembly | no direct | down | up | down if settlement route |
| emergency executive | up short term | down if harsh | no direct | no direct | down | up | mixed | up | up |
| civil republic | up | up | no direct | down | up | down | down | up | down |
| military council | mixed | down | no direct | no direct | down | up | down short term | up | up |
| restoration authority | up if accepted | mixed | no direct | no direct | mixed | up if claimant | mixed | up | up |
| foreign-backed cabinet | mixed | up | up | up | down | no direct | down if aid works | up | up |
| league route | up | up | no direct | down | up | down | down | up | down |
| coercive compact | up for radicals | down | mixed | mixed | down | up | up | mixed | up |
| regional administration | up | no direct | no direct | no direct | up | down | down | up | down |
| ambition reveal | up | mixed | no direct | can rise | mixed | up | mixed | up | up |

The implementation should not hide these effects. Focus tooltips and GUI summaries should communicate visible value movement without exposing hidden future routes.

## Focus integration with decisions and missions

Focuses should unlock or modify decision categories from the decision and GUI system.

| Focus lane | Decision category effect |
| --- | --- |
| Opening survival trunk | Opens provisional statecraft and first survival missions. |
| Administration lane | Expands local control targets, district offices, courts, rail, and port decisions. |
| Army lane | Opens guard, militia integration, officer cadre, defensive line, and command obedience missions. |
| Recognition lane | Opens recognition delegations, observer missions, anti-puppet clauses, sponsor balancing. |
| Host dispute lane | Opens border commission, plebiscite, fortify line, limited demand, settlement. |
| League lane | Opens charter, arbitration, pooled defense, common recognition, common front. |
| Coercive lane | Opens compact founding, synchronized claims, ultimatum, defector punishment, backlash missions. |
| Ambition lane | Opens formable preparation, integrate claimant, neutralize rival, formation security. |
| Regional insert | Changes target lists, costs, units, and success effects by region. |
| High-chaos lane | Opens rare actions with stronger costs and failure states. |

Decision categories should evolve with the tree. Early decisions should be replaced or hidden when later stronger versions exist. Obsolete decisions should be cleaned after settlement, formation, annexation, reabsorption, or route lock.

## Focus and scripted GUI presentation

The scripted GUI from the decision and GUI system should reflect focus progress.

| GUI element | Focus connection |
| --- | --- |
| Country status card | Shows stabilization phase, starting ideas, route selection, and values. |
| Recognition card | Updates after recognition lane and diplomacy focuses. |
| Host dispute card | Updates after border lane and settlement focuses. |
| League card | Appears after league route or membership. |
| Aggressive bloc card | Appears only after coercive route. |
| Regional identity card | Shows regional insert summary and active local missions. |
| Ambition card | Hidden until ambition reveal conditions are met. |

The GUI should make the overlay feel alive, but it should not replace decisions. Buttons on the GUI must use the same costs, cooldowns, and AI equivalents as decisions.

## AI focus behavior

Event 6 AI must choose routes based on survival prospects, region, package tier, host danger, sponsor access, league potential, and chaos.

### AI archetypes

| AI archetype | Preferred routes | Avoids | Trigger conditions |
| --- | --- | --- | --- |
| survival republic | opening, civil republic, recognition, settlement | high-chaos mandate, coercive compact | low army readiness, medium legitimacy, high host anger |
| league builder | assembly, recognition, league, arbitration | foreign-backed cabinet if patron risk high | several Event 6 countries nearby, coalition trust high |
| sponsor client | foreign-backed cabinet, patron office, army aid | balanced sponsors if weak | low recognition, high sponsor access, low industry |
| armed frontier | military council, border defense, frontier roads | neutral conference if host aggressive | high border heat, strong terrain, host anger high |
| restoration court | restoration authority, court route, recognition | civil republic routes | old kingdom or monarchic identity with legitimacy support |
| port survivor | customs, convoy lifeline, foreign support, league or sponsor | inland rail route | port state, island state, sponsor access |
| regional ambition | ambition insert, formable preparation, local control | early war if weak | regional package with high legitimacy and control |
| coercive actor | military council, aggressive bloc, border demand | settlement and league arbitration | high chaos, high border heat, high army readiness |
| antiquarian claimant | high-chaos lane, restoration, dossier | ordinary civil republic unless normalizing | special high-chaos package |

### AI safety checks

AI should not select routes when requirements are invalid.

| Route | AI must avoid if |
| --- | --- |
| League founder | fewer than two eligible members, coalition trust too low, all nearby releases hostile or dead. |
| Coercive compact | army readiness too low, border heat target invalid, host vastly stronger, chaos too low. |
| Foreign-backed cabinet | no valid sponsor, sponsor is enemy without covert route, patron influence already dangerous. |
| Restoration authority | no suitable identity, no leader or portrait direction, recognition too low and legitimacy poor. |
| Formable preparation | required state group impossible, all rivals dead without cleanup, country too weak to survive. |
| Host settlement | former host dead without successor record, host has no linked Event 6 dispute, host would be deleted. |
| Aggressive expansion | target lacks border or claim, global backlash too high, league membership forbids it. |
| High-chaos branch | chaos evolution disabled or not active, package not marked eligible. |

### AI priority by package tier

| Package tier | AI priority |
| --- | --- |
| Seed | survive, gain recognition, avoid war, join league if helpful. |
| Compact | stabilize, build army, settle border or get sponsor. |
| Regional | choose route identity, build economy, manage host, consider league or ambition. |
| Partition | prevent host war, balance sponsors, build army, pursue settlement or strong ambition. |
| Ambition | secure prerequisites before revealing ambition. |
| Special high-chaos | pursue strange route only if survival and route conditions support it. |

## Regional focus icon and visual direction

The focus and package design does not create final assets, but it defines icon families for asset package work.

| Icon family | Usage | Visual direction |
| --- | --- | --- |
| Provisional authority | opening trunk, idea | improvised state symbol, seal, chamber, or local standard without readable text. |
| Local control | district offices, courts, registry | keys, ledgers, town hall, railway office, or local map table with no readable labels. |
| Recognition | diplomacy lane | diplomatic seal, treaty folder, delegates, neutral hall, no final text. |
| Host dispute | border lane | guarded frontier, boundary posts, maps as secondary props only. |
| League | league lane | shared banners, linked hands, council table, common defense emblem. |
| Coercive compact | aggressive lane | hard-edged pact emblem, synchronized banners, warning tone without real extremist symbols. |
| Regional insert | each family | specific terrain, court, port, river, mountain, or local institution. |
| Ambition | selected strong countries | larger symbol tied to formable or league route. |
| High-chaos | hidden routes | archive, ancient seal, strange light, court, banner, or impossible dossier. |

Focus icons, idea icons, decision icons, and achievement icons must be created as separate asset work items. A focus icon must not be resized into a decision icon or idea icon.

## Player-facing text direction for focus and country layer

Final localisation should be written from this direction.

| Surface | Direction |
| --- | --- |
| Shared survival focuses | Sudden government work, practical fear, local offices, guards, railways, capitals, and public uncertainty. |
| Political route focuses | Specific institutional identity and public authority, not generic ideology slogans. |
| Recognition focuses | Delegations, treaty language, observers, public acknowledgment, foreign leverage. |
| Host dispute focuses | Border commissions, local claims, defensive preparations, settlement pressure. |
| League focuses | Mutual survival, arbitration, common defense, shared recognition. |
| Coercive focuses | Hard pressure, impatient claims, contempt for settlement, risk of backlash. |
| Regional inserts | Use region-specific institutions, terrain, economy, and memories. |
| High-chaos focuses | Strange legal certainty, old symbols, irrational resolve, and public unease without spoiling hidden mechanics. |
| Country names | Readable map names. Avoid offices, boards, or internal committees as public names. |
| Leader names | Personal names for one-person leaders, institutional names for councils and bodies. |

Do not paste working labels into localisation. Do not expose hidden formable or high-chaos routes too early.

## Documentation outputs from this layer

Implementation should eventually maintain these docs or tables.

| Document or table | Purpose |
| --- | --- |
| Country package registry | All Event 6 possible release packages with tags, region, tier, states, focus modules, assets, and AI. |
| Focus route coverage table | Required shared lanes, regional inserts, ambition inserts, and actual implementation status. |
| Starting force matrix | Unit families, templates, equipment source, scaling, reinforcement routes by package tier. |
| Leader and portrait ledger | Real versus fictional leaders, portrait source mode, gender/name pool requirements. |
| Flag and symbol ledger | Existing, sourced historical, or generated fictional flags and emblems. |
| AI route matrix | AI route selection by package tier, region, values, chaos, and invalid route checks. |
| Origin separation audit | Tags that overlap Soviet Collapse or other events and how Event 6 origin checks protect them. |

## Acceptance criteria for focus tree architecture

The focus tree design is complete when the implementation agent can build a shared Independence Wave overlay that gives every Event 6 country survival, politics, army, economy, recognition, host dispute, league, aggressive, regional, and ambition routes without writing a unique tree for every possible tag. The implementation must preserve route-aware AI, visible mechanic hooks, focus-to-decision integration, idea lifecycles, regional inserts, and selected strong-country ambition inserts.

## Country package architecture

## Country package design promise

Every country created by Event 6 should enter the map as a playable or AI-usable actor with origin memory, a leader setup, politics, starting forces, economy, ideas, focus loading, decisions, and cleanup. Ordinary small releases use the shared overlay and regional inserts. Selected strong releases receive ambition inserts, formable access, and stronger asset demands.

## Country package tier architecture

Country packages define how much content a release receives at spawn. Tiers should be assigned per release package, not only per tag.

### Seed package

Seed packages are one-state or small releases with limited industry.

| Surface | Requirement |
| --- | --- |
| Focus overlay | Opening trunk, one political choice, economy or army lane, regional mini insert. |
| Ideas | improvised administration plus one of disputed independence, broken logistics, or militia fragmentation. |
| Politics | Provisional council, mayoral authority, local assembly, guard command, or small restoration figure. |
| Forces | One to three small units depending population, local control, state infrastructure, and chaos. |
| Economy | Minimal factories, maybe port or rail support if state has it. |
| Decisions | Emergency government, first registry, raise guards, recognition delegation, host settlement if linked. |
| AI | Seek survival, avoid aggressive route unless high chaos and strong terrain. |
| Ambition | Usually none, but can prepare league membership. |

### Compact package

Compact packages are small but viable releases with several states, a port, a rail hub, or a strong identity.

| Surface | Requirement |
| --- | --- |
| Focus overlay | Opening trunk, political route, economy lane, army lane, recognition lane, regional insert. |
| Ideas | two to three starting ideas with route upgrades. |
| Politics | More defined leader and advisor set. |
| Forces | Three to six units with dynamic template mix. |
| Economy | One or two focused construction paths, not generic industrial boom. |
| Decisions | Full released-country category set from the decision and GUI system, with target caps. |
| AI | Can defend, negotiate, or join league. |
| Ambition | Usually local ambition or minor formation preparation if state control allows. |

### Regional package

Regional packages are multi-state releases that can survive, bargain, and shape nearby politics.

| Surface | Requirement |
| --- | --- |
| Focus overlay | Full shared tree plus regional insert and possible ambition insert. |
| Ideas | three to four starting ideas, with at least two meaningful lifecycle paths. |
| Politics | Full route family subset, advisor roster, possible leader changes. |
| Forces | Six to twelve units based on states, population, depots, host weakness, and chaos. |
| Economy | Industry, logistics, and resource paths tied to actual states. |
| Decisions | Full categories, league or sponsor options, host dispute, formable preparation if eligible. |
| AI | Route archetype chosen from starting conditions. |
| Ambition | Common, especially league founder, federation, restored court, or frontier march. |

### Partition package

Partition packages are large releases from high chaos or major host rupture.

| Surface | Requirement |
| --- | --- |
| Focus overlay | Full shared tree, regional insert, ambition insert, and stronger host dispute branch. |
| Ideas | major starting crisis and meaningful mitigation. |
| Politics | Multiple competing routes and leader outcomes. |
| Forces | Ten or more units if the state count and depots justify it, with regular defectors possible. |
| Economy | Several state-grounded projects and supply route problems. |
| Decisions | Host and sponsor systems become central, not optional. |
| AI | Can seek settlement, league leadership, or regional war depending route. |
| Ambition | Expected, but gated by legitimacy, local control, recognition, and state proof. |

### Ambition package

Ambition packages are selected countries with a larger project. They can be compact, regional, or partition in territory, but they receive special route content.

| Surface | Requirement |
| --- | --- |
| Focus overlay | Ambition insert connected to survival and regional content. |
| Ideas | route identity idea or transformation. |
| Politics | Leader, party, cosmetic name, flag, and advisor direction may change. |
| Forces | Special unit route or doctrine route, with costs and risks. |
| Economy | Project-specific infrastructure or industry. |
| Decisions | Formation, league, aggressive bloc, or restoration decisions. |
| AI | Rare or conditional route selection with safety checks. |
| Failure | If ambition fails, country loses legitimacy, recognition, coalition trust, or becomes isolated. |

### Special high-chaos package

Special high-chaos packages are strange, rare, or extreme. They are not filler. Use only when the wave has reached high chaos and the release has a specific region and identity.

| Surface | Requirement |
| --- | --- |
| Focus overlay | High-chaos lane and regional anchor. |
| Ideas | antiquarian mandate, border fever, foreign ledger, or unstable authority. |
| Politics | Strange council, restoration court, military order, exile state, or radical republic. |
| Forces | Distinct but costly units. |
| Economy | Often weak or distorted, unless tied to a real city or industrial state. |
| Decisions | Aggressive pressure, observation missions, containment, patron exploitation. |
| AI | Low probability unless chaos and conditions support it. |
| Failure | Runaway instability, host war, sponsor capture, or league refusal. |

## Reuse of existing tags and new X-ending tags

The package matrix should never create a new tag when a safe existing vanilla or Chaos Redux tag already exists and is not exclusively owned by another event. It should also never reuse a tag in a way that breaks origin separation.

| Tag decision | Use when | Requirements |
| --- | --- | --- |
| Reuse existing vanilla tag | The tag exists, has suitable name and flag, and can load Event 6 origin content safely | Origin checks, no content overwrite, focus compatibility review. |
| Reuse existing Chaos Redux tag | The tag already exists and is not exclusively tied to another event route | Event ownership audit, origin-aware decisions, docs note. |
| Create new Event 6 country tag | The identity is new, local, historical, or high-chaos and no safe tag exists | Tag ends with X, full package, flag direction, leader direction. |
| Create new Event 6 cosmetic tag | A route changes public identity without needing a separate country | Cosmetic tag ends with X, flag and name direction. |
| Create new Event 6 formable tag | A larger country needs tag-level mechanics beyond cosmetic identity | Tag ends with X, formation requirements, integration and cleanup. |
| Use no new tag | A country can be a route, league status, cosmetic identity, or decision outcome | Use when creating a tag would bloat the pool. |

New tags must not be internal office names. A release can have a provisional committee, emergency cabinet, border board, or district council as leader role, but the public map name should be a country or place identity.

## Country package registry fields

Every release pool entry should use a registry record. The implementation can store this in a script-friendly form, but the design record should include these fields.

| Field | Purpose |
| --- | --- |
| public country identity | Readable name direction for the map. |
| candidate tag | Existing tag or new X-ending tag if needed. |
| release origin | Must mark Event 6. |
| region family | Selects regional insert and unit style. |
| package tier | Seed, compact, regional, partition, ambition, or special high-chaos. |
| host state group | Eligible states and host survival constraints. |
| capital preference | Best capital state, fallback capital, and capital avoidance if host needs it. |
| starting values | Legitimacy, recognition, foreign support, patron influence, instability, local control, host anger. |
| starting ideas | Two to four ideas from lifecycle table. |
| focus overlay modules | Shared lanes, regional insert, ambition insert if any. |
| decision categories | Which the decisions and GUI layer categories unlock at spawn. |
| initial missions | Survival and local control missions. |
| politics | Starting ideology direction, party direction, leader role, elections if relevant. |
| leaders and portraits | Real, fictional, council, monarch, military, or symbolic direction with source mode. |
| advisors | Political, economic, military, diplomacy, league, sponsor, and high-chaos slots. |
| starting forces | Unit families, template concepts, strength bands, equipment source. |
| reinforcement path | Decisions, missions, focuses, sponsors, league, depots. |
| economy | Factories, resources, rail, ports, supply, dockyards, infrastructure direction. |
| asset needs | Flags, portraits, focus icons, idea icons, decision icons, possible GUI or achievement icons. |
| AI plan | Route weights, survival behavior, aggression limits, sponsor behavior. |
| formable hooks | Later formation eligibility and state groups if relevant. |
| cleanup | What happens if annexed, reabsorbed, puppeted, or formed into another country. |

This registry is how the event accounts for many countries without unique bespoke design for each one. Ordinary countries get the shared overlay plus registry-driven regional identity. Important countries get extra fields for ambition inserts.

## Starting political setup

The political setup should make the country playable immediately while leaving route choices open.

### Starting ideology direction

| Release type | Starting ideology direction | Notes |
| --- | --- | --- |
| Civic republic or old parliament | democratic or non-aligned direction based on region and host | Should favor recognition and league routes. |
| Military breakaway | non-aligned or authoritarian direction | Must carry recognition cost and instability risk. |
| Restored kingdom or sultanate | non-aligned or monarchic direction if supported by mod ideology set | Needs sourced leader or generated fictional portrait if invented. |
| Socialist local council | socialist direction where region and host support it | Must remain Event 6 content, not Soviet Collapse. |
| Foreign-backed cabinet | ideology influenced by sponsor | Patron influence starts higher. |
| Indigenous assembly | democratic, non-aligned, or custom direction based on route | Avoid generic imported labels. |
| High-chaos claimant | route-specific direction | May begin non-aligned, extremist, or special ideology if mod supports it. |

### Party direction

Party names should be region-aware and route-aware, but the spec should not provide final strings. Use directions such as civic assembly party, emergency executive party, restoration court party, military council party, local federation party, sponsor-aligned party, league party, and high-chaos claimant party. Final localisation should use researched local terms only when sources support them.

### Elections and laws

Small provisional republics can have delayed elections, emergency elections, or no elections until a focus stabilizes them. Restoration and military routes can suspend elections at legitimacy cost. Assembly routes can unlock elections through local registry or congress focuses. Foreign-backed cabinets can hold elections but risk patron pressure. High-chaos routes can reject normal politics but should pay recognition and stability costs.

### Leader role families

| Leader family | Use for | Portrait direction | Name direction |
| --- | --- | --- | --- |
| Provisional president or prime minister | Civic republics, old parliaments, city states | Fictional generated unless a sourced real figure is intentionally used | Actual-ish personal name from regional pool. |
| Council or assembly | Indigenous, multiethnic, decentralised, fragile provisional states | Generated council or symbolic body portrait | Institutional name, not a person. |
| Military commander | Military councils, frontier states, defecting army districts | Fictional generated or sourced real if historically grounded | Personal name and rank direction. |
| Restored monarch or claimant | Kingdoms, emirates, sultanates, old dynasties | Sourced if real, generated if fictional alternate claimant | Personal or dynastic name direction. |
| Religious or sacred authority | Certain Middle Eastern, African, Asian, or high-chaos states | Sourced if real, generated if fictional symbolic | Handle carefully and source real symbols. |
| Foreign-backed cabinet head | Sponsor route | Fictional or sourced if specific historical figure | Name pool should fit region and sponsor route. |
| Port governor or mayor | Free cities, port polities | Fictional generated or existing portrait if safe | Personal name, not office title as country name. |
| Strange high-chaos authority | Antiquarian, archive, impossible claimant | Generated portrait, council, or symbolic body | Personal name only if one-person portrait. |

Generated one-person portraits must be paired with matching gender name pools and leader metadata. Council, committee, junta, court, or symbolic-body portraits should use institutional leader names. Real leaders must not be generated.

## Advisor and character direction

Advisors should reinforce the chosen route and region. They should not be generic stat vendors.

| Advisor family | Unlocked by | Role | Asset direction |
| --- | --- | --- | --- |
| Recognition envoy | Recognition lane | Improves recognition missions and treaty outcomes | Fictional portrait or sourced real figure if used. |
| District administrator | Administration lane | Improves local control and registry missions | Usually fictional generated. |
| Railway or port engineer | Economy lane | Improves rail, port, supply, and construction decisions | Fictional generated or generic advisor art. |
| Militia organizer | Army lane | Improves local guard and command obedience missions | Fictional generated. |
| Defecting officer | Army district or host rupture | Improves regular unit conversion | Can be real only with sourced portrait. |
| Patron liaison | Foreign-backed route | Improves aid but raises patron influence | Should reflect sponsor route. |
| League delegate | League route | Improves coalition trust and league cohesion | Shared or region-specific generated portrait. |
| Court minister | Restoration route | Improves legitimacy and court route | Sourced or generated depending identity. |
| Frontier commander | Border route | Improves defense and border missions | Fictional or sourced. |
| Antiquarian ideologue | High-chaos route | Improves hidden route but hurts recognition | Generated, not real scholar unless sourced and appropriate. |

Advisor discounts should come from focuses that build the institution. Do not scatter cheap advisors through every branch. Some advisor families can be locked out by route, such as patron liaison versus neutral conference, or court minister versus civil republic.

## Starting forces architecture

Starting forces should scale with package tier, local conditions, and chaos. The event should not create empty fighting countries, and it should not give every country the same divisions.

### Force scaling factors

| Factor | Increases starting force | Decreases or distorts starting force |
| --- | --- | --- |
| Package tier | compact, regional, partition, ambition | seed package, tiny state count |
| Chaos evolution | higher chaos gives more troops and stranger units | higher chaos also raises instability and border heat |
| Local population | more militia and manpower | sparse states limit units |
| Industry and depots | more equipment and regular units | rural states get poorly equipped units |
| Ports and naval bases | port guards, convoys, small naval assets | no coast means no naval path |
| Mountains, forests, deserts, steppe | terrain-specific units | weaker industry and supply |
| Former host weakness | more defections and depot capture | strong host limits defectors |
| Legitimacy and local control | better command and reinforcement | low values create militia fragmentation |
| Sponsor access | better equipment and officer cadres | patron influence and rivalry risk |
| League support | pooled reserves and training | requires coalition trust |

### Starting strength bands

| Package tier | Calm or early chaos | Mid chaos | High chaos | Notes |
| --- | ---: | ---: | ---: | --- |
| Seed | 1 to 2 small units | 2 to 3 small units | 3 units with higher instability | Often militia, guard, or port defense. |
| Compact | 3 to 5 units | 4 to 6 units | 5 to 8 units | Mix of militia and defectors. |
| Regional | 6 to 9 units | 8 to 12 units | 10 to 15 units | Can include regulars and terrain units. |
| Partition | 10 to 14 units | 12 to 18 units | 16 to 24 units | Must scale to host loss and depots. |
| Ambition | Based on base tier plus route assets | plus elite or special unit family | plus stronger but unstable units | Ambition does not mean unlimited units. |
| Special high-chaos | 3 to 12 based on size | 6 to 16 | 8 to 24 if large | Carries recognition and instability penalties. |

Exact numbers should be tuned in implementation. The spec defines bands and scaling direction.

### Unit template families

| Template family | Suitable packages | Role | Reinforcement path |
| --- | --- | --- | --- |
| Local militia | most releases | Emergency defense, weak offense | local control, militia integration |
| District guard | civic and administrative releases | Capital and rail defense | district offices, local courts |
| Border guard | border and host dispute states | Defensive line | border defense plan, host dispute missions |
| Railway troops | Soviet-region, Europe, Asia, African inland, Siberia | Rail and depot security | rail authority, depot missions |
| Port guard | island and port polities | Coastal defense, convoy security | customs house, harbor guard |
| Mountain detachment | Caucasus, Andes, Himalaya, Alps, highlands | Terrain defense | mountain government, frontier roads |
| Desert or steppe cavalry | Sahel, Arabia, Central Asia, Patagonia, steppe | Mobility and frontier control | frontier route, officer cadre |
| River patrol or river infantry | Mesopotamia, Congo, Nile, Amazon, Mekong | River corridor control | river authority, local control |
| Defecting regulars | regional and partition packages | More professional force | officer cadre, command obedience |
| Foreign volunteer cadre | sponsor or league route | Trained support | patron aid, league reserves |
| Ceremonial or royal guard | restoration and high-chaos packages | Elite but small force | legitimacy and court route |
| Factory guard | industrial releases | Local defense and production protection | arsenals and workshops |

### Reinforcement paths

A country can grow forces after release through several routes.

| Path | Requirements | Effect direction | Risk |
| --- | --- | --- | --- |
| Local mobilization | legitimacy, manpower, equipment | more militia or guards | instability if overused |
| Militia integration | command mission success | upgrade militia to regulars | failure creates rogue militia |
| Depot capture | local control and rail hub | equipment and defectors | raises host anger |
| Sponsor arms | recognition or sponsor access | better equipment and cadres | patron influence and sponsor rivalry |
| League pooled reserves | league membership and trust | shared defense units | league cohesion cost |
| Officer school | army lane progress | template upgrades and commanders | XP and time cost |
| Port convoy lifeline | port and convoys | equipment and support units | blockade and patron risk |
| High-chaos levy | special route | larger or stranger forces | recognition, instability, and border heat cost |

## Starting economy and technology setup

The economy should reflect state reality. A tiny inland state should not spawn with a fully developed industry. A port should feel different from a rail hub. A resource state should have resource politics. A high-chaos state can be stronger, but it should not ignore logistics.

| Package profile | Economy setup | Focus path emphasis |
| --- | --- | --- |
| One-state rural | minimal factories, manpower and supply concerns | district offices, ration offices, local guards |
| One-state port | port, convoys if justified, customs, port guard | customs house, convoy lifeline, sponsor access |
| Industrial enclave | factories and factory guard, repair needs | arsenals, rail, production lines |
| Rail corridor | rail, supply hub, trains, depot risk | rail authority, aid corridor |
| River region | infrastructure, river ports where valid, grain and bridges | river authority, local control |
| Mountain region | low industry, defense and roads | frontier roads, mountain guard |
| Large partition | mixed economy, big disruption | emergency budget, rail, districts, industry |
| High-chaos restoration | distorted economy based on claims | legitimacy or ambition first, economy fragile |

Technology should be basic and region-appropriate. New countries should inherit some host technology or templates if they plausibly arise from existing state structures. Very rural, indigenous, or high-chaos antiquarian states can start with fewer technologies but should have focus paths to modernize or secure foreign equipment. Do not make them unplayable for flavor.

## Package matrix by broad release family

The full release pool can include far more than the examples below. These examples define how the registry should classify them. Every additional country should be assigned to one of these families, then given registry fields.

| Family | Ordinary package default | Strong package trigger | Typical focus insert | Typical unit style |
| --- | --- | --- | --- | --- |
| Existing vanilla releasable republic | seed or compact | several states, high legitimacy, old cores | European or regional republic | guards, defectors, militia |
| Old European border claimant | compact | disputed industrial or strategic states | treaty files, border commissions | border guards, rail troops |
| Free city or port | seed | strategic port, sponsor interest | customs house, free port charter | port guards, convoy support |
| Soviet-region republic | compact or regional | large state group or depots | commissariat remnants, rail corridor | defectors, rail troops, cavalry |
| Caucasus or mountain release | compact | mountain passes or old kingdom identity | mountain government | mountain detachments |
| Middle Eastern mosaic state | compact | river or mandate core | mosaic assembly, mandate files | urban militia, desert or mountain guards |
| Mesopotamian river identity | regional | river-state control or antiquarian route | river administration | river patrols, defectors |
| African restored court | compact or regional | old kingdom core or court route | restored court, chiefs council | guards, rifle units, cavalry |
| African port polity | seed or compact | Swahili, island, Gulf, Red Sea, or strategic port | coastal customs | port guards, convoy routes |
| African river or inland polity | compact | river corridor, caravan route, old polity | river and caravan offices | local guards, cavalry, river troops |
| South American indigenous assembly | seed or compact | high local control and land route | land assembly, frontier resistance | local militia, mountain or forest troops |
| Andean restoration | regional or ambition | highland state group and high legitimacy | old imperial road | mountain units, local guards |
| Asian regional polity | compact | old court, industrial corridor, or port | old court, frontier federation | defectors, guards, terrain units |
| Island state | seed | naval base, league route, sponsor interest | harbor guard, convoy lifeline | port guards, marines if justified |
| High-chaos antiquarian claimant | special | chaos evolution and dossier route | archive miracle, old banners | unstable special guards |
| Coercive compact candidate | regional or high-chaos | military route and high border heat | cult of borders, frontier march | regulars, border troops, shock units |

## Country package matrix examples

This section gives a broader example matrix. It is not the full final release pool. It shows how the final registry should classify countries so additional entries can be added without inventing new mechanics.

| Region family | Public identity | Candidate tag rule | Tier | Overlay modules | Starting politics | Force style | Special notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Europe | Scotland | existing if safe | compact | civic, league, port if coastal | civic republic | guards, defectors | Existing content audit required. |
| Europe | Bavaria | existing if safe | regional | restoration, industry, border | republic or restoration | regular defectors, guards | Can be federal or court route. |
| Europe | Danzig | existing or X | seed | free port, border | city republic | port guards | Sponsor rivalry high. |
| Europe | Occitania | X if missing | regional | civic, cultural, league | republic | militia, guards | High-chaos pool. |
| Soviet-region | Ukraine | existing if safe | regional | republic, rail, army district | Event 6 republic | defectors, rail troops | Origin separation mandatory. |
| Soviet-region | Volga Bulgaria | X if missing | ambition | restoration, river, league | restoration or assembly | cavalry, river guards | Same tag through Event 5 uses other content. |
| Soviet-region | Siberian Republic | existing or X | regional | rail, frontier | republic or military | rail troops, cavalry | Isolation and supply. |
| Middle East | Assyria | X if missing | compact or regional | mosaic, mountain, antiquarian | assembly or restoration | mountain guards | Sensitive symbol and identity review. |
| Middle East | Mesopotamia | X if missing | regional or ambition | river, federation | republic or assembly | river troops, regulars | Could be formable instead of release. |
| Middle East | Luristan | X if missing | seed or compact | mountain, tribal | local authority | mountain guards | Strong local control route. |
| Africa | Kongo | X if missing | regional or ambition | restored court, river | court or assembly | guards, river troops | Formable and court routes. |
| Africa | Kilwa | X if missing | seed or compact | Swahili port | port republic or sultanate | port guards | Indian Ocean trade direction. |
| Africa | Benin | X if missing | compact or regional | court, regional diplomacy | restoration or assembly | guards | Sourced court symbols. |
| Africa | Sokoto | X if missing | regional | emirate, Sahel | restoration or council | cavalry, guards | Source review and careful tone. |
| South America | Mapuche | X if missing | compact or regional | land assembly, frontier | assembly | frontier militia | Defensive and anti-client. |
| South America | Quechua Republic | X if missing | regional | highland, assembly | assembly or republic | mountain troops | Andean federation hook. |
| South America | Inca restoration | X if used | ambition | old roads, restoration | restoration | mountain troops, royal guard | Hidden or formable-linked. |
| Asia | Shan | X if missing | compact | mountain, border federation | assembly or local authority | mountain guards | Sponsor and host dispute. |
| Asia | Manchuria | existing if safe | regional | industry, sponsor risk | military or client | regulars, factory guards | Do not overwrite existing content blindly. |
| Asia | Dravidian Republic | X if missing | regional | federal, coastal | assembly or republic | militia, port guards | Needs careful state grouping. |
| Port | Singapore | existing or X | compact | port concession, industry | port republic or client | port guards | Patron influence central. |
| Port | Tangier | X if missing | seed | international port | free city | port guards | Recognition and sponsor rivalry. |
| Port | Malta | existing or X | seed or compact | island, order | republic or restoration | port guards | Existing tag audit. |
| High-chaos | Carthage | X if used | ambition | antiquarian, port | restoration or high-chaos | port guards, special guard | Hidden, not early pool. |
| High-chaos | Hittite Anatolia | X if used | ambition | antiquarian, Anatolian | restoration | ceremonial guards | Sourced symbol caution. |
| High-chaos | Archive Republic | X if used | special | legal absurdity, high-chaos | emergency cabinet | militia | Public name must be region-based. |

## Country-specific ambition examples

These are design examples for stronger releases. They are not final localisation.

### Volga Bulgaria Event 6 route

Volga Bulgaria can appear through Independence Wave, but it receives Independence Wave mechanics and focus content. Its regional insert should use river, steppe, restoration, and league or federation routes. If it appears through Soviet Collapse, this route is not used.

| Lane | Direction |
| --- | --- |
| Survival | Secure river towns, build local registry, guard rail or river routes. |
| Politics | Restoration authority, assembly of peoples, or civil republic. |
| Army | Cavalry, river guards, defecting regulars, depot route. |
| Diplomacy | Recognition through local legitimacy, league with nearby releases, balanced sponsors. |
| Ambition | Idel-Ural or Volga federation preparation if state control and legitimacy support it. |
| Failure | Patron capture, host reclamation, or border fever. |

### Assyria Event 6 route

Assyria should be a compact or regional release, not a generic tag. It should emphasize mosaic assembly, mountain or river defense depending states, recognition struggle, sponsor risk, and a hidden antiquarian or wider Mesopotamian ambition only at higher chaos.

| Lane | Direction |
| --- | --- |
| Survival | Protect local communities and provisional capital, stabilize local districts. |
| Politics | Assembly, restoration authority, foreign-backed cabinet, or emergency executive. |
| Army | Mountain guards, urban militia, foreign-trained cadres if sponsor route. |
| Diplomacy | Recognition and anti-puppet clauses are central. |
| Ambition | Mesopotamian federation or ancient restoration path only if conditions support it. |
| Failure | Patron dependence, host anger, low recognition, or internal fragmentation. |

### Kongo Event 6 route

Kongo can be a strong African restoration or federation route. It should use restored court, river authority, local chiefs council, anti-client clauses, and regional federation mechanics.

| Lane | Direction |
| --- | --- |
| Survival | Establish court or assembly and local control over river or hinterland states. |
| Politics | Restoration court, chiefs council, civil republic, or sponsor-backed cabinet. |
| Army | Local guards, river troops, rifle associations, foreign cadres if patron route. |
| Economy | River trade, roads, limited workshops, regional resources. |
| Ambition | Kongo federation or restored kingdom formation through decisions. |
| Failure | Court legitimacy collapse, sponsor capture, or rival local polities. |

### Mapuche Event 6 route

Mapuche should not be treated as a normal European-style republic. The insert should emphasize land, local authority, frontier resistance, decentralized leadership, and anti-client protection.

| Lane | Direction |
| --- | --- |
| Survival | Local land control, frontier defense, emergency assembly. |
| Politics | Assembly of peoples, military defense council, cautious republic route. |
| Army | Frontier militia, mountain or forest detachments, defensive focus. |
| Diplomacy | Recognition through land control and anti-puppet clauses. |
| Ambition | Wider indigenous confederation or frontier settlement route when state control supports it. |
| Failure | Over-centralization, patron capture, border incident cascade. |

### Kilwa Event 6 route

Kilwa should be a port-centered compact release. It should emphasize Swahili coast trade memory, customs, sponsor competition, port defense, and league or maritime ambition.

| Lane | Direction |
| --- | --- |
| Survival | Secure the port, customs, and aid corridor. |
| Politics | Port republic, sultanate route, or foreign-backed cabinet. |
| Army | Port guards, convoy defense, limited naval path if state supports it. |
| Diplomacy | Recognition through trade and maritime contacts. |
| Ambition | Maritime league or Swahili coast federation through the formable web. |
| Failure | Sponsor capture, blockade, smuggler crisis. |

## Country package cleanup and transformation

The focus and country package system needs clear cleanup.

| Event | Cleanup behavior |
| --- | --- |
| Country annexed | Stop active Event 6 missions, preserve origin history if restoration possible, clear target lists. |
| Country reabsorbed by host through settlement | Remove or transform independence ideas, close Event 6 release decisions, record settlement. |
| Country puppeted by sponsor | Convert foreign ledger to client-state form, close neutral and anti-puppet routes, keep rebellion or liberation options when implemented. |
| Country joins league | Enable league focus and decisions, suppress incompatible sponsor dominance actions if route says so. |
| Country forms larger country | Consume or transform country package into formable package, migrate mechanics, clear obsolete host disputes where appropriate. |
| Country becomes aggressive bloc member | Lock settlement or league arbitration focuses if incompatible, open coercive branch. |
| Former host dies | Use successor host memory if valid, otherwise close host dispute and convert border content to regional settlement. |
| Same tag reappears by another event | Do not reuse Event 6 content unless Event 6 origin memory is present. |

## Player-facing text direction for focus and country layer

Final localisation should be written from this direction.

| Surface | Direction |
| --- | --- |
| Shared survival focuses | Sudden government work, practical fear, local offices, guards, railways, capitals, and public uncertainty. |
| Political route focuses | Specific institutional identity and public authority, not generic ideology slogans. |
| Recognition focuses | Delegations, treaty language, observers, public acknowledgment, foreign leverage. |
| Host dispute focuses | Border commissions, local claims, defensive preparations, settlement pressure. |
| League focuses | Mutual survival, arbitration, common defense, shared recognition. |
| Coercive focuses | Hard pressure, impatient claims, contempt for settlement, risk of backlash. |
| Regional inserts | Use region-specific institutions, terrain, economy, and memories. |
| High-chaos focuses | Strange legal certainty, old symbols, irrational resolve, and public unease without spoiling hidden mechanics. |
| Country names | Readable map names. Avoid offices, boards, or internal committees as public names. |
| Leader names | Personal names for one-person leaders, institutional names for councils and bodies. |

Do not paste working labels into localisation. Do not expose hidden formable or high-chaos routes too early.

## Documentation outputs from this layer

Implementation should eventually maintain these docs or tables.

| Document or table | Purpose |
| --- | --- |
| Country package registry | All Event 6 possible release packages with tags, region, tier, states, focus modules, assets, and AI. |
| Focus route coverage table | Required shared lanes, regional inserts, ambition inserts, and actual implementation status. |
| Starting force matrix | Unit families, templates, equipment source, scaling, reinforcement routes by package tier. |
| Leader and portrait ledger | Real versus fictional leaders, portrait source mode, gender/name pool requirements. |
| Flag and symbol ledger | Existing, sourced historical, or generated fictional flags and emblems. |
| AI route matrix | AI route selection by package tier, region, values, chaos, and invalid route checks. |
| Origin separation audit | Tags that overlap Soviet Collapse or other events and how Event 6 origin checks protect them. |

## Acceptance criteria for country package architecture

The country package design is complete when the implementation agent can create or reuse tags, assign Event 6 origin content, protect host survival, load the correct focus overlay, provide starting forces and reinforcement paths, assign leaders and politics, route assets by source mode, connect packages to decisions and mechanics, and clean up invalid or annexed Event 6 actors without breaking overlapping event systems.
