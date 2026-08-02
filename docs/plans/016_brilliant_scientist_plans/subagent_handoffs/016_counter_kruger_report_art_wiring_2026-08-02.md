# Event 016 counter-Kruger report-art wiring handoff

Date: 2026-08-02

Status: implemented and parent-reviewed as a presentation-only continuation.

## Scope

The one-use counter-Kruger operation already had dedicated host and actor reports, but both events reused the opening appointment picture. The host response now uses the existing machine-security incident card, and the actor's after-action report now uses the existing Directorate dossier card.

## Changed files

- `events/016_brilliant_scientist_foreign_events.txt`
  - `chaosx.nr16.193` uses `GFX_report_event_016_brilliant_scientist_incident_machine_security`.
  - `chaosx.nr16.194` uses `GFX_report_event_016_brilliant_scientist_directorate_dossier`.
- `docs/events/016_brilliant_scientist/systems/foreign_operations.md`
  - Records the dedicated visual contract alongside the existing counter-program gates and no-reward guarantee.

## Validation evidence

- Both sprite names are registered in `interface/016_brilliant_scientist.gfx` and resolve to existing DDS files under `gfx/event_pictures/016_brilliant_scientist/`.
- No event IDs, options, effects, triggers, AI weights, receipts, rewards, log entries, or model references changed.
- The event file remains a presentation-only edit; the counter-program's one-use and project-family safeguards remain unchanged.
- The focused Event Inspector trace for `.193` rendered partially and listed four existing foreign scripted effects as absent from its active helper catalog. A source-side search confirms `brilliant_scientist_foreign_host_secure_response`, `brilliant_scientist_foreign_host_diplomatic_response`, and `brilliant_scientist_foreign_continue_to_actor_report` are defined in `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`; this is recorded as an inspector catalog limitation, not a new unresolved source reference.

## Remaining risks

Live visual presentation and the full counter-program scenario remain user-owned acceptance work. No Event 016-specific 3D asset was created or substituted.
