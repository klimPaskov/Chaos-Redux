# 012 Africa spec part 9, focus route group packs

This file continues the first-pass focus design. It expands the route groups into implementation-ready packs without defining final focus names, final coordinates, or final player-facing localisation. Every focus label below is a working label, not final localisation.

## Shared opening pack

The shared opening pack gives the selected African-capital country a public continental purpose while forcing it to choose how the continent will be united. The opening should be available to any valid unifier, including small countries, large countries, colonial-release countries, and the RSA civil-war continental side.

| Working anchor label | Role | Unlocks | Idea lifecycle | AI notes | Asset motif |
| --- | --- | --- | --- | --- | --- |
| Continental proclamation | Route opener | Cosmetic identity, initial League value display, early claims as visible ambition | Starts `unfinished_continental_claim` | Always first unless the country is in a civil war emergency | Crowds, flags, continent-scale optimism without map-table framing |
| Survey the frontiers | Intelligence and geography | Regional selector decisions, colonial-state target lists, first integration region preview | Adds survey progress to the opening idea | AI prioritizes before expansion if weak | Surveyors, roads, rail markers, field notebooks |
| Call the local congresses | Legitimacy | Member confidence actions, local support missions | Upgrades opening idea with legitimacy component | AI prefers if stability is above 35 or if not at war | Meeting halls, elders, trade delegates, ballots |
| Raise the League guards | Early defense | Emergency units, defensive intervention missions | Opens mixed military weakness idea mitigation | AI prefers if at war, threatened, or small | Guards at bridges, port sentries, rail depots |
| Choose the unification doctrine | Route lock | Opens the main political route family | Converts the opening idea into the chosen doctrine family | AI evaluates ideology, army strength, member confidence, chaos tier, war state | Seven route emblems shown as non-final working labels |

Opening ideas should not stack as many small spirits. Use one main starting problem with visible components:
- disputed continental mandate
- improvised administration
- limited regional reach
- fragile foreign recognition

The first political route should transform this starting idea rather than add another unrelated permanent spirit.

## Federal Charter route

The Federal Charter route is the peaceful and legalist unification path. It aims to make the Charter League into a voluntary federation where members keep meaningful autonomy for a long time. It should be the best route for avoiding wars with independent African countries, but it should be slower and vulnerable to rival blocs.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Charter convention | Charter signatures, member guarantees, court of arbitration | Hard excludes Continental Command takeover and Deep Green Covenant final branch | Works with Black Star Return and most industry branches | Invite members, guarantee members, settle member disputes | `unfinished_continental_claim` becomes `charter_convention` |
| Federal services | Shared customs, common rail standards, shared health offices | Excludes coercive annexation policy | Improves industry branch and integration missions | Joint construction, aid corridors, regional service projects | `charter_convention` becomes `federal_services` |
| Member parliaments | Member seats, rotating capital, local assemblies | Excludes revolutionary central purge | Helps high-confidence members accept federation | Vote on federation, observer missions, local election support | Adds member confidence floor to the route idea |
| Shared defense | League guards, federal staff college, common reserve | Excludes pure pacifist settlement choices if those exist later | Connects to military branch without turning into junta rule | Raise shared reserves, defend member capitals, escort aid | Adds defense component and reduces intervention cooldown |
| Voluntary union congress | Union vote, ratification tours, federal accession | Excludes forced annexation focus group | Unlocks staged member federation route | Federal accession missions, member autonomy settlement | Final form is `continental_federation_framework` |

### Mutual exclusions and convergence

Federal Charter should be mutually exclusive with:
- the final Continental Command route lock
- the final Revolutionary Congress centralisation branch
- the final Crown of the Continent absolute branch
- the Deep Green Covenant reveal if the player accepts the nonhuman compact as the ruling principle

Federal Charter should remain compatible with:
- Black Star Return
- most Sacred Soil content
- non-coercive regional restoration
- defensive military modernization
- industry and resource branches

### AI route weights

| Situation | Weight guidance |
| --- | --- |
| Democratic or moderate non-aligned unifier, stability above 45, not already at war with African countries | Very high |
| Small unifier with low industry but many possible League members nearby | High |
| RSA continental side after civil war victory, if it avoided mass reprisals | Medium |
| Communist, fascist, or military route already dominant | Low |
| Chaos tier 4 or higher with multiple member refusals and strong rival bloc | Low unless the AI has high legitimacy |
| Player is a neighboring African state with high trust and no war | Slightly higher, because peaceful AI behavior should be legible |

### Asset motifs

Use treaty halls, cloth banners, voting hands, railway workers, port cargo, schools, courts, and regional delegates. Avoid making the route look like a generic office or filing cabinet. Do not make public country names include office-like terms.

## Revolutionary Congress route

The Revolutionary Congress route turns the League into an anti-colonial movement with covert cells, labour networks, and liberation armies. It should be faster against colonizers and harsher toward foreign-backed African governments. It risks lower member confidence among conservative states and can create ideological rivals.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Congress cells | Organize cadres, port unions, mine committees | Hard excludes Crown absolute branch and Federal legalist capstone | Strengthens Black Star Return if diaspora politics align | Fund cells, spread pamphlets, organize strikes | `unfinished_continental_claim` becomes `congress_networks` |
| Liberation army | Depot seizures, border schools, volunteer columns | Excludes pacifist federal settlement | Connects to military branch and colonial war interventions | Seize depots, train cadres, send volunteers | Adds army component and war support |
| People's assemblies | Local councils, land redistribution, wartime congresses | Excludes member parliament route if centralizing | Can integrate low-confidence members by pressure | Hold assemblies, replace collaborator elites | Converts member influence into revolutionary legitimacy |
| Continental social program | Rail labour, clinics, literacy brigades | Excludes crown patronage economy | Connects to industry and resource expansion | Labour drives, state rebuilding, emergency rationing | Adds economic reconstruction component |
| Congress of liberation | Continental congress, anti-colonial war plan, permanent revolution | Excludes voluntary union congress | Unlocks stronger anti-colonial wars and pressure on colonies | War goals against colonial owners, rival ideology suppression | Final form is `continental_liberation_congress` |

### Failure states

The route should not become a free war-goal machine. Repeated covert failures should create:
- member suspicion
- foreign intelligence exposure
- equipment loss
- rival socialist or nationalist blocs
- colonial crackdown missions
- League confidence penalties in conservative or monarchist member states

### AI route weights

| Situation | Weight guidance |
| --- | --- |
| Communist unifier, colonizers control nearby African territory, stability above 35 | Very high |
| High chaos with active colonial wars and strong equipment stockpile | High |
| Democratic unifier with many voluntary members | Low |
| Monarchy or Sacred Soil path already chosen | Very low |
| AI has severe equipment deficit or no land border to colonial targets | Low |
| Player is a colonial owner bordering the route | Higher aggression, but only after preparations |

### Asset motifs

Use print shops, dock workers, rail yards, liberation columns, torn colonial signs, and mass rallies. Avoid final text that turns every revolutionary surface into slogans before localisation research.

## Crown of the Continent route

The Crown route restores continental unity through royal, imperial, and dynastic legitimacy. It can work as a coalition of restored houses or as an absolute imperial project. It should be strong for restored polities and ceremonial legitimacy, but it risks resistance from republican members.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Regalia search | Crown records, sacred stools, palace envoys | Excludes Revolutionary central route | Works with restored polity branch | Search for regalia, invite court claimants | `unfinished_continental_claim` becomes `continental_regalia_claim` |
| House of houses | Royal congress, regional oaths, dynastic arbitration | Excludes Federal member parliament capstone if absolute | Integrates restored kingdoms as members | Restore dynasties, mediate succession, pledge guards | Adds court legitimacy and member obligations |
| Court army | Palace guards, cavalry schools, river standards | Excludes egalitarian militia route | Connects to military branch through elite units | Raise guard units, sponsor horse or camel corps where appropriate | Adds elite unit and command component |
| Crowned federation | Autonomy charters, royal seats, local crowns | Mutually exclusive with absolute empire | Compatible with Federal Charter if chosen as compromise | Royal autonomy treaties, federal crown accession | Final moderate form is `crowned_federation` |
| Continental empire | Imperial roads, direct oaths, regnal proclamation | Excludes Federal Charter and Revolutionary Congress | Strengthens coercive integration and risks revolt | Demand oaths, force succession settlements, annex after refusal | Final hardline form is `continental_empire_claim` |

### Leader-name flavor

The required source-language obscene strings may appear only as strange regnal, court, or council flavor after source review:
- `qaama saalaa koo xuuxaa`
- `haadha kee waliin wal qunnamtii saalaa raawwadhe`

Do not place those strings in file names, tags, sprite names, focus ids, decision ids, or technical identifiers. Do not add more obscene names without source review.

### AI route weights

| Situation | Weight guidance |
| --- | --- |
| Non-aligned monarchy, restored polity origin, high legitimacy | Very high |
| Unifier controls a historic royal capital and has high restored-polity support | High |
| Democratic or communist unifier | Very low |
| Member confidence is high but republican states dominate the League | Medium for crowned federation, low for empire |
| High chaos and many restored polities are active | Medium, with chance to turn absolute if legitimacy is high |

### Asset motifs

Use gold weights, court drums, royal umbrellas, stelae, palace courtyards, ceremonial guards, and carved stools. Do not make restored countries generic monarchies with European crowns as the main motif.

## Continental Command route

The Continental Command route is the military route. It treats the event as a continent-scale emergency that must be directed by a general staff. It can liberate colonies quickly and survive outside wars, but it damages member confidence and can create military occupation resistance.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Emergency staff | General staff, command councils, mobilization law | Excludes Federal legalist capstone | Connects to military and industry branches | Draft command plan, centralize reserves | `unfinished_continental_claim` becomes `emergency_continental_staff` |
| Depot continent | Rail hubs, arsenal belts, truck columns | Compatible with most routes, stronger here | Improves industry and supply integration | Build depots, repair rail, move stockpiles | Adds logistics component |
| War for the colonies | Frontier plans, landing corridors, colonial rear-area raids | Excludes pure diplomacy route | Unlocks anti-colonial war preparation | Ultimatums, war plans, cross-border operations | Adds war-plan component |
| Military governors | Occupation districts, command courts, security zones | Excludes Federal autonomy route | Enables puppet and coercive integration routes | Appoint governors, suppress resistance, create protectorates | Can worsen into `continental_command_state` |
| Command continent | Permanent command, unified staff, emergency union | Excludes voluntary federation capstone | Unlocks late aggressive outside-power response | Emergency annexation, forced integration, outside war plans | Final form is `continental_command_state` |

### Tradeoffs

This route should have high military payoff and high legitimacy cost. It should be able to win wars, but it should not be the easiest path to stable cores. Coercive actions should increase resistance and reduce member confidence.

### AI route weights

| Situation | Weight guidance |
| --- | --- |
| Fascist or military unifier, already at war, army strength above regional average | Very high |
| RSA continental side during civil war | High until civil war victory, then route depends on peace settlement |
| Small unifier with no army and low equipment | Low |
| Federal Charter already advanced | Very low |
| Outside coalition preparing an intervention | Medium to high |
| AI has no supply access to target regions | Low until depot branch is complete |

### Asset motifs

Use African soldiers, rail depots, field radios, ports, repair crews, and military training grounds. Maps can appear as secondary props only.

## Sacred Soil route

The Sacred Soil route is the grounded stewardship route. It uses land restitution, water management, heritage protection, rural legitimacy, and religious or spiritual authority. It should be human, researched, and grounded unless the player pushes into Deep Green Covenant.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Land councils | Customary law, village mediation, soil registers | Excludes hardline revolutionary land seizures | Works with Federal Charter and Crown compromise | Local land settlement, rural legitimacy missions | `unfinished_continental_claim` becomes `land_council_legitimacy` |
| Water and grain | Wells, canals, drought stores, harvest roads | Compatible with industry and integration | Improves resistance outcomes and famine pressure | Build wells, protect harvests, drought relief | Adds rural resilience component |
| Heritage guardians | Sacred sites, manuscript houses, old capitals | Compatible with restored polity branch | Helps restore polities without instant annexation | Protect sites, return relics, cultural mediation | Adds cultural legitimacy |
| Rural defense | Rangers, river guards, forest patrols | Compatible with defensive military branch | Protects member states and reduces disaster pressure | Patrol borders, guard forests, escort grain | Adds local defense component |
| Continental stewardship | Land covenant, regional guardians, restoration congress | Mutually exclusive with full coercive route | Opens peaceful integration and high-chaos reveal hooks | Stewardship integration, conservation missions | Final grounded form is `continental_stewardship` |

### Deep Green transition

Sacred Soil can reveal the Deep Green Covenant only if:
- chaos is high enough
- disaster pressure is already unusual
- the player has used stewardship actions repeatedly
- the route accepts supernatural evidence through an event or hidden focus

The transition must be a choice. A grounded Sacred Soil path should remain available without nonhuman or supernatural content.

### AI route weights

| Situation | Weight guidance |
| --- | --- |
| Non-aligned, rural, low industry, high legitimacy | High |
| Federal Charter route with many small member states | Medium to high |
| Revolutionary or military route already centralizing | Low |
| Disaster pressure and high chaos | Medium, but Deep Green requires rare AI gate |
| AI has active famine or drought related pressure | Higher for water and grain group |

### Asset motifs

Use baobabs, wells, terraces, manuscript chests, holy sites, pastoral scenes, rivers, and caretakers. Avoid caricature, exotic spectacle, or generic tribal imagery.

## Black Star Return route

The Black Star Return route is the diaspora route. It links ports, returnee settlement, cultural diplomacy, industry, and citizenship. It should be powerful when the unifier controls ports and convoys, but vulnerable during naval war and housing shortages.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Call the diaspora | Radio addresses, port agents, citizenship offer | Compatible with most routes | Strengthens Federal, Revolutionary, and industry routes | Open return offices, build diaspora support | `unfinished_continental_claim` can gain `diaspora_invitation` component |
| Black Star lanes | Atlantic convoys, Caribbean offices, cargo schedules | Requires ports and convoys | Connects to naval, industry, and diplomacy branches | Open shipping lanes, escort convoys, insure cargo | Adds convoy and port component |
| Settlement works | Housing, clinics, schools, farm allotments | Excludes mass forced resettlement if designed | Connects to regional integration and industry | Settlement missions, port expansion, local mediation | Upgrades to `returnee_settlement_network` |
| Skilled return | Engineers, teachers, dockworkers, doctors, mechanics | Compatible with all non-xenophobic paths | Boosts industry and research through missions | Skilled mission placements, factory mentoring | Adds skill and production component |
| Continental citizenship | Dual citizenship, cultural diplomacy, returnee service | Excludes exclusionary nationalist branch | Helps federal integration and achievements | Citizenship ratification, cultural missions, diaspora guard | Final form is `continental_citizenship` |

### Failure states

Failures should be visible and recoverable:
- convoy losses reduce return momentum
- housing shortages reduce local support
- ideological disputes reduce member confidence
- foreign surveillance can disrupt lanes
- port blockade can pause the route
- exploit attempts with repeated free manpower should be blocked by settlement capacity

### AI route weights

| Situation | Weight guidance |
| --- | --- |
| Unifier controls at least two useful ports and has convoys | High |
| Democratic, Federal, or Revolutionary route with good stability | High |
| Country is landlocked with no port access | Low until it has transit agreements |
| Major naval war threatens all lanes | Low to medium with escort priority |
| Continental Command route | Medium if manpower is low, otherwise low |
| Deep Green route | Very low unless the route has kept human settlement policy intact |

### Asset motifs

Use ocean liners, cargo manifests without readable generated text, port cranes, family arrivals, workshops, citizenship cards, and Black Star style symbols. The phrase Black Star should be treated as a route motif and should not force final player-facing text without localisation review.

## Deep Green Covenant route

The Deep Green Covenant is the high-chaos nature and nonhuman route. It must not be written as a human African caricature. The actors are explicitly nonhuman, supernatural, animal, or impossible entities. The route is strange and powerful, but it should be dangerous to the unifier as well.

### Route structure

| Focus group | Working anchor labels | Mutual exclusions | Branch interactions | Decision unlocks | Idea lifecycle |
| --- | --- | --- | --- | --- | --- |
| Forest signs | Missing surveyors, impossible tracks, speaking canopy | Requires high chaos or Sacred Soil reveal | Opens hidden high-chaos decisions | Investigate signs, appease forests, mark danger zones | Adds hidden `covenant_pressure` |
| Nonhuman envoys | Gorilla messengers, chimpanzee councils, animal signs | Excludes routes that declare all nonhuman actors enemies | Connects to high-chaos country packages | Recognize nonhuman actor, protect habitat, negotiate passage | Converts pressure into `nonhuman_pact` |
| Wrath of weather | Storm bargains, flood warnings, drought bargains | Excludes ordinary federal legality if abused | Connects to disaster pressure | Demand compliance, avert disaster, unleash wrath with blowback | Adds disaster pressure component |
| Living earth | Stone hosts, river guardians, ancient witnesses | Excludes grounded route closure | Connects to ancient hosts and living-statue actors | Awaken host, bind host, contain host | Adds supernatural army component |
| Covenant continent | Final compact, impossible border, green dominion | Excludes ordinary post-unification capstones | Opens rare high-chaos endgame | Continental pact, nonhuman federation, nature war plans | Final form is `deep_green_covenant` |

### AI restrictions

AI should only choose this route when all are true:
- high chaos threshold is met
- the unifier is not a normal major ally of a human great-power faction
- the route has been revealed by event state
- the AI has a rare high-chaos personality flag or the player has enabled high-chaos AI routes
- the route will not immediately delete required baseline content

### Asset motifs

Use forests, animal silhouettes, storms, living stone, river mist, ancient ruins, and uncanny natural signs. Do not give nonhuman actors human ethnic clothing as the main signifier. Use distinct nonhuman or supernatural visual language.

## Branch convergence

The tree should include convergence groups so that major routes interact instead of becoming isolated columns.

| Convergence group | Eligible routes | Purpose | Decision hooks |
| --- | --- | --- | --- |
| Continental services | Federal, Sacred Soil, Black Star Return, moderate Crown | Build region-wide logistics, schools, clinics, and communications | Regional service projects, settlement support, member confidence recovery |
| Liberation war council | Revolutionary, Continental Command, Federal defensive route | Coordinate anti-colonial wars without instant annexation | Joint war planning, intervention missions, postwar settlement |
| Restored polities congress | Crown, Sacred Soil, Federal, moderate Revolutionary | Restore old polities as members, subjects, or cultural centers | Restoration missions, autonomy negotiations, local guards |
| Port and convoy board | Black Star Return, Federal, Revolutionary, Command | Keep shipping lanes and diaspora missions active | Convoy escorts, port repairs, returnee settlement |
| Scramble response council | Any route after near-unification | Respond to outside great-power pressure | Sanctions response, ultimatums, defense mobilization, diplomacy |
| World-is-one gate | Post-unification routes only | Gate terminal world-end content behind continent unifier interactions | Sponsor continent unifiers, negotiate union, fight continental wars |

Convergence groups should not remove route identity. They should let the player solve shared problems in different styles.
