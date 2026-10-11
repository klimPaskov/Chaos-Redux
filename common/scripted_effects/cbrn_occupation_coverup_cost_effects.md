# CBRN occupation coverup cost adapters

This contract covers the existing Seal State and Destroy Contaminated Records purchases.
The quote and affordability bodies live in `common/scripted_triggers/cbrn_occupation_triggers.txt`.
The existing execute and settle bodies live in `cbrn_occupation_effects.txt`.
The recovery helpers live in `cbrn_occupation_coverup_cost_effects.txt`.
The [implementation handoff](../../docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-07_cbrn_coverup_cost_adapter.md) records source evidence and validation limits.

## Price getters and affordability

`cbrn_occupation_prepare_seal_state_pp_quote` and `cbrn_occupation_prepare_destroy_records_pp_quote` are COUNTRY-scoped scripted triggers.
They first obtain the ordinary fractional price from `condemnation_prepare_scaled_fraction_cost`, using the existing 40 or 60 PP base and the existing clamped score multiplier.
They pass that represented ordinary amount to the neutral `universal_cost_quote_exact` producer with family `political_power` and quantum one.
Every eligible registered source composes through that producer, regardless of the Black Friday active flag.
With no eligible source, the ordinary fraction is unchanged.
With eligible sources, the final positive amount is quantized once to an integer PP amount.
A malformed registry or invalid final quote is diagnostic only and cannot authorize a fresh payment.

Before invoking either price getter, the caller initializes all four temporary outputs to zero in its own frame:

```txt
set_temp_variable = { cbrn_occupation_coverup_pp_quote = constant:universal_cost_framework.zero }
set_temp_variable = { cbrn_occupation_coverup_pp_ordinary = constant:universal_cost_framework.zero }
set_temp_variable = { cbrn_occupation_coverup_pp_quote_valid = constant:universal_cost_framework.zero }
set_temp_variable = { cbrn_occupation_coverup_pp_source_id = constant:universal_cost_framework.zero }
cbrn_occupation_prepare_seal_state_pp_quote = yes
```

The final price is `cbrn_occupation_coverup_pp_quote`.
The ordinary price is `cbrn_occupation_coverup_pp_ordinary`.
`cbrn_occupation_coverup_pp_quote_valid = 1` is required before fresh affordability or payment.
`cbrn_occupation_coverup_pp_source_id` is the actual producer's primary source, with zero meaning no eligible source.
There are no additional public price outputs.
The helpers return true after producing data, including invalid data, so callers must test validity explicitly.
The only side effects are temporary quote scratch and exact arithmetic storage.

`cbrn_occupation_can_pay_seal_state_pp` and `cbrn_occupation_can_pay_destroy_records_pp` run in COUNTRY scope with the selected STATE as FROM.
They initialize the four output fields before a nested price call.
For a fresh purchase, they reject any open pointer, recompute the same price and invoke `universal_cost_component_is_affordable` with Political Power and the final quoted amount.
They also accept `cbrn_occupation_coverup_can_retry_refund` as recovery-only availability, even at zero PP or when a fresh quote is invalid.
That pure shared preflight requires a positive pointer, matching saved target, positive saved payment and a refund phase.
Malformed pointers cannot fall through to another paid action.
They never debit, refund, settle, dispatch, change target requirements, or change persistent state.
An outer caller reading their returned quote fields must still initialize all four fields before calling them.
On the recovery branch those fields remain zero and are not a payable purchase quote.

## Execute and settle

`cbrn_occupation_execute_paid_coverup` runs in COUNTRY scope with FROM as the selected STATE.
Its required temporary input is `cbrn_occupation_coverup_payment_action`, set to the existing seal or destruction enum.
It snapshots whether that state already has an open receipt, invokes bounded payer recovery first, and restores its selected target scratch before applying the original action, state, and affordability checks.
A click that began with an open receipt performs recovery only, even if recovery succeeds.
It cannot silently buy a replacement action in the same click.
There is no exported temporary result required by the current decision callers.

`cbrn_occupation_settle_paid_coverup` is an internal COUNTRY-scoped entry used only after the execute gate.
It consumes the four freshly quoted fields, action input, and selected target.
It allocates a unique payer transaction ID, pays through `universal_cost_pay_component`, and stores owner recovery proof before calling any further helper.
Immediately before payment it snapshots the current public `black_friday_achievement_is_valid_sale` predicate together with actual source 26 and positive ordinary/quoted amounts.
Only a successful debit with that positive snapshot adds the receipt ID to the normal payer array `cbrn_occupation_coverup_achievement_eligible_receipts`.
Membership is retained through rejected settlement and cannot be acquired by a later AI-to-human or debug-to-normal transition.
This is positive receipt-ID proof, not a regular numeric boolean or immediate achievement credit.
It records one real shared component with family `political_power`, primary ID `owner_component_political_power`, basis `primary_component`, membership one, and the actual quote's source ID.
Quoted and actual-paid fields are equal.
The ordinary field retains the represented ordinary fraction.

Only a successful record permits state dispatch.
The wrapper creates caller-owned coverup proof, exact-record suppression proof, exact-row selector, and doctrine multiplier storage before entering FROM and invoking the existing requested-action mapper.
It sets and clears the existing state's `cbrn_occupation_requested_coverup_action` around that call.
Outcome helper bodies, exact UID selection rules, evidence changes, penalties, timers, and route predicates remain unchanged.

A missing dispatch proof refunds the recorded actual amount through the real shared refund API.
A rejected record refunds the stored actual amount through the real shared credit API because no shared receipt was accepted.
After an applied outcome, recovery settles the real receipt and only then invokes `black_friday_record_achievement_transaction` with PP-only proof enabled.
Source 26 and the retained sale sequence must match, and the ordinary shared natural-sale, human-country, active-sale and disqualifier gates remain authoritative.
Recovery also requires the retained payment-time eligibility membership before invoking that shared claim API.
Receipts without a positive eligibility snapshot remain settleable and refundable, but current eligibility cannot retrospectively qualify their payment.
There is no pending or refunded family credit and no direct family-credit shortcut.

## Persistent payer proof

All storage below is normal payer-owned state.
Each transaction uses a unique receipt ID, allowing receipts for several target states and later transactions on one state to coexist.

| Field | Meaning |
| --- | --- |
| `cbrn_occupation_coverup_pending_receipts` | Queue of receipt IDs needing recovery or queue cleanup |
| `cbrn_occupation_coverup_achievement_eligible_receipts` | Positive payment-time achievement eligibility for exact receipt IDs, consumed on acknowledged settlement/refund cleanup |
| `cbrn_occupation_coverup_open_receipt_@var:cbrn_occupation_coverup_target` | Exact target's unresolved refund receipt, preventing another debit |
| `cbrn_occupation_coverup_receipt_target_@var:cbrn_occupation_coverup_receipt_id` | Original target STATE pointer |
| `cbrn_occupation_coverup_receipt_action_@var:cbrn_occupation_coverup_receipt_id` | Original seal or destruction selector |
| `cbrn_occupation_coverup_receipt_ordinary_@var:cbrn_occupation_coverup_receipt_id` | Ordinary price snapshot |
| `cbrn_occupation_coverup_receipt_paid_@var:cbrn_occupation_coverup_receipt_id` | Actual debited PP and direct-refund basis |
| `cbrn_occupation_coverup_receipt_source_@var:cbrn_occupation_coverup_receipt_id` | Actual primary source snapshot |
| `cbrn_occupation_coverup_receipt_sale_@var:cbrn_occupation_coverup_receipt_id` | Sale generation at payment |
| `cbrn_occupation_coverup_receipt_phase_@var:cbrn_occupation_coverup_receipt_id` | Recovery phase from the owner constant category |

The phase category is `constant:cbrn_occupation_coverup_receipt_phase`, defined in `common/script_constants/cbrn_occupation_coverup_cost_constants.txt` with an integer schema.
`unrecorded_refund = 1` means the debit has no accepted shared receipt.
`recorded_refund = 2` means no outcome succeeded and the shared receipt needs refund acknowledgment.
`applied_settlement = 3` means the outcome succeeded and its shared receipt needs settlement acknowledgment.
These are lifecycle states, not boolean counters or cost tuning.

An applied outcome immediately clears the per-state open pointer while retaining its transaction-specific proof if settlement fails.
No successful action is additionally locked by an accounting failure.
Shared receipt and component history remains in the neutral API's normal arrays after local recovery finishes.

## Recovery helpers

`cbrn_occupation_recover_paid_coverup_receipt` runs in payer COUNTRY scope.
Its required temporary input is `cbrn_occupation_coverup_receipt_id`.
It exports no temporary output.
Without a retained phase it does nothing.
An unrecorded refund uses the real credit API with the retained actual amount.
A recorded refund uses `universal_cost_refund_transaction` and retains proof on rejection, partial refund, unknown row, or other unacknowledged state.
An applied settlement uses `universal_cost_settle_transaction` and retains proof when no valid settlement is acknowledged.
An explicit public lookup also recognizes an already-refunded or already-settled row for idempotent acknowledgment.
No branch replays an outcome or infers refund success from a missing row.

`cbrn_occupation_clear_paid_coverup_receipt` is an internal payer COUNTRY helper with the same receipt-ID input and no temporary output.
It clears the per-state open pointer only if that pointer still identifies this exact receipt.
It then clears this receipt's private fields and obsolete allocator proof.
It leaves shared receipt, component, and achievement evidence intact.
It removes only the matching receipt ID from the payment-eligibility array, using native value removal rather than dropping the array tail.
Other pending receipts keep their own eligibility proof.
The queue entry is removed on the next bounded queue visit.

`cbrn_occupation_recover_paid_coverups` is the public payer COUNTRY recovery entry.
It takes no inputs, requires no FROM, and exports no temporary output.
It snapshots the initial queue count and removes the first ID before recovering it.
It appends the ID only if a phase remains.
The loop visits at most the initial count and is also bounded by the native 1,000-iteration stop.
Every unvisited suffix remains in the normal queue, and unresolved visited IDs rotate behind it.
There is no payment-count cap, source-count cap, receipt deletion fallback, or world tick scan.

```txt
# Existing owner-trigger or player action, already in the original payer scope.
cbrn_occupation_recover_paid_coverups = yes
```

## Presentation and integration boundary

For an exact-state pending refund, use the [pure recovery preflight](../scripted_triggers/cbrn_occupation_coverup_cost_triggers.md) with caller-owned zero-initialized target and receipt-ID output storage.
On success its receipt ID selects the retained paid amount.
Do not expose a pending refund from `has_variable` alone.
The parent owns localisation and decision integration.
Current parent getter branches show payment recovery and explain that the click makes no new purchase.
Fresh price and tooltip branches initialize all four quote outputs and use the quote-valid flag.
Their nested amount selector renders integral prices with zero decimals and ordinary fractions with five decimals.
Malformed open pointers show price unavailable rather than payment recovery or a new price.

The native decision still applies its existing target requirements and re-enable timer.
An otherwise eligible pending-refund target can be clicked at zero PP.
If target control, route, record or visibility requirements fail, the decision cannot provide a recovery click.
After a successful coverup, that state's existing response flags also normally hide its purchase decision.
Other existing paid-coverup clicks service the payer queue, and an owner-trigger can call the public recovery entry without the target.
This patch does not add an owner-trigger consumer outside the assigned files.
If no subsequent eligible click occurs, invoking that owner path remains an integration requirement.

The source tests establish behavior under modeled native primitives and conservative temporary lifetime.
They do not establish native engine execution, save/reload persistence, timer expiry, native row presentation, multiplayer behavior or AI hint pacing.
No art or sprite identifier changes are needed for these existing decisions.
