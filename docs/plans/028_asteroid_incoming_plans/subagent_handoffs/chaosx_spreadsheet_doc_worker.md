# Event 028 spreadsheet documentation handoff

> Current workbook facts are retained below, but the completion gate remains the parent final audit and the generated CSV export. See `../final_audit.md` for the exact remaining MCP and export-verification blockers.

Catalog update status: complete for the workbook and export workflow, with source-wording blockers recorded below as needs_user_review.

## Workbook changes

The authoritative workbook updated in place is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Only the `Events` sheet, row 29 for Event ID 28, was semantically changed.

Changed cells were `Events!B29`, `Events!C29`, `Events!D29`, `Events!E29`, `Events!J29`, and `Events!N29`.

`Events!B29` changed from `Asteroid incoming` to `Asteroid Incoming`.

`Events!C29` changed from the stale minor-repeatable summary to: `A global, fire-once asteroid episode records a locked impact coordinate, its cross-border footprint, actual deaths and destruction, atmospheric dust, fragment sites, recovery decisions, and control of extraordinary mineral sites. The opening choice presents three distinct country and state coordinates plus a genuine near miss; a confirmed impact locks the coordinate for two days and destroys the centre state while three land rings are damaged across borders, leaving a permanent crater. A miss records no physical consequence.`

`Events!D29` was populated with: `Global Fragmentation — Chaos Tier, 600 Chaos, Stage 1: The chosen main body still strikes, while separated fragments hit several valid states worldwide with smaller damage rings and additional dust.`

`Events!E29` was populated with: `Extraordinary Minerals — Totalen Chaos, 800 Chaos, Stage 1, requires Global Fragmentation: Main and fragment crater control grants transferable land-division armour bonuses, with plus 100 percent from the main crater and plus 20 percent per fragment site.`

`Events!J29` changed from `Minor Repeatable` to `Major`.

`Events!N29` changed from `To Be Reworked` to `Needs Testing` pending live verification.

The type and status cell styles were aligned with the existing `Major` and `Needs Testing` workbook styles, resulting in style IDs 66 and 70 for `J29` and `N29` respectively.

`Events!A29`, `Events!F29:I29`, and `Events!K29:M29` were preserved unchanged.

No rows were added or changed on `Clusters` or `Scenarios`; Event 028 has no cluster or manual-scenario registration in the current workbook schema.

The workbook table, validations, layout, formatting, filters, freeze-pane state, and existing formulas were preserved, and the workbook contains no formulas before or after the update.

Unrelated workbook edits were preserved exactly; the final targeted verification found no semantic or style changes outside the six Event 028 cells and their required type/status style alignment.

## Export

The required command was run from the mod root: `python .tools/export_event_catalog_csv.py`.

The exporter returned `status: success` and refreshed all three export-only snapshots without direct CSV edits.

The Events export reported 166 rows and 14 columns with SHA-256 `ea442acf9bab53e85aa3057f7f7caee7a03990d5c24a891178a942d10c2dfbeb`.

The Clusters export reported 16 rows and 7 columns with SHA-256 `83b4b51268824a6974ba893c91196fc86ba509f5c4d130879d16cc5256527e50`.

The Scenarios export reported 15 rows and 6 columns with SHA-256 `05a5e47238cf23e12a3ac6ba09720106460b42a212b553563f1069e70f139eee`.

The regenerated Events CSV contains exactly one ID 28 row with the updated name, details, evolutions, type, and status, and the regenerated Clusters and Scenarios CSVs contain no Event 028 text registration.

The workbook SHA-256 after export is `55d5014399b657c3fccf4c20b3d443a284fc1612fb7d5d243c7b993e43611617`, confirming the exporter did not modify the workbook after save.

## Assets and audio

Existing Event 028 report, news, category, idea, decision, super-event DDS assets, GFX registrations, and super-event WAV/OGG audio were present and were not edited by this spreadsheet-only task.

## Blockers and needs_user_review

The current scripted event-log registry references `asteroid_incoming.event_details.history.miss`, `asteroid_incoming.event_details.history.impact`, `asteroid_incoming.event_details.history.fail_closed`, `asteroid_incoming.event_details.history.row.impact`, `asteroid_incoming.event_details.history.row.miss`, `asteroid_incoming.event_details.history.row.fail_closed`, and `asteroid_incoming.event_details.history.row.opening`, but current localisation definitions for those player-facing history/detail strings were not found.

There are duplicate `chaosx.event_name.28` definitions: Event 028 localisation names it `Asteroid Incoming`, while `localisation/english/chaosx_event_names_l_english.yml` names it `Asteroid Impact`; the workbook follows the current Event 028 title and needs localisation-owner resolution.

The current implementation constants set `evolution_ii_stage = 2`, while the accepted catalog reconciliation specifies Evolution II as Stage 1; the workbook follows the reconciliation and this contradiction needs implementation/catalog-owner review.

No gameplay, localisation, asset, skill, or unrelated documentation files were edited; this handoff is the only documentation file created by this task.
