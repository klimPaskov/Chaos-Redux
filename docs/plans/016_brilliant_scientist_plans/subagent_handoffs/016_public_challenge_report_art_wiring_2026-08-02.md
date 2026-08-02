# Event 016 public-challenge report-art wiring handoff

Date: 2026-08-02

Status: implemented and parent-reviewed as a presentation-only continuation.

## Scope

The public-challenge host event and actor report were still using the opening appointment picture. The host confrontation now uses the existing sovereignty-confrontation card, and the actor's after-action report uses the existing Directorate dossier card.

## Changed files

- `events/016_brilliant_scientist_foreign_events.txt`
  - `chaosx.nr16.190` uses `GFX_report_event_016_brilliant_scientist_sovereignty_confrontation`.
  - `chaosx.nr16.191` uses `GFX_report_event_016_brilliant_scientist_directorate_dossier`.
- `docs/events/016_brilliant_scientist/systems/foreign_operations.md`
  - Records the visual contract alongside the existing six-answer public challenge and one-use ledger.

## Validation evidence

- Both sprite names are registered in `interface/016_brilliant_scientist.gfx` and resolve to existing DDS files under `gfx/event_pictures/016_brilliant_scientist/`.
- No event IDs, options, effects, triggers, AI weights, receipts, rewards, log entries, or model references changed.
- The public-challenge response and actor-report transaction remain unchanged; this is only a report-card selection fix.

## Remaining risks

Live visual presentation and the full public-challenge scenario remain user-owned acceptance work. No Event 016-specific 3D asset was created or substituted.
