# Event 061: Return to Peacetime

## Part 1: Core event and baseline transaction

## Catalog identity

| Field | Value |
| --- | --- |
| Event ID | `61` |
| Event name | Return to Peacetime |
| Type | Minor Repeatable |
| Status before implementation | To Be Reworked |
| Minimum Chaos level | 1 |
| Primary cluster | Peace |
| Cluster role | High member |
| Canonical entry event | `chaosx.nr61.1` |

The event is a global demobilization shock.

It affects every existing country that uses ordinary civilian systems. Its physical effects remain component-gated so a country without factories, divisions, or a valid law group does not receive an invalid transaction.

The event does not select one victim. It changes the military and economic posture of the ordinary world during one shared firing.

## Player experience

The event should feel abrupt at the point of impact and gradual in its aftermath.

The first report tells the player that procurement offices are cancelling contracts, military plants are changing production, conscription offices are releasing men, and the public expects civilian recovery.

The immediate mechanical loss is severe and easy to read. The player then receives a clear recovery path through the Return to Rearmament decision category.

The category creates a strategic choice between accepting the civilian transition, preserving a limited defence structure, or paying a high civilian cost to rebuild a war economy.

A country can ignore the category at low Chaos. Ignoring it becomes increasingly dangerous after the event evolves.

## Global firing sequence

One firing follows this order:

1. Increment the global Return to Peacetime cycle identifier.
2. Build the valid country set from existing countries that use normal civilian systems.
3. Apply the baseline transaction once to every valid country.
4. Record country-specific before and after values for the national report.
5. Open or refresh the Return to Rearmament category for each affected country.
6. Show one national report to each human-controlled affected country.
7. Apply AI policy silently for AI-controlled affected countries.
8. Record one global Event 61 history entry through the shared Event Logs system.
9. Schedule any enabled evolved layers that belong to the current cycle.
10. Start a bounded country pulse for affected countries whose transition remains active.

The global entry event should orchestrate the world transaction. Player-facing national reports should use country scope so every human sees the exact effect on their own country without receiving reports for AI countries.

## Valid country contract

The primary shared eligibility test is `uses_normal_civilian_systems`.

The implementation should add only the minimum event-specific checks needed to prevent invalid transactions.

A valid affected country may be at peace, at war, capitulated, in exile, a subject, a faction member, or player-controlled. The component rules below decide which physical parts can execute.

A country with no eligible military factories still receives the War Support transfer, valid law steps, reconversion shock, event record, and recovery category when any recovery surface remains relevant.

A country with no conventional divisions remains eligible for the baseline event and later law effects. Division demobilization simply resolves at zero.

A country whose law groups have been replaced by an incompatible event-owned system should receive the compatible baseline components and an explicit internal compatibility result. The implementation must not force an invalid law token.

## Baseline transaction summary

| Component | Baseline result |
| --- | --- |
| Military factories | Convert one half of eligible military factory building levels into civilian factory building levels |
| War Support | Remove one half of current War Support |
| Stability | Add the same amount that was removed from War Support, subject to the engine ceiling |
| Economy law | Move one valid step toward Civilian Economy |
| Conscription law | Move one valid step toward Disarmed Nation |
| Manpower | Let the ordinary conscription law change remove mobilized availability from the recruitable pool |
| Military production | Apply or refresh the staged Industrial Reconversion Shock |
| Recovery | Open or refresh Return to Rearmament |

Each component records its own result. The national report should not imply that a component changed when it resolved at zero.

## Military factory conversion

### Eligible factory definition

For this event, an eligible military factory is a physical military factory building level in a state that is:

- owned by the affected country
- controlled by the affected country at the moment of conversion
- able to hold the corresponding civilian factory after a one-for-one building conversion
- not protected by a verified engine restriction or event-owned hard exclusion

Factories received only through occupation, subject contribution, trade, or another non-owned source do not count toward the conversion quota.

This definition keeps the transaction attached to real state buildings and prevents the event from altering another country's owned territory.

### Conversion amount

Let `M` be the number of eligible military factory building levels when the country transaction begins.

The baseline quota is:

`floor(M / 2)`

Examples:

| Eligible military factories | Converted | Remaining |
| ---: | ---: | ---: |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 1 |
| 3 | 1 | 2 |
| 4 | 2 | 2 |
| 5 | 2 | 3 |
| 10 | 5 | 5 |
| 25 | 12 | 13 |
| 100 | 50 | 50 |

The event does not round up. A country with one eligible military factory keeps it.

### State selection

The quota is distributed across eligible states through a bounded state selection pass.

The selection should avoid arbitrary concentration while still producing an exact country total.

Recommended selection order:

1. Prefer states with more than one military factory before removing the final military factory from a state.
2. Prefer owned core states over non-core states when both are controlled and otherwise equal.
3. Prefer undamaged building levels so the event does not create confusing transactions from already unusable capacity.
4. Spread conversions across several states when the country has a broad industrial base.
5. Use a seeded random tie break among equal candidates so repeat campaigns do not always convert the same state.
6. Continue until the exact quota is met or no valid state remains.

The capital is not absolutely protected. A blanket capital exemption would prevent an exact half conversion in compact countries. The state score may make the final military factory in the capital less likely to convert when another valid option exists.

### One-for-one building transaction

Every converted building level performs one atomic state transaction:

- remove one military factory level
- add one civilian factory level
- add one unit to that state's Return to Peacetime conversion ledger
- increment the country's current cycle converted count
- increment the country's unresolved converted count

The transaction must never add the civilian factory unless the military factory removal succeeded.

The transaction must never add a ledger unit unless both building changes succeeded.

### Physical conversion ledger

Each affected state stores the number of military factory levels converted by Event 61 that remain eligible for restoration.

Working state variable:

`return_to_peacetime_converted_factory_capacity`

The ledger is physical and state-owned.

It follows the state when ownership changes. The current valid owner can reopen the recorded capacity if it controls the state and meets the decision requirements.

The ledger does not represent a claim by the country that originally suffered the event.

A new civilian factory constructed after the event does not increase the ledger.

A civilian factory gained through annexation, focus, decision, repair, or another event does not increase the ledger.

Only the Event 61 one-for-one conversion transaction increases the ledger.

### Repeat firings

A later Event 61 firing calculates a new quota from the current eligible military factories.

New conversions add to the existing state ledger.

A repeat firing can therefore reduce the remaining military base again. This is intended.

The event does not clear earlier restoration rights and does not create parallel copies of the decision category.

### Damaged, lost, or unavailable capacity

A ledger unit can become temporarily unavailable when:

- the state is occupied
- the civilian factory level has been damaged or removed
- the state lacks control stability required by the decision
- the state changes to an incompatible owner
- another system alters the state's building capacity

Unavailable units remain dormant on the state until they can be reconciled.

A reopening action can restore no more military factory levels than the lower of:

- the state ledger count
- the civilian factory levels currently available to convert
- the batch size selected by the decision
- any verified engine building ceiling

If a civilian factory no longer exists, the decision does not recreate it for free.

### Permanent civilian conversion

The current owner can take an irreversible decision that accepts Event 61 conversions in its owned and controlled states as permanent civilian capacity.

The decision clears the state ledger units that belong to valid states under that owner's control. It does not remove civilian factories.

The player must receive a confirmation explaining that the military restoration right is being abandoned.

Lost states are outside the decision. Their ledger remains with the physical state for its current or future valid owner.

## War Support to Stability transfer

### Calculation

Let `W` be current War Support at the beginning of the country transaction.

The event calculates:

`T = W * 0.5`

It then:

- removes `T` from War Support
- adds `T` to Stability

The before and after values must be recorded before another baseline component changes them.

### Stability ceiling

Stability remains subject to the engine maximum.

Any part of the transfer that cannot fit below the maximum is lost.

The event does not create a reserve variable for overflow.

The player-facing effect description should state that the same amount is transferred subject to the country's maximum Stability.

### Examples

| War Support before | Stability before | War Support after | Stability after | Lost to ceiling |
| ---: | ---: | ---: | ---: | ---: |
| 80% | 40% | 40% | 80% | 0% |
| 60% | 80% | 30% | 100% | 10% |
| 20% | 10% | 10% | 20% | 0% |
| 0% | 70% | 0% | 70% | 0% |

### Rearmament reversal rule

Return to Rearmament may later move a limited amount of Stability back into War Support through a public defence campaign.

That recovery is deliberately inefficient. It should never allow repeated Event 61 firings to farm both values.

The standard rearmament action should remove more Stability than the War Support it restores, or pair a one-for-one transfer with a substantial political and industrial burden.

The exact ratio belongs in central tuning constants and must be included in the implementation balance pass.

## Economy law movement

### Ordered law ladder

Event 61 recognizes the following ordinary economy law order from most militarized to least militarized:

1. Total Mobilization
2. War Economy
3. Partial Mobilization
4. Early Mobilization
5. Civilian Economy
6. Peacetime Economy after Evolution III introduces it

The baseline moves one valid step downward toward Civilian Economy.

Examples:

| Law before | Law after baseline |
| --- | --- |
| Total Mobilization | War Economy |
| War Economy | Partial Mobilization |
| Partial Mobilization | Early Mobilization |
| Early Mobilization | Civilian Economy |
| Civilian Economy | Civilian Economy |
| Peacetime Economy | Peacetime Economy |

Peacetime Economy is below Civilian Economy. The ordinary baseline does not force a country into it. That transition belongs to Evolution III.

### Restoration target

Before the law changes, record the highest ordinary economy law rank that Event 61 removes from the country while unresolved recovery remains.

Working variable:

`return_to_peacetime_economy_restore_target_rank`

A later event firing can push the current law farther downward. The restoration target remains the highest valid rank previously lost to unresolved Event 61 cycles.

The Return to Rearmament decision can move the law upward only while the current rank is below that target.

A player who wants to move above the recorded target uses the normal law system or another event.

### External law changes

If Event 82 or another valid system moves the law upward, the current law rank naturally advances toward the Event 61 restoration target.

Return to Rearmament must detect that change before offering another law restoration step.

It must not grant a second upward step for a rank that has already been restored externally.

## Conscription law movement

### Ordered law ladder

Event 61 recognizes the following ordinary conscription order from the largest obligation to the smallest:

1. Scraping the Barrel
2. All Adults Serve
3. Service by Requirement
4. Extensive Conscription
5. Limited Conscription
6. Volunteer Only
7. Disarmed Nation
8. No Army after Evolution III introduces it

The baseline moves one valid step downward toward Disarmed Nation.

Examples:

| Law before | Law after baseline |
| --- | --- |
| Scraping the Barrel | All Adults Serve |
| All Adults Serve | Service by Requirement |
| Service by Requirement | Extensive Conscription |
| Extensive Conscription | Limited Conscription |
| Limited Conscription | Volunteer Only |
| Volunteer Only | Disarmed Nation |
| Disarmed Nation | Disarmed Nation |
| No Army | No Army |

No Army is below Disarmed Nation. The ordinary baseline does not force it.

### Manpower meaning

The baseline does not add a positive manpower grant.

The law change reduces the population share that remains available for military recruitment. The released portion returns to civilian life through the normal recruitable population model.

Deployed division manpower is not returned by the baseline law step. Deployed manpower returns only when divisions are safely disbanded during Evolution II, Evolution III, or ordinary player action.

### Restoration target

Record the highest ordinary conscription rank removed by unresolved Event 61 cycles.

Working variable:

`return_to_peacetime_conscription_restore_target_rank`

Return to Rearmament can restore the law one step at a time until the current law reaches that target.

External law changes count. The event must not duplicate them.

## Industrial Reconversion Shock

### Role

The baseline creates one staged national spirit that represents cancelled contracts, retasked machinery, broken supply chains, labour transfers, and the loss of military production rhythm.

Working name:

`Industrial Reconversion Shock`

This is one lifecycle spirit with staged variants. The event should not create several simultaneous small penalties.

### Default phases

| Phase | Default duration | Military factory output | Dockyard output | Production efficiency growth | Production efficiency cap |
| --- | ---: | ---: | ---: | ---: | ---: |
| Severe reconversion | 90 days | major penalty | strong penalty | major penalty | strong penalty |
| Disrupted contracts | 90 days | strong penalty | moderate penalty | strong penalty | moderate penalty |
| Civilian transition | 90 days | moderate penalty | light penalty | moderate penalty | light penalty |

Initial balance target:

| Phase | Military factory output | Dockyard output | Efficiency growth | Efficiency cap |
| --- | ---: | ---: | ---: | ---: |
| Severe reconversion | `-50%` | `-30%` | `-40%` | `-15%` |
| Disrupted contracts | `-35%` | `-20%` | `-25%` | `-10%` |
| Civilian transition | `-20%` | `-10%` | `-10%` | `-5%` |

These values are starting targets for implementation balance. They must be centralized and audited against vanilla production modifiers.

### Repeat firing behavior

A repeat firing during the shock returns the country to the severe phase and extends the unresolved transition.

The total remaining duration is capped at a balance target of 540 days.

The event refreshes one spirit. It does not stack copies.

### Rearmament mitigation

Restarting arms contracts and reaching higher Readiness can mitigate part of the output penalty after the first severe period.

Rearmament should not erase the shock immediately.

A country at high Readiness may reduce the effective penalty by up to one quarter after 90 days, while accepting a civilian factory burden through its active rearmament program.

### Civilian route

A country that does not rearm lets the shock expire naturally.

Later evolved reconstruction benefits can shorten repair and conversion disruption without restoring military output.

## Country report data

The national report should have access to these recorded values:

- eligible military factories before conversion
- military factories converted
- civilian factories added
- War Support before and after
- Stability before and after
- transfer lost to the Stability ceiling
- economy law before and after
- conscription law before and after
- whether a law component was incompatible or already at its floor
- whether the category was opened or refreshed
- whether an evolved countdown has begun

Player-facing text should mention only values that changed or explain why a visible component resolved at zero.

## Baseline option direction

The baseline popup is an acknowledgement of a forced global transition.

The option should sound like a government accepting that civilian demands have become unavoidable.

Its tooltip must show the actual country-specific results and identify Return to Rearmament as the recovery path.

It should not pretend that the player chose the demobilization.

It should not reveal later evolution outcomes.

## Return to Rearmament category activation

The category becomes active when any of these conditions is true:

- the country owns a state with unresolved converted factory capacity
- the current economy law is below its Event 61 restoration target
- the current conscription law is below its Event 61 restoration target
- Industrial Reconversion Shock is active
- an Event 61 evolution mission or response is active
- the country is under Peacetime Economy or No Army
- a valid Event 61 exit project is in progress

The category closes only when all Event 61 recovery, warning, ledger, law, and spirit surfaces have resolved or have been permanently abandoned.

A later Event 61 firing can reopen it.

## Bounded country pulse

The event needs periodic reconciliation without a permanent whole-world on-action.

Each affected country with an active transition receives a hidden scheduled country event at a balance target interval of 30 days.

The pulse should:

- recalculate Rearmament Readiness
- reconcile external law changes
- reconcile state ledger ownership within the country's owned states
- advance staged spirits when needed
- check deferred Evolution III settlement conditions
- clean up completed state
- reschedule itself only while an Event 61 surface remains active

Decision effects and event outcomes should call the same recalculation immediately.

The implementation should not add `on_daily`, `on_weekly`, or `on_monthly` whole-world iteration for this event.

## Repeat-cycle merge rules

The baseline always applies on each valid firing.

Evolved countdowns are singleton surfaces per country.

When Event 61 fires again while one of its evolution missions is already active:

- do not create a duplicate visible mission
- increment a bounded pending-cycle pressure value
- refresh the mission deadline only when the new firing would otherwise resolve after the existing deadline
- let the evolution resolution scale from the merged pressure within its own hard cap
- record the later baseline firing separately in Event History
- clear the merged pressure after the pending evolved effect resolves

This protects the player from duplicate mission rows and protects performance from parallel country timers.

## Chaos accounting

The baseline transaction adds no event-owned Chaos beyond the shared Minor Event firing source already handled by the global system.

Factory conversion, law reduction, War Support transfer, reconversion, stockpile dismantling, division demobilization, and adoption of peace laws do not create separate Event 61 Chaos gains or reductions.

The event does not grant a repeatable Chaos reduction for choosing pacifist outcomes. Such a reward would be farmable.

Evolution eligibility and activation add zero Chaos.

If the Peace cluster also ends a war through White Peace, the peace-related Chaos result belongs to the White Peace or shared peace system.

## Event Logs integration

Event 61 needs the full event log contract.

The history entry should record:

- event ID 61
- firing date
- global scope
- repeat count
- number of valid countries affected
- total military factories converted
- number of countries whose economy law changed
- number of countries whose conscription law changed
- total number of countries entering or refreshing reconversion shock

The global row should not assign a misleading national actor flag.

Country-specific report values remain in the national popup and optional event-owned documentation surfaces. The main history row should stay concise.

Each evolution uses the shared evolution record path with its own type, stage, tier, and optional national actor when a country-specific milestone is important.

## Peace cluster integration

Event 61 becomes the High member of Cluster 4, Peace.

The cluster member order should be:

1. Event 9, White Peace, Low member
2. Event 61, Return to Peacetime, High member

White Peace resolves first so armies and economies can demobilize after any valid wars end.

If White Peace has no eligible war, it records its skip reason and Event 61 can still execute.

Member minimum Chaos rules remain valid. White Peace can be unavailable at a lower Chaos tier while Return to Peacetime remains eligible.

The cluster counts as one global pacing event. Each fired member still records its own history and applies its own repeatable weight and cap behavior.

Human players should receive one Event 61 national report after the cluster transaction. They should not receive one popup for every AI country.

## Multiplayer behavior

Every human-controlled affected country receives its own national report and decision category.

The global entry and history record occur once.

All state ledger, Readiness, law targets, decisions, missions, and evolution responses remain country-specific.

A country transferred from player control to AI immediately uses its AI stance on the next country pulse.

A country transferred from AI control to a player keeps its current Event 61 state and presents the active category without resetting decisions, timers, or ledgers.

No player receives another player's private country calculation unless the shared UI already exposes that information.

## Acceptance conditions for the core event

The baseline design is satisfied only when all of the following are true:

- `chaosx.nr61.1` triggers the global transaction exactly once per firing
- every valid ordinary country is processed once
- the factory conversion total equals `floor(eligible military factories / 2)` for each country
- every physical conversion is one-for-one and ledgered
- later restoration cannot create free building levels
- one half of War Support is removed before the same amount is added to Stability
- overflow at the Stability ceiling is handled honestly
- economy and conscription laws move through explicit ordered ladders
- external law changes cannot be duplicated through the category
- baseline law changes do not force the two Evolution III laws
- one staged reconversion spirit is used
- repeat firings refresh and extend one spirit within its cap
- each human player receives one accurate national report
- one global history row is recorded
- the Return to Rearmament category opens whenever any relevant surface remains
- reconciliation uses bounded scheduled country events and no permanent whole-world scan
