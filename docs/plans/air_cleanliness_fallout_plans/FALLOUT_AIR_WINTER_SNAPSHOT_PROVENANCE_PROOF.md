# Fallout Air Winter Snapshot Provenance Proof

## Status

World transition schema 12 retains the Air Winter provenance contract that closed the stale-zero defect in the frozen payload and the stale-category defect in grading and rewrite. Schema 12 adds specialty survival inputs without changing Air Winter producer ownership. Fallout does not treat a missing Air Winter producer as a real phase or resource value. It also does not use Air Winter's historical restoration category as the live transition category. The request coordinator withholds blackout and world-end ownership until the player and world snapshot ledgers pass their complete synchronous capture proofs.

This is static source proof. Hearts of Iron IV was not launched.

## Ownership boundary

Air Winter owns the live producer contract in:

- `common/script_constants/air_cleanliness_winter_constants.txt`
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt`
- `common/scripted_effects/air_cleanliness_winter_effects.txt`

Fallout owns the frozen transport and transition contract in:

- `common/script_constants/fallout_world_end_constants.txt`
- `common/scripted_triggers/fallout_world_end_triggers.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`

Fallout opens one Air Winter producer generation inside its existing complete snapshot transaction. No new daily, weekly, monthly, country, or state effect iterator was added. The existing Fallout `every_state` pass remains the only state mutation pass. Snapshot validation also evaluates `game:all_states` collection proofs.

## Live producer receipt

`air_winter_begin_fallout_snapshot_production` increments a global producer generation even when a retry occurs on the same date. It also writes Air Winter producer schema 1.

For each valid Air Winter state, `air_winter_prepare_fallout_snapshot_source`:

1. Clears the previous state receipt.
2. Runs the idempotent Air Winter initializer.
3. Normalizes the state ledger.
4. Proves the original category, phase 0 through 6, and all seven percentage values in the range 0 through 100.
5. Writes the state producer schema and generation only after the complete payload passes.

The canonical values are phase, exposure, recovery, adaptation, food reserve, shelter capacity, reclamation, and water security. The original category is a separate mandatory historical classification field.

## Frozen source kinds

Every accepted Fallout state row has one source kind and one matching frozen producer receipt.

| Source kind | Eligibility | Payload rule |
| --- | --- | --- |
| `produced` | `air_winter_state_is_valid = yes` and the current Air Winter receipt passes | Copy every canonical value and the original category exactly from the live row |
| `not_applicable` | `air_winter_state_is_valid = no` at capture | Do not initialize the state. Write the Air-owned explicit zero N/A payload and retain the original category |

A valid state that fails production receives neither kind. Its missing receipt causes the complete world snapshot proof to fail. It cannot enter the N/A branch.

The synchronous capture proof compares every produced frozen value, schema, generation, and historical category to the live Air Winter source. The same state row records `fallout_pretransition_state_category` from the live `has_state_category` result and proves that match during capture. Grading and category rewrite use this second field. After capture, the durable structural trigger reads only the frozen source kind, frozen schema and generation, frozen payload, frozen live category, and frozen global receipt. Later ownership changes cannot rewrite the accepted history.

## Transactional blackout lock

`fallout_lock_transition` prepares schema 12 and phase 1 before entering a short pre-lock capture transaction. The rebuild helper accepts a call only when:

- the pre-lock authorization flag is active on the request coordinator, or
- a current-schema active Fallout transition remains in the snapshot phase on the coordinator

Both paths reject a previously applied snapshot and any destructive-start receipt.

The coordinator sets `fallout_request_locked`, `fallout_transition_active`, `world_end`, and `world_end_fallout` only after:

- the player snapshot complete flag and current player ledger pass
- the world snapshot complete flag and synchronous capture proof pass
- no transition error owns the ledger

Blackout dirty state, dramatic audio, and phase-event scheduling occur only inside that successful commit branch.

Once the lock is active, the existing Air monthly pass skips Air Winter cycle opening, state mutation, response refresh, event dispatch, and finalization. Contamination collection continues. This pause prevents the frozen category and climate inputs from drifting during the multi-event rewrite and adds no iterator.

If a nonmanual source fails before lock, its pending envelope remains available to the existing once-per-date coordinator retry. If the manual source fails, the pending envelope is cleared so the manual scenario's synchronous caller reports rejection and cannot leave a request that locks unexpectedly on a later date.

## Migration

Schema 7 through schema 11 may attempt a rebuild only when the transition is active in the snapshot phase, the snapshot has not been applied, destruction has not started, and no unrelated error owns the ledger. The rebuild discards both old snapshot halves and attempts one schema-12 epoch through the Air Winter producer, live category capture, and survival-input capture. It writes completion flags only when both halves pass. Otherwise, the existing fail-closed snapshot error remains.

Active schema-10 phases after snapshot use the narrower supply-network migration contract. Phase 2 may promote before grading mutation. Phase 3 through 6 may promote only before successor allocation, after current grading, and after every destructive-grade state's live node and railway aggregates still match the frozen snapshot. Phase 3 continues to population loss and phase 4 executes physical collapse. Phase 5 or 6 rewinds to physical collapse. Schema-10 phase 7 or 8 states and initialized allocation remain blocked.

Completed legacy Fallout saves are promoted without replaying destruction. They receive `fallout_transition_legacy_completed_without_current_schema_receipts` and `fallout_transition_legacy_completed_without_supply_network_receipts`. No state receipt is fabricated.

All other later active legacy phases fail closed. The former schema-3 map-return-error promotion is removed because its consumed rows cannot gain trustworthy Air Winter provenance after the fact.

## Engine reference basis

The implementation follows the installed official documentation for scripted effects, scripted triggers, scope variables, flags, arrays, collections, and script constants. The offline wiki references for data structures, scopes, effects, triggers, on actions, and event modding remain the parallel syntax source.

The proof relies on documented script evaluation and persistent variables. It does not claim runtime evidence for save serialization, multiplayer timing, or engine performance.

## Remaining boundary

This contract authenticates the frozen Air Winter inputs used by grading and survival initialization. The accepted numerical formulas for the nine Fallout survival resources are implemented and documented in `FALLOUT_SURVIVAL_NUMERICAL_CONTRACT_PROPOSAL.md` and `FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md`. This provenance proof does not redefine those formulas. It also does not resolve the manual native sweep, literal lobby-host identity, blackout keyboard capture, or successor allocation blockers.
