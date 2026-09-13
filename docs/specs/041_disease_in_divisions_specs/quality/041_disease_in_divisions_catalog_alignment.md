# Event 41 catalog alignment

## Current catalog defects

The current Event 41 export row is stale.

It currently describes a mysterious shipment falling from the sky and leaves the cluster, severity, and evolution fields empty. That wording belongs to another idea and cannot remain after implementation.

The current Diseases cluster export lists only Events 20 and 2. Its details describe severe state outbreaks and do not account for a low-severity military member.

## Authoritative update path

Update only:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

After saving the workbook, run:

`python .tools/export_event_catalog_csv.py`

Do not edit the three CSV exports directly.

## Event row direction

### ID

`41`

### Event name

Disease in Divisions

### Details direction

Describe a mysterious field epidemic striking frontline formations in one country at war. Explain that sick soldiers reduce military readiness and that the country must balance continued operations against rotation, sanitation, field hospitals, quarantine, and evacuation. Keep exact modifiers and hidden profile rules out of the catalog.

### Evolution I direction

Describe military transmission through camps, depots, shared logistics, allied access, expeditionary forces, and sustained enemy contact.

### Evolution II direction

Describe the War Plague crossing into civilian transport and hospital networks and moving between theaters through coalition logistics. State that civilian outbreaks use the existing shared outbreak systems.

### Type

Minor Repeatable

### Chaos level

1

### Cluster ID

8

### Member Severity

Low

### Status after complete implementation

Use the repository's accepted implemented or testing status based on final evidence. Do not mark the row complete from planning alone.

## Diseases cluster row direction

### Members

Add Event 41 to the member list while preserving Events 20 and 2.

### Details direction

Describe the Diseases cluster as a range of military and civilian outbreaks. Explain that some members establish persistent state disease while Disease in Divisions begins as a bounded wartime military epidemic. Mention that shared medical, containment, transport, and outbreak systems connect members without forcing every disease into the same civilian framework.

### Status

Retain the status supported by the implemented member set. Event 41 planning does not by itself change the cluster to fully available.

## Wording alignment

The workbook wording should match the implemented Event Details and evolution-detail wording. The catalog should describe premise and visible progression. It should not list exact numerical effects, private variables, implementation history, or hidden achievement conditions.
