# Event 014 Catalog Final Re-audit - 2026-07-12

> Historical checkpoint. The catalog status vocabulary was subsequently standardized to `Fully Functional`. Current workbook/helper evidence belongs to `docs/plans/014_cannibalism_plans/audits/event014_integration_catalog_reaudit_2026-07-15.md`; the preserved `Implemented` wording below records the 2026-07-12 state only.

## Scope and authoritative sources

This re-audit checked `docs/spreadsheets/chaos_redux_events_catalog.xlsx` against the live Event 014 player-facing localisation and current event documentation. The workbook is the authoritative catalog artifact.

The wording sources were:

- `localisation/english/chaosx_event_names_l_english.yml` for the Event 014 name.
- `localisation/english/014_cannibalism_l_english.yml` for the pre-reveal Event Details text, all three evolution titles and descriptions, SCN-010 identity, five scenario type titles and descriptions, and four intensity descriptions.
- `localisation/english/chaosx_gui_l_english.yml` for the two distinct Event Details terminal titles and descriptions.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` for the live pre-reveal and revealed selector order, evolution selectors, and terminal detail selectors.
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` for the five live scenario type branches.
- `common/scripted_effects/chaosx_logic_effects.txt` for Event 014 registration in `global.fire_once_events`.
- `common/scripted_effects/chaosx_events_log_effects.txt` for the separate `world_is_the_larder` and `no_thaw_will_come` public terminal registry rows.
- `docs/events/014_cannibalism.md` for the public classification, cluster status, terminal row identities, and catalog status boundary.

## Workbook change

Two factual wording defects were corrected.

- `Events!D15` now uses the exact live `cannibalism.evolution.stage_1.title` and `cannibalism.evolution.stage_1.desc` text. The description ends with `No shared headquarters appears in the records.`
- `Events!E15` now uses the exact live `cannibalism.evolution.stage_2.title` and `cannibalism.evolution.stage_2.desc` text. The description ends with `Captured records identify no common headquarters.`

During the wording correction, no other workbook value, formula, table, validation, conditional-formatting rule, style, row height, column width, sheet, filter, or status was intentionally changed.

## Events row evidence

| Cell | Expected source or invariant | Result |
|---|---|---|
| `Events!A15` | Event ID `14` | Exact |
| `Events!B15` | `chaosx.event_name.14`, `Cannibalism` | Exact |
| `Events!C15` | `chaosx.events_log.window.event_details.cannibalism.pre_reveal` | Exact |
| `Events!D15` | Evolution I title plus description | Exact after correction |
| `Events!E15` | Evolution II title plus description | Exact after correction |
| `Events!F15` | Evolution III title plus description | Exact |
| `Events!G15` | Evolution IV absent | Blank as required |
| `Events!H15` | Evolution V absent | Blank as required |
| `Events!I15` | `The World Is the Larder` title and Event Details description, followed by `No Thaw Will Come` title and Event Details description | Exact and distinct |
| `Events!J15` | Event 014 is registered as fire-once and catalogued as `Minor Fire-Once` | Exact |
| `Events!K15` | Cluster ID | Blank as required |
| `Events!L15` | Cluster member severity | Blank as required |
| `Events!M15` | Completion status | `Implemented` |

`Events!C15` contains none of the reveal-only terms `Hannibal`, `Lecter`, `Wendigo`, `world end`, or `unification`. The player-facing Details field remains pre-reveal safe. Evolution III and the terminal field may name revealed content because those are separate catalog surfaces.

The two terminal entries in `Events!I15` mirror the Event Details localisation, not the separate super-event descriptions. The public registry keeps them separate through `world_end_scenario_id.world_is_the_larder` and `world_end_scenario_id.no_thaw_will_come`, with distinct scenario flags and super-event mappings.

## Scenario row evidence

| Cell | Expected source or invariant | Result |
|---|---|---|
| `Scenarios!A10` | `chaosx.scenarios.entry.id.cannibalism`, `SCN-010` | Exact |
| `Scenarios!B10` | `chaosx.scenarios.cannibalism.name`, `The Hunger Lines` | Exact |
| `Scenarios!C10` | Five title and description pairs in live selector order | Exact |
| `Scenarios!D10` | `Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, Convergence` | Exact |
| `Scenarios!E10` | Low, Medium, High, and Maximum impact descriptions | Exact |
| `Scenarios!F10` | Completion status | `Implemented` |

The five SCN-010 type profiles are Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence. All five titles and all five descriptions match localisation. The workbook also contains all four live intensity stops and their exact impact descriptions.

## Formula and error check

The workbook was loaded and inspected with the bundled Codex Python runtime and `openpyxl`.

- Formula cells found: `0`.
- Excel error values found: `0`.
- Checked error tokens included `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`, `#NUM!`, and `#NULL!`.
- Workbook calculation mode remains `auto`, with full calculation and forced full calculation on load still enabled.

No recalculation pass was required because the workbook contains no formulas.

## Tables, validation, and conditional formatting

- The `Events` table remains `Events!A1:M1015`.
- The `Manual_Scenarios` table remains `Scenarios!A1:F10`, including SCN-010.
- Event type validation remains `Events!J2:J1015`.
- Event cluster severity validation remains `Events!L2:L1015`.
- Event status validation remains `Events!M2:M1015`.
- Scenario status validation remains `Scenarios!F2:F10` and includes `Needs Testing` and `Implemented`.
- Scenario status conditional formatting remains split across `Scenarios!F2:F8` and `Scenarios!F9:F10`. Together these ranges cover every scenario status cell through SCN-010.
- Event conditional formatting remains on `J2:J1015`, `L2:L1015`, and `M2:M1015`.

## Formatting and layout check

- `Events!C15:I15` remain wrapped and top aligned.
- `Events!D15` retains style ID `50` and `Events!E15` retains style ID `51`.
- `Events!I15` retains style ID `81`, nine-point text, wrapping, and top alignment.
- Event row 15 remains at height `409.5`.
- `Scenarios!B10:F10` remain wrapped and top aligned.
- Scenario row 10 remains at height `400`.
- The scenario row retains style IDs `45, 44, 44, 44, 44, 11` across `A10:F10`.

No review render was needed. The correction changed only two evolution descriptions, both fit inside the existing wrapped cells, and every layout property remained unchanged.

## Helper closure and findings

The authoritative workbook is exact after the two wording corrections. No workbook fallback or simplification was used.

`docs/plans/014_cannibalism_plans/tooling/update_event014_catalog.py` is current with all 19 audited target cells. Its Evolution I, Evolution II, and combined terminal literals match the live localisation and workbook. Every other Event 014 and SCN-010 literal also matches the verified row values, including both `Implemented` statuses.

The helper was executed twice against a temporary copy of the authoritative workbook after status promotion. The first run reproduced all 19 audited cells and preserved the full workbook semantic and formatting fingerprint. The second run produced the same fingerprint, confirming the helper is idempotent. Both temporary runs retained the table, validation, and conditional-formatting ranges recorded above and contained zero formulas and zero Excel error values. The source workbook was never passed to the helper during this closure test, and its SHA-256 remained `d008a71c40204505c18cdeb95fca62b900e02cdeab56003d33357fcc216e5da5` before and after the test.

## Post-completion status promotion - 2026-07-13

The final Event 014 completion audit closed cleanly and explicitly authorized catalog promotion. Only `Events!M15` and `Scenarios!F10` were changed in the authoritative workbook during this promotion. Both cells now read `Implemented`.

The matching `EVENT_ROW` and `SCENARIO_ROW` status literals in the update helper also read `Implemented`. No promotion remains pending.

No gameplay, localisation, scripted localisation, specification, or event documentation file was edited. No workbook cell outside the two authorized status cells changed during promotion. No commit was created.
