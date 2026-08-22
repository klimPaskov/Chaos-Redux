# Event 006 catalog reconciliation — 2026-08-22

Date: 2026-08-22.

Owner: `/root/event6_catalog_reconcile_3`.

Scope: Verify and reconcile the authoritative Event 006 workbook and its generated CSV snapshots against the current player-facing Event Details, evolution, and cluster localisation. No gameplay, localisation, scripted localisation, source-map, resume-packet, or audit files were changed.

## Workbook result

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

The workbook was already at the current authoritative wording in the shared worktree, so no cell-value mutation was necessary and no unrelated workbook structure was rewritten.

Verified Event 006 (`Events` row 7, ID `6`, `Independence Wave`) fields:

- `Events!B7` — `Independence Wave`.
- `Events!C7` — exact current Event Details text, beginning `New governments have taken control of capitals, ministries, and borders across several regions.` It contains the dynamic join thresholds and rival-bloc detail placeholders and contains no retired pre-event pressure or category wording.
- `Events!D7` — exact Evolution I title/body: `The Manuals Cross the Border`.
- `Events!E7` — exact Evolution II title/body: `Old Nations Wake`.
- `Events!F7` — exact Evolution III title/body: `Flags Rise Behind the Barracks`.
- `Events!G7` — exact Evolution IV title/body: `The Sovereigns Take Their Seats`.
- `Events!H7` — exact Evolution V title/body: `No Border Is Final`.
- `Events!J7:N7` retained the current catalog metadata: `Minor Repeatable`, chaos level `1`, cluster `2`, `Medium`, and `Partially Available`.

Verified Liberations cluster (`Clusters` row 3, cluster ID `2`) fields:

- `Clusters!B3` — `Liberations`.
- `Clusters!C3` — exact current cluster detail: `Liberation shocks create new countries, break old chains of command, and turn subject or republic disputes into broader independence crises.`
- `Clusters!D3:G3` retained members `5, 6`, type `Minor Repeatable`, chaos level `1`, and status `Partially Available`.

## Source localisation keys checked

- `localisation/english/chaosx_event_names_l_english.yml`: `chaosx.event_name.6`.
- `localisation/english/chaosx_gui_l_english.yml`: `chaosx.events_log.window.event_details.independence_wave`, `chaosx.event_cluster.liberations.name`, and `chaosx.events_log.window.cluster_details.description.liberations`.
- `localisation/english/006_independence_wave_evolutions_l_english.yml`: `independence_wave.evolution.1.title`, `.1.body`, through `.5.title`, `.5.body`.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: `GetEventsLogEventDetailDescription` dispatches Event ID 6 to `chaosx.events_log.window.event_details.independence_wave`; `GetEventsLogEventDetailEvolutionTitle`/`GetEventsLogSelectedEvolutionTitle` dispatch the five evolution title keys; `GetEventsLogEventDetailEvolutionBody`/`GetEventsLogSelectedEvolutionBody` dispatch the five evolution body keys; `GetEventsLogSelectedClusterName` dispatches `chaosx.event_cluster.liberations.name`; and `GetEventsLogSelectedClusterDescription` dispatches `chaosx.events_log.window.cluster_details.description.liberations`.

## Export result

Ran from the repository root:

```text
python .tools/export_event_catalog_csv.py
```

Result: `status: success`.

Refreshed export-only snapshots:

- `docs/spreadsheets/chaos_redux_events_catalog.csv` — Events, 183 rows reported by exporter, 14 columns, SHA-256 `25e79832048b3ffbf2ee2a0746a3e1717e5db248be188ce8d2f081a2e71fbe29`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` — Clusters, 14 rows reported by exporter, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` — Scenarios, 12 rows reported by exporter, 6 columns, SHA-256 `8d31d120dd81adb3ef48bae2afed8cf539bb4f23a60b04771c1eacc57875a398`.

Export verification found Event ID `6` with the same `Events!C7` wording and cluster ID `2` with the same `Clusters!C3` wording.

## Blocked or needs_user_review cells

None for the requested Event 006 event-detail, evolution, or Liberations cluster mirror fields.

## Remaining documentation risks

- The two same-day catalog handoffs retain different process histories: one records a C7 replacement, while the independent reconciliation records that C7 already matched after normalisation. The final workbook and export state agree; this provenance discrepancy remains for parent review.
- Event 006 remains `Partially Available`, the Liberations cluster remains `Partially Available`, and SCN-008 remains `Unavailable`; this catalog reconciliation does not change those implementation-status dispositions.
- The whole-event source-of-truth map and resume packet still govern the broader HOLD/PARTIAL boundary and unresolved package, probability, GUI, and runtime-evidence gaps.
