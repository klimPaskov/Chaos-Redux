# Event 006 Candidate Pool Resolver Fix

## Scope

Parent follow-up after the documentation curator pass and KUB/ALT cutback. This handoff records a code-side fix for the reported runtime issue where manually firing `chaosx.nr6.1` could complete without freeing any republic.

## Changed files

- `events/006_independence_wave.txt`
- `common/script_constants/006_independence_wave_constants.txt`

## Fix

- Removed the `random_select_amount = @independence_wave_candidate_scan_cap` sampling from each `every_possible_country` candidate-pool pass.
- Removed the now-unused `@independence_wave_candidate_scan_cap` macro from the event file.
- Removed the now-unused `independence_wave_release_count.candidate_scan_cap` script constant.

The release target remains controlled by `independence_wave_release_count`. The resolver now builds the full eligible candidate pool and stops through the existing `global.independence_wave_actual_release_count < global.independence_wave_release_count_target` gate instead of gambling on a small random pre-sample that could contain no valid host/candidate pairs.

## Validation

- Brace/trailing whitespace check passed for:
  - `events/006_independence_wave.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `git diff --check` passed for the same touched/related files.
- Event 006 log type mapping parity check passed across current, history-detail, event-detail, and selected-detail views.
- Evolution log call-site count remains four `record_events_log_evolution_entry` calls, all inside `independence_wave_record_tier_evolution_log_entry`.

## Remaining risk

This fixes candidate starvation in the event resolver. It does not claim full Event 006 completion; broader remaining package/focus/decision audit findings still need to be handled separately before the goal can be marked complete.
