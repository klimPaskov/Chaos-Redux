# Event 53 Catalog Alignment Handoff

## Current export state

The supplied `chaos_redux_events_catalog(4).csv` row contains the correct ID, name, type, Chaos level, and status. Its Details field is stale and describes a scientific breakthrough.

The supplied cluster and scenario exports contain no Event 53 entry.

## Authoritative update path

The implementation agent must not edit any catalog CSV directly.

After Event 53 implementation and final localisation are complete, `chaosx_spreadsheet_doc_worker` should update:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

It must then run:

`python .tools/export_event_catalog_csv.py`

## Required row values

| Column | Required value or source |
| --- | --- |
| ID | `53` |
| Event Name | `Mysterious Man` |
| Details | Mirror the final in-game Event Details premise wording |
| Evo I | Mirror the final in-game Evolution I detail wording |
| Evo II | Mirror the final in-game Evolution II detail wording |
| Evo III | Mirror the final in-game Evolution III detail wording |
| Evo IV | Blank |
| Evo V | Blank |
| World-End Scenario | Blank |
| Type | `Minor Fire-Once` |
| Chaos level | `1` |
| Cluster ID | Blank |
| Member Severity | Blank |
| Status | `Needs Testing` after complete source implementation, then advance only when project evidence supports it |

## Player-facing wording direction

### Details

Describe the public premise. An unexplained man repeatedly enters secure government locations, makes a demand, and disappears after the country pays or refuses. Refusal is known to bring serious consequences. Do not list the registry, demand formula, interval formula, identity theories, or source-event bookkeeping.

### Evolution I

Describe the visible expansion from Political Power demands to other political, military, industrial, logistical, and national resources. Explain that later demands become harder to meet. Do not list every internal demand type if final Event Details uses a shorter public summary.

### Evolution II

Describe larger demands and national-scale refusal consequences, including the possibility of coordinated crises. Do not expose package IDs or exact equal-pool composition.

### Evolution III

Describe absurd sacrifices and catastrophe-class consequences at World Collapse. Do not claim that Event 53 itself owns a world-end scenario.

## Synchronization requirement

The spreadsheet fields must mirror final in-game Event Details and evolution wording. This planning handoff gives direction only and is not pasteable localisation.
