# Event 012 Gods contribution and conduct helper API

Contribution receipts are wired to the ordinary tribute, voluntary-aid and Final Council shipment owners listed below.
The conservative source-audit model is not a claim about native getter or variable limits.
See [the arithmetic repair evidence](../../docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_contribution_arithmetic_repair_2026-10-04.md).
Acceptance basis: the contribution/conduct section of [the full grading design](../../docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_full_grading_rewards_design_2026-10-03.md), lines 61-240, accepted by the parent on 2026-10-03 and adopted without a rewrite under agent decision L3.
These helpers contain no contract closure, clocks, events, country scans, GUI, assets, localisation, AI weights, or grading weights; the native sends stay in their owners.

## Wiring

| Owner | Call |
| --- | --- |
| `gods_of_africa_pay_council_pledge` | Freezes the existing Council price/reserve and exact authority, sets the exclusive Council purpose flag, and uses shared begin/native send/complete. Measured donor loss credits total/voluntary/campaign quantities and reduces only the unpaid pledge; host reserve follows bounded receiver gain. Voice and coarse aid publish only after full payment. The [Council API](012_africa_gods_council_effects.md) records retry, speech-switch and cleanup ownership. |
| `gods_of_africa_transfer_payment` | Every material branch sets the bare temp `gods_of_africa_payment_receipt_kind` to the branch it emits, calls `gods_of_africa_begin_payment_receipt`, emits the native transfer only when `gods_of_africa_material_transfer_begin_ready` is set, then calls `gods_of_africa_complete_payment_receipt`. The measured amount is published in the normal participant field `gods_of_africa_payment_delivered`. Fuel is first limited to the receiver's free tank space. Family 13 under a frozen, still-current emergency opens a kind-11 receipt around the existing political-power transfer; other political families deliver their paid political power without material credit. |
| `gods_of_africa_resolve_full_compliance` | Closes the contract only when `gods_of_africa_payment_delivered` covers the remaining balance; a short delivery goes through `gods_of_africa_apply_partial_delivery` and the remainder stays owed, without turning the contract into agreed terms. |
| `gods_of_africa_resolve_partial_compliance` | Requests at most the remaining balance, marks the contract as agreed terms once something arrives, and reduces the balance only by the measured delivery. |
| `gods_of_africa_resolve_substitute` | A partly delivered accepted substitute becomes the contract terms (`gods_of_africa_contract_substitute_terms`); nothing delivered restores the original contract. |
| `gods_of_africa_offer_voluntary_aid` | Infantry aid uses native `send_equipment` (500 shipment, 1000 capacity gate, unchanged cooldown); infantry and fuel both go through `gods_of_africa_begin_voluntary_receipt` and `gods_of_africa_complete_payment_receipt`, and the aid record uses the measured amount. |
| `gods_of_africa_create_demand_contract` | `gods_of_africa_freeze_contract_emergency_proof` right after the contract ledger opens; `gods_of_africa_clear_demand` and every participant cleanup clear it. |
| `africa_activate_evolution_iii` | Sets the bare temp `gods_of_africa_campaign_activation_owned` and calls `gods_of_africa_bind_contribution_campaign` inside the real activation. |
| `gods_of_africa_return_frozen_core_states` (territory payment) | For each state the contract named (`gods_of_africa_demand_states`, frozen at creation by `gods_of_africa_freeze_diplomatic_terms`) and still controlled by the participant, stores it in the normal participant variable `gods_of_africa_return_state`, calls `gods_of_africa_begin_core_return` before `transfer_state_to` and `gods_of_africa_complete_core_return` after it. |

Takeover decisions on the adopted package:

- A measured short or unequal delivery is an accounted outcome: the recorder credits the participant's measured loss (bounded by the request) once and keeps `gods_of_africa_material_transfer_mismatch` as evidence, and it no longer sets `gods_of_africa_material_transaction_unresolved`, which would have blocked every later payment.
  Africa's measured gain is published separately as `gods_of_africa_payment_received` (never more than the credited loss) and is the only value Africa's own stock accounts (`africa_common_defence_stockpile`) read.
  A payment that moves nothing records a `.604` row and a short retry lockout (`gods_of_africa_payment_retry_day`, decision L19).
  `gods_of_africa_material_transaction_unresolved` remains reserved for unreadable native values and identity drift.
- Temporary inputs are read by value (`check_variable`), not with `has_variable`, because an unset temporary input reads zero and fails the kind and amount checks anyway.
  The same applies to the grading helpers' temporary inputs.
- F2: armour is measured per chassis. F4: amounts are integral by construction (`gods_of_africa_floor_equipment_amount` and whole-unit partial payments). There are no lifetime caps; stockpiles above the native getter range are a live-game check, not a gameplay cap.

## Scope, inputs and initialization

Receipt calls run in COUNTRY scope on the donor participant.
Conduct accepts a genuinely initialized current or one explicitly inherited historical participant, including archived/capitulated participants whose history still satisfies the proof owner.
Only campaign binding runs in HOST scope.
Use boolean helper calls with bare caller-initialized temporary inputs; no parameter macros or scoped temporary variables.
All parent-consumed outputs are normal COUNTRY amounts or COUNTRY flags, so the caller does not need temporary output storage.

The grading owner initializes all forty material fields, emergency PP, receipt sequence counters, conduct counters and proof arrays through gods_of_africa_initialize_grading_ledger only at first genuine history.
Receipt helpers require gods_of_africa_full_grade_history_is_valid and gods_of_africa_full_grade_ledger_is_present and never backfill or initialize those fields.
The parent initializes grading before its contract-history initializer and records the actual immutable contract before any ordinary transfer.
Material permission additionally checks actual current roster membership, generation, active committed host/restoration generation, original host identity, and absence of final/frozen results or an unresolved material transaction.
Ordinary proof checks retained gods_of_africa_demand_host, gods_of_africa_demand_host_id and gods_of_africa_demand_origin_host_id against the current proven host and open origin/generation/contract tuple.
No receipt redirects an existing contract to a successor host.

## Helper map and parent hooks

| Helper | Scope, inputs and outputs | Side effects and intended parent call |
| --- | --- | --- |
| gods_of_africa_begin_material_transfer | PARTICIPANT; bare temps gods_of_africa_contribution_kind, gods_of_africa_contribution_native_emit_kind from the actual selected native branch, gods_of_africa_contribution_requested in raw native units, and gods_of_africa_contribution_voluntary as exactly zero or one; COUNTRY flag gods_of_africa_material_transfer_begin_ready is freshly cleared/set | Freeze permission, object references/IDs, origin/generation, actual ordinary contract ID or voluntary zero, request, participant/host authority epoch, day, subsets, native BEFORE readings and monotonic sequence immediately before the actual branch in gods_of_africa_transfer_payment or gods_of_africa_offer_voluntary_aid |
| gods_of_africa_complete_material_transfer | Same PARTICIPANT, synchronous owned effect; no delivered-amount input; COUNTRY flag gods_of_africa_material_transfer_completion_consumed is freshly cleared/set | Recapture both native AFTER stocks, consume once, publish actual delivery/debit/credit and full/mismatch immediately after transfer and before clearing payment/contract work |
| gods_of_africa_record_paid_contribution | Internal PARTICIPANT; current prepared, measured, pending envelope only | Check exact prospective total/subset writes before consuming pending and advancing last-consumed ID; completion calls it, never history/UI/quote/report/affordability |
| gods_of_africa_record_paid_emergency_aid | Same internal measured envelope | Compatibility alias for the same recorder; PP kind 11 never writes material fields; parent uses begin/complete around the real family-13 transfer |
| gods_of_africa_preflight_contribution_fuel | PARTICIPANT; no inputs; normal gods_of_africa_contribution_fuel_headroom_k in thousands of fuel | Read native receiver room before amount selection; begin also independently rejects excess |
| gods_of_africa_freeze_contract_emergency_proof | PARTICIPANT; real open contract and its original gods_of_africa_demand_band | Freeze exact host/contract/original-band proof once after contract opening and before mission/event dispatch |
| gods_of_africa_clear_contract_emergency_proof | PARTICIPANT; no inputs | Clear only emergency work on actual owner contract cleanup, after receipt completion |
| gods_of_africa_bind_contribution_campaign | HOST; bare gods_of_africa_campaign_activation_owned initialized to one inside actual Evolution III activation | Bind host generation/origin and active flag; consume input to zero; never call merely because a global flag is set |
| gods_of_africa_refresh_grading_conduct | Historical PARTICIPANT; no inputs | Capture host/participant scopes, refresh controlled/owned African host-core caches, unique occupied IDs, deduplicated war episodes, prior flags and current floor causes; existing bounded owner review and before acceptance/final freeze |
| gods_of_africa_measure_grading_wrath_floor | Historical PARTICIPANT; normal gods_of_africa_grading_wrath_floor | Compute maximum applicable existing floor and raise existing Wrath if needed; conduct calls it and parent replaces its sequential floor assignments |
| gods_of_africa_begin_core_return | PARTICIPANT in actual territory branch or pending final ultimatum; normal participant variable gods_of_africa_return_state holding the selected STATE (cleared by the caller afterwards); COUNTRY flag gods_of_africa_core_return_begin_ready | Freeze state/host/participant/day and contract or ultimatum identity plus participant pre-owner/pre-controller flags before native state transfer |
| gods_of_africa_complete_core_return | Same PARTICIPANT after that transfer; COUNTRY flag gods_of_africa_core_return_recorded | Require actual post-owner AND post-controller to be proven host; consume pending before first unique returned-state ID; refresh conduct before contract cleanup |
| gods_of_africa_clear_core_return_work | PARTICIPANT; no inputs | Clear only return snapshots/pending; successful completion or explicit accounted parent recovery |
| gods_of_africa_resolve_accepted_grading_conduct | PARTICIPANT inside HOST-root acceptance after the unique actual paid acceptance receipt | Resolve outstanding causes only with no war/controlled/owned core and same accepted offer tuple/day; call after gods_of_africa_record_accepted_reconciliation and before clearing paid/offer flags |
| gods_of_africa_abandon_pending_material_transfer | PARTICIPANT, explicit parent recovery only | Only unmeasured, non-mismatched, never-captured reservations: quarantine, record the gap ID and host session once, consume reservation ID and clear work; measured or uncertain emitted work is retained |
| gods_of_africa_clear_material_transfer_work | Internal PARTICIPANT | Clear transaction work and subset flags; preserve results, lifetime sequence/quantities and unresolved |
| gods_of_africa_capture_contribution_armor_before / gods_of_africa_capture_contribution_armor_after | Internal PARTICIPANT, captured receipt receiver and regular receipt_source target | Capture each real chassis separately on donor and receiver before/after the contiguous typed send, no full-pool sum |
| gods_of_africa_measure_contribution_armor_after | Internal PARTICIPANT, validated per-chassis snapshots and frozen request | Retain each positive difference, add only min(delta, remaining aggregate room), preserve excess evidence before bounding |
| gods_of_africa_read_contribution_native_stock | Internal COUNTRY; invoking capture initializes bare gods_of_africa_native_stock_kind and gods_of_africa_native_stock | Typed native stock output used before returning from that capture; no mutation |

Missing inputs and invalid kind/request/boolean fail closed without defaults.
Ordinary request must equal the normalized gods_of_africa_payment_amount exactly.
The native_emit_kind input must equal contribution_kind and the actual family branch, including gods_of_africa_payment_mobile_type and its frozen contract type.
Transport mirrors the actual convoy-first capacity test and permits train only when convoy capacity is insufficient and train capacity is sufficient.
All these checks precede begin_ready, so a mismatched input grants no native emission permission.
The parent captures the selected kind in a private normal owner field before setting the bare input temp and emits that same selected branch inside the contiguous transaction.
The helper cannot validate a branch the parent changes after begin.
Voluntary kinds are the existing infantry/fuel branches with explicit host need and existing cooldown checks.
Their guard uses an explicit host check rather than the existing aid trigger's host-only ROOT comparison.
It introduces no new voluntary decisions for the other kinds.

## Constants and native stock readings

Every constant category starts with its schema.
The integer gods_of_africa_contribution_kind group contains infantry=1, support=2, trucks=3, artillery=4, armor=5, aircraft=6, fuel=7, convoys=8, trains=9, manpower=10 and emergency_pp=11.
Fixed-point gods_of_africa_contribution_measure contains native_per_k=1000 and k_per_native=0.001.
Fixed-point gods_of_africa_contribution_voluntary contains infantry_capacity=1000, total source capacity BEFORE the exact 500-unit shipment, leaving 500 at the anchor.
Voluntary fuel also requires exactly the existing 500 amount and existing native fuel capacity and cooldown.
Grading retains its separate integer gods_of_africa_contribution_units category and denominators.
Fixed-point gods_of_africa_contribution_representation provides audit_quantum=0.001, ceiling=2147483.647 and sequence_preincrement_ceiling=2147482 for conservative source proof.
These values guard exact helper arithmetic and pending representation, not native prices, lifetime history caps or documented engine type limits.
Prices, existing fuel capacity, cooldowns, ordinary reinforcement reserves, demand bands, debt thresholds, normalization packages and grading/reward valuation remain in their respective owners.

| Kind | Native reading for both BEFORE and AFTER |
| --- | --- |
| Infantry | num_equipment@infantry_equipment |
| Support | num_equipment@support_equipment |
| Trucks | num_equipment@motorized_equipment |
| Artillery | num_equipment@artillery_equipment |
| Armor | Separate raw num_equipment snapshots for light, medium, heavy, modern, super-heavy and amphibious chassis, with separate directed differences |
| Aircraft | num_equipment@small_plane_airframe, the light-airframe fighter type that the payment sends, counting both legacy fighters and By Blood Alone light-airframe designs |
| Fuel | fuel_k, native thousands BEFORE/AFTER |
| Convoys | num_equipment@convoy_1, matching the actual branch |
| Trains | num_equipment@train_equipment |
| Manpower | manpower_k, native thousands BEFORE/AFTER |
| Emergency PP | political_power |

Native material writes gods_of_africa_paid_<kind>_k once and its genuinely qualified voluntary_paid_<kind>_k, campaign_paid_<kind>_k and emergency_paid_<kind>_k subsets under the same prefix.
A quantity can belong to several subsets but enters total once.
Kind 11 writes only gods_of_africa_emergency_paid_pp in raw PP and none of the forty material fields.
Armor sums bounded actual chassis differences, including a partial typed send.
It never adds the six full stockpiles.
An individual raw num_equipment stockpile getter has no verified wide-range route here.
There is no invented num_equipment_k, no silent full-stock clamp, and no claim that an externally reported high stock is proven readable.
Native has_equipment and the existing typed reserve owner supply affordability preflight.
Captured values outside the conservative accounting domain remain available with pending evidence, without asserting that they are natively unrepresentable.
Changing the actual aircraft branch to a different model/archetype requires extending the native reader first.

## Receipt identity, results and cleanup

Begin stores normal gods_of_africa_material_transfer_receipt_{id,kind,requested,source,receiver,source_id,receiver_id,host_generation,origin_id,contract_id,epoch,emit_kind,requested_native,day,source_before,receiver_before}.
The source/receiver fields are object references, with separate immutable IDs.
Ordinary receiver identity comes from the retained original demand host; voluntary receiver identity is the proven current host.
Permission and voluntary/emergency/campaign flags freeze before transfer.
Completion requires the same objects, IDs, origin/generation, ordinary contract tuple, reserved sequence and day.
Receipt epoch must still equal participant_authority_epoch and the captured/current host authority epoch, plus demand_authority_epoch for ordinary payments.
The host-session identity is receiver ID, origin ID, generation and authority epoch.
Unmeasured abandoned reservations retain material_transfer_gap_{id,host_id,origin_id,generation,epoch} once and never reuse the sequence.
Sequence exhaustion within the conservative source-proof domain blocks another reservation without resetting or capping history.
The same-day check is an extra guard, not permission to defer completion: both calls belong in the same synchronous effect.

The latest owner instruction requires an immutable begin-time sequence.
Begin reserves the next gods_of_africa_material_transfer_sequence, and an abandoned reservation leaves a gap rather than reusing an ID.
Only measured completion publishes pending/measured.
The recorder first checks exact precision and prospective room for EVERY total and qualified subset it will write.
Only then does it consume pending and advance gods_of_africa_last_consumed_material_transfer_id before those cumulative writes.
If accumulation cannot be supported exactly, representation_blocked and material_transaction_unresolved retain pending, measured amount, BEFORE/AFTER snapshots, directed native deltas, subset flags and reserved identity with last_consumed unchanged.
The same protection covers emergency PP.
Clear and abandon cannot discard these receipts.
No lifetime total is clamped, reset or waived, and no deferred recovery writer is invented.
Zero delivery consumes its reservation too.
Sequence reservations are not demands, fulfillments, deliveries or penalties.

The actual result within supported helper arithmetic is min(request, positive source debit); the receiver credit is bounded by the request and kept as Africa's own measured gain.
For fuel/manpower, compute both differences in k, bound common actual to request_k, then convert only that bounded actual and bounded raw output fields.
Fuel room stays in k and is compared with request_k.
Native directed delta outputs retain the original k differences, including excess, so full_match is evaluated before raw output bounds.
For armor each difference is retained independently and each addition is bounded by remaining request room, with an excess flag captured before bounding.
Normal outputs are gods_of_africa_material_transfer_actual_amount, gods_of_africa_material_transfer_source_debit, gods_of_africa_material_transfer_receiver_credit, gods_of_africa_material_transfer_output_kind and gods_of_africa_material_transfer_output_requested.
Additional normal source_debit_native and receiver_credit_native outputs use k for fuel/manpower and raw units for scalar equipment/PP.
Armor aggregates are bounded raw evidence, with complete per-chassis native differences retained while pending.
The source_debit/receiver_credit raw convenience outputs for fuel/manpower are bounded by request and cannot describe an entire excess debit.
Begin_ready and completion_consumed are freshly cleared/set COUNTRY flag outputs on each relevant call.
Repeated begin does not republish emission readiness while pending.
Repeated completion does not republish consumption even though durable last-result amounts remain available.

The full_match flag requires BOTH measured native deltas to equal the frozen helper request and no armor excess.
Full_match alone does not establish that the contract balance is closed.
The parent requires fresh completion_consumed, exact output kind/request binding, actual_amount, and its independently owned remaining-balance proof.
A raw actual_amount may be published while accounting is blocked, but must not be acted on as a consumed receipt.
Within supported exact accounting, short, unequal, zero or excess deltas record the measured common actual amount once, set mismatch, and set durable gods_of_africa_material_transaction_unresolved after consumption.
Unsupported accounting retains the measured pending evidence instead of consuming it.
Identity drift retains quarantined snapshots and does not synthesize zero delivery.
The parent must examine the fresh consumption result, actual delivery and both deltas before adjusting an owed balance.
Reduce an ordinary balance only by actual delivered quantity, retain the remainder, and do not repeat a debit for the delivered part.
Never fulfill a contract from a requested amount, quote, payment-success flag, begin-ready flag or stale result.
Unpaired debit/credit requires explicit owner recovery.
No helper automatically forgives, refunds, clears unresolved, repairs an obligation or closes a contract.

Fuel headroom_k is max_fuel_k minus fuel_k with negative room floored to zero, without scaling the complete room.
Supported requests beyond that room reject without changing the request.
The helper does not select a smaller payment.
For a fractional material request such as raw 0.5, the native quoted amount remains 0.5.
A primary native contract may still emit it after owned affordability proof, while exact material-ledger conversion is blocked pending type evidence.
Raw equipment snapshots/deltas and the actual raw 0.5 receipt remain pending without rounding to zero or one.
For a fractional fuel/manpower request, requested_native remains the raw request as an explicitly unusable conversion placeholder while precision_blocked is set.
No request_k, room sufficiency, raw conversion or full_match proof is claimed for that branch.
Completion retains both native k snapshots and, if their conservative arithmetic is supported, directed k deltas with a measured pending evidence envelope and no fabricated raw receipt_amount.
If the snapshots themselves exceed conservative precision or range, the pending envelope retains them with native_read_blocked and no computed amount.
The parent must resolve native type precision and exact representation before accounting or closing those transactions.
A missing raw amount is an evidence gap and never proof of zero delivery.
No PP cap is assumed: the observed receiver PP delta is authoritative.

Successful recording clears prepared/emission/measured/pending, subset flags and receipt work only.
Pending representation/native-read failures retain all work and snapshots.
Same-call primary type evidence is required before claiming fractional or very large exact accumulation, and the recovery design remains unresolved.
Durable sequences, quantities, last results and diagnostics remain.
Emergency snapshots clear after the contract's actual receipt is complete.
Regular event targets clear naturally with the originating chain and are never manually or globally cleared.
A failed pending transfer/return stays visible for owner recovery, or is explicitly abandoned with its evidence gap retained.
The clear helpers are internal cleanup primitives, not permission to discard an unexplained native debit.

## Emergency and campaign evidence

Issue-time emergency proof binds the original participant demand band to its real ordinary origin/generation/contract.
It requires the emergency band and actual current host debt above africa_measure.high, or above africa_measure.medium with needs-profile focus unlocked.
A cached need_emergency bit alone is insufficient.
Normal proof fields are gods_of_africa_contract_emergency_{host,host_id,generation,origin_id,contract_id,band}, with proof_frozen and qualified flags.
Begin and completion recheck the same host/contract and real current debt.
If need ends, material retains actual total but loses emergency subset.
PP retains actual raw delivery output but earns no emergency PP and is marked unresolved for parent review.
Recognition/territory PP, resource rights, ceremonial/procedural families, promises, quotes and host gifts provide no material credit.

Campaign status freezes before native debit.
The active current host must have an actual war, or an Event 012 Evolution III binding through gods_of_africa_contribution_campaign_active, gods_of_africa_contribution_campaign_generation and gods_of_africa_contribution_campaign_origin_id.
A global Evolution III flag alone grants no subset.
The existing activation owner lacked this explicit binding; parent must call the binding helper at actual activation and preserve/validate or retire it during an accepted host transition.
Do not backfill binding from a global flag alone.
Final/frozen hosts never emit receipts, and kind 11 never earns campaign material.

## Conduct, returned territory and paid acceptance

Conduct captures normal gods_of_africa_conduct_{host,host_id,host_generation,origin_id}, plus regular gods_of_africa_conduct_host and gods_of_africa_conduct_participant.
Only the participant's every_controlled_state and every_owned_state are iterated.
Both use exact Africa continent and core-of-explicit-captured-host checks.
Controlled states populate the unique occupied_core_state_ids array and observed_host_core_count.
Ownership alone refreshes owned_host_core_count and does not manufacture occupation.
War observation uses the active flag plus war_observation_host_id to deduplicate repeated review, distinguish a different actual host, and count a subsequent episode after peace.
No war observation writes treaty history.
Prior war/occupation/defiance remains durable; outstanding major cause waits for genuine accepted repair.
Current war/territory floors track actual current facts.
The floor is the maximum of existing war, territory, proven unresolved-treaty, defiant and recent-extreme constants.
A generic broken_treaty flag alone does not create a proven treaty cause.

Return begin stores normal gods_of_africa_core_return_{state,state_id,host,host_id,generation,origin_id,contract_id,day} and participant pre-owned/pre-controlled flags.
Completion requires actual Africa host-core status, same original host/contract, and both AFTER owner and controller equal to host.
The participant must actually have surrendered ownership or control from the before snapshot.
Each state enters returned_core_state_ids only once in lifetime history.
A returned flag, PP payment, unrelated border change or host conquest is not this receipt.
Failure keeps snapshots and grading_conduct_unresolved; parent must resolve that gap before final freeze.

Parent must refresh conduct BEFORE recording paid host acceptance.
Both current core caches must be zero and no current war may remain.
The resolver additionally requires actual paid/offer flags, matching unique accepted sequence, current origin/generation/day and HOST root, with no pending return or unresolved conduct.
It clears outstanding major/treaty causes only.
Recovery baseline, post-reconciliation counters, current streak and current defiance clearing remain owned by the accepted-reconciliation owner.
No lifetime counts, material, occupied/returned arrays, longest streak or prior flags are zeroed here.

## Agreements

Owned agreements and treaty breaches are implemented by the contract owner (`012_africa_gods_contract_effects.md`, section "Owned agreements and treaty breaches").
Conduct reads only `gods_of_africa_unresolved_treaty_break`, which is set exclusively by `gods_of_africa_record_treaty_breach`.

## Native send example

Voluntary infantry aid uses this guarded native send at its existing 500 cost and cooldown.
Begin independently requires an exact 500 shipment and 1000 total pre-debit native infantry capacity.
A stock of 999 fails, while 1000, 1499 and 1500 pass the same existing capacity contract.
Existing success/common-reserve/cooldown bookkeeping must use the fresh measured result.

```
set_temp_variable = { gods_of_africa_contribution_kind = constant:gods_of_africa_contribution_kind.infantry }
set_temp_variable = { gods_of_africa_contribution_native_emit_kind = constant:gods_of_africa_contribution_kind.infantry }
set_temp_variable = { gods_of_africa_contribution_requested = constant:gods_of_africa_transaction.voluntary_aid_equipment_amount }
set_temp_variable = { gods_of_africa_contribution_voluntary = constant:gods_of_africa_value.one }
gods_of_africa_begin_material_transfer = yes
if = {
	limit = { has_country_flag = gods_of_africa_material_transfer_begin_ready }
	send_equipment = {
		equipment = infantry_equipment
		amount = gods_of_africa_contribution_requested
		target = event_target:africa_host
	}
	gods_of_africa_complete_material_transfer = yes
}
```

Ordinary branches initialize voluntary to zero and kind from the actual selected native branch.
Wrap the contiguous typed armor send once, with both helpers capturing each of its six real chassis before and after.
Keep the typed owner actual branch receipt alongside these independent per-chassis differences.
Wrap each distinct real kind once if a future payment sends several kinds.
Fuel retains the actual owner debit/credit between capture calls with explicit room preflight.
Family 13 uses kind 11 around its existing actual PP debit/credit.

## Validation, presentation and future work

The [implementation handoff](../../docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_contribution_helpers_2026-10-03.md) records exact primary paths, line spans, revisions, executed fixture results and MCP gaps.
The previous 24 source fixtures are historical, unbounded evidence with mocked external owner predicates and the wrong reserve interpretation.
They are superseded for arithmetic and pricing by the bounded repair cases and are not complete native evidence.
Native transfer semantics (variant selection by `send_equipment`, getter range) remain live-game checks.
No icons, assets, sprites, GUI, player-facing strings or spreadsheet changes are required by these helper-only files.
The parent owns any shared documentation index link in chaosx_dynamic_effects.md.
Future extensions must retain typed native receipts and accepted owner proof rather than widening permission through quotes, generic history or periodic observers.

## State-return transfer shared by tribute and the final ultimatum

`gods_of_africa_transfer_current_core_return` runs in STATE scope on an already selected African host-core state.
Its regular `gods_of_africa_territory_payer` input identifies the actual returning participant, and `event_target:africa_host` identifies the receiving host.
It stores the state pointer on that participant, begins the exact return proof, transfers ownership and control through the native effect, completes a ready proof and clears the caller input.
It has no default target, price, timer or report and must be called only by the validated territory-payment or pending-ultimatum owner.

Ordinary territory returns retain their live contract identity.
A final-ultimatum return instead freezes its own pending ultimatum due-day and marks `gods_of_africa_core_return_ultimatum`, without inventing a demand contract.
Both sources freeze participant ID, current host pointer and ID, generation, origin, same-day transfer, state ID and pre-transfer ownership/control.
Completion requires the same source identity and actual host ownership and control after transfer.
The existing unique `gods_of_africa_returned_core_state_ids` array records a successful return only once.
Return-work cleanup clears the new participant and ultimatum fields alongside the prior snapshots.

Example inside a validated pending ultimatum participant:

```text
save_event_target_as = gods_of_africa_territory_payer
every_controlled_state = {
	limit = { is_on_continent = africa is_core_of = event_target:africa_host }
	gods_of_africa_transfer_current_core_return = yes
}
```

The native transfer and the restitution factor need the live checks in `takeover_status_2026-10-06.md` under the Event 012 plans folder.
