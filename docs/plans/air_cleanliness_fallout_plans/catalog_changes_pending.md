# Fallout catalog changes pending

Owner: Fallout workstream. Disposition: accepted and queued. Acceptance basis: agent decision recorded by the lead for round 1 (decision 5, 2026-10-04) under the user's grant of full design authority. It stays queued because the Fallout workstream may not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or the exported CSV files; the catalog owner applies it and then runs `python .tools/export_event_catalog_csv.py`.

## SCN-014 Scenarios row

Manual scenario `#014` (`chaosx.scenarios.entry.id.fallout`) is live in the scenario list and is the only active scenario id with no Scenarios row. Add this row to the Scenarios sheet:

| Field | Value |
| --- | --- |
| Scenario ID | `SCN-014` |
| Scenario Name | `Fallout` |
| Details | `A thermonuclear strike hits every valid province. Seven days later the Fallout blackout begins. The population collapses, surviving countries are thrown back, all wars end, and a new fractured map takes shape.` |
| Type Options | `Total Strike` |
| Intensity Scaling | `Low, Medium, High, and Maximum set the aftermath severity, which raises the damage grade of every state and with it population loss, building damage, and the resources survivors start with. Every intensity strikes every valid province.` |
| Status | `Needs Testing` |

Sources: `chaosx.scenarios.fallout.name`, `chaosx.scenarios.fallout.desc`, and `chaosx.scenarios.type.fallout` in `localisation/english/chaosx_gui_l_english.yml`; the intensity mapping in `fallout_manual_submit_standard_request_internal` (standard, severe, terminal, and maximum requests) and its use as the request component of the state grade in `common/scripted_effects/fallout_consolidated_effects.txt`.

## Events and Clusters

No change. The Events and Clusters sheets stay free of Fallout rows. Fallout is a world-end state with its own living-world events, not a catalog event, and its survivor chains are internal candidates rather than public event registrations.
