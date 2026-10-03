# Event 027 Spreadsheet Refresh Handoff

Date: 2026-10-03

## Workbook changes

- Events row 28, event ID 27, cell M28 Status changed from Needs Testing to To Be Reworked under the supplied post-20 root policy. No Playable approval was provided or inferred.
- Cluster Memberships row 44, cluster ID 9, event ID 27, cell G44 Membership Notes changed from “The selected breakthrough is guaranteed and grants each eligible country one doctrine curriculum.” to “Optional member of the National Breakthroughs cluster.”
- The existing membership row already has severity Medium and the correct cluster, slot, event ID, and event name. The workbook has no role or participation column, so no columns were added.
- Event name, Minor Repeatable type, Chaos level 1, and Cluster ID 9 remain unchanged.
- Event Details in Events!C28 and Evolutions I–IV in Events!D28:G28 already matched their current localisation exactly and were left unchanged. Evo V and World-End Scenario remain blank.
- No Event 027 manual scenario entry was present, so none was added. The Scenarios sheet remains unchanged.
- Cluster 9 in Clusters row 10 already matched the current in-game name and detail wording. Its member IDs, severities, Minor Repeatable type, Chaos level 1, and Partially Available status remain unchanged.
- No other event or cluster status was changed. Other cluster membership rows were left unchanged.

## Wording evidence

| Catalog field | Source | Result |
| --- | --- | --- |
| Event name, Events!B28 | localisation/english/027_doctrine_research_l_english.yml, chaosx.nr27.1.t | Exact match |
| Event Details, Events!C28 | Same file, chaosx.events_log.window.event_details.doctrine_research | Exact match; already current |
| Evolution I–IV, Events!D28:G28 | Same file, evolution_details.doctrine_research.body.stage_1 through stage_4 | Exact match; already current |
| Cluster name, Clusters!B10 | localisation/english/chaosx_gui_l_english.yml, chaosx.event_cluster.national_breakthroughs.name | Exact match |
| Cluster Details, Clusters!C10 | Same file, chaosx.events_log.window.cluster_details.description.national_breakthroughs | Exact match; already current |

## Preservation and hashes

- Workbook SHA-256 before: 457BC49DC5418158899417A133BAAD242DA754C8DAB5E86D3C08DFD13250FCB0
- Workbook SHA-256 after: 3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67
- Post-save comparison found exactly the two cell-value changes listed above and no other cell or style differences.
- Sheet order, dimensions, tables, table ranges, validations, conditional formatting, filters, freeze panes, formulas, and XLSX package parts were preserved. The workbook contains zero formulas.
- Events!M28 already used the existing To Be Reworked style (style ID 72), and the To Be Reworked conditional-format rule and status dropdown option cover that cell. The Medium severity validation and style remain in place for the Event 027 membership row.

## CSV exports

Ran python .tools/export_event_catalog_csv.py from the mod root after the workbook save. The exporter returned status success.

| Export | Rows × columns | SHA-256 before export | SHA-256 after export |
| --- | --- | --- | --- |
| docs/spreadsheets/chaos_redux_events_catalog.csv | 166 × 13 | 50B4C49E87D6879CD4AFFCC6CBFB728B5D5BA99780F65556C04CE8D8D858A1ED | 465050976A1134E57945CEC56E95232E6C54FA2A8B4C5A3B569B0D638230D2C0 |
| docs/spreadsheets/chaos_redux_clusters_catalog.csv | 20 × 8 | 276964D65CAD082F678C7BBFFF4D8E89D99930B1F3707B1D8DD07BA1E3755D8A | 276964D65CAD082F678C7BBFFF4D8E89D99930B1F3707B1D8DD07BA1E3755D8A |
| docs/spreadsheets/chaos_redux_scenarios_catalog.csv | 17 × 6 | CDC1C288A885D6B62225D7D84ED6AF560F4267322D74A7A4CF4B28A7D16B124D | CDC1C288A885D6B62225D7D84ED6AF560F4267322D74A7A4CF4B28A7D16B124D |

The cluster and scenario CSVs were already marked modified in the shared worktree before this update. Their hashes were unchanged by export. No CSV was edited directly.

## Remaining limits

Per the parent correction, events/027_doctrine_research.txt defines 32 event IDs and the full owner-helper source exists. Only empty-track assignment and its first mastery step remain gated closed pending engine evidence. Grand Doctrine adoption and eligible mastery on already-assigned tracks remain available. Engine/MCP evidence for the gated path remains blocked. The catalog status remains To Be Reworked under the current post-20 root policy, with no Playable approval or full-playability claim.
