# Current workbook alignment audit: famine and migration

> **Current-status disposition (2026-10-06): superseded by** [takeover_status_2026-10-06.md](../takeover_status_2026-10-06.md) for current famine and migration status.
> This dated document remains historical evidence, with its original acceptance basis, source snapshot, audit outcome, and validation limits scoped to the work described below.
> This reconciliation grants no new design acceptance and upgrades no historical evidence to current or native validation.

Status: read-only audit. The scoped workbook content aligns with the current retirement and separation requirements. No workbook or CSV mutation was made; this report is the only new file.

## Scope and source basis

I inspected the authoritative workbook, the binding spreadsheet-worker prompt, the XLSX skill, the current famine and migration system pages, current-status and source-of-truth handoffs, and only the localized wording needed for the relevant catalog rows. I did not audit unrelated event rows or infer current facts from the export CSVs.

The current system pages describe separate famine and migration mechanics, separate problem-gated decision categories, exactly three canonical values per mechanic, and one mapmode for each mechanic available from campaign start. Their completion status remains explicitly incomplete while native, probability, adapter, and completion evidence is outstanding. The current resume packet records the accepted prospective-reception source tranche and non-advancing food observer as implemented/source-audited, while noting the remaining evidence gates. The new legacy-cost and receiver-intent work under construction was not used as verified workbook input.

Relevant current references: docs/systems/famine_system.md; docs/systems/migration_system.md; docs/plans/famine_and_migration_system_plans/current_resume_20261003.md; docs/plans/famine_and_migration_system_plans/source_of_truth_map.md. The prior spreadsheet handoffs and completion-report export figures are dated snapshots, not fresh evidence for this audit.

## Workbook result

The Events sheet has one row for catalog ID 149 at Excel row 150:

| Cell | Current value | Audit |
| --- | --- | --- |
| Events!A150 | 149 | Preserve historical ID. |
| Events!B150 | Immigrations | Preserve the retired event name. |
| Events!C150 | Retired and absorbed into the separate famine and migration mechanics through explicit adapters. Unavailable as a random event. | Matches the requested retirement role and does not describe a flat population drain. |
| Events!M150 | Unavailable | Correct for the retired event. |

Events!D150:L150 are blank. Those evolution, world-end, type, chaos-level, and cluster fields are appropriately empty for a retired, unavailable event; they are not unexplained missing detail for an active event. No replacement event ID or event row should be added.

No famine/migration system row or runtime category/prefix appears in Clusters, Cluster Memberships, or Scenarios. There are no system mapmode, event-pool, event-pacing, or flat-population-drain entries in the workbook. The workbook has no fields for the system categories, canonical values, or mapmodes; representing those systems as event records would be incorrect.

Other narrowly relevant row references remain in their own event contexts:

- Events!C6 (ID 5) contains “each use deepens famine pressure”; the full detail matches chaosx.events_log.window.event_details.soviet_collapse in localisation/english/chaosx_gui_l_english.yml.
- Events!E14 (ID 13, Evo II) says “The damage spills across state lines. Broken transport, hunger, disease, refugees, and exhausted reconstruction crews turn one ruined region into a problem for all its neighbors.” This exactly matches natural_disaster.evolution.stage_2.body in localisation/english/013_natural_disasters_l_english.yml. Events!C14 also matches natural_disaster.event_details.description.
- Events!E21 (ID 20, Evo II) says “Ports and long-distance transport carry the plague beyond its mainland cradle. Docks, troop convoys, refugees, and wartime shipping can open a second front across the sea.” This exactly matches black_plague.evolution.stage_2.body in localisation/english/020_black_plague_evolutions_l_english.yml. Events!C21 matches black_plague.event_details.description.
- Events!E16 and Events!H16 (ID 15) use migration and refugee wording in the Utopia Manifesto narrative and exactly match that event's evolution localization. These are not famine/migration system rows or category declarations.
- Events!C119 (ID 118) mentions famine, but its status remains Unavailable. The current system documentation treats the missing event owner as a separate blocker; this row was not treated as an implemented famine-system source or reused as an alias.

Current runtime-source searches found no chaosx.nr149 or Immigrations match in events, on_actions, scripted effects/triggers, decisions, or English localization. The current system pages and source-of-truth map describe the event as retired, without a replacement ID, event object, event-pool entry, event-log row, or pacing pulse. The empty Event 149 evolution and cluster fields therefore agree with the source boundary.

No scoped cell is blocked or needs_user_review based on current evidence. No wording change is recommended for the cited rows.

## Current workbook structure and formula context

Read-only openpyxl inspection found five sheets: Events, Clusters, Cluster Memberships, Scenarios, and Legend. Existing table ranges are Events A1:M1014, Clusters A1:H20, Cluster_Memberships A1:G77, and Manual_Scenarios A1:F17. The workbook-level freeze panes and worksheet auto-filter references are unset. Existing data validations remain present on Events (2), Clusters (3), Cluster Memberships (1), and Scenarios (1). No workbook structure was changed.

The workbook has zero formula cells, zero error-typed cells in formula and cached-value reads, zero defined names, and zero external links. No recalculation was needed or run. LibreOffice was not available on PATH, but the workbook contains no formulas requiring the skill's recalculation route.

## Export freshness and shared-workbook coordination

The three export-only snapshots logically match the non-empty workbook rows for Events, Clusters, and Scenarios, including the header rows, after decoding the CSV BOM. The blank formatted rows within the Events table range are not present in the Events export. The exporter was not run because this was read-only and no workbook save occurred.

| File | Length | Last write (UTC) | SHA-256 at audit start | SHA-256 at audit end |
| --- | ---: | --- | --- | --- |
| docs/spreadsheets/chaos_redux_events_catalog.xlsx | 95,215 | 2026-10-03T12:11:41.0471287Z | 3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67 | 3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67 |
| docs/spreadsheets/chaos_redux_events_catalog.csv | 62,907 | 2026-10-03T12:11:49.4353988Z | 465050976A1134E57945CEC56E95232E6C54FA2A8B4C5A3B569B0D638230D2C0 | 465050976A1134E57945CEC56E95232E6C54FA2A8B4C5A3B569B0D638230D2C0 |
| docs/spreadsheets/chaos_redux_clusters_catalog.csv | 5,375 | 2026-10-03T12:11:49.4399806Z | 276964D65CAD082F678C7BBFFF4D8E89D99930B1F3707B1D8DD07BA1E3755D8A | 276964D65CAD082F678C7BBFFF4D8E89D99930B1F3707B1D8DD07BA1E3755D8A |
| docs/spreadsheets/chaos_redux_scenarios_catalog.csv | 18,779 | 2026-10-03T12:11:49.4430191Z | CDC1C288A885D6B62225D7D84ED6AF560F4267322D74A7A4CF4B28A7D16B124D | CDC1C288A885D6B62225D7D84ED6AF560F4267322D74A7A4CF4B28A7D16B124D |

No workbook or export hash changed during this audit. The current Events export has 166 CSV records including its header, while earlier August handoffs cite different catalog counts and hashes. The current resume packet already warns that those catalog figures are historical and that Event 001–040 edits may be concurrent. This audit did not inspect unrelated row deletions, assume full-binary ownership, or overwrite another owner's work; coordinate any future workbook save with the current catalog owner.

## Handoff

- Changed workbook sheets/cells: none.
- Event IDs reviewed: 149; narrowly checked current context rows 5, 13, 15, 20, and 118.
- Recommended workbook repair: none on the present evidence; retain Events!A150:C150 and Events!M150, with Events!D150:L150 blank.
- Exporter output: not run; read-only audit made no workbook save. Existing CSV snapshots matched the workbook's exported logical rows.
- Full-system completion: not claimed; the current system documentation retains open evidence gates.
- Only new file: docs/plans/famine_and_migration_system_plans/subagent_handoffs/current_workbook_alignment_20261003.md.
