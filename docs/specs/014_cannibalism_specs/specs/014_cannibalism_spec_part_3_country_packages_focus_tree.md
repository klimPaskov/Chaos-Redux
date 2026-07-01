# Event 014 Cannibalism, country packages, focus tree, and formables

This file continues the Event 014 source design. All names are working labels and not final localisation.

## When a cannibal country appears

Cannibal countries should appear only after Evolution II, through failed containment, triggerable scenarios, or high-chaos rare openings. The first ordinary firing should not spawn a country unless the scenario is explicitly set to begin at that intensity.

A cannibal country is a special chaos country. It begins as a human death-cult or military commune. It should become an actual nonhuman country only if Evolution III or Hannibal mechanics create a clear monstrous transformation.

The implementation should use one primary placeholder tag until final tag allocation is known.

Recommended placeholder tag: `CBL`.

Possible origin flags:

- `cannibal_origin_island`
- `cannibal_origin_front`
- `cannibal_origin_prison`
- `cannibal_origin_colony`
- `cannibal_origin_exploit_mutiny`
- `cannibal_origin_hannibal`

Origin should affect starting units, focus branch weights, assets, and AI.

## Cannibal country package matrix

| Surface | Design requirement |
| --- | --- |
| Tag | Use a custom tag if available. If shared tags are scarce, use one reusable tag with cosmetic identity and origin flags. |
| Spawn state | Prefer remote islands, cut-off ports, isolated colonies, mountain pockets, jungle pockets, or occupied territories with severe cult pressure. |
| Capital | Use the origin state unless it lacks infrastructure. For islands, use the port state. For prison origin, use the state containing the prison chain or nearest controlled victory point. |
| Cores | No broad free cores. Start with no full cores outside origin territory. Use temporary compliance and terror control instead. |
| Claims | Claims can spread to adjacent hunting corridors and island chains through focus or decisions. |
| Ruling ideology | Fixed high-chaos authoritarian or death-cult neutral ideology unless the mod has a dedicated ideology. The spec should avoid generic fascism unless that fits the origin government. |
| Party names | Use route-specific cult, commune, military kitchen, or Hannibal network names. Final names belong to localisation. |
| Leader | Generated fictional leader or council. If Hannibal exists and takes over, use the Hannibal package from the future Hannibal event. |
| Leader portrait | Generated fictional portrait or council portrait with gore and ritual imagery. Hannibal portrait comes from the Hannibal event if implemented. |
| Advisors | Mostly internal officers, scavenger logisticians, terror preachers, prison wardens, convoy raiders, island pilots, and cult surgeons. |
| Starting ideas | Severe supply hunger, cannibal command, hunted world, local depopulation, unstable obedience. These ideas should be few and staged. |
| Starting army | Dynamic irregular formations from garrisons, defectors, prisoners, cult cells, and local recruits. |
| Starting navy | Only if island or port origin. Small convoy raider or captured patrol profile, not a full navy. |
| Starting air | Only if airfield origin. A few captured scout planes or no air force. |
| Economy | Very weak ordinary economy. Gets manpower and temporary supply through consumption mechanics and raids, at severe death-system cost. |
| Diplomacy | Hostile to normal countries. Can form cannibal pacts with other cannibal actors. Hannibal branch can coordinate globally. |
| AI | Aggressive but supply-aware. It should prefer weak neighbors, ports, prisons, and high-population states once it can reach them. |
| Assets | Generated flags, leader or council portrait, focus icons, idea icons, decision icons, report images, news images, super-event images, animated UI states. Gore is required. |

## Starting forces

Cannibal countries must not spawn empty. Their starting army should scale from origin and severity.

### Force sources

- isolated garrison defectors
- prison guards and prisoners
- deserters from the owner country
- cult cells inside compromised units
- local militias coerced into service
- convoy raiders on island routes
- captured depots and abandoned equipment
- Hannibal-linked cadres after the future event exists

### Template families

| Template family | Role | Origin fit | Notes |
| --- | --- | --- | --- |
| Hunger columns | main irregular infantry | all origins | low equipment need, high attrition, poor defense, frightening attack bonuses under high cult pressure |
| Butcher packs | shock detachments | prison, exploit mutiny, Hannibal | small, high attack, low staying power, high casualty and death-system side effects |
| Garrison gnawers | defensive island or pocket units | island, colony, front | low movement, strong local defense, poor offensive use |
| Scavenger parties | raiding light infantry | front, island, colony | good movement and supply capture, weak in prolonged battle |
| Prison processions | coerced manpower units | prison | large manpower pool, low organization, risk of collapse if cult pressure falls |
| Hannibal cadres | elite special branch | Hannibal only | rare and dangerous, should require Hannibal power and global cult strength |

### Starting force scaling

Weak opening:

- one to three irregular divisions
- poor equipment
- no reliable commander
- one state or island only

Normal opening:

- three to six irregular divisions
- one shock detachment if cult pressure is high
- enough infantry equipment to fight locally
- one origin commander or council trait

Severe opening:

- six to ten divisions
- multiple state modifiers already active
- captured equipment stockpile
- stronger local recruitment decisions

High-chaos opening:

- ten or more divisions only if the origin has enough population or garrison basis
- stronger morale and terror bonuses
- worse supply weakness
- immediate world reaction and containment response

### Reinforcement pathways

Reinforcement should come from actions, not free timer spam.

- consume local population in controlled hunting-ground states, adding deaths and reducing state manpower
- raid prisoner camps for coerced manpower
- seize field kitchens and supply depots
- capture convoys from island routes
- turn exploited terror units from other countries
- recruit through cult cells in high fear states
- receive Hannibal cadres if the Hannibal event exists
- complete focus branches that turn irregulars into structured packs or supply-aware raiders

Every reinforcement source should raise risk, deaths, fear, or condemnation. Cannibal countries should grow by making the map worse.

## Starting idea lifecycle

| Idea working label | Start or unlock | Role | Mitigation or upgrade | Failure or corruption | Final forms |
| --- | --- | --- | --- | --- | --- |
| Commune of Hunger | start | defines the cannibal government and gives irregular war bonuses with severe diplomatic isolation | can become ordered cult under Hannibal or devolve into packs | if discipline collapses, units splinter and raid randomly | Hannibal order, island commune, broken packs |
| No Common Rations | start | ordinary supply and production are terrible | scavenger logistics branch reduces penalties | famine worsens if raids fail | scavenger state, empty larder |
| Hunted by the Living | start | normal countries hate and fear the tag | pact branch can coordinate with other cannibal actors | defeat or containment pressure grows if isolated | world threat, last island |
| The Eating Ledger | unlock by state control | tracks consumption as a power source and a death-system driver | can be slowed by restrained doctrine branch | can become runaway consumption | global table ledger |
| Hannibal's Discipline | Hannibal branch only | transforms loose cults into a strategic network | strengthened by Hannibal victories | impossible if Hannibal dies or never exists | world-end preparation |

## Shared cannibal focus tree architecture

The cannibal country should receive a full shared focus tree because it can become a serious fighting actor. The tree can adapt by origin flags. It should be fixed-purpose but still have real internal choices.

### Architecture map

```text
Opening survival trunk
  -> secure origin state
  -> count garrison and prisoners
  -> choose supply method
  -> choose command hierarchy

Command hierarchy fork
  -> council of knives route
  -> warlord kitchen route
  -> Hannibal discipline route, hidden until Hannibal exists

Supply and economy branch
  -> scavenger logistics
  -> depot raids
  -> prisoner ledger
  -> hunting-ground administration
  -> restrained consumption or runaway consumption fork

Military branch
  -> hunger columns
  -> butcher packs
  -> scavenger parties
  -> prison processions
  -> Hannibal cadres if hidden route active

Expansion branch
  -> island chain raids for island origin
  -> port seizure route for coastal origin
  -> prison road route for inland origin
  -> mainland hunting corridors
  -> cannibal pact or solitary rampage fork

World threat branch
  -> public reveal
  -> global courier routes
  -> Hannibal takeover or leader council hardening
  -> Last Table formable path
  -> world-end preparation if chaos and Hannibal power allow
```

### Opening survival trunk

Purpose:

- proves the country can fight
- sets origin identity
- gives immediate but unstable survival tools
- opens the first military and supply branches

Reward direction:

- starting commander or council trait
- small equipment stockpile from captured depots
- one-time irregular division package scaled by origin
- unlocks local hunting-ground decisions
- sets focus filter tags for cannibal military, supply, expansion, and high-chaos routes

Avoid:

- generic political power
- many separate new ideas
- free factories without a story

### Command hierarchy fork

Council of knives route:

- collective leadership
- better internal obedience
- slower expansion
- lower random unit splinter risk
- can create a council portrait and animated council seal

Warlord kitchen route:

- one brutal commander
- stronger shock units
- higher splinter and coup risk
- easier raids
- less stable diplomacy even with cannibal actors

Hannibal discipline route:

- hidden until Hannibal exists or is connected
- changes leader or overlord relation if the Hannibal event owns the actor
- unlocks global courier, elite cadres, and world-end preparation
- should not be available if Hannibal is dead, absent, or blocked by future event rules

### Supply and economy branch

The economy branch should not make the cannibal country normal. It should make its abnormal supply system playable.

Focus groups:

- captured depot inventory
- field kitchen conversions
- convoy ambush plans
- prisoner ledger administration
- hunting-ground extraction
- corpse-borne disease avoidance if disease systems are active
- restrained consumption versus runaway consumption

Restrained consumption reduces deaths and keeps units supplied longer. Runaway consumption gives faster short-term growth and stronger fear, but damages states, increases chaos, and speeds global response.

### Military branch

The military branch should give route-specific units and templates.

Focus groups:

- hunger column organization
- scavenger party mobility
- butcher pack shock doctrine
- prison procession coercion
- anti-partisan fear tactics
- commander recruitment
- night assault and island landing methods
- Hannibal cadre branch if hidden route is active

Military payoffs should unlock decisions and template improvements. Avoid repeated free divisions.

### Expansion branch

Expansion depends on origin.

Island origin:

- seize nearby islands
- raid convoys
- establish silent anchorages
- threaten mainland ports
- create a hidden landing mission

Coastal origin:

- seize ports
- raid shorelines
- use evacuation flows as spread routes
- attack prison islands or hospital ports

Inland origin:

- control rail corridors
- hunt along prison roads
- target supply hubs and depots
- turn occupied villages into hunting grounds

Expansion should create claims or war goals gradually. It should not grant broad cores. Controlled states receive hunting-ground or fear modifiers and require post-capture consumption decisions.

### Cannibal pact or solitary rampage fork

If multiple cannibal actors exist, they can form a pact or fight.

Pact route:

- shared courier routes
- limited non-aggression between cannibal actors
- coordinated attacks against normal countries
- stronger Hannibal takeover chance

Solitary rampage route:

- stronger individual war goal generation
- cannibal actors can fight each other
- lower Hannibal coordination unless Hannibal conquers them

AI should prefer pact if weaker or if Hannibal exists. AI can prefer solitary rampage if strong, isolated, and high chaos.

## Formable and transformation routes

### Last Table formable

Working label, not final localisation: `Last Table`.

This is a hidden high-chaos formable or cosmetic transformation for a cannibal country. It should be revealed only after the actor controls enough hunting-ground states, survives long enough, and proves it can project power beyond its origin.

Requirements direction:

- Evolution III active
- cannibal country controls a significant number of states with hunting-ground or active cult modifiers
- controls at least one port or capital route unless inland origin has a major rail corridor substitute
- has defeated or consumed a major containment mission
- public fear or global cult pressure is high
- no full world-end yet

Effects direction:

- change cosmetic tag and flag
- strengthen shared focus tree end branch
- set world threat source
- unlock global courier route decisions
- add severe diplomatic reactions
- no instant broad cores
- opens integration or consumption projects for controlled regions
- can trigger a super-event if global visibility is high

### Hannibal dominion transformation

Working label, not final localisation: `Hannibal Dominion`.

This transformation is blocked until the future Hannibal event exists. It should be implemented as a hook in Event 014, not as a finished route until the Hannibal spec exists.

Requirements direction:

- Hannibal exists and is active
- Hannibal has access to a cannibal country or enough cult pressure in multiple countries
- cannibal network reached Evolution III
- enough states, deaths, or cult nodes exist
- chaos exceeds world-end preparation thresholds for the terminal branch

Effects direction:

- Hannibal takes over, inspires, puppets, or coordinates the cult depending on Hannibal implementation
- global world-threat source becomes severe
- hidden Hannibal branch opens in cannibal focus tree
- world-end scenario can become eligible after chaos exceeds the world-end threshold

## Ordinary countries and focus trees

Ordinary countries should not receive full focus-tree replacements from Event 014. They receive decisions, ideas, events, scripted GUI, and possible crisis branch hooks if they already have a relevant focus tree.

Additive focus hooks can be used for major countries or player countries:

- emergency army discipline focus reward can lower discipline collapse
- supply reform focus can lower hunger pressure
- prison oversight focus can lower spread pressure
- authoritarian terror focus can unlock exploitation path but raises Hannibal resonance
- island defense or colonial administration focus can reveal silent island missions

Implementation should not replace an existing meaningful tree because of cannibalism. Existing tags should keep their trees and receive additive crisis mechanics.

## Defeating a cannibal country

Defeating a cannibal country should have aftermath.

Possible defeat outcomes:

- state modifiers remain for cleanup
- hidden cult survivors can persist if the attacker used secrecy or exploitation
- captured archives reveal spread routes
- countries that contained the original outbreak can still fight the cannibal country militarily
- if the threat had global reach, a defeat aftermath super-event can fire
- victorious countries can receive reconstruction, tribunal, and trauma decisions

The world should not reset instantly after a large cannibal state dies. The local states need cleanup and the global network may have nodes elsewhere.
