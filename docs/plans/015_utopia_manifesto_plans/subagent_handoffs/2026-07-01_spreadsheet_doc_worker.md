## Event 015 Spreadsheet Handoff

Workbook updated in place:
`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Scope kept to Event 015 only. No other workbook rows or sheets were edited.

### Sources used

- `docs/events/015_utopia_manifesto.md`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`

### Exact workbook cells changed

Sheet: `Events`
Row: `16`
Event ID: `15`

- `B16` -> `Utopian Manifesto`
- `C16` -> replaced stale implementation summary with the final in-game event detail wording
- `D16` -> updated to the final `Utopian Ledger` wording
- `E16` -> updated route labels to `Living Humanism`, `Common Store State`, `Guild Commonwealth`, `Island Discipline`, and `Marked Bounds`
- `F16` -> updated Needful Land / integration wording using final in-game names and descriptions
- `G16` -> updated to `Marked Bounds Clause` wording
- `H16` -> updated late-outcome names to final in-game wording
- `I16` -> `None; no world-end scenario.`
- `M16` -> `Implemented`

No `Clusters` sheet cells were changed. Event 015 currently has no cluster ID in the workbook.

No `Scenarios` sheet cells were changed. No Event 015 manual scenario row was present or requested by the workbook structure.

### Verification performed

- Confirmed Event 015 row location and existing workbook conventions before editing.
- Saved only cell-value changes in `Events!16`.
- Reloaded the workbook after save and verified:
  - same sheet set
  - same row/column counts on every sheet
  - same freeze panes (`Events!A2`)
  - same autofilter refs
  - unchanged style IDs on every edited cell
- Confirmed the Event 015 status now matches the existing completed status label already used by nearby finished rows: `Implemented`

### Blockers / needs_user_review

- None.
