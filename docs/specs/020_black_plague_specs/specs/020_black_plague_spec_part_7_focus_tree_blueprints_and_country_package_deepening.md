# 020 Black Plague spec Part 7 - Focus tree blueprints and country package deepening

## Part 7 role

This part deepens the playable country layer for Evolution III, Evolution IV, and Evolution V. Part 5 established ordinary rat nations as nonhuman breakaway countries. Part 6 established the King of Rats as a separate sentient state with a world-end path. This part turns those concepts into route-level country packages and focus-tree blueprints.

All focus labels in this file are working labels, not final localisation. Final focus names, descriptions, option text, titles, quotes, cultural remarks, and country text must be written during implementation from the direction here.

## Base rat nation country package deepening

Base rat nations are temporary or semi-permanent nonhuman chaos countries. They can survive long enough to become playable, absorb weaker nests, or serve as the source for the King. They should not feel like a normal minor country with a strange flag. Their package should show that they are plague ecology with borders.

### Spawn archetypes

Each base rat nation should enter through one of four archetypes. The archetype should be derived from the infected state group that created it, not selected randomly without context.

| Archetype | Spawn conditions | Country behavior | Initial focus weighting |
| --- | --- | --- | --- |
| Ruin nest | One or two collapsed states with low infrastructure and heavy deaths | Defensive, hard to remove, slower expansion | warren defense and brood survival |
| Sewer swarm | Dense urban or high-infrastructure infected state group | Faster local attacks and stronger urban units | swarm growth and human war |
| Port warren | Infected port state or coastal cluster after overseas spread exists | Sea-jump support, port raids, convoy infection pressure | plague spread and coastal breach |
| Black warren | Weaponized exposure, long neglect, or very high disease load | Strong starting army, higher accident and blowback pressure around it | plague mastery and absorption |

The archetype can set starting idea variants, AI weights, and the first focus path priority. It should not create four separate complete trees. One base tree should read the archetype and weight branches dynamically.

### Public identity

Base rat public names should be short and map-readable. Use nest, warren, swarm, or regional rat-state direction, but do not use internal administrative words as the map name. The final names belong to localisation. The planning intent is that a base rat tag reads as an alien territorial actor, not a ministry or project.

Suggested identity surfaces:

| Surface | Direction |
| --- | --- |
| Map name | Short nest or warren state name tied to the spawn region where possible. |
| Adjective | Rat, warren, nest, or region-rooted adjective direction. |
| Leader | Institutional nonhuman leader for most nests, such as a warren mass, brood nerve, or nest court. Do not force a personal name for a mass portrait. |
| Portrait | Generated nonhuman council or swarm portrait at leader size. One-person portraits are allowed only for rare unusually sentient nests. |
| Flag | Fictional nonhuman flag. Motifs can include rat silhouette, plague mark, tunnel knot, black field, teeth, or corpse-field geometry. |
| Ruling ideology | High-chaos nonhuman mapping. It should be excluded from ordinary human political logic. |
| Parties | Institutional rat body names, not human parties. They should imply instinct, brood, warren, hunger, or nest order. |
| Diplomacy | No ordinary diplomacy with humans. Rat-to-rat absorption and King unification are the only normal diplomacy-like flows. |

### Starting ideas

Base rat nations should start with a small stack of deep ideas. These ideas need lifecycle, not permanent static badges.

| Idea direction | Start role | Upgrade path | Failure or loss path | Final forms |
| --- | --- | --- | --- | --- |
| Unformed warren | Shows that the country is newly emerged, unstable, and loud with instinct | Opening survival focuses convert it into an established warren | Losing the spawn state worsens it into a hidden remnant or collapse marker | Established warren, fortified warren, absorbed warren |
| Plague immunity | Rats ignore Black Death penalties and can operate inside plague states | Plague ecology focuses improve growth in infected states | Human cure progress can reduce its offensive disease bonus, not its basic immunity | Plague ecology, weaponized ecology, King-directed ecology |
| Swarm without industry | Blocks normal human production identity | Scavenging and warren economy focuses replace missing production with growth ticks and captured supply use | If surrounded and starved, unit growth slows | Scavenger economy, tunnel economy, King levy system |
| Human terror | Rat occupation causes panic and weakens nearby human response | Human war focuses increase border disruption and refugee pressure | Strong cordons and propaganda counterplay reduce the penalty | Terror aura, organized panic, world fear |
| Nonhuman isolation | Blocks diplomacy, factions, advisors, and laws that assume humans | Rat absorption focuses convert isolation into rat-only hierarchy | If the nest fails to absorb others, it can be subordinated by the King | Isolated nest, subject warren, royal warren |

### Starting forces

The base rat army must scale with the state group that spawned it. A base rat nation should begin strong enough to survive the first human counterattack unless a prepared country contained the outbreak early.

Starting force factors:

- released infected state count
- highest disease load among released states
- total population lost in those states
- remaining population that can feed future growth
- urban density and infrastructure
- rodent pressure and rat warren pressure
- weaponized exposure
- owner weakness, occupation, and war state
- local supply state and terrain
- chaos value and evolution state

The starting force should include a core swarm, a defensive nest guard, and one archetype unit. Sewer swarms should get fast urban attackers. Ruin nests should get defensive burrow units. Port warrens should get coastal raiders only when ports and overseas spread are active. Black warrens should get heavier plague units.

### Force growth outside focuses

Base rats should grow even when the player does not finish focuses. The focus tree improves and redirects the growth, but the automatic tick is the core identity.

A base rat reinforcement tick should read:

- current rat-held plague states
- state disease load
- remaining local population
- local warren pressure
- active containment pressure from humans
- current focus route
- King command flag if the King exists
- recent losses
- supply isolation
- continent control progress

Tick outputs can be new locked divisions, strength recovery, temporary attack pressure, or template upgrades. The implementation should keep the output automatic. The player should not train mutated rats manually.

## Base rat focus tree blueprint

The base rat tree is a medium tree. It should be large enough to make rat countries playable, but it should not compete with the King tree. The goal is to make every base rat nation dangerous, specialized, and capable of becoming the King source.

### Base rat tree shape

| Lane | Role | Early focus groups | Middle focus groups | Late focus groups |
| --- | --- | --- | --- | --- |
| Waking nest | Establish control after emergence | secure spawn state, identify nest core, stabilize first swarm | choose instinct route, harden starting ideas | become King candidate or subordinate warren |
| Brood growth | Increase automatic unit generation | brood chambers, corpse feeding, tunnel nurseries | route-specific unit ticks | mass brood capstone |
| Plague ecology | Improve disease interaction | rat immunity, disease load feeding, infected roads | cure resistance, port plague routes after Evolution II | black ecology capstone |
| Human war | Fight nearby humans | night swarms, depot raids, road ambushes | breach cordons, urban shock, supply gnawing | surrounding country collapse pressure |
| Warren defense | Survive counterattack | burrow belts, hidden reserves, plague ruins | defense in infected states, retreat warrens | impossible nest defense below King tier |
| Rat absorption | Unite or consume other nests | read adjacent nest strength, challenge weaker nest | transfer states and units | claim King candidacy |

### Opening survival group

The opening group should be common to all base rat nations. It converts the emergence from a raw revolt into a playable nonhuman country.

Anchor focus group direction:

| Anchor group | Purpose | Main effects |
| --- | --- | --- |
| First nest control | Converts spawned states into stable rat-held plague states | strengthens the spawn state, sets warren core, opens automatic tick visibility |
| Swarm sense | Makes the country recognize nearby infected and threatened states | improves target selection, reveals neighboring prey in rat UI or decisions |
| Broken human roads | Uses ruined infrastructure as a defensive advantage | local movement and supply disruption for enemies in infected border states |
| Establish warren memory | Creates the base idea lifecycle | upgrades Unformed warren into a stable route-ready form |

This opening should be short. It should let a newly spawned rat country act quickly while humans are still reacting.

### Base rat instinct routes

After the opening, each base rat nation should pick one primary instinct route. These are not human politics. They are behavior families that change how the nest grows and fights.

| Route | Meaning | Strength | Cost or weakness | AI preference |
| --- | --- | --- | --- | --- |
| Burrowed citadel | The nest survives through hidden tunnels and layered defense | strong defense, slower cleanup, strong relapse pressure | slower conquest and weaker port jumps | weak isolated nests, nests facing major powers |
| Devouring swarm | The nest converts population and plague load into rapid attacks | fastest unit growth and strongest local offense | high losses, faster human world-threat response | nests near weak neighbors or high-population targets |
| Scavenger intelligence | The nest learns from human depots, radios, and factories | better captured industry use, sabotage, and absorption logic | slower pure plague growth | urban nests, port nests, nests near large stockpiles |

These routes should be mutually exclusive for base rat nations. A later King route can integrate them or choose one as a royal doctrine.

### Burrowed citadel route

Working label, not final localisation: `burrowed citadel`.

This route makes a base nest very difficult to wipe out. It suits a rat nation that starts small or faces strong human armies.

Focus group direction:

| Group | Gameplay role | Decision and mechanic hooks |
| --- | --- | --- |
| Deep nest | Adds defensive state modifiers in core warren states | unlocks maintain hidden tunnels, lowers cleanup success after state retake |
| Reserve tunnels | Improves automatic recovery after losses | reinforcement tick favors strength recovery and burrow guard units |
| Plague ruins | Turns destroyed state capacity into enemy attrition | border battles raise local disease load and supply disruption |
| False silence | Allows a defeated-looking nest to preserve relapse pressure | creates hidden warren remnants if humans retake but fail cleanup |
| Citadel capstone | Makes the nest a hard King candidate if it survives | raises King candidacy score through survival and defense |

This route should not make the nest passive. It should launch selective attacks from fortified plague states. Human counterplay should require sustained cleanup and cordon maintenance.

### Devouring swarm route

Working label, not final localisation: `devouring swarm`.

This route is the aggressive base rat path. It makes the nest spread faster, kill faster, and create more units from fresh plague states.

Focus group direction:

| Group | Gameplay role | Decision and mechanic hooks |
| --- | --- | --- |
| Feeding front | Links active combat to warren growth | battles in infected states add growth pressure and death pressure |
| Breach the cordon | Counters human army containment | unlocks attacks against cordoned states and lowers local containment strength |
| Rush the roads | Targets infrastructure and rail hubs | creates decisions or automatic pressure against supply and rail control |
| Fresh carrion cycle | Converts newly occupied populated states into stronger unit ticks | raises deaths and chaos through the shared systems |
| Swarm capstone | Makes the nest dangerous enough to consume neighbors | raises attack pressure, weakens cleanup windows, increases world-threat weight |

This route should create obvious military danger. It should also burn through state population and supply, so a swarm that expands too far can become overextended until the King organizes it.

### Scavenger intelligence route

Working label, not final localisation: `scavenger intelligence`.

This route moves a base rat nation toward the sentient arc without immediately creating the King. It is useful for urban nests, port nests, and nests that capture industry.

Focus group direction:

| Group | Gameplay role | Decision and mechanic hooks |
| --- | --- | --- |
| Learn the depots | Lets captured supply hubs and factories improve rat growth | turns captured buildings into tick multipliers instead of normal production |
| Gnaw the wires | Improves sabotage and human panic | decisions attack communications, supply, and local resistance control |
| Mimicry signs | Creates the first hint of organized nonhuman thought | raises sentience pressure without revealing King content too early to humans |
| Rat messengers | Improves rat-to-rat absorption and distant warren contact | neighboring rat strength comparison becomes easier and faster |
| Scavenger capstone | Sets the nest as a likely King source | high King candidacy score, better transfer when the King forms |

Player-facing human text should not reveal that the rats are becoming political actors at this stage. It can describe strange coordination, missing supplies, and repeated patterns through direction-only wording.

### Rat absorption lane

The absorption lane should be available to every base route, but the route should change how absorption works.

| Absorption style | Route interaction | Result |
| --- | --- | --- |
| Citadel absorption | absorbs through survival and pressure | fewer lost units, slower annexation |
| Swarm absorption | absorbs through direct strength | faster annexation, more unit loss |
| Scavenger absorption | absorbs through network and contact | better state transfer and King candidacy |

Absorption requirements should compare relative strength, adjacent state borders, disease load, rat-held state count, recent victories, and King candidacy pressure. Humans should be unable to negotiate this. If two nests border and the stronger does not act, the AI should eventually force the absorption check.

### Base rat late transition

A base rat nation can end in three broad states:

| End state | Condition | Result |
| --- | --- | --- |
| Destroyed nest | Humans retake every rat-held state and finish cleanup | tag becomes inactive, hidden remnant can remain only if cleanup failed |
| Subordinate warren | King exists and absorbs it | states, units, and route modifiers convert into King assets |
| King candidate | It controls enough states, has high sentience or dominance, and Evolution IV is active | it becomes source for the King country |

A player controlling a base rat nation should know through visible route direction that becoming the King is possible only through dominance, absorption, high plague pressure, and high chaos. Exact hidden world-end thresholds should remain in tooltips or achievement UI only where appropriate.

## King of Rats country package deepening

The King of Rats is the major nonhuman country package for the event. It is a separate country. It inherits all rat-held territory and units from lesser nests, then changes the crisis from scattered warrens into organized rat sovereignty.

### Formation and transfer package

When the King forms:

- all active rat countries transfer states to the King
- all active rat divisions transfer or are recreated under King control
- rat-held plague state markers stay active
- base rat route memory becomes King starting modifiers
- absorbed nests become regional warren entries for the King
- all human countries near rat territory receive upgraded world-threat response options
- the disease board points to the King as the central nonhuman actor
- any base rat focus tree is retired or hidden for the King

The strongest rat nation should be the default source. Strength should consider state count, unit count, disease load, deaths caused, rat absorption wins, sentience pressure, and recent military success.

### King identity states

The King country should have several visible identity states. These are not ordinary ideology variants. They are route and phase identities.

| Identity state | When active | Visible changes |
| --- | --- | --- |
| Newly crowned King | Immediately after Evolution IV | leader reveal, base royal flag, starting King ideas, inherited warrens |
| Royal command | after choosing sovereign route | stronger personal leader trait, crown-focused flag or cosmetic variant, stricter unity idea |
| Brood council | after choosing council route | collective governance portrait or council modifier, knot or council flag variant, resilient warren idea |
| Hunger mind | after choosing hunger route | more monstrous leader or animated portrait state, blackened flag variant, extreme growth idea |
| Continental sovereign | after controlling a continent or event-defined continent group | late cosmetic state, stronger fear and conquest tools |
| World-end ascendant | after completing the terminal path | world-end super-event state, terminal scenario flag, incompatible normal systems gated |

These identity states need asset coverage. The base leader portrait can be animated for the reveal or for the final world-end phase. Route portrait variants can be static unless the asset plan chooses animation for the Hunger mind or terminal state.

### King starting ideas and lifecycle

| Idea direction | Start role | Route upgrades | Failure or defeat path | Terminal form |
| --- | --- | --- | --- | --- |
| Rat sovereignty | Confirms that scattered nests are now one state | royal command makes it centralized, brood council makes it resilient, hunger mind makes it consuming | if the King loses core warrens, it becomes cracked sovereignty with penalties | world-end rat order |
| Organized swarm | Replaces base automatic growth with directed army building | route and military branches change unit type weights | heavy losses create disordered swarm until recovered | world swarm system |
| Warren administration | Nonhuman replacement for normal economy and state control | economy branch improves captured state use and plague-state extraction | loss of high-population warrens slows growth | continental warren network |
| Human dread | Gives morale and panic pressure against nearby humans | human terror branch increases it | strong human victories and propaganda reduce its local reach | global human collapse pressure |
| Crowned plague ecology | Links Black Death to the King's state | plague mastery improves deaths and spread | high cure progress reduces offensive disease effects | terminal plague ecology |

The King should not receive a pile of generic bonuses. Every major idea should tie to route, unit growth, plague behavior, conquered states, or world-end progress.

## King focus tree blueprint

The King tree is a large fixed-purpose chaos-country tree. It can have one nonhuman political identity, but it still needs meaningful internal branches. The player should feel that the King is building a civilization, army, plague ecology, and final conquest path.

### King tree architecture

| Lane | Early role | Middle role | Late role | Cross-branch links |
| --- | --- | --- | --- | --- |
| Coronation and sentience | unify nests, reveal sovereign identity | set government route | stabilize or radicalize King state | unlocks route branches and world-end preconditions |
| Government route | choose royal command, brood council, or hunger mind | route-specific country identity | route capstone shapes world-end approach | changes army, economy, plague, and AI behavior |
| Swarm command | organize inherited units | unlock King guard and command ticks | continent-scale army pressure | boosted by government and warren economy |
| Warren economy | replace human industry | use captured cities, rails, ports, and ruins | continental warren network | affects unit growth and world-end logistics |
| Plague mastery | make Black Death part of rat ecology | resist cure and spread through state network | weaponized ecology and global pressure | affects disease board and human decisions |
| Human terror | break morale and response | refugee panic, border disruption, anti-cordon attacks | major-country collapse pressure | affects neighboring states and AI reactions |
| Rat order | absorb remnants and prevent splinters | assign regional warrens | suppress internal nest rivalry | supports government stability |
| Continental conquest | prepare and execute continent control | port and overseas routes after Evolution II | continent control recognition | gates final world-end path |
| World-end path | locked until Evolution V conditions | complete terminal focus chain | trigger world-end scenario | requires territory, deaths, plague pressure, and unity |

### Coronation and sentience lane

The opening King lane should convert a violent rat event into a state-level actor. It should not take too long, because the King is already a major crisis when it appears.

Anchor focus group direction:

| Group | Purpose | Unlocks |
| --- | --- | --- |
| Gather all warrens | Consolidates inherited rat states and units | removes lesser rat country remnants, improves transfer cleanup |
| Crown memory | Establishes the King leader and central identity | leader trait, initial King idea stage, super-event trigger connection |
| Name the prey | Makes humans a strategic target category | world-threat escalation, human border target decisions |
| First rat law | Opens government route choice | royal command, brood council, hunger mind branches |
| Make the warrens count | Starts the King's internal territory ledger | regional warren assignments and economy hooks |

Player-facing direction for humans should recognize that the rats are coordinated without spoiling internal branch names. Player-facing direction for rat players can be more explicit after they control the King.

### Government route split

The government route split should be the main internal choice of the King tree. It changes how the entire country plays.

| Route | Route lock | Compatible lanes | Main payoff | Main weakness |
| --- | --- | --- | --- | --- |
| Royal command | one sovereign route | all lanes, strongest with swarm command and conquest | best coordination, fastest absorption, strongest King guard | severe penalty if the capital warren or leader state is threatened |
| Brood council | collective warren route | all lanes, strongest with defense and economy | resilience, recovery, stable growth, lower splinter risk | slower conquest and slower world-end progress |
| Hunger mind | consuming instinct route | all lanes, strongest with plague mastery and terror | extreme growth, faster disease spread, strongest world-end acceleration | weak administration, higher overextension, harsher human coalition response |

The split should be mutually exclusive. Each route should alter AI, unit tick weights, idea upgrades, leader or portrait state, flag variant, and world-end route style.

### Royal command route

Working label, not final localisation: `royal command`.

This route makes the King a sovereign predator. It is the most organized military route.

Focus group direction:

| Group | Gameplay role | Branch interactions |
| --- | --- | --- |
| Single command | raises coordination and army planning | boosts swarm command and King guard units |
| Royal warrens | assigns regional nests under central law | improves rat order and absorption cleanup |
| Crown guard | creates elite units | unlocks King guard template and stronger defensive reserves |
| Punish broken nests | prevents rat splinters and absorbs remnants | strengthens rat-to-rat annexation and inherited unit transfer |
| Royal conquest | improves war goals and invasion pacing | boosts continental conquest route |
| Sovereign capstone | makes the King stable while winning | unlocks route-specific world-end focus modifier |

Weakness design: this route should be vulnerable to targeted human counterplay if the capital warren, King leader state, or command network is threatened. Losing key warrens should temporarily reduce coordination and growth.

### Brood council route

Working label, not final localisation: `brood council`.

This route makes the King a sentient collective. It is slower but resilient and harder to decapitate.

Focus group direction:

| Group | Gameplay role | Branch interactions |
| --- | --- | --- |
| Council of warrens | turns absorbed nests into regional organs | improves rat order and reduces splinter risk |
| Shared brood memory | improves recovery from losses | boosts reinforcement tick stability and defense |
| Rotating hunger | spreads growth across states instead of one capital | improves warren economy and prevents supply collapse |
| Many-mouth planning | improves AI target safety and multi-front defense | reduces suicidal attacks and improves controlled expansion |
| Patient dominion | prepares continent conquest slowly | unlocks stronger occupation and defense in conquered regions |
| Council capstone | makes defeat harder and cleanup longer | improves relapse and warren remnants, but does not hide the terminal path |

Weakness design: this route should not conquer as fast as Hunger mind or Royal command. It wins through durability, multi-state survival, and superior recovery.

### Hunger mind route

Working label, not final localisation: `hunger mind`.

This route makes the King less like a government and more like a continent-sized appetite with enough sentience to organize conquest.

Focus group direction:

| Group | Gameplay role | Branch interactions |
| --- | --- | --- |
| One hunger | converts government stability into growth speed | boosts brood growth and plague mastery |
| No border memory | makes expansion harder to contain | lowers effect of human border controls and cordons |
| Devour the hospitals | attacks medical response and cure progress locally | boosts plague mastery and human terror |
| Empty the cities | converts populated conquered states into growth and death pressure | heavily feeds Deaths and Chaos systems |
| Hunger weather | creates broader pressure around rat-held states | raises threatened state spread risk |
| Hunger capstone | strongest world-end accelerator | unlocks harsher terminal path requirements and stronger AI aggression |

Weakness design: this route should trigger the fastest international response and carry overextension risks. It can burn through population so fast that some growth sources weaken unless it keeps conquering.

### Swarm command lane

This lane makes rat armies organized without turning them into human divisions.

Anchor focus group direction:

| Group | Purpose | Unit hooks |
| --- | --- | --- |
| Countless but directed | converts inherited swarm units into organized army categories | unlocks improved template weighting |
| Tunnel command | improves movement and recovery inside plague states | improves reinforcement spawn placement |
| King guard | creates elite sovereign or council guard units depending on government route | adds locked elite template and leader-state defense |
| Breach columns | improves offensive operations against cordons | counters army containment zones |
| Continental host | prepares armies for continent-level conquest | increases unit cap and multi-front AI use |

This lane should improve templates and tick outputs. It should not open manual human-style recruitment.

### Warren economy lane

This lane replaces normal industry with nonhuman extraction and underground logistics.

Anchor focus group direction:

| Group | Purpose | Map and decision hooks |
| --- | --- | --- |
| Scavenge the ruins | turns captured buildings into growth support | captured factories and supply hubs become tick factors |
| Under-rail nests | uses railways as hidden movement and spread routes | movement and spread bonuses along controlled rail lines |
| Port warrens | becomes relevant only with coast or Evolution II overseas spread | supports sea-jump and port defense pressure |
| Corpse fields | converts deaths into short-term growth with long-term state ruin | increases death pressure and growth, harms future extraction |
| Continental network | creates a late economy for continent control | required for stable world-end push |

This lane should interact strongly with the disease board. Human countries should see occupied high-value states become urgent cleanup targets after liberation.

### Plague mastery lane

This lane ties the King directly into the Black Death system.

Anchor focus group direction:

| Group | Purpose | Disease hooks |
| --- | --- | --- |
| Crowned disease | rat-held states become more stable disease reservoirs | infected state decay slows under rat control |
| Flea roads | improves spread from rat borders and ports | higher threatened-state pressure |
| Cure resistance | reduces effectiveness of cure progress in rat-held states | cure still lowers deaths elsewhere and should never become useless |
| Weaponized ecology | interacts with weaponized exposure if the disease was weaponized | improves Black warren pressure and accident risk around samples |
| Plague dominion | late branch needed for world-end path | raises required plague pressure and terminal unlock score |

Safety boundary: weaponization content remains gameplay-only. This lane should never describe real-world biological methods.

### Human terror lane

This lane weakens human response and increases panic. It should mostly affect neighboring or threatened states, not apply universal global penalties too early.

Anchor focus group direction:

| Group | Purpose | Human counterplay hook |
| --- | --- | --- |
| Border panic | makes adjacent human states harder to stabilize | border cordons cost more and require more units |
| Empty roads | creates refugee and movement pressure | spread risk rises through threatened state routes |
| Night gnawing | raids supply and local order | humans can counter through fortified cordons and patrol missions |
| Break the cordon | active counter to army containment zones | successful rat attacks remove or weaken local containment |
| Fear becomes policy | late branch that forces human AI to prioritize the rat threat | global cooperation and world-threat hooks increase |

This lane should have visible counterplay. Strong propaganda, victories, and successful cleanup should lower local terror pressure.

### Rat order lane

This lane manages internal rat unity, absorbed nests, and splinter prevention.

Anchor focus group direction:

| Group | Purpose | Route interaction |
| --- | --- | --- |
| Sort the warrens | records inherited regional nests | all routes need it for stable growth |
| Break rival scent | prevents base rat revival under the King | strongest under Royal command |
| Feed the little crowns | lets regional warrens grow without independence | strongest under Brood council |
| No second hunger | prevents Hunger mind splinter overload | mandatory for stable Hunger mind late game |
| One rat order | unifies all internal rat systems | prerequisite for world-end path |

This lane is where a player repairs instability after rapid conquest. Without it, the King can still be strong, but overextension and splinter pressure should rise.

### Continental conquest lane

The King should have a distinct expansion branch. It is a conquest branch, but it should still interact with plague, ports, supply, and continent control.

Anchor focus group direction:

| Group | Purpose | Requirements and payoffs |
| --- | --- | --- |
| Choose the feeding ground | identifies a continent or state group for conquest | selects primary continent target if needed by implementation |
| Break the ring | opens war goals or target pressure against neighboring humans | requires border or port access |
| Hold the infected spine | requires connected rat-held plague states | rewards supply adaptation and defense |
| Take the ports | supports overseas spread and future continent jumps | strongest after Evolution II |
| Close the continent | pushes toward full continent control | prerequisite for terminal world-end route |
| Crown the continent | marks continent-scale victory | unlocks late cosmetic state and terminal preconditions |

This lane should include AI safeguards. The King should not chase unreachable overseas targets without port access, convoy or sea-jump logic, or nearby infected ports.

### World-end path

The world-end path is locked until Evolution V. It should be visible only to the King or revealed through high-level event detail after the threat is public. It should not spoil the terminal branch before the King exists.

Prerequisite families:

- King exists
- Evolution V enabled and active
- enough rat-held states or death pressure
- at least one continent control target is fulfilled or nearly fulfilled
- rat order is stable enough
- plague mastery has reached a late branch
- world chaos is above the world-end threshold
- no terminal world-end scenario has already fired

World-end focus group direction:

| Group | Purpose | Gameplay meaning |
| --- | --- | --- |
| World appetite preparation | aligns government route, plague mastery, and conquest | prevents instant terminal trigger after King formation |
| Silence human cures | weakens global cure and containment without deleting them | makes final containment very hard, not impossible before final trigger |
| Rat-held continent proof | verifies continent control or equivalent state set | ensures the King earned the branch |
| Count the dead earth | checks deaths, rat-held pressure, or plague pressure | ties terminal state to actual devastation |
| Final warren order | locks incompatible rat splinter states | prepares the world-end scenario |
| Terminal focus | triggers the world-end scenario if all conditions still hold | sets terminal scenario and super-event through implementation rules |

Route variation:

| Government route | World-end style |
| --- | --- |
| Royal command | terminal path emphasizes command, continent coronation, and royal swarm order |
| Brood council | terminal path emphasizes distributed rat civilization and patient continent integration |
| Hunger mind | terminal path emphasizes consumption, speed, and global plague ecology |

These styles affect mechanics and assets. They do not require three separate world-end scenarios unless later implementation chooses route-specific super-event variants.

## King AI behavior

The King AI should behave like a strategic major threat.

| AI situation | Behavior |
| --- | --- |
| Newly formed | consolidate warrens, finish coronation lane, stop immediate overextension |
| Strong neighbors nearby | build swarm command and terror before major attacks |
| Weak infected neighbors nearby | attack quickly and convert states to plague states |
| Many ports controlled | pursue overseas spread and port warren economy if Evolution II exists |
| High cure progress by humans | prioritize plague mastery and attacks on medical response |
| Low internal unity | prioritize rat order before world-end path |
| Continent nearly controlled | prioritize continental conquest and terminal prerequisites |
| Severe losses | choose recovery focuses, defend warrens, and use reinforcement tick to rebuild |
| Hunger mind route | accept higher risk and attack faster, but still avoid unreachable naval targets |
| Brood council route | prefer defense, recovery, and stable expansion |
| Royal command route | prefer decisive wars and absorption of all remnants |

The AI should never use ordinary diplomacy. It should interact with humans through war, pressure, plague, and threat response. It should not accept faction invites, guarantees, non-aggression pacts, or normal peace deals unless a later implementation creates a special defeat or containment treaty.

## Defeat and aftermath handling for rat countries

### Base rat defeat

A base rat nation is defeated when humans retake all rat-held states and complete enough cleanup to remove active warren pressure. Merely occupying the state should not end the threat if disease load and hidden warren remnants remain high.

Defeat consequences:

- rat tag becomes inactive or annexed
- active rat units are removed
- retaken states remain infected or recovering until cleaned
- hidden remnant pressure can remain if cleanup was incomplete
- neighboring human countries keep monitoring decisions for a defined period
- if no rat nations remain, Evolution III can remain active but dormant

### King defeat before global end

The King should be hard to defeat. If defeated after becoming a regional or global threat, the world should receive an aftermath package only when the threat lasted long enough and controlled enough states.

Possible aftermath directions:

| Threat scale before defeat | Aftermath depth |
| --- | --- |
| Local King defeated early | cleanup events, no global aftermath super-event required |
| Regional King defeated after major war | news or report chain, regional reconstruction, memorial and disease monitoring decisions |
| Near-global King defeated | defeat aftermath super-event, reconstruction compact, long-term anti-plague systems, rat remnant hunts |

The defeat aftermath should not erase ordinary disease cleanup. The Black Death can still exist in recovering or contained states unless cure and cleanup have done the work.

### Rat player loss handling

If a player controls a rat nation or the King, defeat should be clear. The player can survive as a hidden remnant only when a specific route prepared that condition and at least one infected state still has warren pressure. A total military and cleanup defeat ends the rat country.

## Focus tree asset needs

Base rat focus icons should be a coordinated generated icon family. They should use focus-icon style, not resized idea icons. Motifs should cover nest emergence, swarm growth, plague ecology, human war, warren defense, absorption, and route-specific instincts.

King focus icons should use a richer family with sovereign, council, hunger, swarm command, warren economy, plague mastery, terror, conquest, and terminal motifs.

Key asset states:

- base rat generic leader portrait or institutional warren portrait
- base rat flag family with normal, medium, and small variants
- archetype-inspired flag variants only if implementation exposes them visibly
- King base leader portrait
- King animated reveal portrait if produced
- King route portraits or route overlays where useful
- King base flag and route flag variants
- King terminal flag or super-event image state
- idea icons for base rat lifecycle and King lifecycle ideas
- decision icons for absorption, warren cleanup, and rat growth where player-visible

All generated nonhuman portraits and flags belong to generated asset routing. No real leader or real flag source is needed for rat countries, unless implementation intentionally references a historical symbol, which this spec does not require.
