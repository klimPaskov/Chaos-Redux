# Migration cohort visit history

Source: [migration_cohort_history_effects.txt](migration_cohort_history_effects.txt).
Triggers: `migration_cohort_history_arrays_are_aligned` and `migration_cohort_history_live_ledger_arrays_are_aligned` in `common/scripted_triggers/migration_cohort_history_triggers.txt`.

The history is an append-only sparse ledger of the exact states each live cohort has visited.
`global.migration_cohort_history_ids` and `global.migration_cohort_history_states` are aligned by index, increasing index is visit order, and `global.migration_cohort_history_count` mirrors the ID array size.
Destination selection and the transfer preflight read it to keep ordinary hosted distribution and transit from sending a cohort back to a state it already left.

## Alignment contract

`migration_cohort_arrays_are_aligned`, which every cohort writer and reader checks, aliases `migration_cohort_history_live_ledger_arrays_are_aligned`.
That trigger requires the eight live cohort arrays and `global.migration_cohort_count` to agree and then also requires `migration_cohort_history_arrays_are_aligned`, which needs `global.migration_cohort_history_count` to exist.
The history count must therefore exist before the first cohort is written, or no cohort can ever be recorded.

## `migration_initialize_cohort_history`

Purpose: create the history count once, without clearing anything.

Scope: any.

Behaviour: when `migration_cohort_history_initialized` is absent, it derives a missing `global.migration_cohort_history_count` from the ID array size (zero in a new campaign) and sets the flag.
An existing count is never repaired; a mismatch makes the alignment triggers fail closed.

Callers, all idempotent:

1. `humanitarian_initialize_runtime`, outside its one-shot guard, so it also runs where `humanitarian_runtime_initialized` is already set.
2. `migration_initialize_runtime`, outside its one-shot guard.
3. `migration_record_displaced_cohort`, immediately before its alignment check.
4. `migration_record_cohort_history_visit` and `migration_cleanup_cohort_visit_history`.

With zero cohorts and zero history rows every alignment check is true, so the first record writes cohort ID 1 and appends its origin receipt.

## `migration_record_cohort_history_visit`

Purpose: append one proven visit for one live cohort.

Scope: the exact STATE being recorded.

Input: temporary `migration_cohort_history_id_request`, a positive cohort ID, consumed on exit.

Outputs: `migration_cohort_history_record_result`, `migration_cohort_history_append_result`, `migration_cohort_history_cycle_result` and `migration_cohort_history_alignment_result`.

The first receipt is appended even when the live host is already this state, which seeds the true origin.
A repeat call for the newest state is a no-op; a return to an older state appends again, sets the cycle output and records the transfer-cycle achievement disqualifier in the persisted owner.

## `migration_cleanup_cohort_visit_history`

Purpose: remove every history row of one cohort after it reaches a terminal state.

Scope: any.

Input: temporary `migration_cohort_history_id_request`.

It validates only the history arrays, so stale rows can be removed after the live row is gone, and it removes rows in descending index order so the remaining visit order is preserved.

No helper in this file changes population, the Deaths ledger, or any live cohort field, and none scans the map.
