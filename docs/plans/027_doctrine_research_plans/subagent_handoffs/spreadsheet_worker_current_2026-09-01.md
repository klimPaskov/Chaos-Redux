# Event 027 spreadsheet worker handoff — 2026-09-01

## Result

The authoritative workbook was inspected against the current Event 027 localisation, cluster localisation, cluster constants, shared event-name localisation, and National Breakthroughs runtime member registry. The Event 027 row, evolution fields, cluster fields, IDs, and severities were already current, but four stale National Breakthroughs member display names were corrected.

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Changed files:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was updated in `Cluster Memberships!E52`, `E55`, `E56`, and `E57`.
- `docs/plans/027_doctrine_research_plans/subagent_handoffs/spreadsheet_worker_current_2026-09-01.md` records this handoff.
- The three export-only CSV snapshots were refreshed by the exporter and were not edited directly.

This is a spreadsheet-alignment handoff only and does not claim acceptance completion. Event 027 remains `Needs Testing`, and National Breakthroughs remains `Partially Available`.

## Changed sheets and cells

Changed sheet: `Cluster Memberships`.

Changed cells: `E52`, `E55`, `E56`, and `E57` in rows for runtime event IDs `54`, `83`, `85`, and `89`.

The workbook was saved in place with the existing sheets, tables, formatting, validations, and workbook structure preserved. The post-save workbook SHA-256 is `3B13175649159A839A3D0C38E3D4AC96DB8C278EC9A6184A500A4B1272F26706`.

## Before/after verification

The Event 027 row and National Breakthroughs cluster row were identical before and after this worker pass.

`Events!A28:M28` for catalog ID `27` and event ID `chaosx.nr27.1`:

```text
ID = 27
Event Name = Doctrine Research
Details = Military academies across the world periodically receive a shared curriculum. Each curriculum grants one choice at first and as many as five in later stages. A choice can establish a Grand Doctrine or advance one eligible subdoctrine by one mastery level.
Evo I = Each participating country receives two doctrine choices. A choice can establish one eligible Grand Doctrine or advance one eligible subdoctrine by one mastery step.
Evo II = Each participating country receives three doctrine choices. These choices can deepen one branch or develop several eligible tracks.
Evo III = Each participating country receives four doctrine choices. Established domains can divide those choices among several eligible tracks.
Evo IV = Each participating country receives five doctrine choices. A country can complete one branch or spread its mastery across several eligible tracks.
Evo V = blank
World-End Scenario = blank
Type = Minor Repeatable
Chaos level = 1
Cluster ID = 9
Status = Needs Testing
```

`Clusters!A10:H10` for cluster ID `9`:

```text
Cluster ID = 9
Cluster Name = National Breakthroughs
Details = A period of rapid institutional improvement spreads through military schools, research offices, command staffs, public agencies, and national leadership. The selected breakthrough is guaranteed, while other eligible members may join the same worldwide development cycle.
Members (ID) = 27, 54, 65, 67, 83, 85, 89
Member Severities = Medium, Medium, Low, Medium, Low, Medium, High
Type = Minor Repeatable
Chaos level = 1
Status = Partially Available
```

The following National Breakthroughs member name cells changed to the current shared event-name localisation wording:

```text
Cluster Memberships!E52: Gift from Scientists -> Random Tech
Cluster Memberships!E55: Agency upgrade -> Agency Upgrade
Cluster Memberships!E56: XP -> Experience
Cluster Memberships!E57: Tech sharing -> Tech Sharing Group
```

`Cluster Memberships!A51:F57` now matches the current National Breakthroughs runtime order, event IDs, names, and severities:

```text
slot 1 = Event ID 27 | Doctrine Research | Medium
slot 2 = Event ID 54 | Random Tech | Medium
slot 3 = Event ID 65 | Random Trait | Low
slot 4 = Event ID 67 | Generalissimo | Medium
slot 5 = Event ID 83 | Agency Upgrade | Low
slot 6 = Event ID 85 | Experience | Medium
slot 7 = Event ID 89 | Tech Sharing Group | High
```

`Cluster Memberships!G51` was also unchanged: `The selected breakthrough is guaranteed and opens one global country fanout.` This is an explicit catalog membership-summary field, not a direct in-game localisation key. No member-specific localisation exists for Event 027, so the existing summary was retained instead of inventing or substituting cluster-detail wording.

## Export

The required exporter was run from the mod root:

```text
python .tools/export_event_catalog_csv.py
```

Result: success. The exporter refreshed all three export-only snapshots without direct CSV edits.

```text
chaos_redux_events_catalog.csv — 166 rows, 13 columns, SHA-256 E8A5A833832AB5FCB76AC61B457399C386A3D6195C29B5E6E625F891ABDC8BE4
chaos_redux_clusters_catalog.csv — 20 rows, 8 columns, SHA-256 D91CBFED210ACB72A67EF46A4C48D50A0A49F023E583615628388DF276DDFB33
chaos_redux_scenarios_catalog.csv — 15 rows, 6 columns, SHA-256 05A5E47238CF23E12A3AC6BA09720106460B42A212B553563F1069E70F139EEE
```

## Remaining mismatch or review item

No mismatch remains in the Event 027 event row, evolution-detail mirror fields, National Breakthroughs cluster fields, or current member IDs, names, and severities.

Needs user review only if `Cluster Memberships!G51` is required to be a literal in-game string rather than its existing explicit summary; the source provides no member-specific localisation for that cell.
