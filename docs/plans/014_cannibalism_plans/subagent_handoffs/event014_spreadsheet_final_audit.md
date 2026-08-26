# Event 014 Spreadsheet Final Audit

> Historical source-side audit from 2026-08-22. The workbook row and scenario status are now `Needs Testing` while live consumer, MCP/GUI, probability, provenance, portrait, and super-event review gates remain open; this handoff does not close those gates or authorize a completion claim.

Date: 2026-08-22

## Scope

Audited and updated only the Event 014 catalog surfaces in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

The workbook uses the current `Events!A:N` schema: `Chaos level` is column K, `Cluster ID` is column L, `Member Severity` is column M, and `Status` is column N. The current scenario table places `SCN-010` on row 9, with `SCN-009` on the neighboring row 10.

## Workbook changes

- `Scenarios!E9` (`SCN-010` Intensity Scaling) was replaced with the exact four current localisation descriptions for Low, Medium, High, and Maximum intensity.
- `Events!A15:N15` (Event ID 14) was audited and retained. Its current player-facing baseline, three evolution entries, two terminal entries, type, chaos level, blank cluster fields, and status are exact.
- `Scenarios!A9:F9` (`SCN-010`) was audited. Its identity, five type descriptions, five type names, corrected intensity descriptions, and status are exact.
- Existing concurrent Event 014 wording changes already present in `Events!C15:E15` were preserved because they match the live localisation exactly.
- `Scenarios!A10:F10` (`SCN-009`) was not modified.

Changed workbook cell: `Scenarios!E9`.

Event ID: `14` (`chaosx.nr14.1`). Scenario ID: `SCN-010`.

## Source evidence

- `events/014_cannibalism.txt` defines the canonical entry `chaosx.nr14.1`.
- `common/scripted_effects/chaosx_logic_effects.txt` registers Event 014 in `global.fire_once_events`; no Event 014 member appears in the `Clusters` sheet.
- `localisation/english/014_cannibalism_l_english.yml` supplies the exact pre-reveal Event Details text, all three evolution title/description pairs, SCN-010 name, five scenario type descriptions and names, and four intensity descriptions.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` gates Evolution III and revealed details behind `cannibalism_reveal_complete` and supplies the live Event Details selector order.
- `localisation/english/chaosx_gui_l_english.yml` and the world-end localisation registry supply the two independent terminal titles and details: `The World Is the Larder` and `No Thaw Will Come`.
- `docs/events/014_cannibalism/overview.md` and `docs/specs/014_cannibalism_specs/` cover the open, concealment, exploitation, warlord, convergence, ordinary terminal, Wendigo terminal, and defeat-aftermath routes.
- `docs/achievements/014_cannibalism/achievements.md` contains 18 distinct Event 014 achievement identifiers.

## Acceptance checks

- Event 014 is `Minor Fire-Once`, chaos level `1`, and has blank `Cluster ID` and `Member Severity` fields.
- The baseline and all three evolution cells are populated in `Events!C15:F15`; `Evo IV` and `Evo V` remain blank.
- The two terminal branches remain distinct in `Events!I15`.
- SCN-010 has exactly five types in `Scenarios!D9`: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- Pre-reveal fields (`Events!C15:E15` and `Scenarios!B9:E9`) contain no `Hannibal`, `Lecter`, `Prison Host`, `ancient-general`, or `ancient general` text.
- The five scenario types contain no Prison Host and no ancient-general disclaimer.
- The 18 achievement identifiers were counted from the current Event 014 achievement documentation.
- The current workbook status vocabulary is unchanged, but `Events!N15` and `Scenarios!F10` are currently `Needs Testing` pending the open downstream review gates. The status is deliberately not presented as a completion claim.

## Workbook and export validation

- Workbook saved in place at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- `python .tools/export_event_catalog_csv.py` completed successfully after the save.
- Exported snapshots refreshed by the tool: Events 183 rows by 14 columns, Clusters 14 rows by 7 columns, Scenarios 12 rows by 6 columns.
- Export hashes reported by the tool: Events `edb2ac0048cfcf17b1f64de320cf7066132fc72491241c3ceed0921cc91a6bc9`, Clusters `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299`, Scenarios `dd42e7864c7ca520f1b3e5e65e92b51330ba13b2ca35341801a7ae7c48c7adc5`.
- Formula count is zero and no Excel error values were found.
- Existing structure is intact: sheets `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend`; tables `Events!A1:N1015`, `Clusters!A1:G15`, and `Scenarios!A1:F12`; existing data-validation and conditional-format ranges; existing row heights, styles, wrapping, borders, fills, and no-freeze/no-auto-filter settings.
- A LibreOffice PDF render was inspected at the Event 014 baseline, evolution, terminal/type, and SCN-010 type/intensity pages. Text is wrapped, terminal/type/status fills remain visible, and the SCN-010 intensity cell has no clipping or overlap.

## Blockers and simplifications

This historical source-side audit did not cover the later live-consumer, MCP/GUI, probability, provenance, portrait, or super-event review gates. The current workbook therefore remains `Needs Testing`. No fallback or invented wording was used, and the CSV snapshots were not edited directly; they were refreshed only by the required exporter.
