# Cost Payment Contracts and Cost Localisation

This reference holds the payment-contract subsections of section 5 and all of section 6 of [chaos-redux-decisions-missions](../SKILL.md). The cost lists, hard cost budget, and cost display rules remain in [section 5](../SKILL.md#5-cost-and-sacrifice-design).

### Custom-cost affordability and payment

Every native `custom_cost_text = <base>` needs localisation for `<base>`, `<base>_blocked`, and `<base>_tooltip`; the engine selects the row key through `custom_cost_trigger` and the tooltip key on hover (offline Decision modding, lines 311-329).
Per-resource scripted colour selectors do not replace these parent native keys.
When the base already renders each resource's ready or blocked colour independently, exact `$base$` aliases for the suffixed keys can reuse that quote without duplicating amounts or adding fees.
Trace actual decision consumers, scripted getters, and texticon definitions; missing source-key coverage establishes a contract gap, not proof that a native row displayed a raw key.

Custom-cost display is not sufficient evidence that a decision is selectable. Define one shared, inclusive affordability predicate and invoke it from both `available` and `custom_cost_trigger`. Manually debit the custom payment once in `complete_effect`, and set the fixed `ai_hint_pp_cost` amount when political power is included. If the cost row already fully explains payment, the `available` duplicate may use `hidden_trigger` to keep raw requirements out of the visible block. Keep the display, affordability gate, and debit aligned, and document any engine uncertainty rather than inferring behavior.
Each resource's cost colour/display selector must call the same authoritative inclusive affordability component used by that shared gate, with the same payer, quote, units, and equipment token.
Do not copy strict, deprecated, or inexact reserve/equipment predicates into display logic.
Check agreement just below, exactly at, and just above the quoted cost.

For pending-payment actions, use one authoritative pure preflight for cost display, hover text, and availability that requires a positive record ID, matching actor and target, the correct transaction phase, and an existing positive actual-paid field.
A pointer's presence alone must neither expose a pending-payment quote nor authorize fresh payment when the referenced record is malformed.

For fractional dynamic quotes, show enough decimals in every cost row and tooltip to match the actual debit. Keep any display cache separate from fresh availability and debit calculations so a rounded or stale quote cannot govern payment.

When accepted design requires emergency resolution to remain available while every other recovery is unaffordable, do not gate it on full nominal reserves. Bound each actual fee by its nominal fee and the nonnegative current reserve, show the actual quote with matching texticons, and recompute all fees together before any debit, then charge that coherent quote once. Avoid hidden partial payments and threshold fee-waiver cliffs. For variable-fee emergency actions, use an `ai_hint_pp_cost` matching the actual quote only if that input form is verified as supported, otherwise omit the fixed nominal hint so a zero quote remains available to AI at zero political power. Never assume `ai_hint_pp_cost` accepts dynamic values. Verify exact numeric reader tokens in installed dynamic-variable documentation rather than assuming a display or stat name: `has_political_power`, `has_stability`, and `has_war_support` are documented readers, while raw `war_support` is not a documented built-in reader. This does not forbid a custom normal variable named `war_support`. Make final resolution and cleanup idempotent with a closed-state guard, and require queued work and late timed callbacks to match the active context before invoking cleanup. Preserve earned finite aftermath until its intended expiry and retain achievement receipts when removing active-crisis state.

### Paid timed-decision entry and expiry

For a `days_remove` decision, selection must pass the full quote, including free factories committed by its native `civilian_factory_use` modifier.
At `complete_effect` entry, recheck live requirements and spendable reserves without counting that project's own native factory reservation twice.
Limit that factory exception to the exact native-reserved path, retaining full affordability checks elsewhere.
Reject duplicate starts and publish the actor/family/generation-bound active receipt before the custom debit, then charge once.
At `remove_effect` expiry, require exact current paid-project proof and continuing finish requirements without rerunning the purchase quote or slot-open start gate.
Publish the success receipt before clearing active proof so cancellation cannot mistake successful closure for receipt loss.
Cover exact-quote selection, reservation-before-entry, duplicate start, depleted reserves after payment, stale generation, and successful expiry in source cases.
Local simulations cannot confirm exactly when the game holds resources or runs completion effects. Use documented cost and timer settings and tested project patterns even when their behavior cannot be observed in game. Review resource payments, resources held while actions run, timers, completion, cancellation, and cleanup; explain any important behavior these checks cannot confirm. Do not add a second debit, synthetic timer, free payment path, or gameplay rewrite to avoid a verification limit. Known errors in costs, timing, or cleanup still need to be fixed.

### Refundable native political-power credit receipts

For refundable native political-power decisions using the sale price table, read the [receipt API contract](../../../../common/scripted_effects/026_black_friday_simple_cost_api.md#refundable-native-political-power-decisions) and its [production helpers](../../../../common/scripted_effects/026_black_friday_effects.txt).
Keep the exact paid quote in an owner normal variable for currency refunds; achievement credit is a separate receipt and must never be inferred from the price or sale activity.

Clear the previous owner receipt before crediting, initialize both `black_friday_political_power_receipt_credited` and `black_friday_political_power_receipt_sale_sequence` temps to zero in the caller chain, then invoke `black_friday_credit_political_power_purchase_with_receipt` once after payment.
Persist a positive credited output as an owner country flag and its sale sequence as an owner normal variable, with separate pairs for decisions whose timers can overlap.

On cancellation, load that flag and saved sequence into the receipt temps and call `black_friday_withdraw_political_power_purchase_with_receipt`; it withdraws only when the positive receipt sequence matches both the global sale sequence and the payer's retained achievement index.
Refund the recorded paid quote once and clear the persistent receipt pair and paid marker, so repeated cancellation cannot refund currency or withdraw another purchase's credit.
Successful completion clears the receipt and paid marker without withdrawing earned credit.
Do not invent a historical credit ledger, reverse an older sale through a newer index, or revoke an awarded achievement.

Verify same-sale refunds, purchases made outside a sale, older-sale refunds after a newer purchase, excluded credit eligibility, repeated cancellation, and successful completion through the actual helper chain.

### Paid finite-registry release receipts

When a paid decision releases people from a finite row registry, use one read-only, all-target reconciliation preflight in both `available` and `complete_effect`. Require a measured positive actual release before publishing national relief, player-facing release records, or success-only cleanup. If the final preflight or receipt rejects after payment, refund every debited cost and leave success flags, scripted cooldowns, and intake closure unset. A refunded stale click may still consume a native decision cooldown; report that as an engine evidence limit unless verified otherwise.

## 6. Cost localisation

Inline decision cost localisation must be compact and show at most three values, each identified by its matching texticon.
When normal text is necessary, use no more than four words in the entire inline cost/status string.
Separate each texticon name from following formatting codes with whitespace, or use a closed texticon syntax verified in installed vanilla.
Do not repeat a cost already drawn by the native row or expand resource names beside their texticons.
Keep every payment and reserved resource explicit in the full cost tooltip, and check the longest available and blocked strings beside the decision title in an available native preview or inspected text/asset bounds.
The inline display limit does not change the payment contract or the separate gameplay cost budget.

Each cost entry pairs its amount with the matching texticon; either order is allowed when native renders confirm fit and valid icon separation.

`<amount> <matching_texticon>` or `<matching_texticon> <amount>`

Good examples:

- `2,000 <infantry_equipment_texticon>`
- `20 <army_xp_texticon> 20 <command_power_texticon>`
- `20 <army_xp_texticon> 20 <command_power_texticon> 2,000 <infantry_equipment_texticon>`

Do not write literal cost labels such as `Manpower:`, `Fuel:`, `Political Power:`, or `Support Equipment:` in the cost string. Do not use filler words such as `and`, `plus`, `requires`, or `needed` between cost entries. The texticon identifies the resource.

Use:

`20 <army_xp_texticon> 20 <command_power_texticon>`

Do not use:

`20 Army XP and 20 Command Power`

Do not use:

`20 <army_xp_texticon> and 20 <command_power_texticon>`

If the country cannot pay a cost, show the affected amount and texticon in the blocked or red state used by the owning UI. Satisfied costs remain in the normal state.
