# Event 006 FORM-39 decision registry merge — 2026-08-25

## Scope

This source-layout tranche merges the smaller FORM-39 decision parser into the existing formable decision registry. It changes no decision identifier, category identifier, trigger, cost, timer, effect, cancellation, cleanup, AI weight, localisation, event, package gate, or admission rule.

## Files

- Receiver: `common/decisions/006_independence_wave_formable_decisions.txt`
- Removed parser file: `common/decisions/006_independence_wave_form39_decisions.txt`
- Unchanged companion surfaces: `common/scripted_triggers/006_independence_wave_form39_triggers.txt`, `common/scripted_effects/006_independence_wave_form39_effects.txt`, `localisation/english/006_independence_wave_formable_registry_l_english.yml`

The receiver already owns the shared FORM-08 and FORM-09 post-formation decision categories. FORM-39 uses the same formable transaction domain, so the merge keeps related decision definitions together without combining package-owned effects or triggers.

## Preservation evidence

- The original FORM-39 source body is preserved exactly after line-ending normalization.
- The merged section contains two FORM-39 categories and seven decisions with no duplicate identifiers.
- The two FORM-39 category identifiers and all decision IDs remain textually unchanged.
- The removed file was 9,964 normalized source bytes. The receiver now contains the previous FORM-08/FORM-09 definitions followed by the complete FORM-39 section.
- No `custom_cost_text`, `custom_cost_trigger`, payment effect, timer, or AI expression was edited.

## Validation

The maintained source checks passed after the merge:

- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_event6_country_api.py`
- `python -B .tools/audit_event6_scenario_matrix.py`
- `python -B .tools/audit_event6_flags.py --strict`
- `python -B .tools/audit_event6_form16.py`
- `python -B .tools/audit_event6_gui_matrix.py`

These are source-only checks. No live parser, game, tooltip, save/load, or runtime execution claim is made.

## Boundary and remaining risk

FORM-39 remains in the existing adapter and package boundary. The merge does not promote any package, repair the broader 32-attested/161-unattested boundary, or change the partial Event 006 completion status. The current authority remains **HOLD / PARTIAL**.
