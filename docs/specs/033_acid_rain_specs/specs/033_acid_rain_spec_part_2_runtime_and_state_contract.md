# Event 033 Acid Rain, Part 2, runtime and state contract

## Ownership model

Event 33 owns one global runtime, up to three ordinary fronts, one global-layer state, national preparedness records, state exposure records, and permanent event history. No country owns the world scheduler. The host-authoritative global scope advances fronts and state pulses.

## Runtime schema

Use a versioned schema from the first implementation. Suggested identity:

- `global.acid_rain_schema_version`
- accepted first complete schema value `1`
- `acid_rain_active`
- `acid_rain_dissipating`
- `acid_rain_recovery_tail_active`

Every initialization, load reconciliation, migration, and cleanup path checks the schema before mutating arrays.

## Global variables

The final names can follow repository naming standards, but the runtime must hold these facts:

| Fact | Persistence | Purpose |
| --- | --- | --- |
| start date | Permanent history | Event duration and reports |
| active phase | Active runtime | Formation, regional, multiple, global, dissipation, recovery |
| highest enabled evolution | Permanent history | Event Details and cumulative behavior |
| eligible state count | Active and history | Coverage denominator |
| touched state count | Active and history | Coverage numerator |
| coverage percent | Derived display | GUI and completion check |
| event civilian deaths | Permanent history | Sum of actual state population removed by Event 33, used by GUI, reports, and achievements |
| prevented-death estimate | Permanent history | Preparation report and achievements |
| building damage points | Permanent history | Reports and balance review |
| lifetime contamination added in bp | Permanent history | Hard cap and GUI |
| current event source pressure in bp | Air source state | Source ledger display |
| first cross-region receipt | Permanent flag | Direct Chaos deduplication |
| severe impact receipt | Permanent flag | Direct Chaos deduplication |
| second-front receipt | Permanent flag | Direct Chaos deduplication |
| third-front receipt | Permanent flag | Direct Chaos deduplication |
| global-layer receipt | Permanent flag | Direct Chaos deduplication |
| final coverage date | Active and history | Dissipation minimum wait |
| dissipation check index | Active runtime | Guaranteed endpoint |
| next exposure pulse date | Active runtime | Three-day state processing |
| next drift pulse date | Active runtime | Six-day footprint movement |
| next contamination pulse date | Active runtime | Weekly contamination request |

## Global arrays

### Frozen eligibility

- all eligible states
- eligible state count by stable region ID
- optional eligible-state index by state ID for fast membership proof

The eligible registry is built once at formation. It is rebuilt only by a schema migration or explicit load repair when the active flag exists and the registry is missing.

### Coverage

- touched state ledger
- touched-state membership receipt keyed by state ID
- first-touch date keyed by state ID
- first-touch front ID keyed by state ID

The touched count increments only when the membership receipt changes from false to true.

### Front arrays

Each front owns separate active-state, recently-retired-state, severe-cell-state, and visit-touched-state arrays. Do not store three fronts in one array without a stable front identifier because cleanup and display must remain independent.

### Country registries

Maintain bounded country arrays for:

- countries with the category initialized
- countries with active exposure
- countries with unresolved aftermath
- countries with a pending warning or report
- countries with active preparation commitments

A country leaves an active registry when its final relevant state or project closes. The system never uses an all-country daily maintenance pass.

## Region identifiers

Keep the existing seven-region concept as stable internal data:

| ID | Region |
| --- | --- |
| 1 | Europe |
| 2 | Middle East |
| 3 | Asia |
| 4 | Africa |
| 5 | Australia and Pacific states mapped there |
| 6 | North America |
| 7 | South America |

Every frozen eligible state must map to exactly one supported region. Initialization fails closed and logs the state ID if a populated valid state maps to none or more than one. Island states use their engine continent assignment. They are not silently skipped because they lack land neighbors.

## State eligibility

A state is eligible when all conditions hold at formation:

- land state
- positive civilian population
- valid state scope
- valid owner or other repository-approved responsible scope
- one supported region ID
- not an ocean, impassable shell, map dummy, or state excluded by the shared civilian-loss safety trigger

Eligibility is frozen. Later occupation, annexation, civil war, or controller changes do not remove the state from the coverage denominator and do not reset its touched receipt.

## Front record

Each of the three front slots stores:

- active flag
- front ID
- current region ID
- previous region ID
- current intensity band
- exact intensity multiplier
- current visit sequence
- current visit quota
- unique states touched during this visit
- active-state target size
- minimum departure date
- movement due window start and end
- next target region ID when warning is active
- warning reveal date
- movement count
- consecutive no-new-coverage count
- severe-cell active flag
- severe-cell episode ID
- severe-cell start and end dates
- severe-cell cooldown date
- severe-cell intensity multiplier

A front slot is cleared only by its dedicated close helper. The helper removes the slot's state membership, warning, severe-cell membership, and timers before the slot can be reused.

## Country record

Every country receives the category at formation and stores:

- four Preparedness component tiers, 0 to 4
- exact Preparedness value, 0 to 100
- country cost band
- current active project count
- maximum concurrent project count
- temporary resource commitments and their return dates
- number of active exposed states
- number of severe-warning states
- number of unresolved aftermath states by tier
- Event 33 deaths in current country responsibility
- estimated deaths prevented
- national arrival count
- last arrival report date
- last casualty-threshold report date
- last successful-protection report date
- recovery-tail completion receipt
- achievement facts and disqualifiers

Country data follows current responsibility for live decisions. Permanent history keeps the country that owned or controlled a state when a loss was applied so later border changes do not rewrite past totals.

## State record

Every eligible state needs sparse values or keyed arrays for:

- touched receipt
- first-touch date
- current front ID, or zero
- current exposure episode ID
- ordinary opening shock receipt for that episode
- severe-cell episode ID
- severe opening shock receipt for that episode
- global transition shock receipt
- current intensity multiplier
- accumulated damage pressure
- current acute modifier band
- current environmental aftermath tier
- cumulative Event 33 requested deaths
- cumulative Event 33 applied deaths, equal to real state population removed
- most recent pre-pulse and post-pulse civilian population for transaction proof
- latest committed mortality pulse key
- cumulative Event 33 building damage points
- most recent responsible country
- local evacuation active flag and end date
- last exposure date
- recovery completion receipt

A new ordinary exposure episode begins when a state enters an active footprint after at least six full days outside all ordinary footprints. A short drift gap below six days preserves the same episode and cannot retrigger the opening shock.


## State population mutation contract

Every opening, sustained, severe, global, and superstorm mortality calculation is a real state-population transaction.

1. Read the current civilian population of the affected state.
2. Calculate requested deaths from the Part 4 formula.
3. Apply the per-pulse cap, episode cap, and protected population floor.
4. Prove that the mortality pulse key has not already committed.
5. Call `apply_exact_state_civilian_population_loss` in state scope with the requested amount, protected floor, accepted Deaths cause, responsible country, and one-shot contract proof.
6. Read `state_civilian_population_loss_applied` and `state_civilian_population_loss_result` returned by the helper.
7. Treat the returned applied amount as the only authoritative death value.
8. In the same effect chain, commit the pulse receipt and add the applied amount to state, country, and global Event 33 death totals.
9. Schedule reports and threshold checks only after the population transaction has committed.

The post-pulse state population must equal the pre-pulse state population minus the returned applied loss, within the helper's protected floor. A `local_manpower` or recruitable-population modifier can remain as a separate operational penalty, but it cannot represent, replace, or inflate civilian deaths. If the exact population helper returns zero, Event 33 records zero deaths for that pulse.

When shared Deaths logging is disabled, the helper's unlogged transaction path must still remove the real state population unless the repository's global settings contract explicitly disables civilian population loss itself. Disabling a history panel must not make the lethal rain harmless.

## Initialization transaction

The formation chain must complete in this order:

1. Verify Event 33 is not active, fired, reserved by another cluster, or blocked by a terminal world state.
2. Set the schema and a temporary initialization lock.
3. Clear stale prototype flags and arrays only through the migration-aware cleanup helper.
4. Build the frozen eligible-state registry and region counts.
5. Abort cleanly if the registry is empty or has a mapping error.
6. Initialize global counters, coverage ledgers, country records, and front slots.
7. Add Event 33 to the Air Contamination source ledger with zero current pressure if the ledger requires explicit registration.
8. Choose the highest evolution stage allowed at the firing moment.
9. Create the first front or the appropriate higher-stage opening state.
10. Apply the first active-state memberships and state modifiers.
11. Give the category to every existing country in a one-time formation pass.
12. Show the formation super-event through the accepted super-event framework.
13. Register the event history row and enabled evolution subrecords.
14. Apply the one-time formation Chaos outcome.
15. Schedule the first exposure, drift, contamination, and GUI refresh dates.
16. Remove the initialization lock and set the active flag.

If any required step fails before step 14, rollback all new runtime state and leave Event 33 unfired. After history and Chaos are committed, failures enter the fail-closed recovery path and cannot silently refire the event.

## Scheduled processing

### Exposure pulse

Every three days, process only states in front active arrays, severe-cell arrays, or the global-layer eligible registry. Apply opening receipts, sustained mortality, damage pressure, state modifiers, reports, and national counters.

### Drift pulse

Every six days, process each active front. Retire old states, add new states, update coverage, and evaluate region departure. The global layer does not use this pulse.

### Contamination pulse

Every seven days, calculate one Event 33 request from active coverage, intensity, severe cells, and phase. Clamp the request before calling the central Air Cleanliness mutation helper.

### Front movement pulse

Each front moves on its own due date after any warning period and visit quota rule are satisfied. Multiple-front processing is ordered by front ID for deterministic behavior.

### Dissipation pulse

After coverage and minimum-wait conditions, run only on the scheduled check date. Never roll dissipation every day.

## Performance contract

Allowed broad scans:

- one all-state registry build at formation
- one all-country category initialization at formation
- one bounded reconciliation on loading a broken active save
- one final country cleanup pass if required by the decision framework

Forbidden runtime patterns:

- daily or weekly all-country iteration
- daily or weekly all-state iteration during regional or multiple-front phases
- every-country then every-owned-state nested loops
- rebuilding world coverage from state modifiers every pulse
- GUI opening that mutates gameplay or scans the world

Target runtime budget:

- ordinary pulse work proportional to active footprint states
- multiple-front work proportional to the union of active footprint states
- global phase work proportional to the frozen eligible registry on a three-day pulse, accepted because every valid state is genuinely active
- GUI list work proportional to seven regions plus at most three front cards and bounded country summaries

## Cleanup invariants

At acute dissipation:

- stop exposure, drift, warning, severe-cell, movement, and contamination scheduling
- clear every front and active acute-state array
- remove acute state modifiers only from tracked active states
- preserve aftermath tiers and recovery registries
- preserve touched and history facts
- preserve lifetime contamination added
- preserve Deaths records
- close pending warning events that no longer have an arrival

At recovery-tail completion:

- remove the decision category from countries with no unresolved aftermath or commitment
- return any temporary manpower commitment that is still valid
- clear bounded country registries
- retain only event-history and achievement facts

Every cleanup helper is idempotent. Calling cleanup twice must produce the same state as calling it once.
