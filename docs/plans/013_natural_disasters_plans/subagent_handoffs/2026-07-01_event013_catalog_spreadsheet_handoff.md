# Event 013 catalog spreadsheet handoff

Workbook updated in place:
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Sheets and rows changed:
- `Events` row 14 (`ID 13`, Natural Disasters)
  - Updated `Details`, `Evo I`, `Evo II`, `Evo III`, and `World-End Scenario`
  - Event-detail and evolution wording now mirrors current in-game localisation
- `Events` row 47 (`ID 46`, Seismic Archive)
  - Updated `Details` to reflect placeholder/archive status after Event 013 integration
- `Events` row 52 (`ID 51`, Heat Wave)
  - Updated `Details` with the Event 013 relation note: Heat Wave remains separate and Event 013 heat targeting avoids stacking with `heat_wave`
- `Events` row 100 (`ID 99`, Dust Storm Archive)
  - Updated `Details` to reflect placeholder/archive status and the immediate no-log helper relation for old sandstorm callers
- `Clusters` row 9 (`Cluster ID 5`, Natural Disasters)
  - Updated `Details` to the current in-game cluster-detail wording
- `Scenarios` row 8 (`SCN-007`, Disaster Barrage)
  - Updated `Details`, `Type Options`, and `Intensity Scaling`
  - Intensity cadence now records Low `2-4 / 4-7 days`, Medium `5-8 / 2-5 days`, High `8-14 / 1-4 days`, Maximum `12-20 / 1-3 days`

Notes:
- The workbook structure was preserved. No unrelated rows were edited.
- Remaining ambiguity: the `Events` sheet has no dedicated API/helper column, so the immediate no-log helper distinction was only captured in the Event 099 relation note, not as a broader API table entry.
