# Event 22 Catalog Reconciliation — 2026-09-27

Disposition: unresolved in the separate Event 22 rework; the workbook was not edited because the Event 22 design and the current event implementation/localisation disagree.

## Separate Event 22 specification

The current administration implementation contract does not schedule the Event 22 random-country event rewrite. The separate Event 22 specification records its intended identity and remains `To Be Reworked`; it is context for this catalog mismatch, not implementation evidence for the current administration plan.

The package identity records Event ID `22`, intended name `Concentration Camps`, type `Minor Repeatable`, development status `To Be Reworked`, and intended cluster `Random Chaos` in `docs/specs/022_concentration_camps_specs/022_concentration_camps_index.md:3-12`.

The acceptance criteria require Event 22 to keep ID `22`, use the name `Concentration Camps`, remove or migrate the old Spain-specific content, use type `Minor Repeatable`, join `Random Chaos`, and carry `Severe` member severity in `docs/specs/022_concentration_camps_specs/022_concentration_camps_acceptance_criteria.md:48-57`.

The catalog handoff requests those same row values and says to use a registered numeric Random Chaos cluster ID rather than inventing one in `docs/specs/022_concentration_camps_specs/022_concentration_camps_catalog_handoff.md:35-47,98-113`.

## Current Event 22 source and player-facing name

`events/022_jews_massacre.txt:1,23-24` still registers namespace `chaosx.nr22` and defines opening event `chaosx.nr22.1` with title key `chaosx.nr22.1.t`.

`localisation/english/022_jews_massacre_l_english.yml:2,4,8,13-16` still localises the opening as “Massacre of the Jews” and retains the Spain proposal and 1391 massacre text.

The shared event-name mapper resolves Event ID `22` through `GetEventName` to `chaosx.event_name.22` in `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:23,109-110`, and `localisation/english/chaosx_event_names_l_english.yml:24` currently displays “Jews Massacre”.

`events/_chaosx_news.txt:247-249` also retains the “Jews Massacre” event mapping.

The inspected Event 22 implementation and localisation do not contain the accepted camp opening, camp event-detail wording, or camp evolution-detail wording.

## Workbook values inspected

`Events!A23:M23` currently contains: `22 | Spain Antisemitism | A violent antisemitic faction emerges during the Spanish Civil War, seeks an alliance with Nazi Germany, and threatens Jewish communities across Europe. | [Evo I–V and World-End blank] | Minor Fire-Once | 1 | 18 | To Be Reworked`.

`Cluster Memberships!A72:G72` currently contains: `18 | Military Preparation | 1 | 22 | Concentration Camps | High | [blank]`.

The `Clusters` sheet has no `Random Chaos` row. Its `Random Stuff` row is cluster ID `19` and describes a separate dynamic batch event mechanic, so it does not provide a verified Random Chaos ID.

## Reconciliation decision

No workbook cell was changed because replacing the current Event Name with `Concentration Camps` would claim player-facing wording that is not present in the current Event 22 localisation or event-name mapping.

Changing the row to the current legacy label “Jews Massacre” would describe the unreworked chain rather than reconcile the accepted camp package, so that temporary relabel was also left for the package owner to resolve with the Event 22 implementation.

The cluster assignment and member name are likewise unresolved: the workbook links Event 22 to cluster ID `18` / “Military Preparation” and severity `High`, while the accepted package requires a registered `Random Chaos` membership at severity `Severe`.

Keep `Events!M23` at `To Be Reworked`, which matches the accepted package's pre-implementation status direction.

After the separate Event 22 implementation provides matching player-facing name, event-detail and evolution-detail localisation, and a registered Random Chaos cluster ID, update the Event 22 row and membership from those sources and regenerate the CSV exports. This mismatch does not justify renaming the current Event 22 row as part of the administration rework.

## Files and exports

This reconciliation created only this handoff file and made no workbook or CSV edits.

The required exporter was not run because no workbook save occurred.

At the start of this task, the workbook, `chaos_redux_events_catalog.csv`, `chaos_redux_clusters_catalog.csv`, and `common/scripted_effects/chaosx_event_cluster_effects.txt` already had worktree modifications; those pre-existing edits were left untouched.
