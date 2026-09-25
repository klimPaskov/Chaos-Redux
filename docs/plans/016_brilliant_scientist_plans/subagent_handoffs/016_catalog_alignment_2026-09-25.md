# Event 016 Catalog Alignment Handoff

Disposition: no workbook changes. Event 016's requested event name, event detail, four evolution details, world-end scenario wording, and cluster assignment match the committed player-facing wording and accepted design.

Audit source commit: `6566a631685222cf3b27476ee1f6207311ac27c4`.

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Workbook findings

- `Events!B17` (`Event Name`) is `Brilliant Scientist`, matching `chaosx.event_name.16` in `localisation/english/chaosx_event_names_l_english.yml:18`.
- `Events!C17` (`Details`) matches the committed `chaosx.events_log.window.event_details.brilliant_scientist` text in `localisation/english/016_brilliant_scientist_evolutions_l_english.yml:12`, including the exact conditional D’Rhondan clause when sovereignty has formed.
- The clause is selected by `GetDhrondanEventDetailClause` in `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt:9-15`. The appended wording matches `dhrondan_event_detail_clause` in `localisation/english/016_dhrondan_country_l_english.yml:139`; the fallback at line 140 is empty.
- `Events!D17:G17` (`Evo I` through `Evo IV`) match `brilliant_scientist.evolution.1.desc` through `.4.desc` in `localisation/english/016_brilliant_scientist_evolutions_l_english.yml:5,7,9,11`.
- `Events!H17` (`Evo V`) is blank, consistent with the accepted four-evolution design.
- `Events!L17` (`Cluster ID`) is blank, consistent with `docs/specs/016_brilliant_scientist_specs/README.md:111` and `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:16`, which keep Event 016 outside event clusters. No Event 016 cluster-detail wording applies. The `Clusters` sheet's row 17 is cluster ID 16, `Domestic Unrest`; that is a cluster ID, not Event 016 membership.
- The `Scenarios` sheet has no Event 016 row, so no manual scenario table fields were available to align.
- `Events!I17` (`World-End Scenario`) contains the Laboratory World and Strategic Singularity titles and descriptions. Parent follow-up compared the live cell against `chaosx.events_log.world_end.laboratory_world.title`, `.details`, `.strategic_singularity.title`, and `.details` in `localisation/english/chaosx_gui_l_english.yml:673-676`; both titles and both descriptions match. The visible super-event descriptions are a separate presentation surface with different text, so their prose is not the catalog cell's exact-text source.
- `Events!M17` remains `Needs Testing`; it was not changed or promoted to complete.

## Shared-worktree and export status

The workbook was already modified in the shared worktree before this audit. I imported and rendered the live workbook for review and wrote no workbook cells. Git `HEAD` stores the workbook as a 130-byte Git LFS pointer, which Artifact Tool cannot import as a workbook, so comparison against the committed workbook baseline was unavailable.

The working tree also has uncommitted changes to `common/scripted_effects/chaosx_event_cluster_effects.txt`, `common/scripted_effects/chaosx_events_log_effects.txt`, and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. This audit used the committed `HEAD` source as requested. Reconcile those working-tree versions if they are included in the parent’s final source state.

No workbook save occurred in this Event 016 audit, so it did not run `python .tools/export_event_catalog_csv.py`. The shared worktree currently has separate workbook and CSV modifications; their ownership and export status must be reconciled outside this handoff before staging them.

## Files changed

- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_catalog_alignment_2026-09-25.md` only.

Changed sheets, rows, cells, and workbook event IDs: none. Event 016 was audited at Events row 17. No gameplay, localisation, model, or other asset files were touched. No files were staged or committed.
