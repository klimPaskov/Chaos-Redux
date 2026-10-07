# Catalog identifier sync handoff

The catalog identifier repair is complete in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

The accepted cluster identity allocation is Diseases 13 → 8, Random Stuff 19 → 12, and Pacts 12 → 13.

The workbook has 11 changed cells across Events, Clusters, and Cluster Memberships; all are Cluster ID literals and references.

Events rows updated: 3 (event 2, Zombie Outbreak), 12 (event 11, Secret Alliance), 21 (event 20, The Black Plague), and 42 (event 41, Disease in Divisions).

Clusters rows updated: 13 (Pacts), 14 (Diseases), and 20 (Random Stuff).

Cluster Memberships rows updated: 55–58 (Pacts slot 1; Diseases slots 1–3).

The eight dependent references were necessary because Events.Cluster ID and Cluster Memberships.Cluster ID repeat the cluster identity keys.

No event memberships, slot order, event IDs, severity values, names, descriptions, statuses, tuning, formulas, schemas, or scenario IDs changed.

No planned scenario rows SCN-020 through SCN-032, planned clusters 21 or 22, or Fallout scenario 14 were added.

## Replay delta

The exact old/new values, semantic row guards, storage types, style IDs, and sheet coordinates are in [cell_delta.json](cell_delta.json).

For isolated commit integration, apply those cell literals to the target HEAD workbook in place after checking each identity guard and old value; preserve other workbook contents and package parts.

The delta file permits an already-updated value and requires a stop on any unexpected value.

## Preservation and verification

The source workbook matched the supplied immutable baseline hash `43e4796531cb60c77ccf2b477f84ca35a643377c27d7e8d5b1ce6ca2d9997e10` before editing.

The updated workbook hash is `c945a81b16454de68468f73d43348612828df76eae463973626990af06a91a29`.

Only `xl/worksheets/sheet1.xml`, `sheet2.xml`, and `sheet3.xml` changed; each difference is confined to the 11 declared cell literals.

All other ZIP member payloads, the member inventory and order, and ZIP member metadata remained identical.

The candidate reopened without library warnings, retained the target cells’ original storage types and styles, and matched all non-target cells and workbook structure.

Cluster primary IDs are unique, all membership and event cluster references resolve, and the ordered member/severity lists for Pacts and Diseases still match their aggregate rows; Random Stuff remains memberless.

Scenario identifiers and scenario sheet contents remained unchanged.

## Exporter

Ran `python .tools/export_event_catalog_csv.py` from the mod root; it returned success and refreshed all three generated snapshots.

- Events: 166 rows including header, 13 columns, SHA-256 `4e151015dc928d6f69183eb40e4e15fb5ec0a81a0d0dcd972e42689a20aa2801`.
- Clusters: 20 rows including header, 8 columns, SHA-256 `97c6a331e832519e87a075d6f9b13744b4249245d56d7b58162188f0adbc7106`.
- Scenarios: 17 rows including header, 6 columns, SHA-256 `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9`.

Parsed CSV content matches the corresponding workbook sheets, including the expected headers, column widths, and UTF-8 BOM.

No unresolved catalog cells or simplifications remain within this identifier repair.
