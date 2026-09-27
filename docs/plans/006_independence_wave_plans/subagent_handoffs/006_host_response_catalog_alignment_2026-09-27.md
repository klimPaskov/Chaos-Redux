# Event 006 host-response catalog alignment

Review date: 2026-09-27

## Result

No workbook edit was applicable. The Events sheet has one parent row for catalog ID 6, `Independence Wave`, and no fields for host-response popup titles, descriptions, choices, or option tooltips. The workbook also has no separate rows for `chaosx.nr6.60`, `.61`, or `.62`. The existing `Events!C7` cell is the broad main-event Details summary; it does not mirror the individual popup decisions, so it was left intact.

The popup wording is in `localisation/english/006_independence_wave_host_response_l_english.yml`. The accepted outcome semantics are in `docs/events/006_independence_wave/host_response.md`. The localisation confirms the limited `.60`, severe `.61`, and remnant `.62` popup events; the public report and Event Details remain on the main event surface. The workbook's current row/column structure offers no host-choice field for those exact strings, and no rows were added.

## Workbook cells inspected or changed

- `Events!A1:M1` - column definitions. The sheet has `Details`, evolution details, and `World-End Scenario`, but no choice-label or option-description columns.
- `Events!A7:M7` - catalog ID 6, `Independence Wave`; reviewed the main Details, evolution, world-end, and metadata cells. No cells changed.
- `Cluster Memberships!A1:G1`, `A12:G14`, and `A68:G68` - checked Event 6 membership context; these are Liberations and Domestic Unrest memberships, not host-response fields. No cells changed.
- Workbook-wide text search found no `.60`/`.61`/`.62` IDs, host-response option labels, or host-response event/idea terms. No workbook cells changed.

## Export and shared-worktree status

The workbook was not saved, so `python .tools/export_event_catalog_csv.py` was not run. This follows the export rule, which runs after a successful workbook save. No CSV was edited or overwritten by this review.

Before this handoff was written, `git status --short` showed existing modifications to `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `docs/spreadsheets/chaos_redux_events_catalog.csv`, and `docs/spreadsheets/chaos_redux_clusters_catalog.csv`. Those shared working-tree files were left untouched; their prior contents and edits were preserved. The scenarios CSV did not appear as modified.

## Evidence and remaining scope

The workbook schema and Event 6 row do not provide a matching host-response wording field. The `.61` accepted-outcomes table uses concise outcome descriptions that are not verbatim option labels; the localisation file remains the source for player-facing text. Since no catalog cell is defined to mirror those popup choices, no needs-review cell was marked and no workbook summary was rewritten.

If the catalog later defines explicit host-response choice fields or subevent row semantics, those fields can be aligned to the exact `.60`-`.62` localisation while preserving the accepted outcomes. This review does not claim Event 006 is complete.
