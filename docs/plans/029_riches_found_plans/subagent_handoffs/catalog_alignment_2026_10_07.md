# Event029 catalog correction handoff

Applied the current user instruction that Event029 is Minor Repeatable with no cluster. This supersedes the older D2 decision to retain clusters 7 and 15. No gameplay, event, localisation, or status cells were edited.

## Workbook delta

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Event 029 was located by its ID and name in `Events` row 30. The 14 changed cells are:

| Sheet and cell | Before | After |
| --- | --- | --- |
| Events!C30 | A random country receives a major political windfall when a valuable deposit is found in one eligible state. The discovery can transform an isolated district into a crowded mining settlement, and the mine remains tied to that state, with persistent income and industrial value following whoever controls it. Its controller must regulate claims, build transport and housing, settle the revenue, manage concessions and security, resist foreign capture, and keep extraction from outrunning public authority as workers, companies, guards, officials, criminals, and foreign interests struggle over access and control. When no valid country and state pair exists, Event Details shows N/A. | A random country receives a major political windfall when a valuable deposit is found in one eligible state. The discovery can transform an isolated district into a crowded mining settlement, and the mine remains tied to that state, with persistent income and industrial value following whoever controls it. Its controller must regulate claims, build transport and housing, settle the revenue, manage concessions and security, resist foreign capture, and keep extraction from outrunning public authority as workers, companies, guards, officials, criminals, and foreign interests struggle over access and control. |
| Events!L30 | `7, 15` | blank |
| Clusters!D8 | `18, 29, 34, 55, 57, 58` | `18, 34, 55, 57, 58` |
| Clusters!E8 | `Medium, Medium, Low, Medium, High, Medium` | `Medium, Low, Medium, High, Medium` |
| Clusters!D16 | `19, 29, 37, 42, 56, 64` | `19, 37, 42, 56, 64` |
| Clusters!E16 | `Medium, Medium, Medium, Low, Medium, Medium` | `Medium, Medium, Low, Medium, Medium` |
| Cluster Memberships!D37 | `29` | blank |
| Cluster Memberships!E37 | `Riches Found` | blank |
| Cluster Memberships!F37 | `Medium` | blank |
| Cluster Memberships!G37 | `Also Sudden Abundance at Medium severity.` | blank |
| Cluster Memberships!D61 | `29` | blank |
| Cluster Memberships!E61 | `Riches Found` | blank |
| Cluster Memberships!F61 | `Medium` | blank |
| Cluster Memberships!G61 | `Also Positive Economy at Medium severity.` | blank |

The new `Events!C30` value exactly matches `riches_found.event_details.description` in `localisation/english/029_riches_found_l_english.yml` (line 183; source SHA-256 `9af6b0156c9bb191f5e71cb76583739cbd69beaf3f75019ec7fb95f9e98b5c5c`). Membership rows 37 and 61 remain in place; their A:C cluster and slot values and all cell styles are retained. Event type and status were not edited.

## Preservation and snapshots

The workbook was already dirty before this edit. The patch used that exact working-tree binary as its base, rechecked its hash immediately before atomic replacement, and verified that all 14 cell changes were the complete cell delta. All non-target cells, formulas, and styles match the captured pre-edit workbook. The only changed XLSX package parts are `xl/worksheets/sheet1.xml`, `sheet2.xml`, and `sheet3.xml`; the other 22 of 25 package parts are byte-identical. No rows, columns, tables, defined names, data validations, conditional formatting, filters, panes, comments, or other package features were altered.

The full pre-edit cell/formula/style/native-feature inventory is retained at `C:\Users\klimp\AppData\Local\Temp\codex-chaosx-event029-catalog-08f127d10e8d4df092fa77eca508993e\catalog_before_inventory.json`. It records five sheets, zero formulas, zero defined names, four table definitions, seven data validations, 35 conditional-formatting rules, two comments, and 25 XLSX package entries.

| Snapshot | Bytes | SHA-256 |
| --- | ---: | --- |
| Before: `C:\Users\klimp\AppData\Local\Temp\codex-chaosx-event029-catalog-08f127d10e8d4df092fa77eca508993e\catalog_before.xlsx` | 95,001 | `9CFAC64AA2D6D734B9E1D494929B8A515EDC0B99089C854BCC9B3806E5E8A53D` |
| After: `C:\Users\klimp\AppData\Local\Temp\codex-chaosx-event029-catalog-08f127d10e8d4df092fa77eca508993e\catalog_after.xlsx` | 94,940 | `43E4796531CB60C77CCF2B477F84CA35A643377C27D7E8D5B1CE6CA2D9997E10` |

The isolated 14-cell value delta is retained at `C:\Users\klimp\AppData\Local\Temp\codex-chaosx-event029-catalog-08f127d10e8d4df092fa77eca508993e\event029_cell_delta.json` for the parent’s later separate catalog commit. No files were staged or committed. The mixed dirty workbook and its CSV exports are excluded from the parent’s current 10-cost-source commit.

## Export and verification

`python .tools/export_event_catalog_csv.py` exited 0 with `status: success`.

| Export | Rows × columns | SHA-256 | Pre-export snapshot comparison |
| --- | ---: | --- | --- |
| `chaos_redux_events_catalog.csv` | 166 × 13 | `f5936e217d2ac67da30b026b9426d0992261e9caf599ef74713ddb1328ef89e1` | Only row 30 columns C and L changed |
| `chaos_redux_clusters_catalog.csv` | 20 × 8 | `5c6ff98f080e5e93d96a57dd171dd665574f9372dc53002455e8ad145877f260` | Only rows 8 and 16 columns D and E changed |
| `chaos_redux_scenarios_catalog.csv` | 17 × 6 | `95d667fa6c1d5e874b0c51c61efb465b814ae484f6dc48616680238ec85dc5e9` | No row changes |

The saved workbook was reopened with the spreadsheet runtime and recalculated. Event029’s event-row cluster field was blank, both aggregate member lists and severities no longer contained ID 29, and the detailed membership sheet had no Event029 records. Before and after renders were reviewed for the Events row, Clusters sheet, and both detailed membership areas. The exporter and the workbook/package checks confirm that unrelated existing workbook and export content was retained relative to the captured dirty baseline.

## Parent review and isolated commit scope

The parent independently verified that all fourteen pre-edit target values also match the committed workbook's local LFS object `38fa97281b82b7bbdfe3d22fa5d1de7dfa5f869d54b4c35efce6153081110ce6`.
The parent reconstructed an isolated commit blob containing only those reviewed value edits, retained every cell style and all twenty-two unrelated XLSX parts, and ran the repository exporter against that commit artifact.
The artifact is Git ownership evidence, not another editable catalog source, and never replaced the current authoritative working workbook.
Its SHA-256 is `e7809a32119a5866338e8c0a27f0b68affe97669cb43373f8393f21af385fcfd`.

Other rows in the committed CSV snapshots do not yet match their committed workbook values.
The parent does not stage those unrelated reconciliation changes with Event029.
Only the exporter-generated Riches Found row and the two affected aggregate-cluster rows are retained in the isolated export patch.
No CSV value is authored manually and the current working-tree exports remain the outputs of the full authoritative workbook export.
The Scenarios export has no Event029 delta and is excluded from this commit.

Parent visual review of the Events and cluster-7 membership crops confirms the blank membership cells, unchanged surrounding rows and retained template styling.
The compact Events render does not display the entire long detail and evolution text, so it is not proof of full-cell visual fit.
The semantic detail equality is established by the saved string comparison instead.
Evolution wording alignment, final status classification and complete native visual-fit acceptance remain outside this fourteen-cell correction.
This catalog correction is not Event029 package completion.
