# Soviet Union Collapse Final Clean Merged Specification, Part 6
# Internal Republics, High-Chaos Splinters, Factory States, and Ancient Restorations

## Country package rule

Every republic, internal republic, high-chaos splinter, factory state, ancient restoration, and special actor must be a real package.

Required package checklist:

- tag registered
- history setup
- country localisation
- adjective and definite localisation
- ideology names where relevant
- cosmetic names where relevant
- ruling party names where relevant
- leader or council
- leader traits where relevant
- leader or council portrait
- normal flag
- medium flag
- small flag
- route or ideology flags where required
- focus tree or required focus path
- starting ideas and idea lifecycle
- decisions and decision category
- dynamically scaled starting units
- unit templates where needed
- AI strategy
- event log integration
- MTTH release or spawn logic
- local league or Free Republics' League interaction
- foreign influence interaction where relevant
- achievements or tracking where relevant
- asset manifest entry
- documentation entry
- validation note

A new playable country package must not be generic. It needs a specific identity, starting problem, political direction, map role, military style, economy, diplomacy, AI behavior, and at least one mechanic or decision family that makes it play differently.

## Required ordinary and internal republics

Implement coverage for:

- Ukraine
- Belarus
- Kazakhstan
- Estonia
- Latvia
- Lithuania
- Georgia
- Armenia
- Azerbaijan
- Uzbekistan
- Turkmenistan
- Tajikistan
- Kyrgyzstan
- Moldova
- Karelia
- Komi
- Idel-Ural or Tatarstan
- Bashkiria
- North Caucasus or Mountain Republic
- Crimea
- Siberian Regional Authority
- Far Eastern Republic
- Yakutia
- Buryatia
- Tuva
- every other Soviet Collapse republic tag defined in the implementation or source specs

Internal republics must have focus content. They cannot be empty map releases.

## Required high-chaos and evolved splinters

Implement and audit all high-chaos splinters required by the specs.

| Actor | Suggested tag | Required identity |
| --- | --- | --- |
| Kronstadt Free Soviet | KRS or equivalent | sailor and naval council state, anti-Moscow soviet identity, port and fleet mechanics |
| Green Army Congress | GRM, GAC, or equivalent | peasant and rural defense movement, local legitimacy, irregular forces |
| Union Defense Committee | UDC | loyalist non-Moscow union splinter, military district content, emergency union continuity |
| Security Directorate Zone | SDZ, NKD, or equivalent | sealed security authority, archives, prisons, internal control, intelligence mechanics |
| Basmachi Confederation | BSC, BSM, or equivalent | Central Asian old movement, cavalry, irregular routes, local league tension |
| Red Martyrs' Resurrection Cult | RMC, RMT, or equivalent | death or martyr cult, high-chaos ideology, special recruitment or legitimacy |
| Black Banner Host | BBH or equivalent | anarchist or anti-state military actor, Black Banner route, irregular expansion |
| Iron Commissariat of the Dead | ICD or equivalent | rogue Soviet death-state authority, special mechanics, grim command structure |
| Tunguska Star Committee | TSC | Siberian cosmic committee, strange science or myth route, high-chaos events |
| Pale Railway Authority | PRA | rail state, moving-state flavor, rail sovereignty mechanics |
| Dead Soldiers' Congress | DSC | veteran and revenant military memory state, dead army politics |
| Northern Revenant Fleet | NRF | Arctic naval splinter, port and fleet mechanics, naval militia or revenant fleet units |
| Civilian Factory of Russia | final available tag | construction state, factory portrait leader, civilian factory mechanics |
| Military Factory of Russia | final available tag | arsenal state, factory portrait leader, military production mechanics |
| Old Great Bulgaria | final available tag | Volga restoration, historical memory, future event hook |
| Ancient restoration states | final tags | high-chaos historical restoration packages |

If the final tag differs, the ledger must state the final tag and why it was chosen.

If a splinter is implemented as an existing tag, cosmetic tag, dynamic tag, or scripted country state rather than a new tag, the ledger must explain why that is functionally equivalent. If it is not functionally equivalent, it is a simplification.

## Factory states

### Civilian Factory of Russia

Identity:

A construction and civilian works state that treats rebuilding as sovereignty. It controls people through housing, ration cards, cement, bridge permits, work brigades, reconstruction contracts, and construction sites.

Leader direction:

Use a factory, construction site, council, or industrial administrative complex as portrait. The leader can be a board, council, or directorate.

Required mechanics:

- construction capacity
- civilian factory projects
- housing and reconstruction legitimacy
- concrete and engineer decisions
- urban planning authority
- consumer burden and labor pressure
- foreign construction contracts
- merger or rivalry with Military Factory of Russia
- high-chaos city-without-citizens route

Focus paths:

- construction directorate trunk
- governance fork
- construction strategy fork
- defense and engineers branch
- foreign contracts branch
- dark high-chaos branch
- expansion through construction cities
- late-game reconstruction state

### Military Factory of Russia

Identity:

An arsenal state that treats weapon production as sovereignty. It is ruled by production boards, military engineers, arsenal directors, guards, and armored train commands.

Leader direction:

Use factory, arsenal, or industrial military complex portrait.

Required mechanics:

- military factory projects
- arsenal quotas
- production militias
- guard divisions
- armored train and depot branch
- proxy arming
- foreign contracts
- rivalry or merger with Civilian Factory of Russia
- late-game arsenal state

Focus paths:

- production board trunk
- governance fork
- arsenal production branches
- proxy and foreign branch
- guard and armored train branch
- rival and merger branch
- expansion through arsenals
- late-game war economy

## Old Great Bulgaria near the Volga

Identity:

Old Great Bulgaria is a high-chaos Volga restoration state. It should connect to a future event and not be treated as a normal Russian regional committee.

Tone:

Historical memory, Volga identity, steppe trade, religious and cultural legitimacy, and high-chaos restored sovereignty.

Required mechanics:

- Volga legitimacy
- trade and river authority
- religion and society
- old claims and modern survival
- relationship with Idel-Ural or Tatarstan
- future event hook
- expansion and late branch

Focus paths:

- restoration trunk
- legitimacy fork
- trade and river branch
- religion and society branch
- army and defense
- diplomacy and future event connection
- rival branch
- expansion and late branch

Use sourced historical symbols where appropriate.

## Ancient and medieval restoration countries

High-chaos restoration states can appear only when chaos and regional memory support them. They are not normal breakaways.

Rules:

- they need country package rows
- they need flags and localisation
- they need at least compact focus or decision content
- they need a mechanic or route that distinguishes them from ordinary republics
- they should interact with regional leagues, neighboring republics, or Union Unmade
- they should use sourced historical symbols where possible
- fantasy-looking invention should be avoided unless the branch is explicitly high-chaos mythic

Shared decision category:

- proclaim restoration
- secure capital memory site
- gather scholars, clerics, elders, or officers
- claim old borders
- negotiate with modern republics
- raise heritage guard
- seek foreign recognition
- write the restored charter
- decide whether to remain symbolic or become expansionist

Shared focus skeleton:

- emergency restoration council
- legitimacy debate
- modern administration branch
- ancient claim branch
- army and guard branch
- diplomacy branch
- expansion branch
- high-chaos myth branch

## Evolution hooks for splinters

High-chaos splinters must be tied to real evolution tracks, not ordinary stages.

Examples:

- Kronstadt Free Soviet and Northern Revenant Fleet can connect to sailor or naval council evolutions.
- Green Army Congress and Black Banner Host can connect to Old Underground Wakes.
- Pale Railway Authority connects to Depots Choose Flags or The Flags Return Incorrectly.
- Factory states connect to The World as One Factory.
- death-state actors connect to The Dead Are Citizens.
- ancient restorations connect to Ancient Claims Return.

## AI rules for splinters

AI must respect route validity. A high-chaos actor should not appear in ordinary calm runs unless the specific conditions exist.

AI for splinters should include:

- when to expand
- when to join a league
- when to reject leagues
- when to attack Moscow
- when to attack neighboring republics
- when to accept sponsors
- when to follow its unique mechanic
- when to pursue late-game route

## Shared tree adaptation

Shared trees are allowed only when adapted.

Country-specific localisation, route names, leaders, rewards, AI weights, decisions, and icons must make shared trees feel different. If every country using a shared tree reads and plays the same, the tree has failed.
