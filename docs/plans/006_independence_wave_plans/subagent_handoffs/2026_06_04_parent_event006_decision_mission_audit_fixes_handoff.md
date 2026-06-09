# Event 006 Decision/Mission Audit Fixes Handoff

Date: 2026-06-04
Owner: parent agent

## Scope

Resolved the bounded `chaosx_decision_mission_auditor` findings from `2026_06_04_083702_decision_mission_audit.md`.

## Changes

- Added Municipal Authority and Municipal Charter package types to the selected event-log detail body routing.
- Added `@independence_wave_municipal_authority_integration_days` and moved the municipal integration mission off the Free Port integration duration.
- Wrapped Free Port, Canal Authority, Municipal Authority, Protected Mandate, and Oil Protectorate opener/intermediate gates in `custom_trigger_tooltip` blocks.
- Added matching readable `_requirements_tt` localisation keys.
- Prevented Oil Protectorate releases from also enabling the generic Protected Mandate AI strategy overlay.

## Files Changed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`

## Validation

- `git diff --check` passed for the changed files.
- Raw unsupported comparison-operator scan found no matches in the changed Event006 script/localisation surfaces.
- Brace counts are balanced:
  - `common/decisions/006_independence_wave_decisions.txt`: 1206/1206
  - `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: 3124/3124
  - `common/ai_strategy/006_independence_wave.txt`: 171/171
- `localisation/english/006_independence_wave_l_english.yml` still has UTF-8 BOM (`efbbbf`).
- No old `:0` localisation style was found in the touched Event006 localisation file.
- No missing `_requirements_tt` localisation keys were found for tooltip references in the Event006 decision file.

## Assets And Flags

No flags, country files, history files, or assets were touched.

## Remaining Risks

This closes the four findings from the bounded decision/mission audit. Full Event 006 completion still depends on the broader package, asset, catalog, and final audit work tracked in the Event006 specs and plans.
