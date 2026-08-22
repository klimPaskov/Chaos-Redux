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
| [`formables/`](formables/README.md) | Formable-state contracts, consumer specifications, and generated state-puzzle evidence. |
| [`systems/cbrn_warfare/`](systems/cbrn_warfare/) | Shared chemical, biological, condemnation, and related CBRN system documentation. |
| [`assets/`](assets/) | Active asset-production evidence, manifests, previews, and handoffs. Asset workspaces retain their own provenance and do not require a central README. |
| [`spreadsheets/`](spreadsheets/README.md) | The event catalog source workbook, generated catalog exports, and the separate doctrine workbook. |
| [`testing/`](testing/README.md) | Test-country guidance and dated live-QA evidence. |

## Source-of-truth rules

- Event implementation summaries belong in `events/<event_id>_<slug>/overview.md`.
- Event-owned supporting mechanics belong inside the same event folder, usually under `systems/`.
- Accepted event design belongs in `specs/<event_id>_<slug>_specs/`.
- Working plans, audits, and subagent handoffs belong in `plans/<event_id>_<slug>_plans/`.
- Shared systems remain in `systems/`.
- Historical evidence is preserved and identified through package indexes or superseded notices rather than deleted.
- New dated documents use `YYYY-MM-DD_<scope>_<type>.md`.
- Markdown sentences are not hard-wrapped.
