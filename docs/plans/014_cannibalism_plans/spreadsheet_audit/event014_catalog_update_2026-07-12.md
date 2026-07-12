# Event 014 Catalog Update — 2026-07-12

## Workbook changes

- Replaced the disabled placeholder at `Events!A15:M15` with Event 014 Cannibalism.
- Recorded `Minor Fire-Once` in `Events!J15` and left `Events!K15:L15` blank, keeping Event 014 outside every cluster.
- Copied the live pre-reveal Event Details wording into `Events!C15`.
- Copied the three live evolution titles and descriptions into `Events!D15:F15`; Evolution III is the first entry that names Hannibal Lecter.
- Copied both live terminal titles and descriptions into `Events!I15`.
- Added SCN-010 The Hunger Lines at `Scenarios!A10:F10` with all five live type names/descriptions and all four live intensity descriptions.
- Extended the `Manual_Scenarios` table to `A1:F10`, its status validation to `F2:F10`, and its status conditional formatting through `F10`.
- Kept both Event 014 and SCN-010 at `Needs Testing` while the mandatory implementation audits remain open.

## Mechanical verification

- The workbook contains no formulas and no Excel error values.
- Event 014 retains an empty cluster ID and member-severity field.
- The scenario table, validation, and conditional-format ranges include SCN-010.
- The update script is reproducible and idempotent: `docs/plans/014_cannibalism_plans/tooling/update_event014_catalog.py`.

## Render review

LibreOffice rendered an isolated review copy of the updated source workbook. The rendered cells retain the established table colors, borders, wrapping, and alignment. The Event 014 row uses the workbook's maximum practical row height, with a nine-point terminal-description cell so neither terminal body is clipped.

- `event014_catalog_details_and_evolution_i.png`
- `event014_catalog_evolutions_world_ends_and_type.png`
- `scn010_catalog_profiles.png`
- `scn010_catalog_intensity_and_status.png`

These renders are audit evidence only. The authoritative artifact remains `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Open state

The spreadsheet content is aligned, but the final spreadsheet audit and status promotion remain pending until the implementation, asset, localisation, AI, scenario, and completion audits close.
