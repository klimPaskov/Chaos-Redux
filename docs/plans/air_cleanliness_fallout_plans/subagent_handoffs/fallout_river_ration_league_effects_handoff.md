# River Ration League effects handoff

## Scope

The parent agent completed and reviewed the dormant River Ration League scripted effects after the bounded effects audit returned without a final handoff.

## Gameplay files

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`

## Implemented helpers

- Branch cost payment and refund
- Government-aware deterministic grading
- Generation-bound two-state registry snapshots with owner and controller receipts
- 42-day delayed result scheduling
- Four branch result ledgers with exact accepted deltas
- 180-day callback scheduling and durable River memory
- Hidden-AI branch scoring with deterministic tie order
- Event Log payload recording for choice, result, callback, and cancellation
- Authenticated delayed-result and cleanup receipt release

## Deliberate boundary

The chain does not apply population loss and does not set either Fallout scheduler activation flag. The native all-valid-province thermonuclear sweep, live scheduler presentation, save recovery, multiplayer delivery, and runtime Event Log proof remain release blockers outside this tranche.

## Static checks

The effects and triggers have balanced braces, no unsupported comparison operators, no semicolons or em dashes in new prose, no population-loss calls, and no daily, weekly, or monthly world iterator.
