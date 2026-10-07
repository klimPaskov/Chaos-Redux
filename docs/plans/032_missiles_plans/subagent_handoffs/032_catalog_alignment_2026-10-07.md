# Event 32 Catalog Alignment Handoff

Disposition: implemented for the two authorized player-facing evolution-detail cells; awaiting parent review and mixed-file commit handling.

Date: 2026-10-07.

## Changes

- Updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, row 33, event id 32 (`Missiles`), column D (`Evo I`) and column H (`Evo V`).
- Ran `python .tools/export_event_catalog_csv.py` from the mod root after the workbook save. The exporter refreshed the three CSV snapshots; only the Events snapshot's Event 32 row changed semantically.
- This handoff is the only other repository file created. No localisation, gameplay, or other source file was edited.

`Events!D33` now exactly matches `missiles.evolution.saturation.body` in `localisation/english/032_missile_crisis_l_english.yml`: “Countries with working launch sites and enough industry can adopt a saturation doctrine for massed salvos. Saturation attacks can overwhelm defences, but they consume many missiles and strain readiness and command control.”

`Events!H33` now exactly matches `missiles.evolution.automatic_retaliation.body` in the same localisation file: “Governments can choose to delegate retaliation to officers or automatic warning systems. A disputed alert may be verified, delayed, or stopped by severing the network before missiles leave their sites.”

`Events!M33` remains `To Be Reworked`, as directed. The older `Needs Testing` request was not applied because accepted gameplay and validation remain incomplete. No requested wording cell is blocked or marked `needs_user_review`.

## Ownership and preservation evidence

The repository was on branch `master` at `HEAD` `0b30a383a3d27d41022a72ef05c777c15113893f`. The tracked workbook at `HEAD` is a 130-byte Git LFS pointer whose raw SHA-256 is `44da1e4d8bb45bac4bb091fe28c0d4f047cd3b42b928d26dc5358f95b29e5287`; it names LFS object `ce78dfe015137337527f383cbdf15d6ff3cb60d8d041c5416039e054d41a613e`, size 95,012 bytes. The exact local object was present and its size and SHA-256 matched the pointer; no working-tree checkout or Git index operation was used to recover it.

The pre-edit working workbook SHA-256 was `cab19ebe847011804039c7c50cd6ac65e32127b752fc96225ba9d13bd21f7dd8` (94,987 bytes). Its exact bytes, all three pre-edit CSVs, the verified HEAD LFS workbook bytes, and the consulted localisation file were preserved under `C:/Users/klimp/AppData/Local/Temp/event32_catalog_b9b9cef288af4ce89a369e90099d2c2c/` before editing.

Before the edit, `Events!D33` and `Events!H33` matched the recovered `HEAD` workbook values, so neither target cell had a concurrent working-tree change. The other pre-existing workbook semantic differences from `HEAD` were confined to `Clusters!C6`, `Events!C29`, `Events!D29`, `Events!E29`, `Events!C34`, `Events!D34`, `Events!E34`, `Events!F34`, and `Events!M34`.

The post-save semantic comparison against the preserved working workbook found exactly two changed values: `Events!D33` and `Events!H33`. All other workbook cell values remained unchanged. The target style ids stayed 35 and 39, respectively; sheet names, dimensions, tables, validation rules, conditional formatting counts, freeze panes, filters, merged ranges, row and column settings, and active sheet remained the same. No XLSX package parts were removed or added. The workbook contained zero formulas before and after the update.

The separate HEAD-based projection, made from the exact recovered HEAD LFS object and containing only the same two Event 32 cells, is `C:/Users/klimp/AppData/Local/Temp/event32_catalog_b9b9cef288af4ce89a369e90099d2c2c/head_projection/chaos_redux_events_catalog_HEAD_plus_Event32.xlsx`, SHA-256 `fd2ef88adc5ba198263ef531cdcded8bfae6a3f50faff107f5a53d9c24726580`. Its semantic comparison against the exact HEAD workbook also found only `Events!D33` and `Events!H33`; it does not contain the unrelated working-tree changes listed above.

The live workbook SHA-256 after save is `9cfac64aa2d6d734b9e1d494929b8a515edc0b99089c854bcc9b3806e5e8a53d`. Immediately before replacing it, the optimistic raw-SHA check confirmed the captured workbook hash, and checks confirmed all three CSV inputs still matched their captured hashes.

## Export evidence

Before the workbook edit, a temporary exporter run against the captured working workbook produced byte-identical outputs to all three current CSV snapshots. This established that their dirty working-tree content was already represented in the workbook before export; the pre-edit hashes were Events `4336738d42a6f81a61085e6eaFC43eb452542FF8A90E2496B50FE563EE9D467D`, Clusters `b08015ac4cc8f54cbfcb8c8a810abdaae2bfd64c7ef1d4c6afc9d2e493b83f13`, and Scenarios `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9`.

The required repository exporter completed with status `success` and reported:

- Events: 166 rows, 13 columns, SHA-256 `629183fe9c411c912d3a7ca08b73151d417669dc6000d25172b27635e8216799`.
- Clusters: 20 rows, 8 columns, SHA-256 `b08015ac4cc8f54cbfcb8c8a810abdaae2bfd64c7ef1d4c6afc9d2e493b83f13`.
- Scenarios: 17 rows, 6 columns, SHA-256 `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9`.

Comparing the exported Events CSV with the preserved input found only event id 32 changed, in CSV columns `Evo I` and `Evo V` (workbook columns D and H). The exported Clusters and Scenarios files retained their exact pre-edit bytes. No CSV was edited directly.

## Parent follow-up and limits

The workbook remains a mixed-ownership working file because the unrelated pre-existing changes are preserved. Use the HEAD-based projection above when preparing the Event 32-only workbook contribution; no Git index or commit writes were made by this worker.

Openpyxl rewrote the XLSX package, so the resulting workbook is not byte-identical to the pre-edit file; the semantic comparison confirmed only the two authorized cell values changed, and all package-part names and inspected workbook structure were preserved. No formula recalculation was needed because the workbook has no formulas.

## Parent projection review

The parent independently compared the verified HEAD LFS workbook with the isolated projection: only `Events!D33` and `Events!H33` differ, with no changed cell styles.
The working workbook still contains the nine unrelated cell changes listed above and its Event 32 wording/status matches the projection.
Running the repository exporter against that projection produced an Events CSV whose only differences from the committed baseline are event 32's `Evo I` and `Evo V` fields.
The isolated index uses the projected workbook's verified LFS pointer and that generated CSV blob, while the shared working workbook and other owners' exported rows remain untouched by staging.
