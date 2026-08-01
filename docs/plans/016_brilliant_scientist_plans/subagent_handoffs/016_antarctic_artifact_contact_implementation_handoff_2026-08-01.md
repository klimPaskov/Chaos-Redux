# Event 016 Antarctic artifact contact implementation handoff

## Scope

This tranche implements the accepted Event 025 to Event 016 alien-arms warning link without adding a new project reward, origin conclusion, event-log row, evolution, super-event, asset package, or 3D model.

## Runtime contract

- `chaosx.nr25.3` keeps its existing `antarctica_success`, rocket technology, and recovery cleanup effects.
- The shared `brilliant_scientist_try_schedule_alien_artifact_contact` helper also catches the valid ordering where `antarctica_success` exists before the Event 016 appointment; the appointment then queues the same one-time report.
- When the success reaches an active Event 016 host and the Event 016 world has not resolved, the host writes `brilliant_scientist_alien_artifact_contact` and queues `brilliant_scientist_alien_artifact_contact_pending`.
- `chaosx.nr16.17` presents one ordinary report with recovered and archived descriptions. Its option clears the pending flag and writes `brilliant_scientist_alien_artifact_contact_report_seen`.
- The report is a warning/recognition receipt only. `antarctica_success` remains the actual alien-arms Theory gate. No stage, reward, unit, claim, origin conclusion, evolution, event-log row, or super-event is created.

## Persistence and cleanup

- Transfer captures the pending obligation before former-host cleanup, copies contact and seen receipts to the recipient, and reschedules `.17` exactly once.
- Sovereignty formation copies contact, seen, and pending flags in the exact-host and portfolio snapshots, then reschedules a pending `.17` on the carrier.
- Former-host cleanup clears only the pending obligation; durable contact and seen receipts remain in the history snapshot.
- The `.17` trigger requires current-host status, the contact receipt, the pending receipt, and no resolved report receipt, so repeated Event 025 success cannot duplicate the report.

## Validation scenarios

1. Event 025 success for a non-host: no Event 016 flag or report.
2. Event 025 success for an active host: one queued `.17`, then one report and one seen receipt.
3. Repeated `.25.3` or an already-seen report: no second queue or report.
4. Transfer while `.17` is pending: recipient receives exactly one scheduled report.
5. KRG formation while `.17` is pending: carrier retains the pending report and displays it once.
6. World-end or resolved Event 016: the Event 025 success still resolves normally, but no Event 016 report is queued.
7. Antarctic success before appointment: the later appointment picks up the permanent idea and queues exactly one `.17` report.

## Asset boundary

The report reuses `GFX_report_event_antarctica_secured`, already owned by Event 025. No new portrait, report image, animated frame, or 3D package is required.
