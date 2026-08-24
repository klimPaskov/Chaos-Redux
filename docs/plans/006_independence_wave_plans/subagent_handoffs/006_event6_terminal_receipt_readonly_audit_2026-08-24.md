# Event 006 standalone terminal receipt read-only audit

Date: 2026-08-24.

Status: read-only audit. No gameplay file, event file, scripted effect, decision, mission, cost, queue, pre-event helper, or presentation surface was edited.

## Scope and current implementation

The current receipt implementation is present in `common/scripted_effects/006_independence_wave_execution_effects.txt` at the current HEAD.

`independence_wave_clear_standalone_terminal_receipt` owns the global receipt reset at lines 18-50.

`independence_wave_snapshot_standalone_terminal_receipt` owns the global receipt write at lines 56-199.

The standalone wrapper `independence_wave_prepare_and_execute_standalone_incident` clears the receipt at line 905 and snapshots after terminal classification at line 982.

The root `chaosx.nr6.1` event calls that wrapper at `events/006_independence_wave.txt:49` and opens `chaosx.nr6.2` only when the committed outcome flag is present at lines 51-59.

The shared coordinator remains the owner of plan cleanup, ownership mutation, and compensating rollback.

## Required field and flag coverage

The receipt has all requested field families in source.

- Plan identity and dates: `plan_id`, `started_date`, `committed_date`, and `snapshot_date`.
- Terminal state: `phase`, `last_failure`, `finalization_failure`, and `rollback_failure`.
- Planning counts: `target_count` and `selected_count`.
- Execution counts: `instantiated_count`, `transferred_state_count`, `prepared_count`, `activated_count`, `validated_count`, and `initialized_count`.
- Existing terminal outcomes: `committed`, `cancelled_before_mutation`, `failed_after_mutation`, `failed_during_finalization`, and `rolled_back_after_mutation`.
- Additional diagnostics: `rollback_completed`, `rollback_failed`, `finalization_failed`, `capital_restore_failed`, and `optional_expansion_failed`.

The helper uses existing constants for zero values and phase or failure enums. No tuning value or weighted surface was changed.

## Concrete defects proven by source flow

### 1. Selected count is lost before cancellation and successful rollback receipts

`independence_wave_clear_plan_contribution` resets `global.independence_wave_plan_selected_count`, `global.independence_wave_plan_attempt_count`, and `global.independence_wave_plan_sponsorship_count` to zero at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:1003-1005`.

The standalone pre-mutation cancellation branch calls that cleanup at `common/scripted_effects/006_independence_wave_execution_effects.txt:972` and snapshots only afterward at line 982.

The successful compensating rollback path calls the same cleanup from `liberation_release_finish_verified_plan_rollback` at `common/scripted_effects/chaosx_liberation_release_effects.txt:1823`, then clears the plan arrays at lines 1829-1831 before the standalone wrapper reaches its final snapshot.

Therefore a non-empty selected plan that cancels before ownership mutation or rolls back successfully is recorded with `terminal_receipt_selected_count = 0`, even though the selected count was positive before cleanup.

This directly weakens the accepted diagnostic classification in `docs/plans/006_independence_wave_plans/006_event6_improvement_addendum_2026_08_24.md:156-178`, which requires distinguishing a zero-pool result from a selected plan that failed during instantiation, transfer, or finalization.

The same ordering drops the attempt and sponsorship counts, and it clears the optional-expansion flag before the receipt writer can copy it.

### 2. A stale execution failure can override the current transaction failure

The receipt writer prefers `global.independence_wave_execution_last_failure` at lines 94-97 and falls back to `global.liberation_plan_last_failure` only when that variable is absent at lines 98-100.

The standalone root clears the durable receipt at line 905 but does not clear `global.independence_wave_execution_last_failure` before `liberation_release_begin_plan` and allocation begin.

The allocator records a current empty or short pool failure in `global.liberation_plan_last_failure`, including `insufficient_pool` at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:153-155`.

Because the execution failure variable is written during a prior execution attempt and is not cleared by the standalone root, a later transaction that fails before execution can report the prior transaction's execution failure instead of the current allocator failure.

The scenario reset explicitly clears this variable at `common/scripted_effects/006_independence_wave_scenario_effects.txt:1310-1314`, which confirms that the standalone root's omission is a lifecycle asymmetry.

## Timing and cleanup assessment

The receipt remains separate from `chaosx.nr6.2`, the Event Log, decisions, missions, costs, queues, and pre-event compatibility helpers.

The previous durable receipt is cleared at the start of the standalone wrapper, and there are no other call sites for the clear helper besides the snapshot helper's defensive internal reset.

Commit and finalization-failure branches retain enough plan-level data for the current final snapshot, although shared scope marks may already be cleared by commit.

Pre-mutation cancellation and successful rollback do not retain the selected count because contribution cleanup runs before the final snapshot.

No event target is used by the receipt. Existing `independence_wave_latest_actor` persistence and cleanup remain outside this diagnostic surface.

## Recommended bounded repair for the parent

Preserve the selected, attempt, sponsorship, and optional-expansion values before any contribution cleanup or rollback completion, then make the final receipt writer consume those saved values.

Clear `global.independence_wave_execution_last_failure` at the start of a new standalone root transaction, or make the receipt writer prefer the current plan failure unless the current transaction reached execution.

Keep the committed-only `chaosx.nr6.2` gate and all admission, host-survival, allocation, AI, and rollback behavior unchanged.

No event-target migration, GUI, localisation, decision, mission, cost, queue, or pre-event change is justified by this audit.

## Validation and evidence

`python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 40 runtime adapters, 32 attested packages, 29 compatible reservation groups, and a 20-package static standalone witness.

The current read-only `hoi4.event_inspect` file-lint route returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `c3a12107d6e70fad6867a9791e60ada2b0a4647d39568885779376ae890c6ab2`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d44319e356c0c5ca8df0b2667972b6a87f1f789dcf02a04566a45a1a63827c7/dd6a59aaf9fbb5d445c680c0723ec4d1be5592cdeacf17626ae5d9af2ec1ead3/event-lint-c3a12107d6e7.json`.

The MCP report deferred helper and lifecycle projections and reported `helpers = 0`, so it is not engine evidence for the scripted-effect ordering above.

No weighted or probability-bearing surface was changed, so `hoi4.probability_inspect` and `chaosx_ai_probability_auditor` were not applicable to this read-only receipt audit.

No live Hearts of Iron IV session was launched.

## Changed files and remaining risks

Changed file: this handoff only.

The gameplay receipt is currently present but should be treated as diagnostically incomplete for non-empty cancellation or successful rollback, and potentially stale for failures after a prior execution attempt, until the parent applies the bounded lifecycle repair and reruns the targeted static audit.

