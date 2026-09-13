# Event 006 DM-58 lifecycle supersession audit — 2026-09-03

## Disposition

The older DM-58 lifecycle finding is superseded by the current source and requires no gameplay patch in this tranche.

## Current source evidence

`common/decisions/006_independence_wave_decisions.txt:3717-3757` rebuilds one exact reclamation-front witness, pays the coordinated-operation cost only after the witness is valid, applies the witness, and schedules `chaosx.nr6.309` only after the success flag is set.

`common/decisions/006_independence_wave_decisions.txt:3758-3787` marks successful completion, clears per-member staging receipts, and rolls back staging, records failure, and enters the league crisis on an unsuccessful witness.

`common/decisions/006_independence_wave_decisions.txt:3788-3800` marks timeout failure and routes it through the same league-delta and crisis path, while the cancel trigger closes the mission when the shared operation, origin, membership, route, or chaos precondition is no longer valid.

`common/scripted_effects/006_independence_wave_effects.txt:2527-2545` clears the timed global operation flag, coordinator event target, frozen state flags, member readiness receipts, witness arrays, and operation count.

`common/scripted_effects/006_independence_wave_effects.txt:2547-2569` revalidates an active operation when the member minimum is lost or a recorded witness member unregisters, then invokes the shared cleanup.

`events/006_independence_wave.txt:157-176` defines the hidden `chaosx.nr6.309` callback with a coordinator-target identity check and count guard before invoking the same cleanup effect.

`common/scripted_effects/006_independence_wave_effects.txt:2974-2984` also cleans the operation when the active origin ends and still owns the coordinator target.

## Review result

The current order is witness validation, resource payment, material mutation, success receipt, timed operation registration, and delayed cleanup.

The current source therefore covers the previously reported cost-before-mutation, participant invalidation, origin cleanup, and expiry cleanup requirements without adding an unapproved fallback or changing the decision surface.

No gameplay files were edited for this audit, and no visual, localisation, AI, or spreadsheet surface changed.

## Remaining evidence boundary

The repository checks and source inspection do not prove live engine execution, save-load persistence, or in-game mission rendering; those remain user-owned runtime checks.

This handoff supersedes the stale partial recommendation in `006_dm58_reaudit_v18_2026_07_27.md` for the current source snapshot while preserving its runtime-evidence caveat.
