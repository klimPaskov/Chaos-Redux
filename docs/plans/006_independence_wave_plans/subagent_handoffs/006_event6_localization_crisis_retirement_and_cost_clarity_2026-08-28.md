# Event 006 localization retirement and cost clarity handoff (2026-08-28)

## Scope

This bounded source-only tranche removes dormant pre-event crisis localization and clarifies Event 006 decision cost strings. It does not admit a package, change a payment effect, alter a trigger, change AI weights, or create a new visible category before Event 006 fires.

## Changed files

- `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/script_constants/006_independence_wave_constants_registry.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/006_independence_wave_balkan_l_english.yml`
- `localisation/english/006_independence_wave_frontier_l_english.yml`
- `localisation/english/006_independence_wave_form01_02_04_l_english.yml`
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `localisation/english/006_independence_wave_komi_l_english.yml`
- `localisation/english/006_independence_wave_kosovo_l_english.yml`
- `localisation/english/006_independence_wave_ruthenia_l_english.yml`
- `localisation/english/006_independence_wave_tatarstan_l_english.yml`
- `localisation/english/006_independence_wave_transcaucasus_l_english.yml`
- `localisation/english/006_independence_wave_udm_l_english.yml`

The source-of-truth map and resume packet record this handoff.

## Retired surface removed

The dormant `GetIndependenceWaveCrisisHistoryCause` and `GetIndependenceWaveCrisisResolution` selectors, their events-log title and description branches, the `independence_wave_crisis_*` history/resolution constants, and the corresponding English history keys are removed together. No active writer or caller existed outside those retired branches, and the compatibility cleanup stubs remain intentionally hard-disabled.

## Cost clarity

Standard diplomatic transport costs now resolve through the existing `GetIndependenceWaveDiplomaticStandardTransportCostText` and blocked counterpart, so a decision shows the available convoy-or-train alternative rather than two adjacent transport icons. FORM-39 shipping retains one standard diplomatic payment, while civil service explicitly shows two standard transport payments to match its strategic-plus-diplomatic payment helper. Transcaucasus arbitration displays its package-specific command-power and convoy-or-train admission thresholds and uses the word “or” instead of a slash.

## Validation and limits

The retired crisis names have no remaining source matches outside the intentionally dormant compatibility cleanup path. Event 006 allocator, country API, strict flag-family, FORM-16, and SCN-008 static audits remain passing with the 32/29/40/161 boundary and automatic 3/4/5/7/10 ladder unchanged. Current Event MCP inspect/render and probability evidence remain blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED`, so this handoff makes no engine, visual, or weighted-balance claim. Scenario ledger technical-term cleanup and the authoritative workbook/shared-string repair are separate queued work.
