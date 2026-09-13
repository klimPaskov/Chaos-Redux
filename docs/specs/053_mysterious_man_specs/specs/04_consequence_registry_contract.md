# 4. Consequence Registry Contract

## Ownership

Event 53 owns one authoritative consequence selector with the working name:

`mysterious_man_apply_random_consequence`

This selector belongs in Event 53's owner files. It must not be moved into the neutral shared dynamic-effect registry. The selector owns Event 53 validity, equal weighting, selection, attribution, transaction state, lifecycle integration, and receipts.

Connected systems expose bounded adapters. They remain responsible for their own target resolution, gameplay effects, state mutation, delayed processing, aftermath, cleanup, and internal safety rules.

## Definition of a consequence package

A consequence package is one substantively distinct harmful outcome registered with Event 53.

A package receives one ballot when valid. The following do not create extra ballots:

- target state variants
- target country variants
- severity variants within the same package
- flavour text variants
- visual variants
- regional variants that use the same gameplay identity
- several valid disasters inside the Natural Disasters owner
- several valid targets inside one war, uprising, or assassination package
- stronger versions of the same package at higher evolution behavior

A separate ballot is justified when the outcome has a distinct strategic identity, owner contract, target shape, or aftermath. A normal civil war and a multi-front civil fracture are separate packages. Train destruction and convoy destruction are separate packages because they attack different strategic systems. Smallpox and plague are separate top-tier outbreak packages because their owning disease behavior and campaign consequences differ materially.

This rule prevents registry stuffing. A system cannot gain more aggregate chance by exposing many cosmetic or target variants.

## Registry entry contract

Every package entry must define:

| Field | Required content |
| --- | --- |
| Stable package ID | Event 53-owned constant or stable numeric token |
| Working label | Documentation label, not final localisation |
| Minimum behavior tier | Baseline, Evolution I, Evolution II, or Evolution III |
| Owner | Event 53 or a named crisis system |
| Validity trigger | Read-only proof that the package can complete now |
| Apply adapter | One bounded effect that accepts Event 53 attribution |
| Target mode | Country, state, region, character, foreign actor, or compound reservation |
| Severity resolver | Dynamic scale rules that do not create extra ballots |
| Receipt contract | Accepted, rejected, completed, delayed, and cleanup proof as applicable |
| Attribution rule | Event 53 refusal, with no false source-event firing |
| Source bookkeeping rule | Exact source-event systems that must remain untouched |
| Conflict tags | Incompatibilities with other package components or active crises |
| Cleanup owner | System responsible for delayed cleanup and invalid target handling |
| Readiness state | Ready, adapter required, blocked, or excluded |

A package with an incomplete adapter remains absent from the active registry. Documentation can reserve its ID, but a reserved package cannot enter the live pool.

## Fresh-pool rule

Every refusal builds a new candidate pool from the current campaign state.

The build process must:

1. read active Event 53 evolution behavior
2. read the selected target's current state
3. inspect each registered package at or below the active tier
4. add each package exactly once when its full validity trigger passes
5. omit invalid packages completely
6. lock the completed candidate pool for the current transaction
7. select one uniform random index
8. dispatch the selected package
9. accept a final owner receipt
10. clear temporary pool data

The next refusal repeats the complete process. No previous pool is reused.

## Equal probability

If `N` packages are valid, each package has probability `1 / N`.

The selector cannot use:

- strategic weighting
- severity weighting
- recent-history weighting
- anti-repeat weighting
- source-event preference
- evolution preference among already valid entries
- player situation preference after validity is established
- hidden bonus entries
- repeated list entries
- weight values greater than one

A package selected on the previous refusal remains eligible on the next refusal if its current validity trigger passes. There is no no-repeat protection.

## Evolution behavior and existing packages

Higher evolutions affect the registry in two ways:

- they register additional packages
- they allow existing packages to resolve stronger severity bands

An existing package still receives one ballot. Its stronger severity does not create a second entry.

Later evolution behavior does not change the relative weight of two packages that are both valid.

## Validity standard

Validity must prove that the package can perform its core outcome without improvising a substitute.

Examples:

- an occupation revolt requires meaningful occupied or non-core territory and a valid revolt owner
- a convoy catastrophe requires a meaningful convoy system
- a multi-country external war requires enough valid foreign actors and safe war setup
- an assassination requires at least one eligible important character and a safe removal path
- an independence package requires valid releasable movements and viable country packages
- a compound package requires every component and the complete sequence to be valid before it receives a ballot

A package cannot enter and then quietly do nothing. A package also cannot enter with the expectation that an unrelated fallback will replace it after selection.

## Transaction locking

The selector locks:

- target country proof
- refusal transaction ID
- active evolution behavior
- candidate package array or equivalent list
- selected package ID
- any target reservation required by the adapter

The adapter must consume the same locked transaction proof. This prevents target changes between pool construction and application.

## Adapter rejection

A selected adapter should not reject after its validity trigger passed. A rejection indicates a race, stale target, or adapter defect.

The selector should support one bounded recovery:

1. record the rejected package and reason
2. rebuild the current pool from fresh state
3. exclude the rejected package for this transaction only
4. select uniformly from the rebuilt pool
5. dispatch once more

If the second dispatch rejects, Event 53 applies its guaranteed direct government-paralysis package and records an implementation error receipt. This direct package is part of the accepted registry design and is not a mild placeholder.

The player must never receive no consequence after refusing because an adapter failed silently.

## Guaranteed direct package

The Event 53-owned government-paralysis package is valid for every normal target country. It imposes a severe temporary collapse of state capacity through a combination of political, command, stability, war-support, and industrial pressure scaled to the target.

Its exact effect must avoid reducing every value to a meaningless floor, but it must remain substantial for a small state and a major power.

This package serves two roles:

- one ordinary equal-weight baseline consequence
- the final transaction safety package after repeated adapter failure

When used as the safety package, it does not gain an extra ballot in the original pool.

## Receipts

Every adapter returns enough information for Event 53 to close the visit safely.

Minimum receipt fields:

- transaction ID
- selected package ID
- accepted or rejected result
- owning system
- resolved primary target proof
- resolved secondary target proof when applicable
- delayed-job count when applicable
- skipped target count when applicable
- attribution mode
- cleanup owner
- completion state

A delayed owner system can return an accepted queued receipt. Event 53 may schedule the next visit after the owner has safely committed the consequence, even when long aftermath processing continues.

## Attribution

Every selected package is attributed to the Event 53 refusal transaction.

The owner system may use its ordinary public reports, state modifiers, country packages, disease records, famine ledgers, migration cohorts, war setup, or cleanup. It must receive an origin token that distinguishes an Event 53 request from a normal source-event firing.

The Mysterious Man is not represented as an attacker country. Unknown-origin consequences cannot assign Condemnation, war responsibility, diplomatic blame, or nuclear attribution to an innocent actor.

## Source-event bookkeeping isolation

A borrowed package must not:

- increment the source event's fired count
- consume source Fire-Once status
- reduce a source Repeatable weight cap
- recover or change source event weight
- advance the global event timer
- apply source pacing pressure
- create the source event's normal History row
- count as a source cluster firing
- advance source cluster cooldowns
- activate source evolutions automatically
- trigger a source opening super-event automatically
- progress a source world-end route automatically
- satisfy source achievements that require the source event to fire

The source event remains eligible to occur normally later.

Owner-system operational records are allowed when they are required for real gameplay and cleanup. A famine state can enter the famine ledger. A migration cohort can enter the migration ledger. A disaster can create aftermath records. These records must retain Event 53 origin and must not be misrepresented as source-event random-history entries.

## Compound package rule

A compound package is one curated transaction with one ballot. It must define:

- complete prevalidation of every component
- target reservations before mutation
- execution order
- which owner controls each component
- how scopes survive between components
- which component can abort the sequence
- whether any partial state needs rollback
- combined attribution
- final receipt aggregation
- cleanup ownership for every delayed job

A compound package cannot be assembled dynamically from several independent random rolls.

## Registry maintenance

Every new harmful Chaos Redux event or crisis system must be reviewed for an Event 53 adapter.

The review asks:

1. Does the system create a substantial harmful outcome?
2. Can it expose a bounded consequence adapter without firing its source event?
3. Can validity prove that the package will complete?
4. Can it accept Event 53 attribution?
5. Can it avoid source-event history, pacing, evolution, super-event, and world-end bookkeeping?
6. Can it return a receipt and own cleanup?
7. Is it substantively distinct from an existing package?

A positive review adds one registry entry at the appropriate tier. A negative review records why the system is unsafe or duplicative.

Registry maintenance must preserve equal probability. New entries change the pool size by design, but they cannot be added as repeated or weighted variants.
