# Event 006 FORM-08 transport-cost localisation correction

Date: 2026-08-25.

## Finding

The four FORM-08 congress and rail-authority base/blocked cost rows displayed a convoy amount followed by both convoy and train icons, while the current affordability trigger accepts either transport branch and the payment effect consumes the selected convoy-or-train branch.

The affected keys were `independence_wave_form08_congress_cost`, `independence_wave_form08_congress_cost_blocked`, `independence_wave_form08_transport_cost`, and `independence_wave_form08_transport_cost_blocked` in `localisation/english/006_independence_wave_formable_registry_l_english.yml`.

## Correction

The four rows now call `GetIndependenceWaveDiplomaticStandardTransportCostText` or `GetIndependenceWaveDiplomaticStandardTransportCostBlockedText`, reusing the existing branch selectors in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.

The selectors display the convoy branch, train branch, or explicit either-branch fallback based on the same stockpile conditions used by the shared transport cost system.

No decision trigger, payment effect, timer, AI score, formable gate, package admission, or runtime mechanic changed.

## Validation

- The receiver retains one UTF-8-BOM `l_english:` root, 225 keys, and 225 unique keys.
- All four FORM-08 rows now use the branch selectors.
- Zero FORM-08 rows retain the ambiguous `convoy_standard` plus `£GFX_train_texticon` fragment.
- The Event 006 allocator, SCN-008 scenario matrix, and country API audits remain passing after the localisation patch.

