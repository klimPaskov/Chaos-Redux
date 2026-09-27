# Event 006 Catalog Parity Audit — 2026-09-27

## Scope and status

Audited only Events!B7:H7 for Event 006 and Clusters!B3:C3 for cluster ID 2. The workbook rows identify Event 006 and cluster ID 2 as scoped. Whole-event status remains HOLD / PARTIAL; catalog status was not promoted.

## Cell comparisons

All nine scoped cells match their current player-facing source text exactly.

| Cell | Source key | Result |
| --- | --- | --- |
| Events!B7 | `chaosx.event_name.6` | Match: `Independence Wave` |
| Events!C7 | `chaosx.events_log.window.event_details.independence_wave` | Exact match |
| Events!D7 | `independence_wave.evolution.1.body` | Exact match |
| Events!E7 | `independence_wave.evolution.2.body` | Exact match |
| Events!F7 | `independence_wave.evolution.3.body` | Exact match |
| Events!G7 | `independence_wave.evolution.4.body` | Exact match |
| Events!H7 | `independence_wave.evolution.5.body` | Exact match |
| Clusters!B3 | `chaosx.event_cluster.liberations.name` | Match: `Liberations` |
| Clusters!C3 | `chaosx.events_log.window.cluster_details.description.liberations` | Exact match |

The current event-log name mapping in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:10133-10139` maps event ID 6 to `chaosx.event_name.6`. The name value is in `localisation/english/chaosx_event_names_l_english.yml:8`.

The Event Details value is in `localisation/english/chaosx_gui_l_english.yml:1120`. The five evolution bodies are in `localisation/english/006_independence_wave_evolution_l_english.yml:12,14,16,18,20`. The cluster name and description are in `localisation/english/chaosx_gui_l_english.yml:896` and `:418` respectively.

## Workbook and export handling

No scoped mismatch was found, so the workbook was not saved and the CSV exporter was not run. No catalog cells were edited; members, type, chaos level, and status were preserved.

At audit start, Git showed existing modifications to `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `docs/spreadsheets/chaos_redux_events_catalog.csv`, and `docs/spreadsheets/chaos_redux_clusters_catalog.csv`; the scenarios CSV had no reported modification. Those workbook/export states were left untouched. No CSV was edited directly.

This audit makes no HOI4 launch or live-game validation claim.
