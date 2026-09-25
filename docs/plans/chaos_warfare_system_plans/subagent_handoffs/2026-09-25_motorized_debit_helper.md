# CBRN motorized stockpile debit helper handoff

Disposition: implemented helper; caller migration remains with the parent.

## Scope and behavior

The new `cbrn_debit_motorized_stockpile_oldest_first` scripted effect runs in the paying country scope. Its required input is temporary `cbrn_motorized_stock_debit_requested`, a whole truck count that matches the displayed price. It returns temporary `cbrn_motorized_stock_debit_completed` and `cbrn_motorized_stock_debit_remaining`; both are overwritten per call. It reads real `num_equipment@motorized_equipment_0` and `num_equipment@motorized_equipment_1` stock, removes model 0 before model 1, and limits each removal to stock and outstanding demand. A negative request is treated as zero. The request itself is unchanged.

The only lasting side effect is removal of actual motorized equipment. Working variables are temporary. No flag, event target, recurring action, or cleanup effect was added.

## Helper map and tuning

| Helper | Scope | Input | Outputs | Side effect | Intended call sites |
| --- | --- | --- | --- | --- | --- |
| `cbrn_debit_motorized_stockpile_oldest_first` | Country | `cbrn_motorized_stock_debit_requested` temporary integer | `cbrn_motorized_stock_debit_completed`, `cbrn_motorized_stock_debit_remaining` temporary integers | Debits stock of `motorized_equipment_0`, then `_1` | CBRN diplomacy and HQ payment blocks owned by the parent |

No new tuning constant is needed. The helper uses existing `constant:cbrn_math.zero` for the lower bound and existing engine stock counts for model availability. The `-1` multiplication is the documented sign reversal required by `add_equipment_to_stockpile`; it is not a tunable cost. The price and any rounding belong to each caller's existing tuning table.

## Parent migration contract

At each CBRN diplomacy or HQ payment, compute and display one whole motorized cost and use that exact value for `cbrn_motorized_stock_debit_requested`. Keep an inclusive affordability gate over the combined motorized stock before invoking this mutating helper. Replace the direct model-1-only debit with this helper. Record `cbrn_motorized_stock_debit_completed` as consumption and allow the operation only when `cbrn_motorized_stock_debit_remaining` is zero. A partial debit reports the shortfall but cannot by itself refund a payment; the caller must gate affordability before invoking it.

The existing shared `remove_motorized_equipment_from_stockpile` archetype helper was left untouched for unrelated callers. No gameplay call sites were changed under this assignment.

## Evidence and validation limits

Offline wiki pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Equipment modding. Installed vanilla references consulted: `documentation/effects_documentation.md` (`add_equipment_to_stockpile`, temporary variable and clamp effects), `documentation/triggers_documentation.md` (`check_variable`), `documentation/dynamic_variables_documentation.md` (`num_equipment`), `documentation/script_concept_documentation.md` (script constants), `common/script_constants/documentation.md`, `common/units/equipment/motorized.txt`, and the vanilla stockpile-removal precedent in `common/raids/land_infiltration_custom.txt`. The established Chaos Redux debit patterns are `cbrn_debit_mask_stockpile_oldest_first` and `cbrn_hq_debit_decontamination_stock_oldest_first`.

The installed dynamic-variable documentation describes `num_equipment@type` as the country's equipment count but does not specify how every player-designed variant is aggregated. The helper follows the existing model-specific CBRN stock debit pattern; runtime stockpile behavior is unverified because agents do not launch HOI4. No focus, event, map, GUI, or weighted surface was changed here, so this bounded helper had no domain MCP inspection route to run. Parent-owned caller edits require their corresponding inspection and scenario evidence.

A task-specific static check confirmed the model-0 stock read and debit precede model 1, both model counts are floored at zero, there are exactly two stockpile-removal effects, and both branches update completed and remaining amounts. Diff review covered only the two helper files, and `git diff --check` found no patch whitespace errors. Runtime stockpile and caller affordability scenarios were skipped because they require parent-owned call sites and live-game validation.

## Files changed

- `common/scripted_effects/chaosx_dynamic_effects.txt`: helper declaration and model-specific debit sequence.
- `common/scripted_effects/chaosx_dynamic_effects.md`: purpose, scope, input, output, default, side-effect, and usage contract.
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_motorized_debit_helper.md`: this handoff.

No fallback or simplification was made inside the helper. End-to-end no-free-operation behavior remains incomplete until the parent updates the CBRN callers and validates their gates and displayed prices.
