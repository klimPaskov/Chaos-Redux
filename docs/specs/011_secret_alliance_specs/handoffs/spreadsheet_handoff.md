# Event 011 event-catalog spreadsheet handoff

## Current status

The planning-era instruction to defer workbook work is superseded. The live catalog workbook is frozen at commit `97a2da80` and reconciled to final Event 011 and SCN-009 wording. High-impact balance commit `1c87d923` changes numeric decision tuning and matching Event 011 localisation, not the workbook's narrative mirrors or status cells; engine-compatibility commit `407b9a05` leaves those workbook surfaces unchanged.

- Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- SHA-256: `597E71A1307958135BA1B34A8E60741320CD9E2753FA2EBDDBC1ED83403E1D59`
- `Events!M12`: `Implemented`
- `Scenarios!F9`: `Implemented`
- Formula error cells: none
- Formula error tokens: none

This documentation pass does not edit the workbook.

## Event row disposition

| Field | Current disposition |
| --- | --- |
| Event ID | `11` |
| Event name | `Secret Alliance` |
| Type | Minor Fire-Once |
| Status | `Implemented` |
| Cluster | Blank; Event 011 is not clustered |
| Details | Mirrors the implemented Event Log description rather than variables or hidden mechanics |
| Evolutions I-III | Names and detail wording match the in-game localisation |
| Super-event | Records the first public reveal and faction-formation role |
| Scenario | Records SCN-009 `Coalition Unmasked` and its immediate public-coalition role |

## Wording contract

The Event Details mirror describes foreign incidents, corroborated coordinated interference, and the public coalition from the target's world-state perspective. It does not expose hidden member count, exact Cohesion, exact Readiness, internal variables, code paths, or implementation history.

Evolution wording follows the implemented localisation:

- Evolution I widens concealed coordination and minor recruitment.
- Evolution II permits a strategically valid major sponsor, severe operations, and the target's investigation and preparedness system.
- Evolution III closes the coalition toward public formation and open war, with controlled, forced, weakened, and fractured state outcomes.

The scenario record reflects five compositions, Regional Ring, Ideological Front, Great-Power Sponsor, Unlikely Coalition, and Random Coalition, across Low, Medium, High, and Maximum intensity. Scenario members are AI-only and the launching human remains the target.

## Alignment evidence

- Automatic Event Log wording is selected by durable target-owned coordinated-interference and public-reveal history flags. Scenario and forced origins do not manufacture automatic-run history.
- Super-event slot `73` uses the exact five route packages through durable presentation snapshots and `GetSecretAlliancePresentationFactionName`.
- The workbook status matches implemented gameplay, final localisation, six achievements, the 57-DDS asset package, the eight-frame confrontation emblem plus still fallback, and licensed audio ID `43`.

## Remaining items

No workbook content or formula blocker remains. The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this spreadsheet handoff does not replace it. No in-engine playtest is claimed.
