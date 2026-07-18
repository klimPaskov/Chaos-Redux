# Event 019 and SCN-013 Catalog Workbook Reconciliation

Date: 2026-07-18  
Scope: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, Event 19 and
`SCN-013` rows only

## Workbook changes

- `Events!A20:M20` (`ID 19`, **Infantry Spawn**) was checked against the
  current Event Details and evolution localisation. The row remains `19`,
  `Infantry Spawn`, `Minor Repeatable`, unclustered, with no world-end
  scenario, no member severity, and status `In progress`.
- `Events!C20` already matched the current player-facing Event Details text
  exactly and was preserved.
- `Events!D20:G20` already matched the current evolution title/body records
  exactly for Organized Muster, Arsenal Lottery, Command Fracture, and
  Anomalous Muster. `Events!H20` (Evo V) remains blank.
- `Scenarios!A12:F12` (`SCN-013`, **The Unbidden Muster**) retains the four
  implemented type labels and the four Low/Medium/High/Maximum intensity
  stops. Its status remains `In progress`.
- `Scenarios!C12` was extended with the current launch and safety facts:
  immediate start without ordinary event/evolution/chaos/date progression,
  intensity scaling, same-tag military takeover for one-state and all-island
  countries, connected noncapital actor regions, immediate former-parent wars,
  and the explicit non-terminal world-end outcome. The four existing type
  paragraphs were preserved verbatim from the in-game scenario detail
  localisation.
- `Scenarios!D12` and `Scenarios!E12` already matched the current four type
  labels and four intensity impact strings and were preserved. Internal
  prerequisite/bypass cleanup flag names were verified in the scenario system
  docs but intentionally not inserted into player-facing catalog prose.

No unrelated sheets, rows, styles, validations, formulas, filters, or workbook
structure were changed. The workbook contains no formulas, so no formula errors
were introduced.

## Export verification

After saving the workbook, ran:

```text
python .tools/export_event_catalog_csv.py
```

The exporter completed successfully and refreshed all three export-only
snapshots:

- `docs/spreadsheets/chaos_redux_events_catalog.csv`
  (`1015` rows, `13` columns,
  SHA-256 `7303641c56a4f5defe8827901ceda5717b1006ddd5936f76616733516fa999ce`)
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
  (`13` rows, `7` columns,
  SHA-256 `f6f68b0bd3110ce63dc5a4c54303e9d85fb9ad859cb4b2d87897d067e1088c6f`)
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`
  (`12` rows, `6` columns,
  SHA-256 `1b3a73517df6e97ad0237ef6c77f9d383a3e170eedf51a09f0f416448a70b5f8`)

The exported Event 19 row and SCN-013 row were read back and compared field by
field against `Events!A20:M20` and `Scenarios!A12:F12`; both matched exactly.

## Queued follow-up

The status-promotion follow-up was queued pending package inventory
reconciliation and the mandatory final whole-event completion audit. That audit
is now recorded in
`019_final_completion_audit_2026_07_18.md` as **PASS** with P0/P1/P2 = 0 and
explicit authorization to promote the catalog statuses.

## Final-audit status promotion addendum

The workbook-only closure edit changed exactly these two cells:

- `Events!M20`: `In progress` -> `Fully Functional` for Event 19,
  **Infantry Spawn**.
- `Scenarios!F12`: `In progress` -> `Fully Functional` for `SCN-013`,
  **The Unbidden Muster**.

No classification, content, evolution, world-end, cluster, type, intensity, or
other workbook cells changed. Event 19 remains ID 19, `Minor Repeatable`,
unclustered, Evo I-IV only with Evo V blank, and no world-end scenario. SCN-013
remains the approved four-type, four-intensity, non-terminal scenario.

After the status-only save, ran `python .tools/export_event_catalog_csv.py`
successfully. All three snapshots were refreshed:

- events CSV: 1015 rows x 13 columns, SHA-256
  `9de3113ae365c141da13f65db6740894af8dcb4d43a1ed91e813db4179dd2d30`
- clusters CSV: 13 rows x 7 columns, SHA-256
  `f6f68b0bd3110ce63dc5a4c54303e9d85fb9ad859cb4b2d87897d067e1088c6f`
- scenarios CSV: 12 rows x 6 columns, SHA-256
  `2e73a9d27e4a16629aac2d2d503fdafc26eca41e56e3d7483023d37f5d84a0df`

Every exported row was compared field-for-field with its workbook sheet. The
Event 19 and SCN-013 exports both read `Fully Functional`, and all rows in all
three snapshots match the workbook exactly. The workbook has zero formulas.
