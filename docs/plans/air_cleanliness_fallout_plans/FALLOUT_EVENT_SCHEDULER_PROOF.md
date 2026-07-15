# Fallout Living-World Scheduler Proof

## Status

The living-world scheduler has a schema-2 dormant transaction-integrity substrate. It records the reveal timeline, freezes a stable post-allocation country registry, initializes country runtime rows, and exposes five-part orientation, anti-repetition, arc, delayed-result, bilateral, cancellation, cleanup, and routing contracts. It does not select a candidate, schedule an event, or fire an event.

The activation flags `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` have no setter. Suffixes `100` through `122` are typed reservations only. Defined event blocks in that range: `0`. Countable blocks toward the 660-block release floor: `0`.

## Owned files

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- the narrow map-return and coordinator calls in `common/scripted_effects/fallout_world_end_effects.txt`

No Fallout event definition, localisation key, decision, focus, on-action file, sound, sprite, or asset path is added by this tranche.

## Reveal timeline transaction

A successful current-schema map return writes all three identity receipts:

- `global.fallout_event_timeline_generation`
- `global.fallout_event_timeline_start_date`
- `global.fallout_event_timeline_start_day`

It then sets `fallout_event_scheduler_initialization_pending`. The project coordinator calls `fallout_event_scheduler_reconcile` inside the existing at-most-once global-date transaction. A successful registry commit or dormant schema promotion clears the pending flag. The separate initialization status remains at orientation pending until future orientation content completes its receipts. No new daily or monthly on-action is added.

`fallout_event_map_return_receipts_are_current` requires completed Fallout, a successful map-return receipt, an inactive transition, the current transition generation, and start date and day values that are not in the future. Elapsed time is recomputed as current engine day minus the frozen reveal day. The exact phase bands are:

| Phase | Inclusive elapsed-day range |
| --- | ---: |
| Ash week | 0 through 7 |
| First season | 8 through 90 |
| First winter year | 91 through 365 |
| Consolidation | 366 through 730 |
| Rival orders | 731 through 1460 |
| New states | 1461 through 2190 |
| Soot retreat | 2191 through 2920 |
| Second world | 2921 through 3650 |
| Open continuation | 3651 onward |

The phase receipt records the transition generation and exact update day. Completed legacy Fallout saves do not receive a fabricated reveal day or scheduler request.

## Registry commit transaction

Registry construction begins only when `fallout_successor_allocation_is_current` passes. The builder copies the final deterministic order of `global.fallout_successor_assigned_countries`. It does not construct a second world-country pool.

Three aligned arrays retain country, transition generation, and stable zero-based index. Each country row stores the same generation and index. Validation proves:

- equal array lengths
- source count equal to the committed successor assignment count
- reciprocal membership between the source and registry arrays
- each stored numeric index equal to its real array position
- the country at that position stores that same index and generation
- current runtime schemas and bounded row values

The numeric index proof makes a duplicate country fail because one country cannot hold two different stable indexes. `fallout_event_scheduler_registry_ready` is written only after the complete uncommitted payload passes. It is the registry commit marker. Later annexation does not delete the frozen identity row or force the committed source allocation to be rebuilt.

## Country runtime row

Each committed registry member receives versioned runtime receipts for the scheduler, orientation, arc slots, delayed queue, and bilateral ledger. The initialized row contains:

- active major-arc count of zero with a maximum of three
- twenty cooldown-family fatigue entries, including the unused index zero
- a last-family value used as a hard immediate-repeat veto
- an ordinary cooldown day
- a seven-day reveal quiet-period day
- five independent orientation receipts
- twelve aligned compact major-arc arrays initialized empty
- fifteen aligned compact delayed-result arrays initialized empty
- fourteen aligned compact bilateral arrays initialized empty
- independent arc, delayed-result, and bilateral reconciliation cursors
- a generation-bound global ticket allocator with no ticket reuse
- cancellation history receipts
- one structural dispatch envelope with a ready flag written last
- cleanup tokens, cleanup owners, and derived cleanup-pending flags

The five orientation components are national orientation, capital condition, immediate resource crisis, government archetype, and first character or institution. Ordinary-event eligibility requires all five current-generation receipts.

The ordinary cooldown helper and the three reservation APIs are unreachable from gameplay because every producer requires both activation flags and a living owner, no file sets those flags, and no event calls the APIs. Mutable actor, target, parent, and due-day checks apply only when a row is first created. An exact retry is authenticated from its existing immutable payload even after time advances or its subject is lost. Major arcs use derived occupancy for three compact slots. Arc stages advance one step at a time. Typed cancellation outcomes carry an aligned cancellation reason and exact retries do not duplicate history. Delayed rows retain separate human and AI tokens, a due day, target identity, outcome, cancellation reason, and cleanup token. Bilateral reservation writes one ticket to both countries, proves opposite roles, exact back-references, and the initiator cleanup owner, then rolls both rows back when the second commit cannot be proven. Bilateral status changes snapshot both rows, write both payloads before either status, prove both reciprocal directions, and restore both snapshots before recording an error when commit proof fails. Fatigue slots are structural only. The accepted specs do not define mutation, decay, or score magnitudes, so no fatigue producer is implemented. Survival-ledger effects are not implemented by this tranche.

Terminalization and cleanup remain callable without the activation gate so a disabled scheduler can recover existing rows. Public mutation and release APIs require the current frozen country identity, complete aligned family receipts, a current ticket, and exact cleanup tokens where applicable. Invalid arc actors, invalid delayed targets, lost bilateral reciprocals, and annexed transaction owners receive typed cancellation receipts. A country that no longer exists cannot receive a new reservation or dispatch envelope. Resolved rows accept only success, partial, or failure. Cancellation outcomes require a typed nonzero reason through cleanup. A cleanup-pending row may publish a hidden-cleanup envelope only while its owner still exists, but that envelope is data only. No effect consumes its token or executes content-owned cleanup.

Every public scripted effect that returns a temporary receipt requires the outer caller to create that temporary variable first. This follows the documented temporary-variable lifetime rule. All internal callers pre-seed outputs before they inspect them. No external gameplay caller exists in this tranche.

## Required future survival ledger

The accepted resource identities are Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition. Cohesion and Reclamation are not resource entries.

The reviewed transaction contract requires state rows with immutable producer inputs and country rows with immutable initial values, raw aggregation numerators and denominators, and separate mutable values. Each row must bind to the transition generation. The global commit must cover the exact finalized successor assignment and every included state.

Survival initialization belongs inside the blackout after successor allocation and before player continuation. The live transition does not yet enforce this barrier. The constants file reserves the schema and nine resource identities only. No state or country row trigger, initialization effect, numerical formula, value, or ready flag exists in gameplay code.

## Recurring mutation and read cost

The recurring reconciliation path performs timeline arithmetic and checks the frozen registry arrays. It selects one primary registry country per coordinator date and one primary row from each family through independent round-robin cursors. Full local receipt scans validate row shape once per family. Selected ticket, key, actor, and cross-family uniqueness checks are linear in the selected country local ledgers. Reciprocal proof scans the exact partner ledger once to find the matching row, then runs one selected partner uniqueness scan. A verified reciprocal partner may also be mutated by a bilateral status or cleanup transaction. The recurring read cost is therefore linear in the two local ledger sizes, with one primary row per family and at most its exact reciprocal row eligible for mutation.

Reservation production uses stronger full-ledger uniqueness gates. These scan each local row against its family identities, which is quadratic in that local ledger. Bilateral production performs the gate for both participants. These producers are dormant and are not part of the recurring reconciliation path. Delayed and bilateral queue caps are not implemented, so no constant row-count bound is claimed. The reconciler does not build a global candidate pool. The successor-allocation barrier is evaluated only before the initial registry commit. A successful commit clears the initialization-pending flag and prevents that allocation proof from becoming a recurring annexation barrier.

## Engine references

The installed official documentation is the primary syntax reference:

- `documentation/triggers_documentation.md` documents `all_of`, the matched value and index outputs of `any_of`, temporary-variable operations inside trigger evaluation, and the country-only scope of `exists`.
- `documentation/effects_documentation.md` documents `for_each_scope_loop` and `for_loop_effect`.
- `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` document typed script constants.
- the offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` documents arrays, numeric array indexes, scope arrays, and temporary-variable lifetime.

Repository precedents are `006_independence_wave_effects.txt` and `006_independence_wave_triggers.txt` for aligned scope registries and reciprocal row validation, plus `020_black_plague_effects.txt` for delayed scheduler state. The Fallout substrate retains separate schema and identifier ownership.

## Fail-closed boundaries

The initialization and transaction effects record one owned error for reveal, allocation, registry, row-shape, or reciprocal failure. Invalid dynamic country and state scopes require explicit context-loaded receipts, so a skipped variable scope cannot satisfy the proof. Country-row and orientation mismatches fail their eligibility triggers. A guarded one-time migration promotes schema-1 rows only when the map-return receipt is current, both activation flags are absent, every preserved cooldown, fatigue, date, orientation, registry, and source field passes the current invariant, and every transaction array, cursor, history field, cleanup flag, ticket header, and envelope is absent or empty as required. These checks run before any mutation. Frozen country identities may be annexed without invalidating source membership, while invalid dynamic scopes still fail closed. The scheduler does not repair a missing reveal date, substitute a lost actor or bilateral target, invent a survival value, or select an unreviewed successor.

The following work remains blocked or absent:

- Numeric initialization and aggregation rules for Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition are not accepted. Cohesion and Reclamation remain separate mechanics. The full state and country receipt transaction is not implemented.
- Schema 8 authenticates frozen Air Winter rows with an Air-owned producer schema and generation. Valid rows use exact produced values. Invalid rows use a typed N/A payload. Survival initialization may consume only this frozen provenance contract.
- Structural arc, delayed-result, bilateral, cancellation, and cleanup-envelope transactions are implemented but dormant. Candidate selection, event scheduling, event firing, actual human routing, hidden AI mechanical resolution, content-owned cleanup execution, and scheduler debug presentation are not implemented.
- The five orientation components have receipts but no Fallout orientation event content.
- Literal multiplayer lobby-host identity remains unavailable in the documented script surface. The live authority is the project coordinator.
- No runtime observation was performed. HOI4 was not launched.

These omissions keep both scheduler activation flags unset and keep every reserved living-world event outside the release-floor count.
