# Chaos Redux Settings Export

The Save Settings button calls `export_chaosx_settings_config_to_log` from `common/scripted_effects/chaosx_settings_effects.txt`.

The export writes a start marker, one multiline body record, and an end marker to `game.log`. The body starts with a newline so the copyable rows are not prefixed per row by the engine log header. The export records are intentionally parser-oriented:

- scalar settings use `token=value`
- events use `event.<event_id>=0|1`
- event clusters use `event_cluster.<cluster_id>=0|1`
- evolutions use `evolution.<event_id>.<type>.<stage>=0|1`

The export does not write country identities, selected country tags, or per-country event-system lists. `event_system.enabled` is the generic current-scope event-system setting that a future importer should apply to its own active scope.

The export does not include event-history status such as fired counts, unique counts, actor history, dates, or status-log totals.

The export builds runtime row arrays and expands them through recursive scripted localisation so event, cluster, and evolution rows come from the live registries instead of static row lists. Event rows sort by event ID, cluster rows sort by cluster ID, and evolution rows sort by event ID, type, then stage. The Independence Wave main evolution keeps its internal event-log type, but the export token normalizes that type to the Event 6 id so the config row stays compact.
