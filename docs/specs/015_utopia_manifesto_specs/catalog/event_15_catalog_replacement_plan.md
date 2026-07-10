# Event 15 Catalog Replacement Plan

## Current CSV source row

| Field | Current value |
| --- | --- |
| ID | 15 |
| Event Name | World Tension Subsides |
| Details | Reserved |
| Type | Minor Repeatable |
| Cluster | empty |
| Status | To Be Reworked |

## Replacement classification

| Field | Planned value |
| --- | --- |
| ID | 15 |
| Event Name | final Event 15 name from in-game localisation |
| Details | exact final Event Details wording from in-game scripted localisation or GUI localisation |
| Evo I | exact final wording for Glosses in the Margin evolution detail |
| Evo II | exact final wording for Necessary Shores evolution detail |
| Evo III | exact final wording for Cities of One Measure evolution detail |
| Evo IV | exact final wording for Nowhere Made Law evolution detail |
| Evo V | exact final wording for The Perfect Island evolution detail |
| World-End Scenario | empty |
| Type | Minor Fire-Once |
| Cluster ID | empty |
| Member Severity | empty |
| Status | implementation status after validation |

All evolution labels above are working labels, not final player-facing wording.

## Spreadsheet workflow

1. Implement and audit final in-game Event Details and evolution detail wording.
2. Run the localisation auditor and resolve key or wording mismatches.
3. Spawn `chaosx_spreadsheet_doc_worker` with the event ID, workbook path, and exact localisation keys.
4. Update the Event 15 workbook row without changing workbook structure, filters, formulas, validation, or formatting.
5. Confirm that the workbook Details field describes the situation and premise rather than effects.
6. Confirm that baseline campaign phases are not entered as evolutions.
7. Confirm that Type is Minor Fire-Once and no cluster fields remain.

## Player-facing Details direction

The final Details text should describe a weak country reviving an old utopian manifesto and rebuilding its institutions around common provision, occupations, settlements, and land justified by need. It can mention that different interpretations produce different commonwealths. It must not list modifiers, thresholds, hidden routes, achievements, or final formation requirements.
