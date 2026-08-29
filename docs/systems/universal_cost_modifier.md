# Universal discounted-cost framework

This framework lets an owner apply active source ratios to an ordinary current payable cost while keeping displayed price, paid price, multi-resource receipts, delayed quotes, and actual-paid refunds on one contract.

The framework is neutral and does not own Event 026 lifecycle, purchase eligibility, cooldowns, reserve floors, AI weights, event targets, or player-facing event text.

## Public helper map

| Helper | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| `universal_cost_source_register` | any effect scope | source id, ratio, priority, eligibility mask | register result | upserts one global registry row |
| `universal_cost_source_clear` | any effect scope | source id | clear result | removes one source row and expires that source |
| `universal_cost_source_register_black_friday` | owner effect scope | optional ratio and mask | generic register result | registers source id 26 |
| `universal_cost_source_clear_black_friday` | owner effect scope | none | generic clear result | clears only source id 26 |
| `universal_cost_quote_integer` | payer country or owner-selected payer scope | ordinary cost, family mask, quantum | final/displayed/saved cost, composed ratio, source proof | temporary arithmetic only |
| `universal_cost_check_quote_affordable` | payer country | resource kind, final quote | affordability result | no debit |
| `universal_cost_pay_component` | payer country | native resource kind, positive amount | payment result | debits one native component |
| `universal_cost_record_transaction` | payer country | transaction/component ids, ordinary/quoted/actual paid amounts, resource kind, source id | record result | appends one component and totals |
| `universal_cost_refund_transaction` | payer country | transaction id | refund result and totals | credits each pending native component once |
| `universal_cost_mark_component_refunded` | payer country | transaction/component ids | acknowledgement result | records an owner-adapter refund after external credit |
| `universal_cost_settle_transaction` | payer country | transaction id | settle result | prevents later refund and retains proof |

The complete input, output, default, and side-effect contract is in [`chaosx_universal_cost_effects.md`](../../common/scripted_effects/chaosx_universal_cost_effects.md).

## Arithmetic contract

The shared basis is 10000.

The baseline sale ratio is 5000 and the Evolution I sale ratio is 2500.

The owner passes the ordinary current payable cost after all ordinary consumer modifiers have been evaluated.

Eligible sources are composed in ascending priority order by multiplying the remaining ratio and dividing by the 10000 basis after each source.

For a positive cost, the final quote is `ceil(ordinary * composed_ratio / 10000 / quantum) * quantum`.

A positive result is always at least one positive quantum.

Zero remains zero and negative/reward values bypass source discounts and are preserved unchanged.

Quantization happens after all eligible source ratios are composed, so a multi-source quote does not round each source separately.

The quote exposes one `universal_cost_quote_displayed_cost` value equal to the final amount the owner must pass to payment and receipt recording.

## Source registry and expiry

The registry stores source id, active ratio, priority, and eligibility mask in four aligned global arrays.

A zero eligibility mask means every family, while non-zero masks use the low thirty bits defined by `universal_cost_family` and are rejected above the shared thirty-bit bound.

Source id 26 is reserved for `black_friday` by the stable wrapper, but the generic register/clear effects do not depend on Event 026 files.

The framework has no safe generic way to interpolate a source id into a dynamic global-flag name.

The owner therefore registers a source when its activation snapshot is valid and calls the matching clear helper at expiry.

Clearing a source does not rewrite historical receipts, so a delayed payment must quote again and a refund continues to use its recorded actual-paid amount.

## Transaction lifecycle

The owner must call the quote for display, repeat the quote immediately before the purchase or installment, check affordability, and only then debit the resource.

A quote is not a lock and is not a payment receipt.

After every successful component debit, the owner calls `universal_cost_record_transaction` with the same logical transaction id, a unique component id, the ordinary cost, the final quote, and the actual paid amount.

Each component is independently recorded, but the shared transaction id gives the action one logical refund and settlement boundary.

`universal_cost_refund_transaction` uses only stored actual-paid amounts and marks each credited component before returning success.

An unsupported component returns a partial refund result and remains pending until the owner credits it through its own adapter and acknowledges it with `universal_cost_mark_component_refunded`.

The owner calls `universal_cost_settle_transaction` only after the action can no longer be cancelled or refunded.

The receipt arrays remain as duplicate-refund proof and are not deleted by the shared helpers.

## Adapter contract for Event 026

The Event 026 owner keeps `chaosx.nr26.1`, selection reservation, Friday activation, the 50/75 percent snapshot, active-day expiry, non-cost gates, cooldowns, AI policy, Event Log, Event Details, and achievement state in Event 026 files.

At activation it calls `universal_cost_source_register_black_friday` with the snapshot ratio and the chosen family mask.

At next-daily-tick expiry it calls `universal_cost_source_clear_black_friday` before accepting any later quote.

Every owner purchase surface supplies an ordinary current payable cost, a family mask, a positive rounding quantum, and a native or owner-specific payment provider.

Native providers use `universal_cost_check_quote_affordable`, `universal_cost_pay_component`, and `universal_cost_record_transaction`.

Factory commitments, technology, advisor, idea, operation, equipment-design, and other engine-inaccessible surfaces use the same quote and receipt contract but retain their owner-specific eligibility, payment, and refund adapters.

The owner must not use the shared wrapper as a hidden extra cost or bypass a pre-existing requirement.

## Constants and tuning table

| Category | Values | Purpose |
| --- | --- | --- |
| `universal_cost_framework` | basis 10000, baseline 5000, Evolution I 2500 | fixed-point sale arithmetic |
| `universal_cost_framework` | default quantum 1, invalid index -1 | positive minimum and array lookup safety |
| `universal_cost_framework` | source id 26, source priority 500 | stable Black Friday wrapper defaults |
| `universal_cost_family` | one bit per purchase family | source eligibility masks |
| `universal_cost_resource_kind` | nine native kinds plus owner-adapter ids | payment dispatch and receipt identity |
| `universal_cost_component_state` | not_refunded 0, refunded 1 | one-time component refund proof |

The source file is [`chaosx_universal_cost_constants.txt`](../../common/script_constants/chaosx_universal_cost_constants.txt).

## Existing logic migration

An owner migrates one purchase surface at a time by extracting its ordinary cost calculation into the adapter input, replacing any duplicated sale arithmetic with `universal_cost_quote_integer`, and preserving its existing trigger, cooldown, reserve, and AI blocks.

The owner then routes native debit through `universal_cost_pay_component` or supplies a documented owner payment provider for an inaccessible surface.

The owner records each paid component under one transaction id and replaces any refund-from-requested-cost logic with `universal_cost_refund_transaction` or the explicit external-refund acknowledgement.

No shared helper should be introduced for a surface whose ordinary cost cannot be read or whose native debit cannot be proven.

## Engine limits and validation

The engine exposes no generic scripted value for every purchase surface's current modified price, so ordinary cost providers remain explicit adapters.

The engine does not accept an arbitrary dynamic resource token as an effect key, so native payment branches are fixed and unsupported resource kinds are not silently approximated.

The engine does not provide a transactional rollback across unrelated effects, so the owner must debit only after complete affordability validation and record actual paid amounts after successful payment.

The engine's ordinary array API stores numeric values, so stable numeric source/family/resource ids are used instead of inventing token-keyed maps.

The required arithmetic evidence set is BF-R01 through BF-R13 and BF-C01 through BF-C06 from the Event 026 specification.

The required transaction evidence set is BF-X01 through BF-X14, including delayed quote expiry, recomputation, multi-component recording, actual-paid refunds, second-refund no-op, and payer isolation.

No icon, sprite, GFX, localisation, GUI, event target, or spreadsheet asset is required by this framework itself.
