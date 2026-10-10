# Private Event016 Paleogenetics staffing API

Implemented bounded core, 2026-10-09; parent integration review and native evidence remain pending.
Authority: docs/plans/016_brilliant_scientist_plans/016_private_paleogenetics_staff_integration_2026-10-09.md and the accepted private Deployment plan.
Paired dependency: a048109ceef3be2336302dd563f998b4ced66469.
No paired/parent source, assets, models, unit packages, index or Git mutation occurred.

## Contract and registered role

One team holds 250 actual reserve personnel: 100 handlers and 150 veterinary staff for one frozen paid reserve/hatchery pair.
Training consumes nominal 100 concrete support_equipment_1, commits nativeCIC2 and takes60 days.
Only support is quoted/recorded as a purchase: exact UNIVERSAL quote, mask32, resource kind11, existing support component6.
Personnel is fixed returnable allocation using native kind3, outside discount quotes, purchase subtotal and achievement proof.
Native CIC/timer/removal remain parent-owned.
Qualification requires current provider, neutral Paleo tech, full paid pair, current ownership/control and non-damaged capacity at least recorded post-levels, trained actual held250 and settled fee.
Ordinary Prototype production and KRG history remain independent.

The parent accepts Personnel logical family2097152 because the service trains and allocates people.
Support is its declared primary component, primary_component basis1, member1.
This is not an Equipment classification inferred from support currency.
The shared binder and ordinary proof allowlist accept this explicit tuple.
Parent owns registry rows, literal descriptor setter and achievement registration/confirmation/withdrawal.
The game does not query the Markdown registry; the reviewed literal setter is the source contract.

Parent supplies these four caller-owned inputs before full admission and native begin:

| Input | Required value |
|---|---|
| paleo_staff_owner_family | constant:universal_cost_family.personnel |
| paleo_staff_owner_primary_component | constant:black_friday_event.owner_component_support_equipment |
| paleo_staff_owner_cost_basis | constant:universal_cost_achievement_basis.primary_component |
| paleo_staff_owner_primary_member | one |

Begin rejects a missing/wrong tuple, freezes it and consumes all four inputs tozero on every exit.
There is no metadata-zero fallback, Portal action identity or new global family/action ID.
The literal staff training_receipt flag binds the private action to its actor/family/serial/pair.

## APIs and return ownership

Helper prefix: brilliant_scientist_mengele_paleogenetics_staff_.
Persistent prefix: mengele_event016_paleogenetics_staff_.
All APIs are COUNTRY; explicit stored STATE queries use var: pointers and immediate PREV as payer, independent of an unrelated outer ROOT.

| Suffix | Inputs / result | Purpose and side effects |
|---|---|---|
| owner_role_is_ready | Four descriptor inputs | Pure exact registered tuple check |
| quote | Caller owns paleo_staff_quote_support/source/source_count/valid | Pure fresh support quote; no currency or source mutation |
| can_pay_support | Already fresh quote support/valid | Inclusive concrete-model affordability and UI colour predicate |
| can_allocate_personnel | Native reserve query | Inclusive250-person check, no discount |
| serial_is_valid | Saved serial; missing defaults0 | Pure non-negative integral generation |
| pair_is_available | Existing paired APIs, provider/neutral entitlement | Pure current completed, owned/controlled, undamaged pair |
| requirements_met | Descriptor/pair, no live receipt/debt/busy | Pure one-team admission, no payment/CIC |
| can_pay_direct | Owns private quote scratch | One fresh quote plus inclusive fee/personnel checks |
| can_start | Full selection | Requirements/direct affordability and two free nativeCIC |
| receipt_is_current | Original actor/action/family/serial/pair/amounts | Pure identity, nonnegative amounts, debit and held/refund conservation |
| current_pair_is_valid | Frozen pair/generation | Pure exact pair match and current owned/control/non-damaged levels |
| support_record_is_valid | Stored shared row | Pure transaction/component/model/actual/source identity and bounds |
| ledger_is_recorded/settled/refunded | Shared receipt | Pure one-component transaction state checks |
| is_qualified | Paid current pair, trained held250, settled fee | Pure team qualification; no grant |
| can_recover_training | Funded full team, inactive timer, no release/fault/busy | Pure settlement-only readiness |
| release_is_pending | Retained release flag | Display only, not authorization to retry |
| can_recover_release | Original actor, conserved owed debt, no busy/ambiguous debit | Pure remaining-credit/final-ack readiness |
| begin_training | Four role inputs; caller-owned paleo_staff_native_entry=1 and paleo_staff_begin_result | Marker/tuple consumed; frozen authority before debit; measured funding |
| finish_training | Matching funded native-expiry receipt; paleo_staff_finish_result | Full training commit, fee settlement, current qualification/history |
| recover_training | Ready pending settlement; finish result | Settlement-only retry; no new payment/time/CIC |
| cancel_training | Original receipt; paleo_staff_cancel_result | Retires timer/qualification; returns actual workforce and unfinished fee |
| demobilize | Original receipt; paleo_staff_demobilize_result | Returns held personnel; consumed training fee stays consumed |
| cleanup | Original receipt; paleo_staff_cleanup_result | Same bounded release after provider/site loss; parent owns native removal |
| recover_release | Ready owed receipt; paleo_staff_recovery_result | Credits only remaining measured debt and finalizes shared acknowledgment |
| acknowledge_debit/acknowledge_crew_credit/acknowledge_support_credit | Verified positive matching evidence; paleo_staff_ack_result | Ledger acknowledgment only; never changes native resources |

Internal effects: record_support_fee, request_release, credit_crew_remainder, credit_support_remainder and finalize_release.
The record/output/credit helpers retain their receipt/busy/phase guards; bare literal reuse cannot grant an unowned team or resource.
Results: zero is refusal/no-op; one success; two retained partial debt/settlement; acknowledgment rejection is three.
Every consumed temporary output must exist in its outer caller BEFORE calling the helper.
Each consuming helper creates its child output storage before nested calls.
Helper-only temporary storage can disappear on return; normal scoped receipts persist.
Temporary variables are unscoped and must not use ROOT/PREV prefixes.

## Durable fields and phases

Identity: actor, family(existing10), serial, matching receipt_serial, transaction, reserve, hatchery, deployment_serial, reserve_level, hatchery_level.
Price: support_final/source/source_count, support_actual, record_index and frozen owner_family/owner_primary_component/owner_cost_basis/owner_primary_member.
Workforce: crew_allocated, crew_held, crew_released.
Fee obligation: support_due, support_refunded.
Native observations: crew_before/after and crew_credit_before are thousands; support_before/after are concrete equipment units.
Delayed debit: unverified_debit_kind, crew_debit_ack_amount, support_debit_ack_amount.
Successful service: handlers, veterinary_staff, last_completed_serial.
Per-role crew/support release: credit_nonce, credit_before, credit_requested, credit_observed.

Flags: receipt_open, training_receipt, timer_active, busy, funded, trained, fee_consumed, support_recorded, release_pending, closed, training_completed, debit_unverified, crew_credit_inflight, support_credit_inflight, crew_debit_acknowledged, support_debit_acknowledged.
training_completed is durable history; trained/current role counts are disabled at release.
Live held debt remains even when qualification is suspended.
Retraining requires acknowledged receipt closure and no held/refund/in-flight obligation.

Begin performs a fresh quote and direct-only preflight after source-authorized native admission.
It validates positive allocator output, freezes actor/pair/tuple/amounts and opens pending/busy authority BEFORE debit.
Crew uses shared native pay kind3 without a purchase quote/record; only the bounded manpower_k difference is converted from thousands to persons, avoiding an expanded total-manpower scalar.
Support uses shared native pay kind11 and exact concrete stockpile delta.
Only full250 allocation, exact quoted support debit and real successful shared record fund training.
Partial positive payment retains actual owed compensation and never qualifies staff.
Ambiguous zero/negative debit is blocked pending verified original-debit evidence; no blind debit repeat or team top-up.

Native expiry must come from the reviewed parent source.
Full training commits material consumption before settlement, retaining proof for settlement-only retry if needed.
Qualified/history state is published only after settled fee and full actual held team.
The core does not prove timer ordering or immutable same-action callback generation.

Site/provider/tech loss suspends qualification without inventing deaths.
Release does not require the provider to remain valid.
Qualification/timer retire before native credits, preventing modeled reentry from reopening funding.
Only remaining actual personnel/material debt is credited through shared native credit.
Each credit first publishes its matching attempt nonce/request/before balance.
Positive bounded observed credit reduces debt once.
Zero/negative/oversized readback remains in flight; ordinary recovery cannot blindly repeat that credit.
Recorded support must still be refundable before a native credit.
Full observed support restitution is acknowledged through mark_component_refunded before final refund_transaction.
Final refund is invoked only after the component is confirmed refunded, so it cannot issue another full native refund.
Shared corruption retains an unresolved receipt rather than inventing closure.
Completed training never returns consumed support; crew release closes any remaining shared settlement proof.
After exact acknowledged closure, retraining uses a new generation and owner transaction.

## Explicit positive acknowledgment boundary

Caller-owned acknowledgment inputs are consumed tozero:
paleo_staff_ack_verified, paleo_staff_ack_actor, paleo_staff_ack_serial, paleo_staff_ack_nonce, paleo_staff_ack_amount.
Debit also consumes paleo_staff_ack_resource_kind.

Verified=1 is an attestation from a reviewed owner/native evidence path, not a gameplay button guessing a later balance change.
Credit requires original in-flight role, actor, generation and attempt nonce; amount must be positive and within original request/current debt.
Debit requires original ambiguous kind3 or11, receipt-generation nonce and bounded original quantity.
Acknowledgment updates accounting only; it never debits or credits resources.
Wrong actor/serial/nonce, zero, oversized or unverified input is rejected.
Do not attribute unrelated later manpower/stockpile changes to an old operation.
When matching evidence is unavailable, retain blocked debt.
No scheduler, world hook or periodic grant is added.

## Parent wiring and evidence

Parent owns native decisions/CIC/timers/removal, four-input descriptor setter, material/escrow/CIC registry dispositions, names/cost/debt/damage text, cleanup hooks, CXT observations, actual Black Friday claim chain, audits and commit.
Use existing family/team sprites; no assets were inspected/created.
Do not make ordinary production or neutral Prototype entitlement depend on private staffing.
Core cleanup consumes/acknowledges its receipt first; parent may remove the native decision afterward.
The parent adds the modifier-free staffing carrier and matching idempotent CXT readiness setup.
Its bounded startup and CXT-only fallback register the token without granting workforce or resources, and the player-triggered ownership probe observes staffing state.

Run retained CommonJS driver:
~~~
node .tools/tests/event016_paleogenetics_staff.test.js
~~~
57 actual-source cases pass with the real exact quote/pay/credit/record/refund/settle/ack helpers and allocator.
The checked-in fixed-point/lifetime interpreter is reused; no Temp dependency or shared-API no-op.
Only native primitives, strict provider and the reviewed paired API boundary are fixtures.
Cases cover prices/boundaries/source expiry, faults/partial release/positive acknowledgment, country/provider/site loss, corruption, retraining, reentry, caller-temporary lifetimes and Personnel/support role metadata.
Source identities/cases/stubs are retained in core_results.json; MCP receipts in core_validation.json and the handoff.

Whole-file validation has zero unresolved commands but partial native argument/root-scope coverage.
Native manpower observation, clipping/delayed recount, object destruction/persistence, effect/ack interruption, concrete producer/design provenance, save/reload and stale same-action callbacks remain user-owned proof.
The marker proves source-bound entry, not native reservation order.
The Personnel binder/allowlist compatibility is source evidence, not final achievement-credit acceptance.
No simplification to actual250-person allocation; no full private-payoff/Event016 completion claim.

## Parent native integration

The native consumer adapters are `begin_native`, `finish_native`, `cancel_native`, `demobilize_native` and `cleanup_native` under the existing helper prefix.
The pure `bind_owner_role` trigger sets the literal accepted four-field Personnel/support descriptor in caller-owned temporary storage.
Native full admission uses `native_start_is_available`, direct payment display uses `native_payment_is_available`, and the literal complete effect alone sets the native-entry marker.
Actual support claims use the recorded ordinary component cost and frozen sale sequence, with full settlement required before shared confirmation.
Consumed training fees remain consumed and earned credit remains intact after workforce demobilization.
Cleanup and demobilization release the current actor's receipt before native decision removal.
Recovery availability rejects completed training and unresolved credit attempts even when all displayed debt is zero.

The parent provides native human operations navigation with AI bypass, identity-only debt visibility and strict actor/conservation-based action gates.
The existing provider cleanup hook calls the bounded staff cleanup adapter, and the existing CXT ownership probe calls the read-only staff observer.
The current implementation report is `docs/plans/016_brilliant_scientist_plans/016_private_paleogenetics_staff_integration_2026-10-09.md`.
