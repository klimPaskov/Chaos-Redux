# Event 006 FORM-39 civil-service cost localisation patch — 2026-08-25

## Scope

This bounded localisation patch tightens the FORM-39 civil-service decision's custom-cost hover text. It does not change the decision trigger, payment effect, civilian-factory availability gate, AI weight, timer, lifecycle, admission, or any retired pre-event Independence Wave surface.

## Source alignment

- `common/decisions/006_independence_wave_form39_decisions.txt` uses `can_pay_independence_wave_form39_civil_service_cost`, `custom_cost_text = independence_wave_form39_civil_service_cost`, and `independence_wave_form39_pay_civil_service_cost`.
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt` requires the strategic cost, diplomatic-standard cost, aggregate transport reserve, and `NOT = { has_independence_wave_form39_project_active = yes }`. The strategic trigger also requires the standard project-capacity threshold.
- `common/scripted_effects/006_independence_wave_form39_effects.txt` pays the strategic and diplomatic-standard resource bundles; no payment value changed.

## Localisation change

`localisation/english/006_independence_wave_formable_registry_l_english.yml` now renders `independence_wave_form39_civil_service_cost_tooltip` as the existing dynamic amount-plus-icon form:

`$independence_wave_form39_civil_service_cost$  §Y[?constant:independence_wave_decision_cost.civilian_factory_standard|0]§! £civ_factory`

The previous `Requires ... spare civilian factories for the project.` sentence was redundant prose. The dynamic factory threshold remains visible with the vanilla `£civ_factory` texticon, and the existing `_blocked` row remains unchanged.

## Validation

- Confirmed the base, `_tooltip`, and `_blocked` keys remain present exactly once.
- Confirmed the localisation file retains its UTF-8 BOM.
- Confirmed the vanilla texticon registry defines `GFX_civ_factory` in `interface/texticons.gfx` and `gfx/texticons/civ_factory.dds`.
- Confirmed no decision, trigger, effect, AI, or cost constant file changed in this tranche.
- Live tooltip rendering and save/load validation remain outside this source-only handoff.

## Remaining risk

The FORM-39 transaction, category visibility, and runtime member/host scenarios still require the broader Event 006 runtime evidence recorded in the current authority packet. This patch does not claim that evidence.
