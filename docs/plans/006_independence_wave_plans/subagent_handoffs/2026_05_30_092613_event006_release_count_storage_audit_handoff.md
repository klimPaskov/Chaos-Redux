# Event 006 Release Count and Current-Wave Storage Audit Handoff

Date: 2026-05-30 09:26 UTC
Agent: chaosx_scripted_system_architect
Scope: bounded audit/small patch for Event 006 release-count randomization and current-wave dossier capture.

## Files changed

- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_092613_event006_release_count_storage_audit_handoff.md`

No Event 005 files were edited. No flag files or flag assets were edited.

## Identifiers reviewed

- `independence_wave_release_count`
- `independence_wave_prepare_release_count`
- `global.independence_wave_release_count_target`
- `global.independence_wave_actual_release_count`
- `global.independence_wave_current_wave_releases`
- `global.independence_wave_country_1` through `global.independence_wave_country_16`
- `independence_wave_register_successful_release`
- `chaosx.nr6.1`

## Patch made

`independence_wave_prepare_release_count` now copies the selected tier's min and max-exclusive script constants into temporary variables, then performs one `set_variable_to_random` roll using those temp variables as `min` and `max`.

The behavior is intended to remain the same: baseline uses 3 to 5, Evo I 4 to 6, Evo II 5 to 7, Evo III 6 to 9, Evo IV 8 to 12, and Evo V 10 to 16 because `set_variable_to_random` is min-inclusive and max-exclusive. The patch avoids relying on direct `constant:` parsing inside `set_variable_to_random` `min`/`max`, using vanilla-precedented variable-backed random bounds instead.

## Storage audit result

`independence_wave_prepare_release_count` clears `global.independence_wave_current_wave_releases` and named current-wave country slots 1-16 before each wave. `independence_wave_register_successful_release` increments `global.independence_wave_actual_release_count`, adds the released country to the persistent release ledger and current-wave ledger, records the dossier log entry, and stores the release in the matching named slot 1-16.

This matches the current Evo V maximum of 16 releases. I did not add any fallback slot beyond 16 because the release-count constants currently cap max-exclusive at 17.

## Validation run

- Consulted required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.
- Consulted vanilla documentation for `set_variable_to_random`, arrays, event targets, triggers, effects, and script constants.
- Checked vanilla examples for `set_variable_to_random`; vanilla uses variable-backed bounds in `events/GOE_Raj.txt`.
- Brace balance on Event 006 script files:
  - `common/script_constants/006_independence_wave_constants.txt`: `0`
  - `common/scripted_effects/006_independence_wave_effects.txt`: `0`
  - `events/006_independence_wave.txt`: `0`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`: `0`
- Searched Event 006 script files for unsupported `<=`/`>=`: no hits.
- Searched Event 006 script files for `days`, `random_days`, `hours`, or `random_hours` fields using direct `constant:` or `@` values: no hits.
- Searched Event 006 script files for unary negative variable-token assignments: no hits.
- Ran `git diff --check` in `--no-index` mode for the touched untracked files: OK.

## Validation skipped

- No HOI4 executable parser run or in-game scenario validation was performed.
- No logs were requested or inspected.
- No flag or flag-asset validation was performed, per scope constraint.
- No Event 005 mechanics were audited beyond confirming this task did not edit Event 005 files.

## Remaining risks

- The resolver still uses skip-only host survival around `release = PREV`; reduced-territory release starts remain outside this tranche.
- `global.independence_wave_current_wave_releases` is stored but not yet consumed by a broader scripted GUI or recursive dossier list surface in this task.
- The named slots match the current maximum release count. If future tuning raises Evo V above 16, the slot reset/register logic and player-facing current-wave text must expand at the same time.
- The direct parser behavior of `constant:` inside `set_variable_to_random` `min`/`max` was not tested in-game; the patch was made to avoid that uncertainty.
