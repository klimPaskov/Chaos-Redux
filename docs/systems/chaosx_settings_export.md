# Chaos Redux Settings Export

The Save Settings button calls `export_chaosx_settings_config_to_log` from `common/scripted_effects/chaosx_settings_effects.txt`.

The export writes technical records to `game.log` using `chaosx_export` prefixes. The format is intentionally parser-oriented:

- scalar sections use `chaosx_export.<section>;token=value;token=value`
- countries use `chaosx_export.country_event_system.<TAG>=1`
- events use `chaosx_export.event.<event_id>=0|1`
- event clusters use `chaosx_export.event_cluster.<cluster_id>=0|1`
- evolutions use `chaosx_export.evolution.<event_id>.<type>.<stage>=0|1`

Only countries with the event system enabled are written. Missing countries should be treated as disabled by default.

The export does not include event-history status such as fired counts, unique counts, actor history, dates, or status-log totals.

The export avoids recursive scripted localisation and oversized single-line payloads because those can crash the engine when the full event/evolution registry is expanded.
