# Event 006 DM-58 Cost/Coordinator Reconciliation

Date: 2026-07-27.

Scope: parent-owned follow-up to `006_dm58_reaudit_v18_2026_07_27.md` after the FORM-39 tranche. The change is limited to DM-58 witness ordering and coordinator-origin cleanup; no live HOI4 run is claimed.

## Implemented corrections

- `independence_wave_execute_reclamation_front` now performs a mutation-free witness validation pass and sets the effect-chain-only `independence_wave_reclamation_front_witness_valid` marker only after all aligned member/state/owner rows revalidate.
- `independence_wave_coordinate_reclamation_fronts` pays the centralized strategic and major-security costs only after that validation flag exists. `independence_wave_apply_reclamation_front_witness` is then called as the final claim/wargoal/state mutation. A partial post-payment apply still rolls back transaction receipts and enters the existing crisis failure path.
- The validation marker is temporary to the decision effect chain, so it cannot survive save/load or authorize a later operation; rollback still clears all persistent staging receipts.
- `independence_wave_end_active_origin` detects when the exiting country is the saved DM-58 coordinator and invokes operation cleanup before unregistering the origin. This removes state receipts, member readiness flags, the timed global operation flag, arrays, and the coordinator target without a world-iterating fallback.

## Source evidence

| Contract | Evidence |
| --- | --- |
| Cost before gameplay mutation | `common/scripted_effects/006_independence_wave_decision_effects.txt` now separates `independence_wave_validate_reclamation_front_witness` from `independence_wave_apply_reclamation_front_witness`; `common/decisions/006_independence_wave_decisions.txt` calls the payment helpers before the apply helper, and the validation marker is effect-chain-only. |
| No-witness rollback | The decision's failure branch still calls `independence_wave_rollback_reclamation_front_staging` before crisis deltas, and rollback clears claims/wargoals only when their transaction receipts exist. |
| Coordinator loss | `common/scripted_effects/006_independence_wave_effects.txt` calls `independence_wave_cleanup_reclamation_front_operation` when the exiting origin matches `event_target:independence_wave_reclamation_front_coordinator`; the normal `chaosx.nr6.309` callback remains coordinator-bound. |
| Dynamic tuning | No new magic costs or durations were introduced; existing `independence_wave_decision_cost`, `independence_wave_decision_duration`, and `independence_wave_decision_gate` constants remain the source of truth. |

## Remaining validation status

Source-level ordering and cleanup are addressed. Live success, state-owner invalidation, save/load during the finite operation, dense/no-witness performance, and AI campaign priority still require user-side or future bounded runtime evidence. Whole Event 006 remains **HOLD/PARTIAL** for the independent package, exact-ten/nine-group, focus geometry, sensitive research, asset admission, and broader audit gaps.
