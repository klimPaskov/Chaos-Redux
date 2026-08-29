# Universal cost framework handoff

## Status

The reusable universal cost source, quote, quantization, native payment, transaction receipt, and refund layer is implemented in dedicated framework files.

Event 026 lifecycle, purchase-owner call sites, event/log/UI files, the cost-surface registry, and the XLSX were intentionally not edited because they are outside this subtask boundary.

The parent must wire the public adapter contract before claiming Event 026 completion.

## Changed files and identifiers

| File | Evidence | Contents |
| --- | --- | --- |
| [`common/script_constants/chaosx_universal_cost_constants.txt`](../../../common/script_constants/chaosx_universal_cost_constants.txt) | lines 10-109 | Shared basis, ratios, source/result states, cost-family mask bits, resource-kind ids, and component refund state. |
| [`common/scripted_effects/chaosx_universal_cost_effects.txt`](../../../common/scripted_effects/chaosx_universal_cost_effects.txt) | lines 30-134, 141-247, 251-542, 544-830, 835-1379 | Source registry, Black Friday wrappers, deterministic source composition, upward quantization, affordability, nine native payment/credit branches, and payer-scoped multi-component transaction ledger. |
| [`common/scripted_triggers/chaosx_universal_cost_triggers.txt`](../../../common/scripted_triggers/chaosx_universal_cost_triggers.txt) | lines 13-202 | Active-source, native-resource, affordability, and receipt-presence predicates. |
| [`common/scripted_effects/chaosx_universal_cost_effects.md`](../../../common/scripted_effects/chaosx_universal_cost_effects.md) | sections at lines 9-246 | Complete effect API contract, storage, defaults, side effects, and engine boundary. |
| [`common/scripted_triggers/chaosx_universal_cost_triggers.md`](../../../common/scripted_triggers/chaosx_universal_cost_triggers.md) | sections at lines 5-49 | Trigger inputs, scopes, results, and expiry/adapter limitations. |
| [`docs/systems/universal_cost_modifier.md`](../../../systems/universal_cost_modifier.md) | sections at lines 7-125 | Architecture, migration order, Event 026 adapter contract, tuning table, and validation matrix. |
| [`common/scripted_effects/chaosx_dynamic_effects.md`](../../../common/scripted_effects/chaosx_dynamic_effects.md) | line 268 | Shared-helper registry cross-reference only. |

The stable owner-facing names requested by the parent are present: `universal_cost_source_register_black_friday`, `universal_cost_source_clear_black_friday`, `universal_cost_quote_integer`, `universal_cost_record_transaction`, and `universal_cost_refund_transaction`.

## Helper map and adapter call sites

| Helper group | Scope | Inputs and outputs | Side effects | Intended call site |
| --- | --- | --- | --- | --- |
| `universal_cost_source_register`, `universal_cost_source_clear` | Any effect scope with global write access | Source id, ratio, priority, family mask; temporary result code | Upsert or remove one row from four aligned global arrays | Event/source owner activation and expiry. |
| `universal_cost_source_register_black_friday`, `universal_cost_source_clear_black_friday` | Event owner scope | Optional ratio/mask for registration; no inputs for clear; generic result variables | Registers or removes source id 26 only | Parent Event 026 activation snapshot and next-tick expiry. No call site was changed here. |
| `universal_cost_source_matches_quote_family` | Any effect scope | Source mask and quote family mask; temporary match flag | Temporary bit-mask arithmetic only | Internal quote traversal. |
| `universal_cost_round_up_to_quantum` | Any effect scope | Amount and optional positive quantum; quantized result and units | Temporary arithmetic only | Internal quote path or owner tests. |
| `universal_cost_quote_integer` | Payer country or owner-selected payer scope | Ordinary current payable cost, family mask, quantum; final/displayed/saved cost, composed ratio, source count, primary source, validity | Temporary priority/index arrays; registry and payer state are unchanged | Every owner displays a price and repeats the quote immediately before payment. |
| `universal_cost_check_quote_affordable` | Payer country | Native resource kind and final quote; affordability result | Read-only native affordability check | Owner preflight after the final quote. |
| `universal_cost_pay_component`, `universal_cost_credit_component` | Payer country | Native resource kind and positive amount; payment/credit result | Debits or credits a fixed native branch only after/against the documented checks | Owner payment and shared native refund paths. |
| `universal_cost_record_transaction` | Payer country | Logical transaction id, unique component id, resource kind/id, ordinary/quoted/actual-paid costs, source id, optional primary marker | Appends a component and updates aligned totals | Owner calls once after each successful component debit. |
| `universal_cost_refund_transaction` | Payer country | Logical transaction id; result, native refund total, unhandled total | Credits stored actual-paid amounts once and transitions the receipt to refunded or partial | Owner failure/cancellation refund path. |
| `universal_cost_mark_component_refunded` | Payer country | Transaction and component ids; acknowledgement result | Records an exact external adapter refund using stored actual-paid amount | Owner factory/technology/advisor/idea/operation/design/custom refund path. |
| `universal_cost_settle_transaction` | Payer country | Logical transaction id; settle result | Transitions recorded receipt to settled and retains proof arrays | Owner after the cancellation/refund window closes. |

No Event 026 owner call sites were changed. The framework is deliberately disjoint from `events/026_black_friday.txt`, `common/scripted_effects/026_black_friday_effects.txt`, Event Log/Event Details/UI files, owner purchase files, and the workbook.

## Contract details

The shared fixed-point basis is 10000, with baseline payment ratio 5000 and Evolution I payment ratio 2500.

The parent supplies the ordinary current payable cost after the owning surface's ordinary modifiers, requirements, route rules, and reserve checks have been evaluated.

The quote composes eligible sources in ascending priority order and quantizes the positive result once with `ceil(amount / quantum) * quantum`; zero and negative values remain unchanged, and a positive result is at least one positive quantum.

The displayed output is `universal_cost_quote_displayed_cost`, which is set equal to `universal_cost_quote_final_cost` and must be passed to the payment adapter and receipt record.

Each logical transaction can contain multiple resource components, each with its own ordinary, quoted, actual-paid, resource, source, and refund state.

`universal_cost_record_transaction` rejects a component when actual paid differs from the quote, so display/payment/receipt agreement is explicit rather than inferred.

Refunds use only the stored actual-paid amount and never reconstruct a refund from ordinary cost or a later source ratio.

Rows are logically closed by `transaction_state_refunded` or `transaction_state_settled` and retained as duplicate-refund proof; a second refund is a no-op.

## Constants and tuning plan

| Category | Stable values | Use |
| --- | --- | --- |
| `universal_cost_framework` | `basis = 10000`, `baseline_sale_ratio = 5000`, `evolution_i_sale_ratio = 2500` | Ratio arithmetic. |
| `universal_cost_framework` | `default_rounding_quantum = 1`, `invalid_index = -1`, `negative_one = -1` | Integer floor, lookup, and debit arithmetic. |
| `universal_cost_framework` | Black Friday source id `26`, default priority `500`, default ratio `5000` | Stable named wrapper defaults. |
| `universal_cost_family` | Numeric mask bits for government, military, intelligence, equipment, factory, technology, advisor, idea, operation, and design families | Source eligibility and achievement/owner registry alignment. |
| `universal_cost_resource_kind` | Native ids `1-9`; owner-adapter ids `100-107` and `199` | Payment dispatch and receipt identity. |
| `universal_cost_component_state` | `not_refunded = 0`, `refunded = 1` | Per-component duplicate-refund proof. |

The pre-existing parent file `common/script_constants/026_black_friday_constants.txt` was not changed or made a dependency of the framework; the owner can pass its snapshot ratio into `universal_cost_source_register_black_friday`.

## Event target and cleanup plan

The framework uses no event targets and adds no daily or weekly all-country iteration.

The source registry is global and active while source id 26 has a row; the Event 026 owner must register after its activation snapshot and call `universal_cost_source_clear_black_friday` on the next daily expiry tick.

Clearing source id 26 removes only its aligned registry row and leaves other source rows and historical transaction receipts untouched.

Transaction and component arrays are payer-country scoped, so simultaneous country quotes and refunds do not share global scratch state.

The Event 026 owner retains responsibility for its existing event targets, reservation cleanup, disable/terminal cleanup, and status state.

## Migration plan

1. Add one coverage row per purchase/commitment surface with a stable logical transaction id, component id, family, payer scope, resource kind, quantum, and refund policy.
2. Preserve each surface's existing eligibility, DLC, route, reserve, cooldown, AI, and ordinary modifier logic while exposing its ordinary current payable cost to the adapter.
3. Display the quote, recalculate it at confirmation/payment time, and run affordability against that same final quote.
4. Debit all components only after complete affordability succeeds, then record each successful component under one logical transaction id with the exact actual-paid amount.
5. Use shared native refund for the nine supported kinds, or perform the owner-specific external refund before `universal_cost_mark_component_refunded` for inaccessible kinds.
6. Settle only after cancellation/refund is no longer allowed, and keep the source clear path independent from receipt history.

## Risks, unsupported fields, and blockers

The engine exposes no generic scripted accessor for every purchase surface's current modified price, so ordinary cost providers remain owner adapters.

The engine does not accept an arbitrary dynamic resource token as an effect key, so shared payment is fixed to political power, command power, manpower, fuel, infantry equipment, support equipment, motorized equipment 1, train equipment, and convoy 1.

Factory/dockyard commitments, technology, advisors, ideas, operations, equipment designs, and custom currencies are recordable but require owner payment, affordability, and refund adapters.

The engine does not provide a transactional rollback spanning unrelated native effects; owners must validate all components before debit and record only successful debits.

The engine does not provide a safe generic dynamic global-flag name, so source expiry is explicit through the clear helper rather than an invented dynamic flag.

`universal_cost_mark_component_refunded` cannot verify an external credit effect; its contract requires the owner adapter to credit exactly the stored actual-paid value first.

No current owner call sites, full cost-surface registry, Event 026 MCP evidence, AI comparison, or live consumer validation is included in this handoff.

The exact MCP blocker is that the current exposed tool catalog has no callable `hoi4.event_inspect`, `hoi4.probability_inspect`, `hoi4.gui_inspect`, or any `mcp__hoi4__...` route; only Blender HOI4 tools matched the read-only catalog query.

This framework adds no AI weights or probability-bearing helpers, so a probability audit is not applicable to these files; the unavailable probability route is nevertheless recorded rather than substituted with source-only evidence.

## Evidence and checks

The complete Event 026 specification directory was read, with the reusable architecture contract in `026_black_friday_spec_part_3_reusable_cost_modifier_architecture.md` lines 79-139 and 197-220, the rounding/composition/transaction acceptance matrix in `026_black_friday_spec_part_8_acceptance_scenarios.md` lines 44-90, and the shared-framework boundary in `026_black_friday_spec_part_9_implementation_crosswalk.md` lines 60-80.

The required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding were consulted.

The required vanilla documentation was consulted, including `documentation/script_concept_documentation.md`, `documentation/script_math_functions.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, and `common/script_constants/documentation.md`.

Existing Chaos Redux dynamic effects and the paid transaction precedent in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` were inspected before introducing the dedicated files.

The final targeted checks reported zero brace-depth errors in all three script files, unique top-level identifiers in effects/triggers/constants, no literal unsupported `<=` or `>=` operators, and presence of all requested public helper names and matching markdown docs.

An offline arithmetic audit matched BF-R01 through BF-R10, BF-C01/BF-C02, and BF-R11 through BF-R13, including zero preservation, minimum-one rounding, 50/75 percent results, and the 125-to-63 upward round.

No game launch or live consumer test was performed, consistent with repository instructions.

The initial scoped commit attempt was delayed by an existing `.git/index.lock` held while other git add processes were active in this shared repository; the lock was left untouched, and the framework implementation plus the original handoff were committed as `e965edfa9` after it cleared.

The one-line lock-note correction was subsequently carried by concurrent shared-workspace commit `6f12512e9`; no framework source file changed in that concurrent commit.

## Simplifications and omissions

No gameplay, UI, event, owner-surface, spreadsheet, AI, or asset fallback was introduced.

The only omissions are the explicitly documented engine boundaries and the parent-owned integration and MCP evidence listed above.
