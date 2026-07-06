# 006 Independence Wave Spec Part 1: Core Event Model

This source spec defines Event 6 as a repeatable liberation shock in the Liberations cluster. Working labels for routes, mechanics, assets, achievements, and events are design labels only. Final player-facing localisation should be written during implementation from the direction in these files.

## Event identity

Independence Wave is a repeatable liberation shock. It turns dormant claims, ignored petitions, local assemblies, surviving princely files, religious institutions, minority committees, city councils, port authorities, railway boards, exile leagues, and local defense circles into governments that exist on the map immediately.

The event should not feel like a button that releases a few tags. It should feel like the world suddenly accepts that certain borders were weaker than they looked. New countries should arrive with politics, fear, a government problem, a military problem, a recognition problem, a former host problem, and a reason to choose a path.

A normal wave should create several new states instantly. The aftermath should last longer than the release popup. New countries must fight for recognition, assemble institutions, raise forces, decide whether to bargain with the former host, seek foreign help, avoid becoming client states, cooperate with other released countries, and consider larger identities through decisions once they control the right regions.

The former host should survive. The host must keep at least one state, and the preferred remaining state is its capital. If that is impossible because the only meaningful release package would consume the capital, the release package must shrink, choose another host, delay that target, or convert the target into claims and post-release missions instead of ownership.

## Relationship with Soviet Collapse

Independence Wave and Soviet Collapse are separate systems.

A tag may appear through both systems, but its content must depend on release origin. A republic, Soviet-region country, Volga Bulgaria, Central Asian state, Caucasus state, Baltic state, or other overlapping tag that appears through Independence Wave receives Independence Wave flags, mechanics, focus overlay, decisions, ideas, event text direction, AI behavior, and formation rules. The same tag appearing through Soviet Collapse receives Soviet Collapse content.

The release origin rule is stronger than the tag identity rule. The tag tells the engine which country exists. The origin tells the mod which event owns its mechanics.

The implementation design should use origin memory, not one global country assumption. A country created by Event 6 should receive an Independence Wave origin flag and should load only the Independence Wave content package. An existing country that already has meaningful content should not have its focus tree replaced blindly. It should receive an additive Independence Wave crisis package only if the wave actually created it or if the event explicitly marks it as participating in the wave.

Shared tags should always route through origin-aware checks. The spec should treat this as one of the core acceptance criteria for the event.

## Tag and naming rule

New custom tags created for this event should end with `X`.

This applies to new Event 6 country tags, formable tags, cosmetic tags, and route split tags. Existing vanilla tags, existing Chaos Redux tags, and already registered tags can be reused without renaming when they already exist and the implementation confirms that reuse is safe.

The `X` ending rule prevents Event 6 from consuming every good normal tag slot. It also makes origin auditing easier. The country package matrix distinguishes:

| Tag class | Example handling | Rule |
| --- | --- | --- |
| Existing vanilla tag | Reused only if already safe and if release origin can be tracked | No forced `X` suffix. |
| Existing Chaos Redux tag | Reused if already registered and not owned exclusively by another event | No forced `X` suffix unless the existing tag already has it. |
| New Event 6 country tag | New releasable or restored local country | Must end with `X`. |
| New Event 6 cosmetic tag | Route identity, puppet identity, league identity, or formable public name | Must end with `X`. |
| New Event 6 formable tag | Final tag for a large formation if a cosmetic tag is not enough | Must end with `X`. |

Country public names should stay readable on the map. Do not name countries after internal offices, bureaus, boards, compacts, or emergency committees. Such institutions can exist inside the country package, but the public country name should be a country, people, dynasty, region, kingdom, republic, union, federation, sultanate, commune, or empire name when that form fits the route.

## Core wave count ladder

The normal wave count ladder should follow the user direction.

| State of Event 6 | Working stage label | Normal release count | Release identity focus |
| --- | --- | ---: | --- |
| Baseline | First petitions | 3 | Mostly countries that already exist in vanilla, Chaos Redux, or normal releasable pools. |
| Evolution I | Dossier surge | 4 | Existing releasables, dormant republics, subject territories, local councils with obvious state anchors. |
| Evolution II | Cascading petitions | 5 | More hosts, more regional variety, city and rail authorities, protectorate fragments, culturally grounded local packages. |
| Evolution III | Border commission crisis | 7 | Stronger disputed borders, wider foreign attention, claims that can become wars or settlements. |
| Evolution IV | Great partition week | 10 | Historical restorations, regional polities, local kingdoms, indigenous claims, and larger release packages. |
| Evolution V | Open season | 10 | The count does not need to exceed ten. This stage makes releases stranger, stronger, less cooperative, and more ambitious. |

The current catalogue row has wider ranges for some stages, but this rework should use the cleaner ladder above as the normal automatic event behavior. High chaos should usually make each released country stronger, stranger, more unstable, or more ambitious. It should not simply inflate the normal country count forever.

Manual scenario intensity can release all possible countries. That scenario is separate from the automatic count ladder.

## Event flow at a glance

The event starts with a wave assembly step, then resolves releases instantly, then distributes aftermath tools.

1. Select one or more hosts.
2. Build a release candidate pool from valid tags, region packages, host territory, chaos tier, prior waves, current wars, subject status, and cluster pressure.
3. Choose release targets until the stage count is reached.
4. Reserve at least one state for every affected host, preferably the capital.
5. Release each target instantly with a state package.
6. Apply origin flags, wave memory, former host memory, and release package type.
7. Assign opening ideas, decisions, focus overlay, starting units, leaders, and AI route bias.
8. Give the host response tools and a short instability memory.
9. Update the event log and event details.
10. Check whether league, aggressive bloc, high-chaos wave, or other super-event thresholds are met.

The player should see new countries immediately. The deeper mechanics begin after the map changes.

## Host selection

A host is any country that can lose states without being deleted. The event should prefer hosts with credible internal fault lines, multiple possible release packages, subject networks, occupied territory, low stability, high war exhaustion, exposed border regions, or recent liberation pressure.

Possible host weighting factors:

| Factor | Effect on host weight | Reason |
| --- | --- | --- |
| Owns many states | Strong increase | Large countries can absorb state loss without deletion and have more release targets. |
| Controls territory without cores | Strong increase | Occupied or administratively weak land is easier to detach. |
| Has subjects or colonial possessions | Strong increase | Protectorates and colonies fit the wave identity. |
| Low stability | Increase | Weak institutions make petitions more credible. |
| Low war support during war | Increase | Garrison obedience and public patience are weaker. |
| Recently lost a war or large state | Increase | Defeat creates space for committees and local authorities. |
| Recently had Event 5 or another liberation event nearby | Increase | The Liberations cluster should feel connected without merging its member systems. |
| Player host | Moderate weight, not immune | The event should be playable against the player, but not unfairly delete the country. |
| One-state host | Block | The event must not delete a host. |
| Capital-only viable release | Usually block or downgrade to claim-only | Capital retention is preferred. |
| Special nonhuman or terminal chaos country | Usually block | Event 6 is about human political state creation, not nonhuman crisis actors. |

The event should not always hit the largest country. Waves should sometimes target colonial empires, regional majors, fragmented countries, and mid-sized states that have rich release pools. The weighting should prevent tiny countries from being destroyed and prevent every wave from tearing the same major apart.

## Host survival rule

Every affected host must keep at least one state. The preferred retained state is the capital. If keeping the capital leaves the host with only a useless enclave, the host should also keep a supply or adjacent state when possible.

The host survival rule should be resolved before release effects run. The event should never release a target and then discover that the host has been deleted.

Host safety outcomes:

| Situation | Required outcome |
| --- | --- |
| Host has one state | Host is not eligible. |
| Host has two states and one release candidate would take one non-capital state | Release can proceed if the capital remains. |
| Host has two states and the release candidate requires the capital | Release target is downgraded, rerolled, or converted to claim-only. |
| Host has several states but all candidate releases together would consume every non-capital state plus the capital | The wave must reduce that host load, pick another host, or leave some targets claim-only. |
| Host capital is in the selected target package | Capital is removed from the release package unless the host can move capital safely before release. |
| Host is a subject and release would leave overlord logic invalid | Release should proceed only if subject and overlord cleanup rules are defined. |
| Host is in a civil war or scripted crisis | Release can proceed only if origin checks prevent event systems from overwriting each other. |

A release candidate should have an anchor state, support states, and claim states. If the full package would break host safety, the release should receive the anchor state and claims on support states instead of ownership.

## Release package tiers

Each release target should have a package tier. The tier controls how much territory the country gets immediately, how many claims it receives, how strong its starting forces are, how unstable it begins, and how much host anger it creates.

| Package tier | Immediate land | Claims | Starting strength | Typical use |
| --- | --- | --- | --- | --- |
| Seed | One anchor state | Several local claims | Very weak militia and emergency administration | Low-chaos minor identities or host-safety fallback. |
| Compact | Anchor state plus one or two support states | Local claims around the package | Weak but playable | Baseline and Evolution I. |
| Regional | Several contiguous states | Wider region claims | Moderate | Evolution II and Evolution III. |
| Partition | Large coherent region | Wider disputed border claims | Stronger, with patron or depot options | Evolution III and Evolution IV. |
| Ambition | Strong region with route claims | Hidden or revealed formable claims | High instability and major diplomatic backlash | Evolution IV and Evolution V. |

The release tier should never override host survival. A strong package should shrink before the host is deleted.

## Release pool philosophy

The event needs a large pool, but it should not require every possible country to have a bespoke full tree on day one. The correct structure is layered.

Every released country receives:

1. Origin memory.
2. A valid tag or safe custom Event 6 tag.
3. A public country name and adjective.
4. A core or anchor territory package.
5. A starting government and leader model.
6. A small set of starting ideas.
7. Dynamic starting units.
8. Independence Wave decisions.
9. Access to the shared Independence Wave focus overlay.
10. Region-specific branch inserts.
11. Country-specific ambition inserts for selected stronger packages.
12. Formable decision access when region and route conditions fit.
13. AI behavior appropriate to its package, region, and strength.
14. Asset coverage for flags, leaders, ideas, decisions, focuses, and important transformations.

This allows the event to cover a hundred countries without hardcoding a unique full system for every one. The shared layer keeps everything playable. The region and country layers make important countries feel distinct.

## Release pool classes

Release targets should be grouped by origin class. The class affects availability, chaos tier, starting politics, likely mechanics, and asset source mode.

| Class | Working class label | Availability | Examples | Gameplay role |
| --- | --- | --- | --- | --- |
| A | Existing releasable | Baseline onward | Vanilla or Chaos Redux releasables, obvious subject releases, existing national cores | Safe early pool. These should be common in low chaos. |
| B | Administrative republic | Baseline onward, more common after Evolution I | Colonial territories, protectorates, autonomous republics, city administrations, frontier districts | Gives the event variety without deep historical restoration claims. |
| C | Dormant national claim | Evolution I onward | Cultural or national identities with strong regional anchors | Adds stronger legitimacy play and recognition contests. |
| D | Historical restoration | Evolution II onward | Volga Bulgaria, Kongo, Asante, Benin, Kilwa, older kingdoms, old federations | Creates ambition branches and formable routes. |
| E | Local polity or indigenous restoration | Evolution III onward | Mapuche, Guarani, Aymara, Quechua, regional African polities, local confederacies | Gives high chaos local identity and harder recognition play. |
| F | High-chaos claimant | Evolution IV and V | Strange claimant families, exile congresses, aggressive league-backed partitions, restored ancient names with modern committees | Strong, unstable, rare, and potentially frightening. |

Classes D, E, and F need research notes and careful asset source choices. Historical flags, symbols, and real people should be sourced when they exist. Fictional route variants can be generated. Fictional leaders should not be confused with real leaders.

## Research seed principles

The country pool should use researched regional anchors. Research should inform claims, route names, faction institutions, symbols, and formable logic. It should not turn the event into a history lecture.

Examples of useful anchors:

| Region | Research anchor | Use in Event 6 |
| --- | --- | --- |
| Volga and Kama | Volga Bulgaria as a medieval state and Islamic trade center in the Volga-Kama region | A high-chaos historical restoration with claims around the Volga, a trade and river authority branch, and a possible larger Idel-Ural or Bulgar route. |
| Mesopotamia | The Tigris and Euphrates river world as a civilizational and agricultural anchor | A Mesopotamian release or formable route should center rivers, irrigation, archaeology, cities, and contested legitimacy. |
| Assyrian homeland | Assyrian cultural identity tied to northern Mesopotamian regions | An Assyria package should be a vulnerable minority-state survivor with recognition, church, diaspora, and defense branches. |
| Swahili Coast | Kilwa as a prosperous Swahili trading city tied to Indian Ocean commerce | A Kilwa package should use port control, trade revival, coastal diplomacy, and naval logistics. |
| Central Africa | Kongo as a historical kingdom with diplomatic and religious routes | A Kongo package should use court legitimacy, missionary legacies, river corridors, and foreign pressure. |
| West Africa | Benin and Asante as court, kingdom, and symbolic authority anchors | These packages should use royal court legitimacy, regalia, military reform, and anti-colonial diplomacy. |
| Southern South America | Mapuche resistance and confederated polity traditions | A Mapuche package should use local defense, federation, land control, mountain and forest defense, and recognition struggles. |

The country package file expands these anchors into a full country package matrix.

## Regional release layers

Every release target should belong to a regional layer. Region affects decisions, focus inserts, starting units, formables, patron behavior, and host responses.

| Region layer | Generic branch flavor | Typical special unit and mission flavor | Formable direction |
| --- | --- | --- | --- |
| Western Europe | Legal petitions, parliaments, city administrations, old duchies, island parliaments | Territorial guards, port police, border security, fortress repair | Federations, kingdoms, restored unions, coastal leagues. |
| Eastern Europe and Balkans | Old borders, minority treaties, garrisons, rail corridors, mountain regions | Border infantry, railway troops, mountain detachments, anti-occupation networks | Regional unions, old kingdoms, river federations. |
| Soviet-region overlap | Republic ministries, autonomous districts, depot seizures, old khanates, Cossack and Volga claims | Defected garrisons, railway guards, cavalry, depot brigades | Idel-Ural, Turkestan, Transcaucasia, Volga Bulgaria, local federation routes. |
| Middle East and North Africa | Mandate files, religious institutions, tribal congresses, urban committees, river and desert corridors | City guards, tribal cavalry, desert patrols, port guards | Mesopotamia, Greater Syria, Assyria, Kurdistan, Maghreb routes, local sultanates. |
| Sub-Saharan Africa | Kingdom restorations, local councils, anti-colonial congresses, river corridors, coastal trade | Royal guards, local militias, port and river troops, colonial defectors | Kongo, Asante, Benin, Kilwa, Hausa, Kanem-Bornu, regional federations. |
| South America | Indigenous federations, old republic borders, river peoples, mountain peoples, port cities | Mountain militias, forest detachments, cavalry, river guards | Mapuche, Guarani, Aymara, Quechua, Andean or river federations. |
| South Asia | Princely files, religious movements, language regions, port cities, frontier militias | Sepoy defectors, mountain troops, railway guards, port defense | Punjab, Bengal, Deccan, Dravidian, frontier confederations. |
| East and Southeast Asia | Old kingdoms, colonial administrations, city states, island polities, ethnic frontier claims | Jungle detachments, port guards, river patrols, island militia | Regional kingdoms, island federations, old imperial restorations. |
| North America and Oceania | Indigenous nations, island parliaments, dominion fragments, territorial committees | Rangers, local defense battalions, mounted patrols, port guards | Indigenous confederations, island federations, dominion splits. |

The country package file lists exact candidates by region. This overview defines the structure that prevents the event from becoming a random tag dump.

## Release target selection

Each target should have a score built from several factors. The score determines how likely the target is to be selected when its host is eligible.

Target score factors:

| Factor | Weight direction | Notes |
| --- | --- | --- |
| Has existing core or releasable support | Strong increase at low chaos | Keeps early waves grounded in existing HOI4 or mod content. |
| Host owns anchor state | Required | No anchor, no release. |
| Host can keep capital and one state | Required | Host safety overrides everything. |
| Tag already exists | Usually block | Existing independent countries should not be released again. Existing countries can receive crisis participation only if designed. |
| Tag can appear through another event | Allow with origin checks | The tag can exist through Event 6 if the release origin is tracked. |
| High chaos historical package | Increase at high chaos | Unlocks niche countries and local polities later. |
| Prior wave in the same region | Mixed | Can create cascade behavior, but avoid repetition from the same host every time. |
| Nearby released countries | Increase if league content is active | Encourages clusters of new states that can cooperate or compete. |
| Major host weakness | Increase | Weak major states are prime partition targets. |
| Country package missing essential assets | Lower or block until ready | Do not release a country that has no flag, leader model, or valid gameplay package. |

Selection should prefer variety. If a wave needs ten countries, it should usually draw from multiple hosts or multiple regions unless a specific high-chaos partition event is being created.

## Immediate release outcome

Every released country should receive a complete opening package.

Minimum opening package:

| Surface | Required design |
| --- | --- |
| Ownership | At least one anchor state, never all states from the host. |
| Cores and claims | Cores on anchor states, claims or disputed claims on nearby package states. Large foreign regions should usually be claims first. |
| Capital | Anchor state or best urban state inside the package. |
| Leader | Regional provisional leader, council, royal court, junta, congress, or local committee. Real people require sourcing. Fictional one-person leaders need plausible regional name pools. |
| Ruling politics | Start from release class and region, not a global ideology default. |
| Ideas | Small set of deep starting ideas, usually mixed or negative, with lifecycle paths. |
| Units | Dynamic militia, garrison, depot, border, rail, port, mountain, or cavalry units based on territory, package tier, and chaos. |
| Decisions | Independence Wave survival and recognition decisions. |
| Focus content | Shared focus overlay plus region inserts and optional country ambition inserts. |
| AI | Defensive survival AI first, then route behavior based on legitimacy, recognition, host threat, patron influence, and strength. |
| Former host memory | The country remembers who it broke from and the host receives response tools. |
| Event log | The wave records the event and visible actor context. |

A released country should never spawn as a silent empty tag.

## Starting idea model

New countries should start with a small number of important ideas. The starting problems should matter.

Suggested starting ideas:

| Working idea label | Role | Lifecycle direction |
| --- | --- | --- |
| Provisional Government | Mixed legitimacy and bureaucracy problem | Improved by government-building focuses, recognition, elections, councils, or royal consolidation. |
| Unsettled Borders | Border instability and former host claims | Improved by treaties, defended borders, arbitration, league support, or victorious reclamation wars. |
| Improvised Command | Weak army coordination and equipment shortage | Improved by militia integration, depot seizure, foreign training, and army reform. |
| Recognition Question | Diplomatic weakness and trade limitations | Improved by foreign missions, sponsor balancing, league recognition, and treaty outcomes. |
| Host Pressure | Risk from former host | Removed or transformed by settlement, victory, host collapse, puppet compromise, or league deterrence. |
| Patron Entanglement | Only when the country takes heavy foreign help | Can become useful aid, dependency, puppet pressure, or anti-puppet backlash. |

Avoid giving every released country a stack of generic positive spirits. The first year should feel like survival.

## Starting forces

Every released country expected to survive should receive dynamic starting forces. Forces should depend on state count, population, industry, terrain, ports, rail hubs, depots, former host weakness, chaos stage, package tier, and whether the country has foreign support at release.

The force package should be modest at low chaos and serious at high chaos.

| Package | Typical forces | Scaling factors |
| --- | --- | --- |
| Seed | One or two militia units, often under equipped | Population, state priority, local support, chaos. |
| Compact | Several militia units plus one garrison or guard unit | State count, rail or city control, former host weakness. |
| Regional | Militia, garrisons, and at least one better unit family | Industry, captured depots, port access, mountain terrain, chaos. |
| Partition | Mixed regular defectors and local forces | Former host war state, garrison defection chance, depot control. |
| Ambition | Stronger starting army, but higher instability and border heat | High chaos, patron access, league support, host weakness. |

Unit flavor should vary by region. A mountain release should receive mountain detachments or rugged local infantry. A port release should receive port guards and naval logistics decisions. A rail corridor release should receive railway troops and train or rail-control missions. A steppe or Volga package can use cavalry or mobile border detachments. A city-state package can use urban security and factory guards.

## Former host response

The host should not be a passive victim. It should receive response choices that depend on its ideology, strength, stability, wars, and relationship to the released countries.

Host response families:

| Response | When it fits | Consequence |
| --- | --- | --- |
| Recognition | Democratic, exhausted, pressured, or diplomatically isolated hosts | Lowers border heat and raises recognition, may create a treaty or guarantee. |
| Autonomy settlement | Hosts that want influence without immediate war | Creates subject or associated status options if the released country accepts. |
| Reclamation preparation | Strong hosts, nationalist hosts, military hosts, or hosts with high war support | Creates claims, timed preparations, and possible war goals if negotiations fail. |
| Punitive border measures | High anger, contested borders, or low legitimacy releases | Raises border heat and makes League intervention more likely. |
| Infiltration and loyalists | Security-heavy or authoritarian hosts | Raises foreign or host influence inside the released country, can trigger internal crisis. |
| Forced federation proposal | Hosts that still have diplomatic leverage | Offers a compromise that can prevent war but risks dependency. |

The former host should almost always have a path that avoids immediate war and a path that can escalate. The AI should not always pick war. War should depend on strength, wars, ideology, target value, and league deterrence.

## Independence Wave country mechanics

the mechanics layer will define the values in full. the core release logic establishes the required mechanic set.

Every Independence Wave country should track:

| Mechanic value | Meaning | Primary uses |
| --- | --- | --- |
| Legitimacy | Domestic belief that the new government has the right to rule | Focus unlocks, stability, army obedience, resistance to host pressure, formables. |
| Recognition | External acceptance by other countries | Trade, foreign aid, faction access, host settlement, league authority. |
| Foreign Support | Useful help from outside powers | Equipment, advisors, volunteers, industry, recognition. |
| Patron Influence | The cost of foreign support | Puppet pressure, route locks, coups, sponsor demands. |
| Coalition Trust | Trust with other Independence Wave countries | League membership, common defense, shared missions, arbitration. |
| Border Heat | Likelihood of host retaliation or border conflict | Host decisions, missions, war risk, border settlement. |
| Post-Release Instability | Internal administrative and military disorder | Starting penalties, events, missions, route failure. |
| Local Control | Real control of released states | Integration, coring, recruitment, claims, formables. |

These values should be visible through decision category text, scripted localisation, focus tooltips, and later a compact UI panel through the scripted GUI design.

## Shared focus overlay concept

Independence Wave countries should receive a shared focus tree or overlay, with regional and country-specific branches.

The overlay should not be a generic neutral minor tree. It should be the playable story of a newly independent state.

Opening focus architecture:

| Branch | Purpose |
| --- | --- |
| Survival and authority | Build provisional government, stabilize capital, reduce administrative chaos, create first laws, decide how provisional rule works. |
| Recognition and diplomacy | Seek observers, bilateral recognition, league recognition, neutral guarantees, or patron aid. |
| Former host | Negotiate, resist, infiltrate host loyalists, prepare defenses, or accept a protected status. |
| Army and security | Integrate militias, seize depots, train officers, create border guards, reform command. |
| Economy and logistics | Secure railways, ports, ministries, emergency taxation, construction programs, supply hubs, and local industry. |
| League and coalition | Join or lead the Independence League, support other new states, share reserves, arbitrate borders. |
| Regional ambition | Region-specific claims, formable reveal, special institutions, local historical routes. |
| High-chaos ambition | Aggressive or strange routes that unlock at high chaos or extreme instability. |

The overlay should use country-specific scripted localisation where possible. It should not read the same for every country.

## Region inserts and ambition inserts

The shared overlay should have two add-on layers.

Region inserts give all countries in a region a distinct way to solve the same problems. Country-specific ambition inserts are rarer branches for selected stronger releases.

Examples:

| Insert type | Example content |
| --- | --- |
| Volga insert | River trade, rail corridors, Bulgar memory, Tatar and Finno-Ugric settlement politics, steppe defense. |
| Mesopotamia insert | River control, irrigation repair, ancient city legitimacy, urban ministries, Assyrian and Arab minority politics. |
| Swahili coast insert | Port revival, Indian Ocean routes, coastal trade, mosque and merchant institutions, naval logistics. |
| Central African insert | River corridors, royal court legitimacy, missionary legacies, border chiefs, anti-colonial diplomacy. |
| West African kingdom insert | Regalia, court authority, federation of chiefs, forest and gold routes, colonial garrison defections. |
| Southern Cone indigenous insert | Land councils, confederated defense, mountain and forest warfare, autonomy treaties. |

Country-specific ambition inserts should be used for selected countries such as Volga Bulgaria, Assyria, Mesopotamia, Kongo, Asante, Benin, Kilwa, Mapuche, Guarani, Aymara, and other strong candidates. The full list belongs in the country package and formable files.

## League and coalition concept

Independence Wave countries should have a path to form a larger league or coalition. This should not be automatic for every wave.

The league should form when several released countries survive long enough, have enough recognition or shared danger, and have enough coalition trust. It should be easier if the former hosts are threatening them, harder if they are divided by ideology, patrons, border disputes, or local rivalries.

The league should have goals:

1. Keep new states alive.
2. Prevent former hosts from reclaiming members one by one.
3. Share recognition work.
4. Share equipment and advisors.
5. Arbitrate member borders.
6. Create common defense plans.
7. Decide whether the league stays defensive or becomes a tool for further partitions.

League mechanics should include cohesion, common beliefs, member confidence, sponsor pressure, and leadership prestige. the mechanics layer should make this a real system, not only a faction.

A league formation super-event should fire only when the league is large or important enough. It should not fire when two tiny states sign a weak pact.

## Aggressive bloc alternative

High chaos should unlock a more dangerous alternative. Some Independence Wave countries may reject defensive cooperation and build an aggressive bloc that treats every old border as evidence to reopen the map.

This bloc should not usually cooperate with ordinary released countries. It can form from countries with high border heat, low recognition, strong armies, radical focus routes, patron rivalry, or high-chaos ambition inserts.

Its goals are different:

1. Break former hosts before they recover.
2. Back each member's maximal claims.
3. Use league-like mechanics for war preparation.
4. Punish members that accept settlements.
5. Reveal hidden or large formables.
6. Trigger a super-event if it becomes a regional or global fear.

The aggressive bloc can use the same underlying league mechanic with different rules, or it can be a separate faction type if implementation needs cleaner logic.

## Formable nation philosophy

Formables should usually be decisions, sometimes revealed by focuses, events, ideology, chaos tier, or hidden conditions.

A country should not form a larger identity just because a focus completed. If territory matters, a decision should verify state control, subject status, allied membership, claims, legitimacy, recognition, and route flags.

Formation should often grant claims first and then gradual cores through integration missions. Instant cores are acceptable for small, coherent, culturally central areas. Large or contested regions should need work.

Formables should be region-based so the system can support many countries. A few selected countries can have special routes, but the other hundred countries still need access to appropriate regional formation logic.

Examples of formation families defined by the formable web:

| Formation family | Possible candidates | Formation proof |
| --- | --- | --- |
| River federation | Volga, Mesopotamia, Nile, Congo, Paraná, Danube packages | Control river states, rail or port nodes, legitimacy and recognition. |
| Restored kingdom | Kongo, Asante, Benin, Kilwa, old sultanates, old khanates | Control old heartland, complete court or assembly route, secure regalia or symbolic authority. |
| Indigenous confederation | Mapuche, Guarani, Aymara, Quechua, other local polities | Control core local states, win autonomy treaties, build councils, resist patron domination. |
| Regional republic | Administrative republics and modern national claimants | Recognition, capital control, elections or congress route, host settlement. |
| League federation | Any cluster of Independence Wave states | League cohesion, member votes, common defense success, low patron domination. |
| High-chaos partition order | Aggressive bloc members | Border heat, military strength, high chaos, radical route, hidden reveal conditions. |

The formables file defines the state-group model, integration requirements, reveal logic, and host safeguards.

## Evolution structure

Event 6 has baseline waves and five evolution stages. Baseline waves are ordinary event behavior. Evolutions are mutation tracks that change what the next wave can do and what already released countries can access.

Every evolution should have two entry paths:

| Entry path | Meaning |
| --- | --- |
| Active-event evolution | Event 6 has already released one or more countries. When the evolution unlocks, existing Event 6 countries gain new decisions, focus branches, AI behavior, and league options. |
| Pre-fire evolved opening | Event 6 has not fired yet or fires again later. The new wave starts with the evolved release count, release pools, state packages, and opening strength. |

Because Event 6 is repeatable, both entry paths matter. An old released country should not wait for a new wave before getting relevant evolution content.

### Baseline: First petitions

Baseline waves release three countries.

Baseline should mostly use existing releasable or normal tags. Custom countries are possible only when their package is already complete and grounded in obvious local state anchors. The normal player experience should be that the first wave creates fragile but recognizable new states.

Baseline features:

| Surface | Baseline design |
| --- | --- |
| Release count | Three countries. |
| Country classes | Mostly A and B. Rare C if package is complete. |
| Territory | Seed or compact package. |
| Starting forces | Weak militia and local guards. |
| Mechanics | Legitimacy, recognition, host pressure, instability. |
| Decisions | Government, recognition, basic defense, host talks, militia integration. |
| Focus content | Opening survival and basic recognition branches. |
| League | Only early contact, no large league formation yet unless prior Event 6 countries already exist. |
| Host response | Protest, settlement talks, limited reclamation preparation. |
| Super-event | Usually none. |

### Evolution I: Dossier surge

Evolution I waves release four countries.

The dossier surge represents claims that have enough paper, witnesses, guards, and local offices to become governments quickly. It should still feel mostly normal. The difference is that releases arrive with better preparation and a wider set of plausible claimants.

Active-event changes:

| Existing Event 6 countries gain | Purpose |
| --- | --- |
| Recognition dossier decisions | Converts basic petitions into foreign observer missions. |
| Former host negotiation missions | Makes settlement possible before war. |
| Basic league observer contact | Lets several released countries coordinate without forming a full faction. |
| First regional focus inserts | Gives geography some identity. |

Pre-fire opening changes:

| New wave behavior | Purpose |
| --- | --- |
| Four releases | Matches count ladder. |
| Class A and B common, Class C possible | Keeps early wave grounded. |
| Compact packages more common | New states get enough land to play. |
| Slightly stronger militia and garrison units | Releases can survive the first month. |
| First host response choice event | The host sees choices instead of only losing states. |

### Evolution II: Cascading petitions

Evolution II waves release five countries.

Petitions begin copying one another across borders and hosts. One release makes another local group believe its own claim can work. This stage should introduce multi-host waves more often.

Active-event changes:

| Existing Event 6 countries gain | Purpose |
| --- | --- |
| League contact decisions | Countries can build coalition trust. |
| Patron outreach decisions | Foreign support enters as a real system. |
| Early border arbitration missions | Disputed member borders can be settled before they become wars. |
| Region-specific army and logistics decisions | New countries start playing differently by region. |

Pre-fire opening changes:

| New wave behavior | Purpose |
| --- | --- |
| Five releases | Matches count ladder. |
| Multi-host selection stronger | Prevents one host from being shredded every time. |
| Class C common, Class D rare | Adds historical and cultural depth without overwhelming early stages. |
| Regional packages possible | Some countries receive more than one state. |
| Foreign observers can appear | Recognition and patron mechanics begin immediately. |

### Evolution III: Border commission crisis

Evolution III waves release seven countries.

At this stage, the issue is no longer only independence. Borders become dangerous. Released countries can press claims beyond their anchor states, hosts can prepare reclamation, and nearby powers can sponsor their preferred outcomes.

Active-event changes:

| Existing Event 6 countries gain | Purpose |
| --- | --- |
| Border commission decision family | Lets countries claim, negotiate, arbitrate, or prepare for conflict. |
| Former host escalation system | Hosts can move from protest to pressure to war preparation. |
| League arbitration | Cooperative countries can reduce border heat. |
| Aggressive route seeds | High border heat countries can begin rejecting defensive cooperation. |

Pre-fire opening changes:

| New wave behavior | Purpose |
| --- | --- |
| Seven releases | Matches count ladder. |
| Class D common, Class E possible | Historical restorations and local polities enter. |
| Regional and partition packages possible | Some releases are large enough to reshape a region. |
| Stronger starting forces | Countries can fight short wars or defend borders. |
| Host warning choices | Former hosts can decide how hard to resist. |

The phrase warning should not be used as final player-facing wording. The design intent is that hosts get a visible choice before border conflicts or reclamation wars escalate.

### Evolution IV: Great partition week

Evolution IV waves release ten countries.

This is the stage where the event can feel like a world crisis without becoming a terminal branch. Old names, local polities, restored kingdoms, and hard-to-fit identities can appear if their packages are complete.

Active-event changes:

| Existing Event 6 countries gain | Purpose |
| --- | --- |
| Full league formation path | Surviving states can form a major coalition. |
| League shared reserves | Cooperation produces real military support. |
| Hidden regional formables | Strong countries can reveal larger identities. |
| Patron rivalry events | Sponsors can compete for influence and create dependency risks. |
| High-chaos focus branches | Countries can become stranger, stronger, more unstable, or more aggressive. |

Pre-fire opening changes:

| New wave behavior | Purpose |
| --- | --- |
| Ten releases | Matches count ladder. |
| Class D and E common, Class F rare | Enables niche and researched candidates. |
| Partition packages common | Several countries begin as meaningful actors. |
| Strong host backlash | Former hosts get serious response tools. |
| League super-event possible | Only if enough new states coordinate or enough territory is affected. |

### Evolution V: Open season

Evolution V waves still release ten countries, but the behavior changes.

Open season means that legal caution and normal border expectations are failing. The countries released in this stage are more likely to arrive armed, ambitious, radical, or tied to hidden formation routes. Some may refuse the Independence League and join an aggressive bloc.

Active-event changes:

| Existing Event 6 countries gain | Purpose |
| --- | --- |
| Maximal claim routes | High chaos countries can push beyond conservative borders. |
| Aggressive bloc formation | Radical countries can form a frightening faction. |
| Hidden formable reveal checks | Rare formables become possible when route and map proof align. |
| League crisis mechanics | Defensive league can fracture under patron pressure or border disputes. |
| Stronger AI ambition | AI countries can pursue risky routes when conditions fit. |

Pre-fire opening changes:

| New wave behavior | Purpose |
| --- | --- |
| Ten releases with stronger package weighting | Count stays controlled, power rises. |
| Class F more common | High-chaos claimants appear. |
| Ambition packages possible | Some countries start with wider claims and serious forces. |
| Former host war preparation common | Host conflict becomes a central risk. |
| Super-event likely if thresholds are met | Large coalition, aggressive bloc, or frightening wave can trigger presentation. |

## Super-event thresholds, first pass

Super-events should mark major Independence Wave milestones, not ordinary release waves.

Candidate super-event roles:

| Role | Trigger concept | Why it deserves treatment |
| --- | --- | --- |
| League formation | A large Independence League forms with enough members, cohesion, and territory | The event stops being scattered breakaways and becomes a new international bloc. |
| Aggressive bloc formation | A high-chaos border bloc forms with several armed members and maximal claims | The event becomes a feared expansionist coalition. |
| Great partition shock | A high-chaos wave releases ten countries across multiple hosts, including at least one major host or several continents | The world sees a scale of release that normal diplomacy cannot contain. |
| Major formable proclamation | A released country forms a region-changing state through Event 6 mechanics | The release system produces a new regional order. |
| League victory or fracture | The league survives a major host war or collapses into member wars | The coalition system reaches a campaign-defining milestone. |

Super-event title, quote, cultural remark, and audio research belong to the super-event package. the presentation layer should give direction only and require source research before final localisation.

## Triggerable scenario skeleton

The triggerable scenario should release every possible country selected by the Event 6 release pool.

Intensity should not decide whether all possible countries are released. Minimum intensity still releases every valid possible country. Intensity changes how much land they get, how many units they receive, how severe their instability is, how strong the host response is, and whether they start coordinated or at war.

Scenario working title: Independence Wave All Claims Open, working label only.

Scenario intensity:

| Intensity | Territory | Units | Instability | Host response |
| --- | --- | --- | --- | --- |
| Low | Anchor or seed packages for all valid countries | Minimal militia and guards | High instability | Hosts mostly receive protest and settlement tools. |
| Medium | Compact packages where host safety allows | More militia, some garrisons | Moderate to high instability | Hosts can prepare reclamation if strong. |
| High | Regional packages where safe | Serious garrisons, depots, and region units | Moderate instability with high border heat | Hosts can escalate faster. |
| Maximum | Largest safe packages, claims for the rest | Strong armies scaled by state value and chaos | Lower opening weakness but extreme border heat | Hosts can begin hostile or near-hostile depending on scenario type. |

Scenario types:

| Type | Behavior |
| --- | --- |
| Separate republics | All countries release independently without a starting faction. |
| Congress of new states | All eligible Event 6 releases begin in an Independence League or can join one immediately. |
| Host reclamation war | Every former host receives stronger reclamation tools and some releases begin at war or near war. |
| Open season | Released countries receive stronger claims, stronger armies, and weaker cooperation rules. |
| Patron scramble | Major powers immediately compete for recognition and influence over released states. |
| Everyone against the old map | Released countries begin coordinated against former hosts where safe, with a high risk of wider wars. |

The decisions and interface file defines scenario UI controls and cleanup. The formables and presentation files define scenario pool behavior, league outcomes, compact outcomes, super-event thresholds, and asset direction.

## Cluster behavior

Independence Wave belongs to the Liberations cluster with Soviet Collapse, but it does not share the Soviet Collapse system.

Cluster-level design should make Event 5 and Event 6 feel related as liberation shocks. It should not merge their mechanics.

Useful cluster interactions:

| Cluster link | Behavior |
| --- | --- |
| Prior Soviet Collapse | Raises Independence Wave weight near regions with surviving unreleased claims, but origin-specific content stays separate. |
| Prior Independence Wave | Raises local liberation pressure and can make another wave more likely after a delay. |
| Cluster firing | Event 5 and Event 6 can appear together in a wider liberation shock only if both systems keep their origin checks. |
| Cluster detail | Player-facing cluster detail should describe liberation shocks, not mechanical release effects. |
| Shared map consequence | Former hosts and released countries may recognize that similar events are happening elsewhere. Mechanics remain separate. |

## AI first principles

AI behavior should be route-specific from the start.

Released country AI should evaluate:

| AI question | Factors |
| --- | --- |
| Should it seek recognition first | Low legitimacy, weak army, democratic route, host is strong, patron options exist. |
| Should it arm first | Host is hostile, border heat high, war nearby, terrain favors defense. |
| Should it join the league | Nearby Event 6 countries, shared former host, low patron dependence, high host pressure. |
| Should it seek a patron | Weak economy, no league nearby, major sponsor has ideological affinity, host threat is high. |
| Should it resist patron domination | Legitimacy high, recognition moderate, league support available, anti-puppet route. |
| Should it press claims | Army strong, host weak, border heat high, radical or high-chaos route. |
| Should it form a larger country | Controls required states, legitimacy and recognition enough, route supports it, not already in a conflicting formable. |

Former host AI should evaluate:

| AI question | Factors |
| --- | --- |
| Recognize or repress | Strength, wars, ideology, stability, war support, league deterrence, target value. |
| Negotiate settlement | Low war support, diplomatic pressure, many released states, patron interference. |
| Prepare reclamation | Strong army, high war support, nationalist or authoritarian route, release took valuable states. |
| Infiltrate | Security ideology, low target legitimacy, sponsor rivalry. |
| Avoid escalation | Already losing war, poor supply, major powers support releases, league strong. |

Sponsor AI should evaluate:

| AI question | Factors |
| --- | --- |
| Recognize | Ideology, rivalry with host, region interest, low cost, diplomatic goals. |
| Fund | Economic strength, target's industry, long-term influence value. |
| Arm | Target is fighting a rival or blocking a rival. |
| Puppet | Patron influence is high and target legitimacy is low. |
| Abandon | Target is collapsing, too expensive, or causes unwanted war. |
| Balance support | Several sponsors involved and target resists domination. |

the mechanics and decision files turn these into mechanic and decision behavior.

## Player-facing text direction

This specification should not write final localisation.

Text direction for Event 6 should focus on the observed phenomenon: local officials taking oaths, guards changing armbands, courts refusing old orders, rail schedules changing seals, ports raising new flags, and old claims becoming immediate government work. Avoid making the emotional center a map change or a generic diplomatic statement.

Normal wave text should treat the wave as sudden and practical. High chaos text can become stranger and more ambitious, but it should still show concrete people and institutions acting. The player should understand that the new countries exist now and that the consequences are political, military, and local.

Option text direction should vary by actor:

| Actor | Option tone direction |
| --- | --- |
| Released country | Nervous resolve, provisional confidence, legal urgency, or local defiance. |
| Former host | Anger, humiliation, restrained settlement, official coercion, or cold calculation. |
| Foreign sponsor | Opportunity, caution, ideological sympathy, or strategic exploitation. |
| League member | Solidarity, suspicion, bargaining, or common survival. |
| Aggressive bloc member | Triumph, impatience, border hunger, or contempt for compromise. |

Final wording should be written during implementation from this direction. It should not paste working labels from the spec.

## Documentation and catalog direction

Event Details should describe what Independence Wave does in play without listing mechanical effects. It should explain that several new governments can appear at once, that hosts survive, that later waves bring rarer and more ambitious releases, and that released countries struggle over recognition, borders, foreign influence, and cooperation.

Evolution details should describe the character of each stage, not list every reward. The catalog should keep Event 6 as Minor Repeatable, Liberations cluster, medium member severity unless implementation changes the cluster tuning.

The final spreadsheet update should happen after the implementation has final in-game wording. The spreadsheet should mirror player-facing event detail and evolution detail text, not this design specification.

## Acceptance criteria for core release logic

This overview is satisfied only if implementation preserves the following.

| Requirement | Acceptance standard |
| --- | --- |
| Wave count ladder | Automatic waves use 3, 4, 5, 7, and 10 as the normal count ladder. |
| Host survival | No host can be fully deleted by the event. Capital retention is preferred. |
| Origin separation | Every Event 6 release has release origin memory, and overlap with Soviet Collapse uses origin-specific content. |
| Tag suffix rule | New Event 6 custom tags, cosmetic tags, route tags, and formable tags end with `X`. |
| Immediate release | Countries release instantly, not through delayed wars or focus-only setup. |
| Country content | Released countries receive mechanics, ideas, units, decisions, AI, and focus overlay content. |
| Release pool depth | Early waves mostly use existing or normal releasable content, higher stages unlock historical and local polities. |
| Formable structure | Formables use decisions with state, route, legitimacy, recognition, or hidden requirements. |
| League system | A larger league or coalition is possible and has mechanics beyond a faction button. |
| Super-event discipline | Super-events fire only for major league, aggressive bloc, high-chaos wave, major formable, or similar threshold moments. |
| Triggerable scenario | Scenario releases all possible countries at every intensity, with intensity scaling territory and strength. |
| No generic empty tags | No serious released country appears without leader model, flag plan, starting units, and playable content. |
