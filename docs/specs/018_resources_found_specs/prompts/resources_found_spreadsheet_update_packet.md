# Event 018 Resources Found Spreadsheet Update Packet

Use `chaosx_spreadsheet_doc_worker` only after final in-game localisation exists. Do not update the workbook from planning direction.

Workbook:
`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Event id:
`18`

Known catalog baseline from provided CSV:

| Field | Current CSV value |
| --- | --- |
| Event Name | Resources found |
| Details | Random province gets 100 production of some resource. |
| Type | Minor Repeatable |

Blocked source fields:

| Spreadsheet field | Must mirror |
| --- | --- |
| Details | final Event Details window text |
| Evo I | final Evolution I detail text |
| Evo II | final Evolution II detail text |
| Evo III | final Evolution III detail text |
| Evo IV | final Evolution IV detail text |
| World-End Scenario | final world-end detail text if implemented |
| Cluster ID and Member Severity | final cluster integration if implemented |

Worker instructions:

- Read the spreadsheet skill.
- Open the workbook and preserve formatting, formulas, filters, data validation, and freeze panes.
- Read only the final localisation or scripted localisation needed for row 18.
- Do not paraphrase Event Details or evolution details when the workbook field is meant to mirror in-game wording.
- If any final in-game wording is missing, mark the cell blocked or needs user review instead of guessing.
- Report changed sheets, row, columns, fields, and any blocked cells.

Player-facing direction, not final spreadsheet copy:

- Details should describe a surprising resource discovery, exploitation, trade interest, and risk without listing mechanical effects.
- Evolution I should describe larger deposits, concessions, border pressure, and demilitarized field demands.
- Evolution II should describe unsafe deep extraction, worker sickness, corrosion, population loss, and cave incidents.
- Evolution III should describe public monster attacks, evacuation, hunts, and closure by sacrificing resources.
- Evolution IV should describe the Cave Host as a nonhuman country with slow armored divisions created from captured resources.
- World-end should describe the Host spreading beyond one continent only if the world-end branch is implemented.

## Canonical continuation addendum

Do not update the workbook from planning text. Wait for final in-game localisation and event details. The provided CSV catalog row still marks Event 18 as `To Be Reworked` and gives only the old short resource-discovery description.
