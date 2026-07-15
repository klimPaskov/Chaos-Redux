# Event 014 Cannibalism, Part 4: Country Packages

## Country-package philosophy

Cannibal countries are serious fighting actors. A tag, flag, leader, and a few militia divisions are not enough. Every country created by Event 14 needs a complete playable package with an origin, territory, political identity, military role, economy, recruitment loop, focus access, decisions, AI, assets, and cleanup.

Pre-unification countries are human extremist chaos countries. They belong in the shared special-chaos-country classification. They do not belong in the actual-nonhuman classification unless a later transformation changes their nature.

The unified Hannibal country remains human at first, even though its institutions and soldiers are becoming monstrous. A separate final transformation or the Wendigo branch can move the country into actual-nonhuman classification where shared systems require that distinction.

## Tag allocation

The implemented country contract uses eight reusable regional warlord slots, `CBA` through `CBH`, one ordinary unified country, `CBL`, and an in-place transformation of the existing original `ZZZ` country with the `ZZZ_CANNIBALISM_HANNIBAL` cosmetic identity.

The eight warlord slots are origin-agnostic and should be reusable after a country is fully eliminated and cleaned up, provided no history, character, flag, decision, focus, or global target still references the old incarnation. Any available slot can carry an Island Host, Siege Commune, or March Host package selected from the actual origin state.

Each slot has a distinct portrait for Europe, Asia, Africa, the Middle East, North America, South America, and Oceania. The complete matrix contains 56 portraits. The actual origin state's stored region chooses the portrait and male name pool together. That region and portrait survive submission and commander reconstruction at unification. An unsupported or missing region prevents formation instead of selecting a generic face.

A released slot must record:

- origin country
- origin state group
- origin archetype
- release date
- current warlord character
- current policy route
- current Network Alignment
- whether the event actually created the tag

Existing countries must never have their focus trees replaced merely because a placeholder tag or cosmetic identity collides. Event-created flags must gate runtime focus assignment.

## Public naming rules

Country names must be short regional public names. Working patterns include:

- `[Region] Host`
- `[Island] Host`
- `[Region] Commune`
- `[City] Commune`
- `[Mountain or River] Host`

These are naming directions rather than final localisation. The final name should use a recognizable state, island, city, river, mountain, or region connected to the actual spawn territory.

Do not use racial, ethnic, or real tribal labels. Do not use administrative map names such as Feeding Office, Ritual Bureau, Military Larder Authority, or Cannibal Board as the map name. Those can be internal institutions or focus groups.

The adjective should remain readable. The country may later receive a route-specific cosmetic name after Evolution II, but the name must continue to identify a country rather than an agency.

## Generic warlord leaders

Every pre-unification country receives one generated male warlord.

### Portrait direction

- bald head
- blood on skin, clothing, hands, or mouth
- physically intimidating, visibly scarred, feral, and deranged rather than merely stern
- less conventionally human-looking through grounded human-origin traits such as pallor, bloodshot eyes, asymmetry, damaged ears, irregular teeth, extreme posture, and predatory expression
- rough hides, raw cloth, damaged work clothes, scavenged webbing, damaged helmets, or torn period uniforms
- period-compatible weapon or command prop when composition allows
- at least one of the 56 regional portraits must hold a skull and visibly lick a dark-crimson smear from it. The other portraits need different behaviors and props rather than repeating that pose
- no modern objects
- no readable text
- no real Indigenous, African, Pacific, or religious ceremonial regalia
- no resemblance to Hannibal
- no supernatural antlers, elongated limbs, glowing eyes, or Wendigo traits

The art direction uses invented rough survival clothing and post-collapse scavenging. It must not describe the clothing as tribal, copy a living culture, or borrow sacred and ceremonial motifs.

### Name direction

The portrait is male-presenting, so the character uses a male name pool and male metadata. Each slot should select from a small regional pool based on the origin state. The name should sound plausible for the language region and 1930s to 1940s setting.

An epithet can follow the personal name. Epithets should reference battlefield, place, wound, method, or rank. They must not be generic office titles and must not expose Hannibal.

### Leader traits

A warlord receives one origin trait and one personality trait.

Origin traits:

- Island Reaver
- Siege Butcher
- March Predator

Personality traits:

- Hoarder
- Feast Captain
- Charismatic Initiator
- Suspicious Tyrant
- Network Disciple
- Defiant Mouth

These are working labels, not final localisation.

## Warlord origin archetypes

### Island Host

#### Formation conditions

- island or isolated coastal state
- valid port or landing site
- mature island commune
- failed relief, evacuation, or reconnaissance sequence
- enough population and garrison strength to form a country

#### Starting problem

The Host has limited industry, poor repair capacity, and severe dependence on captured shipping. It is difficult to invade but can starve if blockaded.

#### Starting military

- port garrison warbands
- scavenged infantry
- one raider or marine-style formation when local equipment supports it
- captured patrol craft or convoy capacity where engine support and map conditions allow
- weak air force unless an airbase and captured aircraft exist

#### Recruitment path

- raid convoys
- seize coastal towns
- convert prisoners and isolated garrisons
- build island larders
- train landing parties

#### Special decisions

- disappear a convoy
- establish a silent anchorage
- raid a nearby island
- convert a prison hulk
- force a night landing

#### AI role

- protects ports
- raids weak shipping
- avoids suicidal mainland invasion until Larder and transport are sufficient
- aligns with the network when blockade pressure is high

### Siege Commune

#### Formation conditions

- urban state, fortress, occupied city, or prolonged encirclement
- mature cell and failed relief
- defensible contiguous territory

#### Starting problem

The Commune has dense population and captured buildings, but it is surrounded, bombarded, and unable to replace heavy equipment easily.

#### Starting military

- urban assault warbands
- former garrison and police units
- tunnel or fortification units represented through modifiers and decisions
- captured artillery when local stockpiles justify it

#### Recruitment path

- seize hospitals and prisons
- recruit through ration control
- fortify feeding districts
- break relief columns

#### Special decisions

- open a hidden tunnel route
- seize a ration district
- turn a factory into a larder
- stage a night sortie
- display prisoners to break a siege

#### AI role

- defends urban terrain
- targets relief hubs
- accepts high casualties to break encirclement when Frenzy is high

### March Host

#### Formation conditions

- compromised field formations refuse orders
- central command collapses in a contiguous frontline area
- enough defecting units and captured equipment exist

#### Starting problem

The Host has the strongest mobile opening and the weakest civilian base. It must keep moving or starve.

#### Starting military

- defected infantry
- captured trucks and cavalry where available
- one elite shock formation scaled from the original compromised unit
- light artillery or armored equipment only when actually captured

#### Recruitment path

- absorb defeated units
- seize depots
- harvest battlefields
- recruit prisoners
- create mobile feeding columns

#### Special decisions

- consume the battlefield
- break a retreat route
- seize a rail depot
- force-march through a weak front
- abandon a depleted larder

#### AI role

- seeks weak fronts and supply hubs
- avoids static defense unless a city or port is captured
- can become the strongest unification host through rapid conquest

## Dynamic state selection for country formation

A country should receive a coherent map package.

Selection priorities:

1. The mature commune or cell state is always the capital candidate.
2. Adjacent controlled states can join when they share the same active cult network and form a defensible region.
3. Island groups can include nearby islands connected by ports and the same cell route.
4. States with no connection, no port access, and no active cell should not be transferred merely to increase size.
5. The parent country keeps a core claim and gains liberation or containment tools.
6. The new country receives temporary cores or strong control modifiers only where the cult actually dominates.
7. Large culturally mixed conquests remain claims or occupation territory until route decisions process them.

Country creation should avoid tiny impossible enclaves where the new tag has no supply, capital access, unit space, or path to survive.

## Starting politics

### Ideology

The country uses a dedicated event ideology or a verified existing extremist ideology framework. The public party and state form should describe the local cult rule without implying Hannibal's identity.

### Ruling structure

The default is personal warlord rule with subordinate captains. Focus routes can shift toward:

- feast council
- pack-captain confederacy
- centralized personal tyranny
- network-aligned command

### Stability and war support

Warlord countries begin with high war commitment and low conventional stability. Their internal cohesion comes from Larder, Frenzy, fear, and leader authority rather than normal civic legitimacy.

### Diplomacy

- immediate wars with the origin country and relevant controllers
- severe opinion penalties from ordinary countries
- limited normal diplomatic access
- no automatic faction with other warlords before network conditions
- conditional nonaggression, tribute, or submission between cult actors

## Starting economy

Warlord economies are predatory and improvised.

Core strengths:

- captured military factories and depots are used quickly
- low consumer expectations
- scavenging and captured-equipment conversion
- Larder resource converts population consumption into recruitment and operations

Core weaknesses:

- low civilian construction efficiency
- poor repair outside controlled larders
- weak research base
- unreliable trade
- high dependence on conquest
- severe collapse when Larder reaches starvation levels

The countries should be dangerous at birth but unable to survive indefinitely through passive bonuses.

## Starting military package

Starting forces scale dynamically.

### Weak opening

Use when the state has low population, few garrison units, low chaos, and limited captured equipment.

- two to four irregular formations
- one organizer cadre
- poor equipment ratio
- local defensive bonus

### Normal opening

Use when a mature commune controls a substantial state or several formations defect.

- four to eight warbands
- one specialist origin unit
- captured support equipment
- one commander or promoted warlord lieutenant

### Severe opening

Use when a large garrison, major urban complex, or multiple units join at high chaos.

- eight to fourteen formations
- several origin specialists
- meaningful artillery, trucks, or captured armor when present
- stronger initial Larder and Frenzy

### High-chaos opening

Use when Evolution II is mature and the country is one of several network actors.

- twelve to twenty formations scaled to territory and population
- experienced organizer cadres
- coordinated offensive mission
- direct network reinforcement access

The package must draw equipment from local stockpiles, defecting formations, captured depots, and dynamic grants that fit the origin. It should not duplicate free equipment or create infinite unit loops.

## Unit families

These are role directions rather than final names.

### Scavenger Warband

Basic irregular infantry with high attack, low defense, low reliability, and cheap conversion from captured equipment.

### Feast Cohort

More organized infantry unlocked through Larder and hierarchy focuses. Strong organization recovery and breakthrough, high manpower and Larder demand.

### Bone Guard

Elite guard for the warlord or later Hannibal. Small cap, strong combat, expensive equipment, high experience.

### Carrion Riders

Mobile cavalry or truck formations available to March Hosts and suitable terrain routes.

### Island Reavers

Marine or raider formation for Island Hosts. Strong landing and coastal combat, convoy and fuel dependent.

### Siege Eaters

Urban assault and engineer-heavy unit for Siege Communes.

### Network Cadre

Small organizer formation that improves foreign seeding, local recruitment, and coordination. Limited in direct combat.

No Wendigo unit appears in ordinary warlord packages.

## Reinforcement pathways

Warlord countries gain units through action:

- consume controlled population and spend Larder
- capture depots and equipment
- defeat or encircle enemy formations
- seize prisons
- complete origin-specific focus groups
- receive volunteers or transfers from aligned warlords
- absorb communes
- gain network reinforcement at Evolution II

Every unit decision should have a cap, escalating burden, territory requirement, or resource cost. Population consumed for recruitment is removed through the Deaths system and cannot be reused.

## Ideas and lifecycle

### Starving Warband

Starting mixed idea.

- strong attack urgency
- poor supply and defense
- severe penalties when Larder is empty

Upgrade paths:

- disciplined feeding army
- mobile predation doctrine
- island raider system
- siege larder system

Failure path:

- warband devours itself through internal purge and manpower loss

### Broken Chain of Command

Starting negative idea.

- poor coordination
- officer rivalry
- low planning

Mitigation:

- personal tyranny
- feast council
- pack-captain confederacy
- network alignment

### Hunted by All

Starting diplomatic and intelligence penalty.

Can be transformed into:

- terror prestige
- hidden network shelter
- raider diplomacy

It should never become normal international legitimacy.

### The First Larder

State-linked starting idea or mechanic marker.

Upgrade paths:

- protected feeding district
- mobile larder train
- island store network
- prison harvesting system

### Origin idea

Each archetype receives a distinct origin idea with a full lifecycle.

## Local warlord route identities

### Personal tyranny

The warlord destroys rival captains, centralizes Larder, and builds an elite guard.

Strengths:

- powerful leader and guard
- fast decisions
- high purge capability

Weaknesses:

- succession risk
- low officer depth
- vulnerable if the warlord dies or is captured

### Feast council

Several captains divide territory and victims through a formal council.

Strengths:

- better administration
- more commanders
- stable recruitment

Weaknesses:

- slower decisions
- faction conflict
- easier network infiltration

### Pack-captain confederacy

Local warbands retain autonomy and coordinate through raids.

Strengths:

- mobile warfare
- high resistance to decapitation
- distributed recruitment

Weaknesses:

- weak central industry
- hard to unify
- lower Network Alignment

### Network disciple

The warlord accepts common doctrine and shared orders without knowing or publicly naming the supreme coordinator.

Strengths:

- coordinated offensives
- foreign cells
- unification rewards

Weaknesses:

- loss of independence
- future absorption risk

### Defiant mouth

The warlord rejects outside control.

Strengths:

- independent route
- anti-absorption tools
- local identity and strong personal army

Weaknesses:

- hunted by aligned warlords
- excluded from network reinforcement
- likely target during Hannibal's reveal

## Unified Hannibal country package

The unified country appears only after the reveal.

### Host selection

The host should be selected by:

- player-control preservation
- controlled population and states
- Larder Stores
- military strength
- number of submitted warlords
- network centrality
- valid capital and supply

A player-controlled warlord should become the host where safe. The player should not lose control because an AI warlord has a slightly higher score.

### Public identity

Final name research and localisation can use Hannibal after reveal. The map name should be a direct country name, not an administrative institution. Route-specific cosmetics can distinguish centralized, confederated, or transformed forms.

### Leader

Hannibal Lecter is the male leader created by Event 14. The alternate-history portrait must remain consistent across the ordinary and transformed routes without copying a specific screen actor.

Portrait direction:

- distinctive bald or closely shaven head
- calculated intelligence rather than generic screaming rage
- ritual scars and blood
- heavy primitive and military hybrid clothing
- enough visual continuity with warlord society to feel like its unifier
- no visible presence in any earlier asset

### Politics

Hannibal replaces or dominates the local ruling structure. Warlords become characters with dispositions:

- commander
- governor
- lieutenant
- servant
- rival
- purge target

The player's prior route influences the unification settlement. A confederated host can retain more warlords. A tyrannical host can purge them for immediate power. A network-disciple host receives the smoothest absorption.

### Economy

The unified economy converts a regional predatory system into a continental war machine.

- Larder is centralized
- controlled states enter graded consumption
- recruitment and production use population, captured equipment, and conquered industry
- logistical penalties fall as the route develops
- final capstones remove ordinary limits and create absurd special-chaos power

### Military

- warbands are integrated into legions
- origin specialists remain available
- aligned warlords become commanders
- captured equipment conversion expands
- enemy casualties and population loss feed recruitment under strict anti-loop accounting
- final routes gain overwhelming offensive and recovery tools

### Diplomacy

The unified country becomes a world-threat source, receives global hostility, and can issue terror ultimata, absorb aligned warlords, seed foreign cells, and attack coalition anchors.

## Wendigo Hannibal country package

The branch uses the existing original `ZZZ` Wendigo country in place. It preserves its territory, units, technologies, ideas, equipment, special-project state, and active player control rather than replacing the country or rebuilding its OOB.

### Merge rules

- branch evaluates at Hannibal unification
- if a valid Wendigo country exists, the alternate merge becomes available or automatic according to campaign conditions
- player control is preserved whether the player controls the cannibal host or the Wendigo country
- all relevant territory, units, technologies, and powerful bonuses are retained
- Hannibal becomes the transformed leader
- ordinary and Wendigo recruitment systems remain available

The preserved recruitment boundary is paid-only after transformation. The merge calls `cannibalism_wendigo_focus_preserve_pack_contract` before the first overlay focus or player interaction and sets normal queue recruitment for the locked `Wendigo Pack` to `no`. The two Event 014 scripted Pack musters remain available after their focus unlocks.

### Classification

Wendigo Hannibal is an actual nonhuman country for shared exclusions and interactions.

### Portrait

A separate generated animated portrait depicts a transformed Hannibal. It must reuse the existing Chaos Redux Wendigo visual language rather than importing new real-world sacred symbols.

### Military

- all ordinary cannibal units
- existing Wendigo units
- additional Wendigo training
- supernatural winter and supply bonuses
- enemy fear, attrition, and population-consumption effects
- terminal recruitment from consumed territory

### Terminal identity

Before the final transformation locks, ordinary countries can attack anchor states and interrupt the process. After lock, the country becomes effectively impossible to defeat and receives the strongest Event 14 route package.

## Country cleanup and defeat

When a warlord country is defeated:

- ordinary victor receives liberation and recovery decisions
- surviving cells are evaluated rather than automatically erased
- Larder is destroyed or captured only through explicit outcomes
- warlord character can be killed, captured, escape, or become a hidden organizer
- event-created focus assignment and cosmetic identity are cleaned up
- slot becomes reusable only after every reference clears

When Hannibal is defeated:

- all unified and subordinate countries are checked
- remaining communes and cells can continue unless the victory conditions destroy them
- a global defeat aftermath becomes available only if the crisis met duration, territory, and population-loss thresholds
