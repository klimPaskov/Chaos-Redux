# Black Friday sale price table

Source: [`026_black_friday_price_table_effects.txt`](026_black_friday_price_table_effects.txt), constants in [`026_black_friday_constants.txt`](../script_constants/026_black_friday_constants.txt), startup hook in [`026_black_friday_on_actions.txt`](../on_actions/026_black_friday_on_actions.txt).

## Purpose

HOI4 has no modifier that scales a decision's native `cost =`, so a Black Friday sale cannot discount native political power decisions through its sale idea.
The price table gives each registered ordinary price one global variable that a decision reads as its cost.
The engine then computes the shown price, affordability, the debit, and AI evaluation from that one value, so they always agree.

Engine basis: the offline wiki Decision modding page (Decision cost) states that `cost` accepts a variable, vanilla uses `cost = TUR_etatism_cost_penalty_var?50` and `cost = var:AST_call_on_fascists_cost`, and Kaiserreich (`common/decisions/UPC decisions (Federalist China).txt:981`) uses `cost = global.UPC_coalition_cost_var`.
The CXT decision `chaosx_test_country_event026_price_probe_decision` is the live check for display and debit at 100, 50, and 25 percent.

## Contract

| Effect | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `black_friday_price_table_quote` | Any | Temp `black_friday_price_ordinary`, temp `black_friday_price_ratio` (payment ratio in basis points of `constant:black_friday_event.ratio_basis`), optional temp `black_friday_price_quantum` (smallest payable step; unset or zero means 1) | Caller-owned temp `black_friday_price_payable`. A positive price below the full ratio becomes `ordinary x ratio / ratio_basis` rounded up to a whole number of steps, at least one step and never more than the ordinary price, so a price smaller than one step keeps its ordinary amount. Zero, negative, and full-ratio prices are returned unchanged. Caller-owned temp `black_friday_price_spend` holds the negated payable amount, which a payment line can add directly. No other side effect. |
| `black_friday_price_table_refresh_entries` | Any | Temp `black_friday_price_ratio` | Rewrites every registered `global.black_friday_price_<key>` and records the ratio the table now holds in `global.black_friday_price_table_ratio`. |
| `black_friday_price_table_refresh_soviet_collapse_entries` | Any | Temp `black_friday_price_ratio` | Called by `black_friday_price_table_refresh_entries`. Rewrites the Event 005 decision prices: each positive `global.black_friday_price_soviet_collapse_<group>_<key>` and, for each payment constant of that amount, the matching negative `..._spend` global; a tier surcharge (`..._regional_<resource>_extra_spend`, `..._major_<resource>_extra_spend`) holds the base price minus the tier price (agent decision D21). |
| `black_friday_price_table_apply` | Any | `global.black_friday_discount_ratio` | Sets every registered price to the active sale price. Called by `black_friday_activate_sale` after the sale ratio is snapshotted. |
| `black_friday_price_table_restore` | Any | None | Sets every registered price back to its ordinary amount. Called by `black_friday_expire_sale`, which terminal cleanup also uses. |
| `black_friday_price_table_refresh_owner_quotes` | Any | `global.black_friday_price_table_ratio` | Refreshes owner quotes that are computed from the table ratio and cached between owner pulses. Called by apply and restore. Current consumers: Event 020's population-scaled response quotes (`black_plague_refresh_response_quotes_for_sale`), Event 015's state-scaled growth costs (`utopia_manifesto_refresh_dynamic_costs_for_sale` on each accepted country), Event 019's scaled formation request costs (`infantry_spawn_refresh_request_costs` on each participant), Event 011's cached response costs (`secret_alliance_refresh_dynamic_costs` on each country holding them), and Event 018's project estimates (`resources_found_refresh_decision_cost_previews` on each country with estimates). |
| `black_friday_price_table_initialize` | Any | `constant:black_friday_event.price_table_version` | Builds the table once per version, at the sale price while a sale is active and at ordinary prices otherwise, then stores `global.black_friday_price_table_version`. Called from `on_startup` and from `black_friday_initialize_runtime` on every Event 26 pulse. |

Defaults: before the first build a price variable is unset and reads as zero, which is why the table is built in `on_startup` before the first day.
Sale ratios are whole percents of `ratio_basis`, so the quote first turns the ratio into an exact fraction (0.5 or 0.25) and multiplies the ordinary amount by it; no intermediate value exceeds the ordinary amount, and the product is exact before the ceiling.

## Registering a price

1. Literal amount: add `pp_<N> = <N>` to the `black_friday_price_table` constant group if it is missing. Owner constant: use the owner's existing `constant:<group>.<key>` directly.
2. Add one three-line entry to `black_friday_price_table_refresh_entries` under the owner's group comment. The variable name is `black_friday_price_pp_<N>` for a literal and `black_friday_price_<group>_<key>` for an owner constant.
3. Bump `price_table_version` in `black_friday_event`. Bump it again whenever a registered ordinary amount changes, so running campaigns rebuild the table.
4. Set the decision's cost to the global variable.

Example, for a decision that costs `constant:holy_realm_decision.chinese_core_cost`:

```
# 026_black_friday_price_table_effects.txt, inside black_friday_price_table_refresh_entries
set_temp_variable = { black_friday_price_ordinary = constant:holy_realm_decision.chinese_core_cost }
black_friday_price_table_quote = yes
set_variable = { global.black_friday_price_holy_realm_decision_chinese_core_cost = black_friday_price_payable }

# The decision
cost = global.black_friday_price_holy_realm_decision_chinese_core_cost
```

Zero costs stay `cost = 0`.
Base-game decision files are not registered; they keep their normal price (agent decision D7 in `docs/plans/026_black_friday_plans/agent_decisions_2026-10-04.md`).

## Owner custom costs with constant amounts

An owner custom cost whose ordinary amount is a script constant can register that constant in the same table and read the global price in its `custom_cost_trigger`, its payment, and its cost text (agent decision D11).
Integer resources (equipment, manpower, experience, command power) use the default step of 1; stability and war support set `black_friday_price_quantum = constant:universal_cost_fixed_point_quantum.<stability|war_support>` before the quote and reset it to zero after.
The trigger copies the price into a temp before comparing, for example `set_temp_variable = { utopia_manifesto_cost_check = global.black_friday_price_utopia_manifesto_decision_cost_trains_small } NOT = { has_equipment = { train_equipment < utopia_manifesto_cost_check } }`.
The payment passes the same global to the owner's own payment effect, which keeps the owner's equipment types and calls `black_friday_credit_sale_purchase` once with the action's primary family.
Cost text shows `[?global.black_friday_price_<key>|0]`, or `|%0` for stability and war support.
A component that is transferred to another country, such as shipped aid, keeps its ordinary amount so the recipient never receives more than the payer gave.
An owner constant stored as a negative loss, such as Event 013's `natural_disaster_cost_fixed.stabilize_stability`, is registered as its positive amount (`set_temp_variable` to zero, then `subtract_from_temp_variable` the constant), and the payment negates the global before `add_stability`.
A loss at or below one step needs no entry, because its sale price always equals the ordinary amount.
An owner that pays with negative `_spend` constants, such as Event 005, can store the negated price as its own global (`set_variable = { global.black_friday_price_<group>_<key>_spend = black_friday_price_spend }` right after the quote), so each payment line only swaps `constant:<group>.<key>_spend` for that global.
When a payment is a base amount plus a tier surcharge, the surcharge global is the base price minus the tier price, so the base payment and the surcharge add up to exactly the tier price that the affordability check required.
An owner that compares with a strict `>` floor keeps that form: it copies the price into a temp, subtracts its own one-step constant, and compares, as Event 013 does with `natural_disaster_cost_gate.unit_step`.
Variable amounts use the [simple custom-cost API](026_black_friday_simple_cost_api.md) instead, or, when the owner already caches a computed quote, apply `black_friday_price_table_quote` with `black_friday_price_ratio = global.black_friday_price_table_ratio` inside the quote refresh, keep the ratio in the cache key, and add the owner's refresh to `black_friday_price_table_refresh_owner_quotes` (Event 020's response quotes do this).
