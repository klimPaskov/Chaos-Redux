# Event 021 Random Civil War

## Catalog identity

- Event ID: `21`
- Working name: `Random Civil War`
- Canonical entry event: `chaosx.nr21.1`
- Type: `Minor Repeatable`
- Status before implementation: `Unavailable`
- Event chaos level: `1`, Calm World
- Cluster: `1`, Wars
- Cluster severity: `Medium`

## Event promise

A country fractures according to conditions that already exist inside it.

A stable country should face a limited revolt, a failed coup, or one compact breakaway. A country weakened by occupation, war exhaustion, divided politics, regional exclusion, damaged administration, or uncertain military loyalty can lose larger regions and more forces. Later evolutions add rival camps, full independence movements, foreign sponsors, political exposure in nearby countries, nested crises, and a global climate in which every normal human country must manage internal risk.

The event is repeatable because different countries and different political structures should produce different wars. Repeatability must spread varied crises around the world. It must not trap one country in continuous civil war.

## Framework ownership

Event 021 owns:

- dynamic domestic-fracture target selection
- ordinary ideological uprisings
- rival legal governments
- broad command schisms that are not centered on one named commander
- regional secessions
- insertion of complete human Event 006 independence packages
- multi-front civil-war registration
- active-war escalation from Event 021 evolutions
- neighboring political exposure
- foreign support, containment, and mediation around Event 021 wars
- successor and recurrence memory
- the global fracture evolution
- the manual global fracture scenario
- reusable civil-war planning and cleanup helpers that specialized events may later call through explicit contracts

Event 021 does not absorb the unique identity of specialized events.

It must remain distinct from:

- Event 005 Soviet Union Collapse
- Event 006 Independence Wave
- Event 095 Occupation Revolt
- Event 117 Five-Way Civil War
- Event 127 Warlords
- Event 131 Widespread Mutiny
- Event 134 Duchies
- Event 142 Partisans
- Event 144 Freedom or Death
- Event 019 Soldiers from Nowhere and its formation revolts

Those events keep their own triggers, actors, presentation, progression, and outcomes. Shared helpers are allowed only after an explicit integration pass.

## Event family

The final event chain should contain separate families for these roles:

| Family | Design role |
| --- | --- |
| Dispatcher | Select a valid country, calculate hidden Fracture Pressure, select an archetype, plan the opening, and prepare log context |
| Affected-country opening | Present the visible rupture and activate the correct category phase |
| Opposition opening | Establish each claimant's public goal, capital, force base, and first objective |
| Additional-front incidents | Create or reveal Evolution I fronts without erasing current sides |
| Neighbor incidents | Open Evolution II exposure, support, containment, and mediation |
| Strange incidents | Deliver rare uncertain practices with bounded material consequences |
| Settlement events | Resolve surrender, autonomy, coalition, partition, recognition, merger, and demobilization |
| Victory and succession | Transfer legitimate government, preserve unresolved fronts, apply settlement memory, and start reconstruction |
| Evolution III incidents | Maintain global risk bands, critical-country queues, nested crises, and world reactions |
| Scenario wrapper | Launch the manual global fracture setup with selected type and intensity |
| Debug entry points | Offer bounded development triggers that never become ordinary player content |

The final numbering belongs to implementation. The structure must keep state, actor, and cleanup ownership clear.

## Availability

Event 021 is eligible from Calm World.

A normal automatic firing requires at least one valid target and at least one valid opposition route. When no valid target exists:

- the event has no live selection weight
- the Events list displays `N/A`
- the automatic picker does not queue it
- normal manual triggering explains that no valid country can currently fracture
- force-trigger testing may bypass ordinary target preference but may not create an invalid actor, broken map, duplicate country, or unsafe terminal conflict

The event remains disabled by default while its catalog status is unreworked or unavailable. Once the complete rework is implemented for test entry, it enters the reworked-event default allowlist while retaining `Needs Testing` until acceptance certification is complete.

## Universal exclusions

A country is excluded when any of these conditions apply:

- it is classified by the shared `is_actual_nonhuman_country` trigger
- it is in a terminal state incompatible with normal event play
- it has no valid split, claimant, or same-tag takeover route
- it is inside a short creation, annexation, cleanup, or succession lock
- it is already in an incompatible bespoke civil-war chain
- a safe capital, force package, or parent remnant cannot be created
- every possible independence package is incomplete, blocked, duplicated, or territorially invalid
- its only possible territory is controlled by unrelated third parties and belongs to another event's uprising logic
- the active-front or actor-capacity gate cannot admit another crisis

The broader `is_special_chaos_country` trigger must not be used as blanket immunity. Human Event 006 countries, restored states, unusual human governments, subjects, and human chaos-created countries remain eligible after their grace periods.

## Repeat behavior

After a firing:

- the event uses the standard repeatable weight and cap system
- the affected country receives a country-specific cooldown
- Event 021 can still target other countries
- active Event 021 wars can evolve
- the former target cannot return until both cooldown and successor grace have expired
- recurrence weight depends on the settlement, surviving armed networks, remaining divisions, territorial disputes, State Authority, and later chaos
- a rapid victory does not itself justify an immediate second crisis

A country that reaches a durable settlement and rebuilds authority should become a poor target for a long period. A harsh or incomplete settlement can leave recurrence risk, but the recurrence must still pass normal timing and validity.

## Evolution structure

| Stage | Chaos requirement | Main change |
| --- | ---: | --- |
| Baseline | Calm World | One primary opponent with severity based on country conditions |
| Evolution I | Gathering Storm | Multiple fronts, low-weight major targeting, and regular use of full independence packages |
| Evolution II | Rising Chaos | Regional political exposure, foreign sponsorship, stronger sides, and rare strange incidents |
| Evolution III | Chaos Tier | Persistent global fracture risk, bounded critical-country processing, nested crises, and systemic world reactions |
| Higher chaos | Totalen Chaos and World Collapse | Faster and broader Evolution III behavior within tested performance caps |

Each evolution has two entry routes.

### Active-war evolution

A live Event 021 crisis can change after an evolution becomes available. The transition uses the shared MTTH evolution process and records one evolution entry. It must not happen instantly without a scenario or other accepted immediate route.

### Prefire evolved opening

When an evolution is already active before Event 021 fires, the opening uses the evolved rules immediately. This is not a second event identity and does not require the country to pass through a weaker opening first.

## Nonterminal rule

Evolution III creates a persistent world threat and may register an Event 021 source with the shared world-threat aggregate. It does not set `world_end`, freeze normal events, or resolve the campaign into a terminal state.

The Event 021 threat source should exist only while the global fracture evolution is active and capable of creating or sustaining Event 021 crises. Cleanup must clear the source and refresh the aggregate when the evolution is disabled or no longer active.

## Public information boundary

The player should understand:

- the country's current State Authority stage
- the visible causes of the crisis
- which regions, capitals, commands, depots, railways, or ports matter
- what each public claimant wants
- which action spends which resources
- the objectives and deadlines of active missions
- the broad settlement being offered
- why a new front has appeared
- why a nearby war creates domestic pressure
- why a postwar state remains unsettled

The player should not see:

- raw target scores
- hidden Fracture Pressure formulas
- secret future package candidates
- exact strange-incident chances
- hidden sponsor plans
- actor-pool slots
- implementation flags
- future achievements
- unconfirmed supernatural explanations
- technical cleanup or performance state

## Completion boundary

A single working civil-war popup is not completion.

The event is complete only when the full baseline, three evolutions, decisions, missions, AI, Event 006 integration, cluster behavior, scenario, assets, achievements, event logs, Event Details, documentation, cleanup, probability checks, performance checks, and acceptance scenarios are finished without hidden fallback.
