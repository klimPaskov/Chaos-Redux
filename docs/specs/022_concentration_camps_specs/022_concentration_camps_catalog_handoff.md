# Event 22 Concentration Camps Catalog Handoff

## Current catalog state

The supplied `chaos_redux_events_catalog` CSV export still contains:

- ID `22`
- event name `Spain Antisemitism`
- type `Minor Fire-Once`
- no cluster
- status `Unavailable`

The supplied cluster CSV export does not contain a `Random Chaos` cluster row.

The CSV files are export snapshots. They are not the editable source of truth.

## Authoritative update route

The implementation or spreadsheet worker must update:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

After saving the workbook, run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the three catalog CSV files directly.

Use `chaosx_spreadsheet_doc_worker` with the spreadsheet skill when the workbook update is the only task. The worker should read only the workbook, relevant Event 22 player-facing localisation, this handoff, and named source files.

## Event row update

Locate Event ID `22` by ID, not by current row index.

| Field | Required value or direction |
| --- | --- |
| ID | `22` |
| Event Name | `Concentration Camps` |
| Type | `Minor Repeatable` |
| Cluster ID | numeric ID assigned to the accepted `Random Chaos` cluster |
| Member Severity | `Severe` |
| Status before implementation acceptance | `To Be Reworked` |
| Status after implementation and live acceptance | use the repository's current accepted status vocabulary |

## Details field direction

The player-facing details should communicate these points in compact form:

- one eligible country receives concentration camps in 20 percent of its eligible states
- each site causes real continuing population loss
- the affected country chooses closure, restrictive review, forced labour, security expansion, or evolved extermination policy
- forced labour can provide strong temporary local production, construction, extraction, or logistics gains
- deaths, resistance, disease, sabotage, evidence, transport burden, discovery, condemnation, and postwar liability grow with exploitation
- liberation creates survivor relief, displacement, evidence, and tribunal work

Do not describe the system as an efficient genocide bonus. Do not claim a universal ethnicity model.

## Evolution I field direction

Working title direction: `Extermination Network`

Required content:

- 50 percent of existing valid concentration camps convert to extermination camps when the evolution first reaches a network
- a pre-fire evolved opening begins with roughly half concentration and half extermination sites
- killing and terror replace ordinary labour assignment at extermination sites
- valid target purpose, intent, evidence, resistance, discovery, and restricted chemical-site rules enter play

## Evolution II field direction

Working title direction: `One Percent Lost`

Required content:

- every active camp state loses exactly 1 percent of current population once when the evolution reaches that network
- new sites created after the evolution receive the shock once for the same network generation
- the normal dynamic death process continues

Do not imply that the value is a manpower-only penalty.

## Evolution III field direction

Working title direction: `Half the Country Behind Wire`

Required content:

- total camp coverage rises to 50 percent of eligible states
- the final network is split roughly evenly between concentration and extermination camps
- each camp state receives a one-time exact 2 percent population loss
- a country whose first opening begins at Evolution III receives only the 2 percent opening shock, not an additional 1 percent shock

## Cluster registration

### Required action

Audit the authoritative workbook and current cluster implementation for an existing `Random Chaos` identity.

If it exists:

- use its existing numeric ID
- preserve its current description and member rules unless Event 22 requires a bounded update

If it does not exist:

- allocate one collision-free numeric cluster ID
- add a `Random Chaos` row to the workbook
- register the same ID in the event-cluster implementation
- record Event 22 as a Severe member
- regenerate the CSV exports

Do not invent a numeric ID in this planning package.

### Cluster description direction

`Random Chaos` should cover grounded or high-impact disruptions that do not fit a narrower event family. Its description should explain that members can create unrelated domestic crises in several parts of the world during one cluster firing.

The cluster must follow normal cluster pacing. Member events keep their own fired state, repeatable weight behavior, history, and detail entries while the cluster counts as one global pacing event.

### Cluster combination rules

Event 22 should not be clustered in the same country with another member that immediately removes, annexes, empties, or transforms all of that country's eligible states before Event 22 finishes its delayed setup.

If several cluster members target the same country or state:

- validate Event 22 after earlier member effects
- skip invalid states and do not substitute hidden targets outside the accepted pool
- record the skip reason in the cluster log
- preserve the cluster's one-pacing-event rule

## Event log fields

### First firing history

Record:

- country
- date
- evolution stage at opening
- eligible-state count
- target coverage
- created or activated site count
- concentration and extermination split
- opening policy
- network generation
- cluster source if applicable

### Repeat incident history

Log only material incidents:

- coverage expansion
- policy change
- country-package handoff
- public discovery
- major epidemic or famine crisis
- resistance uprising
- responsibility transfer
- liberation of a major network
- transparent closure

Do not add a history row for every normal operation pulse.

### Evolution history

Each evolution row should include:

- evolution stage
- affected country
- active or pre-fire entry
- converted or added site count
- exact applied population loss where relevant
- network generation
- skipped states and reasons

### Public discovery history

Record:

- responsible actor
- discovering or liberating actor
- first verified state
- evidence confidence
- source families
- network verification state
- Condemnation source identifier

### Closure and aftermath history

Record:

- closure type
- sites closed
- survivors stabilized
- evidence status
- underground sites remaining
- relief and tribunal handoff
- refire-protection expiry

## Event-details surface

The Event 22 details view should show:

- current event description
- baseline mechanics
- three evolution summaries
- active or completed status
- current affected countries or a concise count, subject to the shared detail framework
- current Network Reach, Exposure, and Resistance Pressure for the selected affected country where supported
- discovery and closure state
- links to the Deaths and Condemnation details where the shared UI supports them

The shared event-details framework remains out of Event 22 scripted-GUI scope.

## Localisation and workbook alignment

Before workbook export, compare the row against:

- Event 22 opening localisation
- event-detail localisation
- evolution-detail localisation
- Random Chaos cluster localisation
- event log history wording

The workbook should remain player-facing. Do not copy debug identifiers, hidden evidence formulas, AI profile names, or implementation notes into it.

## Spreadsheet validation

The spreadsheet worker must verify:

- Event ID remains numeric and unique
- event name is replaced, not duplicated
- Type is exactly the current workbook vocabulary for repeatable minor events
- cluster ID resolves to a real cluster row
- Member Severity uses current allowed validation values
- Evolution I through III are populated
- filters, formatting, formulas, validation, and sheet structure are preserved
- exported CSV row matches the workbook
- cluster export contains the accepted Random Chaos row

## Handoff status

This file defines the update. The workbook itself was not supplied in the planning environment, so no spreadsheet edit or CSV regeneration is claimed.
