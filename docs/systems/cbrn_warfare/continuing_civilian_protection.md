# Continuing civilian protection

Paid hospital care, issued protective equipment and medical capability reduce continuing chemical losses through the existing state loss event.
Hospital care lasts fourteen days and losses retain their thirty-day assessment period.
The state records valid paid care so a response that expires before the next assessment still contributes its covered time.
The [accepted contract](../../specs/chaos_warfare_system_specs/corrections/2026-10-09_continuing_civilian_protection.md) identifies the existing hospital promise, protection budget and interpretation of time.

## State lifecycle

The existing Protect Hospitals decision is relevant to a controlled state with chemical contamination or an exact raid alert.
An active hospital response prevents a duplicate purchase, and the native cooldown remains in force.
Its three cost getters, affordability check and payment use the same current population quote with existing prices, bounds and rounding.
The order records those ordinary prices in its payment and purchase receipts, including the ordinary basis for a discounted purchase.
No earlier alert or cached state price is required.
The exact-alert adapter has no active caller in the audited source; the contamination route does not fabricate that alert or expose the other pre-raid responses.

1. The existing hospital order validates and settles its displayed payment.
2. Successful completion records the same duration used by the hospital flag and modifier in paired state arrays, `cbrn_hospital_protection_start_days` and `cbrn_hospital_protection_end_days`.
3. Overlapping or contiguous paid periods merge, and the assessment counts their union once.
4. The scheduled assessment uses the current issued models, fitting, filter condition, military-priority cleanup-kit allocation and controller medical capacity.
5. The medical calculation runs with and without the authored hospital bonus, then weights the difference by the covered fraction of that scheduled period.
6. The existing Burn Treatment multiplier joins the other protection factors under the same-mask floor.
7. The existing population, random-value and episode-cap calculation records the resulting loss.
8. Completed portions of care are consumed while future portions remain available for the next period.

The timed flag alone grants no continuing-care history.
Missing, mismatched or invalid interval data cannot create hospital time.
Mismatched paired arrays are retained as evidence rather than guessed into a repaired history.
Valid registrations are chronological and merged.
Unsorted externally modified arrays are outside this contract.

Verified new alerts retain their existing response-reset policy and close future hospital time through the central response clear.
Every real control change also closes future service, including states without issued masks and transfers during suppressed world rewrites.
This state-local closure touches neither country stock nor country protection aggregates.
Other mask and kit callbacks retain the existing world-rewrite guard.
Elapsed valid care remains attached to the state for its pending assessment.

Early and stale callbacks do not move an already-future due date or enqueue another receiver.
A late legitimate callback assesses the originally scheduled period and starts the next period from execution day, preserving the existing unprotected loss cadence.
Disabled and zero-rate assessments consume elapsed care without registering losses or drawing random values.
Expiry prunes idle history without creating a new polling loop.

## Protection calculation

Let `f` be the fraction of the scheduled period covered by the union of paid care intervals.
The existing protection calculator supplies same-mask multiplier `M`, ordinary protection `P0` and protection with hospital care `P1`.
The combined factor is `max((P0 × (1 − f) + P1 × f) × B, M × 0.50)`, where `B` is the existing Burn Treatment factor when applicable.
All durations, coefficients and thresholds come from the existing CBRN tuning files.
The initial medical-saturation multiplier is not reused as an invented death coefficient.

Both medical passes use the same current discrete equipment and controller inputs.
This model records hospital time and does not reconstruct past equipment inventories or medical-capacity changes.
The shared snapshot returns the pre-hospital medical base through caller-owned temporary storage.
The calculation adds the authored hospital bonus before clamping, so a base of ninety is not misread as seventy-five after an earlier combined value reached one hundred.
Existing protection thresholds can leave a hospital intervention on a plateau when equipment, fitting or other care is insufficient.

The stored continuing rate contains the authored stage and class rate.
The current controller's terminal-hazard multiplier applies once to the caller's scaled percentage at its original quantization step.
It is common to full and same-mask outcomes and does not create an additional mitigation allowance.
The factor floor applies before the existing random draws, rounding and caps.
It does not promise a fixed ratio between two realized integer casualty totals.

## Ownership, presentation and verification

`cbrn_continuing_protection_effects.txt` owns the state interval and calculation helpers.
`cbrn_delivery.4` remains the sole continuing-loss consumer, while the paid hospital outcome, central response clear and native control callback own entry and invalidation.
The exact API contracts are in [the helper reference](../../../common/scripted_effects/cbrn_scripted_effects.md#continuing-civilian-protection).
The existing hospital decision icon, modifier presentation and medical MIO nodes are reused.
`interface/cbrn_protection.gfx` binds `GFX_decision_cbrn_protect_hospitals_and_utilities` to `gfx/interface/decisions/stage_2_protective_equipment/decisions/cbrn_protect_hospitals_and_utilities.dds` and `GFX_cbrn_hospitals_utilities_protected` to `gfx/interface/ideas/stage_2_protective_equipment/cbrn_hospitals_utilities_protected.dds`.
No icon, sprite alias, GUI, research node, project, decision or CXT package is added.
The public hospital and medical MIO tooltips describe conditional benefits and retain the existing cost rows and durations.

The [source handoff](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-09_continuing_protection_review.md) records the paid-state and scheduling scenarios and their explicit native-input models.
The [random-value review](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-09_continuing_protection_random_review.md) distinguishes the documented draw range from unknown distribution and seed behavior.
The existing helper-return cleanup model remains conservative, and tests bind state-event ROOT separately from payer-country and control-callback ROOT.
Native execution, timer ordering, stock settlement, tooltip wrapping and full population/history integration remain unproved.

Future work should close those native acceptance gaps and evaluate current-tick equipment sampling against campaign evidence.
Any historical equipment sampling would require its own accepted design and exact lifecycle records.
It must not be inferred from the paid hospital-time arrays.
