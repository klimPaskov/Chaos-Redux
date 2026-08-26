# IW-038 Ruthenia setup-receipt guard re-audit

Date: 2026-08-26

## Scope

Re-audit of `independence_wave_rut_hold_mountain_compact_together` and `independence_wave_setup_iw_038_ruthenia` for the current-generation setup receipt lifecycle.

## Patch status

No gameplay source change was needed in this pass because the requested cancellation guard is already present in `common/decisions/006_independence_wave_siberian_decisions.txt` at line 3396.

The existing guard was added by commit `c903cdcd8` (`Repair IW-038 founding mission setup guard`) and is retained in the current checkout.

## Identifier and behavior

- Mission: `independence_wave_rut_hold_mountain_compact_together`.
- Receipt: `independence_wave_iw_038_setup_complete`.
- Before the existing repair, the cancellation `OR` omitted the setup receipt.
- Current behavior requires the receipt for mission activation, clears it at setup entry, restores it only inside the successful `has_prepared_independence_wave_iw_038_package_setup = yes` branch, and cancels the mission when the receipt is absent.
- No costs, AI weights, package admission, route logic, localisation, or other missions were changed.

## Evidence and validation

- Focused source assertion passed for activation, setup clear/prepare/restore ordering, and exactly one receipt guard inside the cancellation block.
- `python -B .tools/audit_event6_allocator.py` passed.
- The existing related handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw038_rut_setup_receipt_cancel_guard_2026-08-26.md`.

## Remaining risks

This is source-level evidence only. No live save or in-game runtime claim is made.

