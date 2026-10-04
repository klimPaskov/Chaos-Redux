# Event Catalog Fact Check — 2026-09-27

Disposition: the requested player-facing catalog mirror fields are current, so this check made no workbook edits.

## Workbook fields checked

- `Events!A6:M6` (event ID 5, Soviet Union Collapse): `Details` in `C6` matches `chaosx.events_log.window.event_details.soviet_collapse` in `localisation/english/chaosx_gui_l_english.yml:697`. Evolution fields `D6:H6` match the current secession evolution detail titles and bodies in the same file, including the stage 5 rupture and the high-chaos fringe-breakaway text at lines 791-815.
- `Clusters!A19:H19` (cluster ID 18, Military Preparation): `Details` in `C19` matches `chaosx.events_log.window.cluster_details.description.military_preparation` in `localisation/english/chaosx_gui_l_english.yml:437`.
- A workbook-wide text scan found no catalog event-detail or evolution field for the captured-UWR blacksite aftermath or the Italy Libya security sweep. The UWR decision wording is in `localisation/english/005_soviet_collapse_l_english.yml:8741-8753`; the Italy sweep wording is in `localisation/english/camp_repression_country_kits_l_english.yml:524-547`. These are decision mechanics, so no event catalog entry was added.

## Unresolved workbook inconsistency

`Cluster Memberships!A72:G72` assigns event ID 22 to “Concentration Camps” in the Military Preparation cluster, while `Events!A23:M23` currently identifies event ID 22 as “Spain Antisemitism.” The intended cluster membership cannot be established from the requested player-facing mirror fields, so this non-mirror membership row was left untouched for owner review.

## Files and exports

This check did not save the workbook or run the CSV exporter. At the final status check, the shared worktree already showed modifications to the catalog workbook and the Events and Clusters CSV snapshots; these changes were not made by this check and were left untouched. This handoff note is the only file created by this check.
