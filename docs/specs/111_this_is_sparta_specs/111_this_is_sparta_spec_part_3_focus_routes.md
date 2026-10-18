# Part 3: Focus architecture and five campaign routes

This part defines the architecture of Event 111's large focus tree. Semantic keys identify planned consumers for implementation and assets. They are not installed focus IDs or final localisation. The five accepted route names are Spartan Hegemony, Legacy of Alexander, Thermopylae Avenged, The Western Campaign and Hellenic Colonies Reborn.

The country and military contract is in [Part 2](111_this_is_sparta_spec_part_2_country_and_military.md). Actions, missions and territorial settlement are in [Part 4](111_this_is_sparta_spec_part_4_decisions_and_settlements.md). [Part 1](111_this_is_sparta_spec_part_1_core.md) owns common values, milestone persistence and Chaos accounting. Ordinary route completion never requires Age of Heroes.

## 1. Tree shape and progression

The tree opens on a country that already exists. Its first visible choice is where to spend scarce attention: civilian administration, modern military liaison or the local production base. The opening has two to four meaningful choices, followed by political settlement and a sustained set of support branches. It does not make the player complete a long founding corridor before using Sparta.

The implementation owns final focus count, coordinates and individual prerequisite syntax. This architecture requires early, middle and late play in each branch. A group should contain enough focuses to express its actual programs and choices, without splitting one reward into a sequence of empty clicks. Use 7-day emergency or policy handoffs, 35-day strategic choices and 70-day major programs where those roles fit the work. A visible duration must correspond to a meaningful outcome.

| Anchor consumer | Branch responsibility and groups | Primary filters | Icon and navigation direction |
|---|---|---|---|
| `111_anchor_foundation` | Emergency supply, local administration, contact with contemporary specialists | Survival, Administration | Laconian landscape and a compact civic or supply symbol. Initial camera anchor. |
| `111_anchor_polity` | Provisional compact, three institutional directions, citizenship settlement, later succession or authority settlement | Politics, Citizenship | Paired authority, ephor oversight, civic assembly or staff insignia as applicable. |
| `111_anchor_state_capacity` | Workshop recovery, arsenal or licensed supply, construction and rail, regional administrative capacity | Industry, Logistics | Workshop, road, rail and civic building motifs. |
| `111_anchor_research` | Technical education, functioning research network, late imperial institutions | Research, Industry | Technical tools and a research institution, avoiding generic glowing science imagery. |
| `111_anchor_land_forces` | Returned-host liaison, adult Agoge, support arms, staff work, mobile or terrain-specialist emphasis | Army, Training | Ancient and modern equipment remain visually distinct. |
| `111_anchor_sea_power` | Working port, convoy and escort service, fleet or patrol doctrine, amphibious and distant logistics | Navy, Logistics | Harbour, convoy, escort and fleet motifs. |
| `111_anchor_air_power` | Airfield and training, interceptor and observation service, close-support or maritime emphasis | Air, Logistics | Audited aircraft silhouettes and a coastal or land-service context. |
| `111_anchor_foreign_relations` | Recognition, equipment partners, passage agreements, real Greek and regional diplomacy | Diplomacy, Trade | Treaty and route motifs with actual counterpart identity when contextual. |
| `111_anchor_hegemony` | Greek security, league or union, mainland settlement, Aegean responsibility, enduring Greek order | Conquest, Greece, Diplomacy | Shield-circle or shared civic motifs, then a settled Greek realm. |
| `111_anchor_alexander` | Macedonian legitimacy, eastern entry, Egyptian and Levantine campaigns, Mesopotamia and Iran, imperial administration | Conquest, East, Administration | A continental campaign map and distinct regional administrative motifs. |
| `111_anchor_thermopylae` | Greek defence, campaign mandate, alternative eastern corridors, Persian war, bounded settlement and reconstruction | Conquest, East, Army | Pass, spear and eastern campaign motifs. No claim that Leonidas is physically present. |
| `111_anchor_west` | Crossing preparation, southern or Adriatic entry, southern Italy and Sicily, Rome and northern industry, western settlement | Conquest, West, Navy | Crossing, southern Italian theatre, Rome and Mediterranean logistics. |
| `111_anchor_colonies` | Maritime service, five-basin network, sovereign or treaty charter, distant administration, enduring commonwealth | Conquest, Navy, Trade | Distinct port and sea-region motifs rather than repeated generic claims. |

Focus Navigation exposes each available anchor and preserves the selected route as the principal conquest destination. The four closed routes remain understandable in their summaries without dominating the normal view. Their unavailable status must state the actual commitment. A branch should not disappear before the player has been able to compare its strategic promise.

Each focus has one primary branch owner or an explicitly documented convergence. Filters identify its main purpose and its useful secondary role. Implementers must verify AND and OR prerequisites against installed native precedents. Layout review must make early choices, internal alternatives, convergence and terminals readable at normal zoom. No exact coordinates or artificial focus-count quota is prescribed here.

## 2. Support branches that remain useful

The political branch changes who participates in the modern state and how power is exercised. Its three directions are renewed dyarchy, wider citizenship and military supremacy, as defined in Part 2. Each has an early constitutional choice, a practical recruitment or administrative consequence, a later test of promises and a mature or failed institutional stage. Military command can coexist with a naval strategy, and a civic assembly can choose a continental empire. Domestic reform does not unlock a second conquest route.

Industry develops a viable home economy before promising an imperial arsenal. Workshop restoration leads to domestic standardization or foreign licensing. Construction and supply groups then build actual factories, depots, roads, rail and port capacity through paid projects. The mature choice emphasizes concentrated industrial production or a more distributed network with better resilience and regional participation. Both retain essential military supply. One costs more fuel and strategic material, while the other requires more regional administrative work.

Land forces progress from ancient-modern liaison through the adult Agoge and support services to staff integration. The founding contemporary local brigades are ordinary native infantry. Later custom modern cadres follow Part 4's renewable quota and finite original-survivor accounting, including every contemporary replacement. The early group includes a once-only basic firearms familiarization outcome worth 5 Military Adaptation, available below 25 with contemporary instructors, a safe site and 100 real modern rifles. Together with the 10-point liaison stage, it gives the weak opening a legal path from 10 to the first 25-point gate. Mobile combined arms and terrain-specialist warfare are meaningful late emphases. They retain ordinary artillery, engineers, medicine and logistics. Aircraft progress through training and observation to useful defensive and offensive roles. Naval progress covers convoys, escorts, repair and supply before expensive fleet ambitions. These are substantial connected branches, not isolated technology coupons.

Foreign relations supplies recognition, arms contracts and access agreements with actual governments. It also provides tools for recovering from refused route demands. A player can negotiate with a state before deciding to attack it, subject to the terms and duration of agreements. There is no universal focus that makes all neighbours obedient or gives passage through every strait.

Research progression is exactly two, three, four and five slots at the institutional stages in Part 2. A route's late administration can contribute to the fifth-slot gate, but no route is uniquely entitled to modern science. State capacity and research remain relevant after the conquest charter, since the resulting order has ongoing supply and settlement obligations.

The three spirit slots remain polity, military institution and state capacity. Every focus reward declares a replacement in one slot or a genuine different consumer. The branch may grant an actual research opportunity, new equipment access, a paid project, a division template, a treaty family or a state-specific administrative benefit. It may not evade the three-spirit limit by calling a fourth country modifier temporary.

## 3. Commitment and common route structure

The player can inspect all five campaigns from the start. Exploratory diplomatic contacts and shared military preparation do not lock a route. The lock occurs when the player confirms that route's first territorial charter or expansion mandate. The confirmation shows the required regions, first practical objective and four closed routes. It defaults to cancel and rechecks the country and route state.

After commitment, another route's claims, client charter, regional discounts and final identity cannot be collected. Ordinary wars outside the chosen route remain normal gameplay. They do not provide another branch's scripted rewards. A lost battle, changed ideology, regime reform, save reload or temporary annexation never clears the commitment receipt. The player recovers within the chosen route's alternatives.

Every route contains preparation, an internal strategic choice, several campaign groups, regional administration and a final charter. Focuses authorize the political program and provide practical tools. Decisions select the actual target, negotiate, prepare a feasible operation and verify the formable. A focus may unlock a claim family. The paid action applies claims only to the selected current target and disclosed geographic set.

## 4. Geographic roles and authoritative sets

These are complete authored geographic requirements. They describe this fictional political program, not historical proof that Sparta ruled the regions. Final installed state lists, province consumers and exact map-puzzle geometry require the geography audit. A semantic role must resolve to an explicit versioned list with inclusions, exclusions and overlap handling. The implementation cannot replace a difficult requirement with a nearby convenient state without changing the specification.

The Greek homeland uses the geographic territory assigned to Greece in the audited 1936 bookmark, including its mainland and islands, with the new Laconian split reconciled into that footprint. Later annexation or release does not change the shape. Vardar Macedonia, Albania, Bulgarian territory, eastern Thrace, Cyprus and the Dodecanese are not silently added to that homeland. A route can explicitly add one of them through its own set.

| Geographic role | Included authored geography | Exclusion or precision rule |
|---|---|---|
| `111_geo_laconia` | The mandatory new Laconia state containing the Spartan location | Never the whole Peloponnese by convenience. |
| `111_geo_peloponnese` | All Peloponnesian mainland states after the split | Excludes offshore island groups unless already part of an audited indivisible state. |
| `111_geo_greek_homeland` | The fixed Greek mainland and island footprint defined above, including Laconia | Greek Macedonia belongs here. Vardar Macedonia does not. |
| `111_geo_aegean_extension` | The Dodecanese and audited eastern Aegean island role centred on Rhodes | An explicit late extension, not a starting core claim on every Aegean coast. |
| `111_geo_vardar_macedonia` | The geographic territory of modern North Macedonia, mapped to installed states | A current Macedonian actor may own more or less. Its whole empire is not automatically required. |
| `111_geo_anatolia` | All Asian Turkish territory in the authored geographic reference | Excludes European eastern Thrace. A strait crossing still needs legal operational access. |
| `111_geo_levant` | Syria, Lebanon, Jordan and Israel/Palestine as a geographic set | Names identify geography, independent of current tags. No requirement to own a distant colony of a current local ruler. |
| `111_geo_egypt` | Egypt, including Sinai, the Nile valley, delta and western Egyptian territory | Excludes Sudan and a current Egyptian actor's unrelated external possessions. |
| `111_geo_mesopotamia` | The geographic territory of Iraq | Does not expand whenever an Iraqi or Persian actor acquires a foreign state. |
| `111_geo_iran` | The geographic territory of Iran | Actual Event 071 Persia is a separate actor lookup. Its foreign conquests affect diplomacy and force estimates, not this fixed shape. |
| `111_geo_afghanistan` | Afghanistan | An optional eastern extension after the main Alexander charter. |
| `111_geo_indus_western_approach` | Modern Pakistani Balochistan and Khyber Pakhtunkhwa | Excludes Sindh. The mapped role must connect the Iranian and Afghan approach to Punjab. |
| `111_geo_pakistani_punjab` | Modern Pakistani Punjab | Excludes Indian Punjab. These modern geographic choices are authored objectives, not a reconstruction of an ancient frontier. |
| `111_geo_thermopylae_south` | Western Anatolian entry through the Izmir and Bursa regions, central Anatolia around Ankara and Konya, Cilicia and the southeastern Anatolian link, then the Mosul and Baghdad corridor to Iran | Requires an actual connected route through the mapped states. It does not require Egypt, the full Levant or all Iraq. |
| `111_geo_thermopylae_north` | Western Anatolian entry through Bursa and central Anatolia, then the Sivas, Erzurum and Kars corridor, Armenia and Azerbaijan, reaching northwestern Iran | Requires the complete northern alternative. A disconnected port or a friendship with a remote state cannot stand in for the corridor. |
| `111_geo_italian_peninsula` | Continental Italian territory from the southern peninsula through Rome and the northern industrial regions | Includes all peninsula regions, excludes colonies and islands covered by separate roles. |
| `111_geo_sicily` | Sicily | A whole owned state role is required where the installed map cannot express a sovereign city possession. |
| `111_geo_sardinia` | Sardinia | Corsica is an optional later western objective, not a hidden prerequisite. |
| `111_geo_crete` | Crete | Also a shared physical location for evolution access. It receives no automatic mythic reward. |
| `111_geo_theban_site` | The audited state and relevant site containing Thebes | Mythic access uses its own verified site condition, not ownership of every Greek state. |
| `111_geo_arcadian_site` | The audited Arcadian site relevant to Stymphalos | Same distinction between a historical site and a broad territorial formation set. |

Corridor resolution is a build acceptance gate. The resolved lists must have a genuine land connection between their entrance and Iran. Where a named city falls in a broad state, the whole required state is visible in the puzzle. No invisible province lease satisfies a whole-state ownership condition. Alternative corridor lists may share states, but each must independently provide the complete route.

### Colonial anchor roles

The colonial route uses a finite, disclosed selection in each sea region. These are modern strategic holdings inspired by the brief's Hellenic maritime program. The research handoff verifies historical association separately and preserves the different Greek traditions involved.

| Sea region | Required anchor selection | Planned role keys |
|---|---|---|
| Aegean | Crete or Rhodes | `111_port_crete`, `111_port_rhodes` |
| Eastern Mediterranean | Cyprus and either Alexandria or Cyrenaica | `111_port_cyprus`, `111_port_alexandria`, `111_port_cyrenaica` |
| Central Mediterranean | Apulia and Sicily | `111_port_apulia`, `111_port_sicily` |
| Western Mediterranean | Provence and Catalonia | `111_port_provence`, `111_port_catalonia` |
| Black Sea | One northern anchor from Crimea or the Odessa region, and one southern anchor from Sinope or Trabzon | `111_port_crimea`, `111_port_odessa`, `111_port_sinope`, `111_port_trabzon` |

This gives nine required selected anchors across five sea regions. The two Black Sea sides are distinct requirements. A single broad state cannot count twice merely because it contains two named ports. Each role resolves to an actual coastal state and usable port. If the installed geography merges two roles, the author must select a distinct allowed alternative or document a revised role before enablement.

### Final-set predicates

| Final set | Geography | Sovereignty and administration |
|---|---|---|
| `111_set_hegemony_final` | Greek homeland | Union requires Spartan ownership and control. League permits Spartan land and qualifying charter partners that own and control their contribution. Greek mainland and island settlements must be complete. |
| `111_set_alexander_final` | Greek homeland, Vardar Macedonia, Anatolia, Levant, Egypt, Mesopotamia and Iran | Central empire owns and controls the set. The client system permits registered regional clients under binding charter obligations. Each of the seven regional administrations must be complete. |
| `111_set_alexander_eastern_extension` | Afghanistan, Pakistani Balochistan, Khyber Pakhtunkhwa and Pakistani Punjab, with a connected route from Iran | Optional after the main Alexander charter, under the same direct or registered-client rule. Afghan, western-approach and Punjab settlements are required. Sindh and Indian Punjab are excluded. |
| `111_set_thermopylae_south_final` | Greek homeland, Aegean extension, southern corridor and Iran | Greece and Iran require Spartan ownership and control. Corridor states may be direct holdings or qualifying subordinate corridor administrations. Greek, corridor and Iranian settlements are required. |
| `111_set_thermopylae_north_final` | Greek homeland, Aegean extension, northern corridor and Iran | Same rule, using the complete northern alternative. The selected final route cannot combine incomplete halves of two corridors. |
| `111_set_west_final` | Laconia, Italian peninsula, Sicily and Sardinia | Laconia and Rome's state require Spartan ownership and control. The final institutional choice permits direct Italian administration or registered Italian regional clients elsewhere. Southern Italy, central/northern Italy and the two island settlements must be complete. |
| `111_set_colonies_final` | Laconia and the nine selected anchor roles | Sovereign-chain choice requires Spartan ownership and control of every anchor. Commonwealth choice requires direct holdings in at least three different sea regions, including the Aegean anchor, with remaining anchors supplied by qualifying charter partners. Five basin-service settlements are required. |

Ownership, control and a qualifying partner are separate predicates. Generic faction membership, docking rights, military access and a cosmetic puppet relationship do not automatically satisfy a territorial role. Every qualifying charter specifies the real state, ruler, rights, obligations, supply responsibility, duration and exit consequences. The same final-set evaluator drives the puzzle, focus tooltips, proclamation eligibility and achievement consumers.

## 5. Spartan Hegemony

This route begins with securing the remaining Peloponnese and defining relations with living Greece. The early groups offer a border settlement, a Greek defence conference and a practical road and coastal-supply program. A refusal does not delete Greece's agency. Sparta can negotiate a limited settlement, compete for leadership or pursue a normal war through legal mechanics.

The major internal fork is a **direct union** or **chartered league**. Direct union seeks ownership of the Greek homeland and a unified modern administration. It can secure voluntary union through a consequential accepted agreement, or acquire territory by war and then settle it. The league preserves actual partner governments, giving them defined representation, joint-defence commitments and the right to contest broken terms. It cannot silently annex a human Greece through a focus.

The middle groups address mainland roads and arsenals, the relationship with Greek Macedonia and Thessaloniki, island administration, naval protection and civic admission. An internal league choice concerns strong common defence with limited central taxation or a more decentralized commercial arrangement with a smaller common military obligation. The direct-union choice concerns a Laconian institutional centre or wider Greek representation. Both must accommodate the modern population and sustain recruits outside the original host.

The Aegean extension follows the Greek settlement as a substantial optional late campaign. It provides a reason to develop escorts, amphibious troops and island supply. It can add Rhodes and the declared island role without making every Turkish coastal state a secret Hegemony requirement. A player can complete the Greek order first and continue the naval extension afterward.

The final charter uses `111_set_hegemony_final`, Civic Settlement at least 60 and Military Adaptation at least 50. It records `111_milestone_hegemony_complete` and changes the same country's identity to `111_identity_hegemony_union` or `111_identity_hegemony_league`. The reward is a functioning Greek administrative or defence system, access to mature citizen recruitment, route-specific regional production projects and a narrower state-capacity advantage. Treaty partners retain real forces and governments.

Failure involves disputed authority, partner refusal, civil-administrative obstruction or the loss of a major Greek region. Recovery can revise league terms, reduce taxation, replace an unsuccessful federal operation or complete a direct region's legal settlement. A league cannot recover by pretending a departed member remains a contributor. The AI favours this route when Greece is the attainable strategic theatre, broad civic legitimacy is available and a continental expedition would exceed its logistics.

## 6. Legacy of Alexander

The route explicitly appropriates a Macedonian legacy. The narrative and research handoff must identify that origin. The early groups settle the Greek base, deal with the actual Macedonian actor and establish the first eastern supply corridor. IMRO Macedonia, when alive, has its own ambitions and can negotiate recognition, claim a senior role, join a joint campaign, demand concessions or oppose Spartan leadership.

The geographic requirement remains Vardar Macedonia even when the current Macedonian actor owns a different footprint. If it is absent, the route deals with the current owners and the local administrative question. It does not create a replacement Macedonia solely to clear a focus. Any newly released client must use an already complete and audited country package.

The first operational fork chooses a **Levant-first campaign** or **Egyptian maritime entry**. The former invests in Anatolian transit, rail and inland supply. The latter invests in escorts, a real landing base, port repair and the Nile approach. Both regions are ultimately required, but their order changes the war plan, early equipment priorities and diplomatic exposure. Mesopotamia and Iran are later campaigns with separate supply and administration groups.

The institutional fork is a **central empire** or **regional client system**. Central rule provides firmer direct production and military control after expensive settlement. Clients reduce immediate administrative burden and can contribute real local armies, but require binding concessions and can refuse excessive demands. The system uses living governments or complete legal release packages. It does not create anonymous satrapy tags without leaders, economies, forces or growth paths.

Seven regional administrations make this route the longest and most demanding. Greece, Vardar Macedonia, Anatolia, the Levant, Egypt, Mesopotamia and Iran each need a functioning settlement. A different flag on the capital does not complete these obligations. Later optional groups pursue `111_set_alexander_eastern_extension`: Afghanistan, modern Pakistani Balochistan, Khyber Pakhtunkhwa and Pakistani Punjab, reached through a connected route from Iran. Afghan, western-approach and Punjab settlements use the selected direct or registered-client model. Sindh and Indian Punjab are excluded. This is an authored optional political campaign, not a claim that the modern boundaries exactly reproduce Alexander's conquests. It extends the route after the main charter, contributes to achievement ACH07 and never becomes a prerequisite for the principal Alexander completion.

The final gate is `111_set_alexander_final`, Civic Settlement at least 65 and Military Adaptation at least 70. It records `111_milestone_alexander_complete` and grants `111_identity_alexander_empire`. The tangible reward is the mature network of regional administrations, access to the late imperial research institution, regional production and logistics specialization, and an imperial coordination benefit within the existing state-capacity slot. It does not core every conquered state.

Failure should expose the cost of distance. A client can withhold participation, an Egyptian landing can fail, a Mesopotamian supply corridor can collapse, or a powerful Persia can survive beyond the required region. Recovery uses another operational entry, a revised client charter, temporary concentration on fewer fronts or a limited peace. The AI needs a functioning regional base, transport and industrial capacity before choosing this route. Prestigious claims alone are insufficient.

## 7. Thermopylae Avenged

This route turns a Leonidas-centred memory into a modern eastern war program. Leonidas is a political reference, not an automatically resurrected leader. Its purpose is more concentrated than Alexander's imperial itinerary: secure Greece and the Aegean approach, build a usable route to Iran, defeat the actual Persian power and determine the resulting occupation.

The first groups establish Greek defence, modern fire support and an expeditionary mandate. The route then chooses the **southern Anatolian and Mesopotamian corridor** or the **northern Anatolian and Caucasian corridor**. Each has a full geographic list, infrastructure needs and potential adversaries. The northern route does not receive free access through Armenia or Azerbaijan. The southern route does not pretend that capturing one Turkish port provides supply to Baghdad.

Existing Event 071 Persia is evaluated from its actual territory, army, allies and ambitions. A weakened Persia may negotiate a limited settlement, while a stronger one can mobilize regional partners or pre-empt the expedition. If the restored actor is absent or has lost Iran, the route targets the actual owners of the required Iranian region. It does not summon a fresh Persia as a disposable boss.

The middle groups supply artillery, engineers, medical evacuation, winter or difficult-terrain preparation and forward depots appropriate to the selected corridor. A second internal choice selects a bounded occupation settlement with civilian guarantees or a more coercive military administration. The first takes material reconstruction and negotiation. The second mobilizes conquered resources earlier but imposes civic and resistance costs, complicates diplomacy and delays enduring integration.

A negotiated limited victory can end an unsuccessful war and preserve the route, but it is not the full final charter. Completion requires direct Spartan ownership and control of Iran, the Greek and Aegean requirements and the chosen complete corridor. It uses Civic Settlement at least 60 and Military Adaptation at least 75, records `111_milestone_thermopylae_complete` and grants `111_identity_thermopylae_dominion`.

The payoff is a mature eastern expeditionary institution, restored corridor infrastructure, selected regional depots and an administered Iranian settlement. A bounded military-institution specialization can support difficult-terrain operations or long-range supply. Iran does not instantly become a mass of Spartan cores, and symbolic vengeance does not replace postwar government.

Failure can leave an exhausted army on a long frontier. Recovery allows changing the corridor only through a paid strategic revision, retaining valid completed shared states and abandoning the old corridor's exclusive preparation benefits. The player cannot collect both preparations' temporary advantages at once. The AI prefers this route when a credible Persian rival, an attainable corridor and a capable modern army make the campaign coherent.

## 8. The Western Campaign

The route treats southern Italy and Sicily as the first western theatre, with Pyrrhus handled as an Epirote point of inspiration in the research brief. It then confronts Rome and the industrial north. It does not require conquering all Greece first. Laconia must be secure, and Greek port or transit arrangements must be real if the route uses them.

The first fork chooses **southern maritime entry** or an **Adriatic bridgehead**. Maritime entry requires a capable convoy route, escort coverage, transports and an actual landing plan against southern Italy or Sicily. The Adriatic approach requires a real bridgehead and an onward land connection, obtained through diplomacy or war with current owners. Neither focus teleports an army across the sea.

The middle groups secure southern Italian supply, Sicily, Rome and the northern industrial theatre. Rome is a major intermediate political and operational objective, not the finish line while the opposing industrial base remains intact. A defeated Italian government can continue from remaining territory and keeps its actual forces and alliances. Existing global wars and guarantees remain relevant.

The institutional fork chooses **direct western administration** or **Italian regional clients**. Direct administration can exploit repaired industry more reliably after a harder settlement. Regional clients offer local recruitment and lower immediate administrative load, but retain governments and bargain over taxes, basing and participation. Rome's state remains a direct Spartan holding for the final identity. Any optional move of the imperial capital requires a separate peacetime choice and does not invalidate the Laconian origin.

The final set includes Laconia, the complete Italian peninsula, Sicily and Sardinia. It requires the southern, central/northern and two island administration receipts, Civic Settlement at least 60 and Military Adaptation at least 65. It records `111_milestone_west_complete` and grants `111_identity_western_empire`. The reward is access to repaired Italian industrial capacity through completed programs, an integrated amphibious and land-war institution, and a western logistics network.

Post-charter groups can pursue Corsica, North African bases and other named western Mediterranean objectives. They are disclosed optional expansion, not missing pieces of the principal Italian charter. Religious and Mediterranean actors respond through the connection contract when actually present.

Failure focuses on a lost crossing, an isolated bridgehead, hostile air power or a damaged northern economy. Recovery offers evacuation, a different entry plan, a limited peace or a client compromise. It never refunds destroyed ships and soldiers. The AI chooses this route only when it can cross or sustain a real Adriatic approach and when its army can fight the current Italian opposition.

## 9. Hellenic Colonies Reborn

This route builds a network across the Mediterranean and Black Sea. It is deliberately a maritime campaign rather than a land empire with a naval icon. Ports, basin access, convoy supply, repairs, fuel and local agreements determine progress. The nine required selected anchors span five sea regions, so controlling one powerful continental neighbour cannot complete the route by itself.

The opening groups establish a functioning home port, convoy service, escorts and a first Aegean holding. The player then chooses a **sovereign coastal chain** or a **treaty commonwealth**. The former owns every required anchor and bears its occupation costs. The latter must directly own the Aegean anchor and holdings in at least two other sea regions. Remaining anchors can come from explicit coastal charters with actual governments that retain their sovereignty and obligations.

Ordinary docking rights do not count as a charter. A qualifying partner offers a specified port, stable access, agreed convoy or defence duties, local administration and an actual continuing relationship. Sparta supplies its promised protection or industrial service. The partner can refuse, renegotiate or withdraw after a material breach. Where the engine cannot support a proposed lease, the fallback is a supported treaty relationship or direct ownership with truthful map status.

The middle branch has five basin-service groups. Eastern play emphasizes the Cyprus and Egyptian or Cyrenaican chain. Central play confronts Apulia and Sicily. Western play requires the Provence and Catalonian links. Black Sea play requires a northern and southern anchor plus actual access through the straits. These groups open targeted repair, convoy, escort and local-administration programs, rather than five copies of an annexation decision.

A second internal emphasis chooses **concentrated protection** or **distributed commercial service**. Protection uses more fleet concentration and garrison commitment to defend a smaller number of simultaneous operations. Commercial service supports a broader network with civilian-industrial obligations and more vulnerable treaty dependence. Both need real ships and supply. Neither adds a public port currency or a fourth spirit.

Completion uses `111_set_colonies_final`, all five service settlements, Civic Settlement at least 65 and Military Adaptation at least 65. It records `111_milestone_colonies_complete` and grants `111_identity_colonial_commonwealth`, with the sovereignty model reflected in political wording and the exact panel predicate. One shared colonial route flag serves both models. The payoff is a functioning network of regional repairs and depots, improved use of administered ports, mature maritime recruitment and the capacity to sustain distant operations. Local benefits suspend when the relevant port or treaty fails.

Failure can break a basin without destroying the entire route. The player may recover its original port, use an explicitly listed alternative, revise a charter or contract the active network until convoys and escorts recover. A departed partner's flag cannot stay green in the puzzle. The AI requires a credible home fleet and access plan, prefers reachable anchors, and avoids simultaneous expeditions to every basin.

## 10. Enduring charters and postwar play

The proclamation action requires the selected set, all specified regional administrations and the final institutional focus. Territorial and treaty contributions must remain valid for 90 days after their relevant settlement is in force. The action checks Civic Settlement and Military Adaptation, current sovereignty and every material obligation again at confirmation. A capital occupied for one hour cannot produce an enduring empire.

The charter changes the same country's identity, grants the route's actual capstone, records the single completion milestone and permits its major presentation beat. There is no additional reward merely for renaming the country or replaying a scene. The historical completion remains true after a loss. Live bonuses that depend on a lost state, client, port or supply obligation suspend until that requirement is restored and the restoration condition is satisfied.

Postwar integration follows the settlement rules in Part 4. Broad conquered regions do not instantly become cores. State improvements require real facilities and resources. Contemporary recruitment widens through citizenship and administration, while existing native occupation and resistance systems remain relevant. A stable empire, league or maritime network is something the player continues to govern.

The AI evaluates route feasibility from geography, institutions, armed strength, actual opponents and existing relationships. Route preferences are conditional willingness scores until evaluated through the complete installed selection pool. No percentage is claimed here. The implementation handoff must test every route's weak, contested, successful and recovery cases, including absent regional actors, refused human diplomacy, DLC fallbacks and map-set changes.
