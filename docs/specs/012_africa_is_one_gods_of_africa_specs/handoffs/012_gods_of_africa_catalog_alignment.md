# Gods of Africa catalog alignment handoff

## Authoritative source rule

The editable source is:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

After a successful workbook update, run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the Events, Clusters, or Scenarios CSV exports directly.

## Event 070

The current supplied Events CSV still contains an old Event 070 Gods of Africa entry.

Required workbook disposition:

- remove the Gods of Africa name, details, evolution text, cluster assignment, world-end text, and other Event 070 fields that belong to the old idea
- preserve Event ID `070` as available for a future separate idea
- do not replace it with a new concept during this task
- align Event 070's status with the repository's normal reserved or empty-row policy
- remove stale player-facing Event Details mappings and event name mappings if live source still contains them

Gods of Africa must not retain Event 070 type, Chaos level, weight, cluster membership, or namespace.

## Event 012

Update Event 012 player-facing details after implementation facts are final.

Suggested detail additions:

- after Evolution I and a consolidation period, the African unifier can activate Gods of Africa
- every major and player-controlled country receives an independent Wrath relationship
- Africa issues dynamic capacity-based tribute demands
- tribute materially strengthens the African unifier
- Gods of Africa Strength caps punishment capability
- loyal countries can receive protection and final friendship
- permanent defiance ends ordinary demands but creates open hostility
- secured Africa ends the tribute cycle and resolves final relationships

The workbook should describe the premise and visible system. It should not expose exact formulas, hidden friendship values, event targets, script constants, or internal implementation labels.

## Event 012 evolution fields

### Evolution I

Add the delayed activation of Gods of Africa and baseline demand families.

### Evolution II

Add heavy equipment, aircraft, infrastructure, industrial support, continuing contracts, stronger protection, and expanded punishment access when Strength qualifies.

### Evolution III

Add faction and alignment demands, foreign-base removal, sanctions, intervention against occupiers, reconciliation, and extreme punishment access under the full gate.

Keep the wording aligned with in-game Event Details.

## Event 012 world-end field

World Is One remains Event 012's terminal campaign route.

Gods relationship history should be described as an input to invitations, conditions, privileges, and opposition. Do not add a separate Gods world-end row unless a later accepted design creates a genuinely distinct terminal branch.

## Scenario `SCN-011`

Update scenario details only if implementation changes the launch behavior.

Expected behavior:

- Africa Is One type establishes the unifier and starts the normal Gods consolidation delay
- World Is One type initializes relationship disposition needed by its setup and does not launch a redundant normal tribute cycle after continental security
- intensity may affect initial African capability, control, Strength, and hostile positions

The scenario keeps ID `SCN-011`.

## Cluster catalog

Gods of Africa is not a separate event member.

Event 012 retains its existing cluster relationship. The cluster catalog changes only if Event 012's own accepted cluster description needs broader wording after implementation.

## Current supplied catalog inconsistencies to verify

The supplied CSV is an export snapshot and may be stale.

Implementation review should verify:

- Event 012 Chaos level
- Event 012 status
- Event 012 cluster fields
- Event 012 evolution wording
- Event 012 World Is One wording
- Event 070 availability policy
- SCN-011 type and intensity wording

Do not resolve these fields from this planning package alone. The live source, in-game localisation, and authoritative XLSX must agree.

## Spreadsheet worker prompt inputs

Provide the spreadsheet worker:

- Event 012 row identity
- Event 070 row identity
- SCN-011 row identity
- final in-game Event Details text
- final evolution descriptions
- final scenario descriptions
- final Event 012 world-end text
- exact workbook path
- exporter command

The worker should preserve workbook formatting, formulas, filters, and validation.
