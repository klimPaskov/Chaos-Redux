# Event 006 Banat failure tooltip repair — 2026-09-20

Disposition: implemented, bounded localisation repair; no gameplay, AI, probability, admission, asset, workbook, or map surface changed.

## Finding

The Banat foundation-project timeout and cancellation paths call `independence_wave_axx_apply_project_failure` in `common/decisions/006_independence_wave_balkan_decisions.txt:53-59`, with additional cancellation consumers in the same package. The effect in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt:100-110` applies four country-value losses, one instability increase, and equal Banat civic/defence losses.

The previous `independence_wave_axx_project_failure_effect_tt` only named those ledgers and did not disclose their magnitudes, while the package already centralizes the values in `common/script_constants/006_independence_wave_constants_registry.txt`.

## Change

Updated `localisation/english/006_independence_wave_balkan_l_english.yml` so the tooltip exposes the exact centralized magnitudes through `independence_wave_decision_effect.value_standard`, `independence_wave_decision_effect.value_major`, and `independence_wave_banat_pressure.standard_gain`, with no duplicated numeric literals.

The source effect uses the corresponding negative values for the four country ledgers and `independence_wave_banat_pressure.standard_loss` for the two Banat ledgers. The tooltip presents their positive loss magnitudes in player-facing prose, so it does not expose signed implementation values.

## Validation and limits

The change is a single localisation-key replacement with no new key or gameplay identifier. The full static localisation audit was rerun after the edit and reports zero parse errors, duplicate keys, missing BOMs, or missing English headers; its unrelated global undefined-binding and missing-news-key findings remain outside Event 006. Live tooltip rendering and runtime dynamic-value evaluation remain user-owned and unverified.

This repair does not alter the five route-specific Banat government effect tooltips, which already describe their distinct authorities and ledger outcomes.
