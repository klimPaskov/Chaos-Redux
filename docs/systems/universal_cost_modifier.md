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
| `universal_cost_rebuild_custom_quote_ratio_cache` | owner effect scope | active source registry | existing readiness marker | removes retired scalar cache rows, preserves exact source registry |
| `universal_cost_quote_integer` | payer country or owner-selected object scope | ordinary cost, family mask, quantum | exact final/displayed/saved cost, validity, source proof | temporary limb arithmetic only |
| `universal_cost_quote_exact` | read-only trigger in the same selected scope | identical quote inputs and live source registry | identical quote outputs | temporary limb arithmetic only; shared by both frontends |
| `universal_cost_check_quote_affordable` | payer country | resource kind, final quote | affordability result | no debit |
| `universal_cost_pay_component` | payer country | native resource kind, positive amount | payment result | debits one native component |
| `universal_cost_record_transaction` | payer country | transaction/component ids, ordinary/quoted/actual paid amounts, resource kind, source id | record result | appends one component and totals |
| `universal_cost_refund_transaction` | payer country | transaction id | refund result and totals | credits each pending native component once |
| `universal_cost_mark_component_refunded` | payer country | transaction/component ids | acknowledgement result | records an owner-adapter refund after external credit |
| `universal_cost_settle_transaction` | payer country | transaction id | settle result | prevents later refund and retains proof |

The complete input, output, default, and side-effect contract is in [`chaosx_universal_cost_effects.md`](../../common/scripted_effects/chaosx_universal_cost_effects.md).

Every caller must initialize each temporary scalar and array output that it will consume before invoking the scripted helper.
This obligation applies at each nested return boundary, including producers called from `if.limit` and `text.trigger`.
Temporary storage created only inside a helper may disappear on return, while caller-created storage retains its modifications.
The actual-source tests use conservative helper-frame cleanup and separate temporary storage from persistent payer variables and receipt arrays.
Public output contracts and negative bare-API controls are recorded in the exact implementation handoff.
Those source tests do not establish that every production owner has fulfilled the output contract, which remains part of the final call-site registry audit.

## Arithmetic contract

The shared basis is 10000, with baseline ratio 5000 and Evolution I ratio 2500.
The owner passes the ordinary current payable cost after its ordinary modifiers.

Both effect and read-only trigger quotes use `universal_cost_quote_exact` in [chaosx_universal_cost_exact_triggers.txt](../../common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt).
Represented cost, quantum, and source ratios have five fractional digits.
The helper extracts their integer ticks into radix-1000 limbs without constructing an oversized scalar tick value.

For positive ordinary cost C, positive quantum Q, and N eligible source ratios, the payable amount is exactly `ceil(Cticks * product(Rticks) / (Qticks * 1000000000^N)) * Qticks / 100000`.
Identity source factors cancel exactly while retaining their source proof.
All other source products retain every digit until the final ceiling.
The price is independent of source registration order.
The primary source is resolved separately by minimum priority and stable registry-order ties.

Positive quotes with eligible sources produce at least one quantum.
No eligible source preserves the ordinary amount without rounding.
Zero and negative/reward amounts are preserved.
A caller receives the same final and displayed amount and a non-negative saved amount.

The divisor may be any represented positive quantum, including multi-limb ticks.
No integer-ratio restriction, one/.01-only quantum fallback, ordinary-cost threshold, fixed source-count cap, per-source rounding, nearest-integer ceiling approximation, or forced epsilon is introduced.
Arithmetic representation constants are separate from balance tuning.
The live aligned source registry is the exact source cache for every accepted family mask, including combinations and noncanonical families; no twelve-family table governs quotation.

A malformed aligned registry or a mathematical price beyond the represented positive scalar envelope yields `universal_cost_quote_valid = 0`.
Such a quote is not payable.
The shared quoted-affordability helper rejects it, and owner-specific payment providers must likewise check validity.
No output amount is saturated, approximated, or substituted as an accepted quote.
The mathematical integer quantum count may exceed one scalar even when the price fits; the standalone quantizer retains exact unit limbs and explicitly marks its scalar unit count unavailable.

The retired scalar `universal_cost_quote_composed_ratio` output is basis without participating sources and zero meaning unavailable with participating sources.
It is never used for pricing or validity.
The effect/cache/central-trigger consumers that previously used it are migrated together.

[Exact helper documentation](../../common/scripted_triggers/chaosx_universal_cost_exact_triggers.md) records scalar extraction, bounded multiplication, long division, sticky-fraction ceiling, supported trigger iteration, and helper contracts.
[Implementation evidence](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_exact_quote_implementation.md) records tests of the actual parsed helper source against a direct BigInt rational oracle.
[The preceding audit](../plans/026_black_friday_plans/subagent_handoffs/2026-10-03_quantization_audit.md) remains historical evidence for the scalar failures and the accepted minimum guard.

The offline Data structures reference documents five fractional digits and roughly signed-32-bit whole values, independently of deprecated manpower reader limits.
Installed documentation confirms fixed-point operations, temporary arrays, array iteration in triggers, and effect limits containing temporary arithmetic.
These references and source-semantic tests do not establish native engine execution, consumer performance, or native payment universality.
Required MCP queries returned no usable inspection artifacts in this tranche; detailed request and retry evidence is in the handoff.

The bounded Event 026 owner adapters retain their own current price providers, eligibility, payment, receipts, and UI consumers.
No owner inventory, lifecycle, achievement, catalog, asset, or AI implementation is changed by this arithmetic repair.
Owner coverage and native display/debit acceptance remain the parent's separate responsibility.

## Source registry and expiry

The registry stores source id, exact represented ratio, priority, and eligibility mask in four aligned global arrays.
Those rows are the authoritative exact source cache for both quote frontends.
The existing Event 026 readiness marker persists, while register/clear publication removes the twelve retired scalar cache variables.
Source lookup and quotation iterate caller-scope tokens rather than effect loops with a fixed iteration ceiling.

A zero source eligibility mask means every positive quote family mask.
Non-zero source masks retain the existing low-thirty-bit registration contract.
The exact matcher extracts each low bit with modulo, subtracts it, and divides the remaining even integer by two.
No fractional division residue can masquerade as a higher set bit.

Source id 26 is reserved for `black_friday` by the stable wrapper, but the generic register/clear effects do not depend on Event 026 files.

Event 026 currently registers this source from its activation snapshot and clears only this source at next-daily-tick expiry.

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

At activation it calls `universal_cost_source_register_black_friday` with the snapshot ratio and the all-family mask.

At next-daily-tick expiry it calls `universal_cost_source_clear_black_friday` before accepting any later quote.

Every owner purchase surface supplies an ordinary current payable cost, a family mask, a positive rounding quantum, and a native or owner-specific payment provider.

Native providers use `universal_cost_check_quote_affordable`, `universal_cost_pay_component`, and `universal_cost_record_transaction` when the owner exposes a scripted transaction. Flat engine-native cost fields such as MIO assignment and policy costs do not consume a relative factor and remain explicitly blocked in the cost-surface registry.

Factory commitments, custom technology/advisor/idea/operation payments, flat MIO and leader costs, and other engine-inaccessible surfaces remain explicitly classified in the cost-surface registry until an exact adapter or complete static variant set exists. Native equipment, module, and unit design cost-factor surfaces and factor-based commander costs are covered by the installed country/unit-leader dynamic modifiers listed in the Event 26 inventories.

The current source-level owner tranche covers the five Communist-spread logical actions, seventeen reachable Fury decisions, the Japan chemical campaign attack, the biological medical-capacity expansion, the CBRN civilian-shelter movement, the two Japan biological campaign agents, four Germany Mengele command-power actions, and the D'Rhondan landing reserve. Each logical action assigns one registry-defined primary family even when its receipt has multiple components. Custom chemical cylinders, biological payloads, and the alien reserve use explicit owner payment and refund acknowledgements. This is bounded source coverage, not universal owner coverage or live consumer proof.

The owner must not use the shared wrapper as a hidden extra cost or bypass a pre-existing requirement.

The current Event 026 lifecycle call site is `common/scripted_effects/026_black_friday_effects.txt`, where activation registers the snapshot after setting global sale state and expiry clears the source before removing sale modifiers. Bounded owner adapters call the shared quote, affordability, native payment, receipt, settlement, and achievement-primary-family helpers from their owner paths, with custom-resource components using the documented external refund acknowledgement contract.

The current native source coverage is declared by `common/ideas/026_black_friday_ideas.txt` for verified factor-based country cost fields and `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt` for unit-leader and installed equipment, equipment-module, and unit design cost-factor fields documented by the installed game. Flat operation, MIO, licensing-purchase, guarantee, and equipment-upgrade fields are intentionally absent from those modifiers because the installed schema defines them as absolute values. The exact design-key inventory is recorded in `docs/plans/026_black_friday_plans/event26_design_modifier_inventory.md`; display, debit, save, and reload evidence for native consumers remains pending.

The current owner-adapter coverage is incomplete and is tracked row by row in `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md`; Event 026 remains disabled by default until every reachable owner row is closed or has an accepted exact engine-inaccessible disposition.

The bounded Fury owner adapter uses one transaction for each logical decision, quotes and preflights every positive Command Power, equipment, manpower, train, or experience component, records actual paid components, and settles only after the original owner effect succeeds. It preserves Fury's target, requirement, cooldown, mission, stability, and other non-cost effects. Its source-level adapter evidence is recorded in the Event 026 registry; live confirmation remains a required gate.

## Constants and tuning table

| Category | Values | Purpose |
| --- | --- | --- |
| `universal_cost_framework` | basis 10000, baseline 5000, Evolution I 2500 | fixed-point sale arithmetic |
| `universal_cost_framework` | default quantum 1, invalid index -1 | positive minimum and array lookup safety |
| `universal_cost_framework` | source id 26, source priority 500 | stable Black Friday wrapper defaults |
| `universal_cost_exact` | radix 1000, tick scale 100000, denominator shift 3, trial search 10 | exact representation and long division, without new balance tuning |
| `universal_cost_family` | one bit per purchase family | source eligibility masks |
| `universal_cost_resource_kind` | sixteen native kinds plus owner-adapter ids | payment dispatch and receipt identity |
| `universal_cost_component_state` | not_refunded 0, refunded 1 | one-time component refund proof |

The source file is [`chaosx_universal_cost_constants.txt`](../../common/script_constants/chaosx_universal_cost_constants.txt).

`universal_cost_fixed_point.gate_epsilon` is the shared fixed-point threshold used when an owner preserves a vanilla strict affordability gate while replacing its payable amount. It is a comparison epsilon, not a cost, and is never debited.

## Existing logic migration

An owner migrates one purchase surface at a time by extracting its ordinary cost calculation into the adapter input, replacing any duplicated sale arithmetic with `universal_cost_quote_integer`, and preserving its existing trigger, cooldown, reserve, and AI blocks.

The owner then routes native debit through `universal_cost_pay_component` or supplies a documented owner payment provider for an inaccessible surface.

The owner records each paid component under one transaction id and replaces any refund-from-requested-cost logic with `universal_cost_refund_transaction` or the explicit external-refund acknowledgement.

No shared helper should be introduced for a surface whose ordinary cost cannot be read or whose native debit cannot be proven.

## Engine limits and validation

The engine exposes no generic scripted value for every purchase surface's current modified price, so ordinary cost providers remain explicit adapters.

The engine does not accept an arbitrary dynamic resource token as an effect key, so native payment branches are fixed and unsupported resource kinds are not silently approximated. The native registry includes aggregate equipment kinds plus concrete `support_equipment_1` and `train_equipment_1` kinds for owners whose affordability and debit helpers require exact variant stockpiles.

The engine does not provide a transactional rollback across unrelated effects, so the owner must debit only after complete affordability validation and record actual paid amounts after successful payment. If an owner uses an unsupported component, it must credit the stored actual-paid amount itself before calling `universal_cost_mark_component_refunded`.

The engine's ordinary array API stores numeric values, so stable numeric source/family/resource ids are used instead of inventing token-keyed maps.

The required arithmetic evidence set is BF-R01 through BF-R13 and BF-C01 through BF-C06 from the Event 026 specification.

The required transaction evidence set is BF-X01 through BF-X14, including delayed quote expiry, recomputation, multi-component recording, actual-paid refunds, second-refund no-op, and payer isolation.

No icon, sprite, GFX, localisation, GUI, event target, or spreadsheet asset is required by this framework itself.
