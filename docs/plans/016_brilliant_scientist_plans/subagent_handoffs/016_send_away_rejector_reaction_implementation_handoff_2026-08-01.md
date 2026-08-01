# Event 016 send-away rejector reaction implementation handoff

Date: 2026-08-01

## Implemented surface

The player-only opening referral now has a bounded reverse reaction. After the referred country successfully commits the same fixed Kruger appointment, the original rejecting country receives `chaosx.nr16.15` after the constant-defined three-day delay.

The recipient posture selects public, secret, or default wording through the preserved `brilliant_scientist_send_away_recipient` event target. The rejector's `brilliant_scientist_rejection_memory` is consumed exactly once, with `brilliant_scientist_rejection_reaction_pending` preventing duplicate scheduling and `brilliant_scientist_rejection_reaction_seen` preventing repeat presentation.

## Files and identifiers

- `common/script_constants/016_brilliant_scientist_constants.txt`: `brilliant_scientist_opening_duration.rejection_reaction_delay_days`.
- `common/scripted_effects/016_brilliant_scientist_effects.txt`: schedules `.15` only after `brilliant_scientist_opening_appointment_committed` is set by the successful recruitment transaction.
- `events/016_brilliant_scientist.txt`: `chaosx.nr16.15` triggered-only report.
- `localisation/english/016_brilliant_scientist_l_english.yml`: title, public/secret/default descriptions, option, and effect tooltip.
- `docs/events/016_brilliant_scientist/overview.md`: opening-chain documentation.

## Boundaries and validation

This report is not an Event Log row, evolution, project reward, foreign operation, new claim, super-event, news event, asset package, or 3D consumer. It reuses `GFX_report_event_016_brilliant_scientist_directorate_dossier`.

Parent validation should confirm the regular referral targets survive the delayed event chain, that the recipient appointment flag gates `.15`, and that a second helper invocation cannot schedule the report again. No live HOI4 session was run.
