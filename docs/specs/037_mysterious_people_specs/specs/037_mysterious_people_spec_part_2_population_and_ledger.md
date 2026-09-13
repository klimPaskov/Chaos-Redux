# Event 037: Mysterious People

## Part 2: Population creation and provenance ledger

## Real population is authoritative

Every person created by Event 037 becomes part of the state's real civilian population. The event cannot represent the newcomers only through recruitable manpower, a national spirit, a temporary modifier, a hidden reserve, or an abstract country total.

After a firing, the following systems must read the larger population through their ordinary rules:

- state and country population displays
- world population totals
- recruitable-population calculations
- civilian death calculations
- strategic bombing and nuclear mortality
- disease and outbreak mortality
- famine mortality
- camp and atrocity mortality
- migration and forced-displacement transactions
- occupation and resistance systems that use population
- the shared Deaths denominator and country totals

The Event 037 ledger records provenance. It never replaces real population as the gameplay source of truth.

## State provenance ledger

Each state keeps one persistent value for living people created through Event 037. The working design name is `mysterious population`, with final script naming left to implementation.

The ledger follows these invariants:

1. The value begins at zero.
2. A successful Event 037 grant increases it by the amount actually added to state population.
3. The value can never fall below zero.
4. The value can never exceed the state's current real population.
5. General civilian losses reduce it by the mysterious share of the affected population.
6. Explicit persecution of mysterious people reduces it by actual targeted deaths or survivors moved.
7. Ownership and control changes do not erase it.
8. Migration transfers the appropriate mysterious share to the destination.
9. A state with zero living mysterious people leaves active Event 037 processing after any remaining local consequence has ended.

The state keeps one total after several firings. The event may retain a compact internal generation reference for flavour or reconciliation, but the gameplay system must not require the player to manage separate first-wave, second-wave, and third-wave populations.

## Derived original population

The population that did not originate through Event 037 is derived as:

```text
original population = current real state population minus living mysterious population
```

The result has a floor of zero.

This derived value supports proportional loss accounting and flavour. It does not become another player-facing population total.

## Population grant model

Each state uses its pre-fire real population, not a country or world average. The grant model should create proportional growth while protecting small states from a meaningless result and protecting the largest states from an uncontrolled single-state increase.

The intended shape is:

```text
stage grant = a population ratio clamped between a practical local floor and a stage cap
```

The practical floor is limited by a local share ceiling. This prevents a fixed minimum from doubling a very small state.

| Event stage | Main ratio | Nominal floor | Per-state cap | Small-state local ceiling |
| --- | ---: | ---: | ---: | ---: |
| Baseline | `2.5%` | `1,000` | `1,500,000` | `5%` |
| Evolution I | `6%` | `2,500` | `3,000,000` | `10%` |
| Evolution II | `12%` | `5,000` | `7,500,000` | `20%` |
| Evolution III | `25%` | `10,000` | `20,000,000` | `40%` |

The balance matrix provides examples across small islands, rural states, normal industrial states, and very large urban states. These values are planning anchors. Implementation should tune them against installed state-population distribution while preserving the intended scale relationship.

## Grant calculation principles

The final calculation must preserve these rules:

- current stage sets the ratio, floor, cap, and small-state ceiling
- each state snapshots population before the grant
- previous Event 037 arrivals count in the snapshot
- the grant is rounded to a whole number of people
- applied amount is never larger than the calculated grant
- the ledger increases only by the applied amount
- one state cannot receive multiple grants from one firing
- cluster, manual test, or multiplayer presentation cannot duplicate the transaction
- states that become invalid during the firing fail closed and receive no partial ledger update

The event should not reduce the grant because a state already contains many mysterious people. Compounding is part of the premise. Support pressure, policy, migration, famine, and deaths provide the consequences of excessive concentration.

## World and country totals

The event tracks derived totals for presentation and milestone checks:

- living mysterious population in each country
- living mysterious population controlled by each country when occupation matters
- total living mysterious population in the world
- population created by the latest firing
- lifetime population created by Event 037
- lifetime Event 037 deaths, divided between ordinary losses and targeted atrocity losses where the source system can prove the distinction
- lifetime Event 037 survivors transferred through Migration

Country totals should update incrementally when population is created, killed, moved, or changes owner. They should not require a whole-world recount every day or every month.

A bounded reconciliation pass may rebuild totals after a migration transaction, ownership change, save migration, detected invariant failure, or explicit debug action. Reconciliation is a repair path, not the normal runtime loop.

## General civilian losses

Most disasters and wars do not target Event 037 arrivals by origin. When an ordinary population-loss system removes civilians, the mysterious ledger loses the same proportional share as the state's living mysterious population.

Example:

- a state has `1,000,000` people
- `200,000` are recorded as mysterious
- an untargeted disaster kills `100,000`
- the mysterious share is `20%`
- the Event 037 ledger loses approximately `20,000`
- real state population loses the full `100,000`

Rounding must conserve the actual population transaction. The ledger reduction cannot exceed real loss or living mysterious population.

This rule applies to ordinary mortality from famine, disease, bombing, conventional civilian harm, chemical and biological incidents, nuclear attacks, natural disasters, cannibalism, and other untargeted population loss.

The population-loss owner remains responsible for the real mutation and Deaths registration. Event 037 receives the applied result and adjusts provenance once.

## Targeted losses

A policy that explicitly targets mysterious people uses exact provenance accounting.

1. The atrocity or forced-movement owner requests a target amount.
2. The request is limited by living mysterious population in the state.
3. The shared population transaction applies the real loss or transfer.
4. Event 037 reduces its ledger by the amount actually killed or moved.
5. Deaths, evidence, Condemnation, resistance, migration, and other consequences remain with their owners.

A targeted action cannot remove more mysterious people than exist. It cannot reduce the ledger without the matching real population transaction. It cannot lower food pressure through a hidden ledger-only subtraction.

## Migration composition

Every Migration cohort originating in an Event 037 state carries provenance composition.

For ordinary flight, evacuation, reception, resettlement, or return, the mysterious share matches the origin state's current mysterious share unless a narrower group was explicitly selected.

For forced relocation or deportation aimed at mysterious people, the transferred cohort can be fully mysterious up to the living ledger amount.

The transfer must satisfy these conservation rules:

- origin real population loses the full departing cohort once
- origin mysterious population loses mysterious survivors and any mysterious route deaths once
- destination real population gains survivors once
- destination mysterious population gains only mysterious survivors
- route deaths enter the shared Deaths system through Migration
- no survivor exists in both states
- a blocked border creates trapped population, not erased population

The destination inherits the support burden created by arriving survivors. A successful planned settlement may distribute people across several destinations while preserving the same total.

## Ownership and control changes

The state ledger belongs to the state, not the country that controlled it when the population appeared.

When control changes:

- the controller becomes responsible for immediate food, order, settlement, and relief actions
- the owner retains country-history facts that describe earlier policy
- national pressure calculations use the current policy authority defined by the relevant humanitarian system
- occupied-state actions respect occupation and access rules
- Event 037 country totals update without changing state total

When ownership changes:

- living mysterious population transfers with the state
- the former owner's current living total falls
- the new owner's current living total rises
- lifetime created and lifetime death records remain historical
- active missions and decisions re-evaluate target validity

Annexation cannot reset pressure or erase evidence. Liberation cannot duplicate population. A civil war keeps the ledger attached to the states divided between the sides.

## Integration state

Each active state may keep an internal integration status from `0` to `100`. A higher value means the newcomers have entered ordinary employment, registration, education, military administration, and local institutions.

Integration is not a second public meter. The state can show a qualitative status when it affects an immediate decision.

| Internal range | State status direction |
| --- | --- |
| `0` to below `25` | Unregistered |
| `25` to below `50` | Processing |
| `50` to below `75` | Settling |
| `75` to below `100` | Integrated |
| `100` | Fully absorbed |

Recommended starting direction:

| Stage | Starting integration |
| --- | --- |
| Baseline | High, usually near Integrated |
| Evolution I | Moderate to high |
| Evolution II | Moderate |
| Evolution III | Low to moderate in overloaded states |

Integration rises through stability, spare services, housing, employment, open policy, successful missions, and time. It falls or stalls through occupation, famine, severe overcrowding, persecution, isolation, war damage, and repeated arrivals.

If the engine cannot distinguish recruitable share by provenance, implementation should preserve real population and represent incomplete military integration through a temporary effect tied to the unintegrated share. The effect must be verified against actual recruitable behavior and must disappear as integration completes.

## Children, age structure, and military use

The event does not need a public age pyramid. Created population includes families and a plausible age distribution.

Military benefit should arrive in stages:

- existing military-age adults contribute after registration and integration
- children contribute only through ordinary future population logic when supported
- immediate full mobilization of every created person is forbidden
- high conscription laws still face integration delay
- military governments can accelerate registration at a political and social cost

The exact conversion must follow engine behavior. The design goal is a strong long-term manpower benefit without several million instantly deployable soldiers on the same day.

## Settlement and strategic capacity

Mysterious houses and villages exist in the event fiction, but strategic support capacity does not rise automatically to match population.

These remain separate investments:

- infrastructure
- railways
- supply hubs
- housing
- agricultural expansion
- water and sanitation
- urban transport
- clinics, schools, and administration
- civilian and military industry

This distinction drives the later crisis. The anomaly creates people and local social context. It does not create an unlimited national logistics system.

## State concentration

A state can contain more mysterious people than original inhabitants. The ledger remains valid when mysterious share passes `50%` or approaches the full living population after repeated firings, migration, and ordinary losses.

High concentration changes flavour and pressure:

- memory contradictions become more common
- institutions can be dominated by people whose records predate appearance
- persecution risk rises under hostile policy
- migration carries a larger mysterious share
- ordinary disaster kills a larger mysterious share through proportional accounting
- successful integration can produce a powerful workforce

The design does not impose a hidden cap that deletes arrivals above a chosen share.

## Ledger visibility

The player sees the national living total and selected-state status. Detailed data belongs in tooltips or debug surfaces only when it explains a specific action.

A selected-state tooltip should answer:

- how many mysterious people live here
- what share of state population they represent
- whether integration is broadly healthy or failing
- which main factor drives current pressure
- which action can improve the situation

It should not show every internal multiplier, adapter version, receipt, or reconciliation value.

## Integrity failures

The system fails closed when provenance proof is incomplete.

Examples include:

- a targeted killing request has no valid state
- a migration receipt lacks an applied survivor count
- a loss transaction reports more mysterious deaths than living mysterious population
- a destination cannot receive credited survivors
- a state ledger exceeds real population after an external mutation
- a stale country total disagrees with active state registry

A failed transaction applies no guessed population change. A bounded reconciliation may repair totals from authoritative state data. Debug evidence identifies the owner and failed transaction without exposing developer text to players.

## Save and reload contract

All state ledgers, country totals, world totals, milestone flags, policy states, active registries, and pending receipts survive save and reload.

After reload:

- no firing repeats because a delayed report was pending
- no Migration transfer credits survivors twice
- no population grant reapplies
- no ownership update duplicates a country total
- no zero-ledger state remains registered without a consequence
- no active pressure state disappears while population remains
- milestone Chaos gains remain one-shot

Acceptance scenarios include save and reload after creation, migration, ownership change, famine mortality, and targeted atrocity mortality.
