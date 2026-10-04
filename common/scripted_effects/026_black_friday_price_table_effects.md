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
| `black_friday_price_table_quote` | Any | Temp `black_friday_price_ordinary`, temp `black_friday_price_ratio` (payment ratio in basis points of `constant:black_friday_event.ratio_basis`) | Caller-owned temp `black_friday_price_payable`. A positive price below the full ratio becomes `ceil(ordinary x ratio / ratio_basis)`, at least 1. Zero, negative, and full-ratio prices are returned unchanged. No other side effect. |
| `black_friday_price_table_refresh_entries` | Any | Temp `black_friday_price_ratio` | Rewrites every registered `global.black_friday_price_<key>`. |
| `black_friday_price_table_apply` | Any | `global.black_friday_discount_ratio` | Sets every registered price to the active sale price. Called by `black_friday_activate_sale` after the sale ratio is snapshotted. |
| `black_friday_price_table_restore` | Any | None | Sets every registered price back to its ordinary amount. Called by `black_friday_expire_sale`, which terminal cleanup also uses. |
| `black_friday_price_table_initialize` | Any | `constant:black_friday_event.price_table_version` | Builds the table once per version, at the sale price while a sale is active and at ordinary prices otherwise, then stores `global.black_friday_price_table_version`. Called from `on_startup` and from `black_friday_initialize_runtime` on every Event 26 pulse. |

Defaults: before the first build a price variable is unset and reads as zero, which is why the table is built in `on_startup` before the first day.
Sale ratios are whole percents (`ratio_per_percent`), so the payable product is exact before the ceiling.

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
Custom costs (`custom_cost_trigger`) use the custom-cost sale API instead.
Base-game decision files are not registered; they keep their normal price (agent decision D7 in `docs/plans/026_black_friday_plans/agent_decisions_2026-10-04.md`).
