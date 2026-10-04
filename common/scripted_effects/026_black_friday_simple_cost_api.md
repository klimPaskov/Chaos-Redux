# Black Friday simple custom-cost API

Source: triggers in [`026_black_friday_triggers.txt`](../scripted_triggers/026_black_friday_triggers.txt), the payment effect in [`026_black_friday_effects.txt`](026_black_friday_effects.txt), display selectors in [`026_black_friday_scripted_localisation.txt`](../scripted_localisation/026_black_friday_scripted_localisation.txt), and display keys in `localisation/english/026_black_friday_l_english.yml`.

## Purpose

Most Chaos Redux custom costs are one immediate payment in one resource: political power, command power, experience, manpower, fuel, equipment, trains, convoys, stability, or war support.
This API gives such a cost the Black Friday price without a receipt or refund path.
The shown price, the `custom_cost_trigger` requirement, and the payment all read one quote from `black_friday_quote_custom_cost`, so they cannot disagree.
Outside a sale the quote is the ordinary amount, so converting a cost changes nothing until a sale starts.

Use the receipt framework (`universal_cost_*` transactions and the owner adapters) instead when the cost is refundable, settles later, or bundles several resources that must succeed or fail together.
Native `cost =` decisions use the [sale price table](026_black_friday_price_table_effects.md) instead.

## Contract

| Name | Kind | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- | --- |
| `black_friday_simple_cost_quote` | Scripted trigger, always true | Country (payer) | Temps `black_friday_simple_cost_ordinary` (the owner's current ordinary amount) and `black_friday_simple_cost_kind` (`constant:universal_cost_resource_kind.*`) | Temps `black_friday_simple_cost_payable`, `black_friday_simple_cost_family`, `black_friday_simple_cost_quoted` (1 when an active sale priced the cost), `black_friday_simple_cost_on_sale` (1 when payable is below ordinary), `black_friday_simple_cost_valid` (0 when an active sale could not price the cost, which blocks the purchase instead of charging a wrong price), `black_friday_simple_cost_affordable`. Writes the shared `black_friday_quote_*` and `universal_cost_affordability_*` scratch temps. |
| `black_friday_simple_cost_is_affordable` | Scripted trigger | Country (payer) | Same as the quote | True when the quote is valid and the payer can afford the payable amount. Use it as `custom_cost_trigger`. |
| `black_friday_simple_cost_read_family` | Scripted trigger, always true | Any | Temp `black_friday_simple_cost_kind` | Temp `black_friday_simple_cost_family`: the achievement family and sale mask for the resource (equipment kinds share `equipment`, train kinds share `trains`), or zero for a kind without a family, which keeps the ordinary price. |
| `black_friday_simple_cost_pay` | Scripted effect | Country (payer) | Same as the quote | Pays the current quote once through `universal_cost_pay_component`. Temp `black_friday_simple_cost_paid` is 1 on success and 0 when the quote was invalid, unaffordable, or in a resource without a native payment. A payment priced by a valid natural sale credits its family through `black_friday_add_committed_achievement_family`, and a payment in any resource other than political power also counts as the achievement's non-political payment. Optional temp `black_friday_simple_cost_no_credit = 1` skips the family credit for that call (the non-political count still applies); each call consumes it. |
| `black_friday_credit_sale_purchase` | Scripted effect | Country (payer) | Temps `black_friday_purchase_family_id` (zero for no family) and `black_friday_purchase_non_political` (1 when any resource other than political power was paid) | Credits one purchase paid at a sale price toward the achievement during a valid natural sale; no-op otherwise. Used by `black_friday_simple_cost_pay` and by owners that pay price-table amounts through their own payment effect. Consumes the non-political input. |
| `GetBlackFridaySimpleCostLine` | Scripted localisation | Country | The quote's temps, set by the caller's own `defined_text` trigger | Resource icon plus the amount for political power, command power, army, navy, and air experience, manpower, fuel, infantry, support, and motorized equipment, trains, and convoys (`GetBlackFridaySimpleCostAmount`), and for Stability and War Support (`GetBlackFridaySimpleCostPercentAmount`); the amount alone for other kinds. Shared key: `black_friday_simple_cost.line`. |
| `GetBlackFridaySimpleCostAmount` | Scripted localisation | Country | The quote's temps | Yellow payable amount, green sale price followed by "(normally N)" during a sale, red when unaffordable, and the ordinary amount in red when an active sale could not price the cost. |
| `GetBlackFridaySimpleCostPercentAmount` | Scripted localisation | Country | The quote's temps | The same states as `GetBlackFridaySimpleCostAmount`, shown as a percentage for Stability and War Support amounts. |

Defaults: a zero or negative ordinary amount is never discounted and is always affordable.
Rounding follows the shared quote: positive prices round up to the resource's quantum (1 for whole-unit resources), so a paid purchase cannot become free.
No AI weight is read or changed; AI decisions see the same requirement and price as players.

## Conversion example

Before, a decision paying 50 command power:

```
custom_cost_trigger = { command_power > 49.999 }
custom_cost_text = my_owner_decision_cost
complete_effect = { add_command_power = -50 }
```

After, three lines change, and the owner adds one `defined_text` for the shown price:

```
custom_cost_trigger = { set_temp_variable = { black_friday_simple_cost_ordinary = constant:my_owner.decision_cp } set_temp_variable = { black_friday_simple_cost_kind = constant:universal_cost_resource_kind.command_power } black_friday_simple_cost_is_affordable = yes }
custom_cost_text = my_owner_decision_cost
complete_effect = { set_temp_variable = { black_friday_simple_cost_ordinary = constant:my_owner.decision_cp } set_temp_variable = { black_friday_simple_cost_kind = constant:universal_cost_resource_kind.command_power } black_friday_simple_cost_pay = yes }
```

```
# Owner scripted localisation; localisation: my_owner_decision_cost: "[GetMyOwnerDecisionCost]"
defined_text = {
	name = GetMyOwnerDecisionCost
	text = {
		trigger = {
			set_temp_variable = { black_friday_simple_cost_ordinary = constant:my_owner.decision_cp }
			set_temp_variable = { black_friday_simple_cost_kind = constant:universal_cost_resource_kind.command_power }
			black_friday_simple_cost_quote = yes
		}
		localization_key = black_friday_simple_cost.line
	}
}
```

A multi-resource action requires every component in `custom_cost_trigger` (one `black_friday_simple_cost_is_affordable` per component) and pays each component in `complete_effect`.
Set `black_friday_simple_cost_no_credit = 1` before each secondary component and pay the primary component last, so the action credits one achievement family and the completion check already sees any non-political component.

The display is recomputed inside its own `defined_text`, as the South Africa purchase text does, so it never depends on an earlier evaluation of the requirement.
Penalties, upkeep, rewards, and costs that are not voluntary purchases keep their ordinary effect and do not use this API.
