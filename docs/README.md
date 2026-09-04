# Chaos Redux documentation

This directory separates implementation documentation, design specifications, working plans, provenance records, and generated catalog exports.
Start with the relevant package index and its recorded acceptance basis.
Document location, catalog status, timestamps, and old completion reports do not establish approval or current behavior.

## Documentation map

| Area | Purpose |
| --- | --- |
| [`events/`](events/README.md) | Canonical event overviews and event-owned supporting system documents, grouped by event. |
| [`specs/`](specs/README.md) | Design sources and acceptance criteria, with acceptance or unresolved proposal status established by each package's decision evidence. |
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

- Explicit user decisions establish task scope and acceptance. Record their basis separately from proposals and implementation findings.
- [`AGENTS.md`](../AGENTS.md) owns project rules. The relevant [repository skill](../.agents/skills/) owns its reusable workflow, and [canonical Codex role definitions](../.codex/agents/) own specialist instructions.
- Event implementation summaries belong in `events/<event_id>_<slug>/overview.md`.
- Event-owned supporting mechanics belong inside the same event folder, usually under `systems/`.
- Accepted event design belongs in `specs/<event_id>_<slug>_specs/`.
- Working plans, audits, and subagent handoffs belong in `plans/<event_id>_<slug>_plans/`.
- Shared systems remain in `systems/`.
- Historical evidence is preserved and identified through package indexes or superseded notices rather than deleted.
- New dated documents use `YYYY-MM-DD_<scope>_<type>.md`.
- Markdown sentences are not hard-wrapped.

Implementation summaries must identify the source revision or evidence they describe.
Source inspection, calculations, MCP previews, and user-provided live-game results remain distinct forms of evidence.
Keep unresolved decisions visible in the package's existing plan disposition or resume record.

The [documentation cleanup record](plans/repo_cleanup/documentation_state.md) identifies reviewed coverage, completed repairs, unresolved instruction conflicts, and the next bounded source reads for the active cleanup task.
