# Event 24 Catalog Alignment

## Source snapshot

The uploaded export-only event CSV currently contains:

| Field | Current value |
| --- | --- |
| ID | 24 |
| Event Name | Video Game in Sweden |
| Details | A Swedish war game movement grants its divisions new tactical training and battlefield advantages. |
| Evo I | Empty |
| Evo II | Empty |
| Evo III | Empty |
| Type | Minor Fire-Once |
| Cluster ID | Empty |
| Member Severity | Empty |
| Status | Unavailable |

The CSV is an export snapshot and must not be edited directly.

## Proposed design fields

The authoritative workbook should be updated only after implementation creates final in-game Event Details and evolution wording. The spreadsheet worker must mirror that wording instead of copying working labels from this planning package.

### Details direction

Swedish developers produce an advanced strategy simulation that becomes a useful military training tool. Its wider adoption creates a risk that officers, officials, and civilians trust the model more than real terrain, supply, diplomacy, and human behavior.

### Evolution I direction

The officer corps turns the game into a professional competition and doctrine culture. Planning improves, while commanders begin optimizing for the rules and can misread real conditions.

### Evolution II direction

The game spreads through schools, clubs, workplaces, newspapers, and political organizations. Recruitment interest rises, while productivity and public attention suffer.

### Evolution III direction

Senior command and government begin applying simulation logic to real policy and warfare. Sweden must audit, contain, restrict, or temporarily exploit the system before a mandatory reassessment.

### Classification

- Type: Minor Fire-Once
- Chaos level: 1, Calm World
- Cluster ID: Empty
- Member Severity: Empty

The event should remain unclustered. The current unnumbered Scientific Research cluster does not describe this event's main institutional and cultural identity.

## Status flow

| Stage | Recommended status |
| --- | --- |
| Specification only | To Be Reworked or Unavailable, according to current workbook convention |
| Implemented but not live-tested | Needs Testing |
| Full live QA complete | Implemented |

Do not mark the event Implemented while assets, AI, decisions, evolution logs, achievements, documentation, or live checks remain incomplete.

## Workbook procedure after implementation

1. Read final in-game event name, Event Details, and evolution wording.
2. Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` only.
3. Preserve workbook formatting, formulas, filters, validation, and sheet structure.
4. Run `python .tools/export_event_catalog_csv.py` from the mod root.
5. Confirm the Events, Clusters, and Scenarios CSV snapshots were regenerated.
6. Keep Event 24 absent from cluster and scenario membership unless a later accepted specification changes that design.
