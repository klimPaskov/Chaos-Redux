# Famine and migration catalog changes pending

Disposition: accepted and queued.
Acceptance basis: round-2 lead decision 3 (Hunger Lines owner boundary) and agent decision 18 in `agent_decisions_2026-10-04.md`.
Reason queued: the workbook and its CSV exports are not edited by this owner, and the SCN-010 description localisation belongs to the Event 014 owner, so the catalog wording must follow that owner's in-game text.

## SCN-010 The Hunger Lines

Updated 2026-10-10 for [the improvement plan](improvement_plan_2026-10-10.md). The in-game scenario impact text (`chaosx.scenarios.cannibalism.impact.*` in `localisation/english/014_cannibalism_l_english.yml`) already carries the wording below; only the workbook row and its CSV export remain.

Source change: `famine_apply_hunger_lines_scenario_pressure` seizes the food stores of every region the scenario seizes and commits its starting food stage on launch day: acute shortage at Low, famine at Medium and above, for a 120-day food crisis with the ordinary famine flight.

Requested `Intensity Scaling` additions, matching the impact text:

> Low: The seized regions lose their food stores and fall into acute shortage.
> Medium: Famine grips the regions they seize.
> High: Famine grips every region they seize.
> Maximum: Famine grips every region they seize.

Spreadsheet owner action: update the SCN-010 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`.
