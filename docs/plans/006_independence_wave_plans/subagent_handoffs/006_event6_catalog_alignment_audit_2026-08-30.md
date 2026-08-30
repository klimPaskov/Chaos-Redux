# Event 006 catalog alignment audit

Date: 2026-08-30 (Europe/Kyiv).

## Scope and disposition

This bounded spreadsheet audit compared the authoritative workbook rows for Event 006, the Liberations cluster, and SCN-008 against the accepted catalog alignment handoff, the current Event 006 source and overview, and the current player-facing localisation.

No workbook edit was made because every scoped mirror field and status label already matches current source evidence.

The whole Event 006 disposition remains `HOLD / PARTIAL`; this audit does not promote hidden package or formable IDs and does not claim live or in-game testing.

## Workbook rows audited

| Sheet and row | Scope | Result |
| --- | --- | --- |
| `Events!A7:N7` | Event ID `6`, Independence Wave | Exact current alignment; no stale cells found. |
| `Clusters!A3:G3` | Cluster ID `2`, Liberations | Exact current alignment; no stale cells found. |
| `Scenarios!A8:F8` | `SCN-008`, Every Banner Rises | Exact current alignment; no stale cells found. |

### Event 006 row

`Events!A7` is numeric ID `6`, and `Events!B7` is `Independence Wave`, matching `chaosx.event_name.6` in `localisation/english/chaosx_event_names_l_english.yml:8`.

`Events!C7` exactly matches the current premise-only Event Details string `chaosx.events_log.window.event_details.independence_wave` in `localisation/english/chaosx_gui_l_english.yml:1090`.

The Event Details cell contains no retired Join thresholds, rival-compact values, package or formable IDs, implementation terms, automatic-wave counts, or pre-event crisis wording.

`Events!D7:H7` exactly matches `independence_wave.evolution.1.body` through `.5.body` in `localisation/english/006_independence_wave_evolution_l_english.yml:12,14,16,18,20`.

The corresponding current evolution titles are The Manuals Cross the Border, Old Nations Wake, Flags Rise Behind the Barracks, The Sovereigns Take Their Seats, and No Border Is Final.

`Events!I7` is empty, as required because Event 006 has no terminal world-end scenario catalog field.

`Events!J7:N7` remains the accepted metadata tuple `Minor Repeatable`, chaos level `1`, cluster `2`, member severity `Medium`, and status `Needs Testing`.

### Liberations cluster row

`Clusters!B3` exactly matches `chaosx.event_cluster.liberations.name` in `localisation/english/chaosx_gui_l_english.yml:878`.

`Clusters!C3` exactly matches `chaosx.events_log.window.cluster_details.description.liberations` in `localisation/english/chaosx_gui_l_english.yml:418`.

`Clusters!D3` is the current non-duplicated member list `5, 6`.

`Clusters!E3:G3` remains `Minor Repeatable`, chaos level `1`, and status `Partially Available`, consistent with the mixed Event 005/Event 006 cluster authority.

### SCN-008 row

`Scenarios!A8` is `SCN-008`, and `Scenarios!B8` exactly matches `chaosx.scenarios.independence_wave.name` (`Every Banner Rises`) in `localisation/english/006_independence_wave_scenario_l_english.yml:2`.

`Scenarios!C8` exactly matches `chaosx.scenarios.independence_wave.desc.sovereign_scatter` in `localisation/english/006_independence_wave_scenario_l_english.yml:14`.

`Scenarios!D8` contains all eight current selectable labels from `localisation/english/006_independence_wave_scenario_l_english.yml:5-12`: Sovereign Scatter, Common Congress, Wars of Separation, Universal Belligerence: Former Hosts, Universal Belligerence: Neighboring Releases, Universal Belligerence: Nearby Nonleague States, Patron Worlds, and Great Partition.

`Scenarios!E8` contains the current Low, Medium, High, and Maximum impact paragraphs from `localisation/english/006_independence_wave_scenario_l_english.yml:23-26`, with readable intensity labels prefixed for the manual table.

`Scenarios!F8` remains `Needs Testing`; no status promotion was justified by the source-only evidence.

## Ladder and no-pre-event checks

The current automatic ladder is Calm World `3`, Gathering Storm `4`, Rising Chaos `5`, Chaos Tier `7`, Totalen Chaos `10`, and World Collapse `10`, as recorded by the current Event 006 overview and source-of-truth map.

The ladder is not appended to `Events!C7` because that cell mirrors the current in-game Event Details localisation rather than implementation summary text.

The public Event 006 report is the first player-facing indication of the wave; the scoped workbook cells contain no pre-event pressure category, mission, cost, queue, history row, early request, or retired crisis wording.

## Export and integrity evidence

The workbook loaded successfully with `openpyxl` and retained the existing `Events`, `Clusters`, `Scenarios`, and `Legend` sheets for read-only inspection.

The three existing export-only CSV snapshots were read without modification, and the Event ID `6`, Cluster ID `2`, and `SCN-008` CSV rows match their workbook rows field-for-field.

The required exporter command was not run because no workbook save occurred: `python .tools/export_event_catalog_csv.py`.

No CSV was edited directly and no export snapshot was overwritten by this audit.

## Changed cells and remaining gaps

Changed workbook path: none.

Changed workbook sheets, rows, columns, and Event IDs: none.

Changed export files or rows: none.

Blocked or `needs_user_review` cells introduced: none.

Existing status boundary retained: Event 006 `Needs Testing`, SCN-008 `Needs Testing`, and Liberations `Partially Available`.

Remaining catalog/runtime boundary: static wording is aligned, while runtime release receipts, live GUI evidence, and whole-event completion remain outside this spreadsheet audit.
