# SCN-013 Scenario Catalog Dynamic Registry Handoff — 2026-08-22

## Scope

Updated the Event 19 direct scenario catalog entry for `SCN-013`, **The Unbidden Muster**, in the editable workbook only. No gameplay or localisation files were changed.

## Workbook change

- Exact cell: `Scenarios!C11` (`SCN-013` Details).
- Before semantic summary: **The Impossible Host** described only nonhuman formations and specifically named zombie, ghost, and golem hosts.
- After semantic summary: **The Impossible Host** says complete host lineages rise under regional commands; any full host able to take the field may answer the call, including engineered, anomalous, and nonhuman strains, with immediate wars and armed breakaways.
- The four type options, four Low/Medium/High/Maximum intensity stops, `Playable` status, microstate wording, terminal-world wording, and all other workbook content were preserved.
- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Export result

Ran from the mod root after the workbook save:

```text
python .tools/export_event_catalog_csv.py
```

Exporter status: `success`.

- `chaos_redux_events_catalog.csv`: 183 rows, 14 columns, SHA-256 `edb2ac0048cfcf17b1f64de320cf7066132fc72491241c3ceed0921cc91a6bc9`
- `chaos_redux_clusters_catalog.csv`: 14 rows, 7 columns, SHA-256 `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`
- `chaos_redux_scenarios_catalog.csv`: 12 rows, 6 columns, SHA-256 `a0ec93899e3a07855fe55cc593b76a68fc8adaf88c47b09ca6ed1f6b88dc7e14`

Readback confirms the exported `SCN-013` row matches the workbook and differs from its prior version only in Details (`column 3`).

## Remaining blockers

None for this bounded catalog correction. A pre-existing concurrent `SCN-010` intensity edit remains preserved in the workbook and refreshed exports; it was not changed by this handoff.

