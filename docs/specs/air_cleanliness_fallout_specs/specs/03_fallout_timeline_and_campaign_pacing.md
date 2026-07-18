
# Fallout Timeline and Campaign Pacing

Working labels in this file are not final localisation.

## Time structure

The scenario uses time bands to prevent every system from appearing at once.

| Band | Campaign time | Main play |
| --- | --- | --- |
| Winter build-up | Before Fallout | State winter phases, visible cooling, government strain, evacuation, treaty relief, gradual collapse |
| Transition | Request through reveal | Blackout, world rewrite, player continuation, no ordinary events |
| Ash week | Days 1 to 7 after reveal | Orientation, immediate survival values, emergency command, no broad diplomacy |
| First season | Days 8 to 90 | Food, water, shelter, medicine, local authority, first expeditions |
| First winter year | Months 4 to 12 | Famine, heating, migration, first internal political settlement |
| Consolidation | Year 2 | Governments formalize, first reliable trade, militia reform, regional contact |
| Rival orders | Years 3 to 4 | Compacts, warlords, border wars, major reclamation, first constitutions |
| New states | Years 5 to 6 | Rebuilt institutions, post-Fallout generation enters politics, larger wars and federations |
| Soot retreat | Years 7 to 8 | Visible warming, ultraviolet and thaw problems, restored agriculture, old claims return |
| Second world | Years 9 to 10 | Interregional blocs, restored grids, new ideologies, first durable world order |
| Open continuation | Year 10 onward | Long ambitions, recurring seasonal cycles, late formables, no forced campaign end |

## Pre-Fallout winter build-up

The build-up is part of the scenario.

Event priorities:

- first state phase changes
- climate becoming visible on the normal map
- food and heating disputes
- local evacuation
- capital continuity planning
- treaty operations
- military pressure on relief corridors
- institutional strain
- state abandonment
- gradual Fallout request pressure

Governments should accumulate memories that affect their successors:

- who received shelter access
- who was evacuated
- who was abandoned
- whether the government used coercion
- treaty membership and violation
- seed and food preservation
- archive preservation
- military continuity
- mutant or altered-population policy
- relocation of industry and leadership

## Transition

The blackout transition has no ordinary flavour events.

Only transition-owned events may run:

- validation
- text beats
- state grading
- country survival
- successor selection
- player reservation
- relationship reset
- rewrite completion
- reveal

The normal event scheduler remains locked until the reveal grace period.

## Ash week

The user approved the Ash-week orientation contract on 2026-07-18. Every materialized playable successor receives five distinct components in this exact order:

| Sequence | Component | Human root and result | Hidden AI root and result | Result delay | Receipt |
| ---: | --- | --- | --- | ---: | --- |
| 1 | national orientation | `62` and `64` | `63` and `65` | 2 days | `national_orientation` |
| 2 | capital or main-state condition | `66` and `68` | `67` and `69` | 3 days | `capital_condition` |
| 3 | immediate resource crisis | `70` and `72` | `71` and `73` | 4 days | `immediate_resource_crisis` |
| 4 | government-archetype introduction | `74` and `76` | `75` and `77` | 3 days | `government_archetype` |
| 5 | first character or institution | `78` and `80` | `79` and `81` | 2 days | `character_or_institution` |

The sequence closes through human event `82` or hidden AI event `83`. Hidden event `84` owns authenticated cleanup. These 23 `chaosx.fallout` suffixes are reserved with these exact roles:

| Suffix | Event role | Visibility | Follow-up |
| ---: | --- | --- | --- |
| 62 | national orientation root | human visible | 64 |
| 63 | national orientation root | hidden AI | 65 |
| 64 | national orientation result | human visible | 66 |
| 65 | national orientation result | hidden AI | 67 |
| 66 | capital condition root | human visible | 68 |
| 67 | capital condition root | hidden AI | 69 |
| 68 | capital condition result | human visible | 70 |
| 69 | capital condition result | hidden AI | 71 |
| 70 | immediate resource crisis root | human visible | 72 |
| 71 | immediate resource crisis root | hidden AI | 73 |
| 72 | immediate resource crisis result | human visible | 74 |
| 73 | immediate resource crisis result | hidden AI | 75 |
| 74 | government archetype root | human visible | 76 |
| 75 | government archetype root | hidden AI | 77 |
| 76 | government archetype result | human visible | 78 |
| 77 | government archetype result | hidden AI | 79 |
| 78 | character or institution root | human visible | 80 |
| 79 | character or institution root | hidden AI | 81 |
| 80 | character or institution result | human visible | 82 |
| 81 | character or institution result | hidden AI | 83 |
| 82 | orientation closure | human visible | 84 |
| 83 | orientation closure | hidden AI | 84 |
| 84 | orientation cleanup | hidden | none |

Each result uses one deterministic score calculated from its frozen component transaction. The accepted common outcome bands are:

| Score | Outcome |
| ---: | --- |
| 70 or more | success |
| 45 through 69 | partial success |
| below 45 | failure |

Human and hidden AI routes pay the same costs, use the same score, apply the same results, write the same memory, and run the same cleanup. Hidden AI cannot receive reduced costs or guaranteed success. Exact ties use the lowest stable branch identity.

Each component transaction stores its transition generation, country registry index, component identity, mode, branch, required state or character target, region, archetype, frozen survival inputs, issue date, due day, event token, and result-issued identity. Payload fields commit before the pending marker. The result-issued marker commits only after event issue. Save recovery may issue an unissued result once and must preserve an issued token without issuing it again. A stale generation cancels its temporary transaction without promoting an orientation receipt.

The accepted live-ledger contract removes caller-supplied Cohesion and state Supply Access. Each component freezes current Cohesion from the schema-3 survival row and freezes Supply Access from the authenticated assigned capital. Cohesion opens from 35 Food, 35 Shelter capacity, and 30 already-adjusted Recognition, then changes only through its clamp-owning helper. State Supply Access opens from 20 points per surviving post-rewrite infrastructure level and drives `local_supply_impact_factor` from minus 50 percent through zero.

Orientation state results write the authenticated assigned capital directly. Exposure, Shelter capacity, Adaptation, and Reclamation use the live Air Winter values. Recovery writes the same delta to `air_winter_recovery_bonus` and current `air_winter_recovery`. Supply changes use the sole Supply Access helper. Phase and grade remain frozen display and scoring facts. A stale state identity, non-produced Air Winter row, wrong ownership or control, or stale schema-3 Supply Access row records a typed diagnostic and blocks the result before mutation.

Orientation refuses to start when the successor allocation, player-continuation ownership, nine-region row, twelve-archetype row, country-memory row, main-state target, or curated character or institution registry is missing. A missing row records a typed diagnostic. It cannot select a generic fallback. The character or institution component requires at least two valid curated candidates.

The package requires six dedicated Fallout report images for national orientation, capital condition, resource crisis, government authority, first character or institution, and orientation closure. All six dedicated images and sprite registrations exist. The dormant transaction substrate, schema-3 Cohesion and Supply Access ledgers, live Air Winter state-result mapping, shared localisation, national pilot events `62` through `65`, exact twelve-memory resource events `70` through `73`, exact twelve-memory government events `74` through `77`, and authenticated closure and cleanup events `82` through `84` are implemented. The source design contains the manually reviewed 108-cell live-region and government-archetype coverage matrix plus a twelve-successor memory and candidate pilot covering every live region and archetype. The resource pilot has an idempotent exact-memory mapper, one exact supporting resource and deterministic AI preference per reviewed identity, and request authentication against a separate current capital-asset receipt. The government pilot has an idempotent exact-memory mapper, one exact consolidation benefit and deterministic AI preference per reviewed identity, and transaction authentication against its current row. The candidate pilot has 36 typed ids, an idempotent exact-memory mapper, and request authentication against a separate installed-package receipt. None of the required approval or package receipt surfaces has a setter. The completion audit keeps all fifteen defined blocks uncounted because the caller, runtime approval producers, the other 96 regional and archetype cells, exact capital repair, installable candidate packages and assets, logs, and details are absent. The other eight blocks and complete tranche approval remain outstanding.

No caller may be wired until successor allocation, player continuation, and every required candidate registry are proven. The closure and cleanup do not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`. The scheduler remains dormant. The 23 reserved blocks contribute zero to the release floor until the complete tranche is implemented, wired, localised, logged, detailed, manually reviewed, and audited. The Fallout living-world count therefore remains 0 of 660.

The approved scoring inputs, branch costs, result values, regional and archetype coverage rules, human and AI ownership rules, recovery rules, asset requirements, and validation scenarios in `docs/plans/air_cleanliness_fallout_plans/FALLOUT_ASH_WEEK_ORIENTATION_CONTRACT_PROPOSAL.md` are incorporated into this source spec as acceptance criteria.

No country should begin with every decision visible. The orientation opens the first emergency set.

## Days 8 to 30

Eligible event families:

- water
- shelter air
- emergency food inventory
- medical triage
- power and heat
- command legitimacy
- local militia
- immediate refugees
- nearby fires, fallout, or toxic zones
- first salvage permit
- burial and sanitation
- first radio reception

Diplomacy remains limited to nearby signal contact and emergency messages.

## Days 31 to 90

Eligible additions:

- local political factions
- ration law
- work and service obligations
- refugee integration
- skilled survivor recruitment
- black markets
- first surface expedition
- family separation and reunion
- education and child care
- religious or civic ritual
- first bilateral aid exchange
- local bandit or raider pressure

A country may begin one major domestic arc.

## Months 4 to 6

Eligible additions:

- first harvest failure
- winter infrastructure damage
- population relocation
- military professionalization
- official government name and constitutional direction
- first recognition decision
- compact talks
- regional trade routes
- first cause-memory interpretation
- first mutant or altered-community contact where eligible

## Months 7 to 12

The first post-Fallout winter or severe season is a campaign milestone.

Required event coverage:

- heating and fuel
- food rationing
- shelter crowding
- epidemic risk
- rail and port survival
- political confidence
- militia desertion
- winter celebration or mourning
- first full-year census
- survivor births and deaths
- old calendar versus Year Zero debate

The first year ends with a state-of-the-country event that records:

- survival-resource trajectory
- government legitimacy
- active rivals
- most damaged state
- best recovery state
- refugee policy
- altered-population policy
- old-world memory direction
- first late ambition seed

## Year 2, consolidation

New systems:

- formal constitutions or permanent emergency law
- professional army or permanent militia
- regional market
- regular radio network
- education and apprenticeship
- medical policy
- salvage law
- land and housing ownership
- first post-Fallout courts
- compact membership
- formal border claims
- successor identity and flag route
- first country-memory focus branch payoff

Character arcs can advance into office, exile, command, disgrace, death, or opposition.

## Years 3 to 4, rival orders

New event families:

- major regional congresses
- water and food treaties
- trade monopolies
- warlord tribute systems
- port and rail disputes
- ideology export
- refugee citizenship disputes
- coalition wars
- postwar settlement
- city reclamation
- state-category restoration attempt
- first major power-grid project
- first recognized mutant polity
- old government restoration attempt
- military succession

At least one external arc should become available to every viable country by the end of Year 3.

## Years 5 to 6, new states

The world should no longer feel like a temporary emergency.

Event priorities:

- permanent political institutions
- second leadership generation
- adult survivors who were children during the collapse
- post-Fallout military academies
- universities, workshops, monasteries, guilds, or protocol schools
- demographic policy
- intermarriage and citizenship
- language and naming change
- new festivals and mourning days
- old-world technology doctrine
- regional federations
- larger wars with explicit goals
- successful and failed integration of conquered states

Countries that remain small still receive deep internal content.

## Years 7 to 8, soot retreat and unstable warming

Climate recovery does not remove danger.

Event families:

- first bright summer
- ultraviolet exposure
- false spring
- late frost
- flood from thaw
- exposed contaminated ruins
- disease from thawed waste and bodies
- roof and bridge collapse
- new crop opportunities
- migration toward recovering land
- conflict over reclaimed farmland
- altered ecology moving with the climate
- political pressure to reopen sealed zones
- memory conflict as the sky brightens

Successful climate adaptation should pay off here.

## Years 9 to 10, second world

Event priorities:

- interregional communication
- restored long-range shipping
- continental congresses
- competing standards and currencies
- transregional ideological blocs
- old borders versus new nations
- shared scientific projects
- war-crime and atrocity memory
- mutant recognition treaties
- common climate monitoring
- first long-distance passenger routes
- restoration of major cities
- new capital construction
- global food reserve
- disarmament or new weapons race
- competing calendars and historical narratives

The world remains fragmented. A global congress should not restore the old international system in one event.

## Year 10 onward

The scenario continues without forced closure.

Recurring content:

- seasonal climate cycle
- leadership succession
- trade disputes
- border integration
- expeditions
- demographic change
- infrastructure maintenance
- ideology and faction politics
- regional compact goals
- late formables
- wasteland reclamation
- machine and mutant route development
- memory anniversaries
- old weapons discovery
- new scientific risks

Late events should recognize what the player built.

## Phase transitions and event unlocks

A time band alone never guarantees an event. It opens a pool.

Events still require relevant world state.

Examples:

- a reactor crisis needs a reactor or power route
- a maritime congress needs several connected ports
- a mutant recognition event needs an altered polity
- a constitutional event needs a government that has not already fixed its structure
- a thaw event needs a state recovering from severe winter
- a water war needs a contested water source and rival
- a postwar settlement needs a completed war

## Campaign pacing checks

- The first day does not display a wall of popups.
- Diplomacy begins with signals and aid before ordinary alliances.
- Major wars do not start on reveal day.
- Constitutions appear after immediate survival.
- Recovery creates new play and does not end political or environmental pressure.
- Second-generation politics appears before Year 10.
- Every year opens at least one new event layer.
- Small countries have internal arcs when expansion is impossible.
- Long-lived routes receive late payoffs.
- Failure can move a country backward into emergency rule, famine, fragmentation, or migration.
