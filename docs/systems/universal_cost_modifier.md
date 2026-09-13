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
| `universal_cost_rebuild_custom_quote_ratio_cache` | any effect scope | active source registry | twelve canonical-family composed ratios plus valid flag | replaces the trigger-readable cache |
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

For a positive cost, the final quote is the smallest whole quantum whose product is at least `ordinary * composed_ratio / 10000`. The helper computes the Euclidean remainder, subtracts it before division so Clausewitz produces a whole quotient, and adds one unit only when the remainder is positive; a positive fractional result is therefore never truncated or incremented as a fractional quotient.

A positive result is always at least one positive quantum.

Zero remains zero and negative/reward values bypass source discounts and are preserved unchanged.

Quantization happens after all eligible source ratios are composed, so a multi-source quote does not round each source separately.

The quote exposes one `universal_cost_quote_displayed_cost` value equal to the final amount the owner must pass to payment and receipt recording.

The effect-side quote composes every registered source. While Event 026 is active, every successful source registration or clear rebuilds twelve canonical scalar ratios (`political_power`, `command_power`, `manpower`, `equipment`, `trains`, `convoy`, `fuel`, `army_experience`, `navy_experience`, `air_experience`, `stability`, and `war_support`) by invoking the same effect-side quote and storing its pre-quantization composed ratio. Custom-cost trigger owners pass exactly one of those canonical family masks and apply the same Euclidean-remainder ceiling as confirmation payment. Other family masks fail closed rather than displaying a price that payment cannot reproduce.

The current bounded adapters declare source-level quote paths across 104 logical component rows in ten owner tranches, including all ten Random Faction paid actions and Africa Elephant logistics. Fury, Japan chemical, biological medical capacity, and Japan biological sale strings use dynamic values instead of fixed 50/75-percent literals, while Communist-spread, CBRN shelter, Germany Mengele, Random Faction, and Africa owner text consume quote-backed values. Source inspection alone is not live engine proof, so overlapping-source parity remains open in Part 8 until focused MCP/runtime evidence confirms cache rebuild, trigger evaluation, displayed value, and confirmation debit under both source orders.

## Source registry and expiry

The registry stores source id, active ratio, priority, and eligibility mask in four aligned global arrays. The separate nine-scalar trigger-readable quote cache persists with global state and is deterministically replaced after every successful registry mutation while Event 026 remains registered.

A zero eligibility mask means every family, while non-zero masks use the low thirty bits defined by `universal_cost_family` and are rejected above the shared thirty-bit bound. Family membership is evaluated with a modulo-span test (`mask mod (bit * 2) >= bit`) rather than fixed-point division, so a lower family bit cannot leak into a higher-family match.

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
