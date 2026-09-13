# Event 063 catalog and documentation handoff

## Authoritative spreadsheet rule

The editable source is the repository workbook:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

The three CSV files are export snapshots. Do not edit them directly. After updating the workbook, run:

`python .tools/export_event_catalog_csv.py`

Then compare the exported event, scenario, and cluster CSV files with the workbook.

## Event row update

Current supplied row:

- ID: 63
- Event Name: End Subject Status
- Details: A random puppet breaks free and becomes independent.
- Type: Minor Repeatable
- Chaos level: 1
- Status: To Be Reworked

Required planned row identity:

| Field | Value or direction |
| --- | --- |
| ID | `63` |
| Event Name | `Subjects Break Free` |
| Type | `Minor Repeatable` |
| Chaos level | `1` |
| Cluster ID | `2` |
| Member Severity | `Medium` |
| Status before implementation | `To Be Reworked` |
| Status after complete implementation and validation setup | `Needs Testing` |

### Details direction

The Details cell should explain the player-facing premise:

- several existing subjects can become independent in one firing
- release count scales with the valid subject pool
- the countries retain their current territory, government, military, and other campaign state
- former overlords can recognize, negotiate, contest, or fight the separation
- countries liberated through Event 063 can cooperate with Independence Wave countries and compatible Soviet successors
- at high Chaos, a Liberation Pact can form

The cell should not include exact weights, file names, code terms, hidden candidate scores, or implementation notes.

### Evolution columns

Evolution I direction:

- more subjects can leave in one firing
- one same-overlord cohort can coordinate its declarations and immediate support

Evolution II direction:

- refused cohorts can enter a combined independence war
- other liberated states can provide aid or intervene

Evolution III direction:

- compatible liberated states can call a congress and form a defensive Liberation Pact
- the Pact supports later breakaways and protects member independence

Evolution descriptions should remain concise and player-facing. The full mechanics stay in the spec folder.

## Liberations cluster update

Current cluster:

- Cluster ID: 2
- Cluster Name: Liberations
- Members: 5, 6
- Status: Partially Available

Required member update:

- add Event 63 as an ordered Medium member
- keep Events 5 and 6 in their current roles
- preserve one cluster pacing event and separate member history

Suggested catalog member list order:

`5, 6, 63`

The cluster Details direction should mention three distinct surfaces:

- republic collapse
- creation of new independence states
- release of existing subject countries

The cluster text should not imply that one member owns every release system.

## Domestic Unrest secondary classification

The supplied cluster export has no Domestic Unrest row or stable ID.

The event's requested secondary classification is:

- Additional cluster: Domestic Unrest
- Additional cluster role: Medium member

Required handling:

1. inspect the current workbook and runtime registry for a newly added Domestic Unrest row
2. use its verified ID if one exists
3. otherwise leave the secondary integration pending and record the missing registry row
4. do not invent or reuse another cluster ID
5. keep Event 063 primarily mapped to Liberations until a supported multi-cluster initiation rule exists
6. when Domestic Unrest is created, allow Event 063 to appear as an optional Medium member in that cluster's ordered member list

## Event ownership notes for documentation

Permanent event documentation should state:

- Event 063 changes existing subject status in place
- Independence Wave owns its own country creation and release ledger
- Soviet Collapse owns its successor and League systems
- neutral liberation-origin data supports recognition, aid, and Pact eligibility
- the Liberation Pact does not force countries out of unrelated factions
- Event 144 Freedom or Death remains the separate mass National Liberation Front concept

## Event Details and scripted-localisation alignment

Event Details needs:

- updated event name
- updated premise text
- Chaos level 1 display
- Minor Repeatable type
- Liberations cluster name and Medium member role
- evolution descriptions for all three stages
- current weight or `N/A`
- fired count and history state through the existing shared system

History details should be dynamic and include:

- released countries
- former overlords
- settlement outcomes
- coordinated cohort status
- independence-war status
- Pact formation when applicable

Catalog preview text must not display fake history data.

## Documentation files expected after implementation

Use the repository's current event documentation convention. At minimum, permanent docs should cover:

- release transaction and candidate validity
- settlement modes
- shared origin contract and owner boundaries
- Liberation Pact and Liberation Cohesion
- decisions and missions
- AI and probability audit results
- Chaos impact map
- cluster integration
- asset manifest and coverage crosswalk
- achievements
- playtest and acceptance evidence

## Export validation

After workbook changes:

- event row 63 exports with the new name and fields
- cluster row 2 exports with member 63
- no scenario row changes without a separate accepted scenario design
- dropdown and conditional-formatting rules remain aligned with the workbook Legend
- generated CSVs parse with the same logical row counts expected by the repository
- no multiline field is broken by manual CSV editing
