# Malta Crusader country package

## Country identity

The country begins as a revived military-order state rooted in Malta's fortifications, the Order of St John, and an improvised coalition of foreign volunteers and seized Mediterranean commands. The starting state is deliberately unstable. It has a clear military purpose, but its political form is not settled.

The package must support these public identities:

- Malta Crusader State
- Sovereign Order of Malta
- Confederation of the Military Orders
- Crusader Kingdom of Malta
- The Holy See
- Kingdom of God

Hidden cosmetic identities include the Teutonic alliance presentation and German Atlantis identity. Those are handled in their own files.

## Tag and carrier strategy

The implementation must inspect local vanilla first. Reuse the vanilla Malta tag when it exists. Preserve all meaningful vanilla history, colour, names, and release logic that remain compatible. Event 38 adds origin flags and a crusader transformation package instead of creating a duplicate Malta identity.

Required origin facts:

```text
malta_crusaders_origin_event_038
malta_crusaders_release_package_level
malta_crusaders_human_controlled_at_release
malta_crusaders_existing_country_transformed
malta_crusaders_release_transaction_id
```

A country produced through another event cannot receive this package merely because it shares a cosmetic name. The event origin proof controls focus loading, decisions, custom units, and hidden routes.

## Starting government

### Institutional form

The opening government is a temporary **Crusade Council** led by the Grand Master or a provisional council when the historical Grand Master cannot be wired safely. Its ruling ideology is normally non-aligned with a clerical-military identity.

The historical Grand Master in 1936 was Fra' Ludovico Chigi Albani della Rovere, who held office from 1931 to 1951. A grounded portrait requires attributed archival source material and the portrait workflow. The implementation must also verify that the person is not already owned by a live vanilla or mod roster.

If a defensible portrait source or ownership transfer cannot be established, the accepted fallback is not an invented man. Use a people-free institutional leader such as the **Council of the Eight Langues** with an authentic institutional image. This is a source-backed institutional mode, not a fictional portrait shortcut.

### Political actors

The opening political field includes:

- the Grand Magistry and central command
- Hospitaller administrators and medical services
- Templar revivalists and war financiers
- Teutonic officers and heavy-armour advocates
- Saint Lazarus chapters focused on attrition, disease, and relief
- naval orders and Maltese port officers
- siege brotherhoods and military engineers
- Maltese civilian authorities
- Catholic clergy and Papal representatives
- local Christian elites in the occupied territories
- Catholic foreign volunteers
- local resistance and non-Catholic communities

The focus tree chooses which actors gain formal power. The event must not describe all Maltese civilians as members of the Order.

## Party and ideology plan

The exact party names depend on the final political route. Suggested party identities are:

| Political identity | Gameplay ideology | Role |
| --- | --- | --- |
| Crusade Council | Non-aligned | Opening emergency government |
| Grand Magistry | Non-aligned | Centralized military order rule |
| Assembly of the Langues | Democratic or non-aligned | Confederated order government |
| Papal Administration | Non-aligned | Holy See route |
| Christian Social Council | Democratic | Civilian Catholic constitutional route |
| Templar Directorate | Fascist or non-aligned | Militarized finance and conquest route |
| Maltese Labour Opposition | Communist or democratic support | Civilian opposition and reform pressure |

A full communist crusader route is not required. Left-wing and secular actors can shape civilian reform, labour resistance, foreign policy, or a constitutional settlement without receiving a shallow ideological branch.

## Starting national spirits

The country starts with no more than three focus-tree-created visible national spirits.

### Fortress Without a Hinterland

**Role:** Malta has fortifications and ports but lacks land, raw materials, and strategic depth.

**Pressure:** high import dependence, convoy strain, vulnerable supply, limited local construction space.

**Lifecycle:** Mediterranean logistics, captured ports, principality contributions, and a stable hinterland transform it into a fortified network. Total loss of the expedition can worsen it temporarily.

### The Orders Recalled

**Role:** several orders have returned under one council without agreeing on command, land, or wealth.

**Pressure:** command friction, political demands, uneven recruitment, risk of order incidents.

**Lifecycle:** centralization, confederation, Papal arbitration, or dominant-order routes replace it with route-specific institutions.

### An Army Out of Time

**Role:** unusual medieval-modern formations can shock conventional armies but are difficult to equip, transport, and reinforce.

**Pressure:** special equipment dependency, slow heavy formations, weak combined-arms integration.

**Lifecycle:** order doctrine, modern workshops, captured industry, foreign sponsors, and specialized technologies transform it into a viable crusader war machine.

No route should leave all three opening problems unchanged through the late game.

## Laws and government setup

The opening package should set laws according to actual capability:

- a limited emergency conscription policy rather than immediate total mobilization
- a constrained trade law reflecting import dependence
- an economy law appropriate to regional war
- route-neutral initial military advisers
- no unexplained advanced occupation law

Focuses and decisions can later unlock crusader levy systems, order exemptions, Papal taxation, principality contributions, foreign donation networks, and terminal mobilization.

## Population and manpower

Malta's local population cannot sustain the opening army alone. Starting manpower comes from separate, traceable sources:

- Malta's actual core population
- volunteers from Catholic countries
- order members and associated institutions
- local recruits from controlled territory
- militias raised by principalities
- Papal or believer levies in later routes

The opening grant must be dynamic and bounded by package level. It should add recruitable manpower or equipment-backed formations without silently adding millions of permanent state population to Malta.

Local recruitment from occupied states requires compliance, collaboration, a principality, a local Christian administration, or another valid route. Harsh rule can produce short-term manpower at the cost of resistance, legitimacy, migration, and condemnation.

## Industry and construction

### Opening economy

The opening state receives enough distributed capacity to function:

- Malta fortress workshops
- Grand Harbour dockyard capacity
- repair facilities in captured ports
- one or more military workshops in the Holy Land command
- convoy and transport support
- modest civilian administration capacity

The release effect should scale factory and dockyard setup from controlled territory, local existing industry, and evolution package. It must not overwrite existing buildings blindly.

### Long-term economy

The country grows through:

- fortified port network development
- captured workshops and arsenals
- order finance
- Templar banking and credit
- Papal donations
- principality tribute
- foreign equipment and volunteers
- local agricultural and industrial concessions
- shipbuilding and convoy protection
- relic pilgrimage and prestige economy
- terminal believer contributions

Every strong economic route carries a tradeoff. Templar finance increases dependency and order influence. Papal finance increases clerical control. Direct extraction lowers local cooperation. Principality autonomy reduces direct output but improves local stability and recruitment.

## Resources and fuel

The early campaign is resource-poor. The country must import or capture steel, fuel, aluminium, and industrial inputs. Decisions can establish:

- fuel contracts
- protected convoy routes
- captured oil access
- local charcoal and low-tech substitutes for limited equipment families
- foreign sponsor deliveries
- horse breeding and remount systems
- steel salvage and armour workshops

The custom units cannot become a free low-resource alternative to normal armies. Heavy knights, mechanized carriers, siege equipment, and blessed armour consume meaningful industrial inputs.

## Technology and research

The starting package gives a coherent 1936 baseline from Malta's prior controller, the local theaters, and the order network. It does not grant all modern technology.

Priority research areas are:

- infantry support and field hospitals
- engineering and fortification
- logistics and supply
- naval transport and marines
- radio and command
- metallurgy and armour
- artillery and siege modernization
- cavalry and mechanized carriers
- air transport and close support where available

Custom technologies should sit in a dedicated Event 38 branch or approved special project family. Any new technology, doctrine, prerequisite, unlock, bonus, or asset requires `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` evidence.

Technology grants from foreign sponsors must use a compatibility-aware union or targeted bonus. The package must not erase existing research or grant mutually exclusive industry branches incorrectly.

## Army setup

### Baseline force concept

The baseline force is large enough to defend several nodes, but too small to dominate every opening front. It contains:

- one Malta fortress garrison
- two to four Armored Knight formations
- two to four Mounted Knight formations
- two to four Archer or Crossbow formations
- one Siege Host
- engineer and medical support capacity
- local Holy Land militia or guard units
- a small reserve for naval transport

Exact counts scale from evolution, selected territory, displaced owner strength, and human or AI control. The total package should be expressed as a bounded combat-width and equipment budget, not a fixed count copied into every map state.

### Templates

The country begins with a small number of readable templates:

- Fortress Commandery
- Armored Knight Banner
- Mounted Crusader Column
- Crossbow Levy
- Siege Host
- Holy Land Guard

Later routes unlock order-specific and combined-arms templates. The initial template list must not overwhelm the player.

### Reinforcement

Replacement comes from:

- order workshops
- foreign donations
- captured equipment conversion
- principality depots
- dedicated decisions
- focus unlocks
- normal production lines
- volunteer cadres

The implementation must register each custom family through the owner-side unit-family provider contract and CXT setup coverage.

## Navy setup

Malta needs a transport and escort force, not a free major navy.

The opening can include:

- convoys and transports
- a few destroyers, escorts, or converted patrol craft when locally available
- captured or transferred light vessels through a bounded setup rule
- naval transport capacity
- coastal defence and mine support

The naval order route can later develop marines, boarding units, convoy escorts, island warfare, submarines, light surface groups, and limited capital-ship ambitions. Captured fleets must use valid transfer logic and cannot duplicate ships.

## Air setup

The baseline receives enough aircraft or support to avoid total isolation only when the selected territories and donors can provide it. The normal package can include:

- reconnaissance aircraft
- transport aircraft
- a small fighter contingent
- captured or donated tactical aircraft

The event does not make Malta an air superpower. Later blessed or Papal air formations remain conventional aircraft with religious presentation unless a separate accepted technology provides another capability.

## Supply, convoys, and trains

The country starts with dynamic grants based on:

- number of controlled theaters
- total divisions
- distance between Malta and the Holy Land
- number of ports
- pre-fire evolution level
- hostile naval pressure
- available local stockpiles

Minimum grants prevent immediate paralysis. Caps prevent the release from creating an unlimited logistics reserve. Later losses matter.

## Commanders and advisers

The package needs:

- one Grand Master or institutional commander
- several order-specific generals
- one naval commander
- one logistics or engineering officer
- one medical or Hospitaller adviser
- one diplomatic or Papal liaison
- route-specific advisers unlocked later

Grounded people require source research and ownership checks. Fictional officers are allowed only when the character and institution are clearly fictional within the high-chaos route. Ordinary Maltese and order officers should use grounded or institutional sourcing.

Commander traits should express actual roles:

- fortress defence
- cavalry breakthrough
- siege engineering
- amphibious command
- medical recovery
- attrition warfare
- multinational volunteer coordination

Do not give every commander the same generic knight trait.

## Country AI

The Malta AI needs strategy plans by situation.

### Opening survival AI

- defend Malta and the primary port
- maintain a supplied Holy Land front
- avoid scattering units across every claim
- protect convoys
- prioritize one coherent land corridor
- recruit affordable special units
- use ordinary infantry or militia when special equipment is scarce

### Expansion AI

- finish the Holy Land corridor before opening another theater
- prefer adjacent or sea-connected targets
- avoid war with a much stronger major without sponsors
- create principalities when direct occupation is unstable
- repair ports and rail before deeper advance

### Political AI

- choose centralization when cohesion is low and authority is high
- choose confederation when several orders are strong and cooperative
- choose Papal rule when sacred legitimacy and Papal support are high
- avoid the Papal path when relations, control of Rome, or leadership conditions are invalid
- use the Eleventh Crusade route when the expedition is lost

Every AI weight and random route selection requires named scenario evaluation through the probability workflow.

## Country-package completion evidence

Implementation cannot call Malta complete without evidence for:

- tag reuse or collision-safe carrier decision
- names, adjective, colour, and flags
- origin proof and focus loading
- capital, ownership, cores, claims, and occupied commands
- party names, ideology, laws, and government
- leader and portrait provenance
- commanders, advisers, and high command
- starting ideas and complete lifecycles
- manpower and population treatment
- industry, resources, production, and construction
- technology, research, and doctrine
- army templates, unit counts, equipment, and reinforcement
- navy, air force, convoys, trains, fuel, and supply
- decisions and the three-value mechanic
- focus routes and hidden route gating
- AI plans and probability evidence
- release, annexation, defeat, restoration, and cleanup
- multiplayer player-switch behavior
- DLC-present and DLC-absent behavior
