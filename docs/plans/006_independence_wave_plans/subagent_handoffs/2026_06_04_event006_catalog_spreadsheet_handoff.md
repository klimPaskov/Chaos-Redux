# Event006 Catalog Spreadsheet Handoff

Date: 2026-06-04

Supersession note: this workbook row was updated again in
`2026_06_04_090650_event006_catalog_spreadsheet_alignment_handoff.md`
after the Event006 focus tree reached 79 focus blocks. Treat that later handoff
and the workbook itself as the current catalog evidence.

## Scope

Audited and updated only the Event006 catalog workbook row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

No gameplay, localisation, flag, country, history, asset, spec, Event005, or general docs files were edited. This pass does not claim Event006 completion.

## Sources Inspected

- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_parent_event006_wiring_audit_alignment_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_parent_event006_report_callsite_wiring_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_01_event006_completion_audit_remaining_gaps_after_rump.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_01_event006_starter_package_current_audit_handoff.md`

## Workbook Sheets and Rows Inspected

- `Main Sheet`
  - Event table row `7`, cells `A7:L7`: Event006 primary catalog row.
  - Adjacent cluster table row `7`, cells `N7:R7`: Liberations row listing Event ID `6`.
  - Table definitions checked: `Events` range `A1:L1017`; `Event_Clusters` range `N1:R16`.
- `Info`
  - Empty sheet; no Event006 content.

Workbook structure notes:

- The workbook stores these catalog values as plain inline strings in `xl/worksheets/sheet1.xml`.
- No formula cells were found in `sheet1.xml` or `sheet2.xml`.
- `openpyxl` was not installed in this environment, so the update used a narrow XLSX XML package edit instead of forcing a broader workbook rewrite.

## Fields Changed

Changed only row `7` cells:

- `C7` Details: replaced the older short summary with then-current implementation text covering immediate host-survival release resolution, Event006 origin, the shared provisional tree, boards, report/management surfaces, then-current starter packages, formation routes, Event005 separation, and host survival.
- `D7` Evo I: updated committee/survival wording to match current recognition, militia, aid, volunteer, and host-response surfaces.
- `E7` Evo II: updated congress wording to include delegates, mutual guarantees, equipment sharing, volunteer cadres, arms pools, arbitration, compact preparation, and League buildup.
- `F7` Evo III: updated claims/patron wording to include Border Commission, Patron Ledger, and Patronage Recognition behavior.
- `G7` Evo IV: updated old-name/local-polity wording to list currently implemented starter proofs and Timetable Authority coverage.
- `H7` Evo V: updated strange-route wording to reflect Sealed Dossier, containment review, impossible recognition, anti-mankind doctrine, and strange cooperation while preserving follow-up status for deeper strange packages and final route art.
- `J7` World-End Scenario: kept the no-direct-world-end rule and added current major escalation presentation through bounded super-events.
- `O7` Liberations cluster details for Event ID `6`: updated to say Event006-origin releases use host-survival waves and manage dossiers, congresses, patrons, borders, formations, packages, report events, super-events, and achievements without Event005 state.

Unchanged Event006 cells:

- `A7` ID remains `6`.
- `B7` Event Name remains `Independence Wave`.
- `I7` Evo VI remains blank.
- `K7` Type remains `Minor Repeatable`.
- `L7` Status remains `In progress`.
- `N7` Cluster Name remains `Liberations`.
- `P7` Events (ID) remains `6`.
- `Q7` Chaos level remains `1`.
- `R7` Status remains `In progress`.

## Validation Performed

- Confirmed the workbook zip package integrity with `unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx`; all entries passed.
- Parsed `xl/worksheets/sheet1.xml` after the edit and read back row `7` cells `A7:L7` and `N7:R7`; updated values were present and the unchanged ID/type/status cells remained intact.
- Confirmed no formula cells or Excel error literals were present in the inspected worksheet XML before the edit.
- Opened the edited workbook through LibreOffice headless by converting it to a validation copy under `/tmp/chaosx_catalog_validate/`; LibreOffice completed successfully.
- Confirmed only the intended workbook row cells were edited by the script; the handoff is the only non-workbook file intentionally added by this pass.

## Remaining Catalog and Spreadsheet Risks

- Event006 remains incomplete. The workbook status correctly remains `In progress`.
- The workbook does not have dedicated columns for super-event slot IDs, report event IDs, focus count, achievement count, asset completion, package-specific portraits/seals, or animation status, so those facts are summarized in prose rather than represented structurally.
- The older catalog spec still says `16 proposed achievements`, while current implementation docs and handoffs report 19 Event006 achievement definitions. There is no achievement-count column to update in this workbook row.
- Package-specific portraits, seals, animated route assets, and deeper package families remain follow-up work; the updated Evo V and Details wording avoids presenting those as complete.
- The broader worktree was already dirty before this pass, including pre-existing workbook changes, so this handoff reports the cells changed rather than claiming a clean repository-wide diff.
