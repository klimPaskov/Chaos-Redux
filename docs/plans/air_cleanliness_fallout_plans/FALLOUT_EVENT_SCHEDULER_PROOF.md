# Fallout Living-World Scheduler Proof

## Status

The living-world scheduler has a schema-2 dormant transaction-integrity substrate with a backward-compatible fixed ordinary-opening receipt. It records the reveal timeline, freezes a stable post-allocation country registry, initializes country runtime rows, and exposes five-part orientation, anti-repetition, ordinary-opening, arc, delayed-result, bilateral, cancellation, cleanup, routing, and exact dispatch-issuance contracts. It does not select a candidate or schedule an event. Visible and hidden AI issuance remain unreachable because both activation flags have no setter. No live gameplay path can reach hidden cleanup, and no living-world cleanup event is defined.

The activation flags `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` have no setter. Suffixes `100` through `126` are typed reservations only. Defined event blocks in that range: `0`. Countable blocks toward the 660-block release floor: `0`.

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

Each committed registry member receives versioned runtime receipts for the scheduler, orientation, ordinary opening, arc slots, delayed queue, and bilateral ledger. The initialized row contains:

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
- one fixed ordinary-opening receipt with a generation, ticket, stable key, separate human and AI tokens, opening branch, due day, family identities, and optional typed target
- one structural dispatch envelope with a ready flag written last
- one exact dispatch-issuance receipt with its issued flag written last
- cleanup tokens, cleanup owners, and derived cleanup-pending flags

The five orientation components are national orientation, capital condition, immediate resource crisis, government archetype, and first character or institution. Ordinary-event eligibility requires all five current-generation receipts.

The ordinary cooldown helper and the four reservation APIs are unreachable from gameplay because every producer requires both activation flags, a generation-current ordinary-receipt registry proof, and a living owner. No file sets those flags and no event calls the APIs. The fixed ordinary receipt admits one outstanding crisis opening per country without consuming a major-arc slot. It writes its pending flag last, accepts exact payload retries without allocating another ticket, and rejects a request key already owned by the delayed or bilateral ledger. Once its dispatch is issued, the fixed receipt becomes a blocking tombstone. Generic reconciliation cannot clear it after owner or target loss. Only the exact issued event may consume it or cancel it through the issued wrapper. Mutable actor, target, parent, and due-day checks apply only when a transaction is first created. An exact retry is authenticated from its existing immutable payload even after time advances or its subject is lost. Major arcs use derived occupancy for three compact slots. Arc stages advance one step at a time. Typed cancellation outcomes carry an aligned cancellation reason and exact retries do not duplicate history. The shared cancellation receipt also records the transaction source, so an ordinary retry cannot authenticate a delayed or bilateral cancellation with the same ticket and reason. Delayed rows retain separate human and AI tokens, a due day, target identity, outcome, cancellation reason, and cleanup token. An issued delayed row is also a blocking tombstone. Public ticket-only terminalizers reject it, and reconciliation preserves it after owner or target loss until the exact token-authenticated wrapper resolves, cancels, or releases it. Bilateral reservation writes one ticket to both countries, proves opposite roles, exact back-references, and the initiator cleanup owner, then rolls both rows back when the second commit cannot be proven. Bilateral status changes snapshot both rows, write both payloads before either status, prove both reciprocal directions, and restore both snapshots before recording an error when commit proof fails. Fatigue slots are structural only. The accepted specs do not define mutation, decay, or score magnitudes, so no fatigue producer is implemented. The survival identity stage is transition owned and the scheduler can only consume a committed ledger.

Terminalization and cleanup remain callable without the activation gate so a disabled scheduler can recover existing rows. Public mutation and release APIs require the current frozen country identity, complete aligned family receipts, a current ticket, and exact cleanup tokens where applicable. Invalid arc actors, unissued invalid delayed targets, lost bilateral reciprocals, and annexed transaction owners receive typed cancellation receipts. Issued ordinary and delayed rows retain their envelope until their exact event wrapper consumes it. A country that no longer exists cannot receive a new reservation or dispatch envelope. Resolved rows accept only success, partial, or failure. Cancellation outcomes require a typed nonzero reason through cleanup.

The selected country consumer accepts only a current registry row whose envelope still matches its exact ordinary, delayed, or bilateral transaction. Visible and hidden AI envelopes require both activation flags. Exact hidden-cleanup envelopes remain issuable after deactivation so committed rows can finish cleanup. The consumer copies source, ticket, generation, mode, event token, branch, target type, and target into an issuance receipt, records the engine date and day, and writes `fallout_event_dispatch_issued` last. Only then does a `meta_effect` construct and run `country_event = { id = chaosx.fallout.[FALLOUT_EVENT_ID] }`. Later coordinator passes accept the persisted receipt as current and do not emit that envelope again. Future ordinary content must commit any required child transaction before it calls the exact consume wrapper, or revalidate a stale subject and call the issued cancellation wrapper. Both wrappers authenticate the mirrored token and clear the envelope before releasing the fixed receipt. Issued delayed result, cancellation, and cleanup wrappers expose the same token-authenticated terminalization contract. They consume the envelope inside terminalization or removal and do not permit a second acknowledgement. The bilateral contract retains the explicit acknowledgement API until its reciprocal terminalizers receive the same atomic wrapper contract. No event block calls any of these content-facing wrappers in this tranche.

This is a compatible extension of schema 2. An old schema-2 country row can promote only an exactly absent ordinary receipt while both activation flags remain unset. The one-time promotion iterates the numeric frozen-registry index array. Each index must match its stored index and generation, load the exact country context, and prove the promoted or newly initialized receipt. The proven count must equal the frozen registry count before the generation-bound global commit receipt is written. It does not rewrite compact arc, delayed, or bilateral rows or touch an existing envelope. An empty envelope and an unissued ready envelope require every issuance field to be absent. Existing schema-2 rows therefore retain their original empty or unissued meaning. The new transaction-source history field is required only when cancellation count is nonzero. Legitimate dormant schema-2 rows have zero cancellations because production was unreachable. Any unproven nonzero source-free history fails closed. No pre-existing consumer could have emitted an ordinary event because source token `ordinary_event` did not exist. A receipt mismatch clears no unrelated envelope and records the owned `ordinary_receipt_mismatch` or `dispatch_issue_receipt_mismatch` scheduler error. The static proof establishes command issuance and at-most-once coordinator behavior. It does not claim that an event popup was displayed.

Every public scripted effect that returns a temporary receipt requires the outer caller to create that temporary variable first. This follows the documented temporary-variable lifetime rule. All internal callers pre-seed outputs before they inspect them. No external gameplay caller exists in this tranche.

## Dispatch issuance state proof

| State | Envelope commit | Issuance commit | Valid next action |
| --- | --- | --- | --- |
| Empty | ready flag absent and all payload fields absent | issued flag and all receipt fields absent | a reconciled transaction may publish one envelope |
| Ready, unissued | ready flag present with an exact current transaction payload | issued flag and all receipt fields absent | the selected-country consumer may issue once |
| Ready, issued | ready flag present with the same payload | issued flag present with the complete mirrored identity and non-future date and day | ordinary content may commit a child and consume or cancel a stale subject through the issued wrapper, delayed content may use an atomic issued terminalizer, or bilateral content may resolve and acknowledge |
| Consumed | envelope and issuance data cleared together | absent | the ordinary receipt is empty or the compact row has advanced to its terminal state |
| Partial or mismatched | any mixed shape | any mixed shape | fail the country row and preserve the transaction for diagnosis |

The ready flag and issued flag are separate commit markers. This distinction is what makes a save between command issuance and event resolution recover without a second command. Issued ordinary and delayed receipts remain pending even when their subject becomes invalid, so generic reconciliation cannot erase an unresolved engine event. The coordinator advances its registry cursor after the issue attempt only when no owned scheduler error exists.

## Survival ledger boundary

The accepted resource identities are Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition. Cohesion and Reclamation are not resource entries.

The reviewed transaction contract requires state rows with immutable producer inputs and country rows with immutable initial values, raw aggregation numerators and denominators, and separate mutable values. Each row must bind to the transition generation. The global commit must cover the exact finalized successor assignment and every included state.

Survival initialization belongs inside the blackout after successor allocation and before player continuation. The live transition stages exact country and state identity rows, then enforces the committed-ledger barrier before player continuation and map return. Resource identity arrays fix the accepted order, while aligned global arrays prove physical indexes and all-and-only scope coverage. The numerical arrays have a structural row contract, but no effect fills or commits them. No numerical formula, value, aggregation, validation, or ready setter exists.

Registry schema 2 binds the scheduler registry to the survival schema, generation, and country count. A missing ledger records `survival_ledger_not_current`. The scheduler does not create, repair, or default survival values. Full details are in `FALLOUT_SURVIVAL_LEDGER_IDENTITY_TRANSACTION_PROOF.md`.

## Recurring mutation and read cost

The recurring reconciliation path performs timeline arithmetic and checks the frozen registry arrays. It selects one primary registry country per coordinator date, reconciles its fixed ordinary receipt at constant cost, and selects one primary compact row from each family through independent round-robin cursors. Full local receipt scans validate row shape once per family. Selected ticket, key, actor, and cross-family uniqueness checks are linear in the selected country local ledgers. Reciprocal proof scans the exact partner ledger once to find the matching row, then runs one selected partner uniqueness scan. A verified reciprocal partner may also be mutated by a bilateral status or cleanup transaction. The recurring read cost is therefore linear in the two local ledger sizes, with one fixed ordinary receipt, one primary compact row per family, and at most its exact reciprocal row eligible for mutation.

Compact-ledger reservation production uses stronger full-ledger uniqueness gates. These scan each local row against its family identities, which is quadratic in that local ledger. Bilateral production performs the gate for both participants. The fixed ordinary reservation uses current-row validation and linear local key and ticket membership checks instead. These producers are dormant and are not part of the recurring reconciliation path. Delayed and bilateral queue caps are not implemented, so no constant row-count bound is claimed. The reconciler does not build a global candidate pool. The successor-allocation barrier is evaluated only before the initial registry commit. A successful commit clears the initialization-pending flag and prevents that allocation proof from becoming a recurring annexation barrier.

## Engine references

The installed official documentation is the primary syntax reference:

- `documentation/triggers_documentation.md` documents `all_of`, the matched value and index outputs of `any_of`, temporary-variable operations inside trigger evaluation, and the country-only scope of `exists`.
- `documentation/effects_documentation.md` documents `for_each_scope_loop`, `for_loop_effect`, `country_event`, and `meta_effect`.
- `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` document typed script constants.
- the offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` documents arrays, numeric array indexes, scope arrays, and temporary-variable lifetime.

Repository precedents are `006_independence_wave_effects.txt` and `006_independence_wave_triggers.txt` for aligned scope registries and reciprocal row validation, plus `020_black_plague_effects.txt` for delayed scheduler state. Dynamic event dispatch precedents are `013_natural_disasters_effects.txt`, `air_cleanliness_winter_event_effects.txt`, and `fallout_manual_scenario_effects.txt`. Each formats an integer variable into a namespaced `country_event` id through `meta_effect`. The Fallout substrate retains separate schema and identifier ownership.

## Fail-closed boundaries

The initialization and transaction effects record one owned error for reveal, allocation, registry, row-shape, ordinary-receipt, or reciprocal failure. Invalid dynamic country and state scopes require explicit context-loaded receipts, so a skipped variable scope cannot satisfy the proof. Country-row and orientation mismatches fail their eligibility triggers. A guarded one-time migration promotes paired runtime-schema-1 and registry-schema-1 rows only when the map-return receipt and a fully current committed survival ledger are current, both activation flags are absent, every preserved cooldown, fatigue, date, orientation, registry, and source field passes the current invariant, and every transaction array, cursor, history field, cleanup flag, ticket header, and envelope is absent or empty as required. The schema-1 migration initializes the empty ordinary receipt before committing the current registry. Existing schema-2 rows use the narrower absent-receipt promotion, which leaves all prior transaction payloads untouched. That promotion accepts either registry schema 1 or 2 only while dormant, so a current runtime row can acquire its fixed receipt before schema-1 registry-binding eligibility is evaluated. The binding transaction then writes registry schema 2, invokes the idempotent promotion again, and requires the full current payload before it clears initialization. The binding still requires the registry ready flag, absent activation flags, no scheduler error, current map-return receipts, a full survival ledger, and agreement across every indexed registry, allocation, and survival row. These checks run before any gameplay producer can pass. Frozen country identities may be annexed without invalidating source membership, while invalid dynamic scopes still fail closed. The scheduler does not repair a missing reveal date, substitute a lost actor or bilateral target, invent a survival value, or select an unreviewed successor.

The following work remains blocked or absent:

- Numeric initialization and aggregation rules for Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition are not accepted. Cohesion and Reclamation remain separate mechanics. Identity and row-shape staging exist, while numerical producers, arithmetic proof, row commits, and the global commit remain absent.
- World transition schema 11 authenticates frozen Air Winter rows with an Air-owned producer schema and generation. Valid rows use exact produced values. Invalid rows use a typed N/A payload. A separate frozen live category is proven at capture. Survival initialization may consume only this frozen provenance contract.
- Structural ordinary-opening, arc, delayed-result, bilateral, cancellation, cleanup-envelope, and exact dispatch-issuance transactions are implemented but dormant. Candidate selection, calls to the ordinary scheduler API, event definitions, actual human choice content, hidden AI mechanical resolution, content-owned cleanup execution, and scheduler debug presentation are not implemented.
- Bilateral issued-response and cleanup terminalizers still use the bilateral-only explicit acknowledgement contract. Exact token-authenticated reciprocal terminalizers and issued orphan retention are not implemented, so activation must remain blocked.
- The five orientation components have receipts but no Fallout orientation event content.
- Literal multiplayer lobby-host identity remains unavailable in the documented script surface. The live authority is the project coordinator.
- No runtime observation was performed. HOI4 was not launched.

These omissions keep both scheduler activation flags unset and keep every reserved living-world event outside the release-floor count.
