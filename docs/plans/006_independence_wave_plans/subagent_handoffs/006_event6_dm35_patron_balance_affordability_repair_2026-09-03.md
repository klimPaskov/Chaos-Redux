# Event 006 DM-35 patron-balance affordability repair

## Result

The DM-35 `independence_wave_balance_patrons` mission now tests the full command-power payment on repeat use. No new resource, cost family, visible surface, route, AI weight, admission gate, or pre-event surface was introduced.

## Changed source

- `common/script_constants/006_independence_wave_constants_registry.txt`
  - Added `independence_wave_decision_cost.command_power_patron_balance_after_first = 30`, the sum of the existing 20 command-power diplomatic-standard charge and 10 command-power administration-light charge.
- `common/decisions/006_independence_wave_decisions.txt`
  - Replaced the repeat-use `command_power > ...command_power_light` checks in both `available` and `custom_cost_trigger` with the summed DM-35 constant.

The first completion still pays only `independence_wave_decision_pay_diplomatic_standard`. Later completions still pay the same diplomatic-standard charge plus `independence_wave_decision_pay_administration_light` (command power and manpower). The existing transport branch and the compact `independence_wave_cost_patron_balance` / blocked localization remain aligned with those payments.

## Why this was needed

The previous repeat-use predicate checked the standard diplomatic command-power threshold and the light command-power threshold independently. That could admit a country whose command-power stockpile could not cover the combined 30-point payment. The new shared constant keeps the tuning value centralized and makes the affordability test match the transaction.

## Validation

- `python -B .tools/audit_event6_allocator.py --strict` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 content attestations, 29 compatible groups, exact 3/4/5/7/10 ladder, and no pre-event category/mission/cost/queue.
- `python -B .tools/audit_event6_flags.py --strict` passed: 102 registered tags, 102 complete flag families.
- `python -B .tools/audit_event6_country_api.py` passed: 242 broad API tags, 191 resolved carriers, zero missing or duplicate tags.
- `python -B .tools/audit_event6_scenario_matrix.py` passed: all 32 SCN-008 cells and eight edge cases.
- No probability change was made; DM-35's deterministic affordability predicate has no AI-weight source to compare. Existing typed probability evidence remains fixture-incomplete and is not reused as balance proof.

## Scope and blockers

This is a source-only affordability repair. No live engine, save/load, tooltip render, or in-game completion claim is made. The whole Event 006 status remains **HOLD / PARTIAL** because the central boundary is still 32 content-attested packages across 29 reservation groups, 40 adapters, and 161 unattested selectable rows, with separate identity, rights, asset, GUI, probability, and reachability blockers documented in the current source-of-truth map.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`. No skill files were created or updated.
