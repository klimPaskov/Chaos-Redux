# Event 046: Registry, transactions, and safety

## Event-owned framework

The Great Shuffle owns a reusable randomization framework.

Its registry, transaction state, result planning, family selection, reports, and cleanup remain in Event 46's source package.

Other systems expose bounded adapters to Event 46.

Event 46 does not copy their internal logic and does not require a central list of every event-specific variable.

Neutral helpers can move into the shared dynamic registry only when they gain genuine callers across unrelated systems.

An Event 46 helper is not shared merely because it is technically reusable.

## Allowlist first

The framework begins from registered families.

It never scans variables, flags, modifiers, arrays, event targets, objects, or memory to discover candidates.

A new gameplay system is invisible to the Shuffle until its owner registers a safe adapter.

Unknown state fails closed.

An incomplete family is unavailable.

A malformed family cannot fall back to generic numeric mutation.

## Stable family identity

Every family has one stable ID and one owner.

The ID survives save and load and remains distinct from display text.

Renaming player-facing text does not change family identity.

A family ID cannot be reused for a different meaning.

Duplicate registrations are rejected or idempotently merged only when owner, version, and contract match exactly.

The registry records a version so an owner can migrate its adapter without making old saves interpret one value as another.

## Registry lifecycle

The core Event 46 registry initializes through the event package's bounded startup route.

Owner systems register their adapters through owner-controlled setup effects.

Registration is idempotent.

No daily, weekly, or monthly whole-world scan is added for discovery.

Existing-save repair uses the project's bounded registration and synchronization patterns and avoids a permanent global iteration.

A transaction freezes the registry version it started with.

A registration change cannot enter an already planned firing.

## Contract required for every family

Every family declares:

- stable family ID and owner
- minimum evolution capability
- scope kind and scope source
- validity and exclusion rule
- selection group and base weight
- Evolution V mandatory or optional status
- result type and legal range source
- distribution profiles by capability
- compatibility and dependency groups
- result planning method
- commit method
- reconciliation method
- report visibility and importance method
- Chaos severity contribution
- AI refresh need
- save recovery behavior
- cleanup behavior
- test scenarios

The full field matrix appears in `matrices/046_shuffle_registry_schema.md`.

## Owner authority

The owner remains authoritative for lifecycle and meaning.

It can exclude inactive, unresolved, transitional, special, terminal, or malformed instances.

It can reject the whole family when its current world state cannot be reconciled safely.

It can declare a value protected even when the value looks numeric.

The owner cannot use the adapter to expose Event 46's protected framework state.

Event 46 remains authoritative for selection, random result planning, transaction sequencing, report ordering, direct Chaos accounting, and cleanup of its own buffers.

## Transaction state model

### Idle

No Event 46 transaction is active.

No scope carries a live Event 46 result plan.

### Locked

One global transaction ID and registry version are fixed.

A second automatic, cluster, manual, or recovery call cannot open another transaction.

### Snapshotted

The transaction freezes the current capability, Chaos tier, DLC state, legal caps, world anchors, owner registrations, and valid scope lists needed by candidate families.

Only values required for legality, planning, and reports are read.

### Selected

The family roll and compatibility resolution are complete.

The selected list does not change because one later family receives an extreme result.

### Planned

Every selected family has a complete result plan or a complete pre-commit rejection.

No gameplay value has changed yet.

### Validated

Every result, scope, dependency bundle, owner proof, and reconciliation path has passed.

A family that fails is removed before any member of that family commits.

### Committing

Families commit in the dependency order fixed by the plan.

Each family tracks its committed position so recovery can resume idempotently.

### Reconciling

The owner or core family refreshes derived state and proves that the final result is legal.

Reconciliation cannot substitute a new random result after seeing an inconvenient outcome.

### Reporting

The final report reads the frozen before values and committed after values.

The event records direct Chaos once.

### Closing

All temporary scope plans, before values, report candidates, transaction targets, and locks are cleared.

Protected achievement and audit proofs can remain when their sole purpose is later completion tracking.

## Meaning of atomic application

Clausewitz scripting does not provide a general database rollback for arbitrary world state.

Event 46 therefore uses logical family atomicity.

All values and legality checks are fixed before commit.

Commit order cannot affect range generation.

A family either remains untouched because it failed before commit or reaches its complete planned after-state through normal commit or idempotent recovery.

The event does not promise to roll back a family that has already changed half of its scopes.

It promises to finish that family without rerolling or compensating.

The implementation should commit each family in one immediate pass when performance allows.

If batching is required, the transaction lock and immutable plan remain active until the last batch finishes.

No batch can recalculate its range from earlier batches.

The user report appears only after the full transaction closes.

## Result storage

The implementation chooses one result-storage method only after inspecting current engine support.

A valid method can store exact planned values on stable target scopes under the transaction ID.

Another valid method can store an immutable seed schedule plus an immutable ordered scope list when the engine proves that replay produces the exact same values.

The method must survive save and load during a transaction.

It must not create permanent save bloat after cleanup.

It must support enough world scopes for Evolution V without exhausting practical array, variable, or event-target limits.

A report-only summary is not a substitute for a real result plan.

## Ordering and bundles

Most families are independent.

Dependencies are explicit.

The main accepted bundles are:

- state population with reserve manpower side-effect reconciliation
- shared state building capacity with civilian factories, military factories, and dockyards
- party popularity with optional ruling ideology
- production-line legal cap with efficiency and stored progress
- ownership with control, capital, country survival, occupation, and unit handling when the structural adapter exists
- owner mechanic current value with its derived stage or modifier refresh

A bundle is planned as one unit.

It cannot leave one member at the old value because another member received an inconvenient draw.

## Family rejection

A family can be rejected for no valid scopes, missing DLC, missing owner proof, conflicting dependency, unavailable setter, illegal result band, incomplete scope identity, recovery uncertainty, or performance safety.

No valid scopes is normally an ordinary skip.

A malformed core family is an implementation defect.

A malformed owner adapter is rejected and named in debug evidence without exposing internal text to the player.

The player report can state that one selected domain was unavailable, but it should not print variable names or script errors.

## Save and load recovery

The transaction state is protected from shuffling.

A save made during a staged transaction retains its transaction ID, selected families, frozen registry version, planned results, committed positions, and reconciliation status.

On load, the owner resumes the exact transaction.

It does not reroll.

It does not consume a second repeatable firing.

It does not show a second opening or history entry.

When recovery finishes, normal cleanup runs once.

A stale lock with no valid transaction proof fails closed and enters explicit repair logic. It cannot clear itself and reroll.

## Multiplayer authority

One authoritative global context plans the result.

Human clients do not roll local values.

Every player sees the same committed world.

Personal reports are projections of that shared transaction.

A player joining after completion receives the ordinary saved world state and no duplicate report.

A player present during completion receives one report for the country controlled at report creation.

Tag switching cannot open a second transaction.

## Protected framework registry

### Chaos Meter

The current Chaos value, tier, whole-percent buffers, source ledgers, history rows, settings, enable state, and threshold state are protected.

Event 46 can add its own one-time direct Chaos result after commit.

It cannot randomize the authoritative meter.

### Random event system

Event timers, timer acceleration, event weights, caps, recovery, fired history, major-event gain, enabled events, event level, evolution toggles, event arrays, selection state, manual fire state, cluster state, and scenario state are protected.

### Event Logs and Event Details

History arrays, evolution arrays, selected rows, indexes, sorting state, actor proof, event detail registries, world-end rows, and public enable toggles are protected.

Event 46 writes its normal history and evolution records through the shared API.

It never randomizes them.

### World-end and super-event state

The global `world_end` state, terminal owner flags, request state, super-event visibility, current slot, audio ID, settings-aware audio state, and terminal bookkeeping are protected.

### Deaths

Global and country Deaths totals, civilian and military splits, causes, latest changes, thresholds, and history are protected.

Population rewrite bypasses Deaths and suppresses any accidental death registration.

### Air Cleanliness

Current contamination, clean-air remainder, source ledgers, lifetime rises and falls, treaty membership, betrayal memory, Fallout state, and threshold bookkeeping are protected.

An owner may later expose a local non-authoritative pressure through an adapter.

The global authoritative atmosphere cannot be exposed.

### Condemnation and evidence

Public condemnation totals, hidden evidence, tier history, source ledgers, sanctions, cover-up memory, inspection state, and recent-use history are protected.

### Famine and migration

Food Security, reserves, Relief Access, Displacement Load, Reception Capacity, Border Policy, active cohorts, routes, and other current values remain owner adapter only.

Incident history, mortality proof, transfer ledgers, cohort identity, destination proof, versioned receipts, and one-way accounting are protected.

A state population rewrite can change the inputs those systems read on their next normal refresh.

It cannot rewrite their history.

### Camps and repression

Site identity, discovery history, evidence, records, mortality history, authority proof, and atrocity ledgers are protected.

A current owner-declared site pressure can become an adapter only if its lifecycle remains valid.

### Shared world threat

Threat source flags, source count, and the aggregate `world_in_threat` state are protected because they record active owner systems.

### Persistent identity

Country tags, state IDs, province IDs, region IDs, unit IDs, commander and character identity, equipment tokens, technology tokens, production object identity, provider registry identity, event targets used as lifecycle proof, stable array indexes, and transaction IDs are protected.

### Settings, debug, and achievements

User settings, debug variables, test state, feature toggles, achievement completion, achievement disqualifiers, and Event 46 achievement tracking are protected.

## Historical and derived state

A historical ledger records what happened.

It remains protected even when a current gameplay projection can be shuffled.

A derived state can be refreshed after a safe current value changes.

The owner must identify the difference.

For example, current legitimacy can be shuffled through an adapter, while the list of past governments that earned or lost legitimacy remains protected.

## Side-effect suppression

Some setters can trigger generic Chaos, Deaths, politics, diplomacy, or owner hooks.

The transaction uses one bounded source marker so those hooks can distinguish an Event 46 rewrite from an ordinary narrative action.

The marker is active only during the exact commit and reconciliation that needs it.

It cannot suppress later consequences created by normal play.

Changing ruling ideology through the Shuffle should not add the normal ideology-change Chaos on top of Event 46's direct result.

Changing population should not log deaths or migration.

A later civil war, famine, annexation, or military death caused by the new world remains an ordinary generic source.

## Population transaction rule

The existing shared population-loss helpers are not a complete Event 46 setter because they are designed for real civilian loss and Deaths integration.

Event 46 needs an owner-specific absolute population rewrite primitive.

That primitive applies the planned absolute result, observes any recruitable-manpower side effect created by the engine, and reconciles it so the separate national reserve family remains authoritative.

It does not call the Deaths logger.

It must work for population increase and decrease.

It must respect the protected minimum remaining population selected by the family contract.

The helper remains Event 46-owned unless another unrelated system later needs the same ontological rewrite contract.

## Performance contract

Event 46 performs its broad scan only when it fires or resumes a pending transaction.

It does not add a periodic whole-world on-action.

The implementation benchmarks Baseline, Evolution II, Evolution IV with many adapters, and Evolution V with the maximum safe scope set.

Families can use bounded batches when exact result planning and same-transaction recovery remain intact.

The event may exclude a conditional family whose practical cost is unsafe.

It may not silently lower world coverage for core safe families to hide performance problems.

Performance limits, selected scope counts, skipped conditional families, and transaction duration belong in the implementation completion report.

## Cleanup contract

After a successful or safely aborted transaction, no live result plan, stale per-scope transaction variable, temporary event target, selection buffer, report candidate, generic-source suppression marker, or transaction lock remains.

Owner adapters receive one cleanup callback even when their family was rejected after planning.

Protected achievement proofs are stored under separate stable identifiers and are never reused as transaction buffers.
