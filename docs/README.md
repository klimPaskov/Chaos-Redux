# Chaos Redux documentation

This directory separates current implementation documentation, accepted design specifications, working plans, provenance records, and generated catalog exports.

## Documentation map

| Area | Purpose |
| --- | --- |
| [`events/`](events/README.md) | Canonical event overviews and event-owned supporting system documents, grouped by event. |
| [`specs/`](specs/README.md) | Accepted design sources and implementation acceptance criteria. |
| [`plans/`](plans/README.md) | Working plans, audits, handoffs, resume packets, and historical implementation evidence. |
| [`systems/`](systems/README.md) | Shared or cross-event mechanics that do not belong to one event package. |
| [`achievements/`](achievements/README.md) | Event achievement contracts, grouped by event. |
| [`super_events/`](super_events/README.md) | Super-event research, text, audio, and provenance records, grouped by event where applicable. |
| `biological_warfare/` | Biological warfare subsystem documentation. |
| `chemical_warfare/` | Chemical warfare subsystem documentation. |
| `assets/` | Active asset-production evidence, manifests, previews, and handoffs. |
| `spreadsheets/` | The event catalog workbook and its generated export snapshots. |

## Source-of-truth rules

- Event implementation summaries belong in `events/<event_id>_<slug>/overview.md`.
- Event-owned supporting mechanics belong inside the same event folder, usually under `systems/`.
- Accepted event design belongs in `specs/<event_id>_<slug>_specs/`.
- Working plans, audits, and subagent handoffs belong in `plans/<event_id>_<slug>_plans/`.
- Shared systems remain in `systems/`.
- Historical evidence is preserved and identified through package indexes or superseded notices rather than deleted.
- New dated documents use `YYYY-MM-DD_<scope>_<type>.md`.
- Markdown sentences are not hard-wrapped.

