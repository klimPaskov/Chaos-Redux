# Event 046 shuffle-surface classification matrix

This matrix is the design allowlist audit.

`Core safe` still requires confirmation of the current engine setter and legal range before implementation can claim completion.

`Conditional safe` does not enter the live pool until every listed proof exists.

`Owner adapter only` requires an owner declaration.

`Protected` never enters the general registry.

| Domain | Surface | Capability | Class | Accepted treatment | Main proof or exclusion |
| --- | --- | --- | --- | --- | --- |
| Country | Stability | Baseline | Core safe | New legal percentage per country | Ordinary stability consumer and legal setter |
| Country | War Support | Baseline | Core safe | New legal percentage per country | Ordinary War Support consumer and legal setter |
| Country | Political Power | Baseline | Core safe | New absolute stored amount | Current legal cap and negative-balance policy |
| Country | Command Power | Baseline | Core safe | New amount inside frozen cap | Cap read and direct reserve setter |
| Country | Army Experience | Baseline | Core safe | New amount inside legal cap | Direct experience setter |
| Country | Navy Experience | Baseline | Core safe | New amount inside legal cap | Direct experience setter |
| Country | Air Experience | Baseline | Core safe | New amount inside legal cap | Direct experience setter |
| Country | Reserve manpower | Baseline | Core safe | New absolute reserve from dynamic population and world bands | State population side-effect reconciliation |
| Country | Fuel reserve | Baseline | Core safe | New amount between zero and frozen capacity | Direct setter and zero-cap handling |
| Country | Fuel capacity | Evolution II or owner | Conditional safe | Rewritten only through proven capacity sources | Building and modifier dependency audit |
| Country | Convoys | Evolution I | Core safe | New dynamic absolute quantity | Concrete token and practical ceiling |
| Country | Trains | Evolution I | Core safe | New dynamic absolute quantity | Concrete token and practical ceiling |
| Country | Ordinary equipment stockpiles | Evolution I | Core group | New quantities by compatible equipment family | Loaded token audit, variant safety, add and remove support |
| Country | Special event equipment | Evolution IV | Owner adapter only | Owner chooses eligible tokens and quantities | Unique object and progression proof |
| Country | Nuclear stockpile | Evolution IV or V | Owner adapter only | Owner decides whether stockpile is mutable or capability proof | Nuclear system and diplomacy side effects |
| Country | Missile stockpile | Evolution IV | Owner adapter only | Owner-declared inventory adapter | Token identity and launch-system ownership |
| Country | Chemical and biological payloads | Evolution IV | Owner adapter only | Owner-declared inventory adapter | CBRN capability, condemnation, and contamination ownership |
| Country | Consumer goods pressure | Evolution IV | Owner adapter only | Current mutable pressure only | Law and economy owner contract |
| Country | Trade balance or import contracts | Evolution V | Conditional safe | Only proven relationship data | Bilateral object and market recalculation |
| Politics | Party popularity shares | Evolution III | Core safe | Full active ideology set normalized together | Loaded ideologies and exact total reconciliation |
| Politics | Ruling ideology | Evolution III | Conditional safe | Choose approved loaded ideology | Election, leader, flag, AI, and generic Chaos refresh |
| Politics | Economy law | Evolution III | Core or conditional | One loaded legal token in category | DLC, category, and owner restrictions |
| Politics | Trade law | Evolution III | Core or conditional | One loaded legal token in category | DLC, category, and owner restrictions |
| Politics | Conscription law | Evolution III | Core or conditional | One loaded legal token in category | DLC, category, and owner restrictions |
| Politics | Other ordinary law categories | Evolution III | Conditional safe | One token per registered compatibility group | Category inventory and country validity |
| Politics | Country-specific laws | Evolution IV | Owner adapter only | Owner exposes approved current law | Route and lifecycle ownership |
| Politics | Balance of power current value | Evolution IV | Owner adapter only | New value inside owner range | Sides, stages, modifiers, and decisions remain coherent |
| Politics | Balance of power side identity | None | Protected | Never changed | Stable mechanic identity |
| Politics | Election date and election history | None | Protected | Never changed | Historical and lifecycle state |
| Politics | Party names and ideology definitions | None | Protected | Never changed | Stable data identity |
| Politics | Leaders and characters | None | Protected | Never changed | Persistent object identity and ownership |
| Politics | Advisors and high command | None | Protected | Never changed by general family | Character and route identity |
| Politics | National spirits and ideas | Evolution IV | Owner adapter only | Only a narrow owner-approved staged value | Idea identity and lifecycle remain protected |
| State | Absolute civilian population | Evolution II | Core safe | New absolute amount from world bands | No Deaths or migration, manpower side-effect repair |
| State | State category | Evolution V | Conditional safe | Only through a full slots and map bundle | Building capacity and map assumptions |
| State | Extra shared building slots | Evolution II | Conditional-core bundle | Planned with factory counts | Legal capacity setter and cleanup |
| State | Civilian factories | Evolution II | Core bundle | New count inside planned shared capacity | Shared capacity bundle |
| State | Military factories | Evolution II | Core bundle | New count inside planned shared capacity | Shared capacity bundle |
| State | Dockyards | Evolution II | Core conditional | New count in valid coastal state | Coastal consumer and shared capacity |
| State | Infrastructure | Evolution II | Core safe | New legal level | Direct state building setter |
| State | Airbase | Evolution II | Core safe | New legal level | Direct state building setter |
| State | State anti-air | Evolution II | Core safe | New legal level | Direct state building setter |
| State | Radar | Evolution II | Core safe | New legal level under loaded feature | DLC and legal setter |
| State | Land forts | Evolution II | Core safe | New legal level | Direct state building setter |
| State | Coastal forts | Evolution II | Conditional-core | New legal level in coastal state | Coastal validity |
| State | Naval bases | Evolution II | Conditional safe | New legal province-level base | Province placement, supply, and pathing |
| State | Supply hubs | Evolution II or V | Conditional safe | New graph node only under full map contract | Province placement and graph reconciliation |
| State | Railways | Evolution II or V | Conditional safe | New valid network only under full map contract | Adjacency, route, duplicates, and supply refresh |
| State | Ordinary strategic resources | Evolution II | Conditional-core group | New amount by registered resource type | Token list, extraction refresh, protected deposits |
| State | Scripted or unique deposits | Evolution IV | Owner adapter only | Owner controls amount and identity | Discovery history and permanent source proof |
| State | Building damage | None | Protected by default | Existing damage remains | Ongoing repair state |
| State | Construction queue | None | Protected | Existing projects remain | Persistent object identity |
| State | State modifiers | Evolution IV | Owner adapter only | Current numeric pressure may be exposed | Modifier identity and duration remain protected |
| State | Compliance and resistance | Evolution IV or V | Owner adapter only | Current values only under occupation owner | Occupation, history, and target proof |
| State | Weather and climate | None | Protected | Never changed | External simulation state |
| State | Owner | Evolution V | Conditional structural adapter | Selected ownership bundle only | Country survival, capital, war, supply, units, occupation |
| State | Controller | Evolution V | Conditional structural adapter | Separate control bundle | War and occupation legality |
| State | Core relationships | None | Protected | Never changed by general Shuffle | Identity, resistance, release, and manpower |
| State | Claim relationships | Evolution V | Conditional structural adapter | Add, remove, or regenerate approved claims | Pair deduplication and owner protection |
| State | Capital designation | Evolution V | Conditional structural adapter | Choose valid owned state | Country-specific capital restrictions |
| Research | Active project progress | Evolution III | Conditional-core | New progress on same active token | Current engine progress setter |
| Research | Active project identity | None | Protected | Project remains selected | Stable research object |
| Research | Completed technologies | None | Protected by default | Never removed or granted | Dependency graph and unlock side effects |
| Research | Research slots | None | Protected | Never changed | Country progression structure |
| Research | Stored research bonuses | Evolution IV | Owner adapter only | Only owner-approved numeric store | Targeted bonus identity and expiry |
| Research | Doctrine progress | Evolution III | Conditional safe | Current progress only | Doctrine graph and current selection |
| Research | Completed doctrine nodes | None | Protected by default | Never changed | Mutual exclusion and prerequisite graph |
| Research | Special projects and facilities | None | Protected | Never changed | Project identity, facilities, breakthrough history |
| Production | Line efficiency | Evolution III | Conditional-core | New value inside current legal cap | Direct setter and line survival |
| Production | Efficiency progress | Evolution III | Conditional-core | New numeric progress | Direct setter and cap reconciliation |
| Production | Stored production progress | Evolution III | Conditional-core | New numeric progress on same line | Item and line identity preserved |
| Production | Produced item and variant | None | Protected | Never changed | Concrete object and technology identity |
| Production | Assigned factories | Evolution III | Conditional safe | Reallocation only under full queue contract | Factory availability and queue reconciliation |
| Production | Queue order | Evolution III | Conditional safe | Reorder only under full object contract | Stable line identity and UI refresh |
| Production | Military industrial organization assignment | None | Protected by default | Never changed | MIO identity and trait history |
| Units | Land-unit experience | Evolution III | Core safe | New legal experience | Stable unit identity and owner |
| Units | Land-unit planning | Evolution III | Conditional-core | New legal planning value | Direct setter and order behavior |
| Units | Organization | Evolution III | Conditional safe | Only after combat-state proof | Derived combat state |
| Units | Strength, manpower, and equipment fill | Evolution III | Conditional safe | Only through owner-approved reinforcement bundle | Casualty, reinforcement, and equipment accounting |
| Units | Entrenchment | Evolution III | Conditional safe | New legal current value | Movement and combat refresh |
| Units | Supply status | None | Protected derived state | Recalculated normally | Derived from map and logistics |
| Units | Template and battalion structure | None | Protected | Never changed | Unit definition identity |
| Units | Unit name and army assignment | None | Protected | Never changed | Persistent identity and player organization |
| Units | Land-unit location | Evolution V | Conditional structural adapter | Move to legal province | Transport, pathing, owner, order, and encirclement proof |
| Air | Air-wing experience | Evolution III | Conditional safe | New legal experience | Current air-wing scope and setter |
| Air | Air-wing base and mission | Evolution V | Conditional structural adapter | Move only to valid capacity | Base, range, mission, and object proof |
| Navy | Ship experience | Evolution III | Conditional safe | New legal experience | Ship scope and setter |
| Navy | Fleet, task force, base, and mission | Evolution V | Conditional structural adapter | Reassign or relocate only under full naval contract | Port, fleet, mission, and pathing proof |
| Commanders | Commander experience | Evolution III | Core or conditional | New approved numeric experience | Current engine setter |
| Commanders | Level, traits, and trait history | None | Protected by default | Never changed | Persistent character progression |
| Commanders | Trait progress | Evolution III | Conditional safe | Numeric progress only | Token, cap, and assignment proof |
| Diplomacy | Opinion value or owner-approved modifiers | Evolution V | Conditional safe | New pair value or registered modifier | Pair symmetry and cleanup |
| Diplomacy | Guarantee | Evolution V | Conditional safe | Relationship adapter only | Pair legality and war interaction |
| Diplomacy | Military access and docking rights | Evolution V | Conditional safe | Relationship adapter only | Pair legality and unit handling |
| Diplomacy | Non-aggression pact and truce | Evolution V | Conditional safe | Relationship adapter only | Duration and war state |
| Diplomacy | Faction membership and faction identity | None | Protected by default | Never changed | Group identity, war leadership, AI, goals |
| Diplomacy | Subject relationship and autonomy | None | Protected by default | Never changed | Identity, economy, wars, focus, and release logic |
| Diplomacy | War and peace state | None | Protected by default | Never changed | Conflict identity and peace-conference state |
| Diplomacy | Volunteers, attachés, and lend-lease objects | None | Protected by default | Never changed | Persistent bilateral objects |
| Chaos Redux | Current owner-mechanic pressure | Evolution IV | Owner adapter only | New owner-approved current value | Full owner adapter contract |
| Chaos Redux | Owner-mechanic history and first-discovery proof | None | Protected | Never changed | One-way accounting |
| Chaos Redux | Chaos Meter and source history | None | Protected | Never changed by randomizer | Shared authoritative framework |
| Chaos Redux | Deaths totals and causes | None | Protected | Never changed | Historical ledger |
| Chaos Redux | Air Cleanliness and source ledger | None | Protected | Never changed | Shared authoritative framework |
| Chaos Redux | Condemnation and evidence | None | Protected | Never changed | Historical and diplomatic ledger |
| Chaos Redux | Famine and migration current values | Evolution IV | Owner adapter only | Owner decides current-value exposure | Separate ledgers and cohort proof |
| Chaos Redux | Famine and migration ledgers | None | Protected | Never changed | One-way accounting and population proof |
| Chaos Redux | Camp and repression site current pressure | Evolution IV | Owner adapter only | Owner decides safe current state | Site lifecycle and evidence remain valid |
| Chaos Redux | Event weights, timers, history, enable state, evolutions | None | Protected | Never changed | Random event framework |
| Chaos Redux | Cluster and scenario registries | None | Protected | Never changed | Stable registry identity |
| Chaos Redux | Event Log and Event Details arrays | None | Protected | Never changed | UI and history bookkeeping |
| Chaos Redux | World-end and super-event state | None | Protected | Never changed | Terminal ownership and presentation |
| System | Stable IDs, arrays, indexes, event targets, provider registries | None | Protected | Never changed | Save and lifecycle proof |
| System | User settings and debug state | None | Protected | Never changed | User control and validation |
| System | Achievements and Event 46 tracking | None | Protected | Never changed | One-way completion proof |
