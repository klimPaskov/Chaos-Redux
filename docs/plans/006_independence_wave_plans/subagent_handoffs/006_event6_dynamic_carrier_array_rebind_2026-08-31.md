# Event 006 dynamic-carrier plan-array rebind handoff

Date: 2026-08-31.

Status: source repair applied; parent review and live engine validation remain open.

## Problem

The frozen Event 006 plan stores country and state-target entries as scope-valued variables before an absent carrier is materialized. The dynamic-country repair correctly saves the newly created country as `independence_wave_execution_country`, but later executor loops also read `global.liberation_plan_countries`, `global.liberation_plan_state_target_countries`, and each planned state's `liberation_release_target_country` variable. Leaving those values pointed at the absent pre-materialization scope could make state transfer and package setup address a stale target even after country creation succeeds.

## Source repair

`common/scripted_effects/006_independence_wave_execution_effects.txt` now rebinds the current plan row to `event_target:independence_wave_execution_country` whenever the live target exists. A bounded state-row loop matches the current Event 006 package ID and owner, rewrites each aligned state-target array entry to the live country, and updates the state-scoped `liberation_release_target_country` variable before core restoration and transfer.

The repair uses the documented HOI4 variable/array contract: array elements are variables, variables may hold country-scope IDs, and `set_variable` can rewrite an existing array element. It does not add a fallback, alter package admission, change reservation order, widen the pre-event surface, or touch Event 021's separate raw-release adapter.

## Validation

Focused source audits pass after the repair:

- `python -B .tools/audit_event6_allocator.py --strict`
- `python -B .tools/audit_event6_country_api.py --strict`
- `python -B .tools/audit_event6_flags.py --strict`

The allocator remains at 32 content-attested packages, 29 reservation groups, 40 adapters, and the exact 3/4/5/7/10 ladder. The MCP Event 006 inspect/render route is source-linked but partial and does not prove helper semantics, save/load behavior, or live transfer. A user-supplied live receipt is still required before claiming runtime completion.

## Remaining risks

- Event 006's absent-carrier dynamic creation and this array rebind need live save/load verification.
- Event 021's compatibility adapter still has its own literal `release = TAG` branches; it is outside this bounded standalone executor repair and remains a separate audit surface.
- The whole Event 006 implementation remains HOLD / PARTIAL at the current documented 32/29/40/161 boundary; no admission or fallback was introduced here.
