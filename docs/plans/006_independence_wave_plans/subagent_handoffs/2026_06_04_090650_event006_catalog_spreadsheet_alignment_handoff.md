# Event006 Catalog Spreadsheet Alignment Handoff

Role: `chaosx_spreadsheet_doc_worker`

Supersession note: this handoff records the 79-focus catalog state before the Circassian Mountain Council package tranche. The current Circassian-inclusive catalog/tree state is documented in `2026_06_04_092851_parent_event006_circassian_package_handoff.md`.

## Scope

- Updated only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
- Added this one timestamped handoff.
- No gameplay, localisation, GFX, assets, flags, specs, event docs, or other markdown files were edited.
- Event006 is not marked complete. Workbook status remains `In progress`.

## References and Facts Verified

- Offline Paradox wiki snapshot consulted before implementation reads: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.
- Vanilla docs consulted under `/home/klim/projects/Hearts of Iron IV/documentation`: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.
- `xlsx` skill used for workbook handling requirements and validation expectations.
- Focus recount command found `79` current `focus = {` blocks in `common/national_focus/006_independence_wave_focus.txt`.
- Current-state facts were cross-checked against `docs/events/006_independence_wave.md`, `2026_06_04_085712_event_completion_audit.md`, `2026_06_04_090019_parent_event006_completion_audit_focus_loc_fix.md`, and the stale prior catalog handoff.

## Workbook Edits

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Sheet: `Main Sheet`

Row: `7` / Event006 / Independence Wave

Changed cells:

- `C7` Details
  - Before snippet: `Every release receives Event 006 origin, release dossiers, startup support, the shared 60-focus provisional tree...`
  - After snippet: `Every release receives Event 006 origin, release dossiers, startup support, the shared 79-focus Liberation Provisional tree...`
  - Also added current verified starter-package coverage, current super-events, 19 Event006 achievements, Event005 separation, host-survival rule, and explicit `In progress` blocker wording.
- `G7` Evo IV
  - Before snippet: `current starter proofs cover Volga/OGB, Assyria, Danzig, Buganda, Sokoto, Guarani, Charrua, Kurdistan, and Timetable Authority formations.`
  - After snippet: `current starter proofs cover Volga/OGB, Assyria, Danzig, Free Port, Canal, Municipal, Protected Mandate, Oil Protectorate, Buganda, Sokoto, Bukhara, Khiva, Barotse, Dahomey, Miskito, Itza, Maya, Guarani, Charrua, Kurdistan, and Timetable Authority formations.`
- `H7` Evo V
  - Before snippet: `Strange releases can open Sealed Dossier work, containment review, impossible-state recognition, anti-mankind doctrine...`
  - After snippet: `Strange releases can open Sealed Dossier work, Archive-State or Necromantic Custodianship identities, containment review, impossible-state recognition, anti-mankind doctrine...`
- `J7` World-End Scenario
  - Before snippet: `bounded super-events such as league formation, partition week, old-name return, impossible state, league war, human renunciation, and rump-host survival.`
  - After snippet: `bounded super-events: first league, league war, first old name, great partition week, first impossible state, human renunciation, and rump-host survival.`
- `O7` Liberations cluster details
  - Before snippet: `manage dossiers, congresses, patrons, borders, formations, package overlays, report events, super-events, and achievements without using Event005 state.`
  - After snippet: `manage dossiers, congresses, patrons, borders, formations, package overlays, the 79-focus Liberation Provisional tree, report events, super-events, and 19 current achievements without using Event005 state.`
  - Also added explicit `In progress` blocker wording.

Unchanged status cells:

- `L7`: `In progress`
- `R7`: `In progress`

## Validation

- Workbook package integrity:
  - Command: `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx`
  - Result: all entries `OK`; no compressed-data errors detected.
- Workbook opens:
  - Command: `libreoffice --headless --convert-to xlsx --outdir /tmp/... docs/spreadsheets/chaos_redux_events_catalog.xlsx`
  - Result: `rc=0`; LibreOffice produced a validation copy.
- Focus count:
  - Command: `rg -n '^\\s*focus\\s*=\\s*\\{' common/national_focus/006_independence_wave_focus.txt | wc -l`
  - Result: `79`
- Formula and error scan:
  - Command: Python XLSX worksheet XML scan for `<f>` cells and Excel error literals.
  - Result: `formula_count 0`, `error_hits []`, `stale_60_focus_hits []`.
- Readback:
  - Python worksheet readback confirmed the changed `C7`, `G7`, `H7`, `J7`, and `O7` values, and confirmed `L7` and `R7` still read `In progress`.
- Preservation note:
  - The edit changed only inline string values in `xl/worksheets/sheet1.xml`; workbook tables, styles, dimensions, and sheet structure were not rebuilt.

## Remaining Blockers

- Event006 remains incomplete.
- Remaining blockers include future package/formable depth, deeper package overlays, richer scripted-GUI states, final animated/category assets, future catalog rows, and final validation.
- No flags were created or edited in this tranche.
