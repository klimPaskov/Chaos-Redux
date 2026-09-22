# CBRN overhaul event catalog handoff

Disposition: implemented for the bounded catalog corrections. Native raid, project transaction, achievement, and live acceptance evidence remains unresolved and is recorded below without changing catalog wording or status claims.

No gameplay, localisation, scripted localisation, or CSV source file was edited by this worker. The workbook remains the only edited catalog source.

## Workbook and export

The editable source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

The required exporter was run from the mod root with `python .tools/export_event_catalog_csv.py` after the workbook save.

The exporter completed successfully with 166 Event rows and 13 columns, 20 Cluster rows and 8 columns, and 16 Scenario rows and 6 columns, including headers.

The refreshed export hashes are `4716de683b33fd184a0d6dc37b9d3fe908bb121b515e662100bca85ed660851f` for `chaos_redux_events_catalog.csv`, `689fe07883da14abe2ceb7c29c151db50808cf97a366e60808281b16e37c76a2` for `chaos_redux_clusters_catalog.csv`, and `8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7` for `chaos_redux_scenarios_catalog.csv`.

The workbook still loads with the existing five sheets, four existing tables, two Events validations, three Clusters validations, one Cluster Memberships validation, and one Scenarios validation. It contains no formulas requiring recalculation.

## Changed catalog cells

- Event 016, Excel row 17, `Events!L17` was cleared. The current Event 016 overview states `Cluster: none`, and `load_event_cluster_members` has no Event 016 member definition. The previous catalog value `9` was stale.
- Event 024, Excel row 25, `Events!D25`, `Events!E25`, and `Events!F25` now contain only the exact evolution detail bodies from `video_game_in_sweden.evolution.1.body`, `.2.body`, and `.3.body`. The separate titles remain owned by the in-game evolution title selector as required by the event-log contract.

## Validated unchanged rows and source keys

- Event 016 `Events!C17` matches `chaosx.events_log.window.event_details.brilliant_scientist` plus the conditional `dhrondan_event_detail_clause`. The D’Rhondan apostrophe is U+2019 in the workbook and already matched `dhrondan_event_detail_clause`, so no detail edit was necessary. Evolution bodies match `brilliant_scientist.evolution.1.desc` through `.4.desc`.
- Event 020 `Events!C21`, `Events!D21` through `Events!H21`, and `Events!I21` match `black_plague.event_details.description`, `black_plague.evolution.stage_1.body` through `.stage_5.body`, and `chaosx.events_log.world_end.black_plague.details`. The catalog Cluster ID `13` and the Cluster Memberships row for Event 020 remain aligned with the Diseases catalog row and its Severe severity. The runtime cluster constant is 8, while catalog Cluster ID 13 is the workbook's stable catalog identity.
- Event 020 scenario row `Scenarios!A12:F12` remains aligned with `chaosx.scenarios.black_plague.name`, `.desc`, and `.impact.low` through `.impact.maximum`. The current constants still resolve to 14, 28, 52, and 90 established states, 2, 3, 4, and 6 lesser brood basins, and 1, 2, 4, and 8 Royal Basin states.
- Event 024 `Events!C25` matches `chaosx.event_details.24`. The retired `video_game_in_sweden_field_validated` and `video_game_in_sweden_field_validated_desc` wording was absent from the workbook, so no separate stale-text edit was required.
- Event 026 `Events!C27` and `Events!D27` match `black_friday.event_detail.premise` and `black_friday.evolution.1.body`. `Events!M27` remains `Needs Testing`, matching the current Event 026 completion gate.

## Unresolved rows and evidence boundaries

- `Events!M17` remains `Needs Testing` because Event 016 native biological transaction acceptance, tranche-four source review, and live validation remain open.
- `Events!M21` and `Scenarios!F12` remain `Needs Testing` because the current Black Plague package retains live validation and the documented scenario rollback limitation.
- `Events!M25` remains `Needs Testing` after the Field-Validated Planner removal. The workbook contains no retired planner wording, and no approval was found to promote its status.
- `Events!M27` remains `Needs Testing`. The current Black Friday handoff documents the native raid achievement bridge, cancellation or reservation handling, and live acceptance as unresolved. No achievement or native raid outcome was inferred.
- Native biological raid IDs, CBRN project access, and the widened Event 016 special-project routes are implemented in current source files, but the catalog schema has no dedicated raid or project-access field and the Event 016 Event Details localisation does not expose those implementation surfaces. No new prose was invented for `Events!C17` or any other mirror field. Parent review is still needed if a future approved catalog schema adds a player-facing field for those surfaces.

No commit was made by this worker.
