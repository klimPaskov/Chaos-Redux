# KRG clone maturation transaction

Status: transaction, live KRG decision, cost presentation, compatibility callback and world-end cleanup are wired; post-change review and probability comparison remain pending.
Acceptance: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, “Clone maturation production correction”, parent acceptance 2026-09-08.
This is not the private Mengele supplemental-production adapter.

## Scope, costs and physical output

All helpers run in the invoking COUNTRY scope; no persistent event target or caller selector is required.
`clone_maturation` is the single profile: 65 Political Power, 150 support equipment, 1,000 fuel, four native civilian factories, 90 days, 30-day re-enable delay, and 100 `clone_equipment_1`.
No manpower or trucks are paid, and no divisions or direct manpower are awarded.
The existing `clone_refresh_reserve_manpower` reads the physical `clone_equipment` archetype stockpile, so 100 retained equipment contribute 1,000 weekly reserve manpower at the current shared rate of ten.
Normal production/training and provider refinements are unchanged.

## Public helper map

| ID | Input / result | Behavior |
| --- | --- | --- |
| `brilliant_scientist_krg_begin_clone_maturation` | No selector; temp `brilliant_scientist_krg_clone_maturation_started` = 0/1 | Revalidates operation and three direct costs after native admission; creates and pays one snapshot receipt; duplicate begin cannot charge. |
| `brilliant_scientist_krg_cancel_clone_maturation` | No selector; temp `brilliant_scientist_krg_clone_maturation_cancelled` = 0/1 | Snapshots, clears, then refunds a complete receipt once even when the provider/site is invalid; malformed fragments are retired without an inferred refund. |
| `brilliant_scientist_krg_finish_clone_maturation` | No selector; temp `brilliant_scientist_krg_clone_maturation_finished` = 0/1 | Requires complete receipt and live operation; consumes receipt before adding its snapshotted clone quantity, refreshes reserve stockpile and records history; invalid finish calls cancellation. |
| `brilliant_scientist_krg_cleanup_clone_maturation` | No selector; cancellation result as above | Cancels/refunds first, then removes the native decision; any subsequent removal callback has no reward authority. |

Public trigger IDs:

- `brilliant_scientist_krg_clone_maturation_is_operational`: KRG decisions active, not capitulated, canonical cloning operation unsuspended/undamaged/undismantled, `clone_infantry_access_tech`, and an owned-and-controlled marked state.
- `brilliant_scientist_krg_clone_maturation_receipt_is_current`: paid flag plus all four snapshot variables, nonnegative direct values and positive output.
- `brilliant_scientist_krg_clone_maturation_can_pay_direct`: inclusive PP/support/fuel checks only.
- `brilliant_scientist_krg_clone_maturation_can_pay`: inclusive direct costs plus four available civilian factories.
- `brilliant_scientist_krg_clone_maturation_requirements_met`: current operation and no active paid receipt; no lifetime cap.
- `brilliant_scientist_krg_clone_maturation_can_start`: requirements plus all four costs.

`brilliant_scientist_krg_clear_clone_maturation_receipt` and `brilliant_scientist_krg_record_clone_maturation_history` are internal.
The history helper requires and consumes temp `brilliant_scientist_krg_clone_maturation_history_authorized = 1`; only successful finish sets it.
It preserves the old cycle increment, burden flag and identity-crisis condition/effects exactly, excluding the obsolete rifle/support stockpile reward.
The old lifetime maximum of eight and identity-pressure threshold of four remain unchanged in their existing constant file; neither is a new production ceiling.

## Persistent state and cleanup

Authority flag: `brilliant_scientist_krg_clone_maturation_paid`.
Snapshot variables: `brilliant_scientist_krg_clone_maturation_paid_pp`, `_paid_support`, `_paid_fuel`, `_paid_output`.
The receipt freezes amounts against profile changes during a paid timer.
All four variables and the authority flag clear before refund or physical output.
Temporary names under `brilliant_scientist_krg_clone_maturation_` hold result, payment, refund, output and internal history authority; the shared debit helpers also use `equipment_stockpile_removal_amount` and `fuel_stockpile_removal_amount`.
These are documented temporary scratch values, not persistent authority.
No shared project selector, history array, facility or neutral knowledge flag is changed.
Only the existing KRG cycle/burden/crisis history is advanced after successful production.

Two existing STATE markers qualify: `brilliant_scientist_krg_clone_growth_site` from the paid KRG designation decision and `brilliant_scientist_cloning_growth_site` from Kruger Deployment/inherited facilities.
The parent explicitly accepted both on 2026-09-08, avoiding redundant rebuilding of a genuine inherited site.
Country flags alone never qualify.
Within `any_owned_state`, `is_controlled_by = PREV` tests the invoking country even when an outer event's ROOT is another country.
The core requires at least one currently valid marked site, not the continued survival of one originally selected site; it stores no site target.

## Parent wiring contract

The existing `brilliant_scientist_krg_run_bounded_clone_growth_cycle` retains its category/icon and normal native timer/cooldown.
Admission uses `brilliant_scientist_krg_clone_maturation_can_start` and the same inclusive per-cost presentation.
Use native `cost = 0` with explicit custom PP display/planning because this core itself pays all 65 PP; leaving native cost 65 would double-charge.
Native reservation may precede or follow the callback; begin intentionally rechecks only direct costs and never requires four factories again.
Set native CIC to four, timer to 90 and re-enable to 30 from the profile or a documented file-local mirror if the engine field rejects script constants.
The callback calls begin; cancellation calls cancel; normal removal calls finish.
If native admission succeeds but begin rejects revalidation, the timer must cancel for absence of the paid receipt and cannot yield output.
The active timer must also cancel if operation/site eligibility fails.
Parent cleanup paths must call cancel before removing the active decision to return outstanding direct payments and release native CIC.
The dedicated cleanup helper performs that sequence and is called by `brilliant_scientist_cleanup_transient_targets_after_world_end`.
Other loss of live KRG/technology/site eligibility is handled by the decision's cancellation trigger, with invalid expiry also routed through cancellation.
Do not leave the old `brilliant_scientist_krg_pay_project_batch_cost` call or invoke the old rifle/support completion helper.
`brilliant_scientist_krg_complete_clone_growth_cycle` is a thin call to the new finish helper, replacing its old rifle/support reward after the baseline was frozen.

Example future callback: `complete_effect = { brilliant_scientist_krg_begin_clone_maturation = yes }`.
The core trusts native admission for CIC and timer ownership; direct scripted callers are not authorized to bypass that contract.
One active native decision means no arbitrary generation selector is introduced; a future scheduler permitting overlapping same-family callbacks would require explicit generation ownership rather than reusing this single-receipt API unchanged.

## Validation and remaining work

In-memory tests reused the existing project adapter interpreter and parsed these actual sources without changing or adding a test framework.
Fifty-nine transaction assertions covered exact/short costs, both native CIC ordering models, both actual site markers, duplicate begin/finish/cancel, invalid KRG/operation/technology/capitulation/ownership/control, stale country flags, no lifetime cap, paid-snapshot refunds/output, malformed receipts and identity-pressure activation once.
Two additional scope-sensitive source scenarios used invoking country KRG and outer ROOT GER, confirming that KRG-controlled sites qualify and GER-controlled sites do not.
An AST comparison proved the extracted old history/crisis body is identical after excluding its two old stockpile outputs.
KRG identity/operation results and the reserve-refresh consumer were explicit stubs; actual new site predicates, transaction, debit helper, output and history source were executed.
The refresh stub verified invocation after equipment output; the real consumer's stockpile and multiplier source was independently inspected.
These are source checks, not HOI4 native-timer, MCP lifecycle, or in-game evidence.

No icon or asset is created: future consumer retains `GFX_decision_brilliant_scientist_krg_clone_growth` and the current category.
The parent applied the live wrapper and localisation after the baseline `E016_CLONE_MATURATION_2026_09_08` was frozen; the AI base remains `brilliant_scientist_krg_ai.medium`.
Required follow-up is the matching probability comparison and post-integration decision audit.
The broader private Mengele site/production proposal is separate and does not gain access through this KRG core.
No completion claim is made for the wired maturation decision until those tasks are done.
