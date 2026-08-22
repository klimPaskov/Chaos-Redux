# Event 006 retryable rollback recovery tranche

## Scope

The standalone Event 006 wrapper now retries a retained `rollback_failed` ledger before attempting a new release plan. This is limited to an Independence Wave-only plan with execution started, no Event 005 participation, and no finalizer or finalization-failed marker.

## Changed file

- `common/scripted_effects/006_independence_wave_execution_effects.txt`

## Runtime contract

- `independence_wave_reset_stale_standalone_plan` calls the shared idempotent compensation path for the narrow retryable phase.
- A verified rollback is reset to `idle`, allowing the normal Event 006 allocator to begin a fresh plan in the same hidden root-event transaction.
- A failed retry remains `rollback_failed` with its frozen ledger intact; no release, country creation, presentation, category, pressure, queue, or player-facing cue is produced.
- Finalizer-started and finalization-failed plans remain untouched because their package mutations may be irreversible.

## Validation boundary

Static Event 006 allocator, country API, flag, and scenario-matrix audits remain the required checks. Runtime receipt fields (`independence_wave_terminal_receipt_phase`, `...last_failure`, `...target_count`, `...selected_count`, `...validated_count`, and `...initialized_count`) are still needed from a live save to identify any package-specific admission failure after the retry path.

## Remaining risk

This tranche addresses stale retryable compensation state, not an empty candidate pool, package attestation gaps, generic focus/AI contract failures, or finalizer failures. Those branches must remain fail-closed until their runtime receipt identifies a concrete package or contract defect.
