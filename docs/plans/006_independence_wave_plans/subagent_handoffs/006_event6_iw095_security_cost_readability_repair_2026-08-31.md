# Event 006 IW-095 security-cost readability repair

Date: 2026-08-31

Owner: `/root`

Status: **implemented locally; parent review required**.

## Scope

The bounded repair covers the two IW-095 security decisions that selected the verbose `independence_wave_cost_security_standard_factory` row: `iw095_organize_civic_guard` and `iw095_authorize_emergency_directorate` in `common/decisions/006_independence_wave_decisions.txt`.

## Source change

Both decisions now select `independence_wave_cost_security_standard`, whose normal, blocked, and tooltip rows expose the four resources actually consumed by `independence_wave_decision_pay_security_standard`: manpower, Army Experience, infantry equipment, and support equipment.

Both decisions retain `modifier = { civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_IW095_CIVILIAN_FACTORY_USE }`. This is a project-duration reservation, not an additional consumed security payment. The descriptions `iw095_organize_civic_guard_desc` and `iw095_authorize_emergency_directorate_desc` in `localisation/english/006_independence_wave_l_english.yml` now state that one civilian factory is reserved until the project completes, so the requirement remains visible without the two-line spend/commit cost row.

No trigger, payment effect, duration, route, AI weight, package gate, admission, allocator, ladder, pre-event category, pressure, queue, or event entry changed. The legacy factory-specific localisation triplet remains defined but has no active `custom_cost_text` caller after this repair.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 32 content attestations, 29 reservation groups, exact 3/4/5/7/10 ladder, World Collapse at 10, and retired pre-event crisis surface.
- `python -B .tools/audit_event6_country_api.py` passed with zero missing or duplicate carriers.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 complete flag families.
- `python -B .tools/audit_event6_form16.py` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- Scoped source search found no active `custom_cost_text = independence_wave_cost_security_standard_factory` caller and confirmed both IW-095 security decisions retain the security-standard trigger, factory reservation, and payment effect.
- The localisation file remains UTF-8 with BOM (`EF BB BF`).

## Remaining limits

The formable revolutionary/military commit palettes and other broader cost bundles still contain multiple real payment groups and require an accepted gameplay redesign; this repair does not hide or alter those costs. Event MCP execution/render evidence and the required typed probability comparison remain unavailable in this runtime, so no live-engine or balance completion claim is made. Event 006 remains **HOLD / PARTIAL** at the current 32/29/40/161 boundary.
