# Event 6: Independence Wave

## Current source-of-truth correction

Current source-of-truth map: `docs/plans/006_independence_wave_plans/source_of_truth_map.md`.

The 2026-06-05 user correction supersedes earlier Event 006 Kuban (`KUB`) and Altai (`ALT`) package-expansion framing. They are not current requested Event 006 expansions, package carriers, focus overlays, or asset requests unless explicitly reopened later. Because they are vanilla releasable tags, they may still appear as ordinary Independence Wave countries when they pass the same eligibility and host-safety checks as other vanilla non-existing countries.

The active release-pool direction is the generic possible-country base pass. Niche generic, custom, and chaos-only countries belong in a later separate pool when their cores, flags, localisation, and playability package are intentionally wired.

Current wrap-up scope is playable technical completion. Urgent requirements are the release resolver, host survival, origin separation, basic playable tree access, decision usability, current report/news image wiring, and honest docs/audit alignment. Future polish includes additional bespoke package overlays, optional route-specific report/news variants, portraits, animated seals, richer scripted GUI states, and full spreadsheet/catalog polish when implementation facts stop moving.

Base Independence Wave history and release-scale evolution entries must not use a country actor. The event recipient, manual trigger country, and first host that lost land are scopes used by gameplay where needed, not the responsible actor of the wave.

## Core identity

Independence Wave is a minor repeatable event in the Liberations cluster. It is not an Event 005 derivative, not a successor-state event, and not a dependency of any collapse chain. It is a separate random-release system that can happen anywhere in the world when a host state is weak, distracted, overextended, low legitimacy, occupied, colonial, or losing control of peripheral regions.

The base fantasy is simple. A state that looked stable yesterday receives several petitions, local committees, foreign reporter notes, religious appeals, exile letters, mutiny rumors, or municipal declarations. The wave releases several inactive countries immediately after the hidden candidate and host-survival resolver finishes. The petitions, dossiers, and crisis tools are not a delay before independence. They are the explanation and aftermath layer that lets the host, breakaways, majors, and earlier breakaways react to the new facts on the map.

The first wave should release from the generic `every_possible_country` pass: any inactive possible country can enter the base pool. The host-safety resolver then decides whether that candidate has a valid host-owned, controlled, non-protected core state that can be released without erasing the host. These releases should feel plausible. A low-chaos campaign should mostly create defensive, modest states that have a reason to exist in the current map.

Higher chaos changes the scale first. Later work can add custom and chaos-only countries through a separate pool, but the base resolver should not hardcode every releasable tag. At higher tiers, additional researched custom packages can be layered in if the region and chaos state justify them.

The event should never act like a generic release-country button. The important gameplay is the process. The map change comes first. The interesting gameplay is what follows from that sudden shock. A host can mishandle the aftermath. A major power can turn a new state into a client. Earlier breakaways can help the next wave. A new state can seek recognition, build a militia, accept a patron, resist a patron, join a small-state league, demand border districts, or become a strange high-chaos regime.


## Instant release rule

Event 006 is an instant-release event. When the event fires, it chooses one or more valid hosts, scores the release candidates, protects the host survival state, reduces or skips invalid candidates, and then releases the successful countries immediately in the same wave.

Dossiers do not delay independence. A dossier is the release file shown to the host and the world after the map changes. It explains who broke away, why the host was vulnerable, what territory the new country received, what territory was withheld to keep the host alive, who is claiming authority, and what post-release responses are now available.

Host decisions, breakaway decisions, foreign patron actions, recognition missions, loyalist conflicts, scripted GUI boards, and formation routes are aftermath systems. They shape what the new states become. They do not decide whether the visible wave happened, except for hidden resolver validation that runs immediately before the release effect to prevent invalid tags, invalid state transfers, or host deletion.

The player-facing feeling should be sudden. The first report should read as a wave that has already happened: new flags exist, borders changed overnight, ministries are locked out of their former districts, and foreign governments are deciding whether to recognize the new facts.

## Separation from Event 005

Event 006 and Event 005 are separate standalone systems. They may sometimes touch the same region or use the same country tag, but neither event can pull a country into the other event's mechanics by tag name or geography.

Required rule:

- Every country released by Event 006 receives an origin flag or variable such as `chaosx_release_origin = independence_wave`.
- Every country released by Event 005 receives its own origin flag or variable such as `chaosx_release_origin = soviet_collapse`.
- Focus-tree assignment, decision categories, route locks, startup ideas, event details, event logs, formables, GUI entries, and AI behavior must read the origin flag before granting event-specific content.
- If Event 006 releases a Soviet republic style tag, a Russian-region breakaway, a Volga package, a Caucasus package, a Central Asian package, or any other tag that Event 005 can also affect, it remains an Independence Wave country. It must not enter Soviet Collapse missions, republic focus trees, collapse progress, collapse event logs, collapse startup ideas, or Event 005 country package logic.
- If Volga Bulgaria or Old Great Bulgaria appears through Event 005, it uses Event 005 collapse content.
- If Volga Bulgaria or Old Great Bulgaria appears through Event 006, it uses the Independence Wave provisional tree plus the Event 006 Volga historical-return overlay.
- Event 006 must not require Event 005 variables, Event 005 missions, Event 005 focuses, Event 005 progress, Event 005 republic route data, Event 005 event logs, or Event 005 formable logic.
- Event 006 may target a Russian, Soviet, post-Soviet, Ottoman, British, French, Iberian, African, American, Asian, or any other host only because that host satisfies normal Independence Wave targeting rules.

This is important because Event 006 is a general world fragmentation system. It can create the same country identity under a different historical pressure. The tag can be shared. The route must not be shared unless a helper is truly generic and does not bring Event 005 state into Event 006 content.

The implementation must therefore treat origin as the first routing check. If the origin is missing, ambiguous, or from another event, the loader must not guess. It should avoid loading Event 006 package content until the origin is explicit.


## Absolute host survival rule

Event 006 must never fully consume an existing country. Every host that enters an Independence Wave crisis must keep at least one state after the wave resolves. This is absolute at every chaos tier, for every package type, and for every candidate pool.

Implementation rule:

1. Before candidates are released, mark a protected host state.
2. Prefer the host's current capital state as the protected state when the host owns it at resolution.
3. If the host no longer owns its capital at resolution, protect the highest-value remaining owned state using victory points, factories, manpower, supply, and core status.
4. Remove or shrink release candidates until the host still owns the protected state and at least one state total.
5. If a candidate package cannot spawn without taking the protected state or the host's final remaining state, skip that candidate.
6. If the target wave count cannot be reached without deleting the host, release fewer countries.

This rule overrides release count, historical-return ambition, border claims, patron pressure, strange-state pressure, and high-chaos escalation. A host can be reduced to a one-state rump, but Event 006 cannot erase it.

## Campaign experience target

The player should understand the event in three passes.

First pass: ordinary releasables and dormant tags break loose from weak hosts. They are mostly democratic, defensive, low equipment, and focused on recognition.

Second pass: the pattern spreads. More countries release in a wave. Committees learn from earlier successes. Hosts copy suppression methods. Majors learn that guarantees and advisers can buy influence. Earlier breakaways try to help the next wave.

Third pass: independence becomes a weapon. States use the language of self-rule to demand borders, form a league, invite sponsors, refuse sponsors, restore old political names, or create regimes that no normal diplomat can classify.

The best outcome is not always more countries. A host that negotiates well can prevent war. A breakaway that accepts too much help may survive as a puppet. A league can defend small countries but drag them into regional conflict. Harsh suppression can prevent one release while making later releases more radical.

## Catalog and cluster role

| Field | Value |
| --- | --- |
| ID | 6 |
| Event Name | Independence Wave |
| Type | Minor Repeatable |
| Cluster | Liberations |
| Cluster threat | Lowest threat, usually first |
| Details | Several inactive countries begin coordinated independence crises inside weak, unstable, overstretched, colonial, occupied, or wartime hosts. The host receives release dossiers and post-release response decisions as the wave fires. If the crisis succeeds, a wave of countries becomes independent with strength scaled by industry, manpower, depots, foreign aid, previous waves, and chaos tier. Every host keeps at least one state, preferably its capital. Early waves use ordinary HOI4-style releasables. Later waves release more countries and can unlock historical-return, indigenous, local-polity, patron-client, and strange-state packages. |
| Evo I | Committees Learn the Pattern. Batch size rises, non-democratic releases become possible, starting armies become stronger, and earlier breakaways can offer recognition, aid, guarantees, and volunteers. |
| Evo II | The Small States Congress. Released states can coordinate, arbitrate borders, share equipment, send volunteers, form defensive networks, and prepare a formal league. |
| Evo III | Claims Follow the Flag. Released states can demand nearby territory, ask majors to back transfers, issue ultimatums, accept advisers, resist puppeting, or become patron clients. |
| Evo IV | The Old and the Local Return. The release scale expands; later custom-pool work can add researched historical-return countries, indigenous authorities, city leagues, tribal confederacies, and custom tags that need special assets and route overlays. |
| Evo V | The Impossible State. Strange high-chaos releases can appear, including necromantic custodianships, anti-mankind directorates, impossible bureaucracies, and coalitions with other chaos countries. |
| World-End Scenario | No direct world-end branch by default. High-chaos splinter states can feed existing world-threat or strange-state systems only if one becomes strong enough to matter. |

## Event structure at a glance

| Layer | Player-facing meaning | Main actors | Main outputs |
| --- | --- | --- | --- |
| Hidden resolver | The event chooses valid hosts and candidates before the player sees the wave | Event system, with no responsible country actor | Host score, candidate score, protected host state, release count, skipped candidates |
| Immediate release wave | Several new countries appear on the map at once | Host, new breakaways | State transfers, origin flags, startup armies, startup ideas, package type, release dossiers |
| Release dossiers | The world receives files explaining what just happened | Host, breakaways, observers, majors | Dossier cards, grievances, committee types, foreign attention, host anger |
| Aftershock management | Host, breakaways, majors, loyalists, and earlier breakaways react | Host, breakaways, majors, loyalists | Negotiation, suppression, recognition, patron pressure, loyalist crises, border disputes |
| State-building | New states try to survive as actual countries | Breakaways | Focus access, decisions, formation routes, coalition state, event log entries |
| Memory pass | The campaign learns from the wave | Global systems and AI | Future wave weighting, evolution pressure, League cohesion, host precedent |

The hidden resolver is not a playable crisis phase. It is safety logic. The visible event should immediately change the map, then give the player tools to manage the consequences.


## Evolution release scale

The number of released countries must grow with chaos. This is a visible part of the event identity.

Actual Event 006 evolution rows are release-scale tier milestones, not per-country release progressions. Baseline/calm waves can fire and release countries, but they should not record an evolution row. The first evolution row starts no earlier than Dossier Surge, followed by Rising Chaos Release Pattern, Chaos Tier Release Pattern, Great Partition Week, and Open Season. Great Partition Week displays at Chaos Tier, while Open Season is the World Collapse-stage entry displayed at Totalen Chaos.

| State | Typical successful releases | Candidate pool | Army strength | Political risk |
| --- | ---: | --- | --- | --- |
| Baseline | 3 to 5 | Generic `every_possible_country` base pool: inactive possible countries, filtered at release time by host safety and valid releasable core state | Weak militia, few templates, low equipment | Mostly defensive |
| Evo I | 4 to 6 | Same base pool, larger release count | Better militia, limited depots, more trained cadres | Non-democratic chance opens |
| Evo II | 5 to 7 | Same base pool, larger release count | Defensive armies, volunteers, mutual aid | League politics and border arbitration |
| Evo III | 6 to 9 | Claims-based breakaways, patron-backed releases, border protectorates, revived regional identities | Stronger armies, advisers, foreign support | Puppet struggle and limited wars |
| Evo IV | 8 to 12 | Same base pool, larger release count; later custom-pool work can add historical-return and local-polity packages | Mixed. Some fragile, some fanatical or patron-backed | Aggressive claims, legitimacy crises, rare wars |
| Evo V | 10 to 16 | Same base pool, maximum release count; later custom-pool work can add impossible-state and chaos-only packages | Strong or unstable forces with dangerous modifiers | Strange diplomacy, world-threat hooks, containment crises |

The exact count should be weighted by host weakness, number of valid candidates, previous suppressions, foreign attention, chaos tier, and performance constraints. If the valid pool is too small, or if reaching the target would take every state from a host, the event must release fewer countries rather than creating nonsensical tags or deleting an existing country.

## Candidate pool philosophy

## Candidate territory validation

Every candidate must pass a territory validation pass during hidden release validation.

Validation requirements:

- the candidate has at least one valid state to receive
- the candidate does not receive the protected host state
- the candidate does not take the host's final state
- the candidate does not combine with other candidates in the same batch to take every host state
- the candidate has a fallback reduced-state version if its full historical or cultural claim would violate the host survival rule
- the candidate is skipped when no reduced version is valid

Territorial ambition belongs after release through claims, decisions, border commissions, patron pressure, or later wars. Initial release territory must be conservative enough to preserve the host. Even at Evo V, the event can create a hostile or impossible neighbor, but it cannot remove the original country from the map.

Border Commission expansion normally stays inside a released country's cores. Adjacent non-core expansion is a high-chaos league-backed exception, not an ordinary growth path. When a release uses that exception, its original host must receive visible response tools: threaten the overreach, negotiate restraint, and prepare a direct reclamation war goal if the release keeps pressing the claim.

Event 006 uses a ladder, not one flat list.

1. Ordinary countries first. The first pool should prefer countries that already exist in the mod or base game as tags, releasables, dead tags, or game-rule tags.
2. Regional plausibility second. A candidate must have a plausible state cluster, cultural anchor, historical identity, colonial administrative anchor, or campaign-specific reason.
3. Historical-return packages later. Assyria, Mesopotamia, Buganda, Asante, Sokoto, Kanem-Bornu, Mapuche Araucania, Charrua, Guarani, Aymara, Palmares, Darfur, Barotseland, and similar candidates belong to higher chaos unless the mod already contains a practical tag and asset set.
4. Strange packages last. Necromantic, anti-mankind, impossible bureaucracy, and cult-state releases require explicit high-chaos gates.
5. Shared tags are allowed. Shared mechanics are not automatic.

A normal low-chaos wave should not suddenly release Volga Bulgaria, Assyria, Buganda, and Palmares together. A world-collapse wave can.

## Candidate eligibility model

Every candidate should receive a hidden score.

| Factor | Adds score | Subtracts score |
| --- | --- | --- |
| Valid tag or package | existing tag, generated custom tag slot, usable state set | no tag, no assets, no valid state cluster |
| Host weakness | low stability, war, occupation, low manpower, low control, recent capitulation | stable host, high control, no war, high legitimacy |
| Local identity strength | cores, historical region, colonial unit, ethnicity, language, religion, city identity, old polity | arbitrary border, no identity anchor |
| Foreign attention | strategic port, resources, ideological value, border with major | remote region with no sponsor interest |
| Previous waves | nearby breakaways, league help, repeated suppression | no precedent and no communication |
| Chaos tier | high tier unlocks old-state and local-polity packages | low tier blocks niche packages |
| Performance and balance | enough candidates to make a wave coherent | too many tiny tags in one theatre |

Candidate scoring should produce a ranked list. The release batch should draw from the top candidates with some randomness so waves feel alive.

## Regional pressure patterns

### Colonial and overseas holdings

Colonial regions should be fertile ground for ordinary releases. Early waves can release existing colonial or mandate-style countries. Higher waves can reveal local kingdoms, confederacies, protectorates, or indigenous authorities.

Example pressure sources:

- distant overlord at war
- low garrison strength
- ports or resource regions
- exile committees
- missionary or religious networks
- colonial auxiliaries refusing orders
- rival major promising protection

### Borderland and occupied regions

Borderland candidates should appear when host control is weak and a neighboring state or major power might sponsor the committee.

Example pressure sources:

- shared language across a border
- disputed province
- old treaty line
- demilitarized or occupied zone
- puppet dispute
- refugee flow

### Industrial cities and ports

Free cities and port states can appear at medium and high chaos when industrial, commercial, or maritime elites decide that independence is safer than staying with the collapsing host.

Example packages:

- free port
- municipal republic
- merchant council
- foreign-protected city
- syndicalist port commune
- naval base protectorate

### Rail hubs and logistics corridors

Railway sovereignty packages appear when supply collapse becomes political. The state begins as a committee that protects junctions, depots, bridges, or supply timetables.

This package should be rare at low chaos and more common after several waves.

### Old-state memory zones

Historical-return packages are not ordinary nationalism. They are old names returning because chaos has made old maps politically useful again.

Examples:

- Assyria around northern Mesopotamia and the Nineveh or Khabur imagination
- Mesopotamia as a river-state or mandate-era revival in Iraq
- Volga Bulgaria around Volga and Kama identity memory
- Kanem-Bornu around the Lake Chad basin
- Sokoto in northern Nigeria and adjacent Sahel zones
- Asante in the Gold Coast interior
- Buganda around central Uganda
- Barotseland around the upper Zambezi and Lozi institutions
- Mapuche Araucania in southern Chile and Argentina
- Palmares as a quilombo-inspired restoration in Brazil

### Battlefield and grave regions

High-chaos strange packages can spawn from areas with mass death, collapsed administrations, abandoned camps, bombardment, or battlefield contamination. These packages must not use ordinary democratic logic.

### Collapsed capitals and dead administrations

A dead administration can return as an archive-state, emergency directorate, exile cabinet, or impossible bureaucracy. This should require high chaos and a strong narrative reason.

## Host country desirability

The event should prefer hosts that feel capable of losing several regions without the result becoming random map vandalism.

High desirability:

- low stability or low war support
- losing a war
- recently capitulated or restored
- colonial overstretch
- high resistance or low compliance
- many non-core states
- long borders with rivals
- previous harsh suppression
- previous Independence Wave losses
- capital cut off from periphery

Low desirability:

- small country with no valid release pool
- stable state with no internal pressure
- country already destroyed by another world-end chain
- theatre already saturated with too many microstates
- performance danger from another ongoing fragmentation chain

## Host response paths

Host response paths begin after the instant release wave. The host is reacting to lost states, new borders, foreign reporters, loyalist pressure, and the fact that other countries now see the breakaways on the map.

### Recognize the loss

The host accepts that the released country exists and tries to reduce short-term violence. This lowers immediate crisis pressure and foreign condemnation, but creates precedent pressure for later waves. Low-chaos democratic hosts may prefer this if the lost region is low industry and low manpower.

### Negotiate a federal after-settlement

The host offers autonomy-style treaties, trade rights, language rights, demilitarized zones, revenue sharing, or recognition terms after the country has already appeared. Success can prevent war, reduce claims, or create a friendly neighbor. Failure can increase legitimacy for the breakaway because the host publicly admitted the grievance exists.

### Delay recognition and investigate

The host creates commissions, court cases, census disputes, or loyalty checks after the breakaway appears. This buys time and may preserve claims, but raises pressure if repeated.

### Suppress the breakaway aftermath

The host arrests supporters, censors newspapers, deploys troops near the new border, or closes remaining local assemblies. This can weaken a fragile released country, but raises radicalization, foreign attention, and later wave strength.

### Invite loyalist militias

The host arms friendly local groups. This can create a loyalist buffer, but risks civil conflict after release.

### Call a foreign guarantor

The host asks a major to guarantee the existing border. This can scare off weak committees, but gives the major leverage and may turn later negotiations into a patron conflict.

### Trade territory for calm

The host transfers a small district, port, or border zone to avoid full independence. This reduces one crisis but teaches future committees that pressure works.

### Invite foreign observers

Observers reduce suppression credibility and protect elections. They also increase foreign attention.

### Prepare a loyal evacuation

The host moves officials, equipment, trains, gold, archives, or loyal divisions out during hidden release validation. This weakens the new country but can create bitterness and claims.

## Breakaway resolution outcomes

| Outcome | Meaning | Main consequences |
| --- | --- | --- |
| Failed petition | Candidate never releases | Host gains calm, candidate radicalization may persist |
| Autonomy settlement | Region stays inside host with local rights | Pressure reduced, precedent raised |
| Peaceful independence | Candidate releases without war | Legitimacy high, army modest, host anger low |
| Armed independence | Candidate releases with militia and hostile host | Army stronger, war or border conflict possible |
| Patron release | Candidate releases under major influence | Survival easier, patron leverage high |
| Loyalist civil conflict | Candidate releases but loyalists contest it | Civil war or internal crisis branch |
| Border transfer | Candidate gains limited land without full war | Claims logic opens later |
| Impossible release | High-chaos state appears through strange route | Super-event candidate, containment decisions, special tree module |

## Breakaway starting strength

Starting strength must be dynamic and must not be copied from one static template.

Inputs:

- owned factories in released states
- manpower in core states
- military depots or supply hubs
- rail and port access
- host garrison weakness
- foreign aid
- previous wave aid
- suppression intensity
- chaos tier
- ideology route
- package type

Early states should not spawn with absurd armies. High-chaos states can be stronger, but they should pay for it through instability, patron debt, militia politics, strange penalties, or hostile neighbors.

## Country package direction

### Ordinary releasable breakaway

Uses the generic `every_possible_country` base pool. This is the default pool for current baseline and evolution waves. It receives the Liberation Provisional Tree, adjusted by ideology and host relationship.

### Game-rule or formable-compatible breakaway

Uses tags or identities that already exist through HOI4 game rules, focuses, or formables if the mod can safely activate them. The candidate should still pass region and state checks.

### Historical-return package

Uses a researched historical identity. It can reuse an existing tag when appropriate or create a custom tag if needed. It receives the common tree plus a regional overlay.

### Local polity or indigenous authority package

Uses a community, kingdom, confederacy, city, indigenous nation, or protectorate identity. It should not pretend to be a modern nation-state instantly. Its tree should include legitimacy, outside recognition, cultural governance, land settlement, and military survival.

### Border protectorate

Appears when a major power backs independence before the host can suppress it. It receives patron leverage, adviser events, possible puppet pressure, and anti-patron recovery options.

### Free port or free city

Appears in a high-value city, industrial zone, canal area, or port. It receives commercial, diplomatic, and security branches. It has limited expansion unless chaos is high.

### Railway sovereignty

Appears around rail hubs, supply nodes, and logistics corridors. It starts with rail repair and supply control mechanics. At high chaos it can become a rail league or strange timetable-state.

### Necromantic custodianship

Appears from battlefield, grave, camp, plague, or mass-death conditions at very high chaos. It is not a normal country. It uses a special module and should trigger global unease.

### Anti-Mankind Directorate

Appears only at world-collapse levels. It treats statehood as an instrument against humanity and can cooperate with other strange countries.

## Researched high-chaos candidate families

The implementation agent should not treat this table as a mandatory spawn list. It is a research-backed design pool. Each candidate still needs state checks, tag checks, assets, and balance review.

| Family | Candidate examples | Region logic | Chaos gate | Gameplay identity |
| --- | --- | --- | --- | --- |
| Existing vanilla releasables | Catalonia, Galicia, Basque Country, Scotland, Wales, Brittany, Ukraine, Belarus, Kurdistan, Algeria, Morocco, Tunisia, Burma, Vietnam, Indonesia, Nigeria, Angola, Congo variants | Use valid vanilla or modded cores and dead tags | Baseline | Defensive, legitimacy-focused, mostly democratic |
| Americas game-rule tags | Charrua, Guarani, Itza, Maya, Miskito, Nahua, Inuit, Inca, Isthmo-American identities | Only if matching state clusters and game-rule tag support exist | Evo II or higher | Decolonial committee, land congress, protectorate dispute |
| Mesopotamian old-state packages | Assyria, Mesopotamia, Marsh Arab river authority, Mandaean refuge variant, Babylonian symbolic variant | Northern Iraq, Syria, southeast Turkey, southern Iraq marshes, wider river valley | Evo IV or higher | Recognition crisis, river logistics, minority protection, patron pressure |
| Sahel and West African restorations | Sokoto, Kanem-Bornu, Asante, Dahomey if not already a vanilla route, Mossi states, Futa Jallon, Futa Toro | Northern Nigeria, Lake Chad basin, Gold Coast, Bight of Benin, Upper Volta, Senegal and Guinea highlands | Evo IV or higher | Emirate federation, palace council, trade-route revival, colonial border rejection |
| East and Central African kingdoms | Buganda, Bunyoro, Rwanda or Burundi variants, Barotseland, Luba or Lunda references when researched | Uganda, Great Lakes, upper Zambezi, Congo interior | Evo IV or higher | Kabaka or council legitimacy, protectorate treaty dispute, local army and royal guard |
| Southern African local authorities | Zulu restoration, Xhosa council, Basotho mountain state if not already present, Herero authority, Nama authority | Natal, Cape borderlands, Lesotho area, Namibia | Evo IV or higher | Land recovery, mounted or local defense, colonial grievance, prestige and survival |
| South American local and indigenous polities | Mapuche Araucania, Aymara congress, Guarani republic, Charrua revival, Palmares, Muisca cultural state | Southern Chile and Argentina, Andes, Paraguay and adjacent areas, Uruguay, Brazil, Colombia | Evo IV or higher | Land congress, old treaty claims, militia survival, cultural legitimacy |
| Steppe and Caucasus historical packages | Volga Bulgaria, Idel-Ural, Circassia, Mountain Republic, Don, Bukhara, Khiva, Kokand; Kuban only as a superseded historical candidate unless explicitly requested later | Volga-Kama, North Caucasus, Cossack regions, Central Asia | Evo IV or higher | Old-state restoration, cavalry myth, council of elders, sponsor struggle |
| City and infrastructure states | Free Danzig-type city, Shanghai-style municipal emergency, railway republic, canal protectorate, oil port authority | Ports, canals, trade cities, rail hubs, oil zones | Evo II or higher | Commerce, diplomacy, intelligence, foreign guarantees |
| Impossible states | Archive-state, grave census authority, anti-mankind directorate, necromantic custodianship, sealed city | High-death zones, abandoned administrations, contaminated regions | Evo V | Strange mechanics, containment, super-event candidate |

## Example regional chains

### Assyria and Mesopotamia

Assyria should be a high-chaos historical-return package. It should not appear simply because Iraq is weak. It needs a valid northern Mesopotamian state cluster, enough chaos for old identities to return, and a story hook such as minority protection, exile petitions, missionary archives, or regional security collapse.

Mesopotamia should be different. It can be a river-state, mandate-era administrative revival, or federated river valley project. It should focus on Baghdad, Basra, Mosul, river logistics, oil leverage, and British or regional patron pressure if relevant.

### Mapuche Araucania

Mapuche Araucania should not be treated as a normal colonial tag with generic elections. It should use land congresses, treaty memory, mountain and forest defense, Chilean or Argentine host pressure, and possible cross-border claims.

### Sahel old-state wave

Sokoto, Kanem-Bornu, and Darfur should feel like old political worlds resurfacing through clerical, trade-route, palace, emirate, or sultanate legitimacy. They can be defensive at first, but high claim ambition can turn them into regional revisionists.

### South Atlantic and Brazilian interior wave

Palmares should be a quilombo-inspired high-chaos package. It should focus on escaped communities, hidden settlements, plantation resistance memory, forest defense, and recognition struggle. It should not be spawned as a generic Brazil split unless chaos is high enough.

### Volga Bulgaria

Volga Bulgaria and Old Great Bulgaria are allowed in Event 006, but only as high-chaos historical-return packages. Their Event 006 route is not the Event 005 route. In Event 006 they should act like old-state identities revived through Independence Wave logic, with provisional councils, recognition struggle, Volga-Kama consolidation, patron pressure, league politics, and optional steppe myth elements. They must use different focus route names, different decision families, different starting problems, and different formation logic from the Soviet Collapse version.

## Evolution design

### Evo I: Committees Learn the Pattern

The event has fired at least once or chaos has risen. Committees now copy earlier methods.

Unlocks:

- release batch rises to 4 to 6
- non-democratic ideology chance opens
- starting armies improve modestly
- previous breakaways can send equipment or recognition
- host suppression carries stronger future penalties

### Evo II: The Small States Congress

Several breakaways exist or coalition cohesion is high.

Unlocks:

- release batch rises to 5 to 7
- mutual guarantees
- volunteer networks
- shared equipment boards
- border arbitration
- small-state congress decisions
- League of New States preparation

### Evo III: Claims Follow the Flag

Breakaways learn that borders can move.

Unlocks:

- release batch rises to 6 to 9
- territorial demands
- border commission decisions
- protected transfers
- sponsor-backed ultimatums
- limited wars
- stronger nationalist routes

### Evo IV: The Old and the Local Return

The release pool expands beyond ordinary tags.

Unlocks:

- release batch rises to 8 to 12
- historical-return packages
- indigenous authority packages
- city-state and railway packages become more likely
- package-specific focus overlays
- special flags, leaders, advisors, and event text
- stronger army and legitimacy variance

### Evo V: The Impossible State

Statehood becomes a strange weapon.

Unlocks:

- release batch rises to 10 to 16 if performance and valid pools allow it
- necromantic custodianship
- anti-mankind directorate
- impossible bureaucracy
- strange-state cooperation
- super-event candidates
- containment decisions

## Decisions

### Host decision category: Petitions Against the State

Host decisions should let the host respond to each released country and shape the immediate aftermath.

Decision groups:

- open talks
- offer autonomy
- delay with commissions
- arrest committee leaders
- move army to the capital of the candidate region
- flood the airwaves
- arm loyalists
- invite observers
- request a territorial guarantee
- trade a border district
- evacuate archives and depots

### Breakaway decision category: Build the New State

Breakaway decisions begin after the instant release. There is no playable candidate waiting room before independence.

Decision groups:

- request recognition
- seize depot inventory
- form local defense brigades
- call diaspora committees
- convene small-state congress
- demand border parish
- accept advisers
- expose brokers
- hold emergency elections
- impose directorate security rule
- open historical archive claims
- assemble land congress or local council
- activate package-specific legitimacy rituals or institutions

### Major power decision family: Influence the Petitions

Major powers should not always interfere. They should interfere when a candidate has strategic value.

Decision groups:

- send observers
- fund committee newspapers
- supply rifles through a port
- offer recognition pledge
- demand a patron cabinet
- threaten the host
- guarantee the host border
- broker an autonomy settlement
- sabotage a rival patron

## Foreign power behavior

Major powers should decide based on ideology, rivalries, resources, strategic access, and threat perception.

Examples:

- A naval power cares about ports, canals, and islands.
- A continental power cares about border buffers.
- A communist power may support revolutionary committees.
- A fascist power may support nationalist directorates or protectorates.
- A democratic power may support observer elections and recognition.
- A colonial empire may oppose the wave unless using it against a rival.

## Coalition and League of New States

The coalition path gives repeated waves memory.

### Informal cooperation

Earlier breakaways can send recognition, small arms, staff officers, volunteers, or political advice. This creates coalition cohesion.

### Small States Congress

When enough breakaways exist, they can convene a congress. It should unlock arbitration, mutual aid, and foreign-policy coordination.

### League Charter

If cohesion is high and patron leverage is low, the congress can become a faction. This should be a major moment and a super-event candidate.

### League failure

The league can fail if members accept rival patrons, fight over claims, or radicalize into incompatible ideologies.

## Border dispute system

Border disputes should be warnings before wars. A breakaway with high claim ambition can demand a district, port, resource state, old capital, religious site, rail junction, or treaty line.

Outcomes:

- arbitration success
- protected transfer
- host refusal
- limited border war
- sponsor-backed ultimatum
- league intervention
- claim frozen by observers

## Patron leverage and puppet struggle

A patron can save a breakaway and hollow it out. Patron leverage should rise from loans, advisers, guarantees, emergency rescue, arms shipments, or intelligence help. It should fall from domestic legitimacy, league protection, broker exposure, elections, debt refusal, and rival diplomacy.

High patron leverage unlocks:

- patron cabinet route
- puppet drift
- military mission dominance
- forced base rights
- export concessions
- anti-patron crisis

## Internal conflict and loyalists

A host that arms loyalists creates future danger. The new country can inherit hostile militias, governors, police, officers, clergy, merchants, or party machines.

Possible outcomes:

- loyalist sabotage
- capital street fighting
- cabinet collapse
- border fortress handover
- officer coup
- exile host government
- civil conflict branch

## Ideological route behavior

### Democratic and civic route

Builds legitimacy, recognition, observers, elections, civil rights, and league diplomacy. Good at surviving without a patron.

### Military emergency route

Builds army, depot control, officer staff, martial law, and defensive belt. Good in hostile borders, but risks permanent authoritarian rule.

### Revolutionary route

Builds militias, workshops, purges of old police, volunteers, and ideological sponsors. Strong if radicalization is high.

### National directorate route

Builds claims, youth battalions, border memory, and emergency propaganda. Strong in high claim ambition, dangerous for regional peace.

### Patron cabinet route

Builds foreign loans, advisers, recognition, and military missions. Strong for survival, dangerous for autonomy.

### Historical-return route

Builds legitimacy from old institutions, archives, councils, treaty memory, rulers, religious authorities, trade routes, or cultural congresses. It must be specific to the package.

### Strange routes

Require high chaos and special conditions. They should feel like state mechanics breaking down, not ordinary ideology switching.

## High-chaos branch direction

### Historical-return packages

The country starts with a provisional modern emergency government but receives old-state language, old symbols, contested legitimacy, and regional claims.

### Local and indigenous packages

The country starts with land councils, tribal or community assemblies, protectorate disputes, recognition problems, and survival needs. The route should not flatten different regions into one generic indigenous tag.

### Necromantic custodianship

The state counts graves, dead districts, and abandoned archives. It should gain manpower or compliance in horrifying ways while alarming every ordinary country.

### Anti-Mankind Directorate

The state is openly hostile to human political order. It should have few friends, strange allies, and strong containment pressure.

### Strange-state cooperation

If several strange states exist, they can share impossible diplomacy, containment evasion, and world-threat hooks.

## Player roles

### Host player

The host must have real tools. The player can negotiate, suppress, decentralize, trade territory, invite observers, ask for guarantees, or prepare evacuation. None of these should be free.

### Breakaway player

The breakaway must feel playable immediately. The player needs recognition, legitimacy, army, budget, route choices, and a clear path away from fragility.

### Major player

The major can support, coerce, guarantee, puppet, sabotage, or observe. A major should not get free countries without long-term consequences.

### Previous breakaway player

The previous breakaway can build coalition cohesion and help new committees. This should make the event feel cumulative.

### Strange-state player

The strange-state player can exploit high-chaos release logic, but should face containment and fear.

## Event and popup moments

Required popup families:

- first release dossier appears
- host response chosen
- foreign observers arrive
- suppression succeeds or fails
- peaceful independence
- armed independence
- patron-backed release
- loyalist conflict
- border demand warning
- small-state congress
- league formation
- historical-return reveal
- local-polity reveal
- impossible-state reveal

## AI strategy matrix

| Actor | Low chaos | Mid chaos | High chaos |
| --- | --- | --- | --- |
| Democratic host | negotiate, autonomy, observers | negotiate plus selective concessions | may trade territory to prevent war |
| Fascist host | suppress, loyalists, propaganda | suppress plus patron guarantee | harsh suppression, high radicalization |
| Communist host | autonomy or ideological co-option | sponsor friendly committees | purge hostile committees |
| Neutral authoritarian host | delay, arrests, army deployment | protectorate bargaining | evacuation and loyalist arming |
| Democratic breakaway | elections, recognition, league | arbitration and guarantees | anti-patron and survival |
| Revolutionary breakaway | militia, workshops, purges | sponsor alignment | export volunteers |
| Nationalist breakaway | army, claims, border memory | ultimatums | regional wars |
| Patron major | observers and recognition | advisers and loans | puppet pressure |
| Earlier breakaway | recognition and aid | congress and volunteers | league or rival bloc |
| Strange state | unavailable | rare warning behavior | containment evasion and strange coalition |

## Super-event use

The base event should not get a super-event. Super-events are reserved for:

- First League of New States
- First historical-return wave with enough global weight
- First Impossible State
- The Great Partition Week if a very high-chaos wave releases many countries at once
- A regional war caused by Independence Wave claims if it becomes a major conflict

## Connections with existing systems

Event 006 connects to general Chaos Redux systems through:

- Chaos Meter
- event clusters
- evolutions
- event log
- event details
- condemnation if suppression reveals atrocities
- deaths tracker if suppression, civil conflict, or strange routes kill civilians
- wars and factions
- achievements
- asset pipeline

Event 006 does not connect to Event 005 as a prerequisite or dependency. Any reference to Event 005 must be limited to origin safety, shared utility cleanup, or preventing duplicate content if the same tag already exists. It must never make an Event 006 release part of the Soviet Collapse system.

## Focus tree handoff

The focus tree file must stay route-level. It should not map every final focus individually. The implementation agent should build the exact focus count and layout from the route architecture, package overlays, and route locks.

## Implementation-sensitive notes

- Use event-origin flags for released countries.
- Use central scripted effects for candidate scoring and batch release.
- Avoid daily or weekly world polling.
- Cache candidate lists during the dossier phase.
- Use hidden variables for candidate tier, host response, pressure, legitimacy, radicalization, patron leverage, coalition cohesion, and package type.
- Use package overlays for historical-return and local-polity content.
- Do not give Soviet Collapse focuses, missions, startup ideas, event logs, or formable routes to any Event 006 country. This includes Soviet republic style tags, Volga Bulgaria, Old Great Bulgaria, and other shared tags.
- Do not create niche custom tags before verifying state ownership, cores or scripted cores, assets, leaders, and localization.

## Required implementation files

Expected implementation surfaces:

- `events/006_independence_wave.txt`
- `common/decisions/chaosx_independence_wave_decisions.txt`
- `common/national_focus/chaosx_independence_wave_focus.txt`
- `common/ideas/chaosx_independence_wave_ideas.txt`
- `common/scripted_effects/chaosx_independence_wave_effects.txt`
- `common/scripted_triggers/chaosx_independence_wave_triggers.txt`
- `common/script_values/chaosx_independence_wave_values.txt`
- `common/ai_strategy_plans/chaosx_independence_wave_ai.txt`
- `common/country_tags` updates for any custom tags that are not already present
- `common/cosmetic_tags` updates for package variants
- localisation files
- event detail docs
- event log wiring
- catalog spreadsheet update
- asset manifests

## Open design limits

The coding agent should not implement every historical package at once if tag and asset support is missing. It should implement the generic framework, ordinary releasable pool, a safe researched starter set, and clear extension points. The report must list which high-chaos packages are implemented, which are stubbed as data-only candidates, and which need more assets or state mapping.


## Expanded wave lifecycle

The wave should play as a sudden map shock followed by a living aftermath. The same structure applies to a tiny colonial breakaway, a city-state, or a high-chaos old-name return. Only the scale and the candidate pool change.

| Phase | Player-facing event | Hidden work | Main failure case | Result if successful |
| --- | --- | --- | --- | --- |
| Candidate pulse | No popup yet | Build candidate pool, reserve host survival state, score host weakness | No valid host or candidate | Event quietly delays and tries later |
| Host survival validation | No popup yet | Remove or shrink candidates that would delete the host | All candidates fail validation | Wave cancels or releases fewer countries |
| Immediate release | New countries appear on the map at once | Set origin flags, transfer valid states, assign startup packages | Invalid tag or missing package support | Candidate skipped before the visible release effect |
| Release dossier report | Player sees why the wave happened | Write dossier cards, event log entry, package type, host anger, foreign attention | Too many dossiers for one popup | Grouped report and details UI |
| Aftershock management | Host and breakaways respond through decisions, missions, and GUI | Apply recognition, suppression, patronage, loyalist, and coalition mechanics | Host ignores the new map reality | Radicalization, border anger, and patron leverage rise |
| State-building | New states build governments and ask for recognition | Assign focus tree, overlay, startup ideas, army, stockpiles, claims, decisions | New country has limited supported content | Emergency subset and generic provisional tree |
| Memory pass | Other countries learn the pattern | Update future wave values, AI memory, event log, candidate weights | Too many active breakaways | Future releases throttle until the map stabilizes |

A wave is allowed to release fewer countries than its target if host survival, tag validity, state overlap, or performance limits require it. That reduction happens in hidden validation before the visible release effect. The visible event still presents the successful wave as immediate.


## Dossier content standard

Every release dossier needs enough identity to make the instant release feel understandable. A dossier can be short, but it must contain these elements.

| Dossier field | Required design answer | Example content direction |
| --- | --- | --- |
| Candidate name | Which country or package is organizing | Scotland, Syria, Assyria, Mapuche Araucania, Barotseland |
| Host grievance | Why the host is losing legitimacy here | wartime requisitions, colonial taxation, ignored autonomy, broken treaty, closed assembly |
| Committee type | Who speaks for the movement | municipal council, exile office, tribal congress, clergy, officers, workers, archive committee |
| Immediate demand | What they ask before independence | autonomy, observers, a plebiscite, recognition talks, relief of garrison, release of prisoners |
| Risk sign | Why this may escalate | mutinous depot, armed loyalists, foreign reporters, patron promise, old-state documents |
| Host choice hook | Which host decisions matter most | negotiate, suppress, trade, invite observers, arm loyalists, evacuate archives |

The first player-facing event should mention only a few newly released countries by name when the batch is large. Use a report event or follow-up detail panel for the full list. A high-chaos wave with twelve candidates should not create twelve separate popups unless the player opens details.

## Candidate scoring model

Candidate selection should be dynamic and weighted, not a hardcoded list in one order. The event builds a pool, scores candidates, validates host survival, then resolves the wave.

| Score factor | Ordinary releasable | Dormant or game-rule tag | Historical-return package | Local-polity package | Strange package |
| --- | --- | --- | --- | --- | --- |
| Host weakness | high value | high value | medium value | high value if colonial | medium value |
| War or occupation | high value | medium value | medium value | high value | high value |
| Existing cores | mandatory or near mandatory | important | helpful but not mandatory | helpful | not mandatory |
| Cultural or historical plausibility | basic region fit | required | required | required | symbolic or anomaly fit |
| Foreign attention | medium value | high value | medium value | medium value | low value unless fear route |
| Prior wave nearby | high value | high value | medium value | high value | medium value |
| High chaos | small value | medium value | mandatory | mandatory | mandatory |
| Host survival safety | mandatory | mandatory | mandatory | mandatory | mandatory |

A candidate that scores well but fails the host-survival pass must be reduced before it is skipped. A one-state release is acceptable when the country can grow later through focuses, decisions, claims, settlement talks, or border wars.

## Candidate reduction rules

Candidate reduction keeps the wave from deleting hosts and from creating oversized releases.

1. Prefer releasing states that are already cores of the candidate.
2. Prefer contiguous state groups.
3. Prefer states with the candidate's cultural, historical, colonial, or administrative argument.
4. Prefer states away from the protected host state.
5. Prefer leaving the host with its capital, largest victory point, strongest industry state, or supply center.
6. If the candidate has a historical capital that is also the protected host state, release a foothold and give a claim or later border mission instead.
7. If a candidate can only exist by consuming the host, the candidate is invalid for Event 006.

Reduced releases are not failures. They should receive a small-state emergency subset, a claim ledger, and a path to ask for arbitration or future revision. This makes the host-survival rule visible as gameplay rather than a hidden nerf.

## Regional wave archetypes

The event should mix ordinary releases and high-chaos packages by region. The table below is a design map for candidate flavor, not a fixed batch order.

| Region | Low-chaos pattern | Mid-chaos pattern | High-chaos pattern | Common host response |
| --- | --- | --- | --- | --- |
| British Isles | known releasables, island autonomy, city pressure | patron-backed protectorates and neutral ports | old county leagues or maritime city councils | negotiate or delay |
| Iberia | regional releasables and colonial ports | municipal republics, island committees, border commissions | local crowns, old charters, Atlantic free ports | suppress or trade |
| France and Low Countries | occupied-border committees and port cities | rival patron missions and military governors | revived communes, old duchy overlays, archive states | invite observers or suppress |
| Balkans | ordinary releasables and borderland claims | mutually guaranteeing small states | church-backed old polities and mountain leagues | foreign guarantee or suppression |
| Anatolia and Levant | dormant tags, minority committees, mandate memories | Assyria, Mesopotamia, Armenian or Kurdish-adjacent claims if valid | archive states and treaty ghosts | suppress or patron bargain |
| North Africa | colonial committees and port protectorates | tribal congresses and rail sovereignties | emirates, desert confederacies, old urban republics | delay, army, or trade |
| West Africa | colonial and administrative breakaways | Asante, Sokoto, Dahomey-like, Futa or river polities if supported | old-state restorations and land congress routes | suppress or foreign observers |
| Central Africa | colonial districts and rail corridors | kingdom and lake-region packages | Kongo-related, Luba-related, or impossible archive polities if supported | loyalists or foreign guarantee |
| East Africa | colonial administrations and ports | Buganda, coastal protectorates, highland councils | lake kingdoms and religious return states | negotiate or patron cabinet |
| Southern Africa | ordinary releasables and protectorates | Zulu, Barotseland, Herero, Nama, rail or port breakaways | grave-route memory states and land congresses | suppress or trade |
| South America | ordinary releasables and border regions | Aymara, Guarani, Charrua, Mapuche, city leagues | Palmares, revived confederacies, land congress states | suppress, observer, or autonomy |
| Central Asia | ordinary releasables and steppe administrations | Bukhara, Khiva, Kokand overlays if tags exist | archive khanates, caravan states, Sufi councils | suppress or patron bargain |
| Caucasus and Volga | ordinary releasables and mountain districts | Circassia, Mountain Republic logic, Volga Bulgaria | old-state memory and border revision crisis | army, loyalists, or settlement |
| Southeast Asia | colonial districts and port cities | sultanates, hill confederacies, river protectorates | palace archive or monsoon-state packages | foreign guarantor or trade |
| Pacific and Arctic | small releasables, island administrations | naval protectorates and radio stations | impossible weather states only at extreme chaos | delay or ignore |

## Country package integration rules

The package files define exact identity rules, but the main spec needs these global constraints.

| Rule | Design reason |
| --- | --- |
| Ordinary tags dominate early waves | The first event must teach the mechanic with recognizable states |
| Historical-return packages need region fit | Old names should feel tied to place, archives, memory, and institutions |
| Local-polity packages need a land or community argument | They should not appear as random fantasy tags |
| Strange packages need prior crisis pressure | They should feel like a mutation of the independence mechanic |
| Shared tags must read release origin | The same tag can use different content in Event 005 and Event 006 |
| Host survival overrides everything | Existing countries always survive the wave |

## Ordinary releasable behavior

Ordinary releasables should not feel shallow. Even if they use the shared tree, their starting dossier should reflect region, host type, and crisis cause.

Examples:

| Host condition | Ordinary releasable tone | Startup modifier direction |
| --- | --- | --- |
| Host is at war | emergency provisional council, depot seizure, border guard | more militia, less stability, higher host anger |
| Host is colonial | petition to end distant rule, local assembly, tax strike | more legitimacy, lower equipment, higher foreign attention |
| Host is occupied | underground committee, liberation administration, disputed protector | high recognition risk, possible foreign guarantee |
| Host has low stability | civil officials defect, local police refuse orders | moderate militia, weak economy, high loyalist risk |
| Host is a major | press attention and diplomatic fear | more foreign attention, harder recognition |
| Host has suppressed earlier waves | radical committees and martyred petitioners | high radicalization, stronger militia, worse future settlement |

## High-chaos candidate families by research anchor

These candidates are design targets for Evo IV and Evo V. The implementation agent should create only packages that can be supported by states, tags, assets, and reasonable testing.

| Family | Research anchor | Region logic | Suggested package type | Tree overlay theme |
| --- | --- | --- | --- | --- |
| Assyria | northern Mesopotamia and modern Assyrian communities | northern Iraq, southeastern Turkey, northeast Syria, northwest Iran if map supports | historical-return | church, language, diaspora, Nineveh plain defense, modern compromise |
| Mesopotamia | Tigris and Euphrates river region and mandate memory | Iraq core, Syria or Turkish border only if valid | historical-return or mandate-city package | river administration, royal dilemma, Arab civic route, ancient name risk |
| Mapuche Araucania | Mapuche history and Araucania memory | south-central Chile, Andean borderlands if supported | local-polity or historical-return | land congress, community defense, modern treaty path |
| Aymara | Altiplano and Lake Titicaca region | Bolivia, Peru, northern Chile if valid | local-polity | highland congress, lake routes, mining pressure |
| Guarani | eastern Paraguay, Brazil, Argentina, and language identity | Paraguay and nearby border states if valid | local-polity | language schools, forest communities, river route |
| Charrua | Rio de la Plata grasslands | Uruguay and adjacent Argentina or Brazil states if supported | local-polity | memory recovery, mobile defense, recognition by neighbors |
| Palmares | Quilombo dos Palmares and Afro-Brazilian resistance | northeastern Brazil if valid | historical-return or local-polity | maroon republic, fortified settlements, autonomy bargain |
| Buganda | kabaka, Lake Victoria, and kingdom identity | Uganda region if valid | historical-return | kabaka question, Lukiko-style council, protectorate memory |
| Asante | Kumasi and Akan political memory | southern Ghana if valid | historical-return | Golden Stool symbolism, council route, modern federation |
| Sokoto | Fulani jihad and northern Nigerian emirates | northern Nigeria, Niger, Cameroon border if supported | historical-return | emirate federation, scholar councils, border restraint |
| Kanem-Bornu | Lake Chad trading empire | Chad, Nigeria, Niger, Cameroon border region | historical-return | lake trade, mai restoration, caravan guard |
| Darfur | sultanate and western Sudan regional identity | Darfur states if map supports | historical-return | sultanate council, desert militia, humanitarian route |
| Barotseland | Lozi and Zambezi floodplain institutions | western Zambia if valid | local-polity or historical-return | floodplain governance, treaty memory, autonomy settlement |
| Zulu | Zululand and Shaka-era state memory | Natal or Zululand area if supported | historical-return | royal council, regiment memory, modern constitutional path |
| Herero and Nama | Namibian colonial violence and pastoral societies | central and southern Namibia if valid | local-polity | land return, cattle route, grave memory, anti-colonial route |
| Volga Bulgaria | Bulgar and Volga-Kama memory | Volga region only if valid and host survives | historical-return | Islam, trade river, archive legitimacy, Event 006 only overlay |
| Circassia | Circassian and Cherkessia region | northwest Caucasus if valid | historical-return or local-polity | exile memory, mountain defense, Black Sea diplomacy |
| Mountain Republic | North Caucasus confederation logic | multi-state Caucasus only if host survives | historical-return | mountain congress, federal arbitration, militia belts |
| Bukhara | oasis city and emirate memory | Central Asia around Bukhara if state support exists | historical-return | oasis council, emirate compromise, reformist path |
| Khiva | Khwarezm and khanate memory | lower Amu Darya and Khiva region if supported | historical-return | caravan customs, canal defense, protectorate memory |
| Kokand | Fergana valley and khanate memory | Fergana region if supported | historical-return | valley assembly, trade routes, mountain border claims |

The spec should not imply that every entry must be implemented immediately. The implementation target is a deep package ladder and enough concrete examples that future waves can be expanded without redesigning the system.

## Crisis event families

The event chain should include repeatable families rather than one-off popups.

| Event family | Main audience | Trigger direction | Choice design |
| --- | --- | --- | --- |
| Petition arrives | host | dossier formed | negotiate, delay, suppress, invite observers |
| Committee splits | candidate or host | radicalization and legitimacy diverge | civic faction gains, officers intervene, patron brokers appear |
| Reporters cross the border | host and majors | foreign attention high | tolerate observers or risk legitimacy loss |
| Loyalists organize | host | suppression or loyalist decision used | arm loyalists or keep them disbanded |
| Depot ledger missing | candidate and host | militia strength high or depot seizure | candidate arms up, host raids, foreign brokers assist |
| Patron telegram | major and candidate | foreign attention plus strategic value | recognition, advisers, cabinet seats, rival sabotage |
| Settlement table | host and candidate | negotiation succeeds | autonomy, reduced release, peaceful release, border trade |
| Resolution week | all relevant actors | candidate resolves | release, settlement, civil conflict, failed petition |
| First assembly | new country | country appears | route hint, startup decisions, tree assignment |
| Old archive opened | high-chaos candidate | historical-return eligible | modern compromise or old-name escalation |
| Land congress meets | local-polity candidate | local package eligible | autonomy, statehood, land defense, patron refusal |
| Strange dossier sealed | Evo V | occult or impossible pressure high | hidden branch, containment, super-event if first reveal |

## Statehood quality bands

New states should begin with a readable condition, not a generic set of buffs.

| Band | Conditions | Starting feel | Typical startup idea |
| --- | --- | --- | --- |
| Petition state | low pressure, high negotiation | weak but legitimate | Petition Government |
| Emergency state | host war, depot seizure, low stability | armed and unstable | Emergency Council |
| Recognized provisional state | observers, foreign attention, peaceful settlement | fragile but credible | International Observers |
| Patron cabinet | foreign aid, high leverage | safer but compromised | Sponsored Cabinet |
| Loyalist-split state | suppression and local loyalists | internal conflict | Divided Barracks |
| Old-name return | high chaos, archive, historical-return | symbolic and contested | Restored Name, Modern Problem |
| Land congress state | local-polity and community backing | local legitimacy, low industry | Land Congress Mandate |
| Strange state | Evo V and hidden pressure | rule-breaking statecraft | Sealed Dossier State |

Each band should control starting decisions, focus visibility, AI route bias, and first event text.

## Release count pacing

Higher evolution tiers raise the target release count, but the actual number should still feel tied to validation and map pressure.

| Tier | Target count | Normal cap behavior | Failure behavior |
| --- | --- | --- | --- |
| Baseline | 3 to 5 | ordinary tags only unless no ordinary candidates exist | shrink to 1 or 2 only when host survival blocks the rest |
| Evo I | 4 to 6 | mix ordinary and dormant tags | fall back to ordinary tags |
| Evo II | 5 to 7 | congress and dormant tags more common | delay league behavior if fewer than 3 survive |
| Evo III | 6 to 9 | protectorates, cities, territorial claims | reduce claims before reducing releases |
| Evo IV | 8 to 12 | historical-return and local-polity packages | no old-name package if state support is bad |
| Evo V | 10 to 16 | strange packages can appear | throttle if too many active new states or wars exist |

A smaller validated wave is better than a large broken wave.

## Host survival visibility

The absolute host-survival rule should be visible through outcomes.

Examples:

| Situation | Hidden validation result | Player-facing explanation |
| --- | --- | --- |
| Candidate would take the capital | candidate shrinks | committee accepts a foothold while claiming the capital later |
| Two candidates overlap | lower-score candidate loses a state | arbitration table removes one district from the dossier |
| Host has only two states | only one candidate can release | emergency government keeps the capital and loses the periphery |
| High-chaos package wants a full old kingdom | release starts as archive state or rump state | old documents claim more than the committee can hold |
| Patron tries to carve a port and inland state | port may release, inland state delayed | guarantor accepts naval foothold first |

The rule should never be explained as a technical limitation. It is the political fact that even in a wave, some state apparatus survives.

## Major power interpretation

Major powers should read the event through their interests.

| Major type | Interpretation | Likely action |
| --- | --- | --- |
| Democratic major | self-determination, observers, legal recognition | recognize, mediate, guarantee small states if low risk |
| Fascist major | useful fragmentation, anti-rival wedge | send advisers, demand cabinet seats, sponsor national directorates |
| Communist major | popular committees, anti-colonial movements | support revolutionary committees, send volunteers, oppose patron puppets |
| Non-aligned empire | precedent danger, imperial balance | suppress at home, sponsor abroad when useful |
| Isolated major | map noise unless strategic resource or border | ignore or send limited supplies |
| Major already at war | proxy opportunity or distraction | arm committees behind enemy lines, avoid formal recognition |

Major aid must raise patron leverage. Free help should be rare.

## High-chaos philosophy

High chaos should not simply mean stranger names. It should alter how independence is justified.

| High-chaos mode | Statehood claim | Gameplay expression |
| --- | --- | --- |
| Old-name return | archives, graves, dynastic memory, religious institutions, old maps | historical-return overlay, claims, legitimacy disputes |
| Local-polity return | land congress, community law, protectorate memory, clan or kingdom institution | land congress decisions, local defense, autonomy bargains |
| Archive-state | a bureaucracy survives its own country | paperwork decisions, recognition paradoxes, hidden claims |
| Necromantic custodianship | the dead are counted as political members | grave census, manpower distortions, moral panic |
| Anti-Mankind directorate | independence from humanity as a legal category | diplomatic isolation, terror pressure, strange-state cooperation |
| Railway sovereignty | logistics claims statehood | supply-route decisions, rail defense, hub politics |

The player should be able to tell which logic produced the country by reading its first events, decisions, and tree overlay.

## Event log and details entries

Every significant wave should create event log data.

| Log item | Required content |
| --- | --- |
| Wave opened | no country actor, candidate count, main pressure reason, chaos tier |
| Host response | main path chosen, cost paid, suppression or settlement memory |
| Release week | actual release count, skipped candidates, survival state preserved |
| First patron | patron country, target country, leverage type |
| First congress | participating countries, cohesion value, league risk |
| First historical return | package name, origin flag, host, source region |
| First strange state | package type, reveal level, super-event lock |
| Host reduced to rump | host name, protected state reason, number of states lost |

Do not create an evolution log entry for ordinary dossier stages. Only actual evolution milestones or major unlocks should use the evolution pipeline.

## Failure and containment outcomes

Not every dossier should release a country. Failure outcomes make the event less predictable.

| Outcome | Trigger direction | Consequence |
| --- | --- | --- |
| Petition buried | pressure low, host delayed effectively | candidate removed, host pays political and stability cost |
| Autonomy settlement | negotiation succeeds | no release, but future pressure lower and host grants autonomy spirit |
| Peaceful release | legitimacy high, host accepts | low radicalization, fewer claims, better recognition |
| Violent release | host suppresses and fails | stronger army, worse stability, loyalist conflict risk |
| Patron release | major intervenes | stronger startup, puppet risk, rival patron events |
| Civil split | loyalists armed and committee radicalized | released tag starts at war or with internal mission |
| Candidate skipped | host-survival validation fails | wave count reduces, dossier note says capital district remained under host control |
| Foreign bargain | host trades one state and gets guarantee | smaller release, host survival and future diplomacy improved |

## Documentation handoff additions

The implementation should create or update documentation that explains the event as a player-facing system.

Required documentation pages or sections:

- `docs/events/006_independence_wave.md` with lifecycle, evolutions, host survival rule, and release-origin separation
- a package table that lists implemented country packages and their gates
- a focus tree route table that states the tree is architecture-driven and not a fixed sample list
- a decisions table with category lifecycle and cleanup conditions
- an asset manifest summary with source or generated mode for each asset group
- a super-event summary only for evolved moments that actually got wired
- a validation note confirming no Event 006 release can delete a host

## Implementation risks to design around

| Risk | Why it matters | Required design guard |
| --- | --- | --- |
| Candidate pool becomes too broad | random old names feel fake | require region fit, chaos gate, package type, and state support |
| Event 006 borrows Event 005 behavior | shared tags become confusing | origin flag controls all content |
| Focus tree becomes flat | new states feel identical | branch interaction, overlays, route locks, and AI behavior |
| Decisions become passive buttons | player has no crisis management | timed missions, real sacrifices, map goals, and pressure systems |
| Host gets deleted | user explicitly forbids it | protected state validation with no exceptions |
| Too many popups | high-chaos waves become annoying | grouped dossier reports and details UI |
| Too much polling | performance suffers | batch calculations at event moments only |
| High chaos overwhelms low chaos | early event loses identity | ladder gates by evolution and chaos tier |

## Research source notes for implementers

Use reliable historical sources during asset and localisation work. The design anchors below are sufficient to justify package families, but implementation still needs state checks, tag support, and asset review.

| Topic | Recommended source family | Design use |
| --- | --- | --- |
| HOI4 releasables and generated tags | Hearts of Iron 4 Wiki | ordinary and dormant pool framing |
| Assyria and Assyrian identity | Britannica Assyria and Assyrian pages | Assyria package and Nineveh-related route language |
| Mesopotamia and Iraq mandate memory | Britannica Mesopotamia, Iraq, and Faisal I pages | Mesopotamia package, river administration, mandate monarchy option |
| Mapuche | Britannica Mapuche page and Araucania historical research | land congress, Araucania identity, treaty route |
| Guarani and Charrua | Britannica Guarani and Charrua pages | South American local-polity pool |
| Aymara | Britannica Aymara page | Altiplano and Lake Titicaca package |
| Palmares | Britannica Palmares page | Afro-Brazilian maroon republic package |
| Asante | Britannica Asante Empire page | Kumasi, council, royal symbol asset research |
| Kanem-Bornu | Britannica Kanem-Bornu page | Lake Chad old-state package |
| Buganda | Britannica Buganda page | kabaka, Lukiko, Lake Victoria route language |
| Barotseland and Lozi | Britannica Lozi page | floodplain governance and treaty memory |
| Zulu | Britannica Zulu and Shaka pages | royal council and regiment memory route |
| Herero and Nama | Britannica German-Herero conflict, Herero, and Nama pages | land return and grave memory package |
| Volga Bulgaria | Britannica Bulgar and Bolgary pages | Volga historical-return overlay distinct from Event 005 |
| Circassia and Caucasus | Britannica Cherkessia, Circassian, and Caucasus pages | mountain confederation and exile memory route |
| Bukhara, Khiva, Kokand | Britannica Bukhara and Khiva pages, plus academic or UNESCO material for Kokand | Central Asian oasis and khanate packages |

## Implementation quality pass

A first working implementation is not enough for this event. Independence Wave has to be checked as a living system after the basic resolver works.

### Depth checks

| Area | Failure sign | Required improvement |
| --- | --- | --- |
| host crisis | host only clicks one cheap button | add missions, variable costs, delayed consequences, and AI strategy |
| candidate pool | every wave releases similar countries | add package ladder, region weighting, dormant tags, and high-chaos pools |
| country setup | new tags appear with no problems | add provisional ideas, recognition path, militia constraints, and route decisions |
| focus tree | one generic ladder serves every release | add route families, overlays, crisis branches, and package identity |
| decisions | political power buys all progress | add equipment, manpower, supply, rail, observer, legitimacy, and deadline costs |
| old-state packages | old names appear with no institutional logic | add archives, councils, modern compromise, and claims after release |
| local-polity packages | living peoples become generic fantasy states | add land congress, community defense, source review, and restrained naming |
| strange packages | horror is only a flag and modifier | add state-like bureaucracy, doctrine, decisions, and visible consequences |
| assets | all waves share one image | add dossier, suppression, release, patron, league, old-name, local, and strange art |
| super-events | dramatic popup fires too often | gate them to rare world-order or high-chaos moments |
| achievements | unlocks happen just because the event fired | require route mastery, origin checks, and disqualifiers |

### Completion gates

Before the implementation is considered finished, the agent should be able to answer:

1. Can a host ever be deleted by Event 6? The answer must be no.
2. Can Event 6 Volga Bulgaria receive Event 5 content by accident? The answer must be no.
3. Does every release have an origin flag?
4. Does every candidate package have a state validation path?
5. Does every host decision change at least one meaningful variable?
6. Does every major focus route unlock gameplay beyond flat modifiers?
7. Are high-chaos packages rare and regionally justified?
8. Are real symbols, leaders, and flags sourced or blocked?
9. Are super-events complete across trigger, text, quote, image, audio, docs, and log?
10. Are achievements guarded against debug and wrong-origin completion?

## Current source-spec location

This package is the source design pack for Event 006 and should live under:

```text
docs/specs/006_independence_wave_specs/
```

Subagent plans, audit follow-up notes, blocked reports, improvement addenda, and patch handoffs should live under:

```text
docs/plans/006_independence_wave_plans/
```

The specs folder is the source-of-truth design area. The plans folder is a working area. If an improvement addendum becomes accepted design, the main agent should fold it into this spec pack or explicitly report that it remains queued.

## Formation identity layer

Independence Wave should not only create breakaway states. Some breakaway states can later earn larger identities through formable nation routes. These routes must be controlled by Event 006 origin logic and must not reuse Event 005 formation logic unless a shared helper is deliberately generic.

Formation is a later ambition, not the first release action. The wave creates fragile states. Focuses, decisions, diplomacy, wars, recognition, and integration missions decide whether a state can claim a larger identity.

Formation rules:

- Focuses prepare or reveal the claim.
- Decisions verify owned and controlled states or named state groups.
- Hidden formables require route, event, leader, chaos, or rare package reveal logic.
- Large or contested formables should grant claims first and cores through staged integration.
- Formation must not bypass the absolute host survival rule during the initial wave.
- Shared tags must read release origin and formation origin before loading trees or overlays.
- AI can pursue formables only when route, war state, supply, strength, and map control make the attempt plausible.

Formation families for Event 006:

| Family | Typical packages | Formation fantasy | Gameplay proof |
| --- | --- | --- | --- |
| Regional congress | ordinary releasables and city packages | small states become a federation or compact | several breakaways alive, league cohesion, recognition, non-puppet status |
| Historical return | Assyria, Mesopotamia, Volga Bulgaria, Mapuche Araucania, Sokoto, Asante, Buganda, Kanem-Bornu, Palmares | an old name becomes a modern state | route reveal, old-state memory, controlled core region, archives, legitimacy |
| Local polity union | Guarani, Aymara, Charrua, Herero, Nama, Barotseland, Darfur and similar packages | local authority becomes a recognized state or confederation | local support, named state groups, anti-patron route, integration missions |
| Protectorate consolidation | border protectorates and patron-backed states | a sponsor-backed state becomes a mandate, client union, or protected bloc | patron leverage, major guarantee, border control, dependency risk |
| Strange formation | necromantic, anti-mankind, archive-state, railway-state, impossible bureaucracy | a high-chaos authority stops pretending it is normal | hidden reveal, occult pressure, world-collapse tier, special route lock |

Example formation routes are design targets, not fixed final names:

- Assyrian Recognition Congress
- Mesopotamian Federation
- Volga Bulgar Volost Assembly
- Mapuche Araucania
- Palmares Restoration Council
- Barotse Protectorate Congress
- Mountain Republic Compact
- Railway League of Corridors
- The Charter Federation of New States

The implementation agent should build only the formables that have valid states, tag support, asset support, and enough route logic to be worth playing. It should report skipped formables as blocked or queued, not replace them with weak cosmetic renames.

## Interactive management layer

Independence Wave should use decision categories and scripted GUI only where they make the system clearer. The event has four strong candidates for interactive visual management.

### Independence Dossier Board

Purpose: shows active host crisis dossiers after the instant release.

It should show:

- candidate list
- host survival protected state
- pressure
- legitimacy
- radicalization
- foreign attention
- likely package tier
- host response status
- reporter or observer presence
- warning when candidate territory would violate host survival

Buttons can include:

- Open talks
- Suppress committee
- Invite observers
- Arm loyalists
- Trade autonomy
- Delay recognition
- Ask for guarantee
- Evacuate archives

Every button needs costs, requirements, tooltips, AI equivalent, cleanup, and result feedback. Costs should vary by action and country state, using equipment, XP, stability, war support, legitimacy, foreign influence, trains, convoys, fuel, divisions in named states, or supply access where appropriate.

### New States Congress

Purpose: manages cooperation among released Event 006 countries.

It should show:

- member list
- coalition cohesion
- mutual guarantees
- shared stockpile
- volunteer corridors
- patron pressure
- arbitration disputes
- League formation progress

Buttons can include:

- Call a congress vote
- Share rifles
- Send volunteer cadre
- Demand anti-puppet clause
- Arbitrate border dispute
- Draft League charter
- Expel a client delegate

### Patron Ledger

Purpose: visualizes foreign sponsor influence.

It should show:

- sponsor influence tracks
- arms influence
- industrial influence
- intelligence influence
- recognition influence
- dependency risk
- rival sponsor friction
- exposed brokers

Buttons can include:

- Accept advisers
- Reject dependency clauses
- Balance rival patrons
- Expose foreign broker
- Request arms corridor
- Convert loans into treaty debt

### Formation Ledger

Purpose: shows formable progress for packages with formation routes.

It should show:

- required named state groups
- controlled states
- claimed states
- integration progress
- recognition status
- route disqualifiers
- hidden reveal progress where appropriate
- post-formation stability risks

The Formation Ledger must not expose secret formables too early. It can show incomplete rumors, sealed entries, or route-specific clues before the reveal event.

## Animated presentation layer

Animated sprites are optional but expected for major visual states where motion improves readability.

Animation candidates:

| Asset | Purpose | State-driven use |
| --- | --- | --- |
| dossier seal pulse | active crisis warning | pulses faster when pressure is high |
| Congress table glow | League vote ready | glow appears when enough members support charter |
| patron influence shimmer | patron dominance risk | shimmer shifts by sponsor dominance |
| formation seal float | formable decision unlocked | slow float when all visible requirements are met |
| impossible-state particles | high-chaos package active | particle layer appears only after strange reveal |
| animated leader portrait | rare route leader or council | appears after final route reveal or hidden formable |
| rump host candle or capital light | host survival floor | appears in the final warning and Rump That Endures moment |

Every animation must follow `chaos-redux-frame-animation`. It needs real source frames, processed frames, a sheet PNG, a sheet DDS, a static fallback, a GIF preview for review only, a manifest entry, and a gfx handoff. Do not use a GIF as the final game asset. Do not create the final motion by transforming one still image.

## Improvement-loop closure gate

The Independence Wave design is large enough to justify improvement-loop passes, but the loop must not become infinite. After each meaningful implementation tranche, the main agent may spawn `chaosx_improvement_loop_planner` with `fork_context=false` and explicit inputs.

The planner should either write an expansion addendum or a closure handoff.

Expansion addendum is useful when:

- a new country package is shallow
- a formable route has no proof or post-formation play
- a scripted GUI only decorates the mechanic
- AI has no clear strategy
- assets are static where route state should visibly change
- decisions are passive buttons
- focus routes are reward ladders
- historical or regional content is underused

Closure handoff is correct when:

- the accepted specs and plans are implemented
- no known fallbacks or simplifications remain
- countries have identity, routes, AI, forces, and assets
- decisions have costs, timers, failure states, tooltips, and cleanup
- formables have reveal logic, map proof, integration, and AI rules
- GUI has AI equivalents and readable state
- animations have fallbacks and handoffs
- super-events have real thresholds and source notes
- docs, catalog, event details, localisation, assets, and validation are aligned

A closure handoff should say that no broad expansion is recommended because additional mechanics would bloat the system. It should list only final validation, cleanup, and alignment tasks. The main agent still owns the final completion claim.
