# Event 016 cross-domain review and containment exclusivity handoff

Date: 2026-08-02

## Scope

This bounded runtime correction closes the remaining transaction race between the paid cross-domain biological review and the timed containment board. No new project, route, reward, event-log row, asset, or model was introduced.

## Changed files

- `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt`
  - `brilliant_scientist_cross_domain_review_is_ready` now rejects an active `brilliant_scientist_containment_action_in_progress` flag.
  - `brilliant_scientist_cross_domain_review_resolution_is_valid` repeats the same guard for delayed resolution safety.
- `docs/events/016_brilliant_scientist/systems/projects.md`
  - Documents that review and containment resolvers are mutually exclusive.
- `docs/events/016_brilliant_scientist/overview.md`
  - Records the same gameplay contract in the Event 016 overview.

## Behavior

If a containment decision has already started, the cross-domain review remains unavailable until that timed action resolves or cancels. If the review starts first, the existing sovereignty transition gate already blocks every containment decision while the review is pending or in progress. The 120-day civilian-factory burden therefore cannot race a release, exile, arrest, shutdown, seizure, foreign-containment, charter, or institutional-concession resolution.

## Validation

- Confirmed the two guards use existing country flags and the supported trigger syntax.
- The fresh completion audit identified this as the only current cross-domain/containment race before the patch.
- A focused Event 016 event lint was run against the current workspace. The tool returned `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and a workspace-wide validation limitation due to the large mod graph.

## Remaining risks

User-owned live testing is still required for the overlap sequence, timed cancellation, and review completion. No 3D model or entity package was produced or wired.
