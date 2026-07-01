# Event 015, `utopia_manifesto`, core specification

## Working identity

`utopia_manifesto` replaces the old event ID 15 identity. The old catalog row is `World Tension Subsides`, with `Reserved` details and `To Be Reworked` status. The new event is a Minor Fire-Once incident that targets a small country, gives the human player one real choice, and gives AI countries a forced acceptance path.

Working labels in this spec are not final localisation unless explicitly marked as an implementation id. The implementation agent must write final player-facing text from the direction here.

## Core promise

A small country discovers, translates, or revives an old utopian manifesto. It is recognizable as a recreation of Thomas More's island commonwealth, but the event should not become a simple idealist buff. The manifesto offers a society built around measured need, common stores, useful labor, chosen occupations, rotation through agricultural work, restrained war aims, and an islandlike civic imagination. It also carries a dangerous clause. Land can be demanded when the state claims that unused soil is needed for subsistence.

The event should make the target country feel like a strange political experiment that can be generous, disciplined, absurd, coercive, or frightening depending on how the player interprets the manuscript.

The player expectation is:

- a small nation receives a full replacement focus tree
- the country gains a visible Utopian Ledger mechanic
- the player manages need, consent, surplus, overreach, and chosen labor
- expansion is gated by need and public justification
- occupation and integration use common stores, local councils, and consent work
- a high-overreach route twists the manifesto into a doctrine for forced settlement
- AI countries always accept when eligible
- the human player may reject the manifesto and keep the old country direction

## Research basis and design translation

Thomas More's `Utopia` was published in Latin in 1516 and presents a fictional island society with social, political, and religious customs. The planning package uses that background as inspiration, not as a direct historical model. The mechanics translate major elements into HOI4 systems:

| Source theme | Gameplay translation |
| --- | --- |
| Island society and planned towns | focus branches for coastal defense, inland island mimicry, local storehouses, and the late New Utopia proclamation |
| Agriculture as shared training | rotation missions, supply resilience, infrastructure projects, and rural household service |
| People can learn another trade and follow the one they prefer unless public need overrides it | Vocation Accord mechanic with voluntary assignments, shortages, forced assignment risk, and consent loss |
| Common stores and taking according to need | Common Stores decisions, surplus aid, state integration projects, and internal ration pressure |
| No desire to enlarge bounds | claims are locked behind measured need, defensive causes, or friend protection |
| Colonies and the unused-soil claim | the controversial Needful Land doctrine, which can become a high-overreach expansion route |
| Foreign friends and neighbors | recognition, magistrate missions, aid corridors, and a Utopian League route |
| War is inglorious and should be avoided unless necessary | Just War Ledger, defensive war bonuses, arbitration missions, indirect war methods, and penalties for conquest without need |
| Gold kept for war and used to hire foreigners | Treasury Abroad variable, mercenary decisions, indirect conflict, and suspicion costs |

The central design conflict is called `More's Problem` in implementation notes. The same manifesto can support household welfare, voluntary labor, foreign aid, and anti-tyranny intervention. It can also justify forced land claims if the state decides that need outweighs consent. The focus tree should let the player decide how much contradiction the country can live with.

## Initial event direction

The entry popup is a normal country event, not a super-event. It should feel intimate and strange. The subject is an old manifesto being translated, debated, copied, and used by local reformers. The emotional center should be the people, the book, and the national response, not paperwork for its own sake.

### Visible player information

The event should tell the player:

- a manifesto has been found or revived
- it proposes a society organized around common stores, useful labor, chosen trades, and land only when need demands it
- adopting it replaces the national focus tree with the Utopian Manifesto tree
- the government will begin tracking need, consent, surplus, and overreach
- foreign countries may react with curiosity, amusement, suspicion, or fear

### Hidden information

Do not reveal every future branch. The initial event should not name the darkest route, final formable, hidden super-event, achievement paths, exact thresholds, or every possible state integration rule.

### Event options

The event has two options for a human player.

| Option role | Who can take it | Meaning | Immediate public result | Hidden or later result |
| --- | --- | --- | --- | --- |
| Embrace the manifesto | Human player and all AI | The state gives the manifesto official standing and begins the Utopian experiment | focus tree replacement, initial Utopian ideas, Utopian Ledger category, first report event | unlocks all later routes and mechanic values |
| Shelve the manifesto | Human player only | The state treats the text as a curiosity and refuses to reorganize national life around it | small one-time stability or political calm effect, event marked fired | no Utopian tree, no Utopian Ledger, no later Utopian content |

AI must always choose acceptance. If the event targets an AI country, the reject option should be hidden or have zero AI weight.

### Option tone direction

Acceptance should sound curious, bold, and slightly naive for ordinary countries. For authoritarian countries it should sound like controlled enthusiasm. For socialist countries it should lean toward common labor and distribution. For democratic countries it should lean toward public debate and councils. For neutral monarchies or paternal states it should lean toward reform under guardianship.

Rejection should sound practical and mildly dismissive, with a hint that the player is choosing normal politics over a large experiment. It should not insult the player.

Do not write final option text in the spec. The implementation agent must write final localisation from this direction.

## Target selection and eligibility

The event should usually go to a random minor country or to an eligible player country. It must not target strong countries, major powers, or countries whose scale makes the manifesto an instant world system.

### Hard eligibility

The event target must satisfy all of these:

- not a major
- not a special Chaos Redux nonhuman or terminal actor
- not a country already running a mutually exclusive event-created focus tree that should never be replaced
- not a country with a huge industry
- not a country with a huge army
- not in a terminal world-end state
- not already accepted or rejected the manifesto
- not already using the Utopian Manifesto focus tree

The industrial strength gate should be dynamic, but the initial recommended thresholds are:

| Factor | Recommended hard block |
| --- | --- |
| Total factories | over 45 |
| Military factories | over 25 |
| Dockyards | over 18 |
| Owned controlled states | over 18 |
| Fielded divisions | over 70 |
| Major power flag | always blocked |

The implementation should make the thresholds script constants. The coding agent may tune them after testing, but the event must remain aimed at minors.

### Player eligibility

A human player can receive the event only if their current country passes the same hard gates. Do not let a player major receive it just because player agency matters. If the player is too strong, event ID 15 should show as unavailable or `N/A` in the event list rather than as a zero-weight row.

### Preferred automatic targets

Weight the random selection toward countries with these traits:

- generic or shallow existing focus tree
- small to medium minor country
- independent or lightly subject status
- coastal or island geography
- low to moderate world tension exposure
- no ongoing civil war
- weak industry but enough state capacity to play a focus tree
- at least one owned state with a port, river, lake, or defensible capital, where possible

Coastal and island states should not be required. Landlocked countries can create an Inland Utopia interpretation through rail, rivers, and fortified civic corridors.

### AI target safety

The AI should not receive the event if the resulting country would be dead on arrival. Block or sharply reduce weight if:

- the country has no controlled state with a capital
- the country is within days of capitulation
- a stronger enemy occupies most of its territory
- it has no manpower and no plausible recovery path
- it is a subject whose overlord is a major at war against it and focus replacement would create an immediate invalid path

Subject minors can still receive the event when they are stable. The tree includes a subject branch for lawful autonomy, common store reforms, and eventual independence by negotiation or crisis.

## Classification and catalog direction

The new event classification should be Minor Fire-Once.

Recommended catalog direction:

| Field | Direction |
| --- | --- |
| ID | 15 |
| Event Name | final localisation required, based on `utopia_manifesto` |
| Type | Minor Fire-Once |
| Cluster | no cluster membership in the first implementation unless a later `utopian reform cluster` is designed |
| Details | describe the country discovering or reviving the manifesto and choosing whether to build a society around need, common stores, and chosen labor |
| Evolutions | only list formal logged evolutions if implementation uses them. Do not list ordinary focus progression as evolutions |
| World-End Scenario | leave empty unless a later accepted design creates a terminal scenario |
| Status | planned, then needs implementation |

The initial event should not increase chaos heavily. Acceptance should add a small amount of chaos only if the target country is AI and the experiment changes the regional order, or if high-chaos routes are opened later. Rejection should not raise chaos.

## Initial acceptance effects

Acceptance creates a starting package. Effects should be meaningful, but the first popup should not dump large permanent bonuses.

### Starting flags and variables

Set these concepts, with final ids chosen by the implementation agent:

- accepted manifesto flag
- route state `interpretation_unresolved`
- Utopian Ledger visible flag
- initial Need based on country size, supply, stability, and subject status
- initial Consent based on stability, ruling ideology, and war state
- initial Surplus based on civilian factories, infrastructure, convoys, and stockpile health
- initial Overreach at a low value
- initial Foreign Suspicion based on ideology, wars, and proximity to majors
- Vocation Balance split across agriculture, useful arts, learning, civic service, and defense

### Initial national spirits

Use a small set of deep spirits rather than many shallow ideas.

| Working idea label | Start role | Starting effect direction | Lifecycle |
| --- | --- | --- | --- |
| Found Manifesto | temporary political curiosity | opens focus replacement and first decisions | removed or transformed by early focus trunk |
| Unproven Common Stores | mixed economic strain | consumer goods burden or production disruption, stability upside if surplus is high | mitigated by warehouse and census focuses |
| Vocation Confusion | negative to production and training | people ask to choose labor under a state that lacks the machinery for it | upgraded into Vocation Accord or worsened into Compulsory Assignments |
| Foreign Laughter | diplomatic soft penalty | small relation and legitimacy problem with nearby stronger powers | removed by successful diplomacy or worsened by overreach |

### Focus tree replacement

Acceptance loads `utopia_manifesto_tree` only for the country that accepted the event. If a country already had a custom tree, this replacement must be gated by the event acceptance flag and must not affect other instances of the tag in other scenarios. If a vanilla country has unique content and is an AI, prefer not targeting it. If a human player accepts, replacement is allowed by choice.

### First decision category

Acceptance unlocks the Utopian Ledger decision category. The category should show the visible values and opening actions. It should not display every later target decision at once.

Opening decisions should include:

- conduct the household census
- open the first common storehouse
- collect craft petitions
- begin rural rotation
- invite public readers and translators
- calm foreign reaction through observers

These should use varied costs and requirements such as civilian factory burden, stability risk, equipment, convoys, trains, state infrastructure, and time. Do not make the first category a political power store.

## Rejection path

Rejection is intentionally small. The human player should feel that they refused a major alternate path.

Effects:

- mark event ID 15 as fired for that country and globally if required by the event system
- no Utopian focus tree
- no Utopian Ledger category
- optional small stability or political power effect
- optional event-log detail that the manifesto remained a curiosity

The rejection should not create a hidden punishment. The cost is lost opportunity.

## The Utopian Ledger mechanic

The Utopian Ledger is the heart of the event. It makes the manifesto playable by forcing the country to prove what it needs, what it can spare, and what it is willing to coerce.

### Values

| Value | Range | Meaning | Rises from | Falls from | Unlocks or blocks |
| --- | --- | --- | --- | --- | --- |
| Need | 0 to 100 | measured pressure for land, food, labor, ports, defense, and housing | low factories, low supply, high population strain, subject pressure, war, bad infrastructure, lost states | common stores, surplus aid, infrastructure, farms, successful integration, peace | claims, emergency decisions, arbitration, migration, forced routes |
| Consent | 0 to 100 | public belief that the manifesto is chosen rather than imposed | elections, councils, voluntary vocation, relief, defensive victories, low overreach | forced assignments, failed missions, high taxes, conquest, occupation abuses | democratic routes, peaceful league, stable integration |
| Surplus | 0 to 100 | ability to supply common stores and foreign aid | civilian factories, infrastructure, warehouses, convoys, production, peace | shortages, war, blockades, overbuilt military, failed harvest abstractions | aid, recognition, storehouse upgrades, federation leverage |
| Overreach | 0 to 100 | contradiction between need and domination | forced integration, land demands, ignored local councils, mercenary war, leader killings, high compulsion | arbitration, local consent, postwar reconstruction, abandoning claims | Marked Bounds route, backlash events, coalition fear |
| Vocation Balance | 0 to 100 | how well job choice matches public need | honoring petitions while meeting core needs | too many citizens in one vocation, forced assignments, war mobilization | production bonuses, research bonuses, shortages, assignment crisis |
| Foreign Suspicion | 0 to 100 | how threatening the experiment looks outside | claims, radical route, League growth, sabotage, mercenaries | observers, aid, defensive behavior, low overreach | guarantees against the target, diplomatic missions, rival coalitions |

All values should be dynamic. They should move through focuses, decisions, missions, wars, occupation, state control, and foreign relations.

### Value colour direction

Use consistent colours across scripted localisation and tooltips:

- Need: blue or cyan
- Consent: green
- Surplus: yellow or gold
- Overreach: red
- Vocation Balance: light purple or teal
- Foreign Suspicion: orange

### Display surface

The values should appear in the decision category header and in a scripted GUI window called by a category button when implemented. The window should be useful, not decorative. It should show:

- the six values
- current interpretation route
- current vocation distribution
- active land claims and integration projects
- neighbor and friend statuses
- current overreach warnings
- available phase actions

## The manifesto interpretation fork

The focus tree should not ask only whether the country becomes democratic or authoritarian. It should ask how literally the country reads the manifesto.

| Interpretation | Route role | Strength | Risk |
| --- | --- | --- | --- |
| Living Humanism | adapts the book into public councils, consent, and learning | high Consent, good diplomacy, strong integration | slow expansion and weaker emergency power |
| The Common Store State | treats the book as a planning manual for distribution and useful labor | strong economy, stronger Surplus, better crisis response | bureaucracy, lowered choice, compulsion temptation |
| The Island Discipline | treats the book as a defensive civic order with strict service | strong defense and stable state capacity | lower political freedom and higher suspicion |
| Guild Commonwealth | treats labor choice and useful crafts as the new constitution | industry, research, worker mobilization, solidarity | factional labor disputes and production imbalance |
| Marked Bounds | reads the unused-soil doctrine literally | fast claims, forced settlement, fear-based expansion | high Overreach, resistance, diplomatic backlash, possible civil crisis |

The first four interpretations are normal. Marked Bounds should be hidden until the country has high Need, high Overreach, a high chaos tier, or repeated failed arbitration. It can also open as a pre-fire evolved opening if the first event fires very late in a chaotic world.

## Formal evolutions

The event can work without formal logged evolutions if the implementation keeps everything inside focus and decision progression. If formal evolutions are implemented, they should represent the manifesto becoming stranger or more politically contagious, not ordinary focus milestones.

Recommended formal evolutions:

| Evolution stage | Chaos band | Working label, not final localisation | Active-event entry | Pre-fire evolved opening |
| --- | --- | --- | --- | --- |
| I | Gathering Storm | The Ledger Finds Hunger | unlocks stronger Need calculations and regional shortage events if the country already accepted | event opens with higher initial Need and more urgent common store decisions |
| II | Rising Chaos | The Island Is Imagined | unlocks island, inland-island, or port-seeking focus branch based on geography | event opens with the island branch already visible and higher foreign curiosity |
| III | Chaos Tier | The Clause of Unused Soil | unlocks the controversial Needful Land doctrine and sharper arbitration missions | event opens with Marked Bounds hints if the target has severe Need |
| IV | Totalen Chaos | Magistrates Beyond the Shore | unlocks friend, neighbor, and league growth as a regional order system | event opens with nearby minors more likely to receive observer missions |
| V | World Collapse band without terminal use | The Perfect Country Problem | unlocks final route crisis, either New Utopia or Marked Bounds backlash | event opens with stronger route pressure and faster late-tree access |

Evolutions must respect enable and disable controls. If an evolution is disabled, the core focus tree remains playable through normal branches.

## Regional and geographic adaptation

The same focus tree can serve many minor countries if it adapts visibly.

### Coastal and island countries

Coastal or island countries get stronger access to:

- harbor common stores
- fishing and convoy decisions
- coastal fortification
- island defense focuses
- maritime neighbor missions
- New Utopia proclamation requirements based on ports, forts, and controlled islands

### Landlocked countries

Landlocked countries should not feel like second-class targets. Their island idea becomes civic, logistical, and defensive:

- rail corridors act as the island boundary
- rivers and mountain passes become common frontier lines
- supply hubs and forts define the inner civic ring
- a late route can seek a peaceful port charter or a need-based coastal outlet
- the New Utopia route requires either a coastal outlet, a federated port partner, or an inland ring completed through supply hubs and rails

### Subject countries

Subject countries receive extra early content:

- common stores as proof of administrative maturity
- autonomy through useful labor reforms
- overlord inspection missions
- negotiated independence if Consent and Surplus are high
- radical separation only if Overreach or Need are severe

### Tiny one-state countries

One-state countries receive compressed early scaling:

- lower storehouse project costs
- sharper foreign suspicion if they claim land
- easier civic consensus
- limited expansion options until Need has been proven through missions
- stronger dependence on diplomacy or league route

## Foreign reaction model

Foreign countries should not react all the same way.

| Foreign actor | Ordinary reaction | Suspicion trigger | Friendly trigger |
| --- | --- | --- | --- |
| Nearby minors | curiosity, jokes, requests for aid | claims nearby land or raises Overreach | receives surplus aid or magistrates |
| Nearby majors | mild contempt or watchfulness | Utopian country gains claims, forms League, hires mercenaries | Utopian country stays defensive and sends aid |
| Ideological rivals | propaganda mockery | route changes ideology or sponsors opposition | low if relations and trade are good |
| Subjects and colonies | interest in common stores and autonomy | Utopian country uses forced settlement | Utopian country backs consent integration |
| Existing factions | evaluate usefulness and weirdness | League competes for members | Utopian country helps a faction member defensively |

Foreign Suspicion should create consequences such as guarantees, observers, sanctions, hostile propaganda, or rival aid to targeted neighbors. It should not become an instant world war switch.

## Event log and detail direction

Event ID 15 must appear in the event log under its new identity. The event detail should describe the premise and the country-level experiment. It should not list modifiers, focus ids, achievements, hidden routes, or exact future thresholds.

Event detail direction:

- mention a small country reviving a manuscript about common stores, useful work, chosen trades, and land measured by need
- mention that the country can accept or reject the experiment if controlled by a player
- mention that acceptance replaces the focus tree and opens the Utopian Ledger
- keep the dangerous land clause implied through public debate, not fully explained as a future war route

## Connections with existing Chaos Redux systems

The event should interact with existing systems only where the connection improves play.

| System | Connection |
| --- | --- |
| Chaos Meter | small increases from extreme overreach, forced settlement, and regional order shifts. Peaceful routes can lower small amounts through aid or peace arbitration |
| Event Logs | event detail and optional formal evolution rows |
| Super-events | late route proclamation or dangerous doctrine reveal can use super-event treatment |
| Condemnation | only if high-overreach route uses atrocities, forced expulsions, or prohibited warfare through other systems. The baseline event should not touch condemnation |
| Deaths | not a core system. It should only be touched if wars or existing Chaos Redux death systems do so normally |
| World threat | do not use the world threat framework unless a later implementation turns Marked Bounds into a genuine world crisis. The first implementation should stay regional |
| Triggerable scenarios | not required by this spec. If later added, it should test a minor country acceptance setup with intensity controlling starting Need and Overreach |

## Balance posture

The Utopian country should be interesting, not free. It starts with awkward ideas and needs early state-building. Its power comes from focused civic systems and route decisions rather than huge starting buffs.

Balance target:

- stronger than a generic minor after 18 to 24 months of successful play
- weaker than a major unless it grows through diplomacy, integration, or conquest
- peaceful routes gain stability, integration, and diplomacy
- coercive routes gain claims and speed but create backlash and resistance
- industry routes require storehouse and vocation management
- military routes require equipment, XP, manpower, and defensive objectives
- no decision family should be a flat political power purchase loop

## Abuse prevention

The implementation must prevent:

- targeting majors or strong industrial countries
- free core spam on occupied states
- claim spam against large powers
- repeated state integration without compliance, infrastructure, local support, or time
- vocation decisions that farm research or production with no shortage risk
- mercenary unit loops with no cost or foreign suspicion
- league membership farming with dead or invalid countries
- AI taking claims against a much stronger neighbor without defensive logic
- player accepting the event, taking early bonuses, and switching back to an old tree

## Documentation outputs needed after implementation

Implementation should update:

- event script for ID 15
- event classification and random-event registration
- event name and detail localisation
- Utopian Ledger decision category and scripted localisation
- focus tree assignment and focus localisation
- ideas, decisions, missions, and AI strategy
- optional super-event assets and audio package if late route super-events are implemented
- docs/events/015_utopia_manifesto.md
- event catalog workbook after final in-game text exists

