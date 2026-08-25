# Event 006 shared formable transaction registry merge — 2026-08-25

## Scope

This source-layout tranche merges the shared FORM-01 through FORM-48 method-and-consent decision category into the existing formable decision registry, which already owns FORM-08, FORM-09, and FORM-39 federation project categories. It changes no decision identifier, category identifier, trigger, cost, timer, effect, consent rule, family contract, integration gate, localisation, package gate, or admission rule.

## Files

- Receiver: `common/decisions/006_independence_wave_formable_decisions.txt`
- Removed parser file: `common/decisions/006_independence_wave_formable_registry_decisions.txt`
- Unchanged companion surfaces: `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`, `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, `localisation/english/006_independence_wave_formable_registry_l_english.yml`

The receiver is now the single shared parser file for the Event 006 formable decision surface. Package-owned decisions remain in their package files, and FORM-03/FORM-05/FORM-39-specific companions remain bounded by their existing adapters.

## Preservation evidence

- The original registry source body is preserved exactly after line-ending normalization.
- The merged section contains one FORM-01 through FORM-48 category and its ten decisions, with no duplicate category or decision identifiers in the receiver.
- The removed parser was 12,405 normalized source characters. No executable token in the moved section was changed.
- FORM-08, FORM-09, and FORM-39 definitions remain in the same receiver and retain their existing order and bodies.

## Validation

The maintained Event 006 source checks passed after both formable decision merges:

- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_event6_country_api.py`
- `python -B .tools/audit_event6_scenario_matrix.py`
- `python -B .tools/audit_event6_flags.py --strict`
- `python -B .tools/audit_event6_form16.py`
- `python -B .tools/audit_event6_gui_matrix.py`

These are source-only checks. No live parser, game, tooltip, save/load, or runtime execution claim is made.

## Boundary and remaining risk

This merge is a parser-layout reduction only. Formable family admission, exact member and territory contracts, consent, integration, and the broader 32-attested/161-unattested Event 006 boundary remain unchanged. The current authority remains **HOLD / PARTIAL**.
