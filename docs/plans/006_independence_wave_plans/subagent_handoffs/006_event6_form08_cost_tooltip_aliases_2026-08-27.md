# Event 006 FORM-08 cost tooltip aliases

Date: 2026-08-27

## Scope

This handoff records a localization-only completion of the FORM-08 custom decision cost surface.

## Changed surface

- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `independence_wave_form08_congress_cost_tooltip`
- `independence_wave_form08_arbitration_cost_tooltip`
- `independence_wave_form08_transport_cost_tooltip`

## Correction

Each FORM-08 custom cost now has the matching `_tooltip` alias used by the decision UI, pointing to its existing dynamic base cost string.

The existing base and blocked strings, payment effects, and trigger costs are unchanged.

## Validation and boundary

The change is limited to localization and adds no gameplay, package-admission, asset, GUI, spreadsheet, or event-lifecycle behavior.

Event 006 remains HOLD / PARTIAL pending the documented package, identity, rights, MCP, probability, GUI, super-event, and live lifecycle blockers.
