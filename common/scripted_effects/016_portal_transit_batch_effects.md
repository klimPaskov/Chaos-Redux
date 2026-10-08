# Event016 Portal transit batch API

Authority: `docs/plans/016_brilliant_scientist_plans/016_portal_transit_fabrication_receipts_2026-10-08.md`, including the parent's explicit native-entry, quote-consumer and partial-output clarifications.
This country-scope core repairs the existing KRG action and provides one neutral equipment output seam.
It does not implement private Deployment commissioning or change other project-batch payment helpers.
The accepted private route remains queued in `016_mengele_transit_deployment_acceptance_2026-10-08.md`.

## Public effects

All calls are parameter-free literal scripted-effect calls in the paying country.
Every result consumed after return must have temporary storage created in the caller before the call.
Result codes use `universal_cost_framework`: no-op 0, success 1, partial/pending 2 and rejected 3.
Neutral delivery returns a measured quantity rather than a result code.

| Effect | Explicit temporary inputs | Caller-owned output | Behavior |
| --- | --- | --- | --- |
| `brilliant_scientist_add_portal_transit_equipment` | `portal_transit_equipment_amount` positive; actual existing Portal technology required | `portal_transit_equipment_delivered`, initially zero | Adds only `teleportation_equipment_1` with `producer = THIS`; measures concrete inventory delta; consumes amount to zero on every exit. No payment/history/flag/technology/template/unit write. |
| `brilliant_scientist_krg_begin_portal_transit_batch` | `krg_portal_batch_native_entry = one`, set immediately before this call by the existing decision's literal native entry callback | `krg_portal_batch_begin_result` | Rechecks non-CIC admission requirements and one fresh direct quote, publishes actor/action/serial receipt before debit, measures and records actual payments; funds only all-three success. Consumes native-entry marker to zero on every exit, including rejection. |
| `brilliant_scientist_krg_finish_portal_transit_batch` | None | `krg_portal_batch_finish_result` | Requires current funded receipt, operational/cap proof, consumes active timed authority, delivers saved quantity without repurchase/CIC checks. Only exact full delivery advances the existing KRG counter once. |
| `brilliant_scientist_krg_cancel_portal_transit_batch` | None | `krg_portal_batch_cancel_result` | Retires active authority before refund; native cancel/expiry owns removal. Refunds zero-delivery work only; positive partial delivery retains funded recovery. |
| `brilliant_scientist_krg_cleanup_portal_transit_batch` | None | `krg_portal_batch_cleanup_result` | Cancels/retains the receipt first, then explicitly removes the native decision and checks closed state after possible reentry. No scheduler or world hook. |
| `brilliant_scientist_krg_recover_portal_transit_batch_output` | None | `krg_portal_batch_output_recovery_result` | Valid partial funding delivers only expected minus already delivered; completed delivery retries settlement only. No new payment, native timer, CIC, cap consumption or replayed history. |
| `brilliant_scientist_krg_recover_portal_transit_batch_refund` | None | `krg_portal_batch_refund_result` | Retries matching measured refund obligations and acknowledges restored shared components. Failed work remains pending. No payment, timer, CIC or equipment output. |

The native-entry marker is a source-bound authorization seam, not observed engine reservation timing.
Bare BEGIN without exactly one rejects before receipt, allocation or payment mutation and preserves any current paid/recovery records.
The only CIC exception is this authorized entry path.
UI selection uses the full four-free-CIC gate and has no marker requirement.

### Examples

```text
# Inside the existing literal native complete_effect, after native admission:
set_temp_variable = { krg_portal_batch_begin_result = constant:universal_cost_framework.result_no_op }
set_temp_variable = { krg_portal_batch_native_entry = constant:portal_transit_batch.one }
brilliant_scientist_krg_begin_portal_transit_batch = yes
set_temp_variable = { krg_portal_batch_native_entry = constant:portal_transit_batch.zero }
# Only result_success means funded work; a duplicate rejection must not cancel it.
```

```text
# A neutral explicit grant is independent of KRG payment/history:
set_temp_variable = { portal_transit_equipment_amount = constant:portal_transit_batch.equipment_output }
set_temp_variable = { portal_transit_equipment_delivered = constant:portal_transit_batch.zero }
brilliant_scientist_add_portal_transit_equipment = yes
# amount is zero here; retain any expected quantity separately before calling.
```

## Public pure triggers and quote lifetime

`brilliant_scientist_krg_quote_portal_transit_batch` computes one coherent fresh PP/support/fuel quote through the actual shared `universal_cost_quote_exact`.
Its boolean return is always true; `krg_portal_batch_quote_valid` is the validity result.
No regular variable, flag, receipt or inventory is changed.
Malformed shared registry/quote data returns valid zero and is not a substitute ordinary price.

Required consumed caller-owned temporaries are `krg_portal_batch_quote_pp`, `krg_portal_batch_quote_support`, `krg_portal_batch_quote_fuel` and `krg_portal_batch_quote_valid`, initially zero.
Optional `krg_portal_batch_quote_<pp|support|fuel>_source` and `..._source_count` outputs must also be caller-owned if consumed.
BEGIN owns all of them to retain payment-time proof; the parent's UI/CXT need only their four consumed outputs.
PP uses the Political Power family mask; concrete support uses the Support Equipment mask; fuel uses the Fuel mask.
Logical achievement Equipment classification is separate from these resource-specific eligibility masks.

The pure colour predicates are exactly:

- `brilliant_scientist_krg_portal_batch_can_pay_political_power`
- `brilliant_scientist_krg_portal_batch_can_pay_support_equipment`
- `brilliant_scientist_krg_portal_batch_can_pay_fuel`

They consume the already owned four quote outputs, test valid/positive cost and inclusive live affordability, and perform no quotation.
Their caller must obtain a fresh quote first; do not use a display cache for selection/payment.
`...can_pay_direct` computes a fresh quote once and composes these same predicates.
`...can_pay` also requires four currently free CIC.
`...requirements_met` checks operational/cap/receipt/recovery availability and preserves the original non-consumed `num_of_military_factories > constant:brilliant_scientist_krg_value.zero` admission requirement.
One military factory is the exact minimum admissible integer count; zero is rejected.
This is not a fifth cost, and expiry/output recovery does not repurchase or retest military industry.
`...can_start` combines requirements and full affordability.

`...is_operational` preserves active KRG decision authority, operational Teleportation, bounded recruitment focus receipt and the existing raid-AI OR linked-network condition, adding actual Portal technology and noncapitulation.
`...receipt_is_current` validates active/funded actor/action/serial, saved output, three exact shared component rows and their ordered linked chain, and recorded/unrefunded ledger state.

Recovery UI binds these exact pure predicates:

| Predicate | Purpose |
| --- | --- |
| `brilliant_scientist_krg_portal_batch_output_recovery_is_pending` | Partial output or delivered-but-unsettled work exists; also exposes malformed retained work as a blocked row. |
| `brilliant_scientist_krg_portal_batch_refund_recovery_is_pending` | Refund work is retained, including unresolved malformed records. |
| `brilliant_scientist_krg_portal_batch_can_recover_output` | Valid funded partial remainder under current authority/cap, or exact committed full delivery awaiting settlement. |
| `brilliant_scientist_krg_portal_batch_can_recover_refund` | Original actor/action/serial, complete nonnegative snapshot, no delivered output, no active/funded/committed authority. |

The actual refund effect additionally validates all existing recorded rows/count/chain before any credit.
A missing/corrupted shared row or identity is not permission to infer paid amounts or repair history.
A blocked pending record retains its evidence for explicit parent recovery.

## Persistent owner receipt and recovery fields

All fields are in the original paying COUNTRY, not ROOT.
No event target or global singleton is introduced.

| Field | Meaning |
| --- | --- |
| `krg_portal_batch_actor` | Saved THIS country scope identity. |
| `krg_portal_batch_action` | Literal internal action ID from the feature constants. |
| `krg_portal_batch_serial`, `krg_portal_batch_receipt_serial` | Owner sequence and matching receipt snapshot; these establish internal consistency, not immutable native callback generation. |
| `krg_portal_batch_transaction_id` | Payer-local ID from `black_friday_allocate_owner_transaction`. |
| `krg_portal_batch_output_expected`, `krg_portal_batch_output_delivered` | Saved full target and measured cumulative delivery; remainder is their difference. |
| `krg_portal_batch_sale_sequence` | Payment-time sale sequence, independent of live quote changes. |
| `krg_portal_batch_nominal`, `...final`, `...source`, `...source_count` | Three aligned ordinary/final/primary-source/source-count columns. |
| `krg_portal_batch_actual` | Three measured actual-paid quantities. |
| `krg_portal_batch_record_index` | Shared component row indices, invalid index for an unrecorded debit. |
| `krg_portal_batch_refund_remaining` | Measured owed refunds; never nominal prices. Cleared on exact completed delivery, or reduced only by observed credit. |

Array indices are `portal_transit_batch.pp_index` 0, `support_index` 1, and `fuel_index` 2; `component_count` is 3.
Persistent phase/proof flags are `krg_portal_batch_active`, `...funded`, `...output_pending`, `...refund_pending`, `...settlement_pending`, `...delivery_committed`, `...shared_refund_attempted`, `...sale_eligible` and `...closed`.
Closed snapshots remain observable until the next legitimate start; shared historical ledger rows remain permanent.
Different actions and other KRG robot/alien/temporal batch receipts are untouched.

Shared record IDs/kinds use the existing PP, concrete Support Equipment kind 11, and Fuel contracts.
The support component is the logical Equipment primary, using existing Equipment family 112 and `black_friday_event.owner_component_support_equipment`, with explicit primary-component basis and membership on every record.
No achievement family is inferred from PP.
The framework records pending refundable achievement proof at funding, retracts on cancellation and confirms only after full delivery and shared settlement.
Its existing eligibility/expiry/classification rules still govern credit; this core does not authorize awards after expiry or grant new achievements.
Mixed/non-26 source proof is not rewritten into Black Friday eligibility.

## Internal helpers and temporary outputs

| Internal helper | Inputs / caller-owned consumed outputs |
| --- | --- |
| `...portal_batch_read_component_balance` | Literal component index; output `krg_portal_batch_component_balance`. PP/support use direct units; fuel uses thousands, converting only the measured delta to units. |
| `...portal_batch_pay_record_component` | Literal index/kind/component ID and original saved quote; output `krg_portal_batch_component_paid`. |
| `...portal_batch_achievement_claim` | Saved transaction/support primary and sale sequence; shared API decides eligibility, no private result. |
| `...portal_batch_check_recovery_records` | Saved rows; output `krg_portal_batch_recovery_records_valid`; no currency changes. |
| `...portal_batch_credit_owed_component` | Literal component and saved remainder; reduces only measured owed amount via shared credit and acknowledgement. |
| `...portal_batch_settle_delivered` | Exact committed delivery/transaction; output `krg_portal_batch_settlement_result`; never produces equipment/history. |
| `...portal_batch_deliver_remainder` | Funded current/recovery authorization; output `krg_portal_batch_delivery_result`; forwards caller-owned delivery/settlement/cancellation results. |

Internal pure identity/shape/component-row/funding/ledger predicates never write regular state.
Caller-owned scratch such as the component-row index is created before a nested predicate when read after return.
These helpers are feature-owned orchestration, not a central MCP router or shared wrapper skill.

## Tuning and native ownership

`portal_transit_batch` is schema-first and owns ordinary PP 65, concrete support 200, fuel 1,000, native CIC mirror 4, duration mirror 90, re-enable mirror 30 and output 180, plus representation/index constants.
Keys are `political_power`, `support_equipment`, `fuel`, `civilian_factories`, `duration_days`, `cooldown_days` and `equipment_output`.
The existing `brilliant_scientist_krg_capacity.portal_transit_batch_maximum` remains the four-success authority.
Parent decision modifiers/AI hints use reviewed static mirrors where their native fields reject script constants.
Factory commitment remains static and is not represented as universally discounted.
The existing native decision owns its timer and re-enable interval; recovery adds no timer, factory reservation or replacement cooldown scheduler.
Native `remove_decision` skips remove_effect and does not itself start a cooldown.

## Failure, recovery and engine limits

Debit is measured before shared record and compared with the fresh final quote; a partial or unrecorded debit cannot fund an output.
The owner's actual/remainder columns survive failed record operations.
Recorded components first use shared transaction refund; unrecorded debits and observed native-credit shortfalls use shared component credit and acknowledgement, never owner currency effects or locally invented discount arithmetic.
Initial refund authority is consumed before shared calls, and later explicit retries credit only the measured remainder.
If a shared helper reports refund success but actual native credit is zero/capped, the owner obligation remains pending.
Fuel delta conversion avoids multiplying a potentially huge absolute fuel reserve by 1,000.
Exact concrete model quantity can be restored; native stockpile API cannot restore original producer/design provenance.

Zero output may refund actual payments.
Any positive partial output retains funded authority and only its remaining delivery is recoverable.
No output is deleted, no payment is settled early, and no full refund coexists with retained free output.
Exact 180 cumulative output advances `brilliant_scientist_krg_portal_transit_batches` once before a possible settlement retry; recovery cannot replay that advance.
Unexpected over-delivery remains blocked/pending rather than clipped into success.
Corrupted/missing identity or snapshot data is retained; no nominal refund or history reconstruction is invented.

Native callback generation, reservation ordering, stockpile visibility at the getter boundary, source/design provenance and live engine behavior remain acceptance limits.
The source driver in the tranche handoff executes actual owner/shared definitions with conservative temporary frames and declares native/fault boundaries.
Parent owns final decision/wrapper/cleanup/UI/CXT integration, probability/domain audits, final docs and commits.
No HOI4 launch or model/asset/unit-package work belongs to this core.
