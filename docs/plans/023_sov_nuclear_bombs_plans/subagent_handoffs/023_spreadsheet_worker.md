# Event 23 spreadsheet worker handoff

Disposition: `superseded by 023_spreadsheet_cluster_cleanup.md` for the final workbook state.

Disposition of this initial Events-row tranche: `implemented`; final cluster reconciliation is recorded in `023_spreadsheet_cluster_cleanup.md`.

## Changed paths

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/spreadsheets/chaos_redux_events_catalog.csv` (exporter output)
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` (exporter output)
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` (exporter output)
- `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_spreadsheet_worker.md`

Only `Events!24` (Event ID 23) was edited in the workbook; the three CSV files were refreshed by the required exporter and were not edited by hand.

## Event 23 row

| Field | Value |
| --- | --- |
| ID | `23` |
| Event Name | `SOV Nuclear Bombs` |
| Details | `The Soviet atomic arsenal opens a guarded program of production, testing, coercion, command, custody, and possible exchange. Every device remains tied to a physical depot, an accountable authority, trained delivery crews, and a release order; a Soviet collapse can scatter custody without granting immediate launch capability.` |
| Evo I | `The breakthrough becomes a wider nuclear program, expanding the event-owned stockpile and reactor network while keeping control, readiness, and accounting in tension.` |
| Evo II | `Coercive doctrine opens selected demands against valid minor powers and Soviet breakaways, with delivery evidence, target behavior, and settlement terms shaping the result.` |
| Evo III | `A valid nuclear-major rival opens retaliation and the first nonterminal exchange warning, but the world-state gate must exist before multi-major conflict can begin.` |
| Evo IV | `The widest Soviet response profile becomes available, while Soviet AI first use remains rare and requires severe strategic losses, an operational nuclear major target, a viable route, intact command, and no verified stand-down.` |
| Evo V | blank |
| World-End Scenario | blank |
| Type | `Minor Fire-Once` |
| Chaos level | `2` |
| Cluster ID | blank |
| Status | `Playable` |

## Export result

Command run from the mod root: `python .tools/export_event_catalog_csv.py`

Result: success; the exporter overwrote all three snapshots from the workbook with 166 Event rows, 20 Cluster rows, and 16 Scenario rows.

The exported Event 23 row matches the values above, including blank `Evo V`, blank `World-End Scenario`, blank `Cluster ID`, Chaos level `2`, and Status `Playable`.

## Validation limitation

The required cluster assertion is not satisfied by the current workbook source: `chaos_redux_clusters_catalog.csv` still lists Event 23 in `Military Preparation` because `Clusters!19` still contains `Members (ID) = 22, 23, 42, 56, 64`, and `Cluster Memberships!72` still records that membership. Those sheets were left unchanged because the task explicitly limited the workbook edit to the authoritative Events row; the export was not patched by hand.

The existing Events status data-validation list also does not include `Playable`; it was preserved unchanged as required.
