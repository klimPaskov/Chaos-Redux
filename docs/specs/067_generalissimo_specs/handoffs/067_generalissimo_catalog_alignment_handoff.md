# Event 067 Catalog Alignment Handoff

## Source-of-truth rule

The editable source is:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

The three CSV files are export-only. They must be regenerated with:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the CSV exports directly.

## Supplied export findings

### Event row

The supplied Events export contains:

- ID `67`
- name Generalissimo
- type Minor Fire-Once
- Chaos level 1
- status To Be Reworked
- blank Cluster ID
- blank Member Severity
- a one-sentence legacy detail
- no evolution or world-end detail

### Cluster export

The supplied Clusters export does not contain a Military Preparation row.

### Scenario export

The supplied Scenarios export contains IDs through `SCN-014`. It omits `SCN-004`, although the supplied mechanics guide still documents Final Silence under that ID. The workbook and runtime registry therefore need direct inspection before the new scenario is registered.

## Accepted Event 067 catalog facts

- Event ID: `067`
- Event name: Generalissimo
- Type: Minor Fire-Once
- Minimum Chaos level: 1
- Cluster: Military Preparation
- Member severity: High
- Manual scenario: Generalissimo's Coup
- Proposed scenario ID: `SCN-015`
- Public world-end branch: The Generalissimos' World

## Events sheet update

The Events row must receive finished player-facing wording derived from the final localisation.

Required fields:

- ID
- Event Name
- Details
- Evolution I
- Evolution II
- Evolution III
- World-End Scenario
- Type
- Chaos level
- Cluster ID
- Member Severity
- Status

The detail field should explain the premise of an unmatched commander whose military success can become political control. It should not list raw statistics, hidden values, removal chances, or implementation history.

Evolution fields should describe:

- formal control of the armed forces
- state-wide officer and institution network
- final demand for government power

The world-end field should describe an international struggle among military governments, civilian states, resistance movements, and rival juntas.

## Clusters sheet update

Inspect the workbook and runtime registry for an existing Military Preparation identity.

If it exists:

- use its exact Cluster ID
- add Event 067 as a High member
- preserve every existing member and detail

If it does not exist:

- treat cluster creation as a separate accepted catalog and runtime task
- assign no guessed ID from this handoff
- record Event 067's accepted membership in the implementation report
- do not silently place Event 067 in another cluster

## Scenarios sheet update

Register:

- Scenario ID `SCN-015`, after confirming it is free
- Scenario Name Generalissimo's Coup
- four type options
- Low, Medium, High, and Maximum intensity descriptions
- implementation status based on actual evidence

Type fields should cover:

- Favored Commander
- State Within the State
- The Ultimatum
- Generalissimo's War

These are working type labels. Final player-facing wording should follow the scenario localisation review.

## Runtime alignment

Workbook values must agree with:

- event registration
- Event Details
- Event Logs
- evolution previews
- world-end public row
- cluster registry
- triggerable scenario registry
- scenario scripted localisation
- scenario UI detail text

## Completion evidence

The spreadsheet worker should report:

- workbook path
- changed row and sheet names
- exact Cluster ID used
- `SCN-015` collision check
- exported CSV paths
- exporter result
- wording source keys
- any unresolved mismatch
