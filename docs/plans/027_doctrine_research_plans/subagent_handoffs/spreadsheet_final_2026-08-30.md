# Event 027 spreadsheet final handoff — 2026-08-30

## Outcome

The authoritative workbook required a patch because the Event 027 and National Breakthroughs mirror fields did not match the current in-game Event Details, evolution-detail, and cluster-detail localization.

The only catalog source edited was [chaos_redux_events_catalog.xlsx](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/spreadsheets/chaos_redux_events_catalog.xlsx).

The three CSV snapshots were refreshed only by `python .tools/export_event_catalog_csv.py`; none was edited directly.

No gameplay, localization, specification, or non-catalog source file was edited; this required handoff is the only plan file added.

A concurrent workbook hash change was detected after the first inspection, so the guarded patch aborted, the latest workbook was re-read, and the patch was applied only after the six intended cells still contained the previously inspected values.

## Source alignment checked

All files in `docs/specs/027_doctrine_research_specs/`, `docs/events/027_doctrine_research/overview.md`, and `localisation/english/027_doctrine_research_l_english.yml` were read.

The Event 027 root and current event flow were checked in `events/027_doctrine_research.txt`.

Actorless history handling and Event Details evolution preview registration were checked in `common/scripted_effects/chaosx_events_log_effects.txt:226-228` and `common/scripted_effects/chaosx_events_log_effects.txt:3037-3059`.

Event Details and evolution title/body selectors were checked in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2245-2248`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5938`, and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:8666-8669`.

The exact player-facing source strings are `localisation/english/027_doctrine_research_l_english.yml:303`, `localisation/english/027_doctrine_research_l_english.yml:314-317`, and `localisation/english/027_doctrine_research_l_english.yml:309`.

The cluster registry confirms numeric cluster ID `9`, Calm World minimum tier, Medium severity, and the Event 027 member row in `common/script_constants/event_cluster_constants.txt` and `common/scripted_effects/chaosx_event_cluster_effects.txt`.

## Workbook cells checked and changed

### Events sheet, row 28, Event ID 27

The following metadata cells were checked and were already correct: `Events!A28=27`, `Events!B28="Doctrine Research"`, `Events!H28` blank, `Events!I28` blank, `Events!J28="Minor Repeatable"`, `Events!K28=1`, `Events!L28=9`, `Events!M28="Medium"`, and `Events!N28="Needs Testing"`.

`Events!C28` was changed to: `Military academies across the world periodically receive a shared curriculum. Each curriculum grants one choice at first and as many as five in later stages. A choice can establish a Grand Doctrine or advance one eligible subdoctrine by one mastery level.`

`Events!D28` was changed to: `Each participating country receives two doctrine choices. A choice can establish one eligible Grand Doctrine or advance one eligible subdoctrine by one mastery step.`

`Events!E28` was changed to: `Each participating country receives three doctrine choices. These choices can deepen one branch or develop several eligible tracks.`

`Events!F28` was changed to: `Each participating country receives four doctrine choices. Established domains can divide those choices among several eligible tracks.`

`Events!G28` was changed to: `Each participating country receives five doctrine choices. A country can complete one branch or spread its mastery across several eligible tracks.`

The initial synchronization values in `Events!C28:G28` were superseded when the parent revised player-facing localization; this follow-up re-read the live keys and synchronized the final strings above.

### Clusters sheet, row 10, Cluster ID 9

The following cells were checked and were already correct: `Clusters!A10=9`, `Clusters!B10="National Breakthroughs"`, `Clusters!D10="27, 54, 65, 67, 83, 85, 89"`, `Clusters!E10="Minor Repeatable"`, `Clusters!F10=1`, and `Clusters!G10="Partially Available"`.

`Clusters!C10` was changed to: `National Breakthroughs gathers repeatable advances in doctrine, production, administration, and other national institutions. Each breakthrough follows its own conditions and timing.`

The `Partially Available` status is honest because the current runtime cluster branch registers Event 027 while the remaining listed member concepts remain unreworked.

The member status cells were checked and left unchanged: `Events!N55` for ID 54 is `To Be Reworked`, `Events!N66` for ID 65 is `To Be Reworked`, `Events!N68` for ID 67 is `To Be Reworked`, `Events!N84` for ID 83 is `To Be Reworked`, `Events!N86` for ID 85 is `To Be Reworked`, and `Events!N90` for ID 89 is `To Be Reworked`.

The cluster ID and member-severity cells for those unreworked members remain blank rather than implying runtime implementation.

The `Scenarios` sheet was checked for Event 027 references and contains no Event 027 manual scenario row, so no scenario cell was changed.

## Export result and hashes

The exporter completed with `status: success`.

The final workbook SHA-256 is `ebf20975c1fba51dc68cccbc0dfbae62c7805683464a24f2422cfdc9825b972e`.

| Export sheet | Snapshot | Rows | Columns | SHA-256 |
| --- | --- | ---: | ---: | --- |
| Events | `docs/spreadsheets/chaos_redux_events_catalog.csv` | 166 | 14 | `48e639a8d8632bea3838c9c3ec8e4e473517722d3945a844666131cc4bdd75bb` |
| Clusters | `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | 16 | 7 | `77b2509d31b0e86cc20a1cfb226fa9412b31eed59ec713e9c1afe2e352a8597e` |
| Scenarios | `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | 15 | 6 | `05a5e47238cf23e12a3ac6ba09720106460b42a212b553563f1069e70f139eee` |

The exported Event 027 row and Cluster 9 row match the corresponding XLSX values after export.

## Blockers and needs_user_review

No cell was newly marked `blocked` or `needs_user_review`.

The existing `Events!N28="Needs Testing"` remains because the Event 027 implementation still has source-reported acceptance gaps for live save/reload receipt recovery, pure tag-switch validation, rendered pagination/overflow evidence, complete named-scenario probability comparisons, and evolution timing evidence.

The existing `Clusters!G10="Partially Available"` remains because the cluster member concepts for IDs 54, 65, 67, 83, 85, and 89 are still `To Be Reworked`; the cluster must not be promoted to `Playable` from catalog membership alone.

The current Event 027 handoff also records historical event-comparison baseline-caching and technology/doctrine indexer `SCAN_BYTE_LIMIT` evidence gaps; this spreadsheet pass did not alter those systems or statuses.

## Structure preservation

The workbook retains the existing four sheets, table names and ranges, data validations, blank freeze panes, blank worksheet-level filters, formulas, and target-cell styles.

No commit was created because the parent owns final integration and commit, and the worktree contains concurrent changes outside this spreadsheet scope.
