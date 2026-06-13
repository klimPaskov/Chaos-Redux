# Chaos Redux Settings Export

The Save Settings button calls `export_chaosx_settings_config_to_log` from `common/scripted_effects/chaosx_settings_effects.txt`.

The export writes technical records to `game.log` between `CHAOS REDUX SETTINGS EXPORT START` and `CHAOS REDUX SETTINGS EXPORT END` markers. The engine prefixes every `log` call in `game.log`; the record payload after that prefix is intentionally parser-oriented:

- scalar settings use `token=value`
- events use `event.<event_id>=0|1`
- event clusters use `event_cluster.<cluster_id>=0|1`
- evolutions use `evolution.<event_id>.<type>.<stage>=0|1`

The export does not write country identities, selected country tags, or per-country event-system lists. `event_system.enabled` is the generic current-scope event-system setting that a future importer should apply to its own active scope.

The export does not include event-history status such as fired counts, unique counts, actor history, dates, or status-log totals.

The export avoids `print_variables`, recursive scripted localisation, and oversized single-line payloads because those paths either dump unrelated engine state or can crash the engine when the full event/evolution registry is expanded.
