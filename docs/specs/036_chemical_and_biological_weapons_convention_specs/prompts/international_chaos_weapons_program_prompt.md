# International Chaos Weapons Program implementation prompt

Implement the International Chaos Weapons Program exactly from `08_international_chaos_weapons_program.md` and `matrices/chaos_weapon_registry_contract.md`.

This work begins with repository discovery.

Read `AGENTS.md`, `chaos-redux-events`, the relevant CBRN and special-project documentation, current project bridges, every candidate source event, and every owner API before writing the registry.

Use `chaosx_scripted_system_architect` for the provider contract, source-isolation design, contribution ledger, atomic completion transaction, cancellation callbacks, and bounded scheduler.

The parent retains final event integration and completion ownership.

## Registry

Enumerate only real supported weapon prerequisites proven by live source.

Treat Zombie Weapon and Black Plague Weapon as examples that still require exact source verification.

Do not infer projects from localisation, comments, unused assets, or plans.

Each provider must register a stable ID, display token, source owner, exact prerequisite, eligibility trigger, normal-availability trigger, participant trigger, narrow grant adapter, contribution profile, progress factor, immediate cancellation callback, isolation proof, and cleanup adapter.

Block any provider that cannot grant only the prerequisite or cannot distinguish normal availability.

## Equal selection

Build a deduplicated complete candidate array.

Select one candidate uniformly.

AI, war state, member capability, project power, and contribution capacity must not affect selection probability.

Run probability inspection and exact evaluation for candidate counts one through five and for duplicate registration.

## Progress and contributions

Use one global project at a time, one normalized progress value, provider-adjusted target, four contribution families, country cooldowns, exact debit helpers, participant receipts, and small-country floors.

Do not expose internal progress units.

Prevent one large country from completing the project in one unbounded action.

Apply each receipt once across save and reload.

## Completion

Completion must recheck normal availability before any grant.

Grant only to active compatible ratifiers that completed at least one valid contribution.

Open only the exact prerequisite or research route.

Do not fire or advance the source event.

Record and assert every forbidden source side effect before and after the grant.

## Cancellation

The source owner must call the Event 036 cancellation callback in the same transaction that makes the normal route available.

Cancellation freezes contributions, discards progress, preserves spent costs and historical receipts, grants no duplicate unlock, clears the active project, and rebuilds the pool.

A bounded 30-day coordinator heartbeat is only a fail-safe.

Do not use a whole-world daily or monthly scan.

## Dormancy and pause

When no candidate exists, enter Dormant and wake through provider callbacks or a bounded 90-day coordinator recheck.

When charter quorum is lost, pause and preserve progress.

When the charter is repealed, cancel and discard progress.

## Validation

Run acceptance scenarios `E36_A24` through `E36_A39` and the probability scenarios `E36_P12` through `E36_P14`.

Produce a provider table with exact source files, IDs, adapters, callbacks, candidate status, grant scope, isolation proof, and blockers.

Do not mark the program complete with a guessed provider, broad source reward effect, missing callback, unequal selection, non-contributor unlock, or unverified source isolation.
