# Event 006 catalog alignment probe

Date: 2026-08-30 (Europe/Kyiv).

## Scope and disposition

This bounded spreadsheet audit checked the editable Event Catalog workbook against the current Event 006 implementation, player-facing localisation, and current Event 006 authority documentation. No workbook or CSV edit was made because the scoped Event 006 cells already match current source wording, and the workbook plus all three generated CSVs are already modified in the shared working tree by unrelated work.

## Workbook rows audited

| Sheet and row | Scope | Result |
| --- | --- | --- |
| `Events!A7:N7` | Event ID `6`, Independence Wave | No stale cells found. |
| `Clusters!A3:G3` | Cluster ID `2`, Liberations | No stale cells found. |
| `Scenarios!A8:F8` | `SCN-008`, Every Banner Rises | No stale cells found. |

### Event 006 row

`Events!B7` is `Independence Wave`, matching `chaosx.event_name.6` in `localisation/english/chaosx_event_names_l_english.yml`.

`Events!C7` exactly matches `chaosx.events_log.window.event_details.independence_wave` in `localisation/english/chaosx_gui_l_english.yml:1090`. The cell contains the current two-paragraph premise-only wording and does not contain old Join thresholds, rival-compact values, package IDs, implementation terms, or automatic-wave counts.

`Events!D7:H7` exactly matches `independence_wave.evolution.1.body` through `.5.body` in `localisation/english/006_independence_wave_evolution_l_english.yml:12,14,16,18,20`. The five current player-facing evolution names are The Manuals Cross the Border, Old Nations Wake, Flags Rise Behind the Barracks, The Sovereigns Take Their Seats, and No Border Is Final.

`Events!I7` is empty as required because Event 006 has no terminal world-end scenario catalog field. `Events!J7:N7` remains the existing `Minor Repeatable`, chaos level `1`, cluster `2`, `Medium`, and `Needs Testing` metadata; no status promotion or guessed replacement was warranted.

### Liberations cluster row

`Clusters!B3` exactly matches `chaosx.event_cluster.liberations.name`, and `Clusters!C3` exactly matches `chaosx.events_log.window.cluster_details.description.liberations` in `localisation/english/chaosx_gui_l_english.yml:418` and `:878`.

`Clusters!D3` is the current non-duplicated member list `5, 6`. `Clusters!E3:G3` remains `Minor Repeatable`, chaos level `1`, and `Partially Available`, consistent with the mixed Event 005/Event 006 cluster authority.

### SCN-008 row

`Scenarios!B8` exactly matches `chaosx.scenarios.independence_wave.name` (`Every Banner Rises`) in `localisation/english/006_independence_wave_scenario_l_english.yml:2`.

`Scenarios!C8` exactly matches `chaosx.scenarios.independence_wave.desc.sovereign_scatter` in `localisation/english/006_independence_wave_scenario_l_english.yml:14`; it uses the current player-facing wording and omits the retired implementation label `Event 6`.

`Scenarios!D8` contains all eight current selectable labels from `localisation/english/006_independence_wave_scenario_l_english.yml:5-12`: Sovereign Scatter, Common Congress, Wars of Separation, Universal Belligerence: Former Hosts, Universal Belligerence: Neighboring Releases, Universal Belligerence: Nearby Nonleague States, Patron Worlds, and Great Partition.

`Scenarios!E8` contains the current Low, Medium, High, and Maximum impact paragraphs from `localisation/english/006_independence_wave_scenario_l_english.yml:24-27`, with readable intensity labels prefixed for the manual table. `Scenarios!F8` remains `Needs Testing`; no status replacement was guessed.

## Ladder and no-pre-event checks

The current automatic ladder is Calm World `3`, Gathering Storm `4`, Rising Chaos `5`, Chaos Tier `7`, Totalen Chaos `10`, and World Collapse `10`, as recorded in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:25-38`, `docs/events/006_independence_wave/overview.md:7`, and the current source-of-truth documentation.

The ladder is intentionally not appended to `Events!C7`: that cell mirrors the current in-game Event Details localisation, whose 2026-08-29 premise-only repair removed numeric ladder and runtime-only detail from the public summary. The scoped workbook fields contain no superseded `6/8/10/14/20` ladder or historical `4 to 6`, `5 to 7`, `6 to 9`, `8 to 12`, or `10 to 16` wording.

The scoped Event 006, cluster, and SCN-008 cells contain no `pre-event`, `pre-wave crisis`, `pressure category`, `early request`, `shared allocator`, `rival compact`, or Join-threshold wording. This matches the current no-pre-event contract in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_2_event_flow_and_evolutions.md:37-41` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_pre_event_crisis_surface_removed_2026_08_15.md`: the public Event 006 report is the first player-facing indication of the wave.

## Workbook and export integrity observations

The current workbook loads successfully with `openpyxl`, has sheets `Events`, `Clusters`, `Scenarios`, and `Legend`, contains zero formula cells, and retains its existing tables, formatting, conditional formatting, and data-validation rules.

The current generated CSV snapshots match the workbook row-for-row in a read-only comparison: Events `165` data rows, Clusters `15` data rows, and Scenarios `13` data rows. The scoped Event ID `6`, Cluster ID `2`, and `SCN-008` rows match their workbook counterparts exactly.

The workbook and CSVs were not saved or regenerated in this probe. The working tree already reports `M` for `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `docs/spreadsheets/chaos_redux_events_catalog.csv`, `docs/spreadsheets/chaos_redux_clusters_catalog.csv`, and `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`. The tracked `HEAD` workbook is represented by a Git LFS pointer while the working copy is a hydrated binary with unrelated edits, so an `openpyxl` save would rewrite the mixed OOXML package and could overlap other agents' changes. Since no safe Event 006 delta exists, the exporter was intentionally not run; the existing export snapshots were only read.

## Changed cells and remaining gaps

Changed workbook sheets, rows, columns, and Event IDs: none.

Changed export files or rows: none.

Blocked or `needs_user_review` cells introduced: none.

Remaining catalog/runtime boundary: Event 006 and SCN-008 retain `Needs Testing`, while the mixed Liberations cluster retains `Partially Available`; the workbook status schema does not justify a guessed promotion. Runtime release receipts, live GUI evidence, and whole-event completion remain outside this spreadsheet audit.
