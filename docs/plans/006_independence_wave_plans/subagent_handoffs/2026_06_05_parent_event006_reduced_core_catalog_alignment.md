# Event006 Reduced Core Catalog Alignment

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `docs/events/006_independence_wave.md`, and `docs/plans/006_independence_wave_plans/source_of_truth_map.md`.

- Updated the Event006 workbook row to mention reduced starts recovering surveyed unowned cores through the Border Commission without consuming protected host states.
- Updated the Event006 workbook notes to include reduced-core recovery in the current management surfaces.
- Updated the event doc and source-of-truth map so catalog parity reflects the new reduced-core recovery decision.

## Workbook Method

`openpyxl` is not installed in the environment, so the workbook was edited through exact replacement in `xl/sharedStrings.xml` inside the `.xlsx` package. The edit only touched the Event006 row strings for `C7` and `O7`; workbook sheets, relationships, styles, tables, and other rows were left intact.

## Validation

Passed parent validation:

- Re-read Event006 row `C7` and `O7` from the saved workbook XML and confirmed the reduced-core recovery wording is present.
- Confirmed stale `125-focus`, `Kuban`, and `Altai` workbook strings are absent.
- Confirmed current `50-focus` workbook wording remains present.
- `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx` reported no compressed-data errors.
- Scoped documentation brace-balance and `git diff --check` validation passed after the docs patch.

## Remaining Scope

This is a catalog/docs alignment patch only. Event006 still needs final completion audit, final asset/UI validation, remaining package/formable scope closure, and any future spreadsheet updates after additional gameplay changes.
