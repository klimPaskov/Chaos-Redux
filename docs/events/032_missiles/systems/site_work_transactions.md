# Launch-site work and loyal recovery

Site surveys own a country payment receipt for one frozen state, distinct from launch-operation escrow and other site projects.
The receipt records its generation, payer, exact state ID and pointer, start date, purchased duration, three quoted amounts and three observed native payments.
Manpower, support equipment and fuel use one centralized quote and the shared native cost predicates and payment helpers.
The native decision, displayed resource colours and payment entry use inclusive affordability checks.
Another active project, native mission, unsettled refund or quarantined account prevents a fresh survey payment.

Preparation measures national stock before and after each native payment.
Only the observed removal is recorded as paid.
A partly paid start returns those observed amounts and does not activate a mission or establish a site.
A funded survey requires the full-payment flag and positive observed payments equal to its frozen quote, alongside matching payer, generation and state identity.
Missing or mismatched proof cannot found a launch site or authorize a refund.
Recorded payment cannot exceed its frozen quote, and a pending return requires the same closed payer/receipt with credited plus pending quantities bounded by observed payment.

Survey cancellation returns the unused share of the recorded payment.
Elapsed work days round up through the shared date helper, and integer refunds round down.
For a 60-day survey cancelled after 30 days, the ordinary quote returns 150 manpower, 20 support equipment and 125 fuel.
Changing the quote or survey duration later does not change that receipt's purchase or refund.
The payment is retired before any refund credit, so duplicate cancellation cannot spend the same receipt again.
Native credits are measured as well: a storage limit or declined mutation leaves the uncredited balance pending, and later finite programme interactions retry only that balance.
Inconsistent or unobservable changes quarantine the account and stop further automatic credit.
An unavailable pre-observation prevents the native mutation itself, and quarantine stops subsequent components in the same pass while preserving the first anomalous readings.
Zero returns perform no native read or mutation and cannot quarantine an otherwise successful project.
Removed countries receive no invented successor refund; the original payer's unresolved balance remains attached to its account.

The mission succeeds only after its due date with a funded current receipt and a valid state.
Successful completion consumes the survey payment, registers the surveyed state through the existing site owner and records no refund.
The last settlement preserves its state and reason after active project fields are cleared.
The survey decision description reports why the last project stopped and the resources actually returned.
It also distinguishes a pending return from an unreconciled account.

Loyal recovery uses the explicit concrete-garrison alternative in the accepted decision specification.
At least two divisions belonging to the country must be in the actual rogue launch state's location at order entry and at due mission success.
The same native `divisions_in_state` condition applies to human and AI countries; foreign divisions do not count.
The count is not presented as a live division-supply measurement.
AI can use this route when its garrison is present and can choose the other rogue responses when it is absent.
No undocumented dynamic movement order is fabricated.

The recovery quote remains 15 command power, 1,200 manpower and 140 infantry equipment.
The shared gate is inclusive, and the begin effect rechecks it before charging once.
The order snapshots its payer, exact site and allocated rogue-incident context.
Success rechecks that receipt, the due date and garrison before restoring the site, granting command control or closing the crisis.
An early, duplicate, lost-site, scuttled-site, wrong-payer or stale-context completion cannot award recovery.
Closing the rogue crisis removes its recovery mission and clears its private recovery/context fields.

## Files and interfaces

`032_missiles_survey_constants.txt` owns ordinary survey prices and settlement reason IDs.
`032_missiles_survey_triggers.txt` owns quote components, payer receipt, full funding and fresh start gates.
`032_missiles_survey_effects.txt` owns measurement, payment, progress settlement and pending returns.
`032_missiles_recovery_constants.txt`, `032_missiles_recovery_triggers.txt` and `032_missiles_recovery_effects.txt` own the garrison policy, context validation, quote and presentation.
Existing operation effects retain the native project entry/completion/cancellation wrappers and rogue lifecycle.
Existing decisions and missions remain the only player action surface.
`032_missiles_site_work_localisation.txt` and the existing decision localisation own cost colours and settlement wording.

The shared cost API's native dispatch is reused without introducing another discount source or changing Event 26 transaction history.
Its whole-transaction refund API does not express a progress fraction, so the survey owns the fraction and calls the existing native credit component for each fixed remainder.
The native resource readers are `manpower_k`, `fuel_k` and `num_equipment@support_equipment`; thousand-unit readers are converted before measuring deltas.
All cross-helper temporary outputs are created by their caller before use.

`missiles_start_paid_survey` runs in COUNTRY decision scope with FROM as the native selected STATE.
It returns normal `missiles_survey_start_result`, defaults to rejected and publishes the timer only after complete observed payment.
`missiles_refund_cancelled_survey` runs in the actual payer COUNTRY, needs no surviving wallet or state ownership, and defaults to no credit without current payment proof.
`missiles_close_survey_payment_with_refund` consumes caller-created temporary `missiles_survey_refund_ratio`; it closes a current receipt before creating fixed pending credits.
`missiles_settle_pending_survey_refund` runs in its recorded payer and retries three existing balances only, without repricing or scheduling another observation.
`missiles_measure_survey_resource`, `missiles_pay_survey_component` and `missiles_credit_survey_component` use caller-owned native resource-kind/amount and observation outputs; invalid changes retain quarantine rather than manufacturing success.
`missiles_floor_survey_refund_amount` accepts and returns caller-owned `missiles_survey_credit_amount`, defaulting negative values to zero.

Example: the state-targeted survey decision calls `missiles_begin_survey`, then activates the existing mission only when the paid start marked work in progress.
Native cancellation and timeout call `missiles_cancel_site_survey`, which preserves the settlement before clearing active work.
Country removal calls the same settlement before removing native missions.

## Presentation and validation limits

The ordinary category and its static picture are unchanged.
Existing manpower, support-equipment, fuel, command-power and infantry-equipment texticons identify the three fees in each action.
Existing survey and recovery decision/mission sprites remain in use; no new art, GUI, equipment, technology, achievement family or CXT package is introduced by these transactions.
The settlement notice belongs to the survey description and does not add a primary category meter or action.

Actual-source tests exercise the payment/credit owner, shared dispatch, date conversion, identity, closure, decision and mission gates with injected native stock/world facts.
They do not establish engine reader visibility, producer/variant restoration, mission callback timing or native AI movement.
The survey registration consumer is an explicit boundary in this transaction suite; physical construction remains covered by its own site implementation and acceptance work.
Native decision-list layout remains a separate visual check.

The survey's complete candidate-pool and highest-score selection requirement remains accepted work requiring reconciliation with the existing state-targeted entry.
This document describes the paid transaction and current selected-state registration and does not promote that selection gap to an approved simplification.
Secondary construction's separate cancellation contract and physical unconventional payload custody remain separate accepted work.

Future work should preserve these payer/receipt interfaces while completing candidate selection and owner-specific payload custody.
It must retain unacknowledged balances and must not add a periodic country/world refund or mission-grant scan.
